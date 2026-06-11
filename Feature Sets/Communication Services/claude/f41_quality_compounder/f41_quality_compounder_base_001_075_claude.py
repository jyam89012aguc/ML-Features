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


def _slope(s, w):
    # normalized rolling slope per step via covariance with a centered ramp
    xm = (w - 1) / 2.0
    xden = float(((np.arange(w) - xm) ** 2).sum())

    def _f(a):
        am = a.mean()
        return float(((np.arange(len(a)) - xm) * (a - am)).sum() / xden)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (quality compounder) =====
def _f41_growth(s, w):
    # log growth over window w (drift of a fundamental level)
    return np.log(s.replace(0, np.nan).abs() / s.shift(w).replace(0, np.nan).abs())


def _f41_dilution(sharesbas, w):
    # share-count growth = dilution (positive when issuing)
    return sharesbas / sharesbas.shift(w).replace(0, np.nan) - 1.0


def _f41_pos_frac(s, w):
    # fraction of window with positive value (stability of positive sign)
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _f41_stab(s, w):
    # level divided by its own dispersion = stability-weighted level
    return _mean(s, w) / _std(s, w).replace(0, np.nan)


def _f41_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


# ============================================================
# stable-positive-ROIC x positive-FCF composite (core compounder gate), 252d
def f41qc_f41_quality_compounder_roicfcf_252d_base_v001_signal(roic, fcf, revenue):
    roic_pos = _f41_pos_frac(roic, 252)
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 252)
    b = roic_pos * fcf_pos * _mean(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality (ROIC) minus dilution (share growth), 252d
def f41qc_f41_quality_compounder_qmd_252d_base_v002_signal(roic, sharesbas):
    q = _mean(roic, 252)
    dil = _f41_dilution(sharesbas, 252)
    b = q - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounding score: stability-weighted ROIC minus dilution z (consistency net of issuance), 252d
def f41qc_f41_quality_compounder_compound_252d_base_v003_signal(roic, sharesbas):
    stab = _f41_stab(roic, 252)
    dil = _f41_dilution(sharesbas, 63)
    b = np.tanh(stab) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-margin composite: net-margin level x net-margin stability, 252d
def f41qc_f41_quality_compounder_durmargin_252d_base_v004_signal(netmargin):
    lvl = _mean(netmargin, 252)
    stab = _f41_stab(netmargin, 252)
    b = lvl + 0.1 * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin x revenue-growth (cash-generative growth), 252d
def f41qc_f41_quality_compounder_fcfgrow_252d_base_v005_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    g = _f41_growth(revenue, 252)
    b = _mean(fcfm, 252) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC x net-margin (return-and-margin quality), 126d
def f41qc_f41_quality_compounder_roicmargin_126d_base_v006_signal(roic, netmargin):
    b = _mean(roic, 126) * _mean(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-FCF persistence weighted by FCF margin level, 252d
def f41qc_f41_quality_compounder_fcfpersist_252d_base_v007_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    persist = _f41_pos_frac(fcfm, 252)
    b = persist * _mean(fcfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anti-dilution compounding: per-share revenue-growth acceleration (short vs long), 252d
def f41qc_f41_quality_compounder_persharegrow_252d_base_v008_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    b = _f41_growth(rps, 63) - _f41_growth(rps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash return on book: FCF / equity (cash return on book), 252d
def f41qc_f41_quality_compounder_fcfroe_252d_base_v009_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    b = _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple gate: stable ROIC AND positive FCF AND low dilution (continuous product), 252d
def f41qc_f41_quality_compounder_triplegate_252d_base_v010_signal(roic, fcf, sharesbas, revenue):
    roic_pos = _f41_pos_frac(roic, 252)
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 252)
    dil = _f41_dilution(sharesbas, 252)
    lowdil = 1.0 / (1.0 + dil.clip(lower=0) * 10.0)
    b = roic_pos * fcf_pos * lowdil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability-weighted level (consistency of returns), 504d
def f41qc_f41_quality_compounder_roicstab_504d_base_v011_signal(roic):
    b = _f41_stab(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin x FCF-margin (twin profitability), 252d
def f41qc_f41_quality_compounder_twinprofit_252d_base_v012_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _mean(netmargin, 252) * _mean(fcfm, 252) * np.sign(_mean(netmargin, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity compounding rate: log-growth of equity (retained value build), 252d
def f41qc_f41_quality_compounder_equitygrow_252d_base_v013_signal(equity):
    b = _f41_growth(equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-funded growth: equity growth minus dilution (organic book build), 252d
def f41qc_f41_quality_compounder_organicbook_252d_base_v014_signal(equity, sharesbas):
    eg = _f41_growth(equity, 252)
    sg = _f41_growth(sharesbas, 252)
    b = eg - sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC above hurdle (~0.08): persistence-fraction centered, gated by hurdle-excess sign, 252d
def f41qc_f41_quality_compounder_hurdle_252d_base_v015_signal(roic):
    excess = roic - 0.08
    persist = (excess > 0).astype(float).rolling(252, min_periods=126).mean() - 0.5
    b = persist + 0.5 * np.tanh(10.0 * _mean(excess, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share level z-scored vs its own 252d history (scale-per-share extremity)
def f41qc_f41_quality_compounder_revpershare_252d_base_v016_signal(revenue, sharesbas):
    rps = _safe_div(revenue, sharesbas)
    b = _z(rps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF per share level z-scored vs own history (cash-per-share extremity), 252d
def f41qc_f41_quality_compounder_fcfpershare_252d_base_v017_signal(fcf, sharesbas):
    fps = _safe_div(fcf, sharesbas)
    b = _z(fps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable composite: net-margin z plus FCF positive-fraction minus dilution z (standardized blend), 252d
def f41qc_f41_quality_compounder_durable_252d_base_v018_signal(netmargin, sharesbas, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 252) - 0.5
    dil = _f41_dilution(sharesbas, 63)
    b = _z(netmargin, 252) + 2.0 * fcf_pos - 0.5 * _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend (improving returns), 252d slope of roic
def f41qc_f41_quality_compounder_roictrend_252d_base_v019_signal(roic):
    b = _slope(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend x level (improving and high margin), 252d
def f41qc_f41_quality_compounder_margintrend_252d_base_v020_signal(netmargin):
    tr = _slope(netmargin, 252)
    lvl = _mean(netmargin, 252)
    b = tr * np.sign(lvl) + 0.01 * np.sign(tr) * lvl.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion: FCF margin relative to net margin (earnings quality), 252d
def f41qc_f41_quality_compounder_cashconv_252d_base_v021_signal(fcf, revenue, netmargin):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _mean(fcfm, 252) - _mean(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounding quality: ROIC x equity growth (return-driven book build), 252d
def f41qc_f41_quality_compounder_roicequity_252d_base_v022_signal(roic, equity):
    eg = _f41_growth(equity, 252)
    b = _mean(roic, 252) * eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean quality: positive-ROIC fraction z minus dilution z (standardized gate net of issuance)
def f41qc_f41_quality_compounder_cleanquality_252d_base_v023_signal(roic, sharesbas):
    roic_pos = _f41_pos_frac(roic, 252)
    dil = _f41_dilution(sharesbas, 252)
    b = _z(roic_pos, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF stability x positive fraction (durable cash generation), 252d
def f41qc_f41_quality_compounder_fcfdurable_252d_base_v024_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    stab = _f41_stab(fcfm, 252)
    persist = _f41_pos_frac(fcfm, 252)
    b = stab * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin minus dilution (margin quality net of share creep), 252d
def f41qc_f41_quality_compounder_marginmdil_252d_base_v025_signal(netmargin, sharesbas):
    dil = _f41_dilution(sharesbas, 252)
    b = _mean(netmargin, 252) - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compound score 126d: stable ROIC x low dilution
def f41qc_f41_quality_compounder_compound_126d_base_v026_signal(roic, sharesbas):
    stab = _f41_stab(roic, 126)
    dil = _f41_dilution(sharesbas, 126).clip(lower=0)
    b = stab * (1.0 - dil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth x net margin (profitable growth quality), 126d
def f41qc_f41_quality_compounder_profgrowth_126d_base_v027_signal(revenue, netmargin):
    g = _f41_growth(revenue, 126)
    b = g * _mean(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable cash ROE: FCF/equity level z gated by positive-fraction excess (durable cash return)
def f41qc_f41_quality_compounder_durcashroe_252d_base_v028_signal(fcf, equity):
    r = _safe_div(fcf, equity)
    persist = _f41_pos_frac(r, 252) - 0.5
    b = _z(r, 126) + 3.0 * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted ROIC change: quarter-over-quarter shift in roic/(1+share growth)
def f41qc_f41_quality_compounder_diladjroic_252d_base_v029_signal(roic, sharesbas):
    sg = _f41_growth(sharesbas, 252)
    adj = _mean(roic, 63) / (1.0 + sg.clip(lower=-0.9))
    b = adj - adj.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-quality z-composite: z(roic)+z(netmargin)+z(fcfmargin), 252d
def f41qc_f41_quality_compounder_zcomposite_252d_base_v030_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _z(roic, 252) + _z(netmargin, 252) + _z(fcfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin breadth: how many of the last 252d had net-margin above its 504d median
def f41qc_f41_quality_compounder_marginbreadth_252d_base_v031_signal(netmargin):
    med = netmargin.rolling(504, min_periods=252).median()
    above = (netmargin > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-and-cash twin: z-score agreement of ROIC and FCF-margin (co-movement)
def f41qc_f41_quality_compounder_roicfcfm_252d_base_v032_signal(roic, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _z(roic, 126) * _z(fcfm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin expansion net of dilution drag, 252d
def f41qc_f41_quality_compounder_marginexp_252d_base_v033_signal(netmargin, sharesbas):
    exp = _mean(netmargin, 63) - _mean(netmargin, 252)
    dil = _f41_dilution(sharesbas, 252).clip(lower=0)
    b = exp - 0.1 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded compounding: FCF-margin level relative to dilution, ratio form (cash covers issuance)
def f41qc_f41_quality_compounder_selffund_252d_base_v034_signal(fcf, revenue, sharesbas):
    fcfm = _mean(_f41_fcf_margin(fcf, revenue), 252)
    dil = _f41_dilution(sharesbas, 252)
    b = fcfm / (0.05 + dil.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable quality: positive-ROIC fraction blended with stability-weighted level (continuous), 252d
def f41qc_f41_quality_compounder_qstreak_252d_base_v035_signal(roic):
    posfrac = _f41_pos_frac(roic, 252)
    stab = _f41_stab(roic, 126)
    b = posfrac * np.tanh(stab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value-per-share acceleration: short-window growth minus long-window growth
def f41qc_f41_quality_compounder_bvpsgrow_252d_base_v036_signal(equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    b = _f41_growth(bvps, 63) - _f41_growth(bvps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC smoothness: inverse coefficient-of-variation (level relative to dispersion), ranked
def f41qc_f41_quality_compounder_smoothroic_252d_base_v037_signal(roic):
    cv = _std(roic, 252) / _mean(roic, 252).abs().replace(0, np.nan)
    inv = 1.0 / (1.0 + cv)
    b = inv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable cashy growth: revenue-growth z-score gated by FCF positive-fraction excess
def f41qc_f41_quality_compounder_durgrowth_252d_base_v038_signal(revenue, fcf):
    g = _f41_growth(revenue, 126)
    fcf_pos = _f41_pos_frac(fcf, 252) - 0.5
    b = _z(g, 252) * np.sign(fcf_pos) + 2.0 * fcf_pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light quality: ROIC weighted by equity-turnover z-score (decapitalized return)
def f41qc_f41_quality_compounder_capitallight_252d_base_v039_signal(roic, revenue, equity):
    turn = _safe_div(revenue, equity)
    b = _mean(roic, 252) * _z(turn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin x equity growth (profitable book build), 252d
def f41qc_f41_quality_compounder_profbook_252d_base_v040_signal(netmargin, equity):
    eg = _f41_growth(equity, 252)
    b = _mean(netmargin, 252) * eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality momentum: ROIC now vs a year ago, weighted by FCF positivity, 252d
def f41qc_f41_quality_compounder_qmom_252d_base_v041_signal(roic, fcf, revenue):
    dq = _mean(roic, 63) - _mean(roic, 63).shift(252)
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 252)
    b = dq * fcf_pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count discipline: dilution z-score interacted with margin z (issuance-vs-quality)
def f41qc_f41_quality_compounder_buybackq_252d_base_v042_signal(sharesbas, netmargin):
    dil = _f41_dilution(sharesbas, 63)
    b = (-_z(dil, 252)) * (1.0 + _z(netmargin, 252).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-margin composite 504d: level x positivity plus stability
def f41qc_f41_quality_compounder_durmargin_504d_base_v043_signal(netmargin):
    lvl = _mean(netmargin, 504)
    stab = _f41_stab(netmargin, 504)
    pos = _f41_pos_frac(netmargin, 504)
    b = lvl * pos + 0.05 * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return gap: FCF/equity cash return vs ROIC accounting return, 252d
def f41qc_f41_quality_compounder_returngap_252d_base_v044_signal(fcf, equity, roic):
    cashret = _safe_div(fcf, equity)
    b = _mean(cashret, 252) - _mean(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder rank: percentile of ROIC-minus-dilution vs own history, 252d
def f41qc_f41_quality_compounder_qmdrank_252d_base_v045_signal(roic, sharesbas):
    q = _mean(roic, 252) - _f41_dilution(sharesbas, 252)
    b = q.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# big-and-profitable: revenue-scale growth interacted with margin z (scaling profitably)
def f41qc_f41_quality_compounder_scaleprofit_252d_base_v046_signal(revenue, netmargin):
    scale_g = _f41_growth(revenue, 252)
    b = scale_g * _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin consistency ranked (consistent cash producer), 252d
def f41qc_f41_quality_compounder_fcfmconsist_252d_base_v047_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    consist = -_std(fcfm, 252)
    b = consist.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-driver geometric quality: signed cube-root of roic*netmargin*fcfm, 252d
def f41qc_f41_quality_compounder_geomquality_252d_base_v048_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    prod = _mean(roic, 252) * _mean(netmargin, 252) * _mean(fcfm, 252)
    b = np.sign(prod) * prod.abs() ** (1.0 / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anti-dilution per-share FCF: FCF-per-share level z interacted with margin sign, 252d
def f41qc_f41_quality_compounder_fcfpsq_252d_base_v049_signal(fcf, sharesbas, netmargin):
    fps = _safe_div(fcf, sharesbas)
    b = _z(fps, 252) * np.sign(_mean(netmargin, 252)) + 0.5 * _z(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity efficiency: ROIC x equity-per-share growth, 252d
def f41qc_f41_quality_compounder_equityeff_252d_base_v050_signal(roic, equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    g = _f41_growth(bvps, 252)
    b = _mean(roic, 252) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stable profitable franchise: margin z penalized by revenue-growth volatility z (smoothness premium)
def f41qc_f41_quality_compounder_franchise_252d_base_v051_signal(netmargin, revenue):
    rev_vol = _std(_f41_growth(revenue, 63), 252)
    b = _z(netmargin, 252) - _z(rev_vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality gate count: avg of {ROIC>0, FCF>0, margin>0} over the year, 252d
def f41qc_f41_quality_compounder_gatecount_252d_base_v052_signal(roic, fcf, netmargin):
    g = (roic > 0).astype(float) + (fcf > 0).astype(float) + (netmargin > 0).astype(float)
    b = g.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounding consistency: positive equity-growth fraction x ROIC, 504d
def f41qc_f41_quality_compounder_compconsist_504d_base_v053_signal(equity, roic):
    eg = _f41_growth(equity, 63)
    pos = _f41_pos_frac(eg, 504)
    b = pos * _mean(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin acceleration: short-window mean minus long-window mean (cash-margin inflection), 252d
def f41qc_f41_quality_compounder_fcfmtrend_252d_base_v054_signal(fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    b = _mean(fcfm, 63) - _mean(fcfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable returns minus dilution drag (quality compounder core), 504d
def f41qc_f41_quality_compounder_qmd_504d_base_v055_signal(roic, sharesbas):
    q = _mean(roic, 504)
    dil = _f41_dilution(sharesbas, 504)
    b = q - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share profit power: revenue-per-share growth z interacted with margin sign, 252d
def f41qc_f41_quality_compounder_psprofit_252d_base_v056_signal(revenue, sharesbas, netmargin):
    rps = _safe_div(revenue, sharesbas)
    b = _z(_f41_growth(rps, 126), 252) * np.sign(_mean(netmargin, 252)) + _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z minus dilution z (standardized quality net of dilution), 252d
def f41qc_f41_quality_compounder_zqmd_252d_base_v057_signal(roic, sharesbas):
    dil = _f41_dilution(sharesbas, 63)
    b = _z(roic, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-on-book compounding: FCF/equity z interacted with equity-growth z (cash plus book build), 252d
def f41qc_f41_quality_compounder_cashcompound_252d_base_v058_signal(fcf, equity):
    cashret = _safe_div(fcf, equity)
    eg = _f41_growth(equity, 126)
    b = _z(cashret, 252) * (1.0 + _z(eg, 252).clip(-2, 2)) + _z(eg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# twin durability: dispersion-gap between ROIC and netmargin volatility (which is steadier), ranked
def f41qc_f41_quality_compounder_twindurable_252d_base_v059_signal(netmargin, roic):
    gap = _std(roic, 126) - _std(netmargin, 126)
    b = gap.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-funded buyback: FCF margin positive AND shares shrinking, 252d
def f41qc_f41_quality_compounder_qbuyback_252d_base_v060_signal(fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 252)
    shrink = (-_f41_growth(sharesbas, 252)).clip(lower=0)
    b = fcf_pos * shrink
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable compounder index: avg of z(roic), z(netmargin), z(fcf/equity), minus z(dilution), 252d
def f41qc_f41_quality_compounder_durindex_252d_base_v061_signal(roic, netmargin, fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    dil = _f41_dilution(sharesbas, 63)
    b = (_z(roic, 252) + _z(netmargin, 252) + _z(cashret, 252)) / 3.0 - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-of-growth: margin-change dominated composite (z of margin trend minus dilution drag)
def f41qc_f41_quality_compounder_growthquality_252d_base_v062_signal(revenue, netmargin):
    margin_chg = _mean(netmargin, 63) - _mean(netmargin, 252)
    rev_z = _z(_f41_growth(revenue, 252), 252)
    b = _z(margin_chg, 252) + 0.3 * rev_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC consistency rank: -std(roic) percentile (smoothness rank), 504d
def f41qc_f41_quality_compounder_roicconsist_504d_base_v063_signal(roic):
    sm = -_std(roic, 252)
    b = sm.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital allocation quality: per-share book build interacted with ROIC magnitude, ranked
def f41qc_f41_quality_compounder_capalloc_252d_base_v064_signal(equity, sharesbas, roic):
    eg = _f41_growth(equity, 252)
    sg = _f41_growth(sharesbas, 252)
    raw = (eg - sg) * (_mean(roic, 252) + 0.2)
    b = raw.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# free-cash-flow yield on equity, trend (improving cash return on book), 252d
def f41qc_f41_quality_compounder_cashroetrend_252d_base_v065_signal(fcf, equity):
    cashret = _safe_div(fcf, equity)
    b = _slope(cashret, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compounder breadth: continuous min-of-three z-scores (weakest-driver quality), 252d
def f41qc_f41_quality_compounder_allpos_252d_base_v066_signal(roic, netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    stacked = pd.concat([_z(roic, 252), _z(netmargin, 252), _z(fcfm, 252)], axis=1)
    b = stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-adjusted quality: margin-trend slope minus dilution-trend (improving margin net of issuance)
def f41qc_f41_quality_compounder_scalequality_252d_base_v067_signal(netmargin, revenue, sharesbas):
    mtr = _slope(netmargin, 252)
    dil = _f41_dilution(sharesbas, 63)
    rev_z = _z(_f41_growth(revenue, 252), 252)
    b = _z(mtr, 252) - _z(dil, 252) + 0.2 * rev_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC above its own 504d median, persistence (regime durability), 252d
def f41qc_f41_quality_compounder_roicregime_252d_base_v068_signal(roic):
    med = roic.rolling(504, min_periods=252).median()
    above = (roic > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash compounder net of issuance: FCF/equity z minus dilution z (standardized), 252d
def f41qc_f41_quality_compounder_cashqmd_252d_base_v069_signal(fcf, equity, sharesbas):
    cashret = _safe_div(fcf, equity)
    dil = _f41_dilution(sharesbas, 63)
    b = _z(cashret, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin x per-share revenue growth (per-share profitable growth), 252d
def f41qc_f41_quality_compounder_psprofgrowth_252d_base_v070_signal(netmargin, revenue, sharesbas):
    g = _f41_growth(revenue, 252)
    sg = _f41_growth(sharesbas, 252)
    b = _mean(netmargin, 252) * (g - sg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality compounder velocity: change in (ROIC-minus-dilution) over a quarter, 252d
def f41qc_f41_quality_compounder_qmdvel_252d_base_v071_signal(roic, sharesbas):
    q = _mean(roic, 126) - _f41_dilution(sharesbas, 126)
    b = q - q.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-z geometric durability minus dilution, 252d
def f41qc_f41_quality_compounder_tripz_252d_base_v072_signal(roic, netmargin, fcf, revenue, sharesbas):
    fcfm = _f41_fcf_margin(fcf, revenue)
    core = (_z(roic, 252) + _z(netmargin, 252) + _z(fcfm, 252)) / 3.0
    dil = _z(_f41_dilution(sharesbas, 63), 252)
    b = core - 0.5 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-equity build: ROIC level interacted with book-per-share growth z-score
def f41qc_f41_quality_compounder_roebuild_252d_base_v073_signal(roic, equity, sharesbas):
    bvps = _safe_div(equity, sharesbas)
    g = _f41_growth(bvps, 63)
    b = np.sign(_mean(roic, 252)) * _z(g, 252) + _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-and-cash spread dispersion: rolling std of (netmargin - fcfm) (decoupling risk), 252d
def f41qc_f41_quality_compounder_agreement_252d_base_v074_signal(netmargin, fcf, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    spread = netmargin - fcfm
    b = -_z(_std(spread, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full compounder composite: averaged z of roic/netmargin/fcf-margin minus dilution, gated by FCF positivity, 504d
def f41qc_f41_quality_compounder_fullcomp_504d_base_v075_signal(roic, fcf, sharesbas, netmargin, revenue):
    fcfm = _f41_fcf_margin(fcf, revenue)
    fcf_pos = _f41_pos_frac(fcfm, 504)
    dil = _f41_dilution(sharesbas, 126)
    core = (_z(roic, 504) + _z(netmargin, 504) + _z(fcfm, 504)) / 3.0
    b = core * fcf_pos - 0.5 * _z(dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41qc_f41_quality_compounder_roicfcf_252d_base_v001_signal,
    f41qc_f41_quality_compounder_qmd_252d_base_v002_signal,
    f41qc_f41_quality_compounder_compound_252d_base_v003_signal,
    f41qc_f41_quality_compounder_durmargin_252d_base_v004_signal,
    f41qc_f41_quality_compounder_fcfgrow_252d_base_v005_signal,
    f41qc_f41_quality_compounder_roicmargin_126d_base_v006_signal,
    f41qc_f41_quality_compounder_fcfpersist_252d_base_v007_signal,
    f41qc_f41_quality_compounder_persharegrow_252d_base_v008_signal,
    f41qc_f41_quality_compounder_fcfroe_252d_base_v009_signal,
    f41qc_f41_quality_compounder_triplegate_252d_base_v010_signal,
    f41qc_f41_quality_compounder_roicstab_504d_base_v011_signal,
    f41qc_f41_quality_compounder_twinprofit_252d_base_v012_signal,
    f41qc_f41_quality_compounder_equitygrow_252d_base_v013_signal,
    f41qc_f41_quality_compounder_organicbook_252d_base_v014_signal,
    f41qc_f41_quality_compounder_hurdle_252d_base_v015_signal,
    f41qc_f41_quality_compounder_revpershare_252d_base_v016_signal,
    f41qc_f41_quality_compounder_fcfpershare_252d_base_v017_signal,
    f41qc_f41_quality_compounder_durable_252d_base_v018_signal,
    f41qc_f41_quality_compounder_roictrend_252d_base_v019_signal,
    f41qc_f41_quality_compounder_margintrend_252d_base_v020_signal,
    f41qc_f41_quality_compounder_cashconv_252d_base_v021_signal,
    f41qc_f41_quality_compounder_roicequity_252d_base_v022_signal,
    f41qc_f41_quality_compounder_cleanquality_252d_base_v023_signal,
    f41qc_f41_quality_compounder_fcfdurable_252d_base_v024_signal,
    f41qc_f41_quality_compounder_marginmdil_252d_base_v025_signal,
    f41qc_f41_quality_compounder_compound_126d_base_v026_signal,
    f41qc_f41_quality_compounder_profgrowth_126d_base_v027_signal,
    f41qc_f41_quality_compounder_durcashroe_252d_base_v028_signal,
    f41qc_f41_quality_compounder_diladjroic_252d_base_v029_signal,
    f41qc_f41_quality_compounder_zcomposite_252d_base_v030_signal,
    f41qc_f41_quality_compounder_marginbreadth_252d_base_v031_signal,
    f41qc_f41_quality_compounder_roicfcfm_252d_base_v032_signal,
    f41qc_f41_quality_compounder_marginexp_252d_base_v033_signal,
    f41qc_f41_quality_compounder_selffund_252d_base_v034_signal,
    f41qc_f41_quality_compounder_qstreak_252d_base_v035_signal,
    f41qc_f41_quality_compounder_bvpsgrow_252d_base_v036_signal,
    f41qc_f41_quality_compounder_smoothroic_252d_base_v037_signal,
    f41qc_f41_quality_compounder_durgrowth_252d_base_v038_signal,
    f41qc_f41_quality_compounder_capitallight_252d_base_v039_signal,
    f41qc_f41_quality_compounder_profbook_252d_base_v040_signal,
    f41qc_f41_quality_compounder_qmom_252d_base_v041_signal,
    f41qc_f41_quality_compounder_buybackq_252d_base_v042_signal,
    f41qc_f41_quality_compounder_durmargin_504d_base_v043_signal,
    f41qc_f41_quality_compounder_returngap_252d_base_v044_signal,
    f41qc_f41_quality_compounder_qmdrank_252d_base_v045_signal,
    f41qc_f41_quality_compounder_scaleprofit_252d_base_v046_signal,
    f41qc_f41_quality_compounder_fcfmconsist_252d_base_v047_signal,
    f41qc_f41_quality_compounder_geomquality_252d_base_v048_signal,
    f41qc_f41_quality_compounder_fcfpsq_252d_base_v049_signal,
    f41qc_f41_quality_compounder_equityeff_252d_base_v050_signal,
    f41qc_f41_quality_compounder_franchise_252d_base_v051_signal,
    f41qc_f41_quality_compounder_gatecount_252d_base_v052_signal,
    f41qc_f41_quality_compounder_compconsist_504d_base_v053_signal,
    f41qc_f41_quality_compounder_fcfmtrend_252d_base_v054_signal,
    f41qc_f41_quality_compounder_qmd_504d_base_v055_signal,
    f41qc_f41_quality_compounder_psprofit_252d_base_v056_signal,
    f41qc_f41_quality_compounder_zqmd_252d_base_v057_signal,
    f41qc_f41_quality_compounder_cashcompound_252d_base_v058_signal,
    f41qc_f41_quality_compounder_twindurable_252d_base_v059_signal,
    f41qc_f41_quality_compounder_qbuyback_252d_base_v060_signal,
    f41qc_f41_quality_compounder_durindex_252d_base_v061_signal,
    f41qc_f41_quality_compounder_growthquality_252d_base_v062_signal,
    f41qc_f41_quality_compounder_roicconsist_504d_base_v063_signal,
    f41qc_f41_quality_compounder_capalloc_252d_base_v064_signal,
    f41qc_f41_quality_compounder_cashroetrend_252d_base_v065_signal,
    f41qc_f41_quality_compounder_allpos_252d_base_v066_signal,
    f41qc_f41_quality_compounder_scalequality_252d_base_v067_signal,
    f41qc_f41_quality_compounder_roicregime_252d_base_v068_signal,
    f41qc_f41_quality_compounder_cashqmd_252d_base_v069_signal,
    f41qc_f41_quality_compounder_psprofgrowth_252d_base_v070_signal,
    f41qc_f41_quality_compounder_qmdvel_252d_base_v071_signal,
    f41qc_f41_quality_compounder_tripz_252d_base_v072_signal,
    f41qc_f41_quality_compounder_roebuild_252d_base_v073_signal,
    f41qc_f41_quality_compounder_agreement_252d_base_v074_signal,
    f41qc_f41_quality_compounder_fullcomp_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_QUALITY_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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

    # comm-services often have negative netinc/fcf/roic -> allow_neg; cyclical so sign oscillates
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

    print("OK f41_quality_compounder_base_001_075_claude: %d features pass" % n_features)
