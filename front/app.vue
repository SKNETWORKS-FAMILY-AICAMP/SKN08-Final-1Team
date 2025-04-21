<template>
  <v-app>
    <v-main>
      <!-- NavigationBar 고정 -->
      <NavigationBar />
      <NuxtPage />
      <div class="footer-container" style="color: black">
        <p class="reserved-info">
          2025-2026 JOBSTICK Korea LLC. All Rights Reserved.
        </p>
      </div>
    </v-main>
  </v-app>
</template>

<script setup>
import { defineComponent } from "vue";
import NavigationBar from "~/navigationBar/NavigationMenuBar.vue";
</script>

<style>
/* 푸터 설정 */
.footer-container {
  background-color: rgba(255, 255, 255, 0.025);
  color: rgba(14, 13, 13, 0.75);
  font-size: 12px;
  text-align: center;
  padding: 7px;
  position: fixed;
  width: 100%;
  bottom: 0;
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 3px 5px black;
}
</style>
