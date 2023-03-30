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
        self.driver.find_element(By.ID, "username").send_keys("student1")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def test1(self):
        
        self.driver.get("http://127.0.0.1:8000/")
        
        # navigation of all sections and subsections
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_247")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
test = tests()
test.setup_method()
test.test1()
test.quit()