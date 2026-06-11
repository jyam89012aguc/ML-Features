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
# asset turnover smoothed over a half-year (durable level, distinct EMA span)
def f19ce_f19_capital_efficiency_aturnema_126d_base_v076_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover smoothed over a half-year EMA
def f19ce_f19_capital_efficiency_eturnema_126d_base_v077_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = t.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover smoothed over a quarter EMA
def f19ce_f19_capital_efficiency_fturnema_63d_base_v078_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = t.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover z-scored over a longer 504d window (slow regime de-trend)
def f19ce_f19_capital_efficiency_aturnz_504d_base_v079_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = _z(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover z-scored over a longer 504d window
def f19ce_f19_capital_efficiency_eturnz_504d_base_v080_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = _z(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover z over 504d window
def f19ce_f19_capital_efficiency_icturnz_504d_base_v081_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = _z(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover regime spread: 63d EMA minus 252d EMA (fast-vs-slow efficiency)
def f19ce_f19_capital_efficiency_aturnregspr_base_v082_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t.ewm(span=63, min_periods=21).mean() - t.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-turnover regime spread: 63d EMA minus 252d EMA
def f19ce_f19_capital_efficiency_icturnregspr_base_v083_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = t.ewm(span=63, min_periods=21).mean() - t.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-turnover regime spread: 63d EMA minus 252d EMA
def f19ce_f19_capital_efficiency_fturnregspr_base_v084_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = t.ewm(span=63, min_periods=21).mean() - t.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover relative to its 504d mean (long-run efficiency gap)
def f19ce_f19_capital_efficiency_aturnrelmean_504d_base_v085_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t / _mean(t, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover relative to its 504d mean
def f19ce_f19_capital_efficiency_eturnrelmean_504d_base_v086_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = t / _mean(t, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed turnover percentile-ranked vs 504d history (long-run plant-efficiency percentile)
def f19ce_f19_capital_efficiency_fturnrelmean_504d_base_v087_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover position within its 504d hi-lo band (long-range efficiency position)
def f19ce_f19_capital_efficiency_aturnpos_504d_base_v088_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    hi = t.rolling(504, min_periods=252).max()
    lo = t.rolling(504, min_periods=252).min()
    b = (t - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover position within its 504d band
def f19ce_f19_capital_efficiency_eturnpos_504d_base_v089_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    hi = t.rolling(504, min_periods=252).max()
    lo = t.rolling(504, min_periods=252).min()
    b = (t - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed turnover gap to its 504d max (long-run utilization headroom)
def f19ce_f19_capital_efficiency_fturngap_504d_base_v090_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    mx = t.rolling(504, min_periods=252).max()
    b = t / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-assets x revenue-to-invcap product (joint efficiency intensity, ranked)
def f19ce_f19_capital_efficiency_jointeff_base_v091_signal(revenue, assets, invcap):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    b = _rank(a * i, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-invcap turnover ratio (financing-mix efficiency wedge, ranked)
def f19ce_f19_capital_efficiency_eicratio_base_v092_signal(revenue, equity, invcap):
    e = _f19_equity_turn(revenue, equity)
    i = _f19_invcap_turn(revenue, invcap)
    b = _rank(e / i.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover skewness over 252d (asymmetry of efficiency distribution)
def f19ce_f19_capital_efficiency_aturnskew_252d_base_v093_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-turnover kurtosis over 252d (tail-heaviness of efficiency)
def f19ce_f19_capital_efficiency_icturnkurt_252d_base_v094_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = t.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset-turnover skewness over 252d
def f19ce_f19_capital_efficiency_fturnskew_252d_base_v095_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = t.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover 63d growth (level momentum, distinct from derivative-file slope)
def f19ce_f19_capital_efficiency_aturngro_63d_base_v096_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t / t.shift(63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover 63d growth
def f19ce_f19_capital_efficiency_eturngro_63d_base_v097_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = t / t.shift(63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-turnover 63d growth
def f19ce_f19_capital_efficiency_fturngro_63d_base_v098_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = t / t.shift(63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus asset growth (efficiency-improving growth, 126d)
def f19ce_f19_capital_efficiency_revvsasset_126d_base_v099_signal(revenue, assets):
    rg = revenue / revenue.shift(126) - 1.0
    ag = assets / assets.shift(126) - 1.0
    b = rg - ag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus invcap growth (capital-light growth, 126d)
def f19ce_f19_capital_efficiency_revvsic_126d_base_v100_signal(revenue, invcap):
    rg = revenue / revenue.shift(126) - 1.0
    ig = invcap / invcap.shift(126) - 1.0
    b = rg - ig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus equity growth (equity-efficient growth, 126d)
def f19ce_f19_capital_efficiency_revvseq_126d_base_v101_signal(revenue, equity):
    rg = revenue / revenue.shift(126) - 1.0
    eg = equity / equity.shift(126) - 1.0
    b = rg - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus ppnenet growth (asset-light vs plant growth, 126d)
def f19ce_f19_capital_efficiency_revvsppne_126d_base_v102_signal(revenue, ppnenet):
    rg = revenue / revenue.shift(126) - 1.0
    pg = ppnenet / ppnenet.shift(126) - 1.0
    b = rg - pg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover hit-rate above its 252d median over the last half-year
def f19ce_f19_capital_efficiency_aturnhitmed_126d_base_v103_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    med = t.rolling(252, min_periods=126).median()
    above = (t > med).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover hit-rate above its 252d median over the last half-year
def f19ce_f19_capital_efficiency_icturnhitmed_126d_base_v104_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    med = t.rolling(252, min_periods=126).median()
    above = (t > med).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-intensity hit-rate below median (capital-lightening regime)
def f19ce_f19_capital_efficiency_capinthitlo_126d_base_v105_signal(ppnenet, assets):
    c = _f19_capint(ppnenet, assets)
    med = c.rolling(252, min_periods=126).median()
    below = (c < med).astype(float)
    b = below.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-measure cross-sectional max (best-of efficiency across capital bases)
def f19ce_f19_capital_efficiency_bestturn_base_v106_signal(revenue, assets, invcap, equity):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    e = _f19_equity_turn(revenue, equity)
    best = pd.concat([a, i, e], axis=1).max(axis=1)
    b = _z(best, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-measure cross-sectional min (worst-of efficiency, z-scored)
def f19ce_f19_capital_efficiency_worstturn_base_v107_signal(revenue, assets, invcap, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    f = _f19_fixed_turn(revenue, ppnenet)
    worst = pd.concat([a, i, f], axis=1).min(axis=1)
    b = _z(worst, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-measure relative range, z-scored over 252d (efficiency-disagreement extremity)
def f19ce_f19_capital_efficiency_turnrange_base_v108_signal(revenue, assets, invcap, equity, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    e = _f19_equity_turn(revenue, equity)
    f = _f19_fixed_turn(revenue, ppnenet)
    cat = pd.concat([a, i, e, f], axis=1)
    rng = (cat.max(axis=1) - cat.min(axis=1)) / cat.mean(axis=1).replace(0, np.nan)
    b = _z(rng, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover EMA displacement ranked (durable efficiency surprise percentile)
def f19ce_f19_capital_efficiency_aturndisprank_base_v109_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    disp = t - t.ewm(span=126, min_periods=42).mean()
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover EMA displacement ranked
def f19ce_f19_capital_efficiency_eturndisprank_base_v110_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    disp = t - t.ewm(span=126, min_periods=42).mean()
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital share of assets relative to its 252d mean (capital-mix drift)
def f19ce_f19_capital_efficiency_icsharerel_252d_base_v111_signal(invcap, assets):
    s = invcap / assets.replace(0, np.nan)
    b = s / _mean(s, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity share of invested capital z-scored (self-funding mix, de-trended)
def f19ce_f19_capital_efficiency_eqicsharez_252d_base_v112_signal(equity, invcap):
    s = equity / invcap.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet share of invested capital (fixed-capital intensity within invcap)
def f19ce_f19_capital_efficiency_ppneicshare_base_v113_signal(ppnenet, invcap):
    b = ppnenet / invcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet share of invested capital ranked vs 504d history (capital-light percentile)
def f19ce_f19_capital_efficiency_ppneicsharerank_base_v114_signal(ppnenet, invcap):
    s = ppnenet / invcap.replace(0, np.nan)
    b = -_rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spot-vs-average asset turnover wedge ranked (efficiency-timing percentile)
def f19ce_f19_capital_efficiency_aspotavgrank_base_v115_signal(revenue, assets, assetsavg):
    s = _f19_asset_turn(revenue, assets)
    a = revenue / assetsavg.replace(0, np.nan)
    b = _rank(s - a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spot-vs-average invcap turnover wedge z-scored
def f19ce_f19_capital_efficiency_icspotavgz_base_v116_signal(revenue, invcap, invcapavg):
    s = _f19_invcap_turn(revenue, invcap)
    a = revenue / invcapavg.replace(0, np.nan)
    b = _z(s - a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average-based asset turnover stability (inverse CoV over 252d)
def f19ce_f19_capital_efficiency_aturnavgstab_252d_base_v117_signal(revenue, assetsavg):
    t = revenue / assetsavg.replace(0, np.nan)
    b = _mean(t, 252) / _std(t, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average-based invcap turnover CoV (instability of average-capital efficiency)
def f19ce_f19_capital_efficiency_icturnavgvol_126d_base_v118_signal(revenue, invcapavg):
    t = revenue / invcapavg.replace(0, np.nan)
    b = _std(t, 126) / _mean(t, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover downside semi-deviation (efficiency downside risk over 252d)
def f19ce_f19_capital_efficiency_aturnsemidev_252d_base_v119_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    m = _mean(t, 252)
    down = (t - m).clip(upper=0.0)
    b = (down ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-turnover upside semi-deviation (efficiency upside dispersion)
def f19ce_f19_capital_efficiency_fturnupdev_252d_base_v120_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    m = _mean(t, 252)
    up = (t - m).clip(lower=0.0)
    b = (up ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover persistence: autocorrelation of 21d turnover changes over 252d
def f19ce_f19_capital_efficiency_aturnac_252d_base_v121_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    d = t.diff(21)

    def _ac(a):
        x = a[:-1]
        y = a[1:]
        if np.std(x) == 0 or np.std(y) == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    b = d.rolling(252, min_periods=126).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover efficiency-ratio: net asset-turnover change over sum of abs changes (trend purity)
def f19ce_f19_capital_efficiency_aturneff_252d_base_v122_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    net = (t - t.shift(252)).abs()
    path = t.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-turnover efficiency-ratio (trend purity of invested-capital efficiency)
def f19ce_f19_capital_efficiency_icturneff_252d_base_v123_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    net = (t - t.shift(252)).abs()
    path = t.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover year-over-year level change (annual efficiency improvement)
def f19ce_f19_capital_efficiency_aturnyoy_252d_base_v124_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover year-over-year level change
def f19ce_f19_capital_efficiency_icturnyoy_252d_base_v125_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover year-over-year change scaled by its 252d std (standardized YoY)
def f19ce_f19_capital_efficiency_fturnyoy_252d_base_v126_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    b = (t - t.shift(252)) / _std(t, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont equity-multiplier contribution: asset-turnover weighted by leverage, ranked vs 504d
def f19ce_f19_capital_efficiency_dupont_base_v127_signal(revenue, assets, equity):
    a = _f19_asset_turn(revenue, assets)
    lev = assets / equity.replace(0, np.nan)
    score = a * (lev ** 2)
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial leverage level (assets/equity), z-scored (capital-structure context)
def f19ce_f19_capital_efficiency_lev_252d_base_v128_signal(assets, equity):
    lev = assets / equity.replace(0, np.nan)
    b = _z(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial leverage relative to its 252d median (deleveraging/leveraging gap)
def f19ce_f19_capital_efficiency_levrel_252d_base_v129_signal(assets, equity):
    lev = assets / equity.replace(0, np.nan)
    med = lev.rolling(252, min_periods=126).median()
    b = lev / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover composite: equally-weighted z of asset, invcap, fixed turnover (broad efficiency z)
def f19ce_f19_capital_efficiency_compzsum_base_v130_signal(revenue, assets, invcap, ppnenet):
    za = _z(_f19_asset_turn(revenue, assets), 252)
    zi = _z(_f19_invcap_turn(revenue, invcap), 252)
    zf = _z(_f19_fixed_turn(revenue, ppnenet), 252)
    b = (za + zi + zf) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover composite dispersion: std of the three turnover z-scores (efficiency disagreement)
def f19ce_f19_capital_efficiency_compzdisp_base_v131_signal(revenue, assets, invcap, equity):
    za = _z(_f19_asset_turn(revenue, assets), 252)
    zi = _z(_f19_invcap_turn(revenue, invcap), 252)
    ze = _z(_f19_equity_turn(revenue, equity), 252)
    b = pd.concat([za, zi, ze], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover EWMA-volatility ratio: short-EWMA std over long-EWMA std (vol-of-efficiency)
def f19ce_f19_capital_efficiency_aturnvolratio_base_v132_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    vs = _std(t, 63)
    vl = _std(t, 252)
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover short/long vol ratio
def f19ce_f19_capital_efficiency_icturnvolratio_base_v133_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    vs = _std(t, 63)
    vl = _std(t, 252)
    b = vs / vl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover distance to its 252d min (cushion above worst efficiency)
def f19ce_f19_capital_efficiency_aturncushion_252d_base_v134_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    mn = t.rolling(252, min_periods=126).min()
    b = t / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset turnover distance to its 252d min, z-scored over 126d (cushion extremity)
def f19ce_f19_capital_efficiency_fturncushion_252d_base_v135_signal(revenue, ppnenet):
    t = _f19_fixed_turn(revenue, ppnenet)
    mn = t.rolling(252, min_periods=126).min()
    cush = t / mn.replace(0, np.nan) - 1.0
    b = _z(cush, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-intensity trend purity: net change over path of ppnenet/assets (252d efficiency ratio)
def f19ce_f19_capital_efficiency_capinteff_252d_base_v136_signal(ppnenet, assets):
    c = _f19_capint(ppnenet, assets)
    net = (c - c.shift(252)).abs()
    path = c.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover above-vs-below 252d mean asymmetry (efficiency regime balance)
def f19ce_f19_capital_efficiency_aturnasym_252d_base_v137_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    m = _mean(t, 252)
    up = (t > m).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover above-vs-below 252d mean asymmetry
def f19ce_f19_capital_efficiency_eturnasym_252d_base_v138_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    m = _mean(t, 252)
    up = (t > m).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-spread (invcap minus fixed) z-scored over 252d (capital-allocation wedge)
def f19ce_f19_capital_efficiency_icfsprz_252d_base_v139_signal(revenue, invcap, ppnenet):
    i = _f19_invcap_turn(revenue, invcap)
    f = _f19_fixed_turn(revenue, ppnenet)
    b = _z(i - f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-vs-equity turnover spread momentum: 63d change of (asset-turn minus equity-turn)
def f19ce_f19_capital_efficiency_aesprrank_504d_base_v140_signal(revenue, assets, equity):
    a = _f19_asset_turn(revenue, assets)
    e = _f19_equity_turn(revenue, equity)
    spr = a - e
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover EMA-crossover momentum: 21d change of (level minus 252d EMA) displacement
def f19ce_f19_capital_efficiency_aturnsmdisp_base_v141_signal(revenue, assets):
    t = _f19_asset_turn(revenue, assets)
    disp = t - t.ewm(span=252, min_periods=84).mean()
    b = disp - disp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap turnover smoothed displacement scaled by std
def f19ce_f19_capital_efficiency_icturnsmdisp_base_v142_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    disp = t - t.ewm(span=252, min_periods=84).mean()
    b = disp / _std(t, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined turnover momentum: mean of 63d growth across asset/invcap/equity turnover
def f19ce_f19_capital_efficiency_combmom_base_v143_signal(revenue, assets, invcap, equity):
    ga = _f19_asset_turn(revenue, assets)
    gi = _f19_invcap_turn(revenue, invcap)
    ge = _f19_equity_turn(revenue, equity)
    ma = ga / ga.shift(63) - 1.0
    mi = gi / gi.shift(63) - 1.0
    me = ge / ge.shift(63) - 1.0
    b = pd.concat([ma, mi, me], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover vs assetsavg-based turnover ratio (point-vs-average efficiency ratio)
def f19ce_f19_capital_efficiency_spotavgratio_base_v144_signal(revenue, assets, assetsavg):
    s = _f19_asset_turn(revenue, assets)
    a = revenue / assetsavg.replace(0, np.nan)
    b = s / a.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover percentile within 252d band, displacement from 0.5 (centered rank)
def f19ce_f19_capital_efficiency_eturnctrrank_252d_base_v145_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    b = _rank(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-improvement breadth (magnitude-weighted): mean 126d log-growth across three measures
def f19ce_f19_capital_efficiency_imprvbreadth_base_v146_signal(revenue, assets, invcap, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    f = _f19_fixed_turn(revenue, ppnenet)
    la = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    li = np.log(i.replace(0, np.nan) / i.shift(126).replace(0, np.nan))
    lf = np.log(f.replace(0, np.nan) / f.shift(126).replace(0, np.nan))
    b = np.sign(la) + np.sign(li) + np.sign(lf) + 2.0 * (la + li + lf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-efficiency composite gap: asset-turn-z minus capital-intensity-z (net light z)
def f19ce_f19_capital_efficiency_lightz_base_v147_signal(revenue, assets, ppnenet):
    za = _z(_f19_asset_turn(revenue, assets), 252)
    zc = _z(_f19_capint(ppnenet, assets), 252)
    b = za - zc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invcap-turnover minus its 504d EMA, ranked (long-horizon efficiency surprise)
def f19ce_f19_capital_efficiency_icturnlongdisp_base_v148_signal(revenue, invcap):
    t = _f19_invcap_turn(revenue, invcap)
    disp = t - t.ewm(span=504, min_periods=168).mean()
    b = _rank(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover trend-purity (net YoY change over path of daily changes)
def f19ce_f19_capital_efficiency_eturneff_252d_base_v149_signal(revenue, equity):
    t = _f19_equity_turn(revenue, equity)
    net = (t - t.shift(252)).abs()
    path = t.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-measure efficiency harmonic mean z-scored (combined floor efficiency, de-trended)
def f19ce_f19_capital_efficiency_harmallz_base_v150_signal(revenue, assets, invcap, equity, ppnenet):
    a = _f19_asset_turn(revenue, assets)
    i = _f19_invcap_turn(revenue, invcap)
    e = _f19_equity_turn(revenue, equity)
    f = _f19_fixed_turn(revenue, ppnenet)
    inv = (1.0 / a.replace(0, np.nan) + 1.0 / i.replace(0, np.nan)
           + 1.0 / e.replace(0, np.nan) + 1.0 / f.replace(0, np.nan))
    h = 4.0 / inv
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ce_f19_capital_efficiency_aturnema_126d_base_v076_signal,
    f19ce_f19_capital_efficiency_eturnema_126d_base_v077_signal,
    f19ce_f19_capital_efficiency_fturnema_63d_base_v078_signal,
    f19ce_f19_capital_efficiency_aturnz_504d_base_v079_signal,
    f19ce_f19_capital_efficiency_eturnz_504d_base_v080_signal,
    f19ce_f19_capital_efficiency_icturnz_504d_base_v081_signal,
    f19ce_f19_capital_efficiency_aturnregspr_base_v082_signal,
    f19ce_f19_capital_efficiency_icturnregspr_base_v083_signal,
    f19ce_f19_capital_efficiency_fturnregspr_base_v084_signal,
    f19ce_f19_capital_efficiency_aturnrelmean_504d_base_v085_signal,
    f19ce_f19_capital_efficiency_eturnrelmean_504d_base_v086_signal,
    f19ce_f19_capital_efficiency_fturnrelmean_504d_base_v087_signal,
    f19ce_f19_capital_efficiency_aturnpos_504d_base_v088_signal,
    f19ce_f19_capital_efficiency_eturnpos_504d_base_v089_signal,
    f19ce_f19_capital_efficiency_fturngap_504d_base_v090_signal,
    f19ce_f19_capital_efficiency_jointeff_base_v091_signal,
    f19ce_f19_capital_efficiency_eicratio_base_v092_signal,
    f19ce_f19_capital_efficiency_aturnskew_252d_base_v093_signal,
    f19ce_f19_capital_efficiency_icturnkurt_252d_base_v094_signal,
    f19ce_f19_capital_efficiency_fturnskew_252d_base_v095_signal,
    f19ce_f19_capital_efficiency_aturngro_63d_base_v096_signal,
    f19ce_f19_capital_efficiency_eturngro_63d_base_v097_signal,
    f19ce_f19_capital_efficiency_fturngro_63d_base_v098_signal,
    f19ce_f19_capital_efficiency_revvsasset_126d_base_v099_signal,
    f19ce_f19_capital_efficiency_revvsic_126d_base_v100_signal,
    f19ce_f19_capital_efficiency_revvseq_126d_base_v101_signal,
    f19ce_f19_capital_efficiency_revvsppne_126d_base_v102_signal,
    f19ce_f19_capital_efficiency_aturnhitmed_126d_base_v103_signal,
    f19ce_f19_capital_efficiency_icturnhitmed_126d_base_v104_signal,
    f19ce_f19_capital_efficiency_capinthitlo_126d_base_v105_signal,
    f19ce_f19_capital_efficiency_bestturn_base_v106_signal,
    f19ce_f19_capital_efficiency_worstturn_base_v107_signal,
    f19ce_f19_capital_efficiency_turnrange_base_v108_signal,
    f19ce_f19_capital_efficiency_aturndisprank_base_v109_signal,
    f19ce_f19_capital_efficiency_eturndisprank_base_v110_signal,
    f19ce_f19_capital_efficiency_icsharerel_252d_base_v111_signal,
    f19ce_f19_capital_efficiency_eqicsharez_252d_base_v112_signal,
    f19ce_f19_capital_efficiency_ppneicshare_base_v113_signal,
    f19ce_f19_capital_efficiency_ppneicsharerank_base_v114_signal,
    f19ce_f19_capital_efficiency_aspotavgrank_base_v115_signal,
    f19ce_f19_capital_efficiency_icspotavgz_base_v116_signal,
    f19ce_f19_capital_efficiency_aturnavgstab_252d_base_v117_signal,
    f19ce_f19_capital_efficiency_icturnavgvol_126d_base_v118_signal,
    f19ce_f19_capital_efficiency_aturnsemidev_252d_base_v119_signal,
    f19ce_f19_capital_efficiency_fturnupdev_252d_base_v120_signal,
    f19ce_f19_capital_efficiency_aturnac_252d_base_v121_signal,
    f19ce_f19_capital_efficiency_aturneff_252d_base_v122_signal,
    f19ce_f19_capital_efficiency_icturneff_252d_base_v123_signal,
    f19ce_f19_capital_efficiency_aturnyoy_252d_base_v124_signal,
    f19ce_f19_capital_efficiency_icturnyoy_252d_base_v125_signal,
    f19ce_f19_capital_efficiency_fturnyoy_252d_base_v126_signal,
    f19ce_f19_capital_efficiency_dupont_base_v127_signal,
    f19ce_f19_capital_efficiency_lev_252d_base_v128_signal,
    f19ce_f19_capital_efficiency_levrel_252d_base_v129_signal,
    f19ce_f19_capital_efficiency_compzsum_base_v130_signal,
    f19ce_f19_capital_efficiency_compzdisp_base_v131_signal,
    f19ce_f19_capital_efficiency_aturnvolratio_base_v132_signal,
    f19ce_f19_capital_efficiency_icturnvolratio_base_v133_signal,
    f19ce_f19_capital_efficiency_aturncushion_252d_base_v134_signal,
    f19ce_f19_capital_efficiency_fturncushion_252d_base_v135_signal,
    f19ce_f19_capital_efficiency_capinteff_252d_base_v136_signal,
    f19ce_f19_capital_efficiency_aturnasym_252d_base_v137_signal,
    f19ce_f19_capital_efficiency_eturnasym_252d_base_v138_signal,
    f19ce_f19_capital_efficiency_icfsprz_252d_base_v139_signal,
    f19ce_f19_capital_efficiency_aesprrank_504d_base_v140_signal,
    f19ce_f19_capital_efficiency_aturnsmdisp_base_v141_signal,
    f19ce_f19_capital_efficiency_icturnsmdisp_base_v142_signal,
    f19ce_f19_capital_efficiency_combmom_base_v143_signal,
    f19ce_f19_capital_efficiency_spotavgratio_base_v144_signal,
    f19ce_f19_capital_efficiency_eturnctrrank_252d_base_v145_signal,
    f19ce_f19_capital_efficiency_imprvbreadth_base_v146_signal,
    f19ce_f19_capital_efficiency_lightz_base_v147_signal,
    f19ce_f19_capital_efficiency_icturnlongdisp_base_v148_signal,
    f19ce_f19_capital_efficiency_eturneff_252d_base_v149_signal,
    f19ce_f19_capital_efficiency_harmallz_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_CAPITAL_EFFICIENCY_REGISTRY_076_150 = REGISTRY


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

    print("OK f19_capital_efficiency_base_076_150_claude: %d features pass" % n_features)
