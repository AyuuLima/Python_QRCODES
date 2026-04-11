FestaQR – Geração de QR Codes para Lista de Convidados
Descrição do Projeto

Este projeto tem como objetivo automatizar a geração de QR Codes a partir de uma lista de convidados armazenada em uma planilha Excel. Cada convidado recebe um QR Code individual, que é salvo em uma pasta local.

O sistema foi desenvolvido em Python e também containerizado com Docker, permitindo execução padronizada em qualquer ambiente.

Tecnologias Utilizadas
Python 3.11
pandas
qrcode
pillow
openpyxl
Docker
GitHub Actions (CI/CD)

Estrutura do Projeto
FestaQR/
│
├── .github/workflows/     # Pipeline CI/CD
├── qrcodes/               # QR Codes gerados
├── convidados.xlsx        # Lista de convidados
├── gerar_qrcodes.py       # Script principal
├── requirements.txt       # Dependências
├── Dockerfile             # Container da aplicação
└── README.md

Como Executar Localmente
1. Criar ambiente virtual (opcional)
python -m venv .venv
2. Ativar ambiente
.venv\Scripts\activate
3. Instalar dependências
pip install -r requirements.txt
4. Executar o projeto
python gerar_qrcodes.py
