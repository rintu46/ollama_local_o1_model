# Tourist Information and Navigation System

## Overview
This Python script provides local tourist information, including popular attractions, descriptions, visiting hours, and route information from your current location. It automatically detects your location and provides relevant tourist information.

## Installation Guide

### Step 1: Python Installation
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install Python (3.6 or newer)
   - Windows: Check "Add Python to PATH" during installation
   - Mac/Linux: Python usually comes pre-installed

### Step 2: Required Packages
Run these commands in your terminal/command prompt:

```bash
pip install geocoder
pip install wikipedia
pip install requests
pip install beautifulsoup4
pip install googlemaps
pip install geopy
pip install folium
pip install osmnx
pip install networkx
```

### Step 3: File Setup
1. Download `tourist_guide.py` to your computer
2. Open terminal/command prompt
3. Navigate to the folder containing tourist_guide.py:
   ```bash
   cd path/to/folder
   ```

## Running the Script

### Basic Usage
1. Open terminal/command prompt
2. Navigate to the script's directory
3. Run the script:
   ```bash
   python tourist_guide.py
   ```
   or
   ```bash
   python3 tourist_guide.py
   ```

### What to Expect
1. The script will:
   - Show your current time
   - Display your current location
   - Provide a brief description of your area
   - List nearby tourist attractions

2. When the attractions list appears:
   - Enter the number of the attraction you want to learn about
   - Enter '0' to exit
   - Type 'y' to see another place after viewing details

### Features
- Automatic location detection
- Tourist attraction discovery
- Detailed place information
- Distance calculations
- Route information for different transport modes
- Interactive maps (saved as HTML files)

## Troubleshooting

### Common Issues and Solutions

1. **Location Detection Failed**
   - Check internet connection
   - Allow location access if prompted
   - Try running script as administrator

2. **No Tourist Places Found**
   - Check internet connection
   - Try searching with different location names
   - Ensure location name is correctly spelled

3. **Map Not Generated**
   - Check write permissions in the folder
   - Ensure folium package is installed
   - Verify internet connection

4. **Package Installation Errors**
   ```bash
   # Try updating pip first
   pip install --upgrade pip
   
   # Install packages one by one
   pip install geocoder
   pip install wikipedia
   # ... (continue with other packages)
   ```

### System Requirements
- Python 3.6 or newer
- Active internet connection
- 4GB RAM minimum
- 500MB free disk space
- Modern web browser for viewing maps

## Additional Information

### Map Files
- Maps are saved as 'route_map.html'
- Open with any web browser
- New maps overwrite old ones

### Transport Modes
The script provides route information for:
- Car
- Bus
- Taxi

### Data Sources
- Wikipedia
- TripAdvisor
- OpenStreetMap
- IP Geolocation

## Tips for Best Results
1. Ensure stable internet connection
2. Allow location access when prompted
3. Wait for complete results before making selections
4. Keep browser open for viewing maps
5. Run script from a directory with write permissions

## Error Messages
- "Could not fetch location details": Check internet and location services
- "Couldn't find detailed information": Try different attraction or location
- "Route Information error": Verify place name and internet connection

## Support
If you encounter issues:
1. Verify all packages are installed
2. Check internet connection
3. Ensure Python version compatibility
4. Try running as administrator
5. Check for write permissions in directory

## Updates and Maintenance
- Keep Python and packages updated
- Check for script updates regularly
- Clear old map files periodically

This guide should help you get started with the tourist information system. For additional help, check the troubleshooting section or contact support. 