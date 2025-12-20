# Data Cleaner

Una herramienta automatizada para la carga, limpieza y preprocesamiento de datos, diseñada para estandarizar datasets y preparar información para análisis posteriores. 

## Requisitos Previos

Este proyecto utiliza [uv](https://docs.astral.sh/uv/) como gestor de paquetes y entornos virtuales.

Asegúrate de tener `uv` instalado. Puedes consultar la [documentación oficial de uv](https://docs.astral.sh/uv/) para instrucciones detalladas de instalación en tu sistema operativo.


## Instalación

Clona este repositorio en tu máquina local usando git:

```bash
git clone https://github.com/RamonCamacho8/data-cleaner.git
cd data-cleaner
```

Una vez dentro del directorio del proyecto, utiliza `uv` para sincronizar el entorno y las dependencias. Esto creará un entorno virtual y e instalará todo lo necesario automáticamente basándose en el archivo `pyproject.toml`.

```bash
uv sync
```

## Ejecución

Para ejecutar el pipeline principal de limpieza de datos, utiliza el comando `uv run`. Esto asegura que el script se ejecute dentro del entorno virtual gestionado por el proyecto.

```bash
uv run main.py
```

### Ejecución de Pruebas

Para correr la suite de pruebas (unitarias e integración) con `pytest`:

```bash
uv run pytest
```

## Estructura del Proyecto

- `src/`: Contiene la lógica principal (loaders, parsers, preprocessors).
- `data/`: Directorio destinado a los archivos de datos (csv, etc.).
- `test/`: Pruebas automatizadas para asegurar la calidad del código.
- `notebooks/`: Espacio para experimentación y análisis exploratorio.
- `main.py`: Script principal de ejecución.
