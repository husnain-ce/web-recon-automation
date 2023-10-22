# Automated Penetration Testing Tool

This Python-based tool automates several important penetration testing tasks, including:

- Subdomain enumeration
- Port scanning
- Directory enumeration

The tool integrates well-known penetration testing tools like Knockpy, Nmap, and Gobuster, and outputs the results into both a MySQL database and text files for further analysis.

## Installation
`pip install -r requirements`
- Enter the api keys and then
`sudo python3 main.py`

## Usage

Before running the script, ensure you have a MySQL server running and the necessary credentials at hand. Replace the necessary placeholders in the code with your actual MySQL credentials.



You will be prompted to enter the domain you want to test. After entering the domain, the tool will start performing the tasks and will store the results in the MySQL database and the corresponding text files in the `autoscan` directory.

## Note

Use this tool responsibly. Ensure you have legal permission to perform penetration testing on the target domain.

