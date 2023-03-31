from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class test_Login:
    def setup_method(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def quit(self):
        self.driver.quit()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "e1_226 button2").click()
    
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





test = test_Login()

test.setup_method()
test.test()
test.quit()