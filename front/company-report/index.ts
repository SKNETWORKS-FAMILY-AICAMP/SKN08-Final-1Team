import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from 'path';

export default defineNuxtModule({
    meta: {
        name: 'CompanyReportPage',
        configKey: 'CompanyReportPage',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..')

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'CompanyReportPage',
                path: '/company-report/list',
                file: resolve(themeDir, 'company-report/pages/list/company-report-list.vue'),
            },
            {
                name: 'CompanyReportReadPage',
                path: '/company-report/read/:id',
                file: resolve(themeDir, 'company-report/pages/read/company-report-read.vue'),
            },
            {
                name: 'CompanyReportModifyPage',
                path: '/company-report/modify/:id',
                file: resolve(themeDir, 'company-report/pages/modify/company-report-modify.vue'),
            }
            )
        })

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'))
        })
    },
})