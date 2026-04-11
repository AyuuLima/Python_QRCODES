from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar a lista de convidados e entradas registradas
convidados_df = pd.read_excel("convidados.xlsx")
try:
    entradas_df = pd.read_csv("registro-entradas.csv")
except FileNotFoundError:
    entradas_df = pd.DataFrame(columns=["codigo", "nome"])

# Função para salvar os registros de entrada
def salvar_registros():
    entradas_df.to_csv("registro-entradas.csv", index=False)

@app.route("/")
def home():
    return "Bem-vindo ao sistema de validação de QR Codes!"


@app.route("/validar", methods=["POST"])
def validar_qrcode():
    global entradas_df  # A declaração global precisa estar aqui antes do uso

    codigo = request.json.get("codigo")
    if not codigo:
        return jsonify({"success": False, "message": "Código não informado."}), 400

    # Verificar se o código está na lista de convidados
    convidado = convidados_df.loc[convidados_df["codigo"] == codigo]
    if convidado.empty:
        return jsonify({"success": False, "message": "Código inválido. Não está na lista de convidados."}), 404

    nome = convidado.iloc[0]["nome"]

    # Verificar se o código já foi registrado
    if not entradas_df.loc[entradas_df["codigo"] == codigo].empty:
        return jsonify({"success": False, "message": f"O convidado {nome} já foi registrado."}), 400

    # Registrar a entrada
    entradas_df = pd.concat([entradas_df, pd.DataFrame({"codigo": [codigo], "nome": [nome]})], ignore_index=True)
    salvar_registros()

    return jsonify({"success": True, "message": f"Bem-vindo(a), {nome}!"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)