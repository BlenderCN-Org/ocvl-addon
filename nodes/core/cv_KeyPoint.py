import cv2
from bpy.props import IntProperty, FloatProperty, FloatVectorProperty

from ...extend.utils import cv_register_class, cv_unregister_class, OCVLNode, updateNode


class OCVLKeyPointNode(OCVLNode):
    pt_in = FloatVectorProperty(default=(10, 10), size=2, min=0, max=2048)
    size_in = FloatProperty(default=10, min=0, max=100, update=updateNode)
    angle_in = FloatProperty(default=-1, min=-1, max=360, update=updateNode)
    response_in = FloatProperty(default=0, min=0, max=100, update=updateNode)
    octave_in = IntProperty(default=0, min=0, max=100, update=updateNode)
    class_id_in = IntProperty(default=-1, min=-1, max=100, update=updateNode)


    def sv_init(self, context):
        self.inputs.new("StringsSocket", "pt_in").prop_name = "pt_in"
        self.inputs.new("StringsSocket", "size_in").prop_name = "size_in"
        self.inputs.new("StringsSocket", "angle_in").prop_name = "angle_in"
        self.inputs.new("StringsSocket", "response_in").prop_name = "response_in"
        self.inputs.new("StringsSocket", "octave_in").prop_name = "octave_in"
        self.inputs.new("StringsSocket", "class_id_in").prop_name = "class_id_in"
        self.outputs.new("StringsSocket", "key_point_out")

    def wrapped_process(self):
        pt_in = self.get_from_props("pt_in")
        x_in, y_in = pt_in


        kwargs = {
            'x_in': x_in,
            'y_in': y_in,
            '_size_in': self.get_from_props("size_in"),
            '_angle_in': self.get_from_props("angle_in"),
            '_response_in': self.get_from_props("response_in"),
            '_octave_in': self.get_from_props("octave_in"),
            '_class_id_in': self.get_from_props("class_id_in"),
            }

        key_point_out = self.process_cv(fn=cv2.KeyPoint, kwargs=kwargs)
        # key_point_out = cv2.KeyPoint(pt_in, size_in, angle_in, response_in, octave_in, class_id_in)
        self.refresh_output_socket("key_point_out", key_point_out, is_uuid_type=True)

    def draw_buttons(self, context, layout):
        pass


def register():
    cv_register_class(OCVLKeyPointNode)


def unregister():
    cv_unregister_class(OCVLKeyPointNode)
