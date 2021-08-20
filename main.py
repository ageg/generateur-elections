import os

import yaml

from mako.template import Template
from mako.lookup import TemplateLookup

from question_groups import admin, executif, finissante
from models.survey import Survey

from config import validate_config, fill_placehoders

stream = open("config.yaml", 'r')
config = yaml.safe_load(stream)

validate_config(config)
fill_placehoders(config)


print(f"JOB START ! Starting generation for {config['type']}!")
groups = []
questions = []
sousquestions = []

for group in config['groups']:
    if group['type'] == "exec":
        group, question = executif.generate_questions(config, group)
        groups.append(group)
        questions.extend(question)
    elif group['type'] == "admin":
        group, question, sousquestion = admin.generate_questions(group)
        groups.append(group)
        questions.append(question)
        sousquestions.extend(sousquestion)
    elif group['type'] == "finissante":
        group, question = finissante.generate_questions(config,group)
        groups.extend(group)
        questions.extend(question)
    else:
        print("invalid conf type, exiting")
        exit()  # TODO discard conf?

survey_options = Survey(config)

mylookup = TemplateLookup(directories=['.'], input_encoding="utf-8", output_encoding="utf-8")
mytemplate = Template(filename='templates/base.mako', lookup=mylookup, input_encoding="utf-8", output_encoding="utf-8")

output_file = ""
survey = ""

if config['type'] == "l'AGEG":
    survey = mytemplate.render(
        survey_options=survey_options,
        groups=groups,
        questions=questions,
        subquestions=sousquestions,
        withAttributes=False
    )
    output_file = "ageg-survey-test.lss"
elif config['type'] == "la finissante":
    survey = mytemplate.render(
        survey_options=survey_options,
        groups=groups,
        questions=questions,
        subquestions=None,
        withAttributes=True
    )
    output_file = "finissante-survey.lss"
else:
    print("This should never print")
    exit()  # should never happen


survey_file = open(f"output/{output_file}", "w+b")
survey_file.write(survey)
survey_file.close()

print(f"JOB DONE ! You can find your result in output/{output_file}")
