import pandas as pd

songs={'Album':['Reputation','Rare','The Bodyguard'],
       'Released':[2019,2018,1992],
       "Length":['1:00:25','00:50:55','00:57:44']}
songs_frame=pd.DataFrame(songs)
print(songs_frame.iloc[0,1]) # First row, Second Column.
print(songs_frame)
