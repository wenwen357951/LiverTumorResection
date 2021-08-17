# LiverTumorResection

## VHP Lib
###產生 MaskRCNN 資料集之 JSON 標記檔案

1. 請先匯入函式庫
```
import trclab.vhp as vhp
```
2. 載入色塊切片資料集圖片
```
seg_dataset = vhp.OrganDataset(config.ASSETS_LTR_VE_SEG_DIR, "*.bmp")
```
3. 載入顏色區域標籤檔案，並設置為資料集標籤
```
vhp_label = vhp.OrganLabel(os.path.join(config.MAIN_RESOURCES_LTR_DIR, "original_label.txt"))
seg_dataset.set_label(vhp_label)
```
4. 匯出資料集之 JSON 標記檔案
```
# 參數說明(依照順序)
# 1. 需產生標記檔案之目標資料夾
# 2. 檔案搜尋模板
# 3. 輸出檔案位置
seg_dataset.export_label_area(config.ASSETS_LTR_VE_CT_DIR, "*.jpg", os.path.join(config.LOGS_DIR, 'ltr_ct.json'))
```
