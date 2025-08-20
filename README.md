# Conversor de Sistemas Numéricos con Interfaz Gráfica

## 📌 Descripción breve del proyecto
Este proyecto consiste en un **conversor de sistemas numéricos** desarrollado en **Python** con **Tkinter** para la interfaz gráfica.  
Permite convertir números entre los sistemas **decimal, binario, octal y hexadecimal** de manera rápida, precisa e intuitiva.  
Está diseñado con fines **educativos y prácticos**, facilitando la comprensión de las bases numéricas y su aplicación en computación y electrónica digital.

---

## 🎯 Objetivos principales de la aplicación
- Implementar un conversor que soporte conversiones bidireccionales entre los sistemas decimal, binario, octal y hexadecimal.
- Diseñar una interfaz gráfica amigable, intuitiva y validada para el usuario.
- Incluir mecanismos de verificación de errores y manejo de límites en la entrada de datos.
- Servir como herramienta didáctica para estudiantes y profesionales de computación y electrónica.

---

## 🛠️ Tecnologías utilizadas
- **Lenguaje:** Python 3.x  
- **Biblioteca gráfica:** Tkinter  
- **IDE recomendado:** IDLE, Visual Studio Code o cualquier editor compatible con Python.  

---

## 🚀 Instrucciones de instalación

# 📘 Instructivo de Transformaciones de Sistemas Numéricos

Este instructivo explica cómo transformar números entre **Decimal, Binario, Octal y Hexadecimal**.

---

## 1️⃣ Transformación de **Decimal** a otros sistemas

| Conversión | Procedimiento | Ejemplo |
|------------|---------------|---------|
| **Decimal → Binario** | Dividir el número entre 2, anotar el residuo, repetir hasta que el cociente sea 0. El resultado es la secuencia de residuos en orden inverso. | 25 ÷ 2 → residuos: 1,0,0,1,1 → **11001** |
| **Decimal → Octal** | Dividir el número entre 8, anotar el residuo, repetir hasta que el cociente sea 0. Leer residuos al revés. | 100 ÷ 8 → residuos: 4,4 → **144** |
| **Decimal → Hexadecimal** | Dividir el número entre 16, anotar el residuo (usar letras A-F si es >9), repetir hasta que el cociente sea 0. Leer residuos al revés. | 255 ÷ 16 → residuos: F, F → **FF** |

---

## 2️⃣ Transformación de **Octal** a otros sistemas

| Conversión | Procedimiento | Ejemplo |
|------------|---------------|---------|
| **Octal → Decimal** | Multiplicar cada dígito por 8 elevado a su posición (de derecha a izquierda, empezando en 0) y sumar. | (157)₈ = 1×8² + 5×8¹ + 7×8⁰ = **111** |
| **Octal → Binario** | Sustituir cada dígito octal por su equivalente binario de 3 bits. | (157)₈ → 1=001, 5=101, 7=111 → **001101111** |
| **Octal → Hexadecimal** | Pasar primero a binario (3 bits) y luego agrupar en 4 bits para hexadecimal. | (157)₈ = 001 101 111 → agrupar → 0001 1011 11 = (6F)₁₆ |

---

## 3️⃣ Transformación de **Hexadecimal** a otros sistemas

| Conversión | Procedimiento | Ejemplo |
|------------|---------------|---------|
| **Hexadecimal → Decimal** | Multiplicar cada dígito por 16 elevado a su posición (derecha a izquierda desde 0). | (2F)₁₆ = 2×16¹ + 15×16⁰ = **47** |
| **Hexadecimal → Binario** | Reemplazar cada dígito hex por su equivalente binario de 4 bits. | (2F)₁₆ = 2 → 0010, F → 1111 → **00101111** |
| **Hexadecimal → Octal** | Convertir primero a binario (4 bits) y luego agrupar en 3 bits. | (2F)₁₆ = 0010 1111 → 010 1111 → (57)₈ |

---

## 4️⃣ Transformación de **Binario** a otros sistemas

| Conversión | Procedimiento | Ejemplo |
|------------|---------------|---------|
| **Binario → Decimal** | Multiplicar cada dígito por 2 elevado a su posición (derecha a izquierda desde 0). | (1101)₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = **13** |
| **Binario → Octal** | Agrupar los bits en grupos de 3 desde la derecha y convertir cada grupo a octal. | (110101)₂ → 110 101 → (65)₈ |
| **Binario → Hexadecimal** | Agrupar los bits en grupos de 4 desde la derecha y convertir cada grupo a hex. | (11010110)₂ → 1101 0110 → (D6)₁₆ |

---

## 📌 Resumen rápido de conversión directa

| Origen → Destino | Método rápido |
|------------------|---------------|
| Decimal → Otro   | Divisiones sucesivas |
| Octal ↔ Binario  | 1 dígito octal = 3 bits binarios |
| Hex ↔ Binario    | 1 dígito hex = 4 bits binarios |
| Octal ↔ Hex      | Pasar por binario como puente |

 <h2>Anexos</h2>
      <h2><strong> Capturas de pantalla de la aplicación</strong> </h2>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/j51fzJZv/ex1.png"width="400">
        <figcaption>Figura 1: Pantalla principal para el usuario</figcaption>
        </figure>
</div>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/SxQWbq26/ex2.png"width="400">
        <figcaption>Figura 2: Comprobación de errores</figcaption>
        </figure>
</div>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/X7srF5q5/ex4.png"width="400">
        <figcaption>Figura 3: Conversión con selección de número decimal</figcaption>
        </figure>
</div>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/yxWwb2hs/ex5.png"width="400">
        <figcaption>Figura 4: Conversión con selección de número octal</figcaption>
        </figure>
</div>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/kg7krVvT/ex6.png"width="400">
        <figcaption>Figura 5: Conversión con selección de número binario</figcaption>
        </figure>
</div>
<div class="contenedor-imagenes">
        <figure>
            <img src="https://i.postimg.cc/qM4mqP6R/ex7.png"width="400">
        <figcaption>Figura 6:  Conversión con selección de número hexadecimal </figcaption>
        </figure>
</div>

<img src="https://i.postimg.cc/W3KvT21h/ex8.png"width="400">
Figura 7: Código usado para el funcionamiento del sistema</figcaption>
 
    <h2><strong> Enlace de descarga del archivo .exe</strong><a href="  https://drive.google.com/file/d/14cl-T-YL_65qcvLhqEho9dmHGGXXuGQp/view?usp=drive_link
">Dar click aquí</a> </h2>
 
<h2><strong> Enlace de descarga del archivo del código para el sistema</strong><a href="https://drive.google.com/file/d/1Fc1htvwyc1VaNYQATO8Sc8QbtgUD_y3S/view?usp=sharing">Dar click aquí</a> </h2>
  
