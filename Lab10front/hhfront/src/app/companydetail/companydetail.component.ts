import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {CompanyService} from "../company.service";
import{VacancyService} from '../vacancy.service'
import {Company, Vacancy} from "../models";
@Component({
  selector: 'app-companydetail',
  templateUrl: './companydetail.component.html',
  styleUrls: ['./companydetail.component.css']
})
export class CompanydetailComponent implements OnInit {

  company: Company
  vacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService,private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCompany();
    this.getVacancyList();
  }

  getCompany() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getCompany(id).subscribe(company => this.company = company);
  }

  getVacancyList() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.vacancyService.getVacancyList(id)
      .subscribe(vacancies => {
        this.vacancies = vacancies
      });
  }

  deleteVacancy(id) {
    this.vacancyService.deleteVacancy(id).subscribe(res => {
      // this.categories = this.categories.filter(c => c.id != id);
      // this.getCategoryList();
    });
  }

}
