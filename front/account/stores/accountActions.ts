import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios";
import { useAccountStore } from "./accountStore";

export const accountAction = {
  async requestAccountIdToDjango(userToken: string): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/account/request-email",
        { userToken }
      );
      return res.data.accountId;
    } catch (error) {
      console.error("requestAccountIdToDjango() axios 오류!", error);
    }
  },
  async requestWithdrawalToDjango(payload: {
    reason: string;
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    const userToken = localStorage.getItem("userToken");
    const { reason } = payload;
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/account/request-withdraw",
        { reason: reason, userToken: userToken }
      );
      return res.data;
    } catch (error) {
      alert("requestWithdrawalToDjango() 문제 발생!");
      throw error;
    }
  },
  //user정보 요청
  async requestProfileToDjango(payload: {
    email: string;
    nickname: string;
    gender: string;
    birthyear: number;
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    const userToken = localStorage.getItem("userToken");
    const accountStore = useAccountStore();

    try {
      const userInfo: AxiosResponse = await djangoAxiosInstance.post(
        "/account_profile/request-info",
        {
          userToken,
          //email: payload.email,
          //nickname: payload.nickname,
          //gender: payload.gender,
          //birthyear: payload.birthyear,
        }
      );

      // 받은 데이터를 Pinia store에 저장
      accountStore.email = userInfo.data.email;
      accountStore.nickname = userInfo.data.nickname;
      accountStore.gender = userInfo.data.gender;
      accountStore.birthyear = userInfo.data.birthyear;

      return userInfo;
    } catch (error) {
      console.error("requestProfileToDjango() 문제 발생:", error);
      throw error;
    }
  },
};
