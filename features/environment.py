from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application



#firefox env
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager  # Use GeckoDriverManager for Firefox
# from selenium.webdriver.firefox.options import Options
# from app.application import Application
def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    # driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Firefox()
    #context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    #BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user ='shailakshigupta_zAY2tJ'
    # bs_key = 'jFPVxdiodvfrNkWJr7Xe'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #    "osVersion" : "11",
    #     'browserName': 'Edge',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #


    #Mobile Emulator
    # from selenium import webdriver
    mobile_emulation = {"deviceName": "Nexus 5"}
    options = webdriver.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=chrome_options)
    context.driver = webdriver.Chrome(options=chrome_options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

