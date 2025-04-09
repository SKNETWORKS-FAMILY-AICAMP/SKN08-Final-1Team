import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "naverAuthentication",
    configKey: "naverAuthentication",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    nuxt.hook("pages:extend", (pages) => {
      pages.push({
        name: "naverRedirection",
        path: "/naver-oauth/redirect-access-token",
        file: resolve(
          themeDir,
          "naverAuthentication/redirection/NaverRedirection.vue"
        ),
      });
    });

    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store"));
    });
  },
});
