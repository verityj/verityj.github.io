---
layout: post
title: Mac screenshots with no page shadow
---

You can take screenshots different ways on a Mac screen. What comes by default is a shadow effect around a captured window image.

To remove the shadow, there is a quick Terminal command:
```
$ defaults write com.apple.screencapture disable-shadow true
```

What happens when you issue it is an addition to the file `~/Library/Preferences/com.apple.screencapture.plist`. You can open this file in Xcode and see:

<img class="centered" width="70%;" src="/assets/images/2023-06-15a.png" />

For the change to take effect, reboot or issue the command `killall SystemUIServer` and you are done with Terminal.

If in the future you want to undo this change, the correct way is to remove that preference with:
```
$ defaults delete com.apple.screencapture disable-shadow
```

And again, restart for changes to take effect. You should check the preference file again to convince yourself.

By the way, you see in the screenshot that there is a `target` property, currently set to `clipboard`. This copies the screenshot, ready for pasting anywhere I need to. Another option would be to put all screenshot png files on the Desktop. That command:
```
$ defaults write com.apple.screencapture target ~/Desktop/
```

Or modify the setting in Xcode if you have the plist file open.

> Note: if you don't have Xcode, there is no need to install that big beast. Alternatives are: 
> - [PrefsEditor](http://apps.tempel.org/PrefsEditor/) - a free utility
> - [PrefEdit](http://www.bresink.com/osx/PrefEdit.html) - paid, with a demo version that can handle up to 5 items in a `.plist`
