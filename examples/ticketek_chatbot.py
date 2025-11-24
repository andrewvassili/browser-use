"""
Ticketek Chatbot - Ask about Good Things festival

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Run: uv run python examples/ticketek_chatbot.py

This example uses the Ticketek chatbot to find out when Good Things festival is on.
"""

from dotenv import load_dotenv

from browser_use import Agent, BrowserSession, BrowserProfile, ChatBrowserUse

load_dotenv()

# Enable demo mode to see what the agent is doing
browser_profile = BrowserProfile(
	headless=False,
	demo_mode=True,
)

browser_session = BrowserSession(
	browser_profile=browser_profile,
)

agent = Agent(
	task="""Use the Ticketek chatbot to find out when Good Things festival is on:
1. Go to Ticketek (https://premier.ticketek.com.au/)
2. Close any popups or cookie banners
3. Wait for the page to fully load
4. Look for the chatbot in the bottom right corner of the page
5. Click on the chatbot to open it
6. Type the question: "When is Good Things festival on?"
7. Wait for the chatbot response
8. Read the response and extract the date/dates when Good Things festival is on
9. If the chatbot doesn't understand, try asking: "Good Things festival dates" or "Good Things festival schedule"
10. Report back with the festival dates and any other relevant information from the chatbot""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
	use_vision='auto',
	max_actions_per_step=20,
	use_thinking=True,
	use_judge=True,
)
agent.run_sync()
