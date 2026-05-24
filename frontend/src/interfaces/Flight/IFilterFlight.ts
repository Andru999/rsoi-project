import { Dayjs } from "dayjs"


export interface IFilterFlight {
	flightNumber?: string
	fromAirport?: string
	toAirport?: string
	minDate?: Dayjs | null
	maxDate?: Dayjs | null
	minPrice?: number
	maxPrice?: number
};
