import axios, { AxiosInstance } from "axios";
import { Product } from "~/types/product";

export class ApiClient {
  client: AxiosInstance

  constructor() {
    this.client = axios.create({
      baseURL: 'https://madefor.github.io/postal-code-api/'
      // baseURL: 'https://example.com/api/v1'
    })
  }

  async fetchAPI(): Promise<Product[]> {
    // prod
    // const response = await this.client.get<any[]>('/api/v1/223/0062.json');
    // return response.data;

    // mock
    const data: Product[] = [
      {
        id: 1,
        category: "弁当",
        name: "焼肉弁当",
        price: 500
      },
      {
        id: 2,
        category: "カフェ",
        name: "カフェラテ",
        price: 200
      },
      {
        id: 3,
        category: "サラダ",
        name: "すごいサラダ",
        price: 300
      }
    ]
    return data
  }
}