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
# 2nd derivative (31d jerk) of: net-income cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_niswing_31d_jerk_v001_signal(netinc):
    base = _ec_cv(netinc, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_niswing_42d_jerk_v002_signal(netinc):
    base = _ec_cv(netinc, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: net-income cyclical swing (CV) over the full multi-year cycle
def f33ec_f33_earnings_cyclicality_niswing_105d_jerk_v003_signal(netinc):
    base = _ec_cv(netinc, 1260)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_ebitswing_42d_jerk_v004_signal(ebit):
    base = _ec_cv(ebit, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_ebitswing_52d_jerk_v005_signal(ebit):
    base = _ec_cv(ebit, 504)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EPS cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_epsswing_21d_jerk_v006_signal(eps):
    base = _ec_cv(eps, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_roicswing_63d_jerk_v007_signal(roic):
    base = _ec_cv(roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_roeswing_42d_jerk_v008_signal(roe):
    base = _ec_cv(roe, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: ROIC cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_roicswing_52d_jerk_v009_signal(roic):
    base = _ec_cv(roic, 504)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_roeswing_42d_jerk_v010_signal(roe):
    base = _ec_cv(roe, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_niamp_63d_jerk_v011_signal(netinc):
    base = _ec_amp(netinc, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_niamp_63d_jerk_v012_signal(netinc):
    base = _ec_amp(netinc, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EBIT peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_ebitamp_31d_jerk_v013_signal(ebit):
    base = _ec_amp(ebit, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT peak-to-trough amplitude over the full cycle
def f33ec_f33_earnings_cyclicality_ebitamp_52d_jerk_v014_signal(ebit):
    base = _ec_amp(ebit, 1260)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_roicamp_63d_jerk_v015_signal(roic):
    base = _ec_amp(roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_roeamp_63d_jerk_v016_signal(roe):
    base = _ec_amp(roe, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EPS peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_epsamp_52d_jerk_v017_signal(eps):
    base = _ec_amp(eps, 504)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: net-income position in its 252d cyclical range (0=trough,1=peak)
def f33ec_f33_earnings_cyclicality_nipos_21d_jerk_v018_signal(netinc):
    base = _ec_pos(netinc, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: net-income position in its multi-year cyclical range
def f33ec_f33_earnings_cyclicality_nipos_105d_jerk_v019_signal(netinc):
    base = _ec_pos(netinc, 1260)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EBIT cyclical position fast-minus-slow EMA oscillator
def f33ec_f33_earnings_cyclicality_ebitpos_63d_jerk_v020_signal(ebit):
    p = _ec_pos(ebit, 504)
    base = p.ewm(span=21, min_periods=10).mean() - p.ewm(span=84, min_periods=42).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: ROIC position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_roicpos_31d_jerk_v021_signal(roic):
    base = _ec_pos(roic, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_roepos_42d_jerk_v022_signal(roe):
    base = _ec_pos(roe, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EPS position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_epspos_63d_jerk_v023_signal(eps):
    base = _ec_pos(eps, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_nitrough_42d_jerk_v024_signal(netinc):
    base = _ec_fromtrough(netinc, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income recovery off multi-year trough, displacement vs slow EWM
def f33ec_f33_earnings_cyclicality_nitrough_63d_jerk_v025_signal(netinc):
    ft = _ec_fromtrough(netinc, 1260)
    base = ft - ft.ewm(span=189, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT-minus-netinc accrual spread recovery off its 504d trough, EWM displacement
def f33ec_f33_earnings_cyclicality_ebittrough_42d_jerk_v026_signal(ebit, netinc):
    spr = ebit - netinc
    ft = _ec_fromtrough(spr, 504)
    base = ft - ft.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_roictrough_63d_jerk_v027_signal(roic):
    base = _ec_fromtrough(roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_roetrough_63d_jerk_v028_signal(roe):
    base = _ec_fromtrough(roe, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: net-income distance below its 252d cyclical peak (down-cycle depth)
def f33ec_f33_earnings_cyclicality_nipeak_31d_jerk_v029_signal(netinc):
    base = _ec_frompeak(netinc, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_ebitpeak_42d_jerk_v030_signal(ebit):
    base = _ec_frompeak(ebit, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: ROIC distance below its multi-year cyclical peak
def f33ec_f33_earnings_cyclicality_roicpeak_105d_jerk_v031_signal(roic):
    base = _ec_frompeak(roic, 1260)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_roepeak_42d_jerk_v032_signal(roe):
    base = _ec_frompeak(roe, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: consecutive net-income-positive streak length (up-phase durability)
def f33ec_f33_earnings_cyclicality_niposstreak_31d_jerk_v033_signal(netinc):
    base = _ec_posstreak(netinc)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: consecutive EBIT-positive streak length
def f33ec_f33_earnings_cyclicality_ebitposstreak_21d_jerk_v034_signal(ebit):
    base = _ec_posstreak(ebit)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: consecutive ROIC-positive streak length
def f33ec_f33_earnings_cyclicality_roicposstreak_63d_jerk_v035_signal(roic):
    base = _ec_posstreak(roic)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: fraction of the year net income was positive (up-phase persistence)
def f33ec_f33_earnings_cyclicality_niposfrac_42d_jerk_v036_signal(netinc):
    base = _ec_posfrac(netinc, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: fraction of two years EBIT was positive, half-year change (up-phase rotation)
def f33ec_f33_earnings_cyclicality_ebitposfrac_52d_jerk_v037_signal(ebit):
    frac = _ec_posfrac(ebit, 504)
    base = frac - frac.shift(126)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: fraction of the year ROE was positive
def f33ec_f33_earnings_cyclicality_roeposfrac_21d_jerk_v038_signal(roe):
    base = _ec_posfrac(roe, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: fraction of the multi-year cycle EPS was positive
def f33ec_f33_earnings_cyclicality_epsposfrac_105d_jerk_v039_signal(eps):
    base = _ec_posfrac(eps, 1260)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net income cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_niz_42d_jerk_v040_signal(netinc):
    zz = _z(netinc, 252)
    base = zz - zz.ewm(span=63, min_periods=21).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: net income cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_niz_52d_jerk_v041_signal(netinc):
    zz = _z(netinc, 504)
    base = _rank(zz, 252)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EBIT-minus-netinc accrual spread cyclical-z mean-reversion gap
def f33ec_f33_earnings_cyclicality_ebitz_21d_jerk_v042_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 252)
    base = zz - zz.ewm(span=42, min_periods=21).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: ROIC cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_roicz_84d_jerk_v043_signal(roic):
    zz = _z(roic, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_roez_42d_jerk_v044_signal(roe):
    zz = _z(roe, 252)
    base = zz - zz.ewm(span=63, min_periods=31).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EPS cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_epsz_52d_jerk_v045_signal(eps):
    zz = _z(eps, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT-minus-netinc accrual spread cyclical-z year-over-year change
def f33ec_f33_earnings_cyclicality_ebitz_52d_jerk_v046_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 1260)
    base = zz - zz.shift(252)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (26d jerk) of: ROIC level smoothed over a quarter (current return-on-capital)
def f33ec_f33_earnings_cyclicality_roiclvl_26d_jerk_v047_signal(roic):
    base = _mean(roic, 63)
    result = _jerk(base, 26)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROE level smoothed over a quarter
def f33ec_f33_earnings_cyclicality_roelvl_21d_jerk_v048_signal(roe):
    base = _mean(roe, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROE-minus-ROIC spread (leverage contribution) over a half-year
def f33ec_f33_earnings_cyclicality_roespread_21d_jerk_v049_signal(roe, roic):
    base = _mean(roe - roic, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (13d jerk) of: net-income-on-equity (computed ROE) smoothed over a half-year
def f33ec_f33_earnings_cyclicality_niroe_13d_jerk_v050_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    base = _mean(r, 126)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT-on-equity cyclical position over a half-year (operating-return phase)
def f33ec_f33_earnings_cyclicality_ebitroe_42d_jerk_v051_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    base = _ec_pos(r, 126)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income sign x magnitude de-trended vs year (swing intensity)
def f33ec_f33_earnings_cyclicality_nisignmag_42d_jerk_v052_signal(netinc):
    sm = _ec_signmag(netinc, 1e6)
    base = sm - sm.rolling(252, min_periods=126).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EBIT-minus-netinc accrual spread sign x magnitude, quarterly momentum
def f33ec_f33_earnings_cyclicality_ebitsignmag_31d_jerk_v053_signal(ebit, netinc):
    spr = ebit - netinc
    sm = _ec_signmag(spr, 1e6)
    base = sm - sm.shift(63)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EPS sign x magnitude de-trended vs year
def f33ec_f33_earnings_cyclicality_epssignmag_21d_jerk_v054_signal(eps):
    sm = _ec_signmag(eps, 1.0)
    base = sm - sm.rolling(252, min_periods=126).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC sign x magnitude z-scored over two years
def f33ec_f33_earnings_cyclicality_roicsignmag_63d_jerk_v055_signal(roic):
    sm = np.sign(roic) * np.sqrt(roic.abs())
    base = _z(sm, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income drawdown from its two-year peak (earnings down-cycle)
def f33ec_f33_earnings_cyclicality_niddpeak_63d_jerk_v056_signal(netinc):
    peak = _rmax(netinc, 504)
    base = (netinc - peak) / (peak.abs() + 1e-9)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EBIT-minus-netinc accrual spread drawdown from its multi-year peak
def f33ec_f33_earnings_cyclicality_ebitddpeak_63d_jerk_v057_signal(ebit, netinc):
    spr = ebit - netinc
    peak = _rmax(spr, 1260)
    base = (spr - peak) / (peak.abs() + 1e6)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROIC drawdown from its two-year peak, percentile-ranked
def f33ec_f33_earnings_cyclicality_roicddpeak_42d_jerk_v058_signal(roic):
    peak = _rmax(roic, 504)
    dd = (roic - peak) / (peak.abs() + 1e-9)
    base = _rank(dd, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: net-income recovery off two-year trough, quarterly momentum of the multiple
def f33ec_f33_earnings_cyclicality_nirecmult_84d_jerk_v059_signal(netinc):
    trough = _rmin(netinc, 504)
    rec = (netinc - trough) / (trough.abs() + 1e6)
    base = rec - rec.shift(63)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EBIT recovery off multi-year trough, percentile-ranked multiple
def f33ec_f33_earnings_cyclicality_ebitrecmult_84d_jerk_v060_signal(ebit):
    trough = _rmin(ebit, 1260)
    rec = (ebit - trough) / (trough.abs() + 1e6)
    base = _rank(rec, 504)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: net-income sign flips over the year, swing-weighted (cyclical instability)
def f33ec_f33_earnings_cyclicality_niflips_31d_jerk_v061_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    sd = netinc.rolling(63, min_periods=21).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    base = cnt + 30.0 * sd / (lvl + 1e6)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT sign flips over two years, amplitude-weighted
def f33ec_f33_earnings_cyclicality_ebitflips_42d_jerk_v062_signal(ebit):
    flip = (np.sign(ebit) != np.sign(ebit.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    amp = _ec_amp(ebit, 252)
    base = cnt + 5.0 * amp
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC sign flips over the year, amplitude-weighted (return-on-capital instability)
def f33ec_f33_earnings_cyclicality_roicflips_63d_jerk_v063_signal(roic):
    flip = (np.sign(roic) != np.sign(roic.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    amp = _ec_amp(roic, 252)
    base = cnt + 3.0 * amp
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income swing term structure: acute 63d minus chronic 504d
def f33ec_f33_earnings_cyclicality_niampterm_42d_jerk_v064_signal(netinc):
    s = _ec_cv(netinc, 63)
    l = _ec_cv(netinc, 504)
    base = s - l
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EBIT amplitude term structure: half-year vs full cycle
def f33ec_f33_earnings_cyclicality_ebitampterm_31d_jerk_v065_signal(ebit):
    s = _ec_amp(ebit, 126)
    l = _ec_amp(ebit, 1260)
    base = s - l
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROIC swing ratio: half-year vs two-year (worsening volatility regime)
def f33ec_f33_earnings_cyclicality_roicampterm_21d_jerk_v066_signal(roic):
    s = _ec_cv(roic, 126)
    l = _ec_cv(roic, 504)
    base = (s + 0.05) / (l + 0.05) - 1.0
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: net-income full cyclical span (peak-trough gap), log-compressed
def f33ec_f33_earnings_cyclicality_nicycspan_84d_jerk_v067_signal(netinc):
    hi = _rmax(netinc, 504)
    lo = _rmin(netinc, 504)
    base = np.log1p((hi - lo).abs() / 1e6)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EBIT multi-year cyclical span, log-compressed
def f33ec_f33_earnings_cyclicality_ebitcycspan_84d_jerk_v068_signal(ebit):
    hi = _rmax(ebit, 1260)
    lo = _rmin(ebit, 1260)
    base = np.log1p((hi - lo).abs() / 1e6)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: crossings into profitability over the year, trough-distance-weighted (recovery frequency)
def f33ec_f33_earnings_cyclicality_poscross_31d_jerk_v069_signal(netinc):
    pos = _ec_pospos(netinc)
    entries = ((pos == 1) & (pos.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = _ec_fromtrough(netinc, 252)
    base = cnt + 2.0 * depth
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: net-income yearly change normalized by dispersion (cyclical direction)
def f33ec_f33_earnings_cyclicality_nitrend_21d_jerk_v070_signal(netinc):
    sl = (netinc - netinc.shift(252))
    disp = netinc.rolling(252, min_periods=126).std()
    base = sl / disp.replace(0, np.nan)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC yearly change normalized by dispersion
def f33ec_f33_earnings_cyclicality_roictrend_63d_jerk_v071_signal(roic):
    sl = (roic - roic.shift(252))
    disp = roic.rolling(252, min_periods=126).std()
    base = sl / disp.replace(0, np.nan)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EPS half-year change normalized by dispersion
def f33ec_f33_earnings_cyclicality_epstrend_31d_jerk_v072_signal(eps):
    sl = (eps - eps.shift(126))
    disp = eps.rolling(126, min_periods=63).std()
    base = sl / disp.replace(0, np.nan)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: net-income/equity (ROE) swing percentile-ranked (capital-return cyclicality)
def f33ec_f33_earnings_cyclicality_nieqswing_31d_jerk_v073_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    cv = _ec_cv(r, 252)
    base = _rank(cv, 504)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT/equity amplitude displacement vs its slow EWM over two years
def f33ec_f33_earnings_cyclicality_ebiteqswing_42d_jerk_v074_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    amp = _ec_amp(r, 504)
    base = amp - amp.ewm(span=252, min_periods=126).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: net-income/equity cyclical-z half-year change (computed-ROE z momentum)
def f33ec_f33_earnings_cyclicality_nieqz_84d_jerk_v075_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    zz = _z(r, 504)
    base = zz - zz.shift(126)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: net-income/equity multi-year cyclical position, half-year rotation
def f33ec_f33_earnings_cyclicality_nieqpos_84d_jerk_v076_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    p = _ec_pos(r, 1260)
    base = p - p.shift(126)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: net-income downside semi-deviation (down-cycle earnings vol)
def f33ec_f33_earnings_cyclicality_nidownvol_31d_jerk_v077_signal(netinc):
    d = (netinc - _mean(netinc, 252))
    neg = d.clip(upper=0.0)
    base = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean()) / (netinc.abs().rolling(252, min_periods=126).mean() + 1e6)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EBIT upside semi-deviation (up-cycle earnings vol)
def f33ec_f33_earnings_cyclicality_ebitupvol_21d_jerk_v078_signal(ebit):
    d = (ebit - _mean(ebit, 252))
    posd = d.clip(lower=0.0)
    base = np.sqrt((posd ** 2).rolling(252, min_periods=126).mean()) / (ebit.abs().rolling(252, min_periods=126).mean() + 1e6)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: ROIC vol asymmetry: upside minus downside semi-dev (cycle skew)
def f33ec_f33_earnings_cyclicality_roicsemiskew_84d_jerk_v079_signal(roic):
    d = (roic - _mean(roic, 504))
    up = np.sqrt((d.clip(lower=0.0) ** 2).rolling(504, min_periods=252).mean())
    dn = np.sqrt((d.clip(upper=0.0) ** 2).rolling(504, min_periods=252).mean())
    base = (up - dn) / (up + dn + 1e-9)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income amplitude percentile-ranked vs its own two-year history
def f33ec_f33_earnings_cyclicality_niamprank_42d_jerk_v080_signal(netinc):
    amp = _ec_amp(netinc, 252)
    base = _rank(amp, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: ROIC swing percentile-ranked vs its own two-year history
def f33ec_f33_earnings_cyclicality_roicswingrank_31d_jerk_v081_signal(roic):
    cv = _ec_cv(roic, 252)
    base = _rank(cv, 504)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EBIT/equity cyclical position percentile-ranked vs multi-year history
def f33ec_f33_earnings_cyclicality_ebitposrank_21d_jerk_v082_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    p = _ec_pos(r, 504)
    base = _rank(p, 1260)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income days-since-cyclical-peak (staleness of the earnings high)
def f33ec_f33_earnings_cyclicality_nidaysincepeak_63d_jerk_v083_signal(netinc):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    base = netinc.rolling(252, min_periods=126).apply(_f, raw=True)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EBIT days-since-cyclical-trough (time recovering off the bottom)
def f33ec_f33_earnings_cyclicality_ebitdaysincetrough_63d_jerk_v084_signal(ebit):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    base = ebit.rolling(504, min_periods=252).apply(_f, raw=True)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (13d jerk) of: how many of {netinc,ebit,roic} are positive (cycle up-phase breadth)
def f33ec_f33_earnings_cyclicality_cyclebreadth_13d_jerk_v085_signal(netinc, ebit, roic):
    raw = _ec_pospos(netinc) + _ec_pospos(ebit) + _ec_pospos(roic)
    base = raw.rolling(63, min_periods=21).mean()
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: fraction of year all three profit metrics positive, quarterly change (cycle phase rotation)
def f33ec_f33_earnings_cyclicality_tripleposfrac_21d_jerk_v086_signal(netinc, ebit, roe):
    triple = ((netinc > 0) & (ebit > 0) & (roe > 0)).astype(float)
    frac = triple.rolling(252, min_periods=126).mean()
    base = frac - frac.shift(63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-loss-while-operating-profit divergence (below-line cyclical drag)
def f33ec_f33_earnings_cyclicality_cycledivg_42d_jerk_v087_signal(netinc, ebit):
    div = ((netinc < 0) & (ebit > 0)).astype(float)
    base = div.rolling(126, min_periods=63).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income cumulative cyclical earnings, quarterly momentum
def f33ec_f33_earnings_cyclicality_nicumcycle_42d_jerk_v088_signal(netinc):
    sm = _ec_signmag(netinc, 1e6)
    cum = sm.rolling(252, min_periods=126).sum() / 252.0
    base = cum - cum.shift(63)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT cumulative cyclical earnings z-scored over the year
def f33ec_f33_earnings_cyclicality_ebitcumcycle_52d_jerk_v089_signal(ebit):
    sm = _ec_signmag(ebit, 1e6)
    cum = sm.rolling(504, min_periods=252).sum() / 504.0
    base = _z(cum, 252)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income peak-trough amplitude scaled by equity base (cycle severity)
def f33ec_f33_earnings_cyclicality_niampeq_42d_jerk_v090_signal(netinc, equity):
    hi = _rmax(netinc, 504)
    lo = _rmin(netinc, 504)
    base = (hi - lo) / (equity.replace(0, np.nan).abs() + 1e6)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: EBIT multi-year amplitude scaled by equity base
def f33ec_f33_earnings_cyclicality_ebitampeq_105d_jerk_v091_signal(ebit, equity):
    hi = _rmax(ebit, 1260)
    lo = _rmin(ebit, 1260)
    base = (hi - lo) / (equity.replace(0, np.nan).abs() + 1e6)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income up vs down phase balance, percentile-ranked over two years
def f33ec_f33_earnings_cyclicality_niphasebal_42d_jerk_v092_signal(netinc):
    profw = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    lossw = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    bal = (profw - lossw) / (profw + lossw + 1e6)
    base = _rank(bal, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT up-phase vs down-phase magnitude balance over two years
def f33ec_f33_earnings_cyclicality_ebitphasebal_52d_jerk_v093_signal(ebit):
    profw = ebit.clip(lower=0.0).rolling(504, min_periods=252).sum()
    lossw = (-ebit).clip(lower=0.0).rolling(504, min_periods=252).sum()
    base = (profw - lossw) / (profw + lossw + 1e6)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROE up-phase vs down-phase magnitude balance over the year
def f33ec_f33_earnings_cyclicality_roephasebal_21d_jerk_v094_signal(roe):
    profw = roe.clip(lower=0.0).rolling(252, min_periods=126).sum()
    lossw = (-roe).clip(lower=0.0).rolling(252, min_periods=126).sum()
    base = (profw - lossw) / (profw + lossw + 1e-9)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC swing displacement vs its own slow EWM (swing regime shift)
def f33ec_f33_earnings_cyclicality_roiccvdisp_63d_jerk_v095_signal(roic):
    cv = _ec_cv(roic, 252)
    base = cv - cv.ewm(span=126, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE-minus-ROIC spread cyclical position fast-slow EMA oscillator (leverage-phase)
def f33ec_f33_earnings_cyclicality_roeposema_42d_jerk_v096_signal(roe, roic):
    spr = roe - roic
    p = _ec_pos(spr, 252)
    base = p.ewm(span=21, min_periods=10).mean() - p.ewm(span=84, min_periods=42).mean()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: net-income cyclical position year-over-year change (phase rotation)
def f33ec_f33_earnings_cyclicality_niposyoy_31d_jerk_v097_signal(netinc):
    p = _ec_pos(netinc, 252)
    base = p - p.shift(252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: EBIT-minus-netinc accrual spread cyclical-z year-over-year change
def f33ec_f33_earnings_cyclicality_ebitzyoy_42d_jerk_v098_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 504)
    base = zz - zz.shift(252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income swing relative to EBIT swing (below-line amplification ratio)
def f33ec_f33_earnings_cyclicality_niampxpos_63d_jerk_v099_signal(netinc, ebit):
    amp = _ec_cv(netinc, 252)
    opamp = _ec_cv(ebit, 252)
    base = (amp + 0.05) / (opamp + 0.05)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC amplitude-to-CV ratio (peak-trough span relative to dispersion)
def f33ec_f33_earnings_cyclicality_roicampxtrough_63d_jerk_v100_signal(roic):
    amp = _ec_amp(roic, 504)
    cv = _ec_cv(roic, 504)
    base = (amp + 0.05) / (cv + 0.05)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: net-income cyclical swing (CV) over a half-year
def f33ec_f33_earnings_cyclicality_niswing_21d_jerk_v101_signal(netinc):
    base = _ec_cv(netinc, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: EBIT cyclical swing (CV) over the full multi-year cycle
def f33ec_f33_earnings_cyclicality_ebitswing_52d_jerk_v102_signal(ebit):
    base = _ec_cv(ebit, 1260)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EPS cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_epsswing_84d_jerk_v103_signal(eps):
    base = _ec_cv(eps, 504)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: ROIC cyclical swing (CV) over the full cycle
def f33ec_f33_earnings_cyclicality_roicswing_84d_jerk_v104_signal(roic):
    base = _ec_cv(roic, 1260)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE cyclical swing (CV) over the full cycle
def f33ec_f33_earnings_cyclicality_roeswing_63d_jerk_v105_signal(roe):
    base = _ec_cv(roe, 1260)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: net-income peak-to-trough amplitude over the full cycle
def f33ec_f33_earnings_cyclicality_niamp_52d_jerk_v106_signal(netinc):
    base = _ec_amp(netinc, 1260)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EBIT peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_ebitamp_84d_jerk_v107_signal(ebit):
    base = _ec_amp(ebit, 504)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_roicamp_63d_jerk_v108_signal(roic):
    base = _ec_amp(roic, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: ROE peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_roeamp_31d_jerk_v109_signal(roe):
    base = _ec_amp(roe, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: EPS peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_epsamp_21d_jerk_v110_signal(eps):
    base = _ec_amp(eps, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: net-income position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_nipos_84d_jerk_v111_signal(netinc):
    base = _ec_pos(netinc, 504)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EBIT/equity multi-year cyclical position, half-year rotation
def f33ec_f33_earnings_cyclicality_ebitpos_84d_jerk_v112_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    p = _ec_pos(r, 1260)
    base = p - p.shift(126)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC position in its multi-year cyclical range
def f33ec_f33_earnings_cyclicality_roicpos_63d_jerk_v113_signal(roic):
    base = _ec_pos(roic, 1260)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROE position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_roepos_21d_jerk_v114_signal(roe):
    base = _ec_pos(roe, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: EPS position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_epspos_84d_jerk_v115_signal(eps):
    base = _ec_pos(eps, 504)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income recovery off its 504d trough, percentile-ranked
def f33ec_f33_earnings_cyclicality_nitrough_63d_jerk_v116_signal(netinc):
    ft = _ec_fromtrough(netinc, 504)
    base = _rank(ft, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EPS recovery off its multi-year trough, fast-slow EMA oscillator
def f33ec_f33_earnings_cyclicality_ebittrough_63d_jerk_v117_signal(eps):
    ft = _ec_fromtrough(eps, 1260)
    base = ft.ewm(span=42, min_periods=21).mean() - ft.ewm(span=189, min_periods=63).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROIC distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_roictrough_42d_jerk_v118_signal(roic):
    base = _ec_fromtrough(roic, 504)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_roetrough_63d_jerk_v119_signal(roe):
    base = _ec_fromtrough(roe, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EPS distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_epstrough_63d_jerk_v120_signal(eps):
    base = _ec_fromtrough(eps, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: net-income distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_nipeak_52d_jerk_v121_signal(netinc):
    base = _ec_frompeak(netinc, 504)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: ROIC drawdown below its multi-year cyclical peak, percentile-ranked
def f33ec_f33_earnings_cyclicality_ebitpeak_52d_jerk_v122_signal(roic):
    dd = _ec_frompeak(roic, 1260)
    base = _rank(dd, 504)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROIC distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_roicpeak_63d_jerk_v123_signal(roic):
    base = _ec_frompeak(roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_roepeak_63d_jerk_v124_signal(roe):
    base = _ec_frompeak(roe, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EPS distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_epspeak_31d_jerk_v125_signal(eps):
    base = _ec_frompeak(eps, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: consecutive EPS-positive streak length
def f33ec_f33_earnings_cyclicality_epsposstreak_21d_jerk_v126_signal(eps):
    base = _ec_posstreak(eps)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: consecutive ROE-positive streak length
def f33ec_f33_earnings_cyclicality_roeposstreak_63d_jerk_v127_signal(roe):
    base = _ec_posstreak(roe)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: fraction of two years net income was positive
def f33ec_f33_earnings_cyclicality_niposfrac_63d_jerk_v128_signal(netinc):
    base = _ec_posfrac(netinc, 504)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: fraction of the year EBIT was positive
def f33ec_f33_earnings_cyclicality_ebitposfrac_31d_jerk_v129_signal(ebit):
    base = _ec_posfrac(ebit, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: fraction of the multi-year cycle ROIC was positive
def f33ec_f33_earnings_cyclicality_roicposfrac_52d_jerk_v130_signal(roic):
    base = _ec_posfrac(roic, 1260)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: net income cyclical-z mean-reversion gap vs the full multi-year cycle
def f33ec_f33_earnings_cyclicality_niz_105d_jerk_v131_signal(netinc):
    zz = _z(netinc, 1260)
    base = zz - zz.ewm(span=126, min_periods=63).mean()
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EBIT cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_ebitz_63d_jerk_v132_signal(ebit):
    zz = _z(ebit, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: ROIC cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_roicz_31d_jerk_v133_signal(roic):
    zz = _z(roic, 252)
    base = _rank(zz, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE cyclical-z percentile-ranked vs two-year history
def f33ec_f33_earnings_cyclicality_roez_42d_jerk_v134_signal(roe):
    zz = _z(roe, 504)
    base = _rank(zz, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EPS cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_epsz_63d_jerk_v135_signal(eps):
    zz = _z(eps, 252)
    base = _rank(zz, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: net income acute cyclical-z mean-reversion gap (quarter z minus its EWM)
def f33ec_f33_earnings_cyclicality_niz_21d_jerk_v136_signal(netinc):
    zz = _z(netinc, 63)
    base = zz - zz.ewm(span=21, min_periods=10).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROIC level smoothed over a half-year
def f33ec_f33_earnings_cyclicality_roiclvl_21d_jerk_v137_signal(roic):
    base = _mean(roic, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (13d jerk) of: ROE level smoothed over a half-year
def f33ec_f33_earnings_cyclicality_roelvl_13d_jerk_v138_signal(roe):
    base = _mean(roe, 126)
    result = _jerk(base, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: ROE-minus-ROIC spread (leverage contribution) over the year
def f33ec_f33_earnings_cyclicality_roespread_63d_jerk_v139_signal(roe, roic):
    base = _mean(roe - roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: net-income-on-equity (computed ROE) smoothed over the year
def f33ec_f33_earnings_cyclicality_niroe_42d_jerk_v140_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    base = _mean(r, 252)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EBIT-on-equity swing (CV) over the year (operating-return cyclicality)
def f33ec_f33_earnings_cyclicality_ebitroa_31d_jerk_v141_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    base = _ec_cv(r, 252)
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (21d jerk) of: ROE sign x magnitude z-scored over the year
def f33ec_f33_earnings_cyclicality_roesignmag_21d_jerk_v142_signal(roe):
    sm = np.sign(roe) * np.sqrt(roe.abs())
    base = _z(sm, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (105d jerk) of: net-income drawdown from its multi-year peak, tanh-squashed (bounded depth)
def f33ec_f33_earnings_cyclicality_niddpeak_105d_jerk_v143_signal(netinc):
    peak = _rmax(netinc, 1260)
    dd = (netinc - peak) / (peak.abs() + 1e-9)
    base = np.tanh(2.5 * dd)
    result = _jerk(base, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: EBIT drawdown from its two-year peak, tanh-squashed (bounded down-cycle depth)
def f33ec_f33_earnings_cyclicality_ebitddpeak_63d_jerk_v144_signal(ebit):
    peak = _rmax(ebit, 504)
    dd = (ebit - peak) / (peak.abs() + 1e-9)
    base = np.tanh(3.0 * dd)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: ROE drawdown from its two-year peak
def f33ec_f33_earnings_cyclicality_roeddpeak_52d_jerk_v145_signal(roe):
    peak = _rmax(roe, 504)
    base = (roe - peak) / (peak.abs() + 1e-9)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (52d jerk) of: net-income recovery off multi-year trough, tanh-squashed multiple
def f33ec_f33_earnings_cyclicality_nirecmult_52d_jerk_v146_signal(netinc):
    trough = _rmin(netinc, 1260)
    rec = (netinc - trough) / (trough.abs() + 1e6)
    base = np.tanh(rec)
    result = _jerk(base, 52)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (84d jerk) of: ROIC recovery off two-year trough
def f33ec_f33_earnings_cyclicality_roicrecmult_84d_jerk_v147_signal(roic):
    trough = _rmin(roic, 504)
    base = (roic - trough) / (trough.abs() + 0.05)
    result = _jerk(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (63d jerk) of: net-income sign flips over two years, amplitude-weighted (cyclical instability)
def f33ec_f33_earnings_cyclicality_niflips_63d_jerk_v148_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    amp = _ec_amp(netinc, 504)
    base = cnt + 4.0 * amp
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (31d jerk) of: EPS sign flips over the year, swing-weighted
def f33ec_f33_earnings_cyclicality_epsflips_31d_jerk_v149_signal(eps):
    flip = (np.sign(eps) != np.sign(eps.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    amp = _ec_cv(eps, 252)
    base = cnt + 10.0 * amp
    result = _jerk(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 2nd derivative (42d jerk) of: ROE sign flips over two years, swing-weighted
def f33ec_f33_earnings_cyclicality_roeflips_42d_jerk_v150_signal(roe):
    flip = (np.sign(roe) != np.sign(roe.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    cv = _ec_cv(roe, 504)
    base = cnt + 5.0 * cv
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ec_f33_earnings_cyclicality_niswing_31d_jerk_v001_signal,
    f33ec_f33_earnings_cyclicality_niswing_42d_jerk_v002_signal,
    f33ec_f33_earnings_cyclicality_niswing_105d_jerk_v003_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_42d_jerk_v004_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_52d_jerk_v005_signal,
    f33ec_f33_earnings_cyclicality_epsswing_21d_jerk_v006_signal,
    f33ec_f33_earnings_cyclicality_roicswing_63d_jerk_v007_signal,
    f33ec_f33_earnings_cyclicality_roeswing_42d_jerk_v008_signal,
    f33ec_f33_earnings_cyclicality_roicswing_52d_jerk_v009_signal,
    f33ec_f33_earnings_cyclicality_roeswing_42d_jerk_v010_signal,
    f33ec_f33_earnings_cyclicality_niamp_63d_jerk_v011_signal,
    f33ec_f33_earnings_cyclicality_niamp_63d_jerk_v012_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_31d_jerk_v013_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_52d_jerk_v014_signal,
    f33ec_f33_earnings_cyclicality_roicamp_63d_jerk_v015_signal,
    f33ec_f33_earnings_cyclicality_roeamp_63d_jerk_v016_signal,
    f33ec_f33_earnings_cyclicality_epsamp_52d_jerk_v017_signal,
    f33ec_f33_earnings_cyclicality_nipos_21d_jerk_v018_signal,
    f33ec_f33_earnings_cyclicality_nipos_105d_jerk_v019_signal,
    f33ec_f33_earnings_cyclicality_ebitpos_63d_jerk_v020_signal,
    f33ec_f33_earnings_cyclicality_roicpos_31d_jerk_v021_signal,
    f33ec_f33_earnings_cyclicality_roepos_42d_jerk_v022_signal,
    f33ec_f33_earnings_cyclicality_epspos_63d_jerk_v023_signal,
    f33ec_f33_earnings_cyclicality_nitrough_42d_jerk_v024_signal,
    f33ec_f33_earnings_cyclicality_nitrough_63d_jerk_v025_signal,
    f33ec_f33_earnings_cyclicality_ebittrough_42d_jerk_v026_signal,
    f33ec_f33_earnings_cyclicality_roictrough_63d_jerk_v027_signal,
    f33ec_f33_earnings_cyclicality_roetrough_63d_jerk_v028_signal,
    f33ec_f33_earnings_cyclicality_nipeak_31d_jerk_v029_signal,
    f33ec_f33_earnings_cyclicality_ebitpeak_42d_jerk_v030_signal,
    f33ec_f33_earnings_cyclicality_roicpeak_105d_jerk_v031_signal,
    f33ec_f33_earnings_cyclicality_roepeak_42d_jerk_v032_signal,
    f33ec_f33_earnings_cyclicality_niposstreak_31d_jerk_v033_signal,
    f33ec_f33_earnings_cyclicality_ebitposstreak_21d_jerk_v034_signal,
    f33ec_f33_earnings_cyclicality_roicposstreak_63d_jerk_v035_signal,
    f33ec_f33_earnings_cyclicality_niposfrac_42d_jerk_v036_signal,
    f33ec_f33_earnings_cyclicality_ebitposfrac_52d_jerk_v037_signal,
    f33ec_f33_earnings_cyclicality_roeposfrac_21d_jerk_v038_signal,
    f33ec_f33_earnings_cyclicality_epsposfrac_105d_jerk_v039_signal,
    f33ec_f33_earnings_cyclicality_niz_42d_jerk_v040_signal,
    f33ec_f33_earnings_cyclicality_niz_52d_jerk_v041_signal,
    f33ec_f33_earnings_cyclicality_ebitz_21d_jerk_v042_signal,
    f33ec_f33_earnings_cyclicality_roicz_84d_jerk_v043_signal,
    f33ec_f33_earnings_cyclicality_roez_42d_jerk_v044_signal,
    f33ec_f33_earnings_cyclicality_epsz_52d_jerk_v045_signal,
    f33ec_f33_earnings_cyclicality_ebitz_52d_jerk_v046_signal,
    f33ec_f33_earnings_cyclicality_roiclvl_26d_jerk_v047_signal,
    f33ec_f33_earnings_cyclicality_roelvl_21d_jerk_v048_signal,
    f33ec_f33_earnings_cyclicality_roespread_21d_jerk_v049_signal,
    f33ec_f33_earnings_cyclicality_niroe_13d_jerk_v050_signal,
    f33ec_f33_earnings_cyclicality_ebitroe_42d_jerk_v051_signal,
    f33ec_f33_earnings_cyclicality_nisignmag_42d_jerk_v052_signal,
    f33ec_f33_earnings_cyclicality_ebitsignmag_31d_jerk_v053_signal,
    f33ec_f33_earnings_cyclicality_epssignmag_21d_jerk_v054_signal,
    f33ec_f33_earnings_cyclicality_roicsignmag_63d_jerk_v055_signal,
    f33ec_f33_earnings_cyclicality_niddpeak_63d_jerk_v056_signal,
    f33ec_f33_earnings_cyclicality_ebitddpeak_63d_jerk_v057_signal,
    f33ec_f33_earnings_cyclicality_roicddpeak_42d_jerk_v058_signal,
    f33ec_f33_earnings_cyclicality_nirecmult_84d_jerk_v059_signal,
    f33ec_f33_earnings_cyclicality_ebitrecmult_84d_jerk_v060_signal,
    f33ec_f33_earnings_cyclicality_niflips_31d_jerk_v061_signal,
    f33ec_f33_earnings_cyclicality_ebitflips_42d_jerk_v062_signal,
    f33ec_f33_earnings_cyclicality_roicflips_63d_jerk_v063_signal,
    f33ec_f33_earnings_cyclicality_niampterm_42d_jerk_v064_signal,
    f33ec_f33_earnings_cyclicality_ebitampterm_31d_jerk_v065_signal,
    f33ec_f33_earnings_cyclicality_roicampterm_21d_jerk_v066_signal,
    f33ec_f33_earnings_cyclicality_nicycspan_84d_jerk_v067_signal,
    f33ec_f33_earnings_cyclicality_ebitcycspan_84d_jerk_v068_signal,
    f33ec_f33_earnings_cyclicality_poscross_31d_jerk_v069_signal,
    f33ec_f33_earnings_cyclicality_nitrend_21d_jerk_v070_signal,
    f33ec_f33_earnings_cyclicality_roictrend_63d_jerk_v071_signal,
    f33ec_f33_earnings_cyclicality_epstrend_31d_jerk_v072_signal,
    f33ec_f33_earnings_cyclicality_nieqswing_31d_jerk_v073_signal,
    f33ec_f33_earnings_cyclicality_ebiteqswing_42d_jerk_v074_signal,
    f33ec_f33_earnings_cyclicality_nieqz_84d_jerk_v075_signal,
    f33ec_f33_earnings_cyclicality_nieqpos_84d_jerk_v076_signal,
    f33ec_f33_earnings_cyclicality_nidownvol_31d_jerk_v077_signal,
    f33ec_f33_earnings_cyclicality_ebitupvol_21d_jerk_v078_signal,
    f33ec_f33_earnings_cyclicality_roicsemiskew_84d_jerk_v079_signal,
    f33ec_f33_earnings_cyclicality_niamprank_42d_jerk_v080_signal,
    f33ec_f33_earnings_cyclicality_roicswingrank_31d_jerk_v081_signal,
    f33ec_f33_earnings_cyclicality_ebitposrank_21d_jerk_v082_signal,
    f33ec_f33_earnings_cyclicality_nidaysincepeak_63d_jerk_v083_signal,
    f33ec_f33_earnings_cyclicality_ebitdaysincetrough_63d_jerk_v084_signal,
    f33ec_f33_earnings_cyclicality_cyclebreadth_13d_jerk_v085_signal,
    f33ec_f33_earnings_cyclicality_tripleposfrac_21d_jerk_v086_signal,
    f33ec_f33_earnings_cyclicality_cycledivg_42d_jerk_v087_signal,
    f33ec_f33_earnings_cyclicality_nicumcycle_42d_jerk_v088_signal,
    f33ec_f33_earnings_cyclicality_ebitcumcycle_52d_jerk_v089_signal,
    f33ec_f33_earnings_cyclicality_niampeq_42d_jerk_v090_signal,
    f33ec_f33_earnings_cyclicality_ebitampeq_105d_jerk_v091_signal,
    f33ec_f33_earnings_cyclicality_niphasebal_42d_jerk_v092_signal,
    f33ec_f33_earnings_cyclicality_ebitphasebal_52d_jerk_v093_signal,
    f33ec_f33_earnings_cyclicality_roephasebal_21d_jerk_v094_signal,
    f33ec_f33_earnings_cyclicality_roiccvdisp_63d_jerk_v095_signal,
    f33ec_f33_earnings_cyclicality_roeposema_42d_jerk_v096_signal,
    f33ec_f33_earnings_cyclicality_niposyoy_31d_jerk_v097_signal,
    f33ec_f33_earnings_cyclicality_ebitzyoy_42d_jerk_v098_signal,
    f33ec_f33_earnings_cyclicality_niampxpos_63d_jerk_v099_signal,
    f33ec_f33_earnings_cyclicality_roicampxtrough_63d_jerk_v100_signal,
    f33ec_f33_earnings_cyclicality_niswing_21d_jerk_v101_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_52d_jerk_v102_signal,
    f33ec_f33_earnings_cyclicality_epsswing_84d_jerk_v103_signal,
    f33ec_f33_earnings_cyclicality_roicswing_84d_jerk_v104_signal,
    f33ec_f33_earnings_cyclicality_roeswing_63d_jerk_v105_signal,
    f33ec_f33_earnings_cyclicality_niamp_52d_jerk_v106_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_84d_jerk_v107_signal,
    f33ec_f33_earnings_cyclicality_roicamp_63d_jerk_v108_signal,
    f33ec_f33_earnings_cyclicality_roeamp_31d_jerk_v109_signal,
    f33ec_f33_earnings_cyclicality_epsamp_21d_jerk_v110_signal,
    f33ec_f33_earnings_cyclicality_nipos_84d_jerk_v111_signal,
    f33ec_f33_earnings_cyclicality_ebitpos_84d_jerk_v112_signal,
    f33ec_f33_earnings_cyclicality_roicpos_63d_jerk_v113_signal,
    f33ec_f33_earnings_cyclicality_roepos_21d_jerk_v114_signal,
    f33ec_f33_earnings_cyclicality_epspos_84d_jerk_v115_signal,
    f33ec_f33_earnings_cyclicality_nitrough_63d_jerk_v116_signal,
    f33ec_f33_earnings_cyclicality_ebittrough_63d_jerk_v117_signal,
    f33ec_f33_earnings_cyclicality_roictrough_42d_jerk_v118_signal,
    f33ec_f33_earnings_cyclicality_roetrough_63d_jerk_v119_signal,
    f33ec_f33_earnings_cyclicality_epstrough_63d_jerk_v120_signal,
    f33ec_f33_earnings_cyclicality_nipeak_52d_jerk_v121_signal,
    f33ec_f33_earnings_cyclicality_ebitpeak_52d_jerk_v122_signal,
    f33ec_f33_earnings_cyclicality_roicpeak_63d_jerk_v123_signal,
    f33ec_f33_earnings_cyclicality_roepeak_63d_jerk_v124_signal,
    f33ec_f33_earnings_cyclicality_epspeak_31d_jerk_v125_signal,
    f33ec_f33_earnings_cyclicality_epsposstreak_21d_jerk_v126_signal,
    f33ec_f33_earnings_cyclicality_roeposstreak_63d_jerk_v127_signal,
    f33ec_f33_earnings_cyclicality_niposfrac_63d_jerk_v128_signal,
    f33ec_f33_earnings_cyclicality_ebitposfrac_31d_jerk_v129_signal,
    f33ec_f33_earnings_cyclicality_roicposfrac_52d_jerk_v130_signal,
    f33ec_f33_earnings_cyclicality_niz_105d_jerk_v131_signal,
    f33ec_f33_earnings_cyclicality_ebitz_63d_jerk_v132_signal,
    f33ec_f33_earnings_cyclicality_roicz_31d_jerk_v133_signal,
    f33ec_f33_earnings_cyclicality_roez_42d_jerk_v134_signal,
    f33ec_f33_earnings_cyclicality_epsz_63d_jerk_v135_signal,
    f33ec_f33_earnings_cyclicality_niz_21d_jerk_v136_signal,
    f33ec_f33_earnings_cyclicality_roiclvl_21d_jerk_v137_signal,
    f33ec_f33_earnings_cyclicality_roelvl_13d_jerk_v138_signal,
    f33ec_f33_earnings_cyclicality_roespread_63d_jerk_v139_signal,
    f33ec_f33_earnings_cyclicality_niroe_42d_jerk_v140_signal,
    f33ec_f33_earnings_cyclicality_ebitroa_31d_jerk_v141_signal,
    f33ec_f33_earnings_cyclicality_roesignmag_21d_jerk_v142_signal,
    f33ec_f33_earnings_cyclicality_niddpeak_105d_jerk_v143_signal,
    f33ec_f33_earnings_cyclicality_ebitddpeak_63d_jerk_v144_signal,
    f33ec_f33_earnings_cyclicality_roeddpeak_52d_jerk_v145_signal,
    f33ec_f33_earnings_cyclicality_nirecmult_52d_jerk_v146_signal,
    f33ec_f33_earnings_cyclicality_roicrecmult_84d_jerk_v147_signal,
    f33ec_f33_earnings_cyclicality_niflips_63d_jerk_v148_signal,
    f33ec_f33_earnings_cyclicality_epsflips_31d_jerk_v149_signal,
    f33ec_f33_earnings_cyclicality_roeflips_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EARNINGS_CYCLICALITY_REGISTRY_3RD_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f33_earnings_cyclicality_3rd_derivatives_001_150_claude: %d features pass" % n_features)
