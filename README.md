# ROS2_project
This repository contains two folders:

1. publisher_listener
   
   Create a ROS2 Workspace:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   ```
   After going to src folder, clone the publisher_listener package:
```bash
   git clone https://github.com/TanayMaurya84/ROS2_project/tree/main/publisher_listener/publisher_listener
   cd ..  #this brings us back to ros2_ws
   colcon build
   source install/setup.bash
```
   After the package has been built successfully,
   Run publisher and listener nodes on two different terminals:
```bash
   ros2 run publisher_listener publisher_node
   ros2 run publisher_listener listener_node
```
   To launch them together in same terminal,
```bash
   ros2 launch publisher_listener publisher_listener.launch.py
```

2. Navigation through poses
   

Demo for publisher_listener and turtlebot3 simulation:

Publisher_Listener: https://youtu.be/8_fFWVaXSV4

Waypoint_Follower: https://youtu.be/ksUlW_BfOw0

Laser_Scan: https://youtu.be/Za3-zxcnV1A

Autonomy_navigation: https://youtu.be/s6T3glmW2Yg
                             
