class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre=nombre
        self.correo=correo
        self.contraseña=contraseña
        
        
    def aLaColeccion(self):
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "contraseña": self.contraseña
        }