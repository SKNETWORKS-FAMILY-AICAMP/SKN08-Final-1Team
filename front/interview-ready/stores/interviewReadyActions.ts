import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios";
import { useInterviewReadyStore } from "./interviewReadyStore";


export const interviewReadyAction = {
    async requestInterviewReadyIdToDjango(userToken: string): Promise<any> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        try {
            const res: AxiosResponse = await djangoAxiosInstance.post(
                "/interview/", // backend에서 interviewReady에 대한 모델 호출
                { userToken }
            );
            return res.data.interviewReadyId;
        } catch (error) {
            console.error("requestInterviewReadyIdToDjango() axios 오류!", error);
        }
    },
    async requestBackendSkillsToDjango(skills: string): Promise<any> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        const InterviewReadyStore = useInterviewReadyStore();
        try {
            const res: AxiosResponse = await djangoAxiosInstance.post(
                "/interview/",   // backend에서 backendskills에 해당하는 모델 경로,
                skills
            );
            InterviewReadyStore. = res.data;    // 식별자가 필요합니다. 
        } catch (error) {
            console.error("requestInterviewReadyToDjango() 문제 발생: ", error);
            throw error;
        }
    },
    

}