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
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    xm = (w - 1) / 2.0
    xden = float(((np.arange(w) - xm) ** 2).sum())

    def _f(a):
        am = a.mean()
        return float(((np.arange(len(a)) - xm) * (a - am)).sum() / xden)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (quality compounder) =====
def _f41_growth(s, w):
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f41_dilution(sharesbas, w):
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f41_pos_frac(s, w):
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_stab(s, w):
    return _mean(s, w) / _std(s, w).replace(0, np.nan)


def _f41_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


# ============================================================
# core compounder index z-blend: roic + fcf-margin minus dilution (standardized), 252d
def f41qc_f41_quality_compounder_zblend_252d_base_v076_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    b = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level rank vs own 504d history (relative quality regime), 252d
def f41qc_f41_quality_compounder_roicrank_252d_base_v077_signal(roic):
    b = _rank(_mean(roic, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin minus FCF-margin spread (accrual-vs-cash quality gap), 252d
def f41qc_f41_quality_compounder_accrualgap_252d_base_v078_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _mean(fcfm, 126) - _mean(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-growth z gated by ROIC positivity (return-funded book build), 252d
def f41qc_f41_quality_compounder_retfundbook_252d_base_v079_signal(equity, roic):
    eg = _f41_growth(equity, 252)
    pos = _f41_pos_frac(roic, 252) - 0.5
    b = _z(eg, 252) * np.sign(pos) + 2.0 * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z minus margin z (issuance overhang net of profitability), 252d
def f41qc_f41_quality_compounder_dilovhng_252d_base_v080_signal(sharesbas, netmargin):
    dil = _f41_dilution(sharesbas, 63)
    b = _z(dil, 252) - _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/equity dispersion (volatility of cash return on book), inverted, 252d
def f41qc_f41_quality_compounder_cashroevol_252d_base_v081_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    b = -_z(_std(r, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/equity turnover trend (asset productivity slope), 252d
def f41qc_f41_quality_compounder_turntrend_252d_base_v082_signal(revenue, equity):
    turn = _safe_div(revenue, equity)
    b = _slope(turn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-per-share quality: netmargin x (revenue/sharesbas) z, 252d
def f41qc_f41_quality_compounder_marginps_252d_base_v083_signal(netmargin, revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    b = np.sign(_mean(netmargin, 252)) * _z(rps, 252) + _z(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability rank minus dilution rank (consistent quality net of issuance), 252d
def f41qc_f41_quality_compounder_stabrank_252d_base_v084_signal(roic, sharesbas):
    stab = _f41_stab(roic, 252)
    dil = _f41_dilution(sharesbas, 63)
    b = _rank(stab, 504) - _rank(dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin x revenue-growth, but standardized product (cash-generative growth z), 252d
def f41qc_f41_quality_compounder_cashgrowz_252d_base_v085_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    g = _f41_growth(revenue, 126)
    b = _z(fcfm, 252) * np.sign(g) + _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-margin: rolling fraction of days net-margin in top half of own range, 252d
def f41qc_f41_quality_compounder_marginhigh_252d_base_v086_signal(netmargin):
    lo = netmargin.rolling(252, min_periods=126).min()
    hi = netmargin.rolling(252, min_periods=126).max()
    pos = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    b = pos - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-hurdle area: average positive excess over 0.08 (economic-profit intensity), 252d
def f41qc_f41_quality_compounder_econprofit_252d_base_v087_signal(roic):
    excess = (roic - 0.08).clip(lower=0)
    b = _mean(excess, 252) - _mean((0.08 - roic).clip(lower=0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ratio: FCF / (netmargin*revenue proxy) via fcfm/netmargin ratio, 252d
def f41qc_f41_quality_compounder_convratio_252d_base_v088_signal(fcf, revenue, netmargin):
    fcfm = _f41_fcf_margin(fcf, revenue)
    ratio = _safe_div(_mean(fcfm, 126), _mean(netmargin, 126))
    b = np.tanh(ratio - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-per-share level z (book-value-per-share extremity), 252d
def f41qc_f41_quality_compounder_bvpslevel_252d_base_v089_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    b = _z(bvps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-driver dispersion: cross-sectional std of z(roic),z(netmargin),z(fcfm) (driver disagreement), 252d
def f41qc_f41_quality_compounder_drvdisp_252d_base_v090_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    stacked = pd.concat([_z(roic, 252), _z(netmargin, 252), _z(fcfm, 252)], axis=1)
    b = -stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap: FCF level vs equity-financed growth (cash-vs-book funding), 252d
def f41qc_f41_quality_compounder_fundgap_252d_base_v091_signal(fcf, equity):
    fcf_z = _z(fcf, 252)
    eg = _z(_f41_growth(equity, 126), 252)
    b = fcf_z - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin trend rank (improving-margin percentile), 252d
def f41qc_f41_quality_compounder_margintrendrank_252d_base_v092_signal(netmargin):
    tr = _slope(netmargin, 126)
    b = _rank(tr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted FCF yield: FCF/equity minus dilution rate (cash net of share creep), 252d
def f41qc_f41_quality_compounder_dilcashyield_252d_base_v093_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    dil = _f41_dilution(sharesbas, 252)
    b = _mean(cashret, 126) - 0.5 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality momentum: ROIC z change over a quarter (improving returns), 252d
def f41qc_f41_quality_compounder_roiczmom_252d_base_v094_signal(roic):
    zz = _z(roic, 252)
    b = zz - zz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder gate product (continuous): sigmoid(roic) x sigmoid(fcfm) x low-dilution, 252d
def f41qc_f41_quality_compounder_sigmoidgate_252d_base_v095_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    sr = 1.0 / (1.0 + np.exp(-20.0 * _mean(roic, 252)))
    sf = 1.0 / (1.0 + np.exp(-20.0 * _mean(fcfm, 252)))
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    b = sr * sf * (1.0 / (1.0 + 10.0 * dil))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin volatility regime (low vol = durable), ranked, 252d
def f41qc_f41_quality_compounder_marginvolrank_252d_base_v096_signal(netmargin):
    v = _std(netmargin, 126)
    b = -_rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus dilution rank (per-share scaling percentile), 252d
def f41qc_f41_quality_compounder_pscaling_252d_base_v097_signal(revenue, sharesbas):
    g = _f41_growth(revenue, 252)
    dil = _f41_dilution(sharesbas, 252)
    b = _rank(g - dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable cash: FCF positive-fraction excess x FCF-margin z (gated cash quality), 252d
def f41qc_f41_quality_compounder_gatedcash_252d_base_v098_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    pf = _f41_pos_frac(fcfm, 252) - 0.5
    b = pf * (1.0 + _z(fcfm, 126).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x net-margin co-movement (both-strong interaction z), 126d
def f41qc_f41_quality_compounder_roicmarginz_126d_base_v099_signal(roic, netmargin):
    b = _z(roic, 126) * _z(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity compounding stability: equity-growth divided by its dispersion, 252d
def f41qc_f41_quality_compounder_eqstab_252d_base_v100_signal(equity):
    eg = _f41_growth(equity, 63)
    b = _mean(eg, 252) / _std(eg, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution acceleration: change in (z roic - z dil) over a quarter, 252d
def f41qc_f41_quality_compounder_qmdaccel_252d_base_v101_signal(roic, sharesbas):
    dil = _f41_dilution(sharesbas, 63)
    qmd = _z(roic, 252) - _z(dil, 252)
    b = qmd - qmd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-and-margin: log-revenue z interacted with margin sign (big-profitable extremity), 252d
def f41qc_f41_quality_compounder_scalemargin_252d_base_v102_signal(revenue, netmargin):
    logr = np.log(revenue.replace(0, np.nan).abs())
    b = _z(logr, 252) * np.sign(_mean(netmargin, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share growth acceleration (cash-per-share inflection), 252d
def f41qc_f41_quality_compounder_fcfpsaccel_252d_base_v103_signal(fcf, sharesbas):
    fps = _safe_div(fcf, sharesbas)
    b = _f41_growth(fps, 63) - _f41_growth(fps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin x equity-growth standardized (profitable book build z), 252d
def f41qc_f41_quality_compounder_profbookz_252d_base_v104_signal(netmargin, equity):
    eg = _f41_growth(equity, 126)
    b = _z(netmargin, 252) * np.sign(eg) + _z(eg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return durability: fraction of last 252d with ROIC above its 504d median, 252d
def f41qc_f41_quality_compounder_roicabovemed_252d_base_v105_signal(roic):
    med = roic.rolling(504, min_periods=252).median()
    above = (roic > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-accrual quality rank: FCF-margin minus net-margin, percentile, 252d
def f41qc_f41_quality_compounder_qualrank_252d_base_v106_signal(fcf, revenue, netmargin):
    fcfm = _f41_fcf_margin(fcf, revenue)
    gap = _mean(fcfm, 126) - _mean(netmargin, 126)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per share level vs slow EMA (per-share displacement), 252d
def f41qc_f41_quality_compounder_psdisp_252d_base_v107_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    b = (rps - rps.ewm(span=252, min_periods=63).mean()) / rps.ewm(span=252, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-quality composite: avg of z(roic),z(netmargin) gated by FCF positivity, 504d
def f41qc_f41_quality_compounder_durqual_504d_base_v108_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    pf = _f41_pos_frac(fcfm, 504)
    b = ((_z(roic, 504) + _z(netmargin, 504)) / 2.0) * pf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak: fraction of last year with positive share growth (issuance regime), 252d
def f41qc_f41_quality_compounder_dilstreak_252d_base_v109_signal(sharesbas):
    sg = sharesbas.pct_change(63)
    issuing = (sg > 0).astype(float)
    b = 0.5 - issuing.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x FCF-margin geometric (signed sqrt of product), 252d
def f41qc_f41_quality_compounder_geomrf_252d_base_v110_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    prod = _mean(roic, 252) * _mean(fcfm, 252)
    b = np.sign(prod) * prod.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion net of dilution z (improving margin minus issuance), 252d
def f41qc_f41_quality_compounder_marginexpz_252d_base_v111_signal(netmargin, sharesbas):
    exp = _mean(netmargin, 63) - _mean(netmargin, 252)
    dil = _f41_dilution(sharesbas, 63)
    b = _z(exp, 252) - 0.5 * _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounder: FCF/equity z plus equity-growth z minus dilution z (full cash build), 252d
def f41qc_f41_quality_compounder_cashbuild_252d_base_v112_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    eg = _f41_growth(equity, 126)
    dil = _f41_dilution(sharesbas, 63)
    b = _z(cashret, 252) + 0.5 * _z(eg, 252) - 0.5 * _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth volatility (lumpiness penalty), inverted rank, 252d
def f41qc_f41_quality_compounder_revsmooth_252d_base_v113_signal(revenue):
    g = _f41_growth(revenue, 63)
    v = _std(g, 252)
    b = -_rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend gated by margin level (improving returns when profitable), 252d
def f41qc_f41_quality_compounder_roictrendgate_252d_base_v114_signal(roic, netmargin):
    tr = _slope(roic, 252)
    b = tr * np.sign(_mean(netmargin, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-margin 504d composite: margin z gated by positive fraction, 504d
def f41qc_f41_quality_compounder_durmargin2_504d_base_v115_signal(netmargin):
    pf = _f41_pos_frac(netmargin, 504)
    b = _z(netmargin, 504) * pf + (pf - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light return: ROIC z minus equity-growth z (return without book bloat), 252d
def f41qc_f41_quality_compounder_lightreturn_252d_base_v116_signal(roic, equity):
    eg = _f41_growth(equity, 126)
    b = _z(roic, 252) - 0.5 * _z(eg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin minus revenue-growth (cash harvest vs reinvestment), 252d
def f41qc_f41_quality_compounder_harvest_252d_base_v117_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    g = _f41_growth(revenue, 252)
    b = _z(fcfm, 252) - _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-driver positive breadth (continuous): mean of three sigmoids, 252d
def f41qc_f41_quality_compounder_breadth_252d_base_v118_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    sr = np.tanh(15.0 * _mean(roic, 126))
    sn = np.tanh(15.0 * _mean(netmargin, 126))
    sf = np.tanh(15.0 * _mean(fcfm, 126))
    b = (sr + sn + sf) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted ROIC: roic divided by dilution-stress factor (multiplicative penalty), 252d
def f41qc_f41_quality_compounder_roicnetdil_252d_base_v119_signal(roic, sharesbas):
    dil = _f41_dilution(sharesbas, 252)
    b = _mean(roic, 252) / (1.0 + 5.0 * dil.clip(lower=-0.15))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity efficiency: revenue/equity x net-margin z (DuPont-style return z), 252d
def f41qc_f41_quality_compounder_dupont_252d_base_v120_signal(revenue, equity, netmargin):
    turn = _safe_div(revenue, equity)
    b = _z(turn, 252) * np.sign(_mean(netmargin, 252)) + _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin smoothness: inverse coefficient of variation, ranked, 252d
def f41qc_f41_quality_compounder_fcfmsmooth_252d_base_v121_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    cv = _std(fcfm, 252) / _mean(fcfm, 252).abs().replace(0, np.nan)
    b = _rank(1.0 / (1.0 + cv), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality momentum: net-margin z change over a quarter, 252d
def f41qc_f41_quality_compounder_marginzmom_252d_base_v122_signal(netmargin):
    zz = _z(netmargin, 252)
    b = zz - zz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder distance-from-distress: ROIC plus FCF positivity minus dilution (composite score), 252d
def f41qc_f41_quality_compounder_distqual_252d_base_v123_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252) - 0.5
    fp = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    b = rp + fp - 5.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share growth rank (per-share scaling percentile), 252d
def f41qc_f41_quality_compounder_rpsgrowrank_252d_base_v124_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    g = _f41_growth(rps, 126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC dispersion vs net-margin dispersion (which driver steadier), 252d
def f41qc_f41_quality_compounder_dispgap_252d_base_v125_signal(roic, netmargin):
    b = _z(_std(netmargin, 126), 252) - _z(_std(roic, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion trend: FCF-margin-minus-net-margin slope (improving earnings quality), 252d
def f41qc_f41_quality_compounder_convtrend_252d_base_v126_signal(fcf, revenue, netmargin):
    fcfm = _f41_fcf_margin(fcf, revenue)
    spread = fcfm - netmargin
    b = _slope(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable returns: ROIC rank interacted with low-volatility rank (smooth-and-high percentile), 252d
def f41qc_f41_quality_compounder_smoothret_252d_base_v127_signal(roic):
    lvl = _rank(_mean(roic, 63), 504)
    smooth = -_rank(_std(roic, 126), 504)
    b = lvl + smooth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-growth minus dilution z (organic book-build percentile), 252d
def f41qc_f41_quality_compounder_organicz_252d_base_v128_signal(equity, sharesbas):
    eg = _f41_growth(equity, 252)
    sg = _f41_growth(sharesbas, 252)
    b = _rank(eg - sg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF coverage of dilution: FCF-margin relative to share growth (cash funds buybacks), 252d
def f41qc_f41_quality_compounder_fcfcover_252d_base_v129_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 126)
    sg = _f41_growth(sharesbas, 126)
    b = np.tanh(5.0 * (fcfm - sg))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level rank (relative profitability regime), 252d
def f41qc_f41_quality_compounder_marginrank_252d_base_v130_signal(netmargin):
    b = _rank(_mean(netmargin, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality compounder velocity: change in z-blend index over a quarter, 252d
def f41qc_f41_quality_compounder_blendvel_252d_base_v131_signal(roic, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 63)
    idx = _z(roic, 252) + _z(fcfm, 252) - _z(dil, 252)
    b = idx - idx.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-return-on-book level minus its long EMA (cash ROE displacement), 252d
def f41qc_f41_quality_compounder_cashroedisp_252d_base_v132_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    ema = r.ewm(span=252, min_periods=63).mean()
    b = r - ema
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin durability x ROIC sign (profitable-and-positive-return interaction), 252d
def f41qc_f41_quality_compounder_durxsign_252d_base_v133_signal(netmargin, roic):
    dur = _f41_pos_frac(netmargin, 252) - 0.5
    b = dur * np.sign(_mean(roic, 252)) + 0.5 * (_f41_pos_frac(roic, 252) - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale z minus dilution z (scaling without share creep), 252d
def f41qc_f41_quality_compounder_scalenodil_252d_base_v134_signal(revenue, sharesbas):
    logr = np.log(revenue.replace(0, np.nan).abs())
    dil = _f41_dilution(sharesbas, 63)
    b = _z(logr, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF / equity x positive-fraction (durable cash ROE level), 252d
def f41qc_f41_quality_compounder_durcashlevel_252d_base_v135_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    pf = _f41_pos_frac(r, 252)
    b = _mean(r, 252) * pf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-z minimum-driver gated by dilution (weakest-link quality net of issuance), 252d
def f41qc_f41_quality_compounder_weaklink_252d_base_v136_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    stacked = pd.concat([_z(roic, 252), _z(netmargin, 252), _z(fcfm, 252)], axis=1)
    dil = _f41_dilution(sharesbas, 63)
    b = stacked.min(axis=1) - 0.3 * _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-per-share growth gated by ROIC positivity (return-funded per-share book), 252d
def f41qc_f41_quality_compounder_bvpsgate_252d_base_v137_signal(equity, sharesbas, roic):
    bvps = _safe_div(equity, sharesbas)
    g = _f41_growth(bvps, 126)
    pos = _f41_pos_frac(roic, 252) - 0.5
    b = _z(g, 252) * np.sign(pos) + 2.0 * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin acceleration rank (margin-inflection percentile), 252d
def f41qc_f41_quality_compounder_marginaccelrank_252d_base_v138_signal(netmargin):
    acc = _mean(netmargin, 63) - _mean(netmargin, 252)
    b = _rank(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin level minus dilution rate (cash margin net of share creep), 252d
def f41qc_f41_quality_compounder_fcfmnetdil_252d_base_v139_signal(fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    dil = _f41_dilution(sharesbas, 252)
    b = _mean(fcfm, 252) - 0.5 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC and FCF-margin both-above-zero continuous (joint positivity strength), 252d
def f41qc_f41_quality_compounder_jointpos_252d_base_v140_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    rp = _f41_pos_frac(roic, 252)
    fp = _f41_pos_frac(fcfm, 252)
    b = rp * fp - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-growth rank minus dilution rank (book-build vs issuance percentile), 252d
def f41qc_f41_quality_compounder_buildvsdil_252d_base_v141_signal(equity, sharesbas):
    eg = _f41_growth(equity, 126)
    dil = _f41_dilution(sharesbas, 63)
    b = _rank(eg, 504) - _rank(dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth x net-margin standardized product (profitable-growth z), 252d
def f41qc_f41_quality_compounder_profgrowz_252d_base_v142_signal(revenue, netmargin):
    g = _f41_growth(revenue, 126)
    b = _z(g, 252) * np.sign(_mean(netmargin, 252)) + _z(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-return durability: FCF/equity above own median fraction, 252d
def f41qc_f41_quality_compounder_cashabovemed_252d_base_v143_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    med = r.rolling(504, min_periods=252).median()
    above = (r > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-stability x cash-stability (twin smoothness interaction), 252d
def f41qc_f41_quality_compounder_twinsmooth_252d_base_v144_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    ms = -_rank(_std(netmargin, 126), 504)
    cs = -_rank(_std(fcfm, 126), 504)
    b = ms + cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z gated by low-dilution regime (quality in disciplined-issuance regime), 252d
def f41qc_f41_quality_compounder_roiclowdil_252d_base_v145_signal(roic, sharesbas):
    dil = _f41_dilution(sharesbas, 252)
    lowdil = (dil < dil.rolling(504, min_periods=126).median()).astype(float) - 0.5
    b = _z(roic, 252) * (0.5 + lowdil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable compounder full index: blend of z-quality minus dilution, gated by margin positivity, 504d
def f41qc_f41_quality_compounder_fullidx_504d_base_v146_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    core = (_z(roic, 504) + _z(netmargin, 504) + _z(fcfm, 504)) / 3.0
    dil = _f41_dilution(sharesbas, 126)
    mpos = _f41_pos_frac(netmargin, 504)
    b = core * mpos - 0.4 * _z(dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue/equity productivity level rank (capital-light scaling regime), 252d
def f41qc_f41_quality_compounder_prodrank_252d_base_v147_signal(revenue, equity):
    turn = _safe_div(revenue, equity)
    b = _rank(_mean(turn, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin minus accrual-margin volatility-adjusted (robust earnings quality), 252d
def f41qc_f41_quality_compounder_robustqual_252d_base_v148_signal(fcf, revenue, netmargin):
    fcfm = _f41_fcf_margin(fcf, revenue)
    gap = _mean(fcfm, 126) - _mean(netmargin, 126)
    denom = _std(fcfm - netmargin, 252).replace(0, np.nan)
    b = gap / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-funded reinvestment: positive FCF AND positive revenue-growth (self-funded growth), 252d
def f41qc_f41_quality_compounder_selfgrow_252d_base_v149_signal(fcf, revenue):
    fp = _f41_pos_frac(fcf, 252) - 0.5
    g = _f41_growth(revenue, 126)
    b = fp * np.sign(g) + np.tanh(5.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# master compounder score: weighted sum of standardized quality facets minus dilution, 252d
def f41qc_f41_quality_compounder_master_252d_base_v150_signal(roic, netmargin, fcf, revenue, equity, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    cashret = _safe_div(fcf, equity)
    dil = _f41_dilution(sharesbas, 63)
    b = (0.3 * _z(roic, 252) + 0.25 * _z(netmargin, 252)
         + 0.25 * _z(fcfm, 252) + 0.2 * _z(cashret, 252) - 0.4 * _z(dil, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41qc_f41_quality_compounder_zblend_252d_base_v076_signal,
    f41qc_f41_quality_compounder_roicrank_252d_base_v077_signal,
    f41qc_f41_quality_compounder_accrualgap_252d_base_v078_signal,
    f41qc_f41_quality_compounder_retfundbook_252d_base_v079_signal,
    f41qc_f41_quality_compounder_dilovhng_252d_base_v080_signal,
    f41qc_f41_quality_compounder_cashroevol_252d_base_v081_signal,
    f41qc_f41_quality_compounder_turntrend_252d_base_v082_signal,
    f41qc_f41_quality_compounder_marginps_252d_base_v083_signal,
    f41qc_f41_quality_compounder_stabrank_252d_base_v084_signal,
    f41qc_f41_quality_compounder_cashgrowz_252d_base_v085_signal,
    f41qc_f41_quality_compounder_marginhigh_252d_base_v086_signal,
    f41qc_f41_quality_compounder_econprofit_252d_base_v087_signal,
    f41qc_f41_quality_compounder_convratio_252d_base_v088_signal,
    f41qc_f41_quality_compounder_bvpslevel_252d_base_v089_signal,
    f41qc_f41_quality_compounder_drvdisp_252d_base_v090_signal,
    f41qc_f41_quality_compounder_fundgap_252d_base_v091_signal,
    f41qc_f41_quality_compounder_margintrendrank_252d_base_v092_signal,
    f41qc_f41_quality_compounder_dilcashyield_252d_base_v093_signal,
    f41qc_f41_quality_compounder_roiczmom_252d_base_v094_signal,
    f41qc_f41_quality_compounder_sigmoidgate_252d_base_v095_signal,
    f41qc_f41_quality_compounder_marginvolrank_252d_base_v096_signal,
    f41qc_f41_quality_compounder_pscaling_252d_base_v097_signal,
    f41qc_f41_quality_compounder_gatedcash_252d_base_v098_signal,
    f41qc_f41_quality_compounder_roicmarginz_126d_base_v099_signal,
    f41qc_f41_quality_compounder_eqstab_252d_base_v100_signal,
    f41qc_f41_quality_compounder_qmdaccel_252d_base_v101_signal,
    f41qc_f41_quality_compounder_scalemargin_252d_base_v102_signal,
    f41qc_f41_quality_compounder_fcfpsaccel_252d_base_v103_signal,
    f41qc_f41_quality_compounder_profbookz_252d_base_v104_signal,
    f41qc_f41_quality_compounder_roicabovemed_252d_base_v105_signal,
    f41qc_f41_quality_compounder_qualrank_252d_base_v106_signal,
    f41qc_f41_quality_compounder_psdisp_252d_base_v107_signal,
    f41qc_f41_quality_compounder_durqual_504d_base_v108_signal,
    f41qc_f41_quality_compounder_dilstreak_252d_base_v109_signal,
    f41qc_f41_quality_compounder_geomrf_252d_base_v110_signal,
    f41qc_f41_quality_compounder_marginexpz_252d_base_v111_signal,
    f41qc_f41_quality_compounder_cashbuild_252d_base_v112_signal,
    f41qc_f41_quality_compounder_revsmooth_252d_base_v113_signal,
    f41qc_f41_quality_compounder_roictrendgate_252d_base_v114_signal,
    f41qc_f41_quality_compounder_durmargin2_504d_base_v115_signal,
    f41qc_f41_quality_compounder_lightreturn_252d_base_v116_signal,
    f41qc_f41_quality_compounder_harvest_252d_base_v117_signal,
    f41qc_f41_quality_compounder_breadth_252d_base_v118_signal,
    f41qc_f41_quality_compounder_roicnetdil_252d_base_v119_signal,
    f41qc_f41_quality_compounder_dupont_252d_base_v120_signal,
    f41qc_f41_quality_compounder_fcfmsmooth_252d_base_v121_signal,
    f41qc_f41_quality_compounder_marginzmom_252d_base_v122_signal,
    f41qc_f41_quality_compounder_distqual_252d_base_v123_signal,
    f41qc_f41_quality_compounder_rpsgrowrank_252d_base_v124_signal,
    f41qc_f41_quality_compounder_dispgap_252d_base_v125_signal,
    f41qc_f41_quality_compounder_convtrend_252d_base_v126_signal,
    f41qc_f41_quality_compounder_smoothret_252d_base_v127_signal,
    f41qc_f41_quality_compounder_organicz_252d_base_v128_signal,
    f41qc_f41_quality_compounder_fcfcover_252d_base_v129_signal,
    f41qc_f41_quality_compounder_marginrank_252d_base_v130_signal,
    f41qc_f41_quality_compounder_blendvel_252d_base_v131_signal,
    f41qc_f41_quality_compounder_cashroedisp_252d_base_v132_signal,
    f41qc_f41_quality_compounder_durxsign_252d_base_v133_signal,
    f41qc_f41_quality_compounder_scalenodil_252d_base_v134_signal,
    f41qc_f41_quality_compounder_durcashlevel_252d_base_v135_signal,
    f41qc_f41_quality_compounder_weaklink_252d_base_v136_signal,
    f41qc_f41_quality_compounder_bvpsgate_252d_base_v137_signal,
    f41qc_f41_quality_compounder_marginaccelrank_252d_base_v138_signal,
    f41qc_f41_quality_compounder_fcfmnetdil_252d_base_v139_signal,
    f41qc_f41_quality_compounder_jointpos_252d_base_v140_signal,
    f41qc_f41_quality_compounder_buildvsdil_252d_base_v141_signal,
    f41qc_f41_quality_compounder_profgrowz_252d_base_v142_signal,
    f41qc_f41_quality_compounder_cashabovemed_252d_base_v143_signal,
    f41qc_f41_quality_compounder_twinsmooth_252d_base_v144_signal,
    f41qc_f41_quality_compounder_roiclowdil_252d_base_v145_signal,
    f41qc_f41_quality_compounder_fullidx_504d_base_v146_signal,
    f41qc_f41_quality_compounder_prodrank_252d_base_v147_signal,
    f41qc_f41_quality_compounder_robustqual_252d_base_v148_signal,
    f41qc_f41_quality_compounder_selfgrow_252d_base_v149_signal,
    f41qc_f41_quality_compounder_master_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_QUALITY_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False, noise=0.0,
              cycle=0.0, cyc_period=378):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if cycle > 0:
            phase = g.uniform(0, 2 * np.pi)
            s = s + base * cycle * np.sin(2 * np.pi * np.arange(n) / cyc_period + phase)
        if noise > 0:
            s = s * (1.0 + g.normal(0.0, noise, n))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    roic = _fund(101, base=0.18, drift=0.0, vol=0.14, allow_neg=True, noise=0.04,
                 cycle=0.9, cyc_period=340).rename("roic")
    fcf = _fund(102, base=1.2e8, drift=0.0, vol=0.16, allow_neg=True, noise=0.05,
                cycle=0.9, cyc_period=470).rename("fcf")
    netmargin = _fund(103, base=0.22, drift=0.0, vol=0.14, allow_neg=True, noise=0.04,
                      cycle=0.9, cyc_period=410).rename("netmargin")
    sharesbas = _fund(104, base=8e7, drift=0.0, vol=0.05, noise=0.015).rename("sharesbas")
    revenue = _fund(105, base=6e8, drift=0.03, vol=0.06, noise=0.02).rename("revenue")
    equity = _fund(106, base=9e8, drift=0.025, vol=0.05, noise=0.02).rename("equity")

    cols = {"roic": roic, "fcf": fcf, "netmargin": netmargin,
            "sharesbas": sharesbas, "revenue": revenue, "equity": equity}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
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

    print("OK f41_quality_compounder_base_076_150_claude: %d features pass" % n_features)
