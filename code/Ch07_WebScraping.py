import pandas as pd
import seaborn as sns
import os.path
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np
import os

# download data
# be careful to hit webpage too many time and get locked out~
url = "https://www.pro-football-reference.com/years/2022/draft.htm"

chap_7_2022_py_file = "chap_7_2022_py_file.csv"

if os.path.isfile(chap_7_2022_py_file):
    draft_py = pd.read_csv(chap_7_2022_py_file)
else:
    draft_py = pd.read_html(url, header=1)[0]
    draft_py.to_csv(chap_7_2022_py_file)


draft_py.loc[draft_py["DrAV"].isnull(), "DrAV"] = 0

print(draft_py)

draft_py[["Rnd", "Pick", "Tm", "Sk", "College/Univ", "Unnamed: 28"]]

# loop over multiple years

chap_7_all_py_file = "chap_7_all_py_file.csv"

if os.path.isfile(chap_7_all_py_file):
    draft_py = pd.read_csv(chap_7_all_py_file)
else:
    draft_py = pd.DataFrame()
    for i in range(2000, 2022 + 1):
        url = "https://www.pro-football-reference.com/years/" + \
            str(i) + "/draft.htm"
        web_data = pd.read_html(url, header=1)[0]
        web_data["Season"] = i
        web_data = web_data.query('Tm != "Tm"')
        draft_py = pd.concat([draft_py, web_data])
    draft_py.to_csv(chap_7_all_py_file)

draft_py.reset_index(drop=True, inplace=True)

# rename teams
# the Chargers moved to Los Angeles from San Diego
# the Raiders moved from Oakland to Las Vegas
# the Rams moved from St. Louis to Los Angeles

conditions = [
    (draft_py.Tm == "SDG"),
    (draft_py.Tm == "OAK"),
    (draft_py.Tm == "STL"),
]
choices = ["LAC", "LVR", "LAR"]
draft_py["Tm"] = np.select(conditions, choices, default=draft_py.Tm)

# replace missing DrAV with 0
draft_py.loc[draft_py["DrAV"].isnull(), "DrAV"] = 0
draft_py.to_csv("data_py.csv", index=False)

print(draft_py.head())

print(draft_py.columns)

# only look at select columns of interest
draft_py_use = draft_py[["Season", "Pick",
                         "Tm", "Player", "Pos", "wAV", "DrAV"]]

print(draft_py_use)

# Plot for DrAV
# Change theme for chapter
sns.set_theme(style="whitegrid", palette="colorblind")

draft_py_use_pre2019 = draft_py_use.query("Season <= 2019")

# format columns as numeric or integers
draft_py_use_pre2019 = draft_py_use_pre2019.astype(
    {"Pick": int, "DrAV": float})
