from google.cloud import pubsub_v1
import os

os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"

project_id = "my-project-id"
topic_id = "criar-pedido"
subscription_id = "criar-pedido-sub"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

topic_path = publisher.topic_path(project_id, topic_id)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

try:
    publisher.create_topic(request={"name": topic_path})
    print(f"Tópico criado: {topic_path}")
except Exception as e:
    print(f"Erro ao criar tópico: {e}")

try:
    subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})
    print(f"Subscription criada: {subscription_path}")
except Exception as e:
    print(f"Erro ao criar subscription: {e}")
