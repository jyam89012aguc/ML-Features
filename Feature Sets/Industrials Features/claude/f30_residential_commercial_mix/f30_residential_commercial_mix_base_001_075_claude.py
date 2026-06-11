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


def f30rcm_residential_commercial_mix_mixp_5d_base_v001_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_10d_base_v002_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_21d_base_v003_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_42d_base_v004_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_63d_base_v005_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_126d_base_v006_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_189d_base_v007_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_252d_base_v008_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_378d_base_v009_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_504d_base_v010_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma21d_base_v011_signal(grossmargin, revenue, closeadj):
    result = (_mean(_f30_mix_proxy(grossmargin, revenue, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma63d_base_v012_signal(grossmargin, revenue, closeadj):
    result = (_mean(_f30_mix_proxy(grossmargin, revenue, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ma252d_base_v013_signal(grossmargin, revenue, closeadj):
    result = (_mean(_f30_mix_proxy(grossmargin, revenue, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_std63d_base_v014_signal(grossmargin, revenue, closeadj):
    result = (_std(_f30_mix_proxy(grossmargin, revenue, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_std252d_base_v015_signal(grossmargin, revenue, closeadj):
    result = (_std(_f30_mix_proxy(grossmargin, revenue, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_z63d_base_v016_signal(grossmargin, revenue, closeadj):
    result = (_z(_f30_mix_proxy(grossmargin, revenue, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_z252d_base_v017_signal(grossmargin, revenue, closeadj):
    result = (_z(_f30_mix_proxy(grossmargin, revenue, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema21d_base_v018_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema63d_base_v019_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_ema252d_base_v020_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_rank252d_base_v021_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_rank504d_base_v022_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_abs_base_v023_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_sq_base_v024_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_mix_proxy(grossmargin, revenue, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_dev252_base_v025_signal(grossmargin, revenue, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 252) - _mean(_f30_mix_proxy(grossmargin, revenue, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_var252_base_v026_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xlogpx_252_base_v027_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxgap_252_base_v028_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxdet_252_base_v029_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpkgap_252_base_v030_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xrange_252_base_v031_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xvolz_252_base_v032_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xpxchg_63_base_v033_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_diff63_base_v034_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_sign_base_v035_signal(grossmargin, revenue, closeadj):
    result = (np.sign(_f30_mix_proxy(grossmargin, revenue, 63)) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_zema252_base_v036_signal(grossmargin, revenue, closeadj):
    result = (_z(_f30_mix_proxy(grossmargin, revenue, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xlogrev_252_base_v037_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xstd_252_base_v038_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * _std(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_diff252_base_v039_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252).diff(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_xrevg_252_base_v040_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * revenue.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_5d_base_v041_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_10d_base_v042_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_21d_base_v043_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_42d_base_v044_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_63d_base_v045_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_126d_base_v046_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_189d_base_v047_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_252d_base_v048_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_378d_base_v049_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_504d_base_v050_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma21d_base_v051_signal(revenue, ebitda, closeadj):
    result = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma63d_base_v052_signal(revenue, ebitda, closeadj):
    result = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ma252d_base_v053_signal(revenue, ebitda, closeadj):
    result = (_mean(_f30_segment_growth_divergence(revenue, ebitda, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_std63d_base_v054_signal(revenue, ebitda, closeadj):
    result = (_std(_f30_segment_growth_divergence(revenue, ebitda, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_std252d_base_v055_signal(revenue, ebitda, closeadj):
    result = (_std(_f30_segment_growth_divergence(revenue, ebitda, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_z63d_base_v056_signal(revenue, ebitda, closeadj):
    result = (_z(_f30_segment_growth_divergence(revenue, ebitda, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_z252d_base_v057_signal(revenue, ebitda, closeadj):
    result = (_z(_f30_segment_growth_divergence(revenue, ebitda, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema21d_base_v058_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema63d_base_v059_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_ema252d_base_v060_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_rank252d_base_v061_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_rank504d_base_v062_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_abs_base_v063_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_sq_base_v064_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_dev252_base_v065_signal(revenue, ebitda, closeadj):
    result = ((_f30_segment_growth_divergence(revenue, ebitda, 252) - _mean(_f30_segment_growth_divergence(revenue, ebitda, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_var252_base_v066_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogpx_252_base_v067_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxgap_252_base_v068_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxdet_252_base_v069_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpkgap_252_base_v070_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xrange_252_base_v071_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xvolz_252_base_v072_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xpxchg_63_base_v073_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_diff63_base_v074_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_sign_base_v075_signal(revenue, ebitda, closeadj):
    result = (np.sign(_f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rcm_residential_commercial_mix_mixp_5d_base_v001_signal,
    f30rcm_residential_commercial_mix_mixp_10d_base_v002_signal,
    f30rcm_residential_commercial_mix_mixp_21d_base_v003_signal,
    f30rcm_residential_commercial_mix_mixp_42d_base_v004_signal,
    f30rcm_residential_commercial_mix_mixp_63d_base_v005_signal,
    f30rcm_residential_commercial_mix_mixp_126d_base_v006_signal,
    f30rcm_residential_commercial_mix_mixp_189d_base_v007_signal,
    f30rcm_residential_commercial_mix_mixp_252d_base_v008_signal,
    f30rcm_residential_commercial_mix_mixp_378d_base_v009_signal,
    f30rcm_residential_commercial_mix_mixp_504d_base_v010_signal,
    f30rcm_residential_commercial_mix_mixp_ma21d_base_v011_signal,
    f30rcm_residential_commercial_mix_mixp_ma63d_base_v012_signal,
    f30rcm_residential_commercial_mix_mixp_ma252d_base_v013_signal,
    f30rcm_residential_commercial_mix_mixp_std63d_base_v014_signal,
    f30rcm_residential_commercial_mix_mixp_std252d_base_v015_signal,
    f30rcm_residential_commercial_mix_mixp_z63d_base_v016_signal,
    f30rcm_residential_commercial_mix_mixp_z252d_base_v017_signal,
    f30rcm_residential_commercial_mix_mixp_ema21d_base_v018_signal,
    f30rcm_residential_commercial_mix_mixp_ema63d_base_v019_signal,
    f30rcm_residential_commercial_mix_mixp_ema252d_base_v020_signal,
    f30rcm_residential_commercial_mix_mixp_rank252d_base_v021_signal,
    f30rcm_residential_commercial_mix_mixp_rank504d_base_v022_signal,
    f30rcm_residential_commercial_mix_mixp_abs_base_v023_signal,
    f30rcm_residential_commercial_mix_mixp_sq_base_v024_signal,
    f30rcm_residential_commercial_mix_mixp_dev252_base_v025_signal,
    f30rcm_residential_commercial_mix_mixp_var252_base_v026_signal,
    f30rcm_residential_commercial_mix_mixp_xlogpx_252_base_v027_signal,
    f30rcm_residential_commercial_mix_mixp_xpxgap_252_base_v028_signal,
    f30rcm_residential_commercial_mix_mixp_xpxdet_252_base_v029_signal,
    f30rcm_residential_commercial_mix_mixp_xpkgap_252_base_v030_signal,
    f30rcm_residential_commercial_mix_mixp_xrange_252_base_v031_signal,
    f30rcm_residential_commercial_mix_mixp_xvolz_252_base_v032_signal,
    f30rcm_residential_commercial_mix_mixp_xpxchg_63_base_v033_signal,
    f30rcm_residential_commercial_mix_mixp_diff63_base_v034_signal,
    f30rcm_residential_commercial_mix_mixp_sign_base_v035_signal,
    f30rcm_residential_commercial_mix_mixp_zema252_base_v036_signal,
    f30rcm_residential_commercial_mix_mixp_xlogrev_252_base_v037_signal,
    f30rcm_residential_commercial_mix_mixp_xstd_252_base_v038_signal,
    f30rcm_residential_commercial_mix_mixp_diff252_base_v039_signal,
    f30rcm_residential_commercial_mix_mixp_xrevg_252_base_v040_signal,
    f30rcm_residential_commercial_mix_segdiv_5d_base_v041_signal,
    f30rcm_residential_commercial_mix_segdiv_10d_base_v042_signal,
    f30rcm_residential_commercial_mix_segdiv_21d_base_v043_signal,
    f30rcm_residential_commercial_mix_segdiv_42d_base_v044_signal,
    f30rcm_residential_commercial_mix_segdiv_63d_base_v045_signal,
    f30rcm_residential_commercial_mix_segdiv_126d_base_v046_signal,
    f30rcm_residential_commercial_mix_segdiv_189d_base_v047_signal,
    f30rcm_residential_commercial_mix_segdiv_252d_base_v048_signal,
    f30rcm_residential_commercial_mix_segdiv_378d_base_v049_signal,
    f30rcm_residential_commercial_mix_segdiv_504d_base_v050_signal,
    f30rcm_residential_commercial_mix_segdiv_ma21d_base_v051_signal,
    f30rcm_residential_commercial_mix_segdiv_ma63d_base_v052_signal,
    f30rcm_residential_commercial_mix_segdiv_ma252d_base_v053_signal,
    f30rcm_residential_commercial_mix_segdiv_std63d_base_v054_signal,
    f30rcm_residential_commercial_mix_segdiv_std252d_base_v055_signal,
    f30rcm_residential_commercial_mix_segdiv_z63d_base_v056_signal,
    f30rcm_residential_commercial_mix_segdiv_z252d_base_v057_signal,
    f30rcm_residential_commercial_mix_segdiv_ema21d_base_v058_signal,
    f30rcm_residential_commercial_mix_segdiv_ema63d_base_v059_signal,
    f30rcm_residential_commercial_mix_segdiv_ema252d_base_v060_signal,
    f30rcm_residential_commercial_mix_segdiv_rank252d_base_v061_signal,
    f30rcm_residential_commercial_mix_segdiv_rank504d_base_v062_signal,
    f30rcm_residential_commercial_mix_segdiv_abs_base_v063_signal,
    f30rcm_residential_commercial_mix_segdiv_sq_base_v064_signal,
    f30rcm_residential_commercial_mix_segdiv_dev252_base_v065_signal,
    f30rcm_residential_commercial_mix_segdiv_var252_base_v066_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogpx_252_base_v067_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxgap_252_base_v068_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxdet_252_base_v069_signal,
    f30rcm_residential_commercial_mix_segdiv_xpkgap_252_base_v070_signal,
    f30rcm_residential_commercial_mix_segdiv_xrange_252_base_v071_signal,
    f30rcm_residential_commercial_mix_segdiv_xvolz_252_base_v072_signal,
    f30rcm_residential_commercial_mix_segdiv_xpxchg_63_base_v073_signal,
    f30rcm_residential_commercial_mix_segdiv_diff63_base_v074_signal,
    f30rcm_residential_commercial_mix_segdiv_sign_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESIDENTIAL_COMMERCIAL_MIX_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f30_residential_commercial_mix_base_001_075_claude: {n_features} features pass")
