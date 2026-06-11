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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _ema(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (earnings / news gap dynamics) =====
# Per-day gap uses UNADJUSTED open/high/low/close (<=1d event); longer rolling
# stats operate on the per-day gap SERIES.
def _f12gd_gap(open, close):
    return open / close.shift(1).replace(0, np.nan) - 1.0


def _f12gd_loggap(open, close):
    return np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


def _f12gd_intraday(open, close):
    return close / open.replace(0, np.nan) - 1.0


def _f12gd_truerange(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


# opening gap above prior high (breakaway up-gap) magnitude 63d

def f12gd_f12_earnings_gap_dynamics_breakawayup_63d_base_v076_signal(open, high, close):
    ph = high.shift(1)
    bo = (open - ph).clip(lower=0) / close.shift(1).replace(0, np.nan)
    b = bo.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opening gap below prior low (breakaway down-gap) magnitude 63d

def f12gd_f12_earnings_gap_dynamics_breakawaydn_63d_base_v077_signal(open, low, close):
    pl = low.shift(1)
    bo = (pl - open).clip(lower=0) / close.shift(1).replace(0, np.nan)
    b = bo.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap beyond prior range magnitude 21d (clear-air gap size)

def f12gd_f12_earnings_gap_dynamics_clearairgap_21d_base_v078_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    g = (up + dn) / close.shift(1).replace(0, np.nan)
    b = g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net breakaway gap bias (up minus down magnitude beyond range) 126d

def f12gd_f12_earnings_gap_dynamics_breakawaybias_126d_base_v079_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    b = ((up - dn) / close.shift(1).replace(0, np.nan)).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap relative to prior-day range (gap/priorTR) 21d

def f12gd_f12_earnings_gap_dynamics_gapvsrange_21d_base_v080_signal(open, high, low, close):
    pr = (high.shift(1) - low.shift(1))
    g = (open - close.shift(1)).abs()
    b = (g / pr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# open as position within prior day range 21d

def f12gd_f12_earnings_gap_dynamics_openinrange_21d_base_v081_signal(open, high, low):
    ph = high.shift(1)
    pl = low.shift(1)
    pos = (open - pl) / (ph - pl).replace(0, np.nan)
    b = pos.rolling(21, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of open-in-prior-range 63d (open uncertainty)

def f12gd_f12_earnings_gap_dynamics_openrangedisp_63d_base_v082_signal(open, high, low):
    ph = high.shift(1)
    pl = low.shift(1)
    pos = (open - pl) / (ph - pl).replace(0, np.nan)
    b = pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day range expansion ratio (TR/prevTR) on gap days 63d

def f12gd_f12_earnings_gap_dynamics_gapdayexp_63d_base_v083_signal(open, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    ratio = tr / tr.shift(1).replace(0, np.nan)
    ev = (g > 0.02).astype(float)
    b = (ratio * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol vs intraday vol ratio 63d (gap-heavy risk mix)

def f12gd_f12_earnings_gap_dynamics_ovnintravolratio_63d_base_v084_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    b = ov.rolling(63, min_periods=21).std() / intr.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap EWMA span 42 (slow gappiness regime)

def f12gd_f12_earnings_gap_dynamics_absgapewm_42d_base_v085_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight squared-return EWMA (smoothed gap energy) 21d

def f12gd_f12_earnings_gap_dynamics_ovnewm_21d_base_v086_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = (ov ** 2).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return EWMA span 21

def f12gd_f12_earnings_gap_dynamics_intraewm_21d_base_v087_signal(open, close):
    intr = close / open.replace(0, np.nan) - 1.0
    b = intr.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume gaps minus down-volume gaps (sentiment via volume) 63d

def f12gd_f12_earnings_gap_dynamics_volgapsent_63d_base_v088_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    vw = volume * np.sign(g)
    b = vw.rolling(63, min_periods=21).sum() / volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap intensity per dollar of volume change 63d

def f12gd_f12_earnings_gap_dynamics_gapperdvol_63d_base_v089_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    dv = volume / volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    b = (g / dv.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# correlation of |gap| and volume 126d (news-volume coupling)

def f12gd_f12_earnings_gap_dynamics_gapvolcorr_126d_base_v090_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(126, min_periods=63).corr(volume)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume on gap-up days vs gap-down days 126d

def f12gd_f12_earnings_gap_dynamics_volgapupdn_126d_base_v091_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    upv = (volume * (g > 0.02).astype(float)).rolling(126, min_periods=42).sum()
    dnv = (volume * (g < -0.02).astype(float)).rolling(126, min_periods=42).sum()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal next-day fade strength 126d

def f12gd_f12_earnings_gap_dynamics_gapreverse_126d_base_v092_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    fwd = close.shift(-1) / open.shift(-1).replace(0, np.nan) - 1.0
    b = (-np.sign(g) * fwd).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day intraday momentum (open to close on gap days) 63d

def f12gd_f12_earnings_gap_dynamics_gapintramom_63d_base_v093_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    ev = (g.abs() > 0.02).astype(float)
    b = (intr * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-day gap echo: lag-1 product of gaps normalized by variance 63d

def f12gd_f12_earnings_gap_dynamics_gapecho_63d_base_v094_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    prod = (g * g.shift(1)).rolling(63, min_periods=21).mean()
    var = (g ** 2).rolling(63, min_periods=21).mean()
    b = prod / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 90th percentile abs gap 126d (typical big-gap size)

def f12gd_f12_earnings_gap_dynamics_gapp90_126d_base_v095_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(126, min_periods=63).quantile(0.90)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exceedance intensity: magnitude beyond 2x rolling-std 126d

def f12gd_f12_earnings_gap_dynamics_gapexceed_126d_base_v096_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    sd = g.rolling(126, min_periods=63).std()
    ex = (g.abs() - 2.0 * sd).clip(lower=0)
    b = ex.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-gap intensity: mean excess beyond 90th-pct gap 252d

def f12gd_f12_earnings_gap_dynamics_gaptailmean_252d_base_v097_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    thr = g.rolling(252, min_periods=63).quantile(0.90)
    exc = (g - thr).clip(lower=0)
    b = exc.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight share of cumulative total log-return 21d

def f12gd_f12_earnings_gap_dynamics_c2o_21d_base_v098_signal(open, close):
    c2o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    tot = np.log(close.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    cov = c2o.rolling(21, min_periods=10).sum()
    ctot = tot.rolling(21, min_periods=10).sum()
    b = cov / ctot.where(ctot.abs() > 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# open-to-close (intraday) cumulative log 21d

def f12gd_f12_earnings_gap_dynamics_o2c_21d_base_v099_signal(open, close):
    o2c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = o2c.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight/intraday cumulative-return ratio 126d

def f12gd_f12_earnings_gap_dynamics_ovnintraretratio_126d_base_v100_signal(open, close):
    ov = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan)).rolling(126, min_periods=63).sum()
    ic = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)).rolling(126, min_periods=63).sum()
    b = ov / (ov.abs() + ic.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap retracement depth toward prior close, averaged 21d

def f12gd_f12_earnings_gap_dynamics_gapretdepth_21d_base_v101_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    depth_up = (open - low) / g.replace(0, np.nan)
    depth_dn = (high - open) / (-g).replace(0, np.nan)
    d = depth_up.where(g > 0, depth_dn).clip(-1, 3)
    b = d.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# partial-fill ratio mean: how far gaps closed 63d

def f12gd_f12_earnings_gap_dynamics_partialfill_63d_base_v102_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    frac_up = ((open - low) / g.replace(0, np.nan)).where(g > 0)
    frac_dn = ((high - open) / (-g).replace(0, np.nan)).where(g < 0)
    f = pd.concat([frac_up, frac_dn], axis=1).sum(axis=1, min_count=1).clip(0, 1)
    b = f.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net gap-fill bias: filled fraction minus held fraction 126d

def f12gd_f12_earnings_gap_dynamics_fillvshold_126d_base_v103_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    ev = (g.abs() / pc.replace(0, np.nan) > 0.01)
    filled = (((g > 0) & (low <= pc)) | ((g < 0) & (high >= pc))) & ev
    held = (((g > 0) & (low > pc)) | ((g < 0) & (high < pc))) & ev
    b = (filled.astype(float) - held.astype(float)).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sqrt-signed gap mean 21d (variance-stabilized surprise)

def f12gd_f12_earnings_gap_dynamics_sqrtsigngap_21d_base_v104_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    t = np.sign(g) * np.sqrt(g.abs())
    b = t.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# winsorized vs raw gap-mean spread 63d (outlier influence on drift)

def f12gd_f12_earnings_gap_dynamics_wingapmean_63d_base_v105_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    lo = g.rolling(126, min_periods=42).quantile(0.05)
    hi = g.rolling(126, min_periods=42).quantile(0.95)
    gw = g.clip(lower=lo, upper=hi)
    b = g.rolling(63, min_periods=21).mean() - gw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap coefficient of variation 63d (dispersion over mean magnitude)

def f12gd_f12_earnings_gap_dynamics_logabsgap_63d_base_v106_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(63, min_periods=21).std() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current gappiness from its 252d normal 126d

def f12gd_f12_earnings_gap_dynamics_gappinessdist_252d_base_v107_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    cur = g.rolling(21, min_periods=10).mean()
    nrm = g.rolling(252, min_periods=63).mean()
    b = cur / nrm.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-regime z: 21d gap-vol vs 252d gap-vol

def f12gd_f12_earnings_gap_dynamics_gapregimez_252d_base_v108_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    sv = g.rolling(21, min_periods=10).std()
    b = (sv - sv.rolling(252, min_periods=63).mean()) / sv.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days in elevated-gap regime fraction 126d

def f12gd_f12_earnings_gap_dynamics_elevgapfrac_126d_base_v109_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    sv = g.rolling(21, min_periods=10).mean()
    med = sv.rolling(126, min_periods=63).median()
    hot = (sv > med).astype(float)
    b = hot.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap as fraction of subsequent day range 21d (gap vs digestion range)

def f12gd_f12_earnings_gap_dynamics_gapvsdayrange_21d_base_v110_signal(open, high, low, close):
    g = (open - close.shift(1)).abs()
    dr = (high - low)
    b = (g / dr.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap absorbed by intraday range: 1 - gap/range on gap days 63d

def f12gd_f12_earnings_gap_dynamics_gapabsorbed_63d_base_v111_signal(open, high, low, close):
    g = (open - close.shift(1)).abs()
    dr = (high - low)
    ratio = (g / dr.replace(0, np.nan))
    ev = (g / close.shift(1).replace(0, np.nan) > 0.02).astype(float)
    absorbed = (1.0 - ratio).clip(-1, 1)
    b = (absorbed * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return momentum: 5d sum minus 63d mean*5

def f12gd_f12_earnings_gap_dynamics_ovnmom_63d_base_v112_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(5, min_periods=3).sum() - ov.rolling(63, min_periods=21).mean() * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return momentum 5d vs 63d

def f12gd_f12_earnings_gap_dynamics_intramom_63d_base_v113_signal(open, close):
    intr = close / open.replace(0, np.nan) - 1.0
    b = intr.rolling(5, min_periods=3).sum() - intr.rolling(63, min_periods=21).mean() * 5.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-gap continuation strength: gap-up weighted intraday up-move 63d

def f12gd_f12_earnings_gap_dynamics_upgapcontinue_63d_base_v114_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    w = g.clip(lower=0)
    b = (w * intr).rolling(63, min_periods=21).sum() / w.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-gap continuation strength: gap-down weighted intraday down-move 63d

def f12gd_f12_earnings_gap_dynamics_dngapcontinue_63d_base_v115_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    w = (-g).clip(lower=0)
    b = (w * intr).rolling(63, min_periods=21).sum() / w.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs gap rank vs 126d (gappiness percentile)

def f12gd_f12_earnings_gap_dynamics_absgaprank_126d_base_v116_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(126, min_periods=42).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return rank vs 252d

def f12gd_f12_earnings_gap_dynamics_ovnrank_252d_base_v117_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vol persistence: lag-21 autocorrelation of 21d gap-std 252d

def f12gd_f12_earnings_gap_dynamics_gapvolrank_252d_base_v118_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    sv = g.rolling(21, min_periods=10).std()
    b = sv.rolling(252, min_periods=63).corr(sv.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean signed gap times sign of trailing gaps (gap herding) 63d

def f12gd_f12_earnings_gap_dynamics_gapherd_63d_base_v119_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    trail = np.sign(g.rolling(5, min_periods=3).mean())
    b = (g * trail).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized overnight skew via cube 126d (surprise asymmetry)

def f12gd_f12_earnings_gap_dynamics_ovncubeskew_126d_base_v120_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    num = (ov ** 3).rolling(126, min_periods=63).mean()
    den = (ov.rolling(126, min_periods=63).std()) ** 3
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day close above open rate weighted by gap size 126d

def f12gd_f12_earnings_gap_dynamics_gapdaybull_126d_base_v121_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    bull = ((close > open).astype(float) - 0.5) * 2.0
    b = (bull * g).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of gap range to 21d ATR on event days 63d

def f12gd_f12_earnings_gap_dynamics_gapatrratio_63d_base_v122_signal(open, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=10).mean()
    g = (open - pc).abs()
    b = (g / atr.replace(0, np.nan)).rolling(63, min_periods=21).quantile(0.75)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill half-life proxy: filled fraction within day 252d

def f12gd_f12_earnings_gap_dynamics_fillhalflife_252d_base_v123_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    ev = (g.abs() / pc.replace(0, np.nan) > 0.02)
    touched = (((g > 0) & (low <= open - 0.5 * g)) | ((g < 0) & (high >= open - 0.5 * g))) & ev
    b = touched.astype(float).rolling(252, min_periods=63).sum() / ev.astype(float).rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap energy concentration: 5d gap energy over 63d gap energy

def f12gd_f12_earnings_gap_dynamics_gapenergy_63d_base_v124_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    e = (g ** 2)
    b = e.rolling(5, min_periods=3).sum() / e.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight quadratic-variation level rank vs 252d history

def f12gd_f12_earnings_gap_dynamics_ovnqvshare_63d_base_v125_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    qov = (ov ** 2).rolling(63, min_periods=21).sum()
    b = qov.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest 5 gaps share of total absolute gap 126d (concentration)

def f12gd_f12_earnings_gap_dynamics_gapconc_126d_base_v126_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    top = g.rolling(126, min_periods=63).apply(lambda a: np.sort(a)[-5:].sum() if len(a) >= 5 else np.nan, raw=True)
    tot = g.rolling(126, min_periods=63).sum()
    b = top / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day next-day gap-fill rate (overnight reversal) 126d

def f12gd_f12_earnings_gap_dynamics_ovnreversal_126d_base_v127_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    nextov = open.shift(-1) / close.replace(0, np.nan) - 1.0
    b = (-np.sign(g) * nextov).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap drift consistency: magnitude-weighted sign agreement vs trailing 63d

def f12gd_f12_earnings_gap_dynamics_gapsignconsist_63d_base_v128_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    m = g.rolling(63, min_periods=21).mean()
    agree = np.sign(g) * np.sign(m) * g.abs()
    b = agree.rolling(63, min_periods=21).sum() / g.abs().rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-recovers-gap rate (close back to prior close) 63d

def f12gd_f12_earnings_gap_dynamics_intrarecovers_63d_base_v129_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    rec = ((g > 0.02) & (close < close.shift(1))) | ((g < -0.02) & (close > close.shift(1)))
    ev = (g.abs() > 0.02)
    b = rec.astype(float).rolling(63, min_periods=21).sum() / ev.astype(float).rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling mean of gap*volume zscore (confirmed shock z) 63d

def f12gd_f12_earnings_gap_dynamics_gapvolz_63d_base_v130_signal(open, close, volume):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    vs = volume / volume.rolling(63, min_periods=21).mean().replace(0, np.nan)
    x = g * vs
    b = (x - x.rolling(63, min_periods=21).mean()) / x.rolling(63, min_periods=21).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expanding-vs-contracting gap regime slope of gap-vol 63d

def f12gd_f12_earnings_gap_dynamics_gapvolslope_63d_base_v131_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    sv = g.rolling(21, min_periods=10).std()
    b = sv - sv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net overnight alpha minus intraday alpha rank 126d

def f12gd_f12_earnings_gap_dynamics_alphaspreadrank_126d_base_v132_signal(open, close):
    ov = (open / close.shift(1).replace(0, np.nan) - 1.0).rolling(63, min_periods=21).mean()
    ic = (close / open.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).mean()
    sp = ov - ic
    b = sp.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of days gap and prior-day move same direction 63d

def f12gd_f12_earnings_gap_dynamics_gapmomalign_63d_base_v133_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    prevmove = close.shift(1) / close.shift(2).replace(0, np.nan) - 1.0
    align = (np.sign(g) == np.sign(prevmove)).astype(float)
    b = align.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-volume elasticity: |gap| per unit log-volume 126d

def f12gd_f12_earnings_gap_dynamics_gapvolelast_126d_base_v134_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    lv = np.log(volume.replace(0, np.nan))
    cov = g.rolling(126, min_periods=63).cov(lv)
    var = lv.rolling(126, min_periods=63).var()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight downside intensity 63d (gap-down magnitude rate)

def f12gd_f12_earnings_gap_dynamics_ovndownfreq_63d_base_v135_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = (-ov).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight upside intensity 63d (gap-up magnitude rate)

def f12gd_f12_earnings_gap_dynamics_ovnupfreq_63d_base_v136_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap shock load: cumulative excess-gap magnitude 252d

def f12gd_f12_earnings_gap_dynamics_gaprevtime_252d_base_v137_signal(open, close):
    pc = close.shift(1)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    sd = g.rolling(126, min_periods=42).std()
    exc = (g - 2.0 * sd).clip(lower=0)
    b = exc.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clear-air gap dispersion: std of beyond-range gap magnitude 126d

def f12gd_f12_earnings_gap_dynamics_netclearair_126d_base_v138_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0)
    dn = (pl - open).clip(lower=0)
    mag = (up + dn) / close.shift(1).replace(0, np.nan)
    b = mag.rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-magnitude-weighted volume z 63d (news-volume coupling)

def f12gd_f12_earnings_gap_dynamics_gapdayvolz_63d_base_v139_signal(open, close, volume):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    vz = (volume - volume.rolling(63, min_periods=21).mean()) / volume.rolling(63, min_periods=21).std().replace(0, np.nan)
    b = (vz * g).rolling(63, min_periods=21).sum() / g.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio recent gap energy to 252d gap energy

def f12gd_f12_earnings_gap_dynamics_gapenergyratio_252d_base_v140_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    e = (g ** 2)
    b = e.rolling(21, min_periods=10).sum() / e.rolling(252, min_periods=63).sum().replace(0, np.nan) * 12.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap drift t-stat 126d (significance of overnight alpha)

def f12gd_f12_earnings_gap_dynamics_ovntstat_126d_base_v141_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    m = ov.rolling(126, min_periods=63).mean()
    s = ov.rolling(126, min_periods=63).std()
    b = m / (s / np.sqrt(126)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance of filled up-gaps vs filled down-gaps 126d

def f12gd_f12_earnings_gap_dynamics_fillbalance_126d_base_v142_signal(open, low, high, close):
    pc = close.shift(1)
    g = open - pc
    ufill = (((g > 0) & (low <= pc))).astype(float)
    dfill = (((g < 0) & (high >= pc))).astype(float)
    b = (ufill - dfill).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap shock persistence: |gap| autocorrelation 126d

def f12gd_f12_earnings_gap_dynamics_absgapac_126d_base_v143_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    b = g.rolling(126, min_periods=63).corr(g.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-to-close pass-through: corr(gap, close-move) 126d

def f12gd_f12_earnings_gap_dynamics_gappassthrough_126d_base_v144_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    cm = close / close.shift(1).replace(0, np.nan) - 1.0
    b = g.rolling(126, min_periods=63).corr(cm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gap surprise index: z of |gap| EWMA 126d

def f12gd_f12_earnings_gap_dynamics_gapsurpriseidx_126d_base_v145_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    e = g.ewm(span=10, min_periods=5).mean()
    b = (e - e.rolling(126, min_periods=63).mean()) / e.rolling(126, min_periods=63).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return median 126d (robust gap drift)

def f12gd_f12_earnings_gap_dynamics_ovnmedian_126d_base_v146_signal(open, close):
    ov = open / close.shift(1).replace(0, np.nan) - 1.0
    b = ov.rolling(126, min_periods=63).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dominance: |gap| vs |intraday| ratio 63d

def f12gd_f12_earnings_gap_dynamics_gapdominance_63d_base_v147_signal(open, close):
    g = (open / close.shift(1).replace(0, np.nan) - 1.0).abs()
    intr = (close / open.replace(0, np.nan) - 1.0).abs()
    b = (g / (g + intr).replace(0, np.nan)).rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-and-go up intensity: gap-up x intraday-up magnitude 126d

def f12gd_f12_earnings_gap_dynamics_gapgoupct_126d_base_v148_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    intr = close / open.replace(0, np.nan) - 1.0
    ev = g.clip(lower=0) * intr.clip(lower=0)
    b = ev.rolling(126, min_periods=42).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vol regime tanh of gap-energy ratio 126d

def f12gd_f12_earnings_gap_dynamics_gapenergytanh_126d_base_v149_signal(open, close):
    g = open / close.shift(1).replace(0, np.nan) - 1.0
    e = (g ** 2)
    r = e.rolling(21, min_periods=10).sum() / e.rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = np.tanh(r / 21.0 - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day high-wick fraction on event days 63d (failed-spike gaps)

def f12gd_f12_earnings_gap_dynamics_gapwick_63d_base_v150_signal(open, high, low, close):
    pc = close.shift(1)
    wick = (high - pd.concat([open, close], axis=1).max(axis=1)) / (high - low).replace(0, np.nan)
    g = (open / pc.replace(0, np.nan) - 1.0).abs()
    ev = (g > 0.02).astype(float)
    b = (wick * ev).rolling(63, min_periods=21).sum() / ev.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f12gd_f12_earnings_gap_dynamics_breakawayup_63d_base_v076_signal,
    f12gd_f12_earnings_gap_dynamics_breakawaydn_63d_base_v077_signal,
    f12gd_f12_earnings_gap_dynamics_clearairgap_21d_base_v078_signal,
    f12gd_f12_earnings_gap_dynamics_breakawaybias_126d_base_v079_signal,
    f12gd_f12_earnings_gap_dynamics_gapvsrange_21d_base_v080_signal,
    f12gd_f12_earnings_gap_dynamics_openinrange_21d_base_v081_signal,
    f12gd_f12_earnings_gap_dynamics_openrangedisp_63d_base_v082_signal,
    f12gd_f12_earnings_gap_dynamics_gapdayexp_63d_base_v083_signal,
    f12gd_f12_earnings_gap_dynamics_ovnintravolratio_63d_base_v084_signal,
    f12gd_f12_earnings_gap_dynamics_absgapewm_42d_base_v085_signal,
    f12gd_f12_earnings_gap_dynamics_ovnewm_21d_base_v086_signal,
    f12gd_f12_earnings_gap_dynamics_intraewm_21d_base_v087_signal,
    f12gd_f12_earnings_gap_dynamics_volgapsent_63d_base_v088_signal,
    f12gd_f12_earnings_gap_dynamics_gapperdvol_63d_base_v089_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolcorr_126d_base_v090_signal,
    f12gd_f12_earnings_gap_dynamics_volgapupdn_126d_base_v091_signal,
    f12gd_f12_earnings_gap_dynamics_gapreverse_126d_base_v092_signal,
    f12gd_f12_earnings_gap_dynamics_gapintramom_63d_base_v093_signal,
    f12gd_f12_earnings_gap_dynamics_gapecho_63d_base_v094_signal,
    f12gd_f12_earnings_gap_dynamics_gapp90_126d_base_v095_signal,
    f12gd_f12_earnings_gap_dynamics_gapexceed_126d_base_v096_signal,
    f12gd_f12_earnings_gap_dynamics_gaptailmean_252d_base_v097_signal,
    f12gd_f12_earnings_gap_dynamics_c2o_21d_base_v098_signal,
    f12gd_f12_earnings_gap_dynamics_o2c_21d_base_v099_signal,
    f12gd_f12_earnings_gap_dynamics_ovnintraretratio_126d_base_v100_signal,
    f12gd_f12_earnings_gap_dynamics_gapretdepth_21d_base_v101_signal,
    f12gd_f12_earnings_gap_dynamics_partialfill_63d_base_v102_signal,
    f12gd_f12_earnings_gap_dynamics_fillvshold_126d_base_v103_signal,
    f12gd_f12_earnings_gap_dynamics_sqrtsigngap_21d_base_v104_signal,
    f12gd_f12_earnings_gap_dynamics_wingapmean_63d_base_v105_signal,
    f12gd_f12_earnings_gap_dynamics_logabsgap_63d_base_v106_signal,
    f12gd_f12_earnings_gap_dynamics_gappinessdist_252d_base_v107_signal,
    f12gd_f12_earnings_gap_dynamics_gapregimez_252d_base_v108_signal,
    f12gd_f12_earnings_gap_dynamics_elevgapfrac_126d_base_v109_signal,
    f12gd_f12_earnings_gap_dynamics_gapvsdayrange_21d_base_v110_signal,
    f12gd_f12_earnings_gap_dynamics_gapabsorbed_63d_base_v111_signal,
    f12gd_f12_earnings_gap_dynamics_ovnmom_63d_base_v112_signal,
    f12gd_f12_earnings_gap_dynamics_intramom_63d_base_v113_signal,
    f12gd_f12_earnings_gap_dynamics_upgapcontinue_63d_base_v114_signal,
    f12gd_f12_earnings_gap_dynamics_dngapcontinue_63d_base_v115_signal,
    f12gd_f12_earnings_gap_dynamics_absgaprank_126d_base_v116_signal,
    f12gd_f12_earnings_gap_dynamics_ovnrank_252d_base_v117_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolrank_252d_base_v118_signal,
    f12gd_f12_earnings_gap_dynamics_gapherd_63d_base_v119_signal,
    f12gd_f12_earnings_gap_dynamics_ovncubeskew_126d_base_v120_signal,
    f12gd_f12_earnings_gap_dynamics_gapdaybull_126d_base_v121_signal,
    f12gd_f12_earnings_gap_dynamics_gapatrratio_63d_base_v122_signal,
    f12gd_f12_earnings_gap_dynamics_fillhalflife_252d_base_v123_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergy_63d_base_v124_signal,
    f12gd_f12_earnings_gap_dynamics_ovnqvshare_63d_base_v125_signal,
    f12gd_f12_earnings_gap_dynamics_gapconc_126d_base_v126_signal,
    f12gd_f12_earnings_gap_dynamics_ovnreversal_126d_base_v127_signal,
    f12gd_f12_earnings_gap_dynamics_gapsignconsist_63d_base_v128_signal,
    f12gd_f12_earnings_gap_dynamics_intrarecovers_63d_base_v129_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolz_63d_base_v130_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolslope_63d_base_v131_signal,
    f12gd_f12_earnings_gap_dynamics_alphaspreadrank_126d_base_v132_signal,
    f12gd_f12_earnings_gap_dynamics_gapmomalign_63d_base_v133_signal,
    f12gd_f12_earnings_gap_dynamics_gapvolelast_126d_base_v134_signal,
    f12gd_f12_earnings_gap_dynamics_ovndownfreq_63d_base_v135_signal,
    f12gd_f12_earnings_gap_dynamics_ovnupfreq_63d_base_v136_signal,
    f12gd_f12_earnings_gap_dynamics_gaprevtime_252d_base_v137_signal,
    f12gd_f12_earnings_gap_dynamics_netclearair_126d_base_v138_signal,
    f12gd_f12_earnings_gap_dynamics_gapdayvolz_63d_base_v139_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergyratio_252d_base_v140_signal,
    f12gd_f12_earnings_gap_dynamics_ovntstat_126d_base_v141_signal,
    f12gd_f12_earnings_gap_dynamics_fillbalance_126d_base_v142_signal,
    f12gd_f12_earnings_gap_dynamics_absgapac_126d_base_v143_signal,
    f12gd_f12_earnings_gap_dynamics_gappassthrough_126d_base_v144_signal,
    f12gd_f12_earnings_gap_dynamics_gapsurpriseidx_126d_base_v145_signal,
    f12gd_f12_earnings_gap_dynamics_ovnmedian_126d_base_v146_signal,
    f12gd_f12_earnings_gap_dynamics_gapdominance_63d_base_v147_signal,
    f12gd_f12_earnings_gap_dynamics_gapgoupct_126d_base_v148_signal,
    f12gd_f12_earnings_gap_dynamics_gapenergytanh_126d_base_v149_signal,
    f12gd_f12_earnings_gap_dynamics_gapwick_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_EARNINGS_GAP_DYNAMICS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f12_earnings_gap_dynamics_base_076_150_claude: %d features pass" % n_features)
