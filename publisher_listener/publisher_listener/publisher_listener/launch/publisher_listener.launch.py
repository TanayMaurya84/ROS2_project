from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    publisher = Node(
        package="publisher_listener",
        executable="publisher_node",
        name="publisher_node"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    )

    listener = Node(
        package="publisher_listener",
        executable="listener_node",
        name="listener_node"
    )
    return LaunchDescription([publisher,listener]) #to actually run nodes, return is needed
