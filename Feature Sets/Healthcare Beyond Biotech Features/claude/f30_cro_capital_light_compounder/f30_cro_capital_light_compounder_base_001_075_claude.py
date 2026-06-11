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


# 5d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_5d_base_v001_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_10d_base_v002_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(10, min_periods=max(1, 10 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_21d_base_v003_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_42d_base_v004_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(42, min_periods=max(1, 42 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_63d_base_v005_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_126d_base_v006_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(126, min_periods=max(1, 126 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_189d_base_v007_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(189, min_periods=max(1, 189 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_252d_base_v008_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_378d_base_v009_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(378, min_periods=max(1, 378 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capex intensity mean x close
def f30clc_f30_cro_capital_light_compounder_capexint_504d_base_v010_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    result = ci.rolling(504, min_periods=max(1, 504 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_5d_base_v011_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_10d_base_v012_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_21d_base_v013_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_42d_base_v014_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_63d_base_v015_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_126d_base_v016_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_189d_base_v017_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 189)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_252d_base_v018_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_378d_base_v019_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 378)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capital-light score x close
def f30clc_f30_cro_capital_light_compounder_clscore_504d_base_v020_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    result = cls * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_5d_base_v021_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_10d_base_v022_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_21d_base_v023_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_42d_base_v024_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_63d_base_v025_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_126d_base_v026_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 126)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_189d_base_v027_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 189)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_252d_base_v028_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_378d_base_v029_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 378)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capital-light compound x close
def f30clc_f30_cro_capital_light_compounder_clcomp_504d_base_v030_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 504)
    result = clc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_5d_base_v031_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = _z(cim, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_10d_base_v032_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = _z(cim, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_21d_base_v033_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _z(cim, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_42d_base_v034_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = _z(cim, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_63d_base_v035_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _z(cim, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_126d_base_v036_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _z(cim, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_189d_base_v037_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(189, min_periods=max(1, 189 // 2)).mean()
    result = _z(cim, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_252d_base_v038_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _z(cim, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_378d_base_v039_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(378, min_periods=max(1, 378 // 2)).mean()
    result = _z(cim, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capex intensity zscore x close
def f30clc_f30_cro_capital_light_compounder_capexintz_504d_base_v040_signal(capex, revenue, closeadj):
    ci = _f30_capex_intensity(capex, revenue)
    cim = ci.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _z(cim, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_5d_base_v041_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    result = _z(cls, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_10d_base_v042_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    result = _z(cls, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_21d_base_v043_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    result = _z(cls, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_42d_base_v044_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    result = _z(cls, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_63d_base_v045_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    result = _z(cls, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_126d_base_v046_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 126)
    result = _z(cls, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_189d_base_v047_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 189)
    result = _z(cls, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_252d_base_v048_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 252)
    result = _z(cls, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_378d_base_v049_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 378)
    result = _z(cls, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capital-light score zscore x close
def f30clc_f30_cro_capital_light_compounder_clscorez_504d_base_v050_signal(capex, revenue, fcf, closeadj):
    cls = _f30_capital_light_score(capex, revenue, fcf, 504)
    result = _z(cls, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_5d_base_v051_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    result = _z(clc, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_10d_base_v052_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    result = _z(clc, 20) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_21d_base_v053_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    result = _z(clc, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_42d_base_v054_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    result = _z(clc, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_63d_base_v055_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    result = _z(clc, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_126d_base_v056_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 126)
    result = _z(clc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 189d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_189d_base_v057_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 189)
    result = _z(clc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_252d_base_v058_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 252)
    result = _z(clc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 378d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_378d_base_v059_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 378)
    result = _z(clc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d capital-light compound zscore x close
def f30clc_f30_cro_capital_light_compounder_clcompz_504d_base_v060_signal(fcf, revenue, closeadj):
    clc = _f30_capital_light_compound(fcf, revenue, 504)
    result = _z(clc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capex intensity x revenue mean
def f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_base_v061_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = ci * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capex intensity x revenue mean
def f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_base_v062_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = ci * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capex intensity x revenue mean
def f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_base_v063_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = ci * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capex intensity x revenue mean
def f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_base_v064_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = ci * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capex intensity x revenue mean
def f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_base_v065_signal(capex, revenue):
    ci = _f30_capex_intensity(capex, revenue)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = ci * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light score x revenue mean
def f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_base_v066_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 5)
    rm = revenue.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = cls * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light score x revenue mean
def f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_base_v067_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 10)
    rm = revenue.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = cls * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light score x revenue mean
def f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_base_v068_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 21)
    rm = revenue.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = cls * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light score x revenue mean
def f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_base_v069_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 42)
    rm = revenue.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = cls * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light score x revenue mean
def f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_base_v070_signal(capex, revenue, fcf):
    cls = _f30_capital_light_score(capex, revenue, fcf, 63)
    rm = revenue.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = cls * rm / 1e9
    return result.replace([np.inf, -np.inf], np.nan)

# 5d capital-light compound x fcf mean
def f30clc_f30_cro_capital_light_compounder_clcompxfcf_5d_base_v071_signal(fcf, revenue):
    clc = _f30_capital_light_compound(fcf, revenue, 5)
    fm = fcf.rolling(5, min_periods=max(1, 5 // 2)).mean()
    result = clc * fm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# 10d capital-light compound x fcf mean
def f30clc_f30_cro_capital_light_compounder_clcompxfcf_10d_base_v072_signal(fcf, revenue):
    clc = _f30_capital_light_compound(fcf, revenue, 10)
    fm = fcf.rolling(10, min_periods=max(1, 10 // 2)).mean()
    result = clc * fm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# 21d capital-light compound x fcf mean
def f30clc_f30_cro_capital_light_compounder_clcompxfcf_21d_base_v073_signal(fcf, revenue):
    clc = _f30_capital_light_compound(fcf, revenue, 21)
    fm = fcf.rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = clc * fm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# 42d capital-light compound x fcf mean
def f30clc_f30_cro_capital_light_compounder_clcompxfcf_42d_base_v074_signal(fcf, revenue):
    clc = _f30_capital_light_compound(fcf, revenue, 42)
    fm = fcf.rolling(42, min_periods=max(1, 42 // 2)).mean()
    result = clc * fm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

# 63d capital-light compound x fcf mean
def f30clc_f30_cro_capital_light_compounder_clcompxfcf_63d_base_v075_signal(fcf, revenue):
    clc = _f30_capital_light_compound(fcf, revenue, 63)
    fm = fcf.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = clc * fm / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f30clc_f30_cro_capital_light_compounder_capexint_5d_base_v001_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_10d_base_v002_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_21d_base_v003_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_42d_base_v004_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_63d_base_v005_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_126d_base_v006_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_189d_base_v007_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_252d_base_v008_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_378d_base_v009_signal,
    f30clc_f30_cro_capital_light_compounder_capexint_504d_base_v010_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_5d_base_v011_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_10d_base_v012_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_21d_base_v013_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_42d_base_v014_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_63d_base_v015_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_126d_base_v016_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_189d_base_v017_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_252d_base_v018_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_378d_base_v019_signal,
    f30clc_f30_cro_capital_light_compounder_clscore_504d_base_v020_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_5d_base_v021_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_10d_base_v022_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_21d_base_v023_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_42d_base_v024_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_63d_base_v025_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_126d_base_v026_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_189d_base_v027_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_252d_base_v028_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_378d_base_v029_signal,
    f30clc_f30_cro_capital_light_compounder_clcomp_504d_base_v030_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_5d_base_v031_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_10d_base_v032_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_21d_base_v033_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_42d_base_v034_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_63d_base_v035_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_126d_base_v036_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_189d_base_v037_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_252d_base_v038_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_378d_base_v039_signal,
    f30clc_f30_cro_capital_light_compounder_capexintz_504d_base_v040_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_5d_base_v041_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_10d_base_v042_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_21d_base_v043_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_42d_base_v044_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_63d_base_v045_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_126d_base_v046_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_189d_base_v047_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_252d_base_v048_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_378d_base_v049_signal,
    f30clc_f30_cro_capital_light_compounder_clscorez_504d_base_v050_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_5d_base_v051_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_10d_base_v052_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_21d_base_v053_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_42d_base_v054_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_63d_base_v055_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_126d_base_v056_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_189d_base_v057_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_252d_base_v058_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_378d_base_v059_signal,
    f30clc_f30_cro_capital_light_compounder_clcompz_504d_base_v060_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_5d_base_v061_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_10d_base_v062_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_21d_base_v063_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_42d_base_v064_signal,
    f30clc_f30_cro_capital_light_compounder_capexintxrev_63d_base_v065_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_5d_base_v066_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_10d_base_v067_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_21d_base_v068_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_42d_base_v069_signal,
    f30clc_f30_cro_capital_light_compounder_clscorexrev_63d_base_v070_signal,
    f30clc_f30_cro_capital_light_compounder_clcompxfcf_5d_base_v071_signal,
    f30clc_f30_cro_capital_light_compounder_clcompxfcf_10d_base_v072_signal,
    f30clc_f30_cro_capital_light_compounder_clcompxfcf_21d_base_v073_signal,
    f30clc_f30_cro_capital_light_compounder_clcompxfcf_42d_base_v074_signal,
    f30clc_f30_cro_capital_light_compounder_clcompxfcf_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CRO_CAPITAL_LIGHT_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_cro_capital_light_compounder_base_001_075_claude: {n_features} features pass")
