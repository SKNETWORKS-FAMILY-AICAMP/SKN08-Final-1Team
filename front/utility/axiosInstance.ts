// 서버에 요청을 보내는 도메인
import axios, { type AxiosInstance } from "axios";
import { useRuntimeConfig } from "nuxt/app";
export let djangoAxiosInstance: AxiosInstance | null = null;
export let fastapiAxiosInst: AxiosInstance | null = null;

export function createAxiosInstances() {
  const config = useRuntimeConfig();

  const mainApiUrl: string = config.public.MAIN_API_URL as string;
  const aiBaseUrl: string = config.public.AI_BASE_URL as string;

  if (!djangoAxiosInstance) {
    djangoAxiosInstance = axios.create({
      baseURL: mainApiUrl,
      timeout: 40000,
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  if (!fastapiAxiosInst) {
    fastapiAxiosInst = axios.create({
      baseURL: aiBaseUrl,
      timeout: 20000,
    });
  }

  return { djangoAxiosInstance, fastapiAxiosInst };
}
