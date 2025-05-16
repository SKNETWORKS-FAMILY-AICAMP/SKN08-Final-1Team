import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "account",
    configKey: "account",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    nuxt.hook("pages:extend", (pages) => {
      pages.push(
        {
          name: "AccountLoginPage",
          path: "/account/login",
          file: resolve(themeDir, "account/pages/login/account-login.vue"),
        },
        {
          name: "AccountMyPage",
          path: "/account/mypage",
          file: resolve(themeDir, "account/pages/my/account-my.vue"),
        },
        {
          name: "AccountWithdrawPage",
          path: "/account/withdraw",
          file: resolve(
            themeDir,
            "account/pages/withdraw/account-withdraw.vue"
          ),
        },
        {
          name: "AdminCodeInputPage",
          path: "/account/admin-code",
          file: resolve(
            themeDir,
            "account/pages/admin-login/admin-code-input.vue"
          ),
        },

        {
          name: "GithubAdminLoginPage",
          path: "/account/admin-login",
          file: resolve(
            themeDir,
            "account/pages/admin-login/github-admin-login.vue"
          ),
        },
        {
          name: "PrivacyAgreementPage",
          path: "/account/privacy",
          file: resolve(themeDir, "account/pages/login/privacy-agreement.vue"),
        }
      );
    });
    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store"));
    });
  },
});
