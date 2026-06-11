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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f21_revenue_phase(revenue, w):
    g = revenue.pct_change(periods=w)
    m = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (g - m) / sd


def _f21_margin_cycle_position(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (ebitdamargin - m) / sd


def _f21_cycle_composite(revenue, ebitdamargin, w):
    rg = revenue.pct_change(periods=w)
    rg_z = (rg - rg.rolling(w, min_periods=max(1, w // 2)).mean()) / rg.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    m_z = (ebitdamargin - ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()) / ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return (rg_z + m_z) / 2.0

# ===== features =====

def f21ccp_f21_consumer_cycle_phase_revphase_5d_jw5_jerk_v001_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_10d_jw10_jerk_v002_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_21d_jw21_jerk_v003_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_42d_jw42_jerk_v004_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_63d_jw63_jerk_v005_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_84d_jw126_jerk_v006_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_126d_jw5_jerk_v007_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_168d_jw10_jerk_v008_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 168)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_189d_jw21_jerk_v009_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 189)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_252d_jw42_jerk_v010_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 252)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_315d_jw63_jerk_v011_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 315)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_378d_jw126_jerk_v012_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 378)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphase_504d_jw5_jerk_v013_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 504)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_5d_jw10_jerk_v014_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    result = _mean(base, 5) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_10d_jw21_jerk_v015_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    result = _mean(base, 10) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_21d_jw42_jerk_v016_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    result = _mean(base, 21) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_42d_jw63_jerk_v017_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    result = _mean(base, 42) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_63d_jw126_jerk_v018_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    result = _mean(base, 63) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_84d_jw5_jerk_v019_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    result = _mean(base, 84) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_126d_jw10_jerk_v020_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    result = _mean(base, 126) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_168d_jw21_jerk_v021_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 168)
    result = _mean(base, 168) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_189d_jw42_jerk_v022_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 189)
    result = _mean(base, 189) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_252d_jw63_jerk_v023_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 252)
    result = _mean(base, 252) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_315d_jw126_jerk_v024_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 315)
    result = _mean(base, 315) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_378d_jw5_jerk_v025_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 378)
    result = _mean(base, 378) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasemean_504d_jw10_jerk_v026_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 504)
    result = _mean(base, 504) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_5d_jw21_jerk_v027_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    result = _ema(base, 5) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_10d_jw42_jerk_v028_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    result = _ema(base, 10) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_21d_jw63_jerk_v029_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    result = _ema(base, 21) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_42d_jw126_jerk_v030_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    result = _ema(base, 42) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_63d_jw5_jerk_v031_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    result = _ema(base, 63) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_84d_jw10_jerk_v032_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    result = _ema(base, 84) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_126d_jw21_jerk_v033_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    result = _ema(base, 126) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_168d_jw42_jerk_v034_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 168)
    result = _ema(base, 168) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_189d_jw63_jerk_v035_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 189)
    result = _ema(base, 189) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_252d_jw126_jerk_v036_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 252)
    result = _ema(base, 252) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_315d_jw5_jerk_v037_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 315)
    result = _ema(base, 315) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_378d_jw10_jerk_v038_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 378)
    result = _ema(base, 378) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseema_504d_jw21_jerk_v039_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 504)
    result = _ema(base, 504) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_5d_jw42_jerk_v040_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 5)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_10d_jw63_jerk_v041_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 10)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_21d_jw126_jerk_v042_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 21)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_42d_jw5_jerk_v043_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 42)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_63d_jw10_jerk_v044_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 63)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_84d_jw21_jerk_v045_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 84)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_126d_jw42_jerk_v046_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 126)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_168d_jw63_jerk_v047_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 168)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_189d_jw126_jerk_v048_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 189)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_252d_jw5_jerk_v049_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 252)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_315d_jw10_jerk_v050_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 315)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_378d_jw21_jerk_v051_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 378)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margpos_504d_jw42_jerk_v052_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 504)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_5d_jw63_jerk_v053_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 5)
    result = _mean(base, 5) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_10d_jw126_jerk_v054_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 10)
    result = _mean(base, 10) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_21d_jw5_jerk_v055_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 21)
    result = _mean(base, 21) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_42d_jw10_jerk_v056_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 42)
    result = _mean(base, 42) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_63d_jw21_jerk_v057_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 63)
    result = _mean(base, 63) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_84d_jw42_jerk_v058_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 84)
    result = _mean(base, 84) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_126d_jw63_jerk_v059_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 126)
    result = _mean(base, 126) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_168d_jw126_jerk_v060_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 168)
    result = _mean(base, 168) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_189d_jw5_jerk_v061_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 189)
    result = _mean(base, 189) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_252d_jw10_jerk_v062_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 252)
    result = _mean(base, 252) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_315d_jw21_jerk_v063_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 315)
    result = _mean(base, 315) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_378d_jw42_jerk_v064_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 378)
    result = _mean(base, 378) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposmean_504d_jw63_jerk_v065_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 504)
    result = _mean(base, 504) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_5d_jw126_jerk_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 5)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_10d_jw5_jerk_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 10)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_21d_jw10_jerk_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 21)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_42d_jw21_jerk_v069_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 42)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_63d_jw42_jerk_v070_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 63)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_84d_jw63_jerk_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 84)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_126d_jw126_jerk_v072_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 126)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_168d_jw5_jerk_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 168)
    result = base * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_189d_jw10_jerk_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 189)
    result = base * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_252d_jw21_jerk_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 252)
    result = base * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_315d_jw42_jerk_v076_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 315)
    result = base * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_378d_jw63_jerk_v077_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 378)
    result = base * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_comp_504d_jw126_jerk_v078_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 504)
    result = base * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_5d_jw5_jerk_v079_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_10d_jw10_jerk_v080_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_21d_jw21_jerk_v081_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_42d_jw42_jerk_v082_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_63d_jw63_jerk_v083_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_84d_jw126_jerk_v084_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_126d_jw5_jerk_v085_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_168d_jw10_jerk_v086_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 168)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_189d_jw21_jerk_v087_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 189)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_252d_jw42_jerk_v088_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 252)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_315d_jw63_jerk_v089_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 315)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_378d_jw126_jerk_v090_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 378)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphasexni_504d_jw5_jerk_v091_signal(revenue, netinc, closeadj):
    base = _f21_revenue_phase(revenue, 504)
    result = base * netinc / 1e8 * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_5d_jw10_jerk_v092_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 5)
    result = _std(base, 5) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_10d_jw21_jerk_v093_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 10)
    result = _std(base, 10) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_21d_jw42_jerk_v094_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 21)
    result = _std(base, 21) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_42d_jw63_jerk_v095_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 42)
    result = _std(base, 42) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_63d_jw126_jerk_v096_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 63)
    result = _std(base, 63) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_84d_jw5_jerk_v097_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 84)
    result = _std(base, 84) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_126d_jw10_jerk_v098_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 126)
    result = _std(base, 126) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_168d_jw21_jerk_v099_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 168)
    result = _std(base, 168) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_189d_jw42_jerk_v100_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 189)
    result = _std(base, 189) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_252d_jw63_jerk_v101_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 252)
    result = _std(base, 252) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_315d_jw126_jerk_v102_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 315)
    result = _std(base, 315) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_378d_jw5_jerk_v103_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 378)
    result = _std(base, 378) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_margposstd_504d_jw10_jerk_v104_signal(ebitdamargin, closeadj):
    base = _f21_margin_cycle_position(ebitdamargin, 504)
    result = _std(base, 504) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_5d_jw21_jerk_v105_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 5)
    result = _ema(base, 5) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_10d_jw42_jerk_v106_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 10)
    result = _ema(base, 10) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_21d_jw63_jerk_v107_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 21)
    result = _ema(base, 21) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_42d_jw126_jerk_v108_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 42)
    result = _ema(base, 42) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_63d_jw5_jerk_v109_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 63)
    result = _ema(base, 63) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_84d_jw10_jerk_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 84)
    result = _ema(base, 84) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_126d_jw21_jerk_v111_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 126)
    result = _ema(base, 126) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_168d_jw42_jerk_v112_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 168)
    result = _ema(base, 168) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_189d_jw63_jerk_v113_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 189)
    result = _ema(base, 189) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_252d_jw126_jerk_v114_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 252)
    result = _ema(base, 252) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_315d_jw5_jerk_v115_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 315)
    result = _ema(base, 315) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_378d_jw10_jerk_v116_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 378)
    result = _ema(base, 378) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compema_504d_jw21_jerk_v117_signal(revenue, ebitdamargin, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 504)
    result = _ema(base, 504) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_5d_jw42_jerk_v118_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 5)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_10d_jw63_jerk_v119_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 10)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_21d_jw126_jerk_v120_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 21)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_42d_jw5_jerk_v121_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 42)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_63d_jw10_jerk_v122_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 63)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_84d_jw21_jerk_v123_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 84)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_126d_jw42_jerk_v124_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 126)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_168d_jw63_jerk_v125_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 168)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_189d_jw126_jerk_v126_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 189)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_252d_jw5_jerk_v127_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 252)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_315d_jw10_jerk_v128_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 315)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_378d_jw21_jerk_v129_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 378)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_compxni_504d_jw42_jerk_v130_signal(revenue, ebitdamargin, netinc, closeadj):
    base = _f21_cycle_composite(revenue, ebitdamargin, 504)
    result = base * (netinc / 1e8) * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_5d_jw63_jerk_v131_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    m = _f21_margin_cycle_position(ebitdamargin, 5)
    result = base * m * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_10d_jw126_jerk_v132_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    m = _f21_margin_cycle_position(ebitdamargin, 10)
    result = base * m * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_21d_jw5_jerk_v133_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    m = _f21_margin_cycle_position(ebitdamargin, 21)
    result = base * m * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_42d_jw10_jerk_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    m = _f21_margin_cycle_position(ebitdamargin, 42)
    result = base * m * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_63d_jw21_jerk_v135_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    m = _f21_margin_cycle_position(ebitdamargin, 63)
    result = base * m * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_84d_jw42_jerk_v136_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    m = _f21_margin_cycle_position(ebitdamargin, 84)
    result = base * m * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_126d_jw63_jerk_v137_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    m = _f21_margin_cycle_position(ebitdamargin, 126)
    result = base * m * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_168d_jw126_jerk_v138_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 168)
    m = _f21_margin_cycle_position(ebitdamargin, 168)
    result = base * m * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_189d_jw5_jerk_v139_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 189)
    m = _f21_margin_cycle_position(ebitdamargin, 189)
    result = base * m * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_252d_jw10_jerk_v140_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 252)
    m = _f21_margin_cycle_position(ebitdamargin, 252)
    result = base * m * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_315d_jw21_jerk_v141_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 315)
    m = _f21_margin_cycle_position(ebitdamargin, 315)
    result = base * m * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_378d_jw42_jerk_v142_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 378)
    m = _f21_margin_cycle_position(ebitdamargin, 378)
    result = base * m * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revxmarg_504d_jw63_jerk_v143_signal(revenue, ebitdamargin, closeadj):
    base = _f21_revenue_phase(revenue, 504)
    m = _f21_margin_cycle_position(ebitdamargin, 504)
    result = base * m * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_5d_jw126_jerk_v144_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 5)
    result = base.abs() * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_10d_jw5_jerk_v145_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 10)
    result = base.abs() * closeadj
    result = _jerk(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_21d_jw10_jerk_v146_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 21)
    result = base.abs() * closeadj
    result = _jerk(result, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_42d_jw21_jerk_v147_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 42)
    result = base.abs() * closeadj
    result = _jerk(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_63d_jw42_jerk_v148_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 63)
    result = base.abs() * closeadj
    result = _jerk(result, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_84d_jw63_jerk_v149_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 84)
    result = base.abs() * closeadj
    result = _jerk(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f21ccp_f21_consumer_cycle_phase_revphaseabs_126d_jw126_jerk_v150_signal(revenue, closeadj):
    base = _f21_revenue_phase(revenue, 126)
    result = base.abs() * closeadj
    result = _jerk(result, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21ccp_f21_consumer_cycle_phase_revphase_5d_jw5_jerk_v001_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_10d_jw10_jerk_v002_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_21d_jw21_jerk_v003_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_42d_jw42_jerk_v004_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_63d_jw63_jerk_v005_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_84d_jw126_jerk_v006_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_126d_jw5_jerk_v007_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_168d_jw10_jerk_v008_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_189d_jw21_jerk_v009_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_252d_jw42_jerk_v010_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_315d_jw63_jerk_v011_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_378d_jw126_jerk_v012_signal,
    f21ccp_f21_consumer_cycle_phase_revphase_504d_jw5_jerk_v013_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_5d_jw10_jerk_v014_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_10d_jw21_jerk_v015_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_21d_jw42_jerk_v016_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_42d_jw63_jerk_v017_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_63d_jw126_jerk_v018_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_84d_jw5_jerk_v019_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_126d_jw10_jerk_v020_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_168d_jw21_jerk_v021_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_189d_jw42_jerk_v022_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_252d_jw63_jerk_v023_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_315d_jw126_jerk_v024_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_378d_jw5_jerk_v025_signal,
    f21ccp_f21_consumer_cycle_phase_revphasemean_504d_jw10_jerk_v026_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_5d_jw21_jerk_v027_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_10d_jw42_jerk_v028_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_21d_jw63_jerk_v029_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_42d_jw126_jerk_v030_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_63d_jw5_jerk_v031_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_84d_jw10_jerk_v032_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_126d_jw21_jerk_v033_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_168d_jw42_jerk_v034_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_189d_jw63_jerk_v035_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_252d_jw126_jerk_v036_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_315d_jw5_jerk_v037_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_378d_jw10_jerk_v038_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseema_504d_jw21_jerk_v039_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_5d_jw42_jerk_v040_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_10d_jw63_jerk_v041_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_21d_jw126_jerk_v042_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_42d_jw5_jerk_v043_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_63d_jw10_jerk_v044_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_84d_jw21_jerk_v045_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_126d_jw42_jerk_v046_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_168d_jw63_jerk_v047_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_189d_jw126_jerk_v048_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_252d_jw5_jerk_v049_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_315d_jw10_jerk_v050_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_378d_jw21_jerk_v051_signal,
    f21ccp_f21_consumer_cycle_phase_margpos_504d_jw42_jerk_v052_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_5d_jw63_jerk_v053_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_10d_jw126_jerk_v054_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_21d_jw5_jerk_v055_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_42d_jw10_jerk_v056_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_63d_jw21_jerk_v057_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_84d_jw42_jerk_v058_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_126d_jw63_jerk_v059_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_168d_jw126_jerk_v060_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_189d_jw5_jerk_v061_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_252d_jw10_jerk_v062_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_315d_jw21_jerk_v063_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_378d_jw42_jerk_v064_signal,
    f21ccp_f21_consumer_cycle_phase_margposmean_504d_jw63_jerk_v065_signal,
    f21ccp_f21_consumer_cycle_phase_comp_5d_jw126_jerk_v066_signal,
    f21ccp_f21_consumer_cycle_phase_comp_10d_jw5_jerk_v067_signal,
    f21ccp_f21_consumer_cycle_phase_comp_21d_jw10_jerk_v068_signal,
    f21ccp_f21_consumer_cycle_phase_comp_42d_jw21_jerk_v069_signal,
    f21ccp_f21_consumer_cycle_phase_comp_63d_jw42_jerk_v070_signal,
    f21ccp_f21_consumer_cycle_phase_comp_84d_jw63_jerk_v071_signal,
    f21ccp_f21_consumer_cycle_phase_comp_126d_jw126_jerk_v072_signal,
    f21ccp_f21_consumer_cycle_phase_comp_168d_jw5_jerk_v073_signal,
    f21ccp_f21_consumer_cycle_phase_comp_189d_jw10_jerk_v074_signal,
    f21ccp_f21_consumer_cycle_phase_comp_252d_jw21_jerk_v075_signal,
    f21ccp_f21_consumer_cycle_phase_comp_315d_jw42_jerk_v076_signal,
    f21ccp_f21_consumer_cycle_phase_comp_378d_jw63_jerk_v077_signal,
    f21ccp_f21_consumer_cycle_phase_comp_504d_jw126_jerk_v078_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_5d_jw5_jerk_v079_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_10d_jw10_jerk_v080_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_21d_jw21_jerk_v081_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_42d_jw42_jerk_v082_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_63d_jw63_jerk_v083_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_84d_jw126_jerk_v084_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_126d_jw5_jerk_v085_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_168d_jw10_jerk_v086_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_189d_jw21_jerk_v087_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_252d_jw42_jerk_v088_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_315d_jw63_jerk_v089_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_378d_jw126_jerk_v090_signal,
    f21ccp_f21_consumer_cycle_phase_revphasexni_504d_jw5_jerk_v091_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_5d_jw10_jerk_v092_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_10d_jw21_jerk_v093_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_21d_jw42_jerk_v094_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_42d_jw63_jerk_v095_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_63d_jw126_jerk_v096_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_84d_jw5_jerk_v097_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_126d_jw10_jerk_v098_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_168d_jw21_jerk_v099_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_189d_jw42_jerk_v100_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_252d_jw63_jerk_v101_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_315d_jw126_jerk_v102_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_378d_jw5_jerk_v103_signal,
    f21ccp_f21_consumer_cycle_phase_margposstd_504d_jw10_jerk_v104_signal,
    f21ccp_f21_consumer_cycle_phase_compema_5d_jw21_jerk_v105_signal,
    f21ccp_f21_consumer_cycle_phase_compema_10d_jw42_jerk_v106_signal,
    f21ccp_f21_consumer_cycle_phase_compema_21d_jw63_jerk_v107_signal,
    f21ccp_f21_consumer_cycle_phase_compema_42d_jw126_jerk_v108_signal,
    f21ccp_f21_consumer_cycle_phase_compema_63d_jw5_jerk_v109_signal,
    f21ccp_f21_consumer_cycle_phase_compema_84d_jw10_jerk_v110_signal,
    f21ccp_f21_consumer_cycle_phase_compema_126d_jw21_jerk_v111_signal,
    f21ccp_f21_consumer_cycle_phase_compema_168d_jw42_jerk_v112_signal,
    f21ccp_f21_consumer_cycle_phase_compema_189d_jw63_jerk_v113_signal,
    f21ccp_f21_consumer_cycle_phase_compema_252d_jw126_jerk_v114_signal,
    f21ccp_f21_consumer_cycle_phase_compema_315d_jw5_jerk_v115_signal,
    f21ccp_f21_consumer_cycle_phase_compema_378d_jw10_jerk_v116_signal,
    f21ccp_f21_consumer_cycle_phase_compema_504d_jw21_jerk_v117_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_5d_jw42_jerk_v118_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_10d_jw63_jerk_v119_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_21d_jw126_jerk_v120_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_42d_jw5_jerk_v121_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_63d_jw10_jerk_v122_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_84d_jw21_jerk_v123_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_126d_jw42_jerk_v124_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_168d_jw63_jerk_v125_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_189d_jw126_jerk_v126_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_252d_jw5_jerk_v127_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_315d_jw10_jerk_v128_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_378d_jw21_jerk_v129_signal,
    f21ccp_f21_consumer_cycle_phase_compxni_504d_jw42_jerk_v130_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_5d_jw63_jerk_v131_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_10d_jw126_jerk_v132_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_21d_jw5_jerk_v133_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_42d_jw10_jerk_v134_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_63d_jw21_jerk_v135_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_84d_jw42_jerk_v136_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_126d_jw63_jerk_v137_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_168d_jw126_jerk_v138_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_189d_jw5_jerk_v139_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_252d_jw10_jerk_v140_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_315d_jw21_jerk_v141_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_378d_jw42_jerk_v142_signal,
    f21ccp_f21_consumer_cycle_phase_revxmarg_504d_jw63_jerk_v143_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_5d_jw126_jerk_v144_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_10d_jw5_jerk_v145_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_21d_jw10_jerk_v146_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_42d_jw21_jerk_v147_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_63d_jw42_jerk_v148_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_84d_jw63_jerk_v149_signal,
    f21ccp_f21_consumer_cycle_phase_revphaseabs_126d_jw126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_CONSUMER_CYCLE_PHASE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "revenue": revenue,
        "closeadj": closeadj,
        "ebitdamargin": ebitdamargin,
        "netinc": netinc,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_revenue_phase", "_f21_margin_cycle_position", "_f21_cycle_composite",)
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_consumer_cycle_phase_3rd_derivatives_001_150_claude: {n_features} features pass")
