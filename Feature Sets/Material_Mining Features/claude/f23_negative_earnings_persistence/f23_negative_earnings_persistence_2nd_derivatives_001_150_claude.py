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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (negative earnings persistence) =====
def _isloss(s):
    return (s < 0.0).astype(float)


def _losscount(s, w):
    return _isloss(s).rolling(w, min_periods=max(1, w // 2)).mean()


def _losssum(s, w):
    return _isloss(s).rolling(w, min_periods=max(1, w // 2)).sum()


def _lossdepth(s, scale):
    return (-s).clip(lower=0.0) / float(scale)


def _profitdepth(s, scale):
    return s.clip(lower=0.0) / float(scale)


def _streak_loss(s):
    loss = _isloss(s)
    grp = (loss == 0).cumsum()
    return loss.groupby(grp).cumsum()


def _streak_profit(s):
    prof = (s > 0.0).astype(float)
    grp = (prof == 0).cumsum()
    return prof.groupby(grp).cumsum()


def _time_since_profit(s):
    prof = (s > 0.0)
    idx = np.arange(len(s), dtype=float)
    last = pd.Series(np.where(prof.values, idx, np.nan), index=s.index).ffill()
    return pd.Series(idx, index=s.index) - last


def _deficit_growth(retearn, w):
    return (retearn.shift(w) - retearn) / float(w)


def _signmag(s, scale):
    return np.sign(s) * np.sqrt(s.abs() / float(scale))


# ============================================================
# File 3: each feature builds a negative-earnings-persistence BASE series inline,
# then returns its 1st math derivative (slope) over a window matched to the base.


# slope of net-loss persistence (252d base, 21d slope) — chronic-loss velocity
def f23ne_f23_negative_earnings_persistence_lossfrac_21d_slope_v001_signal(netinc):
    base = _losscount(netinc, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-burn persistence (252d base, 21d slope) — burn-regime velocity
def f23ne_f23_negative_earnings_persistence_burnfrac_21d_slope_v002_signal(ncfo):
    base = _losscount(ncfo, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss persistence (252d base, 21d slope) — operating-loss velocity
def f23ne_f23_negative_earnings_persistence_ebitlossfrac_21d_slope_v003_signal(ebit):
    base = _losscount(ebit, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss persistence (252d base, 21d slope)
def f23ne_f23_negative_earnings_persistence_epslossfrac_21d_slope_v004_signal(eps):
    base = _losscount(eps, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence (126d base, 21d slope) — acute-loss velocity
def f23ne_f23_negative_earnings_persistence_lossfrac126_21d_slope_v005_signal(netinc):
    base = _losscount(netinc, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence (126d base, 21d slope)
def f23ne_f23_negative_earnings_persistence_burnfrac126_21d_slope_v006_signal(ncfo):
    base = _losscount(ncfo, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss depth (63d-smoothed base, 21d slope) — loss-deepening velocity
def f23ne_f23_negative_earnings_persistence_lossdepth_21d_slope_v007_signal(netinc):
    base = _lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-burn depth (63d-smoothed base, 21d slope)
def f23ne_f23_negative_earnings_persistence_burndepth_21d_slope_v008_signal(ncfo):
    base = _lossdepth(ncfo, 1e7).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss depth (63d-smoothed base, 21d slope)
def f23ne_f23_negative_earnings_persistence_ebitdepth_21d_slope_v009_signal(ebit):
    base = _lossdepth(ebit, 1e7).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of time-since-net-profit (21d slope) — dry-spell lengthening rate
def f23ne_f23_negative_earnings_persistence_tsprofit_21d_slope_v010_signal(netinc):
    base = np.log1p(_time_since_profit(netinc).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of time-since-cash-positive (21d slope)
def f23ne_f23_negative_earnings_persistence_tsburn_21d_slope_v011_signal(ncfo):
    base = np.log1p(_time_since_profit(ncfo).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulated-deficit depth (21d slope) — deficit-deepening velocity
def f23ne_f23_negative_earnings_persistence_deficitdepth_21d_slope_v012_signal(retearn):
    base = np.log1p((-retearn).clip(lower=0.0) / 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net signed-magnitude earnings (21d slope) — sign-intensity velocity
def f23ne_f23_negative_earnings_persistence_nisignmag_21d_slope_v013_signal(netinc):
    base = _signmag(netinc, 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT signed-magnitude (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitsignmag_21d_slope_v014_signal(ebit):
    base = _signmag(ebit, 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS signed-magnitude (21d slope)
def f23ne_f23_negative_earnings_persistence_epssignmag_21d_slope_v015_signal(eps):
    base = _signmag(eps, 1.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss-streak length (5d slope) — streak-growth velocity
def f23ne_f23_negative_earnings_persistence_lossstreak_5d_slope_v016_signal(netinc):
    base = _streak_loss(netinc)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cash-burn-streak length (5d slope)
def f23ne_f23_negative_earnings_persistence_burnstreak_5d_slope_v017_signal(ncfo):
    base = _streak_loss(ncfo)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of profit-streak length (5d slope) — recovery-build velocity
def f23ne_f23_negative_earnings_persistence_profstreak_5d_slope_v018_signal(netinc):
    base = _streak_profit(netinc)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings level (63d slope) — deficit trajectory velocity
def f23ne_f23_negative_earnings_persistence_retearn_63d_slope_v019_signal(retearn):
    base = np.sign(retearn) * np.log1p(retearn.abs() / 1e6)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative net loss (21d slope) — loss-accumulation velocity
def f23ne_f23_negative_earnings_persistence_cumloss_21d_slope_v020_signal(netinc):
    base = np.log1p((-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum() / 1e7)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative cash burn (21d slope)
def f23ne_f23_negative_earnings_persistence_cumburn_21d_slope_v021_signal(ncfo):
    base = np.log1p((-ncfo).clip(lower=0.0).rolling(252, min_periods=126).sum() / 1e7)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss dominance (21d slope) — loss-tilt velocity
def f23ne_f23_negative_earnings_persistence_lossdom_21d_slope_v022_signal(netinc):
    loss = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    prof = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    base = (loss - prof) / (loss + prof + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn dominance (21d slope)
def f23ne_f23_negative_earnings_persistence_burndom_21d_slope_v023_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).sum()
    gen = ncfo.clip(lower=0.0).rolling(252, min_periods=126).sum()
    base = (burn - gen) / (burn + gen + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross-flow loss breadth (21d slope) — distress-broadening velocity
def f23ne_f23_negative_earnings_persistence_breadth_21d_slope_v024_signal(netinc, ncfo, ebit):
    base = (_isloss(netinc) + _isloss(ncfo)
            + _isloss(ebit)).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of triple-loss regime fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_triple_21d_slope_v025_signal(netinc, ncfo, ebit):
    base = ((netinc < 0) & (ncfo < 0) & (ebit < 0)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence z-score (21d slope) — relative-regime velocity
def f23ne_f23_negative_earnings_persistence_lossz_21d_slope_v026_signal(netinc):
    base = _z(_losscount(netinc, 63), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS level rank (63d slope) — slower per-share position velocity
def f23ne_f23_negative_earnings_persistence_epsrank_21d_slope_v027_signal(eps):
    base = _rank(eps, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings drawdown (21d slope) — deficit-erosion velocity
def f23ne_f23_negative_earnings_persistence_retdd_21d_slope_v028_signal(retearn):
    peak = _rmax(retearn, 504)
    base = (retearn - peak) / (peak.abs() + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings recovery off trough (21d slope) — deficit-healing velocity
def f23ne_f23_negative_earnings_persistence_retrec_21d_slope_v029_signal(retearn):
    trough = _rmin(retearn, 504)
    base = (retearn - trough) / (trough.abs() + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depth-tilted net-income sign tendency (63d slope) — signed-intensity velocity
def f23ne_f23_negative_earnings_persistence_meansign_21d_slope_v030_signal(netinc):
    sgn = np.sign(netinc).rolling(126, min_periods=63).mean()
    depth = np.tanh(_lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean())
    base = sgn - depth
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss-depth relative level (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitrel_21d_slope_v031_signal(ebit):
    d = _lossdepth(ebit, 1.0)
    typ = d.rolling(504, min_periods=252).mean()
    base = d / (typ + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accrual-vs-cash loss gap (21d slope)
def f23ne_f23_negative_earnings_persistence_accrgap_21d_slope_v032_signal(netinc, ncfo):
    base = _losscount(netinc, 252) - _losscount(ncfo, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit-growth rate (21d slope) — deficit-acceleration proxy
def f23ne_f23_negative_earnings_persistence_defgr_21d_slope_v033_signal(retearn):
    base = np.tanh(_deficit_growth(retearn, 126) / 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of profit-depth-weighted recovery breadth (63d slope) — recovery velocity
def f23ne_f23_negative_earnings_persistence_proffrac_21d_slope_v034_signal(netinc):
    frac = (netinc > 0).astype(float).rolling(252, min_periods=126).mean()
    pdepth = np.tanh(_profitdepth(netinc, 1e7).rolling(63, min_periods=21).mean())
    base = frac * (1.0 + pdepth)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWM net-loss persistence (21d slope)
def f23ne_f23_negative_earnings_persistence_lossema_21d_slope_v035_signal(netinc):
    base = _losscount(netinc, 126).ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWM cash-burn persistence (21d slope)
def f23ne_f23_negative_earnings_persistence_burnema_21d_slope_v036_signal(ncfo):
    base = _losscount(ncfo, 126).ewm(span=84, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross-flow average negative count (21d slope)
def f23ne_f23_negative_earnings_persistence_avgneg_21d_slope_v037_signal(netinc, ncfo, ebit, eps):
    base = (_isloss(netinc) + _isloss(ncfo) + _isloss(ebit)
            + _isloss(eps)).rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-income downside semi-deviation (21d slope)
def f23ne_f23_negative_earnings_persistence_semidev_21d_slope_v038_signal(netinc):
    neg = netinc.where(netinc < 0, 0.0)
    base = neg.rolling(252, min_periods=126).std() / 1e6
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-income swing amplitude (21d slope)
def f23ne_f23_negative_earnings_persistence_niswing_21d_slope_v039_signal(netinc):
    sd = netinc.rolling(252, min_periods=126).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    base = sd / (lvl + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWM-smoothed loss persistence position within range (21d slope)
def f23ne_f23_negative_earnings_persistence_losspos_21d_slope_v040_signal(netinc):
    lf = _losscount(netinc, 126)
    hi = _rmax(lf, 504)
    lo = _rmin(lf, 504)
    pos = (lf - lo) / (hi - lo).replace(0, np.nan) - 0.5
    base = pos.ewm(span=42, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of worst-loss-in-year level (21d slope)
def f23ne_f23_negative_earnings_persistence_worstloss_21d_slope_v041_signal(netinc):
    base = np.log1p((-netinc).clip(lower=0.0).rolling(252, min_periods=126).max() / 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss concentration (21d slope)
def f23ne_f23_negative_earnings_persistence_lossconc_21d_slope_v042_signal(netinc):
    loss = (-netinc).clip(lower=0.0)
    worst = loss.rolling(252, min_periods=126).max()
    total = loss.rolling(252, min_periods=126).sum()
    base = worst / (total + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of sign-agreement (netinc vs ncfo) (21d slope)
def f23ne_f23_negative_earnings_persistence_signagree_21d_slope_v043_signal(netinc, ncfo):
    base = (np.sign(netinc) == np.sign(ncfo)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of self-funding fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_selffund_21d_slope_v044_signal(netinc, ncfo):
    base = ((netinc > 0) & (ncfo < 0)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence (63d slope, 252d base) — slower chronic velocity
def f23ne_f23_negative_earnings_persistence_lossfrac_63d_slope_v045_signal(netinc):
    base = _losscount(netinc, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence (63d slope, 504d base)
def f23ne_f23_negative_earnings_persistence_burnfrac_63d_slope_v046_signal(ncfo):
    base = _losscount(ncfo, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss persistence (63d slope, 504d base)
def f23ne_f23_negative_earnings_persistence_ebitfrac_63d_slope_v047_signal(ebit):
    base = _losscount(ebit, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit-build fraction (63d slope)
def f23ne_f23_negative_earnings_persistence_defbuild_63d_slope_v048_signal(retearn):
    base = (retearn < retearn.shift(1)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of accumulated-deficit depth rank vs history (63d slope) — deficit-rank velocity
def f23ne_f23_negative_earnings_persistence_defdepth_63d_slope_v049_signal(retearn):
    base = _rank(np.log1p((-retearn).clip(lower=0.0) / 1e6), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative net loss (63d slope)
def f23ne_f23_negative_earnings_persistence_cumloss_63d_slope_v050_signal(netinc):
    base = np.log1p((-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum() / 1e7)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of time-since-net-profit (63d slope)
def f23ne_f23_negative_earnings_persistence_tsni_63d_slope_v051_signal(netinc):
    base = np.log1p(_time_since_profit(netinc).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net signed-magnitude smoothed (63d slope)
def f23ne_f23_negative_earnings_persistence_nismsm_63d_slope_v052_signal(netinc):
    base = _signmag(netinc, 1e6).ewm(span=42, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT signed-magnitude (63d slope)
def f23ne_f23_negative_earnings_persistence_ebitsm_63d_slope_v053_signal(ebit):
    base = _signmag(ebit, 1e6)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings level (126d slope)
def f23ne_f23_negative_earnings_persistence_retearn_126d_slope_v054_signal(retearn):
    base = np.sign(retearn) * np.log1p(retearn.abs() / 1e6)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss depth (63d slope) — slower loss-deepening
def f23ne_f23_negative_earnings_persistence_lossdepth_63d_slope_v055_signal(netinc):
    base = _lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn depth (63d slope)
def f23ne_f23_negative_earnings_persistence_burndepth_63d_slope_v056_signal(ncfo):
    base = _lossdepth(ncfo, 1e7).rolling(63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss-persistence YoY level (63d slope)
def f23ne_f23_negative_earnings_persistence_lossyoy_63d_slope_v057_signal(netinc):
    lf = _losscount(netinc, 252)
    base = lf - lf.shift(252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deep-loss regime fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_deepreg_21d_slope_v058_signal(netinc, ebit):
    base = ((netinc < 0) & (ebit < 0)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of any-loss regime fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_anyloss_21d_slope_v059_signal(netinc, ncfo, ebit):
    base = ((netinc < 0) | (ncfo < 0) | (ebit < 0)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss persistence EWM (21d slope)
def f23ne_f23_negative_earnings_persistence_epsema_21d_slope_v060_signal(eps):
    base = _losscount(eps, 126).ewm(span=63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS cumulative loss (63d slope) — slower per-share loss-load velocity
def f23ne_f23_negative_earnings_persistence_epscum_21d_slope_v061_signal(eps):
    base = (-eps).clip(lower=0.0).rolling(252, min_periods=126).sum()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dry-spell fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_dryfrac_21d_slope_v062_signal(eps):
    frac = (_time_since_profit(eps) / 252.0).clip(upper=1.0)
    base = frac.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of below-median deficit-time fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_belowmed_21d_slope_v063_signal(retearn):
    med = retearn.rolling(504, min_periods=252).median()
    base = (retearn < med).astype(float).rolling(252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT mean-sign (63d slope) — slower operating-sign tendency velocity
def f23ne_f23_negative_earnings_persistence_ebitsign_21d_slope_v064_signal(ebit):
    base = np.sign(ebit).rolling(126, min_periods=63).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS mean-sign (63d slope)
def f23ne_f23_negative_earnings_persistence_epssign_63d_slope_v065_signal(eps):
    base = np.sign(eps).rolling(504, min_periods=252).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of total value destroyed (cash + accrual) (21d slope)
def f23ne_f23_negative_earnings_persistence_totaldestr_21d_slope_v066_signal(netinc, ncfo):
    nl = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    cb = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).sum()
    base = np.log1p((nl + cb) / 1e7)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of streak balance (5d slope)
def f23ne_f23_negative_earnings_persistence_streakbal_5d_slope_v067_signal(netinc):
    ps = _streak_profit(netinc)
    ls = _streak_loss(netinc)
    base = (ps - ls) / (ps + ls + 1.0)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss-depth (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitdepth21_21d_slope_v068_signal(ebit):
    base = _lossdepth(ebit, 1e7).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-vs-net loss-persistence term spread (21d slope) — cross-flow term velocity
def f23ne_f23_negative_earnings_persistence_lossterm_21d_slope_v069_signal(netinc, ebit):
    base = _losscount(ebit, 63) - _losscount(netinc, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence term structure (21d slope)
def f23ne_f23_negative_earnings_persistence_burnterm_21d_slope_v070_signal(ncfo):
    base = _losscount(ncfo, 21) - _losscount(ncfo, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of compounding-distress regime (21d slope)
def f23ne_f23_negative_earnings_persistence_compdist_21d_slope_v071_signal(netinc, retearn):
    base = ((netinc < 0) & (retearn < retearn.shift(63))).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of quad-loss regime fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_quad_21d_slope_v072_signal(netinc, ncfo, ebit, eps):
    base = ((netinc < 0) & (ncfo < 0) & (ebit < 0) & (eps < 0)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence ratio short/long (5d slope) — fast ratio velocity
def f23ne_f23_negative_earnings_persistence_lossratio_21d_slope_v073_signal(netinc):
    s = _losscount(netinc, 42)
    l = _losscount(netinc, 252)
    base = (s + 0.05) / (l + 0.05) - 1.0
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss persistence ratio (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitratio_21d_slope_v074_signal(ebit):
    s = _losscount(ebit, 63)
    l = _losscount(ebit, 252)
    base = (s + 0.05) / (l + 0.05) - 1.0
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings z-score (21d slope)
def f23ne_f23_negative_earnings_persistence_retz_21d_slope_v075_signal(retearn):
    base = _z(retearn, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence (5d slope, 63d base) — fast acute velocity
def f23ne_f23_negative_earnings_persistence_lossfast_5d_slope_v076_signal(netinc):
    base = _losscount(netinc, 63)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence (5d slope, 63d base)
def f23ne_f23_negative_earnings_persistence_burnfast_5d_slope_v077_signal(ncfo):
    base = _losscount(ncfo, 63)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss depth fast (5d slope)
def f23ne_f23_negative_earnings_persistence_depthfast_5d_slope_v078_signal(netinc):
    base = _lossdepth(netinc, 1e7).rolling(21, min_periods=10).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed net income raw (5d slope) — fast earnings velocity
def f23ne_f23_negative_earnings_persistence_nilevel_5d_slope_v079_signal(netinc):
    base = np.sign(netinc) * np.log1p(netinc.abs() / 1e6)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of signed ncfo raw (5d slope)
def f23ne_f23_negative_earnings_persistence_ncfolevel_5d_slope_v080_signal(ncfo):
    base = np.sign(ncfo) * np.log1p(ncfo.abs() / 1e6)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS raw level (5d slope)
def f23ne_f23_negative_earnings_persistence_epslevel_5d_slope_v081_signal(eps):
    base = np.sign(eps) * np.log1p(eps.abs())
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT raw level (5d slope)
def f23ne_f23_negative_earnings_persistence_ebitlevel_5d_slope_v082_signal(ebit):
    base = np.sign(ebit) * np.log1p(ebit.abs() / 1e6)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence rank (21d slope)
def f23ne_f23_negative_earnings_persistence_lossrank_21d_slope_v083_signal(netinc):
    base = _rank(_losscount(netinc, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-depth rank (21d slope)
def f23ne_f23_negative_earnings_persistence_burndrank_21d_slope_v084_signal(ncfo):
    bd = _lossdepth(ncfo, 1e7).rolling(126, min_periods=63).mean()
    base = _rank(bd, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit-vs-runrate ratio (63d slope)
def f23ne_f23_negative_earnings_persistence_defvsrun_63d_slope_v085_signal(retearn, netinc):
    deficit = (-retearn).clip(lower=0.0)
    run = _lossdepth(netinc, 1.0).rolling(252, min_periods=126).mean() * 252.0
    base = np.log1p(deficit / (run + 1e6))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss-vs-deficit ratio (21d slope)
def f23ne_f23_negative_earnings_persistence_lossvsdef_21d_slope_v086_signal(netinc, retearn):
    lossann = _lossdepth(netinc, 1.0).rolling(252, min_periods=126).mean()
    base = lossann / (retearn.abs() + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-ncfo loss gap (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitncfo_21d_slope_v087_signal(ebit, ncfo):
    eloss = _lossdepth(ebit, 1e7)
    bloss = _lossdepth(ncfo, 1e7)
    base = (eloss - bloss).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of swing-weighted net-income flip intensity (21d slope)
def f23ne_f23_negative_earnings_persistence_niflips_21d_slope_v088_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1))).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    sd = netinc.rolling(63, min_periods=21).std()
    lvl = netinc.abs().rolling(252, min_periods=126).mean()
    base = cnt + 30.0 * sd / (lvl + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-depth-weighted ncfo flip intensity (21d slope)
def f23ne_f23_negative_earnings_persistence_ncfoflips_21d_slope_v089_signal(ncfo):
    flip = (np.sign(ncfo) != np.sign(ncfo.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).sum()
    depth = _lossdepth(ncfo, 1e7).rolling(126, min_periods=63).mean()
    base = cnt + 10.0 * depth
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depth-weighted loss-entry load (21d slope)
def f23ne_f23_negative_earnings_persistence_lossentry_21d_slope_v090_signal(netinc):
    loss = _isloss(netinc)
    entries = ((loss == 1) & (loss.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    depth = _lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    base = cnt + 3.0 * depth
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn-persistence-tilted exit load (21d slope)
def f23ne_f23_negative_earnings_persistence_burnexit_21d_slope_v091_signal(ncfo):
    burn = _isloss(ncfo)
    exits = ((burn == 0) & (burn.shift(1) == 1)).astype(float)
    cnt = exits.rolling(504, min_periods=252).sum()
    persist = _losscount(ncfo, 126)
    base = cnt - 5.0 * persist
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence vol (21d slope)
def f23ne_f23_negative_earnings_persistence_lossvol_21d_slope_v092_signal(netinc):
    base = _losscount(netinc, 63).rolling(252, min_periods=126).std()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT swing amplitude (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitswing_21d_slope_v093_signal(ebit):
    sd = ebit.rolling(252, min_periods=126).std()
    lvl = ebit.abs().rolling(252, min_periods=126).mean()
    base = sd / (lvl + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of chronic-loss (time x depth) (21d slope)
def f23ne_f23_negative_earnings_persistence_chronic_21d_slope_v094_signal(netinc):
    t = _time_since_profit(netinc) / 252.0
    d = _lossdepth(netinc, 1e7)
    base = (t * d).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of chronic-burn (time x depth) (21d slope)
def f23ne_f23_negative_earnings_persistence_chronicburn_21d_slope_v095_signal(ncfo):
    t = _time_since_profit(ncfo) / 252.0
    d = _lossdepth(ncfo, 1e7)
    base = (t * d).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS chronic (dry x depth) (21d slope)
def f23ne_f23_negative_earnings_persistence_epschronic_21d_slope_v096_signal(eps):
    t = _time_since_profit(eps) / 252.0
    d = (-eps).clip(lower=0.0)
    base = (t * d).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings recovery healing rate (21d slope)
def f23ne_f23_negative_earnings_persistence_heal_21d_slope_v097_signal(retearn):
    trough = _rmin(retearn, 504)
    base = ((retearn - trough) / (trough.abs() + 1e6)).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of grand distress score (21d slope)
def f23ne_f23_negative_earnings_persistence_grand_21d_slope_v098_signal(netinc, ncfo, ebit, retearn):
    a = _losscount(netinc, 252)
    c = _losscount(ncfo, 252)
    e = _losscount(ebit, 252)
    dg = (retearn < retearn.shift(126)).astype(float).rolling(126, min_periods=63).mean()
    base = 0.3 * a + 0.25 * c + 0.25 * e + 0.2 * dg
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of distress composite (21d slope)
def f23ne_f23_negative_earnings_persistence_distcomp_21d_slope_v099_signal(netinc, ncfo, retearn):
    a = _losscount(netinc, 252)
    c = _losscount(ncfo, 252)
    dry = (_time_since_profit(netinc) / 252.0).clip(upper=2.0) / 2.0
    dg = (retearn < retearn.shift(126)).astype(float).rolling(126, min_periods=63).mean()
    base = 0.3 * a + 0.3 * c + 0.2 * dry + 0.2 * dg
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of operating-distress composite (21d slope)
def f23ne_f23_negative_earnings_persistence_opdist_21d_slope_v100_signal(ebit):
    lf = _losscount(ebit, 252)
    depth = np.tanh(_lossdepth(ebit, 1e7).rolling(63, min_periods=21).mean())
    base = 0.6 * lf + 0.4 * depth
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence (5d slope, 252d base)
def f23ne_f23_negative_earnings_persistence_loss5_5d_slope_v101_signal(netinc):
    base = _losscount(netinc, 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence (5d slope, 252d base)
def f23ne_f23_negative_earnings_persistence_burn5_5d_slope_v102_signal(ncfo):
    base = _losscount(ncfo, 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit depth (5d slope)
def f23ne_f23_negative_earnings_persistence_defdepth5_5d_slope_v103_signal(retearn):
    base = np.log1p((-retearn).clip(lower=0.0) / 1e6)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of time-since-EBIT-profit (21d slope)
def f23ne_f23_negative_earnings_persistence_tsebit_21d_slope_v104_signal(ebit):
    base = np.log1p(_time_since_profit(ebit).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of time-since-EPS-profit (21d slope)
def f23ne_f23_negative_earnings_persistence_tseps_21d_slope_v105_signal(eps):
    base = np.log1p(_time_since_profit(eps).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss-streak (5d slope)
def f23ne_f23_negative_earnings_persistence_ebitstreak_5d_slope_v106_signal(ebit):
    base = _streak_loss(ebit)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss-streak (5d slope)
def f23ne_f23_negative_earnings_persistence_epsstreak_5d_slope_v107_signal(eps):
    base = _streak_loss(eps)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence displacement (5d slope) — fast displacement velocity
def f23ne_f23_negative_earnings_persistence_lossdisp_21d_slope_v108_signal(netinc):
    lf = _losscount(netinc, 126)
    base = lf - lf.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-income semidev rank (21d slope)
def f23ne_f23_negative_earnings_persistence_semidevrank_21d_slope_v109_signal(netinc):
    neg = netinc.where(netinc < 0, 0.0)
    sd = neg.rolling(252, min_periods=126).std() / 1e6
    base = _rank(sd, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss depth relative level (21d slope)
def f23ne_f23_negative_earnings_persistence_depthrel_21d_slope_v110_signal(netinc):
    d = _lossdepth(netinc, 1.0)
    typ = d.rolling(252, min_periods=126).mean()
    base = d / (typ + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit gated by burn persistence (21d slope) — burn-gated deficit velocity
def f23ne_f23_negative_earnings_persistence_defgated_21d_slope_v111_signal(retearn, ncfo):
    deficit = np.log1p((-retearn).clip(lower=0.0) / 1e6)
    bf = _losscount(ncfo, 126)
    base = deficit * bf
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit gated by burn (21d slope)
def f23ne_f23_negative_earnings_persistence_defburngate_21d_slope_v112_signal(retearn, ncfo):
    dg = np.tanh(_deficit_growth(retearn, 126) / 1e6)
    bf = _losscount(ncfo, 126)
    base = dg * bf
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence x deficit drawdown (63d slope)
def f23ne_f23_negative_earnings_persistence_persxdraw_21d_slope_v113_signal(netinc, retearn):
    lf = _losscount(netinc, 252)
    peak = _rmax(retearn, 504)
    dd = (retearn - peak) / (peak.abs() + 1e6)
    base = lf * dd
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cumulative EBIT loss (21d slope)
def f23ne_f23_negative_earnings_persistence_cumebit_21d_slope_v114_signal(ebit):
    base = np.log1p((-ebit).clip(lower=0.0).rolling(252, min_periods=126).sum() / 1e7)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-destroyed (loss-profit) (63d slope)
def f23ne_f23_negative_earnings_persistence_netdestr_63d_slope_v115_signal(netinc):
    loss = (-netinc).clip(lower=0.0).rolling(504, min_periods=252).sum()
    prof = netinc.clip(lower=0.0).rolling(504, min_periods=252).sum()
    base = np.sign(loss - prof) * np.log1p((loss - prof).abs() / 1e7)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence position (63d slope)
def f23ne_f23_negative_earnings_persistence_losspos_63d_slope_v116_signal(netinc):
    lf = _losscount(netinc, 126)
    hi = _rmax(lf, 504)
    lo = _rmin(lf, 504)
    base = (lf - lo) / (hi - lo).replace(0, np.nan) - 0.5
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence position (63d slope)
def f23ne_f23_negative_earnings_persistence_burnpos_63d_slope_v117_signal(ncfo):
    bf = _losscount(ncfo, 126)
    hi = _rmax(bf, 504)
    lo = _rmin(bf, 504)
    base = (bf - lo) / (hi - lo).replace(0, np.nan) - 0.5
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss-depth z-rank (21d slope)
def f23ne_f23_negative_earnings_persistence_depthrank_21d_slope_v118_signal(netinc):
    d = _lossdepth(netinc, 1e7).rolling(21, min_periods=10).mean()
    base = _rank(d, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of profitable streak balance smoothed (21d slope)
def f23ne_f23_negative_earnings_persistence_streakbalsm_21d_slope_v119_signal(netinc):
    ps = _streak_profit(netinc)
    ls = _streak_loss(netinc)
    base = ((ps - ls) / (ps + ls + 1.0)).rolling(21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss persistence (5d slope, 126d base)
def f23ne_f23_negative_earnings_persistence_ebitfast_5d_slope_v120_signal(ebit):
    base = _losscount(ebit, 126)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss persistence (5d slope, 126d base)
def f23ne_f23_negative_earnings_persistence_epsfast_5d_slope_v121_signal(eps):
    base = _losscount(eps, 126)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit-growth z (63d slope) — slower deficit-growth regime velocity
def f23ne_f23_negative_earnings_persistence_defgrz_21d_slope_v122_signal(retearn):
    base = _z(_deficit_growth(retearn, 126), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss persistence (126d slope, 504d base) — very slow chronic velocity
def f23ne_f23_negative_earnings_persistence_lossslow_126d_slope_v123_signal(netinc):
    base = _losscount(netinc, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence (126d slope, 504d base)
def f23ne_f23_negative_earnings_persistence_burnslow_126d_slope_v124_signal(ncfo):
    base = _losscount(ncfo, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit depth (126d slope)
def f23ne_f23_negative_earnings_persistence_defslow_126d_slope_v125_signal(retearn):
    base = np.log1p((-retearn).clip(lower=0.0) / 1e6)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWM net-loss depth (21d slope)
def f23ne_f23_negative_earnings_persistence_depthema_21d_slope_v126_signal(netinc):
    base = _lossdepth(netinc, 1e7).ewm(span=84, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-loss-depth surge (21d slope)
def f23ne_f23_negative_earnings_persistence_depthsurge_21d_slope_v127_signal(netinc):
    d = _lossdepth(netinc, 1e7)
    base = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of cross-flow loss dispersion (63d slope)
def f23ne_f23_negative_earnings_persistence_lossdispf_21d_slope_v128_signal(netinc, ncfo, ebit):
    a = _losscount(netinc, 252)
    c = _losscount(ncfo, 252)
    d = _losscount(ebit, 252)
    base = pd.concat([a, c, d], axis=1).std(axis=1)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of below-line gap (21d slope)
def f23ne_f23_negative_earnings_persistence_belowline_21d_slope_v129_signal(ebit, netinc):
    base = _losscount(ebit, 252) - _losscount(netinc, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT-EPS sign agreement (21d slope)
def f23ne_f23_negative_earnings_persistence_signagree2_21d_slope_v130_signal(ebit, eps):
    base = (np.sign(ebit) == np.sign(eps)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-income mean-sign (126d slope) — very slow sign-tendency velocity
def f23ne_f23_negative_earnings_persistence_nimeansign_63d_slope_v131_signal(netinc):
    base = np.sign(netinc).rolling(252, min_periods=126).mean()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ncfo mean-sign (63d slope)
def f23ne_f23_negative_earnings_persistence_ncfomeansign_63d_slope_v132_signal(ncfo):
    base = np.sign(ncfo).rolling(252, min_periods=126).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss persistence YoY (21d slope)
def f23ne_f23_negative_earnings_persistence_lossyoy_21d_slope_v133_signal(netinc):
    lf = _losscount(netinc, 252)
    base = lf - lf.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn persistence YoY (21d slope)
def f23ne_f23_negative_earnings_persistence_burnyoy_21d_slope_v134_signal(ncfo):
    bf = _losscount(ncfo, 252)
    base = bf - bf.shift(252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss dominance momentum (21d slope)
def f23ne_f23_negative_earnings_persistence_dommom_21d_slope_v135_signal(netinc):
    loss = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    prof = netinc.clip(lower=0.0).rolling(252, min_periods=126).sum()
    dom = (loss - prof) / (loss + prof + 1e6)
    base = dom - dom.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of burn concentration (21d slope)
def f23ne_f23_negative_earnings_persistence_burnconc_21d_slope_v136_signal(ncfo):
    burn = (-ncfo).clip(lower=0.0)
    yr = burn.rolling(252, min_periods=126).sum()
    worstq = burn.rolling(63, min_periods=21).sum().rolling(252, min_periods=126).max()
    base = worstq / (yr + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT loss-depth relative to its typical depth (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitdv_21d_slope_v137_signal(ebit):
    d = _lossdepth(ebit, 1.0)
    typ = d.rolling(252, min_periods=126).mean()
    base = d.rolling(21, min_periods=10).mean() / (typ + 1e6)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss-depth EWM (21d slope) — per-share loss-size velocity
def f23ne_f23_negative_earnings_persistence_epssmz_21d_slope_v138_signal(eps):
    base = (-eps).clip(lower=0.0).ewm(span=84, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT signed-magnitude displacement (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitsmdisp_21d_slope_v139_signal(ebit):
    sm = _signmag(ebit, 1e6)
    base = sm - sm.ewm(span=84, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net signed-magnitude minus its slow EMA (signed-intensity displacement velocity)
def f23ne_f23_negative_earnings_persistence_nismsm21_21d_slope_v140_signal(netinc):
    sm = _signmag(netinc, 1e6)
    base = sm.ewm(span=21, min_periods=10).mean() - sm.ewm(span=126, min_periods=42).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of deficit-build fraction (21d slope)
def f23ne_f23_negative_earnings_persistence_defbuild_21d_slope_v141_signal(retearn):
    base = (retearn < retearn.shift(1)).astype(float).rolling(
        252, min_periods=126).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of loss count month-vs-quarter (5d slope) — fast acute-vs-quarter velocity
def f23ne_f23_negative_earnings_persistence_losscntdiff_21d_slope_v142_signal(netinc):
    s = _losssum(netinc, 21) / 21.0
    l = _losssum(netinc, 63) / 63.0
    base = s - l
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EPS loss persistence term (21d slope)
def f23ne_f23_negative_earnings_persistence_epsterm_21d_slope_v143_signal(eps):
    base = _losscount(eps, 126) - _losscount(eps, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of worst-burn rank (21d slope)
def f23ne_f23_negative_earnings_persistence_worstburn_21d_slope_v144_signal(ncfo):
    worst = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).max()
    base = _rank(worst, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of replenishment-burden rank (21d slope)
def f23ne_f23_negative_earnings_persistence_replen_21d_slope_v145_signal(netinc, retearn):
    loss = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    ratio = loss / ((-retearn).clip(lower=0.0) + 1e6)
    base = _rank(ratio, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of depth spread (netinc vs ebit) (21d slope)
def f23ne_f23_negative_earnings_persistence_depthspr_21d_slope_v146_signal(netinc, ebit):
    dn = _lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    de = _lossdepth(ebit, 1e7).rolling(63, min_periods=21).mean()
    base = dn - de
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of net-income value level smoothed (63d slope) — slower signed-level velocity
def f23ne_f23_negative_earnings_persistence_nivalsm_21d_slope_v147_signal(netinc):
    base = (np.sign(netinc) * np.log1p(netinc.abs() / 1e6)).rolling(
        63, min_periods=21).mean()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EBIT value level smoothed (21d slope)
def f23ne_f23_negative_earnings_persistence_ebitvalsm_21d_slope_v148_signal(ebit):
    base = (np.sign(ebit) * np.log1p(ebit.abs() / 1e6)).rolling(
        21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of dry-spell trend (21d slope)
def f23ne_f23_negative_earnings_persistence_drytrend_21d_slope_v149_signal(netinc):
    t = _time_since_profit(netinc)
    base = np.tanh((t - t.shift(63)) / 63.0)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of retained-earnings velocity acceleration base (21d slope)
def f23ne_f23_negative_earnings_persistence_retvel_21d_slope_v150_signal(retearn):
    base = _slope(retearn, 63) / 1e6
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23ne_f23_negative_earnings_persistence_lossfrac_21d_slope_v001_signal,
    f23ne_f23_negative_earnings_persistence_burnfrac_21d_slope_v002_signal,
    f23ne_f23_negative_earnings_persistence_ebitlossfrac_21d_slope_v003_signal,
    f23ne_f23_negative_earnings_persistence_epslossfrac_21d_slope_v004_signal,
    f23ne_f23_negative_earnings_persistence_lossfrac126_21d_slope_v005_signal,
    f23ne_f23_negative_earnings_persistence_burnfrac126_21d_slope_v006_signal,
    f23ne_f23_negative_earnings_persistence_lossdepth_21d_slope_v007_signal,
    f23ne_f23_negative_earnings_persistence_burndepth_21d_slope_v008_signal,
    f23ne_f23_negative_earnings_persistence_ebitdepth_21d_slope_v009_signal,
    f23ne_f23_negative_earnings_persistence_tsprofit_21d_slope_v010_signal,
    f23ne_f23_negative_earnings_persistence_tsburn_21d_slope_v011_signal,
    f23ne_f23_negative_earnings_persistence_deficitdepth_21d_slope_v012_signal,
    f23ne_f23_negative_earnings_persistence_nisignmag_21d_slope_v013_signal,
    f23ne_f23_negative_earnings_persistence_ebitsignmag_21d_slope_v014_signal,
    f23ne_f23_negative_earnings_persistence_epssignmag_21d_slope_v015_signal,
    f23ne_f23_negative_earnings_persistence_lossstreak_5d_slope_v016_signal,
    f23ne_f23_negative_earnings_persistence_burnstreak_5d_slope_v017_signal,
    f23ne_f23_negative_earnings_persistence_profstreak_5d_slope_v018_signal,
    f23ne_f23_negative_earnings_persistence_retearn_63d_slope_v019_signal,
    f23ne_f23_negative_earnings_persistence_cumloss_21d_slope_v020_signal,
    f23ne_f23_negative_earnings_persistence_cumburn_21d_slope_v021_signal,
    f23ne_f23_negative_earnings_persistence_lossdom_21d_slope_v022_signal,
    f23ne_f23_negative_earnings_persistence_burndom_21d_slope_v023_signal,
    f23ne_f23_negative_earnings_persistence_breadth_21d_slope_v024_signal,
    f23ne_f23_negative_earnings_persistence_triple_21d_slope_v025_signal,
    f23ne_f23_negative_earnings_persistence_lossz_21d_slope_v026_signal,
    f23ne_f23_negative_earnings_persistence_epsrank_21d_slope_v027_signal,
    f23ne_f23_negative_earnings_persistence_retdd_21d_slope_v028_signal,
    f23ne_f23_negative_earnings_persistence_retrec_21d_slope_v029_signal,
    f23ne_f23_negative_earnings_persistence_meansign_21d_slope_v030_signal,
    f23ne_f23_negative_earnings_persistence_ebitrel_21d_slope_v031_signal,
    f23ne_f23_negative_earnings_persistence_accrgap_21d_slope_v032_signal,
    f23ne_f23_negative_earnings_persistence_defgr_21d_slope_v033_signal,
    f23ne_f23_negative_earnings_persistence_proffrac_21d_slope_v034_signal,
    f23ne_f23_negative_earnings_persistence_lossema_21d_slope_v035_signal,
    f23ne_f23_negative_earnings_persistence_burnema_21d_slope_v036_signal,
    f23ne_f23_negative_earnings_persistence_avgneg_21d_slope_v037_signal,
    f23ne_f23_negative_earnings_persistence_semidev_21d_slope_v038_signal,
    f23ne_f23_negative_earnings_persistence_niswing_21d_slope_v039_signal,
    f23ne_f23_negative_earnings_persistence_losspos_21d_slope_v040_signal,
    f23ne_f23_negative_earnings_persistence_worstloss_21d_slope_v041_signal,
    f23ne_f23_negative_earnings_persistence_lossconc_21d_slope_v042_signal,
    f23ne_f23_negative_earnings_persistence_signagree_21d_slope_v043_signal,
    f23ne_f23_negative_earnings_persistence_selffund_21d_slope_v044_signal,
    f23ne_f23_negative_earnings_persistence_lossfrac_63d_slope_v045_signal,
    f23ne_f23_negative_earnings_persistence_burnfrac_63d_slope_v046_signal,
    f23ne_f23_negative_earnings_persistence_ebitfrac_63d_slope_v047_signal,
    f23ne_f23_negative_earnings_persistence_defbuild_63d_slope_v048_signal,
    f23ne_f23_negative_earnings_persistence_defdepth_63d_slope_v049_signal,
    f23ne_f23_negative_earnings_persistence_cumloss_63d_slope_v050_signal,
    f23ne_f23_negative_earnings_persistence_tsni_63d_slope_v051_signal,
    f23ne_f23_negative_earnings_persistence_nismsm_63d_slope_v052_signal,
    f23ne_f23_negative_earnings_persistence_ebitsm_63d_slope_v053_signal,
    f23ne_f23_negative_earnings_persistence_retearn_126d_slope_v054_signal,
    f23ne_f23_negative_earnings_persistence_lossdepth_63d_slope_v055_signal,
    f23ne_f23_negative_earnings_persistence_burndepth_63d_slope_v056_signal,
    f23ne_f23_negative_earnings_persistence_lossyoy_63d_slope_v057_signal,
    f23ne_f23_negative_earnings_persistence_deepreg_21d_slope_v058_signal,
    f23ne_f23_negative_earnings_persistence_anyloss_21d_slope_v059_signal,
    f23ne_f23_negative_earnings_persistence_epsema_21d_slope_v060_signal,
    f23ne_f23_negative_earnings_persistence_epscum_21d_slope_v061_signal,
    f23ne_f23_negative_earnings_persistence_dryfrac_21d_slope_v062_signal,
    f23ne_f23_negative_earnings_persistence_belowmed_21d_slope_v063_signal,
    f23ne_f23_negative_earnings_persistence_ebitsign_21d_slope_v064_signal,
    f23ne_f23_negative_earnings_persistence_epssign_63d_slope_v065_signal,
    f23ne_f23_negative_earnings_persistence_totaldestr_21d_slope_v066_signal,
    f23ne_f23_negative_earnings_persistence_streakbal_5d_slope_v067_signal,
    f23ne_f23_negative_earnings_persistence_ebitdepth21_21d_slope_v068_signal,
    f23ne_f23_negative_earnings_persistence_lossterm_21d_slope_v069_signal,
    f23ne_f23_negative_earnings_persistence_burnterm_21d_slope_v070_signal,
    f23ne_f23_negative_earnings_persistence_compdist_21d_slope_v071_signal,
    f23ne_f23_negative_earnings_persistence_quad_21d_slope_v072_signal,
    f23ne_f23_negative_earnings_persistence_lossratio_21d_slope_v073_signal,
    f23ne_f23_negative_earnings_persistence_ebitratio_21d_slope_v074_signal,
    f23ne_f23_negative_earnings_persistence_retz_21d_slope_v075_signal,
    f23ne_f23_negative_earnings_persistence_lossfast_5d_slope_v076_signal,
    f23ne_f23_negative_earnings_persistence_burnfast_5d_slope_v077_signal,
    f23ne_f23_negative_earnings_persistence_depthfast_5d_slope_v078_signal,
    f23ne_f23_negative_earnings_persistence_nilevel_5d_slope_v079_signal,
    f23ne_f23_negative_earnings_persistence_ncfolevel_5d_slope_v080_signal,
    f23ne_f23_negative_earnings_persistence_epslevel_5d_slope_v081_signal,
    f23ne_f23_negative_earnings_persistence_ebitlevel_5d_slope_v082_signal,
    f23ne_f23_negative_earnings_persistence_lossrank_21d_slope_v083_signal,
    f23ne_f23_negative_earnings_persistence_burndrank_21d_slope_v084_signal,
    f23ne_f23_negative_earnings_persistence_defvsrun_63d_slope_v085_signal,
    f23ne_f23_negative_earnings_persistence_lossvsdef_21d_slope_v086_signal,
    f23ne_f23_negative_earnings_persistence_ebitncfo_21d_slope_v087_signal,
    f23ne_f23_negative_earnings_persistence_niflips_21d_slope_v088_signal,
    f23ne_f23_negative_earnings_persistence_ncfoflips_21d_slope_v089_signal,
    f23ne_f23_negative_earnings_persistence_lossentry_21d_slope_v090_signal,
    f23ne_f23_negative_earnings_persistence_burnexit_21d_slope_v091_signal,
    f23ne_f23_negative_earnings_persistence_lossvol_21d_slope_v092_signal,
    f23ne_f23_negative_earnings_persistence_ebitswing_21d_slope_v093_signal,
    f23ne_f23_negative_earnings_persistence_chronic_21d_slope_v094_signal,
    f23ne_f23_negative_earnings_persistence_chronicburn_21d_slope_v095_signal,
    f23ne_f23_negative_earnings_persistence_epschronic_21d_slope_v096_signal,
    f23ne_f23_negative_earnings_persistence_heal_21d_slope_v097_signal,
    f23ne_f23_negative_earnings_persistence_grand_21d_slope_v098_signal,
    f23ne_f23_negative_earnings_persistence_distcomp_21d_slope_v099_signal,
    f23ne_f23_negative_earnings_persistence_opdist_21d_slope_v100_signal,
    f23ne_f23_negative_earnings_persistence_loss5_5d_slope_v101_signal,
    f23ne_f23_negative_earnings_persistence_burn5_5d_slope_v102_signal,
    f23ne_f23_negative_earnings_persistence_defdepth5_5d_slope_v103_signal,
    f23ne_f23_negative_earnings_persistence_tsebit_21d_slope_v104_signal,
    f23ne_f23_negative_earnings_persistence_tseps_21d_slope_v105_signal,
    f23ne_f23_negative_earnings_persistence_ebitstreak_5d_slope_v106_signal,
    f23ne_f23_negative_earnings_persistence_epsstreak_5d_slope_v107_signal,
    f23ne_f23_negative_earnings_persistence_lossdisp_21d_slope_v108_signal,
    f23ne_f23_negative_earnings_persistence_semidevrank_21d_slope_v109_signal,
    f23ne_f23_negative_earnings_persistence_depthrel_21d_slope_v110_signal,
    f23ne_f23_negative_earnings_persistence_defgated_21d_slope_v111_signal,
    f23ne_f23_negative_earnings_persistence_defburngate_21d_slope_v112_signal,
    f23ne_f23_negative_earnings_persistence_persxdraw_21d_slope_v113_signal,
    f23ne_f23_negative_earnings_persistence_cumebit_21d_slope_v114_signal,
    f23ne_f23_negative_earnings_persistence_netdestr_63d_slope_v115_signal,
    f23ne_f23_negative_earnings_persistence_losspos_63d_slope_v116_signal,
    f23ne_f23_negative_earnings_persistence_burnpos_63d_slope_v117_signal,
    f23ne_f23_negative_earnings_persistence_depthrank_21d_slope_v118_signal,
    f23ne_f23_negative_earnings_persistence_streakbalsm_21d_slope_v119_signal,
    f23ne_f23_negative_earnings_persistence_ebitfast_5d_slope_v120_signal,
    f23ne_f23_negative_earnings_persistence_epsfast_5d_slope_v121_signal,
    f23ne_f23_negative_earnings_persistence_defgrz_21d_slope_v122_signal,
    f23ne_f23_negative_earnings_persistence_lossslow_126d_slope_v123_signal,
    f23ne_f23_negative_earnings_persistence_burnslow_126d_slope_v124_signal,
    f23ne_f23_negative_earnings_persistence_defslow_126d_slope_v125_signal,
    f23ne_f23_negative_earnings_persistence_depthema_21d_slope_v126_signal,
    f23ne_f23_negative_earnings_persistence_depthsurge_21d_slope_v127_signal,
    f23ne_f23_negative_earnings_persistence_lossdispf_21d_slope_v128_signal,
    f23ne_f23_negative_earnings_persistence_belowline_21d_slope_v129_signal,
    f23ne_f23_negative_earnings_persistence_signagree2_21d_slope_v130_signal,
    f23ne_f23_negative_earnings_persistence_nimeansign_63d_slope_v131_signal,
    f23ne_f23_negative_earnings_persistence_ncfomeansign_63d_slope_v132_signal,
    f23ne_f23_negative_earnings_persistence_lossyoy_21d_slope_v133_signal,
    f23ne_f23_negative_earnings_persistence_burnyoy_21d_slope_v134_signal,
    f23ne_f23_negative_earnings_persistence_dommom_21d_slope_v135_signal,
    f23ne_f23_negative_earnings_persistence_burnconc_21d_slope_v136_signal,
    f23ne_f23_negative_earnings_persistence_ebitdv_21d_slope_v137_signal,
    f23ne_f23_negative_earnings_persistence_epssmz_21d_slope_v138_signal,
    f23ne_f23_negative_earnings_persistence_ebitsmdisp_21d_slope_v139_signal,
    f23ne_f23_negative_earnings_persistence_nismsm21_21d_slope_v140_signal,
    f23ne_f23_negative_earnings_persistence_defbuild_21d_slope_v141_signal,
    f23ne_f23_negative_earnings_persistence_losscntdiff_21d_slope_v142_signal,
    f23ne_f23_negative_earnings_persistence_epsterm_21d_slope_v143_signal,
    f23ne_f23_negative_earnings_persistence_worstburn_21d_slope_v144_signal,
    f23ne_f23_negative_earnings_persistence_replen_21d_slope_v145_signal,
    f23ne_f23_negative_earnings_persistence_depthspr_21d_slope_v146_signal,
    f23ne_f23_negative_earnings_persistence_nivalsm_21d_slope_v147_signal,
    f23ne_f23_negative_earnings_persistence_ebitvalsm_21d_slope_v148_signal,
    f23ne_f23_negative_earnings_persistence_drytrend_21d_slope_v149_signal,
    f23ne_f23_negative_earnings_persistence_retvel_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_NEGATIVE_EARNINGS_PERSISTENCE_REGISTRY_2ND_001_150 = REGISTRY


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

    def _swing(seed, seed2, base, vol, amp, period):
        raw = _fund(seed, base=base, vol=vol, allow_neg=True)
        center = raw - raw.rolling(252, min_periods=1).mean()
        t = np.arange(n)
        wob = amp * base * np.sin(2.0 * np.pi * t / period)
        nz = _fund(seed2, base=base, vol=vol, allow_neg=True)
        nz = (nz - nz.rolling(252, min_periods=1).mean()) * 0.5
        return center + wob + nz

    netinc = _swing(2301, 2311, 4.0e7, 0.30, 0.50, 80).rename("netinc")
    ncfo = _swing(2302, 2312, 3.5e7, 0.28, 0.50, 95).rename("ncfo")
    eps = _swing(2303, 2313, 2.0, 0.32, 0.50, 70).rename("eps")
    ebit = _swing(2304, 2314, 4.5e7, 0.27, 0.50, 110).rename("ebit")
    retearn = _swing(2305, 2315, 8.0e7, 0.18, 0.35, 160).rename("retearn")

    cols = {"netinc": netinc, "ncfo": ncfo, "eps": eps,
            "ebit": ebit, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("netinc", "ncfo", "eps", "ebit", "retearn")
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

    print("OK f23_negative_earnings_persistence_2nd_derivatives_001_150_claude: %d features pass" % n_features)
