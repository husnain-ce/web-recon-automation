import paramiko
from shodan import Shodan


def setup_shodan(api_key='You_Key'):
    # Set up SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Set up Shodan client
    api = Shodan(api_key)

    return ssh, api