import os

import docs.config as config
import trclab.vhp as vhp

if __name__ == '__main__':
    seg_dataset = vhp.OrganDataset(config.ASSETS_LTR_VE_SEG_DIR, "*.bmp")
    vhp_label = vhp.OrganLabel(os.path.join(config.MAIN_RESOURCES_LTR_DIR, "original_label.txt"))
    seg_dataset.set_label(vhp_label)
    seg_dataset.export_label_area(config.ASSETS_LTR_VE_CT_DIR, "*.jpg",
                                  os.path.join(config.LOGS_DIR, 'ltr_ct.json'))
