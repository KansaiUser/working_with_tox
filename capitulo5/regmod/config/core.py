from pathlib import Path


import regmod

PACKAGE_ROOT = Path(regmod.__file__).resolve().parent

print(f"Package root from core {PACKAGE_ROOT}")