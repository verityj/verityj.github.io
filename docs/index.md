---
layout: default
---

# T-Mobile home internet gateway settings

The T-Mobile home internet is an awesome product. But it does come with certain setup and control annoyances. Here, I tackle the main one for me: how to turn on and off the wifi networks so I can keep them off when not in use. If the gateway is not transmitting on its wifi radios, the hope is that by not having to run wifi the gateway may run a little cooler, maybe use less power, and have a smoother connection in general with less to do.
The code below is meant to work with the **Arcadyan KVD21 gateway** and was tested with gateway firmware **1.00.18**.

## WiFi radio turn on and off with a Python script

This script does the following:
1. Displays the current wifi network status (name, password, ssid broadcast state, radio enabled or disabled)
2. Asks the user to choose to either make no changes or enable/disable the wifi networks (radios)

[Direct link to my script](https://github.com/verity-s/verity-s.github.io/blob/main/arcadyan-wifi.py) or if you prefer, check out [raw view of my script](https://raw.githubusercontent.com/verity-s/verity-s.github.io/main/T-Mobile/arcadyan-wifi.py)

***Before the first time using the script*** make sure to open the script file in any text editor and provide your admin password for the gateway to enable script access.

Script usage:

```sh
# In the Terminal:
$ python3 arcadyan-wifi.py
# Read the current wifi information displayed
# Make a choice if you want to change anything
# Make a choice to keep or remove the generated configuration files
```
And that's all there is to it!

Af you encounter any issues, ask on [my github issues page](https://github.com/verity-s/verity-s.github.io/issues)

## WiFi radio status information with a quick shell script

This script makes no changes but instead is meant to quickly show all of the WiFi information from your T-Mobile gateway.

***Before the first time using the script*** make sure to open the script file in any text editor and provide your admin password for the gateway to enable script access.

[Direct link to my script](https://github.com/verity-s/verity-s.github.io/blob/main/T-Mobile/wifi-info.sh) or if you prefer, check out [raw view of my script](https://raw.githubusercontent.com/verity-s/verity-s.github.io/main/T-Mobile/wifi-info.sh)

Change the `admin-password-here` in the script below.
```sh
#!/bin/zsh

# Admin password between quotes:
admin="admin-password-here"

curl -sSX POST http://192.168.12.1/TMI/v1/auth/login -d '{"username": "admin", "password": "'$admin'"}' > temp.txt
token="${$(sed '6!d' temp.txt):14:284}"
rm temp.txt

curl -sS http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H "Authorization:Bearer $token"
echo -e # move to next line to complete output 
```

Script usage:
1. Create a shell script file with the content above. Name it something like `wifi.sh`.
2. Make sure your gateway admin password is provided inside the script.
3. In the command line, make the script file executable and run it:
```sh
$ chmod +x wifi.sh
$ ./wifi.sh
# Read the output to see all the WiFi settings
```
 
# What is happening inside those scripts

Let's dig in.

#### Step 1: Get the access token

Access token is a long string of characters that the gateway generates. A command needs to know this token every time information is read from the gateway or written. We need it for the following steps. A new token is generated every time the token command is issued. 
The command to obtain the current token is used in both scripts above and that is the only part that requires the gateway administrator password. The default administrator password is printed on the back of your gateway, along with the default wifi password.
**Do not confuse** the _Admin password_ and the _Wi-Fi password_. Both are printed on the back of your gateway. The _Wi-Fi password_ is used to connect to the wireless networks that your gateway is broadcasting. What we need here is the _Admin password_ that lets us access the gateway settings.
>If you previously changed and now can't remember your admin password, simply reset the gateway. All settings will reset to default, including the wireless network names and passwords, as well as the admin password. To reset the gateway, follow the usual instructions: hold pressed the _Reset_ button on the back of the gateway, with some sort of pin that fits through that tiny hole to reach the button behind it. It is hidden for a reason, but is a lifesaver when you need to go back to the beginning.
The command to get the current gateway access token:
```sh
curl -X POST http://192.168.12.1/TMI/v1/auth/login -d '{"username": "admin", "password": "admin-password-here"}'
```

#### Step 2: Read the current gateway WiFi settings

Now that we know the token, we can read the current gateway network settings. What are the WiFi names, are the names being broadcasted, what are the WiFi passwords, which antennas are actually enabled, 2.4 GHz and/or 5.0 GHz, etc?
The fastest way to show complete information is to use my second shell script. That's all it is meant for.
The second way, in case you may want to make any changes (you don't have to, everything is an option) is to run the python script above. It will write a text file with all the current WiFi information (called "x-wifi-input.txt"). You will have an option to delete or keep that file at the end of that python script, so no worries there.
The command to read the current gateway WiFi settings:
```sh
curl http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H "Authorization:Bearer your-token-here"
```

#### Step 3: Change WiFi settings

This is an optional step in my python script. You may choose to change nothing or one of the WiFi antennas, or both. Or disable all WiFi.
Thinking backwards, what we intend to do is to send new WiFi settings to the gateway.
To be able to send the settings we first need to create a file of settings to send. My python script creates it and calls it "x-wifi-output.txt". (Just like the other text file, you can choose to delete this once the script is done or keep it for your review later.)
To know what settings options we need to write, the python script asks to choose between five (5) options. To see it in context, here is the full output of the script up to this point:
```sh
$ python3 arcadyan-wifi-mano.py 

Step 1. Obtaining access token

Step 2. Obtaining wifi radio status

--------------------------------------------------
- Current wifi information in "x-wifi-input.txt" -
--------------------------------------------------
  "2.4ghz":
    "isRadioEnabled": false
      "isBroadcastEnabled": false
      "ssidName": "1-2",
      "wpaKey": "somepasswordhere"

  "5.0ghz":
    "isRadioEnabled": false
      "isBroadcastEnabled": false
      "ssidName": "1",
      "wpaKey": "somepasswordhere"

-------------------------
- Next: choose a number -
-------------------------

1 - change nothing
2 - enable 2.4 GHz
3 - enable 5.0 GHh
4 - enable both 2.4 and 5.0 GHz
5 - disable wifi radios
> 
``` 
Once you make a choice, the scripts proceeds to generate a text file that is ready to be sent to the gateway.
The scripts sends the new generated settings file to the gateway.
For fun, I also put out on the screen the command to run if you prefer to execute it manually. You could comment out or delete the line 121 from my script that executes the write:
```sh
cat x.wifi-output.txt | curl -d "@-" http://192.168.12.1/TMI/v1/network/configuration\?set\=ap -H 'Authorization: Bearer token-goes-here'
```

#### Finally, some script cleanup

The python script wants to keep it clean by removing the text files it created. Remember, those contain the initial and final WiFi settings (the final file is only created if we chose to change anything). So, at the end, the script waits for you to hit ENTER (RETURN on some systems) and do the clean up, or hit control - c to exit the script right there, without going on to the clean up.
On Mac OS, the text files are moved to the user Trash folder (`~/.Trash/`).
```sh
-------------------------
- Next: choose a number -
-------------------------

1 - change nothing
2 - enable 2.4 GHz
3 - enable 5.0 GHh
4 - enable both 2.4 and 5.0 GHz
5 - disable wifi radios
> 1
Proceeding with 1: exit with no changes.

---------------------
- Finally: clean up -
---------------------

Press ENTER/RETURN to erase the generated wifi config files.
Press CONTROL-C (^C) to keep the generated wifi config files.
?
``` 

# More joy

Thanks for everyone's encouragement and support to keep pushing me forward and onwards!

[PayPal support](https://www.paypal.com/donate/?hosted_button_id=D2SU4GD8PEXCW)
