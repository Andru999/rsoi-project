import { IStatistics } from "./IStatistics"


export interface IPaginationStatistics {
	page: number
	pageSize: number
	totalElements: number
	items: IStatistics[]
};
