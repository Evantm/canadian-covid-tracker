import { Component } from '@angular/core';
import { faCanadianMapleLeaf, faGithub } from '@fortawesome/free-brands-svg-icons';
import { faTimesCircle } from "@fortawesome/free-solid-svg-icons";

import {Color, Label} from 'ng2-charts';
import { callbackify } from 'util';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'canada-covid-web';
  faCanadianMapleLeaf = faCanadianMapleLeaf;
  faGithub = faGithub;
  faTimesCircle = faTimesCircle;

  disclaimer_hidden_status = "";
  showing_data = "CA";
  REQ_URL = "http://34.67.202.136/covid-19.json"

  // Vars for activation of buttons in group
  ca_active = "active";
  bc_active = "active";
  ab_active = "active";
  sa_active = "active";
  ma_active = "active";
  on_active = "active";
  qc_active = "active";
  nl_active = "active";
  pe_active = "active";
  ns_active = "active";
  nb_active = "active";
  yt_active = "active";
  nt_active = "active";
  nu_active = "active";

  // Chart Config Files & Test Data

  public chartData = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Series A' },
    { data: [33, 23, 85, 33, 11, 22, 49], label: 'Series B' }
  ];
  public chartLabels = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"];
  public chartOptions = {responsive: true};
  public chartColors = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0, 0.5)'
    },
    {
      borderColor: 'black',
      backgroundColor: 'rgba(0,255,0, 0.5)'
    }
  ];
  public chartLegend = true;
  public chartType = 'line';
  public chartPlugins = [];

  ngOnInit(){
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', this.REQ_URL);
    xhttp.onreadystatechange = () => {
      this.handleResponse(xhttp.responseText);
    };
    xhttp.send();
    
  }

  handleResponse(response:string){
    console.log(response);
    
  }

  hideDisclaimer() {
    this.disclaimer_hidden_status = "hidden"
  }

  isActive(key:string){
    if(this.showing_data == key){
      return "active"
    }
    else{
      return ""
    }
  }

  showData(key:string){
    this.showing_data = key;

  }

}
