import { AxiosInstance } from "axios";
import CacheService from "./chacheService";
import { IParcel } from "../../types/parcels";

export default class Parcels {
  private httpWrapper: AxiosInstance;
  private cacheService: CacheService;

  constructor(httpWrapper: AxiosInstance) {
    this.httpWrapper = httpWrapper;
    this.cacheService = new CacheService();
  }

  private async fetchData<T>(url: string, cacheKey: string): Promise<T> {
    const cachedData = this.cacheService.get(cacheKey);

    if (cachedData) {
      return cachedData;
    }

    const res = await this.httpWrapper.get(url);
    this.cacheService.set(cacheKey, res.data);
    return res.data.parcels;
  }

  async list(): Promise<IParcel[]> {
    return this.fetchData<IParcel[]>('/parcels', 'parcels_list');
  }
}