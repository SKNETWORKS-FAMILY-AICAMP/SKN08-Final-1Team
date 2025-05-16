import * as axiosUtility from "../../utility/axiosInstance";
import axios from 'axios'
import type { AxiosResponse } from 'axios'  // ✅ 타입만 import
import { useAiInterviewStore } from "./aiInterviewStore";

// ✅ 회사명 매핑 유틸
const mapCompanyName = (original: string): string => {
  const mapping: Record<string, string> = {
    당근마켓: "danggeun",
    Toss: "toss",
    "SK-encore": "sk_encore",
    "KT M mobile": "kt_mobile",
  };
  return mapping[original] || original.toLowerCase().replace(/[\s-]+/g, "_");
};

export const aiInterviewActions = {
  //첫 질문
  async requestCreateInterviewToDjango(payload: {
    userToken: string;
    jobCategory: number; // 직무
    experienceLevel: number; // 경력
    projectExperience: number; // 프로젝트 경험 여부
    academicBackground: number; // 전공 여부
    interviewTechStack: number[]; // 기술
    interviewId: number;
    companyName: string;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const transformedPayload = {
      ...payload,
      companyName: mapCompanyName(payload.companyName),
    };

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/create",
        transformedPayload
      );
      return res.data;
    } catch (err) {
      console.error("requestCreateInterviewToDjango() -> error:", err);
      throw err;
    }
  },

  async requestListInterviewToDjango(
    userToken: string,
    page: number = 1,
    perPage: number = 10
  ): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/list",
        { userToken, page, perPage }
      );
      return res.data;
    } catch (err) {
      console.error("requestListInterviewToDjango() → error:", err);
      throw err;
    }
  },

  async requestRemoveInterviewToDjango(payload: {
    userToken: string;
    interviewId: number;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/remove",
        {
          payload,
        }
      );
      return res.data;
    } catch (error) {
      console.error("requestRemoveInterviewToDjango() → error:", error);
      throw error;
    }
  },

  //응답 생성
  async requestCreateAnswerToDjango(payload: {
    userToken: string;
    interviewId: number;
    questionId: number;
    answerText: string;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/user-answer", // ✅ 이걸로 고쳐야 정상 작동
        payload
      );

      return res.data;
    } catch (err) {
      console.error("답변 저장 중 오류:", err);
      throw err;
    }
  },

  //첫 질문에 대한 심화질문
  async requestFollowUpQuestionToDjango(payload: {
    jobCategory: number;
    experienceLevel: number;
    academicBackground: number;
    projectExperience: number;
    userToken: string;
    interviewId: number;
    questionId: number;
    answerText: string;
    companyName: string;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const transformedPayload = {
      ...payload,
      companyName: mapCompanyName(payload.companyName),
    };

    try {
      console.log(payload);
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/followup", // 백엔드 Django가 저장하고 FastAPI 호출
        transformedPayload
      );
      return res.data;
    } catch (error) {
      console.error("requestFollowUpQuestionToDjango() → error:", error);
      throw error;
    }
  },

  // 두번째 질문
  async requestProjectCreateInterviewToDjango(payload: {
    userToken: string;
    jobCategory: number; // 직무
    experienceLevel: number; // 경력
    projectExperience: number; // 프로젝트 경험 여부
    academicBackground: number; // 전공 여부
    interviewTechStack: number[]; // 기술
    interviewId: number;
    questionId: number;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/project-create",
        payload
      );
      console.log(res.data.question);
      return res.data;
    } catch (err) {
      console.error("requestProjectCreateInterviewToDjango() -> error:", err);
      throw err;
    }
  },

  // 두번째 심화질문
  async requestProjectFollowUpQuestionToDjango(payload: {
    jobCategory: number;
    projectExperience: number;
    experienceLevel: number;
    interviewTechStack: number[]; // 기술
    userToken: string;
    interviewId: number;
    questionId: number;
    answerText: string;
    companyName: string;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const transformedPayload = {
      ...payload,
      companyName: mapCompanyName(payload.companyName),
    };

    try {
      console.log(payload);
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/project-followup", // 백엔드 Django가 저장하고 FastAPI 호출
        transformedPayload
      );
      return res.data;
    } catch (error) {
      console.error("requestFollowUpQuestionToDjango() → error:", error);
      throw error;
    }
  },

  // 세번째 심화질문
  async requestTechFollowUpQuestionToDjango(payload: {
    interviewTechStack: number[]; // 기술
    userToken: string;
    interviewId: number;
    questionId: number;
    answerText: string;
  }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const transformedPayload = {
      ...payload,
    };

    try {
      console.log(payload);
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview/tech-followup", // 백엔드 Django가 저장하고 FastAPI 호출
        transformedPayload
      );
      return res.data;
    } catch (error) {
      console.error("requestTechFollowUpQuestionToDjango() → error:", error);
      throw error;
    }
  },

  async requestGetScoreResultListToDjango(payload: {
    userToken: string;
    interviewId: number;
    jobCategory: number;
    experienceLevel: number;
    projectExperience: number;
    academicBackground: number;
    interviewTechStack: number[];
  }): Promise<string> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview_result/request-interview-summary",
        payload
      );
      return res.data.interviewResultList;
    } catch (error) {
      console.log("requestGetScoreResultListToDjango() 중 문제 발생:", error);
      throw error;
    }
  },

  //인터뷰 결과 저장
  async requestGetInterviewResultToDjango(payload: {
    userToken: string;
  }): Promise<string> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview_result/get-interview-result",
        payload
      );
      return res.data;
    } catch (error) {
      console.log("requestSaveInterviewResultToDjango() 중 문제 발생:", error);
      throw error;
    }
  },
  //면접 종료
  async requestEndInterviewToDjango(payload: {
    userToken: string;
    interviewId: number;
    companyName: string;
  }): Promise<string> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const transformedPayload = {
      ...payload,
      companyName: mapCompanyName(payload.companyName),
    };

    try {
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/interview_result/end-interview",
        transformedPayload
      );
      return res.data;
    } catch (error) {
      console.log("requestSaveInterviewResultToDjango() 중 문제 발생:", error);
      throw error;
    }
  },
};
