import pandas as pd
import numpy as np
import time

# Steam_Market       | id | gun_id | sticker1_id | sticker2_id | sticker3_id | sticker4_id | price |

# Sticker_Info       | sticker_id | price |

# Gun_Info           | gun_id | price |

Steam_Market = pd.read_csv(r"Result\Table\Steam_Market_1.csv")
Sticker_Info = pd.read_csv(r"Result\Table\Sticker_Info.csv")
Gun_Info = pd.read_csv(r"Result\Table\Gun_Info.csv")

#хз зачем, но чтоб с копиями работать, а не с самими данными
Steam_Market_copy = Steam_Market.copy(deep = True)
Sticker_Info_copy = Sticker_Info.copy(deep = True)
Gun_Info_copy = Gun_Info.copy(deep = True)

Sticker_Info_copy = Sticker_Info_copy.drop_duplicates (subset=['sticker_id'])

lenth = len(Steam_Market_copy) #длинна датафрейма

index = 0 # по этому индексу будем бежать по фрейму в цикле вайл

result = pd.DataFrame(columns = ['id', 'price', 'absolute_profit', 'percent_profit']) # создаём пустой датафрейм, в который
#будем записывать строчки с товарами, что нам подходят
t1 = time.perf_counter()
t2 = t1
#t2, t1 -- моменты времени, чтобы чекать как долго работает вайл
while ((t2 - t1) < 10) and (index < lenth):# выполняется пока не пройдёт 10 секунд или не пробежит все значения
    new_row = {'id' : np.NaN,
            'price' : np.NaN,
            'absolute_profit' : np.NaN,
            'percent_profit' : np.NaN
    }
    good_id = Steam_Market_copy['id'].loc[Steam_Market_copy.index[index]]#айдишник(любая уникальная херня товара) строки под номером 
    #index записана в эту переменную
    gun_price = float(Gun_Info_copy['price'].loc[Gun_Info_copy['gun_id'] == Steam_Market_copy['gun_id'].loc[Steam_Market_copy.index[index]]])#базовая
    #цена на соответсвующее оружие строки под номером index записана в эту переменную
    price = float(Steam_Market_copy['price'].loc[Steam_Market_copy.index[index]])#Цена сделки в строке index записана в эту переменную
    if False == (pd.isnull(Steam_Market_copy['sticker1_id'].loc[Steam_Market_copy.index[index]])):#если наклейка1 существует -- идём дальше
        stick1 = Steam_Market_copy['sticker1_id'].loc[Steam_Market_copy.index[index]]#айдишник 1-го стикера записан в эту переменную
        s = Steam_Market_copy['sticker1_id'].loc[Steam_Market_copy.index[index]]
        stick1_price_ = Sticker_Info_copy['price'].loc[Sticker_Info_copy['sticker_id'] == Steam_Market_copy['sticker1_id'].loc[Steam_Market_copy.index[index]]]
        if stick1_price_.empty:
            stick1_price = 0
        else:
            stick1_price = float(stick1_price_)
        #цена 1-го стикера записана сюда
        if False == (pd.isnull(Steam_Market_copy['sticker2_id'].loc[Steam_Market_copy.index[index]])):#если наклейка2 существует -- идём дальше
            stick2 = Steam_Market_copy['sticker2_id'].loc[Steam_Market_copy.index[index]]#айдишник 2-го стикера записан в эту переменную
            stick2_price_ = Sticker_Info_copy['price'].loc[Sticker_Info_copy['sticker_id'] == Steam_Market_copy['sticker2_id'].loc[Steam_Market_copy.index[index]]]
            if stick2_price_.empty:
                stick2_price = 0
            else:
                stick2_price = float(stick2_price_)
            #цена 2-го стикера записана сюда
            if False == (pd.isnull(Steam_Market_copy['sticker3_id'].loc[Steam_Market_copy.index[index]])):#если наклейка3 существует -- идём дальше
                stick3 = Steam_Market_copy['sticker3_id'].loc[Steam_Market_copy.index[index]]#айдишник 3-го стикера записан в эту переменную
                stick3_price_ = Sticker_Info_copy['price'].loc[Sticker_Info_copy['sticker_id'] == Steam_Market_copy['sticker3_id'].loc[Steam_Market_copy.index[index]]]
                if stick3_price_.empty:
                    stick3_price = 0
                else:
                    stick3_price = float(stick3_price_)
                #цена 3-го стикера записана сюда
                if False == (pd.isnull(Steam_Market_copy['sticker4_id'].loc[Steam_Market_copy.index[index]])):#если наклейка4 существует -- идём дальше
                    stick4 = Steam_Market_copy['sticker4_id'].loc[Steam_Market_copy.index[index]]#айдишник 4-го стикера записан в эту переменную
                    stick4_price_ = Sticker_Info_copy['price'].loc[Sticker_Info_copy['sticker_id'] == Steam_Market_copy['sticker4_id'].loc[Steam_Market_copy.index[index]]]
                    if stick4_price_.empty:
                        stick4_price = 0
                    else:
                        stick4_price = float(stick4_price_)
                    #цена 4-го стикера записана сюда
                    if (stick1 == stick2) and (stick3 == stick4) and (stick2 == stick3):#если все наклейки одинаковые
                        if price - gun_price - stick1_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - stick1_price),
                            'percent_profit' : -(price - gun_price - stick1_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    elif (stick1 == stick2) and (stick2 == stick3):#если 123 наклейки одинаковые
                        if price - gun_price - 0.5 * stick1_price - 0.05 * stick4_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.5 * stick1_price - 0.05 * stick4_price),
                            'percent_profit' : -(price - gun_price - 0.5 * stick1_price - 0.05 * stick4_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    elif (stick1 == stick2) and (stick2 == stick4):#если 124 наклейки одинаковые
                        if price - gun_price - 0.5 * stick1_price - 0.08 * stick3_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' :-(price - gun_price - 0.5 * stick1_price - 0.08 * stick3_price),
                            'percent_profit' : -(price - gun_price - 0.5 * stick1_price - 0.08 * stick3_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    elif (stick1 == stick3) and (stick3 == stick4):#если 134 наклейки одинаковые
                        if price - gun_price - 0.5 * stick1_price - 0.1 * stick2_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.5 * stick1_price - 0.1 * stick2_price),
                            'percent_profit' : -(price - gun_price - 0.5 * stick1_price - 0.1 * stick2_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    elif (stick3 == stick2) and (stick2 == stick4):#если 324 наклейки одинаковые
                        if price - gun_price - 0.5 * stick2_price - 0.12 * stick1_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.5 * stick2_price - 0.12 * stick1_price),
                            'percent_profit' : -(price - gun_price - 0.5 * stick2_price - 0.12 * stick1_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    else:# если 4 наклейки существует но без комбо
                        if (price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price - 0.05 * stick4_price) < 0:#если цена ниже справедливой
                            print(67)
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price - 0.05 * stick4_price),
                            'percent_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price - 0.05 * stick4_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                else:# если существует только три наклейки
                    if (stick1 == stick2) and (stick2 == stick3):# если это три одинаковые наклейки
                        if price - gun_price - 0.5 * stick1_price < 0:# если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.5 * stick1_price),
                            'percent_profit' : -(price - gun_price - 0.5 * stick1_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
                    else:# если 3 наклейки существует но без комбо
                        if price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price),
                            'percent_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price - 0.08 * stick3_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
            else:#если существует только 2 наклейки
                if price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price),
                            'percent_profit' : -(price - gun_price - 0.12 * stick1_price - 0.1 * stick2_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
        else:#если существует только 1 наклейка
            if price - gun_price - 0.12 * stick1_price < 0:#если цена ниже справедливой
                            new_row = {'id' : good_id,
                            'price' : price,
                            'absolute_profit' : -(price - gun_price - 0.12 * stick1_price),
                            'percent_profit' : -(price - gun_price - 0.12 * stick1_price)/price
                            }
                            result = result.append(new_row, ignore_index=True)#добавление новой строчки new_row, которую формировали во всех ифах
    t2 = time.perf_counter()#обновление таймера
    index += 1
result = result.sort_values(by='absolute_profit', ascending=False)
result.to_csv(r"Result\Result\result1.csv")

