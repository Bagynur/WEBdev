import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CompanylistComponent} from "./companylist/companylist.component";
import {CompanydetailComponent} from "./companydetail/companydetail.component";


const routes: Routes = [
  { path: '', component: CompanylistComponent },
  { path: 'company/:id', component: CompanydetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
