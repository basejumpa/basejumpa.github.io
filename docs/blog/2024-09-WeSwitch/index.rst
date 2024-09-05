.. post:: 2024-09-01
    :tags: «DiY», Raspberry PI, Power Socket, Relais, ssh, pinctrl, COMPLETED
    :language: English

«DiY»  WeSwitch
###############

Switch Sockets via wired network  **Completed**

.. contents:: On this page
    :local:
    :depth: 2


The Challenge
*************

Enable switching of a power socket (basically an relais) remotely via wired network operated by a tech-savvy user.

Given / provided components:

.. figure:: _figures/switchbox_with_cable_and_type_label.png
    :scale: 20%

    SwitchBox with cable and type label

.. figure:: _figures/RPI_4B_and_memory_card.png
    :scale: 20%

    Raspberry Pi 4B with memory card

I coulnd't find the operation manual online anymore, since I got it in paper form I scanned it: :download:`Operation Manual SwitchBox Relais-V1 <_attachments/ANTRAX_SwitchBox_Relais_V1.pdf>`


Outcome
*******

Use command line tool `pinctrl <https://github.com/raspberrypi/utils/tree/master/pinctrl>`__ shipped with `Raspberry Pi OS Lite (64-bit) <https://www.raspberrypi.com/software/operating-systems/>`__ to control remotely one or up to 26 Relais via `ssh <https://manpages.debian.org/testing/manpages-de/ssh.1.de.html>`__.

.. drawio-figure:: _figures/bd_system_and_neighbors.drawio


Usage
=====

The `BCM` **pin numbers** are to be used. See :ref:`fig_rpi_pinout`.

Set-up passwordless login:

.. code-block:: bash

    some_user@some_host:~$ ssh-copy-id weswitch@weswitch

Common commands:

.. code-block:: bash
    :linenos:

    some_user@some_host:~$ ssh weswitch@weswitch "pinctrl 26"
    26: op -- pd | hi // GPIO26 = output
    some_user@some_host:~$ ssh weswitch@weswitch "pinctrl 26 dl"
    some_user@some_host:~$ ssh weswitch@weswitch "pinctrl 26"
    26: op -- pd | lo // GPIO26 = output
    some_user@some_host:~$ ssh weswitch@weswitch "pinctrl 26 dh"


Modify initial states
=====================

Currently pins `19` and `26` are set to `ON` after reboot. All other pins are in default behavior which is `OFF`.

The initial state of each pin can be changed by modifying the file `/boot/firmware/config.txt`. The keyword `dh` needs to be replaced by `dl`:

For this edit the file `/boot/firmware/config.txt` (you need sudo rights):

.. code-block:: bash
    :linenos:

    some_user@some_host:~$ ssh weswitch@weswitch "sudo vi /boot/firmware/config.txt"
    some_user@some_host:~$ ssh weswitch@weswitch "sudo reboot"

As default the GPIOs are OFF after reboot. Let's change it as described in the `RPI documentation <https://www.raspberrypi.com/documentation/computers/config_txt.html#gpio>`__:

Hint: Existing explicit settings you can change using sed to be quicker:

.. code-block:: bash
    :linenos:

    some_user@some_host:~$ ssh weswitch@weswitch "sudo sed -i 's/\(gpio=19=op,\)dh/\1dl/' /boot/firmware/config.txt"
    some_user@some_host:~$ ssh weswitch@weswitch "sudo sed -i 's/\(gpio=26=op,\)dh/\1dl/' /boot/firmware/config.txt"
    some_user@some_host:~$ ssh weswitch@weswitch "sudo reboot"


Pin-out
=======

Pin-out and orientation of 40-pin header of RPI 4B. Source/credits to: https://toptechboy.com/understanding-raspberry-pi-4-gpio-pinouts/

.. _fig_rpi_pinout:

.. figure:: _figures/rpi_4b_pinout.png
    :scale: 50%

    RPI Pinout


Making-Of
*********

.. toctree::
    :maxdepth: 2

    making_of
