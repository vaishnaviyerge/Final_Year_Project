import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



STATICFILES_DIRS = [BASE_DIR / 'static']

STATICFILES_DIRS = [BASE_DIR / 'dashboard' / 'static']  # or 'dashboard/static' depending on structure
