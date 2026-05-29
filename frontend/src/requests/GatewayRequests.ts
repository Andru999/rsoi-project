import axios from "axios";
import { config } from "../config";
import { SortFlights } from "../enums/SortFlights";
import { IFilterFlight } from "../interfaces/Flight/IFilterFlight";
import { IPaginationFlight } from "../interfaces/Flight/IPaginationFlight";

const api = axios.create({
  baseURL: config.api.baseUrl,   // "/api/v1"
});

const GatewayRequests = {
  async getListOfFlights(
    page: number,
    size: number,
    sortField: SortFlights,
    filterTable: IFilterFlight
  ): Promise<{ data: IPaginationFlight } | null> {
    const url =
      `/flights` +
      `?page=${page + 1}&size=${size}` +
      `&sort=${sortField}` +
      (filterTable.flightNumber ? `&flightNumber=${filterTable.flightNumber}` : "") +
      (filterTable.fromAirport ? `&fromAirport=${filterTable.fromAirport}` : "") +
      (filterTable.toAirport ? `&toAirport=${filterTable.toAirport}` : "") +
      (filterTable.minDate ? `&minDate=${filterTable.minDate}` : "") +
      (filterTable.maxDate ? `&maxDate=${filterTable.maxDate}` : "") +
      (filterTable.minPrice ? `&minPrice=${filterTable.minPrice}` : "") +
      (filterTable.maxPrice ? `&maxPrice=${filterTable.maxPrice}` : "");

    try {
      const response = await api.get<IPaginationFlight>(url);
      return { data: response.data };
    } catch (error) {
      console.log("Gateway: getListOfFlights network error", error);
      return null;
    }
  },
};

export default GatewayRequests;