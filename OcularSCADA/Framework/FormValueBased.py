import time

from selenium.webdriver.common.by import By # type: ignore



class FormValueBased:

    def __init__(self, driver):
        self.driver = driver




    def set_value(self, key, value, form_type):
        
        if form_type == "textinput":
            self.set_value_of_textinput(key, value)
        elif form_type == "textarea":
            self.set_value_of_textarea(key, value)
        elif form_type == "dropdown":
            self.set_value_of_textarea(key, value)
        elif form_type == "checkbox":
            self.set_value_of_textarea(key, value)



    def set_value_of_textinput(self, key, value):
        pass
    
    def set_value_of_textarea(self, key, value):
        pass

    def set_value_of_dropdown(self, key, value):
        pass

    def set_value_of_checkbox(self, key, value):
        pass





    def get_value(self, key, form_type):
        pass