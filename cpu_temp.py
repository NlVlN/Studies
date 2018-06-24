#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Written by Tomasz Skiba
#
#use on intel galileo gen 2
#send cpu temp through serial port
#
import os

# open the file with a temp value and read it to variable
with open('/sys/class/thermal/thermal_zone0/temp') as f:
    raw_temp = f.read()

msg = 'Temperatura procesora: {0}\'C'.format(raw_temp[0:2]) 
# open device file in write only mode, write msg and close 
dev = os.open('/dev/ttyGS0', os.O_WRONLY)
os.write(dev, msg)
os.close(dev)

