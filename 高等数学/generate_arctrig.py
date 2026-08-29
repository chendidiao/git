"""
反三角函数图像生成(六大主值分支)
遵循 dataviz 可视化规范：色板前 6 槽、浅色网格、端点/渐近线/关键信息标注
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# ── 0. 配置中文字体 ──────────────────────────────────
_cn_fonts = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "WenQuanYi Micro Hei", "PingFang SC"]
_available = {f.name for f in font_manager.fontManager.ttflist}
_cn_family = next((f for f in _cn_fonts if f in _available), None)
if _cn_family:
    plt.rcParams["font.family"] = _cn_family
plt.rcParams["axes.unicode_minus"] = False

# ── 1. 全局样式(dataviz 规范) ────────────────────────
SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
BASELINE = "#c3c2b7"
# 分类色板前 6 槽(已验证 CVD 安全顺序)
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]

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

PI = np.pi
HALF = PI / 2


# ── 2. 绘图辅助函数 ──────────────────────────────────
def origin_axes(ax):
    """加粗 x=0 / y=0 轴线"""
    ax.axhline(0, color=BASELINE, linewidth=1, zorder=1)
    ax.axvline(0, color=BASELINE, linewidth=1, zorder=1)


def pi_yticks(ax, ticks):
    """π 分式刻度标签"""
    m = {0: "0", HALF: "π/2", PI: "π", -HALF: "−π/2", -PI: "−π"}
    ax.set_yticks(ticks)
    ax.set_yticklabels([m.get(t, str(t)) for t in ticks], fontsize=10)


def xticks(ax, ticks):
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{t:g}" for t in ticks], fontsize=10)


def dot(ax, x, y, color, size=8):
    """端点/关键点(表面色环, 2px ring)"""
    ax.plot(x, y, "o", color=color, markersize=size,
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)


def asymptote(ax, y, xlim, label=None, dy=0.16):
    """水平渐近线 + 标注(上侧线标上方, 下侧线标下方, 避免与曲线重叠)"""
    ax.axhline(y, color=INK_MUTED, linewidth=1.0, linestyle=(0, (5, 4)), zorder=2)
    if label is not None:
        if y > 0:
            ax.text(xlim[1] - 0.18, y + dy, label, fontsize=9, color=INK_MUTED,
                    ha="right", va="bottom", zorder=6)
        else:
            ax.text(xlim[1] - 0.18, y - dy, label, fontsize=9, color=INK_MUTED,
                    ha="right", va="top", zorder=6)


def info(ax, text, x, y):
    """左上角信息卡: 定义域/值域/性质"""
    ax.text(x, y, text, fontsize=9.5, color=INK_SECONDARY, ha="left", va="top",
            linespacing=1.7, zorder=6,
            bbox=dict(boxstyle="round,pad=0.35", facecolor=SURFACE,
                      edgecolor=BASELINE, linewidth=0.8, alpha=0.92))


def title(ax, s):
    ax.set_title(s, fontsize=13.5, fontweight="bold", pad=10)


# ── 3. 六大反三角函数 ────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15.5, 9.6), constrained_layout=True)

# ── (1) y = arcsin x ──────────────────────────────
ax = axes[0, 0]
x = np.linspace(-1, 1, 500)
ax.plot(x, np.arcsin(x), color=PALETTE[0], linewidth=2.2, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-1, -0.5, 0, 0.5, 1])
pi_yticks(ax, [-HALF, 0, HALF])
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.98, 1.98)
dot(ax, -1, -HALF, PALETTE[0]); dot(ax, 0, 0, PALETTE[0]); dot(ax, 1, HALF, PALETTE[0])
info(ax, "定义域  [−1, 1]\n值域  [−π/2, π/2]\n奇函数 · 单调递增", -1.42, 1.88)
title(ax, "y = arcsin x")

# ── (2) y = arccos x ──────────────────────────────
ax = axes[0, 1]
x = np.linspace(-1, 1, 500)
ax.plot(x, np.arccos(x), color=PALETTE[1], linewidth=2.2, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-1, -0.5, 0, 0.5, 1])
pi_yticks(ax, [0, HALF, PI])
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.45, 3.68)
dot(ax, -1, PI, PALETTE[1]); dot(ax, 0, HALF, PALETTE[1]); dot(ax, 1, 0, PALETTE[1])
info(ax, "定义域  [−1, 1]\n值域  [0, π]\n单调递减", -1.42, 3.56)
title(ax, "y = arccos x")

# ── (3) y = arctan x ──────────────────────────────
ax = axes[0, 2]
x = np.linspace(-5, 5, 900)
ax.plot(x, np.arctan(x), color=PALETTE[2], linewidth=2.2, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-4, -2, 0, 2, 4])
pi_yticks(ax, [-HALF, 0, HALF])
ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-2.15, 2.15)
asymptote(ax, HALF, (-5.2, 5.2), label="y = π/2")
asymptote(ax, -HALF, (-5.2, 5.2), label="y = −π/2")
dot(ax, 0, 0, PALETTE[2])
info(ax, "定义域  (−∞, +∞)\n值域  (−π/2, π/2)\n奇函数 · 单调递增\n渐近线  y = ±π/2", -5.1, 2.05)
title(ax, "y = arctan x")

# ── (4) y = arccot x ──────────────────────────────
ax = axes[1, 0]
x = np.linspace(-5, 5, 900)
ax.plot(x, HALF - np.arctan(x), color=PALETTE[3], linewidth=2.6, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-4, -2, 0, 2, 4])
pi_yticks(ax, [0, HALF, PI])
ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-0.62, 3.68)
asymptote(ax, 0, (-5.2, 5.2), label="y = 0")
asymptote(ax, PI, (-5.2, 5.2), label="y = π")
dot(ax, 0, HALF, PALETTE[3])
info(ax, "定义域  (−∞, +∞)\n值域  (0, π)\n单调递减\n渐近线  y = 0, y = π", -5.1, 0.5)
title(ax, "y = arccot x")

# ── (5) y = arcsec x ──────────────────────────────
ax = axes[1, 1]
xr = np.linspace(1, 5, 700)
xl = np.linspace(-5, -1, 700)
ax.plot(xr, np.arccos(1 / xr), color=PALETTE[4], linewidth=2.2, solid_capstyle="round", zorder=3)
ax.plot(xl, np.arccos(1 / xl), color=PALETTE[4], linewidth=2.2, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-4, -2, 0, 2, 4])
pi_yticks(ax, [0, HALF, PI])
ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-0.45, 3.68)
asymptote(ax, HALF, (-5.2, 5.2), label="y = π/2")
dot(ax, -1, PI, PALETTE[4]); dot(ax, 1, 0, PALETTE[4])
info(ax, "定义域  (−∞, −1] ∪ [1, +∞)\n值域  [0, π/2) ∪ (π/2, π]\n两支均单调递增", -5.1, 3.56)
title(ax, "y = arcsec x")

# ── (6) y = arccsc x ──────────────────────────────
ax = axes[1, 2]
xr = np.linspace(1, 5, 700)
xl = np.linspace(-5, -1, 700)
ax.plot(xr, np.arcsin(1 / xr), color=PALETTE[5], linewidth=2.2, solid_capstyle="round", zorder=3)
ax.plot(xl, np.arcsin(1 / xl), color=PALETTE[5], linewidth=2.2, solid_capstyle="round", zorder=3)
origin_axes(ax)
xticks(ax, [-4, -2, 0, 2, 4])
pi_yticks(ax, [-HALF, 0, HALF])
ax.set_xlim(-5.2, 5.2)
ax.set_ylim(-2.15, 2.15)
asymptote(ax, 0, (-5.2, 5.2), label="y = 0")
dot(ax, -1, -HALF, PALETTE[5]); dot(ax, 1, HALF, PALETTE[5])
info(ax, "定义域  (−∞, −1] ∪ [1, +∞)\n值域  [−π/2, 0) ∪ (0, π/2]\n奇函数 · 两支均单调递增", -5.1, 2.05)
title(ax, "y = arccsc x")

# ── 4. 总标题与保存 ─────────────────────────────────
fig.suptitle("六大反三角函数图像(主值分支)", fontsize=16, fontweight="bold")
fig.savefig(
    "高等数学/arctrig_overview.png",
    dpi=170,
    facecolor=SURFACE,
    edgecolor="none",
    bbox_inches="tight",
)
plt.close(fig)
print("PNG saved: 高等数学/arctrig_overview.png")
