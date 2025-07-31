# 🛒 Pedido System

Sistema simples de pedidos desenvolvido com:

- **Django REST Framework** (backend)  
- **SQLite** (banco de dados)  
- **Google Pub/Sub Emulator** (mensageria)  
- **Docker + Docker Compose**  
- **React** (frontend - opcional)  
- **JWT Authentication**

---

## 🚀 Como rodar o projeto

### ✅ 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/pedido-system.git
cd pedido-system


Crie o ambiente virtual (caso vá rodar sem Docker)
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

pip install -r requirements.txt

cd backend
python manage.py makemigrations
python manage.py migrate

docker-compose up --build

docker exec -it pedido_worker sh
python pedidos/pubsub/subscriber.py

Rode o worker em outro terminal
source venv/bin/activate
python backend/pedidos/pubsub/subscriber.py




