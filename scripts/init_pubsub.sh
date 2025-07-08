#!/bin/bash

# Ativa o modo "exit on error"
set -e

echo "Instalando libs Python ..."

pip install --no-cache-dir google-cloud-pubsub --break-system-packages  

echo "Iniciando o Pub/Sub Emulator..."
gcloud beta emulators pubsub start --project=my-project-id --host-port=0.0.0.0:8085 &
sleep 5

# Exporta a variável pro Python conseguir encontrar o emulador
export PUBSUB_EMULATOR_HOST=localhost:8085
export GOOGLE_CLOUD_PROJECT=my-project-id

echo "Criando tópicos e subscriptions..."
python3 scripts/setup_pubsub.py

# Mantém o container rodando
tail -f /dev/null
