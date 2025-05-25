import rclpy
import random
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from hello_interfaces.action import StringCommand


class BringmeActionServerNode(Node):
    def __init__(self):
        super().__init__('bringme_action_server_node')
        self.food = ['apple', 'banana', 'candy']
        self.server = ActionServer(
            self, StringCommand, 'command', execute_callback=self.callback)

    def callback(self, goal_handle):
        feedback = StringCommand.Feedback()
        count = random.randint(5, 10)

        while count > 0:
            self.get_logger().info(f'send feedback: {count} sec')
            feedback.process = f'{count}'
            goal_handle.publish_feedback(feedback)
            count -= 1
            time.sleep(1)

        item = goal_handle.request.command
        result = StringCommand.Result()
        if item in self.food:
            result.answer = f'Yes, is is {item}.'
        else:
            result.answer = f'Cannot find {item}.'

        goal_handle.succeed()
        return result


def main():
    rclpy.init()
    node = BringmeActionServerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
