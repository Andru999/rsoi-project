import axios, { AxiosResponse, InternalAxiosRequestConfig } from "axios";

import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { config } from "../config";

// ============================================================
// 1. Создаём экземпляры axios с ОТНОСИТЕЛЬНЫМИ путями
// ============================================================

// Auth-сервис (авторизация, пользователи)
export const $apiAuth = axios.create({
  baseURL: `${config.server.auth.basePath}/api/v1`,   // → /auth/api/v1
});

// Пользовательский сервис (тот же auth)
export const $apiUser = axios.create({
  baseURL: `${config.server.auth.basePath}/api/v1`,   // → /auth/api/v1
});

// Gateway (основное API)
export const $apiGateway = axios.create({
  baseURL: `${config.server.gateway.basePath}`,       // → /api
});

// Statistics (сервис статистики)
export const $apiStatistics = axios.create({
  baseURL: `${config.server.statistics.basePath}`,    // → /statistics
});

// ============================================================
// 2. Интерсепторы (без изменений)
// ============================================================

// --- $apiUser ---
$apiUser.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("accessToken")}`;
  return config;
});

$apiUser.interceptors.response.use(
  (config: AxiosResponse) => {
    return config;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && error.config && !error.config._isRetry) {
      originalRequest._isRetry = true;
      try {
        const data = {
          refresh_token: localStorage.getItem("refreshToken"),
        };
        const response = await $apiAuth
          .post<IAuthResponse>(`/user/refresh/`, data)
          .catch((_) => {
            localStorage.clear();
          });

        if (response) {
          localStorage.setItem("accessToken", response.data.access_token as string);
          return $apiUser.request(originalRequest);
        }
      } catch (e) {
        console.log(e);
      }
    }
    throw error;
  }
);

// --- $apiGateway ---
$apiGateway.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("accessToken")}`;
  return config;
});

$apiGateway.interceptors.response.use(
  (config: AxiosResponse) => {
    return config;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && error.config && !error.config._isRetry) {
      originalRequest._isRetry = true;
      try {
        const data = {
          refresh_token: localStorage.getItem("refreshToken"),
        };
        const response = await $apiAuth
          .post<IAuthResponse>(`/user/refresh/`, data)
          .catch((_) => {
            localStorage.clear();
          });

        if (response) {
          localStorage.setItem("accessToken", response.data.access_token as string);
          return $apiGateway.request(originalRequest);
        }
      } catch (e) {
        console.log(e);
      }
    }
    throw error;
  }
);

// --- $apiStatistics ---
$apiStatistics.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("accessToken")}`;
  return config;
});

$apiStatistics.interceptors.response.use(
  (config: AxiosResponse) => {
    return config;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && error.config && !error.config._isRetry) {
      originalRequest._isRetry = true;
      try {
        const data = {
          refresh_token: localStorage.getItem("refreshToken"),
        };
        const response = await $apiAuth
          .post<IAuthResponse>(`/user/refresh/`, data)
          .catch((_) => {
            localStorage.clear();
          });

        if (response) {
          localStorage.setItem("accessToken", response.data.access_token as string);
          return $apiStatistics.request(originalRequest);
        }
      } catch (e) {
        console.log(e);
      }
    }
    throw error;
  }
);