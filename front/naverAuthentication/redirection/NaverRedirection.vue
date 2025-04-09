<template>
  <div></div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useAccountStore } from "../../account/stores/accountStore";
import { useNaverAuthenticationStore } from "../stores/naverAuthenticationStore";

const accountStore = useAccountStore();
const naverAuthenticationStore = useNaverAuthenticationStore();

const router = useRouter();
const route = useRoute();

const setRedirectNaverData = async () => {
  const code = route.query.code;
  const state = route.query.state;
  const userToken = await naverAuthenticationStore.requestAccessToken({
    code,
    state,
  });

  localStorage.setItem("userToken", userToken);
  naverAuthenticationStore.isAuthenticated = true;

  router.push("/");
};

onMounted(async () => {
  await setRedirectNaverData();
});
</script>
