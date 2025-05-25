# hello

## create package
```bash
ros2 pkg create \
--description "hello world" \
--license Apache-2.0 \
--destination-directory src \
--build-type ament_python \
--maintainer-email ouwa@emtechs.co.jp \
--maintainer-name KatsumiOuwa \
--node-name hello_node \
hello
```

## Add dependency
https://github.com/owhinata/hello/blob/7367a61a3bd983c083accf576f48f8c9cd4e77b5/package.xml#L10-L11

💡 need [hello_interfaces](https://github.com/owhinata/hello_interfaces)

## Add entory points
https://github.com/owhinata/hello/blob/ebe46125d39bb33a41b2cd2bcc089f930e52050c/setup.py#L21-L32

## build and setup
```
colcon build --symlink-install
```

## Nodes
- [hello_node](hello/hello_node.py)
  ```
  ros2 run hello hello_node
  ```
- [hello_publisher_node](hello/hello_publisher_node.py)
  ```
  ros2 run hello hello_publisher_node
  ros2 topic list
  ros2 topic hz /topic
  ros2 topic echo /topic
  ```
- [hello_subscriber_node](hello/hello_subscriber_node.py)
  ```
  ros2 run hello hello_subscriber_node
  ```
- [hello_service_node](hello/hello_service_node.py)
  ```
  ros2 run hello hello_service_node
  ros2 service list
  ros2 service type /command
  ros2 service call /command hello_interfaces/srv/StringCommand '{command: apple}'
  ```
- [hello_client_node](hello/hello_client_node.py)
  ```
  ros2 run hello hello_client_node
  ```
- [bringme_action_server_node](hello/bringme_action_server_node.py)
  ```
  $ ros2 run hello bringme_action_server_node
  $ ros2 action send_goal /command hello_interfaces/action/StringCommand '{command: apple}'
  Waiting for an action server to become available...
  Sending goal:
       command: apple
  
  Goal accepted with ID: 2319cfce1e364007b2a95fd7f99fe731
  
  Result:
      answer: Yes, is is apple.
  
  Goal finished with status: SUCCEEDED
  ```
- [bringme_action_cleint_node](hello/bringme_action_client_node.py)
  ```
  ros2 run hello bringme_action_cleint_node
  ```
- [bringme.launch](launch/bringme.launch.py)
  ```
  ros2 launch src/hello/launch/bringme.launch.py
  ```


