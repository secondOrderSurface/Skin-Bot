import time # модуль для измерения времени
import pandas as pd  # модуль для удобного обращения с таблицей данных
import prettytable as pr # модуль для создания HTML страицы с таблицей
import os # модуль для работы с файлами системы

x_next = ''
x_back = ''

k = 0 # счетчик

while True:
    data = pd.read_csv(r"Result\Result\result1.csv" , delimiter=',') 
    # чтение данных из полученной после парсинга таблицы
    data = data.iloc[k:k + 100]
    f = open('data.data' + str(int(k/100)) + '.csv', 'w+')
    data.to_csv('data.data' + str(int(k/100)) + '.csv')
    # создание csv файла с целью преобразование далее в HTML
    with open('data.data' + str(int(k/100)) + '.csv') as fp:
        data = pr.from_csv(fp)
        fp.close()
    # преобразование в таблицу нужного типа
    k += 100
    data.hrules = pr.ALL
    data.border = True
    data.vrules = pr.FRAME
    # оформление таблицы
    x_next = "<a href=" + '"data' + str(int(k/100)) + '.html"' + ">Next</a>"
    if k > 100:
        x_back = "<a href=" + '"data' + str(int(k/100 - 2)) + '.html"' + ">Back</a>"
    # переход к следующей или предыдущей страницы
    with open("pages.data" + str(int(k/100 - 1)) + ".html", 'w+') as f:
        print('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">', file=f)
        print(data.get_html_string(format=True), file=f)
        print(x_back, file=f)
        print(x_next, file=f)
        f.close()
    # создание HTML страницы
    os.remove('data.data' + str(int(k/100 - 1)) + '.csv')
    # удаление побочного csv файла
    time.sleep(3)


