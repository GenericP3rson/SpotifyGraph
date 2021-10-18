
import pandas as pd 

alternative = pd.read_csv("data/alternative_music_data.csv")
indie_alt = pd.read_csv("data/indie_alt_music_data.csv")
rock = pd.read_csv("data/rock_music_data.csv")
blues = pd.read_csv("data/blues_music_data.csv")
metal = pd.read_csv("data/metal_music_data.csv")
hiphop = pd.read_csv("data/hiphop_music_data.csv")
pop = pd.read_csv("data/pop_music_data.csv")

alternative["Genre"] = ["Alternative" for i in alternative["Track Name"]]
indie_alt["Genre"] = ["Indie Alt" for i in indie_alt["Track Name"]]
rock["Genre"] = ["Rock" for i in rock["Track Name"]]
blues["Genre"] = ["Blues" for i in blues["Track Name"]]
metal["Genre"] = ["Metal" for i in metal["Track Name"]]
hiphop["Genre"] = ["HipHop" for i in hiphop["Track Name"]]
pop["Genre"] = ["Pop" for i in pop["Track Name"]]
