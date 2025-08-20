# Backend_Flask — Curso

Projeto didático para as 3 primeiras aulas de Backend com Framework.

## Primeira aula com exercício
1. Introdução ao Flask, rotas básicas.
2. Templates, HTML dinâmico, Formulários e métodos HTTP.


## Requisitos
- Linux (Ubuntu/Debian recomendado)
- Python 3.10
- Git (opcional, para controle de versão)


**Exercício 1** — adicione uma rota `/hello` que retorna texto simples. Copie esse bloco em `app/routes.py`:
```python
@app.route("/hello")
def hello():
    return "Olá, mundo — esta é a rota /hello"

**Concluido!**
Criamos uma rota que retorna hello no sistema.


