# Summer Internship 2025: Object Identification using USRP in Gigahertz range

### Overview

This internship involved practical experimentation with USRP (Universal Software Radio Peripheral) devices, focusing on wireless signal transmission, reception, and propagation in various configurations with obstacles.

![image](https://github.com/user-attachments/assets/b3df67c4-795a-47f8-94fb-99428c5a6ffa)

---

### Timeline & Activities

**Until 28 May**

* Learned the basics of USRP operation.
* Familiarized with the hardware and software setup.

**28 May**

* Conducted simple transmission and reception tests using two USRPs.
* The receiver (Rx) was placed in the line of sight of the transmitter (Tx).
* An obstacle (a bottle) was placed between the Tx and Rx to observe its effect.

**30 May**

* Moved the receiver to 30 degrees off the direct line of the transmitter antenna.
* The obstacle (bottle) remained on the direct line joining Tx and Rx.

**2 June**

* Arranged three receivers in an equilateral triangle configuration with sides of 120 cm.
* Positioned the Tx at the center of the triangle.
* Conducted measurements with the obstacle placed on one side of the triangle.

  ![WhatsApp Image 2025-06-03 at 15 13 17_eac524f3](https://github.com/user-attachments/assets/92e69d9a-d5ae-4f90-9bc3-4fe1f94ea363)


**3 June**

* Took readings with the obstacle placed on the other two sides of the triangle.
* Verified the power vs. distance plots for all three sides and all three receivers.
* The plots had very little similarity for the plots, indicating incorrect GNU Radio settings or envirnonmental disturbances or some error in data gathering


**4 June**

* Did some research on the probable causes of error and other basics.
* Found a paper titled 'Microwave-based Object Recognition System Using Learning Techniques' which provided insight on how to advance further.
* Instead of multiple receivers which may cause interfernce, use of only one receiver is optimal.
* Signal to be transmitted is white noise instead of some specific waveform, to better identify the disturbances caused by the obstacle.

**5 June**
![WhatsApp Image 2025-06-05 at 17 13 29_6f10c798](https://github.com/user-attachments/assets/529dc89a-a35e-4cab-bd64-3a331f447601)
* Experimented the new setup of one Tx and one Rx by sending a white burst noise for 0.1 seconds.
* The received power levels were plotted and the trends in power were observed.
* The power levels showed a distinct gap with and without the object, which might be helpful in the future as we train ML algorithms.

**6 June**
* Took the readings on the same setup but with 200k sample rate.
* Observed the same readings on the reciever without the object, which led to the fact that power received by the Rx was constant and all disturbances were taken into account.
* Plotted the Average power v/s sample index plot and it was almost similar to the yesterday's one, with discrepancies at some distances.

  
