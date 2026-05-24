import { ITicket } from "../Ticket/ITicket"
import { IPrivilege } from "../Bonus/IPrivilege"

export interface IUserInfo {
	tickets: ITicket[]
	privilege: IPrivilege
};
