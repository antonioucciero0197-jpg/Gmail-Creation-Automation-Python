---
triggers:
- language
- localization
- translate
- spanish
- french
- italian
- german
- english
---

# Localization Guidelines

This script is currently configured for Spanish language Google signup pages.

## Language-Dependent Elements

### Gender Dropdown Options
The gender dropdown uses visible text that changes by language:

| Language | Male | Female | Prefer not to say | Custom |
|----------|------|--------|-------------------|--------|
| Spanish | Masculino | Femenino | Prefiero no decirlo | Personalizado |
| English | Male | Female | Rather not say | Custom |
| French | Homme | Femme | Je préfère ne pas le dire | Personnalisé |
| Italian | Uomo | Donna | Preferisco non specificarlo | Personalizzato |
| German | Männlich | Weiblich | Keine Angabe | Benutzerdefiniert |

### Custom Email Button Text
The button to create a custom Gmail address:

| Language | Text |
|----------|------|
| Spanish | Crear dirección de Gmail personalizada |
| English | Create your own Gmail address |
| French | Créer votre propre adresse Gmail |
| Italian | Crea il tuo indirizzo Gmail |
| German | Eigene Gmail-Adresse erstellen |

## How to Change Language

1. Update the `gender_map` dictionary in `fill_birthday_and_gender()`:
```python
gender_map = {
    "male": "YOUR_LANGUAGE_MALE",
    "female": "YOUR_LANGUAGE_FEMALE",
    "other": "YOUR_LANGUAGE_NOT_SAY",
    "custom": "YOUR_LANGUAGE_CUSTOM"
}
```

2. Update the custom email button selector in `fill_gmailaddress()`:
```python
custom_buttons = driver.find_elements(By.XPATH, "//div[contains(text(), 'YOUR_LANGUAGE_TEXT')]")
```

## Name Lists by Nationality
The script includes name lists. Current options:
- Spanish names (active in `gmail_automation.py`)
- French names (commented out, available in both scripts)

To add new nationalities, create lists following the existing pattern.
