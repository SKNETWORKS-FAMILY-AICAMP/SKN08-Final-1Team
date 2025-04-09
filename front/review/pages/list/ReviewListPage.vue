<template lang="">
  <v-container max-width="1600">
    <br />
    <h2>작성된 설문 조사 확인</h2>
    <br /><br />
    <v-data-table
      v-model:items-per-page="perPage"
      :headers="headerTitle"
      :items="pagedItems"
      v-model:pagination="pagination"
      class="elevation-1"
      hide-default-footer
    >
      <template v-slot:item="{ item }">
        <tr @click="readRow(item)">
          <td>
            {{ item.reviewId }}
          </td>
          <td>
            <span @click.stop="readRow(item)">
              {{ item.reviewTitle }}
            </span>
          </td>
          <td>
            <v-btn @click.stop="goToReviewResultPage(item)"> 응답 확인 </v-btn>
          </td>
        </tr>
      </template>
    </v-data-table>

    <v-pagination
      v-model="pagination.page"
      :length="Math.ceil(reviewTitleList.length / perPage)"
      color="primary"
      @input="updateItems"
    />

    <v-container align="end">
      <v-btn class="ml-2" color="primary" @click="goToReviewRegisterPage"
        >설문조사 만들기
      </v-btn>
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useReviewStore } from "@/stores/reviewStore";
import { useRouter } from "vue-router";

const router = useRouter();
const reviewStore = useReviewStore();

const headerTitle = ref([
  {
    title: "No",
    align: "start",
    sortable: true,
    key: "reviewId",
    width: "50px",
  },
  { title: "제목", align: "start", key: "reviewTitle" },
  { title: "설문 응답 확인", align: "start", key: "actions", sortable: false },
]);

const perPage = ref(5);
const pagination = ref({
  page: 1,
});

const reviewTitleList = computed(() => reviewStore.reviewTitleList || []);

const pagedItems = computed(() => {
  const startIdx = (pagination.value.page - 1) * perPage.value;
  const endIdx = startIdx + perPage.value;
  return (reviewTitleList.value || []).slice(startIdx, endIdx);
});

const readRow = (item) => {
  router.push({
    name: "ReviewReadPage",
    params: { randomString: item.randomString.toString() },
  });
};

const goToReviewResultPage = (item) => {
  router.push({
    name: "ReviewResultPage",
    params: { reviewId: item.reviewId },
  });
};

const goToReviewRegisterPage = () => {
  router.push("/review/register");
};

const updateItems = () => {
  // 페이지 변경 시 실행할 함수
};

/*onMounted(() => {
  reviewStore.requestReviewListToDjango();
});*/
</script>
