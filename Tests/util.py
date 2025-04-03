
from selenium import webdriver # type: ignore
import time


from config import GATEWAY_IP
from config import GATEWAY_PORT
from config import TEST_PROJECT_NAME


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=1")
    driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
    driver.set_window_size(1920,1120)
    driver.get("http://{gateway_ip}:{gateway_port}/data/perspective/client/{test_project_name}".format(gateway_ip=GATEWAY_IP, gateway_port=GATEWAY_PORT, test_project_name=TEST_PROJECT_NAME))
    time.sleep(3)
    return driver