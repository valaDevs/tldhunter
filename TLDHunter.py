import requests
from multiprocessing import Pool

logo = '''
╔╦╗╦  ╔╦╗╦ ╦┬ ┬┌┐┌┌┬┐┌─┐┬─┐
 ║ ║   ║║╠═╣│ ││││ │ ├┤ ├┬┘
 ╩ ╩═╝═╩╝╩ ╩└─┘┘└┘ ┴ └─┘┴└─
            Author: Vabro
            Github: github.com/valaDevs
'''

def check_tld(domain, tld):
    url = f"http://{domain}.{tld}"
    try:
        response = requests.head(url)
        if response.status_code == 200:
            print(f"{url} is available!")
    except requests.exceptions.RequestException:
        pass
    
if __name__ == "__main__":
    print(logo)
    domain = input("[+] Enter domain name(without TLD): ")
    tlds = ['com', 'net', 'org', 'edu', 'co', 'io', 'gov','ir','us','ru','fr','br','ca',
        'de','au','uk','in','xyz','top','icu','info','app','io','ai'] # List of TLDs to check

    with Pool() as pool:
        pool.starmap(check_tld, [(domain, tld) for tld in tlds])
