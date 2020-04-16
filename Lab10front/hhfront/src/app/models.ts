export interface Company {
  id: number;
  name: string;
  city: string;
  address: string;
  description: string;
}

export class LoginResponse {
  token: string;
}
