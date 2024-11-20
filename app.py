# Action 1: Import Items
from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from faicons import icon_svg

# Action 2: Plan Our Reactive Content
UPDATE_INTERVAL_SECS: int = 1 

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp_celsius = round(random.uniform(-18, -16), 1)
    temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 1)  # Convert Celsius to Fahrenheit
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp_celsius": temp_celsius, "temp_fahrenheit": temp_fahrenheit, "timestamp": timestamp}
    return latest_dictionary_entry

# Action 3: Define the UI Layout Page Options
app_ui = ui.page_opts(
    title="PyShiny Express: Live Data (Basic)",  # Page title displayed at the top
    fillable=True  # This will make the UI fluid (use full width of the page)
)

# Action 4: Define the Shiny UI Layout - Sidebar
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")  # Heading
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",  # Centered text
    )

# Action 5: Define the Shiny UI Layout - Main Section
# Main content section where the real-time data will be displayed

ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest temperature and return it as a string."""
    latest_dictionary_entry = reactive_calc_combined()
    temp_celsius = latest_dictionary_entry['temp_celsius']
    temp_fahrenheit = latest_dictionary_entry['temp_fahrenheit']
    return f"{temp_celsius} C / {temp_fahrenheit} F"  # Display both Celsius and Fahrenheit

ui.p("warmer than usual")

icon_svg("sun")

# Add a horizontal line for separation
ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest timestamp and return it as a string."""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"
