from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Caminhos dos arquivos
ARQUIVO_CONVIDADOS = 'convidados.xlsx'
ARQUIVO_REGISTRO = 'registro-entradas.csv'

# Carregar a lista de convidados
if not os.path.exists(ARQUIVO_CONVIDADOS):
    raise FileNotFoundError("O arquivo convidados.xlsx não foi encontrado!")

df_convidados = pd.read_excel(ARQUIVO_CONVIDADOS)

# Criar o arquivo de registro, se não existir
if not os.path.exists(ARQUIVO_REGISTRO):
    with open(ARQUIVO_REGISTRO, 'w') as f:
        f.write('Código,Nome,Data\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar', methods=['POST'])
def validar_qrcode():
    codigo = request.form['codigo']
    # Verificar se o código existe na lista de convidados
    if codigo in df_convidados['Código'].values:
        nome = df_convidados.loc[df_convidados['Código'] == codigo, 'Nome'].values[0]
        # Verificar se o código já foi usado
        registro_df = pd.read_csv(ARQUIVO_REGISTRO)
        if codigo in registro_df['Código'].values:
            return f"O convite de {nome} já foi usado!"
        else:
            # Registrar entrada
            with open(ARQUIVO_REGISTRO, 'a') as f:
                f.write(f'{codigo},{nome},\n')
            return f"Bem-vindo(a), {nome}!"
    else:
        return "Convite inválido!"

if __name__ == '__main__':
    app.run(debug=True)