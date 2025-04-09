import { defineStore } from "pinia";
import { reviewState } from "./reviewState";
import { reviewActions } from "./reviewActions";

export const useReviewStore = defineStore("reviewStore", {
  state: reviewState,
  actions: reviewActions,
});
