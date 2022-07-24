# Smart_HealthCare_Sys

The Smart Healthcare System is an IoT based device to help old people -65 years or above- with chronic diseases, who lives with a caregiver, do their checkups and detect diseases related to imbalance with automated patient monitoring and critical cases alerting.

It provides measurements of body parameters like Electrocardiogram (ECG), body temperature, oxygen saturation, heartbeat rate.

The project used two devices to do its mission:

1- An on-demand device for gathering all body parameters using Raspberry Pi Model 3 B+ and some sensors. Then, send those parameters to ThingSpeak cloud platform and display them on a Mobile application -made using MIT APP Inventor. If any measured parameter passes the threshold, an emergency email will be sent to the doctor with the patient’s records.

2- A portable device for Fall Detection using NodeMCU ESP8266. If a falling threshold is detected, an SMS will be sent to the caregiver.


The Sensors Used :
1.   Body temperature sensor    (DS18B20 body temperature module)
2.   Pulse oximeter sensor      (MAX30102 oxygen saturation & heartbeat rate module)
3.   Electrocardiogram sensor   (AD8232 ECG module & ADS1115 Analogue-to-Digital Convrter module)
4.   Fall detection sensor      (MPU9250 Micro Electro-Mechanical Systems (MEMS) module)


