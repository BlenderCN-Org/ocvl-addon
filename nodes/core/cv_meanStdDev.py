import cv2
import uuid
from gettext import gettext as _
from bpy.props import StringProperty

from ...extend.utils import cv_register_class, cv_unregister_class, OCVLNode, DEVELOP_STATE_BETA


class OCVLmeanStdDevNode(OCVLNode):
    bl_develop_state = DEVELOP_STATE_BETA

    _doc = _("Calculates a mean and standard deviation of array elements.")

    src_in = StringProperty(name="src_in", default=str(uuid.uuid4()),
        description=_("Input array that should have from 1 to 4 channels so that the results can be stored in Scalar_ ‘s."))
    mask_in = StringProperty(name="mask_in", default=str(uuid.uuid4()),
        description=_("Optional operation mask."))

    mean_out = StringProperty(name="array_out", default=str(uuid.uuid4()),
        description=_("Output parameter: calculated mean value."))
    stddev_out = StringProperty(name="array_out", default=str(uuid.uuid4()),
        description=_("Output parameter: calculateded standard deviation."))

    def sv_init(self, context):
        self.inputs.new("StringsSocket", "src_in")
        self.inputs.new("StringsSocket", "mask_in")
        self.outputs.new("StringsSocket", "mean_out")
        self.outputs.new("StringsSocket", "stddev_out")

    def wrapped_process(self):
        self.check_input_requirements(["src_in"])

        kwargs = {
            'src_in': self.get_from_props("src_in"),
            'mask_in': self.get_from_props("mask_in"),
            }
        if isinstance(kwargs['mask_in'], str):
            kwargs.pop('mask_in')

        mean_out, stddev_out = self.process_cv(fn=cv2.meanStdDev, kwargs=kwargs)
        self.refresh_output_socket("mean_out", mean_out, is_uuid_type=True)
        self.refresh_output_socket("stddev_out", stddev_out, is_uuid_type=True)

    def draw_buttons(self, context, layout):
        pass


def register():
    cv_register_class(OCVLmeanStdDevNode)


def unregister():
    cv_unregister_class(OCVLmeanStdDevNode)
