import requests
import json

# Отправляем GET-запрос к API
response = requests.get('https://quotes.toscrape.com/api/quotes')

# Проверяем статус ответа
if response.status_code == 200:
    try:
        json_data = response.json()  # Преобразуем ответ в JSON

        # Сохраняем данные в JSON-файл
        with open('quotes.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False,
                      indent=4)  # Запись в файл с отступами для удобства чтения

        print("Данные успешно сохранены в 'quotes.json'")
    except ValueError as e:
        print("Ошибка при декодировании JSON:", e)
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
