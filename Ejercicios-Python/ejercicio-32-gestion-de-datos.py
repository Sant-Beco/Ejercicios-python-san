import pandas as pd

datos = []  # Lista vacía para almacenar datos

def ingresar_datos():
    nombre = input("Ingrese el nombre: ").strip()
    identificacion = input("Ingrese el número de identificación: ").strip()
    celular = input("Ingrese el número celular: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()

    if not (nombre and identificacion and celular and correo):
        print("Error: Todos los campos son obligatorios.")
        return
    
    # Validar duplicados
    if any(d["Identificación"] == identificacion for d in datos):
        print("Error: Ya existe un usuario con esa identificación.")
        return

    datos.append({"Nombre": nombre, "Identificación": identificacion, "Celular": celular, "Correo": correo})
    print("✅ Datos ingresados correctamente.")

def eliminar_datos():
    global datos  # Declarar primero 'datos' como global
    
    if not datos:
        print("⚠️ No hay datos registrados.")
        return

    ver_datos()
    identificacion = input("Ingrese el número de identificación del usuario a eliminar: ").strip()

    nuevo_datos = [d for d in datos if d["Identificación"] != identificacion]

    if len(datos) == len(nuevo_datos):
        print("⚠️ No se encontró un usuario con ese número de identificación.")
    else:
        datos[:] = nuevo_datos  # Modificar la lista en su lugar
        print("✅ Datos eliminados correctamente.")

def ver_datos():
    if datos:
        try:
            df = pd.DataFrame(datos)
            print(df.to_string(index=False))  # Mostrar sin índices
        except ImportError:
            # Si pandas no está disponible, mostrar con print
            for d in datos:
                print(f"Nombre: {d['Nombre']}, Identificación: {d['Identificación']}, Celular: {d['Celular']}, Correo: {d['Correo']}")
    else:
        print("⚠️ No hay datos ingresados.")

def guardar_datos_excel():
    if datos:
        df = pd.DataFrame(datos)
        try:
            with pd.ExcelWriter("datos.xlsx", engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
            print("✅ Datos guardados en 'datos.xlsx'.")
        except Exception as e:
            print(f"❌ Error al guardar en Excel: {e}")
    else:
        print("⚠️ No hay datos para guardar.")

def cargar_datos():
    global datos
    try:
        df = pd.read_excel("datos.xlsx")
        datos.clear()  # Evitar duplicados
        datos.extend(df.to_dict(orient="records"))
        print("✅ Datos cargados correctamente.")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'datos.xlsx'. Comenzando con datos vacíos.")
    except Exception as e:
        print(f"❌ Error al cargar los datos: {e}")

# Cargar datos al inicio si existen
cargar_datos()

while True:
    print("\n----- MENU -----")
    print("1. Agregar datos")
    print("2. Eliminar datos")
    print("3. Ver datos")
    print("4. Guardar datos en Excel")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        ingresar_datos()
    elif opcion == "2":
        eliminar_datos()
    elif opcion == "3":
        ver_datos()
    elif opcion == "4":
        guardar_datos_excel()
    elif opcion == "5":
        print("👋 Saliendo del programa...")
        break
    else:
        print("⚠️ Opción no válida. Intente nuevamente.")


