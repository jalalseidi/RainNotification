# Weather Notification Script

This script fetches weather forecasts from the **OpenWeatherMap API** and sends an SMS notification via **Twilio** if rain is expected.

## Features
- Fetches a 4-timeframe weather forecast for a given location
- Checks if rain is expected using weather condition codes
- Sends an SMS alert if rain is detected

## Requirements
- Python 3.x
- Twilio account with SMS capabilities
- OpenWeatherMap API key

## Setup

### 1. Install Dependencies
Run the following command to install the required libraries:
```sh
pip install requests twilio python-dotenv
```

### 2. Set Up Environment Variables
To keep your API keys secure, store them in environment variables:

#### Windows (PowerShell)
```powershell
$env:TWILIO_SID="your_twilio_sid"
$env:TWILIO_AUTH="your_twilio_auth_token"
$env:WEATHER_API="your_openweather_api_key"
```

#### Mac/Linux (Terminal)
```bash
export TWILIO_SID="your_twilio_sid"
export TWILIO_AUTH="your_twilio_auth_token"
export WEATHER_API="your_openweather_api_key"
```

### 3. Run the Script
```sh
python weather_sms.py
```

## How It Works
1. The script requests weather data from OpenWeatherMap for a specified location.
2. It checks if **rainy conditions** (`weather_id < 700`) are in the forecast.
3. If rain is detected, an SMS alert is sent via Twilio.

## Customization
- Change `MY_LAT` and `MY_LONG` in the script to get weather data for your location.
- Modify the message content in `client.messages.create()` to customize the SMS alert.

