from pathlib import Path
import sys

def resource_path(rel_path: str | Path) -> str:
    """
    Retourne un chemin utilisable vers une ressource embarquée.
    - En dev : relatif au dossier du fichier source.
    - En exe : dossier temporaire _MEIPASS créé par PyInstaller.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)  
    else:
        base = Path(__file__).resolve().parent  
    return str((base / rel_path).resolve())