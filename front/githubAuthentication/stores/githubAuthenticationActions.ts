import * as axiosUtility from "../../utility/axiosInstance"

export const githubAuthenticationAction = {
    async requestAdminCodeToDjango(adminCode: string): Promise<boolean> {
        console.log("requestAdminCodeToDjango")
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            const response = await djangoAxiosInstance.post('/github-oauth/request-admin-code-validation', {
                admin_code: adminCode  // 데이터로 adminCode를 보내는 방식
            });

            console.log('response:', response)
            console.log('response,data:', response.data)
    
            return response.data.isValid;
        } catch (error) {
            console.error('관리자 코드 검증 실패:', error);
            return false;
        }
    },
    async requestGithubLoginToDjango(): Promise<void> {
        console.log("requestGithubLoginToDjango")
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            return djangoAxiosInstance.get('/github-oauth/request-login-url').then((res) => {
                console.log(`res: ${res}`)
                window.location.href = res.data.url
            })
        } catch (error) {
            console.log('requestGithubLoginToDjango() 중 에러:', error)
        }
    },
    async requestAccessToken(code: string): Promise<string | null> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        try {
            const response = await djangoAxiosInstance.post('/github-oauth/redirect-access-token', code)
            return response.data.userToken
        } catch(error){
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },


    async requestLogout(userToken: string): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            await djangoAxiosInstance.post('/authentication/logout', { userToken })
        } catch (error) {
            console.log('requestLogout() 중 에러:', error)
        }
    },
    async requestValidationUserToken(userToken: string): Promise<boolean> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            const response = await djangoAxiosInstance.post('/authentication/validation', { userToken })

            if (response.data && response.data.valid !== undefined) {
                return response.data.valid;
            } else {
                console.error('Invalid response structure:', response.data);
                return false;
            }
        } catch (error) {
            console.log('requestLogout() 중 에러:', error)
            return false
        }
    }
}