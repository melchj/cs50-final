# cs50 final project
a project to satisfy cs50's final assignment.

## commute tracker/visualizer
---
i hate driving to/from work.

the goal of this project is to provide a tool that can give info about how awful someones drive to/from work is at certain times of day.


### where does the data come from?
---
 - google takeout

therefore, it this will only really work for those who use google maps a lot and have a lot of data to export from google.

### who is this for?
---
(aside from the cs50 autograder bot)

anyone who has location data in their google takeout and would like some insights on their commuting time.


### eventual features
---
the type of data that i would eventually like this tool to provide:
 - average drive time per
   - day of week
   - week
   - month
 - visualizations of the above (graphs? heatmaps?)
 - total count of time wasted commuting
   - comparisons to other useful things that time could be spent doing
 - ??? more to come


## Google Takeout Location Data
---

it is no secret that google stores a lot of data for each user. you can download the data they have stored on you via "google takeout."

the location data in google takout (for me, at least) consists of the following file structure (dates changed for privacy):

```
└── Takeout/Location History
    ├── Semantic Location History
    │   ├── 2019
    │   │   ├── 2019_APRIL.json
    │   │   ├── 2019_AUGUST.json
    │   │   ├── 2019_DECEMBER.json
    │   │   ├── etc...
    │   ├── 2020
    │   │   ├── 2020_APRIL.json
    │   │   ├── 2020_AUGUST.json
    │   │   ├── 2020_DECEMBER.json
    │   │   ├── etc...
    │   ├── etc...
    ├── Records.json
    └── Settings.json
```

### Settings.json
small settings file. looks useles for this project.


### Records.json
absolutely massive file (mine is over 850MB and has nearly 40 million lines). this appears to have information about everywhere i've ever been with my android phone, along with timestamps, charging information, wifi data, and much more.

this file appears to have all the data i need (and more).


### Semantic Location History files
these json files appear to contain location data and timestamps, as well as the name of businesses and stores and other places visited.

looking through these files, it is a bit spooky how much data there is on my minute-by-minute activities and the stores/locations that google assumes/knows i've been to.

