import uuid

import bpy
import cv2
from ocvl.core.node_base import OCVLNodeBase, update_node


class OCVLdctNode(OCVLNodeBase):

    bl_flags_list = 'DCT_INVERSE, DCT_ROWS'
    n_doc = "Performs a forward or inverse discrete Cosine transform of 1D or 2D array."

    src_in: bpy.props.StringProperty(name="src_in", default=str(uuid.uuid4()), description="Input floating-point array.")
    flags_in: bpy.props.BoolVectorProperty(default=[False for i in bl_flags_list.split(",")], size=len(bl_flags_list.split(",")), update=update_node, subtype="NONE", description=bl_flags_list)

    dst_out: bpy.props.StringProperty(name="dst_out", default=str(uuid.uuid4()), description="Output array of the same size and type as src.")

    def init(self, context):
        self.inputs.new("StringsSocket", "src_in")

        self.outputs.new("StringsSocket", "dst_out")

    def wrapped_process(self):
        self.check_input_requirements(["src_in"])
        kwargs = {
            'src_in': self.get_from_props("src_in"),
            'flags_in': self.get_from_props("flags_in"),
            }

        dst_out = self.process_cv(fn=cv2.dct, kwargs=kwargs)
        self.refresh_output_socket("dst_out", dst_out, is_uuid_type=True)

    def draw_buttons(self, context, layout):
        self.add_button(layout, "flags_in")
