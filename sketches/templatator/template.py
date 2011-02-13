import genny

template_file = open("templates/act1stage1.html")
template = template_file.read()

expanded_template = genny.sub_variables(template, genny.variables)

print expanded_template
