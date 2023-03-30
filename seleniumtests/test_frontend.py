from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class tests:
    
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def quit(self):
        self.driver.quit()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "e1_226 button2").click()
        
    def login_student_1(self):
        
        
test = tests()
test.setup_method()
test.test()
test.quit()