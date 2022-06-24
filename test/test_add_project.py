# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project1(app, db, json_projects):
    app.session.ensure_login()
    project = json_projects
    db.clear_project_list()
    old_projects = app.soap.get_list_project()
    # old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = app.soap.get_list_project()
    # new_projects = db.get_project_list()
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

