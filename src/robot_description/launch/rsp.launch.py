from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
import os
import xacro
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    pkg_path = os.path.join(get_package_share_directory('robot_description'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'my_robot.urdf.xacro')

    robot_description_config = Command([
        'xacro ', xacro_file,
        ' use_ros2_control:=', use_ros2_control
    ])

    params = {
        "robot_description": robot_description_config,
        "use_sim_time": use_sim_time
    }

    robot_state_pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[params],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time", default_value="false",
            description="Use sim time if true"
        ),
        DeclareLaunchArgument(
            "use_ros2_control", default_value="true",
            description="Use ros2_control if true"
        ),
        robot_state_pub,
    ])
