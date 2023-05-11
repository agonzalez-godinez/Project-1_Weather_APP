import tkinter
from tkinter import *
from datetime import datetime
import requests
import webbrowser


class GUI:
    """Gui class that holds gui frames, labels and buttons"""
    def __init__(self, window: tkinter) -> None:
        """
        Constructor to create window instance
        :param window: window object
        """
        self.window = window

        self.frame_city = Frame(self.window)
        self.label_city = Label(self.frame_city, text='Enter City: ')
        self.entry_city = Entry(self.frame_city, width=40)
        self.label_city.pack(padx=20, side='left')
        self.entry_city.pack(padx=20, side='left')
        self.frame_city.pack(anchor='w', pady=10)

        self.frame_pop_codes = Frame(self.window)
        self.label_pop_codes = Label(self.frame_pop_codes, text='Popular Country Codes Include')
        self.label_pop_codes.pack(pady=10)
        self.frame_pop_codes.pack()

        self.frame_usa = Frame(self.window)
        self.label_usa = Label(self.frame_usa, text='US/Canada: 1-855')
        self.label_usa.pack(pady=10)
        self.frame_usa.pack()

        self.frame_uk = Frame(self.window)
        self.label_uk = Label(self.frame_uk, text='UK: 44-081')
        self.label_uk.pack(pady=10)
        self.frame_uk.pack()

        self.frame_france = Frame(self.window)
        self.label_france = Label(self.frame_france, text='France: 33-009')
        self.label_france.pack(pady=10)
        self.frame_france.pack()

        self.frame_china = Frame(self.window)
        self.label_china = Label(self.frame_china, text='China: 86-999')
        self.label_china.pack(pady=10)
        self.frame_china.pack()

        self.frame_codes = Frame(self.window)
        self.label_codes = Label(self.frame_codes, text='More country codes can be found at: https://countrycode.org/', fg="blue", cursor="hand2")
        self.label_codes.pack(pady=10)
        self.label_codes.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://countrycode.org/"))
        self.frame_codes.pack()

        self.frame_country = Frame(self.window)
        self.label_country = Label(self.frame_country, text='Enter Country Code: ')
        self.entry_country = Entry(self.frame_country, width=40)
        self.label_country.pack(padx=20, side='left')
        self.entry_country.pack(padx=20, side='left')
        self.frame_country.pack(anchor='w', pady=10)

        self.frame_enter_button = Frame()
        self.label_enter_button = Button(self.frame_enter_button, text='Enter')
        self.label_enter_button.config(command=self.weather_search)
        self.label_enter_button.pack(padx=190, side=tkinter.RIGHT)
        self.frame_enter_button.pack(anchor='w', pady=10)

        # Results Label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Results 2
        self.frame_result2 = Frame(self.window)
        self.label_result2 = Label(self.frame_result2)
        self.label_result2.pack(pady=10)
        self.frame_result2.pack()

        self.frame_cc = Frame(self.window)
        self.label_cc = Label(self.frame_cc)
        self.label_cc.pack(pady=10)
        self.frame_cc.pack()

        self.frame_ctif = Frame(self.window)
        self.label_ctif = Label(self.frame_ctif)
        self.label_ctif.pack(pady=10)
        self.frame_ctif.pack()

        self.frame_cp_hpa = Frame(self.window)
        self.label_cp_hpa = Label(self.frame_cp_hpa)
        self.label_cp_hpa.pack(pady=10)
        self.frame_cp_hpa.pack()

        self.frame_humidity = Frame(self.window)
        self.label_humidity = Label(self.frame_humidity)
        self.label_humidity.pack(pady=10)
        self.frame_humidity.pack()

        self.frame_exp_low = Frame(self.window)
        self.label_exp_low = Label(self.frame_exp_low)
        self.label_exp_low.pack(pady=10)
        self.frame_exp_low.pack()

        self.frame_exp_high = Frame(self.window)
        self.label_exp_high = Label(self.frame_exp_high)
        self.label_exp_high.pack(pady=10)
        self.frame_exp_high.pack()

    def weather_search(self) -> None:
        """
        weather button search
        :return: None
        """
        self.label_pop_codes.pack_forget()
        self.frame_pop_codes.pack_forget()
        self.label_usa.pack_forget()
        self.frame_usa.pack_forget()
        self.label_uk.pack_forget()
        self.frame_uk.pack_forget()
        self.label_france.pack_forget()
        self.frame_france.pack_forget()
        self.label_china.pack_forget()
        self.frame_china.pack_forget()

        now = datetime.now()
        city = self.entry_city.get()
        country = self.entry_country.get()
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_key = 'Your key here'
        try:
            url = api_start + city + ',' + country + api_key
            json_data = requests.get(url).json()
            weather_description = json_data['weather'][0]['description']

            self.label_result.config(text='Weather Data Successfully Retrieved')
            self.label_result2.config(text=f'{now.strftime("%A,")} {now.strftime("%B")} {now.strftime("%d,")} {now.year}')
            self.label_cc.config(text=f'Current Conditions: {weather_description}')

            temp = json_data['main']['temp']
            KtoF = (temp - 273.15) * 9 / 5 + 32
            self.label_ctif.config(text=f'Current Temperature in Fahrenheit: {round(KtoF, 2)}')

            pressure = json_data['main']['pressure']
            self.label_cp_hpa.config(text=f'Current Pressure in hpa: {pressure}')

            humidity = json_data['main']['humidity']
            self.label_humidity.config(text=f'Current Humidity: {humidity}%')

            temp_min = json_data['main']['temp_min']
            lowKtoF = (temp_min - 273.15) * 9 / 5 + 32
            self.label_exp_low.config(text=f'Expected Low Temperature in Fahrenheit: {round(lowKtoF, 2)}')

            temp_max = json_data['main']['temp_max']
            highKtoF = (temp_max - 273.15) * 9 / 5 + 32
            self.label_exp_high.config(text=f'Expected High Temperature in Fahrenheit: {round(highKtoF, 2)}')
        except:
            self.label_cc.config(text='')
            self.label_ctif.config(text='')
            self.label_cp_hpa.config(text='')
            self.label_humidity.config(text='')
            self.label_exp_low.config(text='')
            self.label_exp_high.config(text='')
            self.label_result.config(text=f'Unable to access {city} in {country}')
            self.label_result2.config(text='Verify city name and country code')
