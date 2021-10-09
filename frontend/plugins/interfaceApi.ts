import { Product } from "../types/product";

export interface InterfaceApi {
  fetchAPI: () => Promise<Product[]>;
}