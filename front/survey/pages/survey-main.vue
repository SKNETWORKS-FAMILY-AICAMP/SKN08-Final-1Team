<!-- SurveyMain.vue -->
<template>
  <v-container>
    <h1>설문조사</h1>
    <p>의견을 입력해주세요</p>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue'


// ✅ SEO 메타 정보
definePageMeta({
  title: '설문조사 | JobStick',
  description: 'JobStick 설문조사에 참여해주세요.',
  keywords: ['설문조사', '의견조사', '설문', '구글폼', 'JobStick', '잡스틱'],
  ogTitle: 'JobStick 설문조사',
  ogDescription: 'JobStick 서비스를 이용한 후 다양한 의견을 남겨주세요.',
  ogImage: '', // 실제 이미지 경로
  robots: 'index, follow'
});

export default defineComponent({
  name: 'SurveyMain',
})
</script>
