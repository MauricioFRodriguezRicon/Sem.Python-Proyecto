import os
from PIL import Image, ImageDraw
import tempfile


class Usuario:
    def __init__(self, alias, nombre, edad, genero, esOtroGenero, queOtroGenero, foto, pos):
        self.alias = alias
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.esOtroGenero = esOtroGenero
        self.queOtroGenero = queOtroGenero
        self.foto = foto
        self.pos = pos

    @property
    def get_alias(self):
        return self.alias

    @property
    def set_alias(self, nuevo_alias):
        self.alias = nuevo_alias

    @property
    def get_nombre(self):
        return self.nombre

    @property
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def get_edad(self):
        return self.edad

    @property
    def set_edad(self, nuevo_edad):
        self.edad = nuevo_edad

    @property
    def get_genero(self):
        return self.genero

    @property
    def set_genero(self, nuevo_genero):
        self.genero = nuevo_genero

    @property
    def get_esOtroGenero(self):
        return self.esOtroGenero

    @property
    def set_esOtroGenero(self, esOtro):
        self.esOtroGenero = esOtro

    @property
    def get_queOtroGenero(self):
        return self.queOtroGenero

    @property
    def set_queOtroGenero(self, nuevo_genero):
        self.queOtroGenero = nuevo_genero

    @property
    def get_foto(self):
        return self.foto

    @property
    def set_foto(self, nuevo_foto):
        self.foto = nuevo_foto

    @property
    def get_pos(self):
        return self.pos

    def actualizar(self, alias, nombre, edad, genero, esOtroGenero, queOtroGenero, foto):
        self.alias = alias
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.esOtroGenero = esOtroGenero
        self.queOtroGenero = queOtroGenero
        self.foto = foto