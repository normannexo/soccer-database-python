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

query = """select league.name, season, possession, home_team_goal, away_team_goal
 from match
 inner join league on match.league_id = league.id
 where possession like '%<elapsed>90%'
 """


db = sqla.create_engine('sqlite:///database.sqlite')
df = pd.read_sql(query, db)
df['homepossession'] = df['possession'].apply(getHomePossession)
df['resultdiff'] = df['home_team_goal'] - df['away_team_goal']
df = df.drop('possession', axis=1)
#df['homepossession','resultdiff'].corr()
print(df)
