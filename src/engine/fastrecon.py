from os import system
from sys import argv, exit
import socket

try:
        domain = argv[1]
except:
        print("Syntax Error")
        exit()

system("mkdir engine/results/{}".format(domain))


def dig(domain):
        system("dig {} > engine/results/{}/dig.txt".format(domain, domain))

def host(domain):
        system("host {} > engine/results/{}/host.txt".format(domain, domain))


def assetfinder(domain):
        system("assetfinder --subs-only {} > engine/results/{}/subdomain-enumeration.txt".format(domain, domain))

def dnscan():
        system("python3 engine/tools/dnscan/dnscan.py -d {} -w engine/tools/dnscan/subdomains-1000.txt > engine/results/{}/subdomain-bruteforce-demo.txt".format(domain, domain))
        system("cat engine/results/{}/subdomain-bruteforce-demo.txt | grep '{}' | cut -d '-' -f2 > engine/results/{}/subdomain-bruteforce.txt ".format(domain, domain, domain))

def getallurls():
        system("cat engine/results/{}/all-subdomains.txt | gau > engine/results/{}/spider.txt".format(domain, domain))

def nmap():
        #system("nmap -iL engine/results/{}/ips.txt > engine/results/{}/nmapOutput.txt".format(domain, domain))
        system("touch engine/results/{}/nmapOutput.txt".format(domain))

def waybackurls():
        system("touch engine/results/{}/all-subdomains.txt".format(domain))
        system("cat engine/results/{}/subdomain-enumeration.txt >> engine/results/{}/all-subdomains.txt".format(domain, domain))
        system("cat engine/results/{}/subdomain-bruteforce.txt >> engine/results/{}/all-subdomains.txt".format(domain, domain))
        system("cat engine/results/{}/all-subdomains.txt | waybackurls > engine/results/{}/waybackurls.txt".format(domain, domain))

def aquatone():
        #system("mkdir engine/results/{}/aquatone".format(domain))
        system("cat engine/results/{}/all-subdomains.txt | aquatone -out engine/results/{}/aquatone".format(domain, domain))

def getIps():
        system("cp engine/results/{}/all-subdomains.txt engine/tools/getIps".format(domain))
        system("python3 engine/tools/getIps/getIps.py {} > engine/results/{}/ips.txt".format(domain, domain))


dig(domain)
host(domain)
assetfinder(domain)
dnscan()
nmap()
waybackurls()
aquatone()
getIps()
getallurls()