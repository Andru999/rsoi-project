import { isAxiosError } from "axios";
import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { ICreateUser } from "../interfaces/User/ICreateUser";
import { api } from "./AxiosInstances";

export default class AuthService {
  static async login(login: string, password: string): Promise<string | null> {
    try {
      const response = await api.post<IAuthResponse>(
        "/user/login/",
        { login, password }
      );

      const { access_token, refresh_token } = response.data;

      if (!access_token || !refresh_token) {
        return "Invalid auth response: missing tokens";
      }

      localStorage.setItem("accessToken", access_token);
      localStorage.setItem("refreshToken", refresh_token);

      return null;
    } catch (error) {
      return this.handleError(error);
    }
  }

  static async register(registerDto: ICreateUser): Promise<string | null> {
    try {
      const response = await api.post<IAuthResponse>(
        "/user/register/",
        {
          ...registerDto,
          role: "USER",
        }
      );

      const { access_token, refresh_token } = response.data;

      if (!access_token || !refresh_token) {
        return "Invalid auth response: missing tokens";
      }

      localStorage.setItem("accessToken", access_token);
      localStorage.setItem("refreshToken", refresh_token);

      return null;
    } catch (error) {
      return this.handleError(error);
    }
  }

  static logout(): void {
    localStorage.clear();
  }

  static isAuth(): boolean {
    return !!localStorage.getItem("accessToken");
  }

  private static handleError(error: unknown): string {
    if (isAxiosError(error)) {
      if (error.response?.data?.message) {
        let message = error.response.data.message;

        if (
          error.response.status === 400 &&
          error.response.data.errors?.length
        ) {
          message += `: ${error.response.data.errors[0].loc} - ${error.response.data.errors[0].msg}`;
        }

        return message;
      }

      return error.message;
    }

    return "Unknown error";
  }
}