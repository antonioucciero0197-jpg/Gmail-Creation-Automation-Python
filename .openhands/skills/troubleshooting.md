heil softwa---
triggers:
- error
- bug
- fix
- not working
- failed
- exception
- troubleshoot
- debug
---

# Troubleshooting Guide

## Common Errors and Solutions

### ChromeDriver Version Mismatch
**Error:** `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX`

**Solution:**
1. Check your Chrome version: `chrome://version/`
2. Download matching ChromeDriver: https://chromedriver.chromium.org/downloads
3. Replace `chromedriver.exe` in the project root

### Element Not Found
**Error:** `NoSuchElementException` or `TimeoutException`

**Causes:**
- Google changed the page structure
- Element not loaded yet
- Wrong locator

**Solutions:**
1. Increase wait timeout: `WebDriverWait(driver, 30)`
2. Inspect the signup page to find new element IDs/classes
3. Update locators in the affected function

### Phone Verification Required
**Error:** Script stops at phone verification step

**Solution:**
The script attempts random Moroccan numbers (+2126...). For reliable verification:
1. Use a real phone number service
2. Implement SMS API integration
3. Use virtual phone number services

### Dropdown Selection Fails
**Error:** Cannot select month or gender

**Cause:** Google uses custom dropdowns, not standard `<select>` elements

**Solution:** Use the XPATH approach:
```python
option = wait.until(EC.element_to_be_clickable((
    By.XPATH, f"//li[@role='option' and @data-value='{value}']"
)))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
option.click()
```

### Bot Detection
**Error:** Account creation blocked or CAPTCHA appears

**Solutions:**
1. Use `timeSleep()` for random delays
2. Enable proxy rotation
3. Use `--disable-blink-features=AutomationControlled`
4. Add realistic mouse movements

### SSL Certificate Errors (with Proxy)
**Error:** SSL certificate verification failed

**Solution:** Add to Chrome options:
```python
chrome_options.add_argument('--ignore-certificate-errors')
```

## Debugging Tips

1. **Run in visible mode** (remove `--headless` if present)
2. **Add print statements** to track progress
3. **Take screenshots** on error:
```python
except Exception as e:
    driver.save_screenshot('error.png')
    print(e)
```
4. **Check browser console** for JavaScript errors
