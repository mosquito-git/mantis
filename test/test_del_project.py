# -*- coding: utf-8 -*-
from model.project import Project



def test_del_project1(app, db):
    app.session.ensure_login()
    db.clear_project_list()
    if len(db.get_project_list()) == 0:
        app.project.create(Project(project_name='erfwrq', project_desc='rfdsadsa'))
    # old_projects = db.get_project_list()
    old_projects = app.soap.get_list_project()
    app.project.del_project(old_projects[0])
    # new_projects = db.get_project_list()
    new_projects = app.soap.get_list_project()
    assert len(old_projects)-1 == len(new_projects)
    old_projects.remove(old_projects[0])
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

