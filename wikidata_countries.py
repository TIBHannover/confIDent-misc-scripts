from SPARQLWrapper import SPARQLWrapper, JSON  # , TURTLE, RDF
from typing import Dict
from pprint import pprint

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 ' \
            'Safari/537.36'


def sparql(sparql_query:str) -> Dict:
    endpoint = SPARQLWrapper(endpoint='https://query.wikidata.org/sparql',
                             agent=useragent)
    endpoint.setQuery(sparql_query)
    endpoint.setReturnFormat(JSON)
    results = endpoint.query().convert()
    results_bindings = results['results']['bindings']
    return results_bindings


sparql_countries = '''
SELECT DISTINCT ?countryName
WHERE {
  ?country wdt:P31 wd:Q6256 . # instance of: country
  ?country rdfs:label ?countryName . 
                FILTER (LANG(?countryName) = "en").

}
ORDER BY ASC(?countryName)
'''

results = sparql(sparql_query=sparql_countries)
results_wiki_list = [f"* {entry['countryName']['value']}" for entry in results]
results_wiki_str = ("\n").join(results_wiki_list)
print(results_wiki_str)
    # pprint(entry)
