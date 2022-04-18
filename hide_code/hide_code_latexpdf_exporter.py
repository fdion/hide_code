import os
import os.path

from jupyter_core.paths import jupyter_path
from nbconvert.exporters.pdf import PDFExporter


class HideCodeLatexPDFExporter(PDFExporter):
    def __init__(self, config=None, **kw):
        # self.register_preprocessor('hide_code.HideCodePreprocessor', True)
        super(HideCodeLatexPDFExporter, self).__init__(config, **kw)
        self.preprocessors = ['hide_code.HideCodePreprocessor']
        self._init_preprocessors()

    def _template_file_default(self):
        return 'hide_code_article'

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
