#!/bin/bash
cd /sys/class/leds/beaglebone:green:usr0 
while true; do echo 255 > brightness ; sleep 1; echo 0 > brightness; sleep 1; done;

#Este Script lo que hace es encender el primer led de la Beaglebone cuando es llamado por la regla
