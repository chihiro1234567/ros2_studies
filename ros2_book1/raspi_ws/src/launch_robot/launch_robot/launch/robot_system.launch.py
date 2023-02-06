from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    Node(
      package="py_robot",
      executable="robot_manager"
    ),
    Node(
      package="py_robot",
      executable="status_talker"
    ),
    Node(
      package="py_robot",
      executable="pwm_listener"
    ),
  ])
