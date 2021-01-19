#!/bin/bash
clear


init()
{
	sudo apt-get update
	sudo apt-get install python3-pip libssl-dev -y
	pip3 install --upgrade pip
	pip3 install pipenv
	PATH=~/.local/bin:$PATH && export PATH
	pip3 install python-telegram-bot
	pipenv install python-telegram-bot
}

init
