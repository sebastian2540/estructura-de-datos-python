# estructura-de-datos-python

git remote set-url origin https://sebastian2540@github.com/sebastian2540/estructura-de-datos-python.git
git push -u origin main

git remote set-url origin https://sebastian2540@github.com/sebastian2540/taller-evaluativo-python.git

GIT - Sistema de Control de Versiones
 # Trabajo colaborativo
 # Sin conexión a internet
 # Ramas de trabajo

Creado por Linus Torvals en 2005

# Usos

# Comando terminal GitBash
pwd - muestra la ubicación de donde estoy ubicado en la terminal

ls - listar el contenido de la carpeta de donde estoy ubicado

cd - ingresar a una carpeta

cd .. - salir de la carpeta

mkdir - crear una carpeta, si tiene mas de una palabra se debe de colocar entre "nombre"

git init - inicializar el repositorio

touch - crear archivo

git config --global user.name "nombre dev"
git config --global user.email "correo electrónico"
git config --global core.editor "code --wait"
git config --list
git config --global credential.helper cache - eliminar almacenamiento de credenciales

git add . - agrega todos los archivos que tiene en el ambiente de trabajo
git add *.py - agrega todos los archivos que tengan las extensión de python o la extensión
git status - ver el estado del repositorio
git status -s - ver el estado del repositorio mas resumida
git commit -m "mensaje descriptivo"
git commit - se abre ventana de commit_editmsg
git log - historial de los cambios que han sido confirmados
git show - comparar los commit enviado para saber los cambios realizados
git commit -am "mensaje descriptivo" - realizar commit y push. Tener en cuenta que solo funciona cuando se agrega despuúes de una modificación
git log --stat - ver el historial de cada archivo mas espefico
git log --oneline - historial mas resumido, no muestra quien hizo el commit
mv "nombre del archivo actual" "nombre del archivo asignar"
git branch nombre rama - crear una rama
git branch - ver las ramas creadas
git checkout - cambiar de ramas
car "nombre del archivo" - visualizar el contenido del archivo
git merge "nombre rama" - unir los cambios de la rama