import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "githubAuthentication",
    configKey: "githubAuthentication",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    nuxt.hook("pages:extend", (pages) => {
      pages.push({
        name: "githubRedirection",
        path: "/github-oauth/redirect-access-token",
        file: resolve(
          themeDir,
          "githubAuthentication/redirection/GithubRedirection.vue"
        ),
      });
    });

    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store"));
    });
  },
});
