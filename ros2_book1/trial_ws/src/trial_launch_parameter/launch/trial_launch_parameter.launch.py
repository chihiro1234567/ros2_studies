import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return launch.LaunchDescription([
    Node(
      package="trial_parameter",
      executable="param_publisher",
      name="custom_parameter_node",
      output="screen",
      emulate_tty=True,
      parameters=[
        {"parameter": "Tokyo Publisher"}
      ]),
  ])
