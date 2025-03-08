# Fundamentos Matematicos de Vision Robotica

## Gestion de entornos

Se recomienta utilizar [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) o [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) para la gestion de entornos en Python.

Tutorial de instalacion: [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#verify-your-install)

Si elegiste utilizar conda o miniconda el siguiente paso es crear un entorno de trabajo con:

```sh
conda create --name <NOMBRE> python=3.8
```
>NOTA: Reemplazar <NOMBRE> por el nombre que le queres poner al entorno, por ejemplo vision-robotica.

Una vez creado el entorno ejecutar el siguiente comando para activar el nuevo entorno:
```
conda activate <NOMBRE>
```
## Instalacion de paquetes

Instalar los paquetes necesarios para la materia con:
```
pip install -r requirements.txt
```


