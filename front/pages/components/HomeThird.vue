<template>
  <div class="home-third">
    <div class="home-third-body">
      <div class="content-container" data-aos="fade-left" data-aos-offset="400">
        <v-card class="content-image" id="first-image"></v-card>
        <div class="text-container">
          <p class="number-icon">1</p>
          <div class="text-title-container">
            <p class="text-title">다양한 기업보고서</p>
            <p class="text-subtitle">최신 기업 및 채용정보 확인</p>
          </div>
          <div class="text-content-container">
            <p class="text-content">
              <span class="AIV-span">JOBSTICK</span>는 다양한 기업의 최신 정보를
              제공합니다.
            </p>
          </div>
        </div>
      </div>

      <div
        class="content-container"
        data-aos="fade-right"
        data-aos-offset="400"
      >
        <div class="text-container">
          <p class="number-icon">2</p>
          <div class="text-title-container">
            <p class="text-title">실전 같은 모의면접</p>
            <p class="text-subtitle">AI기반 맞춤 면접 질문 제공</p>
          </div>
          <div class="text-content-container">
            <span class="AIV-span">JOBSTICK</span>는 AI를 기반으로 업계별,
            직무별 맞춤형 질문을 제공하여 실전같은 면접질문을 제공합니다.
          </div>
        </div>
        <v-card class="content-image" id="second-image"></v-card>
      </div>

      <div class="content-container" data-aos="fade-left" data-aos-offset="400">
        <v-card class="content-image" id="third-image"></v-card>
        <div class="text-container">
          <p class="number-icon">3</p>
          <div class="text-title-container">
            <p class="text-title">전문적 피드백</p>
            <p class="text-subtitle">피드백을 통한 문제점 확인</p>
          </div>
          <div class="text-content-container">
            <p class="text-content">
              정확한 피드백을 통해 문제점 확인하여 면접 스킬을 향상시킬 수
              있습니다.
            </p>
          </div>
        </div>
      </div>

      <div
        class="content-container"
        data-aos="fade-right"
        data-aos-offset="400"
      >
        <div class="text-container">
          <p class="number-icon">4</p>
          <div class="text-title-container">
            <p class="text-title">영상 분석 확인 가능</p>
            <p class="text-subtitle">면접 기록 영상 제공</p>
          </div>
          <div class="text-content-container">
            <p class="text-content">
              시선 처리, 발화 습관 등을 파악할 수 있으며
            </p>
            <p class="text-content">
              이를 기반으로 빠른 면접 스킬을 향상할 수 있습니다.
            </p>
          </div>
        </div>
        <v-card class="content-image" id="fourth-image"></v-card>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "HomeThird",
});
</script>

<style scoped>
.home-third {
  width: 100%;
  height: 420vh; /* 기존 350vh에서 400vh로 증가 */
  background: url("@/assets/images/fixed/home_bg2.jpg") center center;
  background-size: cover;
  background-attachment: fixed;
  display: flex;
  justify-content: center;
}

.home-third-body {
  width: 70%;
  height: 100%;
  display: flex;
  display: flex;
  flex-direction: column;
  /* gap: 1%; */
}

.content-container {
  width: 100%;
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 100px;
}

.content-image {
  width: 50%;
  height: 60%;
  border-radius: 25px;
}

#first-image {
  background-image: url("@/assets/images/fixed/info.jpg");
  background-size: 105% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

#second-image {
  background-image: url("@/assets/images/fixed/interview.jpg");
  background-size: 105% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

#third-image {
  background-image: url("@/assets/images/fixed/feedback.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

#fourth-image {
  background-image: url("@/assets/images/fixed/videointerview.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.text-container {
  width: 50%;
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 30px;
}

.number-icon {
  font-size: 4vh;
  font-weight: bold;
  color: #000000d7;
  background-color: #ffffff;
  width: 5vh;
  height: 5vh;
  border-radius: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}

.text-title {
  font-size: 5vh;
  font-weight: bold;
  color: #000000;
}

.text-subtitle {
  font-size: 2.3vh;
  font-weight: bold;
  color: #000000;
}

.text-content {
  font-size: 2.2vh;
  color: #000000;
}

.AIV-span {
  color: rgb(30, 56, 255);
}
</style>
