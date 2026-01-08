# Gmail Creation Automation Python

## Purpose

This repository provides a Python automation script for creating Gmail accounts using Selenium and Chrome WebDriver. It automates the Gmail sign-up process by programmatically filling in required details such as name, username, password, birthday, and gender.

**Note:** This script is provided for educational and informational purposes only. Automating website interactions may violate the website's terms of service.

## Setup Instructions

### Prerequisites
- Python 3.x
- Chrome browser installed
- ChromeDriver executable matching your Chrome version

### Install Dependencies
```bash
pip install -r requirements.txt
```

Dependencies:
- `selenium` - Browser automation framework
- `unidecode` - Unicode text to ASCII conversion (for normalizing names)

### Running the Script
```bash
python gmail_automation.py
```

## Repository Structure

```
.
├── gmail_automation.py    # Main automation script (v1.1.0) - USE THIS
├── script.py              # Legacy script (French names, older implementation)
├── chromedriver.exe       # Chrome WebDriver (Windows only)
├── requirements.txt       # Python dependencies
├── readme.md              # Project documentation
├── env/                   # Python virtual environment (do not modify)
└── .github/
    └── FUNDING.yml        # GitHub sponsorship configuration
```

## CI/CD Workflows

No CI/CD pipelines, GitHub Actions, linters, or pre-commit hooks are configured.
The `.github/` folder contains only `FUNDING.yml` for Buy Me a Coffee sponsorship.

## Development Guidelines

### Primary Script
Always modify `gmail_automation.py` for new features. The `script.py` file is a legacy version.

### Key Functions in gmail_automation.py
- `main()` - Entry point, configures Chrome options and initializes data
- `fill_form()` - Orchestrates the entire form-filling process
- `fill_name()` - Fills first and last name fields
- `fill_birthday_and_gender()` - Handles date picker and gender dropdown
- `fill_gmailaddress()` - Sets custom Gmail username
- `fill_password()` - Enters and confirms password
- `random_birthday()` - Generates random birthdate (18-70 years old)
- `timeSleep()` - Randomized delay to avoid detection

### Selenium Best Practices for This Project
1. Use `WebDriverWait` with `expected_conditions` for element interactions
2. Use `By.ID`, `By.NAME`, `By.XPATH` for element location
3. Add random delays with `timeSleep()` to avoid bot detection
4. Handle dynamic elements (dropdowns) with explicit waits

### Localization Notes
The script uses Spanish language selectors. Key text strings that change by language:
- Gender options: "Masculino", "Femenino", "Prefiero no decirlo", "Personalizado"
- Custom email button: "Crear dirección de Gmail personalizada"

### Proxy Configuration
To enable SOCKS5 proxy, uncomment these lines in `main()`:
```python
chrome_options.add_argument(f'--proxy-server=socks5://{random.choice(proxy)}')
chrome_options.add_argument('--ignore-certificate-errors')
```

### Adding New Name Lists
Name lists are defined as Python lists in `main()`. To add new nationalities:
1. Create new lists: `new_first_names = [...]` and `new_last_names = [...]`
2. Update `random.choice()` calls to use the new lists
3. Ensure names are properly encoded (UTF-8) - `unidecode` handles accent removal

### Common Issues
- **ChromeDriver version mismatch**: Download matching version from https://chromedriver.chromium.org/
- **Element not found**: Google may change element IDs/classes - inspect the signup page
- **Phone verification required**: Script attempts random numbers but may need real verification
