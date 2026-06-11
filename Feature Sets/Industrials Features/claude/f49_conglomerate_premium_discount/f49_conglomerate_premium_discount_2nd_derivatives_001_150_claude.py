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


def _f49_evebitda_dynamics(evebitda, w):
    return _mean(evebitda, w)


def _f49_premium_discount(evebitda, ebitdamargin, w):
    return _mean(evebitda * ebitdamargin, w)


def _f49_sotp_proxy(ev, ebitda, revenue, w):
    return _mean((ev / ebitda.replace(0, np.nan).abs()) * (revenue / ev.replace(0, np.nan).abs()), w)


# 150 slope features

def _e(evebitda, w, c):
    return _f49_evebitda_dynamics(evebitda, w) * c

def _p(evebitda, m, w, c):
    return _f49_premium_discount(evebitda, m, w) * c

def _s(ev, eb, r, w, c):
    return _f49_sotp_proxy(ev, eb, r, w) * c


def f49cpd_f49_conglomerate_premium_discount_evebitda_21d_slope_v001_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_63d_slope_v002_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_126d_slope_v003_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_252d_slope_v004_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_504d_slope_v005_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_5d_slope_v006_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_42d_slope_v007_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_189d_slope_v008_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_378d_slope_v009_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_21d_slope_v010_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_21d_slope_v011_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_63d_slope_v012_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_126d_slope_v013_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_252d_slope_v014_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_504d_slope_v015_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_5d_slope_v016_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_42d_slope_v017_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_189d_slope_v018_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_378d_slope_v019_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_21d_slope_v020_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_63d_slope_v021_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_126d_slope_v022_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_252d_slope_v023_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_504d_slope_v024_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 504) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_5d_slope_v025_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 5) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_42d_slope_v026_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_189d_slope_v027_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 189) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_378d_slope_v028_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_z_63d_slope_v029_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_z_252d_slope_v030_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_z_252d_slope_v031_signal(evebitda, ebitdamargin, closeadj):
    base = _z(_f49_premium_discount(evebitda, ebitdamargin, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_z_252d_slope_v032_signal(ev, ebitda, revenue, closeadj):
    base = _z(_f49_sotp_proxy(ev, ebitda, revenue, 252), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_z_63d_slope_v033_signal(evebitda, ebitdamargin, closeadj):
    base = _z(_f49_premium_discount(evebitda, ebitdamargin, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_z_63d_slope_v034_signal(ev, ebitda, revenue, closeadj):
    base = _z(_f49_sotp_proxy(ev, ebitda, revenue, 63), 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_std_252d_slope_v035_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_std_252d_slope_v036_signal(evebitda, ebitdamargin, closeadj):
    base = _std(_f49_premium_discount(evebitda, ebitdamargin, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_std_252d_slope_v037_signal(ev, ebitda, revenue, closeadj):
    base = _std(_f49_sotp_proxy(ev, ebitda, revenue, 21), 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_63m252_slope_v038_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 63)
    lg = _f49_evebitda_dynamics(evebitda, 252)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_diff_63m252_slope_v039_signal(evebitda, ebitdamargin, closeadj):
    sh = _f49_premium_discount(evebitda, ebitdamargin, 63)
    lg = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_diff_63m252_slope_v040_signal(ev, ebitda, revenue, closeadj):
    sh = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    lg = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_63d_slope_v041_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_252d_slope_v042_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_ema_63d_slope_v043_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_ema_252d_slope_v044_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_ema_63d_slope_v045_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    base = g.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_ema_252d_slope_v046_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = g.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_rank_252d_slope_v047_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_rank_252d_slope_v048_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_rank_252d_slope_v049_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_63d_slope_v050_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_252d_slope_v051_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * _z(volume, 252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxvolz_63d_slope_v052_signal(evebitda, ebitdamargin, volume, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63) * _z(volume, 63) * closeadj
    result = _slope_pct(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxvolz_252d_slope_v053_signal(ev, ebitda, revenue, volume, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252) * _z(volume, 252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxdv_63d_slope_v054_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63) * _mean(closeadj * volume, 21)
    result = _slope_pct(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxdv_252d_slope_v055_signal(evebitda, ebitdamargin, volume, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * _mean(closeadj * volume, 63)
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxdv_252d_slope_v056_signal(ev, ebitda, revenue, volume, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252) * _mean(closeadj * volume, 63)
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_252d_slope_v057_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * ebitdamargin * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_252d_slope_v058_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * ebitdamargin * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_revgrowth_252d_slope_v059_signal(evebitda, revenue, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_revgrowth_252d_slope_v060_signal(evebitda, ebitdamargin, revenue, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_revgrowth_252d_slope_v061_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252) * revenue.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_evgrowth_252d_slope_v062_signal(evebitda, ev, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * ev.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ebgrowth_252d_slope_v063_signal(evebitda, ebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * ebitda.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_slope_v064_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    mr = ebitdamargin.rolling(252, min_periods=63).max() - ebitdamargin.rolling(252, min_periods=63).min()
    result = _slope_pct(g * mr * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_252d_slope_v065_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxsotp_252d_slope_v066_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_premium_discount(evebitda, ebitdamargin, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = (a + b) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxlogprice_252d_slope_v067_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxlogprice_252d_slope_v068_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_chg_252d_slope_v069_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    chg = evebitda - evebitda.shift(252)
    result = _slope_pct((base + chg) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_lagdiff_252d_slope_v070_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    base = (g - g.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lagdiff_252d_slope_v071_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    base = (g - g.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_lagdiff_252d_slope_v072_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = (g - g.shift(252)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_hi_252d_slope_v073_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_hi_252d_slope_v074_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_252d_slope_v075_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    med = g.rolling(252, min_periods=63).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(252, min_periods=63).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_min_63d_slope_v076_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = (g.rolling(63, min_periods=21).min() + g * 0.1) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_max_252d_slope_v077_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = (g.rolling(252, min_periods=63).max() + g * 0.1) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_range_252d_slope_v078_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    result = _slope_pct(rng * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaskew_252d_slope_v079_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.rolling(252, min_periods=63).skew() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdakurt_252d_slope_v080_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    base = g.rolling(252, min_periods=63).kurt() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqevebitda_252d_slope_v081_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = g * g.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqpremdisc_252d_slope_v082_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = g * g.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sqsotp_252d_slope_v083_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = g * g.abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_logevebitda_252d_slope_v084_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = np.sign(g) * np.log1p(g.abs()) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_voladj_252d_slope_v085_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    vol = _std(evebitda.pct_change(), 252)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_252d_slope_v086_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    vol = _std((evebitda * ebitdamargin).pct_change(), 252)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_trend_252d_slope_v087_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_trend_252d_slope_v088_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_trend_252d_slope_v089_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    trend = g.rolling(252, min_periods=63).mean() - g.rolling(504, min_periods=126).mean()
    result = _slope_pct(trend * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_composite_252d_slope_v090_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_premium_discount(evebitda, ebitdamargin, 252)
    c = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = (a + b + c) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_composite_504d_slope_v091_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 504)
    b = _f49_premium_discount(evebitda, ebitdamargin, 504)
    c = _f49_sotp_proxy(ev, ebitda, revenue, 504)
    base = (a + b + c) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_504d_slope_v092_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63)
    med = g.rolling(504, min_periods=126).median()
    flag = (g > med).astype(float)
    cnt = flag.rolling(504, min_periods=126).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_event_lo_504d_slope_v093_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    med = g.rolling(504, min_periods=126).median()
    flag = (g < med).astype(float)
    cnt = flag.rolling(504, min_periods=126).sum()
    base = (cnt + g * 10.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_252d_slope_v094_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    pct = evebitda.pct_change(252)
    base2 = base * (1.0 + pct) * closeadj
    result = _slope_pct(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_pctchg_252d_slope_v095_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252)
    pct = (evebitda * ebitdamargin).pct_change(252)
    base2 = base * (1.0 + pct) * closeadj
    result = _slope_pct(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_pctchg_252d_slope_v096_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    inner = (ev / ebitda.replace(0, np.nan).abs()) * (revenue / ev.replace(0, np.nan).abs())
    pct = inner.pct_change(252)
    base2 = base * (1.0 + pct) * closeadj
    result = _slope_pct(base2, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_lograw_252d_slope_v097_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lograw_252d_slope_v098_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_lograw_252d_slope_v099_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = np.log(g.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_volgrowth_252d_slope_v100_signal(evebitda, volume, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * volume.pct_change(252) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_lo_252d_slope_v101_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    base = (lo * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lo_252d_slope_v102_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    med = g.rolling(252, min_periods=63).median()
    lo = (g < med).astype(float)
    base = (lo * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_med_252d_slope_v103_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    base = (g - med) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxrevmix_252d_slope_v104_signal(evebitda, ebitdamargin, ev, revenue, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 252)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    result = _slope_pct(base * rev_mix * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxrevmix_252d_slope_v105_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    result = _slope_pct(base * rev_mix * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_minus_const_252d_slope_v106_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = (g - 8.0) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_minus_const_252d_slope_v107_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = (g - 1.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ratio_63v252_slope_v108_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 63)
    lg = _f49_evebitda_dynamics(evebitda, 252)
    base = sh / lg.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_diff_5m21_slope_v109_signal(evebitda, ebitdamargin, closeadj):
    sh = _f49_premium_discount(evebitda, ebitdamargin, 5)
    lg = _f49_premium_discount(evebitda, ebitdamargin, 21)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_5m21_slope_v110_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 5)
    lg = _f49_evebitda_dynamics(evebitda, 21)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_diff_5m21_slope_v111_signal(ev, ebitda, revenue, closeadj):
    sh = _f49_sotp_proxy(ev, ebitda, revenue, 5)
    lg = _f49_sotp_proxy(ev, ebitda, revenue, 21)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_42d_alt_slope_v112_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 42) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_42d_alt_slope_v113_signal(evebitda, ebitdamargin, closeadj):
    base = _f49_premium_discount(evebitda, ebitdamargin, 42) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_42d_alt_slope_v114_signal(ev, ebitda, revenue, closeadj):
    base = _f49_sotp_proxy(ev, ebitda, revenue, 42) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_x_revenue_252d_slope_v115_signal(evebitda, revenue, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_x_revenue_252d_slope_v116_signal(evebitda, ebitdamargin, revenue, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * np.log(revenue.abs().replace(0, np.nan)) * closeadj / closeadj.abs().replace(0, np.nan) * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_252d_slope_v117_signal(evebitda, ebitdamargin, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = a / b.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_252d_slope_v118_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = a / b.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_sotp_ratio_252d_slope_v119_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    a = _f49_premium_discount(evebitda, ebitdamargin, 252)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 252)
    base = a / b.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_med_alt_252d_slope_v120_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    med = g.rolling(252, min_periods=63).median()
    base = (g - med) * np.log(closeadj.abs().replace(0, np.nan)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_63d_slope_v121_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 63)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 63)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_63d_slope_v122_signal(evebitda, ev, revenue, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    result = _slope_pct(base * rev_mix * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_252d_slope_v123_signal(evebitda, ev, revenue, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 252)
    rev_mix = revenue / ev.replace(0, np.nan).abs()
    result = _slope_pct(base * rev_mix * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_63d_slope_v124_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63) * ebitdamargin * closeadj
    result = _slope_pct(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_63d_slope_v125_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 63) * ebitdamargin * closeadj
    result = _slope_pct(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_alt_slope_v126_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    mr = ebitdamargin.rolling(252, min_periods=63).max() - ebitdamargin.rolling(252, min_periods=63).min()
    result = _slope_pct(g * mr * closeadj * 2.0, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_marginrange_252d_slope_v127_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    mr = ebitdamargin.rolling(252, min_periods=63).max() - ebitdamargin.rolling(252, min_periods=63).min()
    result = _slope_pct(g * mr * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_z_21d_slope_v128_signal(evebitda, closeadj):
    base = _z(_f49_evebitda_dynamics(evebitda, 21), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_z_21d_slope_v129_signal(evebitda, ebitdamargin, closeadj):
    base = _z(_f49_premium_discount(evebitda, ebitdamargin, 21), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_z_21d_slope_v130_signal(ev, ebitda, revenue, closeadj):
    base = _z(_f49_sotp_proxy(ev, ebitda, revenue, 21), 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_std_63d_slope_v131_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 5), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_std_63d_slope_v132_signal(evebitda, ebitdamargin, closeadj):
    base = _std(_f49_premium_discount(evebitda, ebitdamargin, 5), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_std_504d_slope_v133_signal(evebitda, closeadj):
    base = _std(_f49_evebitda_dynamics(evebitda, 63), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_std_504d_slope_v134_signal(evebitda, ebitdamargin, closeadj):
    base = _std(_f49_premium_discount(evebitda, ebitdamargin, 63), 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_ema_21d_slope_v135_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_ema_21d_slope_v136_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 5)
    base = g.ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_rank_504d_slope_v137_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_rank_504d_slope_v138_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_chg_63d_slope_v139_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    chg = evebitda - evebitda.shift(63)
    result = _slope_pct((base + chg) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_63d_slope_v140_signal(evebitda, closeadj):
    base = _f49_evebitda_dynamics(evebitda, 63)
    pct = evebitda.pct_change(63)
    result = _slope_pct(base * (1.0 + pct) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitdaxprice_252d_slope_v141_signal(evebitda, closeadj):
    g = _f49_evebitda_dynamics(evebitda, 252) * closeadj * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdiscxprice_252d_slope_v142_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 252) * closeadj * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotpxprice_252d_slope_v143_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 252) * closeadj * closeadj
    result = _slope_pct(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_63d_slope_v144_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 63)
    vol = _std((evebitda * ebitdamargin).pct_change(), 63)
    base = g / vol.replace(0, np.nan) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_21m63_slope_v145_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 21)
    lg = _f49_evebitda_dynamics(evebitda, 63)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_diff_252m504_slope_v146_signal(evebitda, closeadj):
    sh = _f49_evebitda_dynamics(evebitda, 252)
    lg = _f49_evebitda_dynamics(evebitda, 504)
    base = (sh - lg) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_premdisc_lo_504d_slope_v147_signal(evebitda, ebitdamargin, closeadj):
    g = _f49_premium_discount(evebitda, ebitdamargin, 504)
    med = g.rolling(504, min_periods=126).median()
    lo = (g < med).astype(float)
    base = (lo * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_sotp_hi_504d_slope_v148_signal(ev, ebitda, revenue, closeadj):
    g = _f49_sotp_proxy(ev, ebitda, revenue, 504)
    med = g.rolling(504, min_periods=126).median()
    hi = (g > med).astype(float)
    base = (hi * g + g * 0.5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_504d_slope_v149_signal(evebitda, ebitdamargin, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 504)
    b = _f49_premium_discount(evebitda, ebitdamargin, 504)
    base = a / b.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_504d_slope_v150_signal(evebitda, ev, ebitda, revenue, closeadj):
    a = _f49_evebitda_dynamics(evebitda, 504)
    b = _f49_sotp_proxy(ev, ebitda, revenue, 504)
    base = a / b.replace(0, np.nan).abs() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49cpd_f49_conglomerate_premium_discount_evebitda_21d_slope_v001_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_63d_slope_v002_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_126d_slope_v003_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_252d_slope_v004_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_504d_slope_v005_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_5d_slope_v006_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_42d_slope_v007_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_189d_slope_v008_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_378d_slope_v009_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_21d_slope_v010_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_21d_slope_v011_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_63d_slope_v012_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_126d_slope_v013_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_252d_slope_v014_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_504d_slope_v015_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_5d_slope_v016_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_42d_slope_v017_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_189d_slope_v018_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_378d_slope_v019_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_21d_slope_v020_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_63d_slope_v021_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_126d_slope_v022_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_252d_slope_v023_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_504d_slope_v024_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_5d_slope_v025_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_42d_slope_v026_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_189d_slope_v027_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_378d_slope_v028_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_63d_slope_v029_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_252d_slope_v030_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_z_252d_slope_v031_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_z_252d_slope_v032_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_z_63d_slope_v033_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_z_63d_slope_v034_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_252d_slope_v035_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_std_252d_slope_v036_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_std_252d_slope_v037_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_63m252_slope_v038_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_diff_63m252_slope_v039_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_diff_63m252_slope_v040_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_63d_slope_v041_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_252d_slope_v042_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_ema_63d_slope_v043_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_ema_252d_slope_v044_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_ema_63d_slope_v045_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_ema_252d_slope_v046_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_rank_252d_slope_v047_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_rank_252d_slope_v048_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_rank_252d_slope_v049_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_63d_slope_v050_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxvolz_252d_slope_v051_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxvolz_63d_slope_v052_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxvolz_252d_slope_v053_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxdv_63d_slope_v054_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxdv_252d_slope_v055_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxdv_252d_slope_v056_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_252d_slope_v057_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_252d_slope_v058_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_revgrowth_252d_slope_v059_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_revgrowth_252d_slope_v060_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_revgrowth_252d_slope_v061_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_evgrowth_252d_slope_v062_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ebgrowth_252d_slope_v063_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_slope_v064_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_252d_slope_v065_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxsotp_252d_slope_v066_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxlogprice_252d_slope_v067_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxlogprice_252d_slope_v068_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_chg_252d_slope_v069_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_lagdiff_252d_slope_v070_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lagdiff_252d_slope_v071_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_lagdiff_252d_slope_v072_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_hi_252d_slope_v073_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_hi_252d_slope_v074_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_252d_slope_v075_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_min_63d_slope_v076_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_max_252d_slope_v077_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_range_252d_slope_v078_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaskew_252d_slope_v079_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdakurt_252d_slope_v080_signal,
    f49cpd_f49_conglomerate_premium_discount_sqevebitda_252d_slope_v081_signal,
    f49cpd_f49_conglomerate_premium_discount_sqpremdisc_252d_slope_v082_signal,
    f49cpd_f49_conglomerate_premium_discount_sqsotp_252d_slope_v083_signal,
    f49cpd_f49_conglomerate_premium_discount_logevebitda_252d_slope_v084_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_voladj_252d_slope_v085_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_252d_slope_v086_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_trend_252d_slope_v087_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_trend_252d_slope_v088_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_trend_252d_slope_v089_signal,
    f49cpd_f49_conglomerate_premium_discount_composite_252d_slope_v090_signal,
    f49cpd_f49_conglomerate_premium_discount_composite_504d_slope_v091_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_event_hi_504d_slope_v092_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_event_lo_504d_slope_v093_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_252d_slope_v094_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_pctchg_252d_slope_v095_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_pctchg_252d_slope_v096_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_lograw_252d_slope_v097_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lograw_252d_slope_v098_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_lograw_252d_slope_v099_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_volgrowth_252d_slope_v100_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_lo_252d_slope_v101_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lo_252d_slope_v102_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_med_252d_slope_v103_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxrevmix_252d_slope_v104_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxrevmix_252d_slope_v105_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_minus_const_252d_slope_v106_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_minus_const_252d_slope_v107_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ratio_63v252_slope_v108_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_diff_5m21_slope_v109_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_5m21_slope_v110_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_diff_5m21_slope_v111_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_42d_alt_slope_v112_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_42d_alt_slope_v113_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_42d_alt_slope_v114_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_x_revenue_252d_slope_v115_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_x_revenue_252d_slope_v116_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_252d_slope_v117_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_252d_slope_v118_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_sotp_ratio_252d_slope_v119_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_med_alt_252d_slope_v120_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxsotp_63d_slope_v121_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_63d_slope_v122_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxrevmix_252d_slope_v123_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxmargin_63d_slope_v124_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxmargin_63d_slope_v125_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_marginrange_252d_alt_slope_v126_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_marginrange_252d_slope_v127_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_z_21d_slope_v128_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_z_21d_slope_v129_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_z_21d_slope_v130_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_63d_slope_v131_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_std_63d_slope_v132_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_std_504d_slope_v133_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_std_504d_slope_v134_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_ema_21d_slope_v135_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_ema_21d_slope_v136_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_rank_504d_slope_v137_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_rank_504d_slope_v138_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_chg_63d_slope_v139_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_pctchg_63d_slope_v140_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitdaxprice_252d_slope_v141_signal,
    f49cpd_f49_conglomerate_premium_discount_premdiscxprice_252d_slope_v142_signal,
    f49cpd_f49_conglomerate_premium_discount_sotpxprice_252d_slope_v143_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_voladj_63d_slope_v144_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_21m63_slope_v145_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_diff_252m504_slope_v146_signal,
    f49cpd_f49_conglomerate_premium_discount_premdisc_lo_504d_slope_v147_signal,
    f49cpd_f49_conglomerate_premium_discount_sotp_hi_504d_slope_v148_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_premdisc_ratio_504d_slope_v149_signal,
    f49cpd_f49_conglomerate_premium_discount_evebitda_sotp_ratio_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CONGLOMERATE_PREMIUM_DISCOUNT_REGISTRY_SLOPE_001_150 = REGISTRY


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
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ev      = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    evebitda = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ev": ev, "evebitda": evebitda,
        "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_evebitda_dynamics", "_f49_premium_discount", "_f49_sotp_proxy")
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
    print(f"OK f49_conglomerate_premium_discount_2nd_derivatives_001_150_claude: {n_features} features pass")
