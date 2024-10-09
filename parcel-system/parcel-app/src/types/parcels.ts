export interface IParcel {
  name: string;
  weight: number;
  value: number;
  department: string;
}

export interface IParcels {
  parcels: IParcel[];
}