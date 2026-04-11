import pandas as pd
import qrcode
import os

# Criar a pasta 'qrcodes' se não existir
qrcodes_pasta = r'C:\Projetos\FestaQR\qrcodes'
if not os.path.exists(qrcodes_pasta):
    os.makedirs(qrcodes_pasta)

# Caminho do arquivo Excel
arquivo_excel = r'C:\Projetos\FestaQR\convidados.xlsx'

# Carregar a planilha de convidados com o engine openpyxl
df = pd.read_excel(arquivo_excel, engine='openpyxl')

# Defina o IP da sua máquina
ip_computador = '###.#.#.#:####'  # Substitua com o seu IP real


# Gerar QR Codes
for index, row in df.iterrows():
    codigo = str(row["Código"])  # Código único do convidado
    nome = row["Nome"]

    # Construir a URL com o IP do computador
    url = f"http://{###.###.###}:####/validar?codigo={codigo}"

    # Gerar o QR code
    qr = qrcode.make(url)

    caminho_arquivo = f"qrcodes/{codigo}_{nome}.png"
    qr.save(caminho_arquivo)

    print(f"QR Code gerado para {nome}: {caminho_arquivo}")

print("Todos os QR Codes foram gerados e salvos na pasta 'qrcodes'.")