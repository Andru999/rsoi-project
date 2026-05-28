import axios from "axios";

import { SortFlights } from "../enums/SortFlights";
import { IFilterFlight } from "../interfaces/Flight/IFilterFlight";
import { IPaginationFlight } from "../interfaces/Flight/IPaginationFlight";
import { config } from "../config";

const baseRequestURL = config.api.baseUrl;

const GatewayRequests = {
  async getListOfFlights(
    page: number,
    size: number,
    sortField: SortFlights,
    filterTable: IFilterFlight,
  ): Promise<IPaginationFlight | null> {
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
      const response = await axios.get<IPaginationFlight>(url);
      return response.data;
    } catch (error) {
      console.log("Gateway: getListOfFlights network error", error);
      return null;
    }
  },
};

export default GatewayRequests;