bl_info = {
    "name": "Mode Switcher",
    "author": "Zack3D (Referenced from MACHIN3tools, AI assisted)",
    "version": (1, 1, 0),
    "blender": (4, 3, 0),
    "location": "3D Viewport (pie menu shortcut)",
    "description": "Quickly switch edit modes with a pie menu in the 3D viewport; from Object Mode jump straight to vertex / edge / face",
    "category": "3D View",
    "doc_url": "",
    "tracker_url": ""
}

import bpy
from . i18n import translations_dict
from . operators.mode import EditMode, MeshMode
from . ui.pies import PieModes, PieSculptMode, PieTexturePaintMode, PieWeightPaintMode, PieVertexPaintMode
from .utils.icons import register_icons, unregister_icons

classes = (
    MeshMode,
    EditMode,
    PieModes,
    PieSculptMode,
    PieTexturePaintMode,
    PieWeightPaintMode,
    PieVertexPaintMode
)

addon_keymaps = []

def register():
    bpy.app.translations.register(__name__, translations_dict)
    register_icons()
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add the keymaps
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # 物體模式
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        addon_keymaps.append((km, kmi))

        # 網格編輯模式
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        addon_keymaps.append((km, kmi))

        # 曲線編輯模式
        km = wm.keyconfigs.addon.keymaps.new(name='Curve')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        addon_keymaps.append((km, kmi))

        # 姿勢模式
        km = wm.keyconfigs.addon.keymaps.new(name='Pose')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        addon_keymaps.append((km, kmi))

        # 骨架編輯模式
        km = wm.keyconfigs.addon.keymaps.new(name='Armature')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        addon_keymaps.append((km, kmi))

        # 雕刻模式
        km = wm.keyconfigs.addon.keymaps.new(name='Sculpt')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_sculpt_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 紋理繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Image Paint')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_texture_paint_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 權重繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Weight Paint')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_weight_paint_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 頂點繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Vertex Paint')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_vertex_paint_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆模式的快捷鍵映射
        # 物體模式
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆編輯模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Edit Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆雕刻模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Sculpt Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆權重模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Weight Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 蠟筆頂點模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Vertex Mode')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "MODESWITCHER_MT_modes_pie"
        kmi.active = True
        addon_keymaps.append((km, kmi))

        # 繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Stroke Paint Mode')
        kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS')
        kmi.properties.name = "GPENCIL_MT_pie_tool_palette"
        addon_keymaps.append((km, kmi))

        # 編輯模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Stroke Edit Mode')
        kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS')
        kmi.properties.name = "GPENCIL_MT_pie_tool_palette"
        addon_keymaps.append((km, kmi))

        # 雕刻模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Stroke Sculpt Mode')
        kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS')
        kmi.properties.name = "GPENCIL_MT_pie_tool_palette"
        addon_keymaps.append((km, kmi))

        # 權重繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Stroke Weight Mode')
        kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS')
        kmi.properties.name = "GPENCIL_MT_pie_tool_palette"
        addon_keymaps.append((km, kmi))

        # 頂點繪製模式
        km = wm.keyconfigs.addon.keymaps.new(name='Grease Pencil Stroke Vertex Mode')
        kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS')
        kmi.properties.name = "GPENCIL_MT_pie_tool_palette"
        addon_keymaps.append((km, kmi))

def unregister():
    unregister_icons()
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    try:
        bpy.app.translations.unregister(__name__)
    except Exception:
        pass

if __name__ == "__main__":
    register()