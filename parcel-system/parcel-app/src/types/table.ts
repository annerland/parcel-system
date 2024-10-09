export interface Column {
  header: string;
  field: string;
  render?: (value: any) => string;
}