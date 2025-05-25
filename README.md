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
https://github.com/owhinata/hello/blob/7367a61a3bd983c083accf576f48f8c9cd4e77b5/setup.py#L21-L29

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
