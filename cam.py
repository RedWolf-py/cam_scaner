import socket

def testar_porta(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f"[+] {ip}:{port} PORTA ABERTA")
        s.close()
    except:
        print(f"{ip}:{port} FECHADA")
        pass  

# Recebe a base do IP
base_ip = input('Digite as 3 primeiras casas do IP (exemplo: 192.168.0): ')

# usuario digita o inicio e o fim do intervalo
inicio = int(input("Digite o número inicial do IP final (ex: 100): "))
fim = int(input("Digite o número final do IP final (ex: 400): "))

# IPS com base do inicio ao fim
ips = [f"{base_ip}.{i}" for i in range(inicio, fim + 1)]

# Lista de portas para testar
portas = [80, 81, 554, 8000, 8080, 8888, 5000, 37777]

for ip in ips:
    print(f"\n🔍 Testando IP: {ip}...")
    for porta in portas:
        testar_porta(ip, porta)
