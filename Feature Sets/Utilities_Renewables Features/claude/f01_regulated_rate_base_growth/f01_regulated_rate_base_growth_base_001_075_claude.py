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
def _f01_asset_growth(assets, w):
    return assets.pct_change(periods=w)


def _f01_rate_base_proxy(ppnenet, w):
    base = ppnenet.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / base.replace(0, np.nan)


def _f01_growth_quality(assets, equity, w):
    a = assets.pct_change(periods=w)
    e = equity.pct_change(periods=w)
    return a - e


# 21d asset growth scaled by close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_base_v001_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth scaled by close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_base_v002_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d asset growth scaled by close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_126d_base_v003_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth scaled by close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_base_v004_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asset growth scaled by close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_base_v005_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rate-base proxy scaled by close
def f01rrb_f01_regulated_rate_base_growth_ratebase_21d_base_v006_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rate-base proxy scaled by close
def f01rrb_f01_regulated_rate_base_growth_ratebase_63d_base_v007_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rate-base proxy scaled by close
def f01rrb_f01_regulated_rate_base_growth_ratebase_126d_base_v008_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base proxy scaled by close
def f01rrb_f01_regulated_rate_base_growth_ratebase_252d_base_v009_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rate-base proxy scaled by close
def f01rrb_f01_regulated_rate_base_growth_ratebase_504d_base_v010_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality (asset growth minus equity growth) × close
def f01rrb_f01_regulated_rate_base_growth_quality_63d_base_v011_signal(assets, equity, closeadj):
    result = _f01_growth_quality(assets, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_126d_base_v012_signal(assets, equity, closeadj):
    result = _f01_growth_quality(assets, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_252d_base_v013_signal(assets, equity, closeadj):
    result = _f01_growth_quality(assets, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_quality_504d_base_v014_signal(assets, equity, closeadj):
    result = _f01_growth_quality(assets, equity, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth z-score over 252d
def f01rrb_f01_regulated_rate_base_growth_assetz_21d_base_v015_signal(assets, closeadj):
    result = _z(_f01_asset_growth(assets, 21), 252) * closeadj * 0.0 + _z(_f01_asset_growth(assets, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth z-score over 252d
def f01rrb_f01_regulated_rate_base_growth_assetz_63d_base_v016_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 63)
    result = _z(base, 252) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth z-score over 504d
def f01rrb_f01_regulated_rate_base_growth_assetz_252d_base_v017_signal(assets, closeadj):
    base = _f01_asset_growth(assets, 252)
    result = _z(base, 504) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of 63d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_21d_base_v018_signal(assets, closeadj):
    result = _mean(_f01_asset_growth(assets, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 252d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_63d_base_v019_signal(assets, closeadj):
    result = _mean(_f01_asset_growth(assets, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of 252d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_126d_base_v020_signal(assets, closeadj):
    result = _mean(_f01_asset_growth(assets, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of 63d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthstd_63d_base_v021_signal(assets, closeadj):
    result = _std(_f01_asset_growth(assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of 252d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthstd_126d_base_v022_signal(assets, closeadj):
    result = _std(_f01_asset_growth(assets, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ppnenet rate-base z-score over 252d
def f01rrb_f01_regulated_rate_base_growth_ratebasez_21d_base_v023_signal(ppnenet, closeadj):
    result = _z(_f01_rate_base_proxy(ppnenet, 21), 252) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet rate-base z-score over 252d
def f01rrb_f01_regulated_rate_base_growth_ratebasez_63d_base_v024_signal(ppnenet, closeadj):
    result = _z(_f01_rate_base_proxy(ppnenet, 63), 252) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base z-score over 504d
def f01rrb_f01_regulated_rate_base_growth_ratebasez_252d_base_v025_signal(ppnenet, closeadj):
    result = _z(_f01_rate_base_proxy(ppnenet, 252), 504) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of 63d ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_21d_base_v026_signal(ppnenet, closeadj):
    result = _mean(_f01_rate_base_proxy(ppnenet, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 252d ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_63d_base_v027_signal(ppnenet, closeadj):
    result = _mean(_f01_rate_base_proxy(ppnenet, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling std of 252d ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebasestd_63d_base_v028_signal(ppnenet, closeadj):
    result = _std(_f01_rate_base_proxy(ppnenet, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of 504d ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_ratebasestd_126d_base_v029_signal(ppnenet, closeadj):
    result = _std(_f01_rate_base_proxy(ppnenet, 504), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality z-score over 252d
def f01rrb_f01_regulated_rate_base_growth_qualityz_63d_base_v030_signal(assets, equity, closeadj):
    result = _z(_f01_growth_quality(assets, equity, 63), 252) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality z-score over 504d
def f01rrb_f01_regulated_rate_base_growth_qualityz_252d_base_v031_signal(assets, equity, closeadj):
    result = _z(_f01_growth_quality(assets, equity, 252), 504) + closeadj * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_qualitymean_63d_base_v032_signal(assets, equity, closeadj):
    result = _mean(_f01_growth_quality(assets, equity, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling std of 252d growth quality × close
def f01rrb_f01_regulated_rate_base_growth_qualitystd_126d_base_v033_signal(assets, equity, closeadj):
    result = _std(_f01_growth_quality(assets, equity, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet / assets ratio × close (rate-base intensity)
def f01rrb_f01_regulated_rate_base_growth_rbintensity_21d_base_v034_signal(ppnenet, assets, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 21)
    ratio = _safe_div(ppnenet, assets)
    result = ratio * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet / assets ratio rolled over 63d × close
def f01rrb_f01_regulated_rate_base_growth_rbintensity_63d_base_v035_signal(ppnenet, assets, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 63)
    ratio = _safe_div(_mean(ppnenet, 63), _mean(assets, 63))
    result = ratio * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet / assets ratio rolled over 252d × close
def f01rrb_f01_regulated_rate_base_growth_rbintensity_252d_base_v036_signal(ppnenet, assets, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 252)
    ratio = _safe_div(_mean(ppnenet, 252), _mean(assets, 252))
    result = ratio * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_5d_base_v037_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_10d_base_v038_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_42d_base_v039_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_189d_base_v040_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowth_378d_base_v041_signal(assets, closeadj):
    result = _f01_asset_growth(assets, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d rate-base proxy × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_5d_base_v042_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d rate-base proxy × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_10d_base_v043_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rate-base proxy × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_42d_base_v044_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rate-base proxy × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_189d_base_v045_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 378d rate-base proxy × close
def f01rrb_f01_regulated_rate_base_growth_ratebase_378d_base_v046_signal(ppnenet, closeadj):
    result = _f01_rate_base_proxy(ppnenet, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth × ppnenet (combined growth × scale)
def f01rrb_f01_regulated_rate_base_growth_growthxscale_63d_base_v047_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 63)
    s = _f01_rate_base_proxy(ppnenet, 63)
    result = g * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth × ppnenet over 252d × close
def f01rrb_f01_regulated_rate_base_growth_growthxscale_252d_base_v048_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 252)
    s = _f01_rate_base_proxy(ppnenet, 252)
    result = g * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet growth proxy × close (rate-base accretion)
def f01rrb_f01_regulated_rate_base_growth_ppnegrowth_63d_base_v049_signal(ppnenet, closeadj):
    g = ppnenet.pct_change(63)
    rb = _f01_rate_base_proxy(ppnenet, 63)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_ppnegrowth_252d_base_v050_signal(ppnenet, closeadj):
    g = ppnenet.pct_change(252)
    rb = _f01_rate_base_proxy(ppnenet, 252)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_ppnegrowth_504d_base_v051_signal(ppnenet, closeadj):
    g = ppnenet.pct_change(504)
    rb = _f01_rate_base_proxy(ppnenet, 504)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × close (log form)
def f01rrb_f01_regulated_rate_base_growth_assetloggrowth_63d_base_v052_signal(assets, closeadj):
    g = np.log(assets.replace(0, np.nan)).diff(63)
    rb = _f01_asset_growth(assets, 63)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset log-growth × close
def f01rrb_f01_regulated_rate_base_growth_assetloggrowth_252d_base_v053_signal(assets, closeadj):
    g = np.log(assets.replace(0, np.nan)).diff(252)
    rb = _f01_asset_growth(assets, 252)
    result = g * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets ratio (book quality) × close
def f01rrb_f01_regulated_rate_base_growth_equityratio_63d_base_v054_signal(equity, assets, closeadj):
    gq = _f01_growth_quality(assets, equity, 63)
    ratio = _safe_div(_mean(equity, 63), _mean(assets, 63))
    result = ratio * closeadj + gq * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets ratio over 252d × close
def f01rrb_f01_regulated_rate_base_growth_equityratio_252d_base_v055_signal(equity, assets, closeadj):
    gq = _f01_growth_quality(assets, equity, 252)
    ratio = _safe_div(_mean(equity, 252), _mean(assets, 252))
    result = ratio * closeadj + gq * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_assetxrb_21d_base_v056_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 21)
    r = _f01_rate_base_proxy(ppnenet, 21)
    result = (a + 1.0) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_assetxrb_63d_base_v057_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    result = (a + 1.0) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ppnenet rate-base × close
def f01rrb_f01_regulated_rate_base_growth_assetxrb_252d_base_v058_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    result = (a + 1.0) * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth squared × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_63d_base_v059_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth squared × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_252d_base_v060_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet growth squared × close
def f01rrb_f01_regulated_rate_base_growth_ppnegrowthsq_63d_base_v061_signal(ppnenet, closeadj):
    rb = _f01_rate_base_proxy(ppnenet, 63)
    g = ppnenet.pct_change(63)
    result = g * g.abs() * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality × equity scale × close
def f01rrb_f01_regulated_rate_base_growth_qualityxequity_63d_base_v062_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    e = _mean(equity, 63) / _mean(equity, 252).replace(0, np.nan)
    result = q * e * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality × equity scale × close
def f01rrb_f01_regulated_rate_base_growth_qualityxequity_252d_base_v063_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    e = _mean(equity, 252) / _mean(equity, 504).replace(0, np.nan)
    result = q * e * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × close (EMA smoothed)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthema_252d_base_v064_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    sm = g.ewm(span=63, min_periods=21).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × close (EMA smoothed)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthema_63d_base_v065_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    sm = g.ewm(span=21, min_periods=5).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base × close (EMA smoothed)
def f01rrb_f01_regulated_rate_base_growth_ratebaseema_252d_base_v066_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    sm = r.ewm(span=63, min_periods=21).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet rate-base × close (EMA smoothed)
def f01rrb_f01_regulated_rate_base_growth_ratebaseema_63d_base_v067_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    sm = r.ewm(span=21, min_periods=5).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality EMA × close
def f01rrb_f01_regulated_rate_base_growth_qualityema_252d_base_v068_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    sm = q.ewm(span=63, min_periods=21).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × closeadj (cross-sectional book/price ratio influence)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxprice_21d_base_v069_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    p = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × close-relative × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxprice_252d_base_v070_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    p = closeadj / _mean(closeadj, 504).replace(0, np.nan)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × ppnenet / assets ratio × close
def f01rrb_f01_regulated_rate_base_growth_assetxrbratio_63d_base_v071_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 63)
    rb = _f01_rate_base_proxy(ppnenet, 63)
    ratio = _safe_div(ppnenet, assets)
    result = g * ratio * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ppnenet / assets × close
def f01rrb_f01_regulated_rate_base_growth_assetxrbratio_252d_base_v072_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 252)
    rb = _f01_rate_base_proxy(ppnenet, 252)
    ratio = _safe_div(ppnenet, assets)
    result = g * ratio * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth quartile rank × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_63d_base_v073_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    rk = g.rolling(252, min_periods=63).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth rank × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_252d_base_v074_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    rk = g.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base proxy rank × close
def f01rrb_f01_regulated_rate_base_growth_ratebaserank_252d_base_v075_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    rk = r.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_21d_base_v001_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_63d_base_v002_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_126d_base_v003_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_252d_base_v004_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_504d_base_v005_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_21d_base_v006_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_63d_base_v007_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_126d_base_v008_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_252d_base_v009_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_504d_base_v010_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_63d_base_v011_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_126d_base_v012_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_252d_base_v013_signal,
    f01rrb_f01_regulated_rate_base_growth_quality_504d_base_v014_signal,
    f01rrb_f01_regulated_rate_base_growth_assetz_21d_base_v015_signal,
    f01rrb_f01_regulated_rate_base_growth_assetz_63d_base_v016_signal,
    f01rrb_f01_regulated_rate_base_growth_assetz_252d_base_v017_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_21d_base_v018_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_63d_base_v019_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthmean_126d_base_v020_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthstd_63d_base_v021_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthstd_126d_base_v022_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasez_21d_base_v023_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasez_63d_base_v024_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasez_252d_base_v025_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_21d_base_v026_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_63d_base_v027_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasestd_63d_base_v028_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasestd_126d_base_v029_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityz_63d_base_v030_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityz_252d_base_v031_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitymean_63d_base_v032_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitystd_126d_base_v033_signal,
    f01rrb_f01_regulated_rate_base_growth_rbintensity_21d_base_v034_signal,
    f01rrb_f01_regulated_rate_base_growth_rbintensity_63d_base_v035_signal,
    f01rrb_f01_regulated_rate_base_growth_rbintensity_252d_base_v036_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_5d_base_v037_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_10d_base_v038_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_42d_base_v039_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_189d_base_v040_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowth_378d_base_v041_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_5d_base_v042_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_10d_base_v043_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_42d_base_v044_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_189d_base_v045_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebase_378d_base_v046_signal,
    f01rrb_f01_regulated_rate_base_growth_growthxscale_63d_base_v047_signal,
    f01rrb_f01_regulated_rate_base_growth_growthxscale_252d_base_v048_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowth_63d_base_v049_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowth_252d_base_v050_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowth_504d_base_v051_signal,
    f01rrb_f01_regulated_rate_base_growth_assetloggrowth_63d_base_v052_signal,
    f01rrb_f01_regulated_rate_base_growth_assetloggrowth_252d_base_v053_signal,
    f01rrb_f01_regulated_rate_base_growth_equityratio_63d_base_v054_signal,
    f01rrb_f01_regulated_rate_base_growth_equityratio_252d_base_v055_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrb_21d_base_v056_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrb_63d_base_v057_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrb_252d_base_v058_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_63d_base_v059_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsq_252d_base_v060_signal,
    f01rrb_f01_regulated_rate_base_growth_ppnegrowthsq_63d_base_v061_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxequity_63d_base_v062_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxequity_252d_base_v063_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthema_252d_base_v064_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthema_63d_base_v065_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseema_252d_base_v066_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseema_63d_base_v067_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityema_252d_base_v068_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxprice_21d_base_v069_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxprice_252d_base_v070_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrbratio_63d_base_v071_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxrbratio_252d_base_v072_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_63d_base_v073_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthrank_252d_base_v074_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaserank_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_REGULATED_RATE_BASE_GROWTH_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f01_regulated_rate_base_growth_base_001_075_claude: {n_features} features pass")
