"""
Create a chart without login using a free online tool

Setup:
1. Get your API key from https://cloud.browser-use.com/new-api-key
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
3. Run: uv run python examples/chart_maker_no_login.py

This example uses a free online chart maker that doesn't require login.
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
	task="""Create a chart using a free online tool (no login required):
1. Go to ChartGo (https://www.chartgo.com) or Meta-Chart (https://www.meta-chart.com/bar) - whichever works without login
2. Close any popups or cookie banners
3. Create a bar chart with the following data:
   - January: 10000
   - February: 15000
   - March: 12000
   - April: 18000
   - May: 22000
   - June: 25000
4. Set chart title to "Monthly Sales"
5. Set Y-axis label to "Sales ($)"
6. Set X-axis label to "Month"
7. Customize colors if possible (make it look professional)
8. Generate/preview the chart
9. Report when complete and describe the chart""",
	llm=ChatBrowserUse(),
	browser_session=browser_session,
	use_vision='auto',
	max_actions_per_step=20,
	use_thinking=True,
	use_judge=True,
)
agent.run_sync()
