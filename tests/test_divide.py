# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import divide

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def divide(self):
        assert divide(4,1) == 4
        assert divide(-1,-2) == 0.5
        assert divide(10,5) == 2
        assert divide(15,3) == 5
