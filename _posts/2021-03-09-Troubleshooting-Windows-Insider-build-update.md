---
layout: post
author: fubar
title: "Troubleshooting Windows Insider build update"
tag: programming
tool: microsoft
excerpt: "I ran into an issue with the v21327 March update of Windows 10 insider build update. This is a log of the steps I have carried out to address the issue."
date: 05th March, 2021
---

After updating to build 21327, I observed two issues
- the date and time is set to 07 August 3209. This results in a dialog popping requesting to move to new build.
- Also the CPU is utilized 100% by  Background Intelligent Transfer Service (BITS).


![dialog-insider-build-expiry](/assets/images/Microsoft/InsiderBuildTroubleshooting/00_buildExpiryDialog.png)

After looking at the update history, it is confirmed that the date is logged as 07 August 3209 for the **Feature Updates**

![update-history-feature-updates-log](/assets/images/Microsoft/InsiderBuildTroubleshooting/01_updateTroubleshooting.png)

As for the **Quality updates**, the update failed at installing Cumulative Update Preview for .NET framework

![update-history-quality-updates-log](/assets/images/Microsoft/InsiderBuildTroubleshooting/02_qualityUpdateFailed.png)

Also there are two herrings with this current update.

- The status message of the update shows that error has occured with the message "There were problems downloading some updates, but we’ll try again later. If you keep seeing this, try searching the web or contacting support for help. This error code might help: (0x80071160)"
- And the `About` tab is missing from the `System` pane. Even the OS build and System info is unresponsive as suggested in the Feeback hub by other Insiders.

![error-hex-code-0x80071160](/assets/images/Microsoft/InsiderBuildTroubleshooting/06_error(0x80071160).png)


To resolve this error, I tried two approaches
- Searched the internet to find a post on [MajorGeeks](https://www.majorgeeks.com/content/page/windows_10_update_error_0x80071160.html) that suggested to try running the troubleshooter as a first step.
- I sought help from inbuilt Help Chat bot,

The first approach resolved that there is a clear issue with update. However the issue still persisted.

![troubleshooting-analysis](/assets/images/Microsoft/InsiderBuildTroubleshooting/03_troubleShooterAnalysis.png)

The second approach suggested the following

```
Important

You need to run both the DISM and SFC commands shown below, not just one of them, and you need to run DISM first and SFC second.

Open an elevated command prompt. Right-click Start, and then select **Command Prompt (Admin).**If you are prompted for an administrator password or for a confirmation, type the password, or click Allow or Yes.

Type the following command, and then press Enter.

DISM.exe /Online /Cleanup-image /Restorehealth

Note It might take several minutes for the command operation to be completed.

Type the following command and press Enter.

sfc /scannow

Note It might take several minutes for the command operation to be completed.

Close the command prompt, and then run Windows Update again.

```

Following the instruction, I executed the first command Deployment Image Servicing and Management Too (DSIM) that leads to

![DSIM-output](/assets/images/Microsoft/InsiderBuildTroubleshooting/04_DISMcompleted.png)

Later the second command system scan gives

![system-scan-output](/assets/images/Microsoft/InsiderBuildTroubleshooting/05_systemScanCompleted.png)

Still bogged by the issue, I sought help from Chat with representative. I was suggested to set the `Windows Time` service Startup option to `Automatic`. It was set to Manual. I did not change it earlier. Maybe the update had to do with this change. Anyways, even after setting to `Automatic` and restarting, the time issue still persists. One reason could be the service unable to sync with time server as the Wifi is not configured when the laptop reboots.

# Conclusion

After following these steps, the issue still persists.

I can try doing two things

- When I restart my laptop, the Wifi needs to be set manually. If I can configure it to be set automatically, the time server can be reached by the service
- If the above fails, for the time being, I can write a custom batch script to automate these tasks. I need to learn a bit of Windows Batch scripting for this!
