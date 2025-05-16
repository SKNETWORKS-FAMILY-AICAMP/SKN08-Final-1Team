<template>
  <div class="wrapper">
    <div class="box_section">
      <!-- 결제 UI -->
      <div id="payment-method"></div>

      <!-- 이용약관 UI -->
      <div id="agreement"></div>

      <!-- 쿠폰 체크박스 (주석 처리됨) -->
      <!--
      <div style="padding-left: 33px">
        <div class="checkable typography--p">
          <label for="coupon-box" class="checkable__label typography--regular">
            <input :disabled="!inputEnabled" @change="updateAmount" id="coupon-box" class="checkable__input"
              type="checkbox" aria-checked="true" />
            <span class="checkable__label-text"> 5원 쿠폰 적용</span>
          </label>
        </div>
      </div>
      -->

      <!-- 결제하기 버튼 -->
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

// ✅ SEO 메타 정보
definePageMeta({
  title: "결제하기 | JobStick",
  description: "JobStick 서비스를 결제하여 더 많은 서비스를 누려보세요.",
  keywords: ["결제", "결제하기", "JobStick", "잡스틱", "서비스", "혜택", "job-stick"],
  ogTitle: "JobStick 결제하기",
  ogDescription: "JobStick 결제하기 페이지입니다. 더 많은 서비스와 혜택을 누려보세요.",
  ogImage: "",
  robots: "index, follow"
})

// ✅ 컴포넌트 상태 변수 정의
const config = useRuntimeConfig()
const route = useRoute()

const paymentWidget = ref(null)
const paymentMethodWidget = ref(null)
const clientKey = ref(config.public.TOSS_CLIENT_KEY)
const customerKey = ref(null)
const amount = ref(route.query.amount ? Number(route.query.amount) : 0)
const inputEnabled = ref(false)
const discountCouponAmount = ref(5)

// ✅ 결제 요청 함수
async function requestPayment() {
  try {
    if (paymentWidget.value) {
      await paymentWidget.value.requestPayment({
        orderId: nanoid(),
        orderName: "AIM",
        customerName: "AIM-sniper",
        customerEmail: "abcdabcd@gmail.com",
        customerMobilePhone: "01012341234",
        successUrl: `${window.location.origin}/payment/success`,
        failUrl: `${window.location.origin}/payment/fail`
      })
    }
  } catch (error) {
    console.error(error)
  }
}

// ✅ 쿠폰 할인 반영 함수 (필요 시 활성화)
async function updateAmount() {
  const coupon = document.getElementById("coupon-box")
  if (coupon?.checked) {
    amount.value -= discountCouponAmount.value
  }
  paymentMethodWidget.value?.updateAmount(amount.value)
}

// ✅ 위젯 로딩
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
