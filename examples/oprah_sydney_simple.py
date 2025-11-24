"""
Simple version - just hardcode your credentials in the task.

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Update your email/password below
4. Run: uv run python examples/oprah_sydney_simple.py

Yes, this sends credentials to the LLM, but it actually works.
"""

from dotenv import load_dotenv

from browser_use import Agent, ChatBrowserUse

load_dotenv()

# UPDATE THESE
YOUR_EMAIL = "zvqzuughccgidhzelt@nesopf.com"
YOUR_PASSWORD = "&%bj6n15aFQrTK&$L"

from browser_use import BrowserSession, BrowserProfile

# Enable demo mode to see what the agent is doing
browser_profile = BrowserProfile(
	headless=False,
	demo_mode=True,  # Shows a visual panel with agent actions
)

browser_session = BrowserSession(
	browser_profile=browser_profile,
)

agent = Agent(
	task=f"""Find and purchase tickets for Oprah's event in Sydney:
1. Go to Ticketek (https://premier.ticketek.com.au)
2. Close any popups, cookie banners, or overlays that appear
3. Search for Oprah in Sydney
4. If you need to login to proceed (e.g., to purchase or see tickets), use these credentials:
   Email: {YOUR_EMAIL}
   Password: {YOUR_PASSWORD}
5. Find the best available seats for 2 people
6. IMPORTANT: Select exactly 2 tickets - look for the + symbol next to the word 'Admit' and the number (usually 0 or 1), click + to increase quantity to 2
7. Select the highest quality/best positioned tickets available (VIP, front row, premium, etc.)
8. Always dismiss/close any popups, cookie banners, or overlays that block the page
9. VERIFY that you have selected 2 tickets before proceeding to checkout
10. Continue through the checkout process until you reach the payment section
11. When you reach the payment page, scroll down to see all payment options (credit card, PayPal, etc.)
12. STOP immediately when you can see the payment options and report: ticket type, price per ticket, total price, quantity (must be 2), seating details, and current checkout step
13. DO NOT enter any payment information - just stop when you see the payment options""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
	use_vision='auto',  # Send screenshots when needed
	max_actions_per_step=20,  # Execute up to 20 actions per step (vs default 4)
	use_thinking=True,  # Enable thinking for better decision making
	use_judge=True,  # Skip quality checking for speed
)
agent.run_sync()
