<template>
  <v-container>
    <h1>리뷰 작성</h1>

    <v-text-field v-model="reviewTitle" label="제목" outlined />
    <v-textarea v-model="reviewContent" label="내용" outlined />
    <v-file-input
      v-model="reviewImage"
      label="이미지 업로드"
      accept="image/*"
    />

    <v-btn color="primary" @click="submitReview">제출하기</v-btn>
  </v-container>
</template>
///
<reference types="nuxt" />
<script setup lang="ts">
import { ref } from "vue";
import { useReviewStore } from "~/review/stores/reviewStore";
import { useRouter } from "vue-router";

// ✅ SEO 메타 정보
definePageMeta({
  title: "리뷰 작성 | JobStick",
  description: "JobStick 리뷰 작성 페이지입니다. 리뷰를 작성해보세요.",
  keywords: ["리뷰", "리뷰 작성", "리뷰 제출", "JobStick", "잡스틱", "job-stick"],
  ogTitle: "JobStick 리뷰 작성",
  ogDescription:
    "JobStick 리뷰 작성 페이지입니다. 서비스 이용 후 리뷰를 남겨보세요.",
  ogImage: "", // 실제 이미지 경로
  robots: "index, follow", // 검색 엔진 노출 허용
});

const router = useRouter();
const reviewStore = useReviewStore();
const reviewTitle = ref("");
const reviewContent = ref("");
const reviewImage = ref<File | null>(null);
const isSubmitting = ref(false);

const submitReview = async () => {
  if (isSubmitting.value) return;
  isSubmitting.value = true;
  try {
    if (!reviewTitle.value || !reviewContent.value) {
      alert("제목과 내용을 입력해 주세요");
      return;
    }
    const formData = new FormData();
    formData.append("title", reviewTitle.value);
    formData.append("content", reviewContent.value);
    if (reviewImage.value) {
      formData.append("image", reviewImage.value);
    }

    const userToken = localStorage.getItem("userToken")!;
    formData.append("userToken", userToken);
    await reviewStore.requestSubmitReviewToDjango(formData);
    router.push("/review/list");
  } catch (e) {
    console.error("제출 중 오류", e);
  } finally {
    isSubmitting.value = false;
  }
};
</script>
