import json
import subprocess
import glob
import os
import time

def get_subdomains(domain):
    # Enumerate subdomains for a given domain
    print(f"Searching on knockpy {domain}")
    command = f"knockpy {domain}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, universal_newlines=True)
    stdout, _ = process.communicate()  # read the output
    print(stdout)
    
    files = glob.glob(f"knockpy_report/{domain}_*.json")
    
    if not files:
        print(f"No report files found for {domain}")
        return []

    # Sort the files by modification time in descending order
    files.sort(key=os.path.getmtime, reverse=True)

    # Open the most recent file
    with open(files[0], "r") as file:
        data = json.load(file)

    # Extract the subdomains and associated IPs, and remove '_meta' if present
    subdomains = [{'subdomain': k, 'ip': v['ipaddr'][0]} for k, v in data.items() if k != '_meta' and 'ipaddr' in v and v['ipaddr']]

    return subdomains


# Usage


a = get_subdomains('domain.com')



 # files = glob.glob(f"knockpy_report/{domain}_*.json")
    
    # if not files:
    #     print(f"No report files found for {domain}")
    #     return []

    # # Sort the files by modification time in descending order
    # files.sort(key=os.path.getmtime, reverse=True)

    # # Open the most recent file
    # with open(files[0], "r") as file:
    #     data = json.load(file)

    # # Extract the subdomains
    
    # subdomains = list(data.keys())
    
    # if '_meta' in subdomains:
    #     subdomains.remove('_meta')

    # return subdomains