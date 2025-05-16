<template>
  <div></div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useAccountStore } from "../../account/stores/accountStore";
import { useGithubAuthenticationStore } from "../../githubAuthentication/stores/githubAuthenticationStore";

const accountStore = useAccountStore();
const githubAuthenticationStore = useGithubAuthenticationStore();

const router = useRouter();
const route = useRoute();

const setRedirectGithubData = async () => {
  const code = route.query.code;
  const userToken = await githubAuthenticationStore.requestAccessToken({
    code,
  });

  localStorage.setItem("userToken", userToken);
  localStorage.setItem("loginType", "GITHUB");
  githubAuthenticationStore.isAuthenticated = true;

  router.push("/");
};

onMounted(async () => {
  await setRedirectGithubData();
});
</script>
