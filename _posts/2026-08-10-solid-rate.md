---
layout: post
parent: Markdown
title: Shortcut to show soUSD contract rate
date: 2026-08-10
last_modified_date: 2026-08-10
nav_order: 5
bluesky_post_url: "https://bsky.app/profile/veri-t.bsky.social/post/3msr2dnmzwk2i"
---

Solid.xyz is a minuscule, really tiny (and buggy) DEFI project on Fuse chain with a current TVL on the order of about $200,000. That's barely a blip. But since I am following the project out of curiosity, I wanted a one-click way to look up the current contract rate of their soUSD token from etherscan.

DefiLlama TVL:

<iframe width="605px" height="345px" src="https://defillama.com/chart/protocol/solid-yield?fees=false&theme=dark" title="DefiLlama" frameborder="0"></iframe>

## Contract source

Etherscan contract 0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe.

Read contract.

Function 5 getRate (0x679aefce)

Shows value as integer. To get it in USDC, divide by 6 decimals (1,000,000).

[https://etherscan.io/address/0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe#readContract](https://etherscan.io/address/0x10f3996904F1fA09Db48e5d46AAdD6D9fd516eFe#readContract)

## iOS and mac shortcut

This shortcut displays the raw rate as well as $ per soUSD. I chose to copy the raw rate and use in a spreadsheet to track the actual yield. As of right now, the Solid app is way too buggy to accurately track anything about the real yield (earned and yearly).

Shortcut content [image below](#Shortcut-content).

Shortcut link: [soUSD.shortcut](/assets/files/soUSD.shortcut).

## How to run: assign a global shortcut

Open the shortcut in the Shortcuts app.

Right side of the shortcut window click on (i). Details tab opens.

Select "Show in Share Sheet" to run in most apps.

Select "Use as Quick Action" and "Services menu".

Run with: click into the field and hit your shortcut (example: fn-1).

<img class="centered" width="60%;" src="/assets/images/2026-08-10-shortcut-setup.png" />

## How to run: command line

In terminal, run:

```
shortcuts run "soUSD"
```

## How to run: AppleScript

```
tell application "Shortcuts Events" to run shortcut "soUSD"
```

## Alternative: Mac command line script

Tested in zsh shell with Python 3.13.15 with web3 package installed (note below).

```
#!/usr/bin/env python3
import json
from web3 import Web3

# 1. Official foundation-grade Fuse Network JSON-RPC nodes
RPC_ENDPOINTS = [
    "https://rpc.fuse.io",
    "https://chainstacklabs.com",
    "https://pocket.network"
]

w3 = None
for url in RPC_ENDPOINTS:
    try:
        temp_w3 = Web3(Web3.HTTPProvider(url, request_kwargs={'timeout': 8}))
        if temp_w3.is_connected():
            w3 = temp_w3
            break
    except Exception:
        continue

if not w3:
    print("Error: All public Fuse Network foundation nodes are currently unreachable.")
    exit()

# 2. Target Vault Contract Address (Solid USD Vault)
vault_address = w3.to_checksum_address("0x75333830E7014e909535389a6E5b0C02aA62ca27")

# 3. Compile clean layout ABIs mapping the production architecture
vault_abi = json.loads('[{"inputs":[],"name":"hook","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
hook_abi = json.loads('[{"inputs":[],"name":"accountant","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
accountant_abi = json.loads('''
[
    {
        "inputs": [],
        "name": "accountantState",
        "outputs": [
            {"internalType": "address", "name": "payoutAddress", "type": "address"},
            {"internalType": "uint96", "name": "highWaterMark", "type": "uint96"},
            {"internalType": "uint128", "name": "interestEarned", "type": "uint128"},
            {"internalType": "uint128", "name": "totalFeesOwed", "type": "uint128"},
            {"internalType": "uint96", "name": "exchangeRate", "type": "uint96"},
            {"internalType": "uint16", "name": "allowedExchangeRateChangePerSecond", "type": "uint16"},
            {"internalType": "uint16", "name": "managementFee", "type": "uint16"},
            {"internalType": "uint64", "name": "lastUpdateTimestamp", "type": "uint64"},
            {"internalType": "bool", "name": "isPaused", "type": "bool"},
            {"internalType": "uint24", "name": "minimumUpdateDelayInSeconds", "type": "uint24"},
            {"internalType": "uint16", "name": "performanceFee", "type": "uint16"},
            {"internalType": "uint16", "name": "managementFeeAddress", "type": "uint16"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
''')

try:
    # Step A: Query the Vault to find its active hook router module
    vault_contract = w3.eth.contract(address=vault_address, abi=vault_abi)
    hook_address = vault_contract.functions.hook().call()
    checksum_hook = w3.to_checksum_address(hook_address)
    
    # Step B: Query the Hook to find the current active Accountant engine
    hook_contract = w3.eth.contract(address=checksum_hook, abi=hook_abi)
    accountant_address = hook_contract.functions.accountant().call()
    checksum_accountant = w3.to_checksum_address(accountant_address)
    
    # Step C: Extract the full accountantState tuple from the live node
    accountant_contract = w3.eth.contract(address=checksum_accountant, abi=accountant_abi)
    state = accountant_contract.functions.accountantState().call()
    
    # Index 4 isolates the uint96 exchangeRate parameter from the V2 Accountant state tuple
    raw_rate = state[4]
    normalized_rate = raw_rate / 10**18
    
    print("     --- Solid Yield State Extracted Successfully ---")
    # print(f"     Current Accountant Address: {checksum_accountant}")
    print(f"\n     Raw Integer Value:         {raw_rate}")
    # print(f"     True Conversion Rate:      {normalized_rate:.6f}")
    ratenow =raw_rate / 1000000
    print(f"\033[34m\n     Price:                     $ {ratenow} / soUSD\n\033[0m")
    
except Exception as e:
    print(f"Execution failed inside contract layer: {e}")
```

Web3 package may need to be added with:

```
/Applications/Xcode.app/Contents/Developer/usr/bin/python3 -m pip install web3  
```

## Resources

- Solid project at [https://www.solid.xyz](https://www.solid.xyz)
- Referral for you to get $10 if you create your Solid account and use it (i.e. make one deposit and 3 purchases totaling $75 within 30 days) (and I get $15): [https://www.solid.xyz/refer?ref=N849V](https://www.solid.xyz/refer?ref=N849V)

## Shortcut content

<img class="centered" width="60%;" src="/assets/images/2026-08-10-shortcut-content.png" />
