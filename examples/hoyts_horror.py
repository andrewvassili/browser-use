"""
Use your existing Chrome profile with saved Hoyts login.

Setup:
1. Make sure you're logged into Hoyts in your regular Chrome browser (if account required)
2. Close Chrome completely (important - Chrome locks the profile when running)
3. Get your API key from https://cloud.browser-use.com/new-api-key
4. Set environment variable: export BROWSER_USE_API_KEY="your-key"
5. Update CHROME_PROFILE_DIR below if your Chrome profile is in a different location
6. Run: uv run python examples/hoyts_horror.py

This uses your existing Chrome login sessions, so no password needed.
"""

from pathlib import Path

from dotenv import load_dotenv

from browser_use import Agent, BrowserSession, ChatBrowserUse

load_dotenv()

# Chrome profile directory for macOS
# Change 'Profile 3' to your actual profile name if different
# To find your profile: cat ~/Library/Application\ Support/Google/Chrome/Local\ State | grep last_used
CHROME_PROFILE_DIR = Path.home() / 'Library' / 'Application Support' / 'Google' / 'Chrome' / 'Profile 3'

if not CHROME_PROFILE_DIR.exists():
	print(f'❌ Error: Chrome profile not found at: {CHROME_PROFILE_DIR}')
	print('\n💡 Find your Chrome profile:')
	print('   - macOS: ~/Library/Application Support/Google/Chrome/Default')
	print('   - Linux: ~/.config/google-chrome/Default')
	print('   - Windows: %LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default')
	print('\nUpdate CHROME_PROFILE_DIR in this script and try again.')
	exit(1)

print('⚠️  IMPORTANT: Make sure Chrome is completely closed!')
print('   Chrome locks the profile when running.\n')
input('Press Enter when Chrome is closed to continue...')

browser_session = BrowserSession(
	headless=False,
	user_data_dir=str(CHROME_PROFILE_DIR.parent),  # Chrome User Data directory
)

agent = Agent(
	task="""Go to Hoyts website and complete the following:
1. Find Hoyts Broadway cinema
2. Look for the latest and best-rated horror movie currently showing
3. Buy 2 tickets for the next available session
4. You should already be logged in from Chrome (if login was required)""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
)
agent.run_sync()
