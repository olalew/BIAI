import { ClassifyComponent } from './components/style-transfer/classify/classify.component';
import { HomeComponent } from './components/general/home/home.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TransferStyleComponent } from './components/style-transfer/transfer-style/transfer-style.component';
import { ChangeAgeComponent } from './components/style-transfer/change-age/change-age.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'home'},
  { path: 'home', component: HomeComponent },
  { path: 'style-transfer', children: [
    { path: '', pathMatch: 'full', redirectTo: 'upload'},
    { path: 'upload', component: TransferStyleComponent }
  ]}, 
  { path: 'classify', children: [
    { path: '', pathMatch: 'full', redirectTo: 'fruits-vegetable'},
    { path: 'fruits-vegetable', component: ClassifyComponent }
  ]},
  {
    path: 'change_age', children: [
      { path: '', pathMatch: 'full', redirectTo: 'generate'},
      { path: 'generate', component: ChangeAgeComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
     
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
