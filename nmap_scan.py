import nmap


def nmap_scan(common_domains):
    # common_domains = {'api-careers.tkxel.com': {'ip': '52.87.100.152', 'domains': ['digitalocean.atlan.com', 'k8s-infraatlan-2aa95f32fb-1174152055.us-east-1.elb.amazonaws.com', 'api-careers.tkxel.com', 'careers.tkxel.com', 'www.careers.tkxel.com', 'prodfeed-lb.spinmasterstudios.com', 'prodfeed-ssl.spinmasterstudios.com', 'salsifyproductfeed-bridge-inst-517359578.us-east-1.elb.amazonaws.com', 'agencialoopers.com.br', 'cpanel.agencialoopers.com.br', 'ftp.agencialoopers.com.br', 'webmail.agencialoopers.com.br', 'www.agencialoopers.com.br', 'logtails.earth-71b883.evergreen.space']}}
    nm = nmap.PortScanner()
    for subdomain, details in common_domains.items():
        ip = details['ip']
        print(f"Running Nmap scan on IP: {ip}")
        nm.scan(ip, '-p- -sV -vv --open -T4')
        details["protocols"] = nm[ip].all_protocols()
        if ip in nm.all_hosts():
            details["protocols"] = nm[ip].all_protocols()
            print(details)
        else:
            details["protocols"] = []