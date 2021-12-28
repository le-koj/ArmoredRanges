###############################################
### FILE: python module                     ###
###                                         ###
### DESCRIPTION: main backend module        ###
###             for armoredrange.com webapp ###
###                                         ###
### PURPOSE: respond/handle request towards ###
###          app.                           ###
###############################################

import webapp2, cgi, os, jinja2

from google.appengine.api import app_identity, mail
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# setup template directory
template_dir = os.path.join(os.path.dirname(__file__))

# jinja environment instance to load html templates
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


############_____ ROOT APP CONTROL OBJECT ___##########
class MainHandler(webapp2.RequestHandler):
    """ main object to handle index.html request """

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("index.html")    # generate and send html page

    #_____ method to finalize template for response _____#
    def renderTemplate(self, template_name, context=None):
        if context is None:     # verify context
            context={}          # context gets empty object

        template = jinja_env.get_template(template_name)    # get html template page
        return template.render(context)                     # add context to template

    #_____ method to generate context for template _____#
    def generateContext(self):
        pass

    #______ method to process get action ______#
    def process_get_method(self, file_name):
        # variable to generate context
        context = None

        # create template based on context and given template name
        rendered_template = self.renderTemplate(file_name, context=context)

        # send out rendered template
        self.response.out.write(rendered_template)




############_____ CONTAINER PAGE CONTROL OBJECT ___##########
class ContainerHandler(MainHandler):
    """object to handle container.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("container.html")    # generate and send html page



############_____ TRAINING PAGE CONTROL OBJECT ___##########
class TrainingHandler(MainHandler):
    """object to handle training.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("training.html")    # generate and send html page

############_____ CUSTOM PAGE CONTROL OBJECT ___##########
class CustomHandler(MainHandler):
    """object to handle CUSTOM.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("custom.html")    # generate and send html page



############_____ ABOUT PAGE CONTROL OBJECT ___##########
class AboutHandler(MainHandler):
    """object to handle training.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("armoredrange.html")    # generate and send html page



############_____ BUILD PAGE CONTROL OBJECT ___##########
class BuildHandler(MainHandler):
    """object to handle build.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("build.html")    # generate and send html page

    #_____ method to process post request _____#
    def post(self):

        information_list = ['firstName', 'lastName', 'email', 'message' ]

        sender_address = 'armoredrange5@gmail.com'
        email = 'info@armoredrange.com'
        subject = cgi.escape(self.request.get('firstName')) + " " + cgi.escape(self.request.get('lastName'))
        body = cgi.escape(self.request.get('email')) + "\n" + cgi.escape(self.request.get('message'))

        mail.send_mail(sender=sender_address,
                  to=email,
                  subject=subject,
                  body=body)

        self.process_get_method('response.html')



############_____ BUILD PAGE CONTROL OBJECT ___##########
class EstimateHandler(MainHandler):
    """object to handle estimate requests"""

    #_____ method to process estimate request _____#
    def post(self):
        sender_address = 'armoredrange5@gmail.com'
        email = 'armoredrange5@gmail.com'
        telephone = cgi.escape(self.request.get('telephone'))
        country = cgi.escape(self.request.get('country'))
        subject = cgi.escape(self.request.get('firstName')) + " " + cgi.escape(self.request.get('lastName'))
        body = cgi.escape(self.request.get('message')) + '\n' + country + '\n' + str(telephone) + '\n' + cgi.escape(self.request.get('email'))  + '\n'

        mail.send_mail(sender=sender_address,
                  to=email,
                  subject=subject,
                  body=body)

        self.process_get_method('response.html')




############_____ GALLERY PAGE CONTROL OBJECT ___##########
class GalleryHandler(MainHandler):
    """object to handle gallery.html response"""

    #_____ method to respond to request _____#
    def get(self):
        self.process_get_method("gallery.html")    # generate and send html page



#######################################################




app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/index', MainHandler),
    (r'/container', ContainerHandler),
    (r'/training', TrainingHandler),
    (r'/build', BuildHandler),
    (r'/contact', BuildHandler),
    (r'/estimate', EstimateHandler),
    (r'/armoredrange', AboutHandler),
    (r'/gallery', GalleryHandler),
    (r'/custom', CustomHandler),
    ], debug=False)
