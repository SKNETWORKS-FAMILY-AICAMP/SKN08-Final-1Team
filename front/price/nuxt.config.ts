// nuxt.config.ts
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  modules: [
    '@pinia/nuxt'
  ],
  imports: {
    dirs: ['stores', 'price/stores'] // userPriceStore.js 경로 인식
  },
  components: true,
})
