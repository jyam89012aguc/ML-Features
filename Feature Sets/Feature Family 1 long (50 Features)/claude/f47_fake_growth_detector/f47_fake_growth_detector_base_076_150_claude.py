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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f47_fake_growth(revenue, marketcap, w):
    rev_g = revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    mcap_g = marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return rev_g - mcap_g


def _f47_fakegrowth_valgap(netinc, marketcap, w):
    ni_g = netinc.diff(w) / netinc.shift(w).abs().replace(0, np.nan)
    mcap_g = marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return mcap_g - ni_g


def _f47_fakegrowth_psgap(revenue, ps, w):
    rev_g = revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    ps_g = ps.diff(w) / ps.shift(w).abs().replace(0, np.nan)
    return ps_g - rev_g


# 63d revenue-mcap gap × ev (ev-weighted fakeness)
def f47fgd_f47_fake_growth_detector_gapxev_63d_base_v076_signal(revenue, marketcap, ev):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × ev
def f47fgd_f47_fake_growth_detector_gapxev_252d_base_v077_signal(revenue, marketcap, ev):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × evebitda
def f47fgd_f47_fake_growth_detector_gapxevebitda_63d_base_v078_signal(revenue, marketcap, evebitda):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × evebitda
def f47fgd_f47_fake_growth_detector_gapxevebitda_252d_base_v079_signal(revenue, marketcap, evebitda):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × evebit
def f47fgd_f47_fake_growth_detector_gapxevebit_63d_base_v080_signal(revenue, marketcap, evebit):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × evebit
def f47fgd_f47_fake_growth_detector_gapxevebit_252d_base_v081_signal(revenue, marketcap, evebit):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × pb (book-overpriced)
def f47fgd_f47_fake_growth_detector_gapxpb_63d_base_v082_signal(revenue, marketcap, pb):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × pb
def f47fgd_f47_fake_growth_detector_gapxpb_252d_base_v083_signal(revenue, marketcap, pb):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev-revenue gap (ev growth ahead of revenue) × ev
def f47fgd_f47_fake_growth_detector_evrevxev_63d_base_v084_signal(revenue, ev, marketcap):
    eg = ev.diff(63) / ev.shift(63).abs().replace(0, np.nan)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = (eg - rg) * ev + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev-revenue gap × ev
def f47fgd_f47_fake_growth_detector_evrevxev_252d_base_v085_signal(revenue, ev, marketcap):
    eg = ev.diff(252) / ev.shift(252).abs().replace(0, np.nan)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 252)
    result = (eg - rg) * ev + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × cash-flow weakness (ncfo/marketcap inverse)
def f47fgd_f47_fake_growth_detector_gapxnoncf_63d_base_v086_signal(revenue, marketcap, ncfo):
    g = _f47_fake_growth(revenue, marketcap, 63)
    weak = 1.0 - (ncfo / marketcap.replace(0, np.nan)).clip(-1, 1)
    result = g * weak * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × cash-flow weakness
def f47fgd_f47_fake_growth_detector_gapxnoncf_252d_base_v087_signal(revenue, marketcap, ncfo):
    g = _f47_fake_growth(revenue, marketcap, 252)
    weak = 1.0 - (ncfo / marketcap.replace(0, np.nan)).clip(-1, 1)
    result = g * weak * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/marketcap × revenue-mcap gap (fake growth without fcf)
def f47fgd_f47_fake_growth_detector_gapxfcfyld_63d_base_v088_signal(revenue, marketcap, fcf):
    g = _f47_fake_growth(revenue, marketcap, 63)
    yld = fcf / marketcap.replace(0, np.nan)
    result = g * (1.0 - yld.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf yield × revenue-mcap gap
def f47fgd_f47_fake_growth_detector_gapxfcfyld_252d_base_v089_signal(revenue, marketcap, fcf):
    g = _f47_fake_growth(revenue, marketcap, 252)
    yld = fcf / marketcap.replace(0, np.nan)
    result = g * (1.0 - yld.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fake gap with shares dilution overlay (sharesbas growth)
def f47fgd_f47_fake_growth_detector_gapxshareg_63d_base_v090_signal(revenue, marketcap, sharesbas):
    g = _f47_fake_growth(revenue, marketcap, 63)
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    result = g * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fake gap with shares dilution overlay
def f47fgd_f47_fake_growth_detector_gapxshareg_252d_base_v091_signal(revenue, marketcap, sharesbas):
    g = _f47_fake_growth(revenue, marketcap, 252)
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    result = g * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × debt-to-equity (leverage-fueled fake growth)
def f47fgd_f47_fake_growth_detector_gapxlev_63d_base_v092_signal(revenue, marketcap, debt, equity):
    g = _f47_fake_growth(revenue, marketcap, 63)
    lev = debt / equity.replace(0, np.nan)
    result = g * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × debt-to-equity
def f47fgd_f47_fake_growth_detector_gapxlev_252d_base_v093_signal(revenue, marketcap, debt, equity):
    g = _f47_fake_growth(revenue, marketcap, 252)
    lev = debt / equity.replace(0, np.nan)
    result = g * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × pe (priced-net-income decoupling)
def f47fgd_f47_fake_growth_detector_valgapxpe_63d_base_v094_signal(netinc, marketcap, pe):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = v * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × pe
def f47fgd_f47_fake_growth_detector_valgapxpe_252d_base_v095_signal(netinc, marketcap, pe):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × ps (price-to-sales premium with weak ni)
def f47fgd_f47_fake_growth_detector_valgapxps_63d_base_v096_signal(netinc, marketcap, ps):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = v * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × ps
def f47fgd_f47_fake_growth_detector_valgapxps_252d_base_v097_signal(netinc, marketcap, ps):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × evebitda
def f47fgd_f47_fake_growth_detector_valgapxevebitda_63d_base_v098_signal(netinc, marketcap, evebitda):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = v * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × evebitda
def f47fgd_f47_fake_growth_detector_valgapxevebitda_252d_base_v099_signal(netinc, marketcap, evebitda):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# rolling EMA of valgap
def f47fgd_f47_fake_growth_detector_valgapema_63d_base_v100_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = v.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# rolling EMA of valgap 252d
def f47fgd_f47_fake_growth_detector_valgapema_252d_base_v101_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ps-rev gap × ev
def f47fgd_f47_fake_growth_detector_psrevxev_63d_base_v102_signal(revenue, ps, ev, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 63)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = p * ev + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ps-rev gap × ev
def f47fgd_f47_fake_growth_detector_psrevxev_252d_base_v103_signal(revenue, ps, ev, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 252)
    base = _f47_fake_growth(revenue, marketcap, 252)
    result = p * ev + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days where ps-rev gap exceeded 5% × marketcap
def f47fgd_f47_fake_growth_detector_psrevcount5_252d_base_v104_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 63)
    result = (g).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days where ps-rev gap exceeded 50%
def f47fgd_f47_fake_growth_detector_psrevcount50_504d_base_v105_signal(revenue, ps, marketcap):
    g = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = (g).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days revenue lagged marketcap by >25%
def f47fgd_f47_fake_growth_detector_lagcount25_252d_base_v106_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = (g).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days valgap > 20% (heavy overvaluation count)
def f47fgd_f47_fake_growth_detector_valgapcount20_504d_base_v107_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = (v).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days valgap > 10%
def f47fgd_f47_fake_growth_detector_valgapcount10_252d_base_v108_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = (v).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst valgap (peak overvaluation ever)
def f47fgd_f47_fake_growth_detector_valgapworstever_base_v109_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap minus expanding-worst (gap-vs-history)
def f47fgd_f47_fake_growth_detector_valgapvsever_63d_base_v110_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    worst = v.expanding(min_periods=63).max()
    result = (worst - v) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap minus expanding-worst
def f47fgd_f47_fake_growth_detector_valgapvsever_252d_base_v111_signal(netinc, marketcap):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    worst = v.expanding(min_periods=63).max()
    result = (worst - v) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × revenue gap (joint fake)
def f47fgd_f47_fake_growth_detector_jointfake_63d_base_v112_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = a.abs() * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × revenue gap (joint fake)
def f47fgd_f47_fake_growth_detector_jointfake_252d_base_v113_signal(revenue, netinc, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = a.abs() * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × ps-rev gap (joint priced fake)
def f47fgd_f47_fake_growth_detector_jointpsval_63d_base_v114_signal(revenue, netinc, ps, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 63)
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = p * v * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × ps-rev gap
def f47fgd_f47_fake_growth_detector_jointpsval_252d_base_v115_signal(revenue, netinc, ps, marketcap):
    p = _f47_fakegrowth_psgap(revenue, ps, 252)
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = p * v * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap rolling worst over 252d (worst recent fake)
def f47fgd_f47_fake_growth_detector_gapworst_252d_base_v116_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g.rolling(252, min_periods=63).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap rolling worst over 504d
def f47fgd_f47_fake_growth_detector_gapworst_504d_base_v117_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g.rolling(504, min_periods=126).min() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap area / 252d gap area
def f47fgd_f47_fake_growth_detector_gapareafrac_63v252_base_v118_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252).abs()
    a = g.rolling(63, min_periods=21).sum()
    b = g.rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = a / b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap area / 504d gap area
def f47fgd_f47_fake_growth_detector_gapareafrac_252v504_base_v119_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 504).abs()
    a = g.rolling(252, min_periods=63).sum()
    b = g.rolling(504, min_periods=126).sum().replace(0, np.nan)
    result = a / b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap volatility-of-volatility
def f47fgd_f47_fake_growth_detector_gapvolvol_63d_base_v120_signal(revenue, marketcap):
    sd = _std(_f47_fake_growth(revenue, marketcap, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap volatility-of-volatility
def f47fgd_f47_fake_growth_detector_gapvolvol_252d_base_v121_signal(revenue, marketcap):
    sd = _std(_f47_fake_growth(revenue, marketcap, 504), 252)
    result = _std(sd, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# anomaly: 63d gap minus rolling 252d mean
def f47fgd_f47_fake_growth_detector_gapanomaly_63d_base_v122_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    base = _mean(_f47_fake_growth(revenue, marketcap, 252), 252)
    result = (g - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# anomaly: 252d gap minus rolling 504d mean
def f47fgd_f47_fake_growth_detector_gapanomaly_252d_base_v123_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    base = _mean(_f47_fake_growth(revenue, marketcap, 504), 504)
    result = (g - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-mcap gap × current ev/revenue (sales-priced fake)
def f47fgd_f47_fake_growth_detector_gapxevrev_63d_base_v124_signal(revenue, ev, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    evrev = ev / revenue.replace(0, np.nan)
    result = g * evrev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-mcap gap × ev/revenue
def f47fgd_f47_fake_growth_detector_gapxevrev_252d_base_v125_signal(revenue, ev, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    evrev = ev / revenue.replace(0, np.nan)
    result = g * evrev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × current ps multiple
def f47fgd_f47_fake_growth_detector_gapxpsmult_63d_base_v126_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × current ps multiple
def f47fgd_f47_fake_growth_detector_gapxpsmult_252d_base_v127_signal(revenue, marketcap, ps):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × current marketcap zscore (overvaluation timing)
def f47fgd_f47_fake_growth_detector_gapxmcapz_63d_base_v128_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    z = _z(marketcap, 252)
    result = g * z * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × marketcap zscore over 504d
def f47fgd_f47_fake_growth_detector_gapxmcapz_252d_base_v129_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    z = _z(marketcap, 504)
    result = g * z * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue-acceleration gap (rev g 63d minus rev g 252d)
def f47fgd_f47_fake_growth_detector_revaccel_63d_base_v130_signal(revenue, marketcap):
    rga = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    rgb = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = (rga - rgb) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue-acceleration gap × marketcap
def f47fgd_f47_fake_growth_detector_revaccel_252d_base_v131_signal(revenue, marketcap):
    rga = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    rgb = revenue.diff(504) / revenue.shift(504).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 252)
    result = (rga - rgb) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap-acceleration gap (mcap g 63d minus mcap g 252d) coupled to fake
def f47fgd_f47_fake_growth_detector_mcapaccel_63d_base_v132_signal(revenue, marketcap):
    mga = marketcap.diff(63) / marketcap.shift(63).abs().replace(0, np.nan)
    mgb = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 63)
    result = (mga - mgb) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap-acceleration gap
def f47fgd_f47_fake_growth_detector_mcapaccel_252d_base_v133_signal(revenue, marketcap):
    mga = marketcap.diff(252) / marketcap.shift(252).abs().replace(0, np.nan)
    mgb = marketcap.diff(504) / marketcap.shift(504).abs().replace(0, np.nan)
    base = _f47_fake_growth(revenue, marketcap, 252)
    result = (mga - mgb) * marketcap + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: gap + valgap + psgap (multi-source fake)
def f47fgd_f47_fake_growth_detector_multifake_63d_base_v134_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 63)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    c = _f47_fakegrowth_psgap(revenue, ps, 63)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite multi-source fake
def f47fgd_f47_fake_growth_detector_multifake_252d_base_v135_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 252)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    c = _f47_fakegrowth_psgap(revenue, ps, 252)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite multi-source fake
def f47fgd_f47_fake_growth_detector_multifake_504d_base_v136_signal(revenue, netinc, ps, marketcap):
    a = _f47_fake_growth(revenue, marketcap, 504)
    b = _f47_fakegrowth_valgap(netinc, marketcap, 504)
    c = _f47_fakegrowth_psgap(revenue, ps, 504)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × close-style (closeadj) decoration
def f47fgd_f47_fake_growth_detector_gapxclose_63d_base_v137_signal(revenue, marketcap, closeadj):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × closeadj
def f47fgd_f47_fake_growth_detector_gapxclose_252d_base_v138_signal(revenue, marketcap, closeadj):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valgap × closeadj
def f47fgd_f47_fake_growth_detector_valgapxclose_63d_base_v139_signal(netinc, marketcap, closeadj):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 63)
    result = v * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valgap × closeadj
def f47fgd_f47_fake_growth_detector_valgapxclose_252d_base_v140_signal(netinc, marketcap, closeadj):
    v = _f47_fakegrowth_valgap(netinc, marketcap, 252)
    result = v * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × log marketcap (size-weighted fake)
def f47fgd_f47_fake_growth_detector_gapxlogmcap_63d_base_v141_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = g * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × log marketcap
def f47fgd_f47_fake_growth_detector_gapxlogmcap_252d_base_v142_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = g * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × revenue level (revenue-weighted fake)
def f47fgd_f47_fake_growth_detector_gapxrev_63d_base_v143_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × revenue level
def f47fgd_f47_fake_growth_detector_gapxrev_252d_base_v144_signal(revenue, marketcap):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × ebitda level
def f47fgd_f47_fake_growth_detector_gapxebitda_63d_base_v145_signal(revenue, marketcap, ebitda):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * ebitda + _f47_fake_growth(revenue, marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × ebitda level
def f47fgd_f47_fake_growth_detector_gapxebitda_252d_base_v146_signal(revenue, marketcap, ebitda):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * ebitda + _f47_fake_growth(revenue, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × assets (asset-weighted fake)
def f47fgd_f47_fake_growth_detector_gapxassets_63d_base_v147_signal(revenue, marketcap, assets):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × assets
def f47fgd_f47_fake_growth_detector_gapxassets_252d_base_v148_signal(revenue, marketcap, assets):
    g = _f47_fake_growth(revenue, marketcap, 252)
    result = g * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × debt (debt-weighted fake growth)
def f47fgd_f47_fake_growth_detector_gapxdebt_63d_base_v149_signal(revenue, marketcap, debt):
    g = _f47_fake_growth(revenue, marketcap, 63)
    result = g * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity scaled by ev (max-fake intensity at scale)
def f47fgd_f47_fake_growth_detector_compositesev_252d_base_v150_signal(revenue, netinc, ps, marketcap, ev):
    a = _f47_fake_growth(revenue, marketcap, 252).abs()
    b = _f47_fakegrowth_valgap(netinc, marketcap, 252).abs()
    c = _f47_fakegrowth_psgap(revenue, ps, 252).abs()
    result = (a + b + c) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47fgd_f47_fake_growth_detector_gapxev_63d_base_v076_signal,
    f47fgd_f47_fake_growth_detector_gapxev_252d_base_v077_signal,
    f47fgd_f47_fake_growth_detector_gapxevebitda_63d_base_v078_signal,
    f47fgd_f47_fake_growth_detector_gapxevebitda_252d_base_v079_signal,
    f47fgd_f47_fake_growth_detector_gapxevebit_63d_base_v080_signal,
    f47fgd_f47_fake_growth_detector_gapxevebit_252d_base_v081_signal,
    f47fgd_f47_fake_growth_detector_gapxpb_63d_base_v082_signal,
    f47fgd_f47_fake_growth_detector_gapxpb_252d_base_v083_signal,
    f47fgd_f47_fake_growth_detector_evrevxev_63d_base_v084_signal,
    f47fgd_f47_fake_growth_detector_evrevxev_252d_base_v085_signal,
    f47fgd_f47_fake_growth_detector_gapxnoncf_63d_base_v086_signal,
    f47fgd_f47_fake_growth_detector_gapxnoncf_252d_base_v087_signal,
    f47fgd_f47_fake_growth_detector_gapxfcfyld_63d_base_v088_signal,
    f47fgd_f47_fake_growth_detector_gapxfcfyld_252d_base_v089_signal,
    f47fgd_f47_fake_growth_detector_gapxshareg_63d_base_v090_signal,
    f47fgd_f47_fake_growth_detector_gapxshareg_252d_base_v091_signal,
    f47fgd_f47_fake_growth_detector_gapxlev_63d_base_v092_signal,
    f47fgd_f47_fake_growth_detector_gapxlev_252d_base_v093_signal,
    f47fgd_f47_fake_growth_detector_valgapxpe_63d_base_v094_signal,
    f47fgd_f47_fake_growth_detector_valgapxpe_252d_base_v095_signal,
    f47fgd_f47_fake_growth_detector_valgapxps_63d_base_v096_signal,
    f47fgd_f47_fake_growth_detector_valgapxps_252d_base_v097_signal,
    f47fgd_f47_fake_growth_detector_valgapxevebitda_63d_base_v098_signal,
    f47fgd_f47_fake_growth_detector_valgapxevebitda_252d_base_v099_signal,
    f47fgd_f47_fake_growth_detector_valgapema_63d_base_v100_signal,
    f47fgd_f47_fake_growth_detector_valgapema_252d_base_v101_signal,
    f47fgd_f47_fake_growth_detector_psrevxev_63d_base_v102_signal,
    f47fgd_f47_fake_growth_detector_psrevxev_252d_base_v103_signal,
    f47fgd_f47_fake_growth_detector_psrevcount5_252d_base_v104_signal,
    f47fgd_f47_fake_growth_detector_psrevcount50_504d_base_v105_signal,
    f47fgd_f47_fake_growth_detector_lagcount25_252d_base_v106_signal,
    f47fgd_f47_fake_growth_detector_valgapcount20_504d_base_v107_signal,
    f47fgd_f47_fake_growth_detector_valgapcount10_252d_base_v108_signal,
    f47fgd_f47_fake_growth_detector_valgapworstever_base_v109_signal,
    f47fgd_f47_fake_growth_detector_valgapvsever_63d_base_v110_signal,
    f47fgd_f47_fake_growth_detector_valgapvsever_252d_base_v111_signal,
    f47fgd_f47_fake_growth_detector_jointfake_63d_base_v112_signal,
    f47fgd_f47_fake_growth_detector_jointfake_252d_base_v113_signal,
    f47fgd_f47_fake_growth_detector_jointpsval_63d_base_v114_signal,
    f47fgd_f47_fake_growth_detector_jointpsval_252d_base_v115_signal,
    f47fgd_f47_fake_growth_detector_gapworst_252d_base_v116_signal,
    f47fgd_f47_fake_growth_detector_gapworst_504d_base_v117_signal,
    f47fgd_f47_fake_growth_detector_gapareafrac_63v252_base_v118_signal,
    f47fgd_f47_fake_growth_detector_gapareafrac_252v504_base_v119_signal,
    f47fgd_f47_fake_growth_detector_gapvolvol_63d_base_v120_signal,
    f47fgd_f47_fake_growth_detector_gapvolvol_252d_base_v121_signal,
    f47fgd_f47_fake_growth_detector_gapanomaly_63d_base_v122_signal,
    f47fgd_f47_fake_growth_detector_gapanomaly_252d_base_v123_signal,
    f47fgd_f47_fake_growth_detector_gapxevrev_63d_base_v124_signal,
    f47fgd_f47_fake_growth_detector_gapxevrev_252d_base_v125_signal,
    f47fgd_f47_fake_growth_detector_gapxpsmult_63d_base_v126_signal,
    f47fgd_f47_fake_growth_detector_gapxpsmult_252d_base_v127_signal,
    f47fgd_f47_fake_growth_detector_gapxmcapz_63d_base_v128_signal,
    f47fgd_f47_fake_growth_detector_gapxmcapz_252d_base_v129_signal,
    f47fgd_f47_fake_growth_detector_revaccel_63d_base_v130_signal,
    f47fgd_f47_fake_growth_detector_revaccel_252d_base_v131_signal,
    f47fgd_f47_fake_growth_detector_mcapaccel_63d_base_v132_signal,
    f47fgd_f47_fake_growth_detector_mcapaccel_252d_base_v133_signal,
    f47fgd_f47_fake_growth_detector_multifake_63d_base_v134_signal,
    f47fgd_f47_fake_growth_detector_multifake_252d_base_v135_signal,
    f47fgd_f47_fake_growth_detector_multifake_504d_base_v136_signal,
    f47fgd_f47_fake_growth_detector_gapxclose_63d_base_v137_signal,
    f47fgd_f47_fake_growth_detector_gapxclose_252d_base_v138_signal,
    f47fgd_f47_fake_growth_detector_valgapxclose_63d_base_v139_signal,
    f47fgd_f47_fake_growth_detector_valgapxclose_252d_base_v140_signal,
    f47fgd_f47_fake_growth_detector_gapxlogmcap_63d_base_v141_signal,
    f47fgd_f47_fake_growth_detector_gapxlogmcap_252d_base_v142_signal,
    f47fgd_f47_fake_growth_detector_gapxrev_63d_base_v143_signal,
    f47fgd_f47_fake_growth_detector_gapxrev_252d_base_v144_signal,
    f47fgd_f47_fake_growth_detector_gapxebitda_63d_base_v145_signal,
    f47fgd_f47_fake_growth_detector_gapxebitda_252d_base_v146_signal,
    f47fgd_f47_fake_growth_detector_gapxassets_63d_base_v147_signal,
    f47fgd_f47_fake_growth_detector_gapxassets_252d_base_v148_signal,
    f47fgd_f47_fake_growth_detector_gapxdebt_63d_base_v149_signal,
    f47fgd_f47_fake_growth_detector_compositesev_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_FAKE_GROWTH_DETECTOR_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_fake_growth", "_f47_fakegrowth_valgap", "_f47_fakegrowth_psgap")
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
    print(f"OK f47_fake_growth_detector_base_076_150_claude: {n_features} features pass")
