import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CompanylistComponent} from "./companylist/companylist.component";
import {CompanydetailComponent} from "./companydetail/companydetail.component";
import {VacancydetailComponent} from "./vacancydetail/vacancydetail.component";


const routes: Routes = [
  {path: ``, redirectTo: '/companies', pathMatch: 'full'},
  { path: 'companies', component: CompanylistComponent },
  { path: 'companies/:id', component: CompanydetailComponent },
  { path: 'companies/:id/vacancies/:id', component: VacancydetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
