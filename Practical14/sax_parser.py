import xml.sax
from datetime import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ''
        self.namespace = ''
        self.term_id = ''
        self.name = ''
        self.is_a_count = 0
        self.in_term = False

        self.max_terms = {
            'molecular_function': ('', '', 0),
            'biological_process': ('', '', 0),
            'cellular_component': ('', '', 0),
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'term':
            self.in_term = True
            self.namespace = ''
            self.term_id = ''
            self.name = ''
            self.is_a_count = 0

    def characters(self, content):
        if self.current_tag == 'id':
            self.term_id += content.strip()
        elif self.current_tag == 'name':
            self.name += content.strip()
        elif self.current_tag == 'namespace':
            self.namespace += content.strip()
        elif self.current_tag == 'is_a':
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == 'term' and self.namespace in self.max_terms:
            if self.is_a_count > self.max_terms[self.namespace][2]:
                self.max_terms[self.namespace] = (self.term_id, self.name, self.is_a_count)
            self.in_term = False

        self.current_tag = ''

start_time = datetime.now()

parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse('go_obo.xml')

end_time = datetime.now()

print("Results using SAX:\n")
for ns, (term_id, name, count) in handler.max_terms.items():
    print(f"{ns}: {term_id} ({name}) with {count} is_a references")

print("\nSAX processing time:", end_time - start_time)
