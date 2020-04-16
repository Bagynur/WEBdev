export interface Company {
  id: number;
  name: string;
  city: string;
  address: string;
  description: string;
}

export interface Vacancy {
  id: number;
  name: string;
  salary: number;
  company: number;
  description: string;
}

export class LoginResponse {
  token: string;
}
