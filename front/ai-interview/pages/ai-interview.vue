<template>
  <v-container v-if="!start" align="center">
    <div class="interview-container">
      <v-icon>mdi-account-tie</v-icon><br />
      <div v-html="startMessage"></div>

      <!-- ✅ 카메라+마이크 녹화 확인 UI -->
      <div style="margin-top: 16px">
        <video
          ref="previewVideo"
          autoplay
          playsinline
          muted
          style="
            width: 320px;
            height: 240px;
            background: #000;
            border-radius: 8px;
          "
        />
        <div style="margin-top: 8px">
          <v-btn color="info" @click="checkMediaReady"
            >카메라/마이크 상태 확인</v-btn
          >
          <v-btn color="success" class="ml-2" @click="startRecording"
            >🎥 녹화 시작</v-btn
          >
          <v-btn color="error" class="ml-2" @click="stopRecording"
            >🛑 녹화 종료</v-btn
          >
          <v-btn
            color="warning"
            class="ml-2"
            @click="playRecording"
            :disabled="!recordedBlob"
            >▶ 영상 재생</v-btn
          >
        </div>
      </div>

      <!-- 면접 시작 버튼 -->
      <v-btn
        color="primary"
        class="mt-4"
        @click="handleStartInterview"
        :disabled="!mediaChecked"
      >
        면접 시작
      </v-btn>
    </div>
  </v-container>

  <!-- 이하 기존 start=true 상태 -->
  <v-container v-else fluid class="pa-0">
    <div style="width: 75%; margin: 0 auto; padding-top: 16px">
      <v-row class="video-row" no-gutters style="margin: 0; padding: 0">
        <v-col
          cols="6"
          class="pa-0"
          style="display: flex; justify-content: flex-end"
        >
          <div class="video-box" style="width: 100%; height: 300px">
            <img :src="hhImage" alt="면접관" class="interviewer-image" />
          </div>
        </v-col>

        <v-col class="pa-0" style="max-width: 16px"></v-col>

        <v-col
          cols="6"
          class="pa-0"
          style="display: flex; justify-content: flex-start"
        >
          <div class="video-box" style="width: 100%; height: 300px">
            <video
              ref="userVideo"
              v-show="start"
              autoplay
              playsinline
              muted
              class="user-video"
            ></video>
          </div>
        </v-col>
      </v-row>
    </div>

    <v-col class="pa-0" style="max-width: 16px"></v-col>

    <v-col
      cols="12"
      class="pa-0 mt-4"
      style="display: flex; justify-content: center"
    >
      <div
        v-if="visible"
        class="interview-container centered-text-box"
        style="margin-top: 0; width: 75%"
      >
        <v-icon>mdi-account-tie</v-icon><br />
        <div v-html="startMessage"></div>
      </div>
      <div
        v-else
        class="interview-container centered-text-box"
        style="margin-top: 0; width: 75%"
      >
        <v-icon>mdi-account-tie</v-icon><br />
        <h2 v-html="formattedAIMessage"></h2>
        <br />
        <div :class="{ timer: true, 'red-text': remainingTime <= 10 }">
          남은 시간: {{ Math.floor(remainingTime / 60) }}:{{
            (remainingTime % 60).toString().padStart(2, "0")
          }}
        </div>
      </div>
    </v-col>

    <div v-if="isLoading && !finished" class="message ai">
      <br />
      <p><strong>다음 질문을 준비 중입니다.</strong></p>
      <v-icon>mdi-account-tie</v-icon>
      <div class="loading-message">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
      </div>
    </div>

    <v-container v-if="start && !visible" class="input-area">
      <div class="button-group">
        <button class="send-button" @click="startSTT" :disabled="recognizing">
          {{ recognizing ? "녹음 중..." : "말하기" }}
        </button>
        <button @click="replayQuestion">🗣 AI 질문 듣기</button>
      </div>
      <v-btn color="primary" @click="onAnswerComplete">답변 완료</v-btn>
      <div v-if="sttLog !== ''" class="stt-log">
        <p><strong>STT 결과:</strong> {{ sttLog }}</p>
      </div>
      <v-text-field
        v-model="sttLog"
        label="개발 중: 답변 직접 입력"
        hide-details
        dense
        solo
        style="max-width: 300px"
      />
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from "vue";
import { useAiInterviewStore } from "../stores/aiInterviewStore";
import { useRouter, onBeforeRouteLeave } from "vue-router";
import "@mdi/font/css/materialdesignicons.css";
import hhImage from "@/assets/images/fixed/al3.png";

// ✅ SEO 메타 정보
definePageMeta({
  title: "AI 모의 면접 시작 | JobStick",
  description:
    "AI 기반 모의 면접을 진행하고, 원하는 기업, 직무에 대한 기술 면접을 대비해보세요.",
  keywords: [
    "AI 면접",
    "모의 면접",
    "기술 면접",
    "AI 기반 모의 면접",
    "카메라 테스트",
    "면접 준비",
    "온라인 면접",
    "비대면 면접",
    "인공지능 면접",
    "JobStick",
    "job-stick",
    "잡스틱"
  ],
  ogTItle: "AI 모의 면접 준비 - JobStick",
  ogDescription:
    "AI 기반의 실전 면습 연습을 통해 기술 면접의 실전 감각을 길러보세요.",
  ogImage: "", // 실제 이미지 경로
  robots: 'index, follow' // 검색 노출 허용 
});

const router = useRouter();
const aiInterviewStore = useAiInterviewStore();

const start = ref(false);
const visible = ref(true);
const isLoading = ref(false);
const finished = ref(false);
const recognizing = ref(false);
const sttLog = ref("");
const currentAIMessage = ref("");
const currentQuestionId = ref(1);
const currentInterviewId = ref(null);
const remainingTime = ref(90);
const timer = ref(null);
const maxQuestionId = ref(10);
const startMessage = ref("");
const userVideo = ref(null);
const mediaChecked = ref(false);
const previewVideo = ref(null);
const mediaStream = ref(null);

const mapCompanyName = (original) => {
  const mapping = {
    당근마켓: "danggeun",
    Toss: "toss",
    "SK-encore": "sk_encore",
    "KT M mobile": "kt_mobile",
  };
  return mapping[original] || original.toLowerCase().replace(/[\s-]+/g, "_");
};

const checkMediaReady = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true,
    });
    mediaChecked.value = true;
    alert("마이크와 카메라가 정상적으로 작동합니다.");
    mediaStream.value = stream;
    if (previewVideo.value) previewVideo.value.srcObject = stream;
  } catch (err) {
    alert(
      "마이크 또는 카메라에 접근할 수 없습니다. 브라우저 권한을 확인하세요."
    );
    mediaChecked.value = false;
  }
};

const recordedVideo = ref(null); // 상단에 선언 필요
const recordedBlob = ref(null); // 상단에 선언 필요
let recordingStream = null;
let recorder = null;
let chunks = [];
//면접 전 녹화 되는지 확인용
const startRecording = async () => {
  try {
    recordingStream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true,
    });
    if (previewVideo.value) previewVideo.value.srcObject = recordingStream;

    chunks = [];
    recorder = new MediaRecorder(recordingStream, { mimeType: "video/webm" });

    recorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        chunks.push(event.data);
      }
    };

    recorder.onstop = () => {
      recordedBlob.value = new Blob(chunks, { type: "video/webm" });
      const videoURL = URL.createObjectURL(recordedBlob.value);
      localStorage.setItem("interviewRecordingUrl", videoURL); //로컬에 임시저장
      // ✅ previewVideo에서 녹화 영상 재생
      if (previewVideo.value) {
        previewVideo.value.srcObject = null; // 스트림 끊기
        previewVideo.value.src = videoURL;
        previewVideo.value.controls = true;
        previewVideo.value.play();
      }
    };
    //영상녹화
    recorder.start();
    alert("녹화를 시작합니다다");
  } catch (err) {
    console.error("🎥 녹화 시작 실패:", err);
    alert("녹화 시작 중 오류가 발생했습니다.");
  }
};
//녹화중지
const stopRecording = () => {
  if (recorder && recorder.state === "recording") {
    recorder.stop();
    if (recordingStream) {
      recordingStream.getTracks().forEach((track) => track.stop());
    }
    alert("녹화 종료됨");
  }
};

let recognition;
const synth = process.client ? window.speechSynthesis : null;
let currentUtteance = null;

onMounted(async () => {
  try {
    const videoOnlyStream = await navigator.mediaDevices.getUserMedia({
      video: true,
    });
    if (previewVideo.value) {
      previewVideo.value.srcObject = videoOnlyStream;
    }
  } catch (err) {
    console.error("previewVideo 카메라 연결 실패:", err);
  }
  if (process.client) {
    speakStartMessage();

    await nextTick(); // ✅ DOM 준비된 다음

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("이 브라우저는 음성 인식을 지원하지 않습니다.");
      return;
    }

    recognition = new SpeechRecognition();
    recognition.lang = "ko-KR";
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onstart = () => (recognizing.value = true);
    recognition.onend = () => (recognizing.value = false);
    recognition.onerror = () => (recognizing.value = false);
    recognition.onresult = (event) => {
      let finalTranscript = "";
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        }
      }
      sttLog.value += finalTranscript;
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
  }
});

const showWarning = ref(true); // 이거 먼저 선언돼 있어야 함

const speakStartMessage = () => {
  startMessage.value = `
    <strong style="display: flex; flex-direction: column; align-items: center;">
      <span style="margin-bottom: 8px;">AI 모의 면접이 곧 시작됩니다.</span>
      <span style="margin-bottom: 8px;">면접 질문이 화면에 표시되며, 자동으로 음성으로 읽어드립니다.</span>
      <span style="margin-bottom: 8px;"><mark style="background: #ffecb3;">말하기 버튼</mark>을 눌러 답변을 시작해 주세요.</span>
      <span style="margin-bottom: 8px;">마이크와 카메라가 정상적으로 작동 중인지 확인해 주세요.</span>
      ${
        showWarning.value
          ? '<span style="color: red; font-weight: bold;">※ 카메라/마이크 상태 확인을 체크해야 면접 시작이 가능합니다.</span>'
          : ""
      }
    </strong>
  `;
};

const formattedAIMessage = computed(() => {
  return currentAIMessage.value.replace(/([.?])/g, "$1<br>");
});

const replayQuestion = () => {
  if (synth?.speaking) synth.cancel();
  const utterance = new SpeechSynthesisUtterance(currentAIMessage.value);
  utterance.lang = "ko-KR";
  utterance.rate = 0.85;
  utterance.pitch = 1.0;
  setTimeout(() => synth?.speak(utterance), 100);
};

const handleBeforeUnload = (event) => {
  if (start.value && !finished.value) {
    event.preventDefault();
    event.returnValue = "면접이 진행 중입니다. 페이지를 나가시겠습니까?";
  }
};

const speakCurrentMessage = () => {
  clearInterval(timer.value);
  remainingTime.value = 90;
  currentUtteance = new SpeechSynthesisUtterance(currentAIMessage.value);
  currentUtteance.lang = "ko-KR";
  currentUtteance.rate = 0.85;
  currentUtteance.pitch = 1.0;
  currentUtteance.onend = () => startTimer();
  synth?.speak(currentUtteance);
};

const showStartMessage = () => {
  visible.value = false;
  speakCurrentMessage();
};

const startTimer = () => {
  clearInterval(timer.value);
  timer.value = setInterval(() => {
    if (remainingTime.value > 0) {
      remainingTime.value--;
    } else {
      clearInterval(timer.value);
      onAnswerComplete();
    }
  }, 1000);
};

const startSTT = () => {
  if (recognition && !recognizing.value) {
    sttLog.value = "";
    recognition.start();
  }
};
//자동 녹화 시작
const startRecordingAuto = async () => {
  try {
    recordingStream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true,
    });
    if (userVideo.value) {
      userVideo.value.srcObject = recordingStream;
    }
    chunks = [];
    recorder = new MediaRecorder(recordingStream, { mimeType: "video/webm" });
    recorder.ondataavailable = (event) => {
      if (event.data.size > 0) chunks.push(event.data);
    };
    recorder.onstop = () => {
      recordedBlob.value = new Blob(chunks, { type: "video/webm" });
      const videoURL = URL.createObjectURL(recordedBlob.value);
      localStorage.setItem("interviewRecordingUrl", videoURL);
    };
    recorder.start();
    console.log("녹화 시작");
  } catch (err) {
    console.error("녹화 실패");
  }
};
// 자동 녹화 종료료
const stopRecordingAuto = () => {
  if (recorder && recorder.state === "recording") {
    recorder.stop();
    if (recordingStream) {
      recordingStream.getTracks().forEach((track) => track.stop());
    }
    console.log("녹화 종료");
  }
};
const handleStartInterview = async () => {
  const info = JSON.parse(localStorage.getItem("interviewInfo") || "{}");
  const processedCompanyName = mapCompanyName(info.company);

  if (!info.tech || !info.exp) {
    alert("면접 정보를 찾을 수 없습니다. 처음으로 돌아갑니다.");
    router.push("/ai-interview");
    return;
  }
  start.value = true;
  await startRecordingAuto(); //녹화 시작

  showWarning.value = false;
  speakStartMessage();

  const res = await aiInterviewStore.requestCreateInterviewToDjango({
    userToken: localStorage.getItem("userToken"),
    jobCategory: info.tech,
    experienceLevel: info.exp,
    academicBackground: info.academic,
    projectExperience: info.project,
    interviewTechStack: info.skills,
    companyName: processedCompanyName,
  });
  currentInterviewId.value = Number(res.interviewId);
  currentQuestionId.value = 1;
  currentAIMessage.value = res.question;
  const utterance = new SpeechSynthesisUtterance(
    "AI 모의 면접이 곧 시작됩니다. 면접 질문이 화면에 표시되며, 자동으로 음성으로 읽어드립니다."
  );
  utterance.lang = "ko-KR";
  utterance.rate = 1;
  utterance.pitch = 1;
  utterance.onend = () => showStartMessage();
  synth?.cancel();
  synth?.speak(utterance);
};

const onAnswerComplete = async () => {
  if (recognition && recognizing.value) recognition.stop();

  if (!sttLog.value.trim()) {
    alert("음성 인식 결과가 없습니다.");
    return;
  }
  if (currentQuestionId.value >= maxQuestionId.value) {
    alert("모든 면접이 완료되었습니다");
    finished.value = true;
    return;
  }

  const info = JSON.parse(localStorage.getItem("interviewInfo") || "{}");
  const processedCompanyName = mapCompanyName(info.company);
  const payload = {
    userToken: localStorage.getItem("userToken"),
    interviewId: currentInterviewId.value,
    questionId: currentQuestionId.value,
    answerText: sttLog.value,
    jobCategory: info.tech,
    experienceLevel: info.exp,
    academicBackground: info.academic,
    projectExperience: info.project,
    interviewTechStack: info.skills,
    companyName: processedCompanyName,
  };
  await aiInterviewStore.requestCreateAnswerToDjango(payload);

  let nextQuestion = null;
  let nextQuestionId = null;
  if (currentQuestionId.value === 1 || currentQuestionId.value === 2) {
    const followUp = await aiInterviewStore.requestFollowUpQuestionToDjango(
      payload
    );
    nextQuestion = followUp?.questions?.[0];
    nextQuestionId = followUp?.questionIds?.[0];
  } else if (currentQuestionId.value === 3) {
    const projectMain =
      await aiInterviewStore.requestProjectCreateInterviewToDjango(payload);
    nextQuestion = projectMain?.question?.[0];
    nextQuestionId = projectMain?.questionId;
  } else if (currentQuestionId.value === 4 || currentQuestionId.value === 5) {
    const projectFollowUp =
      await aiInterviewStore.requestProjectFollowUpQuestionToDjango(payload);
    nextQuestion = projectFollowUp?.questions?.[0];
    nextQuestionId = projectFollowUp?.questionIds?.[0];
  } else if (currentQuestionId.value === 6 || currentQuestionId.value === 7) {
    const techFollowUp =
      await aiInterviewStore.requestTechFollowUpQuestionToDjango(payload);
    nextQuestion = techFollowUp?.questions?.[0];
    nextQuestionId = techFollowUp?.questionIds?.[0];
  } else {
    alert("모든 면접 질문이 완료되었습니다.");
    finished.value = true;
    stopRecordingAuto();
    await aiInterviewStore.requestEndInterviewToDjango(payload);
    await aiInterviewStore.requestGetScoreResultListToDjango(payload);
    router.push("/ai-interview/result");
    return;
  }

  if (!nextQuestion || !nextQuestionId) {
    alert("다음 질문을 불러오지 못했습니다.");
    return;
  }

  currentQuestionId.value = nextQuestionId;
  currentAIMessage.value = nextQuestion;
  sttLog.value = "";
  speakCurrentMessage();
};

onBeforeUnmount(() => {
  if (synth?.speaking) synth.cancel();
  localStorage.removeItem("interviewInfo");
  clearInterval(timer.value);
  window.removeEventListener("beforeunload", handleBeforeUnload);
});

onBeforeRouteLeave((to, from, next) => {
  if (start.value && !finished.value) {
    const answer = window.confirm(
      "면접이 진행 중입니다. 페이지를 나가시겠습니까?"
    );
    answer ? next() : next(false);
  } else {
    next();
  }
});
const playRecording = () => {
  if (recordedBlob.value) {
    const videoURL = URL.createObjectURL(recordedBlob.value);
    if (previewVideo.value) {
      previewVideo.value.srcObject = null;
      previewVideo.value.src = videoURL;
      previewVideo.value.controls = true;
      previewVideo.value.play();
    }
  }
};
</script>

<style scoped>
.interview-container {
  margin-top: 32px;
  border: 1px solid #333;
  padding: 16px;
  border-radius: 10px;
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.input-area {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 50%;
  margin-bottom: 0;
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

.video-row {
  margin-top: 24px;
  margin-bottom: 24px;
}

.video-box {
  width: 100%;
  aspect-ratio: 4 / 3;
  border: 2px solid #ccc;
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000;
}

.interviewer-image,
.user-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
