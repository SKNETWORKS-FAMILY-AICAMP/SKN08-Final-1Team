import * as axiosUtility from "../../utility/axiosInstance";

export const naverAuthenticationAction = {
  async requestNaverLoginToDjango(): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res = await djangoAxiosInstance.get(
        "/naver-oauth/request-login-url"
      );
      console.log("res.data:", res.data);

      if (!res.data?.url) {
        throw new Error("응답에 URL이 없습니다.");
      }

      window.location.href = res.data.url;

      // try-catch 블록은 .then() 안에 있는 promise 체인과 섞여 실제 에러가
      // try-catch로 잡히지 않을 수 있습니다.
      // return djangoAxiosInstance
      //   .get("/naver-oauth/request-login-url")
      //   .then((res) => {
      //     console.log(`res: ${res}`);
      //     window.location.href = res.data.url;
      //   });
    } catch (error) {
      console.log("requestNaverOauthRedirectionToDjango() 중 에러:", error);
      throw error; // 상위 함수에서 에러가 잡히도록 재전파
    }
  },

  async requestAccessToken(
    code: string,
    state: string
  ): Promise<string | null> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      console.log("보내는 데이터:", { code, state });
      const response = await djangoAxiosInstance.post(
        "/naver-oauth/redirect-access-token",
        { code, state }
      );
      return response.data.userToken;
    } catch (error) {
      console.log("Access Token 요청 중 문제 발생:", error);
      throw error;
    }
  },

  async requestNaverWithdrawToDjango(): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    const userToken = localStorage.getItem("userToken");
    try {
      const res = await djangoAxiosInstance.post(
        `/naver-oauth/request-withdraw-url`,
        {},
        { headers: { Authorization: `Bearer ${userToken}` } }
      );
      console.log("네이버 탈퇴 응답:", res.data);

      if (res.data && res.data.message === "네이버 연결 해제 성공") {
        alert("네이버 계정 탈퇴가 완료되었습니다.");
        window.location.href = "/"; // 탈퇴 후 홈으로 이동
      } else {
        console.error("❌ 탈퇴 실패 - 잘못된 응답:", res.data);
      }
    } catch (error) {
      console.error("🚨 네이버 탈퇴 요청 중 오류 발생:", error);
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
