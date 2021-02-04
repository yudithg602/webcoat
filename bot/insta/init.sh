#!/bin/bash


init()
{
	sudo apt-get update
	sudo apt-get install python3-pip -y
	pip3 install anticaptchaofficial
}

init
