<template>
  <div class="home-second">
    <div class="home-second-body">
      <div class="title-container">
        <p
          data-aos="fade-up"
          data-aos-offset="400 "
          style="white-space: nowrap"
        >
          <span class="NOODLE-span">JOBSTICK</span> | 기업 핵심 정보 분석 및 AI
          모의면접
        </p>
      </div>
      <div class="content-area">
        <div class="content-container">
          <div class="content-title" data-aos="fade-up" data-aos-offset="400">
            <p><span class="NOODLE-span">JOBSTICK</span></p>
            <p>팀원을 소개합니다.</p>
          </div>
          <div class="image-container">
            <div class="image-card-container">
              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="100"
                data-aos-offset="400"
              >
                <div class="image-card">
                  <v-img src="@/assets/images/fixed/kim.png" cover> </v-img>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="200"
                data-aos-offset="400"
              >
                <div class="image-card">
                  <v-img src="@/assets/images/fixed/choi.jpg" cover> </v-img>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="300"
                data-aos-offset="400"
              >
                <div class="image-card">
                  <v-img src="@/assets/images/fixed/min.jpg" cover> </v-img>
                </div>
              </v-card>
              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="400"
                data-aos-offset="400"
              >
                <div class="image-card">
                  <v-img src="@/assets/images/fixed/yang.jpg" cover> </v-img>
                </div>
              </v-card>
              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="500"
                data-aos-offset="400"
              >
                <div class="image-card">
                  <v-img src="@/assets/images/fixed/wang.jpg" cover> </v-img>
                </div>
              </v-card>
            </div>
          </div>

          <div class="text-container">
            <div class="text-card-container">
              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="100"
                data-aos-offset="400"
              >
                <div class="text-card">
                  <p>이름: 김현우</p>
                  <p>
                    GitHub:<a
                      href="https://github.com/kimhyeonu4586"
                      class="link"
                      >@kimhyeonu4586</a
                    >
                  </p>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="200"
                data-aos-offset="400"
              >
                <div class="text-card">
                  <p>이름: 최병준</p>
                  <p>
                    GitHub:<a
                      href="https://github.com/ChoiByuengJun"
                      class="link"
                      >@ChoiByuengJun</a
                    >
                  </p>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="300"
                data-aos-offset="400"
              >
                <div class="text-card">
                  <p>이름: 오민수</p>
                  <p>
                    GitHub:<a href="https://github.com/yooodleee" class="link"
                      >@yooodleee</a
                    >
                  </p>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="400"
                data-aos-offset="400"
              >
                <div class="text-card">
                  <p>이름: <span style="color: red">[팀장]</span>양의정</p>
                  <p>
                    GitHub:<a href="https://github.com/UiJungYang6" class="link"
                      >@UiJungYang</a
                    >
                  </p>
                </div>
              </v-card>

              <v-card
                data-aos="fade-up"
                data-aos-anchor=".content-title"
                data-aos-delay="500"
                data-aos-offset="400"
              >
                <div class="text-card">
                  <p>이름: 왕환민</p>
                  <p>
                    GitHub:<a href="https://github.com/minleewang" class="link"
                      >@minleewang</a
                    >
                  </p>
                </div>
              </v-card>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";
import { defineComponent, onMounted, onBeforeUnmount, ref } from "vue";

export default defineComponent({
  name: "HomeSecond",
  setup() {
    onMounted(() => {
      AOS.init({
        duration: 1000,
        once: false,
      });
    });
  },
});
</script>

<style scoped>
/*페이지 전체 틀 및 백그라운드 사진*/
.home-second {
  width: 100%;
  height: 100vh;
  background: url("@/assets/images/fixed/home_bg2.jpg") center center;
  background-size: cover;
  background-attachment: fixed;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/*이미지들 크기 통제*/
.home-second-body {
  width: 70%;
  height: 100%;
}

/*제목*/
.title-container {
  width: 100%;
  height: 15%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  font-size: 4vh;
  font-weight: bold;
  /* padding-bottom: 50px; */
}

/*중앙 배치 영역 통제*/
.content-area {
  width: 100%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  /* padding-bottom: 150px; */
}
/*중앙 컨텐츠 내용 통제*/
.content-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  /* align-items: flex-end; */
  /* justify-content: flex-end; */
  justify-content: center;
  gap: 10px;
}
/*제목*/
.content-title {
  width: 100%;
  height: 10%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 5%;
}
/*제목 스타일*/
.content-title p {
  color: #ffffff;
  font-size: 2.5vh;
  font-weight: bold;
}
/*이미지 틀 크기*/
.image-container {
  width: 100%;
  height: 60%;
}
/*이미지 카드들 영역 관리*/
.image-card-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  gap: 30px;
}

/*이미지가 들어가는 카드 창 관리*/
.v-card {
  width: 40%;
  height: 90%;
  background-color: #877e7e00;
  border: none; /* 테두리 없애기 */
  box-shadow: none;
  overflow: visible;
}

/*들어가는 이미지 관리*/
.image-card {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border-radius: 25px;
}

/*이미지 관리*/
.v-img {
  width: 100%;
  height: 100%;
  transition: transform 0.3s ease;
  border-radius: 25px;
}

.text-container {
  width: 100%;
  height: 60%;
}

.text-card {
  position: relative;
  top: 5%;
  left: 5%;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: visible;
}

.text-card-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  gap: 30px;
}

.image-card:hover .v-img {
  transform: scale(1.05);
}

.NOODLE-span {
  color: rgb(38, 38, 231);
}

.link {
  text-decoration: none; /* 밑줄 제거 */
  color: blue; /* 기본 파란색 제거 (선택사항) */
  font-weight: bold; /* 글자 강조 (선택사항) */
}
</style>
