import redis

myHostname = "treinamentoazureelvenworks.redis.cache.windows.net"
myPassword = "UUyaGPCAVMhiEjOL4MprsjQJTPJIXymaSAzCaA4jDk8="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping retornado : " + str(result))

result = r.set("Message", "Olá!, O cache está funcionando com Python!")
print("Mensagem envia para cache : " + str(result))

result = r.get("Message")
print("Mensagem retornada do cache : " + result.decode("utf-8"))

result = r.client_list()
print("Lista de clientes retornados : ")
for c in result:
    print(f"id : {c['id']}, addr : {c['addr']}")