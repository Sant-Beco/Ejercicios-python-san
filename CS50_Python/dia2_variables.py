# Sistema de Inventario - Día 2: Variables y tipos

# PRODUCTO (diccionario = objeto en Python)
producto_001 = {
    'codigo': 'TOR-M6-100',
    'nombre': 'Tornillo M6 x 100mm',
    'precio': 1.50,
    'stock': 500,
    'proveedor': 'Aceros del Norte',
    'activo': True
}

# CLIENTE
cliente_001 = {
    'id': 1,
    'nombre': 'Ferretería El Martillo',
    'rfc': 'FEM920515XY8',
    'credito_disponible': 50000.00,
    'tipo': 'mayorista'  # mayorista, minorista, distribuidor
}

# REMISIÓN
remision_001 = {
    'numero': 'REM-2024-001',
    'cliente': cliente_001['nombre'],
    'fecha': '2024-05-27',
    'productos': [
        {'codigo': 'TOR-M6-100', 'cantidad': 50, 'precio': 1.50},
        {'codigo': 'TUE-M6', 'cantidad': 50, 'precio': 0.30}
    ],
    'subtotal': 0.0,
    'iva': 0.0,
    'total': 0.0,
    'pagada': False
}

def calcular_totales(remision):
    """Calcula subtotal, IVA y total de una remisión"""
    subtotal = 0
    for item in remision['productos']:
        subtotal += item['precio'] * item['cantidad']
    
    iva = subtotal * 0.16
    total = subtotal + iva
    
    remision['subtotal'] = subtotal
    remision['iva'] = iva
    remision['total'] = total
    
    return remision

def imprimir_remision(remision):
    """Imprime una remisión formateada"""
    print(f"\n{'='*50}")
    print(f"REMISIÓN: {remision['numero']}")
    print(f"Cliente: {remision['cliente']}")
    print(f"Fecha: {remision['fecha']}")
    print(f"{'-'*50}")
    
    for item in remision['productos']:
        print(f"{item['codigo']:15} x{item['cantidad']:3}  ${item['precio']:6.2f}  "
              f"${item['precio'] * item['cantidad']:8.2f}")
    
    print(f"{'-'*50}")
    print(f"{'Subtotal:':>40} ${remision['subtotal']:8.2f}")
    print(f"{'IVA (16%):':>40} ${remision['iva']:8.2f}")
    print(f"{'TOTAL:':>40} ${remision['total']:8.2f}")
    print(f"{'='*50}\n")

# PRUEBAS
remision_001 = calcular_totales(remision_001)
imprimir_remision(remision_001)

# Verificar tipo de datos
print(f"Tipo de 'precio': {type(producto_001['precio'])}")
print(f"Tipo de 'stock': {type(producto_001['stock'])}")
print(f"Tipo de 'activo': {type(producto_001['activo'])}")
print(f"Tipo de 'nombre': {type(producto_001['nombre'])}")