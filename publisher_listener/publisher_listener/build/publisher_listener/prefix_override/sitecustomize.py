import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/tanay/ros2_workspace/src/publisher_listener/install/publisher_listener'
