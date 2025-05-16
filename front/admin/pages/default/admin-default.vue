<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <v-card class="admin-card" @click="goToMonitoring">
          <v-card-title>Github Actions 모니터링</v-card-title>
          <v-card-subtitle>워크플로우 실행 상태를 실시간으로 확인</v-card-subtitle>
        </v-card>
      </v-col>
      
      <v-col cols="6">
        <v-card class="admin-card" @click="goToUserManagement">
          <v-card-title>사용자 관리</v-card-title>
          <v-card-subtitle>관리자 및 일반 사용자 계정 관리</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="6">
        <v-card class="admin-card" @click="goToLogsAndAlerts">
          <v-card-title>로그 분석 및 알림 관리</v-card-title>
          <v-card-subtitle>실패 로그 확인 및 알림 설정</v-card-subtitle>
        </v-card>
      </v-col>
      
      <v-col cols="6">
        <v-card class="admin-card" @click="goToWorkflowSettings">
          <v-card-title>워크플로우 설정 관리</v-card-title>
          <v-card-subtitle>Github Actions 템플릿 및 자동화 설정</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useRouter } from 'vue-router';

// ✅ SEO 메타 정보
definePageMeta({
  title: '관리자 대시보드 | JobStick',
  keywords: ['GitHub Actions', '모니터링','사용자 관리', '로그 및 알림', '워크플로우 설정', 'JobStick', 'job-stick', '잡스틱'],
  description: 'GitHub Actions 모니터링, 사용자 관리, 로그 및 알림, 워크플로우 설정을 위한 관리자 페이지입니다.',
  ogTitle: 'JobStick 관리자 대시보드',
  ogDescription: 'GitHub Actions와 사용자 관리를 한눈에! JobStick 관리자 기능을 확인해보세요.',
  ogImage: '' // 실제 이미지 경로
});

const router = useRouter();

const goToMonitoring = () => router.push('/admin/monitoring');
const goToUserManagement = () => router.push('/admin/user-management');
const goToLogsAndAlerts = () => router.push('/admin/logs-alerts');
const goToWorkflowSettings = () => router.push('/admin/workflow-settings');
</script>

<style scoped>
.admin-card {
  cursor: pointer;
  padding: 20px;
  text-align: center;
  transition: transform 0.2s;
}
.admin-card:hover {
  transform: scale(1.05);
}
</style>