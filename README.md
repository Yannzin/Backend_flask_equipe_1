# Projeto Localiza

É um sistema de rastreamento de veículos, permite fazer o cadastro de veículos e localizá
los.

## Passos para reproduzir
1. Extrair arquivo zipado, abrir a pasta descompactada no VsCode.
2. Excluir as pastas: .venv e migrations. 

### 3. Criar um ambiente virtual
```bash
python -m venv venv / ou python3 -m venv .venv
```
### 4. Ativar o ambiente virtual
```bash
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux
```

### 5. Instalar dependências dentro do ambiente
```bash
pip install -r requirements.txt
```

### Caso precise desativar o ambiente
```bash
deactivate
```


6. Crie e aplique as migrations:
**Caso seu projeto já possua um arquivo app.db dentro da pasta app, delete-o**
```python

# Para iniciar o banco de dados
flask db init # Só é necessário se seu projeto ainda não tiver a pasta migrations

# Para fazer a primeira migração
flask db migrate -m "Initial migration"

# Para salvar o banco de dados
flask db upgrade
```

### Iniciando aplicação (Localmente)
Inicie o servidor: `flask run` 

Abra no navegador: `http://localhost:5000`

### Iniciando aplicação (Servidor)
Inicie o servidor: `python run.py`/ ou `python3 run.py`

Depois acesse a url pelo navegador.

## Para descobrir a url da aplicação

No terminal rode: ipconfig
Procure por:    Endereço IPv4:..... (Endereço/ ou Url) "Copie a url no seu navegador, seguido da porta"

(:8000 Porta)

Exemplo: 192.168.5.777:8000 
        
 

## Requisitos
- Linux (Ubuntu/Debian recomendado), ou Windows (10/11 recomendado). 
- Python 3.10
- Git (opcional, para controle de versão)
- Postgres Sql / PgAdmin

## Instalação rápida
```bash
# 1) clone (ou copie os arquivos já disponibilizados)
git clone https://github.com/Yannzin/Backend_flask_equipe_1
cd Backend_Flask

# 2) crie e ative venv (Python 3.10)
python3.10 -m venv venv
source venv/bin/activate

# 3) instale dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4) rode a aplicação
python run.py
```

Abra no navegador: `http://localhost:5000`

## Como subir para o github
1. Crie um repositório no GitHub com seu nome: `Backend_Flask_<seunome>`.
2. Faça um commit com as alterações no código


### Comandos úteis
```bash
git init
git add .
git commit -m "Projeto primeiro commit"
git remote add origin https://github.com/SEU_USUARIO/NOME_REPOSITORIO.git
git push -u origin main
```
