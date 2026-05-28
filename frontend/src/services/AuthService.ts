import { isAxiosError } from "axios";
import { IAuthResponse } from "../interfaces/Auth/IAuthResponse";
import { ICreateUser } from "../interfaces/User/ICreateUser";
import { api } from "./AxiosInstances";

export default class AuthService {
  static async login(login: string, password: string): Promise<string | null> {
    try {
      const response = await api.post<IAuthResponse>(
        "/auth/user/login/",
        { login, password }
      );

      localStorage.setItem("accessToken", response.data.access_token);
      localStorage.setItem("refreshToken", response.data.refresh_token);

      return null;
    } catch (error) {
      return this.handleError(error);
    }
  }

  static async register(registerDto: ICreateUser): Promise<string | null> {
    try {
      const response = await api.post<IAuthResponse>(
        "/auth/user/register/",
        {
          ...registerDto,
          role: "USER",
        }
      );

      localStorage.setItem("accessToken", response.data.access_token);
      localStorage.setItem("refreshToken", response.data.refresh_token);

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

        if (error.response.status === 400 && error.response.data.errors?.length) {
          message += `: ${error.response.data.errors[0].loc} - ${error.response.data.errors[0].msg}`;
        }

        return message;
      }
      return error.message;
    }

    return "Unknown error";
  }
}