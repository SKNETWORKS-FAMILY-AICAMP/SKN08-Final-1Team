import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "aiInterview",
    configKey: "aiInterview",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    nuxt.hook("pages:extend", (pages) => {
      pages.push(
        {
          name: "AiInterviewPage",
          path: "/ai-test",
          file: resolve(themeDir, "ai-interview/pages/ai-interview.vue"),
        },

        {
          name: "AIInterviewLLMTestPage",
          path: "/ai-interview/llm-test",
          file: resolve(
            themeDir,
            "ai-interview/pages/llm-test/ai-interview-llm.vue"
          ),
        },
        {
          name: "AIInterviewAnswerResult",
          path: "/ai-interview/result",
          file: resolve(
            themeDir,
            "ai-interview/pages/result/ai-interview-answer-result.vue"
          ),
        }
      );
    });

    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "stores"));
    });
  },
});
