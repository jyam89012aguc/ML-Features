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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return s.diff(w) / float(w)


# ===== f37 producer-quality-compounder domain primitives =====
def _dilution(sharesbas, w):
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _antidilution(sharesbas, w):
    return -np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _fcf_per_share(fcf, sharesbas):
    return fcf / sharesbas.replace(0, np.nan)


def _bvps(equity, sharesbas):
    return equity / sharesbas.replace(0, np.nan)


def _pos_frac(s, w):
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _equity_growth(equity, w):
    return np.log(equity.replace(0, np.nan) / equity.shift(w).replace(0, np.nan))


def _rev_growth(revenue, w):
    return np.log(revenue.replace(0, np.nan) / revenue.shift(w).replace(0, np.nan))


def _roic_stability(roic, w):
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _quality(roic, fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    return np.tanh(3.0 * roic) + np.tanh(3.0 * fm)


# ============================================================
# v076 ROE proxy x antidilution: net-margin*rev/equity gated by share discipline
def f37pq_f37_producer_quality_compounder_roeanti_252d_base_v076_signal(netmargin, revenue, equity, sharesbas):
    roe = netmargin * revenue / equity.replace(0, np.nan)
    anti = _antidilution(sharesbas, 252)
    b = np.tanh(2.0 * _mean(roe, 126)) + 3.0 * anti
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v077 quality drawdown: current blended quality vs its 504d peak (quality DD)
def f37pq_f37_producer_quality_compounder_qdd_504d_base_v077_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    peak = _rmax(q, 504)
    b = (q - peak) / (peak.abs() + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v078 FCF-margin z minus net-margin z (cash vs accounting quality gap)
def f37pq_f37_producer_quality_compounder_cashacc_252d_base_v078_signal(fcf, revenue, netmargin):
    fm = _fcf_margin(fcf, revenue)
    b = _z(fm, 252) - _z(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v079 compounding-rate of book value per share vs revenue per share (relative compounding)
def f37pq_f37_producer_quality_compounder_relcomp_252d_base_v079_signal(equity, sharesbas, revenue):
    bv = _bvps(equity, sharesbas)
    rps = revenue / sharesbas.replace(0, np.nan)
    bg = bv.pct_change(252)
    rg = rps.pct_change(252)
    b = bg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v080 ROIC half-year vs two-year (returns improving over the cycle)
def f37pq_f37_producer_quality_compounder_roicterm_base_v080_signal(roic, fcf):
    short = _mean(roic, 126)
    long = _mean(roic, 504)
    b = (short - long) * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v081 dilution dispersion penalty on FCF quality (erratic issuance = low quality)
def f37pq_f37_producer_quality_compounder_dildisp_252d_base_v081_signal(sharesbas, fcf, revenue):
    dgrowth = np.log(sharesbas.replace(0, np.nan)).diff(21)
    disp = _std(dgrowth, 252)
    fm = _fcf_margin(fcf, revenue)
    b = np.tanh(3.0 * fm) - np.tanh(50.0 * disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v082 quality momentum rank: 1y change in blended quality, ranked
def f37pq_f37_producer_quality_compounder_qmomrank_252d_base_v082_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    mom = q - q.shift(252)
    b = _rank(mom, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v083 cash-cushion x return: FCF/revenue level x ROIC level (deep quality)
def f37pq_f37_producer_quality_compounder_deepqual_252d_base_v083_signal(fcf, revenue, roic):
    fm = _mean(_fcf_margin(fcf, revenue), 63)
    b = np.sign(fm) * np.sign(roic) * (fm.abs() * roic.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v084 net-margin trough-distance scaled by ROIC positivity (recovering profitability)
def f37pq_f37_producer_quality_compounder_nmtrough_504d_base_v084_signal(netmargin, roic):
    trough = _rmin(netmargin, 504)
    dist = netmargin - trough
    b = dist * _pos_frac(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v085 owner-yield momentum: FCF-per-share-over-book yield, change over a year
def f37pq_f37_producer_quality_compounder_owneryield_252d_base_v085_signal(fcf, sharesbas, equity):
    fps = _fcf_per_share(fcf, sharesbas)
    bv = _bvps(equity, sharesbas)
    yld = fps / bv.replace(0, np.nan)
    b = np.tanh(3.0 * (yld - yld.shift(252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v086 revenue-per-share acceleration gated by margin (accelerating quality top-line)
def f37pq_f37_producer_quality_compounder_revpsaccel_252d_base_v086_signal(revenue, sharesbas, netmargin):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = rps.pct_change(126)
    accel = g - g.shift(126)
    b = accel * np.tanh(4.0 * _mean(netmargin, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v087 stable-compounder index: low quality-volatility x high quality-level
def f37pq_f37_producer_quality_compounder_stablecomp_504d_base_v087_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    lvl = _mean(q, 252)
    vol = _std(q, 504)
    b = lvl / (1.0 + vol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v088 dilution-vs-equity efficiency: did issuance build book per share?
def f37pq_f37_producer_quality_compounder_dileff_504d_base_v088_signal(sharesbas, equity):
    dil = _dilution(sharesbas, 504)
    bv = _bvps(equity, sharesbas)
    bvg = np.log(bv.replace(0, np.nan) / bv.shift(504).replace(0, np.nan))
    b = bvg - np.tanh(5.0 * dil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v089 quality-weighted scale momentum: revenue growth x quality level
def f37pq_f37_producer_quality_compounder_qscalemom_252d_base_v089_signal(revenue, roic, fcf):
    rg = _rev_growth(revenue, 252)
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    b = rg * _mean(q, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v090 net-margin x FCF-margin minus their disagreement (coherent profitability)
def f37pq_f37_producer_quality_compounder_marcoh_252d_base_v090_signal(netmargin, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    a = np.tanh(4.0 * netmargin)
    bb = np.tanh(4.0 * fm)
    b = (a + bb) / 2.0 - (a - bb).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v091 ROIC-funded growth headroom: ROIC minus revenue/share growth
def f37pq_f37_producer_quality_compounder_roichdrm_252d_base_v091_signal(roic, revenue, sharesbas):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = np.log(rps.replace(0, np.nan) / rps.shift(252).replace(0, np.nan))
    b = np.tanh(3.0 * _mean(roic, 126)) - g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v092 high-conviction compounder: all three (roic,fcf,netmargin) above own median (count)
def f37pq_f37_producer_quality_compounder_conviction_252d_base_v092_signal(roic, fcf, netmargin):
    r = (roic > roic.rolling(504, min_periods=126).median()).astype(float)
    f = (fcf > fcf.rolling(504, min_periods=126).median()).astype(float)
    m = (netmargin > netmargin.rolling(504, min_periods=126).median()).astype(float)
    cnt = r + f + m
    b = cnt.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v093 cash-flow-return-on-equity trend, dilution-adjusted
def f37pq_f37_producer_quality_compounder_croetrend_252d_base_v093_signal(fcf, equity, sharesbas):
    croe = fcf / equity.replace(0, np.nan)
    tr = _slope(_mean(croe, 63), 126)
    anti = _antidilution(sharesbas, 126)
    b = np.tanh(15.0 * tr) + 2.0 * anti
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v094 durable-FCF: positive-FCF fraction over 504d weighted by FCF-margin level
def f37pq_f37_producer_quality_compounder_durfcf_504d_base_v094_signal(fcf, revenue):
    pf = _pos_frac(fcf, 504)
    fm = _mean(_fcf_margin(fcf, revenue), 252)
    b = pf * (1.0 + np.tanh(3.0 * fm))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v095 equity-compounding consistency: positive equity-growth fraction x ROIC
def f37pq_f37_producer_quality_compounder_eqcons_504d_base_v095_signal(equity, roic):
    eg = equity.pct_change(21)
    pf = _pos_frac(eg, 504)
    b = pf * np.tanh(3.0 * _mean(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v096 margin-cycle position: net-margin range position x FCF positivity
def f37pq_f37_producer_quality_compounder_marpos_504d_base_v096_signal(netmargin, fcf):
    hi = _rmax(netmargin, 504)
    lo = _rmin(netmargin, 504)
    pos = (netmargin - lo) / (hi - lo).replace(0, np.nan)
    b = (pos - 0.5) * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v097 self-financed expansion: revenue growth covered by FCF (no raise needed)
def f37pq_f37_producer_quality_compounder_selfexp_252d_base_v097_signal(revenue, fcf, sharesbas):
    rg = _rev_growth(revenue, 252)
    fm = _fcf_margin(fcf, revenue)
    nondil = (_dilution(sharesbas, 252) <= 0.02).astype(float)
    b = rg * np.tanh(3.0 * fm) * (0.5 + 0.5 * nondil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v098 quality vs share-count divergence: quality up while shares flat/down
def f37pq_f37_producer_quality_compounder_qshdiv_252d_base_v098_signal(roic, fcf, revenue, sharesbas):
    q = _quality(roic, fcf, revenue)
    qtr = _slope(q, 126)
    shtr = _slope(np.log(sharesbas.replace(0, np.nan)), 126)
    b = np.tanh(10.0 * qtr) - np.tanh(50.0 * shtr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v099 normalized owner earnings: (netmargin*revenue - dilution cost) per share
def f37pq_f37_producer_quality_compounder_normowner_252d_base_v099_signal(netmargin, revenue, sharesbas):
    earn = netmargin * revenue
    eps = earn / sharesbas.replace(0, np.nan)
    dil = _dilution(sharesbas, 252)
    b = _z(eps, 252) - 2.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v100 long-run returns trajectory: recent ROIC vs its 5y baseline, FCF-sign gated
def f37pq_f37_producer_quality_compounder_roic5y_1260d_base_v100_signal(roic, fcf, revenue):
    base5y = _mean(roic, 1260)
    recent = _mean(roic, 252)
    spread = recent - base5y
    b = np.tanh(4.0 * spread) * np.sign(_mean(fcf, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v101 cash-to-equity yield rank, dilution gated
def f37pq_f37_producer_quality_compounder_croeyrank_504d_base_v101_signal(fcf, equity, sharesbas):
    croe = fcf / equity.replace(0, np.nan)
    rk = _rank(_mean(croe, 126), 504)
    anti = (_dilution(sharesbas, 252) <= 0).astype(float)
    b = rk * (0.5 + 0.5 * anti)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v102 margin x scale interaction z (large + profitable)
def f37pq_f37_producer_quality_compounder_marscale_252d_base_v102_signal(netmargin, revenue):
    scale = np.log(revenue.replace(0, np.nan))
    b = _z(netmargin, 252) + _z(scale, 252) * np.sign(_mean(netmargin, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v103 FCF-conversion of equity: FCF/equity vs ROIC (cash backing reported returns)
def f37pq_f37_producer_quality_compounder_fcfconv_252d_base_v103_signal(fcf, equity, roic):
    croe = fcf / equity.replace(0, np.nan)
    b = np.tanh(3.0 * _mean(croe, 126)) - np.tanh(3.0 * _mean(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v104 durable-quality streak: consecutive 21d windows with quality>0
def f37pq_f37_producer_quality_compounder_qstreak_252d_base_v104_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    good = (q > 0).astype(float)
    streak = good.rolling(252, min_periods=126).sum()
    b = streak + 0.05 * _mean(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v105 antidilution x revenue-per-share growth (per-owner top-line build)
def f37pq_f37_producer_quality_compounder_antirevps_252d_base_v105_signal(sharesbas, revenue):
    anti = _antidilution(sharesbas, 252)
    rps = revenue / sharesbas.replace(0, np.nan)
    g = rps.pct_change(252)
    b = g * (1.0 + np.tanh(8.0 * anti))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v106 quality acceleration (2nd diff) of blended quality, level-gated
def f37pq_f37_producer_quality_compounder_qaccel2_252d_base_v106_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    accel = q.diff(63) - q.diff(63).shift(63)
    b = accel * (0.5 + 0.5 * np.sign(_mean(q, 126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v107 net-margin-funded equity growth (margins, not raises, growing book)
def f37pq_f37_producer_quality_compounder_nmfundeq_252d_base_v107_signal(netmargin, equity, sharesbas):
    eg = _equity_growth(equity, 252)
    dil = _dilution(sharesbas, 252)
    organic = eg - dil
    b = organic * np.tanh(4.0 * _mean(netmargin, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v108 cash-rich grower: FCF margin x revenue growth, dilution-penalized
def f37pq_f37_producer_quality_compounder_cashgrow_252d_base_v108_signal(fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    rg = _rev_growth(revenue, 252)
    dil = _dilution(sharesbas, 252)
    b = np.tanh(3.0 * fm) * rg - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v109 ROIC distance above 5y median scaled by FCF positivity
def f37pq_f37_producer_quality_compounder_roic5yexc_1260d_base_v109_signal(roic, fcf):
    med = roic.rolling(1260, min_periods=504).median()
    b = (roic - med) * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v110 compounder composite minus its own 252d-ago value (regime change)
def f37pq_f37_producer_quality_compounder_compregchg_252d_base_v110_signal(roic, fcf, revenue, netmargin):
    fm = _fcf_margin(fcf, revenue)
    comp = np.tanh(3.0 * roic) + np.tanh(3.0 * fm) + np.tanh(4.0 * netmargin)
    b = _mean(comp, 63) - _mean(comp, 63).shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v111 book-value-per-share new-high frequency (steady book compounding, count)
def f37pq_f37_producer_quality_compounder_bvnewhi_504d_base_v111_signal(equity, sharesbas, roic):
    bv = _bvps(equity, sharesbas)
    hi = _rmax(bv.shift(1), 504)
    flag = (bv >= hi).astype(float)
    freq = flag.rolling(252, min_periods=126).mean()
    b = freq + 0.1 * np.tanh(3.0 * _mean(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v112 net-margin predictability: margin level per unit of margin volatility, ROIC-sign gated
def f37pq_f37_producer_quality_compounder_predict_252d_base_v112_signal(netmargin, roic):
    m = _mean(netmargin, 252)
    mvol = _std(netmargin, 252)
    info = m / mvol.replace(0, np.nan)
    b = np.tanh(info) * np.sign(_mean(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v113 FCF coverage of share-issuance cost (cash funds the raise it didn't need)
def f37pq_f37_producer_quality_compounder_fcfraise_252d_base_v113_signal(fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    raise_rate = _dilution(sharesbas, 126).clip(lower=0)
    b = np.tanh(3.0 * fm) - 8.0 * raise_rate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v114 multi-driver z-average (overall compounder strength)
def f37pq_f37_producer_quality_compounder_zavg_252d_base_v114_signal(roic, fcf, revenue, netmargin, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    stacked = pd.concat([_z(roic, 252), _z(fm, 252), _z(netmargin, 252),
                         -_z(_dilution(sharesbas, 252), 252)], axis=1)
    b = stacked.mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v115 quality range-position over 5y (where in its quality cycle, count-friendly)
def f37pq_f37_producer_quality_compounder_qcyclepos_1260d_base_v115_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    hi = _rmax(q, 1260)
    lo = _rmin(q, 1260)
    b = (q - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v116 cash-margin minus accrual-margin trend (improving cash quality)
def f37pq_f37_producer_quality_compounder_cashqualtr_252d_base_v116_signal(fcf, revenue, netmargin):
    fm = _fcf_margin(fcf, revenue)
    gap = fm - netmargin
    b = _slope(_mean(gap, 63), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v117 ROIC x equity-per-share growth (returns on a growing per-owner base)
def f37pq_f37_producer_quality_compounder_roicbvg_252d_base_v117_signal(roic, equity, sharesbas):
    bv = _bvps(equity, sharesbas)
    g = bv.pct_change(252)
    b = np.tanh(3.0 * _mean(roic, 126)) * np.tanh(3.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v118 distress-free quality: quality level when net-margin and FCF both positive
def f37pq_f37_producer_quality_compounder_distfree_252d_base_v118_signal(roic, fcf, revenue, netmargin):
    q = _quality(roic, fcf, revenue)
    healthy = ((netmargin > 0) & (fcf > 0)).astype(float)
    b = _mean(q * healthy, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v119 share-count stability x profitability (tight float + earns money)
def f37pq_f37_producer_quality_compounder_tightprof_252d_base_v119_signal(sharesbas, netmargin):
    shvol = _std(np.log(sharesbas.replace(0, np.nan)).diff(21), 252)
    b = np.tanh(4.0 * _mean(netmargin, 126)) / (1.0 + np.tanh(80.0 * shvol))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v120 FCF-per-share 5y compounding net of dilution
def f37pq_f37_producer_quality_compounder_fcfps5y_1260d_base_v120_signal(fcf, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    g = fps - fps.shift(1260)
    dil = _dilution(sharesbas, 1260)
    b = g - 0.3 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v121 quality vs cycle-amplitude (quality producers swing less)
def f37pq_f37_producer_quality_compounder_lowswing_504d_base_v121_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    amp = (_rmax(q, 504) - _rmin(q, 504))
    b = _mean(q, 252) - np.tanh(amp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v122 equity-efficiency rank: ROIC x asset turnover proxy (rev/equity), ranked
def f37pq_f37_producer_quality_compounder_effrank_252d_base_v122_signal(roic, revenue, equity):
    turn = revenue / equity.replace(0, np.nan)
    score = np.tanh(3.0 * roic) * np.tanh(turn)
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v123 net-margin x FCF positivity gated by no-dilution flag
def f37pq_f37_producer_quality_compounder_marqualgate_252d_base_v123_signal(netmargin, fcf, sharesbas):
    nondil = (sharesbas.diff(63) <= 0).astype(float)
    b = np.tanh(4.0 * _mean(netmargin, 126)) * _pos_frac(fcf, 252) * (0.5 + 0.5 * nondil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v124 compounder breakout-from-base: time spent compressed then quality lifting off the floor
def f37pq_f37_producer_quality_compounder_qbreak_504d_base_v124_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    floor = _rmin(q.shift(21), 504)
    liftoff = (q - floor)
    tight = (_std(q, 252) < _std(q, 504)).astype(float)
    b = np.tanh(liftoff) * (0.5 + 0.5 * tight)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v125 ROIC-funded dividend capacity proxy: FCF/equity minus reinvest need
def f37pq_f37_producer_quality_compounder_divcap_252d_base_v125_signal(fcf, equity, revenue):
    croe = fcf / equity.replace(0, np.nan)
    reinvest = _rev_growth(revenue, 252).clip(lower=0)
    b = np.tanh(3.0 * _mean(croe, 126)) - reinvest
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v126 quality term-structure: short-horizon quality minus long-horizon (improving/fading)
def f37pq_f37_producer_quality_compounder_qhorizon_base_v126_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    s = _mean(q, 126)
    l = _mean(q, 504)
    b = np.tanh(s - l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v127 dilution-adjusted earnings yield: eps z minus dilution z
def f37pq_f37_producer_quality_compounder_epsdil_252d_base_v127_signal(netmargin, revenue, sharesbas):
    eps = netmargin * revenue / sharesbas.replace(0, np.nan)
    b = _z(_mean(eps, 63), 252) - _z(_dilution(sharesbas, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v128 free-cash compounding rate x positive-net-margin fraction
def f37pq_f37_producer_quality_compounder_fcfcompnm_504d_base_v128_signal(fcf, sharesbas, netmargin):
    fps = _fcf_per_share(fcf, sharesbas)
    g = fps.diff(252)
    b = np.tanh(g / (fps.abs().rolling(252, min_periods=126).mean() + 1e-9)) * _pos_frac(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v129 quality z minus dilution-streak fraction (high quality, no dilution)
def f37pq_f37_producer_quality_compounder_qzdil_252d_base_v129_signal(roic, fcf, revenue, sharesbas):
    q = _quality(roic, fcf, revenue)
    dilbad = (sharesbas.diff(21) > 0).astype(float).rolling(252, min_periods=126).mean()
    b = _z(q, 252) - 2.0 * dilbad
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v130 revenue-quality scale: log-revenue x net-margin x ROIC sign agreement
def f37pq_f37_producer_quality_compounder_revqualscale_252d_base_v130_signal(revenue, netmargin, roic):
    scale = _z(np.log(revenue.replace(0, np.nan)), 252)
    qual = np.sign(_mean(netmargin, 126)) * np.sign(_mean(roic, 126))
    b = scale * qual
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v131 cash-conversion smoothness: fraction of months FCF-margin moves up (steady grind)
def f37pq_f37_producer_quality_compounder_ccstab_504d_base_v131_signal(fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    up = (fm.diff(21) > 0).astype(float)
    smooth = up.rolling(504, min_periods=252).mean()
    b = (smooth - 0.5) * np.sign(_mean(fm, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v132 antidilution-weighted ROIC level (returns that don't dilute owners)
def f37pq_f37_producer_quality_compounder_antiroic_252d_base_v132_signal(roic, sharesbas):
    anti = _antidilution(sharesbas, 252)
    b = np.tanh(3.0 * _mean(roic, 126)) * (1.0 + np.tanh(8.0 * anti))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v133 equity-to-share ratio momentum (book per share accelerating), FCF gated
def f37pq_f37_producer_quality_compounder_bvmomgate_252d_base_v133_signal(equity, sharesbas, fcf):
    bv = _bvps(equity, sharesbas)
    mom = bv.pct_change(126)
    b = np.tanh(3.0 * mom) * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v134 quality persistence rank vs own 5y (durable-producer percentile)
def f37pq_f37_producer_quality_compounder_qpersrank_1260d_base_v134_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    pf = _pos_frac(q, 504)
    b = _rank(pf, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v135 margin-trough recovery x antidilution (recovering profitably & cleanly)
def f37pq_f37_producer_quality_compounder_marrecov_504d_base_v135_signal(netmargin, sharesbas):
    trough = _rmin(netmargin, 504)
    rec = netmargin - trough
    anti = _antidilution(sharesbas, 252)
    b = rec * (1.0 + np.tanh(5.0 * anti))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v136 FCF/revenue x ROIC, drawdown from 504d peak (quality erosion)
def f37pq_f37_producer_quality_compounder_qerode_504d_base_v136_signal(fcf, revenue, roic):
    fm = _fcf_margin(fcf, revenue)
    prod = np.tanh(3.0 * fm) * np.tanh(3.0 * roic)
    peak = _rmax(prod, 504)
    b = prod - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v137 sustainable compounding rate: min(ROIC, equity-growth) net of dilution
def f37pq_f37_producer_quality_compounder_susrate_252d_base_v137_signal(roic, equity, sharesbas):
    eg = _equity_growth(equity, 252)
    dil = _dilution(sharesbas, 252)
    floor = pd.concat([np.tanh(3.0 * _mean(roic, 126)), np.tanh(3.0 * eg)], axis=1).min(axis=1)
    b = floor - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v138 cash-quality breadth: fraction of 5y with FCF-margin above its own median
def f37pq_f37_producer_quality_compounder_ccbreadth_1260d_base_v138_signal(fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    med = fm.rolling(1260, min_periods=504).median()
    flag = (fm > med).astype(float)
    b = flag.rolling(504, min_periods=252).mean() + 0.1 * np.tanh(3.0 * _mean(fm, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v139 ROIC-net-margin product trend (joint profitability improving)
def f37pq_f37_producer_quality_compounder_jointtr_252d_base_v139_signal(roic, netmargin):
    prod = np.tanh(3.0 * roic) * np.tanh(4.0 * netmargin)
    b = _slope(_mean(prod, 63), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v140 per-share total-value build: (equity+FCF)/shares growth
def f37pq_f37_producer_quality_compounder_tvps_252d_base_v140_signal(equity, fcf, sharesbas):
    tv = (equity + fcf.rolling(252, min_periods=126).sum()) / sharesbas.replace(0, np.nan)
    b = np.log(tv.replace(0, np.nan) / tv.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v141 compounder quality minus revenue-volatility (steady, profitable scale)
def f37pq_f37_producer_quality_compounder_steadyscale_252d_base_v141_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    rvol = _std(revenue.pct_change(21), 252)
    b = _mean(q, 126) - np.tanh(4.0 * rvol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v142 antidilution streak length x ROIC positivity (count-friendly)
def f37pq_f37_producer_quality_compounder_antistreak_252d_base_v142_signal(sharesbas, roic):
    good = (sharesbas.diff(21) <= 0).astype(float)
    streak = good.rolling(252, min_periods=126).sum()
    b = streak * (0.5 + 0.5 * _pos_frac(roic, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v143 quality-vs-cycle-low distance, dilution-penalized
def f37pq_f37_producer_quality_compounder_qlowdist_1260d_base_v143_signal(roic, fcf, revenue, sharesbas):
    q = _quality(roic, fcf, revenue)
    lo = _rmin(q, 1260)
    dil = _dilution(sharesbas, 252).clip(lower=0)
    b = (q - lo) - 3.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v144 cash-return spread: cash-on-revenue minus cash-on-equity (margin vs leverage source)
def f37pq_f37_producer_quality_compounder_returnblend_252d_base_v144_signal(fcf, revenue, equity):
    cror = fcf / revenue.replace(0, np.nan)
    croe = fcf / equity.replace(0, np.nan)
    b = np.tanh(3.0 * _mean(cror, 126)) - np.tanh(3.0 * _mean(croe, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v145 dilution-discounted compounder composite (full driver blend)
def f37pq_f37_producer_quality_compounder_fullblend_252d_base_v145_signal(roic, fcf, revenue, netmargin, sharesbas, equity):
    fm = _fcf_margin(fcf, revenue)
    eg = _equity_growth(equity, 252)
    dil = _dilution(sharesbas, 252)
    b = (np.tanh(3.0 * roic) + np.tanh(3.0 * fm) + np.tanh(4.0 * netmargin)
         + np.tanh(3.0 * eg)) / 4.0 - dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v146 quality z-momentum (change in z-scored quality, regime shift)
def f37pq_f37_producer_quality_compounder_qzmom_252d_base_v146_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    zz = _z(q, 252)
    b = zz - zz.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v147 net-margin x antidilution rank (clean profitability percentile)
def f37pq_f37_producer_quality_compounder_cleanprofrank_504d_base_v147_signal(netmargin, sharesbas):
    anti = _antidilution(sharesbas, 252)
    score = np.tanh(4.0 * _mean(netmargin, 126)) + 2.0 * anti
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v148 high-return-low-dilution quadrant score (count-friendly)
def f37pq_f37_producer_quality_compounder_quadrant_252d_base_v148_signal(roic, sharesbas, fcf):
    hr = (roic > roic.rolling(504, min_periods=126).median()).astype(float)
    ld = (_dilution(sharesbas, 126) <= 0).astype(float)
    pf = (fcf > 0).astype(float)
    score = hr + ld + pf
    b = score.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v149 compounder Sharpe: quality mean over quality std (risk-adj durable quality)
def f37pq_f37_producer_quality_compounder_qsharpe_504d_base_v149_signal(roic, fcf, revenue):
    q = _quality(roic, fcf, revenue)
    m = _mean(q, 504)
    sd = _std(q, 504)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v150 master compounder index: quality x antidilution x equity-build, ranked
def f37pq_f37_producer_quality_compounder_master_504d_base_v150_signal(roic, fcf, revenue, sharesbas, equity):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    anti = np.tanh(8.0 * _antidilution(sharesbas, 252))
    eg = np.tanh(3.0 * _equity_growth(equity, 252))
    raw = _mean(q, 126) * (1.0 + 0.5 * anti) * (1.0 + 0.5 * eg)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37pq_f37_producer_quality_compounder_roeanti_252d_base_v076_signal,
    f37pq_f37_producer_quality_compounder_qdd_504d_base_v077_signal,
    f37pq_f37_producer_quality_compounder_cashacc_252d_base_v078_signal,
    f37pq_f37_producer_quality_compounder_relcomp_252d_base_v079_signal,
    f37pq_f37_producer_quality_compounder_roicterm_base_v080_signal,
    f37pq_f37_producer_quality_compounder_dildisp_252d_base_v081_signal,
    f37pq_f37_producer_quality_compounder_qmomrank_252d_base_v082_signal,
    f37pq_f37_producer_quality_compounder_deepqual_252d_base_v083_signal,
    f37pq_f37_producer_quality_compounder_nmtrough_504d_base_v084_signal,
    f37pq_f37_producer_quality_compounder_owneryield_252d_base_v085_signal,
    f37pq_f37_producer_quality_compounder_revpsaccel_252d_base_v086_signal,
    f37pq_f37_producer_quality_compounder_stablecomp_504d_base_v087_signal,
    f37pq_f37_producer_quality_compounder_dileff_504d_base_v088_signal,
    f37pq_f37_producer_quality_compounder_qscalemom_252d_base_v089_signal,
    f37pq_f37_producer_quality_compounder_marcoh_252d_base_v090_signal,
    f37pq_f37_producer_quality_compounder_roichdrm_252d_base_v091_signal,
    f37pq_f37_producer_quality_compounder_conviction_252d_base_v092_signal,
    f37pq_f37_producer_quality_compounder_croetrend_252d_base_v093_signal,
    f37pq_f37_producer_quality_compounder_durfcf_504d_base_v094_signal,
    f37pq_f37_producer_quality_compounder_eqcons_504d_base_v095_signal,
    f37pq_f37_producer_quality_compounder_marpos_504d_base_v096_signal,
    f37pq_f37_producer_quality_compounder_selfexp_252d_base_v097_signal,
    f37pq_f37_producer_quality_compounder_qshdiv_252d_base_v098_signal,
    f37pq_f37_producer_quality_compounder_normowner_252d_base_v099_signal,
    f37pq_f37_producer_quality_compounder_roic5y_1260d_base_v100_signal,
    f37pq_f37_producer_quality_compounder_croeyrank_504d_base_v101_signal,
    f37pq_f37_producer_quality_compounder_marscale_252d_base_v102_signal,
    f37pq_f37_producer_quality_compounder_fcfconv_252d_base_v103_signal,
    f37pq_f37_producer_quality_compounder_qstreak_252d_base_v104_signal,
    f37pq_f37_producer_quality_compounder_antirevps_252d_base_v105_signal,
    f37pq_f37_producer_quality_compounder_qaccel2_252d_base_v106_signal,
    f37pq_f37_producer_quality_compounder_nmfundeq_252d_base_v107_signal,
    f37pq_f37_producer_quality_compounder_cashgrow_252d_base_v108_signal,
    f37pq_f37_producer_quality_compounder_roic5yexc_1260d_base_v109_signal,
    f37pq_f37_producer_quality_compounder_compregchg_252d_base_v110_signal,
    f37pq_f37_producer_quality_compounder_bvnewhi_504d_base_v111_signal,
    f37pq_f37_producer_quality_compounder_predict_252d_base_v112_signal,
    f37pq_f37_producer_quality_compounder_fcfraise_252d_base_v113_signal,
    f37pq_f37_producer_quality_compounder_zavg_252d_base_v114_signal,
    f37pq_f37_producer_quality_compounder_qcyclepos_1260d_base_v115_signal,
    f37pq_f37_producer_quality_compounder_cashqualtr_252d_base_v116_signal,
    f37pq_f37_producer_quality_compounder_roicbvg_252d_base_v117_signal,
    f37pq_f37_producer_quality_compounder_distfree_252d_base_v118_signal,
    f37pq_f37_producer_quality_compounder_tightprof_252d_base_v119_signal,
    f37pq_f37_producer_quality_compounder_fcfps5y_1260d_base_v120_signal,
    f37pq_f37_producer_quality_compounder_lowswing_504d_base_v121_signal,
    f37pq_f37_producer_quality_compounder_effrank_252d_base_v122_signal,
    f37pq_f37_producer_quality_compounder_marqualgate_252d_base_v123_signal,
    f37pq_f37_producer_quality_compounder_qbreak_504d_base_v124_signal,
    f37pq_f37_producer_quality_compounder_divcap_252d_base_v125_signal,
    f37pq_f37_producer_quality_compounder_qhorizon_base_v126_signal,
    f37pq_f37_producer_quality_compounder_epsdil_252d_base_v127_signal,
    f37pq_f37_producer_quality_compounder_fcfcompnm_504d_base_v128_signal,
    f37pq_f37_producer_quality_compounder_qzdil_252d_base_v129_signal,
    f37pq_f37_producer_quality_compounder_revqualscale_252d_base_v130_signal,
    f37pq_f37_producer_quality_compounder_ccstab_504d_base_v131_signal,
    f37pq_f37_producer_quality_compounder_antiroic_252d_base_v132_signal,
    f37pq_f37_producer_quality_compounder_bvmomgate_252d_base_v133_signal,
    f37pq_f37_producer_quality_compounder_qpersrank_1260d_base_v134_signal,
    f37pq_f37_producer_quality_compounder_marrecov_504d_base_v135_signal,
    f37pq_f37_producer_quality_compounder_qerode_504d_base_v136_signal,
    f37pq_f37_producer_quality_compounder_susrate_252d_base_v137_signal,
    f37pq_f37_producer_quality_compounder_ccbreadth_1260d_base_v138_signal,
    f37pq_f37_producer_quality_compounder_jointtr_252d_base_v139_signal,
    f37pq_f37_producer_quality_compounder_tvps_252d_base_v140_signal,
    f37pq_f37_producer_quality_compounder_steadyscale_252d_base_v141_signal,
    f37pq_f37_producer_quality_compounder_antistreak_252d_base_v142_signal,
    f37pq_f37_producer_quality_compounder_qlowdist_1260d_base_v143_signal,
    f37pq_f37_producer_quality_compounder_returnblend_252d_base_v144_signal,
    f37pq_f37_producer_quality_compounder_fullblend_252d_base_v145_signal,
    f37pq_f37_producer_quality_compounder_qzmom_252d_base_v146_signal,
    f37pq_f37_producer_quality_compounder_cleanprofrank_504d_base_v147_signal,
    f37pq_f37_producer_quality_compounder_quadrant_252d_base_v148_signal,
    f37pq_f37_producer_quality_compounder_qsharpe_504d_base_v149_signal,
    f37pq_f37_producer_quality_compounder_master_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_PRODUCER_QUALITY_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    roic = _fund(3, base=0.12, drift=-0.01, vol=0.55, allow_neg=True).rename("roic")
    fcf = _fund(5, base=5e7, drift=-0.01, vol=0.55, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=2e8, drift=0.03, vol=0.04).rename("sharesbas")
    netmargin = _fund(14, base=0.10, drift=-0.01, vol=0.55, allow_neg=True).rename("netmargin")
    revenue = _fund(105, base=3e8, drift=0.02, vol=0.10).rename("revenue")
    equity = _fund(106, base=4e8, drift=0.02, vol=0.08).rename("equity")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "netmargin": netmargin, "revenue": revenue, "equity": equity}

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

    print("OK f37_producer_quality_compounder_base_076_150_claude: %d features pass" % n_features)
