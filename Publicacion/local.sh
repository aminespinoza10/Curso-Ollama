#!/bin/bash

# Modifica el servicio de Ollama
sudo nano /etc/systemd/system/ollama.service

# Agrega en este archivo abierto lo siguiente:
Environment="OLLAMA_HOST=0.0.0.0"

# Reinicia tus servicios para que los cambios tengan efecto
sudo systemctl daemon-reload

# Reinicia el servicio de Ollama
sudo systemctl restart ollama

# Verifica que el servicio esté corriendo correctamente
sudo systemctl status ollama

# Obtener la IP de tu máquina
ip addr show