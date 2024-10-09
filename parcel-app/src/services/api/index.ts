import axios from 'axios'
import Parcels from './parcels'
import { AxiosInstance } from 'axios'

const httpWrapper: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/',
  timeout: 10000
})

export default {
  Parcels: new Parcels(httpWrapper)
}