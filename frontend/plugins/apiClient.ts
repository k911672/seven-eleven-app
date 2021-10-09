import axios, { AxiosInstance } from "axios";

export class ApiClient {
  client: AxiosInstance

  constructor() {
    this.client = axios.create({
      baseURL: 'https://madefor.github.io/postal-code-api/'
      // baseURL: 'https://example.com/api/v1'
    })
  }

  async fetchAPI() {
    const response = await this.client.get<any[]>('/api/v1/223/0062.json');
    return response.data;
  }
}