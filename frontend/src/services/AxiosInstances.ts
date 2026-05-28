import axios, { AxiosResponse, InternalAxiosRequestConfig } from "axios";
import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { config } from "../config";

/**
 * ЕДИНАЯ точка входа:
 * frontend → /api/v1 → ingress → gateway-service → микросервисы
 */
export const api = axios.create({
  baseURL: config.api.baseUrl,
});

// ======================
// 🔐 REQUEST INTERCEPTOR
// ======================
api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const token = localStorage.getItem("accessToken");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

// ======================
// 🔁 RESPONSE INTERCEPTOR (REFRESH TOKEN)
// ======================
api.interceptors.response.use(
  (response: AxiosResponse) => response,
  async (error) => {
    const originalRequest = error.config;

    if (!error.response) {
      return Promise.reject(error);
    }

    if (
      error.response.status === 401 &&
      originalRequest &&
      !originalRequest._isRetry
    ) {
      originalRequest._isRetry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");

        const response = await axios.post<IAuthResponse>(
          `${config.api.baseUrl}/user/refresh/`,
          {
            refresh_token: refreshToken,
          }
        );

        const newAccessToken = response.data.access_token;

        if (!newAccessToken) {
          localStorage.clear();
          return Promise.reject("No access token in refresh response");
        }

        localStorage.setItem("accessToken", newAccessToken);

        originalRequest.headers = originalRequest.headers ?? {};
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

        return api.request(originalRequest);
      } catch (e) {
        localStorage.clear();
        return Promise.reject(e);
      }
    }

    return Promise.reject(error);
  }
);