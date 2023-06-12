---
layout: post
title: Toggle WiFi on and off - Automator shell script
---

Goal: have a simple shortcut if I want to turn WiFi on or off. Shows how it's done with Automator and a script.

To assign a shortcut to some action, we need to define it first.

Open the `Automator` application.

Create a new `Quick Action`.

<img class="bordered" src="/assets/images/2023-06-13a.png" />


There's a loooong list of things we can start with. Just search for and select `Run Shell Script`. Drag the `Run Shell Script` into the main space on the right of the screen.


<img class="bordered" src="/assets/images/2023-06-13b.png" />


The shell script will look like this, below. It receives no input in an application.


<img class="bordered" src="/assets/images/2023-06-13c.png" />


The command is:
```
networksetup -getairportpower en0 | grep "On" && networksetup -setairportpower en0 off || networksetup -setairportpower en0 on
```

If WiFi is on, it gets set to off. And vice versa.

You could easily take this command and run it from the command line with an alias set. Here, we will save it. In the pop up window give it a name, preferably with no spaces (shortcuts may have issues, at least on earlier systems. Test it with spaces in the title if you would prefer.)

When you hit save, your new created action is placed in your user's `~/Library/Services` directory. It also shows up in every command main menu `Services` list, also showing the shortcut you will assign to it.

Lastly, we may assign a keyboard shortcut for this action. Open `System Settings` → `Keyboard` → `Keyboard Shortcuts` → `Services`. Expand the `General` list and you'll see your title. Select it and type the shortcut you would like.

Even if you forget the shortcut or what actions you have created, you will always see them under the `Services` menu in the main menu bar under any application name. A good habit to check there at a glance if you need a reminder.

If you decide to edit / delete / rename this action, just navigate to `~/Library/Services` where all of your created actions are.
