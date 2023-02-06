# trial_interface

## start project

```bash
> ros2 pkg create --build-type ament_cmake trial_interface
```

## build

```bash
> cd trial_ws
> colcon build --symlink-install --cmake-clean-cache --packages-select trial_interface
```

## setup trial_interface

```bash
> . install/setup.bash
```

```bash
> ros2 interface list | grep trial
  trial_interface/msg/Valu
  trial_interface/srv/XYZ

> ros2 interface show trial_interface/msg/Valu
float64 valu

> ros2 interface show trial_interface/srv/XYZ
int64 x
int64 y
int64 z
---
int64 sqsum
```


## how to run

```bash
> 
```

```bash
> 
```
