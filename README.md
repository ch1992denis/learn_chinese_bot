Telegram-бот HSK Vocabulary на Python

Бот реализован с помощью pyTelegramBotAPI. 

Имеет практическое применение для пользователей, изучающих китайский язык и готовящихся к международному экзамену HSK. 

Бот предлагает на выбор изучение лексики для каждого из 6 уровней HSK, а также знакомство с примерами употребления слов. 
После выбора соотетствующего уровня бот выводит рандомные 5 слов на китайском со скрытым переводом и произношением (функция "спойлер"). Пользователь открывает скрытое значение для каждого слова, после чего может попросить новую порцию слов либо вернуться в главное меню или к выбору уровня языка.

Бот подгружает слова из 7 словарей, реализованных в файлах txt:

1) 150 слов для HSK 1

2) 300 слов для HSK 2

3) 600 слов для HSK 3

4) 1200 слов для HSK 4

5) 2500 слов для HSK 5

6) 5000 слов для HSK 6

7) более 2000 примеров предложений и словосочетаний