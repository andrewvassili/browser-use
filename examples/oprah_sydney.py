"""
Oprah Sydney ticket search example.

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Update your email/password below if you want to enable login
4. Run: uv run python examples/oprah_sydney.py
"""

from dotenv import load_dotenv

from browser_use import Agent, BrowserSession, BrowserProfile, ChatBrowserUse

load_dotenv()

# Enable demo mode to see what the agent is doing
browser_profile = BrowserProfile(
	headless=False,
	demo_mode=True,  # Shows a visual panel with agent actions
)

browser_session = BrowserSession(
	browser_profile=browser_profile,
)

# UPDATE THESE - Optional: only needed if login is required
YOUR_EMAIL = "zvqzuughccgidhzelt@nesopf.com"
YOUR_PASSWORD = "&%bj6n15aFQrTK&$L"

agent = Agent(
	task=f"""Find and purchase tickets for Oprah's event in Sydney:
1. Go directly to Ticketek (https://premier.ticketek.com.au)
2. Close any cookie popups, banners, or overlays that appear
3. Search for Oprah events in Sydney
4. Find the best available seats for 2 people
5. Select the highest quality/best positioned tickets available (VIP, front row, premium, etc.)
6. Always dismiss any popups, cookie banners, or overlays that block the page
7. Proceed to purchase the 2 best tickets
8. If you need to login to proceed (e.g., to purchase or see tickets), use these credentials:
   Email: {YOUR_EMAIL}
   Password: {YOUR_PASSWORD}
9. Report the ticket type, price, and seating details before completing purchase""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
)
agent.run_sync()
