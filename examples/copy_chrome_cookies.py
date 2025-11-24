"""
Copy cookies from your Chrome Andrew profile to a browser-use profile.
This lets you use your existing logins without the profile lock issues.
"""

import shutil
import sqlite3
from pathlib import Path

# Source: Your Chrome Andrew profile
CHROME_PROFILE = Path.home() / 'Library' / 'Application Support' / 'Google' / 'Chrome' / 'Profile 3'
CHROME_COOKIES = CHROME_PROFILE / 'Cookies'

# Destination: Browser-use dedicated profile
BROWSERUSE_PROFILE = Path.home() / '.config' / 'browseruse_ticketek'
BROWSERUSE_PROFILE.mkdir(parents=True, exist_ok=True)
BROWSERUSE_COOKIES = BROWSERUSE_PROFILE / 'Cookies'

print('🍪 Copying Ticketek cookies from Chrome to browser-use profile...\n')

if not CHROME_COOKIES.exists():
	print(f'❌ Error: Chrome cookies not found at {CHROME_COOKIES}')
	print('   Make sure Chrome is closed and the path is correct.')
	exit(1)

# Check if Chrome is running (cookies file will be locked)
try:
	# Try to open the cookies database
	conn = sqlite3.connect(str(CHROME_COOKIES))
	conn.close()
except sqlite3.OperationalError:
	print('❌ Error: Chrome cookies database is locked!')
	print('   Please close Chrome completely and try again.')
	exit(1)

# Copy the cookies file
try:
	shutil.copy2(CHROME_COOKIES, BROWSERUSE_COOKIES)
	print(f'✅ Cookies copied successfully!')
	print(f'   From: {CHROME_COOKIES}')
	print(f'   To:   {BROWSERUSE_COOKIES}')
	print(f'\n📁 Browser-use profile directory: {BROWSERUSE_PROFILE}')
	print('\n✨ Now you can run oprah_sydney.py with your Ticketek login!')
except Exception as e:
	print(f'❌ Error copying cookies: {e}')
	exit(1)
