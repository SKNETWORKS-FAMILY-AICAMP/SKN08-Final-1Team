<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted } from 'vue';

const route = useRoute();
const router = useRouter();

onMounted(async () => {
  const { paymentKey, orderId, amount } = route.query;

  try {
    const response = await $fetch('http://localhost:8000/orders/create', {
      method: 'POST',
      body: {
        paymentKey,
        orderId,
        amount,
        // 사용자 인증 토큰이 필요한 경우:
        // userToken: localStorage.getItem("userToken")
      }
    });

    if (response.success) {
      alert("🎉 구독이 생성되었습니다!");
    } else {
      alert("❌ 구독 생성 실패: " + response.message);
    }
  } catch (error) {
    console.error("❌ 주문 생성 오류:", error);
    alert("서버 오류가 발생했습니다.");
  }
});
</script>
