# ESTCube 1 Satellite Orbital Mechanics
This Python script calculates and visualizes the ground track of the ESTCube 1 satellite using Two-Line Element (TLE) data. It utilizes the beyond library for orbital calculations and matplotlib for plotting the ground track on a map. Additionally, it employs folium for generating an interactive HTML map with the ground track overlaid.

## Requirements
- Python 3.x
- Beyond library (install via pip: pip install beyond)
- Matplotlib (install via pip: pip install matplotlib)
- NumPy (install via pip: pip install numpy)
- Folium (install via pip: pip install folium)

## Usage
Ensure all dependencies are installed.
Run the script.
The script will generate an HTML file named Test3.html, which contains an interactive map showing the ground track of the ESTCube 1 satellite.

## How it works
- Processing the TLE: The TLE data for ESTCube 1 satellite is provided and used to initialize the satellite's orbit.
- Ground Track Calculation: The script calculates the satellite's positions over a specified time period and converts them to latitude and longitude coordinates.
- Plotting: The ground track coordinates are plotted on an interactive map using folium. Starting and ending points are marked in red and green, respectively.
- Grid Overlay: The map also includes grid lines representing latitudinal and longitudinal intervals, the equator, and the prime meridian.

## Notes
The script generates an interactive HTML map (Test3.html) in the current directory. You can open this file in a web browser to explore the ground track.
Adjustments to the ground track visualization can be made by modifying parameters such as the time period, step size, or map styling.
Feel free to customize and further develop this script for your specific needs!
