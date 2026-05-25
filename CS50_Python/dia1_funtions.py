# Sistema de Inventario - Día 1: Funciones básicas

def registrar_producto(nombre, precio, cantidad):
    """Registra un producto y muestra su información"""
    print(f"=== PRODUCTO REGISTRADO ===")
    print(f"Nombre: {nombre}")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad} unidades")
    print(f"Valor total: ${precio * cantidad}")
    print("=" * 27)

def crear_remision(cliente, productos):
    """Crea una remisión para un cliente"""
    print(f"\n📋 REMISIÓN PARA: {cliente}")
    print("-" * 40)
    
    total = 0
    for producto in productos:
        subtotal = producto['precio'] * producto['cantidad']
        total += subtotal
        print(f"{producto['nombre']:20} ${subtotal:>8.2f}")
    
    print("-" * 40)
    print(f"{'TOTAL':20} ${total:>8.2f}\n")
    return total

# PRUEBAS
registrar_producto("Tornillos M6", 0.50, 100)
registrar_producto("Tuercas M6", 0.30, 150)
registrar_producto("Arandelas", 0.30, 150)
registrar_producto("Clavos", 0.10, 800)
registrar_producto("Grapas", 0.20, 250)

remision_001 = [
    {'nombre': 'Tornillos M6', 'precio': 0.50, 'cantidad': 100},
    {'nombre': 'Tuercas M6', 'precio': 0.30, 'cantidad': 150},
    {'nombre': 'Arandelas', 'precio': 0.30, 'cantidad': 200},
    {'nombre': 'Clavos', 'precio': 0.10, 'cantidad': 800},
    {'nombre': 'Grapas', 'precio': 0.20, 'cantidad': 250}


]

crear_remision("Ferretería El Tornillo", remision_001)