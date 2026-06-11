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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f26_dilution_rate(sharesbas, w):
    base = sharesbas.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f26_share_growth(sharesbas, w):
    return sharesbas.diff(periods=w) / sharesbas.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f26_dilution_acceleration(sharesbas, w):
    g = _f26_dilution_rate(sharesbas, w)
    return g.diff(periods=w)


# 21d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_21d_base_v001_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_63d_base_v002_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_126d_base_v003_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_252d_base_v004_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_504d_base_v005_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d share growth × close
def f26dr_f26_dilution_rate_sharegrowth_21d_base_v006_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × close
def f26dr_f26_dilution_rate_sharegrowth_63d_base_v007_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d share growth × close
def f26dr_f26_dilution_rate_sharegrowth_126d_base_v008_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d share growth × close
def f26dr_f26_dilution_rate_sharegrowth_252d_base_v009_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d share growth × close
def f26dr_f26_dilution_rate_sharegrowth_504d_base_v010_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution acceleration × close
def f26dr_f26_dilution_rate_dilaccel_21d_base_v011_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution acceleration × close
def f26dr_f26_dilution_rate_dilaccel_63d_base_v012_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d dilution acceleration × close
def f26dr_f26_dilution_rate_dilaccel_126d_base_v013_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution acceleration × close
def f26dr_f26_dilution_rate_dilaccel_252d_base_v014_signal(sharesbas, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d mean dilution rate × close
def f26dr_f26_dilution_rate_dilratemean_63d_base_v015_signal(sharesbas, closeadj):
    result = _mean(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d mean dilution rate × close
def f26dr_f26_dilution_rate_dilratemean_252d_base_v016_signal(sharesbas, closeadj):
    result = _mean(_f26_dilution_rate(sharesbas, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d std dilution rate × close
def f26dr_f26_dilution_rate_dilratestd_63d_base_v017_signal(sharesbas, closeadj):
    result = _std(_f26_dilution_rate(sharesbas, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std dilution rate × close
def f26dr_f26_dilution_rate_dilratestd_252d_base_v018_signal(sharesbas, closeadj):
    result = _std(_f26_dilution_rate(sharesbas, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of dilution rate × close
def f26dr_f26_dilution_rate_dilratez_252d_base_v019_signal(sharesbas, closeadj):
    result = _z(_f26_dilution_rate(sharesbas, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of dilution rate × close
def f26dr_f26_dilution_rate_dilratez_504d_base_v020_signal(sharesbas, closeadj):
    result = _z(_f26_dilution_rate(sharesbas, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of share growth × close
def f26dr_f26_dilution_rate_sharegrowthz_252d_base_v021_signal(sharesbas, closeadj):
    result = _z(_f26_share_growth(sharesbas, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of share growth × close
def f26dr_f26_dilution_rate_sharegrowthz_504d_base_v022_signal(sharesbas, closeadj):
    result = _z(_f26_share_growth(sharesbas, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high dilution (>1%)
def f26dr_f26_dilution_rate_dilhighcount_252d_base_v023_signal(sharesbas, closeadj):
    flag = (_f26_dilution_rate(sharesbas, 63) > 0.01).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean dilution × closeadj (continuous)
def f26dr_f26_dilution_rate_buybackcount_504d_base_v024_signal(sharesbas, closeadj):
    base = _f26_dilution_rate(sharesbas, 252)
    result = base.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of strong dilution (>3%)
def f26dr_f26_dilution_rate_dilstrongcount_252d_base_v025_signal(sharesbas, closeadj):
    flag = (_f26_dilution_rate(sharesbas, 63) > 0.03).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution rate squared × close
def f26dr_f26_dilution_rate_dilratesq_21d_base_v026_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution rate squared × close
def f26dr_f26_dilution_rate_dilratesq_63d_base_v027_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution rate squared × close
def f26dr_f26_dilution_rate_dilratesq_252d_base_v028_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × revenue
def f26dr_f26_dilution_rate_dilxrev_21d_base_v029_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × revenue
def f26dr_f26_dilution_rate_dilxrev_63d_base_v030_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × revenue
def f26dr_f26_dilution_rate_dilxrev_252d_base_v031_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# dilution diff 21m63 × close
def f26dr_f26_dilution_rate_dildiff_21m63_base_v032_signal(sharesbas, closeadj):
    result = (_f26_dilution_rate(sharesbas, 21) - _f26_dilution_rate(sharesbas, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution diff 63m252 × close
def f26dr_f26_dilution_rate_dildiff_63m252_base_v033_signal(sharesbas, closeadj):
    result = (_f26_dilution_rate(sharesbas, 63) - _f26_dilution_rate(sharesbas, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution diff 252m504 × close
def f26dr_f26_dilution_rate_dildiff_252m504_base_v034_signal(sharesbas, closeadj):
    result = (_f26_dilution_rate(sharesbas, 252) - _f26_dilution_rate(sharesbas, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution ratio 63v252 × close
def f26dr_f26_dilution_rate_dilratio_63v252_base_v035_signal(sharesbas, closeadj):
    a = _f26_dilution_rate(sharesbas, 63)
    b = _f26_dilution_rate(sharesbas, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# dilution ratio 21v63 × close
def f26dr_f26_dilution_rate_dilratio_21v63_base_v036_signal(sharesbas, closeadj):
    a = _f26_dilution_rate(sharesbas, 21)
    b = _f26_dilution_rate(sharesbas, 63).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d × 252d dilution product (consistent dilution)
def f26dr_f26_dilution_rate_dilprod_63x252_base_v037_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * _f26_dilution_rate(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × ebitda
def f26dr_f26_dilution_rate_dilxebitda_21d_base_v038_signal(sharesbas, ebitda, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × ebitda
def f26dr_f26_dilution_rate_dilxebitda_252d_base_v039_signal(sharesbas, ebitda, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × netinc
def f26dr_f26_dilution_rate_dilxnetinc_63d_base_v040_signal(sharesbas, netinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × netinc
def f26dr_f26_dilution_rate_dilxnetinc_252d_base_v041_signal(sharesbas, netinc, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × fcf
def f26dr_f26_dilution_rate_dilxfcf_21d_base_v042_signal(sharesbas, fcf, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × fcf
def f26dr_f26_dilution_rate_dilxfcf_252d_base_v043_signal(sharesbas, fcf, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × ncfo
def f26dr_f26_dilution_rate_dilxncfo_252d_base_v044_signal(sharesbas, ncfo, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 21d max dilution × close
def f26dr_f26_dilution_rate_dilmax_63d_base_v045_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 63d max dilution × close
def f26dr_f26_dilution_rate_dilmax_252d_base_v046_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sum of 21d dilution × close
def f26dr_f26_dilution_rate_dilsum_63d_base_v047_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of 63d dilution × close
def f26dr_f26_dilution_rate_dilsum_252d_base_v048_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of 21d share growth × close
def f26dr_f26_dilution_rate_sharegrowthsum_252d_base_v049_signal(sharesbas, closeadj):
    result = _f26_share_growth(sharesbas, 21).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × abs(capex)
def f26dr_f26_dilution_rate_dilxcapex_63d_base_v050_signal(sharesbas, capex, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × abs(capex)
def f26dr_f26_dilution_rate_dilxcapex_252d_base_v051_signal(sharesbas, capex, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d share growth × abs(capex)
def f26dr_f26_dilution_rate_sharegrowthxcapex_63d_base_v052_signal(sharesbas, capex, closeadj):
    result = _f26_share_growth(sharesbas, 63) * capex.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × abs(ncff) (financing context)
def f26dr_f26_dilution_rate_dilxncff_21d_base_v053_signal(sharesbas, ncff, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × abs(ncff)
def f26dr_f26_dilution_rate_dilxncff_252d_base_v054_signal(sharesbas, ncff, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * ncff.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of dilution × close
def f26dr_f26_dilution_rate_dilema_63d_base_v055_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of dilution × close
def f26dr_f26_dilution_rate_dilema_252d_base_v056_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of share growth × close
def f26dr_f26_dilution_rate_sharegrowthema_63d_base_v057_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 63)
    result = g.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of share growth × close
def f26dr_f26_dilution_rate_sharegrowthema_252d_base_v058_signal(sharesbas, closeadj):
    g = _f26_share_growth(sharesbas, 252)
    result = g.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution accel × ebitda
def f26dr_f26_dilution_rate_dilaccelxebitda_21d_base_v059_signal(sharesbas, ebitda, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution accel × ebitda
def f26dr_f26_dilution_rate_dilaccelxebitda_63d_base_v060_signal(sharesbas, ebitda, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 63) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution accel × revenue
def f26dr_f26_dilution_rate_dilaccelxrev_252d_base_v061_signal(sharesbas, revenue, closeadj):
    result = _f26_dilution_acceleration(sharesbas, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of dilution accel × close
def f26dr_f26_dilution_rate_dilaccelz_252d_base_v062_signal(sharesbas, closeadj):
    result = _z(_f26_dilution_acceleration(sharesbas, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d zscore of dilution accel × close
def f26dr_f26_dilution_rate_dilaccelz_504d_base_v063_signal(sharesbas, closeadj):
    result = _z(_f26_dilution_acceleration(sharesbas, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_5d_base_v064_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_10d_base_v065_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_42d_base_v066_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_189d_base_v067_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d dilution rate × close
def f26dr_f26_dilution_rate_dilrate_378d_base_v068_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution area × close
def f26dr_f26_dilution_rate_dilarea_252d_base_v069_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dilution area × close
def f26dr_f26_dilution_rate_dilarea_504d_base_v070_signal(sharesbas, closeadj):
    g = _f26_dilution_rate(sharesbas, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × marketcap
def f26dr_f26_dilution_rate_dilxmcap_252d_base_v071_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution × marketcap
def f26dr_f26_dilution_rate_dilxmcap_63d_base_v072_signal(sharesbas, closeadj):
    result = _f26_dilution_rate(sharesbas, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × equity
def f26dr_f26_dilution_rate_dilxequity_21d_base_v073_signal(sharesbas, equity, closeadj):
    result = _f26_dilution_rate(sharesbas, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × equity
def f26dr_f26_dilution_rate_dilxequity_252d_base_v074_signal(sharesbas, equity, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × assets
def f26dr_f26_dilution_rate_dilxassets_252d_base_v075_signal(sharesbas, assets, closeadj):
    result = _f26_dilution_rate(sharesbas, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26dr_f26_dilution_rate_dilrate_21d_base_v001_signal,
    f26dr_f26_dilution_rate_dilrate_63d_base_v002_signal,
    f26dr_f26_dilution_rate_dilrate_126d_base_v003_signal,
    f26dr_f26_dilution_rate_dilrate_252d_base_v004_signal,
    f26dr_f26_dilution_rate_dilrate_504d_base_v005_signal,
    f26dr_f26_dilution_rate_sharegrowth_21d_base_v006_signal,
    f26dr_f26_dilution_rate_sharegrowth_63d_base_v007_signal,
    f26dr_f26_dilution_rate_sharegrowth_126d_base_v008_signal,
    f26dr_f26_dilution_rate_sharegrowth_252d_base_v009_signal,
    f26dr_f26_dilution_rate_sharegrowth_504d_base_v010_signal,
    f26dr_f26_dilution_rate_dilaccel_21d_base_v011_signal,
    f26dr_f26_dilution_rate_dilaccel_63d_base_v012_signal,
    f26dr_f26_dilution_rate_dilaccel_126d_base_v013_signal,
    f26dr_f26_dilution_rate_dilaccel_252d_base_v014_signal,
    f26dr_f26_dilution_rate_dilratemean_63d_base_v015_signal,
    f26dr_f26_dilution_rate_dilratemean_252d_base_v016_signal,
    f26dr_f26_dilution_rate_dilratestd_63d_base_v017_signal,
    f26dr_f26_dilution_rate_dilratestd_252d_base_v018_signal,
    f26dr_f26_dilution_rate_dilratez_252d_base_v019_signal,
    f26dr_f26_dilution_rate_dilratez_504d_base_v020_signal,
    f26dr_f26_dilution_rate_sharegrowthz_252d_base_v021_signal,
    f26dr_f26_dilution_rate_sharegrowthz_504d_base_v022_signal,
    f26dr_f26_dilution_rate_dilhighcount_252d_base_v023_signal,
    f26dr_f26_dilution_rate_buybackcount_504d_base_v024_signal,
    f26dr_f26_dilution_rate_dilstrongcount_252d_base_v025_signal,
    f26dr_f26_dilution_rate_dilratesq_21d_base_v026_signal,
    f26dr_f26_dilution_rate_dilratesq_63d_base_v027_signal,
    f26dr_f26_dilution_rate_dilratesq_252d_base_v028_signal,
    f26dr_f26_dilution_rate_dilxrev_21d_base_v029_signal,
    f26dr_f26_dilution_rate_dilxrev_63d_base_v030_signal,
    f26dr_f26_dilution_rate_dilxrev_252d_base_v031_signal,
    f26dr_f26_dilution_rate_dildiff_21m63_base_v032_signal,
    f26dr_f26_dilution_rate_dildiff_63m252_base_v033_signal,
    f26dr_f26_dilution_rate_dildiff_252m504_base_v034_signal,
    f26dr_f26_dilution_rate_dilratio_63v252_base_v035_signal,
    f26dr_f26_dilution_rate_dilratio_21v63_base_v036_signal,
    f26dr_f26_dilution_rate_dilprod_63x252_base_v037_signal,
    f26dr_f26_dilution_rate_dilxebitda_21d_base_v038_signal,
    f26dr_f26_dilution_rate_dilxebitda_252d_base_v039_signal,
    f26dr_f26_dilution_rate_dilxnetinc_63d_base_v040_signal,
    f26dr_f26_dilution_rate_dilxnetinc_252d_base_v041_signal,
    f26dr_f26_dilution_rate_dilxfcf_21d_base_v042_signal,
    f26dr_f26_dilution_rate_dilxfcf_252d_base_v043_signal,
    f26dr_f26_dilution_rate_dilxncfo_252d_base_v044_signal,
    f26dr_f26_dilution_rate_dilmax_63d_base_v045_signal,
    f26dr_f26_dilution_rate_dilmax_252d_base_v046_signal,
    f26dr_f26_dilution_rate_dilsum_63d_base_v047_signal,
    f26dr_f26_dilution_rate_dilsum_252d_base_v048_signal,
    f26dr_f26_dilution_rate_sharegrowthsum_252d_base_v049_signal,
    f26dr_f26_dilution_rate_dilxcapex_63d_base_v050_signal,
    f26dr_f26_dilution_rate_dilxcapex_252d_base_v051_signal,
    f26dr_f26_dilution_rate_sharegrowthxcapex_63d_base_v052_signal,
    f26dr_f26_dilution_rate_dilxncff_21d_base_v053_signal,
    f26dr_f26_dilution_rate_dilxncff_252d_base_v054_signal,
    f26dr_f26_dilution_rate_dilema_63d_base_v055_signal,
    f26dr_f26_dilution_rate_dilema_252d_base_v056_signal,
    f26dr_f26_dilution_rate_sharegrowthema_63d_base_v057_signal,
    f26dr_f26_dilution_rate_sharegrowthema_252d_base_v058_signal,
    f26dr_f26_dilution_rate_dilaccelxebitda_21d_base_v059_signal,
    f26dr_f26_dilution_rate_dilaccelxebitda_63d_base_v060_signal,
    f26dr_f26_dilution_rate_dilaccelxrev_252d_base_v061_signal,
    f26dr_f26_dilution_rate_dilaccelz_252d_base_v062_signal,
    f26dr_f26_dilution_rate_dilaccelz_504d_base_v063_signal,
    f26dr_f26_dilution_rate_dilrate_5d_base_v064_signal,
    f26dr_f26_dilution_rate_dilrate_10d_base_v065_signal,
    f26dr_f26_dilution_rate_dilrate_42d_base_v066_signal,
    f26dr_f26_dilution_rate_dilrate_189d_base_v067_signal,
    f26dr_f26_dilution_rate_dilrate_378d_base_v068_signal,
    f26dr_f26_dilution_rate_dilarea_252d_base_v069_signal,
    f26dr_f26_dilution_rate_dilarea_504d_base_v070_signal,
    f26dr_f26_dilution_rate_dilxmcap_252d_base_v071_signal,
    f26dr_f26_dilution_rate_dilxmcap_63d_base_v072_signal,
    f26dr_f26_dilution_rate_dilxequity_21d_base_v073_signal,
    f26dr_f26_dilution_rate_dilxequity_252d_base_v074_signal,
    f26dr_f26_dilution_rate_dilxassets_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_DILUTION_RATE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    ncff = pd.Series(-2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="ncff")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "ncff": ncff, "equity": equity, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_dilution_rate", "_f26_share_growth", "_f26_dilution_acceleration")
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
    print(f"OK f26_dilution_rate_base_001_075_claude: {n_features} features pass")
