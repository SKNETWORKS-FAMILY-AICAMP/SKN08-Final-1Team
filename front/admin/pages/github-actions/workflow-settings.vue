<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-select
          v-model="selectedRepo"
          :items="repositories"
          label="저장소 선택"
        />
      </v-col>

      <v-col cols="12">
        <v-btn color="primary" @click="triggerDeploy" :disabled="!selectedRepo">
          배포하기
        </v-btn>
      </v-col>

      <v-col cols="12">
        <v-alert v-if="message" :type="messageType" class="mt-4">
          {{ message }}
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>
///
<reference types="nuxt" />
<script setup lang="ts">
import { ref } from "vue";
import { useAdminStore } from "@/stores/adminStore";

// ✅ SEO 메타 정보
definePageMeta({
  title: "워크플로우 설정 | Admin Dashboard - JobStick",
  description:
    "GitHub 워크플로우를 직접 선택하고 실행할 수 있는 관리자 설정 페이지입니다.",
  keywords: [
    "GitHub",
    "워크플로우 실행",
    "Admin Dashboard",
    "CI/CD",
    "배포 설정",
    "JobStick",
    "job-stick",
    "잡스틱"
  ],
  ogTitle: "워크플로우 설정 - 관리자 페이지",
  ogDescription:
    "JobStick 관리자 대시보드에서 배포 및 테스트 워크플로우를 관리하세요.",
  ogImage: "", // 실제 이미지 경로
});

const adminStore = useAdminStore();

const repositories = [
  "minleewang/aview-nuxt-frontend",
  "minleewang/aview-django-backend",
  "minleewang/aview-fastapi-ai",
];
const selectedRepo = ref<string | null>(repositories[0]);
const message = ref("");
const messageType = ref<"success" | "error">("success");

const triggerDeploy = async () => {
  message.value = "";
  try {
    const userToken = localStorage.getItem("userToken");

    if (!userToken) {
      throw new Error("사용자 토큰이 존재하지 않습니다.");
    }

    await adminStore.triggerGithubWorkflow({
      userToken,
      repoUrl: selectedRepo.value!,
      workflowName: "main.yml",
    });

    message.value = "워크플로우 실행 성공!";
    messageType.value = "success";
  } catch (err: any) {
    message.value = `실행 실패: ${err.message}`;
    messageType.value = "error";
  }
};
</script>
