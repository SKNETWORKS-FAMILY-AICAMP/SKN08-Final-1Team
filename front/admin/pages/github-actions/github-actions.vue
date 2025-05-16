<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>GitHub Actions 모니터링</v-card-title>
          <v-card-subtitle>실시간으로 CI/CD 상태를 확인하세요</v-card-subtitle>
          <v-divider></v-divider>
          <v-card-text>
            <!-- 리포지토리 선택 -->
            <v-select
              v-model="selectedRepo"
              :items="repositories"
              item-title="name"
              item-value="url"
              label="모니터링할 리포지토리 선택"
              outlined
            ></v-select>
            <v-btn color="primary" @click="fetchWorkflowRuns"
              >데이터 새로고침</v-btn
            >
          </v-card-text>
          <v-divider></v-divider>

          <!-- 워크플로우 실행 리스트 -->
          <v-list>
            <v-list-item-group v-if="adminStore.workflows.length > 0">
              <v-list-item v-for="run in adminStore.workflows" :key="run.id">
                <v-list-item-content>
                  <v-list-item-title class="text-h6">
                    {{ run.name }}
                  </v-list-item-title>
                  <v-list-item-subtitle class="workflow-info">
                    <v-chip :color="statusColor(run.status)" label>
                      {{ statusLabel(run.status, run.conclusion) }}
                    </v-chip>
                    <span class="run-time"
                      >실행 시간:
                      <strong>{{ formatDate(run.created_at) }}</strong></span
                    >
                  </v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn icon @click="viewDetails(run.html_url)">
                    <v-icon>mdi-open-in-new</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list-item-group>
            <v-alert v-else type="info" class="mt-4">
              워크플로우 실행 데이터가 없습니다.
            </v-alert>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
///
<reference types="nuxt" />
<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useAdminStore } from "~/admin/stores/adminStore";

// ✅ SEO 메타 정보
definePageMeta({
  title: "GitHub Actions 모니터링 | Admin Dashboard - JobStick",
  keywords: [
    "GitHub Actions",
    "CI/CD",
    "워크플로우",
    "JobStick",
    "관리자 대시보드",
    "job-stick",
    "잡스틱"
  ],
  description:
    "관리자는 JobStick 프로젝트의 GitHub Actions 워크플로우 상태를 실시간으로 확인하고 상세 내역을 확인할 수 있습니다.",
  ogTitle: "GitHub Actions 모니터링 - JobStick Admin",
  ogDescription:
    "JobStick 프로젝트의 최신 GitHub Workflow 실행 내역을 관리자 페이지에서 확인해보세요.",
  ogImage: "", // 실제 이미지 경로
});

// Pinia 스토어 가져오기
const adminStore = useAdminStore();

// 선택된 리포지토리
const selectedRepo = ref<string | null>(null);

// 두 저장소의 목록
const repositories = [
  {
    name: "aview-nuxt-frontend",
    url: "https://github.com/minleewang/aview-nuxt-frontend",
  },
  {
    name: "aview-django-backend",
    url: "https://github.com/minleewang/aview-django-backend",
  },
  {
    name: "aview-fastapi-ai",
    url: "https://github.com/minleewang/aview-fastapi-ai",
  },
];

// GitHub Workflow 데이터 가져오기
const fetchWorkflowRuns = async () => {
  if (!selectedRepo.value) {
    alert("리포지토리를 선택해 주세요.");
    return;
  }

  const userToken = localStorage.getItem("userToken");
  if (!userToken) {
    alert("로그인이 필요합니다.");
    return;
  }

  try {
    console.log(`🔄 ${selectedRepo.value}의 GitHub Workflow 데이터 요청`);
    await adminStore.requestGithubWorkflow({
      userToken,
      repoUrl: selectedRepo.value,
    });
    console.log("Fetched workflows:", adminStore.workflows);
  } catch (error) {
    console.error("❌ fetchWorkflowRuns() 오류:", error);
  }
};

// 워크플로우 상세 페이지로 이동하는 함수
const viewDetails = (url: string) => {
  window.open(url, "_blank");
};

// 날짜 포맷을 사람이 읽기 좋은 형식으로 변환하는 함수
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    timeZone: "Asia/Seoul",
  }).format(date);
};

// 상태에 따른 색상 설정
const statusColor = (status: string) => {
  switch (status) {
    case "completed":
      return "green";
    case "in_progress":
      return "orange";
    case "queued":
      return "blue";
    case "failed":
    case "cancelled":
      return "red";
    default:
      return "gray";
  }
};

// 상태 레이블 포맷
const statusLabel = (status: string, conclusion: string | null) => {
  if (status === "completed" && conclusion === "success") {
    return "성공";
  } else if (status === "completed" && conclusion === "failure") {
    return "실패";
  } else {
    return status === "in_progress" ? "진행 중" : status;
  }
};

onMounted(() => {
  fetchWorkflowRuns();
});
</script>

<style scoped>
.v-list-item {
  cursor: pointer;
}

.workflow-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.run-time {
  font-weight: normal;
}
</style>
