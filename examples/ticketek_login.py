"""
Pre-login to Ticketek manually - run this once to save your session.

Setup:
1. Run this script: uv run python examples/ticketek_login.py
2. Manually login to Ticketek in the browser window that opens
3. Press Enter when done - your session will be saved
4. Future scripts will use this saved session without needing credentials
"""

import asyncio
from pathlib import Path

from browser_use import BrowserSession

# Persistent browser profile directory
USER_DATA_DIR = Path.home() / '.config' / 'ticketek_profile' / 'browser_profile'
USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Storage state file for cookies
STORAGE_STATE_FILE = USER_DATA_DIR / 'storage_state.json'


async def manual_login():
	"""Open Ticketek for manual login and save the session"""
	print('=' * 60)
	print('Ticketek Manual Login')
	print('=' * 60)
	print(f'Browser profile directory: {USER_DATA_DIR}')
	print(f'Storage state file: {STORAGE_STATE_FILE}')
	print('=' * 60)
	print('\n📌 Instructions:')
	print('1. Browser will open to Ticketek')
	print('2. Login manually with your credentials')
	print('3. Wait until fully logged in')
	print('4. Come back here and press Enter')
	print('5. Your session will be saved for future use')
	print('\nOpening browser...\n')

	# Create browser session with persistent profile
	async with BrowserSession(
		headless=False,  # Must be visible for manual login
		user_data_dir=str(USER_DATA_DIR),
		storage_state=str(STORAGE_STATE_FILE) if STORAGE_STATE_FILE.exists() else None,
	) as session:
		# Get the page from the context
		page = session.context.pages[0] if session.context.pages else await session.context.new_page()

		# Navigate to Ticketek login page
		await page.goto('https://premier.ticketek.com.au/account/login')

		print('✅ Browser opened to Ticketek login page')
		print('\n⏳ Please login now...')
		print('\nPress Enter when you are logged in and ready to save the session: ')

		# Wait for user to complete login
		await asyncio.get_event_loop().run_in_executor(None, input)

		# Save the storage state (cookies, localStorage, etc.)
		storage_state = await session.context.storage_state()
		STORAGE_STATE_FILE.write_text(str(storage_state))

		print(f'\n✅ Session saved to: {STORAGE_STATE_FILE}')
		print('\n🎉 Done! You can now use other scripts without providing credentials.')
		print('   They will automatically use this saved session.\n')


if __name__ == '__main__':
	asyncio.run(manual_login())
