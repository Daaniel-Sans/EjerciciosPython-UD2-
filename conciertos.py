
class Entrada:
    """Entrada general para un concierto. Es la clase padre de los demás tipos."""
    
    def __init__(self, concierto):
        # Concierto al que pertenece la entrada
        self.concierto = concierto

    def get_precio_total(self):
    # La entrada general cuesta el precio base del concierto    
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total():.2f}€'


class EntradaGrada(Entrada):
    """Entrada de grada: hereda de Entrada y añade el asiento."""
    def __init__(self, concierto, asiento):
        super().__init__(concierto) # El padre guarda el concierto
        self.asiento = asiento
    
    def get_precio_total(self):
        # La grada cuesta el precio base
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total():.2f}€'

    
class EntradaPista(Entrada):
    """Entrada de pista: hereda de Entrada y añade si es de pie."""
    def __init__(self, concierto, de_pie):
        super(). __init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        # La pista cuesta el precio base más un 10%
        return self.concierto.precio_base * 1.10

    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total():.2f}€'


class EntradaVIP(Entrada):
    """Entrada VIP: hereda de Entrada y añade si incluye consumición."""
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion    

  
    def get_precio_total(self):
        # Con consumición: precio base + 20%. Sin consumición: precio base + 15%
        if self.incluye_consumicion:
            return self.concierto.precio_base * 1.20
        else:
            return self.concierto.precio_base * 1.15   
    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total():.2f}€'   


class Concierto:
    """Concierto con su artista, ciudad, precio, aforo y entradas vendidas."""
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, entradas_vendidas, activo):
            self.artista = artista
            self.ciudad = ciudad
            self.precio_base = precio_base
            self.aforo_maximo = aforo_maximo
            self.entradas_vendidas = entradas_vendidas # Lista de objetos Entrada
            self.activo = activo

    def calcular_recaudacion(self):
        # Suma el precio total de cada entrada vendida (cada tipo tiene su precio)
        if len(self.entradas_vendidas) == 0:
            return 0.0
        else:
            recaudacion = 0.0
            for entrada in self.entradas_vendidas:
                recaudacion += entrada.get_precio_total()
            return recaudacion  

    def calcular_precio_medio(self):
        # Recaudación total dividida entre el número de entradas vendidas
        if len(self.entradas_vendidas) == 0:
            return 0.0
        else:
            total_precio = 0.0
            for entrada in self.entradas_vendidas:
                total_precio += entrada.get_precio_total()
            return total_precio / len(self.entradas_vendidas)

    def entradas_disponibles(self):
        # True si todavía quedan entradas por vender según el aforo máximo
        return len(self.entradas_vendidas) < self.aforo_maximo          
    
    def __str__(self):
        return f'Concierto de {self.artista} en {self.ciudad}'


class Usuario:
    """Usuario que compra entradas y valora los conciertos a los que asiste."""
    def __init__(self, nombre, edad, entradas_compradas, conciertos_asistidos, valoraciones):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = entradas_compradas # Lista de Entrada
        self.conciertos_asistidos = conciertos_asistidos # Set de Concierto
        self.valoraciones = valoraciones # Diccionario {Concierto: nota}

    def comprar_entrada(self, concierto, tipo_entrada):
        # 1. Comprobaciones previas: si alguna falla, se lanza un error y se detiene
        if not concierto.activo:
            raise Exception(f'El concierto de {concierto.artista} en {concierto.ciudad} no está activo, asi que no hay entradas. Prueba en otro momento, busca otro concierto o aprovecha para repasar Python... pero que no hay entradas, vaya.')
        elif concierto in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} ya ha asistido al concierto de {concierto.artista} en {concierto.ciudad}, por lo que ya no puede comprar más entradas para ese mismo concierto a su nombre. Que se cambie el nombre o algo')
        elif not concierto.entradas_disponibles():
            raise Exception(f'Vaya... Parece que no hay entradas disponibles para el concierto de {concierto.artista} en {concierto.ciudad}. Es verdad que después de esto se retira de su carrera y se comenta no sé qué de que iba a llegar Tom Cruise haciendo la cobra en un Eurofighter Typhoon, pero seguro que no es para tanto')
        else:
        # 2. Crear la entrada del tipo indicado
            if tipo_entrada == 'grada':
                entrada = EntradaGrada(concierto, '1A')
            elif tipo_entrada == 'pista':
                entrada = EntradaPista(concierto, True)
            elif tipo_entrada == 'vip':
                entrada = EntradaVIP(concierto, True)
            else:
                raise Exception(f'Tipo de entrada no válido: {tipo_entrada}. Debe ser "grada", "pista" o "vip".')
        # 3. Registrar la compra
            self.entradas_compradas.append(entrada)
            concierto.entradas_vendidas.append(entrada)
            self.conciertos_asistidos.add(concierto) # Es un set: se usa add, no append

    def valorar(self, concierto, valoracion):
        # 1. Solo se puede valorar un concierto al que se ha asistido
        if concierto not in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} no ha asistido al concierto de {concierto.artista} en {concierto.ciudad}, así que no puede valorarlo. Estaría bueno')
        # 2. La nota debe estar entre 0 y 10
        if valoracion < 0 or valoracion > 10:
            raise Exception(f'Valoración no válida: {valoracion}. Debe estar entre 0 y 10.')
        # 3. Añade la nota o, si ya existía, la modifica
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        return f'{self.nombre} ha asistido a {len(self.conciertos_asistidos)} conciertos'
    