class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total()}€'

class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total()}€'

class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super(). __init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        return self.concierto.precio_base * 1.10

    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total()}€'

class EntradaVIP(Entrada):
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion    

    def get_precio_total(self):
        if self.incluye_consumicion:
            return self.concierto.precio_base * 1.20
        else:
            return self.concierto.precio_base * 1.15   
    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total()}€'   

class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, entradas_vendidas, activo):
            self.artista = artista
            self.ciudad = ciudad
            self.precio_base = precio_base
            self.aforo_maximo = aforo_maximo
            self.entradas_vendidas = entradas_vendidas
            self.activo = activo

    def calcular_recaudacion(self):
        if len(self.entradas_vendidas) == 0:
            return 0.0
        else:
            recaudacion = 0.0
            for entrada in self.entradas_vendidas:
                recaudacion += entrada.get_precio_total()
            return recaudacion  

    def calcular_precio_medio(self):
        if len(self.entradas_vendidas) == 0:
            return 0.0
        else:
            total_precio = 0.0
            for entrada in self.entradas_vendidas:
                total_precio += entrada.get_precio_total()
            return total_precio / len(self.entradas_vendidas)

    def entradas_disponibles(self):
        return len(self.entradas_vendidas) < self.aforo_maximo          
    
    def __str__(self):
        return f'Concierto de {self.artista} en {self.ciudad}'