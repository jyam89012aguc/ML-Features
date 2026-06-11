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
def _f34_revenue_compound(revenue, w):
    return np.log(revenue.replace(0, np.nan).abs()).diff(w)


def _f34_multi_horizon_growth(revenue, w):
    g_short = revenue.pct_change(w)
    g_long = revenue.pct_change(w * 2)
    return _mean(g_short, w) + _mean(g_long, w) * 0.5


def _f34_international_proxy(revenue, ebitdamargin, w):
    rg = revenue.pct_change(w)
    return _mean(rg * (1.0 + ebitdamargin), w)


# ---- features ----

def f34hig_f34_healthcare_international_growth_compound_21d_base_v001_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_63d_base_v002_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_126d_base_v003_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_252d_base_v004_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_504d_base_v005_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_5d_base_v006_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_10d_base_v007_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_42d_base_v008_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_189d_base_v009_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compound_378d_base_v010_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundmean_63d_base_v011_signal(revenue, closeadj):
    result = _mean(_f34_revenue_compound(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundmean_252d_base_v012_signal(revenue, closeadj):
    result = _mean(_f34_revenue_compound(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundstd_63d_base_v013_signal(revenue, closeadj):
    result = _std(_f34_revenue_compound(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundstd_252d_base_v014_signal(revenue, closeadj):
    result = _std(_f34_revenue_compound(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundz_252d_base_v015_signal(revenue, closeadj):
    result = _z(_f34_revenue_compound(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundz_504d_base_v016_signal(revenue, closeadj):
    result = _z(_f34_revenue_compound(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundema_63d_base_v017_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundema_252d_base_v018_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_21d_base_v019_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_63d_base_v020_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_126d_base_v021_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_252d_base_v022_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_5d_base_v023_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_10d_base_v024_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_42d_base_v025_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzn_189d_base_v026_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznmean_63d_base_v027_signal(revenue, closeadj):
    result = _mean(_f34_multi_horizon_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznmean_252d_base_v028_signal(revenue, closeadj):
    result = _mean(_f34_multi_horizon_growth(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznstd_252d_base_v029_signal(revenue, closeadj):
    result = _std(_f34_multi_horizon_growth(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznz_252d_base_v030_signal(revenue, closeadj):
    result = _z(_f34_multi_horizon_growth(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznema_252d_base_v031_signal(revenue, closeadj):
    base = _f34_multi_horizon_growth(revenue, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_21d_base_v032_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_63d_base_v033_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_126d_base_v034_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_252d_base_v035_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_504d_base_v036_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_5d_base_v037_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_10d_base_v038_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_42d_base_v039_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_189d_base_v040_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intl_378d_base_v041_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlmean_63d_base_v042_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f34_international_proxy(revenue, ebitdamargin, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlmean_252d_base_v043_signal(revenue, ebitdamargin, closeadj):
    result = _mean(_f34_international_proxy(revenue, ebitdamargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlstd_252d_base_v044_signal(revenue, ebitdamargin, closeadj):
    result = _std(_f34_international_proxy(revenue, ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlz_252d_base_v045_signal(revenue, ebitdamargin, closeadj):
    result = _z(_f34_international_proxy(revenue, ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlema_252d_base_v046_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundxprice_63d_base_v047_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundxprice_252d_base_v048_signal(revenue, closeadj):
    result = _f34_revenue_compound(revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznxprice_63d_base_v049_signal(revenue, closeadj):
    result = _f34_multi_horizon_growth(revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlxprice_252d_base_v050_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundsq_252d_base_v051_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundsign_252d_base_v052_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 252)
    result = np.sign(base) * _mean(closeadj, 63) * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundrank_252d_base_v053_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundmax_252d_base_v054_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundmin_252d_base_v055_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundrange_252d_base_v056_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihznrank_252d_base_v057_signal(revenue, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlrank_252d_base_v058_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlsq_252d_base_v059_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlsign_252d_base_v060_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 252)
    result = np.sign(base) * _mean(closeadj, 63) * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlmax_252d_base_v061_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlmin_252d_base_v062_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlrange_252d_base_v063_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundratio_63v252_base_v064_signal(revenue, closeadj):
    a = _f34_revenue_compound(revenue, 63)
    b = _f34_revenue_compound(revenue, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundcumsum_252d_base_v065_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzncumsum_252d_base_v066_signal(revenue, closeadj):
    base = _f34_multi_horizon_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlcumsum_252d_base_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compounddiff_63d_base_v068_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compounddiff_252d_base_v069_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_multihzndiff_252d_base_v070_signal(revenue, closeadj):
    base = _f34_multi_horizon_growth(revenue, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intldiff_252d_base_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f34_international_proxy(revenue, ebitdamargin, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundlog_252d_base_v072_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_intlxprice_63d_base_v073_signal(revenue, ebitdamargin, closeadj):
    result = _f34_international_proxy(revenue, ebitdamargin, 63) * _mean(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundxema_252d_base_v074_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f34hig_f34_healthcare_international_growth_compoundpctchg_252d_base_v075_signal(revenue, closeadj):
    base = _f34_revenue_compound(revenue, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34hig_f34_healthcare_international_growth_compound_21d_base_v001_signal,
    f34hig_f34_healthcare_international_growth_compound_63d_base_v002_signal,
    f34hig_f34_healthcare_international_growth_compound_126d_base_v003_signal,
    f34hig_f34_healthcare_international_growth_compound_252d_base_v004_signal,
    f34hig_f34_healthcare_international_growth_compound_504d_base_v005_signal,
    f34hig_f34_healthcare_international_growth_compound_5d_base_v006_signal,
    f34hig_f34_healthcare_international_growth_compound_10d_base_v007_signal,
    f34hig_f34_healthcare_international_growth_compound_42d_base_v008_signal,
    f34hig_f34_healthcare_international_growth_compound_189d_base_v009_signal,
    f34hig_f34_healthcare_international_growth_compound_378d_base_v010_signal,
    f34hig_f34_healthcare_international_growth_compoundmean_63d_base_v011_signal,
    f34hig_f34_healthcare_international_growth_compoundmean_252d_base_v012_signal,
    f34hig_f34_healthcare_international_growth_compoundstd_63d_base_v013_signal,
    f34hig_f34_healthcare_international_growth_compoundstd_252d_base_v014_signal,
    f34hig_f34_healthcare_international_growth_compoundz_252d_base_v015_signal,
    f34hig_f34_healthcare_international_growth_compoundz_504d_base_v016_signal,
    f34hig_f34_healthcare_international_growth_compoundema_63d_base_v017_signal,
    f34hig_f34_healthcare_international_growth_compoundema_252d_base_v018_signal,
    f34hig_f34_healthcare_international_growth_multihzn_21d_base_v019_signal,
    f34hig_f34_healthcare_international_growth_multihzn_63d_base_v020_signal,
    f34hig_f34_healthcare_international_growth_multihzn_126d_base_v021_signal,
    f34hig_f34_healthcare_international_growth_multihzn_252d_base_v022_signal,
    f34hig_f34_healthcare_international_growth_multihzn_5d_base_v023_signal,
    f34hig_f34_healthcare_international_growth_multihzn_10d_base_v024_signal,
    f34hig_f34_healthcare_international_growth_multihzn_42d_base_v025_signal,
    f34hig_f34_healthcare_international_growth_multihzn_189d_base_v026_signal,
    f34hig_f34_healthcare_international_growth_multihznmean_63d_base_v027_signal,
    f34hig_f34_healthcare_international_growth_multihznmean_252d_base_v028_signal,
    f34hig_f34_healthcare_international_growth_multihznstd_252d_base_v029_signal,
    f34hig_f34_healthcare_international_growth_multihznz_252d_base_v030_signal,
    f34hig_f34_healthcare_international_growth_multihznema_252d_base_v031_signal,
    f34hig_f34_healthcare_international_growth_intl_21d_base_v032_signal,
    f34hig_f34_healthcare_international_growth_intl_63d_base_v033_signal,
    f34hig_f34_healthcare_international_growth_intl_126d_base_v034_signal,
    f34hig_f34_healthcare_international_growth_intl_252d_base_v035_signal,
    f34hig_f34_healthcare_international_growth_intl_504d_base_v036_signal,
    f34hig_f34_healthcare_international_growth_intl_5d_base_v037_signal,
    f34hig_f34_healthcare_international_growth_intl_10d_base_v038_signal,
    f34hig_f34_healthcare_international_growth_intl_42d_base_v039_signal,
    f34hig_f34_healthcare_international_growth_intl_189d_base_v040_signal,
    f34hig_f34_healthcare_international_growth_intl_378d_base_v041_signal,
    f34hig_f34_healthcare_international_growth_intlmean_63d_base_v042_signal,
    f34hig_f34_healthcare_international_growth_intlmean_252d_base_v043_signal,
    f34hig_f34_healthcare_international_growth_intlstd_252d_base_v044_signal,
    f34hig_f34_healthcare_international_growth_intlz_252d_base_v045_signal,
    f34hig_f34_healthcare_international_growth_intlema_252d_base_v046_signal,
    f34hig_f34_healthcare_international_growth_compoundxprice_63d_base_v047_signal,
    f34hig_f34_healthcare_international_growth_compoundxprice_252d_base_v048_signal,
    f34hig_f34_healthcare_international_growth_multihznxprice_63d_base_v049_signal,
    f34hig_f34_healthcare_international_growth_intlxprice_252d_base_v050_signal,
    f34hig_f34_healthcare_international_growth_compoundsq_252d_base_v051_signal,
    f34hig_f34_healthcare_international_growth_compoundsign_252d_base_v052_signal,
    f34hig_f34_healthcare_international_growth_compoundrank_252d_base_v053_signal,
    f34hig_f34_healthcare_international_growth_compoundmax_252d_base_v054_signal,
    f34hig_f34_healthcare_international_growth_compoundmin_252d_base_v055_signal,
    f34hig_f34_healthcare_international_growth_compoundrange_252d_base_v056_signal,
    f34hig_f34_healthcare_international_growth_multihznrank_252d_base_v057_signal,
    f34hig_f34_healthcare_international_growth_intlrank_252d_base_v058_signal,
    f34hig_f34_healthcare_international_growth_intlsq_252d_base_v059_signal,
    f34hig_f34_healthcare_international_growth_intlsign_252d_base_v060_signal,
    f34hig_f34_healthcare_international_growth_intlmax_252d_base_v061_signal,
    f34hig_f34_healthcare_international_growth_intlmin_252d_base_v062_signal,
    f34hig_f34_healthcare_international_growth_intlrange_252d_base_v063_signal,
    f34hig_f34_healthcare_international_growth_compoundratio_63v252_base_v064_signal,
    f34hig_f34_healthcare_international_growth_compoundcumsum_252d_base_v065_signal,
    f34hig_f34_healthcare_international_growth_multihzncumsum_252d_base_v066_signal,
    f34hig_f34_healthcare_international_growth_intlcumsum_252d_base_v067_signal,
    f34hig_f34_healthcare_international_growth_compounddiff_63d_base_v068_signal,
    f34hig_f34_healthcare_international_growth_compounddiff_252d_base_v069_signal,
    f34hig_f34_healthcare_international_growth_multihzndiff_252d_base_v070_signal,
    f34hig_f34_healthcare_international_growth_intldiff_252d_base_v071_signal,
    f34hig_f34_healthcare_international_growth_compoundlog_252d_base_v072_signal,
    f34hig_f34_healthcare_international_growth_intlxprice_63d_base_v073_signal,
    f34hig_f34_healthcare_international_growth_compoundxema_252d_base_v074_signal,
    f34hig_f34_healthcare_international_growth_compoundpctchg_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_HEALTHCARE_INTERNATIONAL_GROWTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f34_revenue_compound", "_f34_multi_horizon_growth", "_f34_international_proxy")
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
    print(f"OK f34_healthcare_international_growth_base_001_075_claude: {n_features} features pass")
