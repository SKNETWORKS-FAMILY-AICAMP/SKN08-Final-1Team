import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "admin",
		configKey: "admin",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push({
                name: 'AdminDefaultPage',
                path: '/admin/default',
                file: resolve(themeDir, 'admin/pages/default/admin-default.vue'),
            });

			pages.push({
                name: 'GithubActionsPage',
                path: '/admin/monitoring',
                file: resolve(themeDir, 'admin/pages/github-actions/github-actions.vue'),
            });

			pages.push({
				name: 'WorkflowSettingsPage',
				path: '/admin/workflow-settings',
				file: resolve(themeDir, 'admin/pages/github-actions/workflow-settings.vue'),
			});
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});