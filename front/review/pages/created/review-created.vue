<template>
  <v-container>
    <v-alert type="success">리뷰가 성공적으로 등록되었습니다!</v-alert>
    <v-btn @click="goToList">리스트로 돌아가기</v-btn>
  </v-container>
</template>

<script setup>
import { useRouter } from 'vue-router';


// ✅ SEO 메타 정보
definePageMeta({
  title: '리뷰 등록 성공 | JobStick',
  description: 'JobStick 리뷰가 성공적으로 등록되었습니다.',
  keywords: ['리뷰', '리뷰 등록', '등록 성공', '리뷰 등록 성공', 'JobStick', '잡스틱', 'job-stick'],
  ogTitle: 'JobStick 리뷰 등록 성공',
  ogDescription: 'JobStick 리뷰 등록 성공 페이지입니다. 리뷰가 성공적으로 등록되었습니다.',
  ogImage: '', // 실제 이미지 경로
  robots: 'noindex, nofollow'
});

const router = useRouter();

const goToList = () => {
  router.push('/review/list');
};
</script>