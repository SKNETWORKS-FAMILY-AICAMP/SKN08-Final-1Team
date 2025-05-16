<template>
  <!-- 스크롤 올리기 버튼 -->
  <a class="scroll" href="#" @click.prevent="scrollToTop">Go Top</a>
</template>

<script></script>

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
  padding: 5.5vh 1vh 6vh 4vh; /* 기존 코드와 동일한 간격 */
  display: flex;
  flex-direction: column; /* 세로 정렬 유지 */
  align-items: center;
  gap: 0.9vh; /* 기존 코드의 요소 간 간격 반영 */
}

.scroll::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 20%;
  width: 0;
  height: 0;
  border-left: 1vh solid transparent;
  border-right: 1vh solid transparent;
  border-bottom: 1.5vh solid rgb(0, 0, 0);
  transform: translate(-50%, -50%);
  animation: bounce 1.5s infinite;
}

/* 애니메이션 */
@keyframes bounce {
  0%,
  100% {
    transform: translate(-50%, -50%) translateY(0);
  }
  50% {
    transform: translate(-50%, -50%) translateY(-0.5vh);
  }
}

@media (max-width: 768px) {
  .scroll {
    width: 10h;
    height: 15vh;
    font-size: 1.5vh;
    padding: 8vh 1vh 6vh 5vh;
  }

  .scroll::before {
    border-left: 1.2vh solid transparent;
    border-right: 1.2vh solid transparent;
    border-bottom: 1.8vh solid rgb(0, 0, 0);
  }
}

@media (max-width: 480px) {
  .scroll {
    width: 15vh;
    height: 20vh;
    font-size: 2vh;
    padding: 8vh 1vh 6vh 5vh;
  }

  .scroll::before {
    border-left: 1.4vh solid transparent;
    border-right: 1.4vh solid transparent;
    border-bottom: 2vh solid rgb(0, 0, 0);
  }
}
</style>
