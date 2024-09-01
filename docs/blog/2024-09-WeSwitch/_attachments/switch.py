#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import sys
import re
from gpiozero import LED
import gpiozero.pins.rpigpio


def close(self):
    pass

def parse_state(state):
    true_values = {"true", "1", "on", "t", "yes"}
    false_values = {"false", "0", "off", "f", "no"}

    state_lower = state.lower()
    if state_lower in true_values:
        return "True"
    elif state_lower in false_values:
        return "False"
    else:
        raise argparse.ArgumentTypeError(f"Invalid state value: '{state}'")

def parse_pin_state(pin_state):
    match = re.match(r"^(\d+)(:(1|0))?$", pin_state)
    if match:
        pin = int(match.group(1))
        state = "True" if match.group(3) == "1" else "False" if match.group(3) == "0" else None
        return pin, state
    else:
        raise argparse.ArgumentTypeError(f"Invalid pin:state format: '{pin_state}'")

def main():

    pinout = """
    Raspberry Pi GPIO - BCM Pinout
    +-----+------------+----RPI---+------------+-----+
    | BCM |   Function | Physical | Function   | BCM |
    +-----+------------+----++----+------------+-----+
    |     |       3.3V |  1 || 2  | 5v         |     |
    |  2  |   I2C1 SDA |  3 || 4  | 5v         |     |
    |  3  |   I2C1 SCL |  5 || 6  | GND        |     |
    |  4  |     GPCLK0 |  7 || 8  | UART TX    | 14  |
    |     |        GND |  9 || 10 | UART RX    | 15  |
    | 17  |            | 11 || 12 | PCM CLK    | 18  |
    | 27  |            | 13 || 14 | GND        |     |
    | 22  |            | 15 || 16 |            | 23  |
    |     |       3.3V | 17 || 18 |            | 24  |
    | 10  |  SPI0 MOSI | 19 || 20 | GND        |     |
    |  9  |  SPI0 MISO | 21 || 22 |            | 25  |
    | 11  |  SPI0 SCLK | 23 || 24 | SPI0 CE0   |  8  |
    |     |        GND | 25 || 26 | SPI0 CE1   |  7  |
    |  0  | EEPROM SDA | 27 || 28 | EEPROM SCL |  1  |
    |  5  |            | 29 || 30 | GND        |     |
    |  6  |            | 31 || 32 |            | 12  |
    | 13  |       PWM1 | 33 || 34 | GND        |     |
    | 19  |     PCM FS | 35 || 36 |            | 16  |
    | 26  |            | 37 || 38 | PCM DIN    | 20  |
    |     |        GND | 39 || 40 | PCM DOUT   | 21  |
    +-----+------------+----++----+------------+-----+
    """

    examples = """
    Examples:

    1. Query the state of a pin:
        ./switch.py --pin 19
        ./switch.py 26
        Output: "19:0" on stdout, "Pin 19 is currently OFF" on stderr

    2. Turn on a pin using the --pin option:
        ./switch.py True --pin 26
        ./switch.py 1 --pin 26
        ./switch.py on --pin 26

    3. Turn off a pin using the --pin option:
        ./switch.py False --pin 26
        ./switch.py 0 --pin 26
        ./switch.py off --pin 26

    4. Turn on a pin using the pin:state format:
        ./switch.py 26:1

    5. Turn off a pin using the pin:state format:
        ./switch.py 19:0
    """

    parser = argparse.ArgumentParser(
        description=(
            "Control a GPIO pin (use BCM numbering).\n\n"
            + examples
            + pinout
            + "More detailed/interactive at: https://pinout.xyz/\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "command",
        nargs="?",
        help="Set the pin state in the format <pin>:<state> (e.g., 26:1 or 19:0) or use positional True/False with --pin. Providing only the pin number queries the pin state.",
    )

    parser.add_argument(
        "--pin",
        type=int,
        help="BCM pin number to control (required if using positional True/False).",
    )

    args = parser.parse_args()

    if not args.command and not args.pin:
        parser.print_help()
        sys.exit(1)

    if args.command:
        pin, state = parse_pin_state(args.command)
        if state is None and args.pin is None:
            # If only a pin is provided, query the pin state
            state = None
        elif state is None and args.pin is not None:
            # Handle the True/False positional argument with --pin
            state = parse_state(args.command)
            pin = args.pin
    else:
        # If no command is provided, just query the pin state
        pin = args.pin
        state = None

    # Override the close method to prevent the GPIO pin from being closed when application exits
    gpiozero.pins.rpigpio.RPiGPIOPin.close = close

    # Use the pin and state
    pin_control = LED(pin, pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory())

    # Determine the current state
    current_state = "True" if pin_control.is_lit else "False"

    if state is None:
        # If no state is provided, just output the current state
        machine_readable_state = "1" if current_state == "True" else "0"
        human_readable_state = "ON" if current_state == "True" else "OFF"
        print(f"{pin}:{machine_readable_state}", file=sys.stdout)  # Machine-readable
        print(f"Pin {pin} is currently {human_readable_state}", file=sys.stderr)  # Human-readable
    else:
        # Determine if the state is changing
        if state == current_state:
            print(f"{pin}:{('1' if state == 'True' else '0')}", file=sys.stdout)  # Machine-readable
            print(f"Pin {pin} is already {('ON' if state == 'True' else 'OFF')}. No change made.", file=sys.stderr)  # Human-readable
        else:
            # Set the pin state based on the provided argument
            if state == "True":
                pin_control.on()
                print(f"{pin}:1", file=sys.stdout)  # Machine-readable
                print(f"Pin {pin} is now ON. State changed from OFF to ON.", file=sys.stderr)  # Human-readable
            else:
                pin_control.off()
                print(f"{pin}:0", file=sys.stdout)  # Machine-readable
                print(f"Pin {pin} is now OFF. State changed from ON to OFF.", file=sys.stderr)  # Human-readable

if __name__ == "__main__":
    main()

