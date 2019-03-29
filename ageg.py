from math import isnan

from mako.template import Template
from mako.lookup import TemplateLookup

from pandas import read_csv

from ageg.admin import generer_sousquestion_admin, generer_options_admin
from ageg.exec import generer_questions_exec

from models.answer import Answer
from models.group import Group
from models.question import Question

groupe_exec = Group(id=0, name="Comité exécutif", description="Pour cette section, seulement une personne peut-être élue par poste. Veuillez placer les candidatures en ordre de préférence, du haut vers le bas.")
groupe_admin = Group(id=1, name="Conseil d'administration", description="Vote de confiance pour les postes saisonniers au conseil d'administration de l'AGEG.")
groups = [groupe_exec, groupe_admin]

questions = generer_questions_exec(groupe_exec.gid)
question_admin = Question(id=100, code="CASA19", gid=groupe_admin.gid, title="Qui voulez-vous comme administrateurs saisonniers de l'AGEG?", type='F')
question_admin.add_answer(Answer(qid=question_admin.qid, value="Oui", code="A1", order=1))
question_admin.add_answer(Answer(qid=question_admin.qid, value="Non", code="A2", order=2))
        
sousquestions_admin = generer_sousquestion_admin(question_admin)
options_admin = generer_options_admin()

for option in options_admin:
    question_admin.add_option(option)

questions.append(question_admin)    
mylookup = TemplateLookup(directories=['.'], input_encoding="utf-8", output_encoding="utf-8")
mytemplate = Template(filename='templates/ageg/base.mako', lookup=mylookup, input_encoding="utf-8", output_encoding="utf-8")

survey = mytemplate.render(groups=groups,questions=questions,subquestions=sousquestions_admin)

survey_file = open("result/survey.lss", "w+b")
survey_file.write(survey)
survey_file.close()