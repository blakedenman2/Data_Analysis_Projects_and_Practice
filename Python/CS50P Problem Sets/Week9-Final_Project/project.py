# New England Surf Check
# Created by Blake Denman

#                                                            ,---.
#  ,---.                  ,---.,--.          ,--. ,--.       |   |
# '   .-' ,--.,--.,--.--./  .-'|  |,---.     |  | |  | ,---. |  .'
# `.  `-. |  ||  ||  .--'|  `-,`-'(  .-'     |  | |  || .-. ||  |
# .-'    |'  ''  '|  |   |  .-'   .-'  `)    '  '-'  '| '-' '`--'
# `-----'  `----' `--'   `--'     `----'      `-----' |  |-' .--.
#                                                     `--'   '--'
# Let's check the surf conditions in New England


import pandas as pd
import numpy as np
import requests

# These are the buoys to get wave or wind (or both) data from, to use in determining conditions

# Southern Maine (44007): APD, WVHT, WDIR, WSPD, MWD -
me = "https://www.ndbc.noaa.gov/data/5day2/44007_5day.txt"
# New Hampshire (44098): APD,WVHT, MWD -
nh = "https://www.ndbc.noaa.gov/data/5day2/44098_5day.txt"
# New Hampshire Wind (44030): WDIR, WSPD -
nhw = "https://www.ndbc.noaa.gov/data/5day2/44030_5day.txt"
# North Shore (44013):APD, WVHT, WDIR, MWD -
ns = "https://www.ndbc.noaa.gov/data/5day2/44013_5day.txt"
# Cape Cod (44018):APD, WVHT, MWD -
cc = "https://www.ndbc.noaa.gov/data/5day2/44018_5day.txt"
# Nantucket Sound Wind (44020): WSPD, WDIR -
ccw = "https://www.ndbc.noaa.gov/data/5day2/44020_5day.txt"
# Rhode Island (44097):APD, WVHT, MWD -
ri = "https://www.ndbc.noaa.gov/data/5day2/44097_5day.txt"
# Buzzard's Bay Wind (BUZM3): WDIR, WSPD -
riw = "https://www.ndbc.noaa.gov/data/5day2/BUZM3_5day.txt"


def main():
    print("Let's check the surf in New England")
    # Create a dictionary with parsed and pruned data for each area in individual data frames
    conditions_dict = get_info()
    for area in conditions_dict:
        # Run check functions and return wind and wave conditions in the North Shore Area
        if area == "North Shore":
            print(f"""{area} conditions:
    Wind: {check_windns(conditions_dict[area])}
    Waves: {check_wave(conditions_dict[area])}""")
        # Run check functions and return wind and wave conditions in Rhode Island
        elif area == "Rhode Island":
            print(f"""{area} conditions:
    Wind: {check_windri(conditions_dict[area])}
    Waves: {check_waveri(conditions_dict[area])}""")
        # Run check functions and return wind and wave conditions in the other locations
        else:
            print(f"""{area} conditions:
    Wind: {check_wind(conditions_dict[area])}
    Waves: {check_wave(conditions_dict[area])}""")
    # Ask if user wants to see data frames
    answer = input("Want to see the buoy data? (y/n): ").strip().lower()
    if answer == "y":
        for area in conditions_dict:
            print(f"""{area}:
{conditions_dict[area].to_string(index=False)}""")
    else:
        print("Wapow!")

# Take wave and wind data from buoys and combine them into a single
# data frame for each area, stored in a dictionary with the area as the index


def get_info():
    conditions_dict = {
        "Maine": combine(wave_data(data_frame_half_hour(me)), wind_data(data_frame_half_hour(me))),
        "New Hampshire": combine(wave_data(data_frame_half_hour(nh)), wind_data(data_frame_hour(nhw))),
        "North Shore": combine(wave_data(data_frame_half_hour(ns)), wind_data(data_frame_half_hour(ns))),
        "Cape Cod": combine(wave_data(data_frame_half_hour(cc)), wind_data(data_frame_half_hour(ccw))),
        "Rhode Island": combine(wave_data(data_frame_half_hour(ri)), wind_data(data_frame_hour(riw))),
    }
    return conditions_dict

# Take data from buoys that report every 10 or 30 minutes and put it
# into a data frame with 6 rows and cut empty columns


def data_frame_half_hour(url):
    content = requests.get(url)
    text = content.text
    lines = text.split("\n")
    header = lines[0].replace("#", "").split()
    data = [line.split() for line in lines[2:100]]
    df = pd.DataFrame(data, columns=header)
    pd.set_option('future.no_silent_downcasting', True)
    df.replace("MM", np.nan, inplace=True)
    df = df.dropna(subset=["DPD"])
    half_hour_df = df.head(12).iloc[::2]
    half_hour_df.reset_index(drop=True, inplace=True)
    return half_hour_df

# Take data from buoys that report every 60 minutes and put it
# into a data frame with 6 rows and cut empty columns


def data_frame_hour(url):
    content = requests.get(url)
    text = content.text
    lines = text.split("\n")
    header = lines[0].replace("#", "").split()
    data = [line.split() for line in lines[2:30]]
    df = pd.DataFrame(data, columns=header)
    df.replace("MM", np.nan, inplace=True)
    df = df.dropna(subset=["WSPD"])
    hour_df = df.head(6)
    return hour_df

# Change WVHT column in a data frame from m to ft, return just the
# needed columns in a pruned down data frame


def wave_data(df):
    df["WVHT"] = (df["WVHT"].astype(float) * 3.28084).round(1)
    return df[["hh", "mm", "WVHT", "APD", "MWD"]]

# Change WSPD column in a data frame from m/s to mi/hr, return just
# the needed columns in a pruned down data frame


def wind_data(df):
    df["WSPD"] = (df["WSPD"].astype(float) * 2.2369).round(1)
    return df[["WSPD", "WDIR"]]

# Take the cleaned up and mostly formatted wind and wave data frames
# and combine them into a single data frame for the given area with
# the desired column names and types
# Print -999 if there is an error (Like when it is perfectly calm 
# and WDIR has no value or the buoy isn't transmitting data)


def combine(wave, wind):
    combo = pd.concat([wave, wind], axis=1)
    combo = combo.astype(float)
    combo = combo.fillna(-999)
    combo.rename(columns={"hh": "HR"}, inplace=True)
    combo.rename(columns={"mm": "MIN"}, inplace=True)
    for column in ["HR", "MIN", "MWD", "WDIR"]:
        combo[column] = combo[column].astype(int)
    return combo

# Check the wind data for Maine, New Hampshire, or Cape Cod
# to see how conditions are, based on their geography


def check_wind(df):
    if (df["WSPD"].iloc[0:3] < 5).all():
        return "Glassy"
    elif 225 <= df["WDIR"].iloc[0] <= 315:
        if df["WSPD"].iloc[0] < 15:
            return "Clean!"
        else:
            return "Clean, but windy"
    elif 195 < df["WDIR"].iloc[0] < 225 or 315 < df["WDIR"].iloc[0] < 345:
        if 15 < df["WSPD"].iloc[0]:
            return "Sideshore, but wind is too strong"
        else:
            return "Sideshore, but should be manageable"
    else:
        return "Doesn't look great"

# Check the wind data for the North Shore
# to see how conditions are, based on its geography


def check_windns(df):
    if (df["WSPD"].iloc[0:3] < 5).all():
        return "Glassy"
    elif 255 <= df["WDIR"].iloc[0] <= 345:
        if df["WSPD"].iloc[0] < 15:
            return "Clean!"
        else:
            return "Clean, but windy"
    elif 225 < df["WDIR"].iloc[0] < 255 or 345 < df["WDIR"].iloc[0] <= 360 or 0 <= df["WDIR"].iloc[0] < 15:
        if 15 < df["WSPD"].iloc[0]:
            return "Sideshore, but wind is too strong"
        else:
            return "Sideshore, but should be manageable"
    else:
        return "Doesn't look great"

# Check the wind data for Rhode Island
# to see how conditions are, based on its geography


def check_windri(df):
    if (df["WSPD"].iloc[0:3] < 5).all():
        return "Glassy"
    elif 285 <= df["WDIR"].iloc[0] <= 360 or 0 <= df["WDIR"].iloc[0] <= 75:
        if df["WSPD"].iloc[0] < 15:
            return "Clean!"
        else:
            return "Clean, but windy"
    elif 255 < df["WDIR"].iloc[0] < 285 or 75 < df["WDIR"].iloc[0] < 105:
        if 15 < df["WSPD"].iloc[0]:
            return "Sideshore, but wind is too strong"
        else:
            return "Sideshore, but should be good somewhere"
    else:
        return "Doesn't look great"

# Check the wind data for everywhere except Rhode Island
# to see how conditions are, based on their geography


def check_wave(df):
    if (df["WVHT"] < 1.6).all():
        return "Too small"
    elif ((45 < df["MWD"]) & (df["MWD"] < 180)).any():
        return check_swell(df)
    else:
        return "Wave direction points to waves being poor"

# Check the wave data for Rhode Island
# to see how conditions are, based on its geography


def check_waveri(df):
    if (df["WVHT"] < 1.6).all():
        return "Too small"
    elif ((75 < df["MWD"]) & (df["MWD"] < 240)).any():
        return check_swell(df)
    else:
        return "Wave direction points to waves being poor"

# Check the wave size and period to determine how wave conditions are, after
# having already made sure that the swell direction was correct with the
# check_wave and check_waveri functions


def check_swell(df):
    if (8.9 < df["WVHT"]).any():
        if (9 <= df["APD"]).any():
            return "Looks quite big, check the cams"
        else:
            return "Looks big but shorter period - check the cams"
    elif ((6.9 < df["WVHT"]) & (df["WVHT"] <= 8.9)).any():
        if (9 <= df["APD"]).any():
            return "Looks big, pack the shortboard!"
        else:
            return "Large waves, but period is short"
    elif ((4.9 < df["WVHT"]) & (df["WVHT"] <= 6.9)).any():
        if (9 <= df["APD"]).any():
            return "Looks good for a shortboard!"
        else:
            return "Nice size, but period is short"
    elif ((3.9 < df["WVHT"]) & (df["WVHT"] <= 4.9)).any():
        if (7 <= df["APD"]).any():
            return "Looks good for a midlength!"
        else:
            return "Good size, but period is short"
    elif ((3.0 < df["WVHT"]) & (df["WVHT"] <= 3.9)).any():
        if (8 <= df["APD"]).any():
            return "Looks good for a log!"
        else:
            return "Decent size, but period is short"
    elif ((2.3 <= df["WVHT"]) & (df["WVHT"] <= 3.0)).any():
        if (6 <= df["APD"]).any():
            return "Enough for a log"
        else:
            return "Enough for a paddleboard"
    elif ((1.6 <= df["WVHT"]) & (df["WVHT"] <= 2.2)).any():
        if (5 < df["APD"]).any():
            return "Enough for a paddleboard"
        else:
            return "Too small and short period"


if __name__ == "__main__":
    main()
