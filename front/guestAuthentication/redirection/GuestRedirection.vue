<template>
  <div></div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useAccountStore } from "../../account/stores/accountStore";
import { useGuestAuthenticationStore } from "../../guestAuthentication/stores/guestAuthenticationStore";

const accountStore = useAccountStore();
const guestAuthenticationStore = useGuestAuthenticationStore();

const router = useRouter();
const route = useRoute();

const setRedirectGoogleData = async () => {
  const code = route.query.code;
  const userToken = await guestAuthenticationStore.requestAccessToken({
    code,
  });

  localStorage.setItem("userToken", userToken);
  guestAuthenticationStore.isAuthenticated = true;
  guestAuthenticationStore.userToken = userToken;

  router.push("/");
};

onMounted(async () => {
  await setRedirectGoogleData();
});
</script>
