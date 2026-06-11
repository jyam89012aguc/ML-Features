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


# slope (raw) of P/B multiple (window 21d)
def f42nb_f42_asset_backing_nav_pbraw_21d_slope_v001_signal(pb):
    q = pb
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B multiple (window 63d)
def f42nb_f42_asset_backing_nav_pblogslope_63d_slope_v002_signal(pb):
    q = pb
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B multiple (window 126d)
def f42nb_f42_asset_backing_nav_pbrsslope_126d_slope_v003_signal(pb):
    q = pb
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B multiple (window 63d)
def f42nb_f42_asset_backing_nav_pbzslope_63d_slope_v004_signal(pb):
    q = pb
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B multiple (window 42d)
def f42nb_f42_asset_backing_nav_pbmacdslope_42d_slope_v005_signal(pb):
    q = pb
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B proxy marketcap/equity (M-E) (window 21d)
def f42nb_f42_asset_backing_nav_pbproxyraw_21d_slope_v006_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B proxy marketcap/equity (M-E) (window 63d)
def f42nb_f42_asset_backing_nav_pbproxylogslope_63d_slope_v007_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B proxy marketcap/equity (M-E) (window 126d)
def f42nb_f42_asset_backing_nav_pbproxyrsslope_126d_slope_v008_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B proxy marketcap/equity (M-E) (window 63d)
def f42nb_f42_asset_backing_nav_pbproxyzslope_63d_slope_v009_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B proxy marketcap/equity (M-E) (window 42d)
def f42nb_f42_asset_backing_nav_pbproxymacdslope_42d_slope_v010_signal(marketcap, equity):
    q = marketcap / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of price-to-tangible-assets marketcap/tangibles (M-T) (window 21d)
def f42nb_f42_asset_backing_nav_ptbtangraw_21d_slope_v011_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of price-to-tangible-assets marketcap/tangibles (M-T) (window 63d)
def f42nb_f42_asset_backing_nav_ptbtanglogslope_63d_slope_v012_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of price-to-tangible-assets marketcap/tangibles (M-T) (window 126d)
def f42nb_f42_asset_backing_nav_ptbtangrsslope_126d_slope_v013_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of price-to-tangible-assets marketcap/tangibles (M-T) (window 63d)
def f42nb_f42_asset_backing_nav_ptbtangzslope_63d_slope_v014_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of price-to-tangible-assets marketcap/tangibles (M-T) (window 42d)
def f42nb_f42_asset_backing_nav_ptbtangmacdslope_42d_slope_v015_signal(marketcap, tangibles):
    q = marketcap / tangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of price-to-gross-assets (M-A) (window 21d)
def f42nb_f42_asset_backing_nav_priceassetsraw_21d_slope_v016_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of price-to-gross-assets (M-A) (window 63d)
def f42nb_f42_asset_backing_nav_priceassetslogslope_63d_slope_v017_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of price-to-gross-assets (M-A) (window 126d)
def f42nb_f42_asset_backing_nav_priceassetsrsslope_126d_slope_v018_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of price-to-gross-assets (M-A) (window 63d)
def f42nb_f42_asset_backing_nav_priceassetszslope_63d_slope_v019_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of price-to-gross-assets (M-A) (window 42d)
def f42nb_f42_asset_backing_nav_priceassetsmacdslope_42d_slope_v020_signal(marketcap, assets):
    q = marketcap / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times price-to-assets (multiple x asset-multiple) (window 21d)
def f42nb_f42_asset_backing_nav_pbpriceassetsraw_21d_slope_v021_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times price-to-assets (multiple x asset-multiple) (window 63d)
def f42nb_f42_asset_backing_nav_pbpriceassetslogslope_63d_slope_v022_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times price-to-assets (multiple x asset-multiple) (window 126d)
def f42nb_f42_asset_backing_nav_pbpriceassetsrsslope_126d_slope_v023_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times price-to-assets (multiple x asset-multiple) (window 63d)
def f42nb_f42_asset_backing_nav_pbpriceassetszslope_63d_slope_v024_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times price-to-assets (multiple x asset-multiple) (window 42d)
def f42nb_f42_asset_backing_nav_pbpriceassetsmacdslope_42d_slope_v025_signal(pb, marketcap, assets):
    q = pb * (marketcap / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible-asset share of assets (T-A) (window 21d)
def f42nb_f42_asset_backing_nav_tangshareraw_21d_slope_v026_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible-asset share of assets (T-A) (window 63d)
def f42nb_f42_asset_backing_nav_tangsharelogslope_63d_slope_v027_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible-asset share of assets (T-A) (window 126d)
def f42nb_f42_asset_backing_nav_tangsharersslope_126d_slope_v028_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible-asset share of assets (T-A) (window 63d)
def f42nb_f42_asset_backing_nav_tangsharezslope_63d_slope_v029_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible-asset share of assets (T-A) (window 42d)
def f42nb_f42_asset_backing_nav_tangsharemacdslope_42d_slope_v030_signal(tangibles, assets):
    q = tangibles / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of equity-to-assets cushion (E-A) (window 21d)
def f42nb_f42_asset_backing_nav_eqassetsraw_21d_slope_v031_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of equity-to-assets cushion (E-A) (window 63d)
def f42nb_f42_asset_backing_nav_eqassetslogslope_63d_slope_v032_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of equity-to-assets cushion (E-A) (window 126d)
def f42nb_f42_asset_backing_nav_eqassetsrsslope_126d_slope_v033_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of equity-to-assets cushion (E-A) (window 63d)
def f42nb_f42_asset_backing_nav_eqassetszslope_63d_slope_v034_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of equity-to-assets cushion (E-A) (window 42d)
def f42nb_f42_asset_backing_nav_eqassetsmacdslope_42d_slope_v035_signal(equity, assets):
    q = equity / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of intangibles share of equity (I-E) (window 21d)
def f42nb_f42_asset_backing_nav_intangdragraw_21d_slope_v036_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of intangibles share of equity (I-E) (window 63d)
def f42nb_f42_asset_backing_nav_intangdraglogslope_63d_slope_v037_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of intangibles share of equity (I-E) (window 126d)
def f42nb_f42_asset_backing_nav_intangdragrsslope_126d_slope_v038_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of intangibles share of equity (I-E) (window 63d)
def f42nb_f42_asset_backing_nav_intangdragzslope_63d_slope_v039_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of intangibles share of equity (I-E) (window 42d)
def f42nb_f42_asset_backing_nav_intangdragmacdslope_42d_slope_v040_signal(intangibles, equity):
    q = intangibles / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of intangibles share of assets (I-A) (window 21d)
def f42nb_f42_asset_backing_nav_intangassetsraw_21d_slope_v041_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of intangibles share of assets (I-A) (window 63d)
def f42nb_f42_asset_backing_nav_intangassetslogslope_63d_slope_v042_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of intangibles share of assets (I-A) (window 126d)
def f42nb_f42_asset_backing_nav_intangassetsrsslope_126d_slope_v043_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of intangibles share of assets (I-A) (window 63d)
def f42nb_f42_asset_backing_nav_intangassetszslope_63d_slope_v044_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of intangibles share of assets (I-A) (window 42d)
def f42nb_f42_asset_backing_nav_intangassetsmacdslope_42d_slope_v045_signal(intangibles, assets):
    q = intangibles / assets.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible assets over book equity (T-E) (window 21d)
def f42nb_f42_asset_backing_nav_tangeqraw_21d_slope_v046_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible assets over book equity (T-E) (window 63d)
def f42nb_f42_asset_backing_nav_tangeqlogslope_63d_slope_v047_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible assets over book equity (T-E) (window 126d)
def f42nb_f42_asset_backing_nav_tangeqrsslope_126d_slope_v048_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible assets over book equity (T-E) (window 63d)
def f42nb_f42_asset_backing_nav_tangeqzslope_63d_slope_v049_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible assets over book equity (T-E) (window 42d)
def f42nb_f42_asset_backing_nav_tangeqmacdslope_42d_slope_v050_signal(tangibles, equity):
    q = tangibles / equity.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of soft-to-hard asset mix (I-T) (window 21d)
def f42nb_f42_asset_backing_nav_softhardraw_21d_slope_v051_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of soft-to-hard asset mix (I-T) (window 63d)
def f42nb_f42_asset_backing_nav_softhardlogslope_63d_slope_v052_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of soft-to-hard asset mix (I-T) (window 126d)
def f42nb_f42_asset_backing_nav_softhardrsslope_126d_slope_v053_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of soft-to-hard asset mix (I-T) (window 63d)
def f42nb_f42_asset_backing_nav_softhardzslope_63d_slope_v054_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of soft-to-hard asset mix (I-T) (window 42d)
def f42nb_f42_asset_backing_nav_softhardmacdslope_42d_slope_v055_signal(intangibles, tangibles):
    q = intangibles / tangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times equity-to-assets (multiple x cushion) (window 21d)
def f42nb_f42_asset_backing_nav_pbeqassetsraw_21d_slope_v056_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times equity-to-assets (multiple x cushion) (window 63d)
def f42nb_f42_asset_backing_nav_pbeqassetslogslope_63d_slope_v057_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times equity-to-assets (multiple x cushion) (window 126d)
def f42nb_f42_asset_backing_nav_pbeqassetsrsslope_126d_slope_v058_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times equity-to-assets (multiple x cushion) (window 63d)
def f42nb_f42_asset_backing_nav_pbeqassetszslope_63d_slope_v059_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times equity-to-assets (multiple x cushion) (window 42d)
def f42nb_f42_asset_backing_nav_pbeqassetsmacdslope_42d_slope_v060_signal(pb, equity, assets):
    q = pb * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible-over-equity times tangible share (2T-E-A composite) (window 21d)
def f42nb_f42_asset_backing_nav_tangeqshareraw_21d_slope_v061_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible-over-equity times tangible share (2T-E-A composite) (window 63d)
def f42nb_f42_asset_backing_nav_tangeqsharelogslope_63d_slope_v062_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible-over-equity times tangible share (2T-E-A composite) (window 126d)
def f42nb_f42_asset_backing_nav_tangeqsharersslope_126d_slope_v063_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible-over-equity times tangible share (2T-E-A composite) (window 63d)
def f42nb_f42_asset_backing_nav_tangeqsharezslope_63d_slope_v064_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible-over-equity times tangible share (2T-E-A composite) (window 42d)
def f42nb_f42_asset_backing_nav_tangeqsharemacdslope_42d_slope_v065_signal(tangibles, equity, assets):
    q = (tangibles / equity.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B minus price-to-assets spread (window 21d)
def f42nb_f42_asset_backing_nav_pbpaspreadraw_21d_slope_v066_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B minus price-to-assets spread (window 63d)
def f42nb_f42_asset_backing_nav_pbpaspreadlogslope_63d_slope_v067_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B minus price-to-assets spread (window 126d)
def f42nb_f42_asset_backing_nav_pbpaspreadrsslope_126d_slope_v068_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B minus price-to-assets spread (window 63d)
def f42nb_f42_asset_backing_nav_pbpaspreadzslope_63d_slope_v069_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B minus price-to-assets spread (window 42d)
def f42nb_f42_asset_backing_nav_pbpaspreadmacdslope_42d_slope_v070_signal(pb, marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    q = pb - pa
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of price-to-tangible-book minus P/B wedge (window 21d)
def f42nb_f42_asset_backing_nav_pbptbwedgeraw_21d_slope_v071_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of price-to-tangible-book minus P/B wedge (window 63d)
def f42nb_f42_asset_backing_nav_pbptbwedgelogslope_63d_slope_v072_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of price-to-tangible-book minus P/B wedge (window 126d)
def f42nb_f42_asset_backing_nav_pbptbwedgersslope_126d_slope_v073_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of price-to-tangible-book minus P/B wedge (window 63d)
def f42nb_f42_asset_backing_nav_pbptbwedgezslope_63d_slope_v074_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of price-to-tangible-book minus P/B wedge (window 42d)
def f42nb_f42_asset_backing_nav_pbptbwedgemacdslope_42d_slope_v075_signal(marketcap, equity, intangibles):
    pbx = marketcap / equity.replace(0, np.nan)
    ptb = marketcap / (equity - intangibles).replace(0, np.nan)
    q = ptb - pbx
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of soft-asset overhang per market dollar (window 21d)
def f42nb_f42_asset_backing_nav_softoverhangraw_21d_slope_v076_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of soft-asset overhang per market dollar (window 63d)
def f42nb_f42_asset_backing_nav_softoverhanglogslope_63d_slope_v077_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of soft-asset overhang per market dollar (window 126d)
def f42nb_f42_asset_backing_nav_softoverhangrsslope_126d_slope_v078_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of soft-asset overhang per market dollar (window 63d)
def f42nb_f42_asset_backing_nav_softoverhangzslope_63d_slope_v079_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of soft-asset overhang per market dollar (window 42d)
def f42nb_f42_asset_backing_nav_softoverhangmacdslope_42d_slope_v080_signal(assets, tangibles, marketcap):
    q = (assets - tangibles) / marketcap.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible cover times equity-to-assets (hard-backing x cushion) (window 21d)
def f42nb_f42_asset_backing_nav_tccusharaw_21d_slope_v081_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible cover times equity-to-assets (hard-backing x cushion) (window 63d)
def f42nb_f42_asset_backing_nav_tccushalogslope_63d_slope_v082_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible cover times equity-to-assets (hard-backing x cushion) (window 126d)
def f42nb_f42_asset_backing_nav_tccusharsslope_126d_slope_v083_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible cover times equity-to-assets (hard-backing x cushion) (window 63d)
def f42nb_f42_asset_backing_nav_tccushazslope_63d_slope_v084_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible cover times equity-to-assets (hard-backing x cushion) (window 42d)
def f42nb_f42_asset_backing_nav_tccushamacdslope_42d_slope_v085_signal(tangibles, marketcap, equity, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of price-to-assets times equity-to-assets (M+E vs assets) (window 21d)
def f42nb_f42_asset_backing_nav_paeqassetsraw_21d_slope_v086_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of price-to-assets times equity-to-assets (M+E vs assets) (window 63d)
def f42nb_f42_asset_backing_nav_paeqassetslogslope_63d_slope_v087_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of price-to-assets times equity-to-assets (M+E vs assets) (window 126d)
def f42nb_f42_asset_backing_nav_paeqassetsrsslope_126d_slope_v088_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of price-to-assets times equity-to-assets (M+E vs assets) (window 63d)
def f42nb_f42_asset_backing_nav_paeqassetszslope_63d_slope_v089_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of price-to-assets times equity-to-assets (M+E vs assets) (window 42d)
def f42nb_f42_asset_backing_nav_paeqassetsmacdslope_42d_slope_v090_signal(marketcap, assets, equity):
    q = (marketcap / assets.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times tangible cover (multiple x hard backing) (window 21d)
def f42nb_f42_asset_backing_nav_pbtangcoverraw_21d_slope_v091_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times tangible cover (multiple x hard backing) (window 63d)
def f42nb_f42_asset_backing_nav_pbtangcoverlogslope_63d_slope_v092_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times tangible cover (multiple x hard backing) (window 126d)
def f42nb_f42_asset_backing_nav_pbtangcoverrsslope_126d_slope_v093_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times tangible cover (multiple x hard backing) (window 63d)
def f42nb_f42_asset_backing_nav_pbtangcoverzslope_63d_slope_v094_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times tangible cover (multiple x hard backing) (window 42d)
def f42nb_f42_asset_backing_nav_pbtangcovermacdslope_42d_slope_v095_signal(pb, tangibles, marketcap):
    q = pb * (tangibles / marketcap.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of liabilities over intangible assets (gearing vs soft backing) (window 21d)
def f42nb_f42_asset_backing_nav_liabintangraw_21d_slope_v096_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of liabilities over intangible assets (gearing vs soft backing) (window 63d)
def f42nb_f42_asset_backing_nav_liabintanglogslope_63d_slope_v097_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of liabilities over intangible assets (gearing vs soft backing) (window 126d)
def f42nb_f42_asset_backing_nav_liabintangrsslope_126d_slope_v098_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of liabilities over intangible assets (gearing vs soft backing) (window 63d)
def f42nb_f42_asset_backing_nav_liabintangzslope_63d_slope_v099_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of liabilities over intangible assets (gearing vs soft backing) (window 42d)
def f42nb_f42_asset_backing_nav_liabintangmacdslope_42d_slope_v100_signal(assets, equity, intangibles):
    q = (assets - equity) / intangibles.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times tangible-asset share (window 21d)
def f42nb_f42_asset_backing_nav_pbtangshareraw_21d_slope_v101_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times tangible-asset share (window 63d)
def f42nb_f42_asset_backing_nav_pbtangsharelogslope_63d_slope_v102_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times tangible-asset share (window 126d)
def f42nb_f42_asset_backing_nav_pbtangsharersslope_126d_slope_v103_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times tangible-asset share (window 63d)
def f42nb_f42_asset_backing_nav_pbtangsharezslope_63d_slope_v104_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times tangible-asset share (window 42d)
def f42nb_f42_asset_backing_nav_pbtangsharemacdslope_42d_slope_v105_signal(pb, tangibles, assets):
    ts = tangibles / assets.replace(0, np.nan)
    q = pb * ts
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of book-yield times equity-to-assets (solvent-cheap gate) (window 21d)
def f42nb_f42_asset_backing_nav_byeqassetsraw_21d_slope_v106_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of book-yield times equity-to-assets (solvent-cheap gate) (window 63d)
def f42nb_f42_asset_backing_nav_byeqassetslogslope_63d_slope_v107_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of book-yield times equity-to-assets (solvent-cheap gate) (window 126d)
def f42nb_f42_asset_backing_nav_byeqassetsrsslope_126d_slope_v108_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of book-yield times equity-to-assets (solvent-cheap gate) (window 63d)
def f42nb_f42_asset_backing_nav_byeqassetszslope_63d_slope_v109_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of book-yield times equity-to-assets (solvent-cheap gate) (window 42d)
def f42nb_f42_asset_backing_nav_byeqassetsmacdslope_42d_slope_v110_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (equity / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible cover times tangible share (hard-backing gate) (window 21d)
def f42nb_f42_asset_backing_nav_tangcovshareraw_21d_slope_v111_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible cover times tangible share (hard-backing gate) (window 63d)
def f42nb_f42_asset_backing_nav_tangcovsharelogslope_63d_slope_v112_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible cover times tangible share (hard-backing gate) (window 126d)
def f42nb_f42_asset_backing_nav_tangcovsharersslope_126d_slope_v113_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible cover times tangible share (hard-backing gate) (window 63d)
def f42nb_f42_asset_backing_nav_tangcovsharezslope_63d_slope_v114_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible cover times tangible share (hard-backing gate) (window 42d)
def f42nb_f42_asset_backing_nav_tangcovsharemacdslope_42d_slope_v115_signal(tangibles, marketcap, assets):
    q = (tangibles / marketcap.replace(0, np.nan)) * (tangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of price-to-assets times intangible share (soft overpay) (window 21d)
def f42nb_f42_asset_backing_nav_paintangraw_21d_slope_v116_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of price-to-assets times intangible share (soft overpay) (window 63d)
def f42nb_f42_asset_backing_nav_paintanglogslope_63d_slope_v117_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of price-to-assets times intangible share (soft overpay) (window 126d)
def f42nb_f42_asset_backing_nav_paintangrsslope_126d_slope_v118_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of price-to-assets times intangible share (soft overpay) (window 63d)
def f42nb_f42_asset_backing_nav_paintangzslope_63d_slope_v119_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of price-to-assets times intangible share (soft overpay) (window 42d)
def f42nb_f42_asset_backing_nav_paintangmacdslope_42d_slope_v120_signal(marketcap, assets, intangibles):
    q = (marketcap / assets.replace(0, np.nan)) * (intangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times intangible drag (hype on soft book) (window 21d)
def f42nb_f42_asset_backing_nav_pbintangraw_21d_slope_v121_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times intangible drag (hype on soft book) (window 63d)
def f42nb_f42_asset_backing_nav_pbintanglogslope_63d_slope_v122_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times intangible drag (hype on soft book) (window 126d)
def f42nb_f42_asset_backing_nav_pbintangrsslope_126d_slope_v123_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times intangible drag (hype on soft book) (window 63d)
def f42nb_f42_asset_backing_nav_pbintangzslope_63d_slope_v124_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times intangible drag (hype on soft book) (window 42d)
def f42nb_f42_asset_backing_nav_pbintangmacdslope_42d_slope_v125_signal(pb, intangibles, equity):
    q = pb * (intangibles / equity.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of book-yield times asset-cover (E+A vs marketcap) (window 21d)
def f42nb_f42_asset_backing_nav_eqmcassetsraw_21d_slope_v126_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of book-yield times asset-cover (E+A vs marketcap) (window 63d)
def f42nb_f42_asset_backing_nav_eqmcassetslogslope_63d_slope_v127_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of book-yield times asset-cover (E+A vs marketcap) (window 126d)
def f42nb_f42_asset_backing_nav_eqmcassetsrsslope_126d_slope_v128_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of book-yield times asset-cover (E+A vs marketcap) (window 63d)
def f42nb_f42_asset_backing_nav_eqmcassetszslope_63d_slope_v129_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of book-yield times asset-cover (E+A vs marketcap) (window 42d)
def f42nb_f42_asset_backing_nav_eqmcassetsmacdslope_42d_slope_v130_signal(equity, marketcap, assets):
    q = (equity / marketcap.replace(0, np.nan)) * (assets / marketcap.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of tangible-book-yield minus reported book-to-price (window 21d)
def f42nb_f42_asset_backing_nav_tbminuspbraw_21d_slope_v131_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of tangible-book-yield minus reported book-to-price (window 63d)
def f42nb_f42_asset_backing_nav_tbminuspblogslope_63d_slope_v132_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of tangible-book-yield minus reported book-to-price (window 126d)
def f42nb_f42_asset_backing_nav_tbminuspbrsslope_126d_slope_v133_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of tangible-book-yield minus reported book-to-price (window 63d)
def f42nb_f42_asset_backing_nav_tbminuspbzslope_63d_slope_v134_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of tangible-book-yield minus reported book-to-price (window 42d)
def f42nb_f42_asset_backing_nav_tbminuspbmacdslope_42d_slope_v135_signal(equity, intangibles, marketcap, pb):
    tbm = (equity - intangibles) / marketcap.replace(0, np.nan)
    q = tbm - 1.0 / pb.replace(0, np.nan)
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of book-yield times intangible drag (E+I-... soft-book yield) (window 21d)
def f42nb_f42_asset_backing_nav_byintangdragraw_21d_slope_v136_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of book-yield times intangible drag (E+I-... soft-book yield) (window 63d)
def f42nb_f42_asset_backing_nav_byintangdraglogslope_63d_slope_v137_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of book-yield times intangible drag (E+I-... soft-book yield) (window 126d)
def f42nb_f42_asset_backing_nav_byintangdragrsslope_126d_slope_v138_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of book-yield times intangible drag (E+I-... soft-book yield) (window 63d)
def f42nb_f42_asset_backing_nav_byintangdragzslope_63d_slope_v139_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of book-yield times intangible drag (E+I-... soft-book yield) (window 42d)
def f42nb_f42_asset_backing_nav_byintangdragmacdslope_42d_slope_v140_signal(equity, marketcap, intangibles):
    q = (equity / marketcap.replace(0, np.nan)) * (intangibles / equity.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of P/B times intangible-asset share (hype on soft assets) (window 21d)
def f42nb_f42_asset_backing_nav_pbintangassetsraw_21d_slope_v141_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of P/B times intangible-asset share (hype on soft assets) (window 63d)
def f42nb_f42_asset_backing_nav_pbintangassetslogslope_63d_slope_v142_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of P/B times intangible-asset share (hype on soft assets) (window 126d)
def f42nb_f42_asset_backing_nav_pbintangassetsrsslope_126d_slope_v143_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of P/B times intangible-asset share (hype on soft assets) (window 63d)
def f42nb_f42_asset_backing_nav_pbintangassetszslope_63d_slope_v144_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of P/B times intangible-asset share (hype on soft assets) (window 42d)
def f42nb_f42_asset_backing_nav_pbintangassetsmacdslope_42d_slope_v145_signal(pb, intangibles, assets):
    q = pb * (intangibles / assets.replace(0, np.nan))
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (raw) of intangibles-per-market-dollar times P/B (soft-asset hype) (window 21d)
def f42nb_f42_asset_backing_nav_intangmcpbraw_21d_slope_v146_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    d = (q - q.shift(21)) / 21.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (logslope) of intangibles-per-market-dollar times P/B (soft-asset hype) (window 63d)
def f42nb_f42_asset_backing_nav_intangmcpblogslope_63d_slope_v147_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    lq = np.log(q.replace(0, np.nan).abs().clip(lower=1e-9))
    d = (lq - lq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (rsslope) of intangibles-per-market-dollar times P/B (soft-asset hype) (window 126d)
def f42nb_f42_asset_backing_nav_intangmcpbrsslope_126d_slope_v148_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    d = (q - q.shift(126)) / 126.0
    result = d / _std(q, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)
# slope (zslope) of intangibles-per-market-dollar times P/B (soft-asset hype) (window 63d)
def f42nb_f42_asset_backing_nav_intangmcpbzslope_63d_slope_v149_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    zq = _z(q, 252)
    d = (zq - zq.shift(63)) / 63.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
# slope (macdslope) of intangibles-per-market-dollar times P/B (soft-asset hype) (window 42d)
def f42nb_f42_asset_backing_nav_intangmcpbmacdslope_42d_slope_v150_signal(intangibles, marketcap, pb):
    q = (intangibles / marketcap.replace(0, np.nan)) * pb
    spread = q.ewm(span=21, min_periods=10).mean() - q.ewm(span=126, min_periods=42).mean()
    d = (spread - spread.shift(42)) / 42.0
    result = d
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f42nb_f42_asset_backing_nav_pbraw_21d_slope_v001_signal,
    f42nb_f42_asset_backing_nav_pblogslope_63d_slope_v002_signal,
    f42nb_f42_asset_backing_nav_pbrsslope_126d_slope_v003_signal,
    f42nb_f42_asset_backing_nav_pbzslope_63d_slope_v004_signal,
    f42nb_f42_asset_backing_nav_pbmacdslope_42d_slope_v005_signal,
    f42nb_f42_asset_backing_nav_pbproxyraw_21d_slope_v006_signal,
    f42nb_f42_asset_backing_nav_pbproxylogslope_63d_slope_v007_signal,
    f42nb_f42_asset_backing_nav_pbproxyrsslope_126d_slope_v008_signal,
    f42nb_f42_asset_backing_nav_pbproxyzslope_63d_slope_v009_signal,
    f42nb_f42_asset_backing_nav_pbproxymacdslope_42d_slope_v010_signal,
    f42nb_f42_asset_backing_nav_ptbtangraw_21d_slope_v011_signal,
    f42nb_f42_asset_backing_nav_ptbtanglogslope_63d_slope_v012_signal,
    f42nb_f42_asset_backing_nav_ptbtangrsslope_126d_slope_v013_signal,
    f42nb_f42_asset_backing_nav_ptbtangzslope_63d_slope_v014_signal,
    f42nb_f42_asset_backing_nav_ptbtangmacdslope_42d_slope_v015_signal,
    f42nb_f42_asset_backing_nav_priceassetsraw_21d_slope_v016_signal,
    f42nb_f42_asset_backing_nav_priceassetslogslope_63d_slope_v017_signal,
    f42nb_f42_asset_backing_nav_priceassetsrsslope_126d_slope_v018_signal,
    f42nb_f42_asset_backing_nav_priceassetszslope_63d_slope_v019_signal,
    f42nb_f42_asset_backing_nav_priceassetsmacdslope_42d_slope_v020_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsraw_21d_slope_v021_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetslogslope_63d_slope_v022_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsrsslope_126d_slope_v023_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetszslope_63d_slope_v024_signal,
    f42nb_f42_asset_backing_nav_pbpriceassetsmacdslope_42d_slope_v025_signal,
    f42nb_f42_asset_backing_nav_tangshareraw_21d_slope_v026_signal,
    f42nb_f42_asset_backing_nav_tangsharelogslope_63d_slope_v027_signal,
    f42nb_f42_asset_backing_nav_tangsharersslope_126d_slope_v028_signal,
    f42nb_f42_asset_backing_nav_tangsharezslope_63d_slope_v029_signal,
    f42nb_f42_asset_backing_nav_tangsharemacdslope_42d_slope_v030_signal,
    f42nb_f42_asset_backing_nav_eqassetsraw_21d_slope_v031_signal,
    f42nb_f42_asset_backing_nav_eqassetslogslope_63d_slope_v032_signal,
    f42nb_f42_asset_backing_nav_eqassetsrsslope_126d_slope_v033_signal,
    f42nb_f42_asset_backing_nav_eqassetszslope_63d_slope_v034_signal,
    f42nb_f42_asset_backing_nav_eqassetsmacdslope_42d_slope_v035_signal,
    f42nb_f42_asset_backing_nav_intangdragraw_21d_slope_v036_signal,
    f42nb_f42_asset_backing_nav_intangdraglogslope_63d_slope_v037_signal,
    f42nb_f42_asset_backing_nav_intangdragrsslope_126d_slope_v038_signal,
    f42nb_f42_asset_backing_nav_intangdragzslope_63d_slope_v039_signal,
    f42nb_f42_asset_backing_nav_intangdragmacdslope_42d_slope_v040_signal,
    f42nb_f42_asset_backing_nav_intangassetsraw_21d_slope_v041_signal,
    f42nb_f42_asset_backing_nav_intangassetslogslope_63d_slope_v042_signal,
    f42nb_f42_asset_backing_nav_intangassetsrsslope_126d_slope_v043_signal,
    f42nb_f42_asset_backing_nav_intangassetszslope_63d_slope_v044_signal,
    f42nb_f42_asset_backing_nav_intangassetsmacdslope_42d_slope_v045_signal,
    f42nb_f42_asset_backing_nav_tangeqraw_21d_slope_v046_signal,
    f42nb_f42_asset_backing_nav_tangeqlogslope_63d_slope_v047_signal,
    f42nb_f42_asset_backing_nav_tangeqrsslope_126d_slope_v048_signal,
    f42nb_f42_asset_backing_nav_tangeqzslope_63d_slope_v049_signal,
    f42nb_f42_asset_backing_nav_tangeqmacdslope_42d_slope_v050_signal,
    f42nb_f42_asset_backing_nav_softhardraw_21d_slope_v051_signal,
    f42nb_f42_asset_backing_nav_softhardlogslope_63d_slope_v052_signal,
    f42nb_f42_asset_backing_nav_softhardrsslope_126d_slope_v053_signal,
    f42nb_f42_asset_backing_nav_softhardzslope_63d_slope_v054_signal,
    f42nb_f42_asset_backing_nav_softhardmacdslope_42d_slope_v055_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsraw_21d_slope_v056_signal,
    f42nb_f42_asset_backing_nav_pbeqassetslogslope_63d_slope_v057_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsrsslope_126d_slope_v058_signal,
    f42nb_f42_asset_backing_nav_pbeqassetszslope_63d_slope_v059_signal,
    f42nb_f42_asset_backing_nav_pbeqassetsmacdslope_42d_slope_v060_signal,
    f42nb_f42_asset_backing_nav_tangeqshareraw_21d_slope_v061_signal,
    f42nb_f42_asset_backing_nav_tangeqsharelogslope_63d_slope_v062_signal,
    f42nb_f42_asset_backing_nav_tangeqsharersslope_126d_slope_v063_signal,
    f42nb_f42_asset_backing_nav_tangeqsharezslope_63d_slope_v064_signal,
    f42nb_f42_asset_backing_nav_tangeqsharemacdslope_42d_slope_v065_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadraw_21d_slope_v066_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadlogslope_63d_slope_v067_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadrsslope_126d_slope_v068_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadzslope_63d_slope_v069_signal,
    f42nb_f42_asset_backing_nav_pbpaspreadmacdslope_42d_slope_v070_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgeraw_21d_slope_v071_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgelogslope_63d_slope_v072_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgersslope_126d_slope_v073_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgezslope_63d_slope_v074_signal,
    f42nb_f42_asset_backing_nav_pbptbwedgemacdslope_42d_slope_v075_signal,
    f42nb_f42_asset_backing_nav_softoverhangraw_21d_slope_v076_signal,
    f42nb_f42_asset_backing_nav_softoverhanglogslope_63d_slope_v077_signal,
    f42nb_f42_asset_backing_nav_softoverhangrsslope_126d_slope_v078_signal,
    f42nb_f42_asset_backing_nav_softoverhangzslope_63d_slope_v079_signal,
    f42nb_f42_asset_backing_nav_softoverhangmacdslope_42d_slope_v080_signal,
    f42nb_f42_asset_backing_nav_tccusharaw_21d_slope_v081_signal,
    f42nb_f42_asset_backing_nav_tccushalogslope_63d_slope_v082_signal,
    f42nb_f42_asset_backing_nav_tccusharsslope_126d_slope_v083_signal,
    f42nb_f42_asset_backing_nav_tccushazslope_63d_slope_v084_signal,
    f42nb_f42_asset_backing_nav_tccushamacdslope_42d_slope_v085_signal,
    f42nb_f42_asset_backing_nav_paeqassetsraw_21d_slope_v086_signal,
    f42nb_f42_asset_backing_nav_paeqassetslogslope_63d_slope_v087_signal,
    f42nb_f42_asset_backing_nav_paeqassetsrsslope_126d_slope_v088_signal,
    f42nb_f42_asset_backing_nav_paeqassetszslope_63d_slope_v089_signal,
    f42nb_f42_asset_backing_nav_paeqassetsmacdslope_42d_slope_v090_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverraw_21d_slope_v091_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverlogslope_63d_slope_v092_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverrsslope_126d_slope_v093_signal,
    f42nb_f42_asset_backing_nav_pbtangcoverzslope_63d_slope_v094_signal,
    f42nb_f42_asset_backing_nav_pbtangcovermacdslope_42d_slope_v095_signal,
    f42nb_f42_asset_backing_nav_liabintangraw_21d_slope_v096_signal,
    f42nb_f42_asset_backing_nav_liabintanglogslope_63d_slope_v097_signal,
    f42nb_f42_asset_backing_nav_liabintangrsslope_126d_slope_v098_signal,
    f42nb_f42_asset_backing_nav_liabintangzslope_63d_slope_v099_signal,
    f42nb_f42_asset_backing_nav_liabintangmacdslope_42d_slope_v100_signal,
    f42nb_f42_asset_backing_nav_pbtangshareraw_21d_slope_v101_signal,
    f42nb_f42_asset_backing_nav_pbtangsharelogslope_63d_slope_v102_signal,
    f42nb_f42_asset_backing_nav_pbtangsharersslope_126d_slope_v103_signal,
    f42nb_f42_asset_backing_nav_pbtangsharezslope_63d_slope_v104_signal,
    f42nb_f42_asset_backing_nav_pbtangsharemacdslope_42d_slope_v105_signal,
    f42nb_f42_asset_backing_nav_byeqassetsraw_21d_slope_v106_signal,
    f42nb_f42_asset_backing_nav_byeqassetslogslope_63d_slope_v107_signal,
    f42nb_f42_asset_backing_nav_byeqassetsrsslope_126d_slope_v108_signal,
    f42nb_f42_asset_backing_nav_byeqassetszslope_63d_slope_v109_signal,
    f42nb_f42_asset_backing_nav_byeqassetsmacdslope_42d_slope_v110_signal,
    f42nb_f42_asset_backing_nav_tangcovshareraw_21d_slope_v111_signal,
    f42nb_f42_asset_backing_nav_tangcovsharelogslope_63d_slope_v112_signal,
    f42nb_f42_asset_backing_nav_tangcovsharersslope_126d_slope_v113_signal,
    f42nb_f42_asset_backing_nav_tangcovsharezslope_63d_slope_v114_signal,
    f42nb_f42_asset_backing_nav_tangcovsharemacdslope_42d_slope_v115_signal,
    f42nb_f42_asset_backing_nav_paintangraw_21d_slope_v116_signal,
    f42nb_f42_asset_backing_nav_paintanglogslope_63d_slope_v117_signal,
    f42nb_f42_asset_backing_nav_paintangrsslope_126d_slope_v118_signal,
    f42nb_f42_asset_backing_nav_paintangzslope_63d_slope_v119_signal,
    f42nb_f42_asset_backing_nav_paintangmacdslope_42d_slope_v120_signal,
    f42nb_f42_asset_backing_nav_pbintangraw_21d_slope_v121_signal,
    f42nb_f42_asset_backing_nav_pbintanglogslope_63d_slope_v122_signal,
    f42nb_f42_asset_backing_nav_pbintangrsslope_126d_slope_v123_signal,
    f42nb_f42_asset_backing_nav_pbintangzslope_63d_slope_v124_signal,
    f42nb_f42_asset_backing_nav_pbintangmacdslope_42d_slope_v125_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsraw_21d_slope_v126_signal,
    f42nb_f42_asset_backing_nav_eqmcassetslogslope_63d_slope_v127_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsrsslope_126d_slope_v128_signal,
    f42nb_f42_asset_backing_nav_eqmcassetszslope_63d_slope_v129_signal,
    f42nb_f42_asset_backing_nav_eqmcassetsmacdslope_42d_slope_v130_signal,
    f42nb_f42_asset_backing_nav_tbminuspbraw_21d_slope_v131_signal,
    f42nb_f42_asset_backing_nav_tbminuspblogslope_63d_slope_v132_signal,
    f42nb_f42_asset_backing_nav_tbminuspbrsslope_126d_slope_v133_signal,
    f42nb_f42_asset_backing_nav_tbminuspbzslope_63d_slope_v134_signal,
    f42nb_f42_asset_backing_nav_tbminuspbmacdslope_42d_slope_v135_signal,
    f42nb_f42_asset_backing_nav_byintangdragraw_21d_slope_v136_signal,
    f42nb_f42_asset_backing_nav_byintangdraglogslope_63d_slope_v137_signal,
    f42nb_f42_asset_backing_nav_byintangdragrsslope_126d_slope_v138_signal,
    f42nb_f42_asset_backing_nav_byintangdragzslope_63d_slope_v139_signal,
    f42nb_f42_asset_backing_nav_byintangdragmacdslope_42d_slope_v140_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsraw_21d_slope_v141_signal,
    f42nb_f42_asset_backing_nav_pbintangassetslogslope_63d_slope_v142_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsrsslope_126d_slope_v143_signal,
    f42nb_f42_asset_backing_nav_pbintangassetszslope_63d_slope_v144_signal,
    f42nb_f42_asset_backing_nav_pbintangassetsmacdslope_42d_slope_v145_signal,
    f42nb_f42_asset_backing_nav_intangmcpbraw_21d_slope_v146_signal,
    f42nb_f42_asset_backing_nav_intangmcpblogslope_63d_slope_v147_signal,
    f42nb_f42_asset_backing_nav_intangmcpbrsslope_126d_slope_v148_signal,
    f42nb_f42_asset_backing_nav_intangmcpbzslope_63d_slope_v149_signal,
    f42nb_f42_asset_backing_nav_intangmcpbmacdslope_42d_slope_v150_signal,
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

    print("OK f42_asset_backing_nav_2nd_derivatives_001_150_claude: %d features pass" % n_features)
