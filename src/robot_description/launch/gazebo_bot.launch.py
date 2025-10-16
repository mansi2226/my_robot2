
from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import IncludeLaunchDescription ,SetEnvironmentVariable

from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():


    model_arg = DeclareLaunchArgument(
        name ="model",
        default_value=os.path.join(get_package_share_directory("robot_description"),"urdf", "my_robot.urdf.xacro"),
        description= "Absolute path to thr robot urdf file"
    )


    env_var= SetEnvironmentVariable("GAZEBO_MODEL_PATH", os.path.join(get_package_prefix("robot_description"), "share"))

    robot_description = ParameterValue(Command(["xacro ",LaunchConfiguration("model")]))

    start_gazebo_service = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzserver.launch.py")))

    start_gazebo_client =IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"),"launch","gzclient.launch.py")))

    
   



    robot_state_pub = Node(
         package="robot_state_publisher",
         executable="robot_state_publisher",
         parameters=[{"robot_description" : robot_description}]

    )

    spawn_bot = Node(
     package="gazebo_ros",
     executable="spawn_entity.py",
     arguments=[
        "-entity", "my_robot",
        "-topic", "robot_description",
        "-x", "0.0", "-y", "0.0", "-z", "0.3",
        "-R", "0", "-P", "0", "-Y", "0"
     ]
    )


    joint_state_pub_= Node(

        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    rviz_node  = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output ="screen",
        arguments=["-d", os.path.join(get_package_share_directory("robot_description"), "config","model.rviz")]
    )

    return LaunchDescription([
        model_arg,
        env_var,
        start_gazebo_service,
        start_gazebo_client,
        robot_state_pub,
        spawn_bot,

        joint_state_pub_,
        
        rviz_node,


    ])