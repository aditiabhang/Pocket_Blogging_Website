#!/bin/bash
## make sure we have an updated package index
#sudo apt-get update
#
## install deb packages to get system python and virtualenv utility
#sudo apt install -y python3 python3-pip python3-dev build-essential python-virtualenv
#virtenv_dir="/home/hyperwarp/kp-regress-deps/venv"
#
## ensure base dir exists for venv
#mkdir -p "$virtenv_dir"
#
## build virtualenv with python3 as the venv interpreter
#virtualenv -p python3 "$virtenv_dir/hyperwarp"
#
## update pip inside venv
#"$virtenv_dir/hyperwarp/bin/pip" install -U pip
#
## install deps into venv
#"$virtenv_dir/hyperwarp/bin/pip" install -r /home/hyperwarp/kp-regress-deps/requirements.txt
