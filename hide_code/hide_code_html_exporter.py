import os
import os.path

from jupyter_core.paths import jupyter_path
# import traitlets.config import Config
from traitlets import default, Unicode
from nbconvert.exporters.html import HTMLExporter
from traitlets.log import get_logger


class HideCodeHTMLExporter(HTMLExporter):
    def __init__(self, config=None, **kw):
        # self.register_preprocessor('hide_code.HideCodePreprocessor', True)
        super(HideCodeHTMLExporter, self).__init__(config, **kw)
        # self.preprocessors = ['hide_code.HideCodePreprocessor']
        # self._init_preprocessors()

    @default('template_file')
    def _template_file_default(self):
        # trying with template installed in directory on server
        return 'hide_code_full'
