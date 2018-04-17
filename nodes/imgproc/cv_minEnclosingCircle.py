import cv2
import uuid
from bpy.props import StringProperty, BoolProperty

from ...utils import cv_register_class, cv_unregister_class, updateNode, OCVLNode


class OCVLminEnclosingCircleNode(OCVLNode):

    points_in = StringProperty(default=str(uuid.uuid4()),
        description="Input vector of 2D points, stored in std::vector\<\> or Mat")
    loc_from_findContours = BoolProperty(default=True, update=updateNode,
        description="If linked with findContour node switch to True")

    def sv_init(self, context):
        self.inputs.new("StringsSocket", "points_in")

        self.outputs.new("StringsSocket", "center_out")
        self.outputs.new("StringsSocket", "radius_out")

    def wrapped_process(self):
        self.check_input_requirements(["points_in"])

        kwargs = {
            'points_in': self.get_from_props("points_in")[0] if self.loc_from_findContours else self.get_from_props("points_in"),
            }

        (x, y), radius_out = self.process_cv(fn=cv2.minEnclosingCircle, kwargs=kwargs)
        self.refresh_output_socket("center_out", (int(x), int(y)))
        self.refresh_output_socket("radius_out", int(radius_out))

    def draw_buttons(self, context, layout):
        self.add_button(layout, 'loc_from_findContours')


def register():
    cv_register_class(OCVLminEnclosingCircleNode)


def unregister():
    cv_unregister_class(OCVLminEnclosingCircleNode)
