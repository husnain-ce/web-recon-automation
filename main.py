import os
import warnings
from cryptography.utils import CryptographyDeprecationWarning
import json
import nmap
import subprocess
from knock_scan import get_subdomains
import paramiko
import requests
from shodan import Shodan
from time import sleep
from mysql.connector import connect
from tqdm import tqdm
from get_domains import find_common_domains 
from nmap_scan import nmap_scan
from db import setup_database
from shodan_conf import setup_shodan
from op import *


warnings.simplefilter("ignore", CryptographyDeprecationWarning)

def main(domain, project_name="scan_process"):
    subdomains = get_subdomains(domain)
    print(subdomains)

    common_domains = find_common_domains(subdomains)

    # Perform Nmap Scan on All IPs
    print(common_domains)
    # nmap_scan(common_domains)

    os.makedirs(f"{project_name}/autoscan", exist_ok=True)

    db, cursor = setup_database(project_name)

    ssh, api = setup_shodan()

    for subdomain, details in common_domains.items():
        store_results_in_database(subdomain, details, cursor)
        write_results_to_file(subdomain, details, project_name)
        run_gobuster_and_store_results(subdomain, cursor, project_name)
        get_ssh_fingerprint_and_search_shodan(details, ssh, api)

    db.commit()

    sleep(1)


if __name__ == "__main__":
    domain = "domain.com"
    main(domain)

