# Cry-Chat
El proyecto es un sistema de chat seguro entre dos terminales (Alice y Bob) que implementa múltiples algoritmos criptográficos para proteger la comunicación. Utiliza sockets TCP para la conexión de red y ofrece una interfaz gráfica (Tkinter) para gestionar la comunicación y los parámetros criptográficos. El sistema permite seleccionar dinámicamente entre diferentes criptosistemas durante la sesión de chat mediante el chat.
Interfaz Gráfica (GUI) inicial:

Conectados desde sockets servidor - cliente: Alice - Bob

Menú de cifrados desplegable:

Estado inicial: SinCifrar
Criptosistemas utilizados:
Diffie-Hellman:
Mecanismo:
Intercambio de claves para generar un secreto compartido.
Usa el secreto como desplazamiento en un cifrado César.
Funciones:
encrypt_DiffieHellman(): Cifra con César usando la clave compartida.
decrypt_DiffieHellman(): Descifra con César.
Interfaz: Popup para ingresar claves privadas (a para Alice, b para Bob).

(1ro ingresamos b y apretamos ok, antes de aceptar las claves privadas de A)

RSA:
Mecanismo:
Cifrado carácter a carácter usando claves pública/privada.
Cada carácter se mapea a su índice en el alfabeto: c = m^e mod n.
Funciones:
encrypt_RSA(): Cifra con clave pública (n, e).
decrypt_RSA(): Descifra con clave privada (d).
Interfaz: Popup para ingresar primos p, q y exponente e.



(Al ingresar q nos da opciones para escoger el e de el generador)


ElGamal:
Mecanismo:
Cifra cada carácter como un par (a, b) = (g^k mod p, m * y^k mod p).
Descifra con clave privada x: m = b * (a^x)^{-1} mod p.
Funciones:
encrypt_ElGamal(): Genera pares a:b separados por |.
decrypt_ElGamal(): Reconstruye el mensaje original.
Interfaz: Popup para ingresar p (primo), g (generador), x (clave privada), y k (aleatorio).


Rabin:
Mecanismo:
Cifrado: c = m^2 mod n (donde n = p * q).
Descifrado: Calcula raíces cuadradas módulo p y q (ambos ≡ 3 mod 4) usando CRT.
Funciones:
encrypt_Rabin(): Cifra con clave pública n.
decrypt_Rabin(): Descifra con claves privadas p, q.
Interfaz: Popup para ingresar primos p y q (≡ 3 mod 4).

Uso:
Ingresar dentro de la carpeta, puedes agregar .pyw a los archivos server.py y client.py para no tener que abrir desde las terminales
Si quiere observar el funcionamiento, abrir desde las terminales.
Tiene función continue por lo que esta en bucle, tiene funciones dinamicas en RSA y ElGamal.
Detalles Técnicos Clave
Seguridad:
Diffie-Hellman usa primos predefinidos (p=31).
RSA/ElGamal/Rabin permiten definir primos grandes.
Manejo de Errores:
Verifica primalidad, congruencias (ej: Rabin requiere p,q ≡ 3 mod 4).
Valida coprimalidad en ElGamal (k debe ser coprimo con p-1).
Extensibilidad:
CIPHER_LIST permite añadir nuevos algoritmos fácilmente.
Requerimientos:
Python 3.12.5
Dos terminales (split si se puede)
## Documentación

📄 Informe técnico completo:  
[Ver documento en Google Docs](https://docs.google.com/document/d/1ZdDV_SV9cpiZvX4Qz931eIw7deRRhLaTxfE88dNqkso)
