<template>
  <div></div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useAccountStore } from "../../account/stores/accountStore";
import { useGoogleAuthenticationStore } from "../../googleAuthentication/stores/googleAuthenticationStore";

const accountStore = useAccountStore();
const googleAuthenticationStore = useGoogleAuthenticationStore();

const router = useRouter();
const route = useRoute();

const setRedirectGoogleData = async () => {
  const code = route.query.code;
  const userToken = await googleAuthenticationStore.requestAccessToken({ code });

  localStorage.setItem("userToken", userToken);
  googleAuthenticationStore.isAuthenticated = true;

  router.push("/");
};

onMounted(async () => {
  await setRedirectGoogleData();
});
</script>
