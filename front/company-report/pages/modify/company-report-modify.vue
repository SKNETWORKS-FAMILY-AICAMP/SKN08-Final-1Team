<template>
    <v-container>
        <v-card v-if="companyReport">
        <v-card-title>게시물 수정</v-card-title>
        <v-card-text>
            <v-container>
            <v-row>
                <v-col cols="12">
                <v-text-field v-model="companyReportName" label="제목" />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                <v-text-field
                    v-model="companyReportPrice"
                    label="가격"
                    auto-grow
                />
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="12">
                <v-textarea
                    v-model="content"
                    label="내용"
                    auto-grow
                />
                </v-col>
            </v-row>
            <v-row justify="end">
                <v-col cols="auto">
                <v-btn color="primary" @click="onModify">
                    <v-icon>mdi-check</v-icon>
                    <span>수정 완료</span>
                </v-btn>
                </v-col>
                <v-col cols="auto">
                <router-link :to="{ name: 'CompanyReportReadPage', params: { companyReportId: companyReportId } }">
                    <v-btn color="secondary">
                    <v-icon>mdi-arrow-left</v-icon>
                    <span>돌아가기</span>
                    </v-btn>
                </router-link>
                </v-col>
            </v-row>
            </v-container>
        </v-card-text>
        </v-card>
    </v-container>
</template>
  
<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useCompanyReportStore } from "../../stores/companyReportStore";

// ✅ SEO 메타 정보 
definePageMeta({
  title: '회사 보고서 수정 | JobStick',
  description: 'JobStick 관리자 페이지에서 회사 보고서를 수정할 수 있습니다.',
  keywords: ['회사 보고서', '회사 보고서 수정', '관리자 페이지', 'JobStick 보고서', 'JobStick', '잡스틱'],
  ogTitle: 'JobStick 관리자 - 회사 보고서 수정',
  ogDescription: 'JobStick에서 보고서 내용을 수정하고 관리하세요.',
  ogImage: '',  // 실제 이미지 경로
  robots: 'noindex, nofollow' // 관리자용이라서 검색 노출 방지
});

const route = useRoute();
const router = useRouter();
const companyReportStore = useCompanyReportStore();

const companyReportName = ref(null)
const content = ref(null)
const companyReportPrice = ref(0)
const keyword = ref(null)
const companyReportId = ref(route.params.id);

const companyReport = computed(() => companyReportStore.companyReport);
const companyReports = computed(() => companyReportStore.companyReportList);

async function fetchCompanyReportData(companyReportId) {
  await companyReportStore.requestCompanyReportToDjango(companyReportId);
};

async function onModify() {
  try {
    const payload = {
      companyReportId: Number(companyReportId.value), 
      companyReportName: companyReportName.value || companyReport.value.companyReportName,
      content: content.value || companyReport.value.content,
      companyReportPrice: companyReportPrice.value || companyReport.value.companyReportPrice
    };

    await companyReportStore.requestModifyCompanyReportToDjango(payload);
    alert('수정이 완료되었습니다.');
    await router.push(`/companyReport/read/${companyReportId.value}`);
  } catch (error) {
    console.error('수정 중 에러 발생:', error);
    alert('수정에 실패하였습니다. 다시 시도해 주세요.');
  }
}


onMounted(async () => {
  // 전체 보고서 가져오기
  await fetchCompanyReportData(companyReportId.value);
});

</script>
