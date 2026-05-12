import hashlib
import os
import sys
from hmac import compare_digest
from getpass import getpass


ITERACIONES = 100000
LONGITUD_SALT = 16


def generar_hash(password, salt=None):
    if salt is None:
        salt = os.urandom(LONGITUD_SALT)

    hash_obj = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERACIONES)
    return salt, hash_obj


def registrar_usuario(password):
    return generar_hash(password)


def verificar_password(password, salt, hash_guardado):
    _, hash_prueba = generar_hash(password, salt)
    return compare_digest(hash_prueba, hash_guardado)


def pedir_password(mensaje):
    if sys.stdin.isatty():
        return getpass(mensaje)

    return input(mensaje)


def main():
    print("=== Demo básica de hash con sal ===")
    print("Este programa simula un registro y una verificación de contraseña.\n")

    password_registro = pedir_password("Crea una contraseña: ")
    password_confirmada = pedir_password("Confirma la contraseña: ")

    if password_registro != password_confirmada:
        print("Las contraseñas no coinciden. Intenta de nuevo.")
        return

    salt, password_hasheada = registrar_usuario(password_registro)

    print("\nUsuario registrado correctamente.")
    print(f"Salt generado: {salt.hex()}")
    print(f"Hash almacenado: {password_hasheada.hex()}")

    intento_password = pedir_password("\nIntroduce tu contraseña para entrar: ")

    if verificar_password(intento_password, salt, password_hasheada):
        print("Acceso concedido. La contraseña es correcta.")
    else:
        print("Acceso denegado. La contraseña no coincide.")


if __name__ == "__main__":
    main()

    