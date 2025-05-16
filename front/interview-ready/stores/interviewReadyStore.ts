import { defineStore } from "pinia";
import { interviewReadyState } from "./interviewReadyState";
import { interviewReadyAction } from "./interviewReadyActions";


export const useInterviewReadyStore = defineStore("interviewReadyStore", {
    state: interviewReadyState,
    actions: interviewReadyAction,
});