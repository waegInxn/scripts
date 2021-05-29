# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import time

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class AgreementGenerator:

    def __init__(self):
        
        display = Display(visible=0, size=(800, 800))  
        display.start()

        opt = webdriver.ChromeOptions()
        opt.add_argument("no-sandbox")
        opt.add_argument("--disable-dev-shm-usage")
        opt.add_argument("--remote-debugging-port=9222") 

        self.driver = webdriver.Chrome('chromedriver', options=opt)
        self.user_name = 'valentynp@interxion.com'
        self.password = 'Nevzlomatinxn1'

        self.opps = ['0062p00001Ct74CAAR','0062p00001Ct74FAAR','0062p00001Ct74NAAR','0062p00001Ct748AAB','0062p00001Ct74KAAR','0062p00001Ct74LAAR','0062p00001Ct74DAAR','0062p00001Ct74MAAR','0062p00001Ct74EAAR','0062p00001Ct74IAAR','0062p00001Ct74AAAR','0062p00001Ct74OAAR','0062p00001Ct74HAAR','0062p00001Ct74BAAR','0062p00001Ct74GAAR','0062p00001Ct749AAB','0062p00001Ct74JAAR']
        self.prod_url = 'https://interxion.my.salesforce.com/'
        self.prodmirror_url = 'https://interxion--prodmirror.my.salesforce.com/'

        self.url = self.prod_url
        #self.url = self.prodmirror_url

        self.login_as_user_id = '0052p00000Ad0Pp'

        self.start_creating_agreements()

    def start_creating_agreements(self):
        # Use a breakpoint in the code line below to debug your script.
        print('Start...')

        self.login_to_sandbox()

        b = input('Go to home page in your sandbox and click "y" : ')

        if b == 'y':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "home_Tab")))

            self.driver.get(self.url + self.login_as_user_id + "?noredirect=1&isUserEntityOverride=1")
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "login")))
            self.driver.find_element_by_name("login").click()

            time.sleep(2)

            for oppId in self.opps:
                self.create_agreeement(oppId)

            print('agreemnets created')
    # Press the green button in the gutter to run the script.

    def login_to_sandbox(self):

        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "i0116")))

        username = self.driver.find_element_by_id("i0116")
        username.send_keys(self.user_name)

        self.driver.find_element_by_id("idSIButton9").click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "i0118")))

        password = self.driver.find_element_by_id("i0118")
        password.send_keys(self.password)
        
        self.driver.find_element_by_id("idSIButton9").click()

    def create_agreeement(self, oppId):

        try:
            self.driver.get(self.url + oppId)
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "create_agreement")))

            self.driver.find_element_by_name("create_agreement").click()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "j_id0:j_id1:j_id5:idRecordType:j_id37:j_id38")))

            select = Select(self.driver.find_element_by_name('j_id0:j_id1:j_id5:idRecordType:j_id37:j_id38'))
            select.select_by_visible_text('DLR Amendment - Colo')
            self.driver.find_element_by_name("j_id0:j_id1:j_id5:j_id32:j_id33").click()

            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "save")))
            self.driver.find_element_by_name("save").click()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "alternative_submit_button")))

        except:
            print('Please check the occurred error in browser.. Failed opportunity: ' + oppId)
            pass  #go to next

if __name__ == '__main__':
    ag = AgreementGenerator()
