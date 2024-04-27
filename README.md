
# Learn English Easily - проект Web

Сайт представляет собой бесплатный сервис для обучения английскому языку и прохождения тестов.

## Функционал

Незарегистрированные пользователи могут:

- Зарегистрироватья
- Просматривать содержимое учебника

Зарегистрированные пользователи со статусом 1 дополнительно могут:

- Проходить тесты
- Просматривать результаты пройденных тестов

Учителя со статусом 2 дополнительно:

- Создавать различные тесты

## Содержимое архива

- readme.md - этот файл
- requirements.txt - список подключаемых модулей
- server.py - главный запускаемый файл программы
- data - каталог с файлами описания классов orm-моделей
- db - каталог с базой данных english.db, которая содержит таблицы:
  - users - зарегистрированные пользователи
  - tests - список тестов
  - results - результаты прохождений тестов пользователями
- forms - каталог с файлами описания классов форм
- static - каталог со статическим контентом:
  - css - таблицы стилей bootstrap
  - icons - иконки bootstrap
  - js - JavaScript файлы bootstrap
- templates - каталог с шаблонами html
- ТЗ - файл с описанием технического задания

## Сборка и запуск программы

Перед запуском программы необходимо установить модули, перечисленные в файле requirements.txt.

Логин и пароль для учительского аккаунта: first_teacher@email.com, 1111

Логин и пароль для учебного аккаунта: first_student@email.com, 2222

Запускать нужно файл **server.py**. 

Затем в браузере перейти по адресу: http://127.0.0.1:5000

Или же можно перейти по ссылке ... где можно пользоваться сайтом.
