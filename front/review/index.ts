import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "review",
		configKey: "review",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "ReviewRegisterPage",
					path: "/review/register",
					file: resolve(
						themeDir,
						"review/pages/register/ReviewRegisterPage.vue"
					),
				},
                {
					name: "reviewReadPage",
					path: "/review/read/:randomString",
					file: resolve(themeDir, "review/pages/read/ReviewReadPage.vue"),
				},
                {
                    name: 'ReviewCreatedPage',
                    path: '/review/created',
                    file: resolve(themeDir, "review/pages/created/ReviewCreatedPage.vue"),
                },            
                {
					name: "ReviewListPage",
					path: "/review/list",
					file: resolve(themeDir, "review/pages/list/ReviewListPage.vue"),
				},			
				{
                    name: 'ReviewSubmittedPage',
                    path: '/review/submitted',                    
                    file: resolve(themeDir, "review/pages/submitted/ReviewSubmittedPage.vue"),
                },
                {
                    name: 'ReviewResultPage',
                    path: '/review/result/:reviewId',                    
                    file: resolve(themeDir, "review/pages/result/ReviewResultPage.vue"),
                }
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});