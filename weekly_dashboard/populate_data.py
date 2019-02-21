import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weekly_dashboard.settings')
import datetime
import django
django.setup()


import pandas as pd
from dash_app.models import Registration, Reward_Sli, Registration_KR, Reward_KR, VDP_Sli_KR

def populate_reg(data_file):
    data = pd.read_excel(data_file, sheet_name='Export Worksheet')

    print('Population Database')

    try:
        for e in data.T.to_dict().values():
            print(e)
            obj, created = Registration.objects.get_or_create(
                
                event_type = e['EVENT_TYPE'],
                date_time =  e['DATE_TIME'],
                count = e['COUNT'],            
            )
    except ValueError:
        print('NaTType does not support utcoffset')


def populate_VDP(data_file):
    data = pd.read_excel(data_file, sheet_name='Sheet1')

    print('Population Database')

    try:
        for e in data.T.to_dict().values():
            print(e)
            obj, created = VDP_Sli_KR.objects.get_or_create(
                
               date_time = datetime.datetime.strptime(e['TO_CHAR(PUI.REGISTERED_ON+9/24'], "%d-%m-%Y").strftime("%Y-%m-%d"),
               name = e['NAME'],
               partner_system_name = e['PARTNER_SYSTEM_NAME'],
               linking_status = e['LINKING_STATUS'],
               count = e['COUNT(PUI.PARTNER_USER_INFO_ID'],
            )
    except ValueError:
        print('NaTType does not support utcoffset')

def populate_reward(data_file):
    data = pd.read_excel(data_file, sheet_name='Export Worksheet')

    print('Population Database')

    try:
        for e in data.T.to_dict().values():
            print(e)
            obj, created = Reward_Sli.objects.get_or_create(

                reward = e['REWARD'],
                awarded_on = datetime.datetime.strptime(e['AWARDED_ON'], "%d-%m-%Y").strftime("%Y-%m-%d"),
                count = e['COUNT'],
            )
    except ValueError:
        print('NaTType does not support utcoffset')




def populate_reg_kr(data_file):
    data = pd.read_excel(data_file, sheet_name='REGKR')

    print('Population Database')

    try:
        for e in data.T.to_dict().values():
            print(e)
            obj, created = Registration_KR.objects.get_or_create(
                
                event_type = e['EVENT_TYPE'],
                date_time = e['DATE_TIME'],
                count = e['COUNT'],            
            )
    except ValueError:
        print('NaTType does not support utcoffset')


def populate_reward_kr(data_file):
    data = pd.read_excel(data_file, sheet_name='REWARDSKR')

    print('Population Database')

    try:
        for e in data.T.to_dict().values():
            print(e)
            obj, created = Reward_KR.objects.get_or_create(

                reward = e['REWARD'],
                awarded_on =e['AWARDED_ON'],
                count = e['COUNT'],
            )
    except ValueError:
        print('NaTType does not support utcoffset')





# populate_VDP('Korea and SLI data 25th Jan.xlsx')
populate_reward('REWARDSSLI15FEB.xlsx')
# populate_reward_kr('REWARDSKR15FEB.xlsx')
# populate_reg_kr('REGKR15FEB.xlsx')
# populate_reg('REGSLI15feb.xlsx')