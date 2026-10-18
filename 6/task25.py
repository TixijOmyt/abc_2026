# 11/10/2026
# Matsenko Artemii
# task25

#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

# Добавил необходимые изменения в файл game.py в папке pole-chudes-db
# Теперь перед началом необходимо запустить mongodb
# (предварительно перейти в папку проекта)
""" Данные строчки можно полностью скопировать и вставить в командную строку
    если PyCharm на Windows: """
docker run -d `
--name mongodb-chudes `
-p 27017:27017 `
-v mongodb_chudes_data:/data/db `
-e MONGO_INITDB_ROOT_USERNAME=student `
-e MONGO_INITDB_ROOT_PASSWORD=student123 `
mongo:7.0

""" если PyCharm на Linux: """
docker run -d \
--name mongodb-chudes \
-p 27017:27017 \
-v mongodb_chudes_data:/data/db \
-e MONGO_INITDB_ROOT_USERNAME=student \
-e MONGO_INITDB_ROOT_PASSWORD=student123 \
mongo:7.0

# Далее запускаем файл с нашим словарем add_words.py
python add_words.py
# Слова автоматически добавятся

# После этого нужно запустить файл игры
python game.py