# Git_Jafet

Proyecto básico de Python para demostrar cómo se protege una contraseña con hash y salt.

## Qué hace

El programa pide una contraseña, la confirma, genera un salt aleatorio y guarda el hash derivado con PBKDF2. Después simula un inicio de sesión y verifica si la contraseña ingresada coincide.

## Conceptos

- Hash: transforma la contraseña en una salida irreversible.
- Salt: dato aleatorio que cambia el resultado aunque dos contraseñas sean iguales.
- PBKDF2: algoritmo que repite el hash muchas veces para hacerlo más seguro contra fuerza bruta.

## Requisitos

- Python 3.8 o superior
- No necesita librerías externas

## Cómo ejecutar

```bash
python3 Codigo.py
```

## Nota

El programa solo guarda los datos en memoria mientras se ejecuta. No crea una base de datos ni archivos.

## Ejemplo

Si escribes la misma contraseña dos veces, el programa mostrará acceso concedido.
