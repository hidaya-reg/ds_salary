# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:23:47 2022

@author: hp
"""

import glassdoor_scraper as gs
import pandas as pd
path = 'C:/Users/hp/Documents/ds_salary/chromedriver'
df = gs.get_jobs('data scientist', 80, False, path, 10)  


df.drop_duplicates(inplace=True)
df.to_csv('glassdoor8013.csv', index=False)


