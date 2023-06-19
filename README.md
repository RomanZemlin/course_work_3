# Курсовой проект по курсу «Основы backend-разработки»
Данная программа получает из operations.json весь объем данных, отсеивает не пройденные операции по счету/карте 
клиента, далее сортирует их по дате и оставляет 5 последних операций, выводя их на экран.
## Как установить
1. Клонируйте репозиторий на локальный компьютер: git clone https://github.com/RomanZemlin/course_work_3
2. Откройте терминал в папке проекта.
3. Установите виртуальное окружение: python -m venv venv && soirce venv/bin/activate
4. Установите зависимости: pip install -r requirements.txt
## Как запустить проект
1. Активируйте виртуальное окружение: на Linux source venv/bin/activate или на Windows path/to/venv/bin/activate 
где path/to/venv путь к вашему виртуальному окружению
2. Запустите в терминале приложение: python main.py
3. Резельтат операции вы увидите в терминале
## Как запустить тесты
1. Активируйте виртуальное окружение: на Linux source venv/bin/activate или на Windows path/to/venv/bin/activate 
где path/to/venv путь к вашему виртуальному окружению
2. Запустите тесты: pytest tests
## Технологии использованные в проекте:
python
colorama
pip
pytest
pytest-cov
