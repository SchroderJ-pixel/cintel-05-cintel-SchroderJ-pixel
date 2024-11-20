# cintel-05-cintel-SchroderJ-pixel
Project 5

Continuous Intelligence Dashboard

This project is a real-time temperature monitoring dashboard built using Shiny for Python. It generates simulated temperature data and displays it on a live-updating dashboard with a temperature plot, data grid, and 
timestamp. The dashboard allows users to visualize trends and view recent data.

Features

Real-Time Data: Simulated temperature readings in Celsius and Fahrenheit.

Interactive Plot: Displays temperature data with a regression trend line using Plotly.

Live Data Grid: Shows the most recent temperature entries in a table.

Current Time: Displays the current timestamp of the latest temperature entry.

Warmer than usual message with an icon.

Installation
Follow these steps to get the project up and running on your local machine.

1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
2. Install Dependencies
Ensure you have Python 3.8+ installed. Use pip to install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Alternatively, you can manually install the dependencies:

bash
Copy code
pip install shiny
pip install plotly
pip install scipy
3. Run the App
Once the dependencies are installed, you can start the Shiny app by running:

bash
Copy code
python app.py
The application will start a local server. You can access the dashboard by navigating to http://localhost:8000 in your web browser.

Project Structure
app.py: The main Python file containing the Shiny app logic and UI definition.
styles.css: Custom CSS file for styling the dashboard.
requirements.txt: List of dependencies required for the project.
README.md: Project documentation (this file).
Code Overview
Key Components:
Simulated Data Generation:

reactive_calc_combined(): Generates random temperature data (Celsius and Fahrenheit) at regular intervals and stores the timestamp.
Data Handling:

update_deque(): Updates the deque with the most recent temperature readings, keeping only the latest 10 entries.
Shiny UI Layout:

Dashboard Title and Sidebar: Displays the application title and a short description.
Current Temperature Display: Shows the latest temperature reading in both Celsius and Fahrenheit.
Current Timestamp: Displays the most recent timestamp when data was updated.
Data Grid: A table of the most recent temperature entries.
Temperature Plot: A Plotly chart displaying the temperature data along with a regression trend line.
