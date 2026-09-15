import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from src.utils.comida import Comida

DB_FILE = Path("comidas.json")


def _cargar_datos() -> List[Dict[str, Any]]:
    """Lee el archivo JSON y retorna la lista de comidas."""
    if not DB_FILE.exists():
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def _guardar_datos(datos: List[Dict[str, Any]]) -> None:
    """Escribe la lista de comidas en el archivo JSON."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def obtener_todas() -> List[Dict[str, Any]]:
    """Retorna todas las comidas registradas."""
    return _cargar_datos()


def obtener_por_id(comida_id: int) -> Optional[Dict[str, Any]]:
    """Busca y retorna una comida por su ID."""
    comidas = _cargar_datos()
    for comida in comidas:
        if comida["id"] == comida_id:
            return comida
    return None


def crear_comida(comida: Comida) -> Dict[str, Any]:
    """Crea una nueva comida calculando su ID de forma autoincremental."""
    comidas = _cargar_datos()
    
    if comida.id is None:
        nuevo_id = max([c["id"] for c in comidas], default=0) + 1
    else:
        nuevo_id = comida.id

    nueva_comida_dict = {
        "id": nuevo_id,
        "nombre": comida.nombre,
        "precio": comida.precio
    }
    
    comidas.append(nueva_comida_dict)
    _guardar_datos(comidas)
    return nueva_comida_dict


def eliminar_comida(comida_id: int) -> bool:
    """Elimina una comida por su ID. Retorna True si la encontró y eliminó."""
    comidas = _cargar_datos()
    comidas_filtradas = [c for c in comidas if c["id"] != comida_id]
    
    if len(comidas_filtradas) == len(comidas):
        return False  # The ID was not found.
        
    _guardar_datos(comidas_filtradas)
    return True