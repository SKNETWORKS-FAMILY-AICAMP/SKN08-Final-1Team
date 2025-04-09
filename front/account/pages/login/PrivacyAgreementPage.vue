<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline">개인정보 동의</v-card-title>
          <v-card-text>
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
              합니다. 이용자가 변경된 약관에 동의하지 않는 경우 회원 탈퇴를 할
              수 있으며, 계속 사용할 경우 변경된 약관에 동의한 것으로
              간주됩니다.
            </p>

            <p><strong>제 3 조 (개인정보의 수집 및 이용)</strong></p>
            <p>
              ① 본 서비스는 면접 연습 및 모의 면접 서비스 제공을 위해 다음과
              같은 개인정보를 수집합니다.
            </p>
            <ul>
              <li>
                <strong>필수 정보:</strong> 이메일, 닉네임, 성별, 생년월일, 소셜
                로그인 타입(카카오, 구글 등)
              </li>
              <li>
                <strong>자동 수집 정보:</strong> 서비스 이용 기록, 방문 기록, IP
                주소
              </li>
            </ul>
            <p>② 수집된 정보는 다음의 목적을 위해 사용됩니다.</p>
            <ul>
              <li>면접 연습 서비스 제공 및 맞춤형 면접 질문 제공</li>
              <li>서비스 이용 통계 분석을 통한 품질 개선</li>
              <li>회원 관리(로그인, 인증, 탈퇴 등)</li>
              <li>불법 및 부정 이용 방지</li>
            </ul>

            <p><strong>제 4 조 (개인정보 보관 및 파기)</strong></p>
            <p>
              ① 이용자의 개인정보는 회원 탈퇴 시 즉시 삭제됩니다. 단, 관계
              법령에 의해 보관할 필요가 있는 경우 해당 법령에서 정한 기간 동안
              보관됩니다.
            </p>
            <p>
              ② 개인정보 보관 기간이 경과한 경우, 해당 정보를 복구할 수 없는
              방식으로 완전히 삭제합니다.
            </p>

            <p><strong>제 5 조 (개인정보 제공 및 공유)</strong></p>
            <p>
              ① 본 서비스는 이용자의 개인정보를 제3자에게 제공하지 않습니다.
              다만, 아래의 경우는 예외로 합니다.
            </p>
            <ul>
              <li>이용자가 사전에 동의한 경우</li>
              <li>법령에 따라 수사기관의 요청이 있는 경우</li>
            </ul>

            <p><strong>제 6 조 (이용자의 권리 및 행사 방법)</strong></p>
            <p>
              ① 이용자는 언제든지 본인의 개인정보를 열람, 수정, 삭제 요청할 수
              있습니다.
            </p>
            <p>
              ② 회원 탈퇴를 원할 경우, 서비스 내 ‘회원 탈퇴’ 기능을 이용하면
              개인정보가 즉시 삭제됩니다.
            </p>

            <p><strong>제 7 조 (서비스 이용 제한)</strong></p>
            <p>
              ① 이용자가 다음과 같은 행위를 할 경우, 서비스 이용이 제한될 수
              있습니다.
            </p>
            <ul>
              <li>타인의 개인정보를 도용하는 행위</li>
              <li>불법적인 목적 또는 부정한 방법으로 서비스를 이용하는 행위</li>
              <li>서비스의 정상적인 운영을 방해하는 행위</li>
            </ul>

            <p><strong>제 8 조 (책임 및 면책)</strong></p>
            <p>
              ① 본 서비스는 무료로 제공되며, 이용자가 본 서비스를 통해 얻은
              정보에 대해 보증하지 않습니다.
            </p>
            <p>
              ② 이용자가 서비스 이용 과정에서 발생한 데이터 손실, 오류, 또는
              기타 피해에 대해 본 서비스는 책임을 지지 않습니다.
            </p>

            <p><strong>제 9 조 (관할 법원)</strong></p>
            <p>
              본 서비스 이용과 관련하여 발생하는 분쟁에 대해 대한민국 법을
              적용하며, 소송이 제기될 경우 관할 법원은 대한민국 내 정한 법원으로
              합니다.
            </p>

            <p><strong>부칙</strong></p>
            <p>본 약관은 2025년 3월 1일부터 시행됩니다.</p>

            <!-- 개인정보 동의 후 카카오 로그인 시작 버튼 -->
            <v-btn @click="goToKakaoLogin" color="primary"
              >동의 후 카카오 로그인</v-btn
            >
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useKakaoAuthenticationStore } from "../../../kakaoAuthentication/stores/kakaoAuthenticationStore";

const router = useRouter();
const kakaoAuthentication = useKakaoAuthenticationStore();

const goToKakaoLogin = async () => {
  localStorage.setItem("loginType", "KAKAO");
  await kakaoAuthentication.requestKakaoLoginToDjango();
};

const isAuthenticatedKakao = computed(() => authentication.isAuthenticated);
const loginType = computed(() => account.loginType);
</script>
