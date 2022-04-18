import os
import os.path

from jupyter_core.paths import jupyter_path
from nbconvert.exporters.slides import SlidesExporter


class HideCodeSlidesExporter(SlidesExporter):

    def __init__(self, config=None, **kw):
        super(HideCodeSlidesExporter, self).__init__(config, **kw)
        self.preprocessors = ['hide_code.HideCodePreprocessor']
        self._init_preprocessors()

    def _template_file_default(self):
        return 'hide_code_slides'

    @property
    def template_paths(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return jupyter_path("nbconvert", "templates") + [os.path.join(os.path.dirname(__file__), "Templates")]
