<!-- src/views/WithdrawalPage.vue -->
<template>
  <v-container>
    <!-- 탈퇴 사유 선택 -->
    <v-form v-if="step === 'reason'" class="reason-section">
      <h3>서비스 품질 향상을 위해 탈퇴 사유를 선택해주세요.</h3>
      <v-radio-group class="radio-group-section" v-model="selectedReason">
        <v-radio
          v-for="(reason, index) in reasons"
          :key="index"
          :label="reason.label"
          :value="reason.value"
        />
      </v-radio-group>
      <v-btn :disabled="!isButtonEnabled" @click="goToAgreement">
        다음
      </v-btn>
    </v-form>

    <!-- 탈퇴 안내 및 동의 -->
<div v-else-if="step === 'agreement'" class="agreement-section">
  <h2 class="agreement-title">Jobstick 회원 탈퇴 안내 및 동의</h2>
  <v-card class="agreement-card mt-4 pa-4">
    <p>
      Jobstick 회원 탈퇴 시, 아래 항목은 관계법령에 따라 일정 기간 동안 안전하게 보관됩니다.<br />
      보존된 정보는 법령에 따른 목적 외에는 절대 사용되지 않습니다.
    </p>
    <ul class="mt-2">
      <li>계약 및 결제 관련 기록: 5년 (전자상거래법)</li>
      <li>전자금융 거래 기록: 5년 (전자금융거래법)</li>
      <li>소비자 불만 및 분쟁 처리 기록: 3년 (전자상거래법)</li>
      <li>웹사이트 접속 기록: 3개월 (통신비밀보호법)</li>
    </ul>
    <p class="mt-3">
      위 내용을 확인하였으며 Jobstick 회원 탈퇴를 계속 진행하시겠습니까?
    </p>
  </v-card>

  <div class="agreement-button-group">
    <v-btn class="mr-4" color="grey" @click="goBack">이전</v-btn>
    <v-btn color="red" @click="proceedWithdrawal">탈퇴 동의</v-btn>
  </div>
</div>


    <!-- 완료 다이얼로그 -->
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="headline">알림</v-card-title>
        <v-card-text>회원 탈퇴가 완료되었습니다.</v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" text @click="closeDialog">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

import { useAccountStore } from '@/account/stores/accountStore'
import { useKakaoAuthenticationStore } from '@/kakaoAuthentication/stores/kakaoAuthenticationStore'
import { useNaverAuthenticationStore } from '@/naverAuthentication/stores/naverAuthenticationStore'
import { useGoogleAuthenticationStore } from '@/googleAuthentication/stores/googleAuthenticationStore'
import { useAuthenticationStore } from '@/authentication/stores/authenticationStore'

// ✅ SEO 메타 정보
definePageMeta({
  title: '회원 탈퇴 | JobStick',
  description: 'JobStick 계정을 탈퇴하고자 하는 이유를 선택하고, 계정 삭제 절차를 진행할 수 있습니다.',
  keywords: ['회원 탈퇴', '계정 삭제', 'JobStick', '서비스 해지'],
  ogTitle: 'JobStick 회원 탈퇴',
  ogDescription: '계정을 삭제하고 JobStick 서비스를 탈퇴하는 절차를 안내합니다.',
  ogImage: '' // 실제 이미지 경로
});

const step = ref('reason')
const selectedReason = ref(null)
const isButtonEnabled = computed(() => selectedReason.value !== null)
const dialog = ref(false)
const router = useRouter()

const accountStore = useAccountStore()
const kakaoStore = useKakaoAuthenticationStore()
const naverStore = useNaverAuthenticationStore()
const googleStore = useGoogleAuthenticationStore()
const authStore = useAuthenticationStore()

const reasons = ref([
  { label: '서비스 품질 불만족', value: 'SERVICE_DISSATISFACTION' },
  { label: '사용 빈도 낮음', value: 'LOW_USAGE' },
  { label: '다른 서비스 사용', value: 'OTHER_SERVICE' },
  { label: '개인정보 보호 우려', value: 'PRIVACY_CONCERN' },
  { label: '기타', value: 'OTHER' }
])

const goToAgreement = () => {
  step.value = 'agreement'
}

const goBack = () => {
  step.value = 'reason'
}

const proceedWithdrawal = () => {
  const reason = selectedReason.value ?? ''
  const loginType = localStorage.getItem('loginType')

  if (loginType === 'KAKAO') kakaoStore.requestKakaoWithdrawToDjango()
  else if (loginType === 'GOOGLE') googleStore.requestGoogleWithdrawToDjango()
  else if (loginType === 'NAVER') naverStore.requestNaverWithdrawToDjango()

  accountStore.requestWithdrawalToDjango({ reason })

  // 로컬스토리지 및 인증 초기화
  localStorage.removeItem('userToken')
  localStorage.removeItem('loginType')
  authStore.isAuthenticated = false
  kakaoStore.isAuthenticated = false
  naverStore.isAuthenticated = false
  googleStore.isAuthenticated = false

  dialog.value = true
}

const closeDialog = () => {
  dialog.value = false
  router.push('/')
}
</script>

<style scoped>
.reason-section {
  margin-top: 30px;
}

.radio-group-section {
  margin-top: 30px;
  margin-bottom: 10px;
}

ul {
  margin-left: 1rem;
  list-style-type: disc;
}

/* 중앙 정렬 스타일 추가 */
.agreement-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 80vh;
  text-align: center;
}

.agreement-title {
  margin-bottom: 20px;
}

.agreement-card {
  max-width: 600px;
  width: 100%;
}

.agreement-button-group {
  margin-top: 24px;
  display: flex;
  justify-content: center;
}
</style>
