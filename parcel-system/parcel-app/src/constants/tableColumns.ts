import { Column } from "../types/table";

export const columns: Column[] = [
  { header: "Name", field: "name" },
  { header: "Weight", field: "weight" },
  { header: "Value", field: "value" },
  { 
    header: "Department", 
    field: "department",
    render: (value: string) => value.replace(/([a-z])([A-Z])/g, '$1 $2')
  },
];