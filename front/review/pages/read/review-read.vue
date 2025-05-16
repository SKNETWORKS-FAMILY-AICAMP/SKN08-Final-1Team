<template>
  <v-container>
    <h1>{{ review?.reviewTitle }}</h1>
    <p>{{ review?.reviewDescription }}</p>
    <v-img v-if="review?.imageUrl" :src="review.imageUrl" width="400"></v-img>
    <v-btn @click="goBack">뒤로가기</v-btn>
  </v-container>
</template>
///
<reference types="nuxt" />
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";

// ✅ SEO 메타 정보
definePageMeta({
  title: "리뷰 확인 | JobStick",
  description: "JobStick 리뷰 리스트에서 리뷰를 확인해보세요.",
  keywords: ["리뷰", "리뷰 보기", "리뷰 확인", "JobStick", "잡스틱", "job-stick"],
  ogTitle: "JobStick 리뷰 확인",
  ogDescription: "JobStick 리뷰 확인 페이지입니다. 리뷰 내용을 확인해보세요.",
  ogImage: "", // 실제 이미지 경로
  robots: "index, follow", // 검색 엔진 노출 허용
});

const route = useRoute();
const router = useRouter();
const review = ref<any>(null);

onMounted(async () => {
  const res = await fetch(
    `http://localhost:8000/api/review/detail/${route.params.id}`
  );
  review.value = await res.json();
});

const goBack = () => router.push("/review/list");
</script>
