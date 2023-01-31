import requests
import json

USER_AGENT = 'Wikidata-Data-Extraction/0.1 (steve.baskauf@vanderbilt.edu)'
HEADERS = {'User-Agent': USER_AGENT, 'Accept': 'application/sparql-results+json'}


def get_data_from_wikidata_api(query):
    url = 'https://query.wikidata.org/sparql'
    HEADERS['query'] = query
    r = requests.post(url, headers=HEADERS, data={'query': query})
    #data = r.json()
    data = r.text
    return data

query = '''SELECT ?item ?itemLabel ?description
WHERE
{
    ?item wdt:P195 wd:Q18563658.
    ?item schema:description ?description.
    FILTER (lang(?description) = "en")
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    '''

results = get_data_from_wikidata_api(query)
print(results)
#print(json.dumps(results, indent=4, sort_keys=True))
