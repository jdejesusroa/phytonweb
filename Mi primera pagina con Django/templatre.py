from modelo import obtener_libros
from template import renderizar_template

def renderizar_template(libros):
#simular la renderizacion de un template de libros
html ="<h1>Lista de libros</h1>"
for libro in libros:
  html +=f"<p>ID:{libro['id']},Titulo:{libro['titulo']},Autor:{libro['Autor']}</p>"
  return html

#integrar la vista y el template

def mostrar_libros_con_template():
  libros=obtener_libros()
  html=renderizar_template(libros)
  print(html)

mostrar_libros_con_template()