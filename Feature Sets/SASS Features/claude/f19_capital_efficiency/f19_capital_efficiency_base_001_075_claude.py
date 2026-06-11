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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (capital efficiency / turnover levels) =====
def _f19_asset_turn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f19_invcap_turn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _f19_fixed_turn(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f19_equity_turn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _f19_capint(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan)


# ============================================================
# asset turnover level (revenue/assets)
def f19ce_f19_capital_efficiency_aturn_21d_base_v001_signal(revenue, assets):
    b = _f19_asset_turn(revenue, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover using period-average assets (revenue/assetsavg)
def f19ce_f19_capital_efficiency_aturnavg_21d_base_v002_signal(revenue, assetsavg):
    b = revenue / assetsavg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover z-scored vs its own 252d history (efficiency extremity)
def f19ce_f19_capital_efficiency_aturnz_252d_base_v003_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover percentile-ranked vs its own 504d history
def f19ce_f19_capital_efficiency_aturnrank_504d_base_v004_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover level (revenue/invcap)
def f19ce_f19_capital_efficiency_icturn_21d_base_v005_signal(revenue, invcap):
    b = _f19_invcap_turn(revenue, invcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover using period-average invcap (revenue/invcapavg)
def f19ce_f19_capital_efficiency_icturnavg_21d_base_v006_signal(revenue, invcapavg):
    b = revenue / invcapavg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover z-scored vs its own 252d history
def f19ce_f19_capital_efficiency_icturnz_252d_base_v007_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover level (revenue/ppnenet)
def f19ce_f19_capital_efficiency_fturn_21d_base_v008_signal(revenue, ppnenet):
    b = _f19_fixed_turn(revenue, ppnenet)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover z-scored vs its own 252d history
def f19ce_f19_capital_efficiency_fturnz_252d_base_v009_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover percentile-ranked vs 504d history
def f19ce_f19_capital_efficiency_fturnrank_504d_base_v010_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover level (revenue/equity)
def f19ce_f19_capital_efficiency_eturn_21d_base_v011_signal(revenue, equity):
    b = _f19_equity_turn(revenue, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover z-scored vs its own 252d history
def f19ce_f19_capital_efficiency_eturnz_252d_base_v012_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-to-invested-capital momentum: 63d ratio change of revenue/invcapavg
def f19ce_f19_capital_efficiency_salesic_21d_base_v013_signal(revenue, invcapavg):
    t = revenue / invcapavg.replace(0, np.nan)
    b = t / t.shift(63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity (ppnenet/assets) relative to its 252d median (inverse-efficiency gap)
def f19ce_f19_capital_efficiency_capint_21d_base_v014_signal(ppnenet, assets):
    c = _f19_capint(ppnenet, assets)
    med = c.rolling(252, min_periods=126).median()
    b = c / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity z-scored vs its own 252d history
def f19ce_f19_capital_efficiency_capintz_252d_base_v015_signal(ppnenet, assets):
    c = _f19_capint(ppnenet, assets)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover spread: asset-turnover minus invcap-turnover (where capital is tied)
def f19ce_f19_capital_efficiency_aicspr_21d_base_v016_signal(revenue, assets, invcap):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    b = a - i
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage efficiency wedge: (equity-turn minus asset-turn) scaled by asset-turn (relative wedge)
def f19ce_f19_capital_efficiency_easpr_21d_base_v017_signal(revenue, equity, assets):
    e = _f19_equity_turn(revenue, equity)
    a = _f19_asset_turn(revenue, assets)
    b = (e - a) / a.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# plant-vs-total capital allocation shift: ppnenet-share-of-assets minus its 126d mean
def f19ce_f19_capital_efficiency_faspr_21d_base_v018_signal(revenue, ppnenet, assets):
    share = ppnenet / assets.replace(0, np.nan)
    b = share - share.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-structure leverage drift: 63d log-change of (invcap-turn / asset-turn)
def f19ce_f19_capital_efficiency_icaratio_21d_base_v019_signal(revenue, invcap, assets):
    i = _f19_invcap_turn(revenue, invcap)
    a = _f19_asset_turn(revenue, assets)
    r = i / a.replace(0, np.nan)
    b = np.log(r.replace(0, np.nan)) - np.log(r.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-momentum disagreement: cross-measure std of 63d turnover growth rates
def f19ce_f19_capital_efficiency_turndisp_21d_base_v020_signal(revenue, assets, invcap, equity, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    e = _f19_equity_turn(revenue, equity)
    f = _f19_fixed_turn(revenue, ppnenet)
    ga = a / a.shift(63) - 1.0
    gi = i / i.shift(63) - 1.0
    ge = e / e.shift(63) - 1.0
    gf = f / f.shift(63) - 1.0
    b = pd.concat([ga, gi, ge, gf], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover smoothed (persistent efficiency level, slow EMA)
def f19ce_f19_capital_efficiency_aturnema_63d_base_v021_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover smoothed (persistent efficiency, slow EMA)
def f19ce_f19_capital_efficiency_icturnema_63d_base_v022_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = t.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover displacement: level minus its own slow EMA (efficiency surprise)
def f19ce_f19_capital_efficiency_aturndisp_63d_base_v023_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t - t.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover displacement vs slow EMA
def f19ce_f19_capital_efficiency_eturndisp_63d_base_v024_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = t - t.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover displacement vs slow EMA
def f19ce_f19_capital_efficiency_fturndisp_63d_base_v025_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = t - t.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover stability: inverse coefficient of variation over 252d (durable efficiency)
def f19ce_f19_capital_efficiency_aturnstab_252d_base_v026_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    m = _mean(t, 252)
    sd = _std(t, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover stability (inverse CoV over 252d)
def f19ce_f19_capital_efficiency_icturnstab_252d_base_v027_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    m = _mean(t, 252)
    sd = _std(t, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover log-acceleration: 21d log-change minus its own 63d-lagged log-change
def f19ce_f19_capital_efficiency_aturnsm_21d_base_v028_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    lc = np.log(t.replace(0, np.nan)) - np.log(t.shift(21).replace(0, np.nan))
    b = lc - lc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover percentile-ranked vs 504d history
def f19ce_f19_capital_efficiency_eturnrank_504d_base_v029_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover percentile-ranked vs 504d history
def f19ce_f19_capital_efficiency_icturnrank_504d_base_v030_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover gap to its 252d max (distance below best efficiency)
def f19ce_f19_capital_efficiency_aturngap_252d_base_v031_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    mx = t.rolling(252, min_periods=126).max()
    b = t / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset-turnover gap to its 252d max (utilization headroom)
def f19ce_f19_capital_efficiency_fturngap_252d_base_v032_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    mx = t.rolling(252, min_periods=126).max()
    b = t / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band persistence: fraction of last quarter asset-turnover sat in top third of 252d band
def f19ce_f19_capital_efficiency_aturnpos_252d_base_v033_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    hi = t.rolling(252, min_periods=126).max()
    lo = t.rolling(252, min_periods=126).min()
    rp = (t - lo) / (hi - lo).replace(0, np.nan)
    upper = (rp >= 0.6667).astype(float)
    b = upper.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover range position in its 252d hi-lo band
def f19ce_f19_capital_efficiency_icturnpos_252d_base_v034_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    hi = t.rolling(252, min_periods=126).max()
    lo = t.rolling(252, min_periods=126).min()
    b = (t - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average-asset turnover z-scored (revenue/assetsavg de-trended)
def f19ce_f19_capital_efficiency_aturnavgz_252d_base_v035_signal(revenue, assetsavg):
    t = revenue / assetsavg.replace(0, np.nan)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average-invcap turnover z-scored (revenue/invcapavg de-trended)
def f19ce_f19_capital_efficiency_icturnavgz_252d_base_v036_signal(revenue, invcapavg):
    t = revenue / invcapavg.replace(0, np.nan)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spot-vs-average asset turnover wedge (revenue/assets minus revenue/assetsavg)
def f19ce_f19_capital_efficiency_aspotavg_21d_base_v037_signal(revenue, assets, assetsavg):
    s = _f19_asset_turn(revenue, assets)
    a = revenue / assetsavg.replace(0, np.nan)
    b = s - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spot-vs-average invcap turnover wedge
def f19ce_f19_capital_efficiency_icspotavg_21d_base_v038_signal(revenue, invcap, invcapavg):
    s = _f19_invcap_turn(revenue, invcap)
    a = revenue / invcapavg.replace(0, np.nan)
    b = s - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-base growth normalized vs revenue growth (asset bloat relative to sales)
def f19ce_f19_capital_efficiency_assetbloat_63d_base_v039_signal(revenue, assets):
    ag = assets / assets.shift(63) - 1.0
    rg = revenue / revenue.shift(63) - 1.0
    b = ag - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth minus revenue growth (capital absorption)
def f19ce_f19_capital_efficiency_icbloat_63d_base_v040_signal(revenue, invcap):
    ig = invcap / invcap.shift(63) - 1.0
    rg = revenue / revenue.shift(63) - 1.0
    b = ig - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset growth minus revenue growth (plant absorption)
def f19ce_f19_capital_efficiency_ppnebloat_63d_base_v041_signal(revenue, ppnenet):
    pg = ppnenet / ppnenet.shift(63) - 1.0
    rg = revenue / revenue.shift(63) - 1.0
    b = pg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover harmonic blend: 2/(1/aturn + 1/icturn) (combined efficiency floor)
def f19ce_f19_capital_efficiency_harmturn_21d_base_v042_signal(revenue, assets, invcap):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    b = 2.0 / (1.0 / a.replace(0, np.nan) + 1.0 / i.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover geometric blend across asset & equity turnover
def f19ce_f19_capital_efficiency_geoturn_21d_base_v043_signal(revenue, assets, equity):
    a = _f19_asset_turn(revenue, assets)
    e = _f19_equity_turn(revenue, equity)
    b = np.sign(a * e) * (a.abs() * e.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency utilization: asset turnover as a fraction of its 252d max, smoothed
def f19ce_f19_capital_efficiency_aturnutil_252d_base_v044_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    mx = t.rolling(252, min_periods=126).max()
    util = t / mx.replace(0, np.nan)
    b = util.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover band-position acceleration: 21d change in asset-turnover range position
def f19ce_f19_capital_efficiency_aturnconv_252d_base_v045_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    hi = t.rolling(252, min_periods=126).max()
    lo = t.rolling(252, min_periods=126).min()
    rp = (t - lo) / (hi - lo).replace(0, np.nan)
    b = rp - rp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover distributional asymmetry: rolling skew of revenue/assets over 126d
def f19ce_f19_capital_efficiency_aturntanh_126d_base_v046_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover stability (inverse CoV 252d)
def f19ce_f19_capital_efficiency_fturnstab_252d_base_v047_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    m = _mean(t, 252)
    sd = _std(t, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover stability (inverse CoV 252d)
def f19ce_f19_capital_efficiency_eturnstab_252d_base_v048_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    m = _mean(t, 252)
    sd = _std(t, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite efficiency momentum: 21d change of the mean of three turnover measures
def f19ce_f19_capital_efficiency_compavg_21d_base_v049_signal(revenue, assets, invcap, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    f = _f19_fixed_turn(revenue, ppnenet)
    comp = pd.concat([a, i, f], axis=1).mean(axis=1)
    b = comp / comp.shift(21) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended asset+equity turnover composite z-scored vs 252d history
def f19ce_f19_capital_efficiency_compz_252d_base_v050_signal(revenue, assets, equity):
    a = _f19_asset_turn(revenue, assets)
    e = _f19_equity_turn(revenue, equity)
    comp = pd.concat([a, e], axis=1).mean(axis=1)
    b = _z(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity percentile-rank inverted (low-intensity = capital-light efficiency)
def f19ce_f19_capital_efficiency_capintrank_504d_base_v051_signal(ppnenet, assets):
    c = _f19_capint(ppnenet, assets)
    b = -_rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital share of assets (how much capital base is "invested")
def f19ce_f19_capital_efficiency_icshare_21d_base_v052_signal(invcap, assets):
    b = invcap / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital share of assets z-scored vs 252d history
def f19ce_f19_capital_efficiency_icsharez_252d_base_v053_signal(invcap, assets):
    s = invcap / assets.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity share of invested capital (capital structure within invcap)
def f19ce_f19_capital_efficiency_eqicshare_21d_base_v054_signal(equity, invcap):
    b = equity / invcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover relative to its 252d median (own-history normalization)
def f19ce_f19_capital_efficiency_aturnrelmed_252d_base_v055_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    med = t.rolling(252, min_periods=126).median()
    b = t / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover relative to its 252d median
def f19ce_f19_capital_efficiency_icturnrelmed_252d_base_v056_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    med = t.rolling(252, min_periods=126).median()
    b = t / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover spread z: (equity-turn minus asset-turn) de-trended
def f19ce_f19_capital_efficiency_easprz_252d_base_v057_signal(revenue, equity, assets):
    e = _f19_equity_turn(revenue, equity)
    a = _f19_asset_turn(revenue, assets)
    b = _z(e - a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover spread z: (fixed-turn minus invcap-turn) de-trended
def f19ce_f19_capital_efficiency_ficsprz_252d_base_v058_signal(revenue, ppnenet, invcap):
    f = _f19_fixed_turn(revenue, ppnenet)
    i = _f19_invcap_turn(revenue, invcap)
    b = _z(f - i, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover above its own EMA, as a hit-rate over the last quarter
def f19ce_f19_capital_efficiency_aturnhit_63d_base_v059_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    ema = t.ewm(span=126, min_periods=42).mean()
    above = (t > ema).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover above its EMA hit-rate
def f19ce_f19_capital_efficiency_icturnhit_63d_base_v060_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    ema = t.ewm(span=126, min_periods=42).mean()
    above = (t > ema).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-focus: invcap turnover weighted by equity-share-of-invcap (self-funded efficiency)
def f19ce_f19_capital_efficiency_icfocus_21d_base_v061_signal(revenue, invcap, equity):
    t = _f19_invcap_turn(revenue, invcap)
    share = equity / invcap.replace(0, np.nan)
    prod = t * share
    b = _rank(prod, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# plant-productivity identity check: fixed-turn x capital-intensity equals asset-turn;
# measure its z-scored deviation drift (residual after the algebraic identity, de-trended)
def f19ce_f19_capital_efficiency_plantprod_21d_base_v062_signal(revenue, ppnenet, assets):
    f = _f19_fixed_turn(revenue, ppnenet)
    ci = _f19_capint(ppnenet, assets)
    prod = f * ci
    b = _z(prod, 126) - _z(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover rolling CoV (instability of asset efficiency)
def f19ce_f19_capital_efficiency_aturnvol_126d_base_v063_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = _std(t, 126) / _mean(t, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover rolling CoV (instability of equity efficiency)
def f19ce_f19_capital_efficiency_eturnvol_126d_base_v064_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = _std(t, 126) / _mean(t, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-measure agreement: negative normalized dispersion across three measures
def f19ce_f19_capital_efficiency_turnagree_21d_base_v065_signal(revenue, assets, invcap, equity):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    e = _f19_equity_turn(revenue, equity)
    cat = pd.concat([a, i, e], axis=1)
    b = -(cat.std(axis=1) / cat.mean(axis=1).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover squared deviation from 252d mean (efficiency volatility level)
def f19ce_f19_capital_efficiency_aturndev2_252d_base_v066_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    m = _mean(t, 252)
    b = (t - m) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover relative to fixed-asset turnover (where capital earns more)
def f19ce_f19_capital_efficiency_icfratio_21d_base_v067_signal(revenue, invcap, ppnenet):
    i = _f19_invcap_turn(revenue, invcap)
    f = _f19_fixed_turn(revenue, ppnenet)
    b = i / f.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light score: asset-turnover minus capital-intensity, z-scored over 126d (net light efficiency)
def f19ce_f19_capital_efficiency_lightscore_21d_base_v068_signal(revenue, assets, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    ci = _f19_capint(ppnenet, assets)
    score = a - ci
    b = _z(score, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover rank within its 252d band, EMA-smoothed (durable rank)
def f19ce_f19_capital_efficiency_aturnrankema_252d_base_v069_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    r = _rank(t, 252)
    b = r.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover minus its year-ago level (year-over-year level change)
def f19ce_f19_capital_efficiency_eturnyoy_252d_base_v070_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-turnover mean-reversion gap: level minus its 126d median, ranked vs 252d history
def f19ce_f19_capital_efficiency_icturnsm_21d_base_v071_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    med = t.rolling(126, min_periods=63).median()
    gap = t - med
    b = _rank(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average-based turnover spread as a fraction of asset turnover (scale-free disagreement)
def f19ce_f19_capital_efficiency_avgdisp_21d_base_v072_signal(revenue, assetsavg, invcapavg):
    a = revenue / assetsavg.replace(0, np.nan)
    i = revenue / invcapavg.replace(0, np.nan)
    b = (a - i) / a.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-leverage momentum: 63d change in (asset-turn / equity-turn) = equity/assets drift
def f19ce_f19_capital_efficiency_aeratio_21d_base_v073_signal(revenue, assets, equity):
    a = _f19_asset_turn(revenue, assets)
    e = _f19_equity_turn(revenue, equity)
    r = a / e.replace(0, np.nan)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover percentile-rank EMA-smoothed (durable plant utilization)
def f19ce_f19_capital_efficiency_fturnrankema_252d_base_v074_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    r = _rank(t, 252)
    b = r.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite efficiency: harmonic mean of asset & fixed-asset turnover, z-scored
def f19ce_f19_capital_efficiency_harmafz_252d_base_v075_signal(revenue, assets, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    f = _f19_fixed_turn(revenue, ppnenet)
    h = 2.0 / (1.0 / a.replace(0, np.nan) + 1.0 / f.replace(0, np.nan))
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ce_f19_capital_efficiency_aturn_21d_base_v001_signal,
    f19ce_f19_capital_efficiency_aturnavg_21d_base_v002_signal,
    f19ce_f19_capital_efficiency_aturnz_252d_base_v003_signal,
    f19ce_f19_capital_efficiency_aturnrank_504d_base_v004_signal,
    f19ce_f19_capital_efficiency_icturn_21d_base_v005_signal,
    f19ce_f19_capital_efficiency_icturnavg_21d_base_v006_signal,
    f19ce_f19_capital_efficiency_icturnz_252d_base_v007_signal,
    f19ce_f19_capital_efficiency_fturn_21d_base_v008_signal,
    f19ce_f19_capital_efficiency_fturnz_252d_base_v009_signal,
    f19ce_f19_capital_efficiency_fturnrank_504d_base_v010_signal,
    f19ce_f19_capital_efficiency_eturn_21d_base_v011_signal,
    f19ce_f19_capital_efficiency_eturnz_252d_base_v012_signal,
    f19ce_f19_capital_efficiency_salesic_21d_base_v013_signal,
    f19ce_f19_capital_efficiency_capint_21d_base_v014_signal,
    f19ce_f19_capital_efficiency_capintz_252d_base_v015_signal,
    f19ce_f19_capital_efficiency_aicspr_21d_base_v016_signal,
    f19ce_f19_capital_efficiency_easpr_21d_base_v017_signal,
    f19ce_f19_capital_efficiency_faspr_21d_base_v018_signal,
    f19ce_f19_capital_efficiency_icaratio_21d_base_v019_signal,
    f19ce_f19_capital_efficiency_turndisp_21d_base_v020_signal,
    f19ce_f19_capital_efficiency_aturnema_63d_base_v021_signal,
    f19ce_f19_capital_efficiency_icturnema_63d_base_v022_signal,
    f19ce_f19_capital_efficiency_aturndisp_63d_base_v023_signal,
    f19ce_f19_capital_efficiency_eturndisp_63d_base_v024_signal,
    f19ce_f19_capital_efficiency_fturndisp_63d_base_v025_signal,
    f19ce_f19_capital_efficiency_aturnstab_252d_base_v026_signal,
    f19ce_f19_capital_efficiency_icturnstab_252d_base_v027_signal,
    f19ce_f19_capital_efficiency_aturnsm_21d_base_v028_signal,
    f19ce_f19_capital_efficiency_eturnrank_504d_base_v029_signal,
    f19ce_f19_capital_efficiency_icturnrank_504d_base_v030_signal,
    f19ce_f19_capital_efficiency_aturngap_252d_base_v031_signal,
    f19ce_f19_capital_efficiency_fturngap_252d_base_v032_signal,
    f19ce_f19_capital_efficiency_aturnpos_252d_base_v033_signal,
    f19ce_f19_capital_efficiency_icturnpos_252d_base_v034_signal,
    f19ce_f19_capital_efficiency_aturnavgz_252d_base_v035_signal,
    f19ce_f19_capital_efficiency_icturnavgz_252d_base_v036_signal,
    f19ce_f19_capital_efficiency_aspotavg_21d_base_v037_signal,
    f19ce_f19_capital_efficiency_icspotavg_21d_base_v038_signal,
    f19ce_f19_capital_efficiency_assetbloat_63d_base_v039_signal,
    f19ce_f19_capital_efficiency_icbloat_63d_base_v040_signal,
    f19ce_f19_capital_efficiency_ppnebloat_63d_base_v041_signal,
    f19ce_f19_capital_efficiency_harmturn_21d_base_v042_signal,
    f19ce_f19_capital_efficiency_geoturn_21d_base_v043_signal,
    f19ce_f19_capital_efficiency_aturnutil_252d_base_v044_signal,
    f19ce_f19_capital_efficiency_aturnconv_252d_base_v045_signal,
    f19ce_f19_capital_efficiency_aturntanh_126d_base_v046_signal,
    f19ce_f19_capital_efficiency_fturnstab_252d_base_v047_signal,
    f19ce_f19_capital_efficiency_eturnstab_252d_base_v048_signal,
    f19ce_f19_capital_efficiency_compavg_21d_base_v049_signal,
    f19ce_f19_capital_efficiency_compz_252d_base_v050_signal,
    f19ce_f19_capital_efficiency_capintrank_504d_base_v051_signal,
    f19ce_f19_capital_efficiency_icshare_21d_base_v052_signal,
    f19ce_f19_capital_efficiency_icsharez_252d_base_v053_signal,
    f19ce_f19_capital_efficiency_eqicshare_21d_base_v054_signal,
    f19ce_f19_capital_efficiency_aturnrelmed_252d_base_v055_signal,
    f19ce_f19_capital_efficiency_icturnrelmed_252d_base_v056_signal,
    f19ce_f19_capital_efficiency_easprz_252d_base_v057_signal,
    f19ce_f19_capital_efficiency_ficsprz_252d_base_v058_signal,
    f19ce_f19_capital_efficiency_aturnhit_63d_base_v059_signal,
    f19ce_f19_capital_efficiency_icturnhit_63d_base_v060_signal,
    f19ce_f19_capital_efficiency_icfocus_21d_base_v061_signal,
    f19ce_f19_capital_efficiency_plantprod_21d_base_v062_signal,
    f19ce_f19_capital_efficiency_aturnvol_126d_base_v063_signal,
    f19ce_f19_capital_efficiency_eturnvol_126d_base_v064_signal,
    f19ce_f19_capital_efficiency_turnagree_21d_base_v065_signal,
    f19ce_f19_capital_efficiency_aturndev2_252d_base_v066_signal,
    f19ce_f19_capital_efficiency_icfratio_21d_base_v067_signal,
    f19ce_f19_capital_efficiency_lightscore_21d_base_v068_signal,
    f19ce_f19_capital_efficiency_aturnrankema_252d_base_v069_signal,
    f19ce_f19_capital_efficiency_eturnyoy_252d_base_v070_signal,
    f19ce_f19_capital_efficiency_icturnsm_21d_base_v071_signal,
    f19ce_f19_capital_efficiency_avgdisp_21d_base_v072_signal,
    f19ce_f19_capital_efficiency_aeratio_21d_base_v073_signal,
    f19ce_f19_capital_efficiency_fturnrankema_252d_base_v074_signal,
    f19ce_f19_capital_efficiency_harmafz_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_CAPITAL_EFFICIENCY_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    n = 1500
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(1, base=5e8, drift=0.03, vol=0.06).rename("revenue")
    assets = _fund(2, base=2e9, drift=0.02, vol=0.04).rename("assets")
    assetsavg = _fund(3, base=2e9, drift=0.02, vol=0.04).rename("assetsavg")
    invcap = _fund(4, base=1.2e9, drift=0.02, vol=0.05).rename("invcap")
    invcapavg = _fund(5, base=1.2e9, drift=0.02, vol=0.05).rename("invcapavg")
    equity = _fund(6, base=8e8, drift=0.02, vol=0.05).rename("equity")
    ppnenet = _fund(7, base=6e8, drift=0.015, vol=0.05).rename("ppnenet")

    cols = {"revenue": revenue, "assets": assets, "assetsavg": assetsavg,
            "invcap": invcap, "invcapavg": invcapavg, "equity": equity,
            "ppnenet": ppnenet}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
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

    print("OK f19_capital_efficiency_base_001_075_claude: %d features pass" % n_features)
