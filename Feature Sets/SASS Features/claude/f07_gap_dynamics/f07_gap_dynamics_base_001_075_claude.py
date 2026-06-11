import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (gap dynamics) =====
# All per-day gap quantities use UNADJUSTED open/high/low/close for a SINGLE day.
def _f07_prevclose(close):
    return close.shift(1)


def _f07_gap(openp, close):
    # overnight gap %: open vs prior close
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f07_overnight(openp, close):
    # overnight log return (open vs prior close)
    pc = close.shift(1)
    return np.log(openp.replace(0, np.nan) / pc.replace(0, np.nan))


def _f07_intraday(openp, close):
    # intraday return (close vs same-day open)
    return close / openp.replace(0, np.nan) - 1.0


def _f07_intraday_log(openp, close):
    return np.log(close.replace(0, np.nan) / openp.replace(0, np.nan))


def _f07_gap_fill(openp, high, low, close):
    # fraction of the gap retraced intraday toward prior close.
    # gap-up filled if low pulls back toward prior close; gap-down if high pushes up.
    pc = close.shift(1)
    gap = openp - pc
    # signed distance the day moved back toward prior close from the open
    # for gap up (gap>0): retrace = open - low; for gap down: retrace = high - open
    retrace = np.where(gap > 0, openp - low, high - openp)
    retrace = pd.Series(retrace, index=openp.index)
    return retrace / gap.abs().replace(0, np.nan)


def _f07_gap_continuation(openp, close):
    # does the intraday move continue the gap direction? sign agreement * magnitude
    gap = _f07_gap(openp, close)
    intr = _f07_intraday(openp, close)
    return np.sign(gap) * intr


def _f07_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ============================================================
# raw per-day gap %, smoothed over a week (short window <=5d uses unadjusted OHLC)
def f07gd_f07_gap_dynamics_gap_5d_base_v001_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gap % z-scored vs its own 21d history (gap magnitude z)
def f07gd_f07_gap_dynamics_gapz_21d_base_v002_signal(open, close):
    g = _f07_gap(open, close)
    result = _z(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gap level z-scored vs 63d history (persistent gap regime, not single-day shock)
def f07gd_f07_gap_dynamics_gapz_63d_base_v003_signal(open, close):
    g = _f07_gap(open, close)
    gm = _mean(g, 10)
    result = _z(gm, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap % robust z-score vs 252d history (median/MAD scaled, fat-tail resistant)
def f07gd_f07_gap_dynamics_gapz_252d_base_v004_signal(open, close):
    g = _f07_gap(open, close)
    med = g.rolling(252, min_periods=63).median()
    mad = (g - med).abs().rolling(252, min_periods=63).median()
    result = (g - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up frequency over a month, depth-weighted (fraction + avg up-gap magnitude)
def f07gd_f07_gap_dynamics_upfreq_21d_base_v005_signal(open, close):
    g = _f07_gap(open, close)
    up = (g > 0.002).astype(float)
    freq = up.rolling(21, min_periods=10).mean() - 0.5
    depth = g.clip(lower=0).rolling(21, min_periods=10).mean()
    result = freq + 5.0 * depth
    return result.replace([np.inf, -np.inf], np.nan)


# gap-down frequency over a month, depth-weighted
def f07gd_f07_gap_dynamics_downfreq_21d_base_v006_signal(open, close):
    g = _f07_gap(open, close)
    dn = (g < -0.002).astype(float)
    freq = dn.rolling(21, min_periods=10).mean() - 0.5
    depth = (-g).clip(lower=0).rolling(21, min_periods=10).mean()
    result = freq + 5.0 * depth
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up minus gap-down frequency over a quarter, magnitude-tilted (directional gap bias)
def f07gd_f07_gap_dynamics_dirbias_63d_base_v007_signal(open, close):
    g = _f07_gap(open, close)
    up = (g > 0.002).astype(float)
    dn = (g < -0.002).astype(float)
    freq = (up - dn).rolling(63, min_periods=21).mean()
    tilt = _mean(g, 63)
    result = freq + 8.0 * tilt
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio averaged over a week (how much gaps retrace intraday)
def f07gd_f07_gap_dynamics_fill_5d_base_v008_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close)
    result = _mean(f, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio averaged over a month
def f07gd_f07_gap_dynamics_fill_21d_base_v009_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close)
    result = _mean(f, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio averaged over a quarter
def f07gd_f07_gap_dynamics_fill_63d_base_v010_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close)
    result = _mean(f, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return mean over a month (overnight drift)
def f07gd_f07_gap_dynamics_ovn_21d_base_v011_signal(open, close):
    o = _f07_overnight(open, close)
    result = _mean(o, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over a quarter (sum of overnight log returns)
def f07gd_f07_gap_dynamics_ovncum_63d_base_v012_signal(open, close):
    o = _f07_overnight(open, close)
    result = o.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over a year
def f07gd_f07_gap_dynamics_ovncum_252d_base_v013_signal(open, close):
    o = _f07_overnight(open, close)
    result = o.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return mean over a month (daytime drift)
def f07gd_f07_gap_dynamics_intr_21d_base_v014_signal(open, close):
    i = _f07_intraday(open, close)
    result = _mean(i, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-minus-intraday drift spread over a quarter (where does return accrue)
def f07gd_f07_gap_dynamics_ovnvsintr_63d_base_v015_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    result = o.rolling(63, min_periods=21).sum() - i.rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight share of total return over a quarter (fraction of move from gaps)
def f07gd_f07_gap_dynamics_ovnshare_63d_base_v016_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    co = o.rolling(63, min_periods=21).sum()
    ci = i.rolling(63, min_periods=21).sum()
    result = co / (co.abs() + ci.abs()).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap continuation vs reversal over a month (sign(gap)*intraday)
def f07gd_f07_gap_dynamics_cont_21d_base_v017_signal(open, close):
    c = _f07_gap_continuation(open, close)
    result = _mean(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# gap continuation vs reversal over a quarter
def f07gd_f07_gap_dynamics_cont_63d_base_v018_signal(open, close):
    c = _f07_gap_continuation(open, close)
    result = _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap magnitude mean over a month (typical gap size / overnight vol)
def f07gd_f07_gap_dynamics_absmag_21d_base_v019_signal(open, close):
    g = _f07_gap(open, close).abs()
    result = _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap magnitude mean over a quarter
def f07gd_f07_gap_dynamics_absmag_63d_base_v020_signal(open, close):
    g = _f07_gap(open, close).abs()
    result = _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion (std of gap%) over a quarter (overnight volatility)
def f07gd_f07_gap_dynamics_gapdisp_63d_base_v021_signal(open, close):
    g = _f07_gap(open, close)
    result = _std(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion over a year
def f07gd_f07_gap_dynamics_gapdisp_252d_base_v022_signal(open, close):
    g = _f07_gap(open, close)
    result = _std(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long gap volatility ratio (overnight vol term structure)
def f07gd_f07_gap_dynamics_gapvolratio_base_v023_signal(open, close):
    g = _f07_gap(open, close)
    s = _std(g, 21)
    l = _std(g, 126)
    result = s / l.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# latest gap % z-scored vs 63d then squashed (bounded gap surprise)
def f07gd_f07_gap_dynamics_gapsurprise_63d_base_v024_signal(open, close):
    g = _f07_gap(open, close)
    z = _z(g, 63)
    result = np.tanh(z)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday vol ratio over a quarter (session-risk allocation, not drift)
def f07gd_f07_gap_dynamics_ovnsharpe_63d_base_v025_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    result = _std(o, 63) / _std(i, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight Calmar: 252d cumulative overnight drift over its worst overnight drawdown
def f07gd_f07_gap_dynamics_ovnsharpe_252d_base_v026_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    peak = cum.rolling(252, min_periods=63).max()
    maxdd = (cum - peak).rolling(252, min_periods=63).min().abs()
    drift = o.rolling(252, min_periods=63).sum()
    result = drift / maxdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return skewness over a quarter (daytime asymmetry of close-vs-open moves)
def f07gd_f07_gap_dynamics_intrsharpe_63d_base_v027_signal(open, close):
    i = _f07_intraday(open, close)
    result = i.rolling(63, min_periods=21).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight win rate over a quarter, tilted by average overnight magnitude
def f07gd_f07_gap_dynamics_ovnwin_63d_base_v028_signal(open, close):
    o = _f07_overnight(open, close)
    win = (o > 0).astype(float)
    rate = win.rolling(63, min_periods=21).mean() - 0.5
    tilt = _mean(o, 63) / _std(o, 63).replace(0, np.nan)
    result = rate + 0.2 * tilt
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal tendency over a quarter: fill-frequency blended with mean fill depth
def f07gd_f07_gap_dynamics_revfreq_63d_base_v029_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close)
    big = (f > 0.5).astype(float)
    rate = big.rolling(63, min_periods=21).mean() - 0.5
    depth = _mean(f.clip(0, 2), 63)
    result = rate + 0.3 * depth
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill asymmetry: fill ratio on up-gaps minus fill ratio on down-gaps over a half-year
def f07gd_f07_gap_dynamics_fillasym_126d_base_v030_signal(open, high, low, close):
    g = _f07_gap(open, close)
    f = _f07_gap_fill(open, high, low, close)
    fu = f.where(g > 0)
    fd = f.where(g < 0)
    mu = fu.rolling(126, min_periods=21).sum() / fu.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)
    md = fd.rolling(126, min_periods=21).sum() / fd.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)
    result = mu - md
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude asymmetry: avg up-gap size minus avg |down-gap| size over a quarter
def f07gd_f07_gap_dynamics_magasym_63d_base_v031_signal(open, close):
    g = _f07_gap(open, close)
    up = g.where(g > 0)
    dn = (-g).where(g < 0)
    mu = up.rolling(63, min_periods=15).sum() / up.notna().rolling(63, min_periods=15).sum().replace(0, np.nan)
    md = dn.rolling(63, min_periods=15).sum() / dn.notna().rolling(63, min_periods=15).sum().replace(0, np.nan)
    result = mu - md
    return result.replace([np.inf, -np.inf], np.nan)


# overnight edge: overnight up-day rate minus intraday up-day rate over a quarter
def f07gd_f07_gap_dynamics_ovnedge_63d_base_v032_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    wo = (o > 0).astype(float).ewm(span=63, min_periods=21).mean()
    wi = (i > 0).astype(float).ewm(span=63, min_periods=21).mean()
    result = wo - wi
    return result.replace([np.inf, -np.inf], np.nan)


# tail overnight shock: max |gap| over a quarter relative to its typical gap size
def f07gd_f07_gap_dynamics_maxgap_63d_base_v033_signal(open, close):
    g = _f07_gap(open, close).abs()
    mx = g.rolling(63, min_periods=21).max()
    typ = _mean(g, 63)
    result = mx / typ.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# extreme-gap intensity: avg excess of |gap| over its 252d 90th-percentile band, over a quarter
def f07gd_f07_gap_dynamics_extgapfreq_63d_base_v034_signal(open, close):
    g = _f07_gap(open, close).abs()
    thr = g.rolling(252, min_periods=63).quantile(0.9)
    excess = (g - thr).clip(lower=0)
    result = _mean(excess, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift minus cumulative intraday drift over a year (overnight premium)
def f07gd_f07_gap_dynamics_ovnpremium_252d_base_v035_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    result = o.rolling(252, min_periods=63).sum() - i.rolling(252, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# gap momentum: change in smoothed gap level over a month (gap trend)
def f07gd_f07_gap_dynamics_gapmom_21d_base_v036_signal(open, close):
    g = _mean(_f07_gap(open, close), 21)
    result = g - g.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift acceleration as level: quarter drift minus prior-quarter drift
def f07gd_f07_gap_dynamics_ovnaccel_63d_base_v037_signal(open, close):
    o = _f07_overnight(open, close)
    cur = o.rolling(63, min_periods=21).sum()
    result = cur - cur.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap continuation strength scaled by gap magnitude (big gaps that follow through)
def f07gd_f07_gap_dynamics_contmag_63d_base_v038_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    s = np.sign(g) * i * g.abs()
    result = _mean(s, 63) * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio z-scored vs its own 126d history (unusual retracement regime)
def f07gd_f07_gap_dynamics_fillz_126d_base_v039_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close)
    fm = _mean(f, 21)
    result = _z(fm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol scaled by total range (gap risk vs intraday range)
def f07gd_f07_gap_dynamics_gaptotr_63d_base_v040_signal(open, high, low, close):
    g = _f07_gap(open, close).abs()
    tr = _f07_true_range(high, low, close) / close.shift(1).replace(0, np.nan)
    result = _mean(g, 63) / _mean(tr, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# sign persistence of gaps: magnitude-weighted lag-1 sign agreement over a quarter
def f07gd_f07_gap_dynamics_gapsignac_63d_base_v041_signal(open, close):
    g = _f07_gap(open, close)
    sgn = np.sign(g)
    prod = sgn * sgn.shift(1) * (g.abs() + g.shift(1).abs())
    result = _mean(prod, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return autocorrelation (lag-1) over a half-year (overnight momentum/reversal)
def f07gd_f07_gap_dynamics_ovnac_126d_base_v042_signal(open, close):
    o = _f07_overnight(open, close)
    om = o - _mean(o, 126)
    prod = om * om.shift(1)
    result = _mean(prod, 126) / _std(o, 126).replace(0, np.nan) ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# gap-to-next-day overnight relationship: does a big gap precede another gap (clustering)
def f07gd_f07_gap_dynamics_gapcluster_63d_base_v043_signal(open, close):
    g = _f07_gap(open, close).abs()
    gm = g - _mean(g, 63)
    prod = gm * gm.shift(1)
    result = _mean(prod, 63) / _std(g, 63).replace(0, np.nan) ** 2
    return result.replace([np.inf, -np.inf], np.nan)


# net overnight gap accumulation over a month minus over a quarter (drift convergence)
def f07gd_f07_gap_dynamics_drifgap_base_v044_signal(open, close):
    o = _f07_overnight(open, close)
    short = o.rolling(21, min_periods=10).sum()
    long = o.rolling(63, min_periods=21).sum() / 3.0
    result = short - long
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of total range opened away from prior close (open-location bias) over a quarter
def f07gd_f07_gap_dynamics_openloc_63d_base_v045_signal(open, high, low, close):
    pc = close.shift(1)
    rng = (high - low).replace(0, np.nan)
    loc = (open - pc) / rng
    result = _mean(loc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap exhaustion: conditional avg intraday return on up-gap days over a quarter (fade strength)
def f07gd_f07_gap_dynamics_gapexh_63d_base_v046_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    cond = (i * g.clip(lower=0))
    result = _mean(cond, 63) * 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# gap-and-go: gap-weighted intraday response on down-gap days over a quarter (bounce strength)
def f07gd_f07_gap_dynamics_gapgo_63d_base_v047_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    cond = (i * (-g).clip(lower=0))
    result = _mean(cond, 63) * 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift relative to its own 252d mean (overnight regime deviation)
def f07gd_f07_gap_dynamics_ovnreg_252d_base_v048_signal(open, close):
    o = _f07_overnight(open, close)
    cur = _mean(o, 63)
    result = cur - _mean(o, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap skewness over a half-year (overnight return asymmetry)
def f07gd_f07_gap_dynamics_gapskew_126d_base_v049_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# gap kurtosis over a half-year (overnight tail fatness)
def f07gd_f07_gap_dynamics_gapkurt_126d_base_v050_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-weighted gap level (recent-gap-biased overnight drift)
def f07gd_f07_gap_dynamics_gapewm_base_v051_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday correlation over a half-year (do gaps and days move together)
def f07gd_f07_gap_dynamics_ovnintrcorr_126d_base_v052_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    result = o.rolling(126, min_periods=42).corr(i)
    return result.replace([np.inf, -np.inf], np.nan)


# rank of latest |gap| vs its 252d history (percentile gap shock)
def f07gd_f07_gap_dynamics_gaprank_252d_base_v053_signal(open, close):
    g = _f07_gap(open, close).abs()
    result = _rank(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift per unit of gap volatility scaled, ranked over a year
def f07gd_f07_gap_dynamics_ovnqualrank_252d_base_v054_signal(open, close):
    o = _f07_overnight(open, close)
    q = _mean(o, 63) / _std(o, 63).replace(0, np.nan)
    result = _rank(q, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio momentum: change over a quarter (retracement regime trend)
def f07gd_f07_gap_dynamics_fillmom_63d_base_v055_signal(open, high, low, close):
    f = _mean(_f07_gap_fill(open, high, low, close), 21)
    result = f - f.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# signed overnight magnitude (sign x sqrt|gap|) smoothed over a month
def f07gd_f07_gap_dynamics_signmag_21d_base_v056_signal(open, close):
    g = _f07_gap(open, close)
    sm = np.sign(g) * np.sqrt(g.abs())
    result = _mean(sm, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drawdown: cumulative overnight return vs its trailing peak over a year
def f07gd_f07_gap_dynamics_ovndd_252d_base_v057_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    peak = cum.rolling(252, min_periods=63).max()
    result = cum - peak
    return result.replace([np.inf, -np.inf], np.nan)


# gap consistency: 1 - dispersion-to-magnitude of gaps over a quarter (steady vs erratic)
def f07gd_f07_gap_dynamics_gapconsist_63d_base_v058_signal(open, close):
    g = _f07_gap(open, close)
    result = _mean(g, 63).abs() / _std(g, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight up-streak length scaled (consecutive positive gaps) over a quarter
def f07gd_f07_gap_dynamics_upstreak_63d_base_v059_signal(open, close):
    g = _f07_gap(open, close)
    up = (g > 0).astype(float)

    def _maxrun(a):
        best = cur = 0
        for v in a:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
    streak = up.rolling(63, min_periods=21).apply(_maxrun, raw=True) / 63.0
    result = streak + 2.0 * _mean(g.clip(lower=0), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vs-prior-day-return interaction: does a big prior up-day precede a gap (lead-lag)
def f07gd_f07_gap_dynamics_priorlead_63d_base_v060_signal(open, close):
    g = _f07_gap(open, close)
    prior = (close.shift(1) / close.shift(2) - 1.0)
    prod = np.sign(prior) * g
    result = _mean(prod, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# weekly net gap (sum of gaps over 5d) z-scored vs 63d history
def f07gd_f07_gap_dynamics_wkgapz_base_v061_signal(open, close):
    g = _f07_gap(open, close)
    wk = g.rolling(5, min_periods=3).sum()
    result = _z(wk, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of overnight return relative to close-to-close return over a quarter
def f07gd_f07_gap_dynamics_ovncfrac_63d_base_v062_signal(open, close):
    o = _f07_overnight(open, close)
    cc = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    co = o.rolling(63, min_periods=21).sum()
    cccum = cc.rolling(63, min_periods=21).sum()
    result = co / cccum.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill completeness on down-gaps over a half-year (do down-gaps bounce)
def f07gd_f07_gap_dynamics_downfill_126d_base_v063_signal(open, high, low, close):
    g = _f07_gap(open, close)
    f = _f07_gap_fill(open, high, low, close)
    fd = f.where(g < 0)
    num = fd.rolling(126, min_periods=21).sum()
    cnt = fd.notna().rolling(126, min_periods=21).sum()
    result = num / cnt.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill completeness on up-gaps over a half-year (do up-gaps get sold)
def f07gd_f07_gap_dynamics_upfill_126d_base_v064_signal(open, high, low, close):
    g = _f07_gap(open, close)
    f = _f07_gap_fill(open, high, low, close)
    fu = f.where(g > 0)
    num = fu.rolling(126, min_periods=21).sum()
    cnt = fu.notna().rolling(126, min_periods=21).sum()
    result = num / cnt.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight volatility z vs 252d (overnight risk regime)
def f07gd_f07_gap_dynamics_ovnvolz_252d_base_v065_signal(open, close):
    o = _f07_overnight(open, close)
    v = _std(o, 21)
    result = _z(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap direction entropy over a quarter (how mixed are up/down gaps)
def f07gd_f07_gap_dynamics_gapentropy_63d_base_v066_signal(open, close):
    g = _f07_gap(open, close)
    up = (g > 0).astype(float)
    p = up.ewm(span=63, min_periods=21).mean().clip(1e-6, 1 - 1e-6)
    ent = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    result = ent
    return result.replace([np.inf, -np.inf], np.nan)


# gap-to-range transmission: corr of |gap| with same-day intraday |move| over a quarter
def f07gd_f07_gap_dynamics_gapvarshare_63d_base_v067_signal(open, close):
    g = _f07_gap(open, close).abs()
    i = _f07_intraday(open, close).abs()
    result = g.rolling(63, min_periods=21).corr(i)
    return result.replace([np.inf, -np.inf], np.nan)


# big-gap follow-through: avg intraday continuation on the largest-decile gaps over a year
def f07gd_f07_gap_dynamics_biggapcont_252d_base_v068_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    thr = g.abs().rolling(252, min_periods=63).quantile(0.8)
    big = g.abs() > thr
    cont = (np.sign(g) * i).where(big)
    num = cont.rolling(252, min_periods=21).sum()
    cnt = cont.notna().rolling(252, min_periods=21).sum()
    result = num / cnt.replace(0, np.nan) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight semivariance ratio over a quarter (downside vs upside overnight dispersion)
def f07gd_f07_gap_dynamics_ovneff_63d_base_v069_signal(open, close):
    o = _f07_overnight(open, close)
    dn = (o.clip(upper=0) ** 2).rolling(63, min_periods=21).mean()
    up = (o.clip(lower=0) ** 2).rolling(63, min_periods=21).mean()
    result = dn / up.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude trend: change in absolute-gap level over a quarter (rising gap risk)
def f07gd_f07_gap_dynamics_magtrend_63d_base_v070_signal(open, close):
    g = _f07_gap(open, close).abs()
    gm = _mean(g, 21)
    result = gm - gm.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vs-intraday Sharpe spread over a year (which session is the better bet)
def f07gd_f07_gap_dynamics_sharpespr_252d_base_v071_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday(open, close)
    so = _mean(o, 252) / _std(o, 252).replace(0, np.nan)
    si = _mean(i, 252) / _std(i, 252).replace(0, np.nan)
    result = so - si
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal magnitude: average size of intraday move countering the gap over a quarter
def f07gd_f07_gap_dynamics_revmag_63d_base_v072_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    counter = (-np.sign(g) * i).clip(lower=0)
    result = _mean(counter, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# monthly net overnight drift ranked vs its 252d history (overnight momentum percentile)
def f07gd_f07_gap_dynamics_wkdriftrank_252d_base_v073_signal(open, close):
    o = _f07_overnight(open, close)
    mo = o.rolling(21, min_periods=10).sum()
    result = _rank(mo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap polarity: smoothed sign of gaps (overnight directional persistence) over a quarter
def f07gd_f07_gap_dynamics_polarity_63d_base_v074_signal(open, close):
    g = _f07_gap(open, close)
    result = np.sign(g).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift de-meaned by its slow EMA (overnight displacement)
def f07gd_f07_gap_dynamics_ovndisp_base_v075_signal(open, close):
    o = _f07_overnight(open, close)
    om = _mean(o, 21)
    result = om - om.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07gd_f07_gap_dynamics_gap_5d_base_v001_signal,
    f07gd_f07_gap_dynamics_gapz_21d_base_v002_signal,
    f07gd_f07_gap_dynamics_gapz_63d_base_v003_signal,
    f07gd_f07_gap_dynamics_gapz_252d_base_v004_signal,
    f07gd_f07_gap_dynamics_upfreq_21d_base_v005_signal,
    f07gd_f07_gap_dynamics_downfreq_21d_base_v006_signal,
    f07gd_f07_gap_dynamics_dirbias_63d_base_v007_signal,
    f07gd_f07_gap_dynamics_fill_5d_base_v008_signal,
    f07gd_f07_gap_dynamics_fill_21d_base_v009_signal,
    f07gd_f07_gap_dynamics_fill_63d_base_v010_signal,
    f07gd_f07_gap_dynamics_ovn_21d_base_v011_signal,
    f07gd_f07_gap_dynamics_ovncum_63d_base_v012_signal,
    f07gd_f07_gap_dynamics_ovncum_252d_base_v013_signal,
    f07gd_f07_gap_dynamics_intr_21d_base_v014_signal,
    f07gd_f07_gap_dynamics_ovnvsintr_63d_base_v015_signal,
    f07gd_f07_gap_dynamics_ovnshare_63d_base_v016_signal,
    f07gd_f07_gap_dynamics_cont_21d_base_v017_signal,
    f07gd_f07_gap_dynamics_cont_63d_base_v018_signal,
    f07gd_f07_gap_dynamics_absmag_21d_base_v019_signal,
    f07gd_f07_gap_dynamics_absmag_63d_base_v020_signal,
    f07gd_f07_gap_dynamics_gapdisp_63d_base_v021_signal,
    f07gd_f07_gap_dynamics_gapdisp_252d_base_v022_signal,
    f07gd_f07_gap_dynamics_gapvolratio_base_v023_signal,
    f07gd_f07_gap_dynamics_gapsurprise_63d_base_v024_signal,
    f07gd_f07_gap_dynamics_ovnsharpe_63d_base_v025_signal,
    f07gd_f07_gap_dynamics_ovnsharpe_252d_base_v026_signal,
    f07gd_f07_gap_dynamics_intrsharpe_63d_base_v027_signal,
    f07gd_f07_gap_dynamics_ovnwin_63d_base_v028_signal,
    f07gd_f07_gap_dynamics_revfreq_63d_base_v029_signal,
    f07gd_f07_gap_dynamics_fillasym_126d_base_v030_signal,
    f07gd_f07_gap_dynamics_magasym_63d_base_v031_signal,
    f07gd_f07_gap_dynamics_ovnedge_63d_base_v032_signal,
    f07gd_f07_gap_dynamics_maxgap_63d_base_v033_signal,
    f07gd_f07_gap_dynamics_extgapfreq_63d_base_v034_signal,
    f07gd_f07_gap_dynamics_ovnpremium_252d_base_v035_signal,
    f07gd_f07_gap_dynamics_gapmom_21d_base_v036_signal,
    f07gd_f07_gap_dynamics_ovnaccel_63d_base_v037_signal,
    f07gd_f07_gap_dynamics_contmag_63d_base_v038_signal,
    f07gd_f07_gap_dynamics_fillz_126d_base_v039_signal,
    f07gd_f07_gap_dynamics_gaptotr_63d_base_v040_signal,
    f07gd_f07_gap_dynamics_gapsignac_63d_base_v041_signal,
    f07gd_f07_gap_dynamics_ovnac_126d_base_v042_signal,
    f07gd_f07_gap_dynamics_gapcluster_63d_base_v043_signal,
    f07gd_f07_gap_dynamics_drifgap_base_v044_signal,
    f07gd_f07_gap_dynamics_openloc_63d_base_v045_signal,
    f07gd_f07_gap_dynamics_gapexh_63d_base_v046_signal,
    f07gd_f07_gap_dynamics_gapgo_63d_base_v047_signal,
    f07gd_f07_gap_dynamics_ovnreg_252d_base_v048_signal,
    f07gd_f07_gap_dynamics_gapskew_126d_base_v049_signal,
    f07gd_f07_gap_dynamics_gapkurt_126d_base_v050_signal,
    f07gd_f07_gap_dynamics_gapewm_base_v051_signal,
    f07gd_f07_gap_dynamics_ovnintrcorr_126d_base_v052_signal,
    f07gd_f07_gap_dynamics_gaprank_252d_base_v053_signal,
    f07gd_f07_gap_dynamics_ovnqualrank_252d_base_v054_signal,
    f07gd_f07_gap_dynamics_fillmom_63d_base_v055_signal,
    f07gd_f07_gap_dynamics_signmag_21d_base_v056_signal,
    f07gd_f07_gap_dynamics_ovndd_252d_base_v057_signal,
    f07gd_f07_gap_dynamics_gapconsist_63d_base_v058_signal,
    f07gd_f07_gap_dynamics_upstreak_63d_base_v059_signal,
    f07gd_f07_gap_dynamics_priorlead_63d_base_v060_signal,
    f07gd_f07_gap_dynamics_wkgapz_base_v061_signal,
    f07gd_f07_gap_dynamics_ovncfrac_63d_base_v062_signal,
    f07gd_f07_gap_dynamics_downfill_126d_base_v063_signal,
    f07gd_f07_gap_dynamics_upfill_126d_base_v064_signal,
    f07gd_f07_gap_dynamics_ovnvolz_252d_base_v065_signal,
    f07gd_f07_gap_dynamics_gapentropy_63d_base_v066_signal,
    f07gd_f07_gap_dynamics_gapvarshare_63d_base_v067_signal,
    f07gd_f07_gap_dynamics_biggapcont_252d_base_v068_signal,
    f07gd_f07_gap_dynamics_ovneff_63d_base_v069_signal,
    f07gd_f07_gap_dynamics_magtrend_63d_base_v070_signal,
    f07gd_f07_gap_dynamics_sharpespr_252d_base_v071_signal,
    f07gd_f07_gap_dynamics_revmag_63d_base_v072_signal,
    f07gd_f07_gap_dynamics_wkdriftrank_252d_base_v073_signal,
    f07gd_f07_gap_dynamics_polarity_63d_base_v074_signal,
    f07gd_f07_gap_dynamics_ovndisp_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_GAP_DYNAMICS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f07_gap_dynamics_base_001_075_claude: %d features pass" % n_features)
