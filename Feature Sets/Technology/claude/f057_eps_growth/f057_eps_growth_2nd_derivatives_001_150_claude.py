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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f057_eps_chg(eps, n):
    return eps.diff(periods=n)


# 21d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slope_21d_2d_v001_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slope_63d_2d_v002_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slope_126d_2d_v003_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slope_252d_2d_v004_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_slope_504d_2d_v005_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slope_21d_2d_v006_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slope_63d_2d_v007_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slope_126d_2d_v008_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slope_252d_2d_v009_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_slope_504d_2d_v010_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slope_21d_2d_v011_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slope_63d_2d_v012_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slope_126d_2d_v013_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slope_252d_2d_v014_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_slope_504d_2d_v015_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slope_21d_2d_v016_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slope_63d_2d_v017_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slope_126d_2d_v018_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slope_252d_2d_v019_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_slope_504d_2d_v020_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slope_21d_2d_v021_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slope_63d_2d_v022_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slope_126d_2d_v023_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slope_252d_2d_v024_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_slope_504d_2d_v025_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slope_21d_2d_v026_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slope_63d_2d_v027_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slope_126d_2d_v028_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slope_252d_2d_v029_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_slope_504d_2d_v030_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slope_21d_2d_v031_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slope_63d_2d_v032_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slope_126d_2d_v033_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slope_252d_2d_v034_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_slope_504d_2d_v035_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sm21_sl21_2d_v036_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sm63_sl21_2d_v037_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sm63_sl63_2d_v038_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sm252_sl63_2d_v039_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sm252_sl126_2d_v040_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sm21_sl21_2d_v041_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sm63_sl21_2d_v042_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sm63_sl63_2d_v043_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sm252_sl63_2d_v044_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sm252_sl126_2d_v045_signal(eps, closeadj):
    base = _mean(_f057_eps_chg(eps, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sm21_sl21_2d_v046_signal(eps, closeadj):
    base = _mean(eps.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sm63_sl21_2d_v047_signal(eps, closeadj):
    base = _mean(eps.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sm63_sl63_2d_v048_signal(eps, closeadj):
    base = _mean(eps.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sm252_sl63_2d_v049_signal(eps, closeadj):
    base = _mean(eps.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sm252_sl126_2d_v050_signal(eps, closeadj):
    base = _mean(eps.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sm21_sl21_2d_v051_signal(epsdil, closeadj):
    base = _mean(epsdil.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sm63_sl21_2d_v052_signal(epsdil, closeadj):
    base = _mean(epsdil.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sm63_sl63_2d_v053_signal(epsdil, closeadj):
    base = _mean(epsdil.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sm252_sl63_2d_v054_signal(epsdil, closeadj):
    base = _mean(epsdil.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sm252_sl126_2d_v055_signal(epsdil, closeadj):
    base = _mean(epsdil.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sm21_sl21_2d_v056_signal(eps, closeadj):
    base = _mean((np.sign(eps) != np.sign(eps.shift(252))).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sm63_sl21_2d_v057_signal(eps, closeadj):
    base = _mean((np.sign(eps) != np.sign(eps.shift(252))).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sm63_sl63_2d_v058_signal(eps, closeadj):
    base = _mean((np.sign(eps) != np.sign(eps.shift(252))).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sm252_sl63_2d_v059_signal(eps, closeadj):
    base = _mean((np.sign(eps) != np.sign(eps.shift(252))).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sm252_sl126_2d_v060_signal(eps, closeadj):
    base = _mean((np.sign(eps) != np.sign(eps.shift(252))).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sm21_sl21_2d_v061_signal(eps, closeadj):
    base = _mean((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sm63_sl21_2d_v062_signal(eps, closeadj):
    base = _mean((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sm63_sl63_2d_v063_signal(eps, closeadj):
    base = _mean((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sm252_sl63_2d_v064_signal(eps, closeadj):
    base = _mean((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sm252_sl126_2d_v065_signal(eps, closeadj):
    base = _mean((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sm21_sl21_2d_v066_signal(eps, closeadj):
    base = _mean((-eps).clip(lower=0).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sm63_sl21_2d_v067_signal(eps, closeadj):
    base = _mean((-eps).clip(lower=0).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sm63_sl63_2d_v068_signal(eps, closeadj):
    base = _mean((-eps).clip(lower=0).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sm252_sl63_2d_v069_signal(eps, closeadj):
    base = _mean((-eps).clip(lower=0).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sm252_sl126_2d_v070_signal(eps, closeadj):
    base = _mean((-eps).clip(lower=0).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_pctslope_21d_2d_v071_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_pctslope_63d_2d_v072_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_pctslope_252d_2d_v073_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_pctslope_21d_2d_v074_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_pctslope_63d_2d_v075_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_pctslope_252d_2d_v076_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_pctslope_21d_2d_v077_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_pctslope_63d_2d_v078_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_pctslope_252d_2d_v079_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_pctslope_21d_2d_v080_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_pctslope_63d_2d_v081_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_pctslope_252d_2d_v082_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_pctslope_21d_2d_v083_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_pctslope_63d_2d_v084_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_pctslope_252d_2d_v085_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_pctslope_21d_2d_v086_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_pctslope_63d_2d_v087_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_pctslope_252d_2d_v088_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_pctslope_21d_2d_v089_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_pctslope_63d_2d_v090_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_pctslope_252d_2d_v091_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sgnslope_21d_2d_v092_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sgnslope_63d_2d_v093_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_sgnslope_252d_2d_v094_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sgnslope_21d_2d_v095_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sgnslope_63d_2d_v096_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_sgnslope_252d_2d_v097_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sgnslope_21d_2d_v098_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sgnslope_63d_2d_v099_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_sgnslope_252d_2d_v100_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sgnslope_21d_2d_v101_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sgnslope_63d_2d_v102_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_sgnslope_252d_2d_v103_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sgnslope_21d_2d_v104_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sgnslope_63d_2d_v105_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_sgnslope_252d_2d_v106_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sgnslope_21d_2d_v107_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sgnslope_63d_2d_v108_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_sgnslope_252d_2d_v109_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sgnslope_21d_2d_v110_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sgnslope_63d_2d_v111_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_sgnslope_252d_2d_v112_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_logmagslope_21d_2d_v113_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_logmagslope_63d_2d_v114_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_logmagslope_252d_2d_v115_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_logmagslope_21d_2d_v116_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_logmagslope_63d_2d_v117_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_logmagslope_252d_2d_v118_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_logmagslope_21d_2d_v119_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_logmagslope_63d_2d_v120_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_logmagslope_252d_2d_v121_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_logmagslope_21d_2d_v122_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_logmagslope_63d_2d_v123_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_logmagslope_252d_2d_v124_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_logmagslope_21d_2d_v125_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_logmagslope_63d_2d_v126_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_logmagslope_252d_2d_v127_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_logmagslope_21d_2d_v128_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_logmagslope_63d_2d_v129_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_logmagslope_252d_2d_v130_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_logmagslope_21d_2d_v131_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_logmagslope_63d_2d_v132_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_logmagslope_252d_2d_v133_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_qoq_chg|
def f057epg_f057_eps_growth_eps_qoq_chg_logslope_63d_2d_v134_signal(eps, closeadj):
    base = np.log((_f057_eps_chg(eps, 63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_qoq_chg|
def f057epg_f057_eps_growth_eps_qoq_chg_logslope_252d_2d_v135_signal(eps, closeadj):
    base = np.log((_f057_eps_chg(eps, 63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_yoy_chg|
def f057epg_f057_eps_growth_eps_yoy_chg_logslope_63d_2d_v136_signal(eps, closeadj):
    base = np.log((_f057_eps_chg(eps, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_yoy_chg|
def f057epg_f057_eps_growth_eps_yoy_chg_logslope_252d_2d_v137_signal(eps, closeadj):
    base = np.log((_f057_eps_chg(eps, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_pct_y|
def f057epg_f057_eps_growth_eps_pct_y_logslope_63d_2d_v138_signal(eps, closeadj):
    base = np.log((eps.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_pct_y|
def f057epg_f057_eps_growth_eps_pct_y_logslope_252d_2d_v139_signal(eps, closeadj):
    base = np.log((eps.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|epsdil_yoy_chg|
def f057epg_f057_eps_growth_epsdil_yoy_chg_logslope_63d_2d_v140_signal(epsdil, closeadj):
    base = np.log((epsdil.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|epsdil_yoy_chg|
def f057epg_f057_eps_growth_epsdil_yoy_chg_logslope_252d_2d_v141_signal(epsdil, closeadj):
    base = np.log((epsdil.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_signflip|
def f057epg_f057_eps_growth_eps_signflip_logslope_63d_2d_v142_signal(eps, closeadj):
    base = np.log(((np.sign(eps) != np.sign(eps.shift(252))).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_signflip|
def f057epg_f057_eps_growth_eps_signflip_logslope_252d_2d_v143_signal(eps, closeadj):
    base = np.log(((np.sign(eps) != np.sign(eps.shift(252))).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_5y_cagr|
def f057epg_f057_eps_growth_eps_5y_cagr_logslope_63d_2d_v144_signal(eps, closeadj):
    base = np.log(((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_5y_cagr|
def f057epg_f057_eps_growth_eps_5y_cagr_logslope_252d_2d_v145_signal(eps, closeadj):
    base = np.log(((eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|eps_narrow_loss|
def f057epg_f057_eps_growth_eps_narrow_loss_logslope_63d_2d_v146_signal(eps, closeadj):
    base = np.log(((-eps).clip(lower=0).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|eps_narrow_loss|
def f057epg_f057_eps_growth_eps_narrow_loss_logslope_252d_2d_v147_signal(eps, closeadj):
    base = np.log(((-eps).clip(lower=0).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

