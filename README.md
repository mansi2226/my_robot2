#  Autonomous Mobile Robot (ROS2-Based)

A simple box-sized autonomous robot built using **ROS2** that can **map, navigate, and move autonomously** in a known environment.  
This project was implemented both in **simulation (Gazebo + RViz2)** and **real-world hardware**, showcasing the integration of multiple sensors and control systems.

---

##  Project Overview

The robot performs **SLAM (Simultaneous Localization and Mapping)** to explore and map an unknown area using a LiDAR sensor.  
After the map is generated and saved, the robot uses that reference map to **navigate autonomously** to target locations set remotely from a PC.

Additionally, a camera is mounted on the robot to capture real-time visuals of the surroundings, which can further be used for **object detection** and **machine learning-based tasks** using **OpenCV** and **TensorFlow** or similar frameworks.

---

##  Robot Prototype
![Autonomous Bot](https://github.com/mansi2226/my_robot2/blob/main/image1.jpeg?raw=true)

## navigation setup
![Autonomous Bot](https://github.com/mansi2226/my_robot2/blob/main/image2.jpeg?raw=true)


![Autonomous Bot](https://github.com/yourusername/yourrepo/assets/123456789/robot_image.jpg)



##  Specifications

| Category | Details |
|-----------|----------|
| **Type** | 4-Wheeled Differential Drive Robot |
| **Control System** | ROS2 (Robot Operating System) |
| **Mapping** | SLAM Toolbox |
| **Simulation** | Gazebo |
| **Visualization** | RViz2 |
| **Data Analysis Tools** | RQT Graph, PlotJuggler |
| **Programming Environment** | Arduino IDE, Python (ROS2 Nodes) |
| **Autonomous Navigation** | Nav2 stack with predefined waypoints |

---

##  Hardware Components

- **Chassis:** Custom-built box frame
- **Motors:** 4 DC motors with encoders  
- **Microcontrollers:** Raspberry Pi (main control unit) + Arduino (motor control)
- **Sensors:**
  - LiDAR (for mapping and obstacle detection)
  - IMU (for orientation and stability)
  - Wheel Encoders (for odometry)
  - Camera Module (for vision-based tasks)
- **Power Supply:** Battery-operated
- **Communication:** Wi-Fi (for remote control and data monitoring)

---

##  Software Stack

- **ROS2** (e.g., Humble/Foxy)
- **Gazebo** (robot simulation)
- **RViz2** (visualization and map building)
- **SLAM Toolbox** (for mapping)
- **Nav2 Stack** (for path planning and navigation)
- **RQT Graph** (for node visualization)
- **PlotJuggler** (for real-time data plotting)
- **Arduino IDE** (for microcontroller programming)
- **OpenCV / ML Frameworks** *(future extension)*

---

## Features

- Autonomous Mapping using **SLAM**
- Path Planning and Navigation with **Nav2**
- Real-Time Localization and Pose Estimation
- Live Camera Feed for Vision-Based Applications
- Remote Control via PC or ROS2 Launch Commands
- Scalable Architecture — can integrate:
  - Robotic Arm for spraying or picking tasks
  - Object Detection using Machine Learning
  - IoT or Cloud Integration for Data Logging

---

##  Applications

-  **Agriculture:** Crop detection, spraying fertilizer or medicine, autonomous monitoring  
-  **Service Robots:** Hospital delivery, patient assistance  
-  **Industrial Automation:** Material delivery and inspection  
-  **Surveillance & Security:** Real-time monitoring with camera and sensors  

---

## 📁 Project Structure (Example)


