import { defineStore } from "pinia";
import { githubAuthenticationState } from "./githubAuthenticationState";
import { githubAuthenticationAction } from "./githubAuthenticationActions";

export const useGithubAuthenticationStore = defineStore(
  "githubAuthenticationStore",
  {
    state: githubAuthenticationState,
    actions: githubAuthenticationAction,
  }
);
