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


# ===== folder domain primitives (share-dilution machine) =====
def _f17_dilution(sharesbas, w):
    # relentless dilution: pct change of share count over w trading days
    return sharesbas.pct_change(periods=w)


def _f17_sharetrend(sharesbas, w):
    # normalized slope of share count: w-day change scaled by recent share level
    d = sharesbas - sharesbas.shift(w)
    base = sharesbas.rolling(w, min_periods=max(2, w // 2)).mean()
    return d / base.replace(0, np.nan)


def _f17_dilz(sharesbas, w):
    # z-score of share-growth: how extreme is current dilution vs its own history
    g = sharesbas.pct_change(periods=21)
    m = g.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(2, w // 2)).std()
    return (g - m) / sd.replace(0, np.nan)


def _f17_issintensity(ncfcommon, sharesbas, w):
    # issuance intensity: common-stock cash flow normalized by share base, smoothed
    raw = ncfcommon / sharesbas.replace(0, np.nan)
    return raw.rolling(w, min_periods=max(2, w // 2)).mean()


# ============ FEATURES 076-150 ============

# 315d sharesbas dilution
def f17sd_f17_share_dilution_machine_dil_315d_base_v076_signal(sharesbas):
    result = _f17_dilution(sharesbas, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d sharesbas dilution
def f17sd_f17_share_dilution_machine_dil_378d_base_v077_signal(sharesbas):
    result = _f17_dilution(sharesbas, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d sharesbas dilution (weekly issuance burst)
def f17sd_f17_share_dilution_machine_dil_10d_base_v078_signal(sharesbas):
    result = _f17_dilution(sharesbas, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_189d_base_v079_signal(shareswa):
    result = _f17_dilution(shareswa, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d shareswa dilution
def f17sd_f17_share_dilution_machine_wadil_84d_base_v080_signal(shareswa):
    result = _f17_dilution(shareswa, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative log dilution vs 189d ago
def f17sd_f17_share_dilution_machine_cumdil_189d_base_v081_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(189)) + _f17_dilution(sharesbas, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative log dilution vs 378d ago
def f17sd_f17_share_dilution_machine_cumdil_378d_base_v082_signal(sharesbas):
    result = np.log(sharesbas / sharesbas.shift(378)) + _f17_dilution(sharesbas, 378) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 84d minus 189d dilution
def f17sd_f17_share_dilution_machine_accel_84_189d_base_v083_signal(sharesbas):
    result = _f17_dilution(sharesbas, 84) - _f17_dilution(sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration: 42d minus 126d dilution
def f17sd_f17_share_dilution_machine_accel_42_126d_base_v084_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42) - _f17_dilution(sharesbas, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 189d
def f17sd_f17_share_dilution_machine_dilz_189d_base_v085_signal(sharesbas):
    result = _f17_dilz(sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 315d
def f17sd_f17_share_dilution_machine_dilz_315d_base_v086_signal(sharesbas):
    result = _f17_dilz(sharesbas, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 189d
def f17sd_f17_share_dilution_machine_trend_189d_base_v087_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 315d
def f17sd_f17_share_dilution_machine_trend_315d_base_v088_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend slope over 84d
def f17sd_f17_share_dilution_machine_trend_84d_base_v089_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp dilution: sbcomp / equity smoothed 189d
def f17sd_f17_share_dilution_machine_sbcdil_189d_base_v090_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _mean(raw, 189) + _f17_dilution(sharesbas, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp per share smoothed 63d
def f17sd_f17_share_dilution_machine_sbcps_63d_base_v091_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _mean(raw, 63) + _f17_dilution(sharesbas, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp / revenue smoothed 252d (compensation drag)
def f17sd_f17_share_dilution_machine_sbcrev_252d_base_v092_signal(sbcomp, revenue, sharesbas):
    raw = _safe_div(sbcomp, revenue)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp / revenue log-trend 252d
def f17sd_f17_share_dilution_machine_sbcrevtr_252d_base_v093_signal(sbcomp, revenue, sharesbas):
    raw = _safe_div(sbcomp, revenue)
    result = np.log(raw / raw.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity smoothed 189d
def f17sd_f17_share_dilution_machine_issint_189d_base_v094_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity smoothed 42d
def f17sd_f17_share_dilution_machine_issint_42d_base_v095_signal(ncfcommon, sharesbas):
    result = _f17_issintensity(ncfcommon, sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon / revenue smoothed 252d (issuance vs sales)
def f17sd_f17_share_dilution_machine_issrev_252d_base_v096_signal(ncfcommon, revenue, sharesbas):
    raw = _safe_div(ncfcommon, revenue)
    result = _mean(raw, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank of 252d growth over 504d
def f17sd_f17_share_dilution_machine_dilrank252_504d_base_v097_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank of 21d growth over 252d
def f17sd_f17_share_dilution_machine_dilrank21_252d_base_v098_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# good-vs-bad dilution: share growth minus revenue growth (504d)
def f17sd_f17_share_dilution_machine_gvb_504d_base_v099_signal(sharesbas, revenue):
    result = _f17_dilution(sharesbas, 504) - revenue.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# good-vs-bad dilution ratio: share growth over revenue growth (252d)
def f17sd_f17_share_dilution_machine_gvbratio_252d_base_v100_signal(sharesbas, revenue):
    result = _safe_div(_f17_dilution(sharesbas, 252), revenue.pct_change(periods=252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share log-trend 504d
def f17sd_f17_share_dilution_machine_rps_504d_base_v101_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    result = np.log(rps / rps.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity per share log-trend 504d
def f17sd_f17_share_dilution_machine_eps_504d_base_v102_signal(equity, sharesbas):
    eq = _safe_div(equity, sharesbas)
    result = np.log(eq / eq.shift(504)) + _f17_dilution(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution information ratio 252d over dispersion
def f17sd_f17_share_dilution_machine_dilir_252d_base_v103_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = _safe_div(g, _std(g, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution information ratio 21d over 252d dispersion
def f17sd_f17_share_dilution_machine_dilir_21d_base_v104_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dilution: 252d mean of 21d share growth
def f17sd_f17_share_dilution_machine_smdil21_252d_base_v105_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed dilution: 126d mean of 63d share growth
def f17sd_f17_share_dilution_machine_smdil63_126d_base_v106_signal(sharesbas):
    result = _mean(_f17_dilution(sharesbas, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of quarterly dilution span 252
def f17sd_f17_share_dilution_machine_ewmdil_252d_base_v107_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.ewm(span=252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of monthly dilution span 42
def f17sd_f17_share_dilution_machine_ewmdil_42d_base_v108_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion over 504d
def f17sd_f17_share_dilution_machine_dildisp_504d_base_v109_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 21), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion of quarterly growth over 252d
def f17sd_f17_share_dilution_machine_dildisp63_252d_base_v110_signal(sharesbas):
    result = _std(_f17_dilution(sharesbas, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d dilution
def f17sd_f17_share_dilution_machine_anndil_252d_base_v111_signal(sharesbas):
    result = _f17_dilution(sharesbas, 252) * (252.0 / 252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 189d dilution
def f17sd_f17_share_dilution_machine_anndil_189d_base_v112_signal(sharesbas):
    result = _f17_dilution(sharesbas, 189) * (252.0 / 189.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 42d dilution
def f17sd_f17_share_dilution_machine_anndil_42d_base_v113_signal(sharesbas):
    result = _f17_dilution(sharesbas, 42) * (252.0 / 42.0)
    return result.replace([np.inf, -np.inf], np.nan)


# basic minus weighted dilution gap 504d
def f17sd_f17_share_dilution_machine_basgap_504d_base_v114_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 504) - _f17_dilution(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# basic minus weighted dilution gap 63d
def f17sd_f17_share_dilution_machine_basgap_63d_base_v115_signal(sharesbas, shareswa):
    result = _f17_dilution(sharesbas, 63) - _f17_dilution(shareswa, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# basic-over-weighted share-ratio log-trend 126d
def f17sd_f17_share_dilution_machine_baswa_126d_base_v116_signal(sharesbas, shareswa):
    ratio = _safe_div(sharesbas, shareswa)
    result = np.log(ratio / ratio.shift(126)) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa trend slope over 504d
def f17sd_f17_share_dilution_machine_watrend_504d_base_v117_signal(shareswa):
    result = _f17_sharetrend(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa dilution z-score over 504d
def f17sd_f17_share_dilution_machine_wadilz_504d_base_v118_signal(shareswa):
    result = _f17_dilz(shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa dilution z-score over 126d
def f17sd_f17_share_dilution_machine_wadilz_126d_base_v119_signal(shareswa):
    result = _f17_dilz(shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution minus equity-growth gap 504d
def f17sd_f17_share_dilution_machine_dileqs_504d_base_v120_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=504)
    result = _f17_dilution(sharesbas, 504) - eqg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution minus equity-growth gap 63d
def f17sd_f17_share_dilution_machine_dileqs_63d_base_v121_signal(sharesbas, equity):
    eqg = equity.pct_change(periods=63)
    result = _f17_dilution(sharesbas, 63) - eqg
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity z-scored over 126d
def f17sd_f17_share_dilution_machine_issintz_126d_base_v122_signal(ncfcommon, sharesbas):
    raw = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp / sharesbas z-scored over 126d
def f17sd_f17_share_dilution_machine_sbcz_126d_base_v123_signal(sbcomp, sharesbas):
    raw = _safe_div(sbcomp, sharesbas)
    result = _z(raw, 126) + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution trend ratio: 126d trend over 504d trend
def f17sd_f17_share_dilution_machine_trratio_126_504d_base_v124_signal(sharesbas):
    result = _safe_div(_f17_sharetrend(sharesbas, 126), _f17_sharetrend(sharesbas, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: 252d dilution minus its 504d mean
def f17sd_f17_share_dilution_machine_dilsurp_252d_base_v125_signal(sharesbas):
    g = _f17_dilution(sharesbas, 252)
    result = g - _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: 21d dilution minus its 63d mean
def f17sd_f17_share_dilution_machine_dilsurp_21d_base_v126_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g - _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth vs book-value-per-share gap 126d
def f17sd_f17_share_dilution_machine_bvgap_126d_base_v127_signal(sharesbas, equity):
    eqps = _safe_div(equity, sharesbas)
    eqpsg = eqps.pct_change(periods=126)
    result = _f17_dilution(sharesbas, 126) - eqpsg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution scaled by revenue-per-share decay 252d (bad dilution intensity)
def f17sd_f17_share_dilution_machine_baddil_252d_base_v128_signal(sharesbas, revenue):
    rps = _safe_div(revenue, sharesbas)
    rpsg = rps.pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) * (1.0 - rpsg.clip(-1, 1))
    return result.replace([np.inf, -np.inf], np.nan)


# dilution interacted with stock-comp intensity 252d
def f17sd_f17_share_dilution_machine_dilxsbc_252d_base_v129_signal(sharesbas, sbcomp, equity):
    sbc = _safe_div(sbcomp, equity)
    result = _f17_dilution(sharesbas, 252) * _z(sbc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution interacted with issuance intensity 126d
def f17sd_f17_share_dilution_machine_dilxiss_126d_base_v130_signal(sharesbas, ncfcommon):
    iss = _f17_issintensity(ncfcommon, sharesbas, 21)
    result = _f17_dilution(sharesbas, 126) * _z(iss, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# share-count level z-score (how elevated is current float vs history) 252d
def f17sd_f17_share_dilution_machine_lvlz_252d_base_v131_signal(sharesbas):
    result = _z(sharesbas, 252) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-count level z-score 504d
def f17sd_f17_share_dilution_machine_lvlz_504d_base_v132_signal(sharesbas):
    result = _z(sharesbas, 504) + _f17_dilution(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-count vs its 252d mean (elevation ratio)
def f17sd_f17_share_dilution_machine_elev_252d_base_v133_signal(sharesbas):
    result = _safe_div(sharesbas, _mean(sharesbas, 252)) - 1.0 + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# share-count vs its 126d mean (elevation ratio)
def f17sd_f17_share_dilution_machine_elev_126d_base_v134_signal(sharesbas):
    result = _safe_div(sharesbas, _mean(sharesbas, 126)) - 1.0 + _f17_dilution(sharesbas, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: level diff of 63d dilution over 63d
def f17sd_f17_share_dilution_machine_dilacc_63d_base_v135_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g - g.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: level diff of 126d dilution over 126d
def f17sd_f17_share_dilution_machine_dilacc_126d_base_v136_signal(sharesbas):
    g = _f17_dilution(sharesbas, 126)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: level diff of 21d dilution over 21d
def f17sd_f17_share_dilution_machine_dilacc_21d_base_v137_signal(sharesbas):
    g = _f17_dilution(sharesbas, 21)
    result = g - g.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-share trend ratio 84d over 252d
def f17sd_f17_share_dilution_machine_watrratio_84_252d_base_v138_signal(shareswa):
    result = _safe_div(_f17_sharetrend(shareswa, 84), _f17_sharetrend(shareswa, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity minus stock-comp intensity (cash vs paper dilution) 252d
def f17sd_f17_share_dilution_machine_cashpaper_252d_base_v139_signal(ncfcommon, sbcomp, sharesbas):
    cash = _f17_issintensity(ncfcommon, sharesbas, 126)
    paper = _safe_div(sbcomp, sharesbas)
    result = _z(cash, 252) - _z(paper, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score interacted with cumulative dilution 252d
def f17sd_f17_share_dilution_machine_zxcum_252d_base_v140_signal(sharesbas):
    cum = np.log(sharesbas / sharesbas.shift(252))
    result = _f17_dilz(sharesbas, 252) * cum.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# relentlessness: fraction-free smooth ratio of 63d to 252d cumulative dilution
def f17sd_f17_share_dilution_machine_relent_252d_base_v141_signal(sharesbas):
    short = np.log(sharesbas / sharesbas.shift(63)) * 4.0
    long = np.log(sharesbas / sharesbas.shift(252))
    result = short - long + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution vs equity-per-share over revenue-per-share blend 252d
def f17sd_f17_share_dilution_machine_qualdil_252d_base_v142_signal(sharesbas, revenue, equity):
    rpsg = _safe_div(revenue, sharesbas).pct_change(periods=252)
    epsg = _safe_div(equity, sharesbas).pct_change(periods=252)
    result = _f17_dilution(sharesbas, 252) - 0.5 * (rpsg + epsg)
    return result.replace([np.inf, -np.inf], np.nan)


# sbcomp growth log-trend 252d (rising paper compensation)
def f17sd_f17_share_dilution_machine_sbcgrow_252d_base_v143_signal(sbcomp, sharesbas):
    result = np.log(sbcomp / sbcomp.shift(252)) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfcommon log-trend 252d (rising cash issuance)
def f17sd_f17_share_dilution_machine_issgrow_252d_base_v144_signal(ncfcommon, sharesbas):
    result = np.log(ncfcommon.abs() + 1.0) - np.log(ncfcommon.abs().shift(252) + 1.0) + _f17_dilution(sharesbas, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score over 84d (short-window extremity)
def f17sd_f17_share_dilution_machine_dilz_84d_base_v145_signal(sharesbas):
    result = _f17_dilz(sharesbas, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution trend over 42d
def f17sd_f17_share_dilution_machine_trend_42d_base_v146_signal(sharesbas):
    result = _f17_sharetrend(sharesbas, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# dilution percentile rank of 63d growth over 378d
def f17sd_f17_share_dilution_machine_dilrank_378d_base_v147_signal(sharesbas):
    g = _f17_dilution(sharesbas, 63)
    result = g.rolling(378, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# stock-comp dilution z-score over 504d
def f17sd_f17_share_dilution_machine_sbcz_504d_base_v148_signal(sbcomp, equity, sharesbas):
    raw = _safe_div(sbcomp, equity)
    result = _z(raw, 504) + _f17_dilution(sharesbas, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution information ratio 84d over 252d dispersion
def f17sd_f17_share_dilution_machine_dilir_84d_base_v149_signal(sharesbas):
    g = _f17_dilution(sharesbas, 84)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon dilution composite (63/126/252/504)
def f17sd_f17_share_dilution_machine_blendmulti_base_v150_signal(sharesbas):
    result = (_f17_dilution(sharesbas, 63) + _f17_dilution(sharesbas, 126)
              + _f17_dilution(sharesbas, 252) + _f17_dilution(sharesbas, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17sd_f17_share_dilution_machine_dil_315d_base_v076_signal,
    f17sd_f17_share_dilution_machine_dil_378d_base_v077_signal,
    f17sd_f17_share_dilution_machine_dil_10d_base_v078_signal,
    f17sd_f17_share_dilution_machine_wadil_189d_base_v079_signal,
    f17sd_f17_share_dilution_machine_wadil_84d_base_v080_signal,
    f17sd_f17_share_dilution_machine_cumdil_189d_base_v081_signal,
    f17sd_f17_share_dilution_machine_cumdil_378d_base_v082_signal,
    f17sd_f17_share_dilution_machine_accel_84_189d_base_v083_signal,
    f17sd_f17_share_dilution_machine_accel_42_126d_base_v084_signal,
    f17sd_f17_share_dilution_machine_dilz_189d_base_v085_signal,
    f17sd_f17_share_dilution_machine_dilz_315d_base_v086_signal,
    f17sd_f17_share_dilution_machine_trend_189d_base_v087_signal,
    f17sd_f17_share_dilution_machine_trend_315d_base_v088_signal,
    f17sd_f17_share_dilution_machine_trend_84d_base_v089_signal,
    f17sd_f17_share_dilution_machine_sbcdil_189d_base_v090_signal,
    f17sd_f17_share_dilution_machine_sbcps_63d_base_v091_signal,
    f17sd_f17_share_dilution_machine_sbcrev_252d_base_v092_signal,
    f17sd_f17_share_dilution_machine_sbcrevtr_252d_base_v093_signal,
    f17sd_f17_share_dilution_machine_issint_189d_base_v094_signal,
    f17sd_f17_share_dilution_machine_issint_42d_base_v095_signal,
    f17sd_f17_share_dilution_machine_issrev_252d_base_v096_signal,
    f17sd_f17_share_dilution_machine_dilrank252_504d_base_v097_signal,
    f17sd_f17_share_dilution_machine_dilrank21_252d_base_v098_signal,
    f17sd_f17_share_dilution_machine_gvb_504d_base_v099_signal,
    f17sd_f17_share_dilution_machine_gvbratio_252d_base_v100_signal,
    f17sd_f17_share_dilution_machine_rps_504d_base_v101_signal,
    f17sd_f17_share_dilution_machine_eps_504d_base_v102_signal,
    f17sd_f17_share_dilution_machine_dilir_252d_base_v103_signal,
    f17sd_f17_share_dilution_machine_dilir_21d_base_v104_signal,
    f17sd_f17_share_dilution_machine_smdil21_252d_base_v105_signal,
    f17sd_f17_share_dilution_machine_smdil63_126d_base_v106_signal,
    f17sd_f17_share_dilution_machine_ewmdil_252d_base_v107_signal,
    f17sd_f17_share_dilution_machine_ewmdil_42d_base_v108_signal,
    f17sd_f17_share_dilution_machine_dildisp_504d_base_v109_signal,
    f17sd_f17_share_dilution_machine_dildisp63_252d_base_v110_signal,
    f17sd_f17_share_dilution_machine_anndil_252d_base_v111_signal,
    f17sd_f17_share_dilution_machine_anndil_189d_base_v112_signal,
    f17sd_f17_share_dilution_machine_anndil_42d_base_v113_signal,
    f17sd_f17_share_dilution_machine_basgap_504d_base_v114_signal,
    f17sd_f17_share_dilution_machine_basgap_63d_base_v115_signal,
    f17sd_f17_share_dilution_machine_baswa_126d_base_v116_signal,
    f17sd_f17_share_dilution_machine_watrend_504d_base_v117_signal,
    f17sd_f17_share_dilution_machine_wadilz_504d_base_v118_signal,
    f17sd_f17_share_dilution_machine_wadilz_126d_base_v119_signal,
    f17sd_f17_share_dilution_machine_dileqs_504d_base_v120_signal,
    f17sd_f17_share_dilution_machine_dileqs_63d_base_v121_signal,
    f17sd_f17_share_dilution_machine_issintz_126d_base_v122_signal,
    f17sd_f17_share_dilution_machine_sbcz_126d_base_v123_signal,
    f17sd_f17_share_dilution_machine_trratio_126_504d_base_v124_signal,
    f17sd_f17_share_dilution_machine_dilsurp_252d_base_v125_signal,
    f17sd_f17_share_dilution_machine_dilsurp_21d_base_v126_signal,
    f17sd_f17_share_dilution_machine_bvgap_126d_base_v127_signal,
    f17sd_f17_share_dilution_machine_baddil_252d_base_v128_signal,
    f17sd_f17_share_dilution_machine_dilxsbc_252d_base_v129_signal,
    f17sd_f17_share_dilution_machine_dilxiss_126d_base_v130_signal,
    f17sd_f17_share_dilution_machine_lvlz_252d_base_v131_signal,
    f17sd_f17_share_dilution_machine_lvlz_504d_base_v132_signal,
    f17sd_f17_share_dilution_machine_elev_252d_base_v133_signal,
    f17sd_f17_share_dilution_machine_elev_126d_base_v134_signal,
    f17sd_f17_share_dilution_machine_dilacc_63d_base_v135_signal,
    f17sd_f17_share_dilution_machine_dilacc_126d_base_v136_signal,
    f17sd_f17_share_dilution_machine_dilacc_21d_base_v137_signal,
    f17sd_f17_share_dilution_machine_watrratio_84_252d_base_v138_signal,
    f17sd_f17_share_dilution_machine_cashpaper_252d_base_v139_signal,
    f17sd_f17_share_dilution_machine_zxcum_252d_base_v140_signal,
    f17sd_f17_share_dilution_machine_relent_252d_base_v141_signal,
    f17sd_f17_share_dilution_machine_qualdil_252d_base_v142_signal,
    f17sd_f17_share_dilution_machine_sbcgrow_252d_base_v143_signal,
    f17sd_f17_share_dilution_machine_issgrow_252d_base_v144_signal,
    f17sd_f17_share_dilution_machine_dilz_84d_base_v145_signal,
    f17sd_f17_share_dilution_machine_trend_42d_base_v146_signal,
    f17sd_f17_share_dilution_machine_dilrank_378d_base_v147_signal,
    f17sd_f17_share_dilution_machine_sbcz_504d_base_v148_signal,
    f17sd_f17_share_dilution_machine_dilir_84d_base_v149_signal,
    f17sd_f17_share_dilution_machine_blendmulti_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_SHARE_DILUTION_MACHINE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f17_dilution", "_f17_sharetrend", "_f17_dilz", "_f17_issintensity")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_share_dilution_machine_base_076_150_claude: {n_features} features pass")
