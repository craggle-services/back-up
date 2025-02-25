#craggle/test/quickli/parsing_html.py
#####
import os
import pandas as pd
from bs4 import BeautifulSoup # pip install beautifulsoup4

def parse_file(file_path):
    with open(file_path, 'r') as f: html = f.read()

    # find the depth at which the string 'anz.png' is located
    soup = BeautifulSoup(html, 'html.parser')

    # we expect ANZ to always be in the list
    image_tag = soup.find('img', {'alt': 'ANZ'})

    if image_tag is None:
        raise ValueError("Image not found.")

    res = []

    table_root = image_tag.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent # type: ignore
    for r in table_root.children: # type: ignore
        # go down the tree until we find a row with more than 2 children
        while True:
            ch = list(r.children) # type: ignore
            if len(ch) == 0 or len(ch) > 2: break
            # print(f'children: {len(ch)}')
            r = ch[0]

        lender, max_capacity, monthly_surplus, dti, product_rate, assess_rate, hem_exp = list(r.children)[3:10] # type: ignore

        res.append({
            'lender': lender.find('img')['alt'], #lender.find('img')['src'].split('/')[-1].split('.')[0],
            'max_capacity': max_capacity.text.replace('$', '').replace(',', ''),
            'monthly_surplus': monthly_surplus.text.replace('$', '').replace(',', ''),
            'dti': dti.text,
            'product_rate': product_rate.text,
            'assess_rate': assess_rate.text,
            'hem_exp': hem_exp.text.replace('$', '').replace(',', ''),
        })
    return res

path_in = '/Users/jpetterson/Downloads/requickliscreenshots'
path_out = 'scenarios'
for file in [f for f in os.listdir(path_in) if f.endswith('.txt')]:
    print(f'Parsing {file}...')
    res = pd.DataFrame(parse_file(f'{path_in}/{file}'))
    res.to_csv(f'{path_out}/{file}.csv', index=False)
