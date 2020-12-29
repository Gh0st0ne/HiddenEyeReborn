import subprocess
import ctypes
from os import system, getuid, path
from time import sleep
import requests
from platform import system as systemos, architecture
from subprocess import check_output
from Defs.Languages import *

RED, GREEN, DEFAULT = '\033[91m', '\033[1;32m', '\033[0m'

installGetText()
languageSelector()



def checkConnection(host='https://google.com'):  # Connection check
    system('clear')
    try:
        req = requests.get(host, timeout=10)
        if req.status_code == 200:
            print("{0}HURRAY!! Internet is available.. We can Continue{1}".format(
                GREEN, DEFAULT))
            print("\n\n{0}Wait! Checking for Neccesary Packages{1}...\n ".format(
                GREEN, DEFAULT))
            return True
    except:
        return False


if checkConnection() == False:
    print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}

          {0}[{1}!{0}]{1} ^Network error^. Verify your Internet connection.\n
'''.format(RED, DEFAULT))
    exit()

def verCheck():
    system('clear')
    print("{1}[{0}>{1}] {0}Checking For Updates{2}...".format(GREEN, RED, DEFAULT ))
    ver_url = 'https://raw.githubusercontent.com/darksecdevelopers/hiddeneye/master/version.txt'
    ver_rqst = requests.get(ver_url)
    ver_sc = ver_rqst.status_code
    if ver_sc == 200:
        with open('version.txt') as f:
            ver_current = f.read()
            ver_current = ver_current.strip()
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()
        if ver_current == github_ver:
            print("{1}[{0}+{1}] {0}[Up-To-Date]- {2}v {3}".format(GREEN, RED, DEFAULT, github_ver))
            sleep(3)
        else:
            print("{1}[{0}>{1}] {0}Their Is A Newer Version Available{2}.\n".format(GREEN, RED, DEFAULT))
            print("{1}[{0}+{1}] {0}[Current]- {2}v {3}\n{1}[{0}+{1}] {0}[Available]- {2}v.{4}".format(GREEN, RED, DEFAULT, ver_current, github_ver)) 
            print("{1}[{0}>{1}] {1}Updating To The Latest Version {0}[v {3}]... \n{1}[{0}>{1}] {0}Please Wait\n".format(GREEN, RED, DEFAULT, github_ver))
            system("git clean -d -f > /dev/null && git pull -f > /dev/null")
            with open('version.txt') as f:
                ver_current = f.read()
                ver_current = ver_current.strip()
            print("{1}[{0}>{1}] {0}Version Status After Update.{2}.\n".format(GREEN, RED, DEFAULT))
            print("{1}[{0}+{1}] {0}[Current]- {2}v {3}\n{1}[{0}+{1}] {0}[Available]- {2}v.{4}".format(GREEN, RED, DEFAULT, ver_current, github_ver))
            sleep(5)
            system("clear")
    else:
        print('{1}[{0}^{1}] {0}Failed To Get Update [Status:{1}{3}{0}]\n'.format(GREEN, RED, DEFAULT))

     
def checkPHP(): # PHP installation Check
	if 256 != system('which php > /dev/null'):  # Checking if user have PHP
		print(" {2}* {0}PHP INSTALLATION FOUND".format(GREEN, DEFAULT, RED))
	else:
		print("{0}**{2} PHP NOT FOUND\n {0}** {2} Installing PHP... ".format(RED, GREEN, DEFAULT))
		system('apt-get install php > /dev/null')


def checkNgrok():  # Ngrok check
    if path.isfile('Server/ngrok') == False:  # Is Ngrok downloaded?
        print('[*] Ngrok Not Found !!')
        print('[*] Downloading Ngrok...')
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        req = requests.get(url)
        with open(filename, "wb") as file_obj:
            file_obj.write(req.content)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm ' + filename)
        system('clear')

def checkOpenport(): # Openport Check
	if 256 == system('which openport > /dev/null'):
		print('[*] Openport not Installed !!')
		print("[*] Installing Openport...")
		if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
			filename = 'arm/latest.deb'
		else:
			ostype = systemos().lower()
			if architecture()[0] == '64bit':
				filename = 'debian64/latest.deb'.format(ostype)
			else:
				filename = 'debian32/latest.deb'.format(ostype)
		url = 'https://openport.io/download/' + filename
		req = requests.get(url)
		filename2 = 'openport.deb'
		with open(filename2, "wb") as file_obj:
			file_obj.write(req.content)
		system('chmod 777 openport* && dpkg -i openport* > /dev/null && rm openport.deb && clear')
		checkOpenportinstall()
def checkOpenportinstall(): # Check If installed properly
	if 256 == system('which openport > /dev/null'):
		print('[*] Openport not Installed correctly, Try installing it manually !!')
		print('[*] Check Here ... https://openport.io/download')
		input('\n Press Enter To Continue')
	else:
		print('[*] Openport Installation Success !!')
		sleep(1)

def checkPagekite(): # Check Pagekite
	if path.isfile('Server/pagekite.py') == False:
		print('[*] Pagekite Not Found !!')
		print('[*] Downloading Pagekite...')
		url = 'https://pagekite.net/pk/pagekite.py'
		req = requests.get(url)
		filename = 'pagekite.py'
		with open(filename, "wb") as file_obj:
			file_obj.write(req.content)
		system('chmod 777 pagekite.py && mv pagekite.py Server/pagekite.py')
		print('\n[*] Pagekite install Success !!')
		print('\n[!] Remember: Pagekite Supports only Python2, Not Supports Python3')
		print('[!] So Make Sure You Have installed Python2 as well, if Wants To use Pagekite Tunnel.')
		system('cd Server && chmod 777 * -R')
		input('\n Press Enter To Continue')
		

def checkLocalxpose():  # Localxpose check
    if path.isfile('Server/loclx') == False:  # Is Localxpose downloaded?
        print('[*] Localxpose Not Found !!')
        print('[*] Downloading Localxpose...')
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        req = requests.get(url)
        with open("loclx-linux-download.zip", "wb") as file_obj:
            file_obj.write(req.content)
        system('unzip loclx-linux-download.zip && rm loclx-linux-download.zip')
        system('mv loclx-linux-* loclx && mv loclx Server/')
        system('clear')


def checkbinaryLT():  # LocalTunnel Binary File check.
    if path.isfile('Server/lt') == False:  # Is LocalTunnel downloaded?
        print('[*] LocalTunnel Binary File Not Found !!')
        print('[*] Downloading LocalTunnel...')
        url = "https://www.wa4e.com/downloads/lt-linux.zip"
        req = requests.get(url)
        with open("lt-linux.zip", "wb") as file_obj:
            file_obj.write(req.content)
        system("unzip lt-linux.zip && rm lt-linux.zip")
        system("mv lt* lt && mv lt Server/lt ")
        system('clear')


def checkLT():  # Ask to install npm,node.js,localtunnel(packages).
    system('cd Server && chmod 777 * -R')
    if 256 == system('which lt > /dev/null'):
        system('clear')
        print("{0}[{1}?{0}] Do You Want To Install LOCALTUNNEL(Tunneling Service) Packages.\n{0}[{1}*{0}]{1} May take time , Skip if not wants to use LocalTunnel(Package Version).".format(RED, GREEN, DEFAULT))
        choice = input(
            " \n({1}Y{2}/{2}(N)>> {2}".format(RED, GREEN, DEFAULT)).upper()
        if choice == 'Y':
            system('clear')
            installLT()
        elif choice == 'N':
            print("\n{0}[{1}!{0}]{0} You can not use LocalTunnel(Package Version).\n{0}[{1}!{0}]{0} But still You Can Use LocalTunnel(Binary Version).\n\n\n".format(
                RED, GREEN, DEFAULT))
            input('Press Enter To Continue')
            system('clear')
        else:
            return checkLT()
    else:
        print("[*] LocalTunnel Packages Found !!")
        sleep(2)
        system('clear')


def installLT():  # Localtunnel check
    print('[*] Installing LocalTunnel...')
    if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
        system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel-termux;clear")
        checkagainLT()
    else:
        system("apt-get -y update;apt -y install nodejs npm;npm cache clean -f;npm i -g n;n stable;npm i -g localtunnel;clear")
        checkagainLT()


def checkagainLT():  # Check if Localtunnel installed correctly or not.
    if 256 == system('which lt > /dev/null'):
        system('clear')
        print('{1}[ERROR]: LocalTunnel packages haven\'t been installed correctly...{0}'.format(
            DEFAULT, RED))
        print('')
        input('[^] Press Enter To Go Back To installation..')
        checkLT()
    else:
        print('{1}[SUCCESS] LocalTunnel Installed.{0}'.format(DEFAULT, GREEN))
        sleep(2)


def checkPermissions():

    if systemos() != "Windows":
        if getuid() == 0:
            print("{0}Permissions granted!".format(GREEN))
        else:
            print(
                "{0}if Possible ! Please run as '{1}sudo{0}'".format(RED, GREEN))
            
    else:
        print("{0}Windows system not yet compatible. Make sure you're using a *Unix OS.{1}".format(RED, DEFAULT))
        exit()
