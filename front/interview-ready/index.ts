import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
    meta: {
        name: "interviewReady",
        configKey: "interviewReady",
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, "..");

        nuxt.hook("pages:extend", (pages) => {
            pages.push(
                {
                    name: "InterviewReadyCategoryPage",
                    path: "/interview-ready/category",
                    file: resolve(themeDir, "interview-ready/pages/category/interview-ready-category.vue"),
                },
                {
                    name: "InterviewReadyBackendSkillsPage",
                    path: "/interview-ready/skills",   // 경로를 수정할 필요가 있습니다.
                    file: resolve(themeDir, "interview-ready/pages/skills/interview-ready-backend-skills.vue")
                },

            )
        });
    },
});