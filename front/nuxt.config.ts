import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  app: {
    head: {
      // title: 'JOBSTICK',
      titleTemplate: "%s JOBSTICK",
      meta: [
        // 페이지 인코딩 설정
        { charset: "utf-8" },

        // 뷰포트 설정
        {
          name: "viewport",
          content:
            "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
        },

        // 페이지 설명
        {
          name: "description",
          content:
            "JOBSTICK - AI 모의 기술 면접을 통해 취업 경쟁력을 높이세요!",
        },

        // SEO 키워드 설정
        {
          hid: "keywords",
          name: "keywords",
          content:
            "취업 준비, 면접 준비, 개발자 취업 준비, 개발자 이직 준비, 개발자 자소서, 개발자 취업 사이트, it취업, it 회사, 기업 분석 사이트, 기업 분석 보고서 사이트, 사업 요약, dart 분석, 다트 분석, 재무 분석, 사업 분석, 주사업, 사업 현황, 사업내용, 기업 분석 및 사업 요약, 다트 재무 분석, 사업 분석 및 요약, 기업 분석 사이트, 사업 요약 사이트, 기업 재무 제표 분석 사이트, 기업 타당성 분석, 모의면접, ai 모의면접, 인성면접, ai 인성면접, 인적성 검사 준비, ai 인적, ai 면접, 회사소개, 회사 사업 소개, DART 분석, 지원동기 작성, aiv 기업 요약 사이트, 에임 기업 요약 사이트, aiv 모의면접, aiv ai 모의면접, 에임 모의면접, 에임, 애임, JOBSTICK, JOBSTICK 기업 분석, JOBSTICK 기업 요약",
        },

        // Open Graph Title : 페이지가 SNS에서 공유될 때 표시될 제목 설정
        {
          property: "og:title",
          content: "JOBSTICK | 기업 핵심 정보 분석 및 AI 모의면접",
        },

        // Open Graph Description : SNS에서 페이지가 공유될 때 표시될 설명을 제공
        {
          property: "og:description",
          content:
            "귀찮았던 기업 분석, 나 혼자 하기 힘든 면접 준비 JOBSTICK이 도와드리겠습니다!",
        },

        // Open Graph Image : 소셜 미디어에서 페이지가 공유될 때 함께 표시될 이미지를 지정
        {
          property: "og:image",
          content: "./public/favicon.png",
        },

        // Open Graph Type : 컨텐츠의 유형을 정의
        {
          property: "og:type",
          content: "website",
        },

        // robots : 검색 엔진 크롤러에게 페이지의 인덱싱과 링크 추적 허용 여부를 지시
        {
          hid: "robots",
          name: "robots",
          content: "index, follow",
        },
      ],
      link: [
        { rel: "icon", type: "image/png", href: "/favicon.png" }, // favicon 설정
      ],
    },
  },

  // pages:true,
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  extends: [
    "./ai-interview/nuxt.config.ts",
    "./account/nuxt.config.ts",
    "./kakaoAuthentication/nuxt.config.ts",
    "./naverAuthentication/nuxt.config.ts",
    "./review/nuxt.config.ts",
    "./company-report/nuxt.config.ts",
    "./googleAuthentication/nuxt.config.ts",
    "./cart/nuxt.config.ts",
    "./order/nuxt.config.ts",
    "./payments/nuxt.config.ts",
    "./management/nuxt.config.ts",
    "./githubAuthentication/nuxt.config.ts",
    "./authentication/nuxt.config.ts",
    "./interview-ready/nuxt.config.ts",
    "./guestAuthentication/nuxt.config.ts",
    "./admin/nuxt.config.ts",
  ],
  css: [
    "vuetify/styles",
    "@mdi/font/css/materialdesignicons.min.css",
    "@/assets/css/global.css", // ✅ 너가 만든 global.css 추가
  ],

  build: {
    transpile: ["vuetify"], // Vuetify를 빌드 시 트랜스파일링
  },

  vite: {
    optimizeDeps: {
      include: ["@tosspayments/payment-widget-sdk"],
    },
    ssr: {
      noExternal: ["vuetify"], // SSR에서도 Vuetify를 외부 패키지로 처리하지 않도록 설정
    },
  },

  modules: [
    "vuetify-nuxt-module",
    "@pinia/nuxt",
    "~/ai-interview/index.ts",
    "~/account/index.ts",
    "~/kakaoAuthentication/index.ts",
    "~/naverAuthentication/index.ts",
    "~/review/index.ts",
    "~/company-report/index.ts",
    "~/googleAuthentication/index.ts",
    "~/cart/index.ts",
    "~/order/index.ts",
    "~/payments/index.ts",
    "~/management/index.ts",
    "~/githubAuthentication/index.ts",
    "~/authentication/index.ts",
    "~/interview-ready/index.ts",
    "~/guestAuthentication/index.ts",
    "~/admin/index.ts",
  ],
  components: {
    dirs: [
      "~/components", // 기본 컴포넌트 경로
      "~/navigationBar", // 파일 경로가 아닌 디렉터리 경로로 수정
    ],
  },
  imports: {
    dirs: ["./stores"],
  },

  runtimeConfig: {
    public: {
      MAIN_API_URL: process.env.VUE_APP_BASE_URL,
      AI_BASE_URL: process.env.VUE_APP_AI_BASE_URL,
      AWS_REGION: process.env.VUE_APP_AWS_REGION,
      AWS_S3_IDENTITY_POOL: process.env.VUE_APP_AWS_S3_IDENTITY_POOL_ID,
      VUE_APP_AWS_S3_BUCKET_NAME: process.env.VUE_APP_AWS_S3_BUCKET_NAME,
      GA_MEASUREMENT_ID: process.env.VUE_APP_GA_MEASUREMENT_ID,
      TOSS_CLIENT_KEY: process.env.TOSS_CLIENT_KEY,
      TOSS_SECRET_KEY: process.env.TOSS_SECRET_KEY,
    },
  },

  plugins: [{ src: "~/plugins/vgtag.js", mode: "client" }],
});
