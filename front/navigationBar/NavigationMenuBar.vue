<template>
  <v-app-bar
    color="transparent"
    app
    dark
    height="72"
    class="menu-bar d-flex justify-between align-center px-4"
  >
    <v-btn text @click="goToHome" class="navbar-logo-btn">
      <v-img class="home-icon"></v-img>
    </v-btn>

    <v-spacer />

    <div
      v-if="!$vuetify.display.smAndDown"
      class="d-flex align-center flex-grow-1 justify-center"
      style="gap: 16px"
    >
      <v-btn text @click="goToHome" class="btn-text"> HOME </v-btn>
      <v-btn
        v-if="isLoggedIn"
        text
        @click="goToReviewListPage"
        class="btn-text"
      >
        REVIEW
      </v-btn>

      <v-btn text @click="goToProductList" class="btn-text">
        COMPANY REPORT
      </v-btn>
      <v-btn text @click="goToLlmTestPage" class="btn-text">
        AI INTERVIEW
      </v-btn>
      <v-btn text @click="goToMembership" class="btn-text"> MEMBERSHIP </v-btn>

      <v-spacer></v-spacer>

      <!-- 로그인 후 화면-->
      <v-menu v-if="isLoggedIn && !isAdminLoggedIn" close-on-content-click>
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
      <v-menu v-if="isAdminLoggedIn" close-on-content-click>
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
        v-if="!isLoggedIn && !isAdminLoggedIn"
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
    </div>

    <!--햄메뉴-->
    <v-menu v-if="$vuetify.display.smAndDown" offset-y right>
      <!-- 햄버거 버튼이 메뉴 트리거 역할 -->
      <template v-slot:activator="{ props }">
        <v-app-bar-nav-icon v-bind="props" />
      </template>

      <!-- 드롭다운으로 뜨는 메뉴 항목 -->
      <v-list>
        <template v-if="isLoggedIn && !isAdminLoggedIn">
          <v-list-item @click="goToHome">
            <v-list-item-title>HOME</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToProductList">
            <v-list-item-title>COMPANY REPORT</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToLlmTestPage">
            <v-list-item-title>AI INTERVIEW</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToReviewListPage">
            <v-list-item-title>REVIEW</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToMembership">
            <v-list-item-title>MEMBERSHIP</v-list-item-title>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item
            v-for="(item, index) in myPageItems"
            :key="'mypage-menu-' + index"
            @click="item.action"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </template>

        <!-- ✅ 관리자 로그인 전용 메뉴 -->
        <template v-else-if="isAdminLoggedIn">
          <v-list-item
            v-for="(item, index) in adminPageList"
            :key="'admin-menu-' + index"
            @click="item.action"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </template>

        <!-- ✅ 비로그인 사용자 메뉴 -->
        <template v-else>
          <v-list-item @click="goToHome">
            <v-list-item-title>HOME</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToProductList">
            <v-list-item-title>COMPANY REPORT</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToLlmTestPage">
            <v-list-item-title>AI INTERVIEW</v-list-item-title>
          </v-list-item>
          <v-list-item @click="goToMembership">
            <v-list-item-title>MEMBERSHIP</v-list-item-title>
          </v-list-item>
        </template>

        <v-list-item v-if="!isLoggedIn" @click="signIn">
          <v-list-item-title>LOGIN</v-list-item-title>
        </v-list-item>
        <v-list-item v-else @click="signOut">
          <v-list-item-title>LOGOUT</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useKakaoAuthenticationStore } from "~/kakaoAuthentication/stores/kakaoAuthenticationStore";
import { useNaverAuthenticationStore } from "~/naverAuthentication/stores/naverAuthenticationStore";
import { useGoogleAuthenticationStore } from "~/googleAuthentication/stores/googleAuthenticationStore";
import { useGuestAuthenticationStore } from "~/guestAuthentication/stores/guestAuthenticationStore";
import { useGithubAuthenticationStore } from "~/githubAuthentication/stores/githubAuthenticationStore";
import { useAuthenticationStore } from "~/authentication/stores/authenticationStore";
import { useReviewStore } from "~/review/stores/reviewStore";

// Pinia 스토어 사용
const kakaoAuthenticationStore = useKakaoAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();
const guestAuthenticationStore = useGuestAuthenticationStore();
const githubAuthenticationStore = useGithubAuthenticationStore();
const authenticationStore = useAuthenticationStore();
const reviewStore = useReviewStore();

const router = useRouter();
const drawer = ref(false);
//일반 유저들 로그인 상태 확인
const isLoggedIn = computed(
  () =>
    kakaoAuthenticationStore.isAuthenticated ||
    googleAuthenticationStore.isAuthenticated ||
    naverAuthenticationStore.isAuthenticated ||
    guestAuthenticationStore.isAuthenticated ||
    githubAuthenticationStore.isAuthenticated
);
//관리자 로그인 상태 확인
const isAdminLoggedIn = computed(
  () => githubAuthenticationStore.isAuthenticated
);

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
  {
    title: "go서버 호출",
    action: () => goToGO(),
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
const goToProductList = () => router.push("/company-report/list"); // company report 페이지
const goToCart = () => router.push("/cart/list"); // 카트페이지
const goToOrder = () => router.push("/order/list"); // 주문내역 페이지
const goToMyPage = () => router.push("/account/mypage"); // 내페이지
const goToReviewListPage = () => router.push("/review/list"); // 리뷰페이지
const goToManagementUserPage = () => router.push("/management/user");
const goToManagementUserLogList = () => router.push("/management/log");
const goToGO = () => router.push("/admin/default");
const goToLlmTestPage = () => router.push("/ai-interview/llm-test");
const goToMembership = () => router.push("/price");

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
  guestAuthenticationStore.isAuthenticated = false;
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
  const userToken = localStorage.getItem("userToken");
  const loginType = localStorage.getItem("loginType");

  if (!userToken || !loginType) return;
  const isValid = await authenticationStore.requestValidationUserToken(
    userToken
  );
  if (!isValid) return;

  if (loginType === "KAKAO") {
    kakaoAuthenticationStore.isAuthenticated = true;
  } else if (loginType === "GOOGLE") {
    googleAuthenticationStore.isAuthenticated = true;
  } else if (loginType === "NAVER") {
    naverAuthenticationStore.isAuthenticated = true;
  } else if (loginType === "GUEST") {
    guestAuthenticationStore.isAuthenticated = true;
  } else if (loginType === "GITHUB") {
    githubAuthenticationStore.isAuthenticated = true;
  }
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
  padding: 0 !important;
  margin-left: 8px !important;
}

.v-app-bar-nav-icon {
  color: white;
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
