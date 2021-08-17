import os

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

LOGS_DIR = os.path.join(ROOT_DIR, "logs")

ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
ASSETS_VHP_DIR = os.path.join(ASSETS_DIR, "vhp")
ASSETS_VHP_CT_DIR = os.path.join(ASSETS_VHP_DIR, "(VKH) CT Images (494 X 281)")
ASSETS_VHP_SEG_DIR = os.path.join(ASSETS_VHP_DIR, "(VKH) Segmented Images (1,000 X 570)")
ASSETS_LTR_DIR = os.path.join(ASSETS_DIR, "ltr")
ASSETS_LTR_VE_DIR = os.path.join(ASSETS_LTR_DIR, "vhp_extract")
ASSETS_LTR_VE_CT_DIR = os.path.join(ASSETS_LTR_VE_DIR, "ct")
ASSETS_LTR_VE_SEG_DIR = os.path.join(ASSETS_LTR_VE_DIR, "seg")

MAIN_DIR = os.path.join(ROOT_DIR, "main")
MAIN_RESOURCES_DIR = os.path.join(MAIN_DIR, "resources")
MAIN_RESOURCES_LTR_DIR = os.path.join(MAIN_RESOURCES_DIR, "LiverTumorResection")
MAIN_RESOURCES_VHP_DIR = os.path.join(MAIN_RESOURCES_DIR, "VisibleHumanProject")
