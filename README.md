# EAL-Easy-Addon-Localisation

EAL aims to make localising and translation of Garry's Mod addons much easier by
automatically finding string values that require translations and creating
templates for translators to fill in.

## How does it work?

EAL changes lua code within your addon to implement translations by replacing 
marked hard-coded strings with global variables. It will then inject itself into an autorun file
(or create one if neccessary) in order to load itself before your addon.

## Requirements

EAL requires Python 3

## Localising your addon

In order to localise your addon, you must first mark the strings you want to be translatable. In order to do this, simply place a single % before any string in any of the lua files in your addon. For example, if you had the code:

``local my_variable = "Hello, World!"``

simply prepend a % to make this translatable

``local my_variable = "%Hello, World!"``

This also works for every method of creating a string in lua, including the speechmarks (""), quotation marks ('') and double brackets ([[]])

Next, simply place eal.py into the root of your addon folder,
e.g. the folder layout will look as such:

        - addon_name
            - lua
            - entities
            - ...
            - eal.py

Then simply run the python script using:

``python eal.py``

The script will then run you through the process of localising your addon. Afterwards, EAL will create a new directory, and some new files inside the addon's lua folder:

    - lua
      - eal_addon_name
        - langs
          - EN.lua
          - DE.lua
          - ...
        - eal.lua

In order to now provide translations, simply give the relevant lua files inside langs/ to neccessary translators. EAL will load these language files upon startup of your addon automatically.


