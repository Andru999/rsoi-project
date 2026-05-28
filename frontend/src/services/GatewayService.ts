import { api } from "./AxiosInstances";

import { ITicketResponse } from "../interfaces/Ticket/ITicketResponse";
import { IBuyTicket } from "../interfaces/Ticket/IBuyTicket";
import { IUserInfo } from "../interfaces/User/IUserInfo";
import { IPrivilegeResponse } from "../interfaces/Bonus/IPrivilegeResponse";
import { ITicket } from "../interfaces/Ticket/ITicket";

export default class GatewayService {
  static async getInfoOnUserTicket(ticketUid: string): Promise<ITicket | null> {
    try {
      const { data } = await api.get<ITicket>(`/tickets/${ticketUid}`);
      return data;
    } catch {
      return null;
    }
  }

  static async buyTicket(buyTicket: IBuyTicket): Promise<ITicketResponse | null> {
    try {
      const { data } = await api.post<ITicketResponse>("/tickets", buyTicket);
      return data;
    } catch {
      return null;
    }
  }

  static async ticketRefund(ticketUid: string): Promise<boolean> {
    try {
      await api.delete(`/tickets/${ticketUid}`);
      return true;
    } catch {
      return false;
    }
  }

  static async getUserInformation(): Promise<IUserInfo | null> {
    try {
      const { data } = await api.get<IUserInfo>("/me");
      return data;
    } catch {
      return null;
    }
  }

  static async getInfoAboutBonusAccount(): Promise<IPrivilegeResponse | null> {
    try {
      const { data } = await api.get<IPrivilegeResponse>("/privilege");
      return data;
    } catch {
      return null;
    }
  }
}