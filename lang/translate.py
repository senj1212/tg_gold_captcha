import yaml
import os

def get_translation(language:str, key:str, **kwargs):
    path = "lang/"
    if not os.path.exists(f'{path}{language}.yaml'):
        language = "en"
    with open(f'{path}{language}.yaml', 'r', encoding='utf-8') as file:
        translations = yaml.safe_load(file)
        if key in translations:
            return translations[key].format(**kwargs)
    return f'Missing translation for key: {key}'