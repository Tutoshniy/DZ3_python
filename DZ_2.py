# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
WORDS = 10
text = "КЛЮВ И ПЕРО С земли ааракокры выглядят как большие птицы. Только когда они спускаются на свои насесты на ветвях или ходят по земле, раскрывается их гуманоидный облик. Стоя прямо, ааракокра может достигать 5 футов высотой. У них длинные, тонкие ноги, заканчивающиеся острыми когтями. Их тела покрыты перьями. Цвет их оперения обычно означает положение в племени. У мужчин перья ярко выкрашены в красный, оранжевый или жёлтый цвета. У женщин же цвета более приглушённые, как правило, это коричневый или серый. Их птичьи головы внешне напоминают гибрид попугая и орла с вариациями, характерными для разных племён." \
       "ХРАНИТЕЛИ НЕБА" \
       "Наиболее комфортно ааракокры чувствуют себя в небе. Они могут проводить часы в воздухе, а некоторые даже и дни, расправляя крылья и позволяя восходящим потокам тёплого воздуха держать их в небесах. В сражении они показывают все свои способности динамики и акробатики, двигаясь с невероятной скоростью и изяществом, набрасываясь с оружием или выставленными вперёд когтями на противника, а затем отлетая обратно. " \
       "Однажды летавший ааракокра оставляет небо с неохотой. На своём родном плане они могут летать в течение нескольких дней или даже месяцев, приземляясь только чтобы отложить яйца и накормить своих птенцов, после чего отправляются обратно в небеса. Попавшие на Материальный План считают это место странным." \
       "Они иногда забывают или просто игнорируют вертикальные расстояния, а к народам, вынужденным жить и трудиться на земле, они не испытывают ничего кроме жалости." \
       "ПТИЧЬИ ОСОБЕННОСТИ" \
       "Сходство ааракокр и птиц не ограничивается лишь физическим. Многие ааракокры имеют манеру поведения как у самых обычных птиц. Они скрупулёзно ухаживают за своими перьями, чистят их и вычёсывают «пассажиров», которых могли подхватить. Когда они всё-таки спускаются с небес, то предпочитают делать это рядом с водоёмами, где они могут ловить рыбу и купаться сами." \
       "Многие ааракокры добавляют в свою речь щебет, чтобы акцентировать внимание на том, что у сказанного может быть и другой смысл, так же как человек сделал бы это при помощи мимики и жестов. Ааракокра может расстроиться, если собеседник не в состоянии понять эти нюансы; например, угроза может быть воспринята как насмешка, и наоборот." \
       "Идя владения чем-либо озадачивает большинство ааракокр. Разве может кто-то владеть небом? Даже когда им объясняют, они первоначально полагают, что собственность — это нечто мистическое. В результате у ааракокр, которые мало взаимодействуют с другими народами, могут быть неприятности, когда они спускаются с неба, чтобы забрать домашний скот, фрукты или зерно. Блестящие сверкающие объекты привлекают их взгляд. Им очень трудно не воровать подобные сокровища, так как считают, что они отлично подходят для украшения жилища. Ааракокры, которые проводят годы среди других рас, могут научиться подавлять эти порывы." \
       "Заключение пугает ааракокр. Не иметь возможности летать, быть в ловушке под землёй или в ледяной тюрьме — это пытка, которую не каждый ааракокра может выдержать. Даже сидя на высоких ветвях или отдыхая в своих домах на вершине горы, они всегда настороже с бегающими глазами и телами, готовыми взлететь." \
       "МЕСТА ОБИТАНИ" \
       "Большинство ааракокр живёт на Стихийном Плане Воздуха. Ааракокры могут оказаться на Материальном Плане, преследуя врагов или пытаясь помешать их планам на той стороне. Несчастный случай может перенести гнездо ааракокр на другой план. Некоторые проникают в этот мир через порталы на своём собственном плане, после чего гнездятся в высоких горах или под пологом старых лесов." \
       "После того, как племя ааракокр поселится в районе, они разделяют охотничьи угодья, площадь которых может достигать до 100 миль в поперечнике, и начинают охотиться в землях возле своей колонии, продвигаясь дальше, когда ресурсов становится недостаточно." \
       "Типичная колония состоит из одного большого гнезда без крыши, сплетённого из ветвей. Старейшина, при поддержке шамана, выступает в качестве лидера."
text_list = text.lower().replace(",", "").replace(".", "").split()
final_list = {}
for word in text_list:
    if word not in final_list:
        final_list.update(dict([(word, text_list.count(word))]))
        print(final_list[word])
for i, word in enumerate(sorted(final_list, key=final_list.get, reverse=True)[:10]):
    print(f'{i+1}: {word} {final_list[word]}')



