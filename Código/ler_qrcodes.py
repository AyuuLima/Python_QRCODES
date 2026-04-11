import cv2
from pyzbar.pyzbar import decode
import os
import re

# Pasta onde estão as imagens dos QR Codes
PASTA_QRCODES = "qrcodes"

# Verifica se a pasta existe
if not os.path.exists(PASTA_QRCODES):
    print(f"❌ ERRO: A pasta '{PASTA_QRCODES}' não foi encontrada!")
    exit()

# Lista todas as imagens na pasta
arquivos = [f for f in os.listdir(PASTA_QRCODES) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Função para extrair o número do arquivo
def extrair_numero(arquivo):
    match = re.match(r"(\d+)", arquivo)  # Pega só os números no começo do nome
    return int(match.group(1)) if match else float('inf')  # Se não encontrar número, coloca no final

# Ordena os arquivos numericamente
arquivos.sort(key=extrair_numero)

if not arquivos:
    print("❌ Nenhuma imagem de QR Code encontrada na pasta!")
    exit()

# Percorre todas as imagens e lê os QR Codes
for arquivo in arquivos:
    caminho_completo = os.path.join(PASTA_QRCODES, arquivo)
    imagem = cv2.imread(caminho_completo)

    # Se não conseguiu carregar a imagem, pule para a próxima
    if imagem is None:
        print(f"⚠️ Erro ao carregar a imagem: {arquivo}. Verifique se o arquivo existe e está no formato correto.")
        continue

    # Decodifica o QR Code
    qrcodes = decode(imagem)

    if qrcodes:
        for qr in qrcodes:
            valor_qrcode = qr.data.decode("utf-8")
            print(f"📌 QR Code encontrado em {arquivo}: {valor_qrcode}")
    else:
        print(f"⚠️ Nenhum QR Code detectado em {arquivo}.")
