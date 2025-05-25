import rclpy
from rclpy.node import Node
from hello_interfaces.srv import StringCommand


class HelloClientNode(Node):
    def __init__(self):
        super().__init__('hello_client_node')
        self.client = self.create_client(StringCommand, 'command')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waitting for service...')
        self.request = StringCommand.Request()

    def send_request(self, order):
        self.request.command = order
        self.future = self.client.call_async(self.request)


def main():
    rclpy.init()
    node = HelloClientNode()
    order = input('何をとってきますか: ')
    node.send_request(order)

    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info(f'fail to call service. {e}')
            else:
                node.get_logger().info(f'\nrequest: {node.request.command} -> response: {response.answer}')
                break

    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
