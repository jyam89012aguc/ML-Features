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


# 21d asset growth × closeadj × volume (vol-weighted growth event)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxvol_21d_base_v076_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 21)
    result = g * closeadj * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × dollar volume
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxdv_63d_base_v077_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 63)
    dv = closeadj * volume
    result = g * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × dollar volume mean
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxdv_252d_base_v078_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 252)
    dv = closeadj * volume
    result = g * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ppnenet rate-base × volume
def f01rrb_f01_regulated_rate_base_growth_ratebasexvol_21d_base_v079_signal(ppnenet, closeadj, volume):
    r = _f01_rate_base_proxy(ppnenet, 21)
    result = r * volume * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base × volume
def f01rrb_f01_regulated_rate_base_growth_ratebasexvol_252d_base_v080_signal(ppnenet, closeadj, volume):
    r = _f01_rate_base_proxy(ppnenet, 252)
    result = r * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × close (with abs)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_21d_base_v081_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21).abs()
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d abs asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_252d_base_v082_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252).abs()
    result = g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rate-base proxy × ATR
def f01rrb_f01_regulated_rate_base_growth_ratebasexatr_21d_base_v083_signal(ppnenet, closeadj, high, low):
    r = _f01_rate_base_proxy(ppnenet, 21)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = r * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base × ATR
def f01rrb_f01_regulated_rate_base_growth_ratebasexatr_252d_base_v084_signal(ppnenet, closeadj, high, low):
    r = _f01_rate_base_proxy(ppnenet, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = r * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × ATR
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxatr_63d_base_v085_signal(assets, closeadj, high, low):
    g = _f01_asset_growth(assets, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = g * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ATR
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxatr_252d_base_v086_signal(assets, closeadj, high, low):
    g = _f01_asset_growth(assets, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = g * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth volatility × close (rolling std)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_21d_base_v087_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth volatility × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_63d_base_v088_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base std × close
def f01rrb_f01_regulated_rate_base_growth_ratebasevol_252d_base_v089_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ppnenet rate-base std × close
def f01rrb_f01_regulated_rate_base_growth_ratebasevol_504d_base_v090_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 504)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality × volume mean
def f01rrb_f01_regulated_rate_base_growth_qualityxvol_63d_base_v091_signal(assets, equity, closeadj, volume):
    q = _f01_growth_quality(assets, equity, 63)
    result = q * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality × volume mean
def f01rrb_f01_regulated_rate_base_growth_qualityxvol_252d_base_v092_signal(assets, equity, closeadj, volume):
    q = _f01_growth_quality(assets, equity, 252)
    result = q * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × ev-style scaling (close × volume)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxev_21d_base_v093_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 21)
    ev = closeadj * _mean(volume, 21)
    result = g * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ev scaling
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxev_252d_base_v094_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 252)
    ev = closeadj * _mean(volume, 63)
    result = g * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling sum of asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_21d_base_v095_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    result = g.rolling(21, min_periods=5).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling sum of asset growth × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_63d_base_v096_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ppnenet rate-base log × close
def f01rrb_f01_regulated_rate_base_growth_ratebaselog_21d_base_v097_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 21)
    result = np.log(r.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base log × close
def f01rrb_f01_regulated_rate_base_growth_ratebaselog_252d_base_v098_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    result = np.log(r.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth (sign) × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsign_21d_base_v099_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    result = np.sign(g) * closeadj * _mean(closeadj, 21) / _mean(closeadj, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth sign × close × volume
def f01rrb_f01_regulated_rate_base_growth_assetgrowthsignxvol_63d_base_v100_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 63)
    result = np.sign(g) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rate-base ratio dispersion (max - min over window) × close
def f01rrb_f01_regulated_rate_base_growth_ratebaserange_21d_base_v101_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 21)
    rng = r.rolling(21, min_periods=5).max() - r.rolling(21, min_periods=5).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rate-base ratio dispersion 252d × close
def f01rrb_f01_regulated_rate_base_growth_ratebaserange_252d_base_v102_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    rng = r.rolling(63, min_periods=21).max() - r.rolling(63, min_periods=21).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × close × inv volume z
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvvol_21d_base_v103_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 21)
    result = g * closeadj / _mean(volume, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × close × inv volume z
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvvol_252d_base_v104_signal(assets, closeadj, volume):
    g = _f01_asset_growth(assets, 252)
    result = g * closeadj / _mean(volume, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ppnenet level (rate-base size)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxsize_252d_base_v105_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 252)
    s = np.log(ppnenet.abs().replace(0, np.nan))
    rb = _f01_rate_base_proxy(ppnenet, 252)
    result = g * s * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × ppnenet log × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxsize_63d_base_v106_signal(assets, ppnenet, closeadj):
    g = _f01_asset_growth(assets, 63)
    s = np.log(ppnenet.abs().replace(0, np.nan))
    rb = _f01_rate_base_proxy(ppnenet, 63)
    result = g * s * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality × ppnenet × close
def f01rrb_f01_regulated_rate_base_growth_qualityxsize_252d_base_v107_signal(assets, equity, ppnenet, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    s = np.log(ppnenet.abs().replace(0, np.nan))
    result = q * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rate-base × close × cumulative return
def f01rrb_f01_regulated_rate_base_growth_ratebasexret_21d_base_v108_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 21)
    ret = closeadj.pct_change(21)
    result = r * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base × cumulative return × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexret_252d_base_v109_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    ret = closeadj.pct_change(63)
    result = r * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × cumulative return × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxret_63d_base_v110_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    ret = closeadj.pct_change(21)
    result = g * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × cumulative return × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxret_252d_base_v111_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    ret = closeadj.pct_change(63)
    result = g * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × inverse closeadj (price-aware)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvprice_21d_base_v112_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 21)
    inv = 1.0 / closeadj.replace(0, np.nan)
    result = g * inv * _mean(closeadj, 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × inverse close × scale
def f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvprice_252d_base_v113_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    inv = 1.0 / closeadj.replace(0, np.nan)
    result = g * inv * _mean(closeadj, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality EMA × close (long span)
def f01rrb_f01_regulated_rate_base_growth_qualityema_63d_base_v114_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    sm = q.ewm(span=126, min_periods=21).mean()
    result = sm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base mean over 252d × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_252d_base_v115_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 504)
    result = _mean(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ppnenet rate-base mean × close
def f01rrb_f01_regulated_rate_base_growth_ratebasemean_504d_base_v116_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 504)
    result = _mean(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × equity ratio
def f01rrb_f01_regulated_rate_base_growth_assetxeqratio_63d_base_v117_signal(assets, equity, closeadj):
    g = _f01_asset_growth(assets, 63)
    er = _safe_div(equity, assets)
    result = g * er * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × equity ratio × close
def f01rrb_f01_regulated_rate_base_growth_assetxeqratio_252d_base_v118_signal(assets, equity, closeadj):
    g = _f01_asset_growth(assets, 252)
    er = _safe_div(equity, assets)
    result = g * er * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet rate-base × equity / assets × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexeqratio_63d_base_v119_signal(ppnenet, equity, assets, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    er = _safe_div(equity, assets)
    result = r * er * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ppnenet rate-base × equity / assets × close
def f01rrb_f01_regulated_rate_base_growth_ratebasexeqratio_252d_base_v120_signal(ppnenet, equity, assets, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    er = _safe_div(equity, assets)
    result = r * er * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset growth × ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_21d_base_v121_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 21)
    p = ppnenet.pct_change(21)
    rb = _f01_rate_base_proxy(ppnenet, 21)
    result = a * p * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_63d_base_v122_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 63)
    p = ppnenet.pct_change(63)
    rb = _f01_rate_base_proxy(ppnenet, 63)
    result = a * p * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ppnenet growth × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_252d_base_v123_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 252)
    p = ppnenet.pct_change(252)
    rb = _f01_rate_base_proxy(ppnenet, 252)
    result = a * p * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d dual growth × close
def f01rrb_f01_regulated_rate_base_growth_dualgrowth_504d_base_v124_signal(assets, ppnenet, closeadj):
    a = _f01_asset_growth(assets, 504)
    p = ppnenet.pct_change(504)
    rb = _f01_rate_base_proxy(ppnenet, 504)
    result = a * p * closeadj + rb * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth gap (current vs 252d mean)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_63d_base_v125_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    gm = _mean(g, 252)
    result = (g - gm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth gap (current vs 504d mean)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_252d_base_v126_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    gm = _mean(g, 504)
    result = (g - gm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rate-base proxy gap × close
def f01rrb_f01_regulated_rate_base_growth_ratebasegap_21d_base_v127_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 21)
    rm = _mean(r, 252)
    result = (r - rm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base proxy gap × close
def f01rrb_f01_regulated_rate_base_growth_ratebasegap_252d_base_v128_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    rm = _mean(r, 504)
    result = (r - rm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# growth quality × close vs 504d × close
def f01rrb_f01_regulated_rate_base_growth_qualitygap_252d_base_v129_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    qm = _mean(q, 504)
    result = (q - qm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality gap × close
def f01rrb_f01_regulated_rate_base_growth_qualitygap_63d_base_v130_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    qm = _mean(q, 252)
    result = (q - qm) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × close-z (price-momentum interaction)
def f01rrb_f01_regulated_rate_base_growth_assetxclosez_63d_base_v131_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    cz = _z(closeadj, 252)
    result = g * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × close z
def f01rrb_f01_regulated_rate_base_growth_assetxclosez_252d_base_v132_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    cz = _z(closeadj, 504)
    result = g * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rate-base × close z
def f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_63d_base_v133_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    cz = _z(closeadj, 252)
    result = r * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base × close z
def f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_252d_base_v134_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    cz = _z(closeadj, 504)
    result = r * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × close-pct
def f01rrb_f01_regulated_rate_base_growth_assetxretpct_63d_base_v135_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    p = closeadj.pct_change(5)
    rb = _f01_rate_base_proxy
    result = g * p * closeadj + g * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × close pct
def f01rrb_f01_regulated_rate_base_growth_assetxretpct_252d_base_v136_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    p = closeadj.pct_change(21)
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ppnenet rate-base × close pct
def f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_63d_base_v137_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    p = closeadj.pct_change(5)
    result = r * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base × close pct
def f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_252d_base_v138_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    p = closeadj.pct_change(21)
    result = r * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × abs(close pct) (vol-amplified)
def f01rrb_f01_regulated_rate_base_growth_assetxabsret_63d_base_v139_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    p = closeadj.pct_change(21).abs()
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × abs return × close
def f01rrb_f01_regulated_rate_base_growth_assetxabsret_252d_base_v140_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    p = closeadj.pct_change(63).abs()
    result = g * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality × abs return × close
def f01rrb_f01_regulated_rate_base_growth_qualityxabsret_63d_base_v141_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    p = closeadj.pct_change(21).abs()
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality × abs return × close
def f01rrb_f01_regulated_rate_base_growth_qualityxabsret_252d_base_v142_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    p = closeadj.pct_change(63).abs()
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth diff (4Q acceleration approx)
def f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_252d_base_v143_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 252)
    accel = g - g.shift(63)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth acceleration × close
def f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_63d_base_v144_signal(assets, closeadj):
    g = _f01_asset_growth(assets, 63)
    accel = g - g.shift(21)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate-base acceleration × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_252d_base_v145_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 252)
    accel = r - r.shift(63)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rate-base acceleration × close
def f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_63d_base_v146_signal(ppnenet, closeadj):
    r = _f01_rate_base_proxy(ppnenet, 63)
    accel = r - r.shift(21)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth quality acceleration × close
def f01rrb_f01_regulated_rate_base_growth_qualityaccel_252d_base_v147_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 252)
    accel = q - q.shift(63)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth quality acceleration × close
def f01rrb_f01_regulated_rate_base_growth_qualityaccel_63d_base_v148_signal(assets, equity, closeadj):
    q = _f01_growth_quality(assets, equity, 63)
    accel = q - q.shift(21)
    result = accel * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset growth × ppnenet rate-base × volume mean
def f01rrb_f01_regulated_rate_base_growth_combonexvol_252d_base_v149_signal(assets, ppnenet, closeadj, volume):
    a = _f01_asset_growth(assets, 252)
    r = _f01_rate_base_proxy(ppnenet, 252)
    result = a * r * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset growth × rate-base × volume × close
def f01rrb_f01_regulated_rate_base_growth_combonexvol_63d_base_v150_signal(assets, ppnenet, closeadj, volume):
    a = _f01_asset_growth(assets, 63)
    r = _f01_rate_base_proxy(ppnenet, 63)
    result = a * r * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxvol_21d_base_v076_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxdv_63d_base_v077_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxdv_252d_base_v078_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexvol_21d_base_v079_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexvol_252d_base_v080_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_21d_base_v081_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthabs_252d_base_v082_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexatr_21d_base_v083_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexatr_252d_base_v084_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxatr_63d_base_v085_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxatr_252d_base_v086_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_21d_base_v087_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthvol_63d_base_v088_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasevol_252d_base_v089_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasevol_504d_base_v090_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxvol_63d_base_v091_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxvol_252d_base_v092_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxev_21d_base_v093_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxev_252d_base_v094_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_21d_base_v095_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsum_63d_base_v096_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaselog_21d_base_v097_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaselog_252d_base_v098_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsign_21d_base_v099_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthsignxvol_63d_base_v100_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaserange_21d_base_v101_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaserange_252d_base_v102_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvvol_21d_base_v103_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvvol_252d_base_v104_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxsize_252d_base_v105_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxsize_63d_base_v106_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxsize_252d_base_v107_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexret_21d_base_v108_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexret_252d_base_v109_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxret_63d_base_v110_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxret_252d_base_v111_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvprice_21d_base_v112_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthxinvprice_252d_base_v113_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityema_63d_base_v114_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_252d_base_v115_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasemean_504d_base_v116_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxeqratio_63d_base_v117_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxeqratio_252d_base_v118_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexeqratio_63d_base_v119_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexeqratio_252d_base_v120_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_21d_base_v121_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_63d_base_v122_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_252d_base_v123_signal,
    f01rrb_f01_regulated_rate_base_growth_dualgrowth_504d_base_v124_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_63d_base_v125_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthgap_252d_base_v126_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasegap_21d_base_v127_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasegap_252d_base_v128_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitygap_252d_base_v129_signal,
    f01rrb_f01_regulated_rate_base_growth_qualitygap_63d_base_v130_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxclosez_63d_base_v131_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxclosez_252d_base_v132_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_63d_base_v133_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexclosez_252d_base_v134_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxretpct_63d_base_v135_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxretpct_252d_base_v136_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_63d_base_v137_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebasexretpct_252d_base_v138_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxabsret_63d_base_v139_signal,
    f01rrb_f01_regulated_rate_base_growth_assetxabsret_252d_base_v140_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxabsret_63d_base_v141_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityxabsret_252d_base_v142_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_252d_base_v143_signal,
    f01rrb_f01_regulated_rate_base_growth_assetgrowthaccel_63d_base_v144_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_252d_base_v145_signal,
    f01rrb_f01_regulated_rate_base_growth_ratebaseaccel_63d_base_v146_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityaccel_252d_base_v147_signal,
    f01rrb_f01_regulated_rate_base_growth_qualityaccel_63d_base_v148_signal,
    f01rrb_f01_regulated_rate_base_growth_combonexvol_252d_base_v149_signal,
    f01rrb_f01_regulated_rate_base_growth_combonexvol_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F01_REGULATED_RATE_BASE_GROWTH_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f01_regulated_rate_base_growth_base_076_150_claude: {n_features} features pass")
