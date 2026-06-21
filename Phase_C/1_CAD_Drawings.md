# 核聚變專案 Phase C：CAD 圖紙說明

**版本：1.0**  
**更新日期：2026-06-01**

---

## 1. 需要繪製嘅 3D 模型

| # | 組件 | 說明 | 優先級 |
|:---|:---|:---|:---|
| 1 | 小爐 (Reactor Cartridge) | 1m x 1m x 1m，5 層結構 | 高 |
| 2 | 機械臂 | 6 自由度，負載 5 噸 | 高 |
| 3 | 反應堆容器 | 直徑 20 米，高 30 米 | 高 |
| 4 | 冷卻迴路 | PbLi + sCO₂ 管線 | 中 |
| 5 | 渦輪發電機 | 500 MWe 級 | 中 |

---

## 2. 小爐 (Reactor Cartridge) 規格

| 參數 | 數值 |
|:---|:---|
| 尺寸 | 1m x 1m x 1m |
| 質量 | 約 2 噸 |
| 外殼材料 | 不鏽鋼 (2 cm) |
| 第一壁材料 | ODS Steel (2 cm) |
| 聚變燃料層 | DT 冰 + 鋰 (5 cm) |
| 裂變包層 | 貧鈾 / 釷 (20 cm) |
| 屏蔽層 | 碳化硼 B₄C (5 cm) |

### 2.1 需要繪製嘅視圖
- 正視圖、側視圖、俯視圖
- 3D 等角視圖
- 層疊結構剖面圖 (5 層)
- 冷卻管接頭細節圖

---

## 3. 機械臂規格

| 參數 | 數值 |
|:---|:---|
| 類型 | 6 自由度關節式 |
| 負載能力 | 5 噸 |
| 工作半徑 | 10 米 |
| 重複精度 | ±0.5 mm |
| 數量 | 4 台 (2 主 + 2 備) |

### 3.1 需要繪製嘅視圖
- 機械臂整體外觀
- 夾爪細節圖
- 軌道系統佈置圖

---

## 4. 反應堆容器規格

| 參數 | 數值 |
|:---|:---|
| 類型 | 鋼結構容器 |
| 直徑 | 20 米 |
| 高度 | 30 米 |
| 壁厚 | 0.5 米 |
| 材料 | 低活化鋼 |
| 內部 | 超導磁體、屏蔽層 |

### 4.1 需要繪製嘅視圖
- 容器整體剖面圖
- 小爐陣列佈置圖 (700 個)
- 磁體位置圖

---

## 5. 3D 模型

使用 Meshy AI 生成嘅核聚變小爐 3D 模型：

🔗 [Meshy 模型連結](https://www.meshy.ai/s/wpWnR9)

**生成提示詞**：
Generate a 3D model of a 1 cubic meter nuclear fusion reactor cartridge. It is a cube with a 5-layer structure. The outer shell is stainless steel. Inside there is a fusion fuel layer and a fission blanket. The top has cooling pipe connectors. The overall appearance is industrial, metallic grey.

---

## 6. 下一步

- [ ] 完成材料清單 (2_BOM.md)
- [ ] 完成製造流程 (3_Manufacturing_Process.md)
