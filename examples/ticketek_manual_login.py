"""
Manually login to Ticketek once and save the session.

This script opens a browser, you login manually, then it saves your session
for future automation runs.

Setup:
1. Run this script: uv run python examples/ticketek_manual_login.py
2. Browser will open to Ticketek login page
3. Login manually with your credentials
4. Press Enter when done
5. Your session is saved for future use
"""

import asyncio
from pathlib import Path

from browser_use import BrowserSession

# Dedicated profile for Ticketek automation
TICKETEK_PROFILE = Path.home() / '.config' / 'browseruse_ticketek'
TICKETEK_PROFILE.mkdir(parents=True, exist_ok=True)


async def manual_login():
	"""Open Ticketek for manual login and save the session"""
	print('=' * 60)
	print('Ticketek Manual Login')
	print('=' * 60)
	print(f'Profile directory: {TICKETEK_PROFILE}')
	print('=' * 60)
	print('\n📌 Instructions:')
	print('1. Browser will open to Ticketek login page')
	print('2. Login manually with your email and password')
	print('3. Wait until you see you are logged in')
	print('4. Come back here and press Enter')
	print('5. Your session will be saved for future automation')
	print('\nOpening browser...\n')

	# Create browser session (not an async context manager)
	session = BrowserSession(
		headless=False,  # Must be visible for manual login
		user_data_dir=str(TICKETEK_PROFILE),
	)

	try:
		# Start the session
		await session.start()

		# Get a page
		context = session.context
		page = context.pages[0] if context.pages else await context.new_page()

		# Navigate to Ticketek login
		print('🌐 Navigating to Ticketek login page...')
		await page.goto('https://premier.ticketek.com.au/account/login')

		print('\n✅ Browser opened to Ticketek login page')
		print('\n⏳ Please login now...')
		print('   Enter your email and password')
		print('   Complete any verification steps')
		print('   Make sure you see your account name/profile')
		print('\nPress Enter when you are fully logged in: ')

		# Wait for user to complete login
		await asyncio.get_event_loop().run_in_executor(None, input)

		# Session is automatically saved in the user_data_dir
		print(f'\n✅ Session saved to: {TICKETEK_PROFILE}')
		print('\n🎉 Done! You can now run automation scripts.')
		print('   They will use this saved login session.\n')

	finally:
		# Close the session
		await session.close()


if __name__ == '__main__':
	asyncio.run(manual_login())
