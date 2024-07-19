#!/usr/bin/env python3

import time
import argparse

from onrobot import RG


def run_demo():
    """Runs gripper open-close demonstration once."""
    rg = RG(gripper, ip=toolchanger_ip, port=toolchanger_port, device=toolchanger_device)

    if not rg.get_status()[0]:  # not busy
        print("Current hand opening width: " +
              str(rg.get_width_with_offset()) +
              " mm")

        rg.open_gripper()     # fully opened
        while True:
            time.sleep(0.5)
            if not rg.get_status()[0]:
                break
        rg.close_gripper()    # fully closed
        while True:
            time.sleep(0.5)
            if not rg.get_status()[0]:
                break
        rg.move_gripper(800)  # move to middle point
        while True:
            time.sleep(0.5)
            if not rg.get_status()[0]:
                break

    rg.close_connection()


def get_options():
    """Returns user-specific options."""
    parser = argparse.ArgumentParser(description='Set options.')
    parser.add_argument(
        '--gripper', dest='gripper', type=str,
        default="rg6", choices=['rg2', 'rg6'],
        help='set gripper type, rg2 or rg6')
    parser.add_argument(
        '--ip', dest='ip', type=str, default=None,
        help='set IP address')
    parser.add_argument(
        '--port', dest='port', type=str, default="502",
        help='set port number')
    parser.add_argument(
        '--device', dest='device', type=str, default=None,
        help='set device path')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_options()
    gripper = args.gripper
    toolchanger_ip = args.ip
    toolchanger_port = args.port
    toolchanger_device = args.device
    run_demo()
