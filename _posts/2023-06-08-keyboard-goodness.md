---
layout: post
title: Keyboard goodness with Karabiner modifications
date: 2023-06-08
---

There are a lot of possibilities to create useful and simple keyboard shortcuts with [Karabiner Elements](https://karabiner-elements.pqrs.org). Here are a few examples that I had fun setting up and using.

## 1. Paste special without formatting

> Default Mac shortcut: ⌘ - option - shift - v

Four keys is a little much to remember and mousing around within the paste menu options takes even longer. But this is a very useful function to paste and not carry over the original font formatting into the new document. I usually just need the text content that matches the surrounding format. 

Two options are available for a more simple approach in Karabiner. Both live under `"Complex Modifications"` that you see on the right side bar of the Karabiner-Elements settings window. In there, click the button `"Add rule"` and then `"Import more rules from the internet (Open a web browser)"`.

##### Option 1

Search for _"Right Command + v to paste without formatting"_ with expanded description _Right Command + v does special paste without formatting, equivalent to. cmd+opt+shift+v_. Click the blue `"Import"` button on the right to add it to your Karabiner application.

##### Option 2

Search for _"Command + Shift + v does special paste without formatting, equivalent to cmd+opt+shift+v"_. Import that modification. Then remember to paste using the capital V for this function.

## 2. The emoji menu

> Default Mac shortcut: ⌘ - control - spacebar

I kept forgetting that shortcut so decided to create a new Karabiner complex modification for it. To share it for anyone's use I committed it to the main Karabiner list ([the json code file is here](https://github.com/pqrs-org/KE-complex_modifications/blob/main/public/json/Fn%2Bspace%3Demoji.json)).

Do you have any other ideas or suggestions? Leave a comment for me on [GitHub](https://github.com/verityj/verityj.github.io/discussions/1)!

## 3. Perhaps a bit peculiar: right option key as Delete

Personally, I am frequently deleting text after using the arrow keys to position and adjust the cursor. The hand is on the arrow keys and the right side `option` is already right there. So with a `"Simple Modifications"` menu I changed that to `"forward_delete"` just like the `"Eject"` button [covered previously]({% post_url 2023-06-07-eject-button%}).

![Karabiner screenshot 2](/assets/images/karabiner2.png)

<br />

![Karabiner screenshot 1a](/assets/images/karabiner1a.png)
