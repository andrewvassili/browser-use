"""
StockX - Search and buy Jordan 1 Retro High OG shoes

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Run: uv run python examples/stockx_jordan.py

This example searches for Jordan 1 Retro High OG shoes on StockX and attempts to buy them.
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
	task="""Search for and attempt to buy Jordan 1 Retro High OG shoes on StockX:
1. Go to StockX (https://stockx.com)
2. Close any popups, cookie banners, or overlays
3. Search for "Jordan 1 Retro High OG"
4. Browse the search results and select the most popular/iconic colorway (like Chicago, Bred, Royal Blue, etc.)
5. Review the available sizes and prices
6. Select a common size (US Men's 10 or 10.5)
7. Click to buy/place bid
8. Continue through the checkout process as far as possible
9. STOP when you reach the payment/login section
10. Report: shoe name, colorway, selected size, lowest ask price, and current checkout step
11. DO NOT complete payment or create an account - just stop when asked for payment/login details""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
	use_vision='auto',
	max_actions_per_step=20,
	use_thinking=True,
	use_judge=True,
)
agent.run_sync()
