<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline">개인정보 동의</v-card-title>
          <v-card-text>
            <!-- 약관 내용 -->
            <p><strong>제 1 조 (목적)</strong></p>
            <p>
              본 약관은 본 서비스가 제공하는 면접 연습 및 모의 면접 서비스(이하
              "서비스")의 이용 조건 및 절차, 이용자와 서비스 제공자의 권리, 의무
              및 책임사항을 규정함을 목적으로 합니다.
            </p>

            <p><strong>제 2 조 (약관의 효력과 변경)</strong></p>
            <p>
              ① 본 서비스는 이용자가 본 약관 내용에 동의하는 것을 조건으로
              서비스를 제공하며, 본 서비스의 이용 행위에는 본 약관을 우선적으로
              적용합니다.
            </p>
            <p>
              ② 본 서비스는 사전 고지 없이 본 약관을 변경할 수 있으며, 변경된
              약관은 서비스 내 공지를 통해 이용자가 직접 확인할 수 있도록
              합니다.
            </p>

            <p><strong>제 3 조 (개인정보의 수집 및 이용)</strong></p>
            <ul>
              <li>
                <strong>필수 정보:</strong> 이메일, 닉네임, 성별, 생년월일, 소셜
                로그인 타입, 연령대
              </li>
              <li>
                <strong>자동 수집 정보:</strong> 이용 기록, 방문 기록, IP 주소
              </li>
            </ul>

            <p><strong>제 4 조 (보관 및 파기)</strong></p>
            <p>
              ① 회원 탈퇴 시 즉시 삭제, 단 법령에 따라 보관할 필요가 있는 경우
              예외
            </p>
            <p>② 복구 불가능한 방식으로 파기</p>

            <p><strong>제 5 조 (제공 및 공유)</strong></p>
            <ul>
              <li>이용자 동의 시</li>
              <li>법령에 따른 요청 시</li>
            </ul>

            <p><strong>제 6 조 (이용자의 권리)</strong></p>
            <ul>
              <li>언제든지 열람, 수정, 삭제 요청 가능</li>
              <li>회원 탈퇴 시 개인정보 즉시 삭제</li>
            </ul>

            <p><strong>제 7 조 (서비스 이용 제한)</strong></p>
            <ul>
              <li>타인 정보 도용</li>
              <li>불법적 이용</li>
              <li>운영 방해 행위</li>
            </ul>

            <p><strong>제 8 조 (책임 및 면책)</strong></p>
            <p>① 무료 제공, 정보의 정확성 보장하지 않음</p>
            <p>② 데이터 손실, 오류, 피해에 책임 없음</p>

            <p><strong>제 9 조 (관할 법원)</strong></p>
            <p>대한민국 법 적용, 대한민국 관할 법원</p>

            <p><strong>부칙</strong></p>
            <p>본 약관은 2025년 3월 1일부터 시행됩니다.</p>

            <v-btn
              v-if="loginType === 'KAKAO'"
              @click="agreeAndLogin"
              color="primary"
              >동의 후 카카오 로그인</v-btn
            >
            <v-btn
              v-if="loginType === 'GOOGLE'"
              @click="agreeAndLogin"
              color="primary"
              >동의 후 구글 로그인</v-btn
            >
            <v-btn
              v-if="loginType === 'NAVER'"
              @click="agreeAndLogin"
              color="primary"
              >동의 후 네이버 로그인</v-btn
            >

            <v-alert v-if="!loginType" type="error" class="mt-5">
              로그인 방식이 확인되지 않았습니다. 로그인 페이지에서 다시
              시도해주세요.
            </v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useKakaoAuthenticationStore } from "../../../kakaoAuthentication/stores/kakaoAuthenticationStore";
import { useGoogleAuthenticationStore } from "../../../googleAuthentication/stores/googleAuthenticationStore";
import { useNaverAuthenticationStore } from "../../../naverAuthentication/stores/naverAuthenticationStore";

// ✅ SEO 메타 정보
definePageMeta({
  title: '개인정보 수집 및 이용 동의 | JobStick',
  description: 'JobStick 이용을 위한 개인정보 수집 및 이용 동의 페이지입니다. 사용자의 소중한 정보를 안전하게 처리합니다.',
  keywords: ['개인정보', '개인정보 수집', '개인정보 이용', '개인정보 이용 동의', 'JobStick', 'job-stick', '잡스틱'],
  ogTitle: 'JobStick 개인정보 동의',
  ogDescription: '서비스 이용을 위한 개인정보 동의 내용을 확인하고 동의해주세요.',
  ogImage: '' // 실제 이미지 경로 
});

const kakaoAuthentication = useKakaoAuthenticationStore();
const googleAuthentication = useGoogleAuthenticationStore();
const naverAuthentication = useNaverAuthenticationStore();

const loginType = ref(null);
const router = useRouter();

onMounted(() => {
  const tempType = sessionStorage.getItem("tempLoginType");
  const validTypes = ["KAKAO", "GOOGLE", "NAVER"];
  if (!tempType || !validTypes.includes(tempType)) {
    loginType.value = null;
    alert("잘못된 접근입니다. 로그인 페이지로 이동합니다.");
    router.push("/account/login"); // ✅ 로그인 페이지로 리다이렉트
  } else {
    loginType.value = tempType;
  }
});

const agreeAndLogin = async () => {
  if (!loginType.value) {
    alert("로그인 방식이 확인되지 않았습니다.");
    return;
  }

  try {
    if (loginType.value === "KAKAO") {
      await kakaoAuthentication.requestKakaoLoginToDjango();
    } else if (loginType.value === "GOOGLE") {
      await googleAuthentication.requestGoogleLoginToDjango();
    } else if (loginType.value === "NAVER") {
      await naverAuthentication.requestNaverLoginToDjango();
    }

    // ✅ 로그인 완료 후에만 영구 저장
    localStorage.setItem("loginType", loginType.value);
    sessionStorage.removeItem("tempLoginType");
  } catch (err) {
    console.error("로그인 실패:", err);
    alert("로그인 중 문제가 발생했습니다. 다시 시도해주세요.");
  }
};
</script>

<style scoped>
/* 필요 시 스타일 추가 */
</style>
