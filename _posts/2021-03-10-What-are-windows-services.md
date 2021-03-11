---
layout: post
author: fubar
title: "What are Windows services?"
tag: programming
tool: microsoft
excerpt: "Windows kernel provides access to the hardware to monitor and/or change key parameters, perform essential tasks in the form of services. These services the high level access points to the user."
date: 10th March, 2021
---

# What are Windows services?

[Windows services][1], formerly known as NT services,

>  enable you to create long-running executable applications that run in their own Windows sessions. These services can be automatically started when the computer boots, can be paused and restarted, and do not show any user interface.

From [Stackify][2],

> Unlike regular software that is launched by the end user and only runs when the user is logged on, Windows Services can start **without user intervention** and may continue to run long after the user has logged off.

# How to monitor running services?

Though they do not have a user interface, there is a Services Control Manager accessed by running `services.msc` in the run dialog (Windows key + R)

![services-control-manager][screenshot-services-control-manager]

These services are categorized into

- Local service
- Local system
- Network service
- Third party

Additionally, the running services can be monitored in the Task Manager; this is actually the first place when we come across the services, when they start consuming resources(see [below](#troublesome-services))

![task-manager-services][screenshot-task-manager]

In the above image, it can be noticed that the services run under `Service Host`.

[1]: https://docs.microsoft.com/en-us/dotnet/framework/windows-services/introduction-to-windows-service-applications#requirements
[2]: https://stackify.com/what-are-windows-services/
[screenshot-services-control-manager]: /assets/images/Microsoft/WindowsServices/servicesControlManager.png
[screenshot-task-manager]: /assets/images/Microsoft/WindowsServices/taskManagerServicesListing.png

## What are Service Hosts?

From [EaseUS][3],

> Svchost.exe is a generic host process name for services that run from dynamic-link libraries. Microsoft started changing much of the Windows functionality from relying on internal Windows services (which ran from EXE files) to using DLL files instead. From a programming perspective, this makes the code more reusable and arguably easier to keep up to date. The problem is that you can't launch a DLL file directly from Windows the same way you can an executable file. Instead, a shell that is loaded from an executable file is used to host these DLL services. And so the Service Host process (svchost.exe) was born.

So basically, Service Host is the executable file that launches the shell needed to run the DLL file for the service.



# Examples of services

Some of the commonly encountered services are

Service  |   Description  | Log On As
---|  ---   |---
DHCP client | Registers and updates IP addresses and DNS records for this computer. If this service is stopped, this computer will not receive dynamic IP addresses and DNS updates. If this service is disabled, any services that explicitly depend on it will fail to start. | Local service
Background Intelligent Transfer service (BITS) | Transfers files in the background using idle network bandwidth. If the service is disabled, then any applications that depend on BITS, such as Windows Update or MSN Explorer, will be unable to automatically download programs and other information. | Local System
Windows Time | Maintains date and time synchronization on all clients and servers in the network. If this service is stopped, date and time synchronization will be unavailable. If this service is disabled, any services that explicitly depend on it will fail to start. | Local service
Windows search | Provides content indexing, property caching, and search results for files, e-mail, and other content. | Local system
Windows Insider service | Provides infrastructure support for the Windows Insider Programme. This service must remain enabled for the Windows Insider Programme to work. | Local system

# Troublesome services

Sometimes these services hog resources like CPU and disk usage. From my experience, some of these are

Service  |   Description  | How to disable
---|  ---   |---
SysMain     | (Disk Usage is high, CPU usage is low) Maintains and improves system performance over time. | [MajorGeeks][6]
Superfetch | (Renamed to SysMain in Windows 10 build 21327) Superfetch is like drive caching. It copies all your commonly used files to RAM. This allows programs to boot faster. However, if your system doesn't have the latest hardware, Service Host Superfetch can easily cause high disk usage. High disk usage due to this service isn't always a problem. It's how this service works to optimize your system performance. Ref: [EaseUS][3] | [EaseUS][3]
Defender Antivirus | (Run by AntiMalware Service Executable) Helps protect users from malware and other potentially unwanted software| [Emisoft][4]
Connected User Experience & Telemetry | (Run by utcsvc.exe executable) The Connected User Experiences and Telemetry service enables features that support in-application and connected user experiences. Additionally, this service manages the event driven collection and transmission of diagnostic and usage information (used to improve the experience and quality of the Windows Platform) when the diagnostics and usage privacy option settings are enabled under Feedback and Diagnostics. | [The Windows Club][5]


[3]: https://www.easeus.com/partition-manager-software/fix-service-host-local-system-high-disk-usage.html#2
[4]: https://blog.emsisoft.com/en/28620/antimalware-service-executable/
[5]: https://www.thewindowsclub.com/utcsvc-high-cpu-and-disk-usage
[6]: https://www.majorgeeks.com/content/page/how_to_disable_or_enable_sysmain_superfetch.html
