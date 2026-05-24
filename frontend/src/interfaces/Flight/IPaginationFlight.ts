import { IFlight } from "./IFlight"


export interface IPaginationFlight {
	page: number
	pageSize: number
	totalElements: number
	items: IFlight[]
};
