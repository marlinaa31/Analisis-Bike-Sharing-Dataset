# Analisis_dicoding

**Final Project Data Analysis**

## Setup Environment

```
conda create --name myenv python=3.9.18
conda activate myenv
pip install numpy pandas matplotlib seaborn streamlit
```

## Run Streamlit App

```
streamlit run dashboard.py
```

## Dataset Overview

### Introduction

This dataset contains the hourly and daily count of rental bikes between the years 2011 and 2012 in the Capital bike share system with the corresponding weather and seasonal information.

## Data Structure

- `instant`: Sequential unique identifier for each row.
- `dteday`: Date of the recorded data.
- `season`: Season (1: Spring, 2: Summer, 3: Fall, 4: Winter)
- `yr`: Year (0: 2011, 1: 2012)
- `mnth`: Month (1 to 12)
- `hr`: Hour (0 to 23)
- `holiday`: Binary feature indicating whether it's a holiday or not.
- `weekday`: Day of the week (0: Sunday, 1: Monday, ..., 6: Saturday).
- `workingday`: Binary feature indicating whether it's a working day or not.
- `weathersit`: Weather situation:
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- `temp`: Normalized temperature in Celsius. Values are divided by 41 (max)
- `atemp`: Normalized feeling temperature in Celsius. Values are divided by 50 (max)
- `hum`: Normalized humidity. Values are divided by 100 (max)
- `windspeed`: Normalized wind speed. Values are divided by 67 (max)
- `casual`: Count of casual users
- `registered`: Count of registered users
- `cnt`: Total count of bike rentals (casual + registered).
