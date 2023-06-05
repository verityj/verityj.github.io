# This script is tested to work with T-Mobile home internet Arcadyan KVD21 gateway.
# Tested on Mac OS 13 Ventura with python 3.9.6.

# Purpose:
# Display current wifi information.
# Choose to exit with no changes or enable/disable 2.4 GHz and 5.0 GHz wifi networks.

# This script needs your Arcadyan administrator password to run, type it into this file below.

# Usage:
# Run from the command line:
# python3 arcadyan-wifi.py

from os import popen
from os import remove
from subprocess import run
from pathlib import Path
import sys

# -------------------------------------------------------------
# ----- ATTENTION, PASSWORD NEEDED BELOW FOR GATEWAY ACCESS ---
# -------------------------------------------------------------

# Administrator password goes between quotes on next line 
admin_pass = "admin-password-here"

# These two files may be created by this script
temp_wifi_input = Path("x-wifi-input.txt")
temp_wifi_out = Path("x-wifi-output.txt")

#################
# Get the token #
#################
# curl -s hides the progress bar (verbose is -v)
# curl --progress-bar shows a simplier progress meter
# curl -S with silence activated still shows errors (or --show-error)
# curl -X POST http://192.168.12.1/TMI/v1/auth/login -d '{"username": "admin", "password": "admin-password-goes-here"}'

def get_token():
    curlyl = "{" # curly brackets don't play nice in formatted string
    curlyr = "}"
    print("\nStep 1. Obtaining access token")
    result = popen(f"curl -sSX POST http://192.168.12.1/TMI/v1/auth/login -d '{curlyl}\"username\": \"admin\", \"password\": \"{admin_pass}\"{curlyr}'")
    output = result.read()
    token_start = output.find('\"token\":')
    return output[token_start + 10 : -6]

##############################
# Get wifi radio information #
##############################
# curl http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H "Authorization:Bearer token-goes-here"

def get_wifi_info():
    print("\nStep 2. Obtaining wifi radio status")
    result = popen(f"curl -sS http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H \"Authorization:Bearer {token}")
    output = result.read()
    return output

###############################
# Change 2.4 GHz radio status #
###############################

def radio24(switch):
    print(f"Radio 2.4 GHz next status: {switch}.")
    in_file.seek(0)
    if switch == 'enabled':
        out_file.write(in_file.read(151) + "true,\n")
    elif switch == 'disabled':
        out_file.write(in_file.read(151) + "false,\n")
    else:
        out_file.write(in_file.read(151) + in_file.readline())
    in_file.readline()
    i = 1
    while i <= 26:
        out_file.write(in_file.readline())
        i += 1

###############################
# Change 5.0 GHz radio status #
###############################

def radio50(switch):
    print(f"Radio 5.0 GHz next status: {switch}.")
    if switch == 'enabled':
        out_file.write("    \"isRadioEnabled\": true,\n")
        in_file.readline() # skip the original radio line in input
    elif switch == 'disabled':
        out_file.write("    \"isRadioEnabled\": false,\n")
        in_file.readline() # skip the original radio line in input
    else:
        out_file.write(in_file.readline())
    # copy the rest of input file
    i = 1
    while i <= 15:
        out_file.write(in_file.readline())
        i += 1

####################################
# Write new wifi radio information #
####################################
# cat x.wifi-output.txt | curl -d "@-" http://192.168.12.1/TMI/v1/network/configuration\?set\=ap -H 'Authorization: Bearer token-goes-here'
# adding curl -v for verbose output

def write_wifi_info():
    # Need extra variables to pass into a format string
    vertical = "|"
    b = "\\"
    
    command_bash = "cat {} {} curl -vd \"@-\" http://192.168.12.1/TMI/v1/network/configuration{}?set=ap -H \"Authorization:Bearer {}".format(temp_wifi_out, vertical, b, token)
    command_zsh = "cat {} {} curl -vd \"@-\" http://192.168.12.1/TMI/v1/network/configuration{}?set{}=ap -H \"Authorization:Bearer {}".format(temp_wifi_out, vertical, b, b, token)
    
    print(f"\nCarefully check the {temp_wifi_out} file before proceeding with the Arcadyan change command. May issue manually:")
    
    print("\nIn Z-shell, command to implement the change is:\n" + command_zsh)
    print("\nIn Bash shell, command to implement the change is:\n" + command_bash, "\n")
    
    print("- Give it time, the new file is being sent.")
    print("- When complete, there will be an audible \"done\".\n")
    
    # Default shell is sh, execute Bash command to apply changes:
    result = popen("cat {} {} curl -vd \"@-\" http://192.168.12.1/TMI/v1/network/configuration{}?set=ap -H \"Authorization:Bearer {} ; say done".format(temp_wifi_out, vertical, b, token))
    
    print(result.read()) # causes to wait for shell to finish.
    print(f"Changes are applied. Check by running the script again. Delete {temp_wifi_input} and {temp_wifi_out}.\n")

####################
# Run the commands #
####################

# Check the script before starting
if admin_pass == "admin-password-here":
    print("\nPlease edit the script file in any text editor to provide the Arcadyan admin password.\nThen run this script and have fun.\n")
    sys.exit(0)

token = get_token()

with open(temp_wifi_input, "w") as file_f:
    file_f.write(get_wifi_info())

print("\n" + "-" * 50)
print("- Current wifi information in \"{}\" -".format(temp_wifi_input))
print("-" * 50)

in_file = open(temp_wifi_input)
# 2.4 GHz radio information
in_file.seek(2)
print(in_file.readline(11)) # show 2.4 GHz
i = 1
while i <= 5:
    in_file.readline()
    i += 1
print(in_file.readline(27)) # show radio status
i = 1
while i <= 7:
    in_file.readline()
    i += 1
print(in_file.readline(33)) # show broadcast status
in_file.readline()
print(in_file.readline(), end='') # show ssid name
in_file.readline()
print(in_file.readline()) # show password
while i <= 18:
    in_file.readline()
    i += 1
print(in_file.readline(11)) # show 5.0 GHz
i = 1
while i <= 5:
    in_file.readline()
    i += 1
print(in_file.readline(27)) # show radio status
i = 1
while i <= 7:
    in_file.readline()
    i += 1
print(in_file.readline(33)) # show broadcast status
in_file.readline()
print(in_file.readline(), end='') # show ssid name
in_file.readline()
print(in_file.readline()) # show password

print("""-------------------------
- Next: choose a number -
-------------------------

1 - change nothing
2 - enable 2.4 GHz
3 - enable 5.0 GHh
4 - enable both 2.4 and 5.0 GHz
5 - disable wifi radios""")
choice = input('> ')
print(f"Proceeding with {choice}: ", end='')

if choice == '1':
    print("exit with no changes.")
elif choice == '2':
    print("enable 2.4 GHz radio.")
    out_file = open(temp_wifi_out, 'w')
    radio24('enabled')
    radio50('unchanged')
    out_file.close()
    write_wifi_info()
elif choice == '3':
    print("enable 5.0 GHz radio.")
    out_file = open(temp_wifi_out, 'w')
    radio24('unchanged')
    radio50('enabled')
    out_file.close()
    write_wifi_info()
elif choice == '4':
    print("enable both 2.4 and 5.0 GHz radio.")
    out_file = open(temp_wifi_out, 'w')
    radio24('enabled')
    radio50('enabled')
    out_file.close()
    write_wifi_info()
elif choice == '5':
    print("disable wifi radios.")
    out_file = open(temp_wifi_out, 'w')
    radio24('disabled')
    radio50('disabled')
    out_file.close()
    write_wifi_info()
else:
    print("unrecognized option. Exiting with no changes.")
    in_file.close()
    out_file.close()

in_file.close()

############
# clean up #
############

print('''
---------------------
- Finally: clean up -
---------------------
''')

print("Press ENTER/RETURN to erase the generated wifi config files.")
print("Press CONTROL-C (^C) to keep the generated wifi config files.")
input("? ")

if Path(temp_wifi_input).exists():
    print("\nDeleting {}\n".format(temp_wifi_input))
    remove(temp_wifi_input)
if Path(temp_wifi_out).exists():
    print("Deleting {}\n".format(temp_wifi_out))
    remove(temp_wifi_out)
