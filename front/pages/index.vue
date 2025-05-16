<template>
  <div id="Home_main">
    <!-- ✅ 설문조사 팝업 컴포넌트 -->
    <SurveyPopup />

    <section id="HomeMain" class="section white-bg">
      <HomeMain @scroll-to-home-second="goToHomeSecond" />

      <!-- ✅ 요금제 보기 버튼 추가 -->
      <div style="margin-top: 24px;">
        <button @click="goToMembership" style="padding: 10px 20px; font-size: 16px;">
          요금제 보기
        </button>
      </div>
    </section>

    <section id="HomeSecond" class="section gray-bg">
      <HomeSecond />
    </section>

    <section id="HomeThird" class="section white-bg">
      <HomeThird />
    </section>

    <section id="HomeFour" class="section gray-bg">
      <HomeFour />
    </section>

    <section id="HomeFive" class="section white-bg">
      <HomeFive />
    </section>

    <section id="HomeSix" class="section gray-bg">
      <HomeSix @scroll-to-home="goToUp" />
    </section>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRouter } from 'vue-router';
import HomeMain from "@/components/HomeMain.vue";
import HomeSecond from "@/components/HomeSecond.vue";
import HomeThird from "@/components/HomeThird.vue";
import HomeFour from "@/components/HomeFour.vue";
import HomeFive from "@/components/HomeFive.vue";
import HomeSix from "@/components/HomeSix.vue";
import SurveyPopup from "@/components/SurveyPopup.vue"; // ✅ 팝업 추가

export default defineComponent({
  components: {
    HomeMain,
    HomeSecond,
    HomeThird,
    HomeFour,
    HomeFive,
    HomeSix,
    SurveyPopup, // ✅ 팝업 등록
  },
  setup() {
    const router = useRouter();

    function goToHomeSecond() {
      if (event) event.preventDefault();

      const element = document.getElementById("HomeSecond");
      if (element) {
        const offset = 50;
        const elementPosition =
          element.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - offset;

        requestAnimationFrame(() => {
          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth",
          });
        });
      }
    }

    function goToUp() {
      if (event) event.preventDefault();

      const element = document.getElementById("HomeMain");
      if (element) {
        const offset = 50;
        const elementPosition =
          element.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - offset;

        requestAnimationFrame(() => {
          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth",
          });
        });
      }
    }

    function goToMembership() {
      console.log("✅ [요금제 보기] 버튼 클릭됨")
      router.push('/membership');
    }

    return {
      goToHomeSecond,
      goToUp,
      goToMembership
    };
  },
});
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 공통 섹션 스타일 */
.section {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ✅ 섹션별 배경색 구분 */
.white-bg {
  background-color: #ffffff; /* 하얀색 */
}

.gray-bg {
  background-color: #f5f5f5; /* 연한 회색 */
}

/* GO TOP 버튼 */
.go-top-btn {
  position: fixed;
  bottom: 100px;
  right: 20px;
  font-size: 24px;
  background-color: transparent;
  border: none;
  color: #444;
  cursor: pointer;
  z-index: 1000;
  opacity: 0.8;
  transition: all 0.2s ease;
}

.go-top-btn:hover {
  transform: scale(1.2);
  color: #000;
  opacity: 1;
}
</style>
