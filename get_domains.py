
import requests
import tqdm
from knock_scan import get_subdomains

def get_domains_by_ip(ip):
    print('get domains..')
    response = requests.get(f"https://api.securitytrails.com/v1/ips/nearby/{ip}", 
                            headers={"APIKEY": "You_Key"})
    data = response.json()

    # Extract the hostnames (domains) from each block
    domains = []
    for block in data["blocks"]:
        domains.extend(block.get("hostnames", []))

    return domains
        
def find_common_domains(subdomains):
    common_domains = {}

    for subdomain in subdomains:
        
        print(f"Processing subdomain: {subdomain}")
        subdomain_ip = subdomain["ip"]
        print(f"Getting domains with the same IP as {subdomain}")
        domains_with_same_ip = get_domains_by_ip(subdomain_ip)
        # if domains_with_same_ip:
            # common_domains[subdomain] = domains_with_same_ip
        if domains_with_same_ip:
                common_domains[subdomain['subdomain']] = {
                    'ip': subdomain_ip,
                    'domains': domains_with_same_ip
                }
    return common_domains



# # Step 3: Find common domains that share the same IP
# common_domains = {}
# for subdomain in tqdm(subdomains, desc="Processing subdomains", ncols=75):
# # for subdomain in subdomains:
#     print(f"Processing subdomain: {subdomain}")
#     subdomain_ip = subdomain["ip"]
#     print(f"Getting domains with the same IP as {subdomain}")
#     domains_with_same_ip = get_domains_by_ip(subdomain_ip)
#     if domains_with_same_ip:
#         common_domains[subdomain] = domains_with_same_ip
        