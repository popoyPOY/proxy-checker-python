from time import sleep
import random
import requests


def save_deadproxy(proxy):
    file = open("deadproxy.txt","a")
    file.write(f"{proxy}  ")
    file.write("\n")
    file.close()

def save_live_proxy(proxy):
    with open("liveproxies.txt","a") as file:
        return file.write(f"{proxy}\n") 

def proxy():
    with open('proxies.txt','r') as file:
        line = file.readlines()
        proxy = random.randint(0,len(line)-1)
        test_proxy = line[proxy]
        proxies={'http': f'http://{test_proxy}'}
        try:
            session = requests.Session()
            response = session.get('http://icanhazip.com',headers={'User-Agent': 'Bla'}, proxies=proxies,timeout=3)
            jsonize = response.text
            if response.status_code == 200:
                print(f"LIVE -> {test_proxy} | Status Code: {response.status_code}")
                save_live_proxy(test_proxy)
            else:
                print(f"DEAD -> {test_proxy} | Status Code: {response.status_code}")
        except:
            print(f"DEAD -> {test_proxy} | Status Code: 0")
            save_deadproxy(proxies)

def main():
    with open('proxies.txt','r') as file:
        line = file.readlines()
        for x in range(0,len(line)):
            proxy()



if __name__ == "__main__":
    main()
