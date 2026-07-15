import bpy
from bpy.props import StringProperty

class EditMode(bpy.types.Operator):
    bl_idname = "modeswitcher.edit_mode"
    bl_label = "Edit Mode"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        active = context.active_object
        return active and not active.override_library

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

class MeshMode(bpy.types.Operator):
    bl_idname = "modeswitcher.mesh_mode"
    bl_label = "Mesh Mode"
    bl_options = {'REGISTER', 'UNDO'}

    mode: StringProperty()

    @classmethod
    def poll(cls, context):
        if context.mode in ['OBJECT', 'EDIT_MESH']:
            active = context.active_object
            if active and active.type == 'MESH':
                return not active.override_library
        return False

    def execute(self, context):
        if context.mode == "OBJECT":
            bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type=self.mode)
        return {'FINISHED'}