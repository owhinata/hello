from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hello',
            executable='bringme_action_server_node',
            respawn=True
        ),
        Node(
            package='hello',
            executable='bringme_action_client_node',
            prefix='gnome-terminal -- ',
            #on_exit=launch.actions.Shutdown()
        )
    ])
