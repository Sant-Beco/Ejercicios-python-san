"""🧪 Mini ejercicio - Sets
Instrucciones:

Crea dos sets:

Uno llamado set_a con los números {1, 2, 3, 4, 5}.

Otro llamado set_b con los números {4, 5, 6, 7, 8}.

Luego, imprime:

La unión de ambos sets.

La intersección de ambos sets.

La diferencia entre set_a y set_b.

La diferencia simétrica entre set_a y set_b."""

set_a = {1,2,3,4,5}

set_b ={4,5,6,7,8}

print(f"\nLa unión de ambos sets: {set_a.union(set_b)}")
print(f"La intersección de ambos sets: {set_a.intersection(set_b)}")
print(f"La diferencia entre set_a y set_b: {set_a.difference(set_b)}")
print(f"La diferencia simétrica entre set_a y set_b: {set_a.symmetric_difference(set_b)}\n")


