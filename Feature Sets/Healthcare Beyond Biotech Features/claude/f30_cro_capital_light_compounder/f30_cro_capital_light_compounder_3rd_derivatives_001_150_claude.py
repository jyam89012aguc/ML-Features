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
def _f30_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f30_capital_light_score(capex, revenue, fcf, w):
    ci = capex / revenue.replace(0, np.nan)
    fci = fcf / revenue.replace(0, np.nan)
    return (fci - ci).rolling(w, min_periods=max(1, w // 2)).mean()


def _f30_capital_light_compound(fcf, revenue, w):
    fcfm = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    revm = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (fcfm / revm.replace(0, np.nan)).pct_change(periods=w)


# 3d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v001_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v002_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v003_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v004_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v005_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v006_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v007_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v008_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v009_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexint base_w=21
def f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v010_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(21, min_periods=11).mean() * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v011_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v012_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v013_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v014_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v015_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v016_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v017_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v018_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v019_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexint base_w=63
def f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v020_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(63, min_periods=32).mean() * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v021_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v022_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v023_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v024_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v025_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v026_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v027_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v028_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v029_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexint base_w=252
def f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v030_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    base = ci.rolling(252, min_periods=126).mean() * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v031_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v032_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v033_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v034_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v035_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v036_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v037_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v038_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v039_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscore base_w=21
def f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v040_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    base = cls * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v041_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v042_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v043_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v044_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v045_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v046_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v047_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v048_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v049_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscore base_w=63
def f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v050_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    base = cls * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v051_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v052_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v053_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v054_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v055_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v056_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v057_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v058_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v059_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscore base_w=252
def f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v060_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    base = cls * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v061_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v062_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v063_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v064_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v065_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v066_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v067_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v068_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v069_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clcomp base_w=21
def f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v070_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    base = clc * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v071_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v072_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v073_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v074_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v075_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v076_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v077_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v078_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v079_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clcomp base_w=63
def f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v080_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    base = clc * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v081_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v082_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v083_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v084_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v085_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v086_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v087_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v088_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v089_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clcomp base_w=252
def f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v090_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    base = clc * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v091_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v092_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v093_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v094_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v095_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v096_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v097_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v098_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v099_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexintxrev base_w=21
def f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v100_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=11).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v101_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v102_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v103_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v104_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v105_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v106_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v107_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v108_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v109_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexintxrev base_w=63
def f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v110_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=32).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v111_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v112_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v113_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v114_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v115_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v116_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v117_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v118_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v119_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of capexintxrev base_w=252
def f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v120_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(252, min_periods=126).mean()
    base = ci * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v121_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v122_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v123_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v124_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v125_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v126_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v127_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v128_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v129_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscorexrev base_w=42
def f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v130_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=21).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v131_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v132_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v133_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v134_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v135_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v136_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v137_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v138_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v139_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscorexrev base_w=126
def f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v140_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    rm = revenue.rolling(126, min_periods=63).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

# 3d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v141_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 3)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v142_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 10d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v143_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v144_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 42d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v145_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v146_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 84d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v147_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v148_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 168d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v149_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)

# 189d jerk of clscorexrev base_w=504
def f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v150_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    rm = revenue.rolling(504, min_periods=252).mean()
    base = cls * rm / 1e9
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v001_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v002_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v003_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v004_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v005_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v006_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v007_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v008_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v009_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v010_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v011_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v012_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v013_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v014_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v015_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v016_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v017_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v018_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v019_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v020_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_3d_jerk_v021_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_5d_jerk_v022_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_10d_jerk_v023_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_21d_jerk_v024_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_42d_jerk_v025_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_63d_jerk_v026_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_84d_jerk_v027_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_126d_jerk_v028_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_168d_jerk_v029_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_189d_jerk_v030_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v031_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v032_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v033_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v034_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v035_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v036_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v037_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v038_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v039_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v040_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v041_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v042_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v043_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v044_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v045_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v046_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v047_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v048_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v049_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v050_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_3d_jerk_v051_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_5d_jerk_v052_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_10d_jerk_v053_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_21d_jerk_v054_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_42d_jerk_v055_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_63d_jerk_v056_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_84d_jerk_v057_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_126d_jerk_v058_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_168d_jerk_v059_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_189d_jerk_v060_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v061_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v062_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v063_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v064_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v065_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v066_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v067_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v068_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v069_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v070_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v071_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v072_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v073_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v074_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v075_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v076_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v077_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v078_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v079_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v080_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_3d_jerk_v081_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_5d_jerk_v082_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_10d_jerk_v083_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_21d_jerk_v084_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_42d_jerk_v085_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_63d_jerk_v086_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_84d_jerk_v087_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_126d_jerk_v088_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_168d_jerk_v089_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_189d_jerk_v090_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v091_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v092_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v093_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v094_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v095_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v096_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v097_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v098_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v099_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v100_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v101_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v102_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v103_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v104_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v105_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v106_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v107_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v108_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v109_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v110_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_3d_jerk_v111_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_jerk_v112_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_jerk_v113_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_jerk_v114_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_jerk_v115_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_jerk_v116_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_84d_jerk_v117_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_126d_jerk_v118_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_168d_jerk_v119_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_189d_jerk_v120_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v121_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v122_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v123_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v124_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v125_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v126_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v127_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v128_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v129_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v130_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v131_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v132_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v133_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v134_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v135_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v136_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v137_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v138_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v139_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v140_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_3d_jerk_v141_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_jerk_v142_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_jerk_v143_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_jerk_v144_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_jerk_v145_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_jerk_v146_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_84d_jerk_v147_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_126d_jerk_v148_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_168d_jerk_v149_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_189d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CRO_CAPITAL_LIGHT_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


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
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf, "capex": capex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_capex_intensity", "_f30_capital_light_score", "_f30_capital_light_compound",)
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
    print(f"OK f30_cro_capital_light_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
