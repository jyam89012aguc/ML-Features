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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (commodity momentum / rotation) =====
def _f02_roc(close, w):
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _f02_logmom(close, w):
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_mom_ex(close, w, skip):
    # momentum over w days excluding the most recent `skip` days (e.g. 12-1)
    return close.shift(skip) / close.shift(w).replace(0, np.nan) - 1.0


def _f02_vol(close, w):
    return close.pct_change().rolling(w, min_periods=max(2, w // 2)).std()


def _f02_tstat(close, w):
    r = close.pct_change()
    m = r.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(2, w // 2)).std()
    return (m / sd.replace(0, np.nan)) * np.sqrt(float(w))


def _f02_efficiency(close, w):
    net = (close - close.shift(w))
    gross = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / gross.replace(0, np.nan)


# ============================================================
# ROC 42d level (two-month rotation horizon)
def f02cm_f02_commodity_momentum_rotation_roc_42d_base_v076_signal(closeadj):
    b = _f02_roc(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 189d level (three-quarter horizon)
def f02cm_f02_commodity_momentum_rotation_roc_189d_base_v077_signal(closeadj):
    b = _f02_roc(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROC 378d level (1.5-year cycle horizon)
def f02cm_f02_commodity_momentum_rotation_roc_378d_base_v078_signal(closeadj):
    b = _f02_roc(closeadj, 378)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log momentum 21d (fast monthly)
def f02cm_f02_commodity_momentum_rotation_logmom_21d_base_v079_signal(closeadj):
    b = _f02_logmom(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 9-1 momentum: 189d return excluding most recent 21d
def f02cm_f02_commodity_momentum_rotation_mom91_189d_base_v080_signal(closeadj):
    b = _f02_mom_ex(closeadj, 189, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 18-1 momentum: 378d return excluding most recent 21d (long-cycle)
def f02cm_f02_commodity_momentum_rotation_mom181_378d_base_v081_signal(closeadj):
    b = _f02_mom_ex(closeadj, 378, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-3 momentum: 252d return excluding most recent 63d (slow rotation)
def f02cm_f02_commodity_momentum_rotation_mom123_252d_base_v082_signal(closeadj):
    b = _f02_mom_ex(closeadj, 252, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 42d t-stat, z-scored vs 252d history
def f02cm_f02_commodity_momentum_rotation_riskadj_42d_base_v083_signal(closeadj):
    t = _f02_tstat(closeadj, 42)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum 189d t-stat, z-scored vs 252d history
def f02cm_f02_commodity_momentum_rotation_riskadj_189d_base_v084_signal(closeadj):
    t = _f02_tstat(closeadj, 189)
    b = _z(t, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raw 126d momentum Sharpe (t-stat) percentile-ranked vs 504d history
def f02cm_f02_commodity_momentum_rotation_sharpe_rank_126d_base_v085_signal(closeadj):
    t = _f02_tstat(closeadj, 126)
    b = t.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure: 21d ROC minus 252d ROC (fast-vs-slow rotation)
def f02cm_f02_commodity_momentum_rotation_spread_21v252_base_v086_signal(closeadj):
    b = _f02_logmom(closeadj, 21) - _f02_logmom(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure: 42d ROC minus 126d ROC
def f02cm_f02_commodity_momentum_rotation_spread_42v126_base_v087_signal(closeadj):
    b = _f02_logmom(closeadj, 42) - _f02_logmom(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure: 252d ROC minus 504d ROC (cycle deceleration)
def f02cm_f02_commodity_momentum_rotation_spread_252v504_base_v088_signal(closeadj):
    b = _f02_logmom(closeadj, 252) - _f02_logmom(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum curvature: 63d ROC minus avg of 21d and 126d ROC (mid-horizon bulge)
def f02cm_f02_commodity_momentum_rotation_curv_63d_base_v089_signal(closeadj):
    m21 = _f02_logmom(closeadj, 21)
    m63 = _f02_logmom(closeadj, 63)
    m126 = _f02_logmom(closeadj, 126)
    b = m63 - 0.5 * (m21 + m126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum slope across horizons: linear fit of ROC vs log-horizon (term slope)
def f02cm_f02_commodity_momentum_rotation_termslope_base_v090_signal(closeadj):
    hs = [21, 63, 126, 252, 504]
    xs = np.log(np.array(hs, dtype=float))
    xc = xs - xs.mean()
    cols = [_f02_logmom(closeadj, w) for w in hs]
    mat = pd.concat(cols, axis=1)
    ybar = mat.mean(axis=1)
    num = sum(xc[k] * (cols[k].sub(ybar)) for k in range(len(hs)))
    den = float((xc ** 2).sum())
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum 63d z-scored vs 504d history (cycle-relative mid momentum)
def f02cm_f02_commodity_momentum_rotation_momz_63d_base_v091_signal(closeadj):
    b = _z(_f02_logmom(closeadj, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum 504d z-scored vs 1260d history (full-cycle relative)
def f02cm_f02_commodity_momentum_rotation_momz_504d_base_v092_signal(closeadj):
    b = _z(_f02_logmom(closeadj, 504), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum minus 9-1 momentum (rotation tilt long vs medium-long)
def f02cm_f02_commodity_momentum_rotation_tilt129_base_v093_signal(closeadj):
    m12 = _f02_mom_ex(closeadj, 252, 21)
    m9 = _f02_mom_ex(closeadj, 189, 21)
    b = m12 - m9
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 24-1 momentum minus 12-1 momentum (very-long vs long rotation)
def f02cm_f02_commodity_momentum_rotation_tilt2412_base_v094_signal(closeadj):
    m24 = _f02_mom_ex(closeadj, 504, 21)
    m12 = _f02_mom_ex(closeadj, 252, 21)
    b = m24 - m12
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum strength rank: |252d ROC| percentile vs 504d history (trend magnitude)
def f02cm_f02_commodity_momentum_rotation_strengthrank_252d_base_v095_signal(closeadj):
    s = _f02_logmom(closeadj, 252).abs()
    b = s.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum strength: |126d ROC| relative to its own 252d median (relative magnitude)
def f02cm_f02_commodity_momentum_rotation_strengthrel_126d_base_v096_signal(closeadj):
    s = _f02_logmom(closeadj, 126).abs()
    med = s.rolling(252, min_periods=126).median()
    b = s / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration 126d (second diff of cumulative log-return)
def f02cm_f02_commodity_momentum_rotation_accel_126d_base_v097_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc - 2.0 * roc.shift(126) + roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration 252d (long-cycle second difference)
def f02cm_f02_commodity_momentum_rotation_accel_252d_base_v098_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = roc - 2.0 * roc.shift(126) + roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-of-momentum 252d: change in 252d ROC over a quarter
def f02cm_f02_commodity_momentum_rotation_momom_252d_base_v099_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    b = roc - roc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-of-momentum 63d: change in 63d ROC over a month
def f02cm_f02_commodity_momentum_rotation_momom_63d_base_v100_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    b = roc - roc.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs prior cycle: sign-agreement of 252d momentum now vs two years ago,
# weighted by the smaller magnitude (cycle-echo strength)
def f02cm_f02_commodity_momentum_rotation_vscycle2y_252d_base_v101_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    prev = roc.shift(504)
    echo = np.sign(roc) * np.sign(prev) * np.minimum(roc.abs(), prev.abs())
    b = echo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs prior cycle: 126d ROC now minus 126d ROC one year ago
def f02cm_f02_commodity_momentum_rotation_vscycle1y_126d_base_v102_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc - roc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of 252d momentum from its 504d cycle peak (momentum drawdown depth)
def f02cm_f02_commodity_momentum_rotation_momdd_252d_base_v103_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    peak = roc.rolling(504, min_periods=252).max()
    b = roc - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain of 252d momentum off its 504d cycle trough (momentum recovery)
def f02cm_f02_commodity_momentum_rotation_momrec_252d_base_v104_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    trough = roc.rolling(504, min_periods=252).min()
    b = roc - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d momentum range position within its 1260d history (cycle phase of momentum)
def f02cm_f02_commodity_momentum_rotation_momphase_252d_base_v105_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    hi = roc.rolling(1260, min_periods=504).max()
    lo = roc.rolling(1260, min_periods=504).min()
    b = (roc - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d momentum trough (how mature the momentum recovery is)
def f02cm_f02_commodity_momentum_rotation_dsmomlow_504d_base_v106_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)

    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))

    b = roc.rolling(504, min_periods=252).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with positive 126d momentum (momentum uptime)
def f02cm_f02_commodity_momentum_rotation_uptime_126d_base_v107_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    pos = (roc > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-momentum density: smoothed share of positive 21d momentum over a year
def f02cm_f02_commodity_momentum_rotation_posmonths_base_v108_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    pos = (roc > 0).astype(float)
    samp = pos.rolling(21, min_periods=10).mean()
    b = samp.rolling(252, min_periods=126).sum() / 12.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-momentum sign-flip count over 126d (short-cycle rotation churn)
def f02cm_f02_commodity_momentum_rotation_churn_126d_base_v109_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    sgn = np.sign(roc)
    flip = (sgn != sgn.shift(1)).astype(float)
    b = flip.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum regime streak: signed length of current positive/negative 63d-ROC regime
def f02cm_f02_commodity_momentum_rotation_regstreak_63d_base_v110_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    sgn = np.sign(roc).replace(0, np.nan).ffill()
    grp = (sgn != sgn.shift(1)).cumsum()
    streak = sgn.groupby(grp).cumcount() + 1
    b = sgn * np.log1p(streak)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness 42d (unsigned efficiency, fast)
def f02cm_f02_commodity_momentum_rotation_eff_42d_base_v111_signal(closeadj):
    b = _f02_efficiency(closeadj, 42).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend cleanliness 189d (unsigned efficiency, long)
def f02cm_f02_commodity_momentum_rotation_eff_189d_base_v112_signal(closeadj):
    b = _f02_efficiency(closeadj, 189).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency change: 126d efficiency minus its quarter-ago value (cleanliness trend)
def f02cm_f02_commodity_momentum_rotation_effchg_126d_base_v113_signal(closeadj):
    e = _f02_efficiency(closeadj, 126).abs()
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed trend quality: efficiency 126d times sign of 126d momentum, magnitude-weighted
def f02cm_f02_commodity_momentum_rotation_quality_126d_base_v114_signal(closeadj):
    eff = _f02_efficiency(closeadj, 126).abs()
    roc = _f02_logmom(closeadj, 126)
    mag = roc.abs().rolling(252, min_periods=126).rank(pct=True)
    b = np.sign(roc) * eff * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum smoothed EMA 126d (persistent mid-cycle momentum regime)
def f02cm_f02_commodity_momentum_rotation_momema_126d_base_v115_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum displacement: 126d ROC minus its slow EMA (mid-cycle momentum surprise)
def f02cm_f02_commodity_momentum_rotation_momdisp_126d_base_v116_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    b = roc - roc.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded 504d momentum (squashed long-cycle momentum)
def f02cm_f02_commodity_momentum_rotation_momtanh_504d_base_v117_signal(closeadj):
    roc = _f02_logmom(closeadj, 504)
    b = np.tanh(1.5 * roc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude 126d momentum shape change over a quarter
def f02cm_f02_commodity_momentum_rotation_signmag_126d_base_v118_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    sm = np.sign(roc) * (roc.abs() ** 0.5)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute-momentum regime: fraction of last year with positive 504d momentum (uptime)
def f02cm_f02_commodity_momentum_rotation_absmom_504d_base_v119_signal(closeadj):
    roc = _f02_logmom(closeadj, 504)
    pos = (roc > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum breadth: signed-tanh agreement across 42/126/252/504 horizons
def f02cm_f02_commodity_momentum_rotation_breadth2_base_v120_signal(closeadj):
    h = [42, 126, 252, 504]
    agree = sum(np.tanh(6.0 * _f02_logmom(closeadj, w)) for w in h)
    b = agree / len(h)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum dispersion across 42/126/252/504 horizons (long-set disagreement)
def f02cm_f02_commodity_momentum_rotation_disp2_base_v121_signal(closeadj):
    cols = [_f02_logmom(closeadj, w) for w in [42, 126, 252, 504]]
    b = pd.concat(cols, axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum rank dispersion: spread of 42d and 252d momentum ranks (rotation tension)
def f02cm_f02_commodity_momentum_rotation_rankspread2_base_v122_signal(closeadj):
    r1 = _rank(_f02_logmom(closeadj, 42), 252)
    r2 = _rank(_f02_logmom(closeadj, 252), 504)
    b = r1 - r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-risk-adjusted 252d momentum (Sortino-style trend), ranked vs 504d history
def f02cm_f02_commodity_momentum_rotation_downadj_252d_base_v123_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    r = closeadj.pct_change()
    dvol = r.where(r < 0, 0.0).rolling(252, min_periods=126).std() * np.sqrt(252.0)
    ra = roc / dvol.replace(0, np.nan)
    b = ra.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum stability 504d: rolling std of 21d ROC over two years (long stability)
def f02cm_f02_commodity_momentum_rotation_stab_504d_base_v124_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    b = roc.rolling(504, min_periods=252).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum stability ratio: 63d-ROC std over short vs long window (vol-of-momentum)
def f02cm_f02_commodity_momentum_rotation_volofmom_base_v125_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    s = roc.rolling(63, min_periods=21).std()
    l = roc.rolling(252, min_periods=126).std()
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum minus its 252d-lagged self (year-over-year rotation change)
def f02cm_f02_commodity_momentum_rotation_mom121yoy_base_v126_signal(closeadj):
    m = _f02_mom_ex(closeadj, 252, 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-day excess return share over 504d: up-day return sum / total |return| sum
def f02cm_f02_commodity_momentum_rotation_cumpath_504d_base_v127_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, 0.0).rolling(504, min_periods=252).sum()
    tot = r.abs().rolling(504, min_periods=252).sum()
    b = up / tot.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum semivariance asymmetry 504d: upside vs downside dispersion of monthly ROC
def f02cm_f02_commodity_momentum_rotation_rough_504d_base_v128_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    dev = roc - roc.rolling(504, min_periods=252).mean()
    upv = dev.where(dev > 0, 0.0).rolling(504, min_periods=252).std()
    dnv = (-dev.where(dev < 0, 0.0)).rolling(504, min_periods=252).std()
    b = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-relative momentum: 252d ROC divided by |504d mean of 252d ROC| (own-history rotation)
def f02cm_f02_commodity_momentum_rotation_selfrel_252d_base_v129_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    base = roc.rolling(504, min_periods=252).mean().abs()
    b = roc / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum exhaustion 63d: how stretched 63d ROC is above its 252d band (overextension)
def f02cm_f02_commodity_momentum_rotation_exhaust_63d_base_v130_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    m = roc.rolling(252, min_periods=126).mean()
    sd = roc.rolling(252, min_periods=126).std()
    b = ((roc - m) / sd.replace(0, np.nan)).clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume momentum surprise 126d: sign(126d ROC) * z-scored dollar-volume surge
def f02cm_f02_commodity_momentum_rotation_dvsurge_126d_base_v131_signal(closeadj, volume):
    roc = _f02_logmom(closeadj, 126)
    dv = (closeadj * volume)
    dvz = (dv - dv.rolling(252, min_periods=126).mean()) / dv.rolling(252, min_periods=126).std().replace(0, np.nan)
    b = np.sign(roc) * dvz.clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-momentum divergence 63d: 63d ROC rank minus 63d dollar-volume-growth rank
def f02cm_f02_commodity_momentum_rotation_vmdiv_63d_base_v132_signal(closeadj, volume):
    roc = _f02_logmom(closeadj, 63)
    dv = (closeadj * volume)
    dvg = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / dv.rolling(63, min_periods=21).mean().replace(0, np.nan))
    rr = roc.rolling(252, min_periods=126).rank(pct=True)
    dr = dvg.rolling(252, min_periods=126).rank(pct=True)
    b = rr - dr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum kurtosis 21d returns over 126d (fat-tailed thrust regime)
def f02cm_f02_commodity_momentum_rotation_kurt_126d_base_v133_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum skew of daily returns over 126d (return asymmetry, distinct window)
def f02cm_f02_commodity_momentum_rotation_skew_126d_base_v134_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum coherence 126d: unsigned efficiency times lag-1 return autocorrelation
def f02cm_f02_commodity_momentum_rotation_coherence_126d_base_v135_signal(closeadj):
    eff = _f02_efficiency(closeadj, 126).abs()
    r = closeadj.pct_change()
    prod = (r * r.shift(1)).rolling(126, min_periods=63).mean()
    den = (r * r).rolling(126, min_periods=63).mean()
    ac = prod / den.replace(0, np.nan)
    b = eff * ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum persistence: lag-21 autocorrelation of 21d ROC over 252d (monthly memory)
def f02cm_f02_commodity_momentum_rotation_persist21_base_v136_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    prod = (roc * roc.shift(21)).rolling(252, min_periods=126).mean()
    den = (roc * roc).rolling(252, min_periods=126).mean()
    b = prod / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted multi-horizon momentum z-blend (long-tilted rotation composite, distinct set)
def f02cm_f02_commodity_momentum_rotation_zblend2_base_v137_signal(closeadj):
    b = (_z(_f02_logmom(closeadj, 42), 252) + _z(_f02_logmom(closeadj, 126), 252)
         + _z(_f02_logmom(closeadj, 252), 504) + _z(_f02_logmom(closeadj, 504), 1260)) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum rank of 189d ROC vs 756d history (three-year cycle rank, distinct base)
def f02cm_f02_commodity_momentum_rotation_momrank_756_base_v138_signal(closeadj):
    roc = _f02_logmom(closeadj, 189)
    b = roc.rolling(756, min_periods=378).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 9-1 momentum rank vs 504d history (medium-long rotation rank)
def f02cm_f02_commodity_momentum_rotation_mom91rank_base_v139_signal(closeadj):
    m = _f02_mom_ex(closeadj, 189, 21)
    b = m.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum convexity across horizons: 252d ROC minus avg of 126d and 504d (long bulge)
def f02cm_f02_commodity_momentum_rotation_convlong_base_v140_signal(closeadj):
    m126 = _f02_logmom(closeadj, 126)
    m252 = _f02_logmom(closeadj, 252)
    m504 = _f02_logmom(closeadj, 504)
    b = m252 - 0.5 * (m126 + m504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum impulse: 21d-ROC change over a week, scaled by 63d vol (fast thrust)
def f02cm_f02_commodity_momentum_rotation_impulse_base_v141_signal(closeadj):
    roc = _f02_logmom(closeadj, 21)
    chg = roc - roc.shift(5)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum vs trend: price vs 126d EMA in log terms (distance-from-trend momentum)
def f02cm_f02_commodity_momentum_rotation_emadist_126d_base_v142_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    ema = lp.ewm(span=126, min_periods=42).mean()
    b = lp - ema
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast-vs-slow EMA momentum 63/252: normalized EMA gap (long MACD-style rotation)
def f02cm_f02_commodity_momentum_rotation_emagap_63v252_base_v143_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    fast = lp.ewm(span=63, min_periods=21).mean()
    slow = lp.ewm(span=252, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum z relative to vol regime: 252d ROC z divided by 252d vol z (regime-scaled)
def f02cm_f02_commodity_momentum_rotation_regimescaled_base_v144_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    zr = _z(roc, 504)
    zv = _z(vol, 504)
    b = zr - zv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum drawdown duration: fraction of last year 252d-momentum below its 504d peak
def f02cm_f02_commodity_momentum_rotation_momddur_base_v145_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    peak = roc.rolling(504, min_periods=252).max()
    under = (roc < peak - 0.05).astype(float)
    b = under.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-momentum-high frequency: fraction of last quarter 126d-ROC sets a 252d-high
def f02cm_f02_commodity_momentum_rotation_newmomhi_base_v146_signal(closeadj):
    roc = _f02_logmom(closeadj, 126)
    hi = roc.rolling(252, min_periods=126).max()
    ishi = (roc >= hi * 0.99999).astype(float)
    b = ishi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration sign-persistence: signed share of positive 63d momom over 252d
def f02cm_f02_commodity_momentum_rotation_accelpersist_base_v147_signal(closeadj):
    roc = _f02_logmom(closeadj, 63)
    momom = roc - roc.shift(21)
    cum = (momom > 0).astype(float)
    b = cum.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum value vs its smoothed self ranked: 252d ROC minus 126d-EMA, ranked (rotation gap)
def f02cm_f02_commodity_momentum_rotation_smoothgap_252d_base_v148_signal(closeadj):
    roc = _f02_logmom(closeadj, 252)
    gap = roc - roc.ewm(span=126, min_periods=42).mean()
    b = gap.rolling(504, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-horizon momentum agreement minus dispersion (net-aligned rotation strength)
def f02cm_f02_commodity_momentum_rotation_netalign_base_v149_signal(closeadj):
    cols = [_f02_logmom(closeadj, w) for w in [21, 63, 126, 252]]
    mat = pd.concat(cols, axis=1)
    mean = mat.mean(axis=1)
    disp = mat.std(axis=1)
    b = mean / (disp + disp.rolling(252, min_periods=63).mean()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# very-long-cycle momentum: 756d log-momentum z-scored vs 1260d history
def f02cm_f02_commodity_momentum_rotation_mom756_base_v150_signal(closeadj):
    roc = np.log(closeadj.replace(0, np.nan) / closeadj.shift(756).replace(0, np.nan))
    b = _z(roc, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02cm_f02_commodity_momentum_rotation_roc_42d_base_v076_signal,
    f02cm_f02_commodity_momentum_rotation_roc_189d_base_v077_signal,
    f02cm_f02_commodity_momentum_rotation_roc_378d_base_v078_signal,
    f02cm_f02_commodity_momentum_rotation_logmom_21d_base_v079_signal,
    f02cm_f02_commodity_momentum_rotation_mom91_189d_base_v080_signal,
    f02cm_f02_commodity_momentum_rotation_mom181_378d_base_v081_signal,
    f02cm_f02_commodity_momentum_rotation_mom123_252d_base_v082_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_42d_base_v083_signal,
    f02cm_f02_commodity_momentum_rotation_riskadj_189d_base_v084_signal,
    f02cm_f02_commodity_momentum_rotation_sharpe_rank_126d_base_v085_signal,
    f02cm_f02_commodity_momentum_rotation_spread_21v252_base_v086_signal,
    f02cm_f02_commodity_momentum_rotation_spread_42v126_base_v087_signal,
    f02cm_f02_commodity_momentum_rotation_spread_252v504_base_v088_signal,
    f02cm_f02_commodity_momentum_rotation_curv_63d_base_v089_signal,
    f02cm_f02_commodity_momentum_rotation_termslope_base_v090_signal,
    f02cm_f02_commodity_momentum_rotation_momz_63d_base_v091_signal,
    f02cm_f02_commodity_momentum_rotation_momz_504d_base_v092_signal,
    f02cm_f02_commodity_momentum_rotation_tilt129_base_v093_signal,
    f02cm_f02_commodity_momentum_rotation_tilt2412_base_v094_signal,
    f02cm_f02_commodity_momentum_rotation_strengthrank_252d_base_v095_signal,
    f02cm_f02_commodity_momentum_rotation_strengthrel_126d_base_v096_signal,
    f02cm_f02_commodity_momentum_rotation_accel_126d_base_v097_signal,
    f02cm_f02_commodity_momentum_rotation_accel_252d_base_v098_signal,
    f02cm_f02_commodity_momentum_rotation_momom_252d_base_v099_signal,
    f02cm_f02_commodity_momentum_rotation_momom_63d_base_v100_signal,
    f02cm_f02_commodity_momentum_rotation_vscycle2y_252d_base_v101_signal,
    f02cm_f02_commodity_momentum_rotation_vscycle1y_126d_base_v102_signal,
    f02cm_f02_commodity_momentum_rotation_momdd_252d_base_v103_signal,
    f02cm_f02_commodity_momentum_rotation_momrec_252d_base_v104_signal,
    f02cm_f02_commodity_momentum_rotation_momphase_252d_base_v105_signal,
    f02cm_f02_commodity_momentum_rotation_dsmomlow_504d_base_v106_signal,
    f02cm_f02_commodity_momentum_rotation_uptime_126d_base_v107_signal,
    f02cm_f02_commodity_momentum_rotation_posmonths_base_v108_signal,
    f02cm_f02_commodity_momentum_rotation_churn_126d_base_v109_signal,
    f02cm_f02_commodity_momentum_rotation_regstreak_63d_base_v110_signal,
    f02cm_f02_commodity_momentum_rotation_eff_42d_base_v111_signal,
    f02cm_f02_commodity_momentum_rotation_eff_189d_base_v112_signal,
    f02cm_f02_commodity_momentum_rotation_effchg_126d_base_v113_signal,
    f02cm_f02_commodity_momentum_rotation_quality_126d_base_v114_signal,
    f02cm_f02_commodity_momentum_rotation_momema_126d_base_v115_signal,
    f02cm_f02_commodity_momentum_rotation_momdisp_126d_base_v116_signal,
    f02cm_f02_commodity_momentum_rotation_momtanh_504d_base_v117_signal,
    f02cm_f02_commodity_momentum_rotation_signmag_126d_base_v118_signal,
    f02cm_f02_commodity_momentum_rotation_absmom_504d_base_v119_signal,
    f02cm_f02_commodity_momentum_rotation_breadth2_base_v120_signal,
    f02cm_f02_commodity_momentum_rotation_disp2_base_v121_signal,
    f02cm_f02_commodity_momentum_rotation_rankspread2_base_v122_signal,
    f02cm_f02_commodity_momentum_rotation_downadj_252d_base_v123_signal,
    f02cm_f02_commodity_momentum_rotation_stab_504d_base_v124_signal,
    f02cm_f02_commodity_momentum_rotation_volofmom_base_v125_signal,
    f02cm_f02_commodity_momentum_rotation_mom121yoy_base_v126_signal,
    f02cm_f02_commodity_momentum_rotation_cumpath_504d_base_v127_signal,
    f02cm_f02_commodity_momentum_rotation_rough_504d_base_v128_signal,
    f02cm_f02_commodity_momentum_rotation_selfrel_252d_base_v129_signal,
    f02cm_f02_commodity_momentum_rotation_exhaust_63d_base_v130_signal,
    f02cm_f02_commodity_momentum_rotation_dvsurge_126d_base_v131_signal,
    f02cm_f02_commodity_momentum_rotation_vmdiv_63d_base_v132_signal,
    f02cm_f02_commodity_momentum_rotation_kurt_126d_base_v133_signal,
    f02cm_f02_commodity_momentum_rotation_skew_126d_base_v134_signal,
    f02cm_f02_commodity_momentum_rotation_coherence_126d_base_v135_signal,
    f02cm_f02_commodity_momentum_rotation_persist21_base_v136_signal,
    f02cm_f02_commodity_momentum_rotation_zblend2_base_v137_signal,
    f02cm_f02_commodity_momentum_rotation_momrank_756_base_v138_signal,
    f02cm_f02_commodity_momentum_rotation_mom91rank_base_v139_signal,
    f02cm_f02_commodity_momentum_rotation_convlong_base_v140_signal,
    f02cm_f02_commodity_momentum_rotation_impulse_base_v141_signal,
    f02cm_f02_commodity_momentum_rotation_emadist_126d_base_v142_signal,
    f02cm_f02_commodity_momentum_rotation_emagap_63v252_base_v143_signal,
    f02cm_f02_commodity_momentum_rotation_regimescaled_base_v144_signal,
    f02cm_f02_commodity_momentum_rotation_momddur_base_v145_signal,
    f02cm_f02_commodity_momentum_rotation_newmomhi_base_v146_signal,
    f02cm_f02_commodity_momentum_rotation_accelpersist_base_v147_signal,
    f02cm_f02_commodity_momentum_rotation_smoothgap_252d_base_v148_signal,
    f02cm_f02_commodity_momentum_rotation_netalign_base_v149_signal,
    f02cm_f02_commodity_momentum_rotation_mom756_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_COMMODITY_MOMENTUM_ROTATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f02_commodity_momentum_rotation_base_076_150_claude: %d features pass" % n_features)
