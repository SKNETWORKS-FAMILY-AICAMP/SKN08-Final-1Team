import { defineStore } from "pinia";
import { googleAuthenticationState } from "./googleAuthenticationState";
import { googleAuthenticationAction } from "./googleAuthenticationActions";

export const useGoogleAuthenticationStore = defineStore(
  "googleAuthenticationStore",
  {
    state: googleAuthenticationState,
    actions: googleAuthenticationAction,
  }
);
