from lxml import html
import requests

page = requests.get('http://localhost/Taller4/ejBS_Forms.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
form = tree.xpath('//form[@id="formScrap"]')

#form[0].fields["IdOrigen"].set('value', '12345')
#form[0].fields["IdDestino"].set('value', '54321')

orig = tree.xpath('//input[@name="name"]')
dest = tree.xpath('//input[@name="email"]')

print form[0]
print orig[0].set('value','Pepe')

#orig[0].set('value','12345')
#dest[0].set('value','54321')

response = form[0].submit()

#content = response.read()

#print 'Response: ', content
