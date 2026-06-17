class TemplateLoader():
    @staticmethod
    def load_template(template_name):
        with open(f"src/fnix/templates/{template_name}",encoding="utf-8") as f:
            return f.read()