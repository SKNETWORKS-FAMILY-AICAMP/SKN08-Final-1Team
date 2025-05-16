<template>
  <v-app>
    <div class="layout-wrapper">
      <NavigationBar />
      <v-main class="main-wrapper">
        <NuxtPage />
      </v-main>
      <div :class="['footer-container', { 'home-footer': route.path === '/' }]">
        <div class="footer-inner">
          <img
            src="@/assets/images/fixed/eddi1.png"
            alt="위치 아이콘"
            class="footer-image"
          />
          <p class="reserved-info">서울특별시 송파구 새말로8길 26, 3층(문정동)</p>
          <p class="reserved-info">Copyright © 2025 에디(EDDI). All rights reserved.</p>
        </div>
      </div>
    </div>
  </v-app>
</template>

<script setup>
import { onMounted } from 'vue';
import { useHead } from '#imports';
import { useRoute } from 'vue-router';
import NavigationBar from '~/navigationBar/NavigationMenuBar.vue';

const route = useRoute();

// ✅ SEO 및 네이버 인증 메타 태그
useHead({
  meta: [
    {
      name: 'naver-site-verification',
      content: '8119a7007491408be1083bfa16f47ef6f1bdab01',
    },
  ],
});

// ✅ 구글 애널리틱스 삽입 (gtag.js)
onMounted(() => {
  if (process.client) {
    const script1 = document.createElement('script');
    script1.setAttribute('async', '');
    script1.src = 'https://www.googletagmanager.com/gtag/js?id=G-QG43SWSZTP';
    document.head.appendChild(script1);

    const script2 = document.createElement('script');
    script2.innerHTML = `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-QG43SWSZTP', {
        anonymize_ip: true,
        send_page_view: true
      });
    `;
    document.head.appendChild(script2);
  }
});
</script>

<style>
.layout-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: transparent;
}

.main-wrapper {
  flex: 1;
}

.footer-container {
  text-align: center;
  border-top: 1px solid #e0ccff;
  padding: 0;
}

.footer-inner {
  background-color: #f5f5f5;
  padding: 8px 12px 4px;
}

.footer-image {
  width: 60px;
  height: 60px;
  margin: 0 auto 2px auto;
  display: block;
}

.reserved-info {
  margin: 0 0 2px;
  font-size: 12px;
  color: #111;
}
</style>
