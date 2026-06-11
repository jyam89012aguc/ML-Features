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


def _slope(s, w):
    # ordinary-least-squares style slope via diff over w scaled by w (per-day trend)
    return s.diff(periods=w) / float(w)


# ===== folder domain primitives (dilution-adjusted per-share growth) =====
def _f25_ps(numer, shares):
    # per-share level: a fundamental flow/stock divided by share count
    return numer / shares.replace(0, np.nan)


def _f25_psgrowth(numer, shares, w):
    # per-share value pct change over w (dilution-adjusted growth)
    ps = numer / shares.replace(0, np.nan)
    return ps.pct_change(periods=w)


def _f25_fcfps(fcf, shares):
    # free-cash-flow per share
    return fcf / shares.replace(0, np.nan)


def _f25_bvps(equity, shares):
    # book value (equity) per share
    return equity / shares.replace(0, np.nan)


# ============ FEATURES 076-150 ============

# gp/share growth over 504d
def f25dg_f25_dilution_adjusted_growth_gppsg_504d_base_v076_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth over 504d
def f25dg_f25_dilution_adjusted_growth_fcfpsg_504d_base_v077_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# book value/share growth over 504d
def f25dg_f25_dilution_adjusted_growth_bvpsg_504d_base_v078_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=504)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 21d using weighted shares
def f25dg_f25_dilution_adjusted_growth_spswag_21d_base_v079_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 126d using weighted shares
def f25dg_f25_dilution_adjusted_growth_spswag_126d_base_v080_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of revenue/share growth (252d) over 504d
def f25dg_f25_dilution_adjusted_growth_zspsg_252d_base_v081_signal(revenue, sharesbas):
    result = _z(_f25_psgrowth(revenue, sharesbas, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of gp/share growth (126d) over 252d
def f25dg_f25_dilution_adjusted_growth_zgppsg_126d_base_v082_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _z(ps.pct_change(periods=126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of book value/share growth (252d) over 504d
def f25dg_f25_dilution_adjusted_growth_zbvpsg_252d_base_v083_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _z(ps.pct_change(periods=252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share trend slope over 252d
def f25dg_f25_dilution_adjusted_growth_gpslope_252d_base_v084_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _slope(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# book-value-per-share trend slope over 252d
def f25dg_f25_dilution_adjusted_growth_bvpslope_252d_base_v085_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _slope(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized gp-per-share slope over 126d
def f25dg_f25_dilution_adjusted_growth_gpnslope_126d_base_v086_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(_slope(ps, 126), _mean(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# normalized book-value-per-share slope over 252d
def f25dg_f25_dilution_adjusted_growth_bvpnslope_252d_base_v087_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _safe_div(_slope(ps, 252), _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share log compounding annualized (252d)
def f25dg_f25_dilution_adjusted_growth_gplogcompound_252d_base_v088_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    return result.replace([np.inf, -np.inf], np.nan)


# book-value-per-share log compounding annualized from 126d
def f25dg_f25_dilution_adjusted_growth_bvplogcompound_126d_base_v089_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-per-share percentile rank (126d growth over 504d window)
def f25dg_f25_dilution_adjusted_growth_fcfgrank_126d_base_v090_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=126)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share growth percentile rank (252d growth over 504d window)
def f25dg_f25_dilution_adjusted_growth_gpgrank_252d_base_v091_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-per-share level percentile rank over 252d
def f25dg_f25_dilution_adjusted_growth_fcflevrank_252d_base_v092_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation over 504d window (per-share growth minus dilution)
def f25dg_f25_dilution_adjusted_growth_netcreate_504d_base_v093_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 504)
    shg = sharesbas.pct_change(periods=504)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation over 63d (short horizon)
def f25dg_f25_dilution_adjusted_growth_netcreate_63d_base_v094_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 63)
    shg = sharesbas.pct_change(periods=63)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# fcf net value creation over 126d
def f25dg_f25_dilution_adjusted_growth_fcfnetcreate_126d_base_v095_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# gp net value creation over 126d
def f25dg_f25_dilution_adjusted_growth_gpnetcreate_126d_base_v096_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=126)
    shg = sharesbas.pct_change(periods=126)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag for fcf (raw fcf growth minus per-share fcf growth, 252d)
def f25dg_f25_dilution_adjusted_growth_fcfdilutiondrag_252d_base_v097_signal(fcf, sharesbas):
    rawg = fcf.pct_change(periods=252)
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    result = rawg - psg
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag for gp (252d)
def f25dg_f25_dilution_adjusted_growth_gpdilutiondrag_252d_base_v098_signal(gp, sharesbas):
    rawg = gp.pct_change(periods=252)
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    result = rawg - psg
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp/share growth (42d mean of 126d growth)
def f25dg_f25_dilution_adjusted_growth_gpgsmooth_126d_base_v099_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _mean(ps.pct_change(periods=126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed fcf/share growth (42d mean of 126d growth)
def f25dg_f25_dilution_adjusted_growth_fcfgsmooth_126d_base_v100_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _mean(ps.pct_change(periods=126), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth acceleration 63 vs 126
def f25dg_f25_dilution_adjusted_growth_gpgaccel_63_126_base_v101_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=63) - ps.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# book-value/share growth acceleration 126 vs 252
def f25dg_f25_dilution_adjusted_growth_bvpgaccel_126_252_base_v102_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=126) - ps.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth acceleration 21 vs 63
def f25dg_f25_dilution_adjusted_growth_psgaccel_21_63_base_v103_signal(revenue, sharesbas):
    result = _f25_psgrowth(revenue, sharesbas, 21) - _f25_psgrowth(revenue, sharesbas, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth spread: revenue vs book-value per-share growth (252d)
def f25dg_f25_dilution_adjusted_growth_revbvpspread_252d_base_v104_signal(revenue, equity, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    bvps = _f25_bvps(equity, sharesbas)
    bg = bvps.pct_change(periods=252)
    result = rg - bg
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth spread: gp vs fcf per-share growth (252d)
def f25dg_f25_dilution_adjusted_growth_gpfcfspread_252d_base_v105_signal(gp, fcf, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    result = gg - fg
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share level ratio to 252d mean
def f25dg_f25_dilution_adjusted_growth_gplevratio_252d_base_v106_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(ps, _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share level ratio to 126d mean
def f25dg_f25_dilution_adjusted_growth_pslevratio_126d_base_v107_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _safe_div(ps, _mean(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share yield vs price
def f25dg_f25_dilution_adjusted_growth_gpyield_0d_base_v108_signal(gp, sharesbas, closeadj):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(ps, closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share growth vs price momentum spread (252d)
def f25dg_f25_dilution_adjusted_growth_psgpricespread_252d_base_v109_signal(revenue, sharesbas, closeadj):
    psg = _f25_psgrowth(revenue, sharesbas, 252)
    pricg = closeadj.pct_change(periods=252)
    result = psg - pricg
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth quality: 63d growth / dispersion
def f25dg_f25_dilution_adjusted_growth_psgqual_63d_base_v110_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 63)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gp per-share growth quality (126d growth / dispersion)
def f25dg_f25_dilution_adjusted_growth_gpgqual_126d_base_v111_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    g = ps.pct_change(periods=126)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# book-value per-share growth quality (252d)
def f25dg_f25_dilution_adjusted_growth_bvpgqual_252d_base_v112_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    g = ps.pct_change(periods=252)
    result = _safe_div(g, _std(g, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-share slope z-normalized (252d)
def f25dg_f25_dilution_adjusted_growth_gpslopez_252d_base_v113_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-per-share slope z-normalized (252d)
def f25dg_f25_dilution_adjusted_growth_fcfslopez_252d_base_v114_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _safe_div(_slope(ps, 252), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gp dilution-adjusted log compounding net of share growth (252d)
def f25dg_f25_dilution_adjusted_growth_gplognetcompound_252d_base_v115_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    gplog = np.log(_safe_div(gp, gp.shift(252)))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = gplog - shlog + ps * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf dilution-adjusted log compounding net of share growth (252d)
def f25dg_f25_dilution_adjusted_growth_fcflognetcompound_252d_base_v116_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    fcflog = np.log(_safe_div(fcf.abs() + 1.0, fcf.shift(252).abs() + 1.0))
    shlog = np.log(_safe_div(sharesbas, sharesbas.shift(252)))
    result = fcflog - shlog + ps * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth over 84d
def f25dg_f25_dilution_adjusted_growth_gppsg_84d_base_v117_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = ps.pct_change(periods=84)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth over 189d
def f25dg_f25_dilution_adjusted_growth_fcfpsg_189d_base_v118_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = ps.pct_change(periods=189)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth over 504d using weighted shares
def f25dg_f25_dilution_adjusted_growth_spswag_504d_base_v119_signal(revenue, shareswa):
    result = _f25_psgrowth(revenue, shareswa, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# book-value/share growth over 189d
def f25dg_f25_dilution_adjusted_growth_bvpsg_189d_base_v120_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = ps.pct_change(periods=189)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/share growth annualized from 126d
def f25dg_f25_dilution_adjusted_growth_spsgann_126d_base_v121_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(126))) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# gp/share growth annualized from 252d
def f25dg_f25_dilution_adjusted_growth_gpgann_252d_base_v122_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    result = np.log(_safe_div(ps, ps.shift(252)))
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share growth annualized from 252d
def f25dg_f25_dilution_adjusted_growth_fcfgann_252d_base_v123_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = np.log(_safe_div(ps.abs() + 1.0, ps.shift(252).abs() + 1.0))
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth dispersion of 126d growth over 504d
def f25dg_f25_dilution_adjusted_growth_psgdisp_504d_base_v124_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 126)
    result = _std(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per-share growth dispersion of 63d growth over 252d
def f25dg_f25_dilution_adjusted_growth_fcfgdisp_252d_base_v125_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=63)
    result = _std(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share EWMA-smoothed growth span 126
def f25dg_f25_dilution_adjusted_growth_psewm_126d_base_v126_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=126, min_periods=42).mean() * 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# gp per share EWMA-smoothed growth span 63
def f25dg_f25_dilution_adjusted_growth_gpewm_63d_base_v127_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=63, min_periods=21).mean() * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share EWMA-smoothed growth span 252
def f25dg_f25_dilution_adjusted_growth_bvpewm_252d_base_v128_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    lr = np.log(_safe_div(ps, ps.shift(1)))
    result = lr.ewm(span=252, min_periods=84).mean() * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/share conversion change: fcf-per-rev ratio growth (252d)
def f25dg_f25_dilution_adjusted_growth_fcfconvchg_252d_base_v129_signal(fcf, revenue, sharesbas):
    fps = _f25_fcfps(fcf, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    conv = _safe_div(fps, sps)
    result = conv.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin-per-share change (gp/rev per-share ratio growth, 252d)
def f25dg_f25_dilution_adjusted_growth_gpmarginchg_252d_base_v130_signal(gp, revenue, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    sps = _f25_ps(revenue, sharesbas)
    margin = _safe_div(gpps, sps)
    result = margin.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share to book-value-per-share ratio change (252d)
def f25dg_f25_dilution_adjusted_growth_spsbvpchg_252d_base_v131_signal(revenue, equity, sharesbas):
    sps = _f25_ps(revenue, sharesbas)
    bvps = _f25_bvps(equity, sharesbas)
    ratio = _safe_div(sps, bvps)
    result = ratio.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of fcf-per-share level over 252d
def f25dg_f25_dilution_adjusted_growth_zfcflev_252d_base_v132_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = _z(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of revenue-per-share level over 504d
def f25dg_f25_dilution_adjusted_growth_zpslev_504d_base_v133_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    result = _z(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of book-value-per-share level over 252d
def f25dg_f25_dilution_adjusted_growth_zbvplev_252d_base_v134_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = _z(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation z (gp per-share growth net of dilution, 252d)
def f25dg_f25_dilution_adjusted_growth_zgpnetcreate_252d_base_v135_signal(gp, sharesbas):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net value creation z (fcf per-share growth net of dilution, 252d)
def f25dg_f25_dilution_adjusted_growth_zfcfnetcreate_252d_base_v136_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    psg = ps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = _z(psg - shg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dual-share dilution-adjusted gp growth (basic vs weighted, 252d)
def f25dg_f25_dilution_adjusted_growth_gpdualshare_252d_base_v137_signal(gp, sharesbas, shareswa):
    gpps = _f25_ps(gp, sharesbas)
    psg = gpps.pct_change(periods=252)
    wadil = shareswa.pct_change(periods=252)
    result = psg - wadil
    return result.replace([np.inf, -np.inf], np.nan)


# share-count growth drag on revenue per share (weighted shares, 126d)
def f25dg_f25_dilution_adjusted_growth_wadilution_126d_base_v138_signal(revenue, shareswa):
    psg = _f25_psgrowth(revenue, shareswa, 126)
    shg = shareswa.pct_change(periods=126)
    result = psg - shg
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth smoothed long (63d mean of 252d growth)
def f25dg_f25_dilution_adjusted_growth_spsgsmooth_252d_base_v139_signal(revenue, sharesbas):
    result = _mean(_f25_psgrowth(revenue, sharesbas, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per-share growth percentile rank (252d growth over 504d)
def f25dg_f25_dilution_adjusted_growth_fcfgrank_252d_base_v140_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# book-value per-share growth percentile rank (252d growth over 504d)
def f25dg_f25_dilution_adjusted_growth_bvpgrank_252d_base_v141_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    g = ps.pct_change(periods=252)
    result = g.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per-share growth surprise (252d growth minus its 126d mean)
def f25dg_f25_dilution_adjusted_growth_psgsurp_252d_base_v142_signal(revenue, sharesbas):
    g = _f25_psgrowth(revenue, sharesbas, 252)
    result = g - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf per-share growth surprise (126d growth minus its 63d mean)
def f25dg_f25_dilution_adjusted_growth_fcfgsurp_126d_base_v143_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    g = ps.pct_change(periods=126)
    result = g - _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per-share growth ratio short/long (63d over 252d)
def f25dg_f25_dilution_adjusted_growth_psgratio_63_252_base_v144_signal(revenue, sharesbas):
    s = _f25_psgrowth(revenue, sharesbas, 63)
    l = _f25_psgrowth(revenue, sharesbas, 252)
    result = _safe_div(s, l.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gp per-share growth ratio short/long (126d over 252d)
def f25dg_f25_dilution_adjusted_growth_gpgratio_126_252_base_v145_signal(gp, sharesbas):
    ps = _f25_ps(gp, sharesbas)
    s = ps.pct_change(periods=126)
    l = ps.pct_change(periods=252)
    result = _safe_div(s, l.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level smoothed slope normalized (slope of 21d mean over 252d)
def f25dg_f25_dilution_adjusted_growth_pssmoothslope_252d_base_v146_signal(revenue, sharesbas):
    ps = _f25_ps(revenue, sharesbas)
    sm = _mean(ps, 21)
    result = _safe_div(_slope(sm, 252), _mean(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# combined per-share value composite: rev + gp + fcf per-share growth net of dilution (252d)
def f25dg_f25_dilution_adjusted_growth_valuecomposite_252d_base_v147_signal(revenue, gp, fcf, sharesbas):
    rg = _f25_psgrowth(revenue, sharesbas, 252)
    gpps = _f25_ps(gp, sharesbas)
    gg = gpps.pct_change(periods=252)
    fps = _f25_fcfps(fcf, sharesbas)
    fg = fps.pct_change(periods=252)
    shg = sharesbas.pct_change(periods=252)
    result = (rg + gg + fg) / 3.0 - shg
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon fcf per-share growth (126/252/504)
def f25dg_f25_dilution_adjusted_growth_fcfgblend_multi_base_v148_signal(fcf, sharesbas):
    ps = _f25_fcfps(fcf, sharesbas)
    result = (ps.pct_change(periods=126)
              + ps.pct_change(periods=252)
              + ps.pct_change(periods=504)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon book-value per-share growth (126/252/504)
def f25dg_f25_dilution_adjusted_growth_bvpgblend_multi_base_v149_signal(equity, sharesbas):
    ps = _f25_bvps(equity, sharesbas)
    result = (ps.pct_change(periods=126)
              + ps.pct_change(periods=252)
              + ps.pct_change(periods=504)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted total value creation composite z (252d)
def f25dg_f25_dilution_adjusted_growth_netcreatez_504d_base_v150_signal(revenue, sharesbas):
    psg = _f25_psgrowth(revenue, sharesbas, 504)
    shg = sharesbas.pct_change(periods=504)
    result = _z(psg - shg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25dg_f25_dilution_adjusted_growth_gppsg_504d_base_v076_signal,
    f25dg_f25_dilution_adjusted_growth_fcfpsg_504d_base_v077_signal,
    f25dg_f25_dilution_adjusted_growth_bvpsg_504d_base_v078_signal,
    f25dg_f25_dilution_adjusted_growth_spswag_21d_base_v079_signal,
    f25dg_f25_dilution_adjusted_growth_spswag_126d_base_v080_signal,
    f25dg_f25_dilution_adjusted_growth_zspsg_252d_base_v081_signal,
    f25dg_f25_dilution_adjusted_growth_zgppsg_126d_base_v082_signal,
    f25dg_f25_dilution_adjusted_growth_zbvpsg_252d_base_v083_signal,
    f25dg_f25_dilution_adjusted_growth_gpslope_252d_base_v084_signal,
    f25dg_f25_dilution_adjusted_growth_bvpslope_252d_base_v085_signal,
    f25dg_f25_dilution_adjusted_growth_gpnslope_126d_base_v086_signal,
    f25dg_f25_dilution_adjusted_growth_bvpnslope_252d_base_v087_signal,
    f25dg_f25_dilution_adjusted_growth_gplogcompound_252d_base_v088_signal,
    f25dg_f25_dilution_adjusted_growth_bvplogcompound_126d_base_v089_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgrank_126d_base_v090_signal,
    f25dg_f25_dilution_adjusted_growth_gpgrank_252d_base_v091_signal,
    f25dg_f25_dilution_adjusted_growth_fcflevrank_252d_base_v092_signal,
    f25dg_f25_dilution_adjusted_growth_netcreate_504d_base_v093_signal,
    f25dg_f25_dilution_adjusted_growth_netcreate_63d_base_v094_signal,
    f25dg_f25_dilution_adjusted_growth_fcfnetcreate_126d_base_v095_signal,
    f25dg_f25_dilution_adjusted_growth_gpnetcreate_126d_base_v096_signal,
    f25dg_f25_dilution_adjusted_growth_fcfdilutiondrag_252d_base_v097_signal,
    f25dg_f25_dilution_adjusted_growth_gpdilutiondrag_252d_base_v098_signal,
    f25dg_f25_dilution_adjusted_growth_gpgsmooth_126d_base_v099_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgsmooth_126d_base_v100_signal,
    f25dg_f25_dilution_adjusted_growth_gpgaccel_63_126_base_v101_signal,
    f25dg_f25_dilution_adjusted_growth_bvpgaccel_126_252_base_v102_signal,
    f25dg_f25_dilution_adjusted_growth_psgaccel_21_63_base_v103_signal,
    f25dg_f25_dilution_adjusted_growth_revbvpspread_252d_base_v104_signal,
    f25dg_f25_dilution_adjusted_growth_gpfcfspread_252d_base_v105_signal,
    f25dg_f25_dilution_adjusted_growth_gplevratio_252d_base_v106_signal,
    f25dg_f25_dilution_adjusted_growth_pslevratio_126d_base_v107_signal,
    f25dg_f25_dilution_adjusted_growth_gpyield_0d_base_v108_signal,
    f25dg_f25_dilution_adjusted_growth_psgpricespread_252d_base_v109_signal,
    f25dg_f25_dilution_adjusted_growth_psgqual_63d_base_v110_signal,
    f25dg_f25_dilution_adjusted_growth_gpgqual_126d_base_v111_signal,
    f25dg_f25_dilution_adjusted_growth_bvpgqual_252d_base_v112_signal,
    f25dg_f25_dilution_adjusted_growth_gpslopez_252d_base_v113_signal,
    f25dg_f25_dilution_adjusted_growth_fcfslopez_252d_base_v114_signal,
    f25dg_f25_dilution_adjusted_growth_gplognetcompound_252d_base_v115_signal,
    f25dg_f25_dilution_adjusted_growth_fcflognetcompound_252d_base_v116_signal,
    f25dg_f25_dilution_adjusted_growth_gppsg_84d_base_v117_signal,
    f25dg_f25_dilution_adjusted_growth_fcfpsg_189d_base_v118_signal,
    f25dg_f25_dilution_adjusted_growth_spswag_504d_base_v119_signal,
    f25dg_f25_dilution_adjusted_growth_bvpsg_189d_base_v120_signal,
    f25dg_f25_dilution_adjusted_growth_spsgann_126d_base_v121_signal,
    f25dg_f25_dilution_adjusted_growth_gpgann_252d_base_v122_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgann_252d_base_v123_signal,
    f25dg_f25_dilution_adjusted_growth_psgdisp_504d_base_v124_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgdisp_252d_base_v125_signal,
    f25dg_f25_dilution_adjusted_growth_psewm_126d_base_v126_signal,
    f25dg_f25_dilution_adjusted_growth_gpewm_63d_base_v127_signal,
    f25dg_f25_dilution_adjusted_growth_bvpewm_252d_base_v128_signal,
    f25dg_f25_dilution_adjusted_growth_fcfconvchg_252d_base_v129_signal,
    f25dg_f25_dilution_adjusted_growth_gpmarginchg_252d_base_v130_signal,
    f25dg_f25_dilution_adjusted_growth_spsbvpchg_252d_base_v131_signal,
    f25dg_f25_dilution_adjusted_growth_zfcflev_252d_base_v132_signal,
    f25dg_f25_dilution_adjusted_growth_zpslev_504d_base_v133_signal,
    f25dg_f25_dilution_adjusted_growth_zbvplev_252d_base_v134_signal,
    f25dg_f25_dilution_adjusted_growth_zgpnetcreate_252d_base_v135_signal,
    f25dg_f25_dilution_adjusted_growth_zfcfnetcreate_252d_base_v136_signal,
    f25dg_f25_dilution_adjusted_growth_gpdualshare_252d_base_v137_signal,
    f25dg_f25_dilution_adjusted_growth_wadilution_126d_base_v138_signal,
    f25dg_f25_dilution_adjusted_growth_spsgsmooth_252d_base_v139_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgrank_252d_base_v140_signal,
    f25dg_f25_dilution_adjusted_growth_bvpgrank_252d_base_v141_signal,
    f25dg_f25_dilution_adjusted_growth_psgsurp_252d_base_v142_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgsurp_126d_base_v143_signal,
    f25dg_f25_dilution_adjusted_growth_psgratio_63_252_base_v144_signal,
    f25dg_f25_dilution_adjusted_growth_gpgratio_126_252_base_v145_signal,
    f25dg_f25_dilution_adjusted_growth_pssmoothslope_252d_base_v146_signal,
    f25dg_f25_dilution_adjusted_growth_valuecomposite_252d_base_v147_signal,
    f25dg_f25_dilution_adjusted_growth_fcfgblend_multi_base_v148_signal,
    f25dg_f25_dilution_adjusted_growth_bvpgblend_multi_base_v149_signal,
    f25dg_f25_dilution_adjusted_growth_netcreatez_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_DILUTION_ADJUSTED_GROWTH_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume", "marketcap",
           "ev", "assets", "assetsc", "equity", "revenue", "gp", "ebitda", "ppnenet",
           "sharesbas", "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "intangibles", "evebitda", "evebit", "pe", "pb", "ps",
           "currentratio", "bvps", "sps", "shrvalue", "shrunits", "totalvalue",
           "percentoftotal", "sf3a_shares", "sf3a_value", "sf3b_shares", "sf3b_value",
           "grossmargin", "beta1y", "beta5y", "invcap", "debt", "fcf"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + np.abs(np.random.normal(0, 0.02, n))), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - np.abs(np.random.normal(0, 0.02, n))), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f25_ps", "_f25_psgrowth", "_f25_fcfps", "_f25_bvps")
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
    print(f"OK f25_dilution_adjusted_growth_base_076_150_claude: {n_features} features pass")
