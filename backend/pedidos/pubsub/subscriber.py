import os
import json
import django
import time
import sys
from datetime import datetime

# Caminho absoluto até a pasta 'backend'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(BASE_DIR)

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pedido_system.settings")
django.setup()

from google.cloud import pubsub_v1
from pedidos.models import Pedido

PROJECT_ID = "my-project-id"
SUBSCRIPTION_ID = "criar-pedido-sub"
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}")

def callback(message):
    data = json.loads(message.data.decode("utf-8"))
    pedido_id = data.get("order_id")

    log(f"[Worker] Nova mensagem recebida para pedido ID = {pedido_id}")

    try:
        pedido = Pedido.objects.get(id=pedido_id)
    except Pedido.DoesNotExist:
        log(f"[Erro] Pedido ID={pedido_id} não encontrado.")
        message.ack()
        return

    log(f"[Processamento] Validando pedido...")
    time.sleep(1)

    pedido.status = 'confirmado'
    pedido.save()
    log(f"[Processamento] Pedido {pedido_id} confirmado com sucesso.")

    log(f"[Email] E-mail de confirmação enviado para o cliente do pedido {pedido_id}.")
    time.sleep(1)

    log(f"[Notificação] Push notification enviada para app mobile.")


    message.ack()
    log(f"[Worker] Mensagem ACK enviada ao Pub/Sub.\n")

log(f"[Worker] Escutando subscription '{SUBSCRIPTION_ID}'...")
subscriber.subscribe(subscription_path, callback=callback)

# Mantém o worker vivo
while True:
    time.sleep(60)
