import axios, { AxiosResponse, InternalAxiosRequestConfig } from "axios";
import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { config } from "../config";

// Единый экземпляр axios – экспортируем как api, так и старые имена
export const api = axios.create({
  baseURL: config.api.baseUrl,   // "/api/v1"
});

// Интерсептор запроса – добавляем токен
api.interceptors.request.use((cfg: InternalAxiosRequestConfig) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    cfg.headers.Authorization = `Bearer ${token}`;
  }
  return cfg;
});

// Интерсептор ответа – обработка 401
api.interceptors.response.use(
  (response: AxiosResponse) => response,
  async (error) => {
    const originalRequest = error.config;
    if (
      error.response?.status === 401 &&
      originalRequest &&
      !originalRequest._isRetry
    ) {
      originalRequest._isRetry = true;
      try {
        const refreshToken = localStorage.getItem("refreshToken");
        const response = await axios.post<IAuthResponse>(
          `${config.api.baseUrl}/user/refresh/`,
          { refresh_token: refreshToken }
        );
        const newAccessToken = response.data.access_token;
        if (newAccessToken) {
          localStorage.setItem("accessToken", newAccessToken);
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
          return api.request(originalRequest);
        }
      } catch (e) {
        localStorage.clear();
      }
    }
    return Promise.reject(error);
  }
);

// Экспортируем старые имена для совместимости с существующим кодом
export const $apiAuth = api;
export const $apiUser = api;
export const $apiGateway = api;
export const $apiStatistics = api;