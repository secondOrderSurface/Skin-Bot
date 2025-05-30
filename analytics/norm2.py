import pandas as pd

Steam_Market = pd.read_csv(r"Result\Table\Steam_Market_1.csv")
Steam_Market_ = pd.DataFrame(columns = ['id', 'gun_id', 'sticker1_id', 'sticker2_id', 'sticker3_id', 'sticker4_id', 'price'])
Sticker_Info = pd.read_csv(r"Result\Table\Sticker_Info.csv") 
Sticker_Info_ = pd.DataFrame(columns = ['sticker_id','price'])
Gun_Info = pd.read_csv(r"Result\Table\Gun_Info.csv") 
Gun_Info_ = pd.DataFrame(columns = ['gun_id','price'])

for i in range(len(Steam_Market)):
    price = Steam_Market['price'].loc[Steam_Market.index[i]]
    massive = price.split(".")
    if len(massive) == 1:
        p = float(massive[0])
    if len(massive) == 2:
        p = float(massive[0]) + float(massive[1])/100
    if len(massive) == 3:
        p = 1000 * float(massive[0]) + float(massive[1]) + float(massive[2])/100
    new_row = {
        'id' : Steam_Market['id'].loc[Steam_Market.index[i]],
        'gun_id' : Steam_Market['gun_id'].loc[Steam_Market.index[i]],
        'sticker1_id' : Steam_Market['sticker1_id'].loc[Steam_Market.index[i]],
        'sticker2_id' : Steam_Market['sticker2_id'].loc[Steam_Market.index[i]],
        'sticker3_id' : Steam_Market['sticker3_id'].loc[Steam_Market.index[i]],
        'sticker4_id' : Steam_Market['sticker4_id'].loc[Steam_Market.index[i]],
        'price' : p
    }
    Steam_Market_ = Steam_Market_.append(new_row, ignore_index=True)
Steam_Market_.drop_duplicates()
Steam_Market_.to_csv('Steam_Market.csv')

for i in range(len(Sticker_Info)):
    price = Sticker_Info['price'].loc[Sticker_Info.index[i]]
    massive = price.split(".")
    if len(massive) == 1:
        p = float(massive[0])
    if len(massive) == 2:
        p = float(massive[0]) + float(massive[1])/100
    if len(massive) == 3:
        p = 1000 * float(massive[0]) + float(massive[1]) + float(massive[2])/100
    new_row = {
        'sticker_id' : Sticker_Info['sticker_id'].loc[Sticker_Info.index[i]],
        'price' : p
    }
    Sticker_Info_ = Sticker_Info_.append(new_row, ignore_index=True)
Sticker_Info_.drop_duplicates()
Sticker_Info_.to_csv('Sticker_Info.csv')

for i in range(len(Gun_Info)):
    price = Gun_Info['price'].loc[Gun_Info.index[i]]
    massive = price.split(".")
    if len(massive) == 1:
        p = float(massive[0])
    if len(massive) == 2:
        p = float(massive[0]) + float(massive[1])/100
    if len(massive) == 3:
        p = 1000 * float(massive[0]) + float(massive[1]) + float(massive[2])/100
    new_row = {
        'sticker_id' : Gun_Info['sticker_id'].loc[Gun_Info.index[i]],
        'price' : p
    }
    Gun_Info_ = Gun_Info_.append(new_row, ignore_index=True)
Gun_Info_.drop_duplicates()
Gun_Info_.to_csv('Gun_Info.csv')