from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app



    def can_login(self, username, password):
        client = Client(f"{self.app.config['web']['baseUrl']}api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_project(self):
        client = Client(f"{self.app.config['web']['baseUrl']}api/soap/mantisconnect.php?wsdl")
        list = []
        try:
            projects = client.service.mc_projects_get_user_accessible(
                username=self.app.config['webadmin']['username'], password=self.app.config['webadmin']['password'])
            # print('projects=', projects)
            for proj in projects:
                (id, name, decription) = (proj.id,proj.name,proj.description)
                list.append(Project(id=str(id), project_name=name, project_desc=decription))
            return list
        except WebFault:
            return False
