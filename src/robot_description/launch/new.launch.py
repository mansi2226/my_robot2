from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os


def generate_launch_description():

    package_name='robot_description'

    # Robot State Publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'rsp.launch.py'
            )
        ),
        launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items()
    )

    # Gazebo model path
    env_var = SetEnvironmentVariable(
        "GAZEBO_MODEL_PATH", os.path.join(get_package_prefix("robot_description"), "share")
    )

    # Gazebo parameters
    gazebo_param_file = os.path.join(
        get_package_share_directory(package_name), 'config', 'gazebo_params.yaml'
    )

    # Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")
        ),
        launch_arguments={
            "extra_gazebo_args": "--ros-args --params-file " + gazebo_param_file
        }.items(),
    )

    # Spawn robot
    spawn_bot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "my_robot",
            "-topic", "robot_description",
            "-x", "0.0", "-y", "0.0", "-z", "0.3",
            "-R", "0", "-P", "0", "-Y", "0",
        ],
    )

    # RViz
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=[
            "-d",
            os.path.join(get_package_share_directory("robot_description"), "config", "main.rviz"),
        ],
    )

    # Controllers
    load_joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    load_diff_drive_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )

    return LaunchDescription(
        [
          
            env_var,
            rsp,
            gazebo,
            spawn_bot,
            rviz_node,
            load_joint_state_broadcaster,
            load_diff_drive_controller,
        ]
    )
