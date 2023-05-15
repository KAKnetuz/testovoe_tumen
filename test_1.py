# 1. Считываем данные из текстового файла
advertisers = {}
with open("advertisers.txt", encoding='utf-8') as file:
    for line in file:
        name, *locations = line.strip().split(":")
        advertisers[name] = locations

# 2. Обрабатываем запрос пользователя
user_query = input("Введите локацию: ").strip()
result = []
for name, locations in advertisers.items():
    for location in locations:
        if user_query in location:
            if name not in result:
                result.append(name)

# 3. Выводим результат
if result:
    print("Рекламоносители, действующие в локации", user_query + ":")
    for name in result:
        print(name)
else:
    print("Нет рекламоносителей, действующих в локации", user_query)
