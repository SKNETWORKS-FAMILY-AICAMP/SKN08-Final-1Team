import * as axiosUtility from "../../utility/axiosInstance";

export const kakaoAuthenticationAction = {
  async requestKakaoLoginToDjango(): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      // try-catch 블록은 .then() 안에 있는 promise 체인과 섞여 실제 에러가
      // try-catch로 잡히지 않을 수 있습니다. 
      const res = await djangoAxiosInstance.get("/kakao-oauth/request-login-url");
      console.log("res.data:", res.data);

      if (!res.data?.url) {
        throw new Error("응답에 URL이 없습니다.");
      }

      window.location.href = res.data.url;
      
      // return djangoAxiosInstance
      //   .get("/kakao-oauth/request-login-url")
      //   .then((res) => {
      //     console.log(`res: ${res}`);
      //     window.location.href = res.data.url;
      //   });
    } catch (error) {
      console.log("requestKakaoOauthRedirectionToDjango() 중 에러:", error);
      throw error;  // 상위 함수에서 에러가 잡히도록 재전파합니다. 
    }
  },

  async requestKakaoWithdrawToDjango(): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    const userToken = localStorage.getItem("userToken");
    try {
      const res = await djangoAxiosInstance.post(
        `/kakao-oauth/request-withdraw-url`,
        {},
        { headers: { Authorization: `Bearer ${userToken}` } }
      );
      console.log("카카오 탈퇴 응답:", res.data);

      if (res.data && res.data.url && res.data.url.id) {
        alert("카카오 계정 탈퇴가 완료되었습니다.");
        window.location.href = "/"; // 탈퇴 후 홈으로 이동
      } else {
        console.error("❌ 탈퇴 실패 - 잘못된 응답:", res.data);
      }
    } catch (error) {
      console.error("🚨 카카오 탈퇴 요청 중 오류 발생:", error);
    }
  },

  async requestAccessToken(code: string): Promise<string | null> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const response = await djangoAxiosInstance.post(
        "/kakao-oauth/redirect-access-token",
        code
      );
      return response.data.userToken;
    } catch (error) {
      console.log("Access Token 요청 중 문제 발생:", error);
      throw error;
    }
  },
  async requestLogout(userToken: string): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      await djangoAxiosInstance.post("/authentication/logout", { userToken });
    } catch (error) {
      console.log("requestLogout() 중 에러:", error);
    }
  },
  async requestValidationUserToken(userToken: string): Promise<boolean> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const response = await djangoAxiosInstance.post(
        "/authentication/validation",
        { userToken }
      );

      if (response.data && response.data.valid !== undefined) {
        return response.data.valid;
      } else {
        console.error("Invalid response structure:", response.data);
        return false;
      }
    } catch (error) {
      console.log("requestLogout() 중 에러:", error);
      return false;
    }
  },
};
