# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

"""
Referenced from MACHIN3tools
Modified by Zack3D
Blender Version: 4.3
Development assisted by AI (Trae AI)
"""

import bpy
from bpy.types import Menu
from ..utils.icons import get_icon

class PieModes(Menu):
    bl_idname = "MODESWITCHER_MT_modes_pie"
    bl_label = "Mode Switcher"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        active = context.active_object
        
        if not active:
            return
            
        # 檢查當前模式
        current_mode = context.mode
        
        # 如果是雕刻模式
        if current_mode == 'SCULPT':
            pie.separator()  # LEFT
            pie.separator()  # RIGHT
            pie.separator()  # BOTTOM
            pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'  # TOP
            pie.separator()  # TOP_LEFT
            pie.separator()  # TOP_RIGHT
            pie.separator()  # BOTTOM_RIGHT
            pie.separator()  # BOTTOM_LEFT
            return
            
        # 如果是頂點繪製模式
        elif current_mode == 'PAINT_VERTEX':  # 修改這裡
            pie.separator()  # LEFT
            pie.separator()  # RIGHT
            pie.separator()  # BOTTOM
            pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'  # TOP
            pie.separator()  # TOP_LEFT
            pie.separator()  # TOP_RIGHT
            pie.separator()  # BOTTOM_RIGHT
            pie.separator()  # BOTTOM_LEFT
            return
            
        # 如果是權重繪製模式
        elif current_mode == 'PAINT_WEIGHT':  # 修改這裡
            pie.separator()  # LEFT
            pie.separator()  # RIGHT
            pie.separator()  # BOTTOM
            pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'  # TOP
            pie.separator()  # TOP_LEFT
            pie.separator()  # TOP_RIGHT
            pie.separator()  # BOTTOM_RIGHT
            pie.separator()  # BOTTOM_LEFT
            return
            
        # 如果是紋理繪製模式
        elif current_mode == 'PAINT_TEXTURE':  # 修改這裡
            pie.separator()  # LEFT
            pie.separator()  # RIGHT
            pie.separator()  # BOTTOM
            pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'  # TOP
            pie.separator()  # TOP_LEFT
            pie.separator()  # TOP_RIGHT
            pie.separator()  # BOTTOM_RIGHT
            pie.separator()  # BOTTOM_LEFT
            return
            
        # 其他模式保持原有的邏輯
        if active.type == 'MESH':
            # LEFT (左) - Vertex
            depress = context.mode == 'EDIT_MESH' and context.tool_settings.mesh_select_mode[0]
            pie.operator("modeswitcher.mesh_mode", text="頂點", depress=depress, icon='VERTEXSEL').mode = 'VERT'

            # RIGHT (右) - Face
            depress = context.mode == 'EDIT_MESH' and context.tool_settings.mesh_select_mode[2]
            pie.operator("modeswitcher.mesh_mode", text="面", depress=depress, icon='FACESEL').mode = 'FACE'

            # BOTTOM (下) - Edge
            depress = context.mode == 'EDIT_MESH' and context.tool_settings.mesh_select_mode[1]
            pie.operator("modeswitcher.mesh_mode", text="邊", depress=depress, icon='EDGESEL').mode = 'EDGE'

            # TOP (上) - Edit Mode
            text = "物體模式" if context.mode == "EDIT_MESH" else "編輯模式"
            icon = 'OBJECT_DATAMODE' if context.mode == "EDIT_MESH" else 'EDITMODE_HLT'
            pie.operator("modeswitcher.edit_mode", text=text, icon=icon)

            # TOP_LEFT (左上) - Mode Buttons
            row = pie.row()
            row.scale_x = 1.2
            row.scale_y = 1.2
            if active.data.uv_layers:
                row.operator("object.mode_set", text="", icon='TPAINT_HLT').mode = 'TEXTURE_PAINT'
            row.operator("object.mode_set", text="", icon='WPAINT_HLT').mode = 'WEIGHT_PAINT'
            row.operator("object.mode_set", text="", icon='VPAINT_HLT').mode = 'VERTEX_PAINT'
            row.operator("object.mode_set", text="", icon='SCULPTMODE_HLT').mode = 'SCULPT'  # 修復這行
            # TOP_RIGHT (右上) - Selection Tools
            pie.separator()
            pie.separator()  # BOTTOM_RIGHT
            pie.separator()  # BOTTOM_LEFT

        elif active.type in ['CURVE', 'SURFACE', 'LATTICE', 'META', 'FONT']:
            # TOP (上)
            pie.separator()

            # RIGHT (右)
            pie.separator()

            # BOTTOM (下)
            pie.separator()

            # LEFT (左)
            if context.mode == "OBJECT":
                pie.operator("object.mode_set", text="編輯模式", icon='EDITMODE_HLT').mode = 'EDIT'
            else:
                pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'

            # 其他位置保持空白
            pie.separator()  # TOP_LEFT (左上)
            pie.separator()  # TOP_RIGHT (右上)
            pie.separator()  # BOTTOM_LEFT (左下)
            pie.separator()  # BOTTOM_RIGHT (右下)

        elif active.type == 'ARMATURE':
            # 1 - BOTTOM_LEFT
            pie.separator()

            # 2 - BOTTOM
            if context.mode == 'OBJECT':
                pie.operator("object.mode_set", text="姿態模式", icon='POSE_HLT').mode = 'POSE'
            elif context.mode == 'EDIT_ARMATURE':
                pie.operator("object.mode_set", text="姿態模式", icon='POSE_HLT').mode = 'POSE'
            else:  # POSE mode
                pie.operator("object.mode_set", text="編輯模式", icon='EDITMODE_HLT').mode = 'EDIT'      

            # 3 - BOTTOM_RIGHT
            pie.separator()

            # 4 - TOP
            if context.mode == 'OBJECT':
                pie.operator("object.mode_set", text="編輯模式", icon='EDITMODE_HLT').mode = 'EDIT'
            elif context.mode == 'EDIT_ARMATURE':
                pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
            else:  # POSE mode
                pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'

            # 5 - TOP_RIGHT
            pie.separator()
           
            # 6 - RIGHT
            pie.separator()

            # 7 - TOP_LEFT
            pie.separator()

            # 8 - LEFT
            pie.separator()

        elif active.type == 'GREASEPENCIL':
            # LEFT (左) - Vertex Paint
            pie.operator("object.mode_set", text="頂點繪製", icon='VPAINT_HLT').mode = 'VERTEX_GREASE_PENCIL'

            # RIGHT (右) - Edit Mode
            pie.operator("object.mode_set", text="編輯模式", icon='EDITMODE_HLT').mode = 'EDIT'

            # BOTTOM (下) - Draw Mode
            pie.operator("object.mode_set", text="繪製模式", icon='GREASEPENCIL').mode = 'PAINT_GREASE_PENCIL'

            # TOP (上) - Object Mode
            pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'

            # TOP_LEFT (左上) - Sculpt Mode
            pie.operator("object.mode_set", text="雕刻模式", icon='SCULPTMODE_HLT').mode = 'SCULPT_GREASE_PENCIL'

            # TOP_RIGHT (右上) - Weight Paint
            pie.operator("object.mode_set", text="權重繪製", icon='WPAINT_HLT').mode = 'WEIGHT_GREASE_PENCIL'

            # 其他位置保持空白
            pie.separator()  # BOTTOM_LEFT (左下)
            pie.separator()  # BOTTOM_RIGHT (右下)

class PieSculptMode(Menu):
    bl_idname = "MODESWITCHER_MT_sculpt_pie"
    bl_label = "Sculpt Mode Switcher"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        pie.separator()  # LEFT
        pie.separator()  # RIGHT
        pie.separator()  # BOTTOM
        # 4 - TOP - Object Mode
        pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
        pie.separator()  # TOP_LEFT
        pie.separator()  # TOP_RIGHT
        pie.separator()  # BOTTOM_RIGHT
        pie.separator()  # BOTTOM_LEFT

class PieTexturePaintMode(Menu):
    bl_idname = "MODESWITCHER_MT_texture_paint_pie"
    bl_label = "Texture Paint Mode Switcher"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        pie.separator()  # LEFT
        pie.separator()  # RIGHT
        pie.separator()  # BOTTOM
        # 4 - TOP - Object Mode
        pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
        pie.separator()  # TOP_LEFT
        pie.separator()  # TOP_RIGHT
        pie.separator()  # BOTTOM_RIGHT
        pie.separator()  # BOTTOM_LEFT

class PieWeightPaintMode(Menu):
    bl_idname = "MODESWITCHER_MT_weight_paint_pie"
    bl_label = "Weight Paint Mode Switcher"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        pie.separator()  # LEFT
        pie.separator()  # RIGHT
        pie.separator()  # BOTTOM
        # 4 - TOP - Object Mode
        pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'
        pie.separator()  # TOP_LEFT
        pie.separator()  # TOP_RIGHT
        pie.separator()  # BOTTOM_RIGHT
        pie.separator()  # BOTTOM_LEFT

class PieVertexPaintMode(Menu):
    bl_idname = "MODESWITCHER_MT_vertex_paint_pie"
    bl_label = "Vertex Paint Mode Switcher"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        pie.separator()  # LEFT
        pie.separator()  # RIGHT
        pie.separator()  # BOTTOM
        pie.separator()  # LEFT (左)
        pie.separator()  # RIGHT (右)
        pie.separator()  # BOTTOM (下)
        pie.operator("object.mode_set", text="物體模式", icon='OBJECT_DATAMODE').mode = 'OBJECT'  # TOP (上)
        pie.separator()  # TOP_LEFT (左上)
        pie.separator()  # TOP_RIGHT (右上)
        pie.separator()  # BOTTOM_LEFT (左下)
        pie.separator()  # BOTTOM_RIGHT (右下)







