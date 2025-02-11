# FrontDesk

tags: ui

## A receptionist view the registration location, specialties and providers list in login,appointments and visits

tags: hospital, clinic, regression, cure

* Login to Bahmni as a "receptionist"
* Verify the visit locations
* Open "Appointment scheduling" module
* View all appointments
* Open calender at time "10am"
* Verify the appointment locations
* Verify the appointment specialitis list
* Verify if all the providers are present
* Log out if still logged in

## A receptionist view the list of appointments in the summary page

tags: regression, cure

* Login to Bahmni as a "receptionist"
* Open "Appointment scheduling" module
* Verify the appointments in grid view

## A receptionist admits a patient and do search the patient in the inPatient module

tags: regression, cure

* Login to Bahmni as a "receptionist"
* Receptionist creates the "cure" patient and starts an OPD
* Open "Clinical" app
* Search and select patient
* Admit the patient in "General Ward"
* Open "InPatient" module
* Verify the patient is present in "General Ward"
* visit is closed at the front desk
* Log out if still logged in

## A receptionist starts an opd visit and views the ipd dashboard

tags: regression, cure

* Login to Bahmni as a "receptionist"
* Receptionist creates the "cure" patient and starts an OPD
* Open "Clinical" app
* Search and select patient
* Verify the IPD dashboard
* visit is closed at the front desk
* Log out if still logged in

## A receptionist creates a patient and add a relationship

tags: regression, cure, dev

* Login to Bahmni as a "receptionist"
* Receptionist creates the "cure" patient and adds a relation and starts an OPD
* visit is closed at the front desk
* Log out if still logged in

