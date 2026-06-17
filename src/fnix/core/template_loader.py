from pathlib import Path

class TemplateLoader():
    base_dir = Path(__file__).resolve().parents[1]

    @staticmethod
    def load_template(template_name):
        template_path = TemplateLoader.base_dir / "templates" / template_name
        return template_path.read_text(encoding='utf-8')