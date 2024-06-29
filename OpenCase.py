import os
import random
import time

beginnerCase = '''60 патронов 4.6мм
60 патронов .45 АСР
60 патронов .308 Винчестер
60 патронов 9х19 Парабеллум
60 патронов 5.7мм
60 патронов 5.8мм
60 патронов 7.62х39мм
60 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
3 железа
7 железа
15 железа
20 железа
32 железа
1 золото
2 золота
64 стейка'''.split("\n")

expCase = '''120 патронов 4.6мм
120 патронов .45 АСР
120 патронов .308 Винчестер
120 патронов 9х19 Парабеллум
120 патронов 5.7мм
120 патронов 5.8мм
120 патронов 7.62х39мм
120 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
8 железа
16 железа
25 железа
32 железа
1 золото
3 золота
Glock 17
TEC-9
CZ-75 Auto
Glock 18
128 стейков'''.split("\n")

proCase = '''240 патронов 4.6мм
240 патронов .45 АСР
240 патронов .308 Винчестер
240 патронов 9х19 Парабеллум
240 патронов 5.7мм
240 патронов 5.8мм
240 патронов 7.62х39мм
240 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
Glock 17
TEC-9
CZ-75 Auto
Glock 18
Beretta M93R
Beretta M92FS
Mauser C96
CZ-75
Ф1
M67
Flash Grenade
IFG
64 золотой моркови
Зелье скорости
Зелье прыгучести
Зелье регенерации
Зелье силы
64 стейка
128 стейков
16 железа
32 железа
48 железа
2 золота
3 золота
5 золота
Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"'''.split("\n")

veteranCase = '''480 патронов 4.6мм
480 патронов .45 АСР
480 патронов .308 Винчестер
480 патронов 9х19 Парабеллум
480 патронов 5.7мм
480 патронов 5.8мм
480 патронов 7.62х39мм
480 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
Glock 17
TEC-9
CZ-75 Auto
Glock 18
Beretta M93R
Beretta M92FS
Mauser C96
CZ-75
Ф1
M67
Flash Grenade
IFG
64 золотой моркови
Зелье скорости
Зелье прыгучести
Зелье регенерации
Зелье силы
FN FAL
M1A1 Thompson
ДП-28
РПК
M249
STI P45
M1911A1
HK Mk23
64 стейка
128 стейков
Зелье стремительности
20 железа
32 железа
48 железа
64 железа
3 золота
5 золота
7 золота
Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"'''.split("\n")

masterCase = '''960 патронов 4.6мм
960 патронов .45 АСР
960 патронов .308 Винчестер
960 патронов 9х19 Парабеллум
960 патронов 5.7мм
960 патронов 5.8мм
960 патронов 7.62х39мм
960 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
Glock 17
TEC-9
CZ-75 Auto
Glock 18
Beretta M93R
Beretta M92FS
Mauser C96
CZ-75
Ф1
M67
Flash Grenade
IFG
64 золотой моркови
Зелье скорости
Зелье прыгучести
Зелье регенерации
Зелье силы
FN FAL
M1A1 Thompson
ДП-28
РПК
M249
STI P45
M1911A1
HK Mk23
64 стейка
128 стейков
Зелье стремительности
Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"
M60
AWM
M24
Mk14 EBR
Desert Eagle
Colt Python
.50Gi
AA-12
32 железа
48 железа
64 железа
80 железа
5 золота
7 золота
10 золота'''.split("\n")

legendCase = '''1920 патронов 4.6мм
1920 патронов .45 АСР
1920 патронов .308 Винчестер
1920 патронов 9х19 Парабеллум
1920 патронов 5.7мм
1920 патронов 5.8мм
1920 патронов 7.62х39мм
1920 патронов 6.8мм
Шлем из дерна
Шлем из грязи
Шлем из подзола
Нагрудник из дерна
Нагрудник из грязи
Нагрудник из подзола
Штаны из дерна
Штаны из грязи
Штаны из подзола
Ботинки из дерна
Ботинки из грязи
Ботинки из подзола
Шлем из листвы
Нагрудник из листвы
Штаны из листвы
Ботинки из листвы
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
Glock 17
TEC-9
CZ-75 Auto
Glock 18
Beretta M93R
Beretta M92FS
Mauser C96
CZ-75
Ф1
M67
Flash Grenade
IFG
64 золотой моркови
Зелье скорости
Зелье прыгучести
Зелье регенерации
Зелье силы
FN FAL
M1A1 Thompson
ДП-28
РПК
M249
STI P45
M1911A1
HK Mk23
64 стейка
128 стейков
Зелье стремительности
Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"
M60
AWM
M24
Mk14 EBR
Desert Eagle
Colt Python
.50Gi
AA-12
Barrett M82A3
M134
Шлем из плачущего обсидиана
Нагрудник из плачущего обсидиана
Штаны из плачущего обсидиана
Ботинки из плачущего обсидиана
Шлем из бедрока
Нагрудник из бедрока
Штаны из бедрока
Ботинки из бедрока
48 железа
64 железа
128 железа
10 золота
15 золота
20 золота'''.split("\n")

seasonCase = '''240 патронов 4.6мм
240 патронов .45 АСР
240 патронов .308 Винчестер
240 патронов 9х19 Парабеллум
240 патронов 5.7мм
240 патронов 5.8мм
240 патронов 7.62х39мм
240 патронов 6.8мм
Шлем из дерна
Нагрудник из дерна
Штаны из дерна
Ботинки из дерна
Койф
Кольчуга
Кольчужные штаны
Кольчужные ботинки
Glock 17
TEC-9
CZ-75 Auto
Glock 18
Ф1
M67
Flash Grenade
IFG
Зелье скорости
Зелье прыгучести
Зелье регенерации
Зелье силы
Зелье стремительности
Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"
FN FAL
M1A1 Thompson
ДП-28
РПК
M249
Шлем из плачущего обсидиана
Нагрудник из плачущего обсидиана
Штаны из плачущего обсидиана
Ботинки из плачущего обсидиана
Шлем из бедрока
Нагрудник из бедрока
Штаны из бедрока
Ботинки из бедрока
Mk14 EBR
Desert Eagle
32 стейка
64 стейка
128 стейков
32 золотой моркови
64 золотой моркови
128 золотой моркови
1 железо
3 железа
5 железа
7 железа
10 железа
16 железа
32 железа
64 железа
128 железа
1 золото
2 золота
3 золота
5 золота
7 золота
10 золота
15 золота
20 золота
32 золота'''.split("\n")

bulletCase = '''60 патронов .357 Магнум
60 патронов 4.6мм
60 патронов .45 АСР
60 патронов .50 АЕ
60 патронов .30-30 Винчестер
60 патронов .308 Винчестер
60 патронов 5.56х45мм
60 патронов 9х19 Парабеллум
60 патронов 12мм
60 патронов 5.8мм
60 патронов 7.62х54мм
60 патронов 7.62х39мм
60 патронов .50 BMG
60 патронов .338 Лапуа
60 патронов 6.8мм
60 патронов 5.7мм
120 патронов .357 Магнум
120 патронов 4.6мм
120 патронов .45 АСР
120 патронов .50 АЕ
120 патронов .30-30 Винчестер
120 патронов .308 Винчестер
120 патронов 5.56х45мм
120 патронов 9х19 Парабеллум
120 патронов 12мм
120 патронов 5.8мм
120 патронов 7.62х54мм
120 патронов 7.62х39мм
120 патронов .50 BMG
120 патронов .338 Лапуа
120 патронов 6.8мм
120 патронов 5.7мм
240 патронов .357 Магнум
240 патронов 4.6мм
240 патронов .45 АСР
240 патронов .50 АЕ
240 патронов .30-30 Винчестер
240 патронов .308 Винчестер
240 патронов 5.56х45мм
240 патронов 9х19 Парабеллум
240 патронов 12мм
240 патронов 5.8мм
240 патронов 7.62х54мм
240 патронов 7.62х39мм
240 патронов .50 BMG
240 патронов .338 Лапуа
240 патронов 6.8мм
240 патронов 5.7мм
480 патронов .357 Магнум
480 патронов 4.6мм
480 патронов .45 АСР
480 патронов .50 АЕ
480 патронов .30-30 Винчестер
480 патронов .308 Винчестер
480 патронов 5.56х45мм
480 патронов 9х19 Парабеллум
480 патронов 12мм
480 патронов 5.8мм
480 патронов 7.62х54мм
480 патронов 7.62х39мм
480 патронов .50 BMG
480 патронов .338 Лапуа
480 патронов 6.8мм
480 патронов 5.7мм
960 патронов .357 Магнум
960 патронов 4.6мм
960 патронов .45 АСР
960 патронов .50 АЕ
960 патронов .30-30 Винчестер
960 патронов .308 Винчестер
960 патронов 5.56х45мм
960 патронов 9х19 Парабеллум
960 патронов 12мм
960 патронов 5.8мм
960 патронов 7.62х54мм
960 патронов 7.62х39мм
960 патронов .50 BMG
960 патронов .338 Лапуа
960 патронов 6.8мм
960 патронов 5.7мм
1920 патронов .357 Магнум
1920 патронов 4.6мм
1920 патронов .45 АСР
1920 патронов .50 АЕ
1920 патронов .30-30 Винчестер
1920 патронов .308 Винчестер
1920 патронов 5.56х45мм
1920 патронов 9х19 Парабеллум
1920 патронов 12мм
1920 патронов 5.8мм
1920 патронов 7.62х54мм
1920 патронов 7.62х39мм
1920 патронов .50 BMG
1920 патронов .338 Лапуа
1920 патронов 6.8мм
1920 патронов 5.7мм'''.split("\n")

kitsCase = '''Прицел Coyote Optic
Прицел Aimpoint T2
Прицел Aimpoint T1
Прицел Eotech 553
Прицел Vortex UH 1
Прицел Eotech E-XPS3
Прицел Aimpoint SRS RD
Прицел Trijcon ACOG
Прицел QMK152
Прицел ELCAN SpecterDR
Прицел Vortex LPVO
Прицел MX610
Старый длинный прицел
Старый короткий прицел
Прицел Trijcon RMR
Прицел Trijcon SRO
Глушитель
Дульный тормоз
Дульный компенсатор
Пистолетный глушитель
Легкая ложа
Тактическая ложа
Утяжеленная ложа
Легкая рукоять
Специальная рукоять
Пистолетный лазерный девайс
Автоматный лазерный девайс
Маленький увеличенный магазин
Средний увеличенный магазин
Большой увеличенный магазин
Модификатор "Бронебойный патрон"
Модификатор "Зажигательный патрон"
Модификатор "Экспансивный патрон"'''.split("\n")

weaponCase = '''Glock 17
TEC-9
CZ-75 Auto
Glock 18
Beretta M93R
Beretta M92FS
Mauser C96
CZ-75
FN FAL
M1A1 Thompson
ДП-28
РПК
M249
STI P45
M1911A1
HK Mk23
M60
AWM
M24
Mk14 EBR
Desert Eagle
Colt Python
.50Gi
AA-12
Barrett M82A3
M134'''.split("\n")

caseCase = '''Кейс Новичка
Кейс Опытного
Кейс Профессионала
Кейс Ветерана
Кейс Мастера
Кейс Легенды
Сезонный кейс
Кейс с патронами
Кейс с обвесами
Кейс с оружием
Кейс со скинами
2 кейса с кейсами'''.split("\n")

skinCase = '''Spent Bullet | AK-47
Spirit of Thunder | B&T Mp9
BLOCK | Glock 17
Midnight
Miku
Soil
Abyssal
Forest
Soot
Hedge
Lagoon
Misty
Lilac
Citrus
Sakura
Twilight
Martyrs
Dune
Glaciers'''.split("\n")

partCase = '''Часть Mk14 EBR #1
Часть M249 #1
Часть M82A3 #1
Часть M134 #1
Часть РПГ-7 #1
Часть M1014 #1
Часть SCAR Mk20 #1
Часть MRAD #1
Часть бедроковой брони #1
Часть Mk14 EBR #2
Часть M249 #2
Часть M82A3 #2
Часть M134 #2
Часть РПГ-7 #2
Часть M1014 #2
Часть SCAR Mk20 #2
Часть MRAD #2
Часть бедроковой брони #2
Часть Mk14 EBR #3
Часть M249 #3
Часть M82A3 #3
Часть M134 #3
Часть РПГ-7 #3
Часть M1014 #3
Часть SCAR Mk20 #3
Часть MRAD #3
Часть бедроковой брони #3
Часть M82A3 #4
Часть M134 #4
Часть РПГ-7 #4
Часть бедроковой брони #4
Часть M82A3 #5
Часть M134 #5
Часть РПГ-7 #5
Часть бедроковой брони #5
Часть M82A3 #6
Часть M134 #6
Часть РПГ-7 #6
Часть бедроковой брони #6
Часть M82A3 #7
Часть M134 #7
Часть РПГ-7 #7
Часть бедроковой брони #7
Часть M82A3 #8
Часть M134 #8
Часть РПГ-7 #8
Часть бедроковой брони #8
Часть снаряжения Ветерана
Часть снаряжения Мастера
Часть снаряжения Легенды'''.split("\n")

begCaseChance = '''5
5
5
5
5
5
5
5
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
14.5
5
3
1
0.5
0.75
0.25
10'''.split("\n")
for i in range(len(begCaseChance)):
    begCaseChance[i] = float(begCaseChance[i])

expCaseChance = '''3
3
3
3
3
3
3
3
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
1
1
1
1
10
7
5
4
3
1
1
1
1
1
12'''.split("\n")
for i in range(len(expCaseChance)):
    expCaseChance[i] = float(expCaseChance[i])

proCaseChance = '''6.25
6.25
6.25
6.25
6.25
6.25
6.25
6.25
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.35
0.9975
0.9975
0.9975
0.9975
0.97
0.97
0.97
0.97
0.97
0.97
0.97
0.97
0.75
0.75
0.75
0.75
0.15
0.25
0.25
0.25
0.25
1.5
0.75
7
5
2.75
2.5
1
0.41
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23'''.split("\n")
for i in range(len(proCaseChance)):
    proCaseChance[i] = float(proCaseChance[i])
    
vetCaseChance = '''3.60625
3.60625
3.60625
3.60625
3.60625
3.60625
3.60625
3.60625
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
0.75
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
0.25
1.5
1.5
1.5
1.5
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
1
0.5
1
7
5
4
3
2
1
0.41
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23'''.split("\n")
for i in range(len(vetCaseChance)):
    vetCaseChance[i] = float(vetCaseChance[i])
    
mastCaseChance = '''2.69375
2.69375
2.69375
2.69375
2.69375
2.69375
2.69375
2.69375
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
0.95
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1.5
1
1
1
1
0.75
2.5
2.5
2.5
2.5
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
3
1.5
2
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.01
0.01
0.01
0.01
0.01
0.01
0.01
0.01
5
4
3
2
1.1
0.5
0.33'''.split("\n")
for i in range(len(mastCaseChance)):
    mastCaseChance[i] = float(mastCaseChance[i])
    
legCaseChance = '''3
3
3
3
3
3
3
3
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
2
2
2
2
2
2
2
2
2
2
1
1
1
1
0.7
2
2
2
2
0.1
0.1
0.1
0.1
0.1
0.1
0.1
0.1
2.6
1.3
3
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.05
0.01
0.01
0.01
0.01
0.01
0.01
0.005
0.005
0.005
0.005
3
2.4
1.2
0.6
0.2
0.13'''.split("\n")
for i in range(len(legCaseChance)):
    legCaseChance[i] = float(legCaseChance[i])
    
seasCaseChance = '''1.625
1.625
1.625
1.625
1.625
1.625
1.625
1.625
0.75
0.75
0.75
0.75
0.5
0.5
0.5
0.5
0.5
0.5
0.5
0.5
1.6125
1.6125
1.6125
1.6125
2
2
2
2
1
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.23
0.1
0.1
0.1
0.1
0.1
0.01
0.01
0.01
0.01
0.005
0.005
0.005
0.005
0.05
0.05
5.2
2.6
1.3
1.4
0.7
0.35
5
4.75
4.5
4
3.5
3
2.5
2
1.75
4.75
3
2.25
1.75
1
0.6
0.2
0.13
0.07'''.split("\n")
for i in range(len(seasCaseChance)):
    seasCaseChance[i] = float(seasCaseChance[i])
    
bullCaseChance = '''3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
3.125
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.78125
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.390625
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.29296875
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625
0.09765625'''.split("\n")
for i in range(len(bullCaseChance)):
    bullCaseChance[i] = float(bullCaseChance[i])
    
kitCaseChance = '''3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
3
5
3
2
3
3
3'''.split("\n")
for i in range(len(kitCaseChance)):
    kitCaseChance[i] = float(kitCaseChance[i])
    
weapCaseChance = '''12.5
12.5
12.5
12.5
6.25
6.25
6.25
6.25
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.5625
1.4375
1.4375
1.4375
1.4375
1.4375
1.4375
1.4375
1.4375
0.7
0.3'''.split("\n")
for i in range(len(weapCaseChance)):
    weapCaseChance[i] = float(weapCaseChance[i])
    
caseCaseChance = '''15
13
10
7
5
3
15
10
8
1
10
3'''.split("\n")
for i in range(len(caseCaseChance)):
    caseCaseChance[i] = float(caseCaseChance[i])
    
skinCaseChance = '''7
6
7
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5'''.split("\n")
for i in range(len(skinCaseChance)):
    skinCaseChance[i] = float(skinCaseChance[i])

partCaseChance = '''2
4
2
2
2
5
4
2
2
2
4
2
2
2
5
4
2
2
2
4
2
2
2
5
4
2
2
1.5
1.5
1.5
1.5
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1'''.split("\n")
for i in range(len(partCaseChance)):
    partCaseChance[i] = float(partCaseChance[i])

def OpenCase(case, chances):
    for i in range(100):
        os.system('cls')
        print(random.choices(case, chances))
        time.sleep(0.1)

print('''1 - Кейс Новичка
2 - Кейс Опытного
3 - Кейс Профессионала
4 - Кейс Ветерана
5 - Кейс Мастера
6 - Кейс Легенды
7 - Сезонный кейс
8 - Кейс с патронами
9 - Кейс с обвесами
10 - Кейс с оружием
11 - Кейс с кейсами
12 - Кейс со скинами
13 - Кейс с частями снаряжения
      
      
      ''')
caseChoice = input()
while caseChoice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
    print("Число, сэр...")
    caseChoice = input()
caseChoice = int(caseChoice)

if caseChoice == 1:
    OpenCase(beginnerCase, begCaseChance)
elif caseChoice == 2:
    OpenCase(expCase, expCaseChance)
elif caseChoice == 3:
    OpenCase(proCase, proCaseChance)
elif caseChoice == 4:
    OpenCase(veteranCase, vetCaseChance)
elif caseChoice == 5:
    OpenCase(masterCase, mastCaseChance)
elif caseChoice == 6:
    OpenCase(legendCase, legCaseChance)
elif caseChoice == 7:
    OpenCase(seasonCase, seasCaseChance)
elif caseChoice == 8:
    OpenCase(bulletCase, bullCaseChance)
elif caseChoice == 9:
    OpenCase(kitsCase, kitCaseChance)
elif caseChoice == 10:
    OpenCase(weaponCase, weapCaseChance)
elif caseChoice == 11:
    OpenCase(caseCase, caseCaseChance)
elif caseChoice == 13:
    OpenCase(partCase, partCaseChance)
else:
    OpenCase(skinCase, skinCaseChance)
