<template>
  <main>
    <v-container
      v-if="!start"
      align="center"
      height="100%"
      class="control-margin"
    >
      <!-- 기술 선택 부분: 필터가 열리고 닫히는 부분 -->
      <v-slide-y-transition>
        <v-row class="filter-tags-container">
          <v-col cols="12">
            <!-- 기술 -->
            <v-row class="align-center mb-4">
              <v-col cols="1" class="filter-group-title">
                <strong>기술</strong>
              </v-col>
              <v-col cols="11">
                <v-chip-group
                  v-if="!resetChips"
                  v-model="selectedKeyword"
                  column
                >
                  <!--<v-btn   // 초기화 버튼 일단 주석처리함
                    @click="clearSelectedKeywords"
                    class="reset-chip"
                    style="
                      background-color: white;
                      border-radius: 20px;
                      height: 33px;
                      margin-right: 10px;
                      margin-top: 3px;
                      box-shadow: none;
                      border: 1px solid lightgray;
                    "
                  > 
                    <v-icon left>mdi-refresh</v-icon>
                    초기화
                  </v-btn> -->
                  <v-chip
                    v-for="(keyword, index) in keywords"
                    :key="index"
                    :value="keyword"
                    :class="selectedKeyword === keyword ? 'selected-chip' : 'unselected-chip'"
                    class="keyword-chip"
                    clickable
                  >
                    {{ keyword }}
                  </v-chip>
                </v-chip-group>
              </v-col>
            </v-row>
            <!-- 경력 선택 부분: 기술과 같은 열에 배치 -->
            <v-row class="align-center mb-4">
              <v-col cols="1" class="filter-group-title">
                <strong>경력</strong>
              </v-col>
              <v-col cols="11">
                <v-chip-group
                  v-if="!resetCareer"
                  v-model="selectedCareer"
                  class="career-select-group"
                  column 
                >
                  <!--<v-btn  
                    @click="clearSelectedCareer"
                    class="reset-career"
                    style="
                      background-color: white;
                      border-radius: 20px;
                      height: 33px;
                      margin-right: 10px;
                      margin-top: 3px;
                      box-shadow: none;
                      border: 1px solid lightgray;
                    "
                  >
                    <v-icon left>mdi-refresh</v-icon>
                    초기화
                  </v-btn> -->
                  <v-chip
                    v-for="(career, index) in careers"
                    :key="index"
                    :value="career"
                    :class="selectedCareer === career ? 'selected-chip' : 'unselected-chip'"
                    class="career-chip"
                    clickable
                  >
                    {{ career }}
                  </v-chip>
                </v-chip-group>
              </v-col>
            </v-row>
            <!-- 카테고리 선택 제목과 카테고리 필터를 같은 열에 배치 -->
          </v-col>
        </v-row>
      </v-slide-y-transition>

      <h2>안녕하십니까? AI 모의 면접 서비스입니다.</h2>
      <br />
      <v-container class="draw-line" align="start">
        <v-card-title align="center"
          ><strong>※ 사전 공지 ※</strong></v-card-title
        ><br />
        <li class="li">
          본 면접은 특정 기업 및 직무에 맞추어진 면접인인
          <strong>TECH-INTERVIEW</strong>임을 알려드립니다.
        </li>

        <li class="li">
          모의면접에는 <strong>마이크, 카메라</strong>의 사용이 필요합니다.
        </li>
        <br /> </v-container
      ><br />
      <v-card-text
        ><strong
          >시작에 앞서 체크리스트를 작성하여 주십시오.</strong
        ></v-card-text>
      <!-- 제출 버튼 -->
      <v-btn @click="startQuestion" color="primary">제출하기</v-btn>
    </v-container>

     <!-- 면접 진행 UI (생략 없이 유지) -->
    <v-container v-if="start" align="center">
      <div v-if="visible" class="interview-container">
        <v-icon>mdi-account-tie</v-icon><br />
        <div v-html="startMessage"></div>
      </div>
      <div v-if="!visible" class="interview-container">
        <v-icon>mdi-account-tie</v-icon>
        <h2 v-html="formattedAIMessage"></h2>
        <br />
        <div :class="{ timer: true, 'red-text': remainingTime <= 10 }">
          남은 시간: {{ Math.floor(remainingTime / 60) }}:{{
            (remainingTime % 60).toString().padStart(2, "0")
          }}
        </div>
      </div>

      <div v-if="isLoading && !finished" class="message ai">
        <br />
        <p><strong>다음 질문을 준비 중입니다.</strong></p>
        <v-icon>mdi:account-tie</v-icon>
        <div class="loading-message">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      </div>
      <div v-if="isLoading && finished" class="message ai">
        <br />
        <p><strong>답변을 채점 중입니다. 잠시만 기다려 주세요.</strong></p>
        <v-icon>mdi:account-tie</v-icon>
        <div class="loading-message">
          <div class="dot"></div>
          <div class="dot"></div>
          <div class="dot"></div>
        </div>
      </div>
    </v-container>

    <!-- 답변 입력 영역 -->
    <v-container v-if="start && !visible" clas="input-area">
      <div class="button-group">
        <button class="send-button" @click="startSTT" :disabled="recognizing">
          말하기
        </button>

        <button @click="speakCurrentMessage">🗣 AI 질문 듣기</button>
      </div>

      <v-btn color="primary" @click="onAnswerComplete">답변 완료</v-btn>

      <div v-if="sttLog !== ''" class="stt-log">
        <p><strong>STT 결과:</strong> {{ sttLog }}</p>
      </div>
    </v-container>
  </main>
</template>

<script setup>
import { ref, watch, computed, onMounted } from "vue";
import { useAiInterviewStore } from "../../../aiInterview/stores/aiInterviewStore"; // Pinia store import
import { useAccountStore } from "../../../account/stores/accountStore";
import markdownIt from "markdown-it";
import { useRouter } from "vue-router";
import "@mdi/font/css/materialdesignicons.css";

// Pinia Stores
const aiInterviewStore = useAiInterviewStore();
const accountStore = useAccountStore();
const router = useRouter();

// Component State
const accountId = ref(""); //로그인 확인
const start = ref(false); //면접 시작
const finished = ref(false); //면접 끝
const visible = ref(true); //시작안내에서 면접 질문 표시 돌리기기
const userInput = ref(""); //유저응답
const currentAIMessage = ref(""); //ai응답
const chatHistory = ref([{ type: "ai", content: "" }]); //대화 흐름저장
const isLoading = ref(false); //로딩확인
const sendCount = ref(0); //질문갯수 확인
const maxMessages = 5; //최대질문 갯수 5개
const aiResponseList = ref([]); //ai질문 데이터 저장
const questionIndex = ref(0); //몇번쨰 질문인지 저장
const intentList = ["대처 능력", "소통 능력", "프로젝트 경험", "자기 개발"]; //질문주제
const intentIndex = ref(0); //몇번째 주제인지 저장
const startMessage =
  "<h2>안녕하세요. AI 모의 면접 서비스입니다.</h2><br><strong><span>제한 시간 내에 답변 작성 부탁드립니다.</span><br><span>지금부터 면접을 시작하겠습니다.</span></strong>";
//면접시작 알림 메세지
const selectedKeywords = ref([]);

//기술 모음
const keywords = ref([
  "Backend",
  "Frontend",
  "App·Web",
  "AI",
  "Embeddeed",
  "DevOps",
]);
const selectedKeyword = ref(""); // 기술 단일 선택 (중복선택X)

//경력 모음
const careers = ref(["신입", "3년 이하", "5년 이하", "10년 이하", "10년 이상"]);
const selectedCareer = ref("");  // 경력 단일 선택 (중복선택X)

//질문 문장단위 줄바꿈
const formattedAIMessage = computed(() => {
  return currentAIMessage.value.replace(/([.?])/g, "$1<br>");
});

// 질문개수 초과 여부
const isCheckoutDisabled = computed(() => sendCount.value >= maxMessages);

const timeLimit = 90; //응답 시간제한
const remainingTime = ref(timeLimit); //응답 후 남은 시간
const timer = ref(null); //타이머

//음성인식
const recognizing = ref(false); //음성인식 상태여부
let recognition; //SpeechRecognition 인스턴스
const sttLog = ref(""); //STT결과 저장

//면접이 시작되는걸 감지
//showStartMessage() 출력
watch(start, (newVal) => {
  if (newVal === true) {
    showStartMessage();
  }
});

//2.5초 뒤에 안내문 닫고 질문 시작
const showStartMessage = () => {
  const synth = window.speechSynthesis;
  const utterance = new SpeechSynthesisUtterance(
    "안녕하세요. AI 모의 면접을 시작하겠습니다. 제한 시간 내에 답변 작성 부탁드립니다. 지금부터 면접을 시작하겠습니다."
  );
  utterance.lang = "KO-KR";

  utterance.onend = () => {
    visible.value = false;
  };

  synth.speak(utterance);
};

//false가 되면 getAIQuestions()를 실행
watch(visible, (newVal) => {
  if (newVal === false) {
    getAIQuestions();
  }
});

// usertoken을 확인하여 로그인 상태 확인
// 체크리스트 작성하여 제출하면 sessionstorage확인 후 제거
onMounted(async () => {
  const userToken = localStorage.getItem("userToken");
  if (userToken) {
    accountId.value = await accountStore.requestAccountIdToDjango(userToken);
  } else {
    alert("로그인이 필요합니다.");
    router.push("/account/login");
  }

  if (sessionStorage.getItem("startInterview") === "true") {
    start.value = true;
    sessionStorage.removeItem("startInterview");
  }
});

//기술 초기화 클릭시 초기화
function clearSelectedKeywords() {
  if (selectedKeywords.value.length == 0);

  selectedKeywords.value.splice(0, selectedKeywords.value.length);
  resetChips.value = true;
  selectedKeywords.value = [];
  nextTick(() => {
    selectedKeywords.value.splice(0, selectedKeywords.value.length);
    resetChips.value = false;
  });
}

//경력 초기화 클릭시 초기화
function clearSelectedCareer() {
  if (selectedCareers.value.length == 0);

  selectedCareers.value.splice(0, selectedCareers.value.length);
  resetCareer.value = true;
  selectedCareers.value = [];
  nextTick(() => {
    selectedCareers.value.splice(0, selectedCareers.value.length);
    resetCareer.value = false;
  });
}

//음성인식
onMounted(() => {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert("이 브라우저는 음성 인식을 지원하지 않습니다.");
    return;
  }

  // ✅ 음성 인식 인스턴스 생성
  recognition = new SpeechRecognition();
  recognition.lang = "ko-KR";
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onstart = () => {
    recognizing.value = true;
    console.log("🎤 음성 인식 시작");
  };

  recognition.onend = () => {
    recognizing.value = false;
    console.log("🛑 음성 인식 종료");
  };

  recognition.onerror = (e) => {
    console.error("🎙 음성 인식 오류", e);
    recognizing.value = false;
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    console.log("🎙 인식된 음성:", transcript);

    userInput.value += transcript;
    sttLog.value = transcript;
  };
});

const startSTT = () => {
  if (recognition && !recognizing.value) {
    recognition.start();
  }
};
//여기까지

//면접 시 타이머
const startTimer = () => {
  clearInterval(timer.value);
  remainingTime.value = timeLimit;

  // 타이머 설정
  timer.value = setInterval(() => {
    if (remainingTime.value > 0) {
      remainingTime.value--;
    } else {
      clearInterval(timer.value);
      sendMessage();
    }
  }, 1000);
};

//ai가 새로운 질문이 나오면 답변타이머 시작
watch(currentAIMessage, () => {
  startTimer();
});

//타이머 정리
onBeforeUnmount(() => {
  clearInterval(timer.value);
});

// AiInterviewQuestionPage.vue로 이동
const startQuestion = () => {
  if (!selectedKeyword.value ||
      !selectedCareer.value
   ) {
    alert("기술과 경력을 모두 선택해 주세요.");
    return;
  }
  //const KeywordText = selectedKeywords.value.join(",");
  //const careerText = selectedCareers.value.join(",");

  const message = `선택한 기술: ${selectedKeyword.value}\n선택된 경력: ${selectedCareer.value}`;

  if (confirm(message)) {
    start.value = true;
  }
};

//버튼에 연결하여 다음으로 넘김
const onAnswerComplete = async () => {
  clearInterval(timer.value);
  await sendMessage();
};

//질문
const getAIQuestions = async () => {
  if (aiResponseList.value.length === 0) {
    const questionId = Math.floor(Math.random() * 200) + 1;

    // ✅ 숫자만 넘기기
    aiResponseList.value = await aiInterviewStore.requestFirstQuestionToDjango(
      questionId
    );
  }

  currentAIMessage.value =
    aiResponseList.value.firstQuestion ||
    "질문을 불러오는 데 실패하였습니다. 다시 시도해주세요.";

  chatHistory.value.push({ type: "ai", content: currentAIMessage.value });
  speak(currentAIMessage.value, () => {
    const chunks = chunkText(currentAIMessage.value, 1);
    streamText(chunks);
    startTimer();
  });
};

//질문을 마크다운 형태로 HTML로 변환 렌더링
const renderMessageContent = (message) => {
  if (message.type !== "user") {
    return `<h2>${markdownIt().render(message.content)}</h2>`;
  }
};

//TTS
const speak = (text) => {
  const synth = window.speechSynthesis;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "KO-KR";
  utterance.rate = 0.9;
  utterance.pitch = 1.1;
  utterance.volume = 1;
  synth.speak(utterance);
};

const streamText = async (chunks) => {
  currentAIMessage.value = "";
  let index = 0;
  const interval = setInterval(() => {
    if (index < chunks.length) {
      currentAIMessage.value += chunks[index];
      updateAIMessage();
      index++;
    } else {
      clearInterval(interval);
    }
  }, 10);
};

const updateAIMessage = () => {
  const lastIndex = chatHistory.value.length - 1;
  if (
    chatHistory.value[lastIndex] &&
    chatHistory.value[lastIndex].type === "ai"
  ) {
    chatHistory.value[lastIndex].content = currentAIMessage.value;
  } else {
    chatHistory.value.push({ type: "ai", content: currentAIMessage.value });
  }
};

const adjustTextareaHeight = () => {
  const textarea = document.getElementById("messageInput");
  if (textarea) {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  }
};

const handleEnterKey = (event) => {
  if (!event.shiftKey) {
    sendMessage();
  }
};

const handleShiftEnter = () => {
  adjustTextareaHeight();
};

const sendMessage = async () => {
  if (sendCount.value >= maxMessages) {
    finished.value = true;
    return;
  }
  if (userInput.value.trim()) {
    chatHistory.value.push({ type: "user", content: userInput.value });
  } else {
    chatHistory.value.push({
      type: "user",
      content: "질문에 답변하지 못했습니다.",
    });
  }
  userInput.value = "";
  adjustTextareaHeight();
  isLoading.value = true;
  sendCount.value++;

  setTimeout(async () => {
    if (aiResponseList.value.length === 0) {
      const questionId = Math.floor(Math.random() * 200) + 1;
      aiResponseList.value =
        await aiInterviewStore.requestFirstQuestionToDjango({
          questionId: questionId,
        });
    }

    if (intentIndex.value === 4) {
      currentAIMessage.value =
        "수고하셨습니다. 면접이 종료되었습니다. 추후에 더 발전된 서비스로 찾아뵙겠습니다.";
      chatHistory.value.push({ type: "ai", content: currentAIMessage.value });
      finished.value = true;
      if (finished.value) {
        chatHistory.value.shift();
        chatHistory.value.pop();
        const contents = chatHistory.value.map((item) => item.content);
        const pairedContents = [];
        const interviewIntents = [
          "자기 분석",
          "대처 능력",
          "소통 능력",
          "프로젝트 경험",
          "자기 개발",
        ];

        for (let i = 0; i < contents.length; i += 2) {
          pairedContents.push([
            contents[i],
            contents[i + 1],
            interviewIntents[Math.floor(i / 2)],
          ]);
        }

        const payload = { interviewResult: pairedContents };
        try {
          await aiInterviewStore.requestInferScoreResultToFastAPI(payload);
          const response =
            await aiInterviewStore.requestInferedResultToFastAPI(); //[1,2,3,4,5]
          for (let i = 0; i < response.resultList.length; i++) {
            pairedContents[i].push(response.resultList[i]);
          }

          const result = {
            scoreResultList: pairedContents,
            accountId: accountId.value,
          };
          const saveDone =
            await aiInterviewStore.requestSaveInterviewResultToDjango(result);
          if (saveDone) {
            alert("면접 결과 확인하기");
            router.push(`/ai-interview/result/${accountId.value}`);
          }
        } catch {
          alert("죄송합니다. 지금은 채점 기능을 지원할 수 없습니다.");
        }
      }
    } else {
      const nextIntent = intentList[intentIndex.value];
      intentIndex.value++;

      let lastUserInput = null;
      for (let i = chatHistory.value.length - 1; i >= 0; i--) {
        if (chatHistory.value[i].type === "user") {
          lastUserInput = chatHistory.value[i].content;
          break;
        }
      }

      const payload = { answer: lastUserInput, nextIntent: nextIntent };
      try {
        await aiInterviewStore.requestInferNextQuestionToFastAPI(payload);
        const response = await aiInterviewStore.requestInferedResultToFastAPI();
        if (response && response.nextQuestion) {
          currentAIMessage.value = response.nextQuestion;
          chatHistory.value.push({
            type: "ai",
            content: currentAIMessage.value,
          });
        }
      } catch {
        if (nextIntent == "대처 능력") {
          const tempQuestionList = [
            "어려운 상황이나 갈등이 발생했을 때, 어떻게 대처하시는 편인가요? 그 사례를 들어 설명해 주세요.",
            "어려운 상황에서 예상치 못한 문제가 발생했을 때, 어떻게 대처하시는 편인가요? 구체적인 예시가 있다면 말씀해 주세요.",
            "스트레스를 받는 상황이나 예상치 못한 문제에 직면했을 때, 보통 어떤 방식으로 대처하시나요? 구체적인 예시를 들어주시면 좋겠습니다.",
            "스트레스를 받는 상황이 생겼을 때, 어떻게 대처하는 편인가요? 구체적인 사례와 함께 설명해 주세요.",
          ];
          const randomIndex = Math.floor(
            Math.random() * tempQuestionList.length
          );
          currentAIMessage.value = tempQuestionList[randomIndex];
          speak(currentAIMessage.value);
        }
        if (nextIntent == "소통 능력") {
          const tempQuestionList = [
            "팀원 간에 소통이 원활하지 않을 때, 이를 어떻게 개선할 수 있다고 생각하나요?",
            "팀원 간의 의사소통이 원활하지 않을 때, 이를 개선하기 위해 어떤 노력을 기울였는지 구체적인 사례를 들어 설명해 주세요.",
            "팀원 간의 갈등이 발생했을 때, 그 상황을 어떻게 해결하실 건가요?",
            "팀원들과의 소통에서 가장 중요하게 생각하는 점은 무엇이며, 이를 실천하기 위해 어떤 노력을 하고 있나요?",
          ];
          const randomIndex = Math.floor(
            Math.random() * tempQuestionList.length
          );
          currentAIMessage.value = tempQuestionList[randomIndex];
        }
        if (nextIntent == "프로젝트 경험") {
          const tempQuestionList = [
            "최근에 참여한 프로젝트에 대해 소개해주실 수 있나요? 프로젝트의 목표와 주요 내용을 말씀해 주세요.",
            "이전에 참여했던 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표를 가지고 진행되었고, 어떤 결과를 이끌어냈는지 궁금합니다.",
            "이전에 참여했던 프로젝트 중 가장 기억에 남는 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표가 있었고, 어떤 방식으로 진행되었는지 궁금합니다.",
            "최근에 참여했던 프로젝트에 대해 설명해 주실 수 있나요? 어떤 목표를 가지고 진행했으며, 어떤 결과가 있었는지 궁금합니다.",
          ];
          const randomIndex = Math.floor(
            Math.random() * tempQuestionList.length
          );
          currentAIMessage.value = tempQuestionList[randomIndex];
        }
        if (nextIntent == "자기 개발") {
          const tempQuestionList = [
            "자기 개발을 위해 최근에 어떤 새로운 기술이나 지식을 배우셨나요? 그 과정에서 느낀 점은 무엇인가요?",
            "최근에 본인에게 가장 큰 발전이 있다고 느꼈던 경험은 무엇이었나요? 그 경험이 왜 중요했는지 설명해 주시겠습니까?",
            "최근에 어떤 자기 개발 활동을 진행했는지 설명해 주시고, 그 경험이 어떻게 도움이 되었는지도 이야기해 주시기 바랍니다.",
            "최근에 자신이 개발한 기술이나 역량이 있나요? 그 기술을 어떻게 익히게 되었는지 구체적으로 말씀해 주세요.",
          ];
          const randomIndex = Math.floor(
            Math.random() * tempQuestionList.length
          );
          currentAIMessage.value = tempQuestionList[randomIndex];
        }
      }
    }

    const chunks = chunkText(currentAIMessage.value, 1);
    streamText(chunks);
    isLoading.value = false;
  }, 1000);
};

//면접페이지에 들어오면 출력되는 제목
useHead({
  title: `AI 모의면접 & 인성면접 | `,
  meta: [
    {
      name: "description",
      content: "AI 모의면접, AI 인성면접 🎯jobstcik에서 확인해보세요.",
    },
    {
      hid: "keywords",
      name: "keywords",
      content:
        "모의면접, ai 모의면접, 인성면접, ai 인성면접, 인적성 검사 준비, ai 인적, ai 면접, aim 모의면접, aim ai 모의면접, 에임 모의면접, 에임, 애임, AIM, AIM Sniper",
    },
  ],
});
</script>

<style scoped>
.draw-line {
  border: 1px solid #333;
  padding: 16px;
  border-radius: 10px;
  width: 57%;
}

.li {
  margin-left: 2%;
}
.timer {
  font-size: 15px;
  color: black;
}

.red-text {
  color: red;
}

.control-margin {
  margin-top: 5%;
}

.interview-container {
  margin-top: 20%;
  border: 1px solid #333;
  padding: 16px;
  border-radius: 10px;
  width: 70%;
}

.input-area {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 50%;
  margin-bottom: 0;
}

/*말하기 버튼, 질문듣기 버튼*/
.button-group {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

/* 필터 칩 스타일링 */
.filter-chip {
  margin: 5px;
  font-size: 14px;
}

.selected-chip {
  background-color: #6366f1 !important;
  color: white !important;
}

.unselected-chip {
  background-color: #e0e0e0 !important;
  color: black !important;
}

/*
.chip-selected {
  background-color: #8094f4; /* 선택된 칩의 배경색을 초록색으로 변경 
  color: white; /* 텍스트 색상을 하얀색으로 변경
} */

textarea {
  flex-grow: 1;
  border: 1px solid #ccc;
  padding: 12px;
  resize: none;
  border-radius: 10px;
  box-sizing: border-box;
  font-size: 15px;
  background-color: rgba(255, 255, 255, 1);
  color: black;
  height: 50px;
  max-height: 70px;
}

.send-button {
  padding: 10px 12px;
  background-color: black;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
}

.loading-message {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 15px;
  border-radius: 18px;
  background-color: rgba(233, 233, 235, 0.8);
  color: black;
  font-style: italic;
  width: 50px;
}

.loading-message .dot {
  height: 10px;
  width: 10px;
  margin: 0 2px;
  background-color: black;
  border-radius: 50%;
  display: inline-block;
  opacity: 0;
  animation: loading-animation 1.5s infinite ease-in-out;
}

.loading-message .dot:nth-child(1) {
  animation-delay: 0s;
}

.loading-message .dot:nth-child(2) {
  animation-delay: 0.3s;
}

.loading-message .dot:nth-child(3) {
  animation-delay: 0.6s;
}

@keyframes loading-animation {
  0%,
  80%,
  100% {
    opacity: 0;
  }
  40% {
    opacity: 1;
  }
}
</style>
