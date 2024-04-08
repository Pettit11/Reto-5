# Reto-5
# Primer caso
Se crea un carpeta para el primer caso, en dicha carpeta se encuentra el paquete Shape que es inciado con el __init__.py para que el programa sepa que es un paquete, dentro de este mismo tmabién se encuentre un único módulo shape.py que contiene todo el ejercicio del repo anterior.
```Python
File_structure/
├── Shape/
│      ├── __init__.py
│      └── shape.py
└── main.py
```
# Segundo caso
En este segundo caso ahora se va a crear un módulo para cada una de las clases, inicialmente se crea un paquete Shape que contendrá por ais decirlo todo lo que se va a usar a la hora de construir los poligonos (point, line, shape), luego se crea un subpaquete Polygons que tiene módulos todas las figuras importando el paquete shape, sus módulos y/o módulos del mismo paquete para crear la figura.
```Python
Second way/
├── Shape/
│   ├── __init__.py
│   │── point.py
│   │── line.py
│   │── shape.py
│   └── Polygons
│   │   │   │── __init__.py
│   │   │   │── Equilateral.py
│   │   │   │── Isosceles.py
│   │   │   │── Rectangle.py
│   │   │   │── Scalene.py
│   │   │   │── Square.py
│   │   │   │── Triangle.py
│   │   │   └── TriREctangle.py
└── main.py
