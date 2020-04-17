export class Company {
  id: number;
  name: string;
  city: string;
  address: string;
  description: string;
  vacancies: Vacancy[]
}

export interface Vacancy {
  id: number;
  name: string;
  salary: number;
  description: string;
}

export class LoginResponse {
  token: string;
}
