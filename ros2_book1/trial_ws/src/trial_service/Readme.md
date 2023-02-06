# trial_service

## start project

```bash
> cd trial_ws/src
> ros2 pkg create --build-type ament_python trial_service
```

## build

```bash
> cd trial_ws
> colcon build --symlink-install --packages-select trial_service
```

## setup trial_topic

```bash
> cd trial_ws
> . install/setup.bash
```

## how to run

```bash
> ros2 run trial_service server
[INFO] [1675256811.840141572] [trial_server]: Incoming request
x: 3, y: 4, z: 5
```

```bash
> ros2 run trial_service client 3 4 5
[INFO] [1675256812.088148151] [trial_client]: Result of square sum: 3^2 + 4^2 + 5^2 = 409
```
