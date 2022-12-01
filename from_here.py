from trythis import Music_Recommender
import pandas as pd
def final(name_of_song):
    dataset=pd.read_csv("data.csv")

    result=pd.DataFrame(Music_Recommender([{'name': name_of_song}],dataset))
    return (list(result["name"]))
    # for i in list(result["name"]):
    #     print(type(i))
#final("I Like Me Better")


# final("I Like Me Better")


