import subprocess
import paramiko
from shodan import Shodan

def store_results_in_database(subdomain, details, cursor):
    print(f"Storing results for {subdomain} in the database")
    cursor.execute("INSERT INTO domains (name, ip) VALUES (%s, %s)", (subdomain, details['ip']))
    cursor.execute("INSERT INTO nmapscan (ip, open_ports) VALUES (%s, %s)", (details['ip'], ','.join(details['protocols'])))

def write_results_to_file(subdomain, details, project_name):
    print(f"Writing results for {subdomain} to files")
    with open(f"{project_name}/autoscan/domains.txt", "a") as f:
        f.write(f"{subdomain}, {details['ip']}\n")

    with open(f"{project_name}/autoscan/nmapscan.txt", "a") as f:
        f.write(f"{details['ip']}, {','.join(details['protocols'])}\n")

def run_gobuster_and_store_results(subdomain, cursor, project_name):
    print(f"Running Gobuster on {subdomain}")
    try:
        gobuster_result = subprocess.run(['gobuster', 'dir', '-u', subdomain, '-w', '/path/to/wordlist', '-t', '50', '-to', '10m', '-o', 'gobuster_results.txt'], check=True, timeout=600, text=True, capture_output=True)
        print(f"Writing Gobuster results for {subdomain} to file and database")
        with open(f"{project_name}/autoscan/gobuster_results.txt", "a") as f:
            f.write(gobuster_result.stdout)
        cursor.execute("INSERT INTO gobuster (domain, result) VALUES (%s, %s)", (subdomain, gobuster_result.stdout))
    except subprocess.TimeoutExpired:
        print(f"Gobuster scan timed out for {subdomain}")
    except subprocess.CalledProcessError as e:
        print(f"Gobuster scan failed for {subdomain} with error: {e}")

def get_ssh_fingerprint_and_search_shodan(details, ssh, api):
    print(f"Getting SSH fingerprint for {details['ip']}")
    try:
        ssh.connect(details['ip'], username='test', password='test')  # Use dummy credentials
    except paramiko.AuthenticationException:  # We expect authentication to fail
        key = ssh.get_server_key()  # Get the server's public key
        fingerprint = ':'.join(f"{i:02x}" for i in key.get_fingerprint())

        # Search Shodan with Fingerprint
        print(f"Searching Shodan with fingerprint for {details['ip']}")
        result = api.search(fingerprint)
        print(result)
