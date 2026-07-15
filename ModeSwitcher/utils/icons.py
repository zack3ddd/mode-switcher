import os
import bpy.utils.previews

icons = None

def register_icons():
    global icons
    icons = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "..", "icons")
    
    for icon in ['MS_sel_box', 'MS_sel_circle', 'MS_sel_lasso']:
        icons.load(icon, os.path.join(icons_dir, f"{icon}.png"), 'IMAGE')

def unregister_icons():
    global icons
    if icons:
        bpy.utils.previews.remove(icons)
        icons = None

def get_icon(name):
    global icons
    return icons[name].icon_id if icons else 0