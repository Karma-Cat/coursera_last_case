#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

sender = "automation@example.com"
recipient = "username@example.com"
body = "Please check your system and resolve the issue as soon as possible."

def cpu_use():
    cpu_per = psutil.cpu_percent(percpu=False)
    return cpu_per < 80

def disk_space():    
    disk = shutil.disk_usage("/home")
    space_per = (disk[1]/disk[0]) * 100
    return space_per < 20

def memory_space():
    mem_value = psutil.virtual_memory()[1]/1000000
    return mem_value > 500


def localhost():
    ip_localhost = socket.gethostbyname(socket.gethostname())
    return ip_localhost == '127.0.0.1'

if not cpu_use():
    emails.generate_error_report(sender, recipient, 
                         "Error - CPU usage is over 80%", body)

if not disk_space():
    emails.generate_error_report(sender, recipient, 
                         "Error - Available disk space is less than 20%", body)

if not memory_space():
    emails.generate_error_report(sender, recipient, 
                         "Error - Available memory is less than 500MB", body)

if not localhost():
    emails.generate_error_report(sender, recipient, 
                         "Error - localhost cannot be resolved to 127.0.0.1", body)