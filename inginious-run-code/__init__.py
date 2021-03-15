# Plugin for extra-test

import os

from flask import send_from_directory

from inginious.common.tasks_problems import CodeProblem
from inginious.frontend.task_problems import DisplayableCodeProblem
from inginious.frontend.parsable_text import ParsableText
from inginious.frontend.pages.utils import INGIniousPage

PATH_TO_PLUGIN = os.path.abspath(os.path.dirname(__file__))
PATH_TO_TEMPLATES = os.path.join(PATH_TO_PLUGIN, "templates")

class RunCodeProblem(CodeProblem):
    """Add a different test set, using code from another problem"""

    @classmethod
    def get_type_name(cls, language):
        return _("run_code")

class DisplayableRunCodeProblem(RunCodeProblem, DisplayableCodeProblem):
    """ A displayable match problem """

    def __init__(self, problemid, content, translations, taskfs):
        super(DisplayableRunCodeProblem, self).__init__(problemid, content, translations, taskfs)

    @classmethod
    def get_type_name(cls, language):
        return _("run_code")

class StaticMockPage(INGIniousPage):
    # TODO: Replace by shared static middleware and let webserver serve the files
    def GET(self, path):
        return send_from_directory(os.path.join(PATH_TO_PLUGIN, "static"), path)

    def POST(self, path):
        return self.GET(path)


def init(plugin_manager, course_factory, client, plugin_config):
    plugin_manager.add_page('/plugins/run_code/static/<path:path>', StaticMockPage.as_view("runcodepage"))
    plugin_manager.add_hook("javascript_header", lambda: "/plugins/run_code/static/run_code.js")
    course_factory.get_task_factory().add_problem_type(DisplayableRunCodeProblem)
