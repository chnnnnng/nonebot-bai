from os import path

import jinja2


def getTemplate(TEMPLATE_FILE):
    templateLoader = jinja2.FileSystemLoader(searchpath=path.join(path.dirname(path.dirname(__file__)),'templates',TEMPLATE_FILE))
    templateEnv = jinja2.Environment(loader=templateLoader)
    return templateEnv.get_template(TEMPLATE_FILE+'.html')