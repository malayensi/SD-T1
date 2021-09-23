# SD-T1

Integrantes:
 - Marcelo Quiñones 
 - Tommy Rinaldi

Los códigos utilizados en este trabajo se basan en su mayoría en los proporcionados en la ayudantía

Requisitos
1. Tener redis instalado y corriendo como en la ayudantía por ejemplo, donde se utilizó docker
2. Tener módulos de python instalados como los de grpc, flask, redis

Para ejecutar el software se debe
1. se debe tener corriendo redis
2. se debe ejecutar server.py en una terminal 
3. se debe ejecutar app.py en otra terminal
4. se debe abrir localhost en el puerto 5000

La configuración de Redis es la siguiente:
- config set maxmemory-policy volatile-lru
- maxmemory 10mb
