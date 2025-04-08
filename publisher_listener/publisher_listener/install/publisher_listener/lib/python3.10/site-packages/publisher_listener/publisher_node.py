import rclpy   
from rclpy.node import Node
from std_msgs.msg import String 

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher = self.create_publisher(String,'topic',10)
        time_period = 0.5
        self.timer = self.create_timer(time_period,self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello Everyone {self.count}"
        self.count+=1
        self.get_logger().info(f"Publishing {msg.data}\n")


def main(args=None):
    rclpy.init(args=args)
    publisherNode = PublisherNode()

    rclpy.spin(publisherNode)
    publisherNode.destroy_node()
if __name__ == "__main__":
    main()