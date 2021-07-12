import os

from mako.template import Template
from mako.lookup import TemplateLookup

from question_groups import admin, executif, finissante
from models.survey import Survey

from config import config

for group in config.groups:
    if not os.path.isfile(f"input/{group.input}"):
        print(f"Check if {group.input} is present in input directory")
        exit()  # TODO error code?

if config.type == "l'AGEG" and not all([g.type == "admin" or g.type == "exec" for g in config.groups]):
    print(f"Elections for l'AGEG must only contain exec or admin question groups, see GroupConfig in config.py")
    exit()

if config.type == "la finissante" and (
        len(config.groups) > 1 or not all([g.type == "finissante" for g in config.groups])
):
    print(f"Elections for la finissante must only contain one finissante question group, see GroupConfig in config.py")
    exit()

print(f"JOB START ! Starting generation for {config.type}!")
groups = []
questions = []
sousquestions = []

for i, group in enumerate(config.groups):
    if group.type == "exec":
        group, question = executif.generate_questions(group)
        groups.append(group)
        questions.extend(question)

    elif group.type == "admin":
        group, question, sousquestion = admin.generate_questions(group)
        groups.append(group)
        questions.append(question)
        sousquestions.extend(sousquestion)
    elif group.type == "finissante":
        group, question = finissante.generate_questions(group)
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

if config.type == "l'AGEG":
    survey = mytemplate.render(
        survey_options=survey_options,
        groups=groups, questions=questions,
        subquestions=sousquestions,
        withAttributes=False
    )
    output_file = "ageg-survey.lss"
elif config.type == "la finissante":
    survey = mytemplate.render(groups=groups, questions=questions, subquestions=None, withAttributes=True)
    output_file = "finissante-survey.lss"
else:
    print("This should never print")
    exit()  # should never happen

mypath = "output"
if not os.path.isdir(mypath):
    os.makedirs(mypath)
survey_file = open(f"output/{output_file}", "w+b")
survey_file.write(survey)
survey_file.close()

print(f"JOB DONE ! You can find your result in output/{output_file}")
