---
layout: post
title: Remove leftover system extensions
---

I ended up with a left over ghost system extension that cannot be removed by any of the usual methods (`sudo rm -rf`). I could see it running with the following command (titles removed below for simplicity):
```
$ systemextensionsctl list
3 extension(s)
--- com.apple.system_extension.driver_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       G43BCU2T37  <...>  <...> (...)  <...>  [activated enabled]
--- com.apple.system_extension.network_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
$
```
The typical command to uninstall a system extension does not work:
```
$ systemextensionsctl uninstall G43BCU2T37 <bundleID>
At this time, this tool cannot be used if System Integrity Protection is enabled.
This limitation will be removed in the near future.
Please remember to re-enable System Integrity Protection!
$
```

Steps to remove a system extension:

## 1. Boot into recovery mode

- Shut down the computer. Wait for it to completely shut down.

- Press the power button and hold it until you see `Loading startup options...`. You can let go of the power button.

- A window shows up with your hard drive and `Options`. Click to select `Options`. Click `Continue`.

- On the next screen `Select an admin user you know the password for:` click to select your administrator user name. When prompted, enter your password and click `Continue`.

## 2. Disable the system integrity protection (temporarily)

- Open Terminal by going into the `Utilities` menu on top of the screen and selecting `Terminal`. (Shortcut is command (⌘) - shift - T).

- Execute:
```
-bash-3.2# csrutil disable
Turning off System Integrity Protection requires modifying system security.
Allow booting unsigned operating systems and any kernel extensions for OS "Macintosh HD"? [y/n]: y

Enter password for user <...>:
System Integrity Protection is off.
Restart the machine for the changes to take effect.
-bash-3.2#
```

- Shut down the computer.

## 3. Delete that system extension (finally)

- Start the computer normally. Just a regular press of the power button.

- Open Terminal:
```
$ systemextensionsctl list
3 extension(s)
--- com.apple.system_extension.driver_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       G43BCU2T37  <...>  <...> (...)  <...>  [activated enabled]
--- com.apple.system_extension.network_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
$  systemextensionsctl uninstall G43BCU2T37 <bundleID>
Success
$ systemextensionsctl list
--- com.apple.system_extension.driver_extension
enabled active  teamID  bundleID (version)  name  [state]
                G43BCU2T37  <...>  <...> (...)  <...>  [terminated waiting to uninstall on reboot]
--- com.apple.system_extension.network_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
$
```
The system extension is uninstalled, now to reboot and undo what we changed in Step 2.

## 4. Re-enable the system integrity protection

- Shut down the computer. Wait for it to completely shut down.

- Boot into the recovery mode again: press the power button and hold it until boot options appear.

- Login into your administrator account.

- Open Terminal in recovery mode.

- Execute:
```
-bash-3.2# csrutil enable
Turning on System Integrity Protection allows increased system security.
Raise security level to full boot security for OS "Macintosh HD"? [y/n]: y

Enter password for user <...>:
System Integrity Protection is on.
Restart the machine for the changes to take effect.
-bash-3.2#
```
- Restart your computer and check what system extensions are there.

In my example, now I see:
```
$ systemextensionsctl list
2 extension(s)
--- com.apple.system_extension.network_extension
enabled active  teamID  bundleID (version)  name  [state]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
*       *       J6S6Q257EK  <...>  <...> (...)  <...>  [activated enabled]
$
```

Just like it should be.

To be completely sure we are done and all is as it was, try:
```
$ systemextensionsctl uninstall
At this time, this tool cannot be used if System Integrity Protection is enabled.
This limitation will be removed in the near future.
Please remember to re-enable System Integrity Protection!
$
```

The System Integrity Protection is back on, just like it was.
