import json
from pkg_resources import resource_filename, resource_string

# Get the path to the data file
dict_no_en = resource_filename(__name__, 'data/dict_no_en.csv')
dict_county_region = resource_filename(__name__, 'data/dict_county_region.csv')

####################################################################
def translation_dicts(book='no_en'):
    import pandas as pd
    if book=='no_en':
        df = dict_no_en
    if book=='dict_county_region':
        df = dict_county_region
        
    dict_df=pd.read_csv(df)    
    result=dict(zip(dict_df['from'],dict_df['to']))
    
    return result
####################################################################
# google translate
def translate(string='hello', src='no', dest='en'):
    from googletrans import Translator
    translator = Translator()
    result = translator.translate(string, src='no', dest='en')
    try:
        return result.text
    except:
        return string
    

