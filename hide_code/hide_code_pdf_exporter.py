import os
import os.path
import pdfkit

from jupyter_core.paths import jupyter_path
from traitlets import default
from nbconvert.exporters.html import HTMLExporter


class HideCodePDFExporter(HTMLExporter):
    def __init__(self, config=None, **kw):
        # self.register_preprocessor('hide_code.HideCodePreprocessor', True)
        super(HideCodePDFExporter, self).__init__(config, **kw)
        # self.preprocessors = ['hide_code.HideCodePreprocessor']
        # self._init_preprocessors()

    @default('file_extension')
    def _file_extension_default(self):
        return '.pdf'

    def from_notebook_node(self, nb, resources=None, **kw):
        output, resources = super(HideCodePDFExporter, self).from_notebook_node(nb, resources, **kw)
        options = {
            'print-media-type': '',
            'page-size': 'Letter',
            'margin-top': "0.1in",
            'margin-right': "0.1in",
            'margin-bottom': "0.1in",
            'margin-left': "0.1in",
            'encoding': "UTF-8"
        }
        hide_code = [os.path.join(dir, "hide_code_full") for dir in jupyter_path("nbconvert", "templates")]
        css = None
        for path in hide_code:
            css_file = os.path.join(path, "hide_code_custom.css")
            if os.path.exists(css_file):
                css = css_file
        output = pdfkit.from_string(output, False, css=css, options=options)
        return output, resources

    def _template_file_default(self):
        return 'hide_code_full.tpl'

    @property
    def template_paths(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        classic = [os.path.join(dir, "classic") for dir in jupyter_path("nbconvert", "templates")]
        base = [os.path.join(dir, "base") for dir in jupyter_path("nbconvert", "templates")]
        top = jupyter_path("nbconvert", "templates")
        return classic + base + top + [os.path.join(os.path.dirname(__file__), "Templates")]
