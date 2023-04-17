class Ciudadano:
    def __init__(self, nombre: str, rango: str):
        self.__nombre = nombre 
        self.__rango = rango

#----------------------Getters------------------------------------
    def getNombre(self):
        return self.__nombre

    def getRango(self):
        return self.__rango

#----------------------Setters------------------------------------
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setRango(self, rango: str):
        self.__rango = rango

    def Universidad(self):
        return("Se graduó de la Universidad")

#-----------------------Clase Musico--------------------------------
class CiudadanoMusico(Ciudadano):
    def __init__(self, nombre: str, rango: str, tiempo_profesion: int, instrumento: str, lugar_trabajo: str):
        super().__init__(nombre, rango)
        self.__tiempo_profesion = tiempo_profesion
        self.__instrumento = instrumento
        self.__lugar_trabajo = lugar_trabajo

    #----------------------Getters Musico------------------------------------
    def getTiempo_profesion(self):
        return self.__tiempo_profesion
    
    def getInstrumento(self):
        return self.__instrumento

    def getLugar_trabajo(self):
        return self.__lugar_trabajo

    #----------------------Setters Musico------------------------------------
    def setTiempo_profesion(self, tiempo_profesion):
        self.__tiempo_profesion = tiempo_profesion

    def setInstrumento(self, instrumento):
        self.__instrumento = instrumento

    def setLugar_trabajo(self, lugar_trabajo):
        self.__lugar_trabajo = lugar_trabajo

    def Universidad(self):
        return("Se graduó de la Universidad Nacional")
    
#-----------------------Clase Actor--------------------------------
class CiudadanoActor(Ciudadano):
    def __init__(self, nombre: str, rango: str, tiempo_profesion: int, numero_peliculas: int, Oscars_ganados: int):
        super().__init__(nombre, rango)
        self.__tiempo_profesion = tiempo_profesion
        self.__numero_peliculas = numero_peliculas
        self.__oscars_ganados = Oscars_ganados

#----------------------Getters Actor------------------------------------
    def getTiempo_profesion(self):
        return self.__tiempo_profesion
    
    def getNumero_peliculas(self):
        return self.__numero_peliculas
    
    def getOscars_ganados(self):
        return self.__oscars_ganados

#----------------------Setters Actor------------------------------------
    def setTiempo_profesion(self, tiempo_profesion):
        self.__tiempo_profesion = tiempo_profesion

    def setNumero_peliculas(self, numero_peliculas):
        self.__numero_peliculas = numero_peliculas

    def setOscars_ganados(self, oscars_ganados):
        self.__oscars_ganados = oscars_ganados
    
    def Universidad(self):
        return("Se graduó de la Universidad San Buenaventura")

#-----------------------Clase Abogado--------------------------------
class CiudadanoAbogado(Ciudadano):
    def __init__(self, nombre: str, rango: str, tiempo_profesion: int, casos_ganados: int, bufete: str):
        super().__init__(nombre, rango)
        self.__tiempo_profesion = tiempo_profesion
        self.__casos_ganados = casos_ganados
        self.__bufete = bufete

#----------------------Getters Abogado------------------------------------
    def getTiempo_profesion(self):
        return self.__tiempo_profesion
    
    def getCasos_ganados(self):
        return self.__casos_ganados
    
    def getBufete(self):
        return self.__bufete

#----------------------Setters Abogado------------------------------------
    def setTiempo_profesion(self, tiempo_profesion):
        self.__tiempo_profesion = tiempo_profesion

    def setCasos_ganados(self, casos_ganados):
        self.__casos_ganados = casos_ganados

    def setBufete(self, bufete):
        self.__bufete = bufete

    def Universidad(self):
        return("Se graduó de la Universidad El rosario")

#------------------------Main---------------------------------
def main():
    Musico = CiudadanoMusico('Diego Castro', 'Director', 30, 'Clarinete', 'Banda sinfónica de Ibagué')
    print(f'Músico:   {Musico.getNombre()}\n\
          Rango: {Musico.getRango()}\n\
          Tiempo de Profesión: {Musico.getTiempo_profesion()} años\n\
          Instrumento: {Musico.getInstrumento()}\n\
          Lugar de trabajo: {Musico.getLugar_trabajo()}\n\
          {Musico.Universidad()}\n\
          ')
    
    Actor = CiudadanoActor('Daniel Day-Lewis', 'Actor de Hollywood', 48, '50', '3')
    print(f'Actor:    {Actor.getNombre()}\n\
          Rango: {Actor.getRango()}\n\
          Tiempo de Profesión: {Actor.getTiempo_profesion()} años\n\
          Numero de pelicuas: {Actor.getNumero_peliculas()} peliculas\n\
          premios Oscar ganados: {Actor.getOscars_ganados()}\n\
          {Actor.Universidad()}\n\
          ')
    
    Abogado = CiudadanoAbogado('Isidro Castro', 'Penalista', 25, '12', 'Lex Legal Abogados & Asociados.')
    print(f'Abogado:  {Abogado.getNombre()}\n\
          Rango: {Abogado.getRango()}\n\
          Tiempo de Profesión: {Abogado.getTiempo_profesion()} años\n\
          Casos ganados: {Abogado.getCasos_ganados()} casos el ultimo mes\n\
          Bufete al que pertenece: {Abogado.getBufete()}\n\
          {Abogado.Universidad()}')


if __name__ == '__main__':
    main()
