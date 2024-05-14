import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import conftest



@pytest.mark.usefixtures("driver_init")
class TestSauce:
    #En az 1 testiniz parametrize fonksiyonu ile en az 3 farklı veriyle test edilmelidir.
    @pytest.mark.parametrize("username, password, message", [
        ("", "", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
    ])
    def test_login(self, username, password, message):
        self.login(username, password)
        errorMessage = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error")))
        assert errorMessage.text == message, f"Expected message was not displayed for {username}"

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_input.clear()
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_input.clear()
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()

    # Başarılı giriş testi
    def test_success_login(self):
        self.login("standard_user", "secret_sauce")
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
        productList = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productList) == 6, "Product count after successful login is not correct"
       
       #Kullandığımız SauceDemo sitesinde kendi belirlediğiniz en az "3" test case daha yazını
       
       
     # 1)Ürün sıralaması testi
    def test_product_sorting(self):
       self.login("standard_user", "secret_sauce")
       sort_dropdown = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
       sort_dropdown.click()
       sort_option_low_to_high = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//option[@value='lohi']")))
       sort_option_low_to_high.click()
       first_product_price_sorted = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price")))
       assert first_product_price_sorted.text == "$7.99", "Ürünler düşükten yükseğe doğru sıralanmadı"     
        
    
     # 2)Sepete ilk ürünü ekleme testi
    def test_add_first_product_to_cart(self):
        self.login("standard_user", "secret_sauce")
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        cart_badge = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert cart_badge.text == "1", "Cart badge does not show 1 product"

   
     # 3)solda yer alan menü bar kontrolü 
    def test_menubar(self):
        self.login("standard_user", "secret_sauce")
        menuButton = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    



