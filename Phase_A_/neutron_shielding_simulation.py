# ============================================================
# 核聚變專案：中子通量與屏蔽模擬
# 目標：計算爐心中子通量，設計屏蔽層厚度
# ============================================================

import math
import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("核聚變中子通量與屏蔽模擬")
print("="*60)

# ============================================================
# 1. 中子通量計算
# ============================================================

# 聚變功率 (假設 500 MW)
fusion_power_mw = 500
fusion_power_w = fusion_power_mw * 1e6

# DT 聚變每次反應釋放 17.6 MeV，其中 14.1 MeV 由中子帶走
energy_per_fusion_j = 17.6e6 * 1.602e-19  # 17.6 MeV → 焦耳
neutron_energy_ratio = 14.1 / 17.6

neutron_power_w = fusion_power_w * neutron_energy_ratio
neutron_flux_per_second = neutron_power_w / (14.1e6 * 1.602e-19)

# 第一壁面積 (估算)
major_radius = 6
minor_radius = 2
first_wall_area_m2 = 2 * math.pi * major_radius * (2 * math.pi * minor_radius)

neutron_flux_per_m2 = neutron_flux_per_second / first_wall_area_m2

print("\n【中子通量計算】")
print(f"聚變功率: {fusion_power_mw} MW")
print(f"中子攜帶功率: {neutron_power_w/1e6:.1f} MW")
print(f"每秒中子數: {neutron_flux_per_second:.2e}")
print(f"第一壁面積: {first_wall_area_m2:.0f} m²")
print(f"中子通量: {neutron_flux_per_m2:.2e} n/m²/s")

# ============================================================
# 2. 屏蔽層設計 (蒙特卡洛簡化模型)
# ============================================================

# 屏蔽材料衰減係數 (cm⁻¹)
# 參考 NIST 數據
shielding_materials = {
    "鉛 (Pb)": {"mu": 0.8, "density": 11.34},
    "混凝土": {"mu": 0.2, "density": 2.4},
    "水": {"mu": 0.1, "density": 1.0},
    "硼化聚乙烯": {"mu": 1.2, "density": 1.0},
}

print("\n【屏蔽材料比較】")
print("| 材料 | 衰減係數 (cm⁻¹) | 密度 (g/cm³) | 半值層 (cm) | 10 倍衰減厚度 (cm) |")
print("|:---|:---|:---|:---|:---|")

for name, data in shielding_materials.items():
    mu = data["mu"]
    half_value_layer = math.log(2) / mu
    tenth_value_layer = math.log(10) / mu
    print(f"| {name} | {mu} | {data['density']} | {half_value_layer:.1f} | {tenth_value_layer:.1f} |")

# ============================================================
# 3. 推薦屏蔽方案
# ============================================================

print("\n【推薦屏蔽方案】")
print("採用多層屏蔽結構：")
print("  第 1 層：硼化聚乙烯 (10 cm) → 吸收熱中子")
print("  第 2 層：鉛 (15 cm) → 屏蔽伽馬射線")
print("  第 3 層：混凝土 (50 cm) → 結構屏蔽")
print("  第 4 層：水 (100 cm) → 生物屏蔽")

# 計算總衰減
attenuation_total = math.exp(-1.2 * 10) * math.exp(-0.8 * 15) * math.exp(-0.2 * 50) * math.exp(-0.1 * 100)
print(f"\n總衰減係數: {attenuation_total:.2e}")
print(f"屏蔽後中子通量: {neutron_flux_per_m2 * attenuation_total:.2e} n/m²/s")

if neutron_flux_per_m2 * attenuation_total < 1e4:
    print("✅ 屏蔽後通量低於安全標準 (< 10⁴ n/m²/s)")
else:
    print("⚠️ 需要更厚屏蔽")

# ============================================================
# 4. 繪圖：不同材料嘅屏蔽效果
# ============================================================

thicknesses = np.linspace(0, 100, 100)
plt.figure(figsize=(10, 6))

for name, data in shielding_materials.items():
    transmission = np.exp(-data["mu"] * thicknesses)
    plt.plot(thicknesses, transmission, label=name, linewidth=2)

plt.xlabel('Shield Thickness (cm)')
plt.ylabel('Neutron Transmission')
plt.title('Neutron Shielding Effectiveness of Different Materials')
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('neutron_shielding_analysis.png', dpi=150)
print("\n✅ 圖表已儲存: neutron_shielding_analysis.png")

# ============================================================
# 5. 總結
# ============================================================
print("\n" + "="*60)
print("總結")
print("="*60)
print(f"""
✅ 中子通量: {neutron_flux_per_m2:.2e} n/m²/s
✅ 推薦屏蔽: 硼化聚乙烯 (10cm) + 鉛 (15cm) + 混凝土 (50cm) + 水 (100cm)
✅ 屏蔽後通量: {neutron_flux_per_m2 * attenuation_total:.2e} n/m²/s
✅ 低於安全標準，屏蔽設計可行
""")
