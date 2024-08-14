# Project Name: New England Surf Check
# Created by Blake Denman
# GitHub Username: blakedenman2
# EdX Username: blakedenman2
# Location: Beverly, MA, USA
# Date: June, 30, 2024

    #### Video Demo: https://youtu.be/6Pc6ScmgfBs

    #### Description:

I am a big surfer living North of Boston and am always checking the surf conditions via buoys
and surf cams to see if it's good anywhere. I will surf anywhere from Rhode Island to Maine
depending on conditions.

So the first thing that came to mind when I needed to make a final project for CS50P was to
make something to help me check the surf. I started out by doing some research into how data
analysts use Python in their jobs, since data analysis is where I am hoping the skill-building
process is leading me towards. I saw that Pandas was a very commonly used library for Python
within the field, and wanted to try to use it to get some practice in its use. I learned that
Pandas can read text or html tables on a webpage, which made me think of how data is presented
on NDBC buoy webpages. I tried to find some related NDBC packages on PyPI, and tested a couple
out, but it seemed like I would have to make my own to meet my needs. At the very least this
was a good learning experience for finding packages from other people on PyPI.

Well, I didn't have to start completely from scratch. One of the PyPI packages I played around
with had some info in its documentation about the NDBC having a data index, which I found at:
https://www.ndbc.noaa.gov/data/
This led me to the page with data from the last 5 days from all reporting stations worldwide:
https://www.ndbc.noaa.gov/data/5day2/

Now I was able to access just the data of the buoys I would normally be checking to see
how the surf was - but instead of being the regular HTML website, I was accessing it was just
the data in a text format. Different buoys retrieve different types of data, with there being
some with more simple data and some with more complex parameters - and some do only atmospheric
readings while others only record oceanic data. Similarly, there are some buoys that record
data every 10 minutes, some every 30, and some every 60 - and for those that record every 10
or 30, often there are some parameters that are recorded every 10, and some that are only every
third measurement, or every 30 minutes.

The variances between these buoys made it so I had to do a fair bit of work to get the data I
wanted. For New Hampshire, Cape Cod, and Rhode Island the buoys I use for wave data did not have
the atmospheric (wind) data that I was planning to use as part of my analysis. So for those
areas I had to use two different stations to get the data I wanted, and combine it together.
After I had finally dissected, reassembled, and finally formatted the data how I wanted it, I
could finally use it to match up against my lived observations about what conditions end up being
favorable, so-so, or poor.

The thing is, New England has a lot of variation in its coastline. Conditions that are good
for Rhode Island are not necessarily good for Cape Cod or New Hampshire, meaning I had to
add extra nuance to my analysis of each area's wind and wave data. Wave characteristics
for Maine, New Hampshire, the North Shore, and Cape Cod all follow pretty much the same
pattern, while Rhode Island differs due to its southerly orientation. Ideal wind
conditions for Maine, New Hampshire, and Cape Cod are all pretty much the same, but the North
Shore and Rhode Island Differ in the best wind directions for their surf breaks. Due to these
differences I had to add extra functions and extra checks into my code to make sure that I was
checking the wind and wave conditions for each of these spots according to their unique
geographic and oceanographic features.

So, now that we have had a high-level overview, let's get into a more specific description
of the actual code.

I import requests to read the text buoy data and eventually use Pandas and Numpy to
work it into data frames. I start out by defining the data-containing urls as variables
named after the areas they provide data for. My main function runs the recent buoy data
(which is continuously updated to the urls I used by NDBC) to create a dictionary of data
frames whose indexes are the names of the areas, and whose values are data frames containing
a time (in military time) and the relevant wind and wave data for that region. Wave direction,
size, and period are all relevant to surf conditions, as well as wind direction and intensity.
My data_frame_half_hour() and data_frame_hour() functions take the url data (depending on
whether it is reported every 10, 30, or 60 minutes) and turns it into a list, then a data
frame and cleans it up a bit, removing empty columns and creating a header.

The wave_data() and wind_data() functions take these data frames (one for wind and one for
waves has been established for each area per the get_info() function), and change metric
measurements to standard, and return just the wind and wave data columns I am going to use.
The combine() function takes these two data frames and concatenates them into a single data
frame, renaming a couple of the columns and converting the types of all the columns to either
float or int.  The get_info() function stores this in a dict and returns it to main().

Main() then takes this conditions_dict and  runs it through the check functions of
check_wind(ns)(ri) and check_wave(ri) for each area - recall that there are slightly
different wave and wind conditions that work well in different areas, so some distinction/
extra functions need to be added to checking the wind and waves to account for that.
Once the data frames have been run through the appropriate checks for each area, they are
printed along with the area name, and then the user is asked if they would like to see
the data frames themselves. If yes, each data frame along with it's area name is printed,
if no, the user is sent out with a healthy "Wapow!" to see them out.
