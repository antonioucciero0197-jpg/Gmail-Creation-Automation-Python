---
triggers:
- proxy
- socks5
- anonymous
- vpn
- ip address
---

# Proxy Configuration Guide

This script supports SOCKS5 proxy for anonymous account creation.

## Enabling Proxy Support

In `gmail_automation.py`, uncomment these lines in `main()`:

```python
# Define proxy list
proxy = ["ip:port", "ip:port"]

# Add to Chrome options
chrome_options.add_argument(f'--proxy-server=socks5://{random.choice(proxy)}')
chrome_options.add_argument('--ignore-certificate-errors')
```

## Proxy Format
- Format: `ip:port` (e.g., `192.168.1.1:1080`)
- Protocol: SOCKS5 recommended for better anonymity
- Source: http://free-proxy.cz/en/proxylist/country/all/socks5/ping/all/2

## Proxy Types Supported
```python
# SOCKS5 (recommended)
chrome_options.add_argument(f'--proxy-server=socks5://{proxy}')

# HTTP proxy
chrome_options.add_argument(f'--proxy-server=http://{proxy}')

# HTTPS proxy
chrome_options.add_argument(f'--proxy-server=https://{proxy}')
```

## With Authentication
For proxies requiring authentication:
```python
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.socks_proxy = "user:pass@ip:port"
proxy.socks_version = 5
```

## Best Practices
1. Use residential proxies for better success rates
2. Rotate proxies between account creations
3. Match proxy location with name nationality for consistency
4. Test proxy connectivity before running the script
