<template>
  <v-container>
    <v-form class="reason-section">
      <h3>서비스 품질 향상을 위해 탈퇴 사유를 선택해주세요.</h3>
      <v-radio-group class="radio-group-section" v-model="selectedReason">
        <v-radio
          v-for="(reason, index) in reasons"
          :key="index"
          :label="reason.label"
          :value="reason.value"
        ></v-radio>
      </v-radio-group>
      <v-btn :disabled="!isButtonEnabled" @click="submitWithdrawal">
        탈퇴 신청
      </v-btn>
    </v-form>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="headline">알림</v-card-title>
        <v-card-text>회원 탈퇴가 완료되었습니다.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="closeDialog">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, computed } from "vue";
import { useAccountStore } from "../../../account/stores/accountStore";
import { useKakaoAuthenticationStore } from "../../../kakaoAuthentication/stores/kakaoAuthenticationStore";
import { useNaverAuthenticationStore } from "../../../naverAuthentication/stores/naverAuthenticationStore";
import { useGoogleAuthenticationStore } from "../../../googleAuthentication/stores/googleAuthenticationStore";
import { useAuthenticationStore } from "../../../authentication/stores/authenticationStore";
import { useRouter } from "vue-router";
import { naverAuthenticationState } from "~/naverAuthentication/stores/naverAuthenticationState";

// 탈퇴 사유 리스트
const reasons = ref([
  { label: "서비스 품질 불만족", value: "SERVICE_DISSATISFACTION" },
  { label: "사용 빈도 낮음", value: "LOW_USAGE" },
  { label: "다른 서비스 사용", value: "OTHER_SERVICE" },
  { label: "개인정보 보호 우려", value: "PRIVACY_CONCERN" },
  { label: "기타", value: "OTHER" },
]);

// 선택된 탈퇴 사유와 다이얼로그 상태
const selectedReason = ref(null);
const dialog = ref(false);

// store와 router 사용 설정
const accountStore = useAccountStore();
const kakaoAuthenticationStore = useKakaoAuthenticationStore();
const naverAuthenticationStore = useNaverAuthenticationStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();
const authentication = useAuthenticationStore();
const router = useRouter();

// 버튼 활성화 여부 계산
const isButtonEnabled = computed(() => selectedReason.value !== null);

// 탈퇴 신청 처리
const submitWithdrawal = () => {
  const reasonString = selectedReason.value ? String(selectedReason.value) : "";
  const loginType = localStorage.getItem('loginType'); // 현재 로그인 타입 가져오기

  if (loginType === 'kakao') {
    kakaoAuthenticationStore.requestKakaoWithdrawToDjango();
  } else if (loginType === 'google') {
    googleAuthenticationStore.requestGoogleWithdrawToDjango();
  } else if (loginType === 'naver') {
    naverAuthenticationStore.requestNaverWithdrawToDjango?.(); 
    // naver 탈퇴 함수가 있을 경우에만 호출
  }

  // 공통 탈퇴 요청 (우리 서버 DB에서 탈퇴)
  accountStore.requestWithdrawalToDjango({ reason: reasonString });

  // 로컬 저장소 정리
  localStorage.removeItem("userToken");
  localStorage.removeItem("loginType");

  // 완료 다이얼로그 띄우기
  dialog.value = true;
};


// 다이얼로그 닫기 처리 및 로그아웃
const closeDialog = () => {
  dialog.value = false;
  //kakaoAuthenticationStore.requestLogout();
  //naverAuthenticationStore.requestLogout();
  authentication.isAuthenticated = false;
  naverAuthenticationStore.isAuthenticated = false;
  kakaoAuthenticationStore.isAuthenticated = false;
  googleAuthenticationStore.isAuthenticated = false;
  localStorage.removeItem("userToken");
  localStorage.removeItem("loginType");
  router.push("/");
};
</script>

<style scoped>
.reason-section {
  margin-top: 30px;
}

.radio-group-section {
  margin-top: 30px;
  margin-bottom: 10px;
}
</style>
