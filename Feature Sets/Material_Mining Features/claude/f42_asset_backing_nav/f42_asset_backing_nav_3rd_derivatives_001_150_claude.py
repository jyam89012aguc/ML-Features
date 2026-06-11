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


def _tb(equity, intangibles):
    return equity - intangibles


# jerk raw pb 21d
def f42nb_f42_asset_backing_nav_pbraw_21d_jerk_v001_signal(pb):
    q = pb
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pb 63d
def f42nb_f42_asset_backing_nav_pblogslope_63d_jerk_v002_signal(pb):
    q = pb
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pb 126d
def f42nb_f42_asset_backing_nav_pbrsslope_126d_jerk_v003_signal(pb):
    q = pb
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pb 63d
def f42nb_f42_asset_backing_nav_pbzslope_63d_jerk_v004_signal(pb):
    q = pb
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pb 42d
def f42nb_f42_asset_backing_nav_pbmacdslope_42d_jerk_v005_signal(pb):
    q = pb
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbproxy 21d
def f42nb_f42_asset_backing_nav_pbproxyraw_21d_jerk_v006_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbproxy 63d
def f42nb_f42_asset_backing_nav_pbproxylogslope_63d_jerk_v007_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbproxy 126d
def f42nb_f42_asset_backing_nav_pbproxyrsslope_126d_jerk_v008_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbproxy 63d
def f42nb_f42_asset_backing_nav_pbproxyzslope_63d_jerk_v009_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbproxy 42d
def f42nb_f42_asset_backing_nav_pbproxymacdslope_42d_jerk_v010_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw ptbtang 21d
def f42nb_f42_asset_backing_nav_ptbtangraw_21d_jerk_v011_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope ptbtang 63d
def f42nb_f42_asset_backing_nav_ptbtanglogslope_63d_jerk_v012_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope ptbtang 126d
def f42nb_f42_asset_backing_nav_ptbtangrsslope_126d_jerk_v013_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope ptbtang 63d
def f42nb_f42_asset_backing_nav_ptbtangzslope_63d_jerk_v014_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope ptbtang 42d
def f42nb_f42_asset_backing_nav_ptbtangmacdslope_42d_jerk_v015_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw priceassets 21d
def f42nb_f42_asset_backing_nav_priceassetsraw_21d_jerk_v016_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope priceassets 63d
def f42nb_f42_asset_backing_nav_priceassetslogslope_63d_jerk_v017_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope priceassets 126d
def f42nb_f42_asset_backing_nav_priceassetsrsslope_126d_jerk_v018_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope priceassets 63d
def f42nb_f42_asset_backing_nav_priceassetszslope_63d_jerk_v019_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope priceassets 42d
def f42nb_f42_asset_backing_nav_priceassetsmacdslope_42d_jerk_v020_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbpriceassets 21d
def f42nb_f42_asset_backing_nav_pbpriceassetsraw_21d_jerk_v021_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbpriceassets 63d
def f42nb_f42_asset_backing_nav_pbpriceassetslogslope_63d_jerk_v022_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbpriceassets 126d
def f42nb_f42_asset_backing_nav_pbpriceassetsrsslope_126d_jerk_v023_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbpriceassets 63d
def f42nb_f42_asset_backing_nav_pbpriceassetszslope_63d_jerk_v024_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbpriceassets 42d
def f42nb_f42_asset_backing_nav_pbpriceassetsmacdslope_42d_jerk_v025_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tangshare 21d
def f42nb_f42_asset_backing_nav_tangshareraw_21d_jerk_v026_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tangshare 63d
def f42nb_f42_asset_backing_nav_tangsharelogslope_63d_jerk_v027_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tangshare 126d
def f42nb_f42_asset_backing_nav_tangsharersslope_126d_jerk_v028_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tangshare 63d
def f42nb_f42_asset_backing_nav_tangsharezslope_63d_jerk_v029_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tangshare 42d
def f42nb_f42_asset_backing_nav_tangsharemacdslope_42d_jerk_v030_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw eqassets 21d
def f42nb_f42_asset_backing_nav_eqassetsraw_21d_jerk_v031_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope eqassets 63d
def f42nb_f42_asset_backing_nav_eqassetslogslope_63d_jerk_v032_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope eqassets 126d
def f42nb_f42_asset_backing_nav_eqassetsrsslope_126d_jerk_v033_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope eqassets 63d
def f42nb_f42_asset_backing_nav_eqassetszslope_63d_jerk_v034_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope eqassets 42d
def f42nb_f42_asset_backing_nav_eqassetsmacdslope_42d_jerk_v035_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw intangdrag 21d
def f42nb_f42_asset_backing_nav_intangdragraw_21d_jerk_v036_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope intangdrag 63d
def f42nb_f42_asset_backing_nav_intangdraglogslope_63d_jerk_v037_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope intangdrag 126d
def f42nb_f42_asset_backing_nav_intangdragrsslope_126d_jerk_v038_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope intangdrag 63d
def f42nb_f42_asset_backing_nav_intangdragzslope_63d_jerk_v039_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope intangdrag 42d
def f42nb_f42_asset_backing_nav_intangdragmacdslope_42d_jerk_v040_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw intangassets 21d
def f42nb_f42_asset_backing_nav_intangassetsraw_21d_jerk_v041_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope intangassets 63d
def f42nb_f42_asset_backing_nav_intangassetslogslope_63d_jerk_v042_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope intangassets 126d
def f42nb_f42_asset_backing_nav_intangassetsrsslope_126d_jerk_v043_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope intangassets 63d
def f42nb_f42_asset_backing_nav_intangassetszslope_63d_jerk_v044_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope intangassets 42d
def f42nb_f42_asset_backing_nav_intangassetsmacdslope_42d_jerk_v045_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tangeq 21d
def f42nb_f42_asset_backing_nav_tangeqraw_21d_jerk_v046_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tangeq 63d
def f42nb_f42_asset_backing_nav_tangeqlogslope_63d_jerk_v047_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tangeq 126d
def f42nb_f42_asset_backing_nav_tangeqrsslope_126d_jerk_v048_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tangeq 63d
def f42nb_f42_asset_backing_nav_tangeqzslope_63d_jerk_v049_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tangeq 42d
def f42nb_f42_asset_backing_nav_tangeqmacdslope_42d_jerk_v050_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw softhard 21d
def f42nb_f42_asset_backing_nav_softhardraw_21d_jerk_v051_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope softhard 63d
def f42nb_f42_asset_backing_nav_softhardlogslope_63d_jerk_v052_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope softhard 126d
def f42nb_f42_asset_backing_nav_softhardrsslope_126d_jerk_v053_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope softhard 63d
def f42nb_f42_asset_backing_nav_softhardzslope_63d_jerk_v054_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope softhard 42d
def f42nb_f42_asset_backing_nav_softhardmacdslope_42d_jerk_v055_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbeqassets 21d
def f42nb_f42_asset_backing_nav_pbeqassetsraw_21d_jerk_v056_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbeqassets 63d
def f42nb_f42_asset_backing_nav_pbeqassetslogslope_63d_jerk_v057_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbeqassets 126d
def f42nb_f42_asset_backing_nav_pbeqassetsrsslope_126d_jerk_v058_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbeqassets 63d
def f42nb_f42_asset_backing_nav_pbeqassetszslope_63d_jerk_v059_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbeqassets 42d
def f42nb_f42_asset_backing_nav_pbeqassetsmacdslope_42d_jerk_v060_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tangeqshare 21d
def f42nb_f42_asset_backing_nav_tangeqshareraw_21d_jerk_v061_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tangeqshare 63d
def f42nb_f42_asset_backing_nav_tangeqsharelogslope_63d_jerk_v062_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tangeqshare 126d
def f42nb_f42_asset_backing_nav_tangeqsharersslope_126d_jerk_v063_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tangeqshare 63d
def f42nb_f42_asset_backing_nav_tangeqsharezslope_63d_jerk_v064_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tangeqshare 42d
def f42nb_f42_asset_backing_nav_tangeqsharemacdslope_42d_jerk_v065_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbpaspread 21d
def f42nb_f42_asset_backing_nav_pbpaspreadraw_21d_jerk_v066_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbpaspread 63d
def f42nb_f42_asset_backing_nav_pbpaspreadlogslope_63d_jerk_v067_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbpaspread 126d
def f42nb_f42_asset_backing_nav_pbpaspreadrsslope_126d_jerk_v068_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbpaspread 63d
def f42nb_f42_asset_backing_nav_pbpaspreadzslope_63d_jerk_v069_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbpaspread 42d
def f42nb_f42_asset_backing_nav_pbpaspreadmacdslope_42d_jerk_v070_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbptbwedge 21d
def f42nb_f42_asset_backing_nav_pbptbwedgeraw_21d_jerk_v071_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbptbwedge 63d
def f42nb_f42_asset_backing_nav_pbptbwedgelogslope_63d_jerk_v072_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbptbwedge 126d
def f42nb_f42_asset_backing_nav_pbptbwedgersslope_126d_jerk_v073_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbptbwedge 63d
def f42nb_f42_asset_backing_nav_pbptbwedgezslope_63d_jerk_v074_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbptbwedge 42d
def f42nb_f42_asset_backing_nav_pbptbwedgemacdslope_42d_jerk_v075_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw softoverhang 21d
def f42nb_f42_asset_backing_nav_softoverhangraw_21d_jerk_v076_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope softoverhang 63d
def f42nb_f42_asset_backing_nav_softoverhanglogslope_63d_jerk_v077_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope softoverhang 126d
def f42nb_f42_asset_backing_nav_softoverhangrsslope_126d_jerk_v078_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope softoverhang 63d
def f42nb_f42_asset_backing_nav_softoverhangzslope_63d_jerk_v079_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope softoverhang 42d
def f42nb_f42_asset_backing_nav_softoverhangmacdslope_42d_jerk_v080_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tccusha 21d
def f42nb_f42_asset_backing_nav_tccusharaw_21d_jerk_v081_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tccusha 63d
def f42nb_f42_asset_backing_nav_tccushalogslope_63d_jerk_v082_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tccusha 126d
def f42nb_f42_asset_backing_nav_tccusharsslope_126d_jerk_v083_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tccusha 63d
def f42nb_f42_asset_backing_nav_tccushazslope_63d_jerk_v084_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tccusha 42d
def f42nb_f42_asset_backing_nav_tccushamacdslope_42d_jerk_v085_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw paeqassets 21d
def f42nb_f42_asset_backing_nav_paeqassetsraw_21d_jerk_v086_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope paeqassets 63d
def f42nb_f42_asset_backing_nav_paeqassetslogslope_63d_jerk_v087_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope paeqassets 126d
def f42nb_f42_asset_backing_nav_paeqassetsrsslope_126d_jerk_v088_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope paeqassets 63d
def f42nb_f42_asset_backing_nav_paeqassetszslope_63d_jerk_v089_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope paeqassets 42d
def f42nb_f42_asset_backing_nav_paeqassetsmacdslope_42d_jerk_v090_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbtangcover 21d
def f42nb_f42_asset_backing_nav_pbtangcoverraw_21d_jerk_v091_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbtangcover 63d
def f42nb_f42_asset_backing_nav_pbtangcoverlogslope_63d_jerk_v092_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbtangcover 126d
def f42nb_f42_asset_backing_nav_pbtangcoverrsslope_126d_jerk_v093_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbtangcover 63d
def f42nb_f42_asset_backing_nav_pbtangcoverzslope_63d_jerk_v094_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbtangcover 42d
def f42nb_f42_asset_backing_nav_pbtangcovermacdslope_42d_jerk_v095_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw liabintang 21d
def f42nb_f42_asset_backing_nav_liabintangraw_21d_jerk_v096_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope liabintang 63d
def f42nb_f42_asset_backing_nav_liabintanglogslope_63d_jerk_v097_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope liabintang 126d
def f42nb_f42_asset_backing_nav_liabintangrsslope_126d_jerk_v098_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope liabintang 63d
def f42nb_f42_asset_backing_nav_liabintangzslope_63d_jerk_v099_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope liabintang 42d
def f42nb_f42_asset_backing_nav_liabintangmacdslope_42d_jerk_v100_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbtangshare 21d
def f42nb_f42_asset_backing_nav_pbtangshareraw_21d_jerk_v101_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbtangshare 63d
def f42nb_f42_asset_backing_nav_pbtangsharelogslope_63d_jerk_v102_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbtangshare 126d
def f42nb_f42_asset_backing_nav_pbtangsharersslope_126d_jerk_v103_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbtangshare 63d
def f42nb_f42_asset_backing_nav_pbtangsharezslope_63d_jerk_v104_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbtangshare 42d
def f42nb_f42_asset_backing_nav_pbtangsharemacdslope_42d_jerk_v105_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw byeqassets 21d
def f42nb_f42_asset_backing_nav_byeqassetsraw_21d_jerk_v106_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope byeqassets 63d
def f42nb_f42_asset_backing_nav_byeqassetslogslope_63d_jerk_v107_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope byeqassets 126d
def f42nb_f42_asset_backing_nav_byeqassetsrsslope_126d_jerk_v108_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope byeqassets 63d
def f42nb_f42_asset_backing_nav_byeqassetszslope_63d_jerk_v109_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope byeqassets 42d
def f42nb_f42_asset_backing_nav_byeqassetsmacdslope_42d_jerk_v110_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tangcovshare 21d
def f42nb_f42_asset_backing_nav_tangcovshareraw_21d_jerk_v111_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tangcovshare 63d
def f42nb_f42_asset_backing_nav_tangcovsharelogslope_63d_jerk_v112_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tangcovshare 126d
def f42nb_f42_asset_backing_nav_tangcovsharersslope_126d_jerk_v113_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tangcovshare 63d
def f42nb_f42_asset_backing_nav_tangcovsharezslope_63d_jerk_v114_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tangcovshare 42d
def f42nb_f42_asset_backing_nav_tangcovsharemacdslope_42d_jerk_v115_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw paintang 21d
def f42nb_f42_asset_backing_nav_paintangraw_21d_jerk_v116_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope paintang 63d
def f42nb_f42_asset_backing_nav_paintanglogslope_63d_jerk_v117_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope paintang 126d
def f42nb_f42_asset_backing_nav_paintangrsslope_126d_jerk_v118_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope paintang 63d
def f42nb_f42_asset_backing_nav_paintangzslope_63d_jerk_v119_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope paintang 42d
def f42nb_f42_asset_backing_nav_paintangmacdslope_42d_jerk_v120_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbintang 21d
def f42nb_f42_asset_backing_nav_pbintangraw_21d_jerk_v121_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbintang 63d
def f42nb_f42_asset_backing_nav_pbintanglogslope_63d_jerk_v122_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbintang 126d
def f42nb_f42_asset_backing_nav_pbintangrsslope_126d_jerk_v123_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbintang 63d
def f42nb_f42_asset_backing_nav_pbintangzslope_63d_jerk_v124_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbintang 42d
def f42nb_f42_asset_backing_nav_pbintangmacdslope_42d_jerk_v125_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw eqmcassets 21d
def f42nb_f42_asset_backing_nav_eqmcassetsraw_21d_jerk_v126_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope eqmcassets 63d
def f42nb_f42_asset_backing_nav_eqmcassetslogslope_63d_jerk_v127_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope eqmcassets 126d
def f42nb_f42_asset_backing_nav_eqmcassetsrsslope_126d_jerk_v128_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope eqmcassets 63d
def f42nb_f42_asset_backing_nav_eqmcassetszslope_63d_jerk_v129_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope eqmcassets 42d
def f42nb_f42_asset_backing_nav_eqmcassetsmacdslope_42d_jerk_v130_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw tbminuspb 21d
def f42nb_f42_asset_backing_nav_tbminuspbraw_21d_jerk_v131_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope tbminuspb 63d
def f42nb_f42_asset_backing_nav_tbminuspblogslope_63d_jerk_v132_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope tbminuspb 126d
def f42nb_f42_asset_backing_nav_tbminuspbrsslope_126d_jerk_v133_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope tbminuspb 63d
def f42nb_f42_asset_backing_nav_tbminuspbzslope_63d_jerk_v134_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope tbminuspb 42d
def f42nb_f42_asset_backing_nav_tbminuspbmacdslope_42d_jerk_v135_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw byintangdrag 21d
def f42nb_f42_asset_backing_nav_byintangdragraw_21d_jerk_v136_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope byintangdrag 63d
def f42nb_f42_asset_backing_nav_byintangdraglogslope_63d_jerk_v137_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope byintangdrag 126d
def f42nb_f42_asset_backing_nav_byintangdragrsslope_126d_jerk_v138_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope byintangdrag 63d
def f42nb_f42_asset_backing_nav_byintangdragzslope_63d_jerk_v139_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope byintangdrag 42d
def f42nb_f42_asset_backing_nav_byintangdragmacdslope_42d_jerk_v140_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw pbintangassets 21d
def f42nb_f42_asset_backing_nav_pbintangassetsraw_21d_jerk_v141_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope pbintangassets 63d
def f42nb_f42_asset_backing_nav_pbintangassetslogslope_63d_jerk_v142_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope pbintangassets 126d
def f42nb_f42_asset_backing_nav_pbintangassetsrsslope_126d_jerk_v143_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope pbintangassets 63d
def f42nb_f42_asset_backing_nav_pbintangassetszslope_63d_jerk_v144_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope pbintangassets 42d
def f42nb_f42_asset_backing_nav_pbintangassetsmacdslope_42d_jerk_v145_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk raw intangmcpb 21d
def f42nb_f42_asset_backing_nav_intangmcpbraw_21d_jerk_v146_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    s1 = (q - q.shift(21)) / 21.0
    s2 = (s1 - s1.shift(21)) / 21.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk logslope intangmcpb 63d
def f42nb_f42_asset_backing_nav_intangmcpblogslope_63d_jerk_v147_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    s1 = (lq - lq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk rsslope intangmcpb 126d
def f42nb_f42_asset_backing_nav_intangmcpbrsslope_126d_jerk_v148_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    d = (q - q.shift(126)) / 126.0
    a = (d - d.shift(126)) / 126.0
    result = a / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# jerk zslope intangmcpb 63d
def f42nb_f42_asset_backing_nav_intangmcpbzslope_63d_jerk_v149_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    zq = _z(q, 252)
    s1 = (zq - zq.shift(63)) / 63.0
    s2 = (s1 - s1.shift(63)) / 63.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
# jerk macdslope intangmcpb 42d
def f42nb_f42_asset_backing_nav_intangmcpbmacdslope_42d_jerk_v150_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    s1 = (spread - spread.shift(42)) / 42.0
    s2 = (s1 - s1.shift(42)) / 42.0
    result = s2
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f42nb_f42_asset_backing_nav_pbraw_21d_jerk_v001_signal,
    f42nb_f42_asset_backing_nav_pblogslope_63d_jerk_v002_signal,
    f42nb_f42_asset_backing_nav_pbrsslope_126d_jerk_v003_signal,
    f42nb_f42_asset_backing_nav_pbzslope_63d_jerk_v004_signal,
    f42nb_f42_asset_backing_nav_pbmacdslope_42d_jerk_v005_signal,
    f42nb_f42_asset_backing_nav_pbproxyraw_21d_jerk_v006_signal,
    f42nb_f42_asset_backing_nav_pbproxylogslope_63d_jerk_v007_signal,
    f42nb_f42_asset_backing_nav_pbproxyrsslope_126d_jerk_v008_signal,
    f42nb_f42_asset_backing_nav_pbproxyzslope_63d_jerk_v009_signal,
    f42nb_f42_asset_backing_nav_pbproxymacdslope_42d_jerk_v010_signal,
    f42nb_f42_asset_backing_nav_ptbtangraw_21d_jerk_v011_signal,
    f42nb_f42_asset_backing_nav_ptbtanglogslope_63d_jerk_v012_signal,
    f42nb_f42_asset_backing_nav_ptbtangrsslope_126d_jerk_v013_signal,
    f42nb_f42_asset_backing_nav_ptbtangzslope_63d_jerk_v014_signal,
    f42nb_f42_asset_backing_nav_ptbtangmacdslope_42d_jerk_v015_signal,
    f42nb_f42_asset_backing_nav_priceassetsraw_21d_jerk_v016_signal,
    f42nb_f42_asset_backing_nav_priceassetslogslope_63d_jerk_v017_signal,
    f42nb_f42_asset_backing_nav_priceassetsrsslope_126d_jerk_v018_signal,
    f42nb_f42_asset_backing_nav_priceassetszslope_63d_jerk_v019_signal,
    f42nb_f42_asset_backing_nav_priceassetsmacdslope_42d_jerk_v020_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsraw_21d_jerk_v021_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetslogslope_63d_jerk_v022_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsrsslope_126d_jerk_v023_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetszslope_63d_jerk_v024_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsmacdslope_42d_jerk_v025_signal,
    f42nb_f42_asset_backing_nav_tangshareraw_21d_jerk_v026_signal,
    f42nb_f42_asset_backing_nav_tangsharelogslope_63d_jerk_v027_signal,
    f42nb_f42_asset_backing_nav_tangsharersslope_126d_jerk_v028_signal,
    f42nb_f42_asset_backing_nav_tangsharezslope_63d_jerk_v029_signal,
    f42nb_f42_asset_backing_nav_tangsharemacdslope_42d_jerk_v030_signal,
    f42nb_f42_asset_backing_nav_eqassetsraw_21d_jerk_v031_signal,
    f42nb_f42_asset_backing_nav_eqassetslogslope_63d_jerk_v032_signal,
    f42nb_f42_asset_backing_nav_eqassetsrsslope_126d_jerk_v033_signal,
    f42nb_f42_asset_backing_nav_eqassetszslope_63d_jerk_v034_signal,
    f42nb_f42_asset_backing_nav_eqassetsmacdslope_42d_jerk_v035_signal,
    f42nb_f42_asset_backing_nav_intangdragraw_21d_jerk_v036_signal,
    f42nb_f42_asset_backing_nav_intangdraglogslope_63d_jerk_v037_signal,
    f42nb_f42_asset_backing_nav_intangdragrsslope_126d_jerk_v038_signal,
    f42nb_f42_asset_backing_nav_intangdragzslope_63d_jerk_v039_signal,
    f42nb_f42_asset_backing_nav_intangdragmacdslope_42d_jerk_v040_signal,
    f42nb_f42_asset_backing_nav_intangassetsraw_21d_jerk_v041_signal,
    f42nb_f42_asset_backing_nav_intangassetslogslope_63d_jerk_v042_signal,
    f42nb_f42_asset_backing_nav_intangassetsrsslope_126d_jerk_v043_signal,
    f42nb_f42_asset_backing_nav_intangassetszslope_63d_jerk_v044_signal,
    f42nb_f42_asset_backing_nav_intangassetsmacdslope_42d_jerk_v045_signal,
    f42nb_f42_asset_backing_nav_tangeqraw_21d_jerk_v046_signal,
    f42nb_f42_asset_backing_nav_tangeqlogslope_63d_jerk_v047_signal,
    f42nb_f42_asset_backing_nav_tangeqrsslope_126d_jerk_v048_signal,
    f42nb_f42_asset_backing_nav_tangeqzslope_63d_jerk_v049_signal,
    f42nb_f42_asset_backing_nav_tangeqmacdslope_42d_jerk_v050_signal,
    f42nb_f42_asset_backing_nav_softhardraw_21d_jerk_v051_signal,
    f42nb_f42_asset_backing_nav_softhardlogslope_63d_jerk_v052_signal,
    f42nb_f42_asset_backing_nav_softhardrsslope_126d_jerk_v053_signal,
    f42nb_f42_asset_backing_nav_softhardzslope_63d_jerk_v054_signal,
    f42nb_f42_asset_backing_nav_softhardmacdslope_42d_jerk_v055_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsraw_21d_jerk_v056_signal,
    f42nb_f42_asset_backing_nav_pbeqassetslogslope_63d_jerk_v057_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsrsslope_126d_jerk_v058_signal,
    f42nb_f42_asset_backing_nav_pbeqassetszslope_63d_jerk_v059_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsmacdslope_42d_jerk_v060_signal,
    f42nb_f42_asset_backing_nav_tangeqshareraw_21d_jerk_v061_signal,
    f42nb_f42_asset_backing_nav_tangeqsharelogslope_63d_jerk_v062_signal,
    f42nb_f42_asset_backing_nav_tangeqsharersslope_126d_jerk_v063_signal,
    f42nb_f42_asset_backing_nav_tangeqsharezslope_63d_jerk_v064_signal,
    f42nb_f42_asset_backing_nav_tangeqsharemacdslope_42d_jerk_v065_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadraw_21d_jerk_v066_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadlogslope_63d_jerk_v067_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadrsslope_126d_jerk_v068_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadzslope_63d_jerk_v069_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadmacdslope_42d_jerk_v070_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgeraw_21d_jerk_v071_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgelogslope_63d_jerk_v072_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgersslope_126d_jerk_v073_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgezslope_63d_jerk_v074_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgemacdslope_42d_jerk_v075_signal,
    f42nb_f42_asset_backing_nav_softoverhangraw_21d_jerk_v076_signal,
    f42nb_f42_asset_backing_nav_softoverhanglogslope_63d_jerk_v077_signal,
    f42nb_f42_asset_backing_nav_softoverhangrsslope_126d_jerk_v078_signal,
    f42nb_f42_asset_backing_nav_softoverhangzslope_63d_jerk_v079_signal,
    f42nb_f42_asset_backing_nav_softoverhangmacdslope_42d_jerk_v080_signal,
    f42nb_f42_asset_backing_nav_tccusharaw_21d_jerk_v081_signal,
    f42nb_f42_asset_backing_nav_tccushalogslope_63d_jerk_v082_signal,
    f42nb_f42_asset_backing_nav_tccusharsslope_126d_jerk_v083_signal,
    f42nb_f42_asset_backing_nav_tccushazslope_63d_jerk_v084_signal,
    f42nb_f42_asset_backing_nav_tccushamacdslope_42d_jerk_v085_signal,
    f42nb_f42_asset_backing_nav_paeqassetsraw_21d_jerk_v086_signal,
    f42nb_f42_asset_backing_nav_paeqassetslogslope_63d_jerk_v087_signal,
    f42nb_f42_asset_backing_nav_paeqassetsrsslope_126d_jerk_v088_signal,
    f42nb_f42_asset_backing_nav_paeqassetszslope_63d_jerk_v089_signal,
    f42nb_f42_asset_backing_nav_paeqassetsmacdslope_42d_jerk_v090_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverraw_21d_jerk_v091_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverlogslope_63d_jerk_v092_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverrsslope_126d_jerk_v093_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverzslope_63d_jerk_v094_signal,
    f42nb_f42_asset_backing_nav_pbtangcovermacdslope_42d_jerk_v095_signal,
    f42nb_f42_asset_backing_nav_liabintangraw_21d_jerk_v096_signal,
    f42nb_f42_asset_backing_nav_liabintanglogslope_63d_jerk_v097_signal,
    f42nb_f42_asset_backing_nav_liabintangrsslope_126d_jerk_v098_signal,
    f42nb_f42_asset_backing_nav_liabintangzslope_63d_jerk_v099_signal,
    f42nb_f42_asset_backing_nav_liabintangmacdslope_42d_jerk_v100_signal,
    f42nb_f42_asset_backing_nav_pbtangshareraw_21d_jerk_v101_signal,
    f42nb_f42_asset_backing_nav_pbtangsharelogslope_63d_jerk_v102_signal,
    f42nb_f42_asset_backing_nav_pbtangsharersslope_126d_jerk_v103_signal,
    f42nb_f42_asset_backing_nav_pbtangsharezslope_63d_jerk_v104_signal,
    f42nb_f42_asset_backing_nav_pbtangsharemacdslope_42d_jerk_v105_signal,
    f42nb_f42_asset_backing_nav_byeqassetsraw_21d_jerk_v106_signal,
    f42nb_f42_asset_backing_nav_byeqassetslogslope_63d_jerk_v107_signal,
    f42nb_f42_asset_backing_nav_byeqassetsrsslope_126d_jerk_v108_signal,
    f42nb_f42_asset_backing_nav_byeqassetszslope_63d_jerk_v109_signal,
    f42nb_f42_asset_backing_nav_byeqassetsmacdslope_42d_jerk_v110_signal,
    f42nb_f42_asset_backing_nav_tangcovshareraw_21d_jerk_v111_signal,
    f42nb_f42_asset_backing_nav_tangcovsharelogslope_63d_jerk_v112_signal,
    f42nb_f42_asset_backing_nav_tangcovsharersslope_126d_jerk_v113_signal,
    f42nb_f42_asset_backing_nav_tangcovsharezslope_63d_jerk_v114_signal,
    f42nb_f42_asset_backing_nav_tangcovsharemacdslope_42d_jerk_v115_signal,
    f42nb_f42_asset_backing_nav_paintangraw_21d_jerk_v116_signal,
    f42nb_f42_asset_backing_nav_paintanglogslope_63d_jerk_v117_signal,
    f42nb_f42_asset_backing_nav_paintangrsslope_126d_jerk_v118_signal,
    f42nb_f42_asset_backing_nav_paintangzslope_63d_jerk_v119_signal,
    f42nb_f42_asset_backing_nav_paintangmacdslope_42d_jerk_v120_signal,
    f42nb_f42_asset_backing_nav_pbintangraw_21d_jerk_v121_signal,
    f42nb_f42_asset_backing_nav_pbintanglogslope_63d_jerk_v122_signal,
    f42nb_f42_asset_backing_nav_pbintangrsslope_126d_jerk_v123_signal,
    f42nb_f42_asset_backing_nav_pbintangzslope_63d_jerk_v124_signal,
    f42nb_f42_asset_backing_nav_pbintangmacdslope_42d_jerk_v125_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsraw_21d_jerk_v126_signal,
    f42nb_f42_asset_backing_nav_eqmcassetslogslope_63d_jerk_v127_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsrsslope_126d_jerk_v128_signal,
    f42nb_f42_asset_backing_nav_eqmcassetszslope_63d_jerk_v129_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsmacdslope_42d_jerk_v130_signal,
    f42nb_f42_asset_backing_nav_tbminuspbraw_21d_jerk_v131_signal,
    f42nb_f42_asset_backing_nav_tbminuspblogslope_63d_jerk_v132_signal,
    f42nb_f42_asset_backing_nav_tbminuspbrsslope_126d_jerk_v133_signal,
    f42nb_f42_asset_backing_nav_tbminuspbzslope_63d_jerk_v134_signal,
    f42nb_f42_asset_backing_nav_tbminuspbmacdslope_42d_jerk_v135_signal,
    f42nb_f42_asset_backing_nav_byintangdragraw_21d_jerk_v136_signal,
    f42nb_f42_asset_backing_nav_byintangdraglogslope_63d_jerk_v137_signal,
    f42nb_f42_asset_backing_nav_byintangdragrsslope_126d_jerk_v138_signal,
    f42nb_f42_asset_backing_nav_byintangdragzslope_63d_jerk_v139_signal,
    f42nb_f42_asset_backing_nav_byintangdragmacdslope_42d_jerk_v140_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsraw_21d_jerk_v141_signal,
    f42nb_f42_asset_backing_nav_pbintangassetslogslope_63d_jerk_v142_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsrsslope_126d_jerk_v143_signal,
    f42nb_f42_asset_backing_nav_pbintangassetszslope_63d_jerk_v144_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsmacdslope_42d_jerk_v145_signal,
    f42nb_f42_asset_backing_nav_intangmcpbraw_21d_jerk_v146_signal,
    f42nb_f42_asset_backing_nav_intangmcpblogslope_63d_jerk_v147_signal,
    f42nb_f42_asset_backing_nav_intangmcpbrsslope_126d_jerk_v148_signal,
    f42nb_f42_asset_backing_nav_intangmcpbzslope_63d_jerk_v149_signal,
    f42nb_f42_asset_backing_nav_intangmcpbmacdslope_42d_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_ASSET_BACKING_NAV_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.5
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    pb = _fund(101, base=1.5, drift=0.0, vol=0.10).clip(lower=0.3, upper=5.0).rename("pb")
    marketcap = _fund(102, base=5e8, drift=0.0, vol=0.09).clip(lower=1e6).rename("marketcap")
    equity = _fund(103, base=4e8, drift=0.0, vol=0.08).clip(lower=1e6).rename("equity")
    assets = _fund(104, base=9e8, drift=0.0, vol=0.07).clip(lower=2e6).rename("assets")
    tangibles = _fund(105, base=6e8, drift=0.0, vol=0.075).clip(lower=1e6).rename("tangibles")
    tangibles = pd.Series(np.minimum(tangibles.values, assets.values * 0.97), name="tangibles")
    intangibles = _fund(106, base=1.2e8, drift=0.0, vol=0.085).clip(lower=1e5).rename("intangibles")
    intangibles = pd.Series(np.minimum(intangibles.values, equity.values * 0.9), name="intangibles")

    cols = {"pb": pb, "marketcap": marketcap, "equity": equity,
            "tangibles": tangibles, "intangibles": intangibles, "assets": assets}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
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

    print("OK f42_asset_backing_nav_3rd_derivatives_001_150_claude: %d features pass" % n_features)
