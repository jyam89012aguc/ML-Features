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


def _slope(s, w):
    # OLS slope of s over a trailing window vs time index 0..w-1
    idx = np.arange(w, dtype=float)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        ym = a.mean()
        return ((idx - xm) * (a - ym)).sum() / xden
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (gap dynamics) =====
def _f07_gap(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f07_overnight(openp, close):
    pc = close.shift(1)
    return np.log(openp.replace(0, np.nan) / pc.replace(0, np.nan))


def _f07_intraday(openp, close):
    return close / openp.replace(0, np.nan) - 1.0


def _f07_intraday_log(openp, close):
    return np.log(close.replace(0, np.nan) / openp.replace(0, np.nan))


def _f07_gap_fill(openp, high, low, close):
    pc = close.shift(1)
    gap = openp - pc
    retrace = np.where(gap > 0, openp - low, high - openp)
    retrace = pd.Series(retrace, index=openp.index)
    return retrace / gap.abs().replace(0, np.nan)


def _f07_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ============================================================
# net gap relative to true-range scale (gap in ATR units) smoothed over a week
def f07gd_f07_gap_dynamics_gapatr_5d_base_v076_signal(open, high, low, close):
    g = (open - close.shift(1))
    tr = _f07_true_range(high, low, close)
    ratio = g / tr.replace(0, np.nan)
    result = _mean(ratio, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gap in ATR units z-scored over a quarter
def f07gd_f07_gap_dynamics_gapatrz_63d_base_v077_signal(open, high, low, close):
    g = (open - close.shift(1))
    tr = _f07_true_range(high, low, close)
    ratio = g / tr.replace(0, np.nan)
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return regression slope over a quarter (overnight drift trend)
def f07gd_f07_gap_dynamics_ovnslope_63d_base_v078_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    result = _slope(cum, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap level regression slope over a half-year (is gap bias rising)
def f07gd_f07_gap_dynamics_gapslope_126d_base_v079_signal(open, close):
    gm = _mean(_f07_gap(open, close), 5)
    result = _slope(gm, 126) * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# 75th-percentile gap over a quarter (upper-tail overnight move)
def f07gd_f07_gap_dynamics_gapq75_63d_base_v080_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).quantile(0.75)
    return result.replace([np.inf, -np.inf], np.nan)


# 25th-percentile gap over a quarter (lower-tail overnight move)
def f07gd_f07_gap_dynamics_gapq25_63d_base_v081_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(63, min_periods=21).quantile(0.25)
    return result.replace([np.inf, -np.inf], np.nan)


# interquartile gap spread over a quarter (overnight dispersion, robust)
def f07gd_f07_gap_dynamics_gapiqr_63d_base_v082_signal(open, close):
    g = _f07_gap(open, close)
    q75 = g.rolling(63, min_periods=21).quantile(0.75)
    q25 = g.rolling(63, min_periods=21).quantile(0.25)
    result = q75 - q25
    return result.replace([np.inf, -np.inf], np.nan)


# median gap over a half-year (typical overnight tilt, robust to tails)
def f07gd_f07_gap_dynamics_gapmed_126d_base_v083_signal(open, close):
    g = _f07_gap(open, close)
    result = g.rolling(126, min_periods=42).median()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight beta to intraday: regression of overnight on prior intraday over a half-year
def f07gd_f07_gap_dynamics_ovnbeta_126d_base_v084_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close).shift(1)
    cov = (o * i).rolling(126, min_periods=42).mean() - _mean(o, 126) * _mean(i, 126)
    var = i.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-follows-gap beta: regression of intraday on same-day gap over a half-year
def f07gd_f07_gap_dynamics_intrbeta_126d_base_v085_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    cov = (g * i).rolling(126, min_periods=42).mean() - _mean(g, 126) * _mean(i, 126)
    var = g.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio dispersion over a quarter (how variable is retracement)
def f07gd_f07_gap_dynamics_filldisp_63d_base_v086_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close).clip(-3, 3)
    result = _std(f, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift minus its 252d median (overnight drift anomaly)
def f07gd_f07_gap_dynamics_ovnanom_252d_base_v087_signal(open, close):
    o = _f07_overnight(open, close)
    cur = _mean(o, 21)
    result = cur - o.rolling(252, min_periods=63).median()
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude exponential-weighted vol (recent overnight risk)
def f07gd_f07_gap_dynamics_gapewmvol_base_v088_signal(open, close):
    g = _f07_gap(open, close)
    result = g.ewm(span=21, min_periods=10).std()
    return result.replace([np.inf, -np.inf], np.nan)


# gap vol-of-vol over a quarter (instability of overnight risk)
def f07gd_f07_gap_dynamics_gapvov_63d_base_v089_signal(open, close):
    g = _f07_gap(open, close)
    v = _std(g, 10)
    result = _std(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of intraday range traversed before the open (gap as range fraction) quarter avg
def f07gd_f07_gap_dynamics_gaprngfrac_63d_base_v090_signal(open, high, low, close):
    pc = close.shift(1)
    span_lo = pd.concat([low, pc], axis=1).min(axis=1)
    span_hi = pd.concat([high, pc], axis=1).max(axis=1)
    frac = (open - pc) / (span_hi - span_lo).replace(0, np.nan)
    result = _mean(frac, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# does the day extend beyond the gap? close-vs-open relative to gap over a quarter
def f07gd_f07_gap_dynamics_extend_63d_base_v091_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    ext = i / g.abs().replace(0, np.nan)
    result = _mean(ext.clip(-5, 5), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight cumulative drift acceleration: quarter slope minus prior-quarter slope
def f07gd_f07_gap_dynamics_ovnslopechg_base_v092_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    sl = _slope(cum, 63)
    result = (sl - sl.shift(63)) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal indicator smoothed: -sign(gap)*intraday over a month (mean reversion strength)
def f07gd_f07_gap_dynamics_revstr_21d_base_v093_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    rev = -np.sign(g) * i
    result = _mean(rev, 21) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal strength over a half-year (longer-horizon mean reversion of gaps)
def f07gd_f07_gap_dynamics_revstr_126d_base_v094_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    rev = -np.sign(g) * i
    result = _mean(rev, 126) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return EWM mean minus EWM of close-to-close (gap-specific drift component)
def f07gd_f07_gap_dynamics_ovncomp_base_v095_signal(open, close):
    o = _f07_overnight(open, close)
    cc = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    result = o.ewm(span=42, min_periods=21).mean() - cc.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# upper-tail gap frequency proxy: avg of top-quartile gap excess over a quarter
def f07gd_f07_gap_dynamics_uptail_63d_base_v096_signal(open, close):
    g = _f07_gap(open, close)
    q = g.rolling(63, min_periods=21).quantile(0.75)
    excess = (g - q).clip(lower=0)
    result = _mean(excess, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# lower-tail gap intensity: avg of bottom-quartile gap shortfall over a quarter
def f07gd_f07_gap_dynamics_lotail_63d_base_v097_signal(open, close):
    g = _f07_gap(open, close)
    q = g.rolling(63, min_periods=21).quantile(0.25)
    short = (q - g).clip(lower=0)
    result = _mean(short, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-to-intraday drift correlation sign-weighted regime over a half-year
def f07gd_f07_gap_dynamics_sessregime_126d_base_v098_signal(open, close):
    o = _mean(_f07_overnight(open, close), 21)
    i = _mean(_f07_intraday_log(open, close), 21)
    result = np.sign(o) * np.sign(i) * (o.abs() + i.abs()) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap z-score smoothed and squashed into [-1,1] (bounded persistent gap surprise)
def f07gd_f07_gap_dynamics_gapztanh_63d_base_v099_signal(open, close):
    g = _f07_gap(open, close)
    z = _z(g, 63)
    result = np.tanh(z).ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# overnight Sharpe-of-drift over a half-year using realized overnight vol (distinct horizon)
def f07gd_f07_gap_dynamics_ovnia_126d_base_v100_signal(open, close):
    o = _f07_overnight(open, close)
    skew = o.rolling(126, min_periods=42).skew()
    result = skew
    return result.replace([np.inf, -np.inf], np.nan)


# overnight kurtosis over a half-year (overnight tail risk)
def f07gd_f07_gap_dynamics_ovnkurt_126d_base_v101_signal(open, close):
    o = _f07_overnight(open, close)
    result = o.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio EWM mean (persistent retracement tendency)
def f07gd_f07_gap_dynamics_fillewm_base_v102_signal(open, high, low, close):
    f = _f07_gap_fill(open, high, low, close).clip(-3, 3)
    result = f.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gap continuation EWM (recent-biased follow-through vs reversal)
def f07gd_f07_gap_dynamics_contewm_base_v103_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    cont = np.sign(g) * i
    result = cont.ewm(span=42, min_periods=21).mean() * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude rank over a half-year (percentile of current gap surprise)
def f07gd_f07_gap_dynamics_gaprank_126d_base_v104_signal(open, close):
    g = _f07_gap(open, close).abs()
    result = _rank(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift rank over a half-year (overnight momentum percentile)
def f07gd_f07_gap_dynamics_ovndriftrank_126d_base_v105_signal(open, close):
    o = _f07_overnight(open, close)
    d = o.rolling(21, min_periods=10).sum()
    result = _rank(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gap autocovariance scaled: how a gap predicts the next gap over a half-year
def f07gd_f07_gap_dynamics_gappredict_126d_base_v106_signal(open, close):
    g = _f07_gap(open, close)
    gm = g - _mean(g, 126)
    cov = (gm * gm.shift(1)).rolling(126, min_periods=42).mean()
    result = cov * 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight drift over a half-year minus over a year (drift horizon spread)
def f07gd_f07_gap_dynamics_drifthsp_base_v107_signal(open, close):
    o = _f07_overnight(open, close)
    h = o.rolling(126, min_periods=42).sum() / 126.0
    y = o.rolling(252, min_periods=63).sum() / 252.0
    result = (h - y) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day range expansion: intraday range on gap days vs non-gap days over a half-year
def f07gd_f07_gap_dynamics_gapdayrange_126d_base_v108_signal(open, high, low, close):
    g = _f07_gap(open, close).abs()
    rng = (high - low) / close.replace(0, np.nan)
    big = g > g.rolling(126, min_periods=42).median()
    rg = rng.where(big)
    rng_big = rg.rolling(126, min_periods=21).sum() / rg.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)
    rng_all = _mean(rng, 126)
    result = rng_big / rng_all.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# net overnight vs net intraday rank spread over a year (which session leads, ranked)
def f07gd_f07_gap_dynamics_sessrankspr_252d_base_v109_signal(open, close):
    o = _f07_overnight(open, close).rolling(63, min_periods=21).sum()
    i = _f07_intraday_log(open, close).rolling(63, min_periods=21).sum()
    result = _rank(o, 252) - _rank(i, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap EWM vs its slow EWM (overnight volatility expansion/contraction)
def f07gd_f07_gap_dynamics_gapvolexp_base_v110_signal(open, close):
    g = _f07_gap(open, close).abs()
    fast = g.ewm(span=10, min_periods=5).mean()
    slow = g.ewm(span=63, min_periods=21).mean()
    result = fast / slow.replace(0, np.nan) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift stability: 1 minus normalized dispersion of monthly drifts over a year
def f07gd_f07_gap_dynamics_ovnstab_252d_base_v111_signal(open, close):
    o = _f07_overnight(open, close)
    md = o.rolling(21, min_periods=10).sum()
    result = -_std(md, 252) / _mean(md.abs(), 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal asymmetry: reversal strength on up-gaps minus on down-gaps over a half-year
def f07gd_f07_gap_dynamics_revasym_126d_base_v112_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    up_rev = (-i).where(g > 0)
    dn_rev = (i).where(g < 0)
    mu = up_rev.rolling(126, min_periods=21).sum() / up_rev.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)
    md = dn_rev.rolling(126, min_periods=21).sum() / dn_rev.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)
    result = (mu - md) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap-adjusted momentum: overnight drift signed-share of gross daily motion over a quarter
def f07gd_f07_gap_dynamics_ovnmomshare_63d_base_v113_signal(open, close):
    o = _f07_overnight(open, close)
    drift = o.rolling(63, min_periods=21).sum()
    gross = o.abs().rolling(63, min_periods=21).sum()
    result = (drift / gross.replace(0, np.nan)) ** 3
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gap polarity change over a quarter (shift in overnight directional regime)
def f07gd_f07_gap_dynamics_polchg_63d_base_v114_signal(open, close):
    g = _f07_gap(open, close)
    pol = np.sign(g).ewm(span=42, min_periods=21).mean()
    result = pol - pol.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio trend (slope over a half-year)
def f07gd_f07_gap_dynamics_fillslope_126d_base_v115_signal(open, high, low, close):
    f = _mean(_f07_gap_fill(open, high, low, close).clip(-3, 3), 10)
    result = _slope(f, 126) * 1e3
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift de-trended by its regression line (overnight drift residual)
def f07gd_f07_gap_dynamics_ovnresid_126d_base_v116_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    sl = _slope(cum, 126)
    fitted_chg = sl  # per-day expected
    result = (cum - cum.shift(21)) / 21.0 - fitted_chg
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude vs intraday magnitude ratio over a quarter (overnight share of motion)
def f07gd_f07_gap_dynamics_gapmotion_63d_base_v117_signal(open, close):
    g = _f07_gap(open, close).abs()
    i = _f07_intraday(open, close).abs()
    result = _mean(g, 63) / _mean(i, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight win-rate minus 0.5, depth-weighted, over a half-year
def f07gd_f07_gap_dynamics_ovnwin_126d_base_v118_signal(open, close):
    o = _f07_overnight(open, close)
    win = (o > 0).astype(float).ewm(span=126, min_periods=42).mean() - 0.5
    depth = o.ewm(span=126, min_periods=42).mean() * 1e2
    result = win + depth
    return result.replace([np.inf, -np.inf], np.nan)


# extreme down-gap depth: average of gaps below -2 sigma over a year
def f07gd_f07_gap_dynamics_dngapshock_252d_base_v119_signal(open, close):
    g = _f07_gap(open, close)
    thr = _mean(g, 252) - 1.5 * _std(g, 252)
    shock = g.where(g < thr)
    result = shock.rolling(252, min_periods=10).sum() / shock.notna().rolling(252, min_periods=10).sum().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# extreme up-gap height: average of gaps above +1.5 sigma over a year
def f07gd_f07_gap_dynamics_upgapshock_252d_base_v120_signal(open, close):
    g = _f07_gap(open, close)
    thr = _mean(g, 252) + 1.5 * _std(g, 252)
    shock = g.where(g > thr)
    result = shock.rolling(252, min_periods=10).sum() / shock.notna().rolling(252, min_periods=10).sum().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drawdown depth normalized by overnight vol over a year
def f07gd_f07_gap_dynamics_ovnddnorm_252d_base_v121_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    peak = cum.rolling(252, min_periods=63).max()
    dd = cum - peak
    result = dd / _std(o, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap mean-reversion half-life proxy: lag-1 autocorr of gaps over a year (signed)
def f07gd_f07_gap_dynamics_gapacf_252d_base_v122_signal(open, close):
    g = _f07_gap(open, close)
    gm = g - _mean(g, 252)
    num = (gm * gm.shift(1)).rolling(252, min_periods=63).mean()
    den = (gm ** 2).rolling(252, min_periods=63).mean()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday variance fraction over a year (gap share of variance)
def f07gd_f07_gap_dynamics_varfrac_252d_base_v123_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    vo = o.rolling(252, min_periods=63).var()
    vi = i.rolling(252, min_periods=63).var()
    result = vo / (vo + vi).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# weekly gap momentum: 5d net gap minus its value a week ago
def f07gd_f07_gap_dynamics_wkgapmom_base_v124_signal(open, close):
    g = _f07_gap(open, close)
    wk = g.rolling(5, min_periods=3).sum()
    result = (wk - wk.shift(5)) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up clustering: avg |gap| conditional on prior-day up-gap over a half-year
def f07gd_f07_gap_dynamics_upcluster_126d_base_v125_signal(open, close):
    g = _f07_gap(open, close)
    cond = g.abs().where(g.shift(1) > 0)
    result = (cond.rolling(126, min_periods=21).sum()
              / cond.notna().rolling(126, min_periods=21).sum().replace(0, np.nan)) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap surprise vs realized intraday follow: composite gap-then-go score over a quarter
def f07gd_f07_gap_dynamics_gotoscore_63d_base_v126_signal(open, close):
    z = _z(_f07_gap(open, close), 63)
    i = _f07_intraday(open, close)
    result = _mean(np.tanh(z) * np.sign(i), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of days the open is the extreme of the day (gap-and-fade open-as-high/low) quarter
def f07gd_f07_gap_dynamics_openextreme_63d_base_v127_signal(open, high, low, close):
    open_hi = (open >= high * 0.99999).astype(float)
    open_lo = (open <= low * 1.00001).astype(float)
    raw = (open_hi - open_lo).ewm(span=42, min_periods=21).mean()
    g = _f07_gap(open, close)
    result = raw + 5.0 * _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight Sharpe ratio of the gap z-series stability (gap z mean over its dispersion) year
def f07gd_f07_gap_dynamics_gapzstab_252d_base_v128_signal(open, close):
    z = _z(_f07_gap(open, close), 63)
    result = _mean(z, 252) / _std(z, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# directional gap energy: signed squared gap accumulated over a quarter
def f07gd_f07_gap_dynamics_gapenergy_63d_base_v129_signal(open, close):
    g = _f07_gap(open, close)
    energy = np.sign(g) * g ** 2
    result = energy.rolling(63, min_periods=21).sum() * 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill ratio asymmetry vs magnitude: do bigger gaps fill more (slope) over a half-year
def f07gd_f07_gap_dynamics_fillvsmag_126d_base_v130_signal(open, high, low, close):
    g = _f07_gap(open, close).abs()
    f = _f07_gap_fill(open, high, low, close).clip(-3, 3)
    cov = (g * f).rolling(126, min_periods=42).mean() - _mean(g, 126) * _mean(f, 126)
    var = g.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# net overnight drift scaled by gap dispersion over a year (info-ratio style)
def f07gd_f07_gap_dynamics_ovninfo_252d_base_v131_signal(open, close):
    o = _f07_overnight(open, close)
    drift = o.rolling(126, min_periods=42).sum()
    disp = _std(_f07_gap(open, close), 252)
    result = drift * disp
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return concentration: top gap-day contribution to quarter drift (HHI-like)
def f07gd_f07_gap_dynamics_ovnconc_63d_base_v132_signal(open, close):
    o = _f07_overnight(open, close)
    mx = (o.abs()).rolling(63, min_periods=21).max()
    tot = (o.abs()).rolling(63, min_periods=21).sum()
    result = mx / tot.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap trend acceleration: 2nd difference of smoothed gap level (level form)
def f07gd_f07_gap_dynamics_gapaccel_63d_base_v133_signal(open, close):
    gm = _mean(_f07_gap(open, close), 21)
    result = (gm - 2.0 * gm.shift(21) + gm.shift(42)) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# share of gap-up days that gap up again next day (up-gap persistence) over a year
def f07gd_f07_gap_dynamics_upgappers_252d_base_v134_signal(open, close):
    g = _f07_gap(open, close)
    up = g > 0.002
    cont = (up & up.shift(1)).astype(float)
    base = up.shift(1).astype(float)
    rate = cont.rolling(252, min_periods=63).sum() / base.rolling(252, min_periods=63).sum().replace(0, np.nan)
    depth = _mean(g.clip(lower=0), 252) * 1e2
    result = (rate - 0.5) + depth
    return result.replace([np.inf, -np.inf], np.nan)


# did the open gap clear the prior day's range? open-vs-prior-high/low breakout over a quarter
def f07gd_f07_gap_dynamics_triangle_63d_base_v135_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    above = (open - ph).clip(lower=0)
    below = (pl - open).clip(lower=0)
    net = (above - below) / close.shift(1).replace(0, np.nan)
    result = _mean(net, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion term-structure slope: 21d vol minus 126d vol of gaps
def f07gd_f07_gap_dynamics_gapvolterm_base_v136_signal(open, close):
    g = _f07_gap(open, close)
    result = _std(g, 21) - _std(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# session divergence: overnight drift and intraday drift pulling opposite ways over a quarter
def f07gd_f07_gap_dynamics_ovndiverge_63d_base_v137_signal(open, close):
    o = _f07_overnight(open, close).rolling(63, min_periods=21).sum()
    i = _f07_intraday_log(open, close).rolling(63, min_periods=21).sum()
    result = np.where(np.sign(o) != np.sign(i), -(o.abs() + i.abs()), (o.abs() + i.abs()))
    result = pd.Series(result, index=o.index) * np.sign(o)
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of quarter return earned overnight, ranked vs year history
def f07gd_f07_gap_dynamics_ovnsharerank_252d_base_v138_signal(open, close):
    o = _f07_overnight(open, close).rolling(63, min_periods=21).sum()
    cc = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan)).rolling(63, min_periods=21).sum()
    share = o / (o.abs() + cc.abs()).replace(0, np.nan)
    result = _rank(share, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal vs continuation balance ranked over a year
def f07gd_f07_gap_dynamics_contbalrank_252d_base_v139_signal(open, close):
    g = _f07_gap(open, close)
    i = _f07_intraday(open, close)
    bal = _mean(np.sign(g) * i, 63)
    result = _rank(bal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight tail-risk: ratio of 95th to 50th percentile |gap| over a year
def f07gd_f07_gap_dynamics_taildns_252d_base_v140_signal(open, close):
    g = _f07_gap(open, close).abs()
    q95 = g.rolling(252, min_periods=63).quantile(0.95)
    q50 = g.rolling(252, min_periods=63).quantile(0.50)
    result = q95 / q50.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# gap drift smoothed minus its lagged value over a half-year (gap level momentum, long)
def f07gd_f07_gap_dynamics_gaplevmom_126d_base_v141_signal(open, close):
    gm = _mean(_f07_gap(open, close), 21)
    result = (gm - gm.shift(126)) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift Calmar over a half-year (drift over max overnight drawdown, distinct horizon)
def f07gd_f07_gap_dynamics_ovncalmar_126d_base_v142_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    peak = cum.rolling(126, min_periods=42).max()
    maxdd = (cum - peak).rolling(126, min_periods=42).min().abs()
    drift = o.rolling(126, min_periods=42).sum()
    result = drift / maxdd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-range vs gap covariance sign: do big gaps calm or excite the day, year
def f07gd_f07_gap_dynamics_gapcalm_252d_base_v143_signal(open, high, low, close):
    g = _f07_gap(open, close).abs()
    rng = (high - low) / close.replace(0, np.nan)
    gm = g - _mean(g, 252)
    rm = rng - _mean(rng, 252)
    cov = (gm * rm).rolling(252, min_periods=63).mean()
    result = cov * 1e4
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of gap closed by EOD on average, weighted by gap size, over a half-year
def f07gd_f07_gap_dynamics_wfill_126d_base_v144_signal(open, high, low, close):
    g = _f07_gap(open, close)
    f = _f07_gap_fill(open, high, low, close).clip(-3, 3)
    w = g.abs()
    num = (f * w).rolling(126, min_periods=42).sum()
    den = w.rolling(126, min_periods=42).sum()
    result = num / den.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight skew minus intraday skew over a half-year (session asymmetry spread)
def f07gd_f07_gap_dynamics_skewspr_126d_base_v145_signal(open, close):
    o = _f07_overnight(open, close)
    i = _f07_intraday_log(open, close)
    result = o.rolling(126, min_periods=42).skew() - i.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# gap polarity persistence: fraction of quarter where smoothed gap sign held over a year
def f07gd_f07_gap_dynamics_polpersist_252d_base_v146_signal(open, close):
    g = _f07_gap(open, close)
    pol = np.sign(g).ewm(span=21, min_periods=10).mean()
    strong = (pol.abs() > 0.3).astype(float)
    raw = strong.ewm(span=126, min_periods=42).mean()
    result = raw * np.sign(pol)
    return result.replace([np.inf, -np.inf], np.nan)


# gap z dispersion over a half-year (how variable are standardized gaps)
def f07gd_f07_gap_dynamics_gapzdisp_126d_base_v147_signal(open, close):
    z = _z(_f07_gap(open, close), 63)
    result = _std(z, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift trend strength: |slope| x R-of-fit over a half-year
def f07gd_f07_gap_dynamics_ovntrendstr_126d_base_v148_signal(open, close):
    o = _f07_overnight(open, close)
    cum = o.cumsum()
    sl = _slope(cum, 126)
    disp = _std(cum.diff(), 126)
    result = sl / disp.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# combined gap-fade signal: gap z times next-implied reversal, smoothed over a quarter
def f07gd_f07_gap_dynamics_fadecomp_63d_base_v149_signal(open, close):
    z = _z(_f07_gap(open, close), 63)
    i = _f07_intraday(open, close)
    fade = -z * np.sign(i) * i.abs()
    result = _mean(fade, 63) * 1e2
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vs-intraday drift ratio, bounded, over a year (where return accrues, ranked)
def f07gd_f07_gap_dynamics_accrueratio_252d_base_v150_signal(open, close):
    o = _f07_overnight(open, close).rolling(126, min_periods=42).sum()
    i = _f07_intraday_log(open, close).rolling(126, min_periods=42).sum()
    ratio = o / (o.abs() + i.abs()).replace(0, np.nan)
    result = _rank(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07gd_f07_gap_dynamics_gapatr_5d_base_v076_signal,
    f07gd_f07_gap_dynamics_gapatrz_63d_base_v077_signal,
    f07gd_f07_gap_dynamics_ovnslope_63d_base_v078_signal,
    f07gd_f07_gap_dynamics_gapslope_126d_base_v079_signal,
    f07gd_f07_gap_dynamics_gapq75_63d_base_v080_signal,
    f07gd_f07_gap_dynamics_gapq25_63d_base_v081_signal,
    f07gd_f07_gap_dynamics_gapiqr_63d_base_v082_signal,
    f07gd_f07_gap_dynamics_gapmed_126d_base_v083_signal,
    f07gd_f07_gap_dynamics_ovnbeta_126d_base_v084_signal,
    f07gd_f07_gap_dynamics_intrbeta_126d_base_v085_signal,
    f07gd_f07_gap_dynamics_filldisp_63d_base_v086_signal,
    f07gd_f07_gap_dynamics_ovnanom_252d_base_v087_signal,
    f07gd_f07_gap_dynamics_gapewmvol_base_v088_signal,
    f07gd_f07_gap_dynamics_gapvov_63d_base_v089_signal,
    f07gd_f07_gap_dynamics_gaprngfrac_63d_base_v090_signal,
    f07gd_f07_gap_dynamics_extend_63d_base_v091_signal,
    f07gd_f07_gap_dynamics_ovnslopechg_base_v092_signal,
    f07gd_f07_gap_dynamics_revstr_21d_base_v093_signal,
    f07gd_f07_gap_dynamics_revstr_126d_base_v094_signal,
    f07gd_f07_gap_dynamics_ovncomp_base_v095_signal,
    f07gd_f07_gap_dynamics_uptail_63d_base_v096_signal,
    f07gd_f07_gap_dynamics_lotail_63d_base_v097_signal,
    f07gd_f07_gap_dynamics_sessregime_126d_base_v098_signal,
    f07gd_f07_gap_dynamics_gapztanh_63d_base_v099_signal,
    f07gd_f07_gap_dynamics_ovnia_126d_base_v100_signal,
    f07gd_f07_gap_dynamics_ovnkurt_126d_base_v101_signal,
    f07gd_f07_gap_dynamics_fillewm_base_v102_signal,
    f07gd_f07_gap_dynamics_contewm_base_v103_signal,
    f07gd_f07_gap_dynamics_gaprank_126d_base_v104_signal,
    f07gd_f07_gap_dynamics_ovndriftrank_126d_base_v105_signal,
    f07gd_f07_gap_dynamics_gappredict_126d_base_v106_signal,
    f07gd_f07_gap_dynamics_drifthsp_base_v107_signal,
    f07gd_f07_gap_dynamics_gapdayrange_126d_base_v108_signal,
    f07gd_f07_gap_dynamics_sessrankspr_252d_base_v109_signal,
    f07gd_f07_gap_dynamics_gapvolexp_base_v110_signal,
    f07gd_f07_gap_dynamics_ovnstab_252d_base_v111_signal,
    f07gd_f07_gap_dynamics_revasym_126d_base_v112_signal,
    f07gd_f07_gap_dynamics_ovnmomshare_63d_base_v113_signal,
    f07gd_f07_gap_dynamics_polchg_63d_base_v114_signal,
    f07gd_f07_gap_dynamics_fillslope_126d_base_v115_signal,
    f07gd_f07_gap_dynamics_ovnresid_126d_base_v116_signal,
    f07gd_f07_gap_dynamics_gapmotion_63d_base_v117_signal,
    f07gd_f07_gap_dynamics_ovnwin_126d_base_v118_signal,
    f07gd_f07_gap_dynamics_dngapshock_252d_base_v119_signal,
    f07gd_f07_gap_dynamics_upgapshock_252d_base_v120_signal,
    f07gd_f07_gap_dynamics_ovnddnorm_252d_base_v121_signal,
    f07gd_f07_gap_dynamics_gapacf_252d_base_v122_signal,
    f07gd_f07_gap_dynamics_varfrac_252d_base_v123_signal,
    f07gd_f07_gap_dynamics_wkgapmom_base_v124_signal,
    f07gd_f07_gap_dynamics_upcluster_126d_base_v125_signal,
    f07gd_f07_gap_dynamics_gotoscore_63d_base_v126_signal,
    f07gd_f07_gap_dynamics_openextreme_63d_base_v127_signal,
    f07gd_f07_gap_dynamics_gapzstab_252d_base_v128_signal,
    f07gd_f07_gap_dynamics_gapenergy_63d_base_v129_signal,
    f07gd_f07_gap_dynamics_fillvsmag_126d_base_v130_signal,
    f07gd_f07_gap_dynamics_ovninfo_252d_base_v131_signal,
    f07gd_f07_gap_dynamics_ovnconc_63d_base_v132_signal,
    f07gd_f07_gap_dynamics_gapaccel_63d_base_v133_signal,
    f07gd_f07_gap_dynamics_upgappers_252d_base_v134_signal,
    f07gd_f07_gap_dynamics_triangle_63d_base_v135_signal,
    f07gd_f07_gap_dynamics_gapvolterm_base_v136_signal,
    f07gd_f07_gap_dynamics_ovndiverge_63d_base_v137_signal,
    f07gd_f07_gap_dynamics_ovnsharerank_252d_base_v138_signal,
    f07gd_f07_gap_dynamics_contbalrank_252d_base_v139_signal,
    f07gd_f07_gap_dynamics_taildns_252d_base_v140_signal,
    f07gd_f07_gap_dynamics_gaplevmom_126d_base_v141_signal,
    f07gd_f07_gap_dynamics_ovncalmar_126d_base_v142_signal,
    f07gd_f07_gap_dynamics_gapcalm_252d_base_v143_signal,
    f07gd_f07_gap_dynamics_wfill_126d_base_v144_signal,
    f07gd_f07_gap_dynamics_skewspr_126d_base_v145_signal,
    f07gd_f07_gap_dynamics_polpersist_252d_base_v146_signal,
    f07gd_f07_gap_dynamics_gapzdisp_126d_base_v147_signal,
    f07gd_f07_gap_dynamics_ovntrendstr_126d_base_v148_signal,
    f07gd_f07_gap_dynamics_fadecomp_63d_base_v149_signal,
    f07gd_f07_gap_dynamics_accrueratio_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_GAP_DYNAMICS_REGISTRY_076_150 = REGISTRY


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

    print("OK f07_gap_dynamics_base_076_150_claude: %d features pass" % n_features)
