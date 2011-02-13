import random
import re
import yaml

genny_file = open("gennys/weather.yaml")
genny_yaml = yaml.load(genny_file)
choices = genny_yaml["choices"]
schemas = genny_yaml["schemas"]

variables = {"weavr_name": "bot23",
             "weavr_emotion": "happy"}

def choose_one_of(choices):
    return choices[random.randint(0, len(choices) - 1)]

for key in choices:
    variables[key] = choose_one_of(choices[key])

def sub_variable(text, key, value):
    return re.sub(r"{{[^}]*" + key + r"[^}]*}}", value, text)

def sub_variables(text, variables):
    for key in variables:
        text = sub_variable(text, key, variables[key])
    return text

for key in schemas:
    schema = choose_one_of(schemas[key])
    variables[key] = sub_variables(schema, variables)

#print variables
#for key in schemas:
#    print "%s: %s" % (key, variables[key])
