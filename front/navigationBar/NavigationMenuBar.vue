<template>
  <v-app-bar color="transparent" app dark height="72" class="menu-bar">
    <v-btn text @click="goToHome" class="navbar-logo-btn">
      <v-img class="home-icon"></v-img>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn text @click="goToHome" class="btn-text"> HOME </v-btn>
    <v-btn
      v-if="
        kakaoAuthenticationStore.isAuthenticated ||
        googleAuthenticationStore.isAuthenticated ||
        naverAuthenticationStore.isAuthenticated
      "
      text
      @click="goToReviewListPage"
      class="btn-text"
    >
      REVIEW
    </v-btn>

    <v-btn text @click="goToProductList" class="btn-text">
      COMPANY REPORT
    </v-btn>
    <v-btn text @click="goToLlmTestPage" class="btn-text"> AI INTERVIEW </v-btn>

    <v-spacer></v-spacer>

    <!-- 로그인 후 화면-->
    <v-menu
      v-if="
        kakaoAuthenticationStore.isAuthenticated ||
        googleAuthenticationStore.isAuthenticated ||
        naverAuthenticationStore.isAuthenticated
      "
      close-on-content-click
    >
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>My Page</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in myPageItems"
          :key="index"
          @click="item.action"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <!--추후 관리자 추가하여 교체예정-->
    <v-menu
      v-if="githubAuthenticationStore.isAuthenticated"
      close-on-content-click
    >
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" class="btn-text" style="margin-right: 14px">
          <b>ADMIN</b>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in adminPageList"
          :key="index"
          @click="item.action"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <!--여기까지-->

    <!--로그인/로그아웃 버튼-->
    <v-btn
      v-if="
        !kakaoAuthenticationStore.isAuthenticated &&
        !googleAuthenticationStore.isAuthenticated &&
        !naverAuthenticationStore.isAuthenticated &&
        !githubAuthenticationStore.isAuthenticated
      "
      text
      @click="signIn"
      class="btn-login"
    >
      <!-- <v-icon left>mdi-login</v-icon> -->
      LOGIN
    </v-btn>

    <v-btn v-else text @click="signOut" class="btn-logout">
      <!-- <v-icon left>mdi-logout</v-icon> -->
      LOGOUT
    </v-btn>
  </v-app-bar>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useKakaoAuthenticationStore } from "~/kakaoAuthentication/stores/kakaoAuthenticationStore";
import { useNaverAuthenticationStore } from "~/naverAuthentication/stores/naverAuthenticationStore";
import { useGoogleAuthenticationStore } from "~/googleAuthentication/stores/googleAuthenticationStore";
import { useGithubAuthenticationStore } from "~/githubAuthentication/stores/githubAuthenticationStore";
import { useAuthenticationStore } from "~/authentication/stores/authenticationStore";
import { useReviewStore } from "~/review/stores/reviewStore";

// Pinia 스토어 사용
const kakaoAuthenticationStore = useKakaoAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();
const githubAuthenticationStore = useGithubAuthenticationStore();
const authenticationStore = useAuthenticationStore();
const reviewStore = useReviewStore();

const router = useRouter();

// 데이터 선언

// 관리자 페이지
const adminPageList = ref([
  {
    title: "사용자 관리",
    action: () => goToManagementUserPage(),
  },
  {
    title: "사용자 로그 현황",
    action: () => goToManagementUserLogList(),
  },
]);

//내페이지 안에 있는 아이템 모음
const myPageItems = ref([
  {
    title: "회원 정보",
    action: () => goToMyPage(),
  },
  {
    title: "장바구니",
    action: () => goToCart(),
  },
  {
    title: "주문 목록",
    action: () => goToOrder(),
  },
]);

const aiInterviewPageList = ref([
  // {
  //   title: "대화형",
  //   action: () => goToAiInterviewPage(),
  // },
  {
    title: "단일 질문 노출형",
    action: () => goToLlmTestPage(),
  },
]);

// 라우터 이동 함수들
const signIn = () => router.push("/account/login"); //로그인 페이지
const goToHome = () => router.push("/"); // 홈 메인페이지
const goToProductList = () => router.push("/companyReport/list"); // company report 페이지
const goToCart = () => router.push("/cart/list"); // 카트페이지
const goToOrder = () => router.push("/order/list"); // 주문내역 페이지
const goToMyPage = () => router.push("/account/mypage"); // 내페이지
const goToReviewListPage = () => router.push("/review/list"); // 리뷰페이지
const goToManagementUserPage = () => router.push("/management/user");
const goToManagementUserLogList = () => router.push("/management/log");
// const goToAiInterviewPage = () => router.push('/ai-interview'); 나중에 확인
const goToLlmTestPage = () => router.push("/ai-interview");

// 로그아웃 처리
const signOut = async () => {
  console.log("로그아웃 클릭");
  const userToken = localStorage.getItem("userToken");
  //const loginType = localStorage.getItem("loginType");
  //console.log(loginType);
  if (userToken != null) {
    authenticationStore.requestLogout(userToken);
  } else {
    console.log("userToken이 없습니다");
  }
  authenticationStore.isAuthenticated = false;
  kakaoAuthenticationStore.isAuthenticated = false;
  naverAuthenticationStore.isAuthenticated = false;
  githubAuthenticationStore.isAuthenticated = false;
  googleAuthenticationStore.isAuthenticated = false;
  localStorage.removeItem("userToken");
  localStorage.removeItem("loginType");
  router.push("/");
};

// 설문조사 페이지 이동
const goToReview = async () => {
  const randomString = await reviewStore.requestRandomStringToDjango();

  if (randomString) {
    router.push({
      name: "reviewReadPage",
      params: { randomString: randomString.toString() },
    });
  }
};

// 사용자 상태 복원
onMounted(async () => {
  const kakaoUserToken = localStorage.getItem("userToken");

  if (kakaoUserToken) {
    const isValid = await kakaoAuthenticationStore.requestValidationUserToken(
      kakaoUserToken
    );
    kakaoAuthenticationStore.isAuthenticated = isValid;
  }

  //const googleUserToken = localStorage.getItem("userToken");
  //if (googleUserToken) {
  //  const isValid = await googleAuthenticationStore.requestValidationUserToken(
  //    googleUserToken
  //  );
  //  googleAuthenticationStore.isAuthenticatedGoogle = isValid;
  //}

  //const naverUserToken = localStorage.getItem("userToken");
  //if (naverUserToken) {
  //  const isValid = await naverAuthenticationStore.requestValidationUserToken(
  //    naverUserToken
  //  );
  //  naverAuthenticationStore.isAuthenticatedNaver = isValid;
  //}

  //const adminToken = localStorage.getItem("adminToken");
  //if (adminToken) {
  //  kakaoAuthenticationStore.isKakaoAdmin = true;
  //  googleAuthenticationStore.isGoogleAdmin = true;
  // naverAuthenticationStore.isNaverAdmin = true;
  //  accountStore.isNormalAdmin = true;
  // }
});
</script>

<style scoped>
.menu-bar {
  background: var(
    --Gradient-Liner-1,
    linear-gradient(94deg, #2a49e5 1.69%, #6751e0 116.61%)
  ) !important;
}

/* 로고 이미지 버튼 */
.navbar-logo-btn {
  display: flex;
  align-items: center;
  margin-left: 80px !important;
}

.home-icon {
  height: 50px;
  width: 150px;
  background-image: url("@/assets/images/fixed/logo2.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

.btn-text {
  font-family: "Pretendard", sans-serif;
  font-size: 16px;
  font-weight: 300;
  color: #fff;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 0px 10px;
  margin: 0px 10px;
}

.btn-login {
  font-family: "Pretendard", sans-serif;
  font-size: 16px;
  font-weight: 700px;
  color: #fff;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-right: 80px !important;
  border: 1px solid white;
  color: white;
  /* 텍스트 색상도 흰색으로 변경 */
}

.btn-logout {
  font-family: "Pretendard", sans-serif;
  font-size: 16px;
  font-weight: 700px;
  color: #fff;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-right: 80px !important;
  border: 1px solid white;
  color: white;
  /* 텍스트 색상도 흰색으로 변경 */
}

.btn-text:hover {
  background-color: rgba(255, 255, 255, 0.25);
}

/* 클릭해서 선택되었을시 표시 */
.btn-text:focus {
  background-color: rgba(255, 255, 255, 0.25);
  color: white;
}

.v-menu > .v-overlay__content > .v-card,
.v-menu > .v-overlay__content > .v-sheet,
.v-menu > .v-overlay__content > .v-list {
  background-color: rgba(0, 0, 0, 0.25);
  color: white;
  border: 3px solid white;
}

.v-list-item:hover {
  background-color: rgba(255, 255, 255, 0.25);
}
</style>
