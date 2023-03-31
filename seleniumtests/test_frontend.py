from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class tests:
    
    
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def quit(self):
        self.driver.quit()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "e1_226").click()
        
    def login_student_1(self):
        self.driver.find_element(By.ID, "username").send_keys("s1")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def login_mess_manager(self):
        self.driver.find_element(By.ID, "username").send_keys("mm")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def login_canteen_manager(self):
        self.driver.find_element(By.ID, "username").send_keys("cm")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def login_hall_manager(self):
        self.driver.find_element(By.ID, "username").send_keys("hm")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def login_sports_secy(self):
        self.driver.find_element(By.ID, "username").send_keys("ss")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        
    def test1(self):
        # navigation of all sections and subsections of student side
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        
        # clicking on booking
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        
        # subsections of booking
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        
        # clicking on cleaning
        self.driver.find_elements(By.CLASS_NAME, "e1_238")[0].click()
        
        # subsections of cleaning
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        
        # clicking on my account
        self.driver.find_elements(By.CLASS_NAME, "e1_230")[0].click()
        
        # subsections of my account
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # clicking on home through title
        self.driver.find_elements(By.CLASS_NAME, "e1_261")[0].click()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        # clicking on home
        self.driver.find_elements(By.CLASS_NAME, "e1_250")[0].click()
        
        # logging out
        self.logout()
        
        
    def test2(self):
        # navigation of all sections and subsections of Mess Manager
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_31")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_32")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_33")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_34")[0].click()
        
        # clicking on home
        self.driver.find_elements(By.CLASS_NAME, "e1_250")[0].click()
        
        # logging out
        self.logout()
        
    def test3(self):
        # navigation of all sections and subsections of Canteen Manager
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_31")[0].click()
        
        # clicking on home
        self.driver.find_elements(By.CLASS_NAME, "e1_250")[0].click()
        
        # logging out
        self.logout()
        
    def test4(self):
        # navigation of all sections and subsections of Hall Manager
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_hall_manager()
        
        # clicking on hall
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of hall
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # clicking on home
        self.driver.find_elements(By.CLASS_NAME, "e1_250")[0].click()
        
        # logging out
        self.logout()
        
    def test5(self):
        # navigation of all sections and subsections of Sports secy
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_sports_secy()
        
        # clicking on sports
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of sports
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # clicking on home
        self.driver.find_elements(By.CLASS_NAME, "e1_250")[0].click()
        
        # logging out
        self.logout()
        
    # ################################################ MESS AND RELATED TESTS STARTED #########################################################
    def test6(self):
        # mess manager modify menu
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].click()
        self.driver.find_elements(By.NAME, "a4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b1")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Rajma Chawal")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].click()
        self.driver.find_elements(By.NAME, "a2")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[1].click()
        self.driver.find_elements(By.NAME, "b2")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[1].send_keys("Pav Bhaji")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].click()
        self.driver.find_elements(By.NAME, "a0")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[1].click()
        self.driver.find_elements(By.NAME, "b0")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "c")[1].send_keys("Sandwitch")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].click()
        self.driver.find_elements(By.NAME, "a1")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[2].click()
        self.driver.find_elements(By.NAME, "a2")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[2].click()
        self.driver.find_elements(By.NAME, "b2")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[2].send_keys("Pav Bhaji")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[2].click()
        self.driver.find_elements(By.NAME, "a3")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[2].click()
        self.driver.find_elements(By.NAME, "b0")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[2].send_keys("Idli Sambhar")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[2].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[2].click()
        self.driver.find_elements(By.NAME, "a3")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[2].click()
        self.driver.find_elements(By.NAME, "b0")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[2].send_keys("Idli Sambhar")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].click()
        self.driver.find_elements(By.NAME, "a1")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[1].click()
        self.driver.find_elements(By.NAME, "b2")[1].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "c")[1].send_keys("Masala Dosa")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click()       
       
        # logging out
        self.logout()
        
    def test7(self):
        # mess manager extra menu
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Pav Bhaji")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("150")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("50")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("30-03-002023T05:50")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("02-04-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("30-03-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # editting item
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("30-03-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click()  
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("30-03-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click()
        
        # logging out
        self.logout()
        
    def test8(self):
        # enter BDMR
        
        # mess manager extra menu
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_34")[0].click()
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-03-30")
        self.driver.implicitly_wait(1)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("63.89")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        # logging out
        self.logout()
        
    def test9(self):
        # add item in menu, rate and test in feedback
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].click()
        self.driver.find_elements(By.NAME, "a4")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b1")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Rajma Chawal")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # logging out
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_3")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "Thursday")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[0].text == "Lunch")
        assert(self.driver.find_elements(By.CLASS_NAME, "h")[0].text == "Rajma Chawal")
        assert(self.driver.find_elements(By.CLASS_NAME, "i")[0].text == "Be the first one to rate")
        
        self.driver.find_elements(By.CLASS_NAME, "c")[0].click()
        
        # logging out
        self.logout()
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_31")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Thursday")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Lunch")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Rajma Chawal")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "☆ 3.00")
        
        # logging out
        self.logout()
        
        
    def test10(self):
        # add item in menu, rate and test in feedback
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("30-03-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # logging out
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Masala Dosa")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "April 30, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Dinner")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "March 30, 2023, midnight")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "April 2, 2023, midnight")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[0].text == "34")
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("3")
        self.driver.find_elements(By.NAME, "submit")[0].click()        
        
        # logging out
        self.logout()
        
        
        # logging in as manager
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "April 30, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Dinner")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "Masala Dosa")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "3")
        
        # logging out
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Masala Dosa")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "3")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 30, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "Dinner")

        self.driver.find_elements(By.NAME, "order_validation")[0].click() 
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Dinner")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Masala Dosa")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "3")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "34")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "102")   
        
        # logging out
        self.logout()
        
        # logging in as manager
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(len(self.driver.find_elements(By.CLASS_NAME, "a")) == 0)
        
        # logging out
        self.logout()
        
    def test11(self):
        # start time must be less than end time
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("02-04-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("30-03-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "error")[0].text == "Start time must be less than end time.")
        
        # logging out
        self.logout()
        
    def test12(self):
        # start time must be less than end time
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("01-04-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # logging out
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("2")
        self.driver.find_elements(By.NAME, "submit")[0].click()     
        
        assert(self.driver.find_elements(By.CLASS_NAME, "error")[0].text == "Order cannot be booked now")
        # logging out
        self.logout()
        
    def test13(self):
        # student apply for rebate
        self.driver.get("https://upha.pythonanywhere.com/")
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        self.driver.find_elements(By.NAME, "from")[0].clear()
        self.driver.find_elements(By.NAME, "from")[0].send_keys("2023-03-31")
        self.driver.find_elements(By.NAME, "to")[0].clear()
        self.driver.find_elements(By.NAME, "to")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your rebate request has been sent to the mess manager. You will soon receive a confirmation email.")
        
        self.logout()
        
    def test14(self):
        # student apply for rebate
        self.driver.get("https://upha.pythonanywhere.com/")
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        self.driver.find_elements(By.NAME, "from")[0].clear()
        self.driver.find_elements(By.NAME, "from")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.NAME, "to")[0].clear()
        self.driver.find_elements(By.NAME, "to")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "error")[0].text == "From-Date must be less than equal to To-Date")
        self.logout()
        
    def test15(self):
        
        # student apply for rebate
        self.driver.get("https://upha.pythonanywhere.com/")
        
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        self.driver.find_elements(By.NAME, "from")[0].clear()
        self.driver.find_elements(By.NAME, "from")[0].send_keys("2023-03-31")
        self.driver.find_elements(By.NAME, "to")[0].clear()
        self.driver.find_elements(By.NAME, "to")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your rebate request has been sent to the mess manager. You will soon receive a confirmation email.")
        
        self.logout()
        
        # mess manager login
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_32")[0].click()
        
        self.driver.find_elements(By.NAME, "accept")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Rebate Request Accepted.")
        self.logout()
        
    def test16(self):
        # student apply for rebate
        self.driver.get("https://upha.pythonanywhere.com/")
        
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        self.driver.find_elements(By.NAME, "from")[0].clear()
        self.driver.find_elements(By.NAME, "from")[0].send_keys("2023-03-31")
        self.driver.find_elements(By.NAME, "to")[0].clear()
        self.driver.find_elements(By.NAME, "to")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your rebate request has been sent to the mess manager. You will soon receive a confirmation email.")
        
        self.logout()
        
        # mess manager login
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_32")[0].click()
        
        self.driver.find_elements(By.NAME, "reject")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Rebate Request Rejected.")
        self.logout()
        
    def test17(self):
        # add item in menu, rate and test in feedback
        
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("2023-04-30")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.NAME, "b2")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "d")[0].send_keys("250")
        self.driver.find_elements(By.CLASS_NAME, "e")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "e")[0].send_keys("34")
        self.driver.find_elements(By.CLASS_NAME, "f")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "f")[0].send_keys("30-03-002023T00:00")
        self.driver.find_elements(By.CLASS_NAME, "g")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "g")[0].send_keys("02-04-002023T00:00")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # logging out
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("3")
        self.driver.find_elements(By.NAME, "submit")[0].click()        
        
        # logging out
        self.logout()
        
        # enter BDMR
       
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_34")[0].click()
        
        # adding BDMRS
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-03-30")
        self.driver.implicitly_wait(2)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("63.89")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-03-31")
        self.driver.implicitly_wait(2)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("75.06")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-04-01")
        self.driver.implicitly_wait(2)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("82.47")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-04-02")
        self.driver.implicitly_wait(2)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("81.96")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        self.driver.find_elements(By.NAME, "BDMR_Date")[0].send_keys("2023-04-03")
        self.driver.implicitly_wait(2)
        self.driver.find_elements(By.NAME, "BDMR")[0].send_keys("71.35")
        self.driver.find_elements(By.NAME, "bdmr_submit")[0].click()
        
        self.logout()
        
        # student login
        self.login_student_1()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()
        
        self.driver.find_elements(By.NAME, "from")[0].clear()
        self.driver.find_elements(By.NAME, "from")[0].send_keys("2023-03-31")
        self.driver.find_elements(By.NAME, "to")[0].clear()
        self.driver.find_elements(By.NAME, "to")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your rebate request has been sent to the mess manager. You will soon receive a confirmation email.")
        
        self.logout()
        
        # mess manager login
        self.login_mess_manager()
        
        # clicking on mess
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_32")[0].click()
        
        self.driver.find_elements(By.NAME, "accept")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Rebate Request Accepted.")
        
        # subsections of mess
        self.driver.find_elements(By.CLASS_NAME, "e2_33")[0].click()
        
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[0].text == "171.48")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[3].text == "157.19")
        self.logout()
        
        # logging out
        self.logout()

        # student login
        self.login_student_1()
        
        # clicking on my account
        self.driver.find_elements(By.CLASS_NAME, "e1_230")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "171.48")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "157.19")
        
        # logging out
        self.logout()
        
    # ################################################ MESS AND RELATED TESTS COMPLETED #########################################################
       
       
    # ################################################ CLEANING AND RELATED STARTED ##############################################################
    
    def test18(self):
        self.driver.get("https://upha.pythonanywhere.com/")
        
        # student login
        self.login_student_1()

        # clicking on cleaning
        self.driver.find_elements(By.CLASS_NAME, "e1_238")[0].click()

        # making requests

        self.driver.find_elements(By.CLASS_NAME, "room_text")[1].send_keys("D-213")
        self.driver.find_elements(By.ID, "comment")[0].send_keys("Room check")
        self.driver.find_elements(By.CLASS_NAME, "submit_rec")[0].click()
        
        self.driver.find_elements(By.CLASS_NAME, "room_text")[1].send_keys("F-211")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].click()
        self.driver.find_elements(By.ID, "comment")[0].send_keys("Toilet check")
        self.driver.find_elements(By.CLASS_NAME, "submit_rec")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "room_text")[1].send_keys("D-343")
        self.driver.find_elements(By.CLASS_NAME, "c")[0].click()
        self.driver.find_elements(By.ID, "comment")[0].send_keys("Corridor check")
        self.driver.find_elements(By.CLASS_NAME, "submit_rec")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "room_text")[1].send_keys("F-413")
        self.driver.find_elements(By.CLASS_NAME, "d")[0].click()
        self.driver.find_elements(By.ID, "comment")[0].send_keys("Others check")
        self.driver.find_elements(By.CLASS_NAME, "submit_rec")[0].click()

        #logging out

        self.logout

        #logging in as hall manager

        self.login_hall_manager()
        
        # cleaning subsection
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking the data for hall manager

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "March 31, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "D-213")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "Room")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "Room check")
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "March 31, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "F-211")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Toilet")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Toilet check")
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[2].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[2].text == "March 31, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[2].text == "D-343")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[2].text == "Corridor")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[2].text == "Corridor check")
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[3].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[3].text == "March 31, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[3].text == "F-413")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[3].text == "Others")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[3].text == "Others check")

        # logging out hall manager

        self.logout()

        # logging in student_1

        self.login_student_1()

        # checking the data for student 1

        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Others")
        self.driver.find_elements(By.CLASS_NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Corridor")
        self.driver.find_elements(By.CLASS_NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Toilet")
        self.driver.find_elements(By.CLASS_NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Room")
        self.driver.find_elements(By.CLASS_NAME, "identity")[0].click()

        # Past requests of student 1 assessment

        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Others")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "Corridor")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[2].text == "Toilet")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[3].text == "Room")
       
    # ################################################ CLEANING AND RELATED ENDS ################################################################
    
    
    
    # ################################################ CANTEEN AND RELATED STARTED ############################################################## 
    def test19(self):
        # modify menu ----- owner
        # mess manager modify menu
        self.driver.get("https://upha.pythonanywhere.com/")
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("Veg. Maggi")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].send_keys("30")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("Pav Bhaji")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].send_keys("30")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].send_keys("Sandwitch")
        self.driver.find_elements(By.CLASS_NAME, "b")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[1].send_keys("25")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("Masala Dosa")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].send_keys("30")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("Veg. Maggi")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].send_keys("30")
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[0].send_keys("Cheese Maggi")
        self.driver.find_elements(By.CLASS_NAME, "b")[0].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[0].send_keys("34")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[2].click()
        
        # editting
        self.driver.find_elements(By.NAME, "edit")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "a")[1].send_keys("Veg. Maggi")
        self.driver.find_elements(By.CLASS_NAME, "b")[1].clear()
        self.driver.find_elements(By.CLASS_NAME, "b")[1].send_keys("30")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click()       
       
        # logging out
        self.logout()
    
    
    
    def main_test(self):
        # self.test1()
        # self.test2()        
        # self.test3()
        # self.test4()
        # self.test5()
        # self.test6()
        # self.test7()
        # self.test8()
        # self.test9()
        # self.test10()
        # self.test11()
        # self.test12()
        # self.test13()
        # self.test14()
        # self.test15()
        # self.test16()
        # self.test17()
        # self.test18()
        self.test19()
        
        
test = tests()
test.setup_method()
test.main_test()
test.quit()