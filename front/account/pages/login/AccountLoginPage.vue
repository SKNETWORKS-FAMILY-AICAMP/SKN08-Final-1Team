<template>
  <v-container class="container">
    <div class="login-wrapper">
      <div>
        <div class="login_logo"></div>
        <div class="introduction" style="color: black">
          <p>
            기업 분석과&nbsp;AI 모의면접&nbsp;|&nbsp;취업 준비는
            <b>JOBSTICK</b>에서
          </p>
        </div>
        <v-divider class="mt-5 mb-7" :thickness="3"></v-divider>

        <!-- 카카오 로그인 버튼 클릭 시 개인정보 동의 페이지로 이동 -->
        <v-btn class="kakao-login-btn" @click="goToPrivacyAgreementPage">
          <!-- 카카오 로그인 -->
        </v-btn>

        <v-btn class="google-login-btn" @click="goToGoogleLogin">
          <!-- Google 로그인 -->
        </v-btn>

        <v-btn class="naver-login-btn" @click="goToNaverLogin">
          <!-- 네이버 로그인 -->
        </v-btn>

        <v-btn class="admin-login-btn" @click="goToAdminLogin" block>
          관리자 로그인
        </v-btn>
      </div>
    </div>
  </v-container>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useKakaoAuthenticationStore } from "../../../kakaoAuthentication/stores/kakaoAuthenticationStore";
import { useGoogleAuthenticationStore } from "../../../googleAuthentication/stores/googleAuthenticationStore";
import { useNaverAuthenticationStore } from "../../../naverAuthentication/stores/naverAuthenticationStore";

// Vue Router
const router = useRouter();

// Pinia Store
const kakaoAuthentication = useKakaoAuthenticationStore();
const googleAuthentication = useGoogleAuthenticationStore();
const naverAuthentication = useNaverAuthenticationStore();

// 개인정보 동의 페이지로 이동
const goToPrivacyAgreementPage = () => {
  router.push("/account/privacy");
};

// 로그인 함수들
const goToGoogleLogin = async () => {
  localStorage.setItem("loginType", "GOOGLE");
  try {
    // 구글 로그인 요청
    const response = await googleAuthentication.requestGoogleLoginToDjango();
    if (response.success) {
      // 로그인 성공 시 이동할 페이지
      router.push("/dashboard");
    } else {
      // 로그인 실패 처리
      console.error("Google login failed", response.error);
    }
  } catch (error) {
    console.error("Error during Google login:", error);
  }
};

const goToKakaoLogin = async () => {
  localStorage.setItem("loginType", "KAKAO");
  try {
    // 카카오 로그인 요청
    const response = await kakaoAuthentication.requestKakaoLoginToDjango();
    if (response.success) {
      // 로그인 성공 시 이동할 페이지
      router.push("/dashboard");
    } else {
      // 로그인 실패 처리
      console.error("Kakao login failed", response.error);
    }
  } catch (error) {
    console.error("Error during Kakao login:", error);
  }
};

const goToNaverLogin = async () => {
  localStorage.setItem("loginType", "NAVER");
  try {
    // 네이버 로그인 요청
    const response = await naverAuthentication.requestNaverLoginToDjango();
    if (response.success) {
      // 로그인 성공 시 이동할 페이지
      router.push("/dashboard");
    } else {
      // 로그인 실패 처리
      console.error("Naver login failed", response.error);
    }
  } catch (error) {
    console.error("Error during Naver login:", error);
  }
};

const goToAdminLogin = () => {
  router.push("/account/admin-code");
};
</script>

<style scoped>
.container {
  max-width: 100vw;
  height: 110vh;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  background-color: white;
  background: url("@/assets/images/fixed/login_bg6.jpg") no-repeat center center;
  background-size: contain;
}

.login_logo {
  height: 20vh;
  margin-bottom: -2vh;
  overflow: hidden;
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
  overflow: hidden;
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
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ffea00;
  margin-bottom: 1vh;
  border-radius: 1.4vh;
}

.google-login-btn {
  background-image: url("@/assets/images/fixed/btn_login_google.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  margin-bottom: 1vh;
  border-radius: 1.4vh;
}

.naver-login-btn {
  background-image: url("@/assets/images/fixed/btn_login_naver.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
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
  cursor: pointer;
}
</style>
