import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f032_dil_spread(shareswadil, sharesbas):
    return (shareswadil - sharesbas) / sharesbas.replace(0, np.nan).abs()


# 63d z-score of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_z_63d_base_v076_signal(shareswa, closeadj):
    base = shareswa
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_z_126d_base_v077_signal(shareswa, closeadj):
    base = shareswa
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_z_252d_base_v078_signal(shareswa, closeadj):
    base = shareswa
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_z_504d_base_v079_signal(shareswa, closeadj):
    base = shareswa
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_z_63d_base_v080_signal(shareswadil, closeadj):
    base = shareswadil
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_z_126d_base_v081_signal(shareswadil, closeadj):
    base = shareswadil
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_z_252d_base_v082_signal(shareswadil, closeadj):
    base = shareswadil
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_z_504d_base_v083_signal(shareswadil, closeadj):
    base = shareswadil
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dil_spread
def f032shd_f032_shares_diluted_dil_spread_z_63d_base_v084_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dil_spread
def f032shd_f032_shares_diluted_dil_spread_z_126d_base_v085_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dil_spread
def f032shd_f032_shares_diluted_dil_spread_z_252d_base_v086_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dil_spread
def f032shd_f032_shares_diluted_dil_spread_z_504d_base_v087_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_z_63d_base_v088_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_z_126d_base_v089_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_z_252d_base_v090_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_z_504d_base_v091_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_z_63d_base_v092_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_z_126d_base_v093_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_z_252d_base_v094_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_z_504d_base_v095_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_z_63d_base_v096_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_z_126d_base_v097_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_z_252d_base_v098_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_z_504d_base_v099_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_z_63d_base_v100_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_z_126d_base_v101_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_z_252d_base_v102_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_z_504d_base_v103_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_distmax_252d_base_v104_signal(shareswa, closeadj):
    base = shareswa
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_distmax_504d_base_v105_signal(shareswa, closeadj):
    base = shareswa
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_distmax_252d_base_v106_signal(shareswadil, closeadj):
    base = shareswadil
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_distmax_504d_base_v107_signal(shareswadil, closeadj):
    base = shareswadil
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dil_spread
def f032shd_f032_shares_diluted_dil_spread_distmax_252d_base_v108_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dil_spread
def f032shd_f032_shares_diluted_dil_spread_distmax_504d_base_v109_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_distmax_252d_base_v110_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_distmax_504d_base_v111_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_distmax_252d_base_v112_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_distmax_504d_base_v113_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_distmax_252d_base_v114_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_distmax_504d_base_v115_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_distmax_252d_base_v116_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_distmax_504d_base_v117_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_distmed_126d_base_v118_signal(shareswa, closeadj):
    base = shareswa
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_distmed_252d_base_v119_signal(shareswa, closeadj):
    base = shareswa
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_distmed_504d_base_v120_signal(shareswa, closeadj):
    base = shareswa
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_distmed_126d_base_v121_signal(shareswadil, closeadj):
    base = shareswadil
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_distmed_252d_base_v122_signal(shareswadil, closeadj):
    base = shareswadil
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_distmed_504d_base_v123_signal(shareswadil, closeadj):
    base = shareswadil
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_distmed_126d_base_v124_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_distmed_252d_base_v125_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_distmed_504d_base_v126_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_distmed_126d_base_v127_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_distmed_252d_base_v128_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_distmed_504d_base_v129_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_distmed_126d_base_v130_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_distmed_252d_base_v131_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_distmed_504d_base_v132_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_distmed_126d_base_v133_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_distmed_252d_base_v134_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_distmed_504d_base_v135_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_distmed_126d_base_v136_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_distmed_252d_base_v137_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_distmed_504d_base_v138_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_chg_63d_base_v139_signal(shareswa, closeadj):
    base = shareswa
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_chg_252d_base_v140_signal(shareswa, closeadj):
    base = shareswa
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_chg_63d_base_v141_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_chg_252d_base_v142_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dil_spread
def f032shd_f032_shares_diluted_dil_spread_chg_63d_base_v143_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dil_spread
def f032shd_f032_shares_diluted_dil_spread_chg_252d_base_v144_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_chg_63d_base_v145_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_chg_252d_base_v146_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_chg_63d_base_v147_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_chg_252d_base_v148_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_chg_63d_base_v149_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_chg_252d_base_v150_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

