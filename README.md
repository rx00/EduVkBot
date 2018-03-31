# EduOzsh VK bot
Код бота не претендует на красоту архитектуры и элегантность решений и является исключительно образовательным и демонстрационным проектом для участников ОЗШ, написанным за пару часиков:3  
Бот умеет отвечать на сообщения, будучи активным. Все сообщения во время неактивности им игнорируются.  
(бот раз в секунду тянет сообщения через messages.get, polling и callback api могут оказаться достаточно сложными для школьников :( ))

### Системные требования

- Python 3.5 +
- Библиотека vk  
Установка: `pip3.5 install vk`  
(или) `pip3 install vk`  
(или) `pip install vk`  
(или установка непосредственно из обращения к модулю pip в параметрах командной строки интерпретатора (`python.exe -m pip install vk`))

### Предварительная настройка

- Создать группу и получить ключ доступа сообщества (подробнее [тут в третьем пункте](https://vk.com/dev/access_token?f=2.%20%D0%9A%D0%BB%D1%8E%D1%87%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0))
- Заменить подстроку `## ваш токен ##` в файле `main.py` в 6 строке на полученный Вами токен
- Новые ответы на сообщения можно описывать в файле `handlers.py`, иную логику лучше описывать при полном понимании кода в остальных файлах

 Документация и прочая информация (прим: об ограничениях API) [тут](https://vk.com/dev/)

### Запуск

`python3.5 main.py`


