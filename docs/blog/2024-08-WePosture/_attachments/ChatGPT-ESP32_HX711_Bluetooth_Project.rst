ESP32 HX711 Bluetooth Project
=============================

You:
^^^^

12:50

Create a PlatformIO project for the following:

A ESP32-WROOM shall transmit via Bluetooth the forces measured via load
cells connected to a HX711.

ChatGPT:
^^^^^^^^

12:50

Creating a PlatformIO project for an ESP32-WROOM that transmits force
measurements via Bluetooth using load cells connected to an HX711
involves several steps. Here's a step-by-step guide to set up the
project:

1. Install PlatformIO
~~~~~~~~~~~~~~~~~~~~~

If you haven't already installed PlatformIO, you'll need to do so.
PlatformIO can be integrated into VS Code or used as a standalone
command-line tool.

-  **VS Code:** Install the PlatformIO IDE extension.
-  **Standalone:** Follow the installation instructions on the
   `PlatformIO website <https://platformio.org/>`__.

2. Create a New Project in PlatformIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open **VS Code** (with the PlatformIO extension) or use the
   PlatformIO CLI.
2. Click on **“PlatformIO Home”** and then select **“New Project”**.
3. Enter the project name, select **“Espressif 32”** as the board type,
   and choose **ESP32 Dev Module** (or the specific variant you are
   using, like ESP32-WROOM-32).
4. Set the framework to **Arduino** and click **Finish**.

3. Add Necessary Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need two main libraries:

-  **HX711** for reading from the load cells.
-  **BluetoothSerial** for transmitting data via Bluetooth.

Add these libraries to your ``platformio.ini`` file:

.. code::

   [env:esp32dev]
   platform = espressif32
   board = esp32dev
   framework = arduino
   lib_deps =
       bogde/HX711 @ ^0.7.5

The ``BluetoothSerial`` library is part of the ESP32 core, so you don't
need to add it separately.

4. Write the Code
~~~~~~~~~~~~~~~~~

Create a ``src/main.cpp`` file with the following code:

.. code::

   #include <Arduino.h>
   #include <BluetoothSerial.h>
   #include "HX711.h"

   // Define HX711 pin connections and scale factor
   #define LOADCELL_DOUT_PIN  4
   #define LOADCELL_SCK_PIN   5
   #define SCALE_FACTOR  2280.0  // Update this value according to your load cell

   HX711 scale;
   BluetoothSerial SerialBT;

   void setup() {
     Serial.begin(115200);
     SerialBT.begin("ESP32_LoadCell"); // Bluetooth device name

     scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
     scale.set_scale(SCALE_FACTOR); // Set the scale factor
     scale.tare();  // Reset the scale to 0

     Serial.println("Bluetooth Started. Waiting for connection...");
   }

   void loop() {
     if (SerialBT.hasClient()) {
       // Read the load cell value
       float force = scale.get_units(10);  // Average over 10 readings
       Serial.print("Force: ");
       Serial.println(force);

       // Send the data via Bluetooth
       SerialBT.print("Force: ");
       SerialBT.println(force);

       delay(500);  // Adjust this delay as needed
     }
   }

5. Build and Upload the Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect your ESP32-WROOM board to your computer.
2. Click on the **PlatformIO: Build** button (or use the command
   ``pio run``).
3. After the build is successful, upload the code to the ESP32 by
   clicking the **PlatformIO: Upload** button (or use the command
   ``pio run --target upload``).

6. Test the Project
~~~~~~~~~~~~~~~~~~~

Once the code is uploaded:

1. Use a Bluetooth terminal app on your smartphone or another device to
   connect to the ESP32.
2. You should see the force readings transmitted from the ESP32 over
   Bluetooth.

7. Adjustments and Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Calibration:** The ``SCALE_FACTOR`` in the code is a placeholder.
   You need to calibrate the scale with known weights to get the correct
   value.
-  **Sampling Rate:** Adjust the ``delay(500);`` in the loop to control
   how often the data is transmitted.

This setup provides a basic starting point. You can expand it with
features like multiple load cells, data logging, or more sophisticated
Bluetooth communication protocols.

You:
^^^^

12:50

There are 4 load cells connected.

ChatGPT:
^^^^^^^^

12:51

When working with four load cells connected to a single HX711,
typically, you would use a load cell summing board (sometimes referred
to as a Wheatstone bridge or load cell amplifier) to combine the signals
from the four load cells into a single signal that the HX711 can read.
Assuming you're using such a configuration, the code and setup would
only need minor adjustments to handle multiple load cells.

Here's how you can adjust the PlatformIO project to work with four load
cells:

1. Wiring Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have a summing board that combines the signals from the
four load cells into one signal pair connected to the HX711, your wiring
will look like this:

-  **Load Cell 1:** Connected to the summing board.
-  **Load Cell 2:** Connected to the summing board.
-  **Load Cell 3:** Connected to the summing board.
-  **Load Cell 4:** Connected to the summing board.
-  **HX711 DOUT**: Connected to GPIO 4 on the ESP32.
-  **HX711 SCK**: Connected to GPIO 5 on the ESP32.

2. Adjusting the Code
~~~~~~~~~~~~~~~~~~~~~

In the code, the setup remains largely the same. However, the
calibration process needs to account for the fact that you are now using
multiple load cells, and the scale factor might need to be recalibrated.

Here's the adjusted ``src/main.cpp``:

.. code::

   #include <Arduino.h>
   #include <BluetoothSerial.h>
   #include "HX711.h"

   // Define HX711 pin connections and scale factor
   #define LOADCELL_DOUT_PIN  4
   #define LOADCELL_SCK_PIN   5
   #define SCALE_FACTOR  9120.0  // Example value, adjust according to your calibration

   HX711 scale;
   BluetoothSerial SerialBT;

   void setup() {
     Serial.begin(115200);
     SerialBT.begin("ESP32_LoadCell"); // Bluetooth device name

     scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
     scale.set_scale(SCALE_FACTOR); // Set the scale factor (adjust based on your calibration)
     scale.tare();  // Reset the scale to 0

     Serial.println("Bluetooth Started. Waiting for connection...");
   }

   void loop() {
     if (SerialBT.hasClient()) {
       // Read the load cell value
       float force = scale.get_units(10);  // Average over 10 readings
       Serial.print("Total Force: ");
       Serial.println(force);

       // Send the data via Bluetooth
       SerialBT.print("Total Force: ");
       SerialBT.println(force);

       delay(500);  // Adjust this delay as needed
     }
   }

3. Key Points
~~~~~~~~~~~~~

-  **Scale Factor:** The ``SCALE_FACTOR`` should be adjusted based on
   your specific load cell setup. The value ``9120.0`` is just an
   example, which assumes the force is distributed across four load
   cells. You need to calibrate this value properly.

-  **Tare Function:** The ``scale.tare()`` function is used to zero the
   scale after the load cells are initialized. Ensure there's no load on
   the cells during this step to get accurate readings.

4. Calibration Process
~~~~~~~~~~~~~~~~~~~~~~

To calibrate the scale factor, you should:

1. **Apply a known weight** to the load cells after taring.
2. **Read the raw value** from the HX711 using ``scale.get_value()`` or
   ``scale.get_units()``.
3. **Calculate the scale factor** by dividing the known weight by the
   raw value.
4. **Update the SCALE_FACTOR** in the code with the newly calculated
   value.

5. Build, Upload, and Test
~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the same build and upload steps as before. Once uploaded, you
should be able to see the total force measured by all four load cells
transmitted over Bluetooth.

This setup allows you to monitor the total load across four load cells,
useful for applications like weighing systems where multiple points of
measurement are necessary.

You:
^^^^

12:54

I want to transmit each of the signals, so the signals shall not be
combined, neither electrically nor by the software on the ESP32. The
receiver of the signals on the other side of the Bluetooth connection
needs all signals. The 4 signals shall be captured as samples.

ChatGPT:
^^^^^^^^

12:54

To transmit the signals from four individual load cells via Bluetooth,
each connected to its own HX711 module, you can follow these steps. This
setup will ensure that each signal is transmitted separately, allowing
the receiver to process all four signals independently.

1. Hardware Setup
~~~~~~~~~~~~~~~~~

Each load cell will need to be connected to its own HX711 module. The
HX711 modules will then be connected to different GPIO pins on the
ESP32.

Here's an example of the wiring:

-  **Load Cell 1**: Connected to HX711 #1.

   -  **HX711 #1 DOUT**: Connected to GPIO 4 on ESP32.
   -  **HX711 #1 SCK**: Connected to GPIO 5 on ESP32.

-  **Load Cell 2**: Connected to HX711 #2.

   -  **HX711 #2 DOUT**: Connected to GPIO 18 on ESP32.
   -  **HX711 #2 SCK**: Connected to GPIO 19 on ESP32.

-  **Load Cell 3**: Connected to HX711 #3.

   -  **HX711 #3 DOUT**: Connected to GPIO 21 on ESP32.
   -  **HX711 #3 SCK**: Connected to GPIO 22 on ESP32.

-  **Load Cell 4**: Connected to HX711 #4.

   -  **HX711 #4 DOUT**: Connected to GPIO 23 on ESP32.
   -  **HX711 #4 SCK**: Connected to GPIO 25 on ESP32.

2. Code Implementation
~~~~~~~~~~~~~~~~~~~~~~

You'll need to initialize four separate HX711 instances in the code and
then read from each load cell independently. The ESP32 will then
transmit these readings via Bluetooth.

Here's the updated ``src/main.cpp``:

.. code::

   #include <Arduino.h>
   #include <BluetoothSerial.h>
   #include "HX711.h"

   // Define HX711 pin connections for each load cell
   #define LOADCELL1_DOUT_PIN  4
   #define LOADCELL1_SCK_PIN   5

   #define LOADCELL2_DOUT_PIN  18
   #define LOADCELL2_SCK_PIN   19

   #define LOADCELL3_DOUT_PIN  21
   #define LOADCELL3_SCK_PIN   22

   #define LOADCELL4_DOUT_PIN  23
   #define LOADCELL4_SCK_PIN   25

   #define SCALE_FACTOR1  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR2  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR3  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR4  2280.0  // Placeholder, calibrate accordingly

   HX711 scale1;
   HX711 scale2;
   HX711 scale3;
   HX711 scale4;

   BluetoothSerial SerialBT;

   void setup() {
     Serial.begin(115200);
     SerialBT.begin("ESP32_LoadCells"); // Bluetooth device name

     // Initialize each load cell
     scale1.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
     scale2.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
     scale3.begin(LOADCELL3_DOUT_PIN, LOADCELL3_SCK_PIN);
     scale4.begin(LOADCELL4_DOUT_PIN, LOADCELL4_SCK_PIN);

     // Set scale factors (adjust after calibration)
     scale1.set_scale(SCALE_FACTOR1);
     scale2.set_scale(SCALE_FACTOR2);
     scale3.set_scale(SCALE_FACTOR3);
     scale4.set_scale(SCALE_FACTOR4);

     // Tare the scales
     scale1.tare();
     scale2.tare();
     scale3.tare();
     scale4.tare();

     Serial.println("Bluetooth Started. Waiting for connection...");
   }

   void loop() {
     if (SerialBT.hasClient()) {
       // Read from each load cell
       float force1 = scale1.get_units(10);  // Average over 10 readings
       float force2 = scale2.get_units(10);  // Average over 10 readings
       float force3 = scale3.get_units(10);  // Average over 10 readings
       float force4 = scale4.get_units(10);  // Average over 10 readings

       // Transmit each force reading via Bluetooth
       SerialBT.print("Force 1: ");
       SerialBT.println(force1);
       SerialBT.print("Force 2: ");
       SerialBT.println(force2);
       SerialBT.print("Force 3: ");
       SerialBT.println(force3);
       SerialBT.print("Force 4: ");
       SerialBT.println(force4);

       delay(500);  // Adjust this delay as needed
     }
   }

3. Build, Upload, and Test
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Build the project** using PlatformIO's build tool.
2. **Upload the code** to your ESP32.
3. **Test** by connecting to the ESP32 via Bluetooth using a terminal
   app on your smartphone or another device.

4. Calibration
~~~~~~~~~~~~~~

You'll need to calibrate each load cell independently. The calibration
process involves placing a known weight on each load cell and adjusting
the ``SCALE_FACTOR`` for that load cell accordingly.

5. Data Format
~~~~~~~~~~~~~~

The ESP32 transmits the force readings sequentially over Bluetooth. If
you require a specific data format (e.g., JSON, CSV), you can modify the
``SerialBT.print`` and ``SerialBT.println`` calls to format the output
accordingly.

6. Considerations
~~~~~~~~~~~~~~~~~

-  **Sampling Rate**: The delay in the loop (``delay(500);``) controls
   the sampling rate. Adjust this according to your needs, considering
   both the load cell's response time and the Bluetooth communication
   speed.

-  **Power Supply**: Ensure that your ESP32 and HX711 modules are
   powered correctly, as load cells can be sensitive to power
   fluctuations.

With this setup, you'll be able to transmit each of the four load cell
signals independently via Bluetooth, allowing the receiving device to
process the data separately.

You:
^^^^

12:58

Does our program already cover the process of connecting our device to
an other Bluetooth partner?

ChatGPT:
^^^^^^^^

12:58

No, the current program does not explicitly handle the process of
connecting to another Bluetooth device. It assumes that once the ESP32's
Bluetooth is enabled, any device can connect to it if it's in range and
discovers the ESP32. However, the ESP32's ``BluetoothSerial`` library
does not natively handle connection management like pairing or directly
connecting to a specific device—it's more designed for simple Bluetooth
communication once a connection is established.

If you need to connect to a specific Bluetooth partner or manage
connections in a more controlled way, you would typically implement
additional logic. Here's a breakdown of what you might want to consider:

1. Pairing and Connecting
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``BluetoothSerial`` library allows the ESP32 to act as a Bluetooth
Serial Device (similar to a classic Bluetooth SPP profile). It does not
inherently manage connections like modern Bluetooth Low Energy (BLE)
peripherals might.

Typically, the process would be:

-  **Advertise**: The ESP32 advertises itself as a Bluetooth device.
-  **Discover**: Another Bluetooth-capable device (like a smartphone)
   discovers the ESP32.
-  **Connect**: The remote device initiates a connection to the ESP32.
-  **Communication**: Once connected, they can exchange data.

This process doesn't require any special handling in the code because it
is part of the Bluetooth standard behavior, and ``BluetoothSerial``
handles it once a connection is established.

2. Adding Connection Feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to provide feedback when a device connects or disconnects,
you can use the ``BluetoothSerial`` library's built-in functions to
detect connection events.

Here's how you can modify the code to provide feedback when a device
connects or disconnects:

.. code::

   #include <Arduino.h>
   #include <BluetoothSerial.h>
   #include "HX711.h"

   // Define HX711 pin connections for each load cell
   #define LOADCELL1_DOUT_PIN  4
   #define LOADCELL1_SCK_PIN   5

   #define LOADCELL2_DOUT_PIN  18
   #define LOADCELL2_SCK_PIN   19

   #define LOADCELL3_DOUT_PIN  21
   #define LOADCELL3_SCK_PIN   22

   #define LOADCELL4_DOUT_PIN  23
   #define LOADCELL4_SCK_PIN   25

   #define SCALE_FACTOR1  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR2  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR3  2280.0  // Placeholder, calibrate accordingly
   #define SCALE_FACTOR4  2280.0  // Placeholder, calibrate accordingly

   HX711 scale1;
   HX711 scale2;
   HX711 scale3;
   HX711 scale4;

   BluetoothSerial SerialBT;
   bool deviceConnected = false;

   void setup() {
     Serial.begin(115200);
     SerialBT.begin("ESP32_LoadCells"); // Bluetooth device name

     // Initialize each load cell
     scale1.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
     scale2.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
     scale3.begin(LOADCELL3_DOUT_PIN, LOADCELL3_SCK_PIN);
     scale4.begin(LOADCELL4_DOUT_PIN, LOADCELL4_SCK_PIN);

     // Set scale factors (adjust after calibration)
     scale1.set_scale(SCALE_FACTOR1);
     scale2.set_scale(SCALE_FACTOR2);
     scale3.set_scale(SCALE_FACTOR3);
     scale4.set_scale(SCALE_FACTOR4);

     // Tare the scales
     scale1.tare();
     scale2.tare();
     scale3.tare();
     scale4.tare();

     Serial.println("Bluetooth Started. Waiting for connection...");
   }

   void loop() {
     if (SerialBT.hasClient() && !deviceConnected) {
       deviceConnected = true;
       Serial.println("Device connected");
     }

     if (!SerialBT.hasClient() && deviceConnected) {
       deviceConnected = false;
       Serial.println("Device disconnected");
     }

     if (deviceConnected) {
       // Read from each load cell
       float force1 = scale1.get_units(10);  // Average over 10 readings
       float force2 = scale2.get_units(10);  // Average over 10 readings
       float force3 = scale3.get_units(10);  // Average over 10 readings
       float force4 = scale4.get_units(10);  // Average over 10 readings

       // Transmit each force reading via Bluetooth
       SerialBT.print("Force 1: ");
       SerialBT.println(force1);
       SerialBT.print("Force 2: ");
       SerialBT.println(force2);
       SerialBT.print("Force 3: ");
       SerialBT.println(force3);
       SerialBT.print("Force 4: ");
       SerialBT.println(force4);

       delay(500);  // Adjust this delay as needed
     }
   }

3. Managing Multiple Connections (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to handle multiple connections or manage specific
connections more intricately (like requiring a PIN for pairing), you
would need to look into more advanced Bluetooth functionality, possibly
leveraging ESP32's BLE capabilities (if you're dealing with BLE) or
classic Bluetooth profiles for more control.

However, for a simple SPP (Serial Port Profile) Bluetooth setup, as is
the case with ``BluetoothSerial``, you won't typically manage
connections beyond what's described above.

4. Custom Connection Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to explicitly connect to another Bluetooth device (not the
ESP32 acting as the server but rather as the client initiating a
connection), you would need a different setup and possibly a different
library like ``ESP32_BLE_Arduino`` for BLE or more advanced
configuration with classic Bluetooth profiles.

In summary, the existing code handles basic Bluetooth communication,
assuming the device connects automatically. Additional feedback and
management features can be added using the ``BluetoothSerial`` library
as shown. For more advanced scenarios, a more sophisticated Bluetooth
library and setup might be required.

You:
^^^^

13:00

Does bluetooth allow receiving the signals without previous pairing?
Some kind of broadcasting?

ChatGPT:
^^^^^^^^

13:00

Yes, Bluetooth does allow for communication without prior pairing in
certain configurations, specifically through **Bluetooth Low Energy
(BLE)** and **Classic Bluetooth** broadcasting modes. Here's a brief
overview of the methods available:

1. **Bluetooth Low Energy (BLE) Broadcasting**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BLE supports a mode called **advertising** where a device can broadcast
packets of data without needing to pair or establish a connection.
Devices within range can receive these broadcasts and extract the data.

-  **BLE Advertising**: The ESP32 can be configured to advertise data
   periodically. This is typically used in scenarios like beaconing or
   broadcasting sensor data to any nearby BLE-enabled devices without
   requiring a formal connection.

   -  **Advantages**: Low power consumption, no pairing required,
      broadcast to multiple devices.
   -  **Disadvantages**: Limited data payload (31 bytes per packet in
      standard advertising).

2. **Classic Bluetooth Broadcasts (e.g., Bluetooth SPP)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Classic Bluetooth is generally connection-based, meaning it requires
pairing and a stable connection for communication. However, there is a
feature called **Bluetooth Inquiry Response** where devices can send
limited information in response to inquiry scans, but this is rarely
used for broadcasting data and is much less flexible than BLE.

3. **ESP-NOW (Alternative for ESP32)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While not Bluetooth, **ESP-NOW** is another communication protocol
available on the ESP32. It allows the device to broadcast messages to
multiple other ESP32 devices without pairing or connecting, and it
operates on Wi-Fi rather than Bluetooth.

-  **ESP-NOW**: This protocol is especially useful if you are using
   multiple ESP32 devices and need low-latency communication. It's a
   good alternative when BLE's data payload limits are a concern, or if
   Wi-Fi-based communication fits your application better.

Implementation of BLE Broadcasting on ESP32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For BLE broadcasting on the ESP32, you can use the ``ESP32_BLE_Arduino``
library. Below is an example of how you could broadcast the load cell
readings via BLE advertising:

.. code::

   #include <Arduino.h>
   #include <BLEDevice.h>
   #include <BLEUtils.h>
   #include <BLEServer.h>
   #include "HX711.h"

   // Define HX711 pin connections for each load cell
   #define LOADCELL1_DOUT_PIN  4
   #define LOADCELL1_SCK_PIN   5
   #define LOADCELL2_DOUT_PIN  18
   #define LOADCELL2_SCK_PIN   19
   #define LOADCELL3_DOUT_PIN  21
   #define LOADCELL3_SCK_PIN   22
   #define LOADCELL4_DOUT_PIN  23
   #define LOADCELL4_SCK_PIN   25

   HX711 scale1, scale2, scale3, scale4;

   BLEAdvertising *pAdvertising;

   void setup() {
     Serial.begin(115200);

     // Initialize load cells
     scale1.begin(LOADCELL1_DOUT_PIN, LOADCELL1_SCK_PIN);
     scale2.begin(LOADCELL2_DOUT_PIN, LOADCELL2_SCK_PIN);
     scale3.begin(LOADCELL3_DOUT_PIN, LOADCELL3_SCK_PIN);
     scale4.begin(LOADCELL4_DOUT_PIN, LOADCELL4_SCK_PIN);

     scale1.set_scale(2280.0);  // Set the correct calibration factor for your load cell
     scale2.set_scale(2280.0);
     scale3.set_scale(2280.0);
     scale4.set_scale(2280.0);

     scale1.tare();
     scale2.tare();
     scale3.tare();
     scale4.tare();

     // BLE setup
     BLEDevice::init("ESP32_LoadCell");
     pAdvertising = BLEDevice::getAdvertising();
     pAdvertising->setScanResponse(false);
     pAdvertising->setMinPreferred(0x06);  // Functions that help with iPhone connections issue
     pAdvertising->setMinPreferred(0x12);

     Serial.println("BLE Broadcasting started.");
   }

   void loop() {
     // Collect load cell data
     float force1 = scale1.get_units(10);
     float force2 = scale2.get_units(10);
     float force3 = scale3.get_units(10);
     float force4 = scale4.get_units(10);

     // Format the data as a string (e.g., CSV format)
     char data[31]; // BLE advertising payload is limited to 31 bytes
     snprintf(data, sizeof(data), "F1:%.2f,F2:%.2f,F3:%.2f,F4:%.2f", force1, force2, force3, force4);

     // Create BLE payload
     BLEAdvertisementData advertisementData;
     advertisementData.setName("ESP32_LoadCells");
     advertisementData.setManufacturerData(std::string(data));

     // Start advertising
     pAdvertising->setAdvertisementData(advertisementData);
     pAdvertising->start();

     delay(1000); // Advertise every 1 second
   }

4. **Considerations**
~~~~~~~~~~~~~~~~~~~~~

-  **Payload Size**: BLE advertising packets are limited to 31 bytes. If
   your data exceeds this size, you'll need to either reduce the data or
   implement a scheme to send the data in parts.

-  **Receiver**: The device receiving the broadcasts must be capable of
   handling BLE advertisements. This is typically straightforward with
   modern smartphones or BLE-enabled microcontrollers.

-  **Broadcast Frequency**: Adjust the frequency of broadcasting
   (``delay(1000);``) based on how often you want to send the data and
   the power consumption requirements.

This approach allows the ESP32 to broadcast load cell data continuously,
without the need for pairing or a dedicated connection.
