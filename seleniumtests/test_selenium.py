# ################################################## NOTES ###############################################


# RUN EACH TEST INDEPENDENTLY
# ALL DATA MUST BE REMOVED BEFORE RUNNING EACH TEST
# TESTS MAY NOT WORK AFTER RUNNING ON 31 MARCH DUE TO HARDCODED DATE TIME VALUES IN TESTS 
# WE HAVE TRIED TO COVER EACH POSSIBILITY


# ########################################### THE TECH TITANS ##############################################



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class tests:
    
    def incorrect_then_correct_OTP(self):
        otp=input("OTP has been sent, please input it in the console ")
        self.driver.find_element(By.ID, "otp").send_keys(otp+1)
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "incorrect OTP"
        self.driver.find_element(By.ID, "resend_otp").click()
        otp=input("OTP has been sent, please input it in the console ")
        self.driver.find_element(By.ID, "otp").send_keys(otp)
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def incorrect_then_correct_Password_to_Liv(self):
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Div")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Liv")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Passwords don't match"
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Liv")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Liv")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def incorrect_then_correct_Password_to_Div(self):
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Div")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Liv")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Passwords don't match"
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Div")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def correct_OTP(self):
        otp=input("OTP has been sent, please input it in the console ")
        self.driver.find_element(By.ID, "otp").send_keys(otp)
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def correct_Password_to_Liv(self):
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Liv")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Liv")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def correct_Password_to_Div(self):
        self.driver.find_element(By.ID, "auth1").send_keys("1234@Div")
        self.driver.find_element(By.ID, "auth2").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

    def test(self):
        self.driver.get("http://127.0.0.1:8000/")

        # Signup for student1
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamStudent_1")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("student_1")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Student").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Liv()

        # Signup for student2
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamStudent_2")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("student_2")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Student").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Liv()



        # Signup for student2
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamStudent_3")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("student_3")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Student").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()



        # Signup for Hall Manager
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamHallManager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("hall_manager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Hall Manager").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Liv()
        


        # Signup for Mess Manager
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamMessManager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("mess_manager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Mess Manager").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Liv()



        # Signup for Canteen Manager
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamCanteenManager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("canteen_manager")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Canteen Manager").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Liv()
        


        # Signup for Sports Secy
        self.driver.find_element(By.ID, "new").click()
        self.driver.find_elements(By.CLASS_NAME, "input_text")[0].send_keys("IamSportsSecy")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[1].send_keys("sports_secy")
        self.driver.find_elements(By.CLASS_NAME, "input_text")[2].click()
        self.driver.find_element(By.ID, "Sports Secy").click()
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP verification, first put incorrect otp then resend otp then put the correct otp
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Liv()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("student_1")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student1
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("student_1")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student1
        self.incorrect_then_correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.incorrect_then_correct_Password_to_Div()

        # correct login for student1
        self.driver.find_element(By.ID, "username").send_keys("student_1")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("student_2")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student2
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("student_2")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student2
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()

        # correct login for student2
        self.driver.find_element(By.ID, "username").send_keys("student_2")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()
        


        # testing login for student3
        self.driver.find_element(By.ID, "username").send_keys("student_3")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("hall_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student2
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("hall_manager")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student2
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()

        # correct login for student2
        self.driver.find_element(By.ID, "username").send_keys("hall_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("mess_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student2
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("mess_manager")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student2
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()

        # correct login for student2
        self.driver.find_element(By.ID, "username").send_keys("mess_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("canteen_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student2
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("canteen_manager")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student2
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()

        # correct login for student2
        self.driver.find_element(By.ID, "username").send_keys("canteen_manager")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()



        # testing login for incorrect password
        self.driver.find_element(By.ID, "username").send_keys("sports_secy")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        assert self.driver.find_element(By.CLASS_NAME, "error").text == "Incorrect Password or Username"

        # checking forgot password for student2
        self.driver.find_element(By.ID, "forgot password").click()
        self.driver.find_element(By.ID, "username").send_keys("sports_secy")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()

        # OTP for Student2
        self.correct_OTP()

        # Setting password, first no matching passwords then matching (Correct Passwords)
        self.correct_Password_to_Div()

        # correct login for student2
        self.driver.find_element(By.ID, "username").send_keys("sports_secy")
        self.driver.find_element(By.ID, "password").send_keys("1234@Div")
        self.driver.find_element(By.CLASS_NAME, "submit_btn").click()
        self.logout()   
    
    
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Changes made successfully.")
        
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Changes made successfully.")
        
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Changes made successfully.")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[2].click()
        self.driver.find_elements(By.NAME, "a3")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[2].click()
        self.driver.find_elements(By.NAME, "b0")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[2].send_keys("Idli Sambhar")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[2].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
        
        # adding item
        self.driver.find_elements(By.NAME, "add_hidden_item")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "a")[2].click()
        self.driver.find_elements(By.NAME, "a3")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "b")[2].click()
        self.driver.find_elements(By.NAME, "b0")[2].click()
        self.driver.find_elements(By.CLASS_NAME, "c")[2].send_keys("Idli Sambhar")
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[1].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
        
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click()  
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
             
       
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Changes made successfully.")

        
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
        
        # deleting
        self.driver.find_elements(By.NAME, "delete")[0].click() 
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
         
        
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
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Deleted Successfully.")
        
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

        self.logout()

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

        # clicking on cleaning
        self.driver.find_elements(By.CLASS_NAME, "e1_238")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking the data for student 1

        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Others")
        self.driver.find_elements(By.NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Corridor")
        self.driver.find_elements(By.NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Toilet")
        self.driver.find_elements(By.NAME, "identity")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Room")
        self.driver.find_elements(By.NAME, "identity")[0].click()

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
    
    def test20(self):
        # add item in menu, student adds it to cart, removes from the cart
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
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        self.logout()
        
        # login student 1
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("4")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your order has been successfully added to cart")
        
        # going to cart
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # delete the item
        self.driver.find_elements(By.NAME, "order_validation1")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your Cart Item has been successfully removed")
        
        self.logout()
        
    def test21(self):
        # add item in menu, student adds it to cart, books from the cart, owner rejects
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
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        self.logout()
        
        # login student 1
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("4")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your order has been successfully added to cart")
        
        # going to cart
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # delete the item
        self.driver.find_elements(By.NAME, "order_validation2")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Order request has been made to Canteen Manager")
        
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # rejecting order
        self.driver.find_elements(By.NAME, "rejected")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "error")[0].text == "You rejected the order")
        
        self.logout()
        
        # checking in student order history
        
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        # subsection:Order history
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Veg. Maggi")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "4")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "30")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "120")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "Failed")
        
        self.logout()
        
        
    def test22(self):
        
        # add item in menu, student adds it to cart, books from the cart, owner accepts, served, paid
        # check in order history and bills
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
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        self.logout()
        
        # login student 1
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("4")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your order has been successfully added to cart")
        
        # going to cart
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # delete the item
        self.driver.find_elements(By.NAME, "order_validation2")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Order request has been made to Canteen Manager")
        
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # rejecting order
        self.driver.find_elements(By.NAME, "accepted")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "You accepted the order")
        
        # changing subsection
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # served
        self.driver.find_elements(By.NAME, "served")[0].click()
        
        # paid
        self.driver.find_elements(By.NAME, "paid")[0].click()
        
        assert(len(self.driver.find_elements(By.NAME, "served")) == 0)
        
        
        self.logout()
        
        # checking in student order history
        
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        # subsection:Order history
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Veg. Maggi")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "4")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "30")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "120")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "Sucessful")
        
        # clicking on my account
        self.driver.find_elements(By.CLASS_NAME, "e1_230")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        assert(self.driver.find_elements(By.NAME, "show")[0].text == "Your Canteen bill is Rs. 0")
        
        # logging out
        self.logout()
        
        # self.login_canteen_manager()
        
        # # clicking on canteen
        # self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # # subsection of canteen
        # assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        # assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "0")
        
        # self.logout()
        
        
    def test23(self):
        
        # add item in menu, student adds it to cart, books from the cart, owner accepts, served, removed
        # check in order history and bills
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
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        self.logout()
        
        # login student 1
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("4")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your order has been successfully added to cart")
        
        # going to cart
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # delete the item
        self.driver.find_elements(By.NAME, "order_validation2")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Order request has been made to Canteen Manager")
        
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # rejecting order
        self.driver.find_elements(By.NAME, "accepted")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "You accepted the order")
        
        # changing subsection
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # served
        self.driver.find_elements(By.NAME, "served")[0].click()
        
        # paid
        self.driver.find_elements(By.NAME, "removed")[0].click()
        
        assert(len(self.driver.find_elements(By.NAME, "served")) == 0)
        
        
        self.logout()
        
        # checking in student order history
        
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        # subsection:Order history
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Veg. Maggi")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "4")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "30")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "120")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "Sucessful")
        
        # clicking on my account
        self.driver.find_elements(By.CLASS_NAME, "e1_230")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        assert(self.driver.find_elements(By.NAME, "show")[0].text == "Your Canteen bill is Rs. 120")
        
        # logging out
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsection of canteen
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "120")
        
        self.logout()
        
    def test24(self):
        # checking the clear dues functnality
        
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
        
        # submitting
        self.driver.find_elements(By.NAME, "submit")[0].click()
        
        self.logout()
        
        # login student 1
        self.login_student_1()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_242")[0].click()
        
        self.driver.find_elements(By.NAME, "quantity")[0].clear()
        self.driver.find_elements(By.NAME, "quantity")[0].send_keys("4")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your order has been successfully added to cart")
        
        # going to cart
        
        # subsections of canteen
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # delete the item
        self.driver.find_elements(By.NAME, "order_validation2")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Order request has been made to Canteen Manager")
        
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # rejecting order
        self.driver.find_elements(By.NAME, "accepted")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "You accepted the order")
        
        # changing subsection
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()
        
        # served
        self.driver.find_elements(By.NAME, "served")[0].click()
        
        # paid
        self.driver.find_elements(By.NAME, "removed")[0].click()
        
        assert(len(self.driver.find_elements(By.NAME, "served")) == 0)
        
        self.logout()
        
        self.login_canteen_manager()
        
        # clicking on canteen
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        
        # subsection of canteen
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "120")
        
        self.driver.find_elements(By.NAME, "order_validation1")[0].send_keys("5")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "25")
        self.logout()
        
        
    def test25(self):
        
        # Guest room booking testing
        self.driver.get("https://upha.pythonanywhere.com/")
         
        # logging in as student
        self.login_student_1()

        # clicking on Booking
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()

        # booking a guest room
        self.driver.find_elements(By.NAME, "checkin_date")[0].send_keys("2023-04-03")
        self.driver.find_elements(By.NAME, "checkout_date")[0].send_keys("2023-04-05")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for this room has been sent to the Hall manager, please contact him for further proceedings. UPHA team will communicate their confirmation to you.")

        # checking guestroom bookings
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 5, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "Pending...")

        # logging out student_1
        self.logout()

        # logging in hall manager
        self.login_hall_manager()

        # switching to booking
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()

        # checking
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "April 5, 2023")

        #accepting the request
        self.driver.find_elements(By.CLASS_NAME, "approve")[0].click()

        # checking the message and the updated request
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The booking has been validated")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[0].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "h")[0].text == "April 5, 2023")

        # logging out from hall manager
        self.logout()

        #logging into student_1
        self.login_student_1()

        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking if booked
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 5, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[0].text == "Booked")

        # clicking on Booking
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()

        # booking a guest room
        self.driver.find_elements(By.NAME, "checkin_date")[0].send_keys("2023-04-02")
        self.driver.find_elements(By.NAME, "checkout_date")[0].send_keys("2023-04-04")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for this room has been sent to the Hall manager, please contact him for further proceedings. UPHA team will communicate their confirmation to you.")

        # checking guestroom bookings
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "April 2, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "April 4, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Pending...")

        # logging out student_1
        self.logout()

        # logging in hall manager
        self.login_hall_manager()

        # switching to booking
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()

        # checking
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 2, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "April 4, 2023")

        #accepting the request
        self.driver.find_elements(By.CLASS_NAME, "approve")[0].click()

        # checking the message and the updated request
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The booking has been validated")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[1].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "h  ")[1].text == "April 5, 2023")

        # logging out from hall manager
        self.logout()

        #logging into student_1
        self.login_student_1()

        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking if booked
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "April 2, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "April 4, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Booked")

        # clicking on Booking
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()

        # booking a guest room
        self.driver.find_elements(By.NAME, "checkin_date")[0].send_keys("2023-04-03")
        self.driver.find_elements(By.NAME, "checkout_date")[0].send_keys("2023-04-06")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for this room has been sent to the Hall manager, please contact him for further proceedings. UPHA team will communicate their confirmation to you.")

        # checking guestroom bookings
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "April 6, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Pending...")

        # logging out student_1
        self.logout()

        # logging in hall manager
        self.login_hall_manager()

        # switching to booking
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()

        # checking
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 3, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "April 6, 2023")

        #accepting the request
        self.driver.find_elements(By.CLASS_NAME, "reject")[0].click()

        # checking the message
        assert(self.driver.find_elements(By.CLASS_NAME, "error")[0].text == "The booking has been rejected")
        assert(len(self.driver.find_elements(By.CLASS_NAME, "e")) == 2)

        # logging out from hall manager
        self.logout()

        #logging into student_1
        self.login_student_1()

        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking if booked
        assert(len(self.driver.find_elements(By.CLASS_NAME, "e")) == 2)


        # clicking on Booking
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()

        # booking a guest room
        self.driver.find_elements(By.NAME, "checkin_date")[0].send_keys("2023-04-01")
        self.driver.find_elements(By.NAME, "checkout_date")[0].send_keys("2023-04-06")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for this room has been sent to the Hall manager, please contact him for further proceedings. UPHA team will communicate their confirmation to you.")

        # checking guestroom bookings
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "April 1, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "April 6, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Pending...")

        # logging out student_1
        self.logout()

        # logging in hall manager
        self.login_hall_manager()

        # switching to booking
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()

        # checking
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "April 1, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "April 6, 2023")

        #accepting the request
        self.driver.find_elements(By.CLASS_NAME, "approve")[0].click()

        # checking the message and the updated request
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The booking has been validated")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "g")[1].text == "April 1, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "h  ")[1].text == "April 6, 2023")

        # logging out from hall manager
        self.logout()

        #logging into student_1
        self.login_student_1()

        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        # checking if booked
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "April 1, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[1].text == "April 6, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[1].text == "Rs.900")
        assert(self.driver.find_elements(By.CLASS_NAME, "e")[1].text == "Booked")

    
    def test26(self):

        # Testing of booking of sports equipment and their return
        self.driver.get("https://upha.pythonanywhere.com/")

        # logging in as hall manager
        self.login_sports_secy()

        # adding equipment, first badminton then 
        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        self.driver.find_elements(By.NAME, "equipment_quantity")[0].send_keys("3")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        

        self.driver.find_elements(By.NAME, "sport")[0].click()
        self.driver.find_elements(By.ID, "CB")[0].click()
        self.driver.find_elements(By.NAME, "equipment_quantity")[0].send_keys("3")
        self.driver.find_elements(By.NAME, "submit")[0].click()

        # logging out of sports secy
        self.logout()

        # logging into student_1
        self.login_student_1()
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()

        # requesting for equipment
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for this item has been sent to the secretary.")
        self.driver.find_elements(By.NAME, "submit")[1].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for returning this item has been sent to the secretary.")
        self.driver.find_elements(By.NAME, "submit")[5].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for returning this item has been sent to the secretary.")

        # checking if requested
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Cricket Bat")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Pending...")
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[1].text == "Badminton")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[1].text == "Pending...")

        # logging out of student_1
        self.logout()

        # logging into sports secy
        self.login_sports_secy

        # Validating and rejecting
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Cricket Bat")
        self.driver.find_elements(By.CLASS_NAME, "reject")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The request has been rejected")
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Badminton")
        self.driver.find_elements(By.CLASS_NAME, "accept")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The request has been validated")

        # logging out of sports secy
        self.logout()

        # logging into student_1
        self.login_student_1()

        # checking the reduce in availability
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_9")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "2")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "Not available")
        assert(self.driver.find_elements(By.CLASS_NAME, "f")[0].text == "2")

        # testing return of item
        self.driver.find_elements(By.CLASS_NAME, "e2_4")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Badminton")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "Your request for returning this item has been sent to the secretary.")
        self.driver.find_elements(By.NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "You have already requested for return of this item.")

        # logging out of student_1
        self.logout()

        # logging into sports secy
        self.login_sports_secy()

        self.driver.find_elements(By.CLASS_NAME, "e1_246")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_5")[0].click()

        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "s1")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "Badminton")
        self.driver.find_elements(By.CLASS_NAME, "submit")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "success")[0].text == "The return has been validated")
        
        self.logout()

    def test27(self):
        # testing of booking of sports court

        # logging into student_1
        self.login_student_1()

        # booking menu
        self.driver.find_elements(By.CLASS_NAME, "e1_234")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "e2_8")[0].click()

        self.driver.find_elements(By.NAME, "sport")[0].click()
        self.driver.find_elements(By.ID, "CB")[0].click()
        self.driver.find_elements(By.NAME, "checkin_time")[0].send_keys("14:00")
        self.driver.find_elements(By.NAME, "checkout_time")[0].send_keys("16:00")
        self.driver.find_elements(By.NAME, "date")[0].send_keys("2023-04-02")
        self.driver.find_elements(By.NAME, "submit").click()

        # checking
        self.driver.find_elements(By.CLASS_NAME, "e2_19")[0].click()
        assert(self.driver.find_elements(By.CLASS_NAME, "a")[0].text == "Cricket")
        assert(self.driver.find_elements(By.CLASS_NAME, "b")[0].text == "April 2, 2023")
        assert(self.driver.find_elements(By.CLASS_NAME, "c")[0].text == "2 p.m.")
        assert(self.driver.find_elements(By.CLASS_NAME, "d")[0].text == "4 p.m.")
        
        
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
        # self.test19()
        # self.test20()
        # self.test21()
        # self.test23()
        # self.test24()
        # self.test25()
        # self.test26()
        self.test27()
        
test = tests()
test.setup_method()
test.main_test()
test.quit()