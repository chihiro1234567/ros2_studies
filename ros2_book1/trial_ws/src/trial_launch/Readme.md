# trial_launch

## start project

```bash
> cd trial_ws/src
> ros2 pkg create --build-type ament_python trial_launch
```

## build

```bash
> cd trial_ws
> colcon build --packages-select trial_launch
```

## setup trial_topic

```bash
> cd trial_ws
> . install/setup.bash
```

## how to run

```bash
> ros2 launch trial_launch trial_launch.launch.py

[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [publisher-1]: process started with pid [9132]
[INFO] [subscriber-2]: process started with pid [9134]
[publisher-1] [INFO] [1675266515.868230304] [trial_publisher]: Publising, Hello! 0
[subscriber-2] [INFO] [1675266515.869906918] [trial_subscriber]: Subscribed, Hello! 0
[publisher-1] [INFO] [1675266516.789251795] [trial_publisher]: Publising, Hello! 1
[subscriber-2] [INFO] [1675266516.790936684] [trial_subscriber]: Subscribed, Hello! 1
[publisher-1] [INFO] [1675266517.789235117] [trial_publisher]: Publising, Hello! 2
[subscriber-2] [INFO] [1675266517.790758795] [trial_subscriber]: Subscribed, Hello! 2
```

