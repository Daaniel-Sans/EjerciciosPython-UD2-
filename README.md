# Gestión de conciertos

Aplicación en Python para la gestión de conciertos, entradas y usuarios. Este proyecto resuelve un ejercicio de programación orientada a objetos (herencia, composición, colecciones y manejo de excepciones).

## Enunciado

Un cliente quiere desarrollar una aplicación para la gestión de conciertos, incluyendo la gestión de entradas y usuarios.

> **Consejo:** no utilices *type hints*.

### Módulo `conciertos`

Hacer un módulo `conciertos` con las siguientes clases:

#### `Entrada`

- **Atributos:**
  - `concierto` (de tipo `Concierto`)
- **Métodos:**
  - `get_precio_total()` que devuelva el precio base
  - `__str__()` que devuelva "Entrada general para `<artista>` - `<precio total>` €"

#### `EntradaGrada`

Hereda de `Entrada`.

- **Atributos:**
  - `asiento` (cadena de texto)
- **Métodos:**
  - `get_precio_total()` que devuelva el precio base
  - `__str__()` que devuelva "Entrada de grada para `<artista>` - `<precio total>` €"

#### `EntradaPista`

Hereda de `Entrada`.

- **Atributos:**
  - `de_pie` (booleano)
- **Métodos:**
  - `get_precio_total()` que devuelva el precio base más el 10%
  - `__str__()` que devuelva "Entrada de pista para `<artista>` - `<precio total>` €"

#### `EntradaVIP`

Hereda de `Entrada`.

- **Atributos:**
  - `incluye_consumicion` (booleano)
- **Métodos:**
  - `get_precio_total()` que devuelva el precio base más el 15% si no incluye consumición, o el 20% si la incluye
  - `__str__()` que devuelva "Entrada VIP para `<artista>` - `<precio total>` €"

#### `Concierto`

- **Atributos:**
  - `artista` (cadena de texto)
  - `ciudad` (cadena de texto)
  - `precio_base` (número decimal)
  - `aforo_maximo` (número entero)
  - `entradas_vendidas` (lista de tipo `Entrada`)
  - `activo` (booleano)
- **Métodos:**
  - `calcular_recaudacion()` que devuelva el dinero total recaudado según el número de entradas vendidas y el precio (teniendo en cuenta que las entradas de distinto tipo tienen distinto precio). Si no hay entradas vendidas, devolverá `0.0`
  - `calcular_precio_medio()` que devuelva el precio medio de las entradas vendidas (teniendo en cuenta que las entradas de distinto tipo tienen distinto precio). Si no hay entradas vendidas, devolverá `0.0`
  - `entradas_disponibles()` que devuelva `True` si aún hay entradas disponibles, según el aforo máximo y las entradas vendidas, y `False` en caso contrario
  - `__str__()` que devuelva "Concierto de `<artista>` en `<ciudad>`"

#### `Usuario`

- **Atributos:**
  - `nombre` (cadena de texto)
  - `edad` (número entero)
  - `entradas_compradas` (lista de `Entrada`)
  - `conciertos_asistidos` (`set` de `Concierto`)
  - `valoraciones` (diccionario de `Concierto` y número entero)
- **Métodos:**
  - `comprar_entrada(concierto, tipo_entrada)` que haga lo siguiente:
    1. Compruebe si el concierto está activo
       - Si no lo está, lanzar una `Exception` con un mensaje descriptivo y no continuar con los siguientes pasos
    2. Compruebe si el usuario ya ha asistido al concierto
       - Si ya ha asistido, lanzar una `Exception` con un mensaje descriptivo y no continuar con los siguientes pasos
    3. Compruebe si hay entradas disponibles en el concierto
       - Si no las hay, lanzar una `Exception` con un mensaje descriptivo y no continuar con los siguientes pasos
    4. Cree un objeto de tipo `Entrada`, con concierto, precio base y tipo:
       - El parámetro `tipo_entrada` será una cadena de texto. En función del tipo indicado, debe crear la entrada del tipo correspondiente
       - Si es una entrada de grada, el asiento debe ser `'1A'`
       - Si es una entrada de pista, `de_pie` debe ser `True`
       - Si es una entrada VIP, `incluye_consumicion` debe ser `True`
    5. Añada la entrada al atributo `entradas_vendidas` del concierto
    6. Añada la entrada al atributo `entradas_compradas` del usuario
    7. Añada el concierto al atributo `conciertos_asistidos` del usuario
  - `valorar(concierto, valoracion)` que haga lo siguiente:
    1. Compruebe si `concierto` está en la lista de conciertos asistidos
       - Si no lo está, lanzar una `Exception` con un mensaje descriptivo y no continuar con los siguientes pasos
    2. Compruebe que la valoración está entre 0 y 10
       - Si no lo está, lanzar una `Exception` con un mensaje descriptivo y no continuar con los siguientes pasos
    3. Añada (o modifique) la valoración a la lista de valoraciones
  - `__str__()` que devuelva "`<Nombre>` (ha asistido a `<número de conciertos asistidos>`)"

### Módulo `main`

En el módulo `main` hay que:

1. Crear 3 conciertos
2. Crear 3 usuarios
3. Hacer que cada usuario compre entradas para 2 conciertos
4. Hacer que cada usuario valore 1 concierto
5. Imprimir las siguientes estadísticas de los 3 conciertos, utilizando bucles para calcularlas:
   - Número de entradas vendidas en total (sumando los 3 conciertos)
   - Número de entradas vendidas de cada tipo en total (Pista, Grada y VIP, sumando los 3 conciertos)
   - Recaudación total (sumando los 3 conciertos)
   - Precio medio de todas las entradas (sumando los 3 conciertos)
   - Concierto con más entradas vendidas, y cuántas
   - Concierto con menos entradas vendidas, y cuántas

## Estructura del proyecto

```
.
├── conciertos.py   # Módulo con todas las clases
├── main.py         # Programa principal con datos de prueba y estadísticas
└── README.md
```

## Diseño

Relaciones entre las clases del módulo `conciertos`:

```
Entrada
├── EntradaGrada
├── EntradaPista
└── EntradaVIP

Concierto  ──(entradas_vendidas)──▶  Entrada
Usuario    ──(entradas_compradas)──▶ Entrada
Usuario    ──(conciertos_asistidos, valoraciones)──▶ Concierto
```

Precio total según el tipo de entrada:

| Tipo | Precio total |
|---|---|
| `Entrada` | Precio base |
| `EntradaGrada` | Precio base |
| `EntradaPista` | Precio base + 10 % |
| `EntradaVIP` | Precio base + 15 % (sin consumición) o + 20 % (con consumición) |

## Ejecución

Requiere Python 3. Desde la raíz del proyecto:

```bash
python main.py
```

## Conceptos practicados

- Clases, atributos y métodos
- Herencia y sobrescritura de métodos (`get_precio_total`, `__str__`)
- Polimorfismo (cálculo de precios según el tipo de entrada)
- Colecciones: listas, `set` y diccionarios
- Lanzamiento y gestión de excepciones
- Bucles para el cálculo de estadísticas
