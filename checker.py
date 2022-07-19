import os,sys,requests,time,random,string,json
from colorama import Fore






os.system("cls && title TIKTOK NAME CHECKER")


with open("proxies.txt", encoding="utf-8") as f:
    proxies = [i.strip() for i in f]   


def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())


class Checking:

    def Check():
        while True:
            username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(4))
            proxy = random.choice(proxies)
            x = requests.get('https://tiktok.com/@' + username,
                proxies = {
                    'http'   :'http'+'://'+ proxy
                }

            )  
            if x.status_code == 200:
                print(center(f"         {Fore.LIGHTGREEN_EX}Checked: {Fore.LIGHTBLUE_EX}{username} {Fore.YELLOW}Status: {Fore.RED}INVALID {Fore.LIGHTBLUE_EX}PROXY: {proxy}"))
            else:
                print(center(f"         {Fore.LIGHTGREEN_EX}Checked: {Fore.LIGHTBLUE_EX}{username} {Fore.YELLOW}Status: {Fore.GREEN}VALID {Fore.LIGHTBLUE_EX}PROXY: {proxy}"))





if __name__ == '__main__':
        print(center(f'''
        {Fore.RED}    
╔╦╗┬┬┌─┌┬┐┌─┐┬┌─
 ║ │├┴┐ │ │ │├┴┐
 ╩ ┴┴ ┴ ┴ └─┘┴ ┴
        {Fore.RESET}  
        '''))
        while True:
            Checking.Check()
