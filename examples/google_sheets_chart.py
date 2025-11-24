"""
Google Sheets - Create data and plot a chart

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Run: uv run python examples/google_sheets_chart.py

This example opens Google Sheets, enters some sample data, and creates a chart.
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

agent = Agent(
	task="""Create a chart in Google Sheets with sales data:
1. Go to Google Sheets (https://sheets.google.com)
2. Close any popups, cookie banners, or overlays
3. Create a new blank spreadsheet or use an existing one
4. Enter the following data starting from cell A1:
   - Row 1 headers: Month, Sales, Profit
   - Row 2: January, 10000, 2500
   - Row 3: February, 15000, 3800
   - Row 4: March, 12000, 3000
   - Row 5: April, 18000, 4500
   - Row 6: May, 22000, 5500
   - Row 7: June, 25000, 6200
5. Select the entire data range (A1:C7)
6. Insert a chart (Insert > Chart or use the chart button in toolbar)
7. Make it a column chart showing Sales and Profit by Month
8. Customize the chart with a title: "Monthly Sales and Profit"
9. Position the chart nicely on the spreadsheet
10. Report when complete with a summary of what was created""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
	use_vision='auto',
	max_actions_per_step=20,
	use_thinking=True,
	use_judge=True,
)
agent.run_sync()
