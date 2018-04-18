import cv2
import uuid
from gettext import gettext as _
from bpy.props import EnumProperty, StringProperty, IntProperty

from ...utils import cv_register_class, cv_unregister_class, OCVLNode, CODE_COLOR_POOR_ITEMS, updateNode


class OCVLcvtColorNode(OCVLNode):
    bl_icon = 'COLOR'

    _doc=_("Converts an image from one color space to another.")

    image_in = StringProperty(name="image_in", default=str(uuid.uuid4()), description=_("Input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point."))
    image_out = StringProperty(name="image_out", default=str(uuid.uuid4()), description=_("Output image of the same size and depth as input image."))

    code_in = EnumProperty(items=CODE_COLOR_POOR_ITEMS, default='COLOR_BGR2GRAY', update=updateNode,
        description=_("Color space conversion code (see cv::ColorConversionCodes)."))
    dstCn_in = IntProperty(default=0, update=updateNode, min=0, max=4,
        description=_("Number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from input image and code."))

    def sv_init(self, context):
        self.inputs.new("StringsSocket", "image_in")
        self.inputs.new("StringsSocket", "code_in").prop_name = "code_in"
        self.inputs.new("StringsSocket", "dstCn_in").prop_name = "dstCn_in"

        self.outputs.new("StringsSocket", "image_out")

    def wrapped_process(self):
        self.check_input_requirements(["image_in"])

        kwargs = {
            'src': self.get_from_props("image_in"),
            'code_in': self.get_from_props("code_in"),
            'dstCn_in': self.get_from_props("dstCn_in"),
            }

        image_out = self.process_cv(fn=cv2.cvtColor, kwargs=kwargs)
        self.refresh_output_socket("image_out", image_out, is_uuid_type=True)

    def draw_buttons(self, context, layout):
        pass


def register():
    cv_register_class(OCVLcvtColorNode)


def unregister():
    cv_unregister_class(OCVLcvtColorNode)
