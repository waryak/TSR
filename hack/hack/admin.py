from django.contrib.admin.sites import AdminSite


class OrganisationAdmin(AdminSite):
    pass


class StudentAdmin(AdminSite):
    pass


organisation_admin = OrganisationAdmin(name="OrganisationAdmin")

student_admin = StudentAdmin(name="StudentAdmin")