<template>
  <v-container class="media-check-container" align="center">
    <h2>🎤 카메라 & 마이크 확인</h2>

    <!-- ✅ 카메라 확인 -->
    <video
      ref="videoRef"
      autoplay
      playsinline
      muted
      style="width: 400px; height: 300px; margin-top: 20px; border: 2px solid #ccc;"
    />

    <!-- ✅ 마이크 녹음 버튼 -->
    <div style="margin-top: 24px;">
      <v-btn color="primary" @click="startRecording" :disabled="isRecording">
        ⏺ 녹음 시작
      </v-btn>
      <v-btn color="warning" @click="stopRecording" :disabled="!isRecording">
        ⏹ 녹음 종료
      </v-btn>
      <v-btn color="success" @click="playRecording" :disabled="!audioUrl">
        ▶️ 재생
      </v-btn>
    </div>

    <!-- ✅ 완료 -->
    <v-btn class="mt-6" color="primary" @click="goBack">확인 완료</v-btn>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const videoRef = ref(null)
const router = useRouter()

// ✅ 녹음 관련
let mediaRecorder = null
const audioChunks = ref([])
const isRecording = ref(false)
const audioUrl = ref('')
let audioBlob = null

const startRecording = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false })
  audioChunks.value = []
  mediaRecorder = new MediaRecorder(stream)

  mediaRecorder.ondataavailable = (e) => {
    if (e.data.size > 0) {
      audioChunks.value.push(e.data)
    }
  }

  mediaRecorder.onstop = () => {
    audioBlob = new Blob(audioChunks.value, { type: 'audio/webm' })
    audioUrl.value = URL.createObjectURL(audioBlob)
  }

  mediaRecorder.start()
  isRecording.value = true
}

const stopRecording = () => {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop()
    isRecording.value = false
  }
}

const playRecording = () => {
  if (audioUrl.value) {
    const audio = new Audio(audioUrl.value)
    audio.play()
  }
}

onMounted(() => {
  // 카메라 미리 보기
  navigator.mediaDevices.getUserMedia({ video: true, audio: false }).then((stream) => {
    if (videoRef.value) {
      videoRef.value.srcObject = stream
    }
  }).catch(() => {
    alert('카메라 접근 실패. 브라우저 권한을 확인해 주세요.')
  })
})

const goBack = () => {
  router.push('/ai-test') // 면접 시작 페이지로 돌아가기
}
</script>

<style scoped>
.media-check-container {
  margin-top: 80px;
}
</style>
