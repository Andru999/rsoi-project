import { IPaginationStatistics } from "../interfaces/Statistics/IPaginationStatistics";
import { $apiStatistics } from "./AxiosInstances";


export default class StatisticsService {
  static async getAll(page: number, rowsPerPage: number) {
    try {
      return await $apiStatistics.get<IPaginationStatistics>(
        `/statistics/?page=${ page + 1 }&size=${ rowsPerPage }`
      );
    } catch {
      return null;
    }
  };
}
