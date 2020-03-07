## ejecutar este proyecto

Si no existe el virtual env, crearlo

```bash
virtualenv -p python3.6 venv
```

Activar el entorno

```bash
source venv/bin/activate
```

instalar requerimientos

```bash
pip install -r
```

Crear y llenar, con los datos de acceso a la base de datos, el archivo `database.env`, tal como en el ejemplo `database.env.example`

Crear la base de datos de posgis. Este script crea la base de datos y le agrega la extension postgis a la misma,  a partir de los datos del archivo _.env_. Si ya se cuenta con la bd o si se desea crearla en otro cliente de postgres como _pgadmin_ o _psql_, se puede omitir este paso

```bash
bash create_db.sh
```

crear y ejecutar las migraciones (carga modelos y apps definidas en el proyecto a la base de datos )

```bash
python manage.py makemigrations
python manage.py migrate
```

crar un superusuario para la app *django-admin* que trae por default. La consola pedira usuario, correo y contraseña

```bash
python manage.py createsuperuser
```

correr el servidor django

```bash
export $(cat database.env | xargs)
python manage.py runserver
```
---

### asi se creo de 0 este proyecto

```bash
virtualenv -p python3.6 venv

source venv/bin/activate

pip install django

django-admin startproject geocaptura $(pwd)

python manage.py startapp cafererias
```
