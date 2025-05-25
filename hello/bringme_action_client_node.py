import rclpy
import random
import time
from rclpy.node import Node
from rclpy.action import ActionClient
from hello_interfaces.action import StringCommand


class BringmeActionClientNode(Node):
    def __init__(self):
        super().__init__('bringme_action_client_node')
        self.client = ActionClient(self, StringCommand, 'command')

    def send_goal(self, order):
        goal_msg = StringCommand.Goal()
        goal_msg.command = order
        self.client.wait_for_server()
        return self.client.send_goal_async(
            goal_msg, feedback_callback=self.callback)

    def callback(self, feedback):
        self.get_logger().info(
            f'receive feedback: {feedback.feedback.process} sec')


def main(args=None):
    rclpy.init(args=args)
    node = BringmeActionClientNode()
    order = input('What should I bring? ')

    future = node.send_goal(order)
    rclpy.spin_until_future_complete(node, future)
    goal_handle = future.result()

    if not goal_handle.accepted:
        node.get_logger().info(f'REJECTED')
    else:
        node.get_logger().info(f'ACCEPTED')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(node, result_future)
        result = result_future.result().result
        node.get_logger().info(f'result: {result.answer}')

    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
