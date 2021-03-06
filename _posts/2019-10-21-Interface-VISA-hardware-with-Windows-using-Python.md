---
layout: post
author: fubar
title: "pyVISA on Windows"
tag: programming
tool: python
excerpt: "A tutorial on interfacing VISA compatible hardware using python's wrapper module `pyVISA`."
date: 21st October, 2019
---

# Abstract

Interfacing test and measurement s

## History of VISA

---

## Requirements

- VISA implementation from National Instruments: NI- VISA
- Keithley USB488A and USB488B GPIB drivers
- PyVISA: Python package that is a frontend to the VISA library

### NI- VISA

[Download: Permanent](http://www.ni.com/en-in/support/downloads/drivers/download.ni-visa.html#305862)

[Documentation : Permanent](http://www.ni.com/pdf/manuals/370423a.pdf)

[Documentation: Mirror](/assets/documents/PyVISA/National-Instruments-2001-NI-VISA-User-Manual.pdf)

### Keithley GPIB to USB drivers

488A is older version of the GPIB to USB adaptor. The driver development is supported only till Windows 7. So if trying to install the driver on later Windows versions, it might get tricky

Newer version is 488B

[Download KUSB-488B GPIB driver](https://www.tek.com/accessory/ki-488/3-1-3-1)

[Download KUSB-488A GPIB driver](https://www.tek.com/accessory/gpib488/9-2-0)

---

## Installation

1. Remove the previous installation
1. Check the system is clean
1. Install the Keithley GPIB2USB drivers
1. Install the NI-VISA library
    - [Digression] Alternative Installation of VISA library
1. Install PyVISA
    - Install python virtual environment

> It is essential to have no traces of previous installations of either the GPIB2USB drivers or the VISA libraries. This is ensured from checking the device manager  and installed programs.

> In case PyVISA-py is already installed in a virtual environment, running
> `python -m visa info` will list the VISA libraries(either NI's implementation or PyVISA-py's own pure Python implemenation).
> This check is optional and needed only if one is not sure if the drivers and VISA libraries are completely uninstalled

### Remove the previous installation


![Before Installation - Remove the VISA libraries](/assets/images/PyVISA/InstallationPyVISA-00.png)

Plug the Keithley GPIB-USB adaptor and check the device manager listing. The hardware is not listed.

![Before Installation - Check the device manager](/assets/images/PyVISA/InstallationPyVISA-01.png)

Check the installed programs.  The driver is for KUSB-488B and the hardware is KUSB-USB488A. Hence it is not listed. Unplug the adaptor and remove the installed driver.

![Before Installation - Remove the Installed Keithley Driver](/assets/images/PyVISA/InstallationPyVISA-02.png)

### Check the system is clean

Run  ` python -m visa info` and see if the sytem is clean and ready for proper installation

![Before Installation -Check the system is clean 00](/assets/images/PyVISA/InstallationPyVISA-03.png)

Again plug the the Keithley GPIB-USB adaptor and check the device manager listing. This confirms that the system is ready for a proper installation of hardware.

![Before Installation -Check the system is clean 01](/assets/images/PyVISA/InstallationPyVISA-04.png)

### Install the Keithley GPIB2USB drivers

> Ensure the hardware is unplugged

Install the KUSB-488A driver with version 9.2.0. According to the release notes within the source directory,

> it is recommended to install the Keithley's adaptor driver first followed by the NI's own GPIB-488.2 driver to avoid vendor design conflict.

![Install the GPIB2USB driver 00](/assets/images/PyVISA/InstallationPyVISA-05.png)

> Rebooting the computer is a requirement after the completion of installations

![Install the GPIB2USB driver 01](/assets/images/PyVISA/InstallationPyVISA-06.png)

After reboot, plug the hardware and check if it is installed in the device manager

![Install the GPIB2USB driver 02](/assets/images/PyVISA/InstallationPyVISA-07.png)


### Install the NI-VISA library

Install the NI's implementation of the VISA specification; version 19.0

![Install NI-VISA library-00](/assets/images/PyVISA/InstallationPyVISA-08.png)

Uncheck the additional services provided by NI as these will only increase the number of unneccessary processes and services running in the background. In the older versions of NI-VISA, the option to uncheck GPIB-488.2 driver from NI was present in the installer. However the current version automatically checks for the GPIB driver pre-installed and accordingly proceeds with the installation to avoid conflict.

![Install NI-VISA library-01](/assets/images/PyVISA/InstallationPyVISA-09.png)

After installation, check for the installed components. Check that the GPIB driver is from Maintainer GPIB-488 whereas NI-VISA is from NI itself.

![Install NI-VISA library-02](/assets/images/PyVISA/InstallationPyVISA-10.png)

A successful installation creates `visa32.dll` and `visa64.dll` dynamically linked libraries. DLL files are shareable libraries which can be ported as it is across systems offering convience of using software without recompiling on new systems. They act like patches.

After the installation, look out for the install location; usually the `C:\\Windows\system32` and search for `visa32.dll` and `visa64.dll`. If they are present there, then PyVISA-py can detect them without fuss. If they are not present there (for some reason), then proceed to the [alternative installation](##[Digression]-Alternative-Installation-of-VISA-library)

### [Digression] Alternative Installation of VISA library

For some reason, my VISA installation has not generated the DLLs at the location. I searched for visa* (* is called a wild card evaluating to any character set like 32.dll or 64.dll) across the WINDOWS directory and found a `visa32.dll` at `C:\Windows\SysWOW64\visa32.dll`.

To demonstrate the portability of DLL files, I copied the `visa32.dll` to the PyVISA virtual environment (described below) and checked for the detection of the visa library.

`python -m visa info` lists the detection of the visa32 library at the path of the virtual environment.

>However the bitness of Python installation (64 bit) and that of VISA (32bit) do not match. We need to fix this!

![Install NI-VISA library-03](/assets/images/PyVISA/InstallationPyVISA-11.png)

## Create a virtual environment

Tools available with us:

32 bit VISAcd
