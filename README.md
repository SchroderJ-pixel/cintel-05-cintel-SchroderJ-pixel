# cintel-05-cintel-SchroderJ-pixel
Project 5
Continuous Intelligence Dashboard
This is a real-time temperature monitoring dashboard created using Shiny for Python. The application generates simulated temperature data and displays it with a live-updating graph, table, and timestamp.

Features
Real-time temperature readings in Celsius and Fahrenheit.
Displays a live-updating plot of the temperature data.
Visualizes the trend of temperature with a regression line.
Shows the current timestamp and recent temperature readings in a data table.
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
2. Install dependencies
Ensure you have Python 3.8 or higher installed. You can then install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
Or, to upgrade Shiny if needed:

bash
Copy code
pip install --upgrade shiny
The requirements.txt file should contain:

Copy code
shiny
plotly
scipy
3. Run the app
Once the dependencies are installed, run the Shiny app with:

bash
Copy code
python app.py
This will start a local web server, and you can access the app by navigating to http://localhost:8000 in your browser.

Code Overview
reactive_calc_combined(): Simulates the generation of random temperature data in Celsius and Fahrenheit at regular intervals.
update_deque(): Updates the deque (a data structure) with the most recent temperature readings, maintaining a maximum size of 10 data points.
UI Components:
Displays the latest temperature reading in Celsius and Fahrenheit.
Displays a plot with the temperature data and a regression trend line.
Shows the current timestamp.
Displays the data grid with the most recent entries.
Customization
CSS: You can customize the appearance of the app by modifying the styles.css file.
Temperature Range: The temperature range is currently set between -18°C and -16°C. You can modify this in the reactive_calc_combined function.
