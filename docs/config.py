import os

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

LOGS_DIR = os.path.join(ROOT_DIR, "logs")

ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
ASSETS_VHP_DIR = os.path.join(ASSETS_DIR, "vhp")
ASSETS_VHP_CT_DIR = os.path.join(ASSETS_VHP_DIR, "(VKH) CT Images (494 X 281)")
ASSETS_VHP_SEG_DIR = os.path.join(ASSETS_VHP_DIR, "(VKH) Segmented Images (1,000 X 570)")
ASSETS_ALIGNMENT_DIR = os.path.join(ASSETS_DIR, "alignment")
ASSETS_ALIGNMENT_CT_DIR = os.path.join(ASSETS_ALIGNMENT_DIR, "CT Image (494 x 281)")
ASSETS_ALIGNMENT_CT_RESIZE_DIR = os.path.join(ASSETS_ALIGNMENT_DIR, "CT Image Resize (1000 x 570)")

MAIN_DIR = os.path.join(ROOT_DIR, "main")
MAIN_RESOURCES_DIR = os.path.join(MAIN_DIR, "resources")
MAIN_RESOURCES_LTR_DIR = os.path.join(MAIN_RESOURCES_DIR, "LiverTumorResection")
MAIN_RESOURCES_VHP_DIR = os.path.join(MAIN_RESOURCES_DIR, "VisibleHumanProject")
MAIN_RESOURCES_ACP_DIR = os.path.join(MAIN_RESOURCES_DIR, "AbdominalCavityProject")
