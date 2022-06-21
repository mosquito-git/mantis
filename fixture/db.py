# import random

import pymysql.cursors
from model.project import Project
# from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=name,
                                          autocommit=True)

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,name,description from mantis_project_table")
            for row in cursor:
                (id, name, decription) = row
                list.append(Project(id=str(id), project_name=name, project_desc=decription))
        finally:
            cursor.close()
        return list

    def clear_project_list(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from mantis_project_table")
        finally:
            cursor.close()

    def destroy(self):
        self.connection.close()




    # def get_contact_list(self):
    #     list = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(
    #             "select id,firstname,middlename,lastname,address,home,mobile,work,phone2,email,email2,email3 from addressbook where deprecated='0000-00-00 00:00:00'")
    #         for row in cursor:
    #             (id, firstname, middlename, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
    #             list.append(
    #                 Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, address=address,
    #                         home=home,mobile=mobile,work=work,phone2=phone2,
    #                         email=email, email2=email2, email3=email3,
    #                         all_phones_from_home_page=[home, mobile, work, phone2],
    #                         all_emails_from_home_page=[email, email2, email3]))
    #     finally:
    #         cursor.close()
    #     return list



    # def count_contacts_in_group(self):
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select count(id) from address_in_groups")
    #         cnt = cursor.fetchone()
    #     finally:
    #         cursor.close()
    #     return cnt[0]
    #
    # def get_group_id_in_contacts_in_group(self):
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select group_id from address_in_groups group by group_id")
    #         grp_id = cursor.fetchall()
    #         print('grp in cursor = ', grp_id)
    #     finally:
    #         cursor.close()
    #     return random.choice(grp_id)[0]
