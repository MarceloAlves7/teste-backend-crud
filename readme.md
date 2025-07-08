Pedido System
Sistema simples de pedidos desenvolvido com:

Django REST Framework (backend)

SQLite (banco de dados)

Google Pub/Sub Emulator (mensageria)

Docker + Docker Compose

React (frontend - opcional)

JWT Authentication

🚀 Como rodar o projeto
✅ 1. Clone o repositório
bash
Copy
Edit
git clone https://github.com/seu-usuario/pedido-system.git
cd pedido-system
✅ 2. Crie o ambiente virtual (caso vá rodar sem Docker)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

pip install -r requirements.txt
✅ 3. Configure o banco de dados
bash
Copy
Edit
cd backend
python manage.py makemigrations
python manage.py migrate
✅ 4. Suba os containers (API, Pub/Sub)
bash
Copy
Edit
docker-compose up --build
Isso sobe:

api → Django rodando em localhost:8000

pubsub → Pub/Sub Emulator rodando em localhost:8085

✅ 5. Rode o worker em outro terminal
Este processo escuta mensagens do Pub/Sub e simula tarefas assíncronas (ex: envio de e-mails):

bash
Copy
Edit
docker exec -it pedido_worker sh
# dentro do container:
python pedidos/pubsub/subscriber.py
Caso queira rodar localmente (fora do Docker):

bash
Copy
Edit
source venv/bin/activate
python backend/pedidos/pubsub/subscriber.py
🔑 Autenticação JWT
Após registrar um usuário, obtenha o token:

POST http://localhost:8000/api/token/

json
Copy
Edit
{
  "email": "seu@email.com",
  "password": "suasenha"
}
Use o access token para autenticar chamadas protegidas:

http
Copy
Edit
Authorization: Bearer SEU_TOKEN_AQUI
📬 Exemplo de envio de pedido (via Postman)
POST http://localhost:8000/api/pedidos/

json
Copy
Edit
{
  "itens": [
    { "produto": 1, "quantidade": 2 }
  ]
}
🐳 Portas utilizadas
Serviço	Porta Local
Django API	8000
Pub/Sub	8085
React (opcional)	3000