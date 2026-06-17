from pathlib import Path
import mimetypes

class StaticLoader():
    base_dir = Path(__file__).resolve().parents[1]
    @staticmethod
    def load(file_path: str):
        full_path = StaticLoader.base_dir / "static" / file_path
        content = full_path.read_bytes()
        mime_type, _ = mimetypes.guess_type(full_path)

        return content, mime_type or "text/plain"