import requests
import json

def get_data_from_wikidata_api(query):
    url = 'https://query.wikidata.org/sparql'
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    return data

query = '''
SELECT ?item ?itemLabel ?description
WHERE
{
    ?item wdt:P31 wd:Q5.
    ?item dcterms:description ?description.
    FILTER (lang(?description) = "en")
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". 
    }
    '''

results = get_data_from_wikidata_api(query)
print(json.dumps(results, indent=4, sort_keys=True))
