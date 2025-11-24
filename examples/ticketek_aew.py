"""
Use your existing Chrome profile with saved Ticketek login.

Setup:
1. Make sure you're logged into Ticketek in your regular Chrome browser
2. Close Chrome completely (important - Chrome locks the profile when running)
3. Get your API key from https://cloud.browser-use.com/new-api-key
4. Set environment variable: export BROWSER_USE_API_KEY="your-key"
5. Update CHROME_PROFILE_DIR below if your Chrome profile is in a different location
6. Run: uv run python examples/ticketek_aew.py

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
	task="""Go to https://ticketek.com and complete the following:
1. You should already be logged in from Chrome (check top right for account info)
2. Find the next AEW event in Sydney
3. Buy 2 tickets, but only if each ticket costs $500 or less
4. If tickets are more than $500 each, report the price and do not proceed with purchase""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
)
agent.run_sync()
