import { IPrivilege } from "../Bonus/IPrivilege"


export interface ITicketResponse {
	ticketUid: string
	flightNumber: string
	fromAirport: string
	toAirport: string
	date: string
	price: number
	paidByMoney: number
	paidByBonuses: number
	status: string
	privilege: IPrivilege
};
