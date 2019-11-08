import unittest
from edad import Edad
from datetime import datetime, timedelta

class TestLog(unittest.TestCase):
    def test_1(self):
        hoy = datetime.now()
        fechaNacimiento = datetime(2000, 11, 8)
        edad = (hoy - fechaNacimiento) // timedelta(days=365.2425)
        self.assertEqual(edad, Edad().edad(fechaNacimiento))

if __name__ == '__main__':
    unittest.main()