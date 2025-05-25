import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32


class HappyFizzBuzzNode(Node):
    def __init__(self):
        super().__init__('happy_fizz_buzz_node')
        self.pub = self.create_publisher(String, 'result', 2)
        self.sub = self.create_subscription(Int32, 'number', self.callback, 2)

    def callback(self, msg):
        result = String()
        if msg.data % 3 == 0:
            result.data += 'Fizz'
        if msg.data % 5 == 0:
            result.data += 'Buzz'
        if len(result.data) == 0:
            result.data = str(msg.data)
        self.pub.publish(result)

def main():
    rclpy.init()
    node = HappyFizzBuzzNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
