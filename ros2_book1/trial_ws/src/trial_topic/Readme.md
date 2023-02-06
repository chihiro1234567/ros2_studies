# trial_topic

## start project

```bash
> ros2 pkg create --build-type ament_python trial_topic
```

## build

```bash
> cd trial_ws
> colcon build --symlink-install --cmake-clean-cache --packages-select trial_topic
```

## setup trial_topic

```bash
. install/setup.bash
```

## how to run

```bash
> ros2 run trial_topic publisher

[INFO] [1675178757.710520169] [trial_publisher]: Publising, Hello! 0
[INFO] [1675178758.619139644] [trial_publisher]: Publising, Hello! 1
[INFO] [1675178759.615428716] [trial_publisher]: Publising, Hello! 2
:
```

```bash
> ros2 run trial_topic subscriber

[INFO] [1675178827.735176011] [trial_subscriber]: Subscribed, Hello! 70
[INFO] [1675178828.612676565] [trial_subscriber]: Subscribed, Hello! 71
[INFO] [1675178829.608695722] [trial_subscriber]: Subscribed, Hello! 72
[INFO] [1675178830.612012073] [trial_subscriber]: Subscribed, Hello! 73
:
```
