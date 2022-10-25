#!/bin/bash
ARG=$1

if [ $# -ne 1 ]; then
	echo "Error: Invalid number of arguments. Use gazebo or rviz as run target"
else
  if [ $ARG = "rviz" ]; then
    echo "Build type RVIZ"
    colcon build && 
    ros2 launch src/simulation/launch/launch_rviz.py
  elif [ $ARG = "gazebo" ]; then
    echo "Build type GAZEBO"
    colcon build && 
    ros2 launch src/simulation/launch/launch_gazebo.py
  else
    echo "You must use gazebo|rviz target"
  fi
fi