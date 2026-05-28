import axios from "axios";

import { SortFlights } from "../enums/SortFlights";
import { IFilterFlight } from "../interfaces/Flight/IFilterFlight";
import { IPaginationFlight } from "../interfaces/Flight/IPaginationFlight";
import { config } from "../config";

const baseRequestURL = `${config.api.baseUrl}/v1`;

const GatewayRequests = {
  async getListOfFlights(
    page: number,
    size: number,
    sortField: SortFlights,
    filterTable: IFilterFlight,
  ) {
    const url =
      `${baseRequestURL}/flights` +
      `?page=${page + 1}&size=${size}` +
      `&sort=${sortField}` +
      (filterTable.flightNumber
        ? `&flightNumber=${filterTable.flightNumber}`
        : "") +
      (filterTable.fromAirport
        ? `&fromAirport=${filterTable.fromAirport}`
        : "") +
      (filterTable.toAirport
        ? `&toAirport=${filterTable.toAirport}`
        : "") +
      (filterTable.minDate
        ? `&minDate=${filterTable.minDate}`
        : "") +
      (filterTable.maxDate
        ? `&maxDate=${filterTable.maxDate}`
        : "") +
      (filterTable.minPrice
        ? `&minPrice=${filterTable.minPrice}`
        : "") +
      (filterTable.maxPrice
        ? `&maxPrice=${filterTable.maxPrice}`
        : "");

    try {
      return await axios.get<IPaginationFlight>(url);
    } catch (error) {
      console.log("Gateway: getListOfFlights network error", error);
    }
  },
};

export default GatewayRequests;