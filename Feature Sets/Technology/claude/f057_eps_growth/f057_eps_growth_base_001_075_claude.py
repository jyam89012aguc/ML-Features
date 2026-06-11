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


# 21d mean of eps_qoq_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_qoq_chg_mean_21d_base_v001_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_qoq_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_qoq_chg_mean_63d_base_v002_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_qoq_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_qoq_chg_mean_126d_base_v003_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_qoq_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_qoq_chg_mean_252d_base_v004_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_qoq_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_qoq_chg_mean_504d_base_v005_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_yoy_chg_mean_21d_base_v006_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_yoy_chg_mean_63d_base_v007_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_yoy_chg_mean_126d_base_v008_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_yoy_chg_mean_252d_base_v009_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_eps_yoy_chg_mean_504d_base_v010_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_pct_y scaled by closeadj
def f057epg_f057_eps_growth_eps_pct_y_mean_21d_base_v011_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_pct_y scaled by closeadj
def f057epg_f057_eps_growth_eps_pct_y_mean_63d_base_v012_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_pct_y scaled by closeadj
def f057epg_f057_eps_growth_eps_pct_y_mean_126d_base_v013_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_pct_y scaled by closeadj
def f057epg_f057_eps_growth_eps_pct_y_mean_252d_base_v014_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_pct_y scaled by closeadj
def f057epg_f057_eps_growth_eps_pct_y_mean_504d_base_v015_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of epsdil_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_epsdil_yoy_chg_mean_21d_base_v016_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of epsdil_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_epsdil_yoy_chg_mean_63d_base_v017_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of epsdil_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_epsdil_yoy_chg_mean_126d_base_v018_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of epsdil_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_epsdil_yoy_chg_mean_252d_base_v019_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of epsdil_yoy_chg scaled by closeadj
def f057epg_f057_eps_growth_epsdil_yoy_chg_mean_504d_base_v020_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_signflip scaled by closeadj
def f057epg_f057_eps_growth_eps_signflip_mean_21d_base_v021_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_signflip scaled by closeadj
def f057epg_f057_eps_growth_eps_signflip_mean_63d_base_v022_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_signflip scaled by closeadj
def f057epg_f057_eps_growth_eps_signflip_mean_126d_base_v023_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_signflip scaled by closeadj
def f057epg_f057_eps_growth_eps_signflip_mean_252d_base_v024_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_signflip scaled by closeadj
def f057epg_f057_eps_growth_eps_signflip_mean_504d_base_v025_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_5y_cagr scaled by closeadj
def f057epg_f057_eps_growth_eps_5y_cagr_mean_21d_base_v026_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_5y_cagr scaled by closeadj
def f057epg_f057_eps_growth_eps_5y_cagr_mean_63d_base_v027_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_5y_cagr scaled by closeadj
def f057epg_f057_eps_growth_eps_5y_cagr_mean_126d_base_v028_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_5y_cagr scaled by closeadj
def f057epg_f057_eps_growth_eps_5y_cagr_mean_252d_base_v029_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_5y_cagr scaled by closeadj
def f057epg_f057_eps_growth_eps_5y_cagr_mean_504d_base_v030_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of eps_narrow_loss scaled by closeadj
def f057epg_f057_eps_growth_eps_narrow_loss_mean_21d_base_v031_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of eps_narrow_loss scaled by closeadj
def f057epg_f057_eps_growth_eps_narrow_loss_mean_63d_base_v032_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of eps_narrow_loss scaled by closeadj
def f057epg_f057_eps_growth_eps_narrow_loss_mean_126d_base_v033_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of eps_narrow_loss scaled by closeadj
def f057epg_f057_eps_growth_eps_narrow_loss_mean_252d_base_v034_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of eps_narrow_loss scaled by closeadj
def f057epg_f057_eps_growth_eps_narrow_loss_mean_504d_base_v035_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_median_63d_base_v036_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_median_252d_base_v037_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_median_504d_base_v038_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_median_63d_base_v039_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_median_252d_base_v040_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_median_504d_base_v041_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_median_63d_base_v042_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_median_252d_base_v043_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_median_504d_base_v044_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_median_63d_base_v045_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_median_252d_base_v046_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_median_504d_base_v047_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_median_63d_base_v048_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_median_252d_base_v049_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_median_504d_base_v050_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_median_63d_base_v051_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_median_252d_base_v052_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_median_504d_base_v053_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_median_63d_base_v054_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_median_252d_base_v055_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_median_504d_base_v056_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_rmax_252d_base_v057_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_rmax_504d_base_v058_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_rmax_252d_base_v059_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_rmax_504d_base_v060_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_rmax_252d_base_v061_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_rmax_504d_base_v062_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_rmax_252d_base_v063_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of epsdil_yoy_chg
def f057epg_f057_eps_growth_epsdil_yoy_chg_rmax_504d_base_v064_signal(epsdil, closeadj):
    base = epsdil.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_rmax_252d_base_v065_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_signflip
def f057epg_f057_eps_growth_eps_signflip_rmax_504d_base_v066_signal(eps, closeadj):
    base = (np.sign(eps) != np.sign(eps.shift(252))).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_rmax_252d_base_v067_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_5y_cagr
def f057epg_f057_eps_growth_eps_5y_cagr_rmax_504d_base_v068_signal(eps, closeadj):
    base = (eps / eps.shift(1260).replace(0, np.nan).abs())**(1/5) - 1
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_rmax_252d_base_v069_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of eps_narrow_loss
def f057epg_f057_eps_growth_eps_narrow_loss_rmax_504d_base_v070_signal(eps, closeadj):
    base = (-eps).clip(lower=0).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_rmin_252d_base_v071_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of eps_qoq_chg
def f057epg_f057_eps_growth_eps_qoq_chg_rmin_504d_base_v072_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 63)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_rmin_252d_base_v073_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of eps_yoy_chg
def f057epg_f057_eps_growth_eps_yoy_chg_rmin_504d_base_v074_signal(eps, closeadj):
    base = _f057_eps_chg(eps, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of eps_pct_y
def f057epg_f057_eps_growth_eps_pct_y_rmin_252d_base_v075_signal(eps, closeadj):
    base = eps.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

