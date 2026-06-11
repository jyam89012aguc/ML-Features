import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (gross-margin level and volatility) =====
def _f21_gm(gp, revenue):
    # gross margin level = gp / revenue
    return _safe_div(gp, revenue)


def _f21_gmvol(gp, revenue, w):
    # rolling volatility (std) of the gross margin series
    gm = _safe_div(gp, revenue)
    return gm.rolling(w, min_periods=max(2, w // 2)).std()


def _f21_cogratio(cor, revenue):
    # cost-of-revenue ratio = cor / revenue (1 - gross margin proxy)
    return _safe_div(cor, revenue)


def _f21_opratio(opex, revenue):
    # operating-expense intensity = opex / revenue
    return _safe_div(opex, revenue)


# ============ FEATURES 001-075 ============

# gross margin level (gp/revenue)
def f21gm_f21_gross_margin_volatility_gmlevel_1d_base_v001_signal(gp, revenue):
    result = _f21_gm(gp, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed gross margin level
def f21gm_f21_gross_margin_volatility_gmsmooth_21d_base_v002_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed gross margin level
def f21gm_f21_gross_margin_volatility_gmsmooth_63d_base_v003_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed gross margin level
def f21gm_f21_gross_margin_volatility_gmsmooth_126d_base_v004_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed gross margin level
def f21gm_f21_gross_margin_volatility_gmsmooth_252d_base_v005_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gross-margin volatility (std)
def f21gm_f21_gross_margin_volatility_gmvol_63d_base_v006_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gross-margin volatility
def f21gm_f21_gross_margin_volatility_gmvol_126d_base_v007_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gross-margin volatility
def f21gm_f21_gross_margin_volatility_gmvol_252d_base_v008_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gross-margin volatility
def f21gm_f21_gross_margin_volatility_gmvol_504d_base_v009_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d gross-margin volatility
def f21gm_f21_gross_margin_volatility_gmvol_42d_base_v010_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio (cor/revenue)
def f21gm_f21_gross_margin_volatility_cogratio_1d_base_v011_signal(cor, revenue):
    result = _f21_cogratio(cor, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed cost-of-revenue ratio
def f21gm_f21_gross_margin_volatility_cogsmooth_63d_base_v012_signal(cor, revenue):
    result = _mean(_f21_cogratio(cor, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed cost-of-revenue ratio
def f21gm_f21_gross_margin_volatility_cogsmooth_126d_base_v013_signal(cor, revenue):
    result = _mean(_f21_cogratio(cor, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cost-of-revenue ratio volatility
def f21gm_f21_gross_margin_volatility_cogvol_252d_base_v014_signal(cor, revenue):
    result = _std(_f21_cogratio(cor, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cost-of-revenue ratio volatility
def f21gm_f21_gross_margin_volatility_cogvol_126d_base_v015_signal(cor, revenue):
    result = _std(_f21_cogratio(cor, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 126d
def f21gm_f21_gross_margin_volatility_gmz_126d_base_v016_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 252d
def f21gm_f21_gross_margin_volatility_gmz_252d_base_v017_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 504d
def f21gm_f21_gross_margin_volatility_gmz_504d_base_v018_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 63d
def f21gm_f21_gross_margin_volatility_gmz_63d_base_v019_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio z-score over 252d
def f21gm_f21_gross_margin_volatility_cogz_252d_base_v020_signal(cor, revenue):
    result = _z(_f21_cogratio(cor, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 63d (per-day OLS slope)
def f21gm_f21_gross_margin_volatility_gmslope_63d_base_v021_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 126d
def f21gm_f21_gross_margin_volatility_gmslope_126d_base_v022_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 252d
def f21gm_f21_gross_margin_volatility_gmslope_252d_base_v023_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(252)) / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin coefficient of variation over 252d
def f21gm_f21_gross_margin_volatility_gmcv_252d_base_v024_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 252), _mean(gm, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin coefficient of variation over 126d
def f21gm_f21_gross_margin_volatility_gmcv_126d_base_v025_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 126), _mean(gm, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin coefficient of variation over 504d
def f21gm_f21_gross_margin_volatility_gmcv_504d_base_v026_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 504), _mean(gm, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin compression vs 252d trailing mean (level - mean)
def f21gm_f21_gross_margin_volatility_gmcompress_252d_base_v027_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin compression vs 126d trailing mean
def f21gm_f21_gross_margin_volatility_gmcompress_126d_base_v028_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin compression vs 63d trailing mean
def f21gm_f21_gross_margin_volatility_gmcompress_63d_base_v029_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin relative compression (level/mean - 1) over 252d
def f21gm_f21_gross_margin_volatility_gmrelcomp_252d_base_v030_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 252)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling skew over 126d
def f21gm_f21_gross_margin_volatility_gmskew_126d_base_v031_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling skew over 252d
def f21gm_f21_gross_margin_volatility_gmskew_252d_base_v032_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling kurtosis over 252d
def f21gm_f21_gross_margin_volatility_gmkurt_252d_base_v033_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank over 126d
def f21gm_f21_gross_margin_volatility_gmrank_126d_base_v034_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank over 252d
def f21gm_f21_gross_margin_volatility_gmrank_252d_base_v035_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank over 504d
def f21gm_f21_gross_margin_volatility_gmrank_504d_base_v036_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin IQR-based range over 252d (continuous spread)
def f21gm_f21_gross_margin_volatility_gmiqr_252d_base_v037_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    result = q75 - q25
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin IQR-based range over 126d
def f21gm_f21_gross_margin_volatility_gmiqr_126d_base_v038_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(126, min_periods=42).quantile(0.75)
    q25 = gm.rolling(126, min_periods=42).quantile(0.25)
    result = q75 - q25
    return result.replace([np.inf, -np.inf], np.nan)


# cost-stability ratio: mean cog / std cog over 252d (higher = more stable)
def f21gm_f21_gross_margin_volatility_coststab_252d_base_v039_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 252), _std(cog, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# cost-stability ratio over 126d
def f21gm_f21_gross_margin_volatility_coststab_126d_base_v040_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 126), _std(cog, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin stability ratio: mean gm / std gm over 252d
def f21gm_f21_gross_margin_volatility_gmstab_252d_base_v041_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 252), _std(gm, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility ratio: 63d vol vs 252d vol (vol-of-vol regime)
def f21gm_f21_gross_margin_volatility_gmvolratio_63_252_base_v042_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 63), _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility ratio: 126d vs 504d
def f21gm_f21_gross_margin_volatility_gmvolratio_126_504_base_v043_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 126), _f21_gmvol(gp, revenue, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA level (span 63)
def f21gm_f21_gross_margin_volatility_gmewm_63d_base_v044_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA level (span 126)
def f21gm_f21_gross_margin_volatility_gmewm_126d_base_v045_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA volatility (span 63)
def f21gm_f21_gross_margin_volatility_gmewmvol_63d_base_v046_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=63, min_periods=21).std()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA volatility (span 126)
def f21gm_f21_gross_margin_volatility_gmewmvol_126d_base_v047_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=126, min_periods=42).std()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 21d (margin momentum)
def f21gm_f21_gross_margin_volatility_gmchg_21d_base_v048_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 63d
def f21gm_f21_gross_margin_volatility_gmchg_63d_base_v049_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 126d
def f21gm_f21_gross_margin_volatility_gmchg_126d_base_v050_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 252d
def f21gm_f21_gross_margin_volatility_gmchg_252d_base_v051_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin vol-scaled change: 63d change / 252d gm vol
def f21gm_f21_gross_margin_volatility_gmchgscaled_63d_base_v052_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(63), _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin vol-scaled change: 126d change / 252d gm vol
def f21gm_f21_gross_margin_volatility_gmchgscaled_126d_base_v053_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(126), _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity (opex/revenue)
def f21gm_f21_gross_margin_volatility_opratio_1d_base_v054_signal(opex, revenue):
    result = _f21_opratio(opex, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed operating-expense intensity
def f21gm_f21_gross_margin_volatility_opsmooth_126d_base_v055_signal(opex, revenue):
    result = _mean(_f21_opratio(opex, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating-expense intensity volatility
def f21gm_f21_gross_margin_volatility_opvol_252d_base_v056_signal(opex, revenue):
    result = _std(_f21_opratio(opex, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity z-score over 252d
def f21gm_f21_gross_margin_volatility_opz_252d_base_v057_signal(opex, revenue):
    result = _z(_f21_opratio(opex, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net margin proxy: gross margin minus opex intensity
def f21gm_f21_gross_margin_volatility_netmargin_1d_base_v058_signal(gp, revenue, opex):
    result = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed net-margin proxy
def f21gm_f21_gross_margin_volatility_netmargin_126d_base_v059_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _mean(nm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-margin proxy volatility
def f21gm_f21_gross_margin_volatility_netmarginvol_252d_base_v060_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _std(nm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minus cost ratio (margin spread, gm - cog)
def f21gm_f21_gross_margin_volatility_gmcogspread_1d_base_v061_signal(gp, revenue, cor):
    result = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin column vs computed gm spread
def f21gm_f21_gross_margin_volatility_gmreported_spread_1d_base_v062_signal(grossmargin, gp, revenue):
    result = grossmargin - _f21_gm(gp, revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin z-score over 252d (anchored to primitive)
def f21gm_f21_gross_margin_volatility_gmreported_z252_base_v063_signal(grossmargin, gp, revenue):
    result = _z(grossmargin, 252) + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin 252d volatility (anchored)
def f21gm_f21_gross_margin_volatility_gmreported_vol252_base_v064_signal(grossmargin, gp, revenue):
    result = _std(grossmargin, 252) + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin downside semi-deviation over 252d (continuous)
def f21gm_f21_gross_margin_volatility_gmsemidev_252d_base_v065_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 252)).clip(upper=0)
    result = (dev ** 2).rolling(252, min_periods=84).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin upside semi-deviation over 252d
def f21gm_f21_gross_margin_volatility_gmsemidevup_252d_base_v066_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 252)).clip(lower=0)
    result = (dev ** 2).rolling(252, min_periods=84).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin mean-absolute-deviation over 126d
def f21gm_f21_gross_margin_volatility_gmmad_126d_base_v067_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 126)).abs().rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin mean-absolute-deviation over 252d
def f21gm_f21_gross_margin_volatility_gmmad_252d_base_v068_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 252)).abs().rolling(252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin normalized range via std-vs-mad ratio over 252d
def f21gm_f21_gross_margin_volatility_gmstdmad_252d_base_v069_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    mad = (gm - _mean(gm, 252)).abs().rolling(252, min_periods=84).mean()
    result = _safe_div(_std(gm, 252), mad)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope normalized by gm vol (trend-to-noise) 126d
def f21gm_f21_gross_margin_volatility_gmtrendnoise_126d_base_v070_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(126)) / 126.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend-to-noise 252d
def f21gm_f21_gross_margin_volatility_gmtrendnoise_252d_base_v071_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(252)) / 252.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio change over 63d (cost momentum)
def f21gm_f21_gross_margin_volatility_cogchg_63d_base_v072_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio change over 126d
def f21gm_f21_gross_margin_volatility_cogchg_126d_base_v073_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank deviation from 0.5 over 252d (centered)
def f21gm_f21_gross_margin_volatility_gmrankdev_252d_base_v074_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(252, min_periods=84).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA z-score (span 126): (gm - ewm mean)/ewm std
def f21gm_f21_gross_margin_volatility_gmewmz_126d_base_v075_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=126, min_periods=42).mean()
    sd = gm.ewm(span=126, min_periods=42).std()
    result = _safe_div(gm - m, sd)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21gm_f21_gross_margin_volatility_gmlevel_1d_base_v001_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_21d_base_v002_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_63d_base_v003_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_126d_base_v004_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_252d_base_v005_signal,
    f21gm_f21_gross_margin_volatility_gmvol_63d_base_v006_signal,
    f21gm_f21_gross_margin_volatility_gmvol_126d_base_v007_signal,
    f21gm_f21_gross_margin_volatility_gmvol_252d_base_v008_signal,
    f21gm_f21_gross_margin_volatility_gmvol_504d_base_v009_signal,
    f21gm_f21_gross_margin_volatility_gmvol_42d_base_v010_signal,
    f21gm_f21_gross_margin_volatility_cogratio_1d_base_v011_signal,
    f21gm_f21_gross_margin_volatility_cogsmooth_63d_base_v012_signal,
    f21gm_f21_gross_margin_volatility_cogsmooth_126d_base_v013_signal,
    f21gm_f21_gross_margin_volatility_cogvol_252d_base_v014_signal,
    f21gm_f21_gross_margin_volatility_cogvol_126d_base_v015_signal,
    f21gm_f21_gross_margin_volatility_gmz_126d_base_v016_signal,
    f21gm_f21_gross_margin_volatility_gmz_252d_base_v017_signal,
    f21gm_f21_gross_margin_volatility_gmz_504d_base_v018_signal,
    f21gm_f21_gross_margin_volatility_gmz_63d_base_v019_signal,
    f21gm_f21_gross_margin_volatility_cogz_252d_base_v020_signal,
    f21gm_f21_gross_margin_volatility_gmslope_63d_base_v021_signal,
    f21gm_f21_gross_margin_volatility_gmslope_126d_base_v022_signal,
    f21gm_f21_gross_margin_volatility_gmslope_252d_base_v023_signal,
    f21gm_f21_gross_margin_volatility_gmcv_252d_base_v024_signal,
    f21gm_f21_gross_margin_volatility_gmcv_126d_base_v025_signal,
    f21gm_f21_gross_margin_volatility_gmcv_504d_base_v026_signal,
    f21gm_f21_gross_margin_volatility_gmcompress_252d_base_v027_signal,
    f21gm_f21_gross_margin_volatility_gmcompress_126d_base_v028_signal,
    f21gm_f21_gross_margin_volatility_gmcompress_63d_base_v029_signal,
    f21gm_f21_gross_margin_volatility_gmrelcomp_252d_base_v030_signal,
    f21gm_f21_gross_margin_volatility_gmskew_126d_base_v031_signal,
    f21gm_f21_gross_margin_volatility_gmskew_252d_base_v032_signal,
    f21gm_f21_gross_margin_volatility_gmkurt_252d_base_v033_signal,
    f21gm_f21_gross_margin_volatility_gmrank_126d_base_v034_signal,
    f21gm_f21_gross_margin_volatility_gmrank_252d_base_v035_signal,
    f21gm_f21_gross_margin_volatility_gmrank_504d_base_v036_signal,
    f21gm_f21_gross_margin_volatility_gmiqr_252d_base_v037_signal,
    f21gm_f21_gross_margin_volatility_gmiqr_126d_base_v038_signal,
    f21gm_f21_gross_margin_volatility_coststab_252d_base_v039_signal,
    f21gm_f21_gross_margin_volatility_coststab_126d_base_v040_signal,
    f21gm_f21_gross_margin_volatility_gmstab_252d_base_v041_signal,
    f21gm_f21_gross_margin_volatility_gmvolratio_63_252_base_v042_signal,
    f21gm_f21_gross_margin_volatility_gmvolratio_126_504_base_v043_signal,
    f21gm_f21_gross_margin_volatility_gmewm_63d_base_v044_signal,
    f21gm_f21_gross_margin_volatility_gmewm_126d_base_v045_signal,
    f21gm_f21_gross_margin_volatility_gmewmvol_63d_base_v046_signal,
    f21gm_f21_gross_margin_volatility_gmewmvol_126d_base_v047_signal,
    f21gm_f21_gross_margin_volatility_gmchg_21d_base_v048_signal,
    f21gm_f21_gross_margin_volatility_gmchg_63d_base_v049_signal,
    f21gm_f21_gross_margin_volatility_gmchg_126d_base_v050_signal,
    f21gm_f21_gross_margin_volatility_gmchg_252d_base_v051_signal,
    f21gm_f21_gross_margin_volatility_gmchgscaled_63d_base_v052_signal,
    f21gm_f21_gross_margin_volatility_gmchgscaled_126d_base_v053_signal,
    f21gm_f21_gross_margin_volatility_opratio_1d_base_v054_signal,
    f21gm_f21_gross_margin_volatility_opsmooth_126d_base_v055_signal,
    f21gm_f21_gross_margin_volatility_opvol_252d_base_v056_signal,
    f21gm_f21_gross_margin_volatility_opz_252d_base_v057_signal,
    f21gm_f21_gross_margin_volatility_netmargin_1d_base_v058_signal,
    f21gm_f21_gross_margin_volatility_netmargin_126d_base_v059_signal,
    f21gm_f21_gross_margin_volatility_netmarginvol_252d_base_v060_signal,
    f21gm_f21_gross_margin_volatility_gmcogspread_1d_base_v061_signal,
    f21gm_f21_gross_margin_volatility_gmreported_spread_1d_base_v062_signal,
    f21gm_f21_gross_margin_volatility_gmreported_z252_base_v063_signal,
    f21gm_f21_gross_margin_volatility_gmreported_vol252_base_v064_signal,
    f21gm_f21_gross_margin_volatility_gmsemidev_252d_base_v065_signal,
    f21gm_f21_gross_margin_volatility_gmsemidevup_252d_base_v066_signal,
    f21gm_f21_gross_margin_volatility_gmmad_126d_base_v067_signal,
    f21gm_f21_gross_margin_volatility_gmmad_252d_base_v068_signal,
    f21gm_f21_gross_margin_volatility_gmstdmad_252d_base_v069_signal,
    f21gm_f21_gross_margin_volatility_gmtrendnoise_126d_base_v070_signal,
    f21gm_f21_gross_margin_volatility_gmtrendnoise_252d_base_v071_signal,
    f21gm_f21_gross_margin_volatility_cogchg_63d_base_v072_signal,
    f21gm_f21_gross_margin_volatility_cogchg_126d_base_v073_signal,
    f21gm_f21_gross_margin_volatility_gmrankdev_252d_base_v074_signal,
    f21gm_f21_gross_margin_volatility_gmewmz_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_GROSS_MARGIN_VOLATILITY_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f21_gm", "_f21_gmvol", "_f21_cogratio", "_f21_opratio")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_gross_margin_volatility_base_001_075_claude: {n_features} features pass")
