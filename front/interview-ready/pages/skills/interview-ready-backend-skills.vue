<template>
    <div>
        <h1>{{  role  }} Backend Tech Skill 선택</h1>
        <v-checkbox-group v-model="selectedBackendSkills">
            <v-checkbox v-for="tech in techMap[role]" :key="tech" :label="tech" :value="tech" />
        </v-checkbox-group>
        <v-btn @click="goToNext">다음</v-btn>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { useRouter, useRoute } from "vue-router"

// ✅ SEO 메타 정보
definePageMeta({
    title: '백엔드 기술 선택 페이지 | JobStick',
    description: 'JobStick 모의 면접을 시작하기 전에 백엔드 직무의 기술을 선택해보세요.',
    keywords: ['기술 선택', '모의 면접', 'AI 모의 면접', 'JobStick', '백엔드', 'backend', 'tech', '잡스틱'],
    ogTitle: 'JobStick 백엔드 기술 선택 페이지',
    ogDescription: '모의 면접 시작하기 전에 백엔드 기술을 선택해보세요.',
    ogImage: '',    // 실제 이미지 경로
    robots: 'index, follow' // 검색엔진에 노출 혀용
});

const router = useRouter()
const route = useRoute()

const role = route.query.role as string
const selectedSkills = ref<string[]>([])

const techMap: Record<string, string[]> = {
    Backend: [
        // 향후 Tech Skill은 수정될 수 있습니다. 현재 임의로 넣은 값입니다. 
        'Python',
        'Java',
        'Go',
        'Django', 
        'SpringBoot', 
        'Falsk',
        'MySQL',
        'MongoDB',
        'AWS',
        'GCP',
        'Azure',
        'Docker',
        'Kubernetes'
    ]
}

function goToNext() {
    router.push('/experience')
}

// 일단 mocking 하여 definePageMeta is not defined 에러를 방지합니다.
function definePageMeta(arg0: {
    title: string; description: string; keywords: string[]; ogTitle: string; ogDescription: string; ogImage: string; // 실제 이미지 경로
    robots: string; // 검색엔진에 노출 혀용
}) {
    throw new Error("Function not implemented.");
}
</script>

<style scoped>
/* 기본 레이아웃: 중앙 정렬 + 여백 */
div {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    background-color: white;
    transition: background-color 0.3s ease;
}

/* 다크 모드 대응 */
:deep(.v-application--is-ltr.theme--dark) div {
    background-color: #1e1e1e;
    color: #ffffff;
}

/* 제목 스타일 */
h1 {
    font-size: 1.5rem;
    font-size: bold;
    margin-bottom: 1.5rem;
    text-align: center;
}

/* 체크박스 그룹 spacing */
:deep(.v-cehckbox-group) {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-bottom: 2rem;
}

/* 버튼 스타일 */
:deep(.v-btn) {
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding: 0.5rem 1.5rem;
}

/* 반응형 대응 */
@media (max-width: 600px) {
    div {
        padding: 1.2rem;
        margin: 1rem;
    }

    h1 {
        font-size: 1.25rem;
    }

    :deep(.v-btn) {
        width: 100%
    }
}
</style>