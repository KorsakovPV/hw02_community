# backend_community_homework
hw02_community

[![hw_python_oop-app workflow](https://github.com/KorsakovPV/hw02_community/workflows/hw02_community/badge.svg)](https://github.com/KorsakovPV/hw02_community/actions)

Учебный проект на Django

## Техническое задание.
Ваша задача — создать сообщества для публикаций. Дайте блогеру возможность опубликовать пост не только у себя в ленте, но и выбрать группу, в которой появится этот пост. Сообщества создаются администрацией сайта, посетители не смогут их добавлять. При публикации записи автор может выбрать одно сообщество и отправить туда свой пост.
Сообщество должно иметь следующие свойства:

1. Имя (title).
2. Адрес (slug) — уникальный адрес группы, часть URL (например, для группы любителей котиков slug будет равен cats: group/cats).
3. Описание (description) — текст, который появится на странице сообщества.

## Технологии
Код приложения написан на **[Python](https://www.python.org/)**. Фреймворк **[Django](https://www.djangoproject.com/)**.

## Подготовка к работе:

Клонируйте репозиторий на локальную машину.

    git clone https://github.com/KorsakovPV/hw02_community

Создайте виртуальное окружение и запустите его.

    python3 -m venv venv 

    source venv/bin/activate

Установите необходимые пакеты

    pip install -r requirements.txt

Создайте пользователя с правами администратора

    python manage.py createsuperuser

Запустите проект

    python manage.py runserver 

В браузере откройте ссылку

    http://127.0.0.1:8000/

Для доступа на страницу администратора используйте

    http://127.0.0.1:8000/admin

## Над проектом работал:
**[Павел Корсаков](https://github.com/KorsakovPV)**.
