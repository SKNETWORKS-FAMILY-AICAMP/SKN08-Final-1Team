import { AxiosResponse } from "axios";
import * as axiosUtility from "../../utility/axiosInstance";
import { useReviewStore } from "./reviewStore";
import { Review } from "./reviewState";

export const reviewActions = {
  async requestCreateReviewFormToDjango(
    randomString: string
  ): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/creat-form",
        randomString
      );
      return res.data;
    } catch (e) {
      console.error("requestCreateReviewFormToDjango() -> error:", e);
      throw e;
    }
  },

  async requestRegisterTitleAndDescriptionToDjango(payload: {
    reviewId: number;
    reviewTitle: string;
    reviewDescription: string;
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/register-title-description",
        payload
      );
      return res.data;
    } catch (e) {
      console.error(
        "requestRegisterTitleAndDescriptionToDjango() -> error:",
        e
      );
      throw e;
    }
  },

  async requestCreateQuestionToDjango(
    imageFormData: FormData
  ): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/register-question",
        imageFormData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      return res.data;
    } catch (e) {
      console.error("requestCreateQuestionToDjango() -> error:", e);
      throw e;
    }
  },

  async requestRegisterSelectionToDjango(payload: {
    questionId: number;
    selection: string;
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/register-selection",
        payload
      );
      return res.data;
    } catch (e) {
      console.error("requestRegisterSelectionToDjango() -> error:", e);
      throw e;
    }
  },

  async requestReviewListToDjango() {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse<{ reviewTitleList: Review[] }> =
        await djangoAxiosInstance.get("/review/review-title-list");
      this.reviewTitleList = res.data.reviewTitleList;
    } catch (e) {
      console.error("requestReviewListToDjango() -> error:", e);
      throw e;
    }
  },

  async requestReviewFormToDjango(randomString: string) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse<Review> = await djangoAxiosInstance.get(
        `/review/read-review-form/${randomString}`
      );
      this.reviewForm = res.data;
    } catch (e) {
      console.error("requestReviewFormToDjango() -> error:", e);
      throw e;
    }
  },

  async requestSubmitReviewToDjango(payload: {
    submitForm: [];
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/submit-review",
        payload
      );
      return res.data;
    } catch (e) {
      console.error("requestSubmitReviewToDjango() -> error:", e);
      throw e;
    }
  },

  async requestRandomStringToDjango(reviewId: number): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/randomstring",
        reviewId
      );
      return res.data;
    } catch (e) {
      console.error("Django 서버에서 랜덤 문자열을 받아오지 못했습니다:", e);
      return null;
    }
  },

  async requestReviewResultToDjango(reviewId: number) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse<Review> = await djangoAxiosInstance.get(
        `/review/review-result/${reviewId}`
      );
      this.resultForm = res.data;
    } catch (e) {
      console.error("requestReviewResultToDjango() -> error:", e);
      throw e;
    }
  },

  async requestCheckIsFirstSubmit(accountId: {
    accountId: string;
  }): Promise<AxiosResponse> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/review/check-first-submit",
        accountId
      );
      return res.data;
    } catch (e) {
      console.error("requestCheckIsFirstSubmit() -> error:", e);
      throw e;
    }
  },
};
