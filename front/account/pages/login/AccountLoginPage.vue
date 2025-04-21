<template>
  <v-container class="container">
    <div class="login-wrapper">
      <div>
        <div class="login_logo"></div>
        <div class="introduction" style="color: black">
          <p>
            기업 분석과 AI 모의면접 | 취업 준비는 <b>JOBSTICK</b>에서
          </p>
        </div>
        <v-divider class="mt-5 mb-7" :thickness="3"></v-divider>

        <!-- 로그인 버튼들 -->
        <v-btn class="kakao-login-btn" @click="goToPrivacyAgreementPage('KAKAO')"></v-btn>
        <v-btn class="google-login-btn" @click="goToPrivacyAgreementPage('GOOGLE')"></v-btn>
        <v-btn class="naver-login-btn" @click="goToPrivacyAgreementPage('NAVER')"></v-btn>

        <!-- 관리자 로그인 -->
        <v-btn class="admin-login-btn" @click="goToAdminLogin" block>관리자 로그인</v-btn>
      </div>
    </div>
  </v-container>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goToPrivacyAgreementPage = (loginType) => {
  // 로그인 타입을 쿼리로 넘김
  router.push({ path: "/account/privacy", query: { loginType } });
};

const goToAdminLogin = () => {
  router.push("/account/admin-code");
};
</script>

<style scoped>
.container {
  max-width: 100vw;
  min-height: 89vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url("@/assets/images/fixed/login_bg61.jpg") no-repeat center center;
  background-size: 900px auto;
}

.login_logo {
  height: 20vh;
  margin-bottom: -2vh;
  background-image: url("@/assets/images/fixed/logo1.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.login-wrapper {
  position: relative;
  z-index: 1;
  top: 70px;
  width: 50vh;
  height: 70vh;
  background-color: #877e7e00;
  border-radius: 9vh;
  padding: 0vh 10vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.v-btn {
  width: 100%;
  height: 50px;
  margin: 1.3vh auto;
}

.kakao-login-btn {
  background-image: url("@/assets/images/fixed/btn_login_kakao.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-color: #ffea00;
  margin-bottom: 1vh;
  border-radius: 1.4vh;
}

.google-login-btn {
  background-image: url("@/assets/images/fixed/btn_login_google.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-color: #fff;
  margin-bottom: 1vh;
  border-radius: 1.4vh;
}

.naver-login-btn {
  background-image: url("@/assets/images/fixed/btn_login_naver.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  background-color: #03c75a;
  border-radius: 1.4vh;
}

.admin-login-btn {
  width: 100%;
  max-width: 300px;
  height: 50px;
  background-color: #4caf50;
  color: white;
  font-weight: bold;
  border-radius: 1.4vh;
  margin-bottom: 20px;
}
</style>
