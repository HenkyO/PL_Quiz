# file: test_app.py
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Jalankan browser tanpa tampilan GUI
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = "http://localhost:8000"  # Ubah sesuai alamat aplikasi uji

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def open_register_page(self):
        self.driver.get(f"{self.base_url}/register")
        time.sleep(1)

    def test_TC_REG_01(self):
        """Registrasi dengan Data Valid"""
        self.open_register_page()
        self.driver.find_element(By.ID, "nama").send_keys("user1")
        self.driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
        self.driver.find_element(By.ID, "username").send_keys("user1")
        self.driver.find_element(By.ID, "password").send_keys("user1")
        self.driver.find_element(By.ID, "re_password").send_keys("user1")
        self.driver.find_element(By.ID, "btnRegister").click()
        time.sleep(1)

    def test_TC_REG_02(self):
        """Registrasi dengan Field Kosong"""
        self.open_register_page()
        self.driver.find_element(By.ID, "btnRegister").click()
        time.sleep(1)

    def test_TC_REG_03(self):
        """Registrasi dengan Format Email Salah"""
        self.open_register_page()
        self.driver.find_element(By.ID, "nama").send_keys("user2")
        self.driver.find_element(By.ID, "email").send_keys("user2")  # Email tidak valid
        self.driver.find_element(By.ID, "username").send_keys("user2")
        self.driver.find_element(By.ID, "password").send_keys("user2")
        self.driver.find_element(By.ID, "re_password").send_keys("user2")
        self.driver.find_element(By.ID, "btnRegister").click()
        time.sleep(1)

    def test_TC_REG_04(self):
        """Registrasi dengan Password Tidak Cocok"""
        self.open_register_page()
        self.driver.find_element(By.ID, "nama").send_keys("user3")
        self.driver.find_element(By.ID, "email").send_keys("user3@gmail.com")
        self.driver.find_element(By.ID, "username").send_keys("user3")
        self.driver.find_element(By.ID, "password").send_keys("user3")
        self.driver.find_element(By.ID, "re_password").send_keys("user")  # Tidak sama dengan password
        self.driver.find_element(By.ID, "btnRegister").click()
        time.sleep(1)

    def test_TC_REG_05(self):
        """Registrasi dengan Data Duplikat"""
        self.open_register_page()
        self.driver.find_element(By.ID, "nama").send_keys("user1")
        self.driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
        self.driver.find_element(By.ID, "username").send_keys("user1")
        self.driver.find_element(By.ID, "password").send_keys("user1")
        self.driver.find_element(By.ID, "re_password").send_keys("user1")
        self.driver.find_element(By.ID, "btnRegister").click()
        time.sleep(1)

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = "http://localhost:8000"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def open_login_page(self):
        self.driver.get(f"{self.base_url}/login")
        time.sleep(1)

    def test_TC_LOGIN_01(self):
        """Login dengan Data Valid"""
        self.open_login_page()
        self.driver.find_element(By.ID, "username").send_keys("user1")
        self.driver.find_element(By.ID, "password").send_keys("user1")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

    def test_TC_LOGIN_02(self):
        """Login dengan Password Salah"""
        self.open_login_page()
        self.driver.find_element(By.ID, "username").send_keys("user1")
        self.driver.find_element(By.ID, "password").send_keys("user")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

    def test_TC_LOGIN_03(self):
        """Login dengan Field Kosong"""
        self.open_login_page()
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

    def test_TC_LOGIN_04(self):
        """Login dengan Username Tidak Terdaftar"""
        self.open_login_page()
        self.driver.find_element(By.ID, "username").send_keys("user")
        self.driver.find_element(By.ID, "password").send_keys("user")
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()
