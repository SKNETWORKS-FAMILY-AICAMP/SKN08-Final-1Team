<template>
  <v-container>
    <v-row class="justify-space-between align-center mb-6">
      <h2>📋 리뷰 리스트</h2>
      <v-btn color="primary" @click="goToRegister">✍ 리뷰 작성하기</v-btn>
    </v-row>

    <v-row>
      <v-col
        v-for="review in reviewStore.reviewList"
        :key="review.id"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card>
          <!-- 이미지가 있을 경우만 출력 -->
          <v-img
            v-if="review.imageUrl"
            :src="review.imageUrl"
            height="200px"
            cover
          />
          <v-card-title class="text-h6">{{ review.title }}</v-card-title>
          <v-card-subtitle class="grey--text text--darken-1">
            작성자: {{ review.nickname }} / {{ review.createDate }}
          </v-card-subtitle>
          <v-card-text>{{
            review.content && review.content.length > 100
              ? review.content.slice(0, 100) + "..."
              : review.content
          }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { defineStore } from "pinia";
import { onMounted } from "vue";
import { useReviewStore } from "~/review/stores/reviewStore";
import { useRouter } from "vue-router";

// ✅ SEO 메타 정보
definePageMeta({
  title: "리뷰 리스트 | JobStick",
  description: "JobStick 리뷰 리스트페이지입니다.",
  keywords: ["리뷰", "리뷰 리스트", "리뷰 목록", "Jobstick", "잡스틱", "job-stick"],
  ogTitle: "JobStick 리뷰 리스트",
  ogDescription: "JobStick 리뷰 리스트 페이지입니다.",
  ogImage: "", // 실제 이미지 경로
  robots: "index, follow", // 검색 엔진에서 리뷰 페이지 노출 허용
});

const reviewStore = useReviewStore();
const router = useRouter();

const goToRegister = () => {
  // 프롬트 게이지 리스트 페이지와 연결합니다.
  router.push("/review/register");
};

onMounted(() => {
  if (process.client) {
    const userToken = localStorage.getItem("userToken");
    if (!userToken) {
      alert("로그인이 필요합니다. 로그인 페이지로 이동합니다.");
      router.push("/account/login");
    } else {
      reviewStore.requestReviewListToDjango();
    }
  }
});
</script>
