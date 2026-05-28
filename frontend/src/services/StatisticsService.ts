import { IPaginationStatistics } from "../interfaces/Statistics/IPaginationStatistics";
import { api } from "./AxiosInstances";

export default class StatisticsService {
  static async getAll(
    page: number,
    rowsPerPage: number
  ): Promise<IPaginationStatistics | null> {
    try {
      const response = await api.get<IPaginationStatistics>(
        `/statistics?page=${page + 1}&size=${rowsPerPage}`
      );

      return response.data;
    } catch (error) {
      console.log("StatisticsService.getAll error:", error);
      return null;
    }
  }
}