
# `switch` - GPIO Pin Control Tool

## Overview

`switch` is a tool implemented in Python designed to control a GPIO pin on a Raspberry Pi. The script allows you to turn a GPIO pin on or off (using True/False or similar commands), query its current state, and set the pin number.

This script is particularly useful for controlling LEDs or other simple devices connected to the GPIO pins.

## Installation

1. Ensure Python 3 and the `gpiozero` library are installed on your Raspberry Pi.

   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-gpiozero
   ```

2. Download or copy `switch.py` to your Raspberry Pi.

3. (Optional) Make the script executable:

   ```bash
   chmod +x switch.py
   ```

4. (Optional) Move the script to a directory in your `PATH` (e.g., `/usr/local/bin`) for easy access:

   ```bash
   sudo mv switch.py /usr/local/bin/switch
   ```

## Usage

### Basic Command Structure

```bash
switch [True|False] [--pin PIN]
switch <pin>:<state>
switch <pin>
```

- **True/False**: Set the pin to `True` (ON) or `False` (OFF).
- **<pin>:<state>**: Set the state of the specified pin directly, where `state` is `1` (ON) or `0` (OFF).
- **<pin>**: Query the state of the specified pin.
- **--pin PIN**: Specify the BCM pin number to control. Required when using the `True/False` format.

### Examples

1. **Query the state of a pin**:
   ```bash
   ./switch.py --pin 19
   ./switch.py 26
   ```
   - Output: `19:0` on stdout, `Pin 19 is currently OFF` on stderr.

2. **Turn on a pin using the --pin option**:
   ```bash
   ./switch.py True --pin 26
   ./switch.py 1 --pin 26
   ./switch.py on --pin 26
   ```

3. **Turn off a pin using the --pin option**:
   ```bash
   ./switch.py False --pin 26
   ./switch.py 0 --pin 26
   ./switch.py off --pin 26
   ```

4. **Turn on a pin using the pin:state format**:
   ```bash
   ./switch.py 26:1
   ```

5. **Turn off a pin using the pin:state format**:
   ```bash
   ./switch.py 19:0
   ```

### Input Tolerance

The script accepts various forms of input for `True` and `False`:

- **True**: `True`, `true`, `1`, `on`, `On`, `ON`, `t`, `yes`
- **False**: `False`, `false`, `0`, `off`, `Off`, `OFF`, `f`, `no`

### Help Screen

For more information, run:

```bash
switch.py --help
```

This will display:

```
usage: switch.py [-h] [--pin PIN] [True | False]

Control a GPIO pin.

Pinout information can be found at: https://pinout.xyz/

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

positional arguments:
  {True,False}        Set the pin to True (ON) or False (OFF).

optional arguments:
  -h, --help          show this help message and exit
  --pin PIN           BCM pin number to control.
```

### Pinout Information

For detailed pinout information on your Raspberry Pi, visit [pinout.xyz](https://pinout.xyz/).

## Troubleshooting

If you don't see the expected behavior on the electrical side (e.g., the LED doesn't turn on/off):

- **Verify the Pin Numbering**: Ensure you are using the correct BCM pin number.
- **Check the Wiring**: Make sure the LED and resistor are correctly connected.
- **Check the LED Polarity**: The longer leg (anode) should be connected to the GPIO pin, and the shorter leg (cathode) should be connected to ground.
- **Test the Pin**: Use a simple script to manually test turning the pin on and off.

## License

```
MIT License

Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Happy remote switching :-)
