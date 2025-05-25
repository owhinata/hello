import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HappyPublisherNode(Node):
    def __init__(self):
        super().__init__('happy_publisher_node')
        self.count = 0
        self.pub = self.create_publisher(String, 'topic', 4)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.count += 1
        self.pub.publish(String(data = f'count: {self.count}'))

def main():
    rclpy.init()
    node = HappyPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
