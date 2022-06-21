from selenium.webdriver.common.by import By
# from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def manage_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        # time.sleep(1)
        self.manage_projects_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        self.fill_project(project)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()

    def fill_project(self, project):
        wd = self.app.wd
        wd.find_element(By.NAME, "name").click()
        wd.find_element(By.NAME, "name").clear()
        wd.find_element(By.NAME, "name").send_keys(project.project_name)
        wd.find_element(By.NAME, "description").click()
        wd.find_element(By.NAME, "description").clear()
        wd.find_element(By.NAME, "description").send_keys(project.project_desc)

    def del_project(self, project):
        wd = self.app.wd
        self.manage_projects_page()
        wd.find_element(By.LINK_TEXT, f"{project.project_name}").click()
        wd.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Delete Project']").click()
        wd.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Delete Project']").click()


