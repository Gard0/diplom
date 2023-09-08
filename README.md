# Автотест

Этот проект содержит автоматизированные тесты для дипломного проекта.

## Подготовка и запуск теста

1. Установите среду разработки - PyCharm Community Edition.
2. Перенесите все файлы из архива в новый проект.
3. Установите Python и pip через PowerShell (запустить PowerShell от имени Администратора) либо через Терминал в IDE
   PyCharm Community Edition.
4. Установите необходимые пакеты:
   `pip install pip`,
   `pip install pytest`,
   `pip install requests`,
   `python.exe -m pip install --upgrade pip`.
5. Получить актуальный "Адрес стенда" и вставить <url запущенного сервера> в `Configuration.py`
6. Запустите тесты в файле нажатием кнопки:`Run`
   либо командой в терминале IDE:` pytest order_test.py`

## Описание файлов

- `configuration.py`: Содержит базовый URL (адрес стенда) и конечные.
- `data.py`: Содержит тело запроса.
- `sender_stand_request.py`: Содержит функции для отправки запросов к приложению.
- `order_test.py`: Содержит тест.
- `.gitignore`: Содержит файлы и директории, игнорируемые Git.
