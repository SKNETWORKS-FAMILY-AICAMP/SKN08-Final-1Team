<!-- payments/pages/payment/index.vue -->
<template>
  <div class="wrapper">
    <div class="box_section">
      <div id="payment-method"></div>
      <div id="agreement"></div>
      <v-btn
        :disabled="!inputEnabled"
        @click="requestPayment"
        class="button"
        id="payment-button"
        style="margin: 30px"
      >
        결제하기
      </v-btn>
    </div>
  </div>
</template>

<script setup>
import { loadPaymentWidget, ANONYMOUS } from "@tosspayments/payment-widget-sdk"
import { useRuntimeConfig } from "nuxt/app"
import { nanoid } from "nanoid"
import { onMounted, ref } from "vue"
import { useRoute } from "vue-router"

const config = useRuntimeConfig()
const route = useRoute()
const paymentWidget = ref(null)
const paymentMethodWidget = ref(null)
const clientKey = ref(config.public.TOSS_CLIENT_KEY)
const amount = ref(route.query.amount ? Number(route.query.amount) : 0)
const inputEnabled = ref(false)

async function requestPayment() {
  try {
    if (paymentWidget.value) {
      await paymentWidget.value.requestPayment({
        orderId: nanoid(),
        orderName: "JobStick 멤버십 구독",
        customerName: "사용자",
        customerEmail: "user@example.com",
        customerMobilePhone: "01012341234",
        successUrl: `${window.location.origin}/payment/success`,
        failUrl: `${window.location.origin}/payment/fail`
      })
    }
  } catch (error) {
    console.error("❌ 결제 요청 실패:", error)
  }
}

onMounted(async () => {
  paymentWidget.value = await loadPaymentWidget(clientKey.value, ANONYMOUS)
  paymentMethodWidget.value = paymentWidget.value.renderPaymentMethods(
    "#payment-method",
    { value: amount.value },
    { variantKey: "DEFAULT" }
  )
  paymentWidget.value.renderAgreement("#agreement", { variantKey: "AGREEMENT" })
  paymentMethodWidget.value.on("ready", () => {
    inputEnabled.value = true
    console.log("✅ Toss 위젯 렌더링 완료")
  })
})
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: center;
  padding-top: 60px;
}
.box_section {
  width: 600px;
}
</style>
