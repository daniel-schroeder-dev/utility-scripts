#!/usr/bin/python

import os


def rebuild_current():
    prep_commands = """
        wget https://kathirj.codewizardshq.com/download-points-project.zip && \
        rm -rf current/* && \
        mv download-points-project.zip current && \
        cp format.py current
    """

    os.system(prep_commands)

    os.chdir("./current")

    rebuild_commands = """\
        touch __init__.py && \
        unzip download-points-project.zip && \
        rm -rf download-points-project.zip __pycache__ && \
        mv schema.txt schema.sql && \
        ./format.py 
    """

    os.system(rebuild_commands)
    os.chdir("../")


def _replace_approot_app_py():
    app_lines = []
    with open("./current/app.py", mode="rt", encoding="utf-8") as app_file:
        app_lines = app_file.readlines()

    replaced_lines = []
    for line in app_lines:
        if "approot/" in line:
            line = line.replace("approot/", "").replace("txt", "sql")
        replaced_lines.append(line)

    with open("./current/app.py", mode="wt", encoding="utf-8") as app_file:
        app_file.writelines(replaced_lines)


def _replace_approot_db_py():
    db_lines = []
    with open("./current/db.py", mode="rt", encoding="utf-8") as db_file:
        db_lines = db_file.readlines()

    replaced_lines = []
    for line in db_lines:
        if "approot/" in line:
            line = line.replace("approot/", "")
        replaced_lines.append(line)

    with open("./current/db.py", mode="wt", encoding="utf-8") as db_file:
        db_file.writelines(replaced_lines)


def remove_approot():
    _replace_approot_app_py()
    _replace_approot_db_py()


if __name__ == "__main__":
    rebuild_current()
    remove_approot()
