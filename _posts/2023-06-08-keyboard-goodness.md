---
layout: post
title: Keyboard goodness with Karabiner (or others)
date: 2023-06-08
---

There are a lot of possibilities to create useful and simple keyboard shortcuts with [Karabiner Elements](https://karabiner-elements.pqrs.org). Here are a few examples that I had fun setting up and using.

## 1. Paste without formatting ("Paste and Match Style")

> Default Mac shortcut: ⌘ - option - shift - v

Four keys is a little much to remember and mousing around within the paste menu options takes even longer. But this is a very useful function to paste and not carry over the original font formatting into the new document. I usually just need the text content that matches the surrounding format. 

Two options are available for a more simple approach in Karabiner. Both live under `"Complex Modifications"` that you see on the right side bar of the Karabiner-Elements settings window. In there, click the button `"Add rule"` and then `"Import more rules from the internet (Open a web browser)"`.

##### Option 1

Search for _"Right Command + v to paste without formatting"_ with expanded description _Right Command + v does special paste without formatting, equivalent to. cmd+opt+shift+v_. Click the blue `"Import"` button on the right to add it to your Karabiner application.

##### Option 2

Search for _"Command + Shift + v does special paste without formatting, equivalent to cmd+opt+shift+v"_. Import that modification. Then remember to paste using the capital V for this function.

##### Option 3

Recently I came across a separate mac app that accomplishes just this, with some additional modifications: [Pure paste on Mac app store](https://apps.apple.com/app/id1611378436). Options include automatically clearing formatting while the app is running, setting a keyboard shortcut, excluding applications where it may not work well (e.g. Excel) and trimming leading and trailing whitespaces.

##### Option 4

Where the command is natively supported, you could create a shortcut in `System Settings` → `Keyboard` → `Keyboard Shortcuts` → `App Shortcut` → `+`. Create a new shortcut for `All Applications` called `Paste and Match Style`. It will propagate to any application that has that option in its menu.

Note: Some applications are not compliant with this menu title convention, even Apple ones. For example, Xcode (currently 14.3.1) is weird. It has menu `Edit` → `Paste` with unique titles: `Paste`, `Paste Special` and `Paste and Preserve Formatting`. If you use an app like that you will need to check how it is called in the menu and create another shortcut with that title.

You may end up with something like: 

<img class="centered" width="50%;" src="/assets/images/2023-06-08a.png" />

## 2. The emoji & symbols menu

> Default Mac shortcut: ⌘ - control - spacebar. 
> Or a globe (fn) key can display the emoji menu if set in Keyboard settings in System Preferences. But that may conflict with changing keyboard input sources or the default forward delete which is fn - delete.

##### Option 1

I kept forgetting the default triple shortcut so decided to create a new Karabiner complex modification for it. To share it for anyone's use I committed it to the main Karabiner list ([the json code file lives here](https://github.com/pqrs-org/KE-complex_modifications/blob/main/public/json/Fn%2Bspace%3Demoji.json)).

##### Option 2

This is a little limited, but a shortcut can be set under `System Preferences` → `Keyboard` → `Keyboard shortcuts` → `App Shortcuts` → `All applications`. Click + to create new, leave `Application` as `All Applications` and set menu title exactly as `Emoji & Symbols`.

Caution: some shortcuts may be set but won't work. If that is the case, try something else. I found no way to create a shortcut with `fn` or `globe` key, for example.

## 3. Perhaps a bit peculiar: right option key as Delete

Personally, I am frequently deleting text after using the arrow keys to position and adjust the cursor. The hand is on the arrow keys and the right side `option` is already right there. So with a `"Simple Modifications"` menu I changed that to `"forward_delete"` just like the `"Eject"` button [covered previously]({% post_url 2023-06-07-eject-button%}).

######

<img class="centered" width="90%;" src="/assets/images/karabiner2.png" />

######

<img class="centered" width="90%;" src="/assets/images/karabiner1a.png" />
