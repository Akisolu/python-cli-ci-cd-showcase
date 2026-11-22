# Python CLI CI/CD Showcase

*🇺🇸 [Read this in English](README.md)*

**Qué hace:** Una pequeña aplicación de menús cuyo verdadero propósito es mostrar cómo se prueba el código automáticamente y se publica como programas listos para usar en Windows y Linux.  
**Por qué importa:** Sin comprobaciones automáticas, los cambios con errores pueden llegar a los usuarios sin que nadie los detecte.

> 📄 Versión en inglés: [README.md](README.md)

## Descripción general

Este repositorio muestra buenas prácticas de pruebas y automatización en un proyecto de Python. El objetivo no es la funcionalidad del menú de comidas, sino demostrar cómo se valida el código, se protege la calidad y se automatiza la entrega con GitHub Actions.

## Qué se demuestra

- Pruebas automáticas con `pytest`, en tres niveles: unitarias, de integración y de extremo a extremo.
- Validación de la lógica y del comportamiento de la aplicación.
- Ejecución automática de las pruebas en cada cambio mediante GitHub Actions.
- Generación de ejecutables con PyInstaller para Windows y Linux.
- Publicación automática de versiones en GitHub Releases.

El flujo central es: `código -> pruebas -> validación -> compilación -> publicación`.

## Descargar y ejecutar

Para probar la aplicación sin instalar Python:

1. Abrir la pestaña **Releases** en GitHub y descargar la última versión para tu sistema operativo.
2. **Windows:** ejecutar `restaurant_cli_windows.exe`.
3. **Linux:** dar permiso de ejecución con `chmod +x restaurant_cli_linux` y ejecutar `./restaurant_cli_linux`.

## Ejecutar las pruebas

```bash
python -m pytest tests/ -v
```

La suite actual cuenta con 64 pruebas que pasan correctamente (`64 passed`).

## Tecnologías

Python, Pytest, Pydantic, PyInstaller y GitHub Actions.
