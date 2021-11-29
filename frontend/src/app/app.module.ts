import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {SearchBarComponent} from "./components/search-bar/search-bar.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { addItemComponent } from "./components/addItem/addItem.component";
import { FooterComponent } from "./components/footer/footer.component";
import { AppRoutingModule, routingComponents } from "./app-routing.module";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {NgbCollapseModule, NgbDropdownModule} from '@ng-bootstrap/ng-bootstrap';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { MatDialogModule } from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ParticlesButtonComponent } from './components/particles-button/particles-button.component';
import { CardSliderComponent } from './components/card-slider/card-slider.component';
import { SlickCarouselModule } from 'ngx-slick-carousel';
import { HomeProductsComponent } from './components/home-products/home-products.component';
import {DialogEdit} from "./components/user-products/user-products.component";
import {Payment} from "./components/products/products.component";

/*import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';*/

@NgModule({
  declarations: [
    AppComponent,
    SearchBarComponent,
    addItemComponent,
    FooterComponent,
    routingComponents,
    ParticlesButtonComponent,
    CardSliderComponent,
    HomeProductsComponent,
    DialogEdit,
    Payment
    ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule,
    NgbModule,
    NgbCollapseModule,
    NgbDropdownModule,
    FontAwesomeModule,
    MatDialogModule,
    BrowserAnimationsModule,
    SlickCarouselModule,
    FormsModule

    /*FontAwesomeModule*/
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
