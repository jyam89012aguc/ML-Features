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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f21_consumables_revenue_share(grossmargin, revenue, w):
    # high gross margin × revenue captures dollar-weighted consumable contribution
    gm = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return gm * revenue


def _f21_recurring_quality(revenue, w):
    # low-volatility revenue growth = recurring consumable mix
    g = revenue.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return g / sd.replace(0, np.nan).abs()


def _f21_consumables_signature(revenue, grossmargin, w):
    # composite: revenue compounding × margin stability
    r = revenue.pct_change(periods=w)
    gm_sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return r / (gm_sd.replace(0, np.nan) + 1e-6)


# ===== features =====
def f21lcr_f21_lst_consumables_recurring_revshare_21d_base_v001_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_63d_base_v002_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_126d_base_v003_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 126)
    result = base.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_252d_base_v004_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_504d_base_v005_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 504)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_z21d_base_v006_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_z63d_base_v007_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_z126d_base_v008_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 126)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_z252d_base_v009_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_log21d_base_v010_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_log63d_base_v011_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_log252d_base_v012_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_ema21d_base_v013_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = _ema(base, 21).pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_ema63d_base_v014_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = _ema(base, 63).pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_ema252d_base_v015_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = _ema(base, 126).pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_revratio_63d_base_v016_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = (base / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_revratio_252d_base_v017_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = (base / revenue.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_diff21d_base_v018_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 21)
    result = base.diff(21) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_diff63d_base_v019_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = base.diff(63) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_diff252d_base_v020_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = base.diff(126) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_std63d_base_v021_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = _std(base, 63) / _mean(base, 63).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_std252d_base_v022_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = _std(base, 252) / _mean(base, 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_sqrt63d_base_v023_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = np.sqrt(base.abs() + 1.0) * closeadj * np.sign(base)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_sqrt252d_base_v024_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 252)
    result = np.sqrt(base.abs() + 1.0) * closeadj * np.sign(base)
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_revshare_invrev_63d_base_v025_signal(grossmargin, revenue, closeadj):
    base = _f21_consumables_revenue_share(grossmargin, revenue, 63)
    result = (base / (revenue.rolling(252, min_periods=63).mean().replace(0, np.nan))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ----- _f21_recurring_quality based features -----
def f21lcr_f21_lst_consumables_recurring_rq_21d_base_v026_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_63d_base_v027_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_126d_base_v028_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_252d_base_v029_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_504d_base_v030_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_z21d_base_v031_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_z63d_base_v032_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_z252d_base_v033_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_mean21d_base_v034_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_mean63d_base_v035_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_mean252d_base_v036_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_std21d_base_v037_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_std63d_base_v038_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_std252d_base_v039_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_ema21d_base_v040_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_ema63d_base_v041_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_ema252d_base_v042_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sq21d_base_v043_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sq63d_base_v044_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_sq252d_base_v045_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_diff21d_base_v046_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_diff63d_base_v047_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_diff252d_base_v048_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_minmax63d_base_v049_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = (base - lo) / (hi - lo).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_rq_minmax252d_base_v050_signal(revenue, closeadj):
    base = _f21_recurring_quality(revenue, 252)
    lo = base.rolling(504, min_periods=126).min()
    hi = base.rolling(504, min_periods=126).max()
    result = (base - lo) / (hi - lo).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ----- _f21_consumables_signature based features -----
def f21lcr_f21_lst_consumables_recurring_sig_21d_base_v051_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_63d_base_v052_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_126d_base_v053_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_252d_base_v054_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_504d_base_v055_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_z21d_base_v056_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_z63d_base_v057_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_z252d_base_v058_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_mean21d_base_v059_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_mean63d_base_v060_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_mean252d_base_v061_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_std21d_base_v062_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_std63d_base_v063_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_std252d_base_v064_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_ema21d_base_v065_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_ema63d_base_v066_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_ema252d_base_v067_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sq21d_base_v068_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sq63d_base_v069_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_sq252d_base_v070_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_diff21d_base_v071_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 21)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_diff63d_base_v072_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_diff252d_base_v073_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    result = base.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_mmr63d_base_v074_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 63)
    lo = base.rolling(252, min_periods=63).min()
    hi = base.rolling(252, min_periods=63).max()
    result = (base - lo) / (hi - lo).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f21lcr_f21_lst_consumables_recurring_sig_mmr252d_base_v075_signal(revenue, grossmargin, closeadj):
    base = _f21_consumables_signature(revenue, grossmargin, 252)
    lo = base.rolling(504, min_periods=126).min()
    hi = base.rolling(504, min_periods=126).max()
    result = (base - lo) / (hi - lo).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21lcr_f21_lst_consumables_recurring_revshare_21d_base_v001_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_63d_base_v002_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_126d_base_v003_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_252d_base_v004_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_504d_base_v005_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_z21d_base_v006_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_z63d_base_v007_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_z126d_base_v008_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_z252d_base_v009_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_log21d_base_v010_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_log63d_base_v011_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_log252d_base_v012_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_ema21d_base_v013_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_ema63d_base_v014_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_ema252d_base_v015_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_revratio_63d_base_v016_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_revratio_252d_base_v017_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_diff21d_base_v018_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_diff63d_base_v019_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_diff252d_base_v020_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_std63d_base_v021_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_std252d_base_v022_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_sqrt63d_base_v023_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_sqrt252d_base_v024_signal,
    f21lcr_f21_lst_consumables_recurring_revshare_invrev_63d_base_v025_signal,
    f21lcr_f21_lst_consumables_recurring_rq_21d_base_v026_signal,
    f21lcr_f21_lst_consumables_recurring_rq_63d_base_v027_signal,
    f21lcr_f21_lst_consumables_recurring_rq_126d_base_v028_signal,
    f21lcr_f21_lst_consumables_recurring_rq_252d_base_v029_signal,
    f21lcr_f21_lst_consumables_recurring_rq_504d_base_v030_signal,
    f21lcr_f21_lst_consumables_recurring_rq_z21d_base_v031_signal,
    f21lcr_f21_lst_consumables_recurring_rq_z63d_base_v032_signal,
    f21lcr_f21_lst_consumables_recurring_rq_z252d_base_v033_signal,
    f21lcr_f21_lst_consumables_recurring_rq_mean21d_base_v034_signal,
    f21lcr_f21_lst_consumables_recurring_rq_mean63d_base_v035_signal,
    f21lcr_f21_lst_consumables_recurring_rq_mean252d_base_v036_signal,
    f21lcr_f21_lst_consumables_recurring_rq_std21d_base_v037_signal,
    f21lcr_f21_lst_consumables_recurring_rq_std63d_base_v038_signal,
    f21lcr_f21_lst_consumables_recurring_rq_std252d_base_v039_signal,
    f21lcr_f21_lst_consumables_recurring_rq_ema21d_base_v040_signal,
    f21lcr_f21_lst_consumables_recurring_rq_ema63d_base_v041_signal,
    f21lcr_f21_lst_consumables_recurring_rq_ema252d_base_v042_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sq21d_base_v043_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sq63d_base_v044_signal,
    f21lcr_f21_lst_consumables_recurring_rq_sq252d_base_v045_signal,
    f21lcr_f21_lst_consumables_recurring_rq_diff21d_base_v046_signal,
    f21lcr_f21_lst_consumables_recurring_rq_diff63d_base_v047_signal,
    f21lcr_f21_lst_consumables_recurring_rq_diff252d_base_v048_signal,
    f21lcr_f21_lst_consumables_recurring_rq_minmax63d_base_v049_signal,
    f21lcr_f21_lst_consumables_recurring_rq_minmax252d_base_v050_signal,
    f21lcr_f21_lst_consumables_recurring_sig_21d_base_v051_signal,
    f21lcr_f21_lst_consumables_recurring_sig_63d_base_v052_signal,
    f21lcr_f21_lst_consumables_recurring_sig_126d_base_v053_signal,
    f21lcr_f21_lst_consumables_recurring_sig_252d_base_v054_signal,
    f21lcr_f21_lst_consumables_recurring_sig_504d_base_v055_signal,
    f21lcr_f21_lst_consumables_recurring_sig_z21d_base_v056_signal,
    f21lcr_f21_lst_consumables_recurring_sig_z63d_base_v057_signal,
    f21lcr_f21_lst_consumables_recurring_sig_z252d_base_v058_signal,
    f21lcr_f21_lst_consumables_recurring_sig_mean21d_base_v059_signal,
    f21lcr_f21_lst_consumables_recurring_sig_mean63d_base_v060_signal,
    f21lcr_f21_lst_consumables_recurring_sig_mean252d_base_v061_signal,
    f21lcr_f21_lst_consumables_recurring_sig_std21d_base_v062_signal,
    f21lcr_f21_lst_consumables_recurring_sig_std63d_base_v063_signal,
    f21lcr_f21_lst_consumables_recurring_sig_std252d_base_v064_signal,
    f21lcr_f21_lst_consumables_recurring_sig_ema21d_base_v065_signal,
    f21lcr_f21_lst_consumables_recurring_sig_ema63d_base_v066_signal,
    f21lcr_f21_lst_consumables_recurring_sig_ema252d_base_v067_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sq21d_base_v068_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sq63d_base_v069_signal,
    f21lcr_f21_lst_consumables_recurring_sig_sq252d_base_v070_signal,
    f21lcr_f21_lst_consumables_recurring_sig_diff21d_base_v071_signal,
    f21lcr_f21_lst_consumables_recurring_sig_diff63d_base_v072_signal,
    f21lcr_f21_lst_consumables_recurring_sig_diff252d_base_v073_signal,
    f21lcr_f21_lst_consumables_recurring_sig_mmr63d_base_v074_signal,
    f21lcr_f21_lst_consumables_recurring_sig_mmr252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_LST_CONSUMABLES_RECURRING_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "grossmargin": grossmargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = (
        "_f21_consumables_revenue_share",
        "_f21_recurring_quality",
        "_f21_consumables_signature",
    )
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_lst_consumables_recurring_base_001_075_claude: {n_features} features pass")
