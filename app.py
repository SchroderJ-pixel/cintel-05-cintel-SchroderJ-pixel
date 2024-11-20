# Action 1: Import Items
from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from faicons import icon_svg
from collections import deque
import plotly.graph_objects as go
from scipy import stats
import os
import plotly.graph_objects as go
from scipy import stats
import shutil


# Action 2: Plan Our Reactive Content
UPDATE_INTERVAL_SECS = 1

@reactive.calc()
def reactive_calc_combined():
    """Generate new data (simulated temperature) at regular intervals."""
    # Generate random temperature values
    temp_celsius = round(random.uniform(-18, -16), 1)
    temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 1)  # Convert to Fahrenheit
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_entry = {"temp_celsius": temp_celsius, "temp_fahrenheit": temp_fahrenheit, "timestamp": timestamp}
    return latest_entry

# Deque to store recent data points
max_size = 10  # Maximum number of data points to store
recent_data = deque(maxlen=max_size)

@reactive.calc()
def update_deque():
    """Update the deque with new data entries."""
    latest_entry = reactive_calc_combined()
    recent_data.append(latest_entry)
    return list(recent_data)  # Return the deque as a list

# Action 3: Define the UI Layout Page Options
app_ui = ui.page_opts(
    title="Continuous Intelligence Dashboard",  # Page title displayed at the top
    fillable=True  # This will make the UI fluid (use full width of the page)
)

# Action 4: Define the Shiny UI Layout - Sidebar
with ui.sidebar(open="open"):
    ui.h2("Live Data Dashboard", class_="text-center")  # Heading
    ui.p("Real-time temperature readings.", class_="text-center")  # Centered description

# Main section where the real-time data will be displayed
ui.h2("Current Temperature")

@render.text
def display_temp():
    """Display the latest temperature."""
    latest_data = reactive_calc_combined()  # Getting the most recent data from the reactive function
    return f"{latest_data['temp_celsius']} C / {latest_data['temp_fahrenheit']} F"  # Display both Celsius and Fahrenheit

# Icon and warmer message
ui.p("Warmer than usual")
icon_svg("sun")

# Horizontal line for separation
ui.hr()

# Display current timestamp
ui.h2("Current Date and Time")

@render.text
def display_time():
    """Display the current timestamp."""
    latest_data = reactive_calc_combined()  # Get the most recent timestamp
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
    data = update_deque()  # Fetch the most recent data from the deque
    timestamps = [entry['timestamp'] for entry in data]  # Extract timestamps for the x-axis
    temps_celsius = [entry['temp_celsius'] for entry in data]  # Extract temperature values for the y-axis
    
    # Perform linear regression for the trend line
    x = range(len(temps_celsius))  # x-axis data (indices of the data points)
    slope, intercept, _, _, _ = stats.linregress(x, temps_celsius)  # Linear regression
    trend_line = [slope * i + intercept for i in x]  # Compute the trend line

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=temps_celsius, mode='markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=timestamps, y=trend_line, mode='lines', name='Trend Line'))
    
    # Save the figure to a PNG file
    image_path = "/tmp/temp_plot.png"
    fig.write_image(image_path)

    # Return the image file path to render it
    return image_path

