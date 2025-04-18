<template>
  <v-container style="maxwidth: 50%; margin-top: 10vh">
    <v-form ref="form" v-model="valid">
      <v-card-title>
        <form v-if="showTitleDescription" @submit.prevent>
          <v-text-field
            class="headline"
            label="제목을 작성하세요."
            v-model="reviewTitle"
            @keyup.enter="disableEnter"
            :rules="[
              (v) => (v && v.trim() !== '') || '질문 제목은 필수 항목입니다.',
            ]"
            required
            lazy-rules
          ></v-text-field>
          <v-text-field
            class="headline"
            label="내용을 작성하세요."
            v-model="reviewDescription"
            @keyup.enter="disableEnter"
            :rules="[(v) => (v && v.trim() !== '') || '설명은 필수 항목입니다']"
            aria-required=""
          ></v-text-field>
          <v-btn
            :disabled="
              reviewTitle === null ||
              reviewTitle === '' ||
              reviewDescription === null ||
              reviewDescription === ''
            "
            @click="sendTitleAndDescription"
            >완료</v-btn
          >
        </form>
      </v-card-title>

      <v-btn v-if="titleAndDescriptionCreated" @click="addQuestion"
        >질문 추가</v-btn
      >
      <v-select
        v-if="isAdded"
        v-model="questionType"
        :items="generateOptions"
        label="질문 유형을 선택하세요"
      />

      <v-row>
        <v-col cols="12" v-if="questionType">
          <v-card v-if="questionType === 'text'" outlined>
            <v-card-text>
              <v-checkbox
                v-model="isEssential"
                label="이 질문을 필수 항목으로 설정합니다."
              />
              <v-text-field
                v-model="questionTitle"
                label="질문 제목을 입력하세요"
                :rules="[(v) => !!v || '질문 제목은 필수 항목입니다.']"
                required
              ></v-text-field>
              <v-row>
                <v-col cols="8">
                  <v-file-input
                    v-model="uploadedImage"
                    label="사진 등록"
                    multiple
                    @change="onFileChange(uploadedImage)"
                  />
                  <v-container v-if="uploadedImages.length !== 0">
                    <ul>
                      <li
                        class="li-margin"
                        v-for="(image, index) in uploadedImages"
                        :key="index"
                      >
                        {{ image.name }}
                      </li>
                    </ul>
                  </v-container>
                </v-col>
              </v-row>
              <v-btn
                :disabled="questionTitle === null || questionTitle === ''"
                @click="createQuestion(questionType)"
                >완료</v-btn
              >
            </v-card-text>
          </v-card>

          <v-card
            v-if="questionType === 'radio' || questionType === 'checkbox'"
            outlined
          >
            <v-card-text>
              <v-checkbox
                v-model="isEssential"
                label="이 질문을 필수 항목으로 설정합니다."
              />
              <v-text-field
                v-model="questionTitle"
                label="질문 제목을 입력하세요"
                :rules="[(v) => !!v || '질문 제목은 필수 항목입니다.']"
                required
              ></v-text-field>
              <v-row>
                <v-col cols="8">
                  <v-file-input
                    v-model="uploadedImage"
                    label="사진 등록"
                    multiple
                    @change="onFileChange(uploadedImage)"
                  />
                  <v-container v-if="uploadedImages.length !== 0">
                    <ul>
                      <li
                        class="li-margin"
                        v-for="(image, index) in uploadedImages"
                        :key="index"
                      >
                        {{ image.name }}
                      </li>
                    </ul>
                  </v-container>
                </v-col>
              </v-row>
              <v-btn
                v-if="readyToCreateQuestionTitle"
                :disabled="questionTitle === null || questionTitle === ''"
                @click="createQuestion(questionType)"
                >질문 생성</v-btn
              >
              <v-text-field
                v-if="!readyToCreateQuestionTitle"
                v-model="option"
                @keyup.enter="createSelection"
                label="항목 이름을 입력하세요"
                required
              />
              <v-btn
                v-if="!readyToCreateQuestionTitle"
                @click="createSelection"
              >
                항목 생성</v-btn
              >
              <br />
              <ul>
                <br />
                <li
                  class="li-margin"
                  v-for="(option, index) in selection"
                  :key="index"
                >
                  {{ option }}
                </li>
              </ul>
              <br />
              <v-btn
                v-if="selection.length !== 0"
                @click="finishCreateSelection"
                >완료</v-btn
              >
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <br /><br /><br /><br /><br />
      <hr class="tuning-hr" v-if="reviewQuestions.length !== 0" />
      <br />
      <v-row v-if="reviewQuestions.length !== 0">
        <v-card-title>
          <span>설문 폼 미리보기</span><br /><br /><br />
          <span class="headline">{{ reviewTitle }}</span>
          <v-card-subtitle class="review-subtitle">
            <br />
            <span>{{ reviewDescription }}</span>
          </v-card-subtitle>
        </v-card-title>
      </v-row>
      <v-row
        v-for="(question, index) in reviewQuestions"
        :key="index"
        class="mb-4"
      >
        <v-col cols="12">
          <v-card outlined>
            <v-card-text>
              <h4 v-html="formatQuestionTitle(index, question)"></h4>
              <br />
              <v-row v-if="question.images.length !== 0">
                <v-col
                  v-for="(image, index) in question.images"
                  :key="index"
                  cols="4"
                  class="mb-4"
                >
                  <span>추가된 이미지 {{ image.name }}</span>
                  <!-- <v-img :src="getImageUrl(image.name)" aspect-ratio="1.0" contain></v-img> -->
                </v-col>
              </v-row>
              <v-text-field
                v-if="question.questionType === 'text'"
                label="답변을 입력하세요"
              />
              <v-radio-group v-if="question.questionType === 'radio'">
                <v-radio
                  v-for="option in question.selection"
                  :key="option"
                  :label="option"
                  :value="option"
                />
              </v-radio-group>

              <v-row v-if="question.questionType === 'checkbox'">
                <v-col cols="12">
                  <v-checkbox
                    v-for="option in question.selection"
                    :key="option"
                    v-model="question.selectedOptions"
                    :label="option"
                    :value="option"
                  ></v-checkbox>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-btn
        v-if="reviewQuestions.length !== 0 && reviewTitle !== null"
        :disabled="!valid || reviewQuestions.length === 0 || reviewTitle === ''"
        @click="submitForm"
        color="primary"
        >제출</v-btn
      >
    </v-form>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";
import { useReviewStore } from "../../stores/reviewStore";

const reviewStore = useReviewStore();
const router = useRouter();

// Reactive state variables
const showTitleDescription = ref(true);
const titleAndDescriptionCreated = ref(false);
const readyToCreateQuestionTitle = ref(true);
const formCreated = ref(true);
const reviewId = ref(null);
const questionId = ref(null);
const selectionId = ref(null);
const reviewTitle = ref(null);
const reviewDescription = ref(null);
const reviewQuestions = ref([]);
const option = ref("");
const questionTitle = ref("");
const questionType = ref(null);
const selection = ref([]);
const isAdded = ref(false);
const isEssential = ref(false);
const generateOptions = ["text", "radio", "checkbox"];
const isFormDirty = ref(false);
const randomString = ref("");
const uploadedImages = ref([]);
const uploadedImage = ref(null);
const valid = ref(false);

// Methods
const createForm = async () => {
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  for (let i = 0; i < 32; i++) {
    randomString.value += characters.charAt(
      Math.floor(Math.random() * charactersLength)
    );
  }

  reviewId.value = await reviewStore.requestCreateReviewFormToDjango({
    randomString: randomString.value,
  });

  if (reviewId.value !== "") {
    formCreated.value = true;
    start.value = false;
  }
};

const sendTitleAndDescription = async () => {
  const payload = {
    reviewId: reviewId.value,
    reviewTitle: reviewTitle.value,
    reviewDescription: reviewDescription.value,
  };
  const titleDescriptionSaved =
    await reviewStore.requestRegisterTitleAndDescriptionToDjango(payload);

  if (titleDescriptionSaved) {
    titleAndDescriptionCreated.value = true;
    showTitleDescription.value = false;
  }
};

const createQuestion = async (type) => {
  if (!questionTitle.value) {
    alert("내용을 입력하세요");
    return;
  }

  const imageFormData = new FormData();
  imageFormData.append("reviewId", reviewId.value);
  imageFormData.append("questionTitle", questionTitle.value);
  imageFormData.append("questionType", questionType.value);
  imageFormData.append("isEssential", isEssential.value ? "true" : "false");

  uploadedImages.value.forEach((image) => {
    imageFormData.append("images", image);
  });

  questionId.value = await reviewStore.requestCreateQuestionToDjango(
    imageFormData
  );
  readyToCreateQuestionTitle.value = false;

  if (questionId.value !== null && type === "text") {
    const preForm = {
      questionTitle: questionTitle.value,
      questionType: type,
      isEssential: isEssential.value,
      images: uploadedImages.value,
    };
    reviewQuestions.value.push(preForm);
    resetQuestionFields();
  }
};

const createSelection = async () => {
  if (option.value.trim() !== "") {
    selection.value.push(option.value);
    const payload = { questionId: questionId.value, selection: option.value };
    selectionId.value = await reviewStore.requestRegisterSelectionToDjango(
      payload
    );
    option.value = "";
    isFormDirty.value = true;
  } else {
    alert("항목에 내용을 입력하세요");
  }
};

const finishCreateSelection = () => {
  if (selection.value.length === 0) {
    alert("항목을 입력해주세요.");
    return;
  }
  if (questionId.value !== null && selectionId.value !== null) {
    const preForm = {
      questionTitle: questionTitle.value,
      questionType: questionType.value,
      isEssential: isEssential.value,
      selection: selection.value,
      images: uploadedImages.value,
    };
    reviewQuestions.value.push(preForm);
    resetQuestionFields();
  }
};

const addQuestion = () => {
  isAdded.value = true;
  questionType.value = null;
  isFormDirty.value = true;
};

const onFileChange = (files) => {
  const newImages = Array.from(files);
  uploadedImages.value = [...uploadedImages.value, ...newImages];
  uploadedImage.value = null;
};

const resetQuestionFields = () => {
  questionTitle.value = "";
  selection.value = [];
  isAdded.value = false;
  questionType.value = null;
  isEssential.value = false;
  uploadedImages.value = [];
  isFormDirty.value = true;
  readyToCreateQuestionTitle.value = true;
};

const submitForm = () => {
  alert("제출 완료");
  router.push("/review/created");
};

const formatQuestionTitle = (index, question) => {
  if (question.questionType === "checkbox") {
    return `${index + 1}. ${
      question.questionTitle
    } (중복 선택 가능) <span class="essential"> ${
      question.isEssential ? "* 필수" : "* 선택"
    }</span>`;
  } else {
    return `${index + 1}. ${question.questionTitle} <span class="essential">${
      question.isEssential ? "* 필수" : "* 선택"
    }</span>`;
  }
};

const sleep = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};

const getImageUrl = async (imageName) => {
  try {
    await sleep(2500);
    return new URL(`@/assets/images/uploadImages/${imageName}`, import.meta.url)
      .href;
  } catch (e) {
    console.error("Image not found:", imageName);
    return "";
  }
};

const disableEnter = (event) => {
  event.preventDefault();
  event.stopPropagation();
};

const handleBeforeUnload = (event) => {
  if (isFormDirty.value) {
    const confirmationMessage = "작성 중인 정보가 저장되지 않을 수 있습니다.";
    event.returnValue = confirmationMessage;
    return confirmationMessage;
  }
};

// Lifecycle hooks
onMounted(() => {
  window.addEventListener("beforeunload", handleBeforeUnload);
});

onBeforeUnmount(() => {
  window.removeEventListener("beforeunload", handleBeforeUnload);
});
</script>

<style>
.headline {
  font-size: 30px;
  font-weight: bold;
}

.pre-title {
  margin-top: 5%;
  text-align: start;
}

.review-subtitle {
  max-width: 600px;
  overflow-wrap: break-word;
  word-break: break-all;
}

.essential {
  font-size: 0.8em;
  color: rgb(255, 123, 0);
}

.li-margin {
  margin-left: 4%;
}
.tuning-hr {
  border: none;
  border-top: 1px solid #d1d1d1;
}
</style>
