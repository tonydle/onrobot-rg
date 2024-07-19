# onrobot-rg

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/tonydle/onrobot-rg)

Controller for OnRobot RG2 and RG6 grippers, using Modbus RTU over RS-485 (from an UR e-Series robot) or TCP/IP (using Compute Box).
This repository is inspired by fwarmuth's [onrobot-vg](https://github.com/fwarmuth/onrobot-vg/tree/feat/serial-connection) repository.

## Requirements

- Python 3.7.3
  - pymodbus==2.5.3

## Installation

```bash
git clone https://github.com/tonydle/onrobot-rg && cd onrobot-rg && pip install -r requirements.txt
```

## Usage
### Using TCP connection, e.g. Compute Box

1. Connect the cable between Compute Box and Tool Changer.
2. Connect an ethernet cable between Compute Box and your computer.
3. Execute a demo script as below  
```bash
python src/demo.py --ip 150.22.0.42 --port 502 --gripper rg2
```
```bash
python src/demo.py --ip 150.22.0.42 --port 502 --gripper rg6
```

### Using serial connection, e.g. UR Robot with RS-485 daemon forwarded to local machine

1. Make sure the RS-485 daemon is running and it is available on port `54321`, details: [Here](https://github.com/UniversalRobots/Universal_Robots_ToolComm_Forwarder_URCap)

Note: Currently there is a [bug](https://github.com/UniversalRobots/Universal_Robots_ToolComm_Forwarder_URCap/issues/9) where the robotiq_grippers URCap prevents the RS-485 URCap from running. To fix this, you can remove the robotiq_grippers URCap from the robot and restart the robot.

2. Forward that serial connection between to your computer using `socat`:
```bash
export ROBOT_IP=150.22.0.250
export LOCAL_DEVICE_NAME=/tmp/ttyUR
socat pty,link=${LOCAL_DEVICE_NAME},raw,ignoreeof,waitslave tcp:${ROBOT_IP}:54321
```
3. Execute the demo script as below  
```bash
python src/demo.py --gripper rg2 --device ${LOCAL_DEVICE_NAME}
```

<img src="img/rg6_2x.gif" width="30%">  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)
[Tony Le](https://github.com/tonydle)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
