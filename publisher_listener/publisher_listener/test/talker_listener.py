import os
import sys
import time 
import uuid
import unittest

import launch
import launch_ros
import launch_ros.actions
import launch_testing.actions
import pytest
import rclpy
from std_msgs.msg import String

#launching all nodes under test

def generate_test_description():
    file_path=os.path.dirname(__file__)
    publisher_node=launch_ros.actions(
        executable=sys.executable,
        arguments=[os.path.join(
            file_path,"..","publisher_listener",'publisher_node.py')],
            additional_env={'PYTHONUNBUFFERED':'1'},
            parameters=[{
                "topic":"publisher_chatter"
            }]
    )
    listener_node=launch_ros.actions(
        executable=sys.executable,
        arguments=[os.path.join(
            file_path,"..","publisher_listener",'listener_node.py')],
            additional_env={'PYTHONUNBUFFERED':'1'},
            parameters=[{
                "topic":"listener_chatter"
            }]
    )
    return(
        launch.LaunchDescription([
            publisher_node,
            listener_node,
            launch_testing.actions.ReadyToTest()
        ]),
        {
            
        "publisher":publisher_node,
        "listener":listener_node
    
    
        }
    )

#testing the nodes

#the class method runs once for testing the nodes
#class TestTalkerListenerLink(unittest.TestCase):
    