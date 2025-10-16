from launch import LaunchDescription
from launch_ros.actions import Node 
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    model_arg = DeclareLaunchArgument(
        name ="model",
        default_value=os.path.join(get_package_share_directory("robot_description"),"urdf", "my_robot.urdf.xacro"),
        description= "Absolute path to thr robot urdf file"
    )
    
    robot_description = ParameterValue(Command(["xacro ",LaunchConfiguration("model")]))



    robot_state_pub = Node(
         package="robot_state_publisher",
         executable="robot_state_publisher",
         parameters=[{"robot_description" : robot_description}]

    )

   

  
    return LaunchDescription([
        model_arg,
      
        robot_state_pub,
       


    ])