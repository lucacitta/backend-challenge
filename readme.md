# Desafio BackEnd LinkChar

## Creado por Luca Cittá Giordano :D

### instalacion

* Clonar el repositorio con: git clone https://github.com/lucacitta/backend-challenge.git
* Instalar Python (version utilizada 3.9.6) https://www.python.org/downloads/
* Crear y activar un virtualenv.
* Instalar las dependencias de requirements.txt usando 'pip install -r requirements.txt'
* Instalar 'rabbitmq server' (version utilizada 3.9.12). https://www.rabbitmq.com/download.html
* Una vez todo listo realizar las primeras migraciones y estaremos listos para la puesta en marcha.
    python manage.py makemigrations
    python manage.py migrate

### Puesta en marcha

* Inciar el servidor de rabbitmq, en una nueva consola movernos al directorio donde se encuentre el archivo 'rabbitmq-server.bat' y ejecutarlo.
    cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.9.12\sbin
    rabbitmq-server.bat

* Iniciar celery utilizando el siguiente codigo en la raiz de nuestro proyecto.
    celery -A challenge  worker -l info --pool=solo

* Iniciar el servidor de django utilizando el siguiente codigo en la raiz del proyecto.
    python manage.py runserver

### Funcionamiento

La api conta con 5 endpoints (Todos deben ser accedidos mediante metodo POST):
    */populate-apis: Llama a la task de celery encargada de popular la base de datos, es necesario realizarlo primero.

    */keyword: Recibe en el body una keyword y devuelve las apis cuyo nombre comiencen con la misma, debe enviarse la informacion de la siguiente manera: {"keyword":"palabra_clave"}

    */category: Funciona similar a /keyword, pero esta recibe una categoria y devuelve las apis que pertenezcan a la misma, la informacion debe enviarse siguiendo la misma logica {"category":"categoria"}

    */ordered-list: No recibe ningun parametro y devuelve la informacion de todas las apis ordenadas segun el pk (id).

    */item: El endpoint recibe un pk especifico y devuelve toda la informacion sobre la api que tenga ese id. Debe recibir la informacion siguiendo la misma logica que los endpoints anteriores {"pk":"id"}