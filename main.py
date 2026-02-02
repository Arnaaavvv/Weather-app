import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from config import OPENWEATHER_API_KEY

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city = QLabel("Enter the city name : ",self)
        self.city_input = QLineEdit(self)
        self.get_weather = QPushButton("Get Weather",self)
        self.temp = QLabel(self)
        self.emoji = QLabel(self)
        self.description = QLabel(self)
        self.min_temp = QLabel(self)
        self.max_temp = QLabel(self)
        self.feels_like = QLabel(self)
        self.wind_speed = QLabel(self)
        self.coordinates = QLabel(self)
        self.UI()
        
    def UI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather)
        
        hbox = QHBoxLayout()
        
        center_vbox = QVBoxLayout()
        center_vbox.addWidget(self.temp)
        center_vbox.addWidget(self.emoji)
        center_vbox.addWidget(self.description)
        
        right_vbox = QVBoxLayout()
        right_vbox.addWidget(self.min_temp)
        right_vbox.addWidget(self.max_temp)
        right_vbox.addWidget(self.feels_like)
        right_vbox.addWidget(self.wind_speed)
        right_vbox.addWidget(self.coordinates)
        right_vbox.addStretch()
        
        hbox.addLayout(center_vbox)
        hbox.addLayout(right_vbox)
        
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.city.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        self.min_temp.setAlignment(Qt.AlignRight)
        self.max_temp.setAlignment(Qt.AlignRight)
        self.feels_like.setAlignment(Qt.AlignRight)
        self.wind_speed.setAlignment(Qt.AlignRight)
        self.coordinates.setAlignment(Qt.AlignRight)
        
        self.city.setObjectName("city")
        self.city_input.setObjectName("city_input")
        self.get_weather.setObjectName("get_weather")
        self.temp.setObjectName("temp")
        self.emoji.setObjectName("emoji")
        self.description.setObjectName("description")
        self.min_temp.setObjectName("min_temp")
        self.max_temp.setObjectName("max_temp")
        self.feels_like.setObjectName("feels_like")
        self.wind_speed.setObjectName("wind_speed")
        self.coordinates.setObjectName("coordinates")
        
        self.base_style = '''
            QLabel, QPushButton {
                font-family : calibri;
            }
            
            QLabel#city {
                font-size : 40px;
                font-style : Italic;
                font-weight : bold;
            }
            
            QLineEdit#city_input {
                font-size : 40px;
            }
            
            QPushButton#get_weather {
                font-size : 30px;
                font-weight : bold;
            }
            
            QLabel#temp {
                font-size : 75px;
            }
            
            QLabel#emoji {
                font-size : 100px;
                font-family : Segoe UI emoji;
            }
            
            QLabel#description {
                font-size : 40px
            }
            
            QLabel#min_temp, QLabel#max_temp, QLabel#feels_like, QLabel#wind_speed {
                font-size : 30px;
                padding : 10px;
            }
            
            QLabel#coordinates {
                font-family : Roboto Mono;
                font-size : 30px;
                padding : 10px;
            }
        '''
        
        self.setStyleSheet(self.base_style)
        
        self.get_weather.clicked.connect(self.getWeather)
        
    def getWeather(self):
        api_key = OPENWEATHER_API_KEY
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.displayWeather(data)
            
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.displayError("Bad Request:\nPlease check your input")
                case 401:
                    self.displayError("Unauthorized:\nInvalid API key")
                case 403:
                    self.displayError("Forbidden access:\nAccess is denied")
                case 404:
                    self.displayError("Not found:\nCity not found")
                case 500:
                    self.displayError("Internal server error:\nPlease try again later")
                case 502:
                    self.displayError("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.displayError("Service unavailable:\nPlease check your input")
                case 504:
                    self.displayError("Gateway Timeout:\nNo response from server")
                case _:
                    self.displayError(f"HTTP error occured:\n{http_error}")
                    
        except requests.exceptions.ConnectionError:
            self.displayError("Connection Error:\nCheck your internet connection")
        
        except requests.exceptions.Timeout:
            self.displayError("Timeout Error:\nThe request timed out")
        
        except requests.exceptions.TooManyRedirects:
            self.displayError("Too many redirects:\nCheck the url")
        
        except requests.exceptions.RequestException as reqError:
            self.displayError(f"Request Error:\n{reqError}")
        
    def displayError(self, message):
        self.temp.setStyleSheet('font-size:30px')
        self.temp.setText(message)
        self.emoji.clear()
        self.description.clear()
        self.min_temp.clear()
        self.max_temp.clear()
        self.feels_like.clear()
        self.wind_speed.clear()
        self.coordinates.clear()
    
    def displayWeather(self,data):
        self.temp.setStyleSheet('font-size:75px')
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = (temp_k*9/5) - 459.67
        
        min_temp_k = data['main']['temp_min']
        max_temp_k = data['main']['temp_max']
        feels_like_k = data['main']['feels_like']
        
        min_temp_c = min_temp_k - 273.15
        max_temp_c = max_temp_k - 273.15
        feels_like_c = feels_like_k - 273.15
        
        wind_speed = data['wind']['speed']
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        
        weather_id = data['weather'][0]['id']
        weather_desc = data['weather'][0]['description']
        
        self.temp.setText(f"{temp_c:.0f}°C/{temp_f:.0f}°F")
        self.emoji.setText(self.getWeatherIcon(weather_id))
        self.description.setText(weather_desc)
        self.min_temp.setText(f"* Min Temp: {min_temp_c:.0f}°C")
        self.max_temp.setText(f"* Max Temp: {max_temp_c:.0f}°C")
        self.feels_like.setText(f"Feels Like: {feels_like_c:.0f}°C")
        self.wind_speed.setText(f"Wind Speed: {wind_speed} m/s")
        self.coordinates.setText(f"Coordinates of place:\n({latitude}°, {longitude}°)")
        self.setBackground(weather_id)
        
    @staticmethod
    def getWeatherIcon(weather_id):
        
        if 200<=weather_id<=232:
            return "⛈️"
        elif 300<=weather_id<=321:
            return "🌦️"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600<=weather_id<=622:
            return "🌨️"
        elif 701<=weather_id<=741:
            return "🌫️"
        elif weather_id==762:
            return "🌋"
        elif weather_id==771:
            return "🍃"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"
        elif 801<= weather_id<= 804:
            return "☁️"
        else:
            return " "
        
    def setBackground(self, weather_id):
        if 200 <= weather_id <= 232:      
            bg = "background-color: darkgray;"
        elif 300 <= weather_id <= 321:    
            bg = "background-color: lightslategray;"
        elif 500 <= weather_id <= 531:   
            bg = "background-color: skyblue;"
        elif 600 <= weather_id <= 622:   
            bg = "background-color: snow;"
        elif 701 <= weather_id <= 741:   
            bg = "background-color: silver;"
        elif weather_id == 800:        
            bg = "background-color: lightblue;"
        elif 801 <= weather_id <= 804:  
            bg = "background-color: lightgray;"
        else:
            bg = "background-color: white;"

        self.setStyleSheet(self.base_style + f"QWidget {{ {bg} }}")

if __name__=="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())