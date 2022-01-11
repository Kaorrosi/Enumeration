"""
    A simple subdomain enumerator
"""

from argparse import ArgumentParser

def enumerate(domainname,file):
    import requests
    import sys

    sub_list = open(file).read()
    subdoms = sub_list.splitlines()

    for sub in subdoms:
        sub_domains = f"http://{sub}.{domainname}"

        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", sub_domains)

if __name__== '__main__':
    choices = {'subdom': enumerate}
    parser = ArgumentParser()
    parser.add_argument('action', choices=choices)
    parser.add_argument('domain')
    parser.add_argument('file')
    args = parser.parse_args()
    function = choices[args.action]
    function(args.domain, args.file)