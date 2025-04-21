<template>
  <div class="home-container">
    <div class="text-container">
      <transition name="fade-down">
        <div v-if="showElements" class="home-icon"></div>
      </transition>
      <div style="margin-bottom: 10px"></div>

      <h2 class="title typing-animation">
        <p style="text-transform: none; font-size: 56px">
          &nbsp;
          <!-- &nbsp은 공백을 의미,대신 줄바꿈은 일어나지 않음-->
          <span style="color: black; font-weight: bold"
            >{{ typedText }}&nbsp;
          </span>
        </p>
        <div style="margin-bottom: 10px"></div>
        <p class="subtitle" style="color: black">SINCE 2025</p>
        <div style="margin-bottom: 24px"></div>
      </h2>

      <!-- 메인화면의 있는 글씨를 나타냄-->
      <transition name="fade-down">
        <p v-if="showElements" class="description" style="color: black">
          JOBSTICK은 한국 IT 기업 분석 보고서와 AI 모의면접 서비스를 제공하여
          <br />
          보다 많은 사람들에게 양질의 정보를 공유하고 도움을 드릴 수 있도록
          최선을 다하겠습니다.
        </p>
      </transition>
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

    onMounted(() => {
      typeText();
    });

    return {
      fullText,
      typedText,
      typeIndex,
      showElements,

      goToHomeSecond,
      typeText,
    };
  },
});
</script>

<!--선언한 class들 모음-->
<style scoped>
/* 홈화면 설정*/
.home-container {
  width: 100%; /*너비*/
  max-width: 100vw; /*너비*/
  height: 100vh; /*높이*/
  display: flex; /*flexbox레이아웃 모델 사용*/
  justify-content: center; /*수평 중앙*/
  align-items: center; /*수직 중앙앙*/
  text-align: center; /*텍스트 수평 중앙앙*/
  overflow: hidden; /*콘텐츠가 영역을 벗어나면 안보이도록 설정*/
  position: relative;
  background: url("@/assets/images/fixed/home_bg2.jpg") center center;
  /*배경이미지가 반복 되지 않도록 설정, 즉 남는 공간 발생 시 이미지가 다시 생성되는 것을 막음*/
  background-size: cover;
  background-attachment: fixed;
}

/*read more나타내는 설정*/
.scrollanimation {
  position: absolute;
  bottom: 8vh;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 6s ease 0s infinite;
  animation-delay: 5s;
}

/*홈 화면에 있는 로고 설정*/
.home-icon {
  height: 130px;
  background-image: url("@/assets/images/fixed/logo1.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

/*문자 크기 설정*/
.text-container {
  width: 80vw;
  padding: 20px;
}

/*메인화면 들어갈 떄 글씨가 타자치면서 나오는 연출을 의미*/
.typing-animation {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  border-right: 5px solid white;
  animation: typing 2s steps(30), blink 0.5s step-end infinite alternate;
}

/*타이핑 모션*/
@keyframes typing {
  from {
    width: 0; /*여기서부터*/
  }

  to {
    width: 100%; /*여기까지*/
  }
}

/*깜빡이는 모션*/
@keyframes blink {
  from {
    border-color: transparent;
  }

  to {
    border-color: white;
  }
}

/*fade-down 시작상태(처음 적용)*/
.fade-down-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}

/*fade-down 애니매이션 적용중*/
.fade-down-enter-active {
  transition: all 0.8s ease-out;
}

/*fade-down 최종상태*/
.fade-down-enter-to {
  opacity: 1;
  transform: translateY(0);
}

/*SINCE 2025크기 설정*/
.subtitle {
  font-size: 24px;
  font-weight: bold;
}

/*설명글 크기 설정*/
.description {
  font-size: 18px;
  color: #ffffff;
  margin-top: 10vh;
}

/*모바일적용 */
@media screen and (max-width: 768px) {
  .home-container {
    background-position: center;
    background-size: cover;
  }

  .home-icon {
    height: 80px; /* 줄임 */
  }

  .text-container {
    width: 90vw;
    padding: 10px;
  }

  .typing-animation p {
    font-size: 32px !important;
  }

  .subtitle {
    font-size: 18px;
  }

  .description {
    font-size: 16px;
    margin-top: 5vh;
  }

  .scrollanimation {
    bottom: 5vh;
  }
}
</style>
