# trial_parameter

## start project

```bash
> cd trial_ws/src
> ros2 pkg create --build-type ament_python trial_launch_parameter
```

## build

```bash
> cd trial_ws
> colcon build --packages-select trial_launch_parameter
```
## setup trial_topic

```bash
> cd trial_ws
> . install/setup.bash
```

## how to run

```bash
> ros2 launch trial_launch_parameter trial_launch_parameter.launch.py

[INFO] [launch]: All log files can be found below /home/chihiro/.ros/log/2023-02-02-01-02-31-012781-DESKTOP-9LN1UN6-9236
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [param_publisher-1]: process started with pid [9238]
[param_publisher-1] [INFO] [1675267358.941428496] [custom_parameter_node]: This is initial_param = Tokyo Publisher !
[param_publisher-1] [INFO] [1675267359.831188067] [custom_parameter_node]: This is initial_param = Tokyo !
[param_publisher-1] [INFO] [1675267360.830464436] [custom_parameter_node]: This is initial_param = Tokyo !
[param_publisher-1] [INFO] [1675267361.830771961] [custom_parameter_node]: This is initial_param = Tokyo !
[param_publisher-1] [INFO] [1675267362.830558925] [custom_parameter_node]: This is initial_param = Tokyo !
```

