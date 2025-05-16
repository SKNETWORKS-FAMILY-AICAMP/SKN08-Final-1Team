import * as axiosUtility from "../../utility/axiosInstance";
import type { AxiosResponse } from "axios";

export const reviewActions = {
  async requestReviewListToDjango(this: {
    reviewList: any[];
    totalItems: number;
    totalPages: number;
  }) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.get("/review/list", {
        params: { page: 1, perPage: 8 },
      });

      this.reviewList = res.data.dataList;
      this.totalItems = res.data.totalItems;
      this.totalPages = res.data.totalPages;
      console.log("📦 리뷰 목록 응답 전체:", res.data);
    } catch (error: any) {
      console.error(
        "❌ 리뷰 목록 불러오기 실패:",
        error.response?.data || error.message
      );
      alert("리뷰 목록을 불러오는 데 실패했습니다.");
    }
  },

  async requestSubmitReviewToDjango(this: any, formData: FormData) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      console.log("📤 리뷰 등록 요청 데이터:", this.formData);
      const response: AxiosResponse = await djangoAxiosInstance.post(
        "/review/create",
        formData
      );
      console.log("✅ 리뷰 등록 응답 수신:", response.data);
      alert("리뷰가 성공적으로 등록되었습니다.");
      // ✅ 리뷰 목록 갱신
      await this.requestReviewListToDjango();
    } catch (error: any) {
      console.error(
        "❌ 리뷰 등록 실패:",
        error.response?.data || error.message
      );
      alert("리뷰 등록 중 오류가 발생했습니다.");
    }
  },
};
