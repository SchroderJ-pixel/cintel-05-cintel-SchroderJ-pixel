from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from collections import deque
import plotly.graph_objects as go
from scipy import stats

pip install --upgrade shiny


# Action 2: Plan Our Reactive Content
UPDATE_INTERVAL_SECS = 1

@reactive.calc()
def reactive_calc_combined():
    """Generate new data (simulated temperature) at regular intervals."""
    temp_celsius = round(random.uniform(-18, -16), 1)
    temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_entry = {"temp_celsius": temp_celsius, "temp_fahrenheit": temp_fahrenheit, "timestamp": timestamp}
    return latest_entry

max_size = 10  # Maximum number of data points to store
recent_data = deque(maxlen=max_size)

@reactive.calc()
def update_deque():
    """Update the deque with new data entries."""
    latest_entry = reactive_calc_combined()
    recent_data.append(latest_entry)
    return list(recent_data)

# Action 3: Define the UI Layout Page Options
app_ui = ui.page_opts(
    title="Continuous Intelligence Dashboard",
    fillable=True,
    css="styles.css"  # Link to the custom CSS file
)

# Action 4: Define the Shiny UI Layout - Sidebar
with ui.sidebar(open="open"):
    ui.h2("Live Data Dashboard", class_="text-center")
    ui.p("Real-time temperature readings.", class_="text-center")

ui.h2("Current Temperature")

@render.text
def display_temp():
    """Display the latest temperature."""
    latest_data = update_deque()[-1]  # Getting the most recent data from the deque
    return f"{latest_data['temp_celsius']} C / {latest_data['temp_fahrenheit']} F"

# Icon and warmer message
ui.p("Warmer than usual")
ui.icon("sun")  # FontAwesome sun icon

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Display the current timestamp."""
    latest_data = update_deque()[-1]  # Get the most recent timestamp
    return f"{latest_data['timestamp']}"

# Action 5: Display the data grid (recent data stored in deque)
@render.table
def display_data_grid():
    """Display the data grid with the most recent entries."""
    return update_deque()

# Action 6: Display the Plotly Chart with temperature data and trend line
@render.plot
def display_plot():
    """Display a Plotly chart with temperature data and a trend line."""
    data = update_deque()
    timestamps = [entry['timestamp'] for entry in data]
    temps_celsius = [entry['temp_celsius'] for entry in data]
    
    x = range(len(temps_celsius))
    slope, intercept, _, _, _ = stats.linregress(x, temps_celsius)
    trend_line = [slope * i + intercept for i in x]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=temps_celsius, mode='markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=timestamps, y=trend_line, mode='lines', name='Trend Line'))
    
    return fig  # This returns the figure directly for interactive display
