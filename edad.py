from datetime import datetime, timedelta

class Edad():
    def edad(self, fechaNacimiento):
        return (datetime.now() - fechaNacimiento) // timedelta(days=365.2425)
