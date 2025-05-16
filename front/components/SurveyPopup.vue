<template>
  <div
    v-if="visible"
    class="popup-container animate__animated animate__shakeX"
    ref="popupRef"
    @mousedown="startDrag"
  >
    <v-card elevation="12" class="popup-card">
      <!-- ✅ 상단 쿠폰 이미지 -->
      <div class="popup-coupon-image">
        <img src="@/assets/images/fixed/coupon.png" alt="쿠폰 이미지" />
      </div>

      <v-card-title class="popup-title">
        🎁 설문조사 이벤트
      </v-card-title>

      <v-card-text class="popup-text">
        안녕하세요!<br /><br />
        JOBSTICK 팀이 준비한 깜짝 이벤트!<br /><br />
        간단한 설문에 참여해주시면<br />
        <strong>추첨을 통해 총 5분께</strong><br />
        <strong>메머드 커피 기프티콘</strong>을 드려요 ☕🎉<br /><br />
        지금 바로 참여해보세요!
      </v-card-text>

      <v-card-actions class="popup-actions">
        <v-btn color="grey" variant="elevated" size="small" class="btn-today pulse-hover" @click="dontShowToday">
          오늘 하루 보지 않기
        </v-btn>
        <v-btn color="primary" variant="elevated" size="small" class="btn-close pulse-hover" @click="visible = false">
          닫기
        </v-btn>
        <v-btn color="red" variant="elevated" size="small" class="btn-submit pulse-hover" @click="goToSurvey">
          참여하기
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

const visible = ref(false);
const popupRef = ref<HTMLElement | null>(null);
let isDragging = false;
let offsetX = 0;
let offsetY = 0;

function getTodayKey(): string {
  const today = new Date();
  return today.toISOString().split("T")[0];
}

function dontShowToday() {
  const today = getTodayKey();
  localStorage.setItem("hideSurveyPopupUntil", today);
  visible.value = false;
}

onMounted(() => {
  const today = getTodayKey();
  const stored = localStorage.getItem("hideSurveyPopupUntil");

  if (stored === today) return;

  setTimeout(() => {
    visible.value = true;
  }, 1000);

  document.addEventListener("mousemove", onDrag);
  document.addEventListener("mouseup", stopDrag);
});

const startDrag = (e: MouseEvent) => {
  if (popupRef.value) {
    isDragging = true;
    offsetX = e.clientX - popupRef.value.offsetLeft;
    offsetY = e.clientY - popupRef.value.offsetTop;
  }
};

const onDrag = (e: MouseEvent) => {
  if (isDragging && popupRef.value) {
    popupRef.value.style.left = `${e.clientX - offsetX}px`;
    popupRef.value.style.top = `${e.clientY - offsetY}px`;
  }
};

const stopDrag = () => {
  isDragging = false;
};

const goToSurvey = () => {
  visible.value = false;
  window.open(
    "https://docs.google.com/forms/d/e/1FAIpQLSep5cE1W5SzDzAyZmjC30YKuRiJrIiZQCTgo5hu4HiU_NjyiA/viewform",
    "_blank"
  );
};
</script>

<style scoped>
@import 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css';

/* 💻 웹 기본 위치 */
.popup-container {
  position: fixed;
  top: 14%;
  left: 45%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  cursor: move;
  padding: 16px;
}

/* 📱 모바일 화면에서 위치 중앙으로 */
@media (max-width: 600px) {
  .popup-container {
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

.popup-card {
  width: 90vw;
  max-width: 320px;
  background: #ffffff;
  color: #0d47a1;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  user-select: none;
  padding: 16px 0 8px 0;
  background-repeat: no-repeat;
  background-position: center bottom;
  background-size: contain;
}

.popup-coupon-image {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 12px;
  margin-bottom: 8px;
}

.popup-coupon-image img {
  width: 120px;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.popup-icon {
  display: none;
}

.popup-title {
  text-align: center;
  color: #d32f2f;
  font-weight: bold;
  font-size: 22px;
}

.popup-text {
  text-align: center;
  font-size: 14px;
  color: #333;
  margin: 0 12px;
}

.popup-actions {
  display: flex;
  justify-content: space-around;
  margin-top: 8px;
}

/* 버튼 스타일 */
.btn-today {
  border-bottom: 2px solid grey;
}

.btn-close {
  border-bottom: 2px solid #1976d2;
}

.btn-submit {
  border-bottom: 2px solid red;
}

/* 호버 애니메이션 */
.pulse-hover:hover {
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

/* 📱 모바일 화면에서 위치를 더 위로 조정 */
@media (max-width: 600px) {
  .popup-container {
    top: 30%;
    left: 10%;
    transform: translate(-50%, -50%);
  }

  .popup-card {
    width: 90vw;
    max-width: 320px;
  }

  .popup-coupon-image img {
    width: 100px;
  }

  .popup-title {
    font-size: 18px;
  }

  .popup-text {
    font-size: 13px;
    margin: 0 8px;
  }

  .popup-actions {
    flex-direction: column;
    align-items: center;
    gap: 6px;
    margin-top: 12px;
  }
}
</style>