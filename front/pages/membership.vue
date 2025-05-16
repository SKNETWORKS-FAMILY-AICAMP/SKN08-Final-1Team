<template>
  <div style="padding: 40px">
    <h2>💼 멤버십 요금제</h2>

    <!-- 에러 발생 시 -->
    <div v-if="error">
      <p style="color: red">❗ 요금제를 불러오는 중 오류가 발생했습니다.</p>
    </div>

    <!-- 요금제 리스트 -->
    <ul v-else>
      <li v-for="plan in plans" :key="plan.id" style="margin-bottom: 16px">
        <strong>{{ plan.name }}</strong> - {{ plan.price }}원
        <button @click="subscribe(plan)">구독하기</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useFetch } from '#app'

const router = useRouter()

// ✅ 백엔드에서 요금제 목록 가져오기
const { data: plans, error } = await useFetch('http://localhost:8000/membership_plan/memberships/')

// ✅ 구독하기 버튼 클릭 시 호출
const subscribe = (plan) => {
  console.log("✅ [구독하기 버튼 클릭됨]", plan)

  if (!plan || !plan.price || !plan.id) {
    alert("❗ 잘못된 요금제 정보입니다.")
    return
  }

  // ✅ 결제 페이지로 이동
  router.push({
    path: '/payment',
    query: {
      amount: plan.price,
      planId: plan.id
    }
  })
}
</script>

<style scoped>
button {
  padding: 6px 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>
