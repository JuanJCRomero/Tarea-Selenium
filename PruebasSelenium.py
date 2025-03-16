import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Automatizacion Selenium")

# Configurar opciones de Chrome (también puedes hacer esto para Firefox)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Inicializar el navegador (Chrome)
driver = webdriver.Chrome(options=chrome_options)

# -------------------------------------
# 1. Abrir una página y cerrar el navegador
logger.info("Abriendo Google...")
driver.get("https://www.google.com")
time.sleep(2)

# -------------------------------------
# 2. Buscar un elemento y realizar acciones básicas
logger.info("Buscando en Google...")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# -------------------------------------
# 3. Identificación de elementos de distintas formas (navegaremos a saucedemo)
logger.info("Navegando a SauceDemo para login...")
driver.get("https://www.saucedemo.com/")

# Por ID
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Por Name
driver.find_element(By.NAME, "password").send_keys("secret_sauce")

# Por XPath
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# -------------------------------------
# 4. Manejo de Esperas (Explícitas e Implícitas)
driver.implicitly_wait(10)  # Espera implícita

# Espera explícita: Espera que cargue un elemento después de iniciar sesión
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)
logger.info("Productos cargados en la tienda.")

# -------------------------------------
# 5. Interacción con elementos dinámicos (haciendo clic en el carrito)
cart_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
)
cart_icon.click()
logger.info("Carrito de compras abierto.")

time.sleep(2)

# -------------------------------------
# 6. Manejo de cookies
logger.info("Mostrando cookies actuales...")
cookies = driver.get_cookies()
print("Cookies actuales:", cookies)

logger.info("Agregando nueva cookie...")
driver.add_cookie({"name": "mi_cookie", "value": "valor_123"})

# Confirmamos que se añadió
cookies = driver.get_cookies()
print("Cookies actualizadas:", cookies)

# -------------------------------------
# 7. Ejecución de JavaScript
logger.info("Ejecutando JavaScript en la página...")
driver.execute_script("alert('¡Hola desde Selenium!')")
time.sleep(2)

# Aceptar alerta
driver.switch_to.alert.accept()

# -------------------------------------
# 8. Manejo de ventanas emergentes
logger.info("Abriendo ventana emergente de prueba...")
driver.get("https://demo.guru99.com/popup.php")

driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.find_element(By.NAME, "emailid").send_keys("prueba@example.com")
driver.find_element(By.NAME, "btnLogin").click()

time.sleep(2)
driver.close()

driver.switch_to.window(windows[0])

# -------------------------------------
# 9. Manejo de frames
logger.info("Probando navegación dentro de un frame...")
driver.get("https://demo.guru99.com/test/guru99home/")

# Espera y cambia al frame
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "a077aa5e")))
driver.find_element(By.TAG_NAME, "img").click()

driver.switch_to.default_content()
time.sleep(2)

# -------------------------------------
# 10. Ejemplo de Page Object Model (POM) básico
logger.info("Ejecutando un ejemplo POM...")

# --- Clase Page Object ---
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        logger.info("Usando el POM para hacer login.")
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

# Ejecutamos el POM
driver.get("https://www.saucedemo.com/")
login_page = LoginPage(driver)
login_page.login("standard_user", "secret_sauce")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)
logger.info("Login exitoso con POM.")

# -------------------------------------
# Cerrar navegador
logger.info("Finalizando prueba y cerrando navegador.")
driver.quit()

logger.info("Ejecución completa.")
