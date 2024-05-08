# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplica

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_multiplica(self):
        assert multiplica(4,5) == 20
        assert multiplica(-1,-2) == 2
        assert multiplica(-7,5) == -35
        assert multiplica(-7,9) == -63
