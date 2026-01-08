---
triggers:
- selenium
- webdriver
- chromedriver
- browser automation
---

# Selenium WebDriver Guidelines for This Project

When working with Selenium in this Gmail automation project:

## Element Location Strategies
Use these locators in order of preference:
1. `By.ID` - Most reliable (e.g., `By.ID, "month"`)
2. `By.NAME` - For form fields (e.g., `By.NAME, "firstName"`)
3. `By.XPATH` - For complex selections (e.g., `By.XPATH, "//li[@role='option']"`)
4. `By.CLASS_NAME` - For buttons (e.g., `By.CLASS_NAME, "VfPpkd-LgbsSe"`)

## Wait Strategies
Always use explicit waits instead of `time.sleep()`:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)
element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))
element = wait.until(EC.element_to_be_clickable((By.NAME, "field_name")))
```

## Handling Google's Dynamic Dropdowns
Google uses custom dropdowns (not standard `<select>`). Handle them like this:
```python
# Click to open dropdown
dropdown_div = wait.until(EC.element_to_be_clickable((By.ID, "dropdown_id")))
dropdown_div.click()

# Select option by data-value or text
option = wait.until(EC.element_to_be_clickable((
    By.XPATH, f"//li[@role='option' and @data-value='{value}']"
)))
option.click()
```

## Anti-Detection Measures
Use the `timeSleep()` function for randomized delays:
```python
def timeSleep(min):
    time.sleep(random.randint(min, min+2))
```

## Chrome Options for This Project
```python
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-infobars")
# For proxy: chrome_options.add_argument(f'--proxy-server=socks5://{proxy}')
# For headless: chrome_options.add_argument("--headless")
```
