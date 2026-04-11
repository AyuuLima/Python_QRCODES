import pandas as pd
import qrcode
import os

# Criar pasta local (funciona no CI)
os.makedirs("qrcodes", exist_ok=True)

# Arquivo Excel (tem que estar no repo)
arquivo_excel = "convidados.xlsx"

# Ler Excel
df = pd.read_excel(arquivo_excel)

# Gerar QR Codes
for index, row in df.iterrows():
    codigo = str(row["Código"])
    nome = row["Nome"]

    conteudo = f"Convidado: {nome} | Código: {codigo}"

    qr = qrcode.make(conteudo)

    # Evitar erro com nomes (espaço, acento)
    nome_arquivo = nome.strip().replace(" ", "_")

    caminho = f"qrcodes/{codigo}_{nome_arquivo}.png"
    qr.save(caminho)

    print(f"QR gerado: {caminho}")

print("QR Codes gerados com sucesso!")