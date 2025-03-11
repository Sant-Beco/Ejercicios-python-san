import sqlite3
import requests
from datetime import datetime

with open("log_tarea.txt", "a") as log:
    log.write(f"Script ejecutado en: {datetime.now()}\n")


# Configuración de la base de datos SQLite
DB_FILE = "estacion_climatica.db"

# Configuración de ThingSpeak
READ_API_KEY = "****************"
CHANNEL_ID = "******"
LAST_DOWNLOAD_FILE = "ultima_descarga.txt"

def obtener_fecha_ultima_descarga():
    """Obtiene la última fecha de descarga desde un archivo de texto."""
    try:
        with open(LAST_DOWNLOAD_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        # Si no existe el archivo, se devuelve una fecha por defecto
        return "2024-01-01T00:00:00Z"

def guardar_fecha_ultima_descarga(fecha):
    """Guarda la fecha de la última descarga en un archivo de texto."""
    with open(LAST_DOWNLOAD_FILE, "w") as file:
        file.write(fecha)

def inicializar_base_de_datos():
    """Inicializa la base de datos SQLite y crea la tabla si no existe."""
    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos_climaticos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            humedad REAL,
            luz REAL,
            presion REAL,
            fecha DATETIME
        )
    ''')
    conexion.commit()
    conexion.close()

def descargar_y_guardar_datos():
    """Descarga datos de ThingSpeak y los guarda en la base de datos."""
    # Obtener la última fecha de descarga
    ultima_fecha = obtener_fecha_ultima_descarga()
    
    # Construir la URL con el parámetro de fecha de inicio
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
    params = {
        "api_key": READ_API_KEY,
        "start": ultima_fecha
    }
    
    # Realizar la solicitud
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        datos = response.json()
        feeds = datos.get("feeds", [])
        
        
        if feeds:
            print(f"Se han descargado {len(feeds)} nuevos datos.")
            
            # Conectar a la base de datos SQLite
            conexion = sqlite3.connect(DB_FILE)
            cursor = conexion.cursor()
            
            for feed in feeds:
                try:
                    # Extraer los valores de los campos
                    temperatura = float(feed['field1']) if feed['field1'] else None
                    humedad = float(feed['field2']) if feed['field2'] else None
                    luz = float(feed['field3']) if feed['field3'] else None
                    presion = float(feed['field4']) if feed['field4'] else None
                    fecha = datetime.strptime(feed['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                    
                    # Insertar los datos en SQLite
                    cursor.execute('''
                        INSERT INTO datos_climaticos (temperatura, humedad, luz, presion, fecha)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (temperatura, humedad, luz, presion, fecha))
                except Exception as e:
                    print(f"Error procesando feed: {feed}, Error: {e}")
            
            # Confirmar los cambios y guardar la última fecha
            conexion.commit()
            conexion.close()
            
            ultima_fecha_descargada = feeds[-1]["created_at"]
            guardar_fecha_ultima_descarga(ultima_fecha_descargada)
        else:
            print("No hay datos nuevos para descargar.")
    else:
        print(f"Error en la solicitud: {response.status_code}, Detalles: {response.text}")

# Inicializar base de datos
inicializar_base_de_datos()

# Descargar y guardar datos
descargar_y_guardar_datos()