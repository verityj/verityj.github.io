# verity-s.github.io  ::  T-Mobile scripts

## T-Mobile home internet gateway settings

The T-Mobile home internet is an awesome product. But it does come with certain setup and control annoyances. Here, I tackle the main one for me: how to turn on and off the wifi networks so I can keep them off when not in use. If the gateway is not transmitting on its wifi radios, the hope is that by not having to run wifi the gateway may run a little cooler, maybe use less power, and have a smoother connection in general with less to do.
The code below is meant to work with the **Arcadyan KVD21 gateway** and was tested with gateway firmware **1.00.18**.

### WiFi radio turn on and off with a Python script

This script does the following:
1. Displays the current wifi network status (name, password, ssid broadcast state, radio enabled or disabled)
2. Asks the user to choose to either make no changes or enable/disable the wifi networks (radios)

[Direct link to the script](https://github.com/verity-s/verity-s.github.io/blob/main/T-Mobile/arcadyan-wifi.py)

[Direct link to display raw script](https://raw.githubusercontent.com/verity-s/verity-s.github.io/main/T-Mobile/arcadyan-wifi.py)

> ***Before the first time using the script*** make sure to open the script file in any text editor and provide your admin password for the gateway to enable script access.

Script usage:

```sh
# In the Terminal:
$ python3 arcadyan-wifi.py
# Read the current wifi information displayed
# Make a choice if you want to change anything
# Make a choice to keep or remove the generated configuration files
```
And that's all there is to it!

### WiFi radio status information with a quick shell script

This script makes no changes but instead is meant to quickly show all of the WiFi information from your T-Mobile gateway.

> ***Before the first time using the script*** make sure to open the script file in any text editor and provide your admin password for the gateway to enable script access.

[Direct link to the shell script shown below](https://github.com/verity-s/verity-s.github.io/blob/main/T-Mobile/wifi-info.sh)

Change the `admin-password-here` in the script below.
```
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
1. Create a shell script file with the content above. Name it something like `wifi-info.sh`.
2. Make sure your gateway admin password is provided inside the script.
3. In the command line, make the script file executable and run it:
```
$ chmod +x wifi-info.sh
$ ./wifi-info.sh
# Read the output to review all the WiFi settings
```

## Encourage the author

Thanks for everyone's encouragement and support to keep pushing me forward and onwards!

Tip a satoshi to   <img src="/assets/images/strike.png" width="12px;" />  [strike.me/verity](https://strike.me/verity/)  <img src="/assets/images/strike.png" width="12px;" />

Or [PayPal support](https://www.paypal.com/donate/?hosted_button_id=D2SU4GD8PEXCW)

<img src="/assets/images/qr.png" width="40px;" />

## License

Open sourced under the [MIT license](LICENSE.md).
