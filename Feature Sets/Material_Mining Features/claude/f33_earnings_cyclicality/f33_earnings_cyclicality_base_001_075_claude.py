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
# net-income cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_niswing_252d_base_v001_signal(netinc):
    base = _ec_cv(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_niswing_504d_base_v002_signal(netinc):
    base = _ec_cv(netinc, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income cyclical swing (CV) over the full multi-year cycle
def f33ec_f33_earnings_cyclicality_niswing_1260d_base_v003_signal(netinc):
    base = _ec_cv(netinc, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_ebitswing_252d_base_v004_signal(ebit):
    base = _ec_cv(ebit, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_ebitswing_504d_base_v005_signal(ebit):
    base = _ec_cv(ebit, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_epsswing_252d_base_v006_signal(eps):
    base = _ec_cv(eps, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_roicswing_252d_base_v007_signal(roic):
    base = _ec_cv(roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE cyclical swing (CV) over the trailing year
def f33ec_f33_earnings_cyclicality_roeswing_252d_base_v008_signal(roe):
    base = _ec_cv(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_roicswing_504d_base_v009_signal(roic):
    base = _ec_cv(roic, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE cyclical swing (CV) over two years
def f33ec_f33_earnings_cyclicality_roeswing_504d_base_v010_signal(roe):
    base = _ec_cv(roe, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_niamp_252d_base_v011_signal(netinc):
    base = _ec_amp(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_niamp_504d_base_v012_signal(netinc):
    base = _ec_amp(netinc, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_ebitamp_252d_base_v013_signal(ebit):
    base = _ec_amp(ebit, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT peak-to-trough amplitude over the full cycle
def f33ec_f33_earnings_cyclicality_ebitamp_1260d_base_v014_signal(ebit):
    base = _ec_amp(ebit, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC peak-to-trough amplitude over the year
def f33ec_f33_earnings_cyclicality_roicamp_252d_base_v015_signal(roic):
    base = _ec_amp(roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_roeamp_504d_base_v016_signal(roe):
    base = _ec_amp(roe, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS peak-to-trough amplitude over two years
def f33ec_f33_earnings_cyclicality_epsamp_504d_base_v017_signal(eps):
    base = _ec_amp(eps, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income position in its 252d cyclical range (0=trough,1=peak)
def f33ec_f33_earnings_cyclicality_nipos_252d_base_v018_signal(netinc):
    base = _ec_pos(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income position in its multi-year cyclical range
def f33ec_f33_earnings_cyclicality_nipos_1260d_base_v019_signal(netinc):
    base = _ec_pos(netinc, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT cyclical position fast-minus-slow EMA oscillator
def f33ec_f33_earnings_cyclicality_ebitpos_504d_base_v020_signal(ebit):
    p = _ec_pos(ebit, 504)
    base = p.ewm(span=21, min_periods=10).mean() - p.ewm(span=84, min_periods=42).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_roicpos_252d_base_v021_signal(roic):
    base = _ec_pos(roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE position in its 504d cyclical range
def f33ec_f33_earnings_cyclicality_roepos_504d_base_v022_signal(roe):
    base = _ec_pos(roe, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS position in its 252d cyclical range
def f33ec_f33_earnings_cyclicality_epspos_252d_base_v023_signal(eps):
    base = _ec_pos(eps, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_nitrough_252d_base_v024_signal(netinc):
    base = _ec_fromtrough(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income recovery off multi-year trough, displacement vs slow EWM
def f33ec_f33_earnings_cyclicality_nitrough_1260d_base_v025_signal(netinc):
    ft = _ec_fromtrough(netinc, 1260)
    base = ft - ft.ewm(span=189, min_periods=63).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread recovery off its 504d trough, EWM displacement
def f33ec_f33_earnings_cyclicality_ebittrough_504d_base_v026_signal(ebit, netinc):
    spr = ebit - netinc
    ft = _ec_fromtrough(spr, 504)
    base = ft - ft.ewm(span=63, min_periods=21).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC distance above its 252d cyclical trough
def f33ec_f33_earnings_cyclicality_roictrough_252d_base_v027_signal(roic):
    base = _ec_fromtrough(roic, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE distance above its 504d cyclical trough
def f33ec_f33_earnings_cyclicality_roetrough_504d_base_v028_signal(roe):
    base = _ec_fromtrough(roe, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income distance below its 252d cyclical peak (down-cycle depth)
def f33ec_f33_earnings_cyclicality_nipeak_252d_base_v029_signal(netinc):
    base = _ec_frompeak(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT distance below its 504d cyclical peak
def f33ec_f33_earnings_cyclicality_ebitpeak_504d_base_v030_signal(ebit):
    base = _ec_frompeak(ebit, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC distance below its multi-year cyclical peak
def f33ec_f33_earnings_cyclicality_roicpeak_1260d_base_v031_signal(roic):
    base = _ec_frompeak(roic, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE distance below its 252d cyclical peak
def f33ec_f33_earnings_cyclicality_roepeak_252d_base_v032_signal(roe):
    base = _ec_frompeak(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive net-income-positive streak length (up-phase durability)
def f33ec_f33_earnings_cyclicality_niposstreak_base_v033_signal(netinc):
    base = _ec_posstreak(netinc)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive EBIT-positive streak length
def f33ec_f33_earnings_cyclicality_ebitposstreak_base_v034_signal(ebit):
    base = _ec_posstreak(ebit)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive ROIC-positive streak length
def f33ec_f33_earnings_cyclicality_roicposstreak_base_v035_signal(roic):
    base = _ec_posstreak(roic)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year net income was positive (up-phase persistence)
def f33ec_f33_earnings_cyclicality_niposfrac_252d_base_v036_signal(netinc):
    base = _ec_posfrac(netinc, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years EBIT was positive, half-year change (up-phase rotation)
def f33ec_f33_earnings_cyclicality_ebitposfrac_504d_base_v037_signal(ebit):
    frac = _ec_posfrac(ebit, 504)
    base = frac - frac.shift(126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year ROE was positive
def f33ec_f33_earnings_cyclicality_roeposfrac_252d_base_v038_signal(roe):
    base = _ec_posfrac(roe, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the multi-year cycle EPS was positive
def f33ec_f33_earnings_cyclicality_epsposfrac_1260d_base_v039_signal(eps):
    base = _ec_posfrac(eps, 1260)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net income cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_niz_252d_base_v040_signal(netinc):
    zz = _z(netinc, 252)
    base = zz - zz.ewm(span=63, min_periods=21).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net income cyclical-z percentile-ranked vs its own year
def f33ec_f33_earnings_cyclicality_niz_504d_base_v041_signal(netinc):
    zz = _z(netinc, 504)
    base = _rank(zz, 252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread cyclical-z mean-reversion gap
def f33ec_f33_earnings_cyclicality_ebitz_252d_base_v042_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 252)
    base = zz - zz.ewm(span=42, min_periods=21).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_roicz_504d_base_v043_signal(roic):
    zz = _z(roic, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_roez_252d_base_v044_signal(roe):
    zz = _z(roe, 252)
    base = zz - zz.ewm(span=63, min_periods=31).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS cyclical-z mean-reversion gap (z minus its slow EWM)
def f33ec_f33_earnings_cyclicality_epsz_504d_base_v045_signal(eps):
    zz = _z(eps, 504)
    base = zz - zz.ewm(span=84, min_periods=42).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread cyclical-z year-over-year change
def f33ec_f33_earnings_cyclicality_ebitz_1260d_base_v046_signal(ebit, netinc):
    spr = ebit - netinc
    zz = _z(spr, 1260)
    base = zz - zz.shift(252)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC level smoothed over a quarter (current return-on-capital)
def f33ec_f33_earnings_cyclicality_roiclvl_63d_base_v047_signal(roic):
    base = _mean(roic, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE level smoothed over a quarter
def f33ec_f33_earnings_cyclicality_roelvl_63d_base_v048_signal(roe):
    base = _mean(roe, 63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROE-minus-ROIC spread (leverage contribution) over a half-year
def f33ec_f33_earnings_cyclicality_roespread_126d_base_v049_signal(roe, roic):
    base = _mean(roe - roic, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-on-equity (computed ROE) smoothed over a half-year
def f33ec_f33_earnings_cyclicality_niroe_126d_base_v050_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    base = _mean(r, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-on-equity cyclical position over a half-year (operating-return phase)
def f33ec_f33_earnings_cyclicality_ebitroe_126d_base_v051_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    base = _ec_pos(r, 126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income sign x magnitude de-trended vs year (swing intensity)
def f33ec_f33_earnings_cyclicality_nisignmag_base_v052_signal(netinc):
    sm = _ec_signmag(netinc, 1e6)
    base = sm - sm.rolling(252, min_periods=126).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread sign x magnitude, quarterly momentum
def f33ec_f33_earnings_cyclicality_ebitsignmag_base_v053_signal(ebit, netinc):
    spr = ebit - netinc
    sm = _ec_signmag(spr, 1e6)
    base = sm - sm.shift(63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS sign x magnitude de-trended vs year
def f33ec_f33_earnings_cyclicality_epssignmag_base_v054_signal(eps):
    sm = _ec_signmag(eps, 1.0)
    base = sm - sm.rolling(252, min_periods=126).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC sign x magnitude z-scored over two years
def f33ec_f33_earnings_cyclicality_roicsignmag_base_v055_signal(roic):
    sm = np.sign(roic) * np.sqrt(roic.abs())
    base = _z(sm, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income drawdown from its two-year peak (earnings down-cycle)
def f33ec_f33_earnings_cyclicality_niddpeak_504d_base_v056_signal(netinc):
    peak = _rmax(netinc, 504)
    base = (netinc - peak) / (peak.abs() + 1e-9)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-minus-netinc accrual spread drawdown from its multi-year peak
def f33ec_f33_earnings_cyclicality_ebitddpeak_1260d_base_v057_signal(ebit, netinc):
    spr = ebit - netinc
    peak = _rmax(spr, 1260)
    base = (spr - peak) / (peak.abs() + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from its two-year peak, percentile-ranked
def f33ec_f33_earnings_cyclicality_roicddpeak_504d_base_v058_signal(roic):
    peak = _rmax(roic, 504)
    dd = (roic - peak) / (peak.abs() + 1e-9)
    base = _rank(dd, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income recovery off two-year trough, quarterly momentum of the multiple
def f33ec_f33_earnings_cyclicality_nirecmult_504d_base_v059_signal(netinc):
    trough = _rmin(netinc, 504)
    rec = (netinc - trough) / (trough.abs() + 1e6)
    base = rec - rec.shift(63)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT recovery off multi-year trough, percentile-ranked multiple
def f33ec_f33_earnings_cyclicality_ebitrecmult_1260d_base_v060_signal(ebit):
    trough = _rmin(ebit, 1260)
    rec = (ebit - trough) / (trough.abs() + 1e6)
    base = _rank(rec, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income sign flips over the year, swing-weighted (cyclical instability)
def f33ec_f33_earnings_cyclicality_niflips_252d_base_v061_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    sd = netinc.rolling(63, min_periods=21).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    base = cnt + 30.0 * sd / (lvl + 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT sign flips over two years, amplitude-weighted
def f33ec_f33_earnings_cyclicality_ebitflips_504d_base_v062_signal(ebit):
    flip = (np.sign(ebit) != np.sign(ebit.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    amp = _ec_amp(ebit, 252)
    base = cnt + 5.0 * amp
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC sign flips over the year, amplitude-weighted (return-on-capital instability)
def f33ec_f33_earnings_cyclicality_roicflips_252d_base_v063_signal(roic):
    flip = (np.sign(roic) != np.sign(roic.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    amp = _ec_amp(roic, 252)
    base = cnt + 3.0 * amp
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income swing term structure: acute 63d minus chronic 504d
def f33ec_f33_earnings_cyclicality_niampterm_base_v064_signal(netinc):
    s = _ec_cv(netinc, 63)
    l = _ec_cv(netinc, 504)
    base = s - l
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT amplitude term structure: half-year vs full cycle
def f33ec_f33_earnings_cyclicality_ebitampterm_base_v065_signal(ebit):
    s = _ec_amp(ebit, 126)
    l = _ec_amp(ebit, 1260)
    base = s - l
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC swing ratio: half-year vs two-year (worsening volatility regime)
def f33ec_f33_earnings_cyclicality_roicampterm_base_v066_signal(roic):
    s = _ec_cv(roic, 126)
    l = _ec_cv(roic, 504)
    base = (s + 0.05) / (l + 0.05) - 1.0
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income full cyclical span (peak-trough gap), log-compressed
def f33ec_f33_earnings_cyclicality_nicycspan_504d_base_v067_signal(netinc):
    hi = _rmax(netinc, 504)
    lo = _rmin(netinc, 504)
    base = np.log1p((hi - lo).abs() / 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT multi-year cyclical span, log-compressed
def f33ec_f33_earnings_cyclicality_ebitcycspan_1260d_base_v068_signal(ebit):
    hi = _rmax(ebit, 1260)
    lo = _rmin(ebit, 1260)
    base = np.log1p((hi - lo).abs() / 1e6)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# crossings into profitability over the year, trough-distance-weighted (recovery frequency)
def f33ec_f33_earnings_cyclicality_poscross_252d_base_v069_signal(netinc):
    pos = _ec_pospos(netinc)
    entries = ((pos == 1) & (pos.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = _ec_fromtrough(netinc, 252)
    base = cnt + 2.0 * depth
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income yearly change normalized by dispersion (cyclical direction)
def f33ec_f33_earnings_cyclicality_nitrend_252d_base_v070_signal(netinc):
    sl = (netinc - netinc.shift(252))
    disp = netinc.rolling(252, min_periods=126).std()
    base = sl / disp.replace(0, np.nan)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC yearly change normalized by dispersion
def f33ec_f33_earnings_cyclicality_roictrend_252d_base_v071_signal(roic):
    sl = (roic - roic.shift(252))
    disp = roic.rolling(252, min_periods=126).std()
    base = sl / disp.replace(0, np.nan)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EPS half-year change normalized by dispersion
def f33ec_f33_earnings_cyclicality_epstrend_126d_base_v072_signal(eps):
    sl = (eps - eps.shift(126))
    disp = eps.rolling(126, min_periods=63).std()
    base = sl / disp.replace(0, np.nan)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income/equity (ROE) swing percentile-ranked (capital-return cyclicality)
def f33ec_f33_earnings_cyclicality_nieqswing_252d_base_v073_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    cv = _ec_cv(r, 252)
    base = _rank(cv, 504)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/equity amplitude displacement vs its slow EWM over two years
def f33ec_f33_earnings_cyclicality_ebiteqswing_504d_base_v074_signal(ebit, equity):
    r = _ec_ratio(ebit, equity)
    amp = _ec_amp(r, 504)
    base = amp - amp.ewm(span=252, min_periods=126).mean()
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


# net-income/equity cyclical-z half-year change (computed-ROE z momentum)
def f33ec_f33_earnings_cyclicality_nieqz_504d_base_v075_signal(netinc, equity):
    r = _ec_ratio(netinc, equity)
    zz = _z(r, 504)
    base = zz - zz.shift(126)
    result = base
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ec_f33_earnings_cyclicality_niswing_252d_base_v001_signal,
    f33ec_f33_earnings_cyclicality_niswing_504d_base_v002_signal,
    f33ec_f33_earnings_cyclicality_niswing_1260d_base_v003_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_252d_base_v004_signal,
    f33ec_f33_earnings_cyclicality_ebitswing_504d_base_v005_signal,
    f33ec_f33_earnings_cyclicality_epsswing_252d_base_v006_signal,
    f33ec_f33_earnings_cyclicality_roicswing_252d_base_v007_signal,
    f33ec_f33_earnings_cyclicality_roeswing_252d_base_v008_signal,
    f33ec_f33_earnings_cyclicality_roicswing_504d_base_v009_signal,
    f33ec_f33_earnings_cyclicality_roeswing_504d_base_v010_signal,
    f33ec_f33_earnings_cyclicality_niamp_252d_base_v011_signal,
    f33ec_f33_earnings_cyclicality_niamp_504d_base_v012_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_252d_base_v013_signal,
    f33ec_f33_earnings_cyclicality_ebitamp_1260d_base_v014_signal,
    f33ec_f33_earnings_cyclicality_roicamp_252d_base_v015_signal,
    f33ec_f33_earnings_cyclicality_roeamp_504d_base_v016_signal,
    f33ec_f33_earnings_cyclicality_epsamp_504d_base_v017_signal,
    f33ec_f33_earnings_cyclicality_nipos_252d_base_v018_signal,
    f33ec_f33_earnings_cyclicality_nipos_1260d_base_v019_signal,
    f33ec_f33_earnings_cyclicality_ebitpos_504d_base_v020_signal,
    f33ec_f33_earnings_cyclicality_roicpos_252d_base_v021_signal,
    f33ec_f33_earnings_cyclicality_roepos_504d_base_v022_signal,
    f33ec_f33_earnings_cyclicality_epspos_252d_base_v023_signal,
    f33ec_f33_earnings_cyclicality_nitrough_252d_base_v024_signal,
    f33ec_f33_earnings_cyclicality_nitrough_1260d_base_v025_signal,
    f33ec_f33_earnings_cyclicality_ebittrough_504d_base_v026_signal,
    f33ec_f33_earnings_cyclicality_roictrough_252d_base_v027_signal,
    f33ec_f33_earnings_cyclicality_roetrough_504d_base_v028_signal,
    f33ec_f33_earnings_cyclicality_nipeak_252d_base_v029_signal,
    f33ec_f33_earnings_cyclicality_ebitpeak_504d_base_v030_signal,
    f33ec_f33_earnings_cyclicality_roicpeak_1260d_base_v031_signal,
    f33ec_f33_earnings_cyclicality_roepeak_252d_base_v032_signal,
    f33ec_f33_earnings_cyclicality_niposstreak_base_v033_signal,
    f33ec_f33_earnings_cyclicality_ebitposstreak_base_v034_signal,
    f33ec_f33_earnings_cyclicality_roicposstreak_base_v035_signal,
    f33ec_f33_earnings_cyclicality_niposfrac_252d_base_v036_signal,
    f33ec_f33_earnings_cyclicality_ebitposfrac_504d_base_v037_signal,
    f33ec_f33_earnings_cyclicality_roeposfrac_252d_base_v038_signal,
    f33ec_f33_earnings_cyclicality_epsposfrac_1260d_base_v039_signal,
    f33ec_f33_earnings_cyclicality_niz_252d_base_v040_signal,
    f33ec_f33_earnings_cyclicality_niz_504d_base_v041_signal,
    f33ec_f33_earnings_cyclicality_ebitz_252d_base_v042_signal,
    f33ec_f33_earnings_cyclicality_roicz_504d_base_v043_signal,
    f33ec_f33_earnings_cyclicality_roez_252d_base_v044_signal,
    f33ec_f33_earnings_cyclicality_epsz_504d_base_v045_signal,
    f33ec_f33_earnings_cyclicality_ebitz_1260d_base_v046_signal,
    f33ec_f33_earnings_cyclicality_roiclvl_63d_base_v047_signal,
    f33ec_f33_earnings_cyclicality_roelvl_63d_base_v048_signal,
    f33ec_f33_earnings_cyclicality_roespread_126d_base_v049_signal,
    f33ec_f33_earnings_cyclicality_niroe_126d_base_v050_signal,
    f33ec_f33_earnings_cyclicality_ebitroe_126d_base_v051_signal,
    f33ec_f33_earnings_cyclicality_nisignmag_base_v052_signal,
    f33ec_f33_earnings_cyclicality_ebitsignmag_base_v053_signal,
    f33ec_f33_earnings_cyclicality_epssignmag_base_v054_signal,
    f33ec_f33_earnings_cyclicality_roicsignmag_base_v055_signal,
    f33ec_f33_earnings_cyclicality_niddpeak_504d_base_v056_signal,
    f33ec_f33_earnings_cyclicality_ebitddpeak_1260d_base_v057_signal,
    f33ec_f33_earnings_cyclicality_roicddpeak_504d_base_v058_signal,
    f33ec_f33_earnings_cyclicality_nirecmult_504d_base_v059_signal,
    f33ec_f33_earnings_cyclicality_ebitrecmult_1260d_base_v060_signal,
    f33ec_f33_earnings_cyclicality_niflips_252d_base_v061_signal,
    f33ec_f33_earnings_cyclicality_ebitflips_504d_base_v062_signal,
    f33ec_f33_earnings_cyclicality_roicflips_252d_base_v063_signal,
    f33ec_f33_earnings_cyclicality_niampterm_base_v064_signal,
    f33ec_f33_earnings_cyclicality_ebitampterm_base_v065_signal,
    f33ec_f33_earnings_cyclicality_roicampterm_base_v066_signal,
    f33ec_f33_earnings_cyclicality_nicycspan_504d_base_v067_signal,
    f33ec_f33_earnings_cyclicality_ebitcycspan_1260d_base_v068_signal,
    f33ec_f33_earnings_cyclicality_poscross_252d_base_v069_signal,
    f33ec_f33_earnings_cyclicality_nitrend_252d_base_v070_signal,
    f33ec_f33_earnings_cyclicality_roictrend_252d_base_v071_signal,
    f33ec_f33_earnings_cyclicality_epstrend_126d_base_v072_signal,
    f33ec_f33_earnings_cyclicality_nieqswing_252d_base_v073_signal,
    f33ec_f33_earnings_cyclicality_ebiteqswing_504d_base_v074_signal,
    f33ec_f33_earnings_cyclicality_nieqz_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EARNINGS_CYCLICALITY_REGISTRY_001_075 = REGISTRY


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

    print("OK f33_earnings_cyclicality_base_001_075_claude: %d features pass" % n_features)
