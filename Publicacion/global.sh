#!/bin/bash

# Descarga primero ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

# Descomprime el archivo descargado
tar -xvzf ngrok-v3-stable-linux-amd64.tgz

# Elimina el archivo comprimido
rm -rf ngrok-v3-stable-linux-amd64.tgz

# Mueve el ejecutable de ngrok a /usr/local/bin para que esté disponible globalmente
sudo mv ngrok /usr/local/bin/

# Agrega el token de autenticación de ngrok (reemplaza YOUR_AUTH_TOKEN con tu token real)
ngrok authtoken YOUR_AUTH_TOKEN

# Inicia ngrok en el puerto 11434 (puedes cambiar el puerto si es necesario)
ngrok http 11434

