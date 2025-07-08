import os
import json
from google.cloud import pubsub_v1

PROJECT_ID = "my-project-id"
TOPIC_ID = "criar-pedido"

# Aponta para o Pub/Sub Emulator local
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_pedido_created(pedido_id):
    message = json.dumps({ "order_id": pedido_id }).encode("utf-8")
    future = publisher.publish(topic_path, message)
    print(f"[PubSub] Pedido {pedido_id} publicado com sucesso.")
