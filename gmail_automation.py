# Gmail Account Creation Automation Script - Version 2.0.0
# Automated Gmail account creation with Italian language support
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import random
import time
from datetime import datetime, timedelta
from unidecode import unidecode

# Configuration - Set these before running
RECOVERY_EMAIL = ""  # Your existing email for verification (e.g., "myemail@example.com")
PHONE_NUMBER = ""    # Phone number for verification (format: +39xxxxxxxxxx)

def main():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--lang=it-IT")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Use system chromium
    chrome_options.binary_location = "/usr/bin/chromium"
    
    from selenium.webdriver.chrome.service import Service
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Italian names
    first_names = [
        "Marco", "Giuseppe", "Giovanni", "Francesco", "Antonio", "Alessandro", "Andrea", "Luca", "Matteo", "Lorenzo",
        "Davide", "Simone", "Federico", "Riccardo", "Stefano", "Gabriele", "Daniele", "Michele", "Nicola", "Tommaso",
        "Maria", "Anna", "Giulia", "Francesca", "Sara", "Laura", "Chiara", "Valentina", "Alessia", "Martina",
        "Elisa", "Giorgia", "Federica", "Silvia", "Elena", "Roberta", "Claudia", "Paola", "Monica", "Cristina"
    ]

    last_names = [
        "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco",
        "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Rizzo", "Lombardi", "Moretti",
        "Barbieri", "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone"
    ]

    your_first_name = random.choice(first_names)
    your_last_name = random.choice(last_names)
    random_number = random.randint(1000, 9999)
    
    your_first_name_normalized = unidecode(your_first_name).lower()
    your_last_name_normalized = unidecode(your_last_name).lower().replace(" ", "")
    your_username = f"{your_first_name_normalized}.{your_last_name_normalized}{random_number}"
    
    your_birthday = random_birthday()
    your_gender = "other"  # Always "Preferisco non specificarlo"
    your_password = f"Pwd{random.randint(10000, 99999)}!@#"

    fill_form(driver, your_username, your_password, your_first_name, your_last_name, your_birthday, your_gender)

def fill_form(driver, your_username, your_password, your_first_name, your_last_name, your_birthday, your_gender):
    try:
        # Step 1: Go to Google signup
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        wait = WebDriverWait(driver, 30)
        timeSleep(2)

        # Step 2: Fill name
        fill_name(driver, wait, your_first_name, your_last_name)
        timeSleep(2)

        # Step 3: Fill birthday and gender
        fill_birthday_and_gender(driver, wait, your_birthday, your_gender)
        timeSleep(2)

        # Step 4: Click "Non hai un indirizzo email o un numero di telefono?" and choose email
        click_no_email_option(driver, wait)
        timeSleep(2)

        # Step 5: Fill Gmail address
        fill_gmailaddress(driver, wait, your_username)
        timeSleep(2)

        # Step 6: Fill password
        fill_password(driver, wait, your_password)
        timeSleep(2)

        # Step 7: Handle verification (recovery email or phone)
        handle_verification(driver, wait, your_username)
        timeSleep(2)

        print(f"\n{'='*50}")
        print(f"Gmail creato con successo!")
        print(f"Email: {your_username}@gmail.com")
        print(f"Password: {your_password}")
        print(f"{'='*50}\n")

        # input("Premi INVIO per chiudere il browser...")  # Disabled for headless

    except Exception as e:
        print(f"Errore durante la creazione: {e}")
        try:
            driver.save_screenshot("error_screenshot.png")
            print("Screenshot salvato come error_screenshot.png")
        except:
            pass
    finally:
        driver.quit()

def fill_name(driver, wait, your_first_name, your_last_name):
    first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    first_name.clear()
    first_name.send_keys(your_first_name)
    
    last_name = driver.find_element(By.NAME, "lastName")
    last_name.clear()
    last_name.send_keys(your_last_name)
    
    click_next_button(driver, wait)
    print(f"✓ Nome inserito: {your_first_name} {your_last_name}")

def fill_birthday_and_gender(driver, wait, your_birthday, your_gender):
    wait.until(EC.visibility_of_element_located((By.ID, "day")))
    your_day, your_month, your_year = your_birthday.split()

    # Month dropdown
    month_div = wait.until(EC.element_to_be_clickable((By.ID, "month")))
    month_div.click()
    timeSleep(1)
    
    month_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//li[@role='option' and @data-value='{int(your_month)}']"
    )))
    month_option.click()

    # Day
    day_field = driver.find_element(By.ID, "day")
    day_field.clear()
    day_field.send_keys(your_day)

    # Year
    year_field = driver.find_element(By.ID, "year")
    year_field.clear()
    year_field.send_keys(your_year)

    # Gender - support multiple languages
    gender_map = {
        "other": ["Preferisco non specificarlo", "Rather not say", "Prefiero no decirlo"],
        "male": ["Uomo", "Male", "Masculino"],
        "female": ["Donna", "Female", "Femenino"],
        "custom": ["Personalizzato", "Custom", "Personalizado"]
    }
    
    gender_texts = gender_map.get(your_gender, gender_map["other"])
    
    gender_div = wait.until(EC.element_to_be_clickable((By.ID, "gender")))
    gender_div.click()
    timeSleep(1)

    # Try each language variant
    gender_option = None
    for gender_text in gender_texts:
        try:
            gender_option = driver.find_element(By.XPATH, f"//li[@role='option' and .//span[contains(text(), '{gender_text}')]]")
            if gender_option:
                break
        except:
            continue
    
    if gender_option:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", gender_option)
        timeSleep(0.5)
        gender_option.click()
    else:
        # Fallback: select third option (usually "Rather not say")
        options = driver.find_elements(By.XPATH, "//li[@role='option']")
        if len(options) >= 3:
            options[2].click()

    click_next_button(driver, wait)
    print(f"✓ Data di nascita: {your_day}/{your_month}/{your_year}, Genere: {your_gender}")

def click_no_email_option(driver, wait):
    """Click on 'Don't have an email address or phone number?' or similar"""
    try:
        # Try multiple selectors for the link (multiple languages)
        selectors = [
            # Italian
            "//button[contains(., 'Non hai un indirizzo')]",
            "//span[contains(text(), 'Non hai un indirizzo')]",
            # English
            "//*[contains(text(), \"Don't have\")]",
            "//button[contains(., \"Don't have\")]",
            "//*[contains(text(), 'without')]",
            # Spanish
            "//*[contains(text(), 'No tienes')]",
        ]
        
        for selector in selectors:
            try:
                elements = driver.find_elements(By.XPATH, selector)
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        print("✓ Cliccato su opzione 'senza email/telefono'")
                        timeSleep(1)
                        return
            except:
                continue
        
        # If not found, maybe we're already on the username page
        if driver.find_elements(By.NAME, "Username"):
            print("✓ Già sulla pagina username")
            return
        
        print("⚠ Opzione 'senza email' non trovata, continuo...")
            
    except Exception as e:
        print(f"Nota: {e}")

def fill_gmailaddress(driver, wait, your_username):
    # Try to find and click "Create your own Gmail address" if present (multiple languages)
    custom_selectors = [
        "//*[contains(text(), 'Crea il tuo indirizzo Gmail')]",
        "//*[contains(text(), 'Create your own Gmail address')]",
        "//*[contains(text(), 'Crear tu propia')]",
        "[jsname='CeL6Qc']",
    ]
    
    for selector in custom_selectors:
        try:
            if selector.startswith("["):
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
            else:
                elements = driver.find_elements(By.XPATH, selector)
            for el in elements:
                if el.is_displayed():
                    el.click()
                    timeSleep(1)
                    break
        except:
            continue

    # Fill username
    try:
        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field.clear()
        username_field.send_keys(your_username)
        
        click_next_button(driver, wait)
        print(f"✓ Username inserito: {your_username}@gmail.com")
    except Exception as e:
        print(f"⚠ Errore inserimento username: {e}")
        driver.save_screenshot("username_error.png")

def fill_password(driver, wait, your_password):
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.clear()
    password_field.send_keys(your_password)
    
    # Find confirm password field
    try:
        confirm_field = driver.find_element(By.NAME, "PasswdAgain")
    except:
        confirm_field = driver.find_element(By.NAME, "ConfirmPasswd")
    
    confirm_field.clear()
    confirm_field.send_keys(your_password)
    
    click_next_button(driver, wait)
    print(f"✓ Password inserita")

def handle_verification(driver, wait, your_username):
    """Handle verification step - recovery email or phone number"""
    timeSleep(2)
    
    # Check if we need phone verification
    phone_field = driver.find_elements(By.ID, "phoneNumberId")
    if phone_field and PHONE_NUMBER:
        phone_field[0].clear()
        phone_field[0].send_keys(PHONE_NUMBER)
        click_next_button(driver, wait)
        print(f"✓ Numero di telefono inserito: {PHONE_NUMBER}")
        print("⚠ Verifica telefono richiesta - completare manualmente")
        return

    # Check for recovery email option
    try:
        recovery_selectors = [
            (By.NAME, "recoveryEmail"),
            (By.ID, "recoveryEmail"),
            (By.XPATH, "//input[@type='email']"),
        ]
        
        for by, selector in recovery_selectors:
            recovery_fields = driver.find_elements(by, selector)
            if recovery_fields:
                if RECOVERY_EMAIL:
                    recovery_fields[0].clear()
                    recovery_fields[0].send_keys(RECOVERY_EMAIL)
                    click_next_button(driver, wait)
                    print(f"✓ Email di recupero inserita: {RECOVERY_EMAIL}")
                    return
                break
    except:
        pass

    # Try to skip if possible
    try:
        skip_buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Salta') or contains(text(), 'Skip')]")
        if skip_buttons:
            skip_buttons[0].click()
            print("✓ Verifica saltata")
            return
    except:
        pass

    # Handle terms acceptance
    try:
        agree_buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'Accetto') or contains(text(), 'I agree')]")
        if agree_buttons:
            agree_buttons[0].click()
            print("✓ Termini accettati")
    except:
        pass

    print("⚠ Verifica richiesta - processo in attesa")

def click_next_button(driver, wait):
    """Click the next/continue button"""
    try:
        # Try multiple selectors
        selectors = [
            (By.XPATH, "//button[contains(@class, 'VfPpkd-LgbsSe') and .//span[contains(text(), 'Avanti')]]"),
            (By.XPATH, "//button[.//span[contains(text(), 'Avanti')]]"),
            (By.XPATH, "//button[.//span[contains(text(), 'Next')]]"),
            (By.CLASS_NAME, "VfPpkd-LgbsSe"),
        ]
        
        for by, selector in selectors:
            try:
                buttons = driver.find_elements(by, selector)
                for btn in buttons:
                    if btn.is_displayed() and btn.is_enabled():
                        btn.click()
                        return
            except:
                continue
                
    except Exception as e:
        print(f"Errore click next: {e}")

def random_birthday(min_age=18, max_age=50):
    today = datetime.today()
    start_date = datetime(today.year - max_age, 1, 1)
    end_date = datetime(today.year - min_age, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    birth_date = start_date + timedelta(days=random_days)
    return f"{birth_date.day} {birth_date.month} {birth_date.year}"

def timeSleep(seconds):
    time.sleep(seconds + random.uniform(0.5, 1.5))

if __name__ == "__main__":
    main()
