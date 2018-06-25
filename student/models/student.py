from odoo import api, fields, models, _


class studentstudent(models.Model):
    _name = "student.student"
    _description = "Jobportal"

    name = fields.Char(string="Name", required=True)
    lastname = fields.Char(string="Last Name", required=True)
    address = fields.Char(string="Address", required=True)
    city = fields.Char(string="City", required=True)
    dob = fields.Date(string="D.O.B", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection([('m','Male'),('f','Femele')],string="Gender", required=True)  
    Location = fields.Many2one('student.job', String="Location")
    job_id= fields.One2many('student.job', 'company_id',String="Job Id")
	
class studentjob(models.Model):
    _name = "student.job"
    _description = "Jobportal"

    degree = fields.Selection([('g','Graduate'),('pg','Post Graduate'),('dp','Diploma')],string="Qualification", required=True)
    year = fields.Char(string="Passing Year", required=True)
    per = fields.Integer(string="Persentage", required=True)
    application = fields.Selection([('d','Devloper'),('pm','Project Manager'),('tl','Team Leader'),                                     
                                        ('tr','Trainee')],string="Apply For",required=True)
    language = fields.Selection([('o','Odoo'),('p','Python'),('x','XML'),('j','Java')],string="Interested In",required=True)
    company_id = fields.One2many('student.student', String="company")
    
    
