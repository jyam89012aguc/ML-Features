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
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    # 2nd math derivative: change of slope over w trading days
    sl = (s - s.shift(w)) / float(w)
    return (sl - sl.shift(w)) / float(w)


# ===== folder domain primitives (earnings cyclicality) =====
# Deeply cyclical miners: netinc/eps/ebit/roic/roe swing across zero through the
# commodity cycle; equity is a positive scale base. These primitives quantify
# earnings volatility/amplitude through cycle, ROIC/ROE swing, earnings
# trough/peak distance, earnings-positive streak, cyclical earnings z, EBIT swing.
def _ec_amp(s, w):
    # peak-to-trough amplitude over the window, normalized by typical magnitude
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    typ = s.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return (hi - lo) / (typ + 1e-9)


def _ec_cv(s, w):
    # coefficient-of-variation style swing: dispersion over absolute level
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    lvl = s.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / (lvl + 1e-9)


def _ec_pos(s, w):
    # position in the cyclical range: 0 at trough, 1 at peak
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _ec_fromtrough(s, w):
    # recovery off the cyclical trough as a signed-magnitude multiple of trough
    # size, then percentile-ranked vs a longer window so it is a genuinely
    # distinct facet from linear range position (_ec_pos) and drawdown-from-peak.
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    raw = (s - lo) / (lo.abs() + 1e-9)
    rec = np.sign(raw) * np.log1p(raw.abs())
    lw = min(1260, max(126, 2 * w))
    return rec.rolling(lw, min_periods=max(1, lw // 4)).rank(pct=True) - 0.5


def _ec_frompeak(s, w):
    # drawdown below the cyclical peak as a signed-magnitude fraction of peak
    # size, then displaced vs its own slow EWM (mean-reversion of the drawdown)
    # so it is a distinct facet from range position and trough-recovery.
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    raw = (s - hi) / (hi.abs() + 1e-9)
    dd = np.sign(raw) * np.log1p(raw.abs())
    span = max(21, w // 4)
    return dd - dd.ewm(span=span, min_periods=max(5, span // 2)).mean()


def _ec_pospos(s):
    # 1.0 when the earnings flow is positive (in an up-phase of the cycle)
    return (s > 0.0).astype(float)


def _ec_posstreak(s):
    # consecutive earnings-positive streak length (resets to 0 on any loss)
    pos = (s > 0.0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()


def _ec_posfrac(s, w):
    # fraction of the window the flow was positive (earnings-positive persistence)
    return _ec_pospos(s).rolling(w, min_periods=max(1, w // 2)).mean()


def _ec_signmag(s, scale):
    # sign x sqrt-magnitude (compresses the cyclical swing across zero)
    return np.sign(s) * np.sqrt(s.abs() / float(scale))


def _ec_ratio(a, b):
    # ratio of an earnings flow to an equity scale (return-on-equity-like)
    return a / b.replace(0, np.nan)


# ============================================================
# net-income/equity multi-year cyclical position, half-year rotation
def f33ec_f33_earnings_cyclicality_nieqpos_1260d_base_v076_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    p = _ec_pos(r, 1260)
    base = p - p.shift(126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income downside semi-deviation (down-cycle earnings vol)
def f33ec_f33_earnings_cyclicality_nidownvol_252d_base_v077_signal(netinc):
    d = (netinc - _mean(netinc, 252))
    neg = d.clip(upper=0.0)
    base = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean()) / (netinc.abs().rolling(252, min_periods=126).mean() + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT upside semi-deviation (up-cycle earnings vol)
def f33ec_f33_earnings_cyclicality_ebitupvol_252d_base_v078_signal(ebit):
    d = (ebit - _mean(ebit, 252))
    posd = d.clip(lower=0.0)
    base = np.sqrt((posd ** 2).rolling(252, min_periods=126).mean()) / (ebit.abs().rolling(252, min_periods=126).mean() + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC vol asymmetry: upside minus downside semi-dev (cycle skew)
def f33ec_f33_earnings_cyclicality_roicsemiskew_504d_base_v079_signal(roic):
    d = (roic - _mean(roic, 504))
    up = np.sqrt((d.clip(lower=0.0) ** 2).rolling(504, min_periods=252).mean())
    dn = np.sqrt((d.clip(upper=0.0) ** 2).rolling(504, min_periods=252).mean())
    base = (up - dn) / (up + dn + 1e-9)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income amplitude percentile-ranked vs its own two-year history
def f33ec_f33_earnings_cyclicality_niamprank_base_v080_signal(netinc):
    amp = _ec_amp(netinc, 252)
    base = _rank(amp, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC swing percentile-ranked vs its own two-year history
def f33ec_f33_earnings_cyclicality_roicswingrank_base_v081_signal(roic):
    cv = _ec_cv(roic, 252)
    base = _rank(cv, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/equity cyclical position percentile-ranked vs multi-year history
def f33ec_f33_earnings_cyclicality_ebitposrank_base_v082_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    p = _ec_pos(r, 504)
    base = _rank(p, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income days-since-cyclical-peak (staleness of the earnings high)
def f33ec_f33_earnings_cyclicality_nidaysincepeak_252d_base_v083_signal(netinc):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = netinc.rolling(252, min_periods=126).apply(_f, raw=True)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT days-since-cyclical-trough (time recovering off the bottom)
def f33ec_f33_earnings_cyclicality_ebitdaysincetrough_504d_base_v084_signal(ebit):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    base = ebit.rolling(504, min_periods=252).apply(_f, raw=True)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# how many of {netinc,ebit,roic} are positive (cycle up-phase breadth)
def f33ec_f33_earnings_cyclicality_cyclebreadth_63d_base_v085_signal(netinc, ebit, roic):
    raw = _ec_pospos(netinc) + _ec_pospos(ebit) + _ec_pospos(roic)
    base = raw.rolling(63, min_periods=21).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year all three profit metrics positive, quarterly change (cycle phase rotation)
def f33ec_f33_earnings_cyclicality_tripleposfrac_252d_base_v086_signal(netinc, ebit, roe):
    triple = ((netinc > 0) & (ebit > 0) & (roe > 0)).astype(float)
    frac = triple.rolling(252, min_periods=126).mean()
    base = frac - frac.shift(63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-loss-while-operating-profit divergence (below-line cyclical drag)
def f33ec_f33_earnings_cyclicality_cycledivg_126d_base_v087_signal(netinc, ebit):
    div = ((netinc < 0) & (ebit > 0)).astype(float)
    base = div.rolling(126, min_periods=63).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income cumulative cyclical earnings, quarterly momentum
def f33ec_f33_earnings_cyclicality_nicumcycle_252d_base_v088_signal(netinc):
    sm = _ec_signmag(netinc, 1e6)
    cum = sm.rolling(252, min_periods=126).sum() / 252.0
    base = cum - cum.shift(63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cumulative cyclical earnings z-scored over the year
def f33ec_f33_earnings_cyclicality_ebitcumcycle_504d_base_v089_signal(ebit):
    sm = _ec_signmag(ebit, 1e6)
    cum = sm.rolling(504, min_periods=252).sum() / 504.0
    base = _z(cum, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income peak-trough amplitude scaled by equity base (cycle severity)
def f33ec_f33_earnings_cyclicality_niampeq_504d_base_v090_signal(netinc, equity):
    hi = _rmax(netinc, 504)
    lo = _rmin(netinc, 504)
    base = (hi - lo) / (equity.replace(0, np.nan).abs() + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT multi-year amplitude scaled by equity base
def f33ec_f33_earnings_cyclicality_ebitampeq_1260d_base_v091_signal(ebit, equity):
    hi = _rmax(ebit, 1260)
    lo = _rmin(ebit, 1260)
    base = (hi - lo) / (equity.replace(0, np.nan).abs() + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income up vs down phase balance, percentile-ranked over two years
def f33ec_f33_earnings_cyclicality_niphasebal_252d_base_v092_signal(netinc):
    profw = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    lossw = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    bal = (profw - lossw) / (profw + lossw + 1e6)
    base = _rank(bal, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT up-phase vs down-phase magnitude balance over two years
def f33ec_f33_earnings_cyclicality_ebitphasebal_504d_base_v093_signal(ebit):
    profw = ebit.clip(lower=0.0).rolling(504, min_periods=252).sum()
    lossw = (-ebit).clip(lower=0.0).rolling(504, min_periods=252).sum()
    base = (profw - lossw) / (profw + lossw + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE up-phase vs down-phase magnitude balance over the year
def f33ec_f33_earnings_cyclicality_roephasebal_252d_base_v094_signal(roe):
    profw = roe.clip(lower=0.0).rolling(252, min_periods=126).sum()
    lossw = (-roe).clip(lower=0.0).rolling(252, min_periods=126).sum()
    base = (profw - lossw) / (profw + lossw + 1e-9)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC swing displacement vs its own slow EWM (swing regime shift)
def f33ec_f33_earnings_cyclicality_roiccvdisp_252d_base_v095_signal(roic):
    cv = _ec_cv(roic, 252)
    base = cv - cv.ewm(span=126, min_periods=63).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-minus-ROIC spread cyclical position fast-slow EMA oscillator (leverage-phase)
def f33ec_f33_earnings_cyclicality_roeposema_252d_base_v096_signal(roe, roic):
    spr = roe - roic
    p = _ec_pos(spr, 252)
    base = p.ewm(span=21, min_periods=10).mean() - p.ewm(span=84, min_periods=42).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income cyclical position year-over-year change (phase rotation)
def f33ec_f33_earnings_cyclicality_niposyoy_252d_base_v097_signal(netinc):
    p = _ec_pos(netinc, 252)
    base = p - p.shift(252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread cyclical-z year-over-year change
def f33ec_f33_earnings_cyclicality_ebitzyoy_504d_base_v098_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 504)
    base = zz - zz.shift(252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income swing relative to EBIT swing (below-line amplification ratio)
def f33ec_f33_earnings_cyclicality_niampxpos_252d_base_v099_signal(netinc, ebit):
    amp = _ec_cv(netinc, 252)
    opamp = _ec_cv(ebit, 252)
    base = (amp + 0.05) / (opamp + 0.05)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC amplitude-to-CV ratio (peak-trough span relative to dispersion)
def f33ec_f33_earnings_cyclicality_roicampxtrough_504d_base_v100_signal(roic):
    amp = _ec_amp(roic, 504)
    cv = _ec_cv(roic, 504)
    base = (amp + 0.05) / (cv + 0.05)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income cyclical swing (CV) over a half-year
def f33ec_f33_earnings_cyclicality_niswing_126d_base_v101_signal(netinc):
    base = _ec_cv(netinc, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cyclical swing (CV) over the full multi-year cycle
def f33ec_f33_earnings_cyclicality_ebitswing_1260d_base_v102_signal(ebit):
    base = _ec_cv(ebit, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_epsswing_504d_base_v103_signal(eps):
    base = _ec_cv(eps, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC cyclical swing (CV) over the full cycle
def f33ec_f33_earnings_cyclicality_roicswing_1260d_base_v104_signal(roic):
    base = _ec_cv(roic, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE cyclical swing (CV) over the full cycle
def f33ec_f33_earnings_cyclicality_roeswing_1260d_base_v105_signal(roe):
    base = _ec_cv(roe, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income peak-to-trough amplitude over the full cycle
def f33ec_f33_earnings_cyclicality_niamp_1260d_base_v106_signal(netinc):
    base = _ec_amp(netinc, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_ebitamp_504d_base_v107_signal(ebit):
    base = _ec_amp(ebit, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_roicamp_504d_base_v108_signal(roic):
    base = _ec_amp(roic, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_roeamp_252d_base_v109_signal(roe):
    base = _ec_amp(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_epsamp_252d_base_v110_signal(eps):
    base = _ec_amp(eps, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_nipos_504d_base_v111_signal(netinc):
    base = _ec_pos(netinc, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/equity multi-year cyclical position, half-year rotation
def f33ec_f33_earnings_cyclicality_ebitpos_1260d_base_v112_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    p = _ec_pos(r, 1260)
    base = p - p.shift(126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC position in its multi-year cyclical range
def f33ec_f33_earnings_cyclicality_roicpos_1260d_base_v113_signal(roic):
    base = _ec_pos(roic, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_roepos_252d_base_v114_signal(roe):
    base = _ec_pos(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_epspos_504d_base_v115_signal(eps):
    base = _ec_pos(eps, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income recovery off its 504d trough, percentile-ranked
def f33ec_f33_earnings_cyclicality_nitrough_504d_base_v116_signal(netinc):
    ft = _ec_fromtrough(netinc, 504)
    base = _rank(ft, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS recovery off its multi-year trough, fast-slow EMA oscillator
def f33ec_f33_earnings_cyclicality_ebittrough_1260d_base_v117_signal(eps):
    ft = _ec_fromtrough(eps, 1260)
    base = ft.ewm(span=42, min_periods=21).mean() - ft.ewm(span=189, min_periods=63).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_roictrough_504d_base_v118_signal(roic):
    base = _ec_fromtrough(roic, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_roetrough_252d_base_v119_signal(roe):
    base = _ec_fromtrough(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_epstrough_504d_base_v120_signal(eps):
    base = _ec_fromtrough(eps, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_nipeak_504d_base_v121_signal(netinc):
    base = _ec_frompeak(netinc, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown below its multi-year cyclical peak, percentile-ranked
def f33ec_f33_earnings_cyclicality_ebitpeak_1260d_base_v122_signal(roic):
    dd = _ec_frompeak(roic, 1260)
    base = _rank(dd, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_roicpeak_252d_base_v123_signal(roic):
    base = _ec_frompeak(roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_roepeak_504d_base_v124_signal(roe):
    base = _ec_frompeak(roe, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_epspeak_252d_base_v125_signal(eps):
    base = _ec_frompeak(eps, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive EPS-positive streak length
def f33ec_f33_earnings_cyclicality_epsposstreak_base_v126_signal(eps):
    base = _ec_posstreak(eps)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive ROE-positive streak length
def f33ec_f33_earnings_cyclicality_roeposstreak_base_v127_signal(roe):
    base = _ec_posstreak(roe)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years net income was positive
def f33ec_f33_earnings_cyclicality_niposfrac_504d_base_v128_signal(netinc):
    base = _ec_posfrac(netinc, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year EBIT was positive
def f33ec_f33_earnings_cyclicality_ebitposfrac_252d_base_v129_signal(ebit):
    base = _ec_posfrac(ebit, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the multi-year cycle ROIC was positive
def f33ec_f33_earnings_cyclicality_roicposfrac_1260d_base_v130_signal(roic):
    base = _ec_posfrac(roic, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net income cyclical-z mean-reversion gap vs the full multi-year cycle
def f33ec_f33_earnings_cyclicality_niz_1260d_base_v131_signal(netinc):
    zz = _z(netinc, 1260)
    base = zz - zz.ewm(span=126, min_periods=63).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_ebitz_504d_base_v132_signal(ebit):
    zz = _z(ebit, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_roicz_252d_base_v133_signal(roic):
    zz = _z(roic, 252)
    base = _rank(zz, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE cyclical-z percentile-ranked vs two-year history
def f33ec_f33_earnings_cyclicality_roez_504d_base_v134_signal(roe):
    zz = _z(roe, 504)
    base = _rank(zz, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_epsz_252d_base_v135_signal(eps):
    zz = _z(eps, 252)
    base = _rank(zz, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net income acute cyclical-z mean-reversion gap (quarter z minus its EWM)
def f33ec_f33_earnings_cyclicality_niz_63d_base_v136_signal(netinc):
    zz = _z(netinc, 63)
    base = zz - zz.ewm(span=21, min_periods=10).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level smoothed over a half-year
def f33ec_f33_earnings_cyclicality_roiclvl_126d_base_v137_signal(roic):
    base = _mean(roic, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE level smoothed over a half-year
def f33ec_f33_earnings_cyclicality_roelvl_126d_base_v138_signal(roe):
    base = _mean(roe, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-minus-ROIC spread (leverage contribution) over the year
def f33ec_f33_earnings_cyclicality_roespread_252d_base_v139_signal(roe, roic):
    base = _mean(roe - roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-on-equity (computed ROE) smoothed over the year
def f33ec_f33_earnings_cyclicality_niroe_252d_base_v140_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    base = _mean(r, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-on-equity swing (CV) over the year (operating-return cyclicality)
def f33ec_f33_earnings_cyclicality_ebitroa_252d_base_v141_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    base = _ec_cv(r, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE sign x magnitude z-scored over the year
def f33ec_f33_earnings_cyclicality_roesignmag_base_v142_signal(roe):
    sm = np.sign(roe) * np.sqrt(roe.abs())
    base = _z(sm, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income drawdown from its multi-year peak, tanh-squashed (bounded depth)
def f33ec_f33_earnings_cyclicality_niddpeak_1260d_base_v143_signal(netinc):
    peak = _rmax(netinc, 1260)
    dd = (netinc - peak) / (peak.abs() + 1e-9)
    base = np.tanh(2.5 * dd)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT drawdown from its two-year peak, tanh-squashed (bounded down-cycle depth)
def f33ec_f33_earnings_cyclicality_ebitddpeak_504d_base_v144_signal(ebit):
    peak = _rmax(ebit, 504)
    dd = (ebit - peak) / (peak.abs() + 1e-9)
    base = np.tanh(3.0 * dd)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE drawdown from its two-year peak
def f33ec_f33_earnings_cyclicality_roeddpeak_504d_base_v145_signal(roe):
    peak = _rmax(roe, 504)
    base = (roe - peak) / (peak.abs() + 1e-9)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income recovery off multi-year trough, tanh-squashed multiple
def f33ec_f33_earnings_cyclicality_nirecmult_1260d_base_v146_signal(netinc):
    trough = _rmin(netinc, 1260)
    rec = (netinc - trough) / (trough.abs() + 1e6)
    base = np.tanh(rec)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC recovery off two-year trough
def f33ec_f33_earnings_cyclicality_roicrecmult_504d_base_v147_signal(roic):
    trough = _rmin(roic, 504)
    base = (roic - trough) / (trough.abs() + 0.05)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income sign flips over two years, amplitude-weighted (cyclical instability)
def f33ec_f33_earnings_cyclicality_niflips_504d_base_v148_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    amp = _ec_amp(netinc, 504)
    base = cnt + 4.0 * amp
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS sign flips over the year, swing-weighted
def f33ec_f33_earnings_cyclicality_epsflips_252d_base_v149_signal(eps):
    flip = (np.sign(eps) != np.sign(eps.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    amp = _ec_cv(eps, 252)
    base = cnt + 10.0 * amp
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE sign flips over two years, swing-weighted
def f33ec_f33_earnings_cyclicality_roeflips_504d_base_v150_signal(roe):
    flip = (np.sign(roe) != np.sign(roe.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    cv = _ec_cv(roe, 504)
    base = cnt + 5.0 * cv
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ec_f33_earnings_cyclicality_nieqpos_1260d_base_v076_signal,
    f33ec_f33_earnings_cyclicality_nidownvol_252d_base_v077_signal,
    f33ec_f33_earnings_cyclicality_ebitupvol_252d_base_v078_signal,
    f33ec_f33_earnings_cyclicality_roicsemiskew_504d_base_v079_signal,
    f33ec_f33_earnings_cyclicality_niamprank_base_v080_signal,
    f33ec_f33_earnings_cyclicality_roicswingrank_base_v081_signal,
    f33ec_f33_earnings_cyclicality_ebitposrank_base_v082_signal,
    f33ec_f33_earnings_cyclicality_nidaysincepeak_252d_base_v083_signal,
    f33ec_f33_earnings_cyclicality_ebitdaysincetrough_504d_base_v084_signal,
    f33ec_f33_earnings_cyclicality_cyclebreadth_63d_base_v085_signal,
    f33ec_f33_earnings_cyclicality_tripleposfrac_252d_base_v086_signal,
    f33ec_f33_earnings_cyclicality_cycledivg_126d_base_v087_signal,
    f33ec_f33_earnings_cyclicality_nicumcycle_252d_base_v088_signal,
    f33ec_f33_earnings_cyclicality_ebitcumcycle_504d_base_v089_signal,
    f33ec_f33_earnings_cyclicality_niampeq_504d_base_v090_signal,
    f33ec_f33_earnings_cyclicality_ebitampeq_1260d_base_v091_signal,
    f33ec_f33_earnings_cyclicality_niphasebal_252d_base_v092_signal,
    f33ec_f33_earnings_cyclicality_ebitphasebal_504d_base_v093_signal,
    f33ec_f33_earnings_cyclicality_roephasebal_252d_base_v094_signal,
    f33ec_f33_earnings_cyclicality_roiccvdisp_252d_base_v095_signal,
    f33ec_f33_earnings_cyclicality_roeposema_252d_base_v096_signal,
    f33ec_f33_earnings_cyclicality_niposyoy_252d_base_v097_signal,
    f33ec_f33_earnings_cyclicality_ebitzyoy_504d_base_v098_signal,
    f33ec_f33_earnings_cyclicality_niampxpos_252d_base_v099_signal,
    f33ec_f33_earnings_cyclicality_roicampxtrough_504d_base_v100_signal,
    f33ec_f33_earnings_cyclicality_niswing_126d_base_v101_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_1260d_base_v102_signal,
    f33ec_f33_earnings_cyclicality_epsswing_504d_base_v103_signal,
    f33ec_f33_earnings_cyclicality_roicswing_1260d_base_v104_signal,
    f33ec_f33_earnings_cyclicality_roeswing_1260d_base_v105_signal,
    f33ec_f33_earnings_cyclicality_niamp_1260d_base_v106_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_504d_base_v107_signal,
    f33ec_f33_earnings_cyclicality_roicamp_504d_base_v108_signal,
    f33ec_f33_earnings_cyclicality_roeamp_252d_base_v109_signal,
    f33ec_f33_earnings_cyclicality_epsamp_252d_base_v110_signal,
    f33ec_f33_earnings_cyclicality_nipos_504d_base_v111_signal,
    f33ec_f33_earnings_cyclicality_ebitpos_1260d_base_v112_signal,
    f33ec_f33_earnings_cyclicality_roicpos_1260d_base_v113_signal,
    f33ec_f33_earnings_cyclicality_roepos_252d_base_v114_signal,
    f33ec_f33_earnings_cyclicality_epspos_504d_base_v115_signal,
    f33ec_f33_earnings_cyclicality_nitrough_504d_base_v116_signal,
    f33ec_f33_earnings_cyclicality_ebittrough_1260d_base_v117_signal,
    f33ec_f33_earnings_cyclicality_roictrough_504d_base_v118_signal,
    f33ec_f33_earnings_cyclicality_roetrough_252d_base_v119_signal,
    f33ec_f33_earnings_cyclicality_epstrough_504d_base_v120_signal,
    f33ec_f33_earnings_cyclicality_nipeak_504d_base_v121_signal,
    f33ec_f33_earnings_cyclicality_ebitpeak_1260d_base_v122_signal,
    f33ec_f33_earnings_cyclicality_roicpeak_252d_base_v123_signal,
    f33ec_f33_earnings_cyclicality_roepeak_504d_base_v124_signal,
    f33ec_f33_earnings_cyclicality_epspeak_252d_base_v125_signal,
    f33ec_f33_earnings_cyclicality_epsposstreak_base_v126_signal,
    f33ec_f33_earnings_cyclicality_roeposstreak_base_v127_signal,
    f33ec_f33_earnings_cyclicality_niposfrac_504d_base_v128_signal,
    f33ec_f33_earnings_cyclicality_ebitposfrac_252d_base_v129_signal,
    f33ec_f33_earnings_cyclicality_roicposfrac_1260d_base_v130_signal,
    f33ec_f33_earnings_cyclicality_niz_1260d_base_v131_signal,
    f33ec_f33_earnings_cyclicality_ebitz_504d_base_v132_signal,
    f33ec_f33_earnings_cyclicality_roicz_252d_base_v133_signal,
    f33ec_f33_earnings_cyclicality_roez_504d_base_v134_signal,
    f33ec_f33_earnings_cyclicality_epsz_252d_base_v135_signal,
    f33ec_f33_earnings_cyclicality_niz_63d_base_v136_signal,
    f33ec_f33_earnings_cyclicality_roiclvl_126d_base_v137_signal,
    f33ec_f33_earnings_cyclicality_roelvl_126d_base_v138_signal,
    f33ec_f33_earnings_cyclicality_roespread_252d_base_v139_signal,
    f33ec_f33_earnings_cyclicality_niroe_252d_base_v140_signal,
    f33ec_f33_earnings_cyclicality_ebitroa_252d_base_v141_signal,
    f33ec_f33_earnings_cyclicality_roesignmag_base_v142_signal,
    f33ec_f33_earnings_cyclicality_niddpeak_1260d_base_v143_signal,
    f33ec_f33_earnings_cyclicality_ebitddpeak_504d_base_v144_signal,
    f33ec_f33_earnings_cyclicality_roeddpeak_504d_base_v145_signal,
    f33ec_f33_earnings_cyclicality_nirecmult_1260d_base_v146_signal,
    f33ec_f33_earnings_cyclicality_roicrecmult_504d_base_v147_signal,
    f33ec_f33_earnings_cyclicality_niflips_504d_base_v148_signal,
    f33ec_f33_earnings_cyclicality_epsflips_252d_base_v149_signal,
    f33ec_f33_earnings_cyclicality_roeflips_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EARNINGS_CYCLICALITY_REGISTRY_076_150 = REGISTRY


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

    # Cyclical miners: profitability flows GENUINELY swing across zero through the
    # commodity cycle so amplitude / trough-distance / positive-streak / cyclical-z
    # features vary over time. Each flow = a zero-mean cyclical _fund center
    # (allow_neg) + a multi-quarter sine (the boom-bust cycle) + a second _fund
    # noise draw, all centered so the sign flips through the cycle. Equity is a
    # strictly-positive scale base (no allow_neg).
    def _swing(seed, seed2, base, vol, amp, period):
        raw = _fund(seed, base=base, vol=vol, allow_neg=True)
        center = raw - raw.rolling(252, min_periods=1).mean()
        t = np.arange(n)
        wob = amp * base * np.sin(2.0 * np.pi * t / period)
        nz = _fund(seed2, base=base, vol=vol, allow_neg=True)
        nz = (nz - nz.rolling(252, min_periods=1).mean()) * 0.5
        return center + wob + nz

    netinc = _swing(3301, 3311, 5.0e7, 0.30, 0.55, 130).rename("netinc")
    eps = _swing(3302, 3312, 2.5, 0.32, 0.55, 115).rename("eps")
    ebit = _swing(3303, 3313, 6.0e7, 0.28, 0.55, 150).rename("ebit")
    roic = _swing(3304, 3314, 0.12, 0.34, 0.60, 95).rename("roic")
    roe = _swing(3305, 3315, 0.14, 0.33, 0.60, 105).rename("roe")
    equity = _fund(3306, base=4.0e8, drift=0.01, vol=0.10, allow_neg=False).rename("equity")

    cols = {"netinc": netinc, "eps": eps, "ebit": ebit,
            "roic": roic, "roe": roe, "equity": equity}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("netinc", "eps", "ebit", "roic", "roe", "equity")
                   for c in meta["inputs"]), name
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

    print("OK f33_earnings_cyclicality_base_076_150_claude: %d features pass" % n_features)
