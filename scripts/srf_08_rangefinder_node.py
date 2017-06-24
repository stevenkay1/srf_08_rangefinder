#!/usr/bin/env python


from __future__ import division
import smbus
import time
import sys
import rospy
from sensor_msgs.msg import Range


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
		


def main():
	
	range_data = Range()
	rospy.init_node('srf_08_rangefinder', anonymous = True)
	
	device_address = rospy.get_param('~device_addr')
	sample_rate = rospy.get_param('~sample_rate')
	
	range_data.radiation_type = rospy.get_param('~radiation_type')
	range_data.min_range = rospy.get_param('~min_range')
	range_data.max_range = rospy.get_param('~max_range')
	range_data.field_of_view = rospy.get_param('~fov')
	
	
	pub = rospy.Publisher('rangefinder_data', Range, queue_size = 1)
	rate = rospy.Rate(sample_rate)
	
	rangefinder = srf_08(device_address)
	
	while not rospy.is_shutdown():
		range_data.header.stamp = rospy.Time.now()
		
		range_data.range = (rangefinder.distance()/100)
				
		
		pub.publish(range_data)
		rate.sleep()
	
	

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
