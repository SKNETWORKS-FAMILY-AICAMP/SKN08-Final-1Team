<template>
  <v-container>
    <p>로그인 처리 중...</p>
  </v-container>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

onMounted(() => {
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get("code");

  if (code) {
    fetchAccessToken(code);
  } else {
    console.error("로그인 실패: 코드가 없습니다.");
    router.push("/login"); // 로그인 페이지로 리디렉션
  }
});

const fetchAccessToken = async (code) => {
  const clientId = import.meta.env.VITE_KAKAO_CLIENT_ID; // 환경 변수 사용
  const redirectUri = import.meta.env.VITE_KAKAO_REDIRECT_URI; // 환경 변수 사용

  try {
    const response = await fetch("https://kauth.kakao.com/oauth/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        grant_type: "authorization_code",
        client_id: clientId,
        redirect_uri: redirectUri,
        code: code,
      }),
    });

    if (!response.ok) {
      throw new Error("카카오 로그인 실패");
    }

    const data = await response.json();
    console.log("카카오 로그인 응답:", data);
    // 액세스 토큰(data.access_token)을 안전하게 저장하고 처리

    router.push("/"); // 홈 페이지로 리디렉션
  } catch (error) {
    console.error("카카오 로그인 에러:", error);
    router.push("/login"); // 로그인 페이지로 리디렉션
  }
};
</script>
