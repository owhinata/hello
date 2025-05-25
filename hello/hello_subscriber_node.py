import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HappySubscriberNode(Node):
    def __init__(self):
        super().__init__('happy_subscriber_node')
        self.sub = self.create_subscription(String, 'topic', self.callback, 4)

    def callback(self, msg):
        self.get_logger().info(f'subscribe: {msg.data}')

def main():
    rclpy.init()
    node = HappySubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
