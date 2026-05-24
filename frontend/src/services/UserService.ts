import { IUser } from "../interfaces/User/IUser";
import { $apiUser } from "./AxiosInstances";


export default class UserService {
  static async getMe() {
    try {
      const response = await $apiUser.get<IUser>('/user/me/');
      return response.data;
    } catch {
      return null;
    }
  };
}
