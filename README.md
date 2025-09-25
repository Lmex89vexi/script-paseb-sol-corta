# Guía de Inicio para script-paseb-sol-corta

Este proyecto contiene scripts para realizar solicitudes a un servidor API y otros procesos automatizados relacionados.

## Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga los archivos en tu máquina local.
2. Instala las dependencias necesarias ejecutando:

```bash
python3.11 -m venv .venv_scripts
pip install -r requirements.pip
source .venv_scripts/bin/activate
```

## Reemplazar Varible en main.py:
```bash
APISOL_ORQUESTADOR = "http://172.20.80.1:61997/"
```

Para ejecutar el script principal, utiliza el siguiente comando:

```bash
python main.py
```

Asegúrate de tener configurados correctamente los parámetros necesarios en los archivos de configuración o constantes según tu caso de uso.

## Archivos Principales

- `main.py`: Script principal de ejecución.
- `api_server_request.py`: Funciones para realizar solicitudes al servidor API.
- `constantes.py`: Variables y constantes utilizadas en el proyecto.
- `requirements.pip`: Lista de dependencias necesarias.

## Notas

- Si encuentras algún error relacionado con dependencias, revisa que todas estén correctamente instaladas.
- Puedes modificar los scripts según tus necesidades específicas.

---

Si tienes dudas o necesitas soporte, contacta al responsable del repositorio.
