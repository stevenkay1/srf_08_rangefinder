cmake_minimum_required(VERSION 2.8.3)
project(srf_08_rangefinder)

find_package(catkin REQUIRED COMPONENTS
	std_msgs
	sensor_msgs
)
	
catkin_package(CATKIN_DEPENDS
	std_msgs
	sensor_msgs
)

catkin_package()

include_directories()
