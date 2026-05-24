export interface ICreateUser {
  login: string
  password: string
  email: string
  phone: string
  lastname: string
  firstname: string
  role?: "USER" | "MODERATOR" | "ADMIN"
};
