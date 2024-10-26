from SPARQLWrapper import SPARQLWrapper, JSON
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

query = '''
    SELECT DISTINCT ?actor1 ?actor2 ?movie
    WHERE {
        ?person1 a dbo:Person ;
                 dbo:occupation dbr:Actor ;
                 foaf:name ?actor1 ;
                 dbo:spouse ?person2 .
                 
        ?person2 foaf:name ?actor2 ;
                 dbo:occupation dbr:Actor .

        ?movie dbo:starring ?person1, ?person2 .
    }
'''

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
query_res = sparql.query().convert()

print("Сімейні акторські пари, які знімалися разом у фільмах:")
for value in query_res['results']['bindings']:
    actor1 = value['actor1']['value']
    actor2 = value['actor2']['value']
    movie = value['movie']['value']
    print(f"{actor1} та {actor2} знімались разом в фільмі {movie}")
