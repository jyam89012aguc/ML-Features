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
def _f01_asset_growth(assets, w):
    return assets.pct_change(periods=w)


def _f01_rate_base_proxy(ppnenet, w):
    base = ppnenet.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / base.replace(0, np.nan)


def _f01_growth_quality(assets, equity, w):
    a = assets.pct_change(periods=w)
    e = equity.pct_change(periods=w)
    return a - e


# 5d jerk of 21d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v001_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v002_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v003_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v004_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v005_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v006_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_jerk_v007_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_jerk_v008_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v009_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v010_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v011_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v012_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v013_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v014_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_504d_jerk_v015_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v016_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v017_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v018_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v019_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_504d_jerk_v020_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 504) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × volume × close
def f01rrb_f01_regulated_rate_base_growth_assetxvol_63d_jerk_v021_signal(assets, closeadj, volume):
    base = _f01_asset_growth(assets, 63) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × volume × close
def f01rrb_f01_regulated_rate_base_growth_assetxvol_252d_jerk_v022_signal(assets, closeadj, volume):
    base = _f01_asset_growth(assets, 252) * closeadj * _mean(volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × volume × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexvol_63d_jerk_v023_signal(ppnenet, closeadj, volume):
    base = _f01_rate_base_proxy(ppnenet, 63) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × volume × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexvol_252d_jerk_v024_signal(ppnenet, closeadj, volume):
    base = _f01_rate_base_proxy(ppnenet, 252) * closeadj * _mean(volume, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset-z × close
def f01rrb_f01_regulated_rate_base_growth_assetz_63d_jerk_v025_signal(assets, closeadj):
    base = _z(_f01_asset_growth(assets, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset-z × close
def f01rrb_f01_regulated_rate_base_growth_assetz_252d_jerk_v026_signal(assets, closeadj):
    base = _z(_f01_asset_growth(assets, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base z × close
def f01rrb_f01_regulated_rate_base_growth_ratebasez_63d_jerk_v027_signal(ppnenet, closeadj):
    base = _z(_f01_rate_base_proxy(ppnenet, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base z × close
def f01rrb_f01_regulated_rate_base_growth_ratebasez_252d_jerk_v028_signal(ppnenet, closeadj):
    base = _z(_f01_rate_base_proxy(ppnenet, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth-quality z × close
def f01rrb_f01_regulated_rate_base_growth_qualityz_63d_jerk_v029_signal(assets, equity, closeadj):
    base = _z(_f01_growth_quality(assets, equity, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth-quality z × close
def f01rrb_f01_regulated_rate_base_growth_qualityz_252d_jerk_v030_signal(assets, equity, closeadj):
    base = _z(_f01_growth_quality(assets, equity, 252), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth rolling mean × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_63d_jerk_v031_signal(assets, closeadj):
    base = _mean(_f01_asset_growth(assets, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth rolling mean × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_252d_jerk_v032_signal(assets, closeadj):
    base = _mean(_f01_asset_growth(assets, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base rolling mean × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_63d_jerk_v033_signal(ppnenet, closeadj):
    base = _mean(_f01_rate_base_proxy(ppnenet, 63), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base rolling mean × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_252d_jerk_v034_signal(ppnenet, closeadj):
    base = _mean(_f01_rate_base_proxy(ppnenet, 252), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth volatility × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_63d_jerk_v035_signal(assets, closeadj):
    base = _std(_f01_asset_growth(assets, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of rate-base volatility × close
def f01rrb_f01_regulated_rate_base_growth_ratebasevol_252d_jerk_v036_signal(ppnenet, closeadj):
    base = _std(_f01_rate_base_proxy(ppnenet, 252), 252) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth × scale × close
def f01rrb_f01_regulated_rate_base_growth_growthxscale_63d_jerk_v037_signal(assets, ppnenet, closeadj):
    base = _f01_asset_growth(assets, 63) * _f01_rate_base_proxy(ppnenet, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth × scale × close
def f01rrb_f01_regulated_rate_base_growth_growthxscale_252d_jerk_v038_signal(assets, ppnenet, closeadj):
    base = _f01_asset_growth(assets, 252) * _f01_rate_base_proxy(ppnenet, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of equity / assets × close
def f01rrb_f01_regulated_rate_base_growth_equityratio_63d_jerk_v039_signal(equity, assets, closeadj):
    gq = _f01_growth_quality(assets, equity, 63)
    base = (_mean(equity, 63) / _mean(assets, 63).replace(0, np.nan)) * closeadj + gq * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of equity / assets × close
def f01rrb_f01_regulated_rate_base_growth_equityratio_252d_jerk_v040_signal(equity, assets, closeadj):
    gq = _f01_growth_quality(assets, equity, 252)
    base = (_mean(equity, 252) / _mean(assets, 252).replace(0, np.nan)) * closeadj + gq * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth squared × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_21d_jerk_v041_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    base = g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth squared × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_63d_jerk_v042_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth EMA × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthema_63d_jerk_v043_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth EMA × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthema_252d_jerk_v044_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g.ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base EMA × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseema_63d_jerk_v045_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r.ewm(span=21, min_periods=5).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base EMA × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseema_252d_jerk_v046_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r.ewm(span=63, min_periods=21).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth rank × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_63d_jerk_v047_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth rank × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_252d_jerk_v048_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base rank × close
def f01rrb_f01_regulated_rate_base_growth_ratebaserank_63d_jerk_v049_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base rank × close
def f01rrb_f01_regulated_rate_base_growth_ratebaserank_252d_jerk_v050_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r.rolling(504, min_periods=126).rank(pct=True) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of dual growth × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_21d_jerk_v051_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 21)
    p = ppnenet.pct_change(21)
    rb = _f01_rate_base_proxy(ppnenet, 21)
    base = a * p * closeadj + rb * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of dual growth 63d × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_63d_jerk_v052_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 63)
    p = ppnenet.pct_change(63)
    rb = _f01_rate_base_proxy(ppnenet, 63)
    base = a * p * closeadj + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dual growth 252d × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_252d_jerk_v053_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 252)
    p = ppnenet.pct_change(252)
    rb = _f01_rate_base_proxy(ppnenet, 252)
    base = a * p * closeadj + rb * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth gap × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_63d_jerk_v054_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = (g - _mean(g, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth gap × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_252d_jerk_v055_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = (g - _mean(g, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base gap × close
def f01rrb_f01_regulated_rate_base_growth_ratebasegap_63d_jerk_v056_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = (r - _mean(r, 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base gap × close
def f01rrb_f01_regulated_rate_base_growth_ratebasegap_252d_jerk_v057_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = (r - _mean(r, 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × close pct × close
def f01rrb_f01_regulated_rate_base_growth_assetxretpct_63d_jerk_v058_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × close pct × close
def f01rrb_f01_regulated_rate_base_growth_assetxretpct_252d_jerk_v059_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × close pct × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_63d_jerk_v060_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r * closeadj.pct_change(21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × close pct × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_252d_jerk_v061_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r * closeadj.pct_change(63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × abs(return) × close
def f01rrb_f01_regulated_rate_base_growth_assetxabsret_63d_jerk_v062_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × abs(return) × close
def f01rrb_f01_regulated_rate_base_growth_assetxabsret_252d_jerk_v063_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality × abs(return) × close
def f01rrb_f01_regulated_rate_base_growth_qualityxabsret_63d_jerk_v064_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    base = q * closeadj.pct_change(21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality × abs(return) × close
def f01rrb_f01_regulated_rate_base_growth_qualityxabsret_252d_jerk_v065_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    base = q * closeadj.pct_change(63).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth acceleration × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_63d_jerk_v066_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = (g - g.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth acceleration × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_252d_jerk_v067_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = (g - g.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base acceleration × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_63d_jerk_v068_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = (r - r.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base acceleration × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_252d_jerk_v069_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = (r - r.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality acceleration × close
def f01rrb_f01_regulated_rate_base_growth_qualityaccel_63d_jerk_v070_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    base = (q - q.shift(21)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality acceleration × close
def f01rrb_f01_regulated_rate_base_growth_qualityaccel_252d_jerk_v071_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    base = (q - q.shift(63)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × ATR
def f01rrb_f01_regulated_rate_base_growth_assetxatr_63d_jerk_v072_signal(assets, closeadj, high, low):
    g = _f01_asset_growth(assets, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = g * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × ATR
def f01rrb_f01_regulated_rate_base_growth_assetxatr_252d_jerk_v073_signal(assets, closeadj, high, low):
    g = _f01_asset_growth(assets, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = g * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × ATR
def f01rrb_f01_regulated_rate_base_growth_ratebasexatr_63d_jerk_v074_signal(ppnenet, closeadj, high, low):
    r = _f01_rate_base_proxy(ppnenet, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = r * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × ATR
def f01rrb_f01_regulated_rate_base_growth_ratebasexatr_252d_jerk_v075_signal(ppnenet, closeadj, high, low):
    r = _f01_rate_base_proxy(ppnenet, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = r * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_assetxdv_63d_jerk_v076_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 63)
    dv = closeadj * volume
    base = g * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_assetxdv_252d_jerk_v077_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 252)
    dv = closeadj * volume
    base = g * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_ratebasexdv_63d_jerk_v078_signal(ppnenet, closeadj, volume):
    r = _f01_rate_base_proxy(ppnenet, 63)
    dv = closeadj * volume
    base = r * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_ratebasexdv_252d_jerk_v079_signal(ppnenet, closeadj, volume):
    r = _f01_rate_base_proxy(ppnenet, 252)
    dv = closeadj * volume
    base = r * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_qualityxdv_63d_jerk_v080_signal(assets, equity, closeadj, volume):
    q = _f01_growth_quality(assets, equity, 63)
    dv = closeadj * volume
    base = q * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_qualityxdv_252d_jerk_v081_signal(assets, equity, closeadj, volume):
    q = _f01_growth_quality(assets, equity, 252)
    dv = closeadj * volume
    base = q * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of asset log growth × close
def f01rrb_f01_regulated_rate_base_growth_assetloggrowth_63d_jerk_v082_signal(assets, closeadj):
    rb = _f01_asset_growth(assets, 63)
    base = np.log(assets.replace(0, np.nan)).diff(63) * closeadj + rb * 0.0
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset log growth × close
def f01rrb_f01_regulated_rate_base_growth_assetloggrowth_252d_jerk_v083_signal(assets, closeadj):
    rb = _f01_asset_growth(assets, 252)
    base = np.log(assets.replace(0, np.nan)).diff(252) * closeadj + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ppnenet log × close
def f01rrb_f01_regulated_rate_base_growth_ppnelog_63d_jerk_v084_signal(ppnenet, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 63)
    base = np.log(ppnenet.replace(0, np.nan)).diff(63) * closeadj + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ppnenet log × close
def f01rrb_f01_regulated_rate_base_growth_ppnelog_252d_jerk_v085_signal(ppnenet, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 252)
    base = np.log(ppnenet.replace(0, np.nan)).diff(252) * closeadj + rb * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ppnenet/assets ratio × close
def f01rrb_f01_regulated_rate_base_growth_rbintensity_63d_jerk_v086_signal(ppnenet, assets, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 63)
    base = (ppnenet / assets.replace(0, np.nan)) * closeadj + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ppnenet/assets ratio × close
def f01rrb_f01_regulated_rate_base_growth_rbintensity_252d_jerk_v087_signal(ppnenet, assets, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 252)
    base = (ppnenet / assets.replace(0, np.nan)) * closeadj + rb * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × inverse close
def f01rrb_f01_regulated_rate_base_growth_assetxinvprice_63d_jerk_v088_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × inverse close
def f01rrb_f01_regulated_rate_base_growth_assetxinvprice_252d_jerk_v089_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of equity / assets × close return × close
def f01rrb_f01_regulated_rate_base_growth_eqassetxret_63d_jerk_v090_signal(assets, equity, closeadj):
    gq = _f01_growth_quality(assets, equity, 63)
    er = equity / assets.replace(0, np.nan)
    base = er * closeadj.pct_change(21) * closeadj + gq * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of equity / assets × close return × close
def f01rrb_f01_regulated_rate_base_growth_eqassetxret_252d_jerk_v091_signal(assets, equity, closeadj):
    gq = _f01_growth_quality(assets, equity, 252)
    er = equity / assets.replace(0, np.nan)
    base = er * closeadj.pct_change(63) * closeadj + gq * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_ppnegrowth_63d_jerk_v092_signal(ppnenet, closeadj):
    g = ppnenet.pct_change(63) * closeadj
    rb = _f01_rate_base_proxy(ppnenet, 63)
    base = g + rb * 0.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_ppnegrowth_252d_jerk_v093_signal(ppnenet, closeadj):
    g = ppnenet.pct_change(252) * closeadj
    rb = _f01_rate_base_proxy(ppnenet, 252)
    base = g + rb * 0.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rolling-sum asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_63d_jerk_v094_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g.rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rolling-sum asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_252d_jerk_v095_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × close-z × close
def f01rrb_f01_regulated_rate_base_growth_assetxclosez_63d_jerk_v096_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × close-z × close
def f01rrb_f01_regulated_rate_base_growth_assetxclosez_252d_jerk_v097_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × close-z × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_63d_jerk_v098_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r * _z(closeadj, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × close-z × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_252d_jerk_v099_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r * _z(closeadj, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of asset growth abs × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_21d_jerk_v100_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21).abs()
    base = g * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth abs × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_63d_jerk_v101_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63).abs()
    base = g * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base abs × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseabs_21d_jerk_v102_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 21)
    base = (r - 1.0).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base abs × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseabs_63d_jerk_v103_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = (r - 1.0).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality abs × close
def f01rrb_f01_regulated_rate_base_growth_qualityabs_63d_jerk_v104_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63).abs()
    base = q * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality abs × close
def f01rrb_f01_regulated_rate_base_growth_qualityabs_252d_jerk_v105_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252).abs()
    base = q * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth sign × close × volume
def f01rrb_f01_regulated_rate_base_growth_assetsign_63d_jerk_v106_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 63)
    base = np.sign(g) * _mean(volume, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth sign × close × volume
def f01rrb_f01_regulated_rate_base_growth_assetsign_252d_jerk_v107_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 252)
    base = np.sign(g) * _mean(volume, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base sign × close
def f01rrb_f01_regulated_rate_base_growth_ratebasesign_63d_jerk_v108_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = np.sign(r - 1.0) * closeadj * _mean(closeadj, 21) / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × equity ratio × close
def f01rrb_f01_regulated_rate_base_growth_assetxeqratio_63d_jerk_v109_signal(assets, equity, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * (equity / assets.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth × equity ratio × close
def f01rrb_f01_regulated_rate_base_growth_assetxeqratio_252d_jerk_v110_signal(assets, equity, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * (equity / assets.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base × equity ratio × close
def f01rrb_f01_regulated_rate_base_growth_rbxeqratio_63d_jerk_v111_signal(ppnenet, equity, assets, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r * (equity / assets.replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base × equity ratio × close
def f01rrb_f01_regulated_rate_base_growth_rbxeqratio_252d_jerk_v112_signal(ppnenet, equity, assets, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r * (equity / assets.replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality × growth × close
def f01rrb_f01_regulated_rate_base_growth_qualityxgrowth_63d_jerk_v113_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    g = _f01_asset_growth(assets, 63)
    base = q * g * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality × growth × close
def f01rrb_f01_regulated_rate_base_growth_qualityxgrowth_252d_jerk_v114_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    g = _f01_asset_growth(assets, 252)
    base = q * g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base log × close
def f01rrb_f01_regulated_rate_base_growth_ratebaselog_63d_jerk_v115_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = np.log(r.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base log × close
def f01rrb_f01_regulated_rate_base_growth_ratebaselog_252d_jerk_v116_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = np.log(r.abs().replace(0, np.nan)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (asset growth + 1) × rate-base × close
def f01rrb_f01_regulated_rate_base_growth_assetxrb_63d_jerk_v117_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = (a + 1.0) * r * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (asset growth + 1) × rate-base × close
def f01rrb_f01_regulated_rate_base_growth_assetxrb_252d_jerk_v118_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = (a + 1.0) * r * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v119_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v120_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v121_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 252d rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v122_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of asset growth 63d × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v123_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of asset growth 252d × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v124_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d jerk of asset growth 21d × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v125_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d jerk of rate-base 21d × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v126_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d jerk of asset growth 63d × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v127_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d jerk of rate-base 63d × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v128_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d jerk of growth quality 63d × close
def f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v129_signal(assets, equity, closeadj):
    base = _f01_growth_quality(assets, equity, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d jerk of asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v130_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d jerk of rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v131_signal(ppnenet, closeadj):
    base = _f01_rate_base_proxy(ppnenet, 252) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (rate-base × asset growth) × ATR
def f01rrb_f01_regulated_rate_base_growth_combo_atr_63d_jerk_v132_signal(assets, ppnenet, closeadj, high, low):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = a * r * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of combo × ATR
def f01rrb_f01_regulated_rate_base_growth_combo_atr_252d_jerk_v133_signal(assets, ppnenet, closeadj, high, low):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = a * r * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (rate-base × asset growth) × dv
def f01rrb_f01_regulated_rate_base_growth_combo_dv_63d_jerk_v134_signal(assets, ppnenet, closeadj, volume):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    dv = closeadj * volume
    base = a * r * _mean(dv, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of combo × dv
def f01rrb_f01_regulated_rate_base_growth_combo_dv_252d_jerk_v135_signal(assets, ppnenet, closeadj, volume):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    dv = closeadj * volume
    base = a * r * _mean(dv, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (a + r - 1) × close
def f01rrb_f01_regulated_rate_base_growth_combosum_63d_jerk_v136_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = (a + r - 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (a + r - 1) × close
def f01rrb_f01_regulated_rate_base_growth_combosum_252d_jerk_v137_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = (a + r - 1.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthdn_63d_jerk_v138_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g.diff(21) / g.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthdn_252d_jerk_v139_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g.diff(63) / g.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of rate-base diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_ratebasedn_63d_jerk_v140_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    base = r.diff(21) / r.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of rate-base diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_ratebasedn_252d_jerk_v141_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    base = r.diff(63) / r.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_qualitydn_63d_jerk_v142_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    base = q.diff(21) / q.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality diff-norm × close
def f01rrb_f01_regulated_rate_base_growth_qualitydn_252d_jerk_v143_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    base = q.diff(63) / q.abs().replace(0, np.nan) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × asset growth × close (squared, signed)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthcube_63d_jerk_v144_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    base = g * g * g.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of asset growth cubed × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthcube_252d_jerk_v145_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    base = g * g * g.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of growth quality EMA × close (long span)
def f01rrb_f01_regulated_rate_base_growth_qualityema_63d_jerk_v146_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    base = q.ewm(span=126, min_periods=21).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of growth quality EMA × close
def f01rrb_f01_regulated_rate_base_growth_qualityema_252d_jerk_v147_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    base = q.ewm(span=126, min_periods=42).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of (a × p) × ATR with ppnenet pct change
def f01rrb_f01_regulated_rate_base_growth_dualgrowthatr_63d_jerk_v148_signal(assets, ppnenet, closeadj, high, low):
    a = _f01_asset_growth(assets, 63)
    p = ppnenet.pct_change(63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = a * p * atr
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of dual growth × ATR
def f01rrb_f01_regulated_rate_base_growth_dualgrowthatr_252d_jerk_v149_signal(assets, ppnenet, closeadj, high, low):
    a = _f01_asset_growth(assets, 252)
    p = ppnenet.pct_change(252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    base = a * p * atr
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of asset growth × equity / assets × close × volume
def f01rrb_f01_regulated_rate_base_growth_assetxeqxvol_63d_jerk_v150_signal(assets, equity, closeadj, volume):
    g = _f01_asset_growth(assets, 63)
    base = g * (equity / assets.replace(0, np.nan)) * closeadj * _mean(volume, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v001_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v002_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v003_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v004_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v005_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v006_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_jerk_v007_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_jerk_v008_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v009_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v010_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v011_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v012_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v013_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v014_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_504d_jerk_v015_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v016_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v017_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v018_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v019_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_504d_jerk_v020_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxvol_63d_jerk_v021_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxvol_252d_jerk_v022_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexvol_63d_jerk_v023_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexvol_252d_jerk_v024_signal,
    f01rrb_f01_regulated_rate_base_growth_assetz_63d_jerk_v025_signal,
    f01rrb_f01_regulated_rate_base_growth_assetz_252d_jerk_v026_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasez_63d_jerk_v027_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasez_252d_jerk_v028_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityz_63d_jerk_v029_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityz_252d_jerk_v030_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_63d_jerk_v031_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_252d_jerk_v032_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_63d_jerk_v033_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_252d_jerk_v034_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_63d_jerk_v035_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasevol_252d_jerk_v036_signal,
    f01rrb_f01_regulated_rate_base_growth_growthxscale_63d_jerk_v037_signal,
    f01rrb_f01_regulated_rate_base_growth_growthxscale_252d_jerk_v038_signal,
    f01rrb_f01_regulated_rate_base_growth_equityratio_63d_jerk_v039_signal,
    f01rrb_f01_regulated_rate_base_growth_equityratio_252d_jerk_v040_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_21d_jerk_v041_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_63d_jerk_v042_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthema_63d_jerk_v043_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthema_252d_jerk_v044_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseema_63d_jerk_v045_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseema_252d_jerk_v046_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_63d_jerk_v047_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_252d_jerk_v048_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaserank_63d_jerk_v049_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaserank_252d_jerk_v050_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_21d_jerk_v051_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_63d_jerk_v052_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_252d_jerk_v053_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_63d_jerk_v054_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_252d_jerk_v055_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasegap_63d_jerk_v056_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasegap_252d_jerk_v057_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxretpct_63d_jerk_v058_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxretpct_252d_jerk_v059_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_63d_jerk_v060_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_252d_jerk_v061_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxabsret_63d_jerk_v062_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxabsret_252d_jerk_v063_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxabsret_63d_jerk_v064_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxabsret_252d_jerk_v065_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_63d_jerk_v066_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_252d_jerk_v067_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_63d_jerk_v068_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_252d_jerk_v069_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityaccel_63d_jerk_v070_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityaccel_252d_jerk_v071_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxatr_63d_jerk_v072_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxatr_252d_jerk_v073_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexatr_63d_jerk_v074_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexatr_252d_jerk_v075_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxdv_63d_jerk_v076_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxdv_252d_jerk_v077_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexdv_63d_jerk_v078_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexdv_252d_jerk_v079_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxdv_63d_jerk_v080_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxdv_252d_jerk_v081_signal,
    f01rrb_f01_regulated_rate_base_growth_assetloggrowth_63d_jerk_v082_signal,
    f01rrb_f01_regulated_rate_base_growth_assetloggrowth_252d_jerk_v083_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnelog_63d_jerk_v084_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnelog_252d_jerk_v085_signal,
    f01rrb_f01_regulated_rate_base_growth_rbintensity_63d_jerk_v086_signal,
    f01rrb_f01_regulated_rate_base_growth_rbintensity_252d_jerk_v087_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxinvprice_63d_jerk_v088_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxinvprice_252d_jerk_v089_signal,
    f01rrb_f01_regulated_rate_base_growth_eqassetxret_63d_jerk_v090_signal,
    f01rrb_f01_regulated_rate_base_growth_eqassetxret_252d_jerk_v091_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowth_63d_jerk_v092_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowth_252d_jerk_v093_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_63d_jerk_v094_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_252d_jerk_v095_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxclosez_63d_jerk_v096_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxclosez_252d_jerk_v097_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_63d_jerk_v098_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_252d_jerk_v099_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_21d_jerk_v100_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_63d_jerk_v101_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseabs_21d_jerk_v102_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseabs_63d_jerk_v103_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityabs_63d_jerk_v104_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityabs_252d_jerk_v105_signal,
    f01rrb_f01_regulated_rate_base_growth_assetsign_63d_jerk_v106_signal,
    f01rrb_f01_regulated_rate_base_growth_assetsign_252d_jerk_v107_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasesign_63d_jerk_v108_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxeqratio_63d_jerk_v109_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxeqratio_252d_jerk_v110_signal,
    f01rrb_f01_regulated_rate_base_growth_rbxeqratio_63d_jerk_v111_signal,
    f01rrb_f01_regulated_rate_base_growth_rbxeqratio_252d_jerk_v112_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxgrowth_63d_jerk_v113_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxgrowth_252d_jerk_v114_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaselog_63d_jerk_v115_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaselog_252d_jerk_v116_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrb_63d_jerk_v117_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrb_252d_jerk_v118_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v119_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_252d_jerk_v120_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v121_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v122_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v123_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v124_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_jerk_v125_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_21d_jerk_v126_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_jerk_v127_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_63d_jerk_v128_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_63d_jerk_v129_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_jerk_v130_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_252d_jerk_v131_signal,
    f01rrb_f01_regulated_rate_base_growth_combo_atr_63d_jerk_v132_signal,
    f01rrb_f01_regulated_rate_base_growth_combo_atr_252d_jerk_v133_signal,
    f01rrb_f01_regulated_rate_base_growth_combo_dv_63d_jerk_v134_signal,
    f01rrb_f01_regulated_rate_base_growth_combo_dv_252d_jerk_v135_signal,
    f01rrb_f01_regulated_rate_base_growth_combosum_63d_jerk_v136_signal,
    f01rrb_f01_regulated_rate_base_growth_combosum_252d_jerk_v137_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthdn_63d_jerk_v138_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthdn_252d_jerk_v139_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasedn_63d_jerk_v140_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasedn_252d_jerk_v141_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitydn_63d_jerk_v142_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitydn_252d_jerk_v143_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthcube_63d_jerk_v144_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthcube_252d_jerk_v145_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityema_63d_jerk_v146_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityema_252d_jerk_v147_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowthatr_63d_jerk_v148_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowthatr_252d_jerk_v149_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxeqxvol_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_REGULATED_RATE_BASE_GROWTH_REGISTRY_JERK_001_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "assets": assets, "ppnenet": ppnenet, "equity": equity,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f01_asset_growth", "_f01_rate_base_proxy", "_f01_growth_quality")
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
    print(f"OK f01_regulated_rate_base_growth_3rd_derivatives_001_150_claude: {n_features} features pass")
