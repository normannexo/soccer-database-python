'''
Created on 24.11.2019

@author: norma
'''
import sqlalchemy as sqla
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

def getHomePossession(strPossession):
    root = ET.fromstring(strPossession)
    tag = root.find(".//value[elapsed='90']")
    return tag.findtext('homepos')


db = sqla.create_engine('sqlite:///database.sqlite')
df = pd.read_sql("select season, possession from match where possession <> '<possession />' limit 4", db)
df['homepossession'] = getHomePossession(df['possession'][0])
print(df)
