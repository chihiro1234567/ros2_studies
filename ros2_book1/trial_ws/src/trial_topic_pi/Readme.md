# trial_topic

## start project

```bash
> ros2 pkg create --build-type ament_python trial_topic_pi
```

## build

```bash
> cd trial_ws
> colcon build --symlink-install --cmake-clean-cache --packages-select trial_topic_pi
```

## setup trial_topic

```bash
> cd trial_ws
> . install/setup.bash
```

## how to run

```bash
> ros2 run trial_topic_pi publisher

[INFO] [1675237005.647831927] [trial_publisher]: Publising Pi, 3.14089398295866
[INFO] [1675237006.647878059] [trial_publisher]: Publising Pi, 3.1409020362003375
[INFO] [1675237007.649220548] [trial_publisher]: Publising Pi, 3.1409099510044687
[INFO] [1675237008.649343136] [trial_publisher]: Publising Pi, 3.14091773052594
:
```

```bash
> ros2 run trial_topic_pi subscriber

[INFO] [1675236969.642964845] [trial_subscriber]: Subscribed Pi, 3.140475187910292
[INFO] [1675236970.644307949] [trial_subscriber]: Subscribed Pi, 3.140491440030626
[INFO] [1675236971.649108253] [trial_subscriber]: Subscribed Pi, 3.140507340174488
[INFO] [1675236972.640725056] [trial_subscriber]: Subscribed Pi, 3.1405228984324434
:
```
