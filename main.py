# импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

# импортируем объект класса Flask
app = Flask(__name__)

# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
# создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
    weather = None
    news = None
    # формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.
    if request.method == 'POST':
        # этот определенный город мы будем брать для запроса API
        city = request.form['city']
        # вызовем функцию для получения погоды
        weather = get_weather(city)
        news = get_news()
    return render_template("index.html", weather=weather, news=news)

# в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
    api_key = "your_api_key"
    # Адрес, по котором мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    return response.json()

def get_news():
   api_key = "your_api_key"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])


if __name__ == '__main__':
    app.run(debug=True)