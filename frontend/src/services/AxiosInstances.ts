import axios, { AxiosResponse, InternalAxiosRequestConfig } from "axios";
import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { config } from "../config";

// Единый экземпляр axios
const api = axios.create({
  baseURL: config.api.baseUrl, // "/api/v1"
});

// Интерсептор запроса: добавляем токен, если есть
api.interceptors.request.use((cfg: InternalAxiosRequestConfig) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    cfg.headers.Authorization = `Bearer ${token}`;
  }
  return cfg;
});

// Интерсептор ответа: обработка 401 и попытка обновить токен
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
        // опционально можно редиректить на логин
      }
    }
    return Promise.reject(error);
  }
);

// Для обратной совместимости с существующим кодом,
// который импортирует $apiAuth, $apiUser, $apiGateway и $apiStatistics
export const $apiAuth = api;
export const $apiUser = api;
export const $apiGateway = api;
export const $apiStatistics = api;