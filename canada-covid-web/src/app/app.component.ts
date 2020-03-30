import { Component } from '@angular/core';
import { faCanadianMapleLeaf, faGithub } from '@fortawesome/free-brands-svg-icons';
import { faTimesCircle } from "@fortawesome/free-solid-svg-icons";

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
