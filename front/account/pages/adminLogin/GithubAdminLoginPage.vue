<template>
  <div class="grey lighten-5" style="font-family: 'Noto Sans KR', sans-serif">
    <v-container class="white">
      <v-row justify="center">
        <v-col cols="auto" style="padding-bottom: 90px">
          <v-card width="460">
            <v-card-text class="text-center px-12 py-16">
              <div class="text-h4 font-weight-black mb-10">
                GitHub Oauth 로그인
              </div>
              <div class="d-flex">
                <v-img
                  :src="githubIconSrc"
                  width="120"
                  class="mx-auto mb-6"
                ></v-img>
              </div>

              <v-btn
                block
                x-large
                rounded
                color="gray lighten-1"
                class="mt-6"
                @click="goToAdminCodeInput"
              >
                로그인
              </v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import logoSrc from "@/assets/images/fixed/logo1.png";
import githubIconSrc from "@/assets/images/fixed/icon-github.svg";

import { useGithubAuthenticationStore } from "../../../githubAuthentication/stores/githubAuthenticationStore";

// Pinia store 상태
const githubAuthentication = useGithubAuthenticationStore();

// 관리자 코드 입력 페이지로 이동
const goToAdminCodeInput = () => {
  router.push("/account/admin-code");
};

// Github 로그인 함수
const goToGithubLogin = async () => {
  console.log("goToGithubLogin");
  await githubAuthentication.requestGithubLoginToDjango();
};
</script>

<style scoped>
/* 추가적인 스타일이 필요하면 여기에 작성 */
</style>
