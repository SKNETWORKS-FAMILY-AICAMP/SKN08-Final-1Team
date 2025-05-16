<template>
  <main>
    <v-container class="report-containeer">
      <h1 class="report-title">AI 모의면접 결과</h1>
      <v-divider class="my-4" thickness="2" color="white" />

      <v-row
        v-for="(item, index) in inputList"
        :key="index"
        class="question-box my-6"
      >
        <v-col cols="12">
          <h3 class="question-title">{{ index + 1 }}.{{ item.question }}</h3>

          <div class="answer-section">
            <h4>📄 당신의 답변</h4>
            <p class="answer-text">{{ item.answer }}</p>
          </div>

          <div class="evaluation-section">
            <h4>AI 평가 결과</h4>
            <p><strong>의도파악:</strong>{{ item.intent }}</p>
            <p><strong>피드백:</strong></p>
            <p class="feedback-text">{{ item.feedback }}</p>
          </div>
        </v-col>
      </v-row>
      <div v-if="downloadUrl" style="text-align: center; margin-top: 16px">
        <a
          :href="downloadUrl"
          download="interview-recording.webm"
          style="color: blue; text-decoration: underline"
        >
          🎥 녹화 영상 다운로드
        </a>
      </div>
    </v-container>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";
import { useAiInterviewStore } from "../../stores/aiInterviewStore"; // Pinia store import
import markdownIt from "markdown-it";

// ✅ SEO 메타 정보
definePageMeta({
  title: 'AI 면접 결과 보기 | JobStick',
  description: 'AI 기반 모의 면접 결과를 확인하고, 나의 강점과 개선점을 분석해보세요.',
  keywords: ['AI 면접', '면접 결과', '자기 분석', '모의 면접', 'AI 분석', 'JotStick', 'job-stick', '잡스틱'],
  ogTitle: 'AI 면접 결과 - JobStick',
  ogDescription: 'AI가 분석한 나의 면접 결과를 지금 확인해보세요.',
  ogImage: '' // 실제 이미지 경로
});

// Pinia Store
const aiInterviewStore = useAiInterviewStore();
const router = useRouter();
// Component State
const userToken = localStorage.getItem("userToken");
const inputList = ref([]);
const downloadUrl = ref(null);

// Lifecycle Hooks
onMounted(async () => {
  await getScoreResultList(userToken);
});
//영상 저장 url 불러오기
onMounted(() => {
  const saveUrl = localStorage.getItem("interviewRecordingUrl");
  if (saveUrl) {
    downloadUrl.value = saveUrl;
  }
});

// Methods
const getScoreResultList = async (userToken) => {
  try {
    const res = await aiInterviewStore.requestGetInterviewResultToDjango({
      userToken: userToken,
    });
    console.log("✅ 응답 확인:", res);
    inputList.value = res.interviewResultList;
  } catch (err) {
    console.error("❌ 면접 결과 불러오기 실패:", err);
  }
};

//페이지 이탈 시 url정리
onBeforeUnmount(() => {
  if (downloadUrl.value) {
    URL.revokeObjectURL(downloadUrl.value);
  }
  localStorage.removeItem("interviewRecordingUrl");
});
</script>

<style>
.report-container {
  max-width: 850px;
  margin: auto;
  padding: 40px 30px;
  background-color: #ffff;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  border-radius: 16px;
}

.report-title {
  font-size: 32px;
  font-weight: bold;
  text-align: center;
  color: #333;
}

.question-box {
  background-color: #f0f5ff;
  border-radius: 12px;
  margin-bottom: 24px;
  padding: 24px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.question-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 16px;
}

.answer-section,
.evaluation-section {
  margin-top: 12px;
  padding: 16px;
  border-radius: 8px;
  background-color: #ffff;
  border: 1px solid #cbd7f1;
}

.answer-section h4,
.evaluation-section h4 {
  margin-bottom: 10px;
  font-weight: 600;
  color: #2c3e50;
}

.answer-text,
.feedback-text {
  font-size: 15px;
  line-height: 1.7;
  white-space: pre-line;
  color: #444;
  padding-left: 10px;
}
</style>
