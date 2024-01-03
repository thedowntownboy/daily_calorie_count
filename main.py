from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, FloatField, validators

from weather import WeatherLocation

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class CaloriePage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template("calorie_page.html", cform=calorie_form)

    def post(self):
        calorieform = CalorieForm(request.form)
        weight = calorieform.weight.data
        height = calorieform.height.data
        age = calorieform.age.data
        city = calorieform.city.data
        country = calorieform.country.data

        calorie = CalorieConsumption(city, country)
        temp = calorie.Temperature()
        calcalories = calorie.calcutale(weight, height, age)
        return render_template("calorie_page.html", result=True,
                               cform=calorieform,
                               your_calorie=calcalories, city=city,
                               country=country, temperature=temp)


class CalorieForm(Form):
    weight = FloatField("Weight (kg):")
    height = FloatField("Height (cm):")
    age = FloatField("Age :")

    city = StringField("City :")
    country = StringField("Country :")
    button = SubmitField("Calculate")


class CalorieConsumption(WeatherLocation):

    def calcutale(self, weight, height, age):
        bmr = 10 * weight + 6.5 * height + 5 * age - 5 - self.Temperature()
        return bmr


app.add_url_rule('/', view_func=HomePage.as_view("home_page"))
app.add_url_rule('/calories_page',
                 view_func=CaloriePage.as_view("calories_page"))
app.run()
