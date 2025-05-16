<template>
  <a class="scroll" href="#">Read more</a>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ScrollAnimation",
});
</script>

<style scoped>
*,
*:before,
*:after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.scroll {
  position: relative;
  display: block;
  font-size: 1.5vh;
  color: rgb(0, 0, 0);
  text-decoration: none;
  padding: 1vh 1vh 1vh 4vh;
}

.scroll::before {
  display: block;
  position: absolute;
  top: -0.2vh;
  left: 0;
  width: 2.5vh;
  height: 4vh;
  border: 0.2vh solid rgb(0, 0, 0);
  border-radius: 1.2vh;
  content: "";
}

.scroll::after {
  display: block;
  position: absolute;
  top: 0.9vh;
  left: 1.1vh;
  width: 0.2vh;
  height: 0.8vh;
  background: rgb(0, 0, 0);
  border-radius: 0.1vh;
  content: "";
  animation-name: scroll;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: 2s;
}

@keyframes scroll {
  0% {
    opacity: 1;
    height: 0.8vh;
  }

  20% {
    opacity: 1;
    height: 0.8vh;
  }

  30% {
    transform: translateY(0);
    opacity: 1;
    height: 1.9vh;
  }

  40% {
    opacity: 1;
  }

  80% {
    transform: translateY(1.9vh);
    opacity: 0;
    height: 0;
  }

  81% {
    transform: translateY(0);
    opacity: 0;
    height: 0.8vh;
  }

  100% {
    opacity: 1;
    height: 0.8vh;
  }
}

/* 미디어 쿼리는 필요한 경우에만 미세 조정을 위해 사용 */
@media (max-width: 768px) {
  .scroll {
    font-size: 1.8vh;
  }
}

@media (max-width: 480px) {
  .scroll {
    font-size: 2vh;
  }
}
</style>
