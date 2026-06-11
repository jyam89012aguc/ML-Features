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
def _f10_dso(receivables, revenue):
    return receivables / revenue.replace(0, np.nan).abs() * 365.0


def _f10_rec_revenue_gap(receivables, revenue, w):
    rec_g = receivables.pct_change(periods=w)
    rev_g = revenue.pct_change(periods=w)
    return rec_g - rev_g


def _f10_collection_efficiency(receivables, revenue, w):
    rec_chg = receivables.diff(periods=w)
    return -rec_chg / revenue.replace(0, np.nan).abs()


# DSO max 252d * close
def f10rcq_f10_receivables_quality_dsomax_252d_base_v076_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO max 504d * close
def f10rcq_f10_receivables_quality_dsomax_504d_base_v077_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO min 252d * close
def f10rcq_f10_receivables_quality_dsomin_252d_base_v078_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO range 252d
def f10rcq_f10_receivables_quality_dsorng_252d_base_v079_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    rng = b.rolling(252, min_periods=63).max() - b.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO range 504d
def f10rcq_f10_receivables_quality_dsorng_504d_base_v080_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    rng = b.rolling(504, min_periods=126).max() - b.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile 252d
def f10rcq_f10_receivables_quality_dsopct_252d_base_v081_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile 504d
def f10rcq_f10_receivables_quality_dsopct_504d_base_v082_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((b - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO CV 21d
def f10rcq_f10_receivables_quality_dsocv_21d_base_v083_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _std(b, 21) / _mean(b, 21).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO CV 63d
def f10rcq_f10_receivables_quality_dsocv_63d_base_v084_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _std(b, 63) / _mean(b, 63).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO CV 252d
def f10rcq_f10_receivables_quality_dsocv_252d_base_v085_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _std(b, 252) / _mean(b, 252).replace(0, np.nan).abs()
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO sign deviation
def f10rcq_f10_receivables_quality_dsosign_63d_base_v086_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    dev = b - _mean(b, 252)
    result = np.sign(dev) * _std(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll sign deviation
def f10rcq_f10_receivables_quality_collsign_63d_base_v087_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    dev = c - _mean(c, 252)
    result = np.sign(dev) * _std(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite (DSO + gap) * close
def f10rcq_f10_receivables_quality_comp_21d_base_v088_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = (_mean(d, 21) / 100 + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite
def f10rcq_f10_receivables_quality_comp_63d_base_v089_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = (_mean(d, 63) / 100 + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite
def f10rcq_f10_receivables_quality_comp_252d_base_v090_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = (_mean(d, 252) / 100 + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite
def f10rcq_f10_receivables_quality_comp_504d_base_v091_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    g = _f10_rec_revenue_gap(receivables, revenue, 504)
    result = (_mean(d, 504) / 100 + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * cum close
def f10rcq_f10_receivables_quality_dsoxcumcl_63d_base_v092_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 63) * closeadj
    result = _mean(b, 63) * cv / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * cum close 252d
def f10rcq_f10_receivables_quality_dsoxcumcl_252d_base_v093_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 252) * closeadj
    result = _mean(b, 252) * cv / 100
    return result.replace([np.inf, -np.inf], np.nan)


# gap z 21d
def f10rcq_f10_receivables_quality_gapz_21d_base_v094_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap z 63d
def f10rcq_f10_receivables_quality_gapz_63d_base_v095_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = _z(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap z 252d
def f10rcq_f10_receivables_quality_gapz_252d_base_v096_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = _z(g, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap std 63d
def f10rcq_f10_receivables_quality_gapstd_63d_base_v097_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = _std(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap std 252d
def f10rcq_f10_receivables_quality_gapstd_252d_base_v098_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = _std(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap abs 63d
def f10rcq_f10_receivables_quality_gapabs_63d_base_v099_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap abs 252d
def f10rcq_f10_receivables_quality_gapabs_252d_base_v100_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap cum 252d
def f10rcq_f10_receivables_quality_gapcum_252d_base_v101_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap cum 504d
def f10rcq_f10_receivables_quality_gapcum_504d_base_v102_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# excess count: gap > 0.05 over 252d
def f10rcq_f10_receivables_quality_excesscount_252d_base_v103_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    excess = (g > 0.05).astype(float)
    result = (excess.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# excess count 504d
def f10rcq_f10_receivables_quality_excesscount_504d_base_v104_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    excess = (g > 0.05).astype(float)
    result = (excess.rolling(504, min_periods=126).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * receivables (dollar value receivables)
def f10rcq_f10_receivables_quality_dsoxrec_63d_base_v105_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b, 63) * receivables * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * receivables 252d
def f10rcq_f10_receivables_quality_dsoxrec_252d_base_v106_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = _mean(b, 252) * receivables * closeadj / 1e10
    return result.replace([np.inf, -np.inf], np.nan)


# coll * revenue 63d
def f10rcq_f10_receivables_quality_collxrev_63d_base_v107_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 63)
    result = c * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# coll * revenue 252d
def f10rcq_f10_receivables_quality_collxrev_252d_base_v108_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 252)
    result = c * revenue * closeadj / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# DSO level normalized
def f10rcq_f10_receivables_quality_dsolevel_63d_base_v109_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    norm = b / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO level normalized 252d
def f10rcq_f10_receivables_quality_dsolevel_252d_base_v110_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    norm = _mean(b, 252) / _mean(b, 504).replace(0, np.nan).abs()
    result = norm * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# gap rolling sum * gap z 252d
def f10rcq_f10_receivables_quality_gapcumz_252d_base_v111_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    base = g.rolling(252, min_periods=63).sum() + _z(g, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll z * close return
def f10rcq_f10_receivables_quality_collzxcret_21d_base_v112_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    z = _z(c, 252)
    cret = closeadj.pct_change(21)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll z * close return 63d
def f10rcq_f10_receivables_quality_collzxcret_63d_base_v113_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 63)
    z = _z(c, 252)
    cret = closeadj.pct_change(63)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll z * close return 252d
def f10rcq_f10_receivables_quality_collzxcret_252d_base_v114_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 252)
    z = _z(c, 504)
    cret = closeadj.pct_change(252)
    result = z * cret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO sqrt 252d
def f10rcq_f10_receivables_quality_dsosqrt_504d_base_v115_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue).abs()
    result = np.sqrt(_mean(b, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d DSO sqrt
def f10rcq_f10_receivables_quality_dsosqrt_21d_base_v116_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue).abs()
    result = np.sqrt(_mean(b, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Bad debt risk: gap>0 + DSO>252mean
def f10rcq_f10_receivables_quality_badrisk_252d_base_v117_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    risk = ((g > 0.05) & (d > _mean(d, 252))).astype(float)
    result = (risk.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Bad debt risk 504d
def f10rcq_f10_receivables_quality_badrisk_504d_base_v118_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    risk = ((g > 0.05) & (d > _mean(d, 252))).astype(float)
    result = (risk.rolling(504, min_periods=126).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Good quality count: gap<0 + DSO<252mean
def f10rcq_f10_receivables_quality_goodcount_252d_base_v119_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    good = ((g < -0.05) & (d < _mean(d, 252))).astype(float)
    result = (good.rolling(252, min_periods=63).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Good count 504d
def f10rcq_f10_receivables_quality_goodcount_504d_base_v120_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 21)
    d = _f10_dso(receivables, revenue)
    good = ((g < -0.05) & (d < _mean(d, 252))).astype(float)
    result = (good.rolling(504, min_periods=126).sum() + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Receivables/revenue raw ratio * close
def f10rcq_f10_receivables_quality_arar_63d_base_v121_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    result = _mean(b, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# AR/rev 252d
def f10rcq_f10_receivables_quality_arar_252d_base_v122_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    result = _mean(b, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# AR/rev 504d
def f10rcq_f10_receivables_quality_arar_504d_base_v123_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue) / 365.0
    result = _mean(b, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll long
def f10rcq_f10_receivables_quality_colllong_base_v124_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO long
def f10rcq_f10_receivables_quality_dsolong_base_v125_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rec growth - rev growth scaled 63d
def f10rcq_f10_receivables_quality_recgrwscaled_63d_base_v126_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    rev_g = revenue.pct_change(63)
    result = g / (rev_g.abs() + 0.01) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rec growth - rev growth scaled 252d
def f10rcq_f10_receivables_quality_recgrwscaled_252d_base_v127_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    rev_g = revenue.pct_change(252)
    result = g / (rev_g.abs() + 0.01) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO sign change count (events) 252d
def f10rcq_f10_receivables_quality_dsoflip_252d_base_v128_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    chg = b.diff(21)
    flips = (np.sign(chg).diff().abs() > 1).astype(float)
    result = (flips.rolling(252, min_periods=63).sum() + b) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ema gap 63v252
def f10rcq_f10_receivables_quality_dsoemagap_63v252_base_v129_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    e63 = b.ewm(span=63, adjust=False).mean()
    e252 = b.ewm(span=252, adjust=False).mean()
    result = (e63 - e252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ema gap 21v252
def f10rcq_f10_receivables_quality_dsoemagap_21v252_base_v130_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    e21 = b.ewm(span=21, adjust=False).mean()
    e252 = b.ewm(span=252, adjust=False).mean()
    result = (e21 - e252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll EMA gap
def f10rcq_f10_receivables_quality_collemagap_21v252_base_v131_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    e21 = c.ewm(span=21, adjust=False).mean()
    e252 = c.ewm(span=252, adjust=False).mean()
    result = (e21 - e252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO worst 504d
def f10rcq_f10_receivables_quality_dsoworst_504d_base_v132_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b.expanding(min_periods=126).max() / b.expanding(min_periods=126).mean().replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO best 504d
def f10rcq_f10_receivables_quality_dsobest_504d_base_v133_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = b.expanding(min_periods=126).min() / b.expanding(min_periods=126).mean().replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rec quality composite 63d (low DSO, high coll, low gap)
def f10rcq_f10_receivables_quality_qualcomp_63d_base_v134_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 63)
    g = _f10_rec_revenue_gap(receivables, revenue, 63)
    result = (-_mean(d, 63) / 100 + c - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# quality composite 252d
def f10rcq_f10_receivables_quality_qualcomp_252d_base_v135_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    result = (-_mean(d, 252) / 100 + c - g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rec * close return 21d
def f10rcq_f10_receivables_quality_dsoxret_21d_base_v136_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cret = closeadj.pct_change(21)
    result = b * cret * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * close return 252d
def f10rcq_f10_receivables_quality_dsoxret_252d_base_v137_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cret = closeadj.pct_change(252)
    result = b * cret * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * AR / rev sq
def f10rcq_f10_receivables_quality_dsoxarsq_63d_base_v138_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    ar_rev = b / 365.0
    result = _mean(b * ar_rev, 63) * closeadj / 100
    return result.replace([np.inf, -np.inf], np.nan)


# gap pct from 252d
def f10rcq_f10_receivables_quality_gappct_252d_base_v139_signal(receivables, revenue, closeadj):
    g = _f10_rec_revenue_gap(receivables, revenue, 252)
    mx = g.rolling(252, min_periods=63).max()
    mn = g.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((g - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll pct 252d
def f10rcq_f10_receivables_quality_collpct_252d_base_v140_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    mx = c.rolling(252, min_periods=63).max()
    mn = c.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    result = ((c - mn) / rng) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll max 252d
def f10rcq_f10_receivables_quality_collmax_252d_base_v141_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = c.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll min 252d
def f10rcq_f10_receivables_quality_collmin_252d_base_v142_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = c.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# coll range 252d
def f10rcq_f10_receivables_quality_collrng_252d_base_v143_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    rng = c.rolling(252, min_periods=63).max() - c.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO * volume proxy (close cum) 252d
def f10rcq_f10_receivables_quality_dsoxvolp_252d_base_v144_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    cv = _mean(closeadj, 252) * closeadj
    result = _mean(b, 252) * cv / 100
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite full
def f10rcq_f10_receivables_quality_compfull_504d_base_v145_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 252)
    g = _f10_rec_revenue_gap(receivables, revenue, 504)
    result = (_mean(d, 504) / 100 + c + g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ratio 21v504
def f10rcq_f10_receivables_quality_dsoratio_21v504_base_v146_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 21) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# DSO ratio 126v504
def f10rcq_f10_receivables_quality_dsoratio_126v504_base_v147_signal(receivables, revenue, closeadj):
    b = _f10_dso(receivables, revenue)
    result = (_mean(b, 126) / _mean(b, 504).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Coll ratio 63v252
def f10rcq_f10_receivables_quality_collratio_63v252_base_v148_signal(receivables, revenue, closeadj):
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = (_mean(c, 63) / _mean(c, 252).replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# AR risk: DSO z * coll z 63d
def f10rcq_f10_receivables_quality_riskz_63d_base_v149_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(d, 63) * _z(c, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# AR risk 252d
def f10rcq_f10_receivables_quality_riskz_252d_base_v150_signal(receivables, revenue, closeadj):
    d = _f10_dso(receivables, revenue)
    c = _f10_collection_efficiency(receivables, revenue, 21)
    result = _z(d, 252) * _z(c, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rcq_f10_receivables_quality_dsomax_252d_base_v076_signal,
    f10rcq_f10_receivables_quality_dsomax_504d_base_v077_signal,
    f10rcq_f10_receivables_quality_dsomin_252d_base_v078_signal,
    f10rcq_f10_receivables_quality_dsorng_252d_base_v079_signal,
    f10rcq_f10_receivables_quality_dsorng_504d_base_v080_signal,
    f10rcq_f10_receivables_quality_dsopct_252d_base_v081_signal,
    f10rcq_f10_receivables_quality_dsopct_504d_base_v082_signal,
    f10rcq_f10_receivables_quality_dsocv_21d_base_v083_signal,
    f10rcq_f10_receivables_quality_dsocv_63d_base_v084_signal,
    f10rcq_f10_receivables_quality_dsocv_252d_base_v085_signal,
    f10rcq_f10_receivables_quality_dsosign_63d_base_v086_signal,
    f10rcq_f10_receivables_quality_collsign_63d_base_v087_signal,
    f10rcq_f10_receivables_quality_comp_21d_base_v088_signal,
    f10rcq_f10_receivables_quality_comp_63d_base_v089_signal,
    f10rcq_f10_receivables_quality_comp_252d_base_v090_signal,
    f10rcq_f10_receivables_quality_comp_504d_base_v091_signal,
    f10rcq_f10_receivables_quality_dsoxcumcl_63d_base_v092_signal,
    f10rcq_f10_receivables_quality_dsoxcumcl_252d_base_v093_signal,
    f10rcq_f10_receivables_quality_gapz_21d_base_v094_signal,
    f10rcq_f10_receivables_quality_gapz_63d_base_v095_signal,
    f10rcq_f10_receivables_quality_gapz_252d_base_v096_signal,
    f10rcq_f10_receivables_quality_gapstd_63d_base_v097_signal,
    f10rcq_f10_receivables_quality_gapstd_252d_base_v098_signal,
    f10rcq_f10_receivables_quality_gapabs_63d_base_v099_signal,
    f10rcq_f10_receivables_quality_gapabs_252d_base_v100_signal,
    f10rcq_f10_receivables_quality_gapcum_252d_base_v101_signal,
    f10rcq_f10_receivables_quality_gapcum_504d_base_v102_signal,
    f10rcq_f10_receivables_quality_excesscount_252d_base_v103_signal,
    f10rcq_f10_receivables_quality_excesscount_504d_base_v104_signal,
    f10rcq_f10_receivables_quality_dsoxrec_63d_base_v105_signal,
    f10rcq_f10_receivables_quality_dsoxrec_252d_base_v106_signal,
    f10rcq_f10_receivables_quality_collxrev_63d_base_v107_signal,
    f10rcq_f10_receivables_quality_collxrev_252d_base_v108_signal,
    f10rcq_f10_receivables_quality_dsolevel_63d_base_v109_signal,
    f10rcq_f10_receivables_quality_dsolevel_252d_base_v110_signal,
    f10rcq_f10_receivables_quality_gapcumz_252d_base_v111_signal,
    f10rcq_f10_receivables_quality_collzxcret_21d_base_v112_signal,
    f10rcq_f10_receivables_quality_collzxcret_63d_base_v113_signal,
    f10rcq_f10_receivables_quality_collzxcret_252d_base_v114_signal,
    f10rcq_f10_receivables_quality_dsosqrt_504d_base_v115_signal,
    f10rcq_f10_receivables_quality_dsosqrt_21d_base_v116_signal,
    f10rcq_f10_receivables_quality_badrisk_252d_base_v117_signal,
    f10rcq_f10_receivables_quality_badrisk_504d_base_v118_signal,
    f10rcq_f10_receivables_quality_goodcount_252d_base_v119_signal,
    f10rcq_f10_receivables_quality_goodcount_504d_base_v120_signal,
    f10rcq_f10_receivables_quality_arar_63d_base_v121_signal,
    f10rcq_f10_receivables_quality_arar_252d_base_v122_signal,
    f10rcq_f10_receivables_quality_arar_504d_base_v123_signal,
    f10rcq_f10_receivables_quality_colllong_base_v124_signal,
    f10rcq_f10_receivables_quality_dsolong_base_v125_signal,
    f10rcq_f10_receivables_quality_recgrwscaled_63d_base_v126_signal,
    f10rcq_f10_receivables_quality_recgrwscaled_252d_base_v127_signal,
    f10rcq_f10_receivables_quality_dsoflip_252d_base_v128_signal,
    f10rcq_f10_receivables_quality_dsoemagap_63v252_base_v129_signal,
    f10rcq_f10_receivables_quality_dsoemagap_21v252_base_v130_signal,
    f10rcq_f10_receivables_quality_collemagap_21v252_base_v131_signal,
    f10rcq_f10_receivables_quality_dsoworst_504d_base_v132_signal,
    f10rcq_f10_receivables_quality_dsobest_504d_base_v133_signal,
    f10rcq_f10_receivables_quality_qualcomp_63d_base_v134_signal,
    f10rcq_f10_receivables_quality_qualcomp_252d_base_v135_signal,
    f10rcq_f10_receivables_quality_dsoxret_21d_base_v136_signal,
    f10rcq_f10_receivables_quality_dsoxret_252d_base_v137_signal,
    f10rcq_f10_receivables_quality_dsoxarsq_63d_base_v138_signal,
    f10rcq_f10_receivables_quality_gappct_252d_base_v139_signal,
    f10rcq_f10_receivables_quality_collpct_252d_base_v140_signal,
    f10rcq_f10_receivables_quality_collmax_252d_base_v141_signal,
    f10rcq_f10_receivables_quality_collmin_252d_base_v142_signal,
    f10rcq_f10_receivables_quality_collrng_252d_base_v143_signal,
    f10rcq_f10_receivables_quality_dsoxvolp_252d_base_v144_signal,
    f10rcq_f10_receivables_quality_compfull_504d_base_v145_signal,
    f10rcq_f10_receivables_quality_dsoratio_21v504_base_v146_signal,
    f10rcq_f10_receivables_quality_dsoratio_126v504_base_v147_signal,
    f10rcq_f10_receivables_quality_collratio_63v252_base_v148_signal,
    f10rcq_f10_receivables_quality_riskz_63d_base_v149_signal,
    f10rcq_f10_receivables_quality_riskz_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RECEIVABLES_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "receivables": receivables, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f10_dso", "_f10_rec_revenue_gap", "_f10_collection_efficiency")
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
    print(f"OK f10_receivables_quality_base_076_150_claude: {n_features} features pass")
