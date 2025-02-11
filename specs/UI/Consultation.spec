# Consultation

tags: clinic, consultation, regression, ui


## Doctor should be able to see the specialities tab

tags: cure

* Login to Bahmni as a "doctor"
* Goto Clinical application
* Open "Clinical" module
* Verify the specialitis list
* Log out if still logged in

## Doctor should be able to see the patient in My Patient queue and speciality tab

tags: cure

* Login to Bahmni as a "receptionist"
* Receptionist creates the "cure" patient and starts an OPD
* Receptionist creates a regular appointment "11am" on same day for provider "Test Doctor" for speciality "ENT" for service "New Assessment - ENT"
* Goto Clinical application
* Logout and Login to Bahmni as a "doctor"
* Open "Clinical" app
* Verify the patient visit is added in my patient queue and the "ENT" queue
* Goto Clinical application
* Receptionist cancels the newly created "regular" appointment
* Goto Clinical application
* Logout and Login to Bahmni as a "receptionist"
* visit is closed at the front desk
* Log out if still logged in

## Doctor should be able to capture Consultation

tags: cure

* Login to Bahmni as a "receptionist"
* Goto Clinical application
* Receptionist creates the "cure" patient and starts an OPD
* Logout and Login to Bahmni as a "doctor"
* Open "Clinical" module
* Goto All sections and search the newly created patient
* Doctor clicks consultation
* Enter History and Examination details "consultation/observations/historyAndExaminationDetails"
* Enter Orthopaedic Followup "consultation/observations/OrthopaedicFollowup"
* Doctor notes the diagnosis and conditions "consultation/diagnosis/diagnosis_condition"
* Doctor prescribes medications "consultation/medications/paracetamol,consultation/medications/Morphine,consultation/medications/Diazepam,consultation/medications/Ceftriaxone"
* Doctor prescribes radiology "consultation/orders/CTscan"
* Doctor prescribes tests "consultation/orders/Platelets"
* Click back button
* Goto All sections and search the newly created patient
* Verify medical prescription in patient clinical dashboard
* Verify diagnosis and condition in patient clinical dashboard
* Validate the lab tests are available in patient clinical dashboard
* Verify history & examination in patient clinical dashboard
* Logout and Login to Bahmni as a "receptionist"
* visit is closed at the front desk
* Log out if still logged in

## Doctor should be able to add Observation Form

tags: forms, cure

* Login to Bahmni as a "receptionist"
* Goto Clinical application
* Receptionist creates the "cure" patient and starts an OPD
* Logout and Login to Bahmni as a "doctor"
* Open "Clinical" module
* Goto All sections and search the newly created patient
* Doctor clicks consultation
* Enter Form Values and validate no error is displayed on save "consultation/observations/OrthopaedicHistoryPhysical"
* Enter Form Values and validate no error is displayed on save "consultation/observations/physicalTherapy"
* Enter Form Values and validate no error is displayed on save "consultation/observations/pediatricsForm"
* Click back button
* Goto All sections and search the newly created patient
* Validate obs "consultation/observations/OrthopaedicHistoryPhysical" on the patient clinical dashboard
* Validate obs "consultation/observations/physicalTherapy" on the patient clinical dashboard
* Validate obs "consultation/observations/pediatricsForm" on the patient clinical dashboard
* Logout and Login to Bahmni as a "receptionist"
* visit is closed at the front desk
* Log out if still logged in
