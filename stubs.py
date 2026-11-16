import sys, types
from unittest.mock import MagicMock
for m in ['PySide6','PySide6.QtCore','PySide6.QtGui','PySide6.QtWidgets','fastapi','fastapi.responses','fastapi.middleware','fastapi.middleware.cors','uvicorn']:
    sys.modules.setdefault(m, MagicMock())
