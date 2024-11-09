from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fouls_value = 0
match_fouls_value =0
player_name = ""
match_info = ""



def closeCookiesWindow(driver):
    cookie_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@aria-label, 'Consent') or contains(@class, 'fc-cta-consent')]")
        )
    )
    cookie_button.click()

def foulsPlayer(driver):
    fouls_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Faule')]/following-sibling::div//span"))
    )
    global fouls_value
    fouls_value = fouls_element.text

def playerName(driver):
    player_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-zt63wq-PlayerNameCSS"))
    )
    global player_name
    player_name = player_name_element.text

def matches(driver):
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-iho0mw-PlayerMatchStatsTableBody"))
    )
    link_element = div_element.find_element(By.TAG_NAME, "a")
    link = link_element.get_attribute("href")
    driver.get(link + ":tab=lineup")

def matchFouls(driver):
    span_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(@class, 'css-1kub1nq-LineupPlayerText') and contains(@title, '{player_name}')]")
        )
    )
    span_element.click()
    match_fouls_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "li.css-qc4i8b-RowContainer.e1jy3r7k3 .StatValue span"))
    )
    
    global match_fouls_value
    match_fouls_value = match_fouls_element.text
    print(match_fouls_value)

def matchTeams(driver):
    team1 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='css-12r3z1-TeamName e1vkkyp5']//span"))
    )
    
    team2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//header//div[3]//span/span[2]"))
    )
    
    score = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//header//div[2]//span[1]"))
    )
   
    global match_info
    match_info = f"{team1.text} {score.text} {team2.text}"
    



def getFouls():
    return fouls_value

def getName():
    return player_name
def getMatchFouls():
    return match_fouls_value
def getMatchInfo():
    return match_info
