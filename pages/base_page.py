from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop


class BasePageMethods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click(self, element_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(element_locator)).click()

    def send_keys(self, element_locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(element_locator)).send_keys(text)

    def find_element(self, element_locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def find_elements(self, elements_locator):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(elements_locator))

    def is_element_clickable(self, element_locator):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(element_locator))
            return True
        except:
            return False

    def is_element_invisible(self, element_locator):
        try:
            self.wait.until(expected_conditions.invisibility_of_element_located(element_locator))
            return True
        except:
            return False

    def is_element_displayed(self, element_locator):
        try:
            element = self.wait.until(expected_conditions.visibility_of_element_located(element_locator))
            return element.is_displayed()
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def dnd_element_to_target(self, element, target):
        drag_and_drop(self.driver, element, target)

    def get_text(self, element_locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(element_locator)).text

    def wait_for_text_to_change(self, element_locator, old_text, timeout=10):
        def _predicate(driver):
            try:
                element = self.find_element(element_locator)
                element_text = element.text.strip()
                return element_text != old_text
            except:
                return False

        try:
            WebDriverWait(self.driver, timeout).until(_predicate)
            return True
        except TimeoutException:
            return False

    def scroll_into_view(self, target):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
