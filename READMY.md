Данный проект написан в рамках тествого задания.
Python = 3.9
selenium==4.7.2
pytest==7.2.0
Остальные зависимости можно посмотреть в файле requirements.txt

Для смены каталога chromedriver перейдите в файл config.py

### Примеры использования:
Запустить тест: ```pytest -s -v```
Запуск через Allure: ```pytest --alluredir=results```
Просмотр отчётов: ```allure serve results/```


