
import mechanize

url = "http://www.renfe.com/index.html"
br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
for form in br.forms():
    if form.attrs['id'] == 'datosBusqueda':
        br.form = form
        break

br.form["IdOrigen"] = "60600"
br.form["IdDestino"] = "61200"
res = br.submit()
content = res.read()
print content
