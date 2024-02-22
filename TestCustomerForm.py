import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCustomerForm(unittest.TestCase):

    def take_screenshot(self, test_name):
        screenshot_path = f"{test_name}_screenshot.png"
        self.driver.save_screenshot(screenshot_path)

    def test_case1(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual(result, "First Name: johnjohn")

        self.take_screenshot("image/test_case1")

        self.driver.close()

    def test_case2(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("Johnj")
        lastNameInput.send_keys("canoncanoncano")
        ageInput.send_keys("149")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual(result, "First Name: Johnj")

        self.take_screenshot("image/test_case2")

        self.driver.close()

    def test_case3(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjo")
        lastNameInput.send_keys("canoncanoncanon")
        ageInput.send_keys("150")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual(result, "First Name: johnjo")

        self.take_screenshot("image/test_case3")

        self.driver.close()

    def test_case4(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohnjohnjo")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual(result, "First Name: johnjohnjohnjo")

        self.take_screenshot("image/test_case4")

        self.driver.close()

    def test_case5(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohnjohnjoh")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "firstname").text
        self.assertEqual(result, "First Name: johnjohnjohnjoh")

        self.take_screenshot("image/test_case5")

        self.driver.close()

    def test_case6(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("John")
        lastNameInput.send_keys("cannoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual(result, "Customer Detail Form")

        self.take_screenshot("image/test_case6")

        self.driver.close()

    def test_case8(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("cano")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual(result, "Customer Detail Form")

        self.take_screenshot("image/test_case8")

        self.driver.close()

    def test_case10(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("0")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual(result, "Customer Detail Form")

        self.take_screenshot("image/test_case10")

        self.driver.close()

    def test_case11(self):
        self.driver = webdriver.Chrome(executable_path="D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://localhost/customer/form.html")

        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")

        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("151")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual(result, "Customer Detail Form")

        self.take_screenshot("image/test_case11")

        self.driver.close()

if __name__ == "__main__":
    unittest.main()
