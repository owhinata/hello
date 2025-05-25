import rclpy
from rclpy.node import Node
from hello_interfaces.srv import StringCommand


class HelloServiceNode(Node):
    def __init__(self):
        super().__init__('hello_service_node')
        self.food = ['apple', 'banana', 'candy']
        self.service = self.create_service(StringCommand, 'command', self.callback)

    def callback(self, req, res):
        item = req.command
        if item in self.food:
            res.answer = f'Yes. It is {item}.'
        else:
            res.answer = f'I cannot find {item}.'
        return res


def main():
    rclpy.init()
    node = HelloServiceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
