# Weather App 🌤️

A beautiful desktop weather application built with PyQt5 that provides real-time weather information for any city in the world using the OpenWeather API.

## ✨ Features

- 🌡️ **Real-time Weather Data**: Get current weather information for any city worldwide
- 🎨 **Dynamic UI**: Background color changes based on weather conditions
- 📊 **Comprehensive Information**:
  - Current temperature (Celsius & Fahrenheit)
  - Min/Max temperature
  - Feels-like temperature
  - Wind speed
  - Weather description with emoji
  - Geographic coordinates
- 🛡️ **Robust Error Handling**: Handles network errors, API errors, and invalid inputs gracefully
- 💅 **Beautiful Interface**: Clean, modern design with custom styling

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- OpenWeather API key (free)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arnaaavvv/Weather-app.git
   cd Weather-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Get a free API key from [OpenWeather API](https://openweathermap.org/api)
   - Rename `config_example.py` to `config.py`
   - Open `config.py` and replace `your_api_key_here` with your actual API key:
     ```python
     OPENWEATHER_API_KEY = "your_actual_api_key_here"
     ```

5. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

1. Launch the application
2. Enter a city name in the text field
3. Click the "Get Weather" button
4. View the weather information displayed on the screen

The background color will automatically change based on the current weather conditions:
- ☀️ Clear sky → Light blue
- 🌧️ Rain → Sky blue
- ⛈️ Thunderstorm → Dark gray
- 🌨️ Snow → White
- 🌫️ Fog/Mist → Silver
- ☁️ Cloudy → Light gray

## 🛠️ Technologies Used

- **Python** - Programming language
- **PyQt5** - GUI framework
- **Requests** - HTTP library for API calls
- **OpenWeather API** - Weather data provider

## 📦 Dependencies

```
certifi==2026.1.4
charset-normalizer==3.4.4
idna==3.11
PyQt5==5.15.11
PyQt5-Qt5==5.15.2
PyQt5_sip==12.18.0
requests==2.32.5
urllib3==2.6.3
```

## 🔒 API Key Security

This project uses a separate configuration file to keep your API key secure:
- `config.py` contains your actual API key and is listed in `.gitignore`
- `config_example.py` is a template for users to create their own `config.py`
- Never commit your `config.py` file to version control

## ⚠️ Error Handling

The application handles various errors gracefully:
- Invalid city names
- Network connection issues
- API timeouts
- Invalid API keys
- Server errors (500, 502, 503, 504)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Arnav Chaudhari**
GitHub: [@Arnaaavvv](https://github.com/Arnaaavvv)

## 🏆 Acknowledgments

- Weather data provided by [OpenWeather API](https://openweathermap.org/)
- Icons and emojis from Unicode standard
- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)

⭐ If you found this project helpful, please give it a star!