from SPARQLWrapper import SPARQLWrapper, JSON
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

query = '''
    SELECT ?city ?cityLabel ?foundingDate
    WHERE {
      ?city dbo:country dbr:Ukraine ;
            a dbo:City ;
            dbo:foundingDate ?foundingDate ;
            rdfs:label ?cityLabel .
    }
    ORDER BY DESC(?foundingDate)
    LIMIT 1
'''

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()

print("Наймолодше місто України:")
for value in query_res['results']['bindings']:
    city = value['city']['value']
    cityLabel = value['cityLabel']['value']
    foundingDate = value['foundingDate']['value']
    print(f"{city} - {cityLabel} дата {foundingDate}")
