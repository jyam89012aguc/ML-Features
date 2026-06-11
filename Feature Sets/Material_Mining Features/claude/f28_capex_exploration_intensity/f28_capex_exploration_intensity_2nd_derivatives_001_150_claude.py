import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    # 2nd math derivative: discrete second difference over window w
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)


# ===== folder domain primitives (capex / exploration MAGNITUDE & FUNDING & DEVELOPMENT) =====
# depamor-centric tightened domain (see base files). Avoids capex/revenue & rnd/revenue momentum
# (f25/f27) and raw capex/assets, capex/ppnenet level z/rank (f40/f30).
def _f28_capex_depamor(capex, depamor):
    return capex / depamor.replace(0, np.nan)


def _f28_rnd_depamor(rnd, depamor):
    return rnd / depamor.replace(0, np.nan)


def _f28_rnd_capex(rnd, capex):
    return rnd / capex.replace(0, np.nan)


def _f28_explore_share(capex, rnd):
    return rnd / (capex + rnd).replace(0, np.nan)


def _f28_invest_intensity(ncfi, depamor):
    return (-ncfi) / depamor.replace(0, np.nan)


def _f28_age(depamor, ppnenet):
    return depamor / ppnenet.replace(0, np.nan)


def _f28_excess_over_ppne(capex, depamor, ppnenet):
    return (capex - depamor) / ppnenet.replace(0, np.nan)


# slope of log capex/depamor build multiple base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdeplog_21d_slope_v001_signal(capex, depamor):
    base = np.log(_f28_capex_depamor(capex, depamor).clip(lower=1e-6))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log capex/depamor build multiple base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdeplog_63d_slope_v002_signal(capex, depamor):
    base = np.log(_f28_capex_depamor(capex, depamor).clip(lower=1e-6))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log capex/depamor build multiple base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdeplog_126d_slope_v003_signal(capex, depamor):
    base = np.log(_f28_capex_depamor(capex, depamor).clip(lower=1e-6))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored capex/depamor build multiple base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdepz_63d_slope_v004_signal(capex, depamor):
    base = _z(_f28_capex_depamor(capex, depamor), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored capex/depamor build multiple base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdepz_126d_slope_v005_signal(capex, depamor):
    base = _z(_f28_capex_depamor(capex, depamor), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored capex/depamor build multiple base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdepz_21d_slope_v006_signal(capex, depamor):
    base = _z(_f28_capex_depamor(capex, depamor), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/depamor build multiple base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdeprank_126d_slope_v007_signal(capex, depamor):
    base = _rank(_f28_capex_depamor(capex, depamor), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/depamor build multiple base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdeprank_21d_slope_v008_signal(capex, depamor):
    base = _rank(_f28_capex_depamor(capex, depamor), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/depamor build multiple base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdeprank_63d_slope_v009_signal(capex, depamor):
    base = _rank(_f28_capex_depamor(capex, depamor), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor distance below 504d peak base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdeppeak_21d_slope_v010_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor distance below 504d peak base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdeppeak_63d_slope_v011_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor distance below 504d peak base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdeppeak_126d_slope_v012_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor minus its 252d median base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdeprelmed_63d_slope_v013_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor minus its 252d median base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdeprelmed_126d_slope_v014_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor minus its 252d median base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdeprelmed_21d_slope_v015_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor short-vs-long mean ratio base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdepslr_126d_slope_v016_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor short-vs-long mean ratio base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdepslr_21d_slope_v017_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex/depamor short-vs-long mean ratio base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdepslr_63d_slope_v018_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _mean(r, 63) / _mean(r, 252).replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of capex/depamor base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdepcv_21d_slope_v019_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of capex/depamor base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdepcv_63d_slope_v020_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of capex/depamor base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdepcv_126d_slope_v021_signal(capex, depamor):
    r = _f28_capex_depamor(capex, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of excess (growth) capex over maintenance per PP&E base, 63d slope window
def f28cx_f28_capex_exploration_intensity_excessppne_63d_slope_v022_signal(capex, depamor, ppnenet):
    base = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of excess (growth) capex over maintenance per PP&E base, 126d slope window
def f28cx_f28_capex_exploration_intensity_excessppne_126d_slope_v023_signal(capex, depamor, ppnenet):
    base = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of excess (growth) capex over maintenance per PP&E base, 21d slope window
def f28cx_f28_capex_exploration_intensity_excessppne_21d_slope_v024_signal(capex, depamor, ppnenet):
    base = _f28_excess_over_ppne(capex, depamor, ppnenet)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored excess-capex per PP&E base, 126d slope window
def f28cx_f28_capex_exploration_intensity_excessppnez_126d_slope_v025_signal(capex, depamor, ppnenet):
    base = _z(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored excess-capex per PP&E base, 21d slope window
def f28cx_f28_capex_exploration_intensity_excessppnez_21d_slope_v026_signal(capex, depamor, ppnenet):
    base = _z(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored excess-capex per PP&E base, 63d slope window
def f28cx_f28_capex_exploration_intensity_excessppnez_63d_slope_v027_signal(capex, depamor, ppnenet):
    base = _z(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of excess-capex per PP&E base, 21d slope window
def f28cx_f28_capex_exploration_intensity_excessppnerank_21d_slope_v028_signal(capex, depamor, ppnenet):
    base = _rank(_f28_excess_over_ppne(capex, depamor, ppnenet), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of excess-capex per PP&E base, 63d slope window
def f28cx_f28_capex_exploration_intensity_excessppnerank_63d_slope_v029_signal(capex, depamor, ppnenet):
    base = _rank(_f28_excess_over_ppne(capex, depamor, ppnenet), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of excess-capex per PP&E base, 126d slope window
def f28cx_f28_capex_exploration_intensity_excessppnerank_126d_slope_v030_signal(capex, depamor, ppnenet):
    base = _rank(_f28_excess_over_ppne(capex, depamor, ppnenet), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of excess-capex per PP&E base, 63d slope window
def f28cx_f28_capex_exploration_intensity_excessvol_63d_slope_v031_signal(capex, depamor, ppnenet):
    base = _std(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of excess-capex per PP&E base, 126d slope window
def f28cx_f28_capex_exploration_intensity_excessvol_126d_slope_v032_signal(capex, depamor, ppnenet):
    base = _std(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of excess-capex per PP&E base, 21d slope window
def f28cx_f28_capex_exploration_intensity_excessvol_21d_slope_v033_signal(capex, depamor, ppnenet):
    base = _std(_f28_excess_over_ppne(capex, depamor, ppnenet), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growth-capex vs 252d PP&E increment base, 126d slope window
def f28cx_f28_capex_exploration_intensity_growthshare_126d_slope_v034_signal(capex, depamor, ppnenet):
    excess = (capex - depamor)
    ppc = (ppnenet - ppnenet.shift(252)).abs()
    base = (excess / ppc.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growth-capex vs 252d PP&E increment base, 21d slope window
def f28cx_f28_capex_exploration_intensity_growthshare_21d_slope_v035_signal(capex, depamor, ppnenet):
    excess = (capex - depamor)
    ppc = (ppnenet - ppnenet.shift(252)).abs()
    base = (excess / ppc.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of growth-capex vs 252d PP&E increment base, 63d slope window
def f28cx_f28_capex_exploration_intensity_growthshare_63d_slope_v036_signal(capex, depamor, ppnenet):
    excess = (capex - depamor)
    ppc = (ppnenet - ppnenet.shift(252)).abs()
    base = (excess / ppc.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log rnd/depamor exploration intensity base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddeplog_21d_slope_v037_signal(rnd, depamor):
    base = np.log1p(_f28_rnd_depamor(rnd, depamor).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log rnd/depamor exploration intensity base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddeplog_63d_slope_v038_signal(rnd, depamor):
    base = np.log1p(_f28_rnd_depamor(rnd, depamor).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log rnd/depamor exploration intensity base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddeplog_126d_slope_v039_signal(rnd, depamor):
    base = np.log1p(_f28_rnd_depamor(rnd, depamor).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/depamor exploration intensity base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddepz_63d_slope_v040_signal(rnd, depamor):
    base = _z(_f28_rnd_depamor(rnd, depamor), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/depamor exploration intensity base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddepz_126d_slope_v041_signal(rnd, depamor):
    base = _z(_f28_rnd_depamor(rnd, depamor), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/depamor exploration intensity base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddepz_21d_slope_v042_signal(rnd, depamor):
    base = _z(_f28_rnd_depamor(rnd, depamor), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/depamor base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprank_126d_slope_v043_signal(rnd, depamor):
    base = _rank(_f28_rnd_depamor(rnd, depamor), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/depamor base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprank_21d_slope_v044_signal(rnd, depamor):
    base = _rank(_f28_rnd_depamor(rnd, depamor), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/depamor base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprank_63d_slope_v045_signal(rnd, depamor):
    base = _rank(_f28_rnd_depamor(rnd, depamor), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/depamor minus its 252d median base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprelmed_21d_slope_v046_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/depamor minus its 252d median base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprelmed_63d_slope_v047_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/depamor minus its 252d median base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddeprelmed_126d_slope_v048_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = r - r.rolling(252, min_periods=63).median()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of rnd/depamor base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddepcv_63d_slope_v049_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of rnd/depamor base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddepcv_126d_slope_v050_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of coefficient of variation of rnd/depamor base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddepcv_21d_slope_v051_signal(rnd, depamor):
    r = _f28_rnd_depamor(rnd, depamor)
    base = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/capex mix displacement from slow EMA base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rndcapdisp_126d_slope_v052_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/capex mix displacement from slow EMA base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rndcapdisp_21d_slope_v053_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd/capex mix displacement from slow EMA base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rndcapdisp_63d_slope_v054_signal(rnd, capex):
    r = _f28_rnd_capex(rnd, capex)
    base = r - r.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/capex mix base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rndcaprank_21d_slope_v055_signal(rnd, capex):
    base = _rank(_f28_rnd_capex(rnd, capex), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/capex mix base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rndcaprank_63d_slope_v056_signal(rnd, capex):
    base = _rank(_f28_rnd_capex(rnd, capex), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/capex mix base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rndcaprank_126d_slope_v057_signal(rnd, capex):
    base = _rank(_f28_rnd_capex(rnd, capex), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/capex mix base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rndcapz_63d_slope_v058_signal(rnd, capex):
    base = _z(_f28_rnd_capex(rnd, capex), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/capex mix base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rndcapz_126d_slope_v059_signal(rnd, capex):
    base = _z(_f28_rnd_capex(rnd, capex), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/capex mix base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rndcapz_21d_slope_v060_signal(rnd, capex):
    base = _z(_f28_rnd_capex(rnd, capex), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration share relative to 1260d mean base, 126d slope window
def f28cx_f28_capex_exploration_intensity_explshare_126d_slope_v061_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = share - share.rolling(1260, min_periods=252).mean()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration share relative to 1260d mean base, 21d slope window
def f28cx_f28_capex_exploration_intensity_explshare_21d_slope_v062_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = share - share.rolling(1260, min_periods=252).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration share relative to 1260d mean base, 63d slope window
def f28cx_f28_capex_exploration_intensity_explshare_63d_slope_v063_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = share - share.rolling(1260, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of exploration share (mix instability) base, 21d slope window
def f28cx_f28_capex_exploration_intensity_explsharevol_21d_slope_v064_signal(capex, rnd):
    base = _std(_f28_explore_share(capex, rnd), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of exploration share (mix instability) base, 63d slope window
def f28cx_f28_capex_exploration_intensity_explsharevol_63d_slope_v065_signal(capex, rnd):
    base = _std(_f28_explore_share(capex, rnd), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of exploration share (mix instability) base, 126d slope window
def f28cx_f28_capex_exploration_intensity_explsharevol_126d_slope_v066_signal(capex, rnd):
    base = _std(_f28_explore_share(capex, rnd), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/ppnenet greenfield tilt base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rndppnerank_63d_slope_v067_signal(rnd, ppnenet):
    base = _rank(rnd / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/ppnenet greenfield tilt base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rndppnerank_126d_slope_v068_signal(rnd, ppnenet):
    base = _rank(rnd / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of rnd/ppnenet greenfield tilt base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rndppnerank_21d_slope_v069_signal(rnd, ppnenet):
    base = _rank(rnd / ppnenet.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of -ncfi/depamor investing-deployment multiple base, 126d slope window
def f28cx_f28_capex_exploration_intensity_ncfideplog_126d_slope_v070_signal(ncfi, depamor):
    base = _f28_invest_intensity(ncfi, depamor)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of -ncfi/depamor investing-deployment multiple base, 21d slope window
def f28cx_f28_capex_exploration_intensity_ncfideplog_21d_slope_v071_signal(ncfi, depamor):
    base = _f28_invest_intensity(ncfi, depamor)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of -ncfi/depamor investing-deployment multiple base, 63d slope window
def f28cx_f28_capex_exploration_intensity_ncfideplog_63d_slope_v072_signal(ncfi, depamor):
    base = _f28_invest_intensity(ncfi, depamor)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored -ncfi/depamor deployment base, 21d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepz_21d_slope_v073_signal(ncfi, depamor):
    base = _z(_f28_invest_intensity(ncfi, depamor), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored -ncfi/depamor deployment base, 63d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepz_63d_slope_v074_signal(ncfi, depamor):
    base = _z(_f28_invest_intensity(ncfi, depamor), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored -ncfi/depamor deployment base, 126d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepz_126d_slope_v075_signal(ncfi, depamor):
    base = _z(_f28_invest_intensity(ncfi, depamor), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of -ncfi/depamor deployment base, 63d slope window
def f28cx_f28_capex_exploration_intensity_ncfideprank_63d_slope_v076_signal(ncfi, depamor):
    base = _rank(_f28_invest_intensity(ncfi, depamor), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of -ncfi/depamor deployment base, 126d slope window
def f28cx_f28_capex_exploration_intensity_ncfideprank_126d_slope_v077_signal(ncfi, depamor):
    base = _rank(_f28_invest_intensity(ncfi, depamor), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of -ncfi/depamor deployment base, 21d slope window
def f28cx_f28_capex_exploration_intensity_ncfideprank_21d_slope_v078_signal(ncfi, depamor):
    base = _rank(_f28_invest_intensity(ncfi, depamor), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of deployment distance below its 504d peak base, 126d slope window
def f28cx_f28_capex_exploration_intensity_ncfideppeak_126d_slope_v079_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of deployment distance below its 504d peak base, 21d slope window
def f28cx_f28_capex_exploration_intensity_ncfideppeak_21d_slope_v080_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of deployment distance below its 504d peak base, 63d slope window
def f28cx_f28_capex_exploration_intensity_ncfideppeak_63d_slope_v081_signal(ncfi, depamor):
    r = _f28_invest_intensity(ncfi, depamor)
    base = r / _rmax(r, 504).replace(0, np.nan) - 1.0
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of ncfi/depamor deployment base, 21d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepvol_21d_slope_v082_signal(ncfi, depamor):
    base = _std(ncfi / depamor.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of ncfi/depamor deployment base, 63d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepvol_63d_slope_v083_signal(ncfi, depamor):
    base = _std(ncfi / depamor.replace(0, np.nan), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of ncfi/depamor deployment base, 126d slope window
def f28cx_f28_capex_exploration_intensity_ncfidepvol_126d_slope_v084_signal(ncfi, depamor):
    base = _std(ncfi / depamor.replace(0, np.nan), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex share of total investing magnitude base, 63d slope window
def f28cx_f28_capex_exploration_intensity_organicshare_63d_slope_v085_signal(capex, ncfi):
    base = capex / (capex + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex share of total investing magnitude base, 126d slope window
def f28cx_f28_capex_exploration_intensity_organicshare_126d_slope_v086_signal(capex, ncfi):
    base = capex / (capex + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of capex share of total investing magnitude base, 21d slope window
def f28cx_f28_capex_exploration_intensity_organicshare_21d_slope_v087_signal(capex, ncfi):
    base = capex / (capex + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/|ncfi| coverage base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capexcover_126d_slope_v088_signal(capex, ncfi):
    r = (capex / ncfi.abs().replace(0, np.nan)).clip(upper=5.0)
    base = _rank(r, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/|ncfi| coverage base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capexcover_21d_slope_v089_signal(capex, ncfi):
    r = (capex / ncfi.abs().replace(0, np.nan)).clip(upper=5.0)
    base = _rank(r, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex/|ncfi| coverage base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capexcover_63d_slope_v090_signal(capex, ncfi):
    r = (capex / ncfi.abs().replace(0, np.nan)).clip(upper=5.0)
    base = _rank(r, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored investing magnitude vs installed PP&E base, 21d slope window
def f28cx_f28_capex_exploration_intensity_deployppne_21d_slope_v091_signal(ncfi, ppnenet):
    base = _z(ncfi.abs() / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored investing magnitude vs installed PP&E base, 63d slope window
def f28cx_f28_capex_exploration_intensity_deployppne_63d_slope_v092_signal(ncfi, ppnenet):
    base = _z(ncfi.abs() / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored investing magnitude vs installed PP&E base, 126d slope window
def f28cx_f28_capex_exploration_intensity_deployppne_126d_slope_v093_signal(ncfi, ppnenet):
    base = _z(ncfi.abs() / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd share of total investing deployment base, 63d slope window
def f28cx_f28_capex_exploration_intensity_exploredeploy_63d_slope_v094_signal(rnd, ncfi):
    base = rnd / (rnd + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd share of total investing deployment base, 126d slope window
def f28cx_f28_capex_exploration_intensity_exploredeploy_126d_slope_v095_signal(rnd, ncfi):
    base = rnd / (rnd + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rnd share of total investing deployment base, 21d slope window
def f28cx_f28_capex_exploration_intensity_exploredeploy_21d_slope_v096_signal(rnd, ncfi):
    base = rnd / (rnd + ncfi.abs()).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log depamor/ppnenet asset-aging rate base, 126d slope window
def f28cx_f28_capex_exploration_intensity_aginglog_126d_slope_v097_signal(depamor, ppnenet):
    base = np.log1p(_f28_age(depamor, ppnenet).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log depamor/ppnenet asset-aging rate base, 21d slope window
def f28cx_f28_capex_exploration_intensity_aginglog_21d_slope_v098_signal(depamor, ppnenet):
    base = np.log1p(_f28_age(depamor, ppnenet).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of log depamor/ppnenet asset-aging rate base, 63d slope window
def f28cx_f28_capex_exploration_intensity_aginglog_63d_slope_v099_signal(depamor, ppnenet):
    base = np.log1p(_f28_age(depamor, ppnenet).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored asset-aging rate base, 21d slope window
def f28cx_f28_capex_exploration_intensity_agingz_21d_slope_v100_signal(depamor, ppnenet):
    base = _z(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored asset-aging rate base, 63d slope window
def f28cx_f28_capex_exploration_intensity_agingz_63d_slope_v101_signal(depamor, ppnenet):
    base = _z(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored asset-aging rate base, 126d slope window
def f28cx_f28_capex_exploration_intensity_agingz_126d_slope_v102_signal(depamor, ppnenet):
    base = _z(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of asset-aging rate base, 63d slope window
def f28cx_f28_capex_exploration_intensity_agingrank_63d_slope_v103_signal(depamor, ppnenet):
    base = _rank(_f28_age(depamor, ppnenet), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of asset-aging rate base, 126d slope window
def f28cx_f28_capex_exploration_intensity_agingrank_126d_slope_v104_signal(depamor, ppnenet):
    base = _rank(_f28_age(depamor, ppnenet), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of asset-aging rate base, 21d slope window
def f28cx_f28_capex_exploration_intensity_agingrank_21d_slope_v105_signal(depamor, ppnenet):
    base = _rank(_f28_age(depamor, ppnenet), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of asset-aging rate base, 126d slope window
def f28cx_f28_capex_exploration_intensity_agingvol_126d_slope_v106_signal(depamor, ppnenet):
    base = _std(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of asset-aging rate base, 21d slope window
def f28cx_f28_capex_exploration_intensity_agingvol_21d_slope_v107_signal(depamor, ppnenet):
    base = _std(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of volatility of asset-aging rate base, 63d slope window
def f28cx_f28_capex_exploration_intensity_agingvol_63d_slope_v108_signal(depamor, ppnenet):
    base = _std(_f28_age(depamor, ppnenet), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/ppnenet greenfield-vs-installed intensity base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rndppnez_21d_slope_v109_signal(rnd, ppnenet):
    base = _z(rnd / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/ppnenet greenfield-vs-installed intensity base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rndppnez_63d_slope_v110_signal(rnd, ppnenet):
    base = _z(rnd / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of z-scored rnd/ppnenet greenfield-vs-installed intensity base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rndppnez_126d_slope_v111_signal(rnd, ppnenet):
    base = _z(rnd / ppnenet.replace(0, np.nan), 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration contribution to total-investment z (tot z minus capex z) base, 63d slope window
def f28cx_f28_capex_exploration_intensity_totinvdepz_63d_slope_v112_signal(capex, rnd, depamor):
    tot = (capex + rnd) / depamor.replace(0, np.nan)
    cap = capex / depamor.replace(0, np.nan)
    base = _z(tot, 504) - _z(cap, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration contribution to total-investment z (tot z minus capex z) base, 126d slope window
def f28cx_f28_capex_exploration_intensity_totinvdepz_126d_slope_v113_signal(capex, rnd, depamor):
    tot = (capex + rnd) / depamor.replace(0, np.nan)
    cap = capex / depamor.replace(0, np.nan)
    base = _z(tot, 504) - _z(cap, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration contribution to total-investment z (tot z minus capex z) base, 21d slope window
def f28cx_f28_capex_exploration_intensity_totinvdepz_21d_slope_v114_signal(capex, rnd, depamor):
    tot = (capex + rnd) / depamor.replace(0, np.nan)
    cap = capex / depamor.replace(0, np.nan)
    base = _z(tot, 504) - _z(cap, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fraction of year total-investment above its 252d median base, 126d slope window
def f28cx_f28_capex_exploration_intensity_totinvregime_126d_slope_v115_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    med = r.rolling(252, min_periods=126).median()
    base = (r > med).astype(float).rolling(252, min_periods=126).mean()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fraction of year total-investment above its 252d median base, 21d slope window
def f28cx_f28_capex_exploration_intensity_totinvregime_21d_slope_v116_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    med = r.rolling(252, min_periods=126).median()
    base = (r > med).astype(float).rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of fraction of year total-investment above its 252d median base, 63d slope window
def f28cx_f28_capex_exploration_intensity_totinvregime_63d_slope_v117_signal(capex, rnd, depamor):
    r = (capex + rnd) / depamor.replace(0, np.nan)
    med = r.rolling(252, min_periods=126).median()
    base = (r > med).astype(float).rolling(252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion of exploration share across horizons base, 21d slope window
def f28cx_f28_capex_exploration_intensity_mixdisp_21d_slope_v118_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = pd.concat([_mean(share, 63), _mean(share, 126), _mean(share, 252)], axis=1).std(axis=1)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion of exploration share across horizons base, 63d slope window
def f28cx_f28_capex_exploration_intensity_mixdisp_63d_slope_v119_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = pd.concat([_mean(share, 63), _mean(share, 126), _mean(share, 252)], axis=1).std(axis=1)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion of exploration share across horizons base, 126d slope window
def f28cx_f28_capex_exploration_intensity_mixdisp_126d_slope_v120_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = pd.concat([_mean(share, 63), _mean(share, 126), _mean(share, 252)], axis=1).std(axis=1)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of (capex-rnd)/depamor build-vs-explore tilt base, 63d slope window
def f28cx_f28_capex_exploration_intensity_devexpltilt_63d_slope_v121_signal(capex, rnd, depamor):
    base = (capex - rnd) / depamor.replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of (capex-rnd)/depamor build-vs-explore tilt base, 126d slope window
def f28cx_f28_capex_exploration_intensity_devexpltilt_126d_slope_v122_signal(capex, rnd, depamor):
    base = (capex - rnd) / depamor.replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of (capex-rnd)/depamor build-vs-explore tilt base, 21d slope window
def f28cx_f28_capex_exploration_intensity_devexpltilt_21d_slope_v123_signal(capex, rnd, depamor):
    base = (capex - rnd) / depamor.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of build-vs-explore tilt base, 126d slope window
def f28cx_f28_capex_exploration_intensity_devexplrank_126d_slope_v124_signal(capex, rnd, depamor):
    base = _rank((capex - rnd) / depamor.replace(0, np.nan), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of build-vs-explore tilt base, 21d slope window
def f28cx_f28_capex_exploration_intensity_devexplrank_21d_slope_v125_signal(capex, rnd, depamor):
    base = _rank((capex - rnd) / depamor.replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of build-vs-explore tilt base, 63d slope window
def f28cx_f28_capex_exploration_intensity_devexplrank_63d_slope_v126_signal(capex, rnd, depamor):
    base = _rank((capex - rnd) / depamor.replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex vs combined maintenance+exploration call on funds base, 21d slope window
def f28cx_f28_capex_exploration_intensity_buildfund_21d_slope_v127_signal(capex, rnd, depamor):
    base = _rank(capex / (depamor + rnd).replace(0, np.nan), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex vs combined maintenance+exploration call on funds base, 63d slope window
def f28cx_f28_capex_exploration_intensity_buildfund_63d_slope_v128_signal(capex, rnd, depamor):
    base = _rank(capex / (depamor + rnd).replace(0, np.nan), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of 504d-rank of capex vs combined maintenance+exploration call on funds base, 126d slope window
def f28cx_f28_capex_exploration_intensity_buildfund_126d_slope_v129_signal(capex, rnd, depamor):
    base = _rank(capex / (depamor + rnd).replace(0, np.nan), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of quarterly change in exploration share base, 63d slope window
def f28cx_f28_capex_exploration_intensity_greenfieldmom_63d_slope_v130_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = np.tanh(5.0 * (share - share.shift(63)))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of quarterly change in exploration share base, 126d slope window
def f28cx_f28_capex_exploration_intensity_greenfieldmom_126d_slope_v131_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = np.tanh(5.0 * (share - share.shift(63)))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of quarterly change in exploration share base, 21d slope window
def f28cx_f28_capex_exploration_intensity_greenfieldmom_21d_slope_v132_signal(capex, rnd):
    share = _f28_explore_share(capex, rnd)
    base = np.tanh(5.0 * (share - share.shift(63)))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rolling corr of capex/dep and rnd/dep (joint ramp) base, 126d slope window
def f28cx_f28_capex_exploration_intensity_jointramp_126d_slope_v133_signal(capex, rnd, depamor):
    a = _f28_capex_depamor(capex, depamor); b2 = _f28_rnd_depamor(rnd, depamor)
    base = a.rolling(252, min_periods=126).corr(b2)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rolling corr of capex/dep and rnd/dep (joint ramp) base, 21d slope window
def f28cx_f28_capex_exploration_intensity_jointramp_21d_slope_v134_signal(capex, rnd, depamor):
    a = _f28_capex_depamor(capex, depamor); b2 = _f28_rnd_depamor(rnd, depamor)
    base = a.rolling(252, min_periods=126).corr(b2)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of rolling corr of capex/dep and rnd/dep (joint ramp) base, 63d slope window
def f28cx_f28_capex_exploration_intensity_jointramp_63d_slope_v135_signal(capex, rnd, depamor):
    a = _f28_capex_depamor(capex, depamor); b2 = _f28_rnd_depamor(rnd, depamor)
    base = a.rolling(252, min_periods=126).corr(b2)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion across intensity z-scores base, 21d slope window
def f28cx_f28_capex_exploration_intensity_intensdisp_21d_slope_v136_signal(capex, rnd, ncfi, depamor):
    a = _z(_f28_capex_depamor(capex, depamor), 252)
    b2 = _z(_f28_rnd_depamor(rnd, depamor), 252)
    c = _z(_f28_invest_intensity(ncfi, depamor), 252)
    base = pd.concat([a, b2, c], axis=1).std(axis=1)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion across intensity z-scores base, 63d slope window
def f28cx_f28_capex_exploration_intensity_intensdisp_63d_slope_v137_signal(capex, rnd, ncfi, depamor):
    a = _z(_f28_capex_depamor(capex, depamor), 252)
    b2 = _z(_f28_rnd_depamor(rnd, depamor), 252)
    c = _z(_f28_invest_intensity(ncfi, depamor), 252)
    base = pd.concat([a, b2, c], axis=1).std(axis=1)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of dispersion across intensity z-scores base, 126d slope window
def f28cx_f28_capex_exploration_intensity_intensdisp_126d_slope_v138_signal(capex, rnd, ncfi, depamor):
    a = _z(_f28_capex_depamor(capex, depamor), 252)
    b2 = _z(_f28_rnd_depamor(rnd, depamor), 252)
    c = _z(_f28_invest_intensity(ncfi, depamor), 252)
    base = pd.concat([a, b2, c], axis=1).std(axis=1)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of build magnitude gated by revenue near multi-year low base, 63d slope window
def f28cx_f28_capex_exploration_intensity_buildwhenlean_63d_slope_v139_signal(capex, depamor, revenue):
    capdep = _z(_f28_capex_depamor(capex, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = capdep * gate
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of build magnitude gated by revenue near multi-year low base, 126d slope window
def f28cx_f28_capex_exploration_intensity_buildwhenlean_126d_slope_v140_signal(capex, depamor, revenue):
    capdep = _z(_f28_capex_depamor(capex, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = capdep * gate
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of build magnitude gated by revenue near multi-year low base, 21d slope window
def f28cx_f28_capex_exploration_intensity_buildwhenlean_21d_slope_v141_signal(capex, depamor, revenue):
    capdep = _z(_f28_capex_depamor(capex, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = capdep * gate
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration magnitude gated by revenue near multi-year low base, 126d slope window
def f28cx_f28_capex_exploration_intensity_explwhenlean_126d_slope_v142_signal(rnd, depamor, revenue):
    expl = _z(_f28_rnd_depamor(rnd, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = expl * gate
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration magnitude gated by revenue near multi-year low base, 21d slope window
def f28cx_f28_capex_exploration_intensity_explwhenlean_21d_slope_v143_signal(rnd, depamor, revenue):
    expl = _z(_f28_rnd_depamor(rnd, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = expl * gate
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of exploration magnitude gated by revenue near multi-year low base, 63d slope window
def f28cx_f28_capex_exploration_intensity_explwhenlean_63d_slope_v144_signal(rnd, depamor, revenue):
    expl = _z(_f28_rnd_depamor(rnd, depamor), 126)
    gate = 1.0 - revenue.rolling(504, min_periods=126).rank(pct=True)
    base = expl * gate
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short capex/depamor surprise base, 21d slope window
def f28cx_f28_capex_exploration_intensity_capdeptanh_21d_slope_v145_signal(capex, depamor):
    base = np.tanh(_z(_f28_capex_depamor(capex, depamor), 63))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short capex/depamor surprise base, 63d slope window
def f28cx_f28_capex_exploration_intensity_capdeptanh_63d_slope_v146_signal(capex, depamor):
    base = np.tanh(_z(_f28_capex_depamor(capex, depamor), 63))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short capex/depamor surprise base, 126d slope window
def f28cx_f28_capex_exploration_intensity_capdeptanh_126d_slope_v147_signal(capex, depamor):
    base = np.tanh(_z(_f28_capex_depamor(capex, depamor), 63))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short rnd/depamor surprise base, 63d slope window
def f28cx_f28_capex_exploration_intensity_rnddeptanh_63d_slope_v148_signal(rnd, depamor):
    base = np.tanh(_z(_f28_rnd_depamor(rnd, depamor), 63))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short rnd/depamor surprise base, 126d slope window
def f28cx_f28_capex_exploration_intensity_rnddeptanh_126d_slope_v149_signal(rnd, depamor):
    base = np.tanh(_z(_f28_rnd_depamor(rnd, depamor), 63))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# slope of tanh of short rnd/depamor surprise base, 21d slope window
def f28cx_f28_capex_exploration_intensity_rnddeptanh_21d_slope_v150_signal(rnd, depamor):
    base = np.tanh(_z(_f28_rnd_depamor(rnd, depamor), 63))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28cx_f28_capex_exploration_intensity_capdeplog_21d_slope_v001_signal,
    f28cx_f28_capex_exploration_intensity_capdeplog_63d_slope_v002_signal,
    f28cx_f28_capex_exploration_intensity_capdeplog_126d_slope_v003_signal,
    f28cx_f28_capex_exploration_intensity_capdepz_63d_slope_v004_signal,
    f28cx_f28_capex_exploration_intensity_capdepz_126d_slope_v005_signal,
    f28cx_f28_capex_exploration_intensity_capdepz_21d_slope_v006_signal,
    f28cx_f28_capex_exploration_intensity_capdeprank_126d_slope_v007_signal,
    f28cx_f28_capex_exploration_intensity_capdeprank_21d_slope_v008_signal,
    f28cx_f28_capex_exploration_intensity_capdeprank_63d_slope_v009_signal,
    f28cx_f28_capex_exploration_intensity_capdeppeak_21d_slope_v010_signal,
    f28cx_f28_capex_exploration_intensity_capdeppeak_63d_slope_v011_signal,
    f28cx_f28_capex_exploration_intensity_capdeppeak_126d_slope_v012_signal,
    f28cx_f28_capex_exploration_intensity_capdeprelmed_63d_slope_v013_signal,
    f28cx_f28_capex_exploration_intensity_capdeprelmed_126d_slope_v014_signal,
    f28cx_f28_capex_exploration_intensity_capdeprelmed_21d_slope_v015_signal,
    f28cx_f28_capex_exploration_intensity_capdepslr_126d_slope_v016_signal,
    f28cx_f28_capex_exploration_intensity_capdepslr_21d_slope_v017_signal,
    f28cx_f28_capex_exploration_intensity_capdepslr_63d_slope_v018_signal,
    f28cx_f28_capex_exploration_intensity_capdepcv_21d_slope_v019_signal,
    f28cx_f28_capex_exploration_intensity_capdepcv_63d_slope_v020_signal,
    f28cx_f28_capex_exploration_intensity_capdepcv_126d_slope_v021_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_63d_slope_v022_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_126d_slope_v023_signal,
    f28cx_f28_capex_exploration_intensity_excessppne_21d_slope_v024_signal,
    f28cx_f28_capex_exploration_intensity_excessppnez_126d_slope_v025_signal,
    f28cx_f28_capex_exploration_intensity_excessppnez_21d_slope_v026_signal,
    f28cx_f28_capex_exploration_intensity_excessppnez_63d_slope_v027_signal,
    f28cx_f28_capex_exploration_intensity_excessppnerank_21d_slope_v028_signal,
    f28cx_f28_capex_exploration_intensity_excessppnerank_63d_slope_v029_signal,
    f28cx_f28_capex_exploration_intensity_excessppnerank_126d_slope_v030_signal,
    f28cx_f28_capex_exploration_intensity_excessvol_63d_slope_v031_signal,
    f28cx_f28_capex_exploration_intensity_excessvol_126d_slope_v032_signal,
    f28cx_f28_capex_exploration_intensity_excessvol_21d_slope_v033_signal,
    f28cx_f28_capex_exploration_intensity_growthshare_126d_slope_v034_signal,
    f28cx_f28_capex_exploration_intensity_growthshare_21d_slope_v035_signal,
    f28cx_f28_capex_exploration_intensity_growthshare_63d_slope_v036_signal,
    f28cx_f28_capex_exploration_intensity_rnddeplog_21d_slope_v037_signal,
    f28cx_f28_capex_exploration_intensity_rnddeplog_63d_slope_v038_signal,
    f28cx_f28_capex_exploration_intensity_rnddeplog_126d_slope_v039_signal,
    f28cx_f28_capex_exploration_intensity_rnddepz_63d_slope_v040_signal,
    f28cx_f28_capex_exploration_intensity_rnddepz_126d_slope_v041_signal,
    f28cx_f28_capex_exploration_intensity_rnddepz_21d_slope_v042_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprank_126d_slope_v043_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprank_21d_slope_v044_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprank_63d_slope_v045_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprelmed_21d_slope_v046_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprelmed_63d_slope_v047_signal,
    f28cx_f28_capex_exploration_intensity_rnddeprelmed_126d_slope_v048_signal,
    f28cx_f28_capex_exploration_intensity_rnddepcv_63d_slope_v049_signal,
    f28cx_f28_capex_exploration_intensity_rnddepcv_126d_slope_v050_signal,
    f28cx_f28_capex_exploration_intensity_rnddepcv_21d_slope_v051_signal,
    f28cx_f28_capex_exploration_intensity_rndcapdisp_126d_slope_v052_signal,
    f28cx_f28_capex_exploration_intensity_rndcapdisp_21d_slope_v053_signal,
    f28cx_f28_capex_exploration_intensity_rndcapdisp_63d_slope_v054_signal,
    f28cx_f28_capex_exploration_intensity_rndcaprank_21d_slope_v055_signal,
    f28cx_f28_capex_exploration_intensity_rndcaprank_63d_slope_v056_signal,
    f28cx_f28_capex_exploration_intensity_rndcaprank_126d_slope_v057_signal,
    f28cx_f28_capex_exploration_intensity_rndcapz_63d_slope_v058_signal,
    f28cx_f28_capex_exploration_intensity_rndcapz_126d_slope_v059_signal,
    f28cx_f28_capex_exploration_intensity_rndcapz_21d_slope_v060_signal,
    f28cx_f28_capex_exploration_intensity_explshare_126d_slope_v061_signal,
    f28cx_f28_capex_exploration_intensity_explshare_21d_slope_v062_signal,
    f28cx_f28_capex_exploration_intensity_explshare_63d_slope_v063_signal,
    f28cx_f28_capex_exploration_intensity_explsharevol_21d_slope_v064_signal,
    f28cx_f28_capex_exploration_intensity_explsharevol_63d_slope_v065_signal,
    f28cx_f28_capex_exploration_intensity_explsharevol_126d_slope_v066_signal,
    f28cx_f28_capex_exploration_intensity_rndppnerank_63d_slope_v067_signal,
    f28cx_f28_capex_exploration_intensity_rndppnerank_126d_slope_v068_signal,
    f28cx_f28_capex_exploration_intensity_rndppnerank_21d_slope_v069_signal,
    f28cx_f28_capex_exploration_intensity_ncfideplog_126d_slope_v070_signal,
    f28cx_f28_capex_exploration_intensity_ncfideplog_21d_slope_v071_signal,
    f28cx_f28_capex_exploration_intensity_ncfideplog_63d_slope_v072_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepz_21d_slope_v073_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepz_63d_slope_v074_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepz_126d_slope_v075_signal,
    f28cx_f28_capex_exploration_intensity_ncfideprank_63d_slope_v076_signal,
    f28cx_f28_capex_exploration_intensity_ncfideprank_126d_slope_v077_signal,
    f28cx_f28_capex_exploration_intensity_ncfideprank_21d_slope_v078_signal,
    f28cx_f28_capex_exploration_intensity_ncfideppeak_126d_slope_v079_signal,
    f28cx_f28_capex_exploration_intensity_ncfideppeak_21d_slope_v080_signal,
    f28cx_f28_capex_exploration_intensity_ncfideppeak_63d_slope_v081_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepvol_21d_slope_v082_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepvol_63d_slope_v083_signal,
    f28cx_f28_capex_exploration_intensity_ncfidepvol_126d_slope_v084_signal,
    f28cx_f28_capex_exploration_intensity_organicshare_63d_slope_v085_signal,
    f28cx_f28_capex_exploration_intensity_organicshare_126d_slope_v086_signal,
    f28cx_f28_capex_exploration_intensity_organicshare_21d_slope_v087_signal,
    f28cx_f28_capex_exploration_intensity_capexcover_126d_slope_v088_signal,
    f28cx_f28_capex_exploration_intensity_capexcover_21d_slope_v089_signal,
    f28cx_f28_capex_exploration_intensity_capexcover_63d_slope_v090_signal,
    f28cx_f28_capex_exploration_intensity_deployppne_21d_slope_v091_signal,
    f28cx_f28_capex_exploration_intensity_deployppne_63d_slope_v092_signal,
    f28cx_f28_capex_exploration_intensity_deployppne_126d_slope_v093_signal,
    f28cx_f28_capex_exploration_intensity_exploredeploy_63d_slope_v094_signal,
    f28cx_f28_capex_exploration_intensity_exploredeploy_126d_slope_v095_signal,
    f28cx_f28_capex_exploration_intensity_exploredeploy_21d_slope_v096_signal,
    f28cx_f28_capex_exploration_intensity_aginglog_126d_slope_v097_signal,
    f28cx_f28_capex_exploration_intensity_aginglog_21d_slope_v098_signal,
    f28cx_f28_capex_exploration_intensity_aginglog_63d_slope_v099_signal,
    f28cx_f28_capex_exploration_intensity_agingz_21d_slope_v100_signal,
    f28cx_f28_capex_exploration_intensity_agingz_63d_slope_v101_signal,
    f28cx_f28_capex_exploration_intensity_agingz_126d_slope_v102_signal,
    f28cx_f28_capex_exploration_intensity_agingrank_63d_slope_v103_signal,
    f28cx_f28_capex_exploration_intensity_agingrank_126d_slope_v104_signal,
    f28cx_f28_capex_exploration_intensity_agingrank_21d_slope_v105_signal,
    f28cx_f28_capex_exploration_intensity_agingvol_126d_slope_v106_signal,
    f28cx_f28_capex_exploration_intensity_agingvol_21d_slope_v107_signal,
    f28cx_f28_capex_exploration_intensity_agingvol_63d_slope_v108_signal,
    f28cx_f28_capex_exploration_intensity_rndppnez_21d_slope_v109_signal,
    f28cx_f28_capex_exploration_intensity_rndppnez_63d_slope_v110_signal,
    f28cx_f28_capex_exploration_intensity_rndppnez_126d_slope_v111_signal,
    f28cx_f28_capex_exploration_intensity_totinvdepz_63d_slope_v112_signal,
    f28cx_f28_capex_exploration_intensity_totinvdepz_126d_slope_v113_signal,
    f28cx_f28_capex_exploration_intensity_totinvdepz_21d_slope_v114_signal,
    f28cx_f28_capex_exploration_intensity_totinvregime_126d_slope_v115_signal,
    f28cx_f28_capex_exploration_intensity_totinvregime_21d_slope_v116_signal,
    f28cx_f28_capex_exploration_intensity_totinvregime_63d_slope_v117_signal,
    f28cx_f28_capex_exploration_intensity_mixdisp_21d_slope_v118_signal,
    f28cx_f28_capex_exploration_intensity_mixdisp_63d_slope_v119_signal,
    f28cx_f28_capex_exploration_intensity_mixdisp_126d_slope_v120_signal,
    f28cx_f28_capex_exploration_intensity_devexpltilt_63d_slope_v121_signal,
    f28cx_f28_capex_exploration_intensity_devexpltilt_126d_slope_v122_signal,
    f28cx_f28_capex_exploration_intensity_devexpltilt_21d_slope_v123_signal,
    f28cx_f28_capex_exploration_intensity_devexplrank_126d_slope_v124_signal,
    f28cx_f28_capex_exploration_intensity_devexplrank_21d_slope_v125_signal,
    f28cx_f28_capex_exploration_intensity_devexplrank_63d_slope_v126_signal,
    f28cx_f28_capex_exploration_intensity_buildfund_21d_slope_v127_signal,
    f28cx_f28_capex_exploration_intensity_buildfund_63d_slope_v128_signal,
    f28cx_f28_capex_exploration_intensity_buildfund_126d_slope_v129_signal,
    f28cx_f28_capex_exploration_intensity_greenfieldmom_63d_slope_v130_signal,
    f28cx_f28_capex_exploration_intensity_greenfieldmom_126d_slope_v131_signal,
    f28cx_f28_capex_exploration_intensity_greenfieldmom_21d_slope_v132_signal,
    f28cx_f28_capex_exploration_intensity_jointramp_126d_slope_v133_signal,
    f28cx_f28_capex_exploration_intensity_jointramp_21d_slope_v134_signal,
    f28cx_f28_capex_exploration_intensity_jointramp_63d_slope_v135_signal,
    f28cx_f28_capex_exploration_intensity_intensdisp_21d_slope_v136_signal,
    f28cx_f28_capex_exploration_intensity_intensdisp_63d_slope_v137_signal,
    f28cx_f28_capex_exploration_intensity_intensdisp_126d_slope_v138_signal,
    f28cx_f28_capex_exploration_intensity_buildwhenlean_63d_slope_v139_signal,
    f28cx_f28_capex_exploration_intensity_buildwhenlean_126d_slope_v140_signal,
    f28cx_f28_capex_exploration_intensity_buildwhenlean_21d_slope_v141_signal,
    f28cx_f28_capex_exploration_intensity_explwhenlean_126d_slope_v142_signal,
    f28cx_f28_capex_exploration_intensity_explwhenlean_21d_slope_v143_signal,
    f28cx_f28_capex_exploration_intensity_explwhenlean_63d_slope_v144_signal,
    f28cx_f28_capex_exploration_intensity_capdeptanh_21d_slope_v145_signal,
    f28cx_f28_capex_exploration_intensity_capdeptanh_63d_slope_v146_signal,
    f28cx_f28_capex_exploration_intensity_capdeptanh_126d_slope_v147_signal,
    f28cx_f28_capex_exploration_intensity_rnddeptanh_63d_slope_v148_signal,
    f28cx_f28_capex_exploration_intensity_rnddeptanh_126d_slope_v149_signal,
    f28cx_f28_capex_exploration_intensity_rnddeptanh_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_CAPEX_EXPLORATION_INTENSITY_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    capex = _fund(2801, base=7e7, drift=0.01, vol=0.18).rename("capex")
    rnd = _fund(2802, base=2e7, drift=0.0, vol=0.20).rename("rnd")
    revenue = _fund(2803, base=3e8, drift=0.01, vol=0.12).rename("revenue")
    assets = _fund(2804, base=1.5e9, drift=0.005, vol=0.06).rename("assets")
    ppnenet = _fund(2805, base=8e8, drift=0.008, vol=0.07).rename("ppnenet")
    ncfi = _fund(2806, base=9e7, drift=0.0, vol=0.30, allow_neg=True).rename("ncfi")
    depamor = _fund(2807, base=5e7, drift=0.006, vol=0.10).rename("depamor")

    cols = {"capex": capex, "rnd": rnd, "revenue": revenue,
            "assets": assets, "ppnenet": ppnenet, "ncfi": ncfi, "depamor": depamor}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("capex", "rnd", "revenue", "assets", "ppnenet", "ncfi", "depamor")
                   for c in meta["inputs"]), name
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f28_capex_exploration_intensity_2nd_derivatives_001_150_claude: %d features pass" % n_features)
