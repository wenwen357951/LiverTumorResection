import os

import docs.config as config
import trclab.vhp as vhp

if __name__ == '__main__':
    # 讀取標籤
    vhp_label = vhp.OrganLabel(os.path.join(config.MAIN_RESOURCES_LTR_DIR, "original_label.txt"))
    # 讀入資料集
    seg_dataset = vhp.OrganDataset(config.ASSETS_LTR_VE_SEG_DIR, "*.bmp")
    # 設置標籤
    seg_dataset.set_label(vhp_label)
    # 匯出標記區域根據目標圖片(映射圖片)至輸出位置
    seg_dataset.export_label_area(config.ASSETS_LTR_VE_CT_DIR, "*.jpg",
                                  os.path.join(config.LOGS_DIR, 'ltr_ct.json'))
