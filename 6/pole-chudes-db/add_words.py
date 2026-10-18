from db import get_collection

words = [
    {
        "word": "False",
        "description": "Логическое значение"
    },
    {
        "word": "None",
        "description": "Пустой"
    },
    {
        "word": "Python",
        "description": "Язык программирования"
    }
]

collection = get_collection()

collection.insert_many(words)

print("Слова успешно добавлены!")
