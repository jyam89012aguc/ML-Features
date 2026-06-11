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
def _f35_self_growth(revenue, w):
    return revenue.pct_change(w)


def _f35_share_gain_proxy(revenue, w):
    g = revenue.pct_change(w)
    return g - _mean(g, w * 2)


def _f35_relative_growth_score(revenue, ebitda, w):
    rg = revenue.pct_change(w)
    eg = ebitda.pct_change(w)
    return _mean(rg + eg, w) - _mean(rg, w * 2)


# ---- features ----

def f35hms_f35_healthcare_market_share_selfg_21d_base_v001_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_63d_base_v002_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_126d_base_v003_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_252d_base_v004_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_504d_base_v005_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_5d_base_v006_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_10d_base_v007_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_42d_base_v008_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_189d_base_v009_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_378d_base_v010_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgmean_63d_base_v011_signal(revenue, closeadj):
    result = _mean(_f35_self_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgmean_252d_base_v012_signal(revenue, closeadj):
    result = _mean(_f35_self_growth(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgstd_63d_base_v013_signal(revenue, closeadj):
    result = _std(_f35_self_growth(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgstd_252d_base_v014_signal(revenue, closeadj):
    result = _std(_f35_self_growth(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgz_252d_base_v015_signal(revenue, closeadj):
    result = _z(_f35_self_growth(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgz_504d_base_v016_signal(revenue, closeadj):
    result = _z(_f35_self_growth(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgema_63d_base_v017_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgema_252d_base_v018_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_21d_base_v019_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_63d_base_v020_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_126d_base_v021_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_252d_base_v022_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_5d_base_v023_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_42d_base_v024_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_189d_base_v025_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainmean_63d_base_v026_signal(revenue, closeadj):
    result = _mean(_f35_share_gain_proxy(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainmean_252d_base_v027_signal(revenue, closeadj):
    result = _mean(_f35_share_gain_proxy(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainstd_252d_base_v028_signal(revenue, closeadj):
    result = _std(_f35_share_gain_proxy(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainz_252d_base_v029_signal(revenue, closeadj):
    result = _z(_f35_share_gain_proxy(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainema_252d_base_v030_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_21d_base_v031_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_63d_base_v032_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_126d_base_v033_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_252d_base_v034_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_5d_base_v035_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_10d_base_v036_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_42d_base_v037_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_189d_base_v038_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegmean_63d_base_v039_signal(revenue, ebitda, closeadj):
    result = _mean(_f35_relative_growth_score(revenue, ebitda, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegmean_252d_base_v040_signal(revenue, ebitda, closeadj):
    result = _mean(_f35_relative_growth_score(revenue, ebitda, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegstd_252d_base_v041_signal(revenue, ebitda, closeadj):
    result = _std(_f35_relative_growth_score(revenue, ebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegz_252d_base_v042_signal(revenue, ebitda, closeadj):
    result = _z(_f35_relative_growth_score(revenue, ebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegema_252d_base_v043_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgxprice_63d_base_v044_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgxprice_252d_base_v045_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainxprice_252d_base_v046_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegxprice_252d_base_v047_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgsq_252d_base_v048_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainsq_252d_base_v049_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegsq_252d_base_v050_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgrank_252d_base_v051_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainrank_252d_base_v052_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegrank_252d_base_v053_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgmax_252d_base_v054_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgmin_252d_base_v055_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgrange_252d_base_v056_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainmax_252d_base_v057_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainmin_252d_base_v058_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegmax_252d_base_v059_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegmin_252d_base_v060_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgsign_252d_base_v061_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = np.sign(base) * _mean(closeadj, 21) * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainsign_252d_base_v062_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = np.sign(base) * _mean(closeadj, 63) * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegsign_252d_base_v063_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = np.sign(base) * _mean(closeadj, 63) * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgratio_63v252_base_v064_signal(revenue, closeadj):
    a = _f35_self_growth(revenue, 63)
    b = _f35_self_growth(revenue, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgcumsum_252d_base_v065_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegaincumsum_252d_base_v066_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegcumsum_252d_base_v067_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfglog_252d_base_v068_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegaindiff_252d_base_v069_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegdiff_252d_base_v070_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgpctchg_252d_base_v071_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainpctchg_252d_base_v072_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfgxema_252d_base_v073_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegainxema_252d_base_v074_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativegxema_252d_base_v075_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35hms_f35_healthcare_market_share_selfg_21d_base_v001_signal,
    f35hms_f35_healthcare_market_share_selfg_63d_base_v002_signal,
    f35hms_f35_healthcare_market_share_selfg_126d_base_v003_signal,
    f35hms_f35_healthcare_market_share_selfg_252d_base_v004_signal,
    f35hms_f35_healthcare_market_share_selfg_504d_base_v005_signal,
    f35hms_f35_healthcare_market_share_selfg_5d_base_v006_signal,
    f35hms_f35_healthcare_market_share_selfg_10d_base_v007_signal,
    f35hms_f35_healthcare_market_share_selfg_42d_base_v008_signal,
    f35hms_f35_healthcare_market_share_selfg_189d_base_v009_signal,
    f35hms_f35_healthcare_market_share_selfg_378d_base_v010_signal,
    f35hms_f35_healthcare_market_share_selfgmean_63d_base_v011_signal,
    f35hms_f35_healthcare_market_share_selfgmean_252d_base_v012_signal,
    f35hms_f35_healthcare_market_share_selfgstd_63d_base_v013_signal,
    f35hms_f35_healthcare_market_share_selfgstd_252d_base_v014_signal,
    f35hms_f35_healthcare_market_share_selfgz_252d_base_v015_signal,
    f35hms_f35_healthcare_market_share_selfgz_504d_base_v016_signal,
    f35hms_f35_healthcare_market_share_selfgema_63d_base_v017_signal,
    f35hms_f35_healthcare_market_share_selfgema_252d_base_v018_signal,
    f35hms_f35_healthcare_market_share_sharegain_21d_base_v019_signal,
    f35hms_f35_healthcare_market_share_sharegain_63d_base_v020_signal,
    f35hms_f35_healthcare_market_share_sharegain_126d_base_v021_signal,
    f35hms_f35_healthcare_market_share_sharegain_252d_base_v022_signal,
    f35hms_f35_healthcare_market_share_sharegain_5d_base_v023_signal,
    f35hms_f35_healthcare_market_share_sharegain_42d_base_v024_signal,
    f35hms_f35_healthcare_market_share_sharegain_189d_base_v025_signal,
    f35hms_f35_healthcare_market_share_sharegainmean_63d_base_v026_signal,
    f35hms_f35_healthcare_market_share_sharegainmean_252d_base_v027_signal,
    f35hms_f35_healthcare_market_share_sharegainstd_252d_base_v028_signal,
    f35hms_f35_healthcare_market_share_sharegainz_252d_base_v029_signal,
    f35hms_f35_healthcare_market_share_sharegainema_252d_base_v030_signal,
    f35hms_f35_healthcare_market_share_relativeg_21d_base_v031_signal,
    f35hms_f35_healthcare_market_share_relativeg_63d_base_v032_signal,
    f35hms_f35_healthcare_market_share_relativeg_126d_base_v033_signal,
    f35hms_f35_healthcare_market_share_relativeg_252d_base_v034_signal,
    f35hms_f35_healthcare_market_share_relativeg_5d_base_v035_signal,
    f35hms_f35_healthcare_market_share_relativeg_10d_base_v036_signal,
    f35hms_f35_healthcare_market_share_relativeg_42d_base_v037_signal,
    f35hms_f35_healthcare_market_share_relativeg_189d_base_v038_signal,
    f35hms_f35_healthcare_market_share_relativegmean_63d_base_v039_signal,
    f35hms_f35_healthcare_market_share_relativegmean_252d_base_v040_signal,
    f35hms_f35_healthcare_market_share_relativegstd_252d_base_v041_signal,
    f35hms_f35_healthcare_market_share_relativegz_252d_base_v042_signal,
    f35hms_f35_healthcare_market_share_relativegema_252d_base_v043_signal,
    f35hms_f35_healthcare_market_share_selfgxprice_63d_base_v044_signal,
    f35hms_f35_healthcare_market_share_selfgxprice_252d_base_v045_signal,
    f35hms_f35_healthcare_market_share_sharegainxprice_252d_base_v046_signal,
    f35hms_f35_healthcare_market_share_relativegxprice_252d_base_v047_signal,
    f35hms_f35_healthcare_market_share_selfgsq_252d_base_v048_signal,
    f35hms_f35_healthcare_market_share_sharegainsq_252d_base_v049_signal,
    f35hms_f35_healthcare_market_share_relativegsq_252d_base_v050_signal,
    f35hms_f35_healthcare_market_share_selfgrank_252d_base_v051_signal,
    f35hms_f35_healthcare_market_share_sharegainrank_252d_base_v052_signal,
    f35hms_f35_healthcare_market_share_relativegrank_252d_base_v053_signal,
    f35hms_f35_healthcare_market_share_selfgmax_252d_base_v054_signal,
    f35hms_f35_healthcare_market_share_selfgmin_252d_base_v055_signal,
    f35hms_f35_healthcare_market_share_selfgrange_252d_base_v056_signal,
    f35hms_f35_healthcare_market_share_sharegainmax_252d_base_v057_signal,
    f35hms_f35_healthcare_market_share_sharegainmin_252d_base_v058_signal,
    f35hms_f35_healthcare_market_share_relativegmax_252d_base_v059_signal,
    f35hms_f35_healthcare_market_share_relativegmin_252d_base_v060_signal,
    f35hms_f35_healthcare_market_share_selfgsign_252d_base_v061_signal,
    f35hms_f35_healthcare_market_share_sharegainsign_252d_base_v062_signal,
    f35hms_f35_healthcare_market_share_relativegsign_252d_base_v063_signal,
    f35hms_f35_healthcare_market_share_selfgratio_63v252_base_v064_signal,
    f35hms_f35_healthcare_market_share_selfgcumsum_252d_base_v065_signal,
    f35hms_f35_healthcare_market_share_sharegaincumsum_252d_base_v066_signal,
    f35hms_f35_healthcare_market_share_relativegcumsum_252d_base_v067_signal,
    f35hms_f35_healthcare_market_share_selfglog_252d_base_v068_signal,
    f35hms_f35_healthcare_market_share_sharegaindiff_252d_base_v069_signal,
    f35hms_f35_healthcare_market_share_relativegdiff_252d_base_v070_signal,
    f35hms_f35_healthcare_market_share_selfgpctchg_252d_base_v071_signal,
    f35hms_f35_healthcare_market_share_sharegainpctchg_252d_base_v072_signal,
    f35hms_f35_healthcare_market_share_selfgxema_252d_base_v073_signal,
    f35hms_f35_healthcare_market_share_sharegainxema_252d_base_v074_signal,
    f35hms_f35_healthcare_market_share_relativegxema_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_HEALTHCARE_MARKET_SHARE_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_self_growth", "_f35_share_gain_proxy", "_f35_relative_growth_score")
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
    print(f"OK f35_healthcare_market_share_base_001_075_claude: {n_features} features pass")
