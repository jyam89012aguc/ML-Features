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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f30_mix_proxy(grossmargin, revenue, w):
    # Mix proxy: gross margin × revenue growth (high-margin commercial vs low-margin residential)
    return grossmargin * revenue.pct_change(periods=w)


def _f30_segment_growth_divergence(revenue, ebitda, w):
    # Divergence between revenue growth and ebitda growth — segment mix shift indicator
    return revenue.pct_change(periods=w) - ebitda.pct_change(periods=w)


def _f30_mix_quality(grossmargin, ebitdamargin, w):
    # Mix quality: gross margin minus its trailing mean × ebitda margin
    gm_dev = grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return gm_dev * ebitdamargin


def f30rcm_residential_commercial_mix_mixp_5d_jerk_v001_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 5)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_10d_jerk_v002_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 10)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_21d_jerk_v003_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_42d_jerk_v004_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 42)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_63d_jerk_v005_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_126d_jerk_v006_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 126)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_189d_jerk_v007_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 189)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_252d_jerk_v008_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_378d_jerk_v009_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 378)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_504d_jerk_v010_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma21d_jerk_v011_signal(grossmargin, revenue, closeadj):
    base = (_mean(_f30_mix_proxy(grossmargin, revenue, 21), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma63d_jerk_v012_signal(grossmargin, revenue, closeadj):
    base = (_mean(_f30_mix_proxy(grossmargin, revenue, 63), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma252d_jerk_v013_signal(grossmargin, revenue, closeadj):
    base = (_mean(_f30_mix_proxy(grossmargin, revenue, 252), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_std63d_jerk_v014_signal(grossmargin, revenue, closeadj):
    base = (_std(_f30_mix_proxy(grossmargin, revenue, 63), 63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_std252d_jerk_v015_signal(grossmargin, revenue, closeadj):
    base = (_std(_f30_mix_proxy(grossmargin, revenue, 252), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_z63d_jerk_v016_signal(grossmargin, revenue, closeadj):
    base = (_z(_f30_mix_proxy(grossmargin, revenue, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_z252d_jerk_v017_signal(grossmargin, revenue, closeadj):
    base = (_z(_f30_mix_proxy(grossmargin, revenue, 252), 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema21d_jerk_v018_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 21).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema63d_jerk_v019_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema252d_jerk_v020_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252).ewm(span=252, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_rank252d_jerk_v021_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_rank504d_jerk_v022_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_abs_jerk_v023_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_sq_jerk_v024_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_mix_proxy(grossmargin, revenue, 63).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_dev252_jerk_v025_signal(grossmargin, revenue, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 252) - _mean(_f30_mix_proxy(grossmargin, revenue, 252), 252))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_var252_jerk_v026_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xlogpx_252_jerk_v027_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxgap_252_jerk_v028_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxdet_252_jerk_v029_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpkgap_252_jerk_v030_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xrange_252_jerk_v031_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xvolz_252_jerk_v032_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxchg_63_jerk_v033_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_diff63_jerk_v034_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63).diff(21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_sign_jerk_v035_signal(grossmargin, revenue, closeadj):
    base = (np.sign(_f30_mix_proxy(grossmargin, revenue, 63)) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_zema252_jerk_v036_signal(grossmargin, revenue, closeadj):
    base = (_z(_f30_mix_proxy(grossmargin, revenue, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xlogrev_252_jerk_v037_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xstd_252_jerk_v038_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_diff252_jerk_v039_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252).diff(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xrevg_252_jerk_v040_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_5d_jerk_v041_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 5)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_10d_jerk_v042_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 10)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_21d_jerk_v043_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_42d_jerk_v044_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 42)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_63d_jerk_v045_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_126d_jerk_v046_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 126)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_189d_jerk_v047_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 189)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_252d_jerk_v048_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_378d_jerk_v049_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 378)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_504d_jerk_v050_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma21d_jerk_v051_signal(revenue, ebitda, closeadj):
    base = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 21), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma63d_jerk_v052_signal(revenue, ebitda, closeadj):
    base = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 63), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma252d_jerk_v053_signal(revenue, ebitda, closeadj):
    base = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 252), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_std63d_jerk_v054_signal(revenue, ebitda, closeadj):
    base = (_std(_f30_segment_growth_divergence(revenue, ebitda, 63), 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_std252d_jerk_v055_signal(revenue, ebitda, closeadj):
    base = (_std(_f30_segment_growth_divergence(revenue, ebitda, 252), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_z63d_jerk_v056_signal(revenue, ebitda, closeadj):
    base = (_z(_f30_segment_growth_divergence(revenue, ebitda, 63), 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_z252d_jerk_v057_signal(revenue, ebitda, closeadj):
    base = (_z(_f30_segment_growth_divergence(revenue, ebitda, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema21d_jerk_v058_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 21).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema63d_jerk_v059_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema252d_jerk_v060_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252).ewm(span=252, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_rank252d_jerk_v061_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_rank504d_jerk_v062_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_abs_jerk_v063_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63).abs()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_sq_jerk_v064_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_dev252_jerk_v065_signal(revenue, ebitda, closeadj):
    base = ((_f30_segment_growth_divergence(revenue, ebitda, 252) - _mean(_f30_segment_growth_divergence(revenue, ebitda, 252), 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_var252_jerk_v066_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogpx_252_jerk_v067_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxgap_252_jerk_v068_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxdet_252_jerk_v069_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpkgap_252_jerk_v070_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xrange_252_jerk_v071_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xvolz_252_jerk_v072_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxchg_63_jerk_v073_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_diff63_jerk_v074_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 63).diff(21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_sign_jerk_v075_signal(revenue, ebitda, closeadj):
    base = (np.sign(_f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_zema252_jerk_v076_signal(revenue, ebitda, closeadj):
    base = (_z(_f30_segment_growth_divergence(revenue, ebitda, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogrev_252_jerk_v077_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogebitda_252_jerk_v078_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(ebitda.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xstd_252_jerk_v079_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xebitda_growth_jerk_v080_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ebitda.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_5d_jerk_v081_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 5)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_10d_jerk_v082_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 10)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_21d_jerk_v083_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_42d_jerk_v084_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 42)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_63d_jerk_v085_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_126d_jerk_v086_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 126)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_189d_jerk_v087_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 189)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_252d_jerk_v088_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_378d_jerk_v089_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 378)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_504d_jerk_v090_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma21d_jerk_v091_signal(grossmargin, ebitdamargin, closeadj):
    base = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 21), 21)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma63d_jerk_v092_signal(grossmargin, ebitdamargin, closeadj):
    base = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 63), 21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma252d_jerk_v093_signal(grossmargin, ebitdamargin, closeadj):
    base = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 252), 21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_std63d_jerk_v094_signal(grossmargin, ebitdamargin, closeadj):
    base = (_std(_f30_mix_quality(grossmargin, ebitdamargin, 63), 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_std252d_jerk_v095_signal(grossmargin, ebitdamargin, closeadj):
    base = (_std(_f30_mix_quality(grossmargin, ebitdamargin, 252), 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_z63d_jerk_v096_signal(grossmargin, ebitdamargin, closeadj):
    base = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 63), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_z252d_jerk_v097_signal(grossmargin, ebitdamargin, closeadj):
    base = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 252), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema21d_jerk_v098_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 21).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema63d_jerk_v099_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema252d_jerk_v100_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252).ewm(span=252, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_rank252d_jerk_v101_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_rank504d_jerk_v102_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_abs_jerk_v103_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63).abs()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_sq_jerk_v104_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * _f30_mix_quality(grossmargin, ebitdamargin, 63).abs()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_dev252_jerk_v105_signal(grossmargin, ebitdamargin, closeadj):
    base = ((_f30_mix_quality(grossmargin, ebitdamargin, 252) - _mean(_f30_mix_quality(grossmargin, ebitdamargin, 252), 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_var252_jerk_v106_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xlogpx_252_jerk_v107_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxgap_252_jerk_v108_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxdet_252_jerk_v109_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpkgap_252_jerk_v110_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xrange_252_jerk_v111_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xvolz_252_jerk_v112_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * _z(closeadj, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxchg_63_jerk_v113_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_diff63_jerk_v114_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63).diff(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_sign_jerk_v115_signal(grossmargin, ebitdamargin, closeadj):
    base = (np.sign(_f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj.pct_change(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_zema252_jerk_v116_signal(grossmargin, ebitdamargin, closeadj):
    base = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xgrossmargin_jerk_v117_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * grossmargin) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xebitdamargin_jerk_v118_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ebitdamargin) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xstd_252_jerk_v119_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * _std(closeadj, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_gmdiff_252_jerk_v120_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * grossmargin.diff(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_63_jerk_v121_signal(grossmargin, revenue, ebitda, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_252_jerk_v122_signal(grossmargin, revenue, ebitda, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * _f30_segment_growth_divergence(revenue, ebitda, 252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_mixq_63_jerk_v123_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_mixq_252_jerk_v124_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _f30_mix_quality(grossmargin, ebitdamargin, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_plus_mixq_63_jerk_v125_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 63) + _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_252_jerk_v126_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 252) + _f30_segment_growth_divergence(revenue, ebitda, 252) + _f30_mix_quality(grossmargin, ebitdamargin, 252))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compow_all_252_jerk_v127_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((0.5 * _f30_mix_proxy(grossmargin, revenue, 252) + 0.3 * _f30_segment_growth_divergence(revenue, ebitda, 252) + 0.2 * _f30_mix_quality(grossmargin, ebitdamargin, 252))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_63_jerk_v128_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 63) + _f30_segment_growth_divergence(revenue, ebitda, 63) + _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_minus_segdiv_63_jerk_v129_signal(grossmargin, revenue, ebitda, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 63) - _f30_segment_growth_divergence(revenue, ebitda, 63))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_minus_segdiv_252_jerk_v130_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((_f30_mix_quality(grossmargin, ebitdamargin, 252) - _f30_segment_growth_divergence(revenue, ebitda, 252))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_x_close_jerk_v131_signal(grossmargin, revenue, ebitda, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(21)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_segdiv_x_close_jerk_v132_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compow3_63_jerk_v133_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((0.4 * _f30_mix_proxy(grossmargin, revenue, 63) + 0.3 * _f30_segment_growth_divergence(revenue, ebitda, 63) + 0.3 * _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_gp_jerk_v134_signal(grossmargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * grossmargin) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_revg_252_jerk_v135_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_revg_252_jerk_v136_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * revenue.pct_change(252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_ebitda_growth_jerk_v137_signal(grossmargin, revenue, ebitda, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 252) * ebitda.pct_change(252)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_emargdiff_252_jerk_v138_signal(revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ebitda.diff(252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_emarg_252_jerk_v139_signal(grossmargin, ebitdamargin, closeadj):
    base = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ebitdamargin.diff(252) * 100.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_logema_63_jerk_v140_signal(grossmargin, revenue, closeadj):
    base = (np.log(_f30_mix_proxy(grossmargin, revenue, 63).abs() + 1e-6).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_logema_252_jerk_v141_signal(grossmargin, revenue, closeadj):
    base = (np.log(_f30_mix_proxy(grossmargin, revenue, 252).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_logema_63_jerk_v142_signal(revenue, ebitda, closeadj):
    base = (np.log(_f30_segment_growth_divergence(revenue, ebitda, 63).abs() + 1e-6).ewm(span=21, adjust=False).mean()) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_logema_252_jerk_v143_signal(grossmargin, ebitdamargin, closeadj):
    base = (np.log(_f30_mix_quality(grossmargin, ebitdamargin, 252).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_504_jerk_v144_signal(grossmargin, revenue, ebitda, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 504) * _f30_segment_growth_divergence(revenue, ebitda, 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_mixq_504_jerk_v145_signal(grossmargin, ebitdamargin, revenue, closeadj):
    base = (_f30_mix_proxy(grossmargin, revenue, 504) * _f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_mixq_504_jerk_v146_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = (_f30_segment_growth_divergence(revenue, ebitda, 504) * _f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_emadiff_63_jerk_v147_signal(grossmargin, revenue, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 63).ewm(span=21, adjust=False).mean() - _f30_mix_proxy(grossmargin, revenue, 63).ewm(span=63, adjust=False).mean())) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_emadiff_63_jerk_v148_signal(revenue, ebitda, closeadj):
    base = ((_f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=21, adjust=False).mean() - _f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=63, adjust=False).mean())) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_emadiff_63_jerk_v149_signal(grossmargin, ebitdamargin, closeadj):
    base = ((_f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=21, adjust=False).mean() - _f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=63, adjust=False).mean())) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_504_jerk_v150_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    base = ((_f30_mix_proxy(grossmargin, revenue, 504) + _f30_segment_growth_divergence(revenue, ebitda, 504) + _f30_mix_quality(grossmargin, ebitdamargin, 504))) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rcm_residential_commercial_mix_mixp_5d_jerk_v001_signal,
    f30rcm_residential_commercial_mix_mixp_10d_jerk_v002_signal,
    f30rcm_residential_commercial_mix_mixp_21d_jerk_v003_signal,
    f30rcm_residential_commercial_mix_mixp_42d_jerk_v004_signal,
    f30rcm_residential_commercial_mix_mixp_63d_jerk_v005_signal,
    f30rcm_residential_commercial_mix_mixp_126d_jerk_v006_signal,
    f30rcm_residential_commercial_mix_mixp_189d_jerk_v007_signal,
    f30rcm_residential_commercial_mix_mixp_252d_jerk_v008_signal,
    f30rcm_residential_commercial_mix_mixp_378d_jerk_v009_signal,
    f30rcm_residential_commercial_mix_mixp_504d_jerk_v010_signal,
    f30rcm_residential_commercial_mix_mixp_ma21d_jerk_v011_signal,
    f30rcm_residential_commercial_mix_mixp_ma63d_jerk_v012_signal,
    f30rcm_residential_commercial_mix_mixp_ma252d_jerk_v013_signal,
    f30rcm_residential_commercial_mix_mixp_std63d_jerk_v014_signal,
    f30rcm_residential_commercial_mix_mixp_std252d_jerk_v015_signal,
    f30rcm_residential_commercial_mix_mixp_z63d_jerk_v016_signal,
    f30rcm_residential_commercial_mix_mixp_z252d_jerk_v017_signal,
    f30rcm_residential_commercial_mix_mixp_ema21d_jerk_v018_signal,
    f30rcm_residential_commercial_mix_mixp_ema63d_jerk_v019_signal,
    f30rcm_residential_commercial_mix_mixp_ema252d_jerk_v020_signal,
    f30rcm_residential_commercial_mix_mixp_rank252d_jerk_v021_signal,
    f30rcm_residential_commercial_mix_mixp_rank504d_jerk_v022_signal,
    f30rcm_residential_commercial_mix_mixp_abs_jerk_v023_signal,
    f30rcm_residential_commercial_mix_mixp_sq_jerk_v024_signal,
    f30rcm_residential_commercial_mix_mixp_dev252_jerk_v025_signal,
    f30rcm_residential_commercial_mix_mixp_var252_jerk_v026_signal,
    f30rcm_residential_commercial_mix_mixp_xlogpx_252_jerk_v027_signal,
    f30rcm_residential_commercial_mix_mixp_xpxgap_252_jerk_v028_signal,
    f30rcm_residential_commercial_mix_mixp_xpxdet_252_jerk_v029_signal,
    f30rcm_residential_commercial_mix_mixp_xpkgap_252_jerk_v030_signal,
    f30rcm_residential_commercial_mix_mixp_xrange_252_jerk_v031_signal,
    f30rcm_residential_commercial_mix_mixp_xvolz_252_jerk_v032_signal,
    f30rcm_residential_commercial_mix_mixp_xpxchg_63_jerk_v033_signal,
    f30rcm_residential_commercial_mix_mixp_diff63_jerk_v034_signal,
    f30rcm_residential_commercial_mix_mixp_sign_jerk_v035_signal,
    f30rcm_residential_commercial_mix_mixp_zema252_jerk_v036_signal,
    f30rcm_residential_commercial_mix_mixp_xlogrev_252_jerk_v037_signal,
    f30rcm_residential_commercial_mix_mixp_xstd_252_jerk_v038_signal,
    f30rcm_residential_commercial_mix_mixp_diff252_jerk_v039_signal,
    f30rcm_residential_commercial_mix_mixp_xrevg_252_jerk_v040_signal,
    f30rcm_residential_commercial_mix_segdiv_5d_jerk_v041_signal,
    f30rcm_residential_commercial_mix_segdiv_10d_jerk_v042_signal,
    f30rcm_residential_commercial_mix_segdiv_21d_jerk_v043_signal,
    f30rcm_residential_commercial_mix_segdiv_42d_jerk_v044_signal,
    f30rcm_residential_commercial_mix_segdiv_63d_jerk_v045_signal,
    f30rcm_residential_commercial_mix_segdiv_126d_jerk_v046_signal,
    f30rcm_residential_commercial_mix_segdiv_189d_jerk_v047_signal,
    f30rcm_residential_commercial_mix_segdiv_252d_jerk_v048_signal,
    f30rcm_residential_commercial_mix_segdiv_378d_jerk_v049_signal,
    f30rcm_residential_commercial_mix_segdiv_504d_jerk_v050_signal,
    f30rcm_residential_commercial_mix_segdiv_ma21d_jerk_v051_signal,
    f30rcm_residential_commercial_mix_segdiv_ma63d_jerk_v052_signal,
    f30rcm_residential_commercial_mix_segdiv_ma252d_jerk_v053_signal,
    f30rcm_residential_commercial_mix_segdiv_std63d_jerk_v054_signal,
    f30rcm_residential_commercial_mix_segdiv_std252d_jerk_v055_signal,
    f30rcm_residential_commercial_mix_segdiv_z63d_jerk_v056_signal,
    f30rcm_residential_commercial_mix_segdiv_z252d_jerk_v057_signal,
    f30rcm_residential_commercial_mix_segdiv_ema21d_jerk_v058_signal,
    f30rcm_residential_commercial_mix_segdiv_ema63d_jerk_v059_signal,
    f30rcm_residential_commercial_mix_segdiv_ema252d_jerk_v060_signal,
    f30rcm_residential_commercial_mix_segdiv_rank252d_jerk_v061_signal,
    f30rcm_residential_commercial_mix_segdiv_rank504d_jerk_v062_signal,
    f30rcm_residential_commercial_mix_segdiv_abs_jerk_v063_signal,
    f30rcm_residential_commercial_mix_segdiv_sq_jerk_v064_signal,
    f30rcm_residential_commercial_mix_segdiv_dev252_jerk_v065_signal,
    f30rcm_residential_commercial_mix_segdiv_var252_jerk_v066_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogpx_252_jerk_v067_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxgap_252_jerk_v068_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxdet_252_jerk_v069_signal,
    f30rcm_residential_commercial_mix_segdiv_xpkgap_252_jerk_v070_signal,
    f30rcm_residential_commercial_mix_segdiv_xrange_252_jerk_v071_signal,
    f30rcm_residential_commercial_mix_segdiv_xvolz_252_jerk_v072_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxchg_63_jerk_v073_signal,
    f30rcm_residential_commercial_mix_segdiv_diff63_jerk_v074_signal,
    f30rcm_residential_commercial_mix_segdiv_sign_jerk_v075_signal,
    f30rcm_residential_commercial_mix_segdiv_zema252_jerk_v076_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogrev_252_jerk_v077_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogebitda_252_jerk_v078_signal,
    f30rcm_residential_commercial_mix_segdiv_xstd_252_jerk_v079_signal,
    f30rcm_residential_commercial_mix_segdiv_xebitda_growth_jerk_v080_signal,
    f30rcm_residential_commercial_mix_mixq_5d_jerk_v081_signal,
    f30rcm_residential_commercial_mix_mixq_10d_jerk_v082_signal,
    f30rcm_residential_commercial_mix_mixq_21d_jerk_v083_signal,
    f30rcm_residential_commercial_mix_mixq_42d_jerk_v084_signal,
    f30rcm_residential_commercial_mix_mixq_63d_jerk_v085_signal,
    f30rcm_residential_commercial_mix_mixq_126d_jerk_v086_signal,
    f30rcm_residential_commercial_mix_mixq_189d_jerk_v087_signal,
    f30rcm_residential_commercial_mix_mixq_252d_jerk_v088_signal,
    f30rcm_residential_commercial_mix_mixq_378d_jerk_v089_signal,
    f30rcm_residential_commercial_mix_mixq_504d_jerk_v090_signal,
    f30rcm_residential_commercial_mix_mixq_ma21d_jerk_v091_signal,
    f30rcm_residential_commercial_mix_mixq_ma63d_jerk_v092_signal,
    f30rcm_residential_commercial_mix_mixq_ma252d_jerk_v093_signal,
    f30rcm_residential_commercial_mix_mixq_std63d_jerk_v094_signal,
    f30rcm_residential_commercial_mix_mixq_std252d_jerk_v095_signal,
    f30rcm_residential_commercial_mix_mixq_z63d_jerk_v096_signal,
    f30rcm_residential_commercial_mix_mixq_z252d_jerk_v097_signal,
    f30rcm_residential_commercial_mix_mixq_ema21d_jerk_v098_signal,
    f30rcm_residential_commercial_mix_mixq_ema63d_jerk_v099_signal,
    f30rcm_residential_commercial_mix_mixq_ema252d_jerk_v100_signal,
    f30rcm_residential_commercial_mix_mixq_rank252d_jerk_v101_signal,
    f30rcm_residential_commercial_mix_mixq_rank504d_jerk_v102_signal,
    f30rcm_residential_commercial_mix_mixq_abs_jerk_v103_signal,
    f30rcm_residential_commercial_mix_mixq_sq_jerk_v104_signal,
    f30rcm_residential_commercial_mix_mixq_dev252_jerk_v105_signal,
    f30rcm_residential_commercial_mix_mixq_var252_jerk_v106_signal,
    f30rcm_residential_commercial_mix_mixq_xlogpx_252_jerk_v107_signal,
    f30rcm_residential_commercial_mix_mixq_xpxgap_252_jerk_v108_signal,
    f30rcm_residential_commercial_mix_mixq_xpxdet_252_jerk_v109_signal,
    f30rcm_residential_commercial_mix_mixq_xpkgap_252_jerk_v110_signal,
    f30rcm_residential_commercial_mix_mixq_xrange_252_jerk_v111_signal,
    f30rcm_residential_commercial_mix_mixq_xvolz_252_jerk_v112_signal,
    f30rcm_residential_commercial_mix_mixq_xpxchg_63_jerk_v113_signal,
    f30rcm_residential_commercial_mix_mixq_diff63_jerk_v114_signal,
    f30rcm_residential_commercial_mix_mixq_sign_jerk_v115_signal,
    f30rcm_residential_commercial_mix_mixq_zema252_jerk_v116_signal,
    f30rcm_residential_commercial_mix_mixq_xgrossmargin_jerk_v117_signal,
    f30rcm_residential_commercial_mix_mixq_xebitdamargin_jerk_v118_signal,
    f30rcm_residential_commercial_mix_mixq_xstd_252_jerk_v119_signal,
    f30rcm_residential_commercial_mix_mixq_x_gmdiff_252_jerk_v120_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_63_jerk_v121_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_252_jerk_v122_signal,
    f30rcm_residential_commercial_mix_mixp_x_mixq_63_jerk_v123_signal,
    f30rcm_residential_commercial_mix_segdiv_x_mixq_252_jerk_v124_signal,
    f30rcm_residential_commercial_mix_mixp_plus_mixq_63_jerk_v125_signal,
    f30rcm_residential_commercial_mix_compo_all_252_jerk_v126_signal,
    f30rcm_residential_commercial_mix_compow_all_252_jerk_v127_signal,
    f30rcm_residential_commercial_mix_compo_all_63_jerk_v128_signal,
    f30rcm_residential_commercial_mix_mixp_minus_segdiv_63_jerk_v129_signal,
    f30rcm_residential_commercial_mix_mixq_minus_segdiv_252_jerk_v130_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_x_close_jerk_v131_signal,
    f30rcm_residential_commercial_mix_mixq_x_segdiv_x_close_jerk_v132_signal,
    f30rcm_residential_commercial_mix_compow3_63_jerk_v133_signal,
    f30rcm_residential_commercial_mix_mixp_x_gp_jerk_v134_signal,
    f30rcm_residential_commercial_mix_segdiv_x_revg_252_jerk_v135_signal,
    f30rcm_residential_commercial_mix_mixq_x_revg_252_jerk_v136_signal,
    f30rcm_residential_commercial_mix_mixp_x_ebitda_growth_jerk_v137_signal,
    f30rcm_residential_commercial_mix_segdiv_x_emargdiff_252_jerk_v138_signal,
    f30rcm_residential_commercial_mix_mixq_x_emarg_252_jerk_v139_signal,
    f30rcm_residential_commercial_mix_mixp_logema_63_jerk_v140_signal,
    f30rcm_residential_commercial_mix_mixp_logema_252_jerk_v141_signal,
    f30rcm_residential_commercial_mix_segdiv_logema_63_jerk_v142_signal,
    f30rcm_residential_commercial_mix_mixq_logema_252_jerk_v143_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_504_jerk_v144_signal,
    f30rcm_residential_commercial_mix_mixp_x_mixq_504_jerk_v145_signal,
    f30rcm_residential_commercial_mix_segdiv_x_mixq_504_jerk_v146_signal,
    f30rcm_residential_commercial_mix_mixp_emadiff_63_jerk_v147_signal,
    f30rcm_residential_commercial_mix_segdiv_emadiff_63_jerk_v148_signal,
    f30rcm_residential_commercial_mix_mixq_emadiff_63_jerk_v149_signal,
    f30rcm_residential_commercial_mix_compo_all_504_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESIDENTIAL_COMMERCIAL_MIX_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_mix_proxy", "_f30_segment_growth_divergence", "_f30_mix_quality")
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
    print(f"OK f30_residential_commercial_mix_3rd_derivatives_001_150_claude: {n_features} features pass")
