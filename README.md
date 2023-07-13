# azure-redis-python
#Clone Repo:
1. Clone Repo:
    $ git clone https://github.com/Formacao-SRE/azure-redis-python.git
#Command Line: 
$ apt update && apt install python3-pip -y
$ pip3 install redis
$ python3
>>> import redis
>>> r = redis.StrictRedis(host='treinamentoazureelvenworks.redis.cache.windows.net', port=6380, db=0, password='UUyaGPCAVMhiEjOL4MprsjQJTPJIXymaSAzCaA4jDk8=', ssl=True)
>>> r.set('treinamento', 'Azure Elvenworks')
True
>>> r.get('treinamento')
b'Azure Elvenworks'


#Aplicação01: 
$ python3 Aplicacao01.py 


#Aplicação02: 
This code is part of an Amazon ElastiCache Tutorial


1. Install dependencies:

    $ pip3 install -r requirements.txt

2. Configure environment variables:

    $ export FLASK_APP=Aplicacao02.py
    $ export SECRET_KEY=UUyaGPCAVMhiEjOL4MprsjQJTPJIXymaSAzCaA4jDk8=
    $ export REDIS_URL=rediss://:UUyaGPCAVMhiEjOL4MprsjQJTPJIXymaSAzCaA4jDk8=@treinamentoazureelvenworks.redis.cache.windows.net:6380/0

3.  Start the server on port 5000:

    $ flask run -h 0.0.0.0 -p 5000