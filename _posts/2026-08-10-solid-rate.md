---
layout: post
parent: Markdown
title: Shortcut to show soUSD contract rate
date: 2023-06-29
last_modified_date: 2023-06-29
nav_order: 5
---

Since I am interested in the Solid.xyz project, I wanted a one-click way to look up the current contract rate of their soUSD token from etherscan.

## Contract source

Etherscan contract 0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe.

Read contract.

Function 5 getRate (0x679aefce)

Shows value as integer. To get it in USDC, divide by 6 decimals (1,000,000).

[https://etherscan.io/address/0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe#readContract](https://etherscan.io/address/0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe#readContract)

## iOS and mac shortcut

This shortcut displays the raw rate as well as $ per soUSD. I chose to copy the raw rate and use in a spreadsheet to track the actual yield. As of right now, the Solid app is way too buggy to accurately track anything about the real yield (earned and yearly).

Shortcut link: [soUSD.shortcut](/assets/files/soUSD.shortcut) or [https://www.icloud.com/shortcuts/ff2e9997dad549adb4dd1fc79aa3163f](https://www.icloud.com/shortcuts/ff2e9997dad549adb4dd1fc79aa3163f).

## How to run: assign a global shortcut

Open the shortcut in the Shortcuts app.

Right side of the shortcut window click on (i). Details tab opens.

Select "Show in Share Sheet" to run in most apps.

Select "Use as Quick Action" and "Services menu".

Run with: click into the field and hit your shortcut (example: fn-1).

## How to run: command line

In terminal, run:

```
shortcuts run "soUSD"
```

## How to run: AppleScript

```
tell application "Shortcuts Events" to run shortcut " Shortcut Name"
```

## Resources

- Solid project at [https://www.solid.xyz](https://www.solid.xyz)
- Referral for you to get $10 if you create your Solid account and use it (i.e. make one deposit and 3 purchases totaling $75 within 30 days) (and I get $15): [https://www.solid.xyz/refer?ref=N849V](https://www.solid.xyz/refer?ref=N849V)
