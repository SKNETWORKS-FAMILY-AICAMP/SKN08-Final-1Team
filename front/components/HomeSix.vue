<template>
  <div class="home-six">
    <!-- h1 아래에 작은 텍스트 추가 -->
    <h1>JOBSTICK의 주요 기능</h1>
    <p class="intro-text">
      JOBSTICK을 통해 실전 면접에 필요한 여러 시스템을 이용해 보세요.
    </p>

    <!-- 큰 직사각형 컨테이너 안에 콘텐츠가 이동 -->
    <div class="content-container">
      <!-- 첫 번째 콘텐츠 박스 -->
      <div v-if="currentIndex === 0" class="content-box">
        <div class="content-description">
          <h2>원하는 기업의 요구사항 정보 제공</h2>
          <p>
            기업 뿐만이 아니라 다양한 분야, 직무별로 원하는 인재상 정보들 등
            면접에 필요한 다양한 정보를 제공해드리고 있습니다.
          </p>
        </div>
        <div class="content-image">
          <!-- 첫 번째 이미지 -->
          <img :src="images[0]" alt="기업 요구사항 이미지" />
        </div>
      </div>
      <!-- 두 번째 콘텐츠 박스 -->
      <div v-if="currentIndex === 1" class="content-box">
        <div class="content-description">
          <h2>ai를 이용한 정확한 피드백 제공</h2>
          <p>
            혼자서 준비하는 면접의 가장 큰 어려움인 피드백을 ai를 통해
            사용자에게 제공합니다.
          </p>
        </div>
        <div class="content-image">
          <!-- 두 번째 이미지 -->
          <img :src="images[1]" alt="긴장 완화 이미지" />
        </div>
      </div>
      <!-- 세 번째 콘텐츠 박스 -->
      <div v-if="currentIndex === 2" class="content-box">
        <div class="content-description">
          <h2>모의 면접 녹화본 제공</h2>
          <p>
            자신의 문제점과 불필요한 행동을 파악하여 빠르게 수정할 수 있도록
            도와드립니다.
          </p>
        </div>
        <div class="content-image">
          <!-- 세 번째 이미지 -->
          <img :src="images[2]" alt="면접 준비 이미지" />
        </div>
      </div>
    </div>
    <ScrollUpAnimation class="scrollupanimation" @click="goToUp" />
  </div>
</template>

<script>
import AOS from "aos";
import image1 from "@/assets/images/fixed/in.jpg"; // 첫 번째 이미지
import image2 from "@/assets/images/fixed/dc.jpg"; // 두 번째 이미지
import image3 from "@/assets/images/fixed/cam.jpg"; // 세 번째 이미지
import ScrollUpAnimation from "./ScrollUpAnimation.vue";
import "aos/dist/aos.css";
import { defineComponent, ref, getCurrentInstance, onMounted } from "vue";
export default defineComponent({
  name: "HomeSix",
  components: {
    ScrollUpAnimation,
  },
  setup() {
    const { emit } = getCurrentInstance();
    const images = [image1, image2, image3];
    const currentIndex = ref(0);
    function goToUp() {
      emit("scroll-to-home");
    }
    function changeContent() {
      setInterval(() => {
        currentIndex.value = (currentIndex.value + 1) % 3; // currentIndex를 0, 1, 2로 순차적으로 변경
      }, 4000);
    }
    onMounted(() => {
      changeContent();
    });

    return {
      images,
      currentIndex,
      changeContent,
      goToUp,
    };
  },
});
</script>

<style scoped>
/* 페이지 전체 틀 및 백그라운드 이미지 */
.home-six {
  width: 100%;
  min-height: 100vh; /* 페이지가 적어도 전체 화면을 덮도록 설정 */
  background: url("@/assets/images/fixed/home_bg2.jpg") center center;
  background-size: cover; /* 배경 이미지 크기를 화면 크기에 맞추어 조정 */
  background-attachment: fixed; /* 배경 이미지를 고정하여 스크롤 시에도 배경이 고정되도록 설정 */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 240px 30px; /* 여백을 2배로 늘림 (원래 120px에서 240px로) */
  box-sizing: border-box; /* 패딩을 포함한 크기 계산 */
}
.intro-text {
  color: #333; /* 색상 변경 (진한 회색) */
  font-size: 2rem; /* 글씨 크기 */
  text-align: center;
  margin-bottom: 20px; /* 하단 여백 */
}
h1 {
  color: #333;
  font-size: 3rem; /* 글씨 크기 */
  font-weight: bold;
  margin-bottom: 20px; /* 하단 여백 */
  margin-top: 10px; /* 상단 여백을 살짝 추가 */
  text-align: center;
}
.content-container {
  position: relative;
  width: 80%; /* 큰 직사각형의 너비 */
  height: 400px; /* 직사각형의 높이 */
  overflow: hidden; /* 자식 요소가 직사각형 밖으로 나가지 않도록 */
}
.content-box {
  width: 100%; /* 한 콘텐츠 박스가 전체 영역을 차지하도록 설정 */
  height: 100%; /* 콘텐츠 박스의 높이를 부모 높이와 동일하게 설정 */
  padding: 15px;
  box-sizing: border-box;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
  display: flex;
  flex-direction: row; /* 텍스트와 이미지를 가로로 배치 */
  gap: 20px;
  position: absolute; /* 각 콘텐츠가 겹치지 않도록 위치를 절대값으로 설정 */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  transition: opacity 1s ease-in-out; /* 1초간 페이드 인/아웃 효과 */
  justify-content: center; /* 가운데 정렬을 위해 추가 */
  align-items: center; /* 수직 가운데 정렬을 위해 추가 */
}
.content-description {
  width: 50%; /* 왼쪽 절반은 글씨 영역 */
  font-size: 18px; /* 글씨 크기 살짝 키움 */
  color: #333;
  display: flex;
  flex-direction: column;
  justify-content: center; /* 세로 중앙 정렬 */
  text-align: center; /* 텍스트를 가운데 정렬 */
}
.content-description h2 {
  font-size: 1.8rem; /* 제목 크기 살짝 키움 */
  margin-bottom: 10px;
}
.content-image {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100px;  /* 강제로 영역 확보 */
}
.scrollupanimation {
  position: absolute;
  bottom: 7vh;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 6s ease 0s infinite;
  animation-delay: 5s;
}
.content-image img {
  display: block;  /* 추가 */
  width: 100%;
  height: auto;
  max-height: 250px;
  object-fit: contain;
}
/* 반응형 웹 디자인: 화면이 좁을 경우 레이아웃을 자동으로 변경 */
@media (max-width: 768px) {
  .content-container {
    width: 100%;
    height: auto;
  }
  .content-box {
    position: static !important;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: auto !important;
    padding: 15px;
  }
  .content-description,
  .content-image {
    width: 100%;
    text-align: center;
  }
  .content-image {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100px;
  }
  .content-image img {
    display: block;
    width: 90%;
    height: auto;
    max-height: 250px;
    object-fit: contain;
    border: 1px solid red; /* 디버깅용 */
  }
}

</style>
