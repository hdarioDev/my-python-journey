# Django REST API Project

Proyecto de API REST desarrollado con Django REST Framework como parte del curso de Python.

## Requisitos

- Python 3.8+
- Django 4.2+
- Django REST Framework

## Instalación

1. Clona el repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```
5. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

- `projects/` - Aplicación principal de la API
- `simpleCrud/` - Configuración del proyecto Django
- `manage.py` - Script de administración de Django

## Licencia

Este proyecto es parte de un curso educativo.
