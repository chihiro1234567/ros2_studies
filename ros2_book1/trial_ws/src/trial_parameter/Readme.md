# trial_parameter

## start project

```bash
> cd trial_ws/src
> ros2 pkg create --build-type ament_python trial_parameter
```

## build

```bash
> cd trial_ws
> colcon build --symlink-install --packages-select trial_parameter
```

## setup trial_topic

```bash
> cd trial_ws
> . install/setup.bash
```

## how to run

```bash
> ros2 run trial_parameter param_publisher

[INFO] [1675258000.561721846] [trial_param_publisher]: This is initial_param =  !
[INFO] [1675258001.450155227] [trial_param_publisher]: This is initial_param = Tokyo !
[INFO] [1675258002.449877219] [trial_param_publisher]: This is initial_param = Tokyo !
[INFO] [1675258003.449463880] [trial_param_publisher]: This is initial_param = Tokyo !
:
```

other terminal

```bash
> ros2 param list

/trial_param_publisher:
  parameter
  use_sim_time
```

```bash
> ros2 param set /trial_param_publisher parameter TYO
Set parameter successful
```

```bash
[INFO] [1675258163.458058906] [trial_param_publisher]: This is initial_param = Tokyo !
[INFO] [1675258164.458941390] [trial_param_publisher]: This is initial_param = TYO !
[INFO] [1675258165.458672959] [trial_param_publisher]: This is initial_param = Tokyo !
```
