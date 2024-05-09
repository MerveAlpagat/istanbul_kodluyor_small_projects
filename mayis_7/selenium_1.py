from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        try:
          username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
          username_input.clear()
          username_input.send_keys(username)

          password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
          password_input.clear()
          password_input.send_keys(password)

          login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
          login_button.click()
        except:
         print("Login failed or timed out.")

     #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_blank_fields(self):
        self.login("", "")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")))
            errorMessage = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")
            testResult = errorMessage.text == "Epic sadface: Username is required"
            print(f"Empty Fields Test Result: {testResult}")
        except NoSuchElementException:
            print("Element not found.")
       #Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.  
    def test_blank_password(self): 
        self.login("standard_user", "")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"login_button_container\"]/div/form/div[3]")))
            errorMessage = self.driver.find_element(By.XPATH, "//*[@id=\"login_button_container\"]/div/form/div[3]")
            testResult = errorMessage.text == "Epic sadface: Password is required"
            print(f"Empty Password Test Result: {testResult}")
        except NoSuchElementException:
            print("Element not found.")
       #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_out_user(self):
        self.login("locked_out_user", "secret_sauce")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")))
            errorMessage = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")
            testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
            print(f"Locked Out User Test Result: {testResult}")
        except NoSuchElementException:
            print("Element not found.")
          #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_success_login(self):
        self.login("standard_user", "secret_sauce")
        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
            productList = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            testResult = len(productList) == 6
            print(f"Successful Login Test Result: {testResult}")
        except:
            print("Test failed or timed out.")
    

             
                #Bir tane de siz bulunuz.     ilk ürünü sepete ekle
    def add_first_product_to_cart(self):  
        self.login("standard_user", "secret_sauce")  # Önce giriş yap.
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']")))
         # İlk ürünü bul.
         # Sepete ekle butonunu bul.
        add_to_cart_button = self.driver.find_element(By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()  # Ürünü sepete ekle.
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))  # Sepet ikonunu kontrol et.
        # Sepet ikonunu bul.
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
         # Sepette 1 ürün olduğunu doğrula
        assert cart_badge.text == "1", "Sepette 1 ürün yok!"
        print("Doğrulama başarılı: Sepette 1 ürün var.")
   
    def quit_driver(self):
        self.driver.quit()

# Test sınıfını başlat
testClass = Test_Sauce()

# Testleri çağır
testClass.test_blank_fields()
testClass.test_blank_password() 
testClass.test_locked_out_user() 
testClass.test_success_login()
testClass.add_first_product_to_cart()
# Sürücüyü kapat
testClass.quit_driver()