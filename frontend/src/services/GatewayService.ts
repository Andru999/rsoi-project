import { api } from "./AxiosInstances";

import { ITicketResponse } from "../interfaces/Ticket/ITicketResponse";
import { IBuyTicket } from "../interfaces/Ticket/IBuyTicket";
import { IUserInfo } from "../interfaces/User/IUserInfo";
import { IPrivilegeResponse } from "../interfaces/Bonus/IPrivilegeResponse";
import { ITicket } from "../interfaces/Ticket/ITicket";

export default class GatewayService {
  static async getInfoOnUserTicket(ticketUid: string): Promise<ITicket | null> {
    try {
      return await api.get<ITicket>(`/tickets/${ticketUid}`);
    } catch (error) {
      console.log("getInfoOnUserTicket error", error);
      return null;
    }
  }

  static async buyTicket(buyTicket: IBuyTicket): Promise<ITicketResponse | null> {
    try {
      return await api.post<ITicketResponse>(
        "/tickets",
        buyTicket
      );
    } catch (error) {
      console.log("buyTicket error", error);
      return null;
    }
  }

  static async ticketRefund(ticketUid: string): Promise<boolean> {
    try {
      await api.delete(`/tickets/${ticketUid}`);
      return true;
    } catch (error) {
      console.log("ticketRefund error", error);
      return false;
    }
  }

  static async getUserInformation(): Promise<IUserInfo | null> {
    try {
      return await api.get<IUserInfo>("/me");
    } catch (error) {
      console.log("getUserInformation error", error);
      return null;
    }
  }

  static async getInfoAboutBonusAccount(): Promise<IPrivilegeResponse | null> {
    try {
      return await api.get<IPrivilegeResponse>("/privilege");
    } catch (error) {
      console.log("getInfoAboutBonusAccount error", error);
      return null;
    }
  }
}