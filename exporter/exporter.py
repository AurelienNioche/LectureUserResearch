"""
adapted from https://github.com/jupyter/nbconvert/blob/5.x/nbconvert/exporters/html.py
and https://github.com/ipython-contrib/jupyter_contrib_nbextensions/blob/master/src/jupyter_contrib_nbextensions/nbconvert_support/collapsible_headings.py
"""
import json
import os

from notebook.services.config import ConfigManager

from jupyter_contrib_nbextensions import __file__ as contrib_init

from nbconvert.exporters.html import HTMLExporter
from traitlets import Dict


class CH_TOC(HTMLExporter):
    """
    HTMLExporter which inlines the collapsible_headings nbextension
    and the toc2 extension.
    """

    inliner_resources = Dict(
        {'css': [], 'js': []}, config=True,
        help='css and js scripts to wrap in html <style> or <script> tags')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.inliner_resources['css'].append("""
/* no local copies of fontawesome fonts in basic templates, so use cdn */
@import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css)
""")  # noqa: E501

        ch_dir = os.path.join(
            os.path.dirname(contrib_init), 'nbextensions',
            'collapsible_headings')

        with open(os.path.join(ch_dir, 'main.css'), 'r') as f:
            self.inliner_resources['css'].append(f.read())

        with open(os.path.join(ch_dir, 'main.js'), 'r') as f:
            self.inliner_resources['js'].append(f.read())

        cm = ConfigManager()
        collapsible_headings_options = cm.get('notebook').get(
            'collapsible_headings', {})
        self.inliner_resources['js'].append("""
$(document).ready(function () {
    require(['nbextensions/collapsible_headings/main'], function (ch) {
        ch.set_collapsible_headings_options(%s);
        ch.refresh_all_headings();
    });
});
""" % json.dumps(collapsible_headings_options))

    def _default_template_path_default(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "templates")

        return path

    def _template_file_default(self):
        return 'ch_toc'

    def from_notebook_node(self, nb, resources=None, **kw):

        # ensure resources used by template actually exist, add in any from
        # config
        if resources is None:
            resources = {}
        inliner_resources = resources.setdefault('inliner', {})
        for tt in ('css', 'js'):
            existing_items = inliner_resources.setdefault(tt, [])
            existing_items += [
                item for item in self.inliner_resources[tt]
                if item not in existing_items]

        return super().from_notebook_node(
            nb, resources, **kw)

    @property
    def default_config(self):
        c = super().default_config
        #  import here to avoid circular import
        from jupyter_contrib_nbextensions.nbconvert_support import (
            templates_directory)
        contrib_templates_dir = templates_directory()

        template_path = c.TemplateExporter.setdefault('template_path', [])
        if contrib_templates_dir not in template_path:
            template_path.append(contrib_templates_dir)

        return c
