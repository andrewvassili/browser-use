"""
Setup:
1. First run: uv run python examples/ticketek_login.py (to save your login session)
2. Get your API key from https://cloud.browser-use.com/new-api-key
3. Set environment variable: export BROWSER_USE_API_KEY="your-key"
4. Run this script: uv run python examples/ticketek_aew_secure.py

This example uses a pre-saved login session, so your password never goes to the LLM.
"""

from pathlib import Path

from dotenv import load_dotenv

from browser_use import Agent, BrowserSession, ChatBrowserUse

load_dotenv()

# Use the same profile directory as the login script
USER_DATA_DIR = Path.home() / '.config' / 'ticketek_profile' / 'browser_profile'
STORAGE_STATE_FILE = USER_DATA_DIR / 'storage_state.json'

# Check if user has logged in first
if not STORAGE_STATE_FILE.exists():
	print('❌ Error: You need to login first!')
	print('   Run: uv run python examples/ticketek_login.py')
	exit(1)

browser_session = BrowserSession(
	headless=False,
	user_data_dir=str(USER_DATA_DIR),
	storage_state=str(STORAGE_STATE_FILE),
)

agent = Agent(
	task="""Go to https://ticketek.com and complete the following:
1. You should already be logged in (check top right for account info)
2. Find the next AEW event in Sydney
3. Buy 2 tickets, but only if each ticket costs $500 or less
4. If tickets are more than $500 each, report the price and do not proceed with purchase""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
)
agent.run_sync()
