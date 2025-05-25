import rclpy
from rclpy.node import Node


class HappyNode(Node):
    def __init__(self):
        super().__init__('happy_node')
        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.count = self.count + 1
        self.get_logger().info(f'count: {self.count}')

def main():
    rclpy.init()
    node = HappyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
