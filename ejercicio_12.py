"""
En este ejercicio, debes crear dos clases padres, a saber: la clase Video y la clase Audio. Luego, debes crear una subclase Media que herede de las clases Video y Audio.
"""

class Video:
    def __init__(self, titulo_vid, duracion_vid, categoria_vid):
        self.titulo = titulo_vid
        self.duracion = duracion_vid
        self.categoria = categoria_vid
        
    def mirar_video(self):
        return "Estas mirando el video: " + self.titulo
    
    def detener_video(self):
        return "Se detuvo el video: " + self.titulo
        
class Audio:
    def __init__(self, titulo_audio, nombre_artista):
        self.titulo = titulo_audio
        self.nombre_artista = nombre_artista
        
    def escuchar_audio(self):
        return "Estas escuchando el audio: " + self.titulo
    
    def detener_audio(self):
        return "Se detuvo el audio: " + self.titulo
        
class Media(Video, Audio):
    def __init__(self, titulo, duracion, categoria, nombre_artista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, nombre_artista)
        
    def mostrar_informacion(self):
        print("Titulo: ", self.titulo)
        print("Duracion: ", self.duracion)
        print("Categoria: ", self.categoria)
        print("Nombre del artista: ", self.nombre_artista)
        
 # Instanciar la clase Media       
media = Media("El señor de los anillos", 120, "Accion", "J.R.R Tolkien")
media.mirar_video()
media.mostrar_informacion()
        
        