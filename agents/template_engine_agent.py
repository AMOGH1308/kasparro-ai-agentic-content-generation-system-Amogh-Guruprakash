from logic_blocks.template_loader import load_template
from logic_blocks.template_logic import fill_template

class TemplateEngineAgent:
    def apply_template(self, template_filename, data):
        template = load_template(template_filename)
        return fill_template(template, data)
