from launch import LaunchDescription
from launch_ros.actions import Node
import os
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Load robot description from xacro
    robot_description = ParameterValue(
        Command([
            "xacro ",
            os.path.join(
                get_package_share_directory("robot_description"),
                "urdf",
                "my_robot.urdf.xacro"
            )
        ]),
        value_type=str
    )

    # Path to controller config
    controller_config = os.path.join(
        get_package_share_directory("robot_description"),
        "config",
        "my_controller.yaml"
    )

    # Robot State Publisher
    robot_state_publish = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description},
            {"use_sim_time": True}
        ]
    )

    # ros2_control_node (controller manager)
    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{"robot_description": robot_description},
                    controller_config],
        output="screen"
    )

    # Controller spawners
    joint_state_broadcaster_spawn = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
        output="screen"
    )

    diff_drive_controller_spawn = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
        output="screen"
    )

    return LaunchDescription([
        robot_state_publish,
        control_node,
        joint_state_broadcaster_spawn,
        diff_drive_controller_spawn,
    ])
