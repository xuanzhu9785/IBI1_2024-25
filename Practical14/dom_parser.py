from xml.dom import minidom
from datetime import datetime

time1 = datetime.now()

doc = minidom.parse('go_obo.xml')
terms = doc.getElementsByTagName('term')

max_terms = {'molecular_function': ('', '', 0), 'biological_process': ('', '', 0), 'cellular_component': ('', '', 0),}

for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
    name = term.getElementsByTagName('name')[0].firstChild.nodeValue
    is_as = term.getElementsByTagName('is_a')
    is_a_count = len(is_as)

    if namespace in max_terms and is_a_count > max_terms[namespace][2]:
        max_terms[namespace] = (term_id, name, is_a_count)

time2 = datetime.now()
print("Results using DOM:\n")
for namespace, (term_id, name, count) in max_terms.items():
    print(f"{namespace}: {term_id} ({name}), is_a: {count}")

print("\nDOM processing time:", time2 - time1)

#time: 0:00:23.938130. SAX is faster