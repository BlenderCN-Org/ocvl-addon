import os

TUTORIAL_ENGINE_VERSION = "0.1.0"
TUTORIAL_ENGINE_PORT = 4000
TUTORIAL_ENGINE_DEFAULT_NODE_TREE_NAME = 'TutorialNodeTree'
TUTORIAL_ENGINE_DEFAULT_IMAGE_SAMPLE_NAME = 'OCVLImageSampleNode'
TUTORIAL_ENGINE_DEFAULT_VIEWER_NAME = 'OCVLImageViewerNode'
TUTORIAL_ENGINE_DEFAULT_INPUT_NAME = 'image_in'
TUTORIAL_ENGINE_DEFAULT_OUTPUT_NAME = 'image_out'
TUTORIAL_HEARTBEAT_INTERVAL = 0.5

current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
TUTORIAL_ASSETS_PATH = os.path.abspath(os.path.join(current_dir, "../tutorials"))