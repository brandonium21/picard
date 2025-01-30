from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    uros_params = os.path.join(get_package_share_directory('picard'),'config','uros_params.yaml')

    uros_node = Node(
        package='micro_ros_agent',
        executable='micro_ros_agent',
        name='micro_ros_agent',
        arguments=["serial", "--dev", "/dev/ttyACM0", "baudrate=115200"],
    )

    return LaunchDescription([
        uros_node,
    ])