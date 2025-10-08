from environs import env
import requests


def main():
    env.read_env()

    params = {
    'api_key' : env("HOLIDAYS_API_KEY"),
    'country' : 'US',
    'year' : 2025
    }

    months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]

    holidays_url = 'https://calendarific.com/api/v2/holidays?'

    response = requests.get(holidays_url, params=params)
    response.raise_for_status()

    holidays = response.json()['response']['holidays']
    for holiday in holidays:
        month_of_holiday = int(holiday['date']['datetime']['month']) - 1
        day_of_holiday = holiday['date']['datetime']['day']
        print(f'''Дата : {day_of_holiday} {months[month_of_holiday]}
Название: {holiday['name']}
Описание: {holiday['description']}
''')


if __name__ == '__main__':
    main()