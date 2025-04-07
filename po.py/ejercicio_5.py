class Libro:
    def __init__(self,libro,autor,año_publicacion):
        self.__titulo_libro=libro
        self.__autor_libro=autor
        self.__año_publicacion_libro=año_publicacion
        
    def descripcion(self):
        print(f"El libro {self.__titulo_libro} fue escrito por {self.__autor_libro} en el año {self.__año_publicacion_libro}")
    
    def get_titulo(self):
        return self.__titulo_libro
    
    def get_autor(self):
        return self.__autor_libro
    
    def set_titulo(self,nuevo_titulo):
        self.__titulo_libro=nuevo_titulo

    def set_autor(self,nuevo_autor):
        self.__autor_libro=nuevo_autor
        
    def get_año(self):
        return self.__año_publicacion_libro

    def set_año(self,nuevo_año):
        self.__año_publicacion_libro=nuevo_año
  
libro_1=Libro("Harry Potter",1998,"J K Rowling")
libro_1.descripcion()