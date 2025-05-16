import { defineStore } from "pinia";
import { guestAuthenticationState } from "./guestAuthenticationState";
import { guestAuthenticationAction } from "./guestAuthenticationActions";

export const useGuestAuthenticationStore = defineStore(
  "guestAuthenticationStore",
  {
    state: guestAuthenticationState,
    actions: guestAuthenticationAction,
  }
);
