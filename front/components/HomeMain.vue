<template>
  <div class="home-container">
    <div class="text-container">
      <transition name="fade-down">
        <div v-if="showElements" class="home-icon"></div>
      </transition>

      <h2 class="title typing-animation">
        <p style="text-transform: none; font-size: 48px; text-align: left">
          <span style="color: black; font-weight: bold">
            {{ typedText }}
          </span>
        </p>
        <p class="subtitle" style="color: black; text-align: left">
          SINCE 2025
        </p>
      </h2>

      <!-- 설문조사 하러가기 버튼 -->
      <transition name="fade-down">
        <div v-if="showElements" class="survey-button">
          <v-btn color="primary" @click="goToSurvey">설문조사 하러가기</v-btn>
        </div>
      </transition>

      <!-- 설명글 -->
      <transition name="fade-down">
        <p
          v-if="showElements"
          class="description"
          style="color: black; text-align: left"
        >
          JOBSTICK은 한국 IT 기업 분석 보고서와 AI 모의면접 서비스를 제공하여
          <br />
          보다 많은 사람들에게 양질의 정보를 공유하고 도움을 드릴 수 있도록
          최선을 다하겠습니다.
        </p>
      </transition>
    </div>

    <!-- 아이폰 이미지 -->
    <div class="image-container" v-if="showElements">
      <img
        src="@/assets/images/fixed/ph1.png"
        alt="iPhone Interview"
        class="iphone-image"
      />
    </div>

    <ScrollAnimation
      class="scrollanimation"
      v-if="showElements"
      @click="goToHomeSecond"
    />
  </div>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";
import {
  defineComponent,
  getCurrentInstance,
  onMounted,
  nextTick,
  ref,
} from "vue";
import ScrollAnimation from "./ScrollAnimation.vue";

export default defineComponent({
  name: "HomeMain",
  components: {
    ScrollAnimation,
  },
  setup() {
    const fullText = ref("USE YOUR JOBSTICK!");
    const typedText = ref("");
    const typeIndex = ref(0);
    const showElements = ref(false);
    const message = ref(""); // ✅ Go 응답 메시지 상태
    const { emit } = getCurrentInstance();

    function typeText() {
      if (typeIndex.value < fullText.value.length) {
        typedText.value += fullText.value.charAt(typeIndex.value);
        typeIndex.value++;
        setTimeout(typeText, 80);
      } else {
        showElements.value = true;
        nextTick(() => {
          AOS.refresh();
        });
      }
    }

    function goToHomeSecond() {
      emit("scroll-to-home-second");
    }

    function goToSurvey() {
      window.open(
        "https://docs.google.com/forms/d/e/1FAIpQLSep5cE1W5SzDzAyZmjC30YKuRiJrIiZQCTgo5hu4HiU_NjyiA/viewform"
      );
    }

    onMounted(() => {
      typeText();
    });

    return {
      fullText,
      typedText,
      typeIndex,
      showElements,
      goToHomeSecond,
      goToSurvey,
      typeText,
      message, // ✅ 등록
    };
  },
});
</script>

<style scoped>
.home-container {
  width: 100%;
  max-width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  overflow: hidden;
  position: relative;
  padding: 0 5%;
  background-color: #ffffff;
  background-size: cover;
  background-attachment: fixed;
}

.text-container {
  width: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.image-container {
  width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* ✅ 수정된 iphone-image */
.iphone-image {
  width: 90%;
  max-width: 400px;
  height: auto;
  transform: rotate(-5deg);
  /* box-shadow 삭제 */
  /* border-radius 삭제 */
  /* background-color 삭제 */
}

.survey-button {
  margin: 20px 0;
  text-align: left;
}

.scrollanimation {
  position: absolute;
  bottom: 8vh;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 6s ease 0s infinite;
  animation-delay: 5s;
}

.typing-animation {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  border-right: 5px solid white;
  animation: typing 2s steps(30), blink 0.5s step-end infinite alternate;
}

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

@keyframes blink {
  from {
    border-color: transparent;
  }
  to {
    border-color: white;
  }
}

.fade-down-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}

.fade-down-enter-active {
  transition: all 0.8s ease-out;
}

.fade-down-enter-to {
  opacity: 1;
  transform: translateY(0);
}

.subtitle {
  font-size: 24px;
  font-weight: bold;
  margin-top: 10px;
}

.description {
  font-size: 18px;
  margin-top: 20px;
}

@media screen and (max-width: 768px) {
  .home-container {
    flex-direction: column;
    padding: 20px;
  }

  .text-container,
  .image-container {
    width: 100%;
    text-align: center;
  }

  .iphone-image {
    margin-top: 20px;
    transform: rotate(0deg);
  }

  .survey-button {
    text-align: center;
  }
}
</style>
