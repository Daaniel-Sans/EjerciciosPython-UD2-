from conciertos import Concierto, Usuario, EntradaPista, EntradaGrada, EntradaVIP

# Creación de los 3 conciertos
concierto1 = Concierto('The Weeknd', 'Madrid', 120.0, 100, [], True)
concierto2 = Concierto('Jorge Drexler', 'Madrid', 55.0, 100, [], True)
concierto3 = Concierto('Estopa', 'Sevilla', 40.0, 100, [], True)

# Creación de los 3 usuarios
usuario1 = Usuario('Terry', 20, [], set(), {})
usuario2 = Usuario('Branson', 21, [], set(), {})
usuario3 = Usuario('Manuel', 24, [], set(), {})

# Cada usuario compra entradas para 2 conciertos
usuario1.comprar_entrada(concierto1, 'pista')
usuario1.comprar_entrada(concierto2, 'vip')
usuario2.comprar_entrada(concierto3, 'vip')
usuario2.comprar_entrada(concierto1, 'grada')
usuario3.comprar_entrada(concierto2, 'pista')
usuario3.comprar_entrada(concierto1, 'pista')

# Cada usuario valora 1 concierto al que ha asistido
usuario1.valorar(concierto1, 8)
usuario2.valorar(concierto3, 9)
usuario3.valorar(concierto2, 10)

# Lista con los conciertos para poder recorrerlos con bucles
conciertos = [concierto1, concierto2, concierto3]

# i) Número de entradas vendidas en total
total_entradas = 0
for concierto in conciertos:
    total_entradas += len(concierto.entradas_vendidas)
print(f'Entradas vendidas en total: {total_entradas}')

# ii) Número de entradas vendidas de cada tipo
pistas = 0
gradas = 0
vips = 0
for concierto in conciertos:
    for entrada in concierto.entradas_vendidas:
        if isinstance(entrada, EntradaPista):
            pistas += 1
        elif isinstance(entrada, EntradaGrada):
            gradas += 1
        elif isinstance(entrada, EntradaVIP):
            vips += 1
print(f'Entradas de pista: {pistas}')
print(f'Entradas de grada: {gradas}')
print(f'Entradas VIP: {vips}')

# iii) Recaudación total
recaudacion_total = 0.0
for concierto in conciertos:
    recaudacion_total += concierto.calcular_recaudacion()
print(f'Recaudación total: {recaudacion_total:.2f}€')

# iv) Precio medio de todas las entradas
if total_entradas > 0:
    precio_medio = recaudacion_total / total_entradas
else:
    precio_medio = 0.0
print(f'Precio medio de las entradas: {precio_medio:.2f}€')

# v) Concierto con más entradas vendidas
concierto_mas = conciertos[0]
for concierto in conciertos:
    if len(concierto.entradas_vendidas) > len(concierto_mas.entradas_vendidas):
        concierto_mas = concierto
print(f'Concierto con más entradas vendidas: {concierto_mas} - entradas vendidas: {len(concierto_mas.entradas_vendidas)}')

# vi) Concierto con menos entradas vendidas
concierto_menos = conciertos[0]
for concierto in conciertos:
    if len(concierto.entradas_vendidas) < len(concierto_menos.entradas_vendidas):
        concierto_menos = concierto
print(f'Concierto con menos entradas vendidas: {concierto_menos} - entradas vendidas: {len(concierto_menos.entradas_vendidas)}')