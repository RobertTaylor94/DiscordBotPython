from discord import File
import os

def get_embed_file(user_id):
    script_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(script_dir)
    filePath = os.path.join(project_root, "assets", str(user_id), "stitched_image.png")
    file = File(filePath, filename="image.png")
    return file