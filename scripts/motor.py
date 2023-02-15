from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager


class Motor:
    def __init__(self) -> None:
        self.open_driver()
        self.open_chat()
        
    def open_driver(self)-> None:
        profile_path = r''
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('-profile')
        firefox_options.add_argument(profile_path)
        self.dr = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        
    def open_chat(self):
        self.dr.get('https://chat.openai.com/chat')
    
    def write_text(self, msg:str) -> str:
        self.dr.find_element(By.TAG_NAME, 'textarea').send_keys(msg)
        self.dr.find_element(By.TAG_NAME, 'textarea').send_keys(Keys.ENTER)
        
    def get_response(self) -> str:
        tag = 'w-full border-b border-black/10 dark:border-gray-900/50 text-gray-800 dark:text-gray-100 group bg-gray-50 dark:bg-[#444654]'
        response = self.dr.find_elements(By.XPATH, "//div[@class='{}']".format(tag))
        print(response[-1].text)
        return response[-1].text
    
    def query_response(self) -> str:
        tag = 'btn flex justify-center gap-2 btn-neutral border-0 md:border'
        try:
            response = self.dr.find_element(By.XPATH, "//button[@class='{}']".format(tag)).text
            print(response)
            return response
        except:
            ...            
    def await_response(self) -> str:
        while True:
            response = self.query_response()
            if isinstance(response, str) and response == 'Regenerate response':
                return self.get_response()

            print('await...')
            sleep(1)
            

# motor = Motor()
# motor.write_text('como usar firefox com profile no selenium')
# motor.await_response()