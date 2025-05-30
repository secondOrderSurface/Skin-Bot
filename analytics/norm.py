import pandas as pd

df = pd.read_csv(r"Result\Table\skin_1.csv")
df1 = pd.DataFrame(columns = ['id', 'gun_id', 'sticker1_id', 'sticker2_id', 'sticker3_id', 'sticker4_id', 'price'])
lenth = len(df)
for i in range (lenth):
    s = df['sticker_id'].loc[df.index[i]]
    l = len(s)
    s = s[10:l]
    Sticks = s.split(", ")
    num = len(Sticks)
    if num == 1:
        new_row = {
            'id' : df['gun_id'].loc[df.index[i]] + df['sticker_id'].loc[df.index[i]] + str(i),
            'gun_id' : df['gun_id'].loc[df.index[i]],
            'sticker1_id' : 'Наклейка | ' + Sticks[0],
            'price' : df['price'].loc[df.index[i]]
        }
    if num == 2:
        new_row = {
            'id' : df['gun_id'].loc[df.index[i]] + df['sticker_id'].loc[df.index[i]] + str(i),
            'gun_id' : df['gun_id'].loc[df.index[i]],
            'sticker1_id' : 'Наклейка | ' + Sticks[0],
            'sticker2_id' : 'Наклейка | ' + Sticks[1],
            'price' : df['price'].loc[df.index[i]]
        }
    if num == 3:
        new_row = {
            'id' : df['gun_id'].loc[df.index[i]] + df['sticker_id'].loc[df.index[i]] + str(i),
            'gun_id' : df['gun_id'].loc[df.index[i]],
            'sticker1_id' : 'Наклейка | ' + Sticks[0],
            'sticker2_id' : 'Наклейка | ' + Sticks[1],
            'sticker3_id' : 'Наклейка | ' + Sticks[2],
            'price' : df['price'].loc[df.index[i]]
        }
    if num == 4:
        new_row = {
            'id' : df['gun_id'].loc[df.index[i]] + df['sticker_id'].loc[df.index[i]] + str(i),
            'gun_id' : df['gun_id'].loc[df.index[i]],
            'sticker1_id' : 'Наклейка | ' + Sticks[0],
            'sticker2_id' : 'Наклейка | ' + Sticks[1],
            'sticker3_id' : 'Наклейка | ' + Sticks[2],
            'sticker4_id' : 'Наклейка | ' + Sticks[3],
            'price' : df['price'].loc[df.index[i]]
        }
    df1 = df1.append(new_row, ignore_index=True)
df1.to_csv(r"Result\Table\Steam_Market_1.csv") 


