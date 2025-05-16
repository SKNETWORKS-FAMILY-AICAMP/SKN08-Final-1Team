<template>
  <div class="home-four">
    <!-- h1 아래에 작은 텍스트 추가 -->
    <h1>면접 준비가 어렵고 막막하신 분들?</h1>

    <!-- 컨테이너로 사진과 설명을 정렬 -->
    <div class="content-container">
      <!-- 설명 왼쪽 3개 (지금은 오른쪽을 향하게 설정) -->
      <div class="description-container right">
        <div class="description">
          <h2>회사를 어떻게 조사해야 할지 모르겠어요</h2>
        </div>
        <div class="description">
          <h2>면접 중에 지나치게 긴장해서 머리가 하얗게 될까 걱정이에요</h2>
        </div>
        <div class="description">
          <h2>면접을 준비하기 막막해요</h2>
        </div>
        <div class="description">
          <h2>예상 질문을 예측하기 어려워요</h2>
        </div>
      </div>

      <!-- 가운데 이미지 -->
      <div class="image-container">
        <img :src="imageSrc" alt="부적 이미지" />
      </div>

      <!-- 설명 오른쪽 3개 (지금은 왼쪽을 향하게 설정) -->
      <div class="description-container left">
        <div class="description">
          <h2>어떤 질문이 나올지 두려워요</h2>
        </div>
        <div class="description">
          <h2>필요한 피드백을 받아보고 싶어요</h2>
        </div>
        <div class="description">
          <h2>면접 중에 말을 잘못하거나 말실수를 할까 봐 두려워요</h2>
        </div>
        <div class="description">
          <h2>
            직장, 학업, 일상 생활 등 다른 일들로 면접 준비를 할 시간이 부족해요
          </h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import imageSrc from "@/assets/images/fixed/sc.png"; // 이미지 경로를 import로 불러옵니다.

export default {
  name: "HomeFour",
  data() {
    return {
      imageSrc, // 가져온 이미지 경로를 데이터로 사용
    };
  },
};
</script>

<style scoped>
/* 페이지 전체 틀 및 백그라운드 이미지 */
.home-four {
  width: 100%;
  min-height: 100vh; /* 페이지가 적어도 전체 화면을 덮도록 설정 */
  background-size: cover; /* 배경 이미지 크기를 화면 크기에 맞추어 조정 */
  background-attachment: fixed; /* 배경 이미지를 고정하여 스크롤 시에도 배경이 고정되도록 설정 */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 140px 30px; /* 여백을 좁혀서 요소들을 더 가깝게 만듦 */
  box-sizing: border-box; /* 패딩을 포함한 크기 계산 */
}

.intro-text {
  color: #666; /* 색상 변경 */
  font-size: 2rem;
  font-weight: bold; /* 글씨 크기 */
  text-align: center;
  margin-bottom: 15px; /* 하단 여백을 조금 더 좁힘 */
}

h1 {
  color: #333;
  font-size: 2.5rem; /* 글씨 크기 축소 */
  font-weight: bold;
  margin-bottom: 15px; /* 하단 여백을 줄임 */
  margin-top: 0px; /* 상단 여백을 없앰 */
  text-align: center;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap; /* 화면 크기에 따라 자동 배치 */
  gap: 10px; /* 간격을 더 좁혀서 가까워지도록 */
  margin-top: 100px; /* 설명과 좀 더 가까워지도록 상단 여백을 축소 */
  margin-bottom: 120px; /* 하단 여백을 좀 더 좁힘 */
}

.description-container {
  display: flex;
  flex-direction: column;
  gap: 10px; /* 간격을 줄여서 가까워지도록 */
  width: 30%; /* 크기 설정을 조금 더 키움 */
  position: relative;
  padding: 0 10px; /* 왼쪽, 오른쪽 패딩을 줄여서 간격을 더 가깝게 설정 */
  box-sizing: border-box; /* 패딩을 포함한 크기 계산 */
}

/* 오른쪽 설명 칸에 말풍선 스타일 */
.description-container.left .description {
  background-color: #fff;
  padding: 16px; /* 패딩을 조금 줄임 */
  border-radius: 12px; /* 둥근 모서리 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1); /* 그림자 */
  position: relative;
  font-size: 15px; /* 글씨 크기 조금 줄임 */
  color: #333;
}

.description-container.left .description::after {
  content: "";
  position: absolute;
  top: 50%;
  left: -10px; /* 왼쪽으로 삼각형 배치 */
  transform: translateY(-50%);
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 12px solid #fff; /* 삼각형 크기 */
}

/* 왼쪽 설명 칸에 말풍선 스타일 */
.description-container.right .description {
  background-color: #fff;
  padding: 14px; /* 패딩을 더 줄임 */
  border-radius: 12px; /* 둥근 모서리 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1); /* 그림자 */
  position: relative;
  font-size: 15px; /* 글씨 크기 더 줄임 */
  color: #333;
}

.description-container.right .description::before {
  content: "";
  position: absolute;
  top: 50%;
  right: -10px; /* 오른쪽으로 삼각형 배치 */
  transform: translateY(-50%);
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  border-top: 12px solid #fff; /* 삼각형 크기 */
}

/* 설명 제목 스타일 */
.description h2 {
  margin-bottom: 6px; /* 하단 마진을 더 좁힘 */
}

.image-container {
  width: 30%; /* 이미지 크기를 조금 더 넓힘 */
  height: auto; /* 높이 자동 */
  display: flex;
  justify-content: center;
  align-items: center; /* 이미지가 중앙에 위치하도록 설정 */
  position: relative;
  padding: 0 10px; /* 왼쪽, 오른쪽 패딩을 줄여서 간격을 더 가깝게 설정 */
  box-sizing: border-box; /* 패딩을 포함한 크기 계산 */
}

.image-container img {
  width: 100%; /* 이미지 크기를 칸 크기에 맞추기 */
  height: auto; /* 이미지 비율을 유지 */
  object-fit: contain; /* 이미지가 비율을 유지하면서 잘리지 않게 설정 */
  border-radius: 0; /* 테두리 제거 */
  box-shadow: none; /* 그림자 제거 */
}

/* 반응형 웹 디자인: 화면이 좁을 경우 레이아웃을 자동으로 변경 */
@media (max-width: 768px) {
  .content-container {
    flex-direction: column;
    align-items: center;
  }

  .description-container,
  .image-container {
    width: 100%; /* 작은 화면에서는 각 요소가 전체 너비를 차지하도록 */
    padding: 0 20px; /* 작은 화면에서 왼쪽, 오른쪽 여백을 조금 더 추가 */
  }

  .image-container img {
    max-width: 100%; /* 이미지 크기 제한 */
  }
}
</style>
