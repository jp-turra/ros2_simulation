import os
import sys

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

package_name = 'simulation'
world_file = 'empty.world'
urdf_file = 'fuck.urdf'

def generate_launch_description():
  pkg_share = FindPackageShare(package=package_name).find(package_name)
  default_urdf = os.path.join(pkg_share, 'urdf', urdf_file)
  
  pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
  pkg_simulation = get_package_share_directory(package_name)

  # Gazebo launch
  gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
    )
  )

  # Load World
  world_ag = DeclareLaunchArgument(
    'world',
    default_value=[os.path.join(pkg_simulation, 'worlds', world_file)],
    description="SDF empty world file"
  )

  #Spwan robot
  spawn_entity = Node(
    package='gazebo_ros', executable='spawn_entity.py',
    arguments=['-entity', 'ROBO', '-file', default_urdf],
    output='screen'
  )

  ld = LaunchDescription()
  ld.add_action(gazebo)
  ld.add_action(world_ag)
  ld.add_action(spawn_entity)

  return ld