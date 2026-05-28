import { IUser } from "../interfaces/User/IUser";
import { api } from "./AxiosInstances";

export default class UserService {
  static async getMe(): Promise<IUser | null> {
    try {
      const response = await api.get<IUser>("/auth/user/me/");
      return response.data;
    } catch (error) {
      console.log("UserService.getMe error:", error);
      return null;
    }
  }
}
