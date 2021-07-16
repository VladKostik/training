text = """Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так.
Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад.
Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения.
Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32!"""

import re

new_line = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z][А-Я][а-я]\.)(?<=\.|\?)\s', text)

for line in new_line:  # 5 sentences instead of 6 were e
       print(line)
       print()

# Almost right but only 5 sentences and text is not original
# it could be done with
# for item in re.findall("\S.*?[.!?](?=\s|$)", text):
#     print(item)
#     print()
# -2 points
