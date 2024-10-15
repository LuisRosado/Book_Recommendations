# Book_Recommendations
# Sistema de Recomendación de Libros

Este proyecto es un sistema de recomendación de libros que utiliza Flask como framework web y scikit-learn para generar recomendaciones basadas en el contenido de los libros.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la lógica del servidor y las rutas de la aplicación.
- `recommendation.py`: Contiene la lógica para obtener recomendaciones de libros utilizando un modelo de similitud.
- `templates/`: Carpeta que contiene las plantillas HTML para la interfaz de usuario.
  - `index.html`: Página principal donde los usuarios pueden ingresar el título de un libro.
  - `recommendations.html`: Página que muestra las recomendaciones de libros.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener un archivo CSV de libros en la carpeta `data/` llamado `books.csv` con las columnas `title`, `authors`, y `average_rating`.

## Uso

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000/`.

3. Ingresa el título de un libro en la página principal y haz clic en "Obtener recomendaciones".

![index](https://github.com/user-attachments/assets/3c977102-d16a-4515-83a5-67ea1de157f6)

5. Serás redirigido a una página que mostrará las recomendaciones de libros.

![recommendation](https://github.com/user-attachments/assets/6a96676f-9b08-460e-b989-cd50663678a6)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
