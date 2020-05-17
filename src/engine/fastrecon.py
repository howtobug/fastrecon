from os import system
from sys import argv, exit
import socket

try:
        domain = argv[1]
except:
        print("Syntax Error")
        exit()

system("mkdir /results/{}".format(domain))


def dig(domain):
        system("dig {} > results/{}/dig.txt".format(domain, domain))

def host(domain):
        system("host {} > results/{}/host.txt".format(domain, domain))


def assetfinder(domain):
        system("assetfinder --subs-only {} > results/{}/subdomain-enumeration.txt".format(domain, domain))

def dnscan():
        system("python3 tools/dnscan/dnscan.py -d {} -w tools/dnscan/subdomains-1000.txt > results/{}/subdomain-bruteforce-demo.txt".format(domain, domain))
        system("cat results/{}/subdomain-bruteforce-demo.txt | grep '{}' | cut -d '-' -f2 > results/{}/subdomain-bruteforce.txt ".format(domain, domain, domain))

def getallurls():
        system("cat results/{}/all-subdomains.txt | gau > results/{}/spider.txt".format(domain, domain))

def nmap():
        system("nmap -iL results/{}/ips.txt > results/{}/nmapOutput.txt".format(domain, domain))

def waybackurls():
        system("touch results/{}/all-subdomains.txt".format(domain))
        system("cat results/{}/subdomain-enumeration.txt >> results/{}/all-subdomains.txt".format(domain, domain))
        system("cat results/{}/subdomain-bruteforce.txt >> results/{}/all-subdomains.txt".format(domain, domain))
        system("cat results/{}/all-subdomains.txt | waybackurls > results/{}/waybackurls.txt".format(domain, domain))

def aquatone():
        #system("mkdir engine/results/{}/aquatone".format(domain))
        system("cat results/{}/all-subdomains.txt | aquatone -out results/{}/aquatone".format(domain, domain))

def getIps():
        system("cp results/{}/all-subdomains.txt tools/getIps".format(domain))
        system("python3 tools/getIps/getIps.py {} > results/{}/ips.txt".format(domain, domain))


dig(domain)
host(domain)
assetfinder(domain)
dnscan()
nmap()
waybackurls()
aquatone()
getIps()
getallurls()