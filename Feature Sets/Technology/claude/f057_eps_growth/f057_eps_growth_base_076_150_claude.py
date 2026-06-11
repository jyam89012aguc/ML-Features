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
def _f057_eps_chg(eps, n):
    return eps.diff(periods=n)


# 63d z-score of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_z_63d_base_v076_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_z_126d_base_v077_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_z_252d_base_v078_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_z_504d_base_v079_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_z_63d_base_v080_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_z_126d_base_v081_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_z_252d_base_v082_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_z_504d_base_v083_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_z_63d_base_v084_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_z_126d_base_v085_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_z_252d_base_v086_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_z_504d_base_v087_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_z_63d_base_v088_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_z_126d_base_v089_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_z_252d_base_v090_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_z_504d_base_v091_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_z_63d_base_v092_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_z_126d_base_v093_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_z_252d_base_v094_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_z_504d_base_v095_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_z_63d_base_v096_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_z_126d_base_v097_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_z_252d_base_v098_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_z_504d_base_v099_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_z_63d_base_v100_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_z_126d_base_v101_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_z_252d_base_v102_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_z_504d_base_v103_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_distmax_252d_base_v104_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_distmax_504d_base_v105_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_distmax_252d_base_v106_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_distmax_504d_base_v107_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_distmax_252d_base_v108_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_distmax_504d_base_v109_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_distmax_252d_base_v110_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_distmax_504d_base_v111_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_distmax_252d_base_v112_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_distmax_504d_base_v113_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_distmax_252d_base_v114_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_distmax_504d_base_v115_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_distmax_252d_base_v116_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_distmax_504d_base_v117_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_distmed_126d_base_v118_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_distmed_252d_base_v119_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_distmed_504d_base_v120_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_distmed_126d_base_v121_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_distmed_252d_base_v122_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_distmed_504d_base_v123_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_distmed_126d_base_v124_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_distmed_252d_base_v125_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_distmed_504d_base_v126_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_distmed_126d_base_v127_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_distmed_252d_base_v128_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_distmed_504d_base_v129_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_distmed_126d_base_v130_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_distmed_252d_base_v131_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_distmed_504d_base_v132_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_distmed_126d_base_v133_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_distmed_252d_base_v134_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_distmed_504d_base_v135_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_distmed_126d_base_v136_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_distmed_252d_base_v137_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_distmed_504d_base_v138_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_chg_63d_base_v139_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_chg_252d_base_v140_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_chg_63d_base_v141_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_chg_252d_base_v142_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_chg_63d_base_v143_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_chg_252d_base_v144_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_chg_63d_base_v145_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_chg_252d_base_v146_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_signflip
def f057epg_f057_eps_growth_eps_signflip_chg_63d_base_v147_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_signflip
def f057epg_f057_eps_growth_eps_signflip_chg_252d_base_v148_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_chg_63d_base_v149_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_chg_252d_base_v150_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

