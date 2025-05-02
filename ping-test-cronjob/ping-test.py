#!/usr/bin/env python3
import subprocess
import datetime

ip_address = "8.8.8.8" #edit IP Address desired here
# url = "google.com" # edit URL desired here
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

command = ['ping', '-c', '5', ip_address] # change ip_address to url for URL ping
ping_result = subprocess.run(command, capture_output=True, text=True)

with open ("/<full directory path>/ping_output.txt", "a") as file: 
    file.write("\nPing test at: " + timestamp + "\n")
    file.write(ping_result.stdout)

#print("Ping output written to ping_output.txt")