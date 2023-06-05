#!/bin/zsh

# curl -s hides the progress bar (verbose is -v)
# curl --progress-bar shows a simplier progress meter
# curl -S with silence activated still shows errors (or --show-error)

# Admin password between quotes:
admin="admin-password-here"

# First command:
# curl -X POST http://192.168.12.1/TMI/v1/auth/login -d '{"username": "admin", "password": "admin-password-here"}'
# Second command:
# curl http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H "Authorization:Bearer your-token-here"
# (Script from https://github.com/christopherjnelson/Arcadyan-5G-Web-Admin/issues/4)

curl -sSX POST http://192.168.12.1/TMI/v1/auth/login -d '{"username": "admin", "password": "'$admin'"}' > temp.txt
token="${$(sed '6!d' temp.txt):14:284}"
rm temp.txt

curl -sS http://192.168.12.1/TMI/v1/network/configuration\?get=ap -H "Authorization:Bearer $token"
echo -e # move to next line to complete output
