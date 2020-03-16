from init_photos_service import service 
import pandas as pd 
import urllib.request


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_colwidth', 60)
pd.set_option('display.width', 120)
pd.set_option('expand_frame_repr', True)

#list method 

response = service.mediaItems().list(pageSize = 25).execute()


lst_medias = response.get('mediaItems')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.mediaItems().list(
        pageSize = 25,
        pageToken = nextPageToken
    ).execute()

    lst_medias.extend(response.get('mediaItems'))
    nextPageToken = response.get('nextPageToken') 

df_media_items = pd.DataFrame(lst_medias)


print(len(df_media_items.baseUrl))
pathname = 'C:/Users/Varun Chandra/Desktop/pics'

c = 1
for i in df_media_items.baseUrl:
    urllib.request.urlretrieve(i, pathname + '/' + 'file{}.jpg'.format(c))
    c += 1
    

