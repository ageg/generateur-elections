import os
from pandas import read_csv


def validate_dir(dir):
    if not os.path.isdir(dir):
        print(f"{dir} is not present, creating {dir} directory")
        os.makedirs(dir)


def validate_input_file(file):
    if not os.path.isfile(f"input/{file}"):
        print(f"Check if {file} is present in input directory")
        exit()  # TODO error code?


def validate_columns(group):
    from constants import file_columns
    for col in file_columns[group['type']]:
        if col not in group['df'].columns:
            print(f"Column \"{col}\" not in {group['file']}")
            exit()


def validate_question_groups(groups):
    if any(group['type'] not in ['exec', 'admin', 'finissante'] for group in groups):
        invalid_groups = [group for group in groups if group['type']]
        print(f"Invalid group types present")
        for group in invalid_groups:
            print(f"discarding group of type {group['type']}")
        groups.remove(invalid_groups)
    for group in groups:
        validate_input_file(group['file'])
        group['df'] = read_csv(f"input/{group['file']}")
        validate_columns(group)


def validate_survey_config(conf):
    if conf['type'] == "l'AGEG" and not all(g['type'] == "admin" or g['type'] == "exec" for g in conf['groups']):
        print(f"Elections for l'AGEG must only contain exec or admin question groups, see GroupConfig in config.py")
        exit()

    if conf['type'] == "la finissante" and (
            len(conf['groups']) > 1 or not all(g['type'] == "finissante" for g in conf['groups'])
    ):
        print(
            f"Elections for la finissante must only contain one finissante question group, see GroupConfig in config.py")
        exit()


def validate_config(conf):
    validate_dir("input")
    validate_dir("output")
    validate_question_groups(conf['groups'])
    validate_survey_config(conf)


# validate file columns

# set survey values from conf analysis

# fill placeholder references
# list of text options to check
def fill_placehoders(conf):
    import re
    from constants import text_elements
    for text in text_elements:
        placehoders = set(re.findall(r"conf\[([^\s]*)\]", conf[text]))
        for ph in placehoders:
            conf[text] = conf[text].replace(f"conf[{ph}]", conf[ph])
