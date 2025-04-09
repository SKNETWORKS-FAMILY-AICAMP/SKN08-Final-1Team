import { defineStore } from "pinia";
import { naverAuthenticationState } from "./naverAuthenticationState";
import { naverAuthenticationAction } from "./naverAuthenticationActions";

export const useNaverAuthenticationStore = defineStore(
  "naverAuthenticationStore",
  {
    state: naverAuthenticationState,
    actions: naverAuthenticationAction,
  }
);
