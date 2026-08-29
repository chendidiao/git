"""
正弦函数 y = sin(x) 图像生成
遵循 dataviz 可视化规范：蓝色曲线、浅色网格、关键点标注
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# ── 0. 配置中文字体 ──────────────────────────────────
# 尝试常见中文字体，找不到则回退默认
_cn_fonts = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "WenQuanYi Micro Hei", "PingFang SC"]
_available = {f.name for f in font_manager.fontManager.ttflist}
_cn_family = next((f for f in _cn_fonts if f in _available), None)

if _cn_family:
    plt.rcParams["font.family"] = _cn_family
plt.rcParams["axes.unicode_minus"] = False

# ── 1. 全局样式（dataviz 规范） ──────────────────────
SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
BASELINE = "#c3c2b7"
SERIES_BLUE = "#2a78d6"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "axes.edgecolor": BASELINE,
    "axes.linewidth": 1.0,
    "axes.grid": True,
    "grid.color": GRIDLINE,
    "grid.linewidth": 0.5,
    "grid.alpha": 1.0,
    "xtick.color": INK_MUTED,
    "ytick.color": INK_MUTED,
    "text.color": INK_SECONDARY,
    "axes.labelcolor": INK_SECONDARY,
    "axes.titlecolor": INK_PRIMARY,
})

# ── 2. 数据 ──────────────────────────────────────────
x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
y = np.sin(x)

# ── 3. 绘图 ──────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor(SURFACE)

# 主曲线：2px 蓝线
ax.plot(x, y, color=SERIES_BLUE, linewidth=2, solid_capstyle="round", zorder=3)

# y=0 基线加粗
ax.axhline(y=0, color=BASELINE, linewidth=1, zorder=1)

# x 轴标签（π 刻度）
x_ticks = [-2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
x_labels = ["−2π", "−π", "−π/2", "0", "π/2", "π", "3π/2", "2π"]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, fontsize=11)
ax.set_xlim(-2*np.pi, 2*np.pi)

# y 轴
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_ylim(-1.4, 1.4)
ax.tick_params(axis="both", labelsize=10, pad=6)

# 轴标签
ax.set_xlabel("x", fontsize=12, labelpad=8)
ax.set_ylabel("y", fontsize=12, labelpad=8)

# 标题
ax.set_title("正弦函数  y = sin(x)", fontsize=16, fontweight="bold", pad=16)

# ── 4. 关键点标注 ────────────────────────────────────
# 标注极大值
ax.annotate(
    "极大值 1", xy=(np.pi/2, 1), xytext=(np.pi/2, 1.18),
    fontsize=10, color=INK_SECONDARY, ha="center",
    arrowprops=dict(arrowstyle="->", color=INK_MUTED, lw=0.8, connectionstyle="arc3,rad=0"),
)

# 标注极小值
ax.annotate(
    "极小值 −1", xy=(-np.pi/2, -1), xytext=(-np.pi/2, -1.22),
    fontsize=10, color=INK_SECONDARY, ha="center",
    arrowprops=dict(arrowstyle="->", color=INK_MUTED, lw=0.8, connectionstyle="arc3,rad=0"),
)

# 标记五个关键点（圆点 + 表面色环 = 2px ring）
key_x = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
for kx in key_x:
    ax.plot(kx, np.sin(kx), "o", color=SERIES_BLUE, markersize=9,
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)

# ── 5. 图例（单系列无需图例，直接标题命名） ────────────

# ── 6. 保存 ──────────────────────────────────────────
fig.tight_layout(pad=1.5)
fig.savefig(
    "高等数学/sine_wave.png",
    dpi=150,
    facecolor=SURFACE,
    edgecolor="none",
    bbox_inches="tight",
)
plt.close(fig)
print("PNG saved: 高等数学/sine_wave.png")
