#!/usr/bin/env python

import smbus
import time
#~ bus = smbus.SMBus(1)
#~ address = 0x70
#~ def write(value):
        #~ bus.write_byte_data(address, 0, value)
        #~ return -1

#~ def lightlevel():
        #~ light = bus.read_byte_data(address, 1)
        #~ return light

#~ def range():
        #~ range1 = bus.read_byte_data(address, 2)
        #~ range2 = bus.read_byte_data(address, 3)
        #~ range3 = (range1 << 8) + range2
        #~ return range3

#~ while True:
        #~ write(0x51)
        #~ time.sleep(0.7)
        #~ lightlvl = lightlevel()
        #~ rng = range()
        #~ #print lightlvl
        #~ print "distance to target " + str(rng) + " cm"

class srf_08:
	
	device = smbus.SMBus(1)
	address = None
	delay_time = 0.1
	
	def __init__(self,dev_addr):
		self.address = dev_addr
		
	def distance(self):
		self.__write_i2c(0x51)
		time.sleep(self.delay_time)
		range_byte_1 = self.__read_i2c(2)
		range_byte_2 = self.__read_i2c(3)
		
		distance = (range_byte_1 << 8) + range_byte_2
		return distance
		
	def light_level(self):
		self.__write_i2c(self.delay_time)
		time.sleep(0.1)
		return __read_i2c(1)
		

	def __write_i2c(self,data):
		self.device.write_byte_data(self.address,0,data)
		return 0
		
	def __read_i2c(self,reg):
		data = self.device.read_byte_data(self.address,reg)
		return data
		
		

#~ distance_sensor = srf_08(0x70)
		
#~ while True:
	#~ print distance_sensor.distance()
	
		
		
		
	


