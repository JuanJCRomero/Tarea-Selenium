
---

# 🚀 Automatización de Pruebas con Selenium en Python

## Descripción

Este proyecto demuestra cómo automatizar pruebas de una página web utilizando **Selenium WebDriver** en **Python**. El script cubre aspectos esenciales como la **interacción con elementos**, la **gestión de esperas**, la **automatización de pruebas en diferentes navegadores**, y **manejo de ventanas emergentes**. 

Este README proporciona una guía completa para ejecutar el código y realizar las configuraciones necesarias.

---

## 📋 Requisitos

Para ejecutar este script, necesitarás tener instalado lo siguiente:

- **Python 3.x**: [Descargar Python](https://www.python.org/downloads/)
- **Selenium WebDriver**: [Instalar Selenium](https://pypi.org/project/selenium/)

### Dependencias

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install selenium
```

### Drivers de Navegador

**1. ChromeDriver**  
Descarga el driver correspondiente para **Google Chrome**:
- [ChromeDriver - Download](https://chromedriver.chromium.org/downloads)

Coloca el `chromedriver` en la misma carpeta donde está el script.

**2. FirefoxDriver (opcional)**  
Si prefieres usar Firefox, puedes descargar **GeckoDriver**:
- [GeckoDriver - Download](https://github.com/mozilla/geckodriver/releases)

---

## 🔧 Instalación

1. **Clona este repositorio** (o simplemente guarda el archivo `prueba_selenium.py` en tu máquina).

2. **Configura tu entorno**:
   - Asegúrate de tener Python y Selenium instalados.
   - Descarga el **ChromeDriver** y colócalo en el mismo directorio que el archivo Python.

---

## 🖥️ Ejecución

Para ejecutar el script, abre tu terminal o línea de comandos, navega a la carpeta donde se encuentra el archivo `prueba_selenium.py` y ejecuta el siguiente comando:

```bash
python prueba_selenium.py
```

---

## 🔍 ¿Qué hace este código?

Este script cubre múltiples aspectos de la automatización de pruebas con Selenium en Python, incluyendo:

### 1. **Abrir y cerrar el navegador**  
Abre Google y realiza una búsqueda de "Selenium Python".

### 2. **Identificación de elementos**  
Encuentra elementos en la página web usando diferentes métodos:
- Por ID
- Por Name
- Por XPath

### 3. **Manejo de esperas**  
Demuestra el uso de esperas **implícitas** y **explícitas** para garantizar que los elementos estén disponibles antes de interactuar con ellos.

### 4. **Interacción con elementos dinámicos**  
Haz clic en el **carrito de compras** en una página web que carga productos dinámicamente.

### 5. **Manejo de cookies**  
Muestra cómo ver, agregar y actualizar cookies en el navegador.

### 6. **Ejecución de JavaScript**  
Ejecuta una alerta de JavaScript dentro del navegador.

### 7. **Manejo de ventanas emergentes**  
Simula la interacción con una ventana emergente de un enlace en la página **Guru99**.

### 8. **Manejo de frames**  
Accede a contenido dentro de un **frame** y realiza una acción dentro de él.

### 9. **Uso de Page Object Model (POM)**  
Implementa un ejemplo básico de **Page Object Model (POM)** para realizar el login en **SauceDemo**.

---

## 🧩 Estructura del Código

```plaintext
.
├── prueba_selenium.py           # Script principal de automatización
└── README.md                   # Documentación del proyecto
```

---

## 🎯 Objetivo de la Actividad

El objetivo de este código es proporcionar un ejemplo práctico y funcional de cómo usar Selenium para automatizar pruebas en una página web real. Se enfoca en interactuar con la interfaz, manejar situaciones dinámicas, y aplicar buenas prácticas como el uso de **esperas** y el patrón de diseño **Page Object Model** (POM).

---

## 🌐 Navegadores Soportados

Este script está configurado para usar **Google Chrome** por defecto, pero puedes cambiar el navegador a **Firefox** modificando el driver.

```python
# Usar Firefox
driver = webdriver.Firefox(options=firefox_options)
```

---

## 📝 Log de Ejecución

El código genera logs detallados en la consola utilizando el módulo `logging` para hacer un seguimiento de cada paso ejecutado:

```plaintext
INFO:Automatizacion Selenium: Abriendo Google...
INFO:Automatizacion Selenium: Buscando en Google...
INFO:Automatizacion Selenium: Navegando a SauceDemo para login...
INFO:Automatizacion Selenium: Login exitoso con POM.
```

---

## 🔧 ¿Qué más puedes hacer?

- **Personalizar el script** para automatizar pruebas de otras páginas web.
- **Expandir el patrón Page Object Model (POM)** para hacer más modular y mantenible el código de pruebas.
- **Ejecutar pruebas en múltiples navegadores** (Chrome, Firefox) para garantizar la compatibilidad cruzada.
- **Capturar errores** y generar informes con herramientas como **Allure** o **TestNG**.

---

¡Gracias por leer y mucho éxito en tus pruebas automatizadas con Selenium! 🧑‍💻🚀

