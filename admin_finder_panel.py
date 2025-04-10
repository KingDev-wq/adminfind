import requests
import os
from bs4 import BeautifulSoup
import time

# Limpa terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Arte inicial
def arte_ascii():
    print("\033[91m")
    print(r"""
                 :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
    """)
    print("\033[0m")
    print("\033[1;92m[ King Admin Finder Painel - V1.0 ]\033[0m\n")

# Lista de caminhos de admin comuns
def carregar_paths():
    return [
        "admin", "admin/login", "login", "cpanel", "administrator", "adminarea", "user/login",
        "dashboard", "auth", "backend", "manage", "painel", "adm", "admincp", "usuarios", "wp-admin",
        "admin1", "admin2", "adminpanel", "admin-console", "admin_area", "system/login", "admincontrol"
    ]

# Verifica se há um formulário com input de senha
def contem_login(html):
    soup = BeautifulSoup(html, 'html.parser')
    for form in soup.find_all('form'):
        if any('password' in str(i).lower() for i in form.find_all('input')):
            return True
    return False

# Exibe os resultados encontrados
def painel_resultados(resultados):
    print("\n\033[1;94m+----------------------------------------+")
    print("|       PAINÉIS ENCONTRADOS (SCAN)       |")
    print("+----------------------------------------+\033[0m")
    for r in resultados:
        print(f"\033[92m[✓] {r}\033[0m")
    print("\033[1;94m+----------------------------------------+\033[0m")
    print(f"\033[96mTotal: {len(resultados)} painel(is) encontrado(s).\033[0m\n")

# Função principal
def admin_finder(base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (KingAdminFinder)'}
    achados = []

    print(f"\n\033[93m[+] Iniciando escaneamento de: {base_url}\033[0m\n")
    time.sleep(1)

    for path in carregar_paths():
        url = f"{base_url.rstrip('/')}/{path}"
        try:
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code in [200, 301, 302]:
                if contem_login(r.text):
                    print(f"\033[92m[+] Painel com login: {url}\033[0m")
                    achados.append(url)
                else:
                    print(f"\033[96m[~] Possível painel: {url}\033[0m")
            else:
                print(f"\033[90m[-] {url} ({r.status_code})\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Falha ao acessar: {url}\033[0m")

    painel_resultados(achados)

# Execução principal
if __name__ == "__main__":
    limpar()
    arte_ascii()
    alvo = input("\033[95m>> Digite a URL alvo (ex: https://site.com): \033[0m").strip()
    if not alvo.startswith("http"):
        alvo = "http://" + alvo
    admin_finder(alvo)
