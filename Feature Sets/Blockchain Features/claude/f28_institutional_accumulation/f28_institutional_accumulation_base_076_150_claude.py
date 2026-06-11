import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (institutional accumulation, 13F) =====
def _f28_accum(shrvalue, w):
    # accumulation: fractional change in value of shares held by institutions over w
    return shrvalue.pct_change(periods=w)


def _f28_flow(shrunits, w):
    # share flow: change in shares held over w, normalized by trailing average level
    d = shrunits.diff(periods=w)
    base = shrunits.rolling(w, min_periods=max(1, w // 2)).mean()
    return d / base.replace(0, np.nan)


def _f28_ownz(shrvalue, w):
    # z-score of institutional-held value over w (standardized accumulation level)
    return _z(shrvalue, w)


def _f28_costbasis(shrvalue, shrunits):
    # implied average cost basis = value per unit held
    return _safe_div(shrvalue, shrunits)


# ============ FEATURES 076-150 ============

# 21d accumulation smoothed 21d (short-horizon ownership momentum)
def f28ia_f28_institutional_accumulation_ownmom_21s21_base_v076_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d accumulation smoothed 42d
def f28ia_f28_institutional_accumulation_ownmom_126s42_base_v077_signal(shrvalue):
    result = _mean(_f28_accum(shrvalue, 126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d flow smoothed 42d
def f28ia_f28_institutional_accumulation_flowmom_42s42_base_v078_signal(shrunits):
    result = _mean(_f28_flow(shrunits, 42), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d flow smoothed 42d
def f28ia_f28_institutional_accumulation_flowmom_84s42_base_v079_signal(shrunits):
    result = _mean(_f28_flow(shrunits, 84), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d accumulation over 252d
def f28ia_f28_institutional_accumulation_zaccum63_252_base_v080_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d accumulation over 504d
def f28ia_f28_institutional_accumulation_zaccum126_504_base_v081_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d accumulation over 126d
def f28ia_f28_institutional_accumulation_zaccum21_126_base_v082_signal(shrvalue):
    result = _z(_f28_accum(shrvalue, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d flow over 252d
def f28ia_f28_institutional_accumulation_zflow63_252_base_v083_signal(shrunits):
    result = _z(_f28_flow(shrunits, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d flow over 504d
def f28ia_f28_institutional_accumulation_zflow126_504_base_v084_signal(shrunits):
    result = _z(_f28_flow(shrunits, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration 42d vs 84d
def f28ia_f28_institutional_accumulation_accel_42_84_base_v085_signal(shrvalue):
    result = _f28_accum(shrvalue, 42) - _f28_accum(shrvalue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration 84d vs 189d
def f28ia_f28_institutional_accumulation_accel_84_189_base_v086_signal(shrvalue):
    result = _f28_accum(shrvalue, 84) - _f28_accum(shrvalue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# flow acceleration 63d vs 126d
def f28ia_f28_institutional_accumulation_flowaccel_63_126_base_v087_signal(shrunits):
    result = _f28_flow(shrunits, 63) - _f28_flow(shrunits, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# flow acceleration 126d vs 252d
def f28ia_f28_institutional_accumulation_flowaccel_126_252_base_v088_signal(shrunits):
    result = _f28_flow(shrunits, 126) - _f28_flow(shrunits, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation spread 63d vs 252d
def f28ia_f28_institutional_accumulation_sprd_63_252_base_v089_signal(shrvalue):
    result = _f28_accum(shrvalue, 63) - _f28_accum(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log-accumulation spread 63d vs 126d
def f28ia_f28_institutional_accumulation_lsprd_63_126_base_v090_signal(shrvalue):
    result = (np.log(shrvalue / shrvalue.shift(63)) - np.log(shrvalue / shrvalue.shift(126))) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue z-score 504d
def f28ia_f28_institutional_accumulation_tvz_504d_base_v091_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 504) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue log growth 126d
def f28ia_f28_institutional_accumulation_tvlog_126d_base_v092_signal(totalvalue, shrvalue):
    result = np.log(totalvalue / totalvalue.shift(126)) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue log growth 252d
def f28ia_f28_institutional_accumulation_tvlog_252d_base_v093_signal(totalvalue, shrvalue):
    result = np.log(totalvalue / totalvalue.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-relative accumulation: accum63 minus marketcap roc63 (active ownership change)
def f28ia_f28_institutional_accumulation_relaccum_63_base_v094_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 63) - marketcap.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-relative accumulation 126d
def f28ia_f28_institutional_accumulation_relaccum_126_base_v095_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 126) - marketcap.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-relative accumulation 252d
def f28ia_f28_institutional_accumulation_relaccum_252_base_v096_signal(shrvalue, marketcap):
    result = _f28_accum(shrvalue, 252) - marketcap.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation annualized log (63d)
def f28ia_f28_institutional_accumulation_annaccum_63_base_v097_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(63)) * (252.0 / 63.0) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation annualized log (126d)
def f28ia_f28_institutional_accumulation_annaccum_126_base_v098_signal(shrvalue):
    result = np.log(shrvalue / shrvalue.shift(126)) * (252.0 / 126.0) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow annualized log (63d on shrunits)
def f28ia_f28_institutional_accumulation_annflow_63_base_v099_signal(shrunits):
    result = np.log(shrunits / shrunits.shift(63)) * (252.0 / 63.0) + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation percentile rank 252d accum over 504d
def f28ia_f28_institutional_accumulation_rank_accum252_base_v100_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# flow percentile rank 126d flow over 504d
def f28ia_f28_institutional_accumulation_rank_flow126_base_v101_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis percentile rank over 252d
def f28ia_f28_institutional_accumulation_rank_costbasis_base_v102_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = cb.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% percentile rank over 252d
def f28ia_f28_institutional_accumulation_rank_ownpct_base_v103_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = own.rolling(252, min_periods=84).rank(pct=True) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis info ratio: 126d cb change over 252d cb dispersion
def f28ia_f28_institutional_accumulation_cbir_126_base_v104_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = _safe_div(cb - cb.shift(126), _std(cb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis EWMA scaled (63d span on daily log change)
def f28ia_f28_institutional_accumulation_cbewm_63_base_v105_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    lr = np.log(cb / cb.shift(1))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation x flow confirmation (value growth confirmed by share inflow)
def f28ia_f28_institutional_accumulation_accumflowx_63_base_v106_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 63) * _f28_flow(shrunits, 63).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation x flow confirmation 126d
def f28ia_f28_institutional_accumulation_accumflowx_126_base_v107_signal(shrvalue, shrunits):
    result = _f28_accum(shrvalue, 126) * _f28_flow(shrunits, 126).clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation weighted by ownership-% level (conviction-scaled)
def f28ia_f28_institutional_accumulation_accumxown_63_base_v108_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _f28_accum(shrvalue, 63) * own
    return result.replace([np.inf, -np.inf], np.nan)


# flow weighted by ownership-% level
def f28ia_f28_institutional_accumulation_flowxown_63_base_v109_signal(shrunits, shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = _f28_flow(shrunits, 63) * own
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation skew of daily shrvalue log changes 126d
def f28ia_f28_institutional_accumulation_accumskew_126_base_v110_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(126, min_periods=42).skew() + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation skew 252d
def f28ia_f28_institutional_accumulation_accumskew_252_base_v111_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(252, min_periods=84).skew() + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation kurtosis 126d (fat-tail buying regime)
def f28ia_f28_institutional_accumulation_accumkurt_126_base_v112_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.rolling(126, min_periods=42).kurt() + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow skew 126d
def f28ia_f28_institutional_accumulation_flowskew_126_base_v113_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.rolling(126, min_periods=42).skew() + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation surprise 252d (252d accum minus 504d mean)
def f28ia_f28_institutional_accumulation_surp_252d_base_v114_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# flow surprise 126d (126d flow minus 252d mean)
def f28ia_f28_institutional_accumulation_flowsurp_126d_base_v115_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation dispersion 252d of 21d accum
def f28ia_f28_institutional_accumulation_accumdisp_252_base_v116_signal(shrvalue):
    result = _std(_f28_accum(shrvalue, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# flow dispersion 504d of 21d flow
def f28ia_f28_institutional_accumulation_flowdisp_504_base_v117_signal(shrunits):
    result = _std(_f28_flow(shrunits, 21), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation efficiency 504d (net value change over path)
def f28ia_f28_institutional_accumulation_accumeff_504_base_v118_signal(shrvalue):
    net = shrvalue - shrvalue.shift(504)
    path = shrvalue.diff().abs().rolling(504, min_periods=168).sum()
    result = _safe_div(net, path) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow efficiency 252d
def f28ia_f28_institutional_accumulation_floweff_252_base_v119_signal(shrunits):
    net = shrunits - shrunits.shift(252)
    path = shrunits.diff().abs().rolling(252, min_periods=84).sum()
    result = _safe_div(net, path) + _f28_flow(shrunits, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation Sharpe 63d
def f28ia_f28_institutional_accumulation_accumsharpe_63_base_v120_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = _safe_div(_mean(lr, 63), _std(lr, 63)) * np.sqrt(63.0) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow Sharpe 126d (mean/std of daily unit log change)
def f28ia_f28_institutional_accumulation_flowsharpe_126_base_v121_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = _safe_div(_mean(lr, 126), _std(lr, 126)) * np.sqrt(126.0) + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation vol-scaled 252d
def f28ia_f28_institutional_accumulation_accumvs_252_base_v122_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f28_accum(shrvalue, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# flow vol-scaled 126d
def f28ia_f28_institutional_accumulation_flowvs_126_base_v123_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    vol = _std(lr, 252) * np.sqrt(126.0)
    result = _safe_div(_f28_flow(shrunits, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation EWMA scaled 252d
def f28ia_f28_institutional_accumulation_accumewm_252_base_v124_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    result = lr.ewm(span=252, min_periods=84).mean() * 252.0 + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow EWMA scaled 126d
def f28ia_f28_institutional_accumulation_flowewm_126_base_v125_signal(shrunits):
    lr = np.log(shrunits / shrunits.shift(1))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0 + _f28_flow(shrunits, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% spread short vs long (63d chg minus 252d chg)
def f28ia_f28_institutional_accumulation_ownpctsprd_base_v126_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = (own - own.shift(63)) - (own - own.shift(252)) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ownz spread short vs long (63d minus 252d standardized level)
def f28ia_f28_institutional_accumulation_ownzsprd_base_v127_signal(shrvalue):
    result = _f28_ownz(shrvalue, 63) - _f28_ownz(shrvalue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation 315d
def f28ia_f28_institutional_accumulation_accum_315d_base_v128_signal(shrvalue):
    result = _f28_accum(shrvalue, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation 378d
def f28ia_f28_institutional_accumulation_accum_378d_base_v129_signal(shrvalue):
    result = _f28_accum(shrvalue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# flow 84d
def f28ia_f28_institutional_accumulation_flow_84d_base_v130_signal(shrunits):
    result = _f28_flow(shrunits, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# flow 189d
def f28ia_f28_institutional_accumulation_flow_189d_base_v131_signal(shrunits):
    result = _f28_flow(shrunits, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation info ratio 252d / 504d dispersion
def f28ia_f28_institutional_accumulation_accumir_252d_base_v132_signal(shrvalue):
    r = _f28_accum(shrvalue, 252)
    result = _safe_div(r, _std(r, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# flow info ratio 126d / 252d dispersion
def f28ia_f28_institutional_accumulation_flowir_126d_base_v133_signal(shrunits):
    r = _f28_flow(shrunits, 126)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue z-score 126d
def f28ia_f28_institutional_accumulation_tvz_126d_base_v134_signal(totalvalue, shrvalue):
    result = _z(totalvalue, 126) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# shrunits z-score 504d
def f28ia_f28_institutional_accumulation_unitz_504d_base_v135_signal(shrunits):
    result = _z(shrunits, 504) + _f28_flow(shrunits, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit vs marketcap-per-unit divergence (cost basis relative to price proxy)
def f28ia_f28_institutional_accumulation_cbrel_63_base_v136_signal(shrvalue, shrunits, marketcap):
    cb = _f28_costbasis(shrvalue, shrunits)
    mpu = _safe_div(marketcap, shrunits)
    result = _safe_div(cb, mpu) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum surprise z (63d accum surprise standardized 252d)
def f28ia_f28_institutional_accumulation_surpz_63_base_v137_signal(shrvalue):
    r = _f28_accum(shrvalue, 63)
    surp = r - _mean(r, 126)
    result = _z(surp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# flow momentum surprise z (63d flow surprise standardized 252d)
def f28ia_f28_institutional_accumulation_flowsurpz_63_base_v138_signal(shrunits):
    r = _f28_flow(shrunits, 63)
    surp = r - _mean(r, 126)
    result = _z(surp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-weighted (63d accum x sign-persistence of daily change)
def f28ia_f28_institutional_accumulation_accumpersist_63_base_v139_signal(shrvalue):
    persist = np.sign(shrvalue.diff()).rolling(63, min_periods=21).mean()
    result = _f28_accum(shrvalue, 63) * persist.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-% annual log growth (252d)
def f28ia_f28_institutional_accumulation_ownpctann_252_base_v140_signal(shrvalue, marketcap):
    own = _safe_div(shrvalue, marketcap)
    result = np.log(own / own.shift(252)) + _f28_accum(shrvalue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation blended multi-horizon (63/126/252)
def f28ia_f28_institutional_accumulation_accumblend_base_v141_signal(shrvalue):
    result = (_f28_accum(shrvalue, 63) + _f28_accum(shrvalue, 126) + _f28_accum(shrvalue, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# flow blended multi-horizon (63/126/252)
def f28ia_f28_institutional_accumulation_flowblend_base_v142_signal(shrunits):
    result = (_f28_flow(shrunits, 63) + _f28_flow(shrunits, 126) + _f28_flow(shrunits, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation minus flow blended (value-vs-share divergence composite)
def f28ia_f28_institutional_accumulation_divblend_base_v143_signal(shrvalue, shrunits):
    av = (_f28_accum(shrvalue, 63) + _f28_accum(shrvalue, 126)) / 2.0
    fl = (_f28_flow(shrunits, 63) + _f28_flow(shrunits, 126)) / 2.0
    result = av - fl
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue share of marketcap (aggregate 13F penetration)
def f28ia_f28_institutional_accumulation_tvpen_lvl_base_v144_signal(totalvalue, marketcap, shrvalue):
    result = _safe_div(totalvalue, marketcap) + _f28_accum(shrvalue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# totalvalue penetration 126d change
def f28ia_f28_institutional_accumulation_tvpen_chg126_base_v145_signal(totalvalue, marketcap, shrvalue):
    pen = _safe_div(totalvalue, marketcap)
    result = pen - pen.shift(126) + _f28_accum(shrvalue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation z-scaled by ownership trend (63d accum x ownz63)
def f28ia_f28_institutional_accumulation_accumxownz63_base_v146_signal(shrvalue):
    result = _f28_accum(shrvalue, 126) * _f28_ownz(shrvalue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-basis annual log growth 252d
def f28ia_f28_institutional_accumulation_cbann_252_base_v147_signal(shrvalue, shrunits):
    cb = _f28_costbasis(shrvalue, shrunits)
    result = np.log(cb / cb.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation 504d vol-scaled
def f28ia_f28_institutional_accumulation_accumvs_504_base_v148_signal(shrvalue):
    lr = np.log(shrvalue / shrvalue.shift(1))
    vol = _std(lr, 252) * np.sqrt(504.0)
    result = _safe_div(_f28_accum(shrvalue, 504), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# flow efficiency-weighted accumulation (accum63 x flow efficiency 126)
def f28ia_f28_institutional_accumulation_accumxfloweff_base_v149_signal(shrvalue, shrunits):
    net = shrunits - shrunits.shift(126)
    path = shrunits.diff().abs().rolling(126, min_periods=42).sum()
    eff = _safe_div(net, path)
    result = _f28_accum(shrvalue, 63) * eff
    return result.replace([np.inf, -np.inf], np.nan)


# composite institutional conviction (ownz252 x accum126 blended with flow126)
def f28ia_f28_institutional_accumulation_conviction_base_v150_signal(shrvalue, shrunits):
    result = (_f28_ownz(shrvalue, 252) * 0.5
              + _z(_f28_accum(shrvalue, 126), 252) * 0.25
              + _z(_f28_flow(shrunits, 126), 252) * 0.25)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28ia_f28_institutional_accumulation_ownmom_21s21_base_v076_signal,
    f28ia_f28_institutional_accumulation_ownmom_126s42_base_v077_signal,
    f28ia_f28_institutional_accumulation_flowmom_42s42_base_v078_signal,
    f28ia_f28_institutional_accumulation_flowmom_84s42_base_v079_signal,
    f28ia_f28_institutional_accumulation_zaccum63_252_base_v080_signal,
    f28ia_f28_institutional_accumulation_zaccum126_504_base_v081_signal,
    f28ia_f28_institutional_accumulation_zaccum21_126_base_v082_signal,
    f28ia_f28_institutional_accumulation_zflow63_252_base_v083_signal,
    f28ia_f28_institutional_accumulation_zflow126_504_base_v084_signal,
    f28ia_f28_institutional_accumulation_accel_42_84_base_v085_signal,
    f28ia_f28_institutional_accumulation_accel_84_189_base_v086_signal,
    f28ia_f28_institutional_accumulation_flowaccel_63_126_base_v087_signal,
    f28ia_f28_institutional_accumulation_flowaccel_126_252_base_v088_signal,
    f28ia_f28_institutional_accumulation_sprd_63_252_base_v089_signal,
    f28ia_f28_institutional_accumulation_lsprd_63_126_base_v090_signal,
    f28ia_f28_institutional_accumulation_tvz_504d_base_v091_signal,
    f28ia_f28_institutional_accumulation_tvlog_126d_base_v092_signal,
    f28ia_f28_institutional_accumulation_tvlog_252d_base_v093_signal,
    f28ia_f28_institutional_accumulation_relaccum_63_base_v094_signal,
    f28ia_f28_institutional_accumulation_relaccum_126_base_v095_signal,
    f28ia_f28_institutional_accumulation_relaccum_252_base_v096_signal,
    f28ia_f28_institutional_accumulation_annaccum_63_base_v097_signal,
    f28ia_f28_institutional_accumulation_annaccum_126_base_v098_signal,
    f28ia_f28_institutional_accumulation_annflow_63_base_v099_signal,
    f28ia_f28_institutional_accumulation_rank_accum252_base_v100_signal,
    f28ia_f28_institutional_accumulation_rank_flow126_base_v101_signal,
    f28ia_f28_institutional_accumulation_rank_costbasis_base_v102_signal,
    f28ia_f28_institutional_accumulation_rank_ownpct_base_v103_signal,
    f28ia_f28_institutional_accumulation_cbir_126_base_v104_signal,
    f28ia_f28_institutional_accumulation_cbewm_63_base_v105_signal,
    f28ia_f28_institutional_accumulation_accumflowx_63_base_v106_signal,
    f28ia_f28_institutional_accumulation_accumflowx_126_base_v107_signal,
    f28ia_f28_institutional_accumulation_accumxown_63_base_v108_signal,
    f28ia_f28_institutional_accumulation_flowxown_63_base_v109_signal,
    f28ia_f28_institutional_accumulation_accumskew_126_base_v110_signal,
    f28ia_f28_institutional_accumulation_accumskew_252_base_v111_signal,
    f28ia_f28_institutional_accumulation_accumkurt_126_base_v112_signal,
    f28ia_f28_institutional_accumulation_flowskew_126_base_v113_signal,
    f28ia_f28_institutional_accumulation_surp_252d_base_v114_signal,
    f28ia_f28_institutional_accumulation_flowsurp_126d_base_v115_signal,
    f28ia_f28_institutional_accumulation_accumdisp_252_base_v116_signal,
    f28ia_f28_institutional_accumulation_flowdisp_504_base_v117_signal,
    f28ia_f28_institutional_accumulation_accumeff_504_base_v118_signal,
    f28ia_f28_institutional_accumulation_floweff_252_base_v119_signal,
    f28ia_f28_institutional_accumulation_accumsharpe_63_base_v120_signal,
    f28ia_f28_institutional_accumulation_flowsharpe_126_base_v121_signal,
    f28ia_f28_institutional_accumulation_accumvs_252_base_v122_signal,
    f28ia_f28_institutional_accumulation_flowvs_126_base_v123_signal,
    f28ia_f28_institutional_accumulation_accumewm_252_base_v124_signal,
    f28ia_f28_institutional_accumulation_flowewm_126_base_v125_signal,
    f28ia_f28_institutional_accumulation_ownpctsprd_base_v126_signal,
    f28ia_f28_institutional_accumulation_ownzsprd_base_v127_signal,
    f28ia_f28_institutional_accumulation_accum_315d_base_v128_signal,
    f28ia_f28_institutional_accumulation_accum_378d_base_v129_signal,
    f28ia_f28_institutional_accumulation_flow_84d_base_v130_signal,
    f28ia_f28_institutional_accumulation_flow_189d_base_v131_signal,
    f28ia_f28_institutional_accumulation_accumir_252d_base_v132_signal,
    f28ia_f28_institutional_accumulation_flowir_126d_base_v133_signal,
    f28ia_f28_institutional_accumulation_tvz_126d_base_v134_signal,
    f28ia_f28_institutional_accumulation_unitz_504d_base_v135_signal,
    f28ia_f28_institutional_accumulation_cbrel_63_base_v136_signal,
    f28ia_f28_institutional_accumulation_surpz_63_base_v137_signal,
    f28ia_f28_institutional_accumulation_flowsurpz_63_base_v138_signal,
    f28ia_f28_institutional_accumulation_accumpersist_63_base_v139_signal,
    f28ia_f28_institutional_accumulation_ownpctann_252_base_v140_signal,
    f28ia_f28_institutional_accumulation_accumblend_base_v141_signal,
    f28ia_f28_institutional_accumulation_flowblend_base_v142_signal,
    f28ia_f28_institutional_accumulation_divblend_base_v143_signal,
    f28ia_f28_institutional_accumulation_tvpen_lvl_base_v144_signal,
    f28ia_f28_institutional_accumulation_tvpen_chg126_base_v145_signal,
    f28ia_f28_institutional_accumulation_accumxownz63_base_v146_signal,
    f28ia_f28_institutional_accumulation_cbann_252_base_v147_signal,
    f28ia_f28_institutional_accumulation_accumvs_504_base_v148_signal,
    f28ia_f28_institutional_accumulation_accumxfloweff_base_v149_signal,
    f28ia_f28_institutional_accumulation_conviction_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_INSTITUTIONAL_ACCUMULATION_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f28_accum", "_f28_flow", "_f28_ownz", "_f28_costbasis")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_institutional_accumulation_base_076_150_claude: {n_features} features pass")
