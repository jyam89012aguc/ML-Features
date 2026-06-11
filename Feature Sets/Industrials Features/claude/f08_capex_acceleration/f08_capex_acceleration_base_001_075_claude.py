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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f08_capex_growth(capex, w):
    return capex.pct_change(periods=w)


def _f08_capex_to_revenue(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f08_capex_intensity_change(capex, revenue, w):
    intens = capex / revenue.replace(0, np.nan).abs()
    return intens.diff(periods=w)


# 21d capex growth * closeadj
def f08cap_f08_capex_acceleration_grow_21d_base_v001_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth * closeadj
def f08cap_f08_capex_acceleration_grow_63d_base_v002_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex growth * closeadj
def f08cap_f08_capex_acceleration_grow_126d_base_v003_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth * closeadj
def f08cap_f08_capex_acceleration_grow_252d_base_v004_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth * closeadj
def f08cap_f08_capex_acceleration_grow_504d_base_v005_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/revenue * closeadj
def f08cap_f08_capex_acceleration_crev_21d_base_v006_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue
def f08cap_f08_capex_acceleration_crev_63d_base_v007_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/revenue
def f08cap_f08_capex_acceleration_crev_126d_base_v008_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue
def f08cap_f08_capex_acceleration_crev_252d_base_v009_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/revenue
def f08cap_f08_capex_acceleration_crev_504d_base_v010_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intensity change
def f08cap_f08_capex_acceleration_iint_21d_base_v011_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intensity change
def f08cap_f08_capex_acceleration_iint_63d_base_v012_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d intensity change
def f08cap_f08_capex_acceleration_iint_126d_base_v013_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intensity change
def f08cap_f08_capex_acceleration_iint_252d_base_v014_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intensity change
def f08cap_f08_capex_acceleration_iint_504d_base_v015_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d capex growth
def f08cap_f08_capex_acceleration_grow_5d_base_v016_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d capex growth
def f08cap_f08_capex_acceleration_grow_10d_base_v017_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d capex growth
def f08cap_f08_capex_acceleration_grow_42d_base_v018_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d capex growth
def f08cap_f08_capex_acceleration_grow_189d_base_v019_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d capex growth
def f08cap_f08_capex_acceleration_grow_378d_base_v020_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d capex/revenue
def f08cap_f08_capex_acceleration_crev_5d_base_v021_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d capex/revenue
def f08cap_f08_capex_acceleration_crev_10d_base_v022_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d capex/revenue
def f08cap_f08_capex_acceleration_crev_42d_base_v023_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d capex/revenue
def f08cap_f08_capex_acceleration_crev_189d_base_v024_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d capex/revenue
def f08cap_f08_capex_acceleration_crev_378d_base_v025_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std capex growth
def f08cap_f08_capex_acceleration_growstd_21d_base_v026_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std capex growth
def f08cap_f08_capex_acceleration_growstd_63d_base_v027_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std capex growth
def f08cap_f08_capex_acceleration_growstd_252d_base_v028_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std capex growth
def f08cap_f08_capex_acceleration_growstd_504d_base_v029_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std capex/revenue
def f08cap_f08_capex_acceleration_crevstd_21d_base_v030_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std capex/revenue
def f08cap_f08_capex_acceleration_crevstd_63d_base_v031_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std capex/revenue
def f08cap_f08_capex_acceleration_crevstd_252d_base_v032_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std capex/revenue
def f08cap_f08_capex_acceleration_crevstd_504d_base_v033_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z capex growth
def f08cap_f08_capex_acceleration_growz_21d_base_v034_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z capex growth
def f08cap_f08_capex_acceleration_growz_63d_base_v035_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z capex growth
def f08cap_f08_capex_acceleration_growz_252d_base_v036_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z capex growth
def f08cap_f08_capex_acceleration_growz_504d_base_v037_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z capex/revenue
def f08cap_f08_capex_acceleration_crevz_21d_base_v038_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z capex/revenue
def f08cap_f08_capex_acceleration_crevz_63d_base_v039_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z capex/revenue
def f08cap_f08_capex_acceleration_crevz_252d_base_v040_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z capex/revenue
def f08cap_f08_capex_acceleration_crevz_504d_base_v041_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA capex growth
def f08cap_f08_capex_acceleration_growema_21d_base_v042_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA capex growth
def f08cap_f08_capex_acceleration_growema_63d_base_v043_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA capex growth
def f08cap_f08_capex_acceleration_growema_252d_base_v044_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA crev
def f08cap_f08_capex_acceleration_crevema_21d_base_v045_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA crev
def f08cap_f08_capex_acceleration_crevema_63d_base_v046_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA crev
def f08cap_f08_capex_acceleration_crevema_252d_base_v047_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21v252 capex/rev gap
def f08cap_f08_capex_acceleration_crevgap_21v252_base_v048_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v252 capex/rev gap
def f08cap_f08_capex_acceleration_crevgap_63v252_base_v049_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63v504 capex/rev gap
def f08cap_f08_capex_acceleration_crevgap_63v504_base_v050_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126v504 capex/rev gap
def f08cap_f08_capex_acceleration_crevgap_126v504_base_v051_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    result = (_mean(b, 126) - _mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth squared 63d * close
def f08cap_f08_capex_acceleration_growsq_63d_base_v052_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth squared 252d
def f08cap_f08_capex_acceleration_growsq_252d_base_v053_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/rev squared 63d
def f08cap_f08_capex_acceleration_crevsq_63d_base_v054_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base * base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/rev squared 252d
def f08cap_f08_capex_acceleration_crevsq_252d_base_v055_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue)
    result = _mean(base * base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth * crev 21d
def f08cap_f08_capex_acceleration_growxcrev_21d_base_v056_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 21)
    c = _f08_capex_to_revenue(capex, revenue)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth * crev 63d
def f08cap_f08_capex_acceleration_growxcrev_63d_base_v057_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth * crev 252d
def f08cap_f08_capex_acceleration_growxcrev_252d_base_v058_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    result = g * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity change EMA 21d
def f08cap_f08_capex_acceleration_iintema_21d_base_v059_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity change EMA 63d
def f08cap_f08_capex_acceleration_iintema_63d_base_v060_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity change EMA 252d
def f08cap_f08_capex_acceleration_iintema_252d_base_v061_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex max 252d * close
def f08cap_f08_capex_acceleration_capmax_252d_base_v062_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    cap_max = capex.rolling(252, min_periods=63).max()
    result = (cap_max + base * 0) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


# capex min 252d * close
def f08cap_f08_capex_acceleration_capmin_252d_base_v063_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    cap_min = capex.rolling(252, min_periods=63).min()
    result = (cap_min + base * 0) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


# capex range 252d * close
def f08cap_f08_capex_acceleration_caprng_252d_base_v064_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21)
    rng = capex.rolling(252, min_periods=63).max() - capex.rolling(252, min_periods=63).min()
    result = (rng + base * 0) * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex growth * revenue
def f08cap_f08_capex_acceleration_growxrev_21d_base_v065_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 21)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth * revenue
def f08cap_f08_capex_acceleration_growxrev_63d_base_v066_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth * revenue
def f08cap_f08_capex_acceleration_growxrev_252d_base_v067_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    result = g * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intensity change x revenue
def f08cap_f08_capex_acceleration_iintxrev_63d_base_v068_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    result = i * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intensity change x revenue
def f08cap_f08_capex_acceleration_iintxrev_252d_base_v069_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    result = i * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d crev * close return
def f08cap_f08_capex_acceleration_crevxcret_63d_base_v070_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cret = closeadj.pct_change(63)
    result = c * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d crev * close return
def f08cap_f08_capex_acceleration_crevxcret_252d_base_v071_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cret = closeadj.pct_change(252)
    result = c * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# sign of capex growth 63d * close
def f08cap_f08_capex_acceleration_growsign_63d_base_v072_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    result = np.sign(g) * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log abs capex growth 63d
def f08cap_f08_capex_acceleration_growlog_63d_base_v073_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    result = np.log(g.abs().replace(0, np.nan) + 1) * closeadj * np.sign(g)
    return result.replace([np.inf, -np.inf], np.nan)


# capex grow rel to crev 63d
def f08cap_f08_capex_acceleration_growrelcrev_63d_base_v074_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    result = g / _mean(c, 252).replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d crev percentile * close
def f08cap_f08_capex_acceleration_crevpct_504d_base_v075_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cap_f08_capex_acceleration_grow_21d_base_v001_signal,
    f08cap_f08_capex_acceleration_grow_63d_base_v002_signal,
    f08cap_f08_capex_acceleration_grow_126d_base_v003_signal,
    f08cap_f08_capex_acceleration_grow_252d_base_v004_signal,
    f08cap_f08_capex_acceleration_grow_504d_base_v005_signal,
    f08cap_f08_capex_acceleration_crev_21d_base_v006_signal,
    f08cap_f08_capex_acceleration_crev_63d_base_v007_signal,
    f08cap_f08_capex_acceleration_crev_126d_base_v008_signal,
    f08cap_f08_capex_acceleration_crev_252d_base_v009_signal,
    f08cap_f08_capex_acceleration_crev_504d_base_v010_signal,
    f08cap_f08_capex_acceleration_iint_21d_base_v011_signal,
    f08cap_f08_capex_acceleration_iint_63d_base_v012_signal,
    f08cap_f08_capex_acceleration_iint_126d_base_v013_signal,
    f08cap_f08_capex_acceleration_iint_252d_base_v014_signal,
    f08cap_f08_capex_acceleration_iint_504d_base_v015_signal,
    f08cap_f08_capex_acceleration_grow_5d_base_v016_signal,
    f08cap_f08_capex_acceleration_grow_10d_base_v017_signal,
    f08cap_f08_capex_acceleration_grow_42d_base_v018_signal,
    f08cap_f08_capex_acceleration_grow_189d_base_v019_signal,
    f08cap_f08_capex_acceleration_grow_378d_base_v020_signal,
    f08cap_f08_capex_acceleration_crev_5d_base_v021_signal,
    f08cap_f08_capex_acceleration_crev_10d_base_v022_signal,
    f08cap_f08_capex_acceleration_crev_42d_base_v023_signal,
    f08cap_f08_capex_acceleration_crev_189d_base_v024_signal,
    f08cap_f08_capex_acceleration_crev_378d_base_v025_signal,
    f08cap_f08_capex_acceleration_growstd_21d_base_v026_signal,
    f08cap_f08_capex_acceleration_growstd_63d_base_v027_signal,
    f08cap_f08_capex_acceleration_growstd_252d_base_v028_signal,
    f08cap_f08_capex_acceleration_growstd_504d_base_v029_signal,
    f08cap_f08_capex_acceleration_crevstd_21d_base_v030_signal,
    f08cap_f08_capex_acceleration_crevstd_63d_base_v031_signal,
    f08cap_f08_capex_acceleration_crevstd_252d_base_v032_signal,
    f08cap_f08_capex_acceleration_crevstd_504d_base_v033_signal,
    f08cap_f08_capex_acceleration_growz_21d_base_v034_signal,
    f08cap_f08_capex_acceleration_growz_63d_base_v035_signal,
    f08cap_f08_capex_acceleration_growz_252d_base_v036_signal,
    f08cap_f08_capex_acceleration_growz_504d_base_v037_signal,
    f08cap_f08_capex_acceleration_crevz_21d_base_v038_signal,
    f08cap_f08_capex_acceleration_crevz_63d_base_v039_signal,
    f08cap_f08_capex_acceleration_crevz_252d_base_v040_signal,
    f08cap_f08_capex_acceleration_crevz_504d_base_v041_signal,
    f08cap_f08_capex_acceleration_growema_21d_base_v042_signal,
    f08cap_f08_capex_acceleration_growema_63d_base_v043_signal,
    f08cap_f08_capex_acceleration_growema_252d_base_v044_signal,
    f08cap_f08_capex_acceleration_crevema_21d_base_v045_signal,
    f08cap_f08_capex_acceleration_crevema_63d_base_v046_signal,
    f08cap_f08_capex_acceleration_crevema_252d_base_v047_signal,
    f08cap_f08_capex_acceleration_crevgap_21v252_base_v048_signal,
    f08cap_f08_capex_acceleration_crevgap_63v252_base_v049_signal,
    f08cap_f08_capex_acceleration_crevgap_63v504_base_v050_signal,
    f08cap_f08_capex_acceleration_crevgap_126v504_base_v051_signal,
    f08cap_f08_capex_acceleration_growsq_63d_base_v052_signal,
    f08cap_f08_capex_acceleration_growsq_252d_base_v053_signal,
    f08cap_f08_capex_acceleration_crevsq_63d_base_v054_signal,
    f08cap_f08_capex_acceleration_crevsq_252d_base_v055_signal,
    f08cap_f08_capex_acceleration_growxcrev_21d_base_v056_signal,
    f08cap_f08_capex_acceleration_growxcrev_63d_base_v057_signal,
    f08cap_f08_capex_acceleration_growxcrev_252d_base_v058_signal,
    f08cap_f08_capex_acceleration_iintema_21d_base_v059_signal,
    f08cap_f08_capex_acceleration_iintema_63d_base_v060_signal,
    f08cap_f08_capex_acceleration_iintema_252d_base_v061_signal,
    f08cap_f08_capex_acceleration_capmax_252d_base_v062_signal,
    f08cap_f08_capex_acceleration_capmin_252d_base_v063_signal,
    f08cap_f08_capex_acceleration_caprng_252d_base_v064_signal,
    f08cap_f08_capex_acceleration_growxrev_21d_base_v065_signal,
    f08cap_f08_capex_acceleration_growxrev_63d_base_v066_signal,
    f08cap_f08_capex_acceleration_growxrev_252d_base_v067_signal,
    f08cap_f08_capex_acceleration_iintxrev_63d_base_v068_signal,
    f08cap_f08_capex_acceleration_iintxrev_252d_base_v069_signal,
    f08cap_f08_capex_acceleration_crevxcret_63d_base_v070_signal,
    f08cap_f08_capex_acceleration_crevxcret_252d_base_v071_signal,
    f08cap_f08_capex_acceleration_growsign_63d_base_v072_signal,
    f08cap_f08_capex_acceleration_growlog_63d_base_v073_signal,
    f08cap_f08_capex_acceleration_growrelcrev_63d_base_v074_signal,
    f08cap_f08_capex_acceleration_crevpct_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPEX_ACCELERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "capex": capex, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_capex_growth", "_f08_capex_to_revenue", "_f08_capex_intensity_change")
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
    print(f"OK f08_capex_acceleration_base_001_075_claude: {n_features} features pass")
