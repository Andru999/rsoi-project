import axios from "axios";

import { SortFlights } from "../enums/SortFlights";
import { IFilterFlight } from "../interfaces/Flight/IFilterFlight";
import { IPaginationFlight } from "../interfaces/Flight/IPaginationFlight";
import { config } from "../config";


axios.defaults.headers.common['Access-Control-Allow-Headers'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Methods'] = '*';

const baseRequestURL = 
	`http://${config.server.gateway.host}:${config.server.gateway.port}/api/v1`;


const GatewayRequests = {
	async getListOfFlights(
		page: number, 
		size: number, 
		sortField: SortFlights, 
		filterTable: IFilterFlight,
	) {
		const url = 
			`${ baseRequestURL }/flights` + 
			`?page=${ page + 1 }&size=${ size }` + 
			`&sort=${ sortField }` +
			( filterTable.flightNumber ? `&flightNumber=${ filterTable.flightNumber }` : '' ) +
			( filterTable.fromAirport ? `&fromAirport=${ filterTable.fromAirport }` : '' ) +
			( filterTable.toAirport ? `&toAirport=${ filterTable.toAirport }` : '' ) +
			( filterTable.minDate ? `&minDate=${ filterTable.minDate }` : '' ) +
			( filterTable.maxDate ? `&maxDate=${ filterTable.maxDate }` : '' ) +
			( filterTable.minPrice ? `&minPrice=${ filterTable.minPrice }` : '' ) +
			( filterTable.maxPrice ? `&maxPrice=${ filterTable.maxPrice }` : '' );
		try {
			return await axios.get<IPaginationFlight>(url)
		} catch {
			console.log("Gateway: getListOfFlights network error");
		}
	},
};

export default GatewayRequests;
