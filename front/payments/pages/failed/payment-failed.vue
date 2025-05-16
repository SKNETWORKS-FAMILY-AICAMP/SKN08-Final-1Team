<template>
  <div id="info" class="box_section" style="width: 600px">
    <img style="width: 100px" src="https://static.toss.im/lotties/error-spot-no-loop-space-apng.png" />
    <h2>결제를 실패했어요</h2>

    <div class="p-grid typography--p" style="margin-top: 50px">
      <div class="p-grid-col text--left"><b>에러메시지</b></div>
      <div class="p-grid-col text--right" id="message">{{ route.query.message }}</div>
    </div>
    <div class="p-grid typography--p" style="margin-top: 10px">
      <div class="p-grid-col text--left"><b>에러코드</b></div>
      <div class="p-grid-col text--right" id="code">{{ route.query.code }}</div>
    </div>
    <div class="p-grid">
      <button class="button p-grid-col5"
        onclick="location.href='https://docs.tosspayments.com/guides/payment/integration';">연동 문서</button>
      <button class="button p-grid-col5" onclick="location.href='https://discord.gg/A4fRFXQhRu';"
        style="background-color: #e8f3ff; color: #1b64da">실시간 문의</button>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

definePageMeta({
  title: '결제 실패 | JobStick',
  description: 'JobStick 결제에 실패했습니다.',
  keywords: ['결제 실패', '실패', 'JobStick', '잡스틱', 'job-stick'],
  ogTitle: 'JobStick 결제 실패',
  ogDescription: 'JobStick 결제 실패 안내 페이지입니다. 결제 과정에서 문제가 발생했습니다.',
  ogImage: '', // 실제 이미지 경로
  robots: 'noindex, nofollow'
})
</script>

<style scoped>
.box_section {
  margin-top: 10%;
  margin-left: 42%;
}
</style>
