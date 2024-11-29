# ✈️ Mape.ia

# Estrutura do diretório
- Esboço da estrutura

```
project/
|── frontend/ # interface do usuário
|── backend/ # aplicação do servidor, API
|── database/ # arquivos relacionados ao banco de dados
|── scripts/ # scripts de inicialização e deploy
|── tests/ # testes do projeto
|── docker-compose.yml # opcional, configuração do ambiente
```


## Como executar:
Para executar facilmente o backend e o frontend, execute primeiro os comandos separadamente, para configurar o ambiente,
e depois rode:
``python start.py``

### backend:
```bash
pip install -r requirements.txt
fastapi dev main.py
```

### frontend:
```bash
cd frontend
npm install
npm run dev
```

### Passos tomados no desenvolvimento
- Svelte puro com vite: npm create vite@latest ->  svelte -> typescript
