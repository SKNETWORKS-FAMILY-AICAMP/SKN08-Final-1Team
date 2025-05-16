<template>
    <!--페이지 중앙 중렬-->
    <v-container class="fill-height d-flex align-center justify-center">
        <!--데스크탑/모바일 모두 적당한 너비, 입체감과 부드러운 모서리-->
        <v-card class="pa-8" max-width="600" elevation="10" rounded="xl">
            <!--제목을 강조합니다-->
            <v-card-title class="text-h5 font-weight-bold mb-4">
                ✅ 직무를 선택하세요
            </v-card-title>

            <v-card-text>
                <v-radio-group v-model="selectedRole" column>
                    <v-radio
                        v-for="role in roles"
                        :key="role"
                        :label="role"
                        :value="role"
                        class="mb-2"
                    />
                </v-radio-group>
            </v-card-text>

            <v-card-actions class="justify-end">
                <v-btn
                    color="primary"
                    @click="goToNext"
                    :disabled="!selectedRole"
                    rounded
                    elevation="2"
                >
                    다음
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router"
import { ref } from "vue"

// ✅ SEO 메타 정보
definePageMeta({
    title: '직무 선택 페이지 | JobStick',
    description: 'JobStick 모의 면접을 시작하기 전에 원하는 직무를 선택해보세요.',
    keywords: ['직무 선택', '모의 면접', 'AI 모의 면접', 'JobStick', '직무 선택', '직무 카테고리', 'job-stick', '잡스틱'],
    ogTitle: 'JobStick 직무 선택 페이지',
    ogDescription: '모의 면접 시작하기 전에 지원하고자 하는 기업을 선택해보세요.',
    ogImage: '',    // 실제 이미지 경로
    robots: 'index, follow' // 검색엔진에 노출 혀용
});

const router = useRouter()
const selectedRole = ref('')
const roles = [
    'Backend',
    'Frontend',
    'Web/App',
    'AI',
    'Embedded',
    'DevOps',
]

function goToNext() {
    if (selectedRole.value) {
        router.push(`/skills?role=${selectedRole.value}`)
    }
}

// 일단 mocking하여 definePageMeta is not defined 에러를 방지합니다.
function definePageMeta(arg0: {
    title: string; description: string; keywords: string[]; ogTitle: string; ogDescription: string; ogImage: string; // 실제 이미지 경로
    robots: string; // 검색엔진에 노출 혀용
}) {
    throw new Error("Function not implemented.");
}
</script>

<style scoped>
/** 모바일에서도 적당한 여백 확보 */
.v-container {
    padding: 16px;
}

/* 라디오 버튼 간격을 조금 더 부드럽게 */
.v-radio {
    margin-bottom: 12px;
}

/* "다음" 버튼에 약간의 전환 효과 추가 */
.v-btn {
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.v-btn:hover {
    transform: scale(1.02);
}

/* 카드 내부 여백을 모바일에서도 최적화 */
.v-card {
    width: 100%;
    box-sizing: border-box;
}

/* 제목 강조 (이미 Vuetify의 text-h5가 있지만, 추가 강조를 원할 경우) */
.v-card-title {
    color: #2c3e50;
    letter-spacing: 0.5px;
}

/* 다크 모드 대응 */
:deep(.v-card) {
    transition: background-color 0.3s ease;
    background-color: white;
}

:deep(.v-application--is-ltr .v-card) {
    background-color: white;
}

:deep(.v-application--is-ltr.theme--dark .v-card) {
    background-color: #1e1e1e;
    color: #fff;
}

/* 버튼 hover 효과 개선 */
:deep(.v-btn:hover) {
    filter: brightness(1.1);
}

/* 반응형 레이아웃: 모바일에서는 여백 줄이기 */
@media (max-width: 600px) {
    :deep(.v-card) {
        padding: 1.5rem !important;
    }

    :deep(.v-card-title) {
        font-size: 1.2rem;
        text-align: center;
    }

    :deep(.v-btn) {
        width: 100%;
    }

    :deep(.v-card-actions) {
        justify-content: center !important;
    }
}
</style>