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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (momentum rotation) =====
def _f02_roc(close, w):
    # rate of change over w days (simple return)
    return close / close.shift(w).replace(0, np.nan) - 1.0


def _f02_logmom(close, w):
    # log momentum over w days
    return np.log(close.replace(0, np.nan) / close.shift(w).replace(0, np.nan))


def _f02_ret(close):
    return close.pct_change()


def _f02_vol(close, w):
    # realized vol of daily returns over w days
    return close.pct_change().rolling(w, min_periods=max(1, w // 2)).std()


def _f02_dnvol(close, w):
    # downside (semi) deviation of daily returns over w days
    r = close.pct_change()
    neg = r.where(r < 0, 0.0)
    return neg.rolling(w, min_periods=max(1, w // 2)).std()


def _f02_hitrate(close, w):
    # fraction of up days over the window
    up = (close.pct_change() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean()


def _f02_12_1(close):
    # classic 12-1 momentum: 252d return excluding the most recent 21d
    return close.shift(21) / close.shift(252).replace(0, np.nan) - 1.0


# ============================================================
# --- ROC family: plain rate of change over standard windows ---
def f02mr_f02_momentum_rotation_roc_5d_base_v001_signal(closeadj):
    b = _f02_roc(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_21d_base_v002_signal(closeadj):
    b = _f02_roc(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_63d_base_v003_signal(closeadj):
    b = _f02_roc(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_126d_base_v004_signal(closeadj):
    b = _f02_roc(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_roc_252d_base_v005_signal(closeadj):
    b = _f02_roc(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log momentum (63d) displaced from its own slow EMA (momentum vs its trend) ---
def f02mr_f02_momentum_rotation_logmomz_63d_base_v006_signal(closeadj):
    lm = _f02_logmom(closeadj, 63)
    b = lm - lm.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log momentum (126d) displaced from its own slow EMA ---
def f02mr_f02_momentum_rotation_logmomz_126d_base_v007_signal(closeadj):
    lm = _f02_logmom(closeadj, 126)
    b = lm - lm.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 12-1 momentum (252 minus 21) ---
def f02mr_f02_momentum_rotation_mom12m1_252d_base_v008_signal(closeadj):
    b = _f02_12_1(closeadj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum z-scored vs its own 252d history (de-trended)
def f02mr_f02_momentum_rotation_mom12m1z_252d_base_v009_signal(closeadj):
    m = _f02_12_1(closeadj)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 6-1 momentum: 126d return excluding the most recent 21d
def f02mr_f02_momentum_rotation_mom6m1_126d_base_v010_signal(closeadj):
    b = closeadj.shift(21) / closeadj.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum strength = ROC scaled by realized vol (risk-adjusted) ---
def f02mr_f02_momentum_rotation_radjmom_21d_base_v011_signal(closeadj):
    # 21d momentum scaled by the SHORTER 5d vol, then ranked vs 126d history (decorrelates from raw ROC)
    roc = _f02_roc(closeadj, 21)
    vol = _f02_vol(closeadj, 5)
    ratio = roc / (vol * np.sqrt(21)).replace(0, np.nan)
    b = _rank(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_63d_base_v012_signal(closeadj):
    # 63d risk-adjusted momentum z-scored vs its own 252d history (de-trended Sharpe-mom)
    roc = _f02_roc(closeadj, 63)
    vol = _f02_vol(closeadj, 63)
    ratio = roc / (vol * np.sqrt(63)).replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_126d_base_v013_signal(closeadj):
    # spread of risk-adjusted momentum across 63d and 126d horizons (risk-adj rotation)
    roc63 = _f02_roc(closeadj, 63)
    roc126 = _f02_roc(closeadj, 126)
    v63 = _f02_vol(closeadj, 63)
    v126 = _f02_vol(closeadj, 126)
    radj63 = roc63 / (v63 * np.sqrt(63)).replace(0, np.nan)
    radj126 = roc126 / (v126 * np.sqrt(126)).replace(0, np.nan)
    b = radj126 - radj63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_radjmom_252d_base_v014_signal(closeadj):
    # 252d risk-adjusted momentum minus its 252d trailing mean (excess Sharpe-mom)
    roc = _f02_roc(closeadj, 252)
    vol = _f02_vol(closeadj, 126)
    ratio = roc / (vol * np.sqrt(252)).replace(0, np.nan)
    b = ratio - ratio.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Sortino spread: upside/downside deviation ratio (asymmetry, not level) ---
def f02mr_f02_momentum_rotation_sortino_63d_base_v015_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    dn = _f02_dnvol(closeadj, 63)
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino ratio at 126d, de-trended vs its own EMA (so it is not a monotone of 126d ROC)
def f02mr_f02_momentum_rotation_sortino_126d_base_v016_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    dn = _f02_dnvol(closeadj, 126)
    ratio = roc / (dn * np.sqrt(126)).replace(0, np.nan)
    b = ratio - ratio.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- daily-Sharpe (21d) ranked vs its 252d history (regime position of short Sharpe) ---
def f02mr_f02_momentum_rotation_sharpe_21d_base_v017_signal(closeadj):
    r = closeadj.pct_change()
    sh = _mean(r, 21) / _std(r, 21).replace(0, np.nan)
    b = _rank(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# daily-Sharpe (63d) ranked vs its own 504d history (long-memory regime position of Sharpe)
def f02mr_f02_momentum_rotation_sharpe_63d_base_v018_signal(closeadj):
    r = closeadj.pct_change()
    sh = _mean(r, 63) / _std(r, 63).replace(0, np.nan)
    b = _rank(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum concentration (126d): share of total abs daily move contributed by the largest day ---
def f02mr_f02_momentum_rotation_momconc_126d_base_v019_signal(closeadj):
    ar = closeadj.pct_change().abs()
    mx = ar.rolling(126, min_periods=63).max()
    tot = ar.rolling(126, min_periods=63).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- up-day hit-rate / consistency ---
def f02mr_f02_momentum_rotation_hitrate_21d_base_v020_signal(closeadj):
    # blended hit-rate over 21d/42d so the value is continuous, not 21 discrete steps
    hr_fast = _f02_hitrate(closeadj, 21) - 0.5
    hr_slow = _f02_hitrate(closeadj, 42) - 0.5
    b = 0.6 * hr_fast + 0.4 * hr_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitrate_63d_base_v021_signal(closeadj):
    # 63d up-day hit-rate z-scored vs its own 252d history (continuous, de-trended)
    hr = _f02_hitrate(closeadj, 63)
    b = _z(hr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_hitrate_126d_base_v022_signal(closeadj):
    # 126d hit-rate minus its slow EMA (continuous consistency displacement)
    hr = _f02_hitrate(closeadj, 126)
    b = hr - hr.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consistency: hit-rate-tilt times the magnitude of momentum (directional agreement, continuous)
def f02mr_f02_momentum_rotation_consist_63d_base_v023_signal(closeadj):
    hr = _f02_hitrate(closeadj, 63) - 0.5
    roc = _f02_roc(closeadj, 63)
    b = (2.0 * hr) * roc.abs() * np.sign(roc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average up-day magnitude vs average down-day magnitude (per-event payoff asymmetry, sign-free)
def f02mr_f02_momentum_rotation_gainloss_63d_base_v024_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0)
    neg = r.where(r < 0)
    up_avg = pos.abs().rolling(63, min_periods=21).mean()
    dn_avg = neg.abs().rolling(63, min_periods=21).mean()
    b = np.log(up_avg.replace(0, np.nan) / dn_avg.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum rank / percentile vs own history ---
def f02mr_f02_momentum_rotation_rocrank_63d_base_v025_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = _rank(roc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocrank_126d_base_v026_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = _rank(roc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_rocrank_252d_base_v027_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = _rank(roc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-window momentum dispersion / term-structure spreads ---
# spread: short momentum (21d annualized) minus long momentum (252d) -> rotation
def f02mr_f02_momentum_rotation_mtspr_21v252_base_v028_signal(closeadj):
    short = _f02_logmom(closeadj, 21) * 12.0
    long = _f02_logmom(closeadj, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 63d momentum minus 252d momentum (intermediate vs long)
def f02mr_f02_momentum_rotation_mtspr_63v252_base_v029_signal(closeadj):
    mid = _f02_logmom(closeadj, 63) * 4.0
    long = _f02_logmom(closeadj, 252)
    b = mid - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 21d vs 63d momentum (acceleration of short-horizon momentum)
def f02mr_f02_momentum_rotation_mtspr_21v63_base_v030_signal(closeadj):
    s = _f02_logmom(closeadj, 21) * 3.0
    m = _f02_logmom(closeadj, 63)
    b = s - m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of momentum across 5/21/63/126/252 (term-structure spread of momentum)
def f02mr_f02_momentum_rotation_momdisp_multi_base_v031_signal(closeadj):
    a = _f02_logmom(closeadj, 5) * 50.4
    b1 = _f02_logmom(closeadj, 21) * 12.0
    c = _f02_logmom(closeadj, 63) * 4.0
    d = _f02_logmom(closeadj, 126) * 2.0
    e = _f02_logmom(closeadj, 252)
    stacked = pd.concat([a, b1, c, d, e], axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum term-structure R^2: how well annualized-mom fits a line in log-horizon (term-structure regularity)
def f02mr_f02_momentum_rotation_momtslope_multi_base_v032_signal(closeadj):
    ws = [21, 63, 126, 252]
    ann = [_f02_logmom(closeadj, w) * (252.0 / w) for w in ws]
    x = np.log(np.array(ws, dtype=float))
    xd = x - x.mean()
    denom = (xd ** 2).sum()
    stacked = pd.concat(ann, axis=1)
    ym = stacked.mean(axis=1)
    num = sum(xd[i] * (ann[i] - ym) for i in range(len(ws)))
    slope = num / denom
    fitted_ss = (slope ** 2) * denom
    total_ss = sum((ann[i] - ym) ** 2 for i in range(len(ws)))
    b = (fitted_ss / total_ss.replace(0, np.nan)) * np.sign(slope)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum acceleration (change in ROC) ---
# 63d ROC now vs a quarter ago (momentum acceleration, level)
def f02mr_f02_momentum_rotation_rocaccel_63d_base_v033_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ROC now vs half a year ago
def f02mr_f02_momentum_rotation_rocaccel_126d_base_v034_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    b = roc - roc.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA momentum (exponentially weighted return drift) ---
def f02mr_f02_momentum_rotation_ewmamom_21d_base_v035_signal(closeadj):
    r = closeadj.pct_change()
    b = r.ewm(span=21, min_periods=10).mean() * 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_ewmamom_63d_base_v036_signal(closeadj):
    r = closeadj.pct_change()
    b = r.ewm(span=63, min_periods=21).mean() * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regression-slope momentum: OLS slope of log-price over the window (trend speed) ---
def _f02_logslope(close, w):
    lp = np.log(close.replace(0, np.nan))

    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xd = x - x.mean()
        denom = (xd ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(xd, a - a.mean()) / denom)
    return lp.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def f02mr_f02_momentum_rotation_logslope_63d_base_v037_signal(closeadj):
    b = _f02_logslope(closeadj, 63) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f02mr_f02_momentum_rotation_logslope_126d_base_v038_signal(closeadj):
    b = _f02_logslope(closeadj, 126) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum signed magnitude (sqrt compression to tame outliers) ---
def f02mr_f02_momentum_rotation_signmag_63d_base_v039_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = np.sign(roc) * roc.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tanh-squashed momentum displacement: bounded 5d mom minus bounded 21d mom (micro rotation) ---
def f02mr_f02_momentum_rotation_tanhmom_21d_base_v040_signal(closeadj):
    fast = np.tanh(10.0 * _f02_roc(closeadj, 5))
    slow = np.tanh(10.0 * _f02_roc(closeadj, 21) / 4.0)
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum x volume confirmation (dollar-volume weighting on >21d uses closeadj) ---
def f02mr_f02_momentum_rotation_momdolvol_63d_base_v041_signal(closeadj, volume):
    roc = _f02_roc(closeadj, 63)
    dv = (closeadj * volume)
    dvz = _z(dv, 63)
    b = roc * (1.0 + np.tanh(dvz))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative volume-confirmed up-day pressure over a quarter
def f02mr_f02_momentum_rotation_volconfirm_63d_base_v042_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    sign_dv = np.sign(r) * dv
    b = sign_dv.rolling(63, min_periods=21).sum() / dv.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum quality: ROC divided by max drawdown over same window (Calmar-like, momentum-side) ---
def f02mr_f02_momentum_rotation_calmar_126d_base_v043_signal(closeadj):
    roc = _f02_roc(closeadj, 126)
    roll_peak = closeadj.rolling(126, min_periods=63).max()
    dd = (closeadj / roll_peak.replace(0, np.nan) - 1.0).rolling(126, min_periods=63).min().abs()
    b = roc / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- return stability spread: 21d info-ratio minus 126d info-ratio (consistency rotation) ---
def f02mr_f02_momentum_rotation_retstability_63d_base_v044_signal(closeadj):
    r = closeadj.pct_change()
    ir_fast = _mean(r, 21) / _std(r, 21).replace(0, np.nan) * np.sqrt(21.0)
    ir_slow = _mean(r, 126) / _std(r, 126).replace(0, np.nan) * np.sqrt(126.0)
    b = ir_fast - ir_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- max up-streak length normalized by window, scaled by quarter momentum (continuous) ---
def f02mr_f02_momentum_rotation_upstreak_63d_base_v045_signal(closeadj):
    up = (closeadj.pct_change() > 0).astype(float)

    def _maxrun(a):
        best = 0
        cur = 0
        for v in a:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    streak = up.rolling(63, min_periods=21).apply(_maxrun, raw=True) / 63.0
    roc = _f02_roc(closeadj, 63)
    b = streak * (1.0 + np.tanh(5.0 * roc))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum percentile spread: rank(63d) minus rank(252d) (rotation in rank space) ---
def f02mr_f02_momentum_rotation_rankspr_63v252_base_v046_signal(closeadj):
    r63 = _rank(_f02_roc(closeadj, 63), 252)
    r252 = _rank(_f02_roc(closeadj, 252), 504)
    b = r63 - r252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum convexity ratio: recent-quarter vs prior-quarter momentum ratio (curvature, scale-free) ---
def f02mr_f02_momentum_rotation_momconvex_63d_base_v047_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    recent = lp - lp.shift(63)
    prior = lp.shift(63) - lp.shift(126)
    b = (recent - prior) / (recent.abs() + prior.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- weekly momentum z-score (short horizon, de-meaned) ---
def f02mr_f02_momentum_rotation_wkmomz_5d_base_v048_signal(closeadj):
    roc = _f02_roc(closeadj, 5)
    b = _z(roc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- residual momentum: 252d return minus its 504d trailing average (excess long mom) ---
def f02mr_f02_momentum_rotation_excessmom_252d_base_v049_signal(closeadj):
    roc = _f02_roc(closeadj, 252)
    b = roc - roc.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- soft momentum diffusion: avg tanh of annualized momentum across horizons ---
def f02mr_f02_momentum_rotation_momdiffuse_multi_base_v050_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    soft = sum(np.tanh(3.0 * _f02_logmom(closeadj, w) * (252.0 / w)) for w in ws)
    b = soft / float(len(ws))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum acceleration ratio: 21d annualized vs 126d annualized (rotation strength) ---
def f02mr_f02_momentum_rotation_accelratio_21v126_base_v051_signal(closeadj):
    short = _f02_logmom(closeadj, 21) * (252.0 / 21.0)
    long = _f02_logmom(closeadj, 126) * (252.0 / 126.0)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- risk-adjusted 12-1 momentum, ranked vs 504d history (regime position of skip-month mom) ---
def f02mr_f02_momentum_rotation_radj12m1_252d_base_v052_signal(closeadj):
    m = _f02_12_1(closeadj)
    vol = _f02_vol(closeadj, 252)
    ratio = m / (vol * np.sqrt(231)).replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- path efficiency (unsigned trendiness): net move / sum of abs daily moves over 63d ---
def f02mr_f02_momentum_rotation_patheff_63d_base_v053_signal(closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    gross = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in 126d path efficiency over a quarter (trendiness becoming choppy or vice versa)
def f02mr_f02_momentum_rotation_patheff_126d_base_v054_signal(closeadj):
    net = (closeadj - closeadj.shift(126)).abs()
    gross = closeadj.diff().abs().rolling(126, min_periods=63).sum()
    eff = net / gross.replace(0, np.nan)
    b = eff - eff.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum reversal flag: short-term ROC opposing long-term ROC sign ---
def f02mr_f02_momentum_rotation_revtilt_21v252_base_v055_signal(closeadj):
    short = _f02_roc(closeadj, 21)
    long = _f02_roc(closeadj, 252)
    b = -np.sign(long) * short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum z-score of 5d return averaged (smoothed micro-momentum) ---
def f02mr_f02_momentum_rotation_micromom_5d_base_v056_signal(closeadj):
    roc = _f02_roc(closeadj, 5)
    b = roc.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- rolling cumulative-return skew of daily returns (momentum tail shape) ---
def f02mr_f02_momentum_rotation_retskew_63d_base_v057_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-scaled momentum diffusion index (diffusion x risk-adj 63d mom) ---
def f02mr_f02_momentum_rotation_diffstrength_63d_base_v058_signal(closeadj):
    ws = [5, 21, 63]
    pos = sum((_f02_roc(closeadj, w) > 0).astype(float) for w in ws) / float(len(ws)) - 0.5
    radj = _f02_roc(closeadj, 63) / (_f02_vol(closeadj, 63) * np.sqrt(63)).replace(0, np.nan)
    b = pos * radj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum vs its EMA (displacement of momentum from its trend) ---
def f02mr_f02_momentum_rotation_momdisp_63d_base_v059_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    b = roc - roc.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- best vs worst window momentum spread (rotation breadth) ---
def f02mr_f02_momentum_rotation_bestworst_multi_base_v060_signal(closeadj):
    a = _f02_logmom(closeadj, 21) * 12.0
    b1 = _f02_logmom(closeadj, 63) * 4.0
    c = _f02_logmom(closeadj, 126) * 2.0
    d = _f02_logmom(closeadj, 252)
    stacked = pd.concat([a, b1, c, d], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum persistence: autocorrelation of 21d non-overlapping-ish returns ---
def f02mr_f02_momentum_rotation_momac_63d_base_v061_signal(closeadj):
    r = closeadj.pct_change()

    def _ac(a):
        a0 = a[:-1]
        a1 = a[1:]
        s0 = a0.std()
        s1 = a1.std()
        if s0 == 0 or s1 == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])
    b = r.rolling(63, min_periods=30).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-regime-gated momentum: sign of 63d momentum gated by vol-term-structure (short/long vol) ---
def f02mr_f02_momentum_rotation_volregmom_63d_base_v062_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    vshort = _f02_vol(closeadj, 21)
    vlong = _f02_vol(closeadj, 126)
    vts = _z(vshort / vlong.replace(0, np.nan), 252)
    b = np.sign(roc) * np.tanh(vts)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum acceleration via slope difference (logslope short minus long) ---
def f02mr_f02_momentum_rotation_slopespr_63v126_base_v063_signal(closeadj):
    s = _f02_logslope(closeadj, 63) * 252.0
    l = _f02_logslope(closeadj, 126) * 252.0
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cumulative up-volume minus down-volume momentum (volume-weighted drift) ---
def f02mr_f02_momentum_rotation_volmomflow_126d_base_v064_signal(closeadj, volume):
    r = closeadj.pct_change()
    dv = closeadj * volume
    up = dv.where(r > 0, 0.0).rolling(126, min_periods=63).sum()
    dn = dv.where(r < 0, 0.0).rolling(126, min_periods=63).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum half-life proxy: ratio of 21d to 63d EWMA drift ---
def f02mr_f02_momentum_rotation_momhalflife_base_v065_signal(closeadj):
    r = closeadj.pct_change()
    fast = r.ewm(span=21, min_periods=10).mean()
    slow = r.ewm(span=63, min_periods=21).mean()
    b = (fast - slow) / (fast.abs() + slow.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- 21d momentum percentile vs its own 126d distribution ---
def f02mr_f02_momentum_rotation_rocrank_21d_base_v066_signal(closeadj):
    roc = _f02_roc(closeadj, 21)
    b = _rank(roc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- intermediate skip-month momentum (126-21) z-scored vs 252d history (de-trended) ---
def f02mr_f02_momentum_rotation_radj6m1_126d_base_v067_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(126).replace(0, np.nan) - 1.0
    vol = _f02_vol(closeadj, 126)
    ratio = m / (vol * np.sqrt(105)).replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum sign agreement count across windows times magnitude of 252d ---
def f02mr_f02_momentum_rotation_signagree_multi_base_v068_signal(closeadj):
    ws = [21, 63, 126, 252]
    sgn = sum(np.sign(_f02_roc(closeadj, w)) for w in ws) / float(len(ws))
    b = sgn * _f02_logmom(closeadj, 252).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-frequency regime: down-day fraction z-scored, signed by momentum direction ---
def f02mr_f02_momentum_rotation_dnfreqmom_63d_base_v069_signal(closeadj):
    roc = _f02_roc(closeadj, 63)
    dn = (closeadj.pct_change() < 0).astype(float).rolling(63, min_periods=21).mean()
    dnz = _z(dn, 252)
    b = -np.sign(roc) * dnz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- sign-flip choppiness index (de-meaned): how erratic the daily direction is ---
def f02mr_f02_momentum_rotation_choppen_63d_base_v070_signal(closeadj):
    sgn = np.sign(closeadj.pct_change())
    flips = (sgn != sgn.shift(1)).astype(float)
    chop = flips.rolling(63, min_periods=21).mean()
    b = _z(chop, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure curvature of momentum: short + long - 2*mid ---
def f02mr_f02_momentum_rotation_momcurv_multi_base_v071_signal(closeadj):
    short = _f02_logmom(closeadj, 21) * 12.0
    mid = _f02_logmom(closeadj, 63) * 4.0
    long = _f02_logmom(closeadj, 252)
    b = short + long - 2.0 * mid
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-target scaled momentum: difference between vol-scaled 63d and 126d momentum ---
def f02mr_f02_momentum_rotation_voltarget_63d_base_v072_signal(closeadj):
    roc63 = _f02_roc(closeadj, 63)
    roc126 = _f02_roc(closeadj, 126)
    va63 = _f02_vol(closeadj, 63) * np.sqrt(252)
    va126 = _f02_vol(closeadj, 126) * np.sqrt(252)
    s63 = roc63 * (0.20 / va63.replace(0, np.nan))
    s126 = roc126 * (0.20 / va126.replace(0, np.nan))
    b = s63 - s126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- momentum t-stat (252d) acceleration: current t-stat minus a quarter ago ---
def f02mr_f02_momentum_rotation_momtstat_252d_base_v073_signal(closeadj):
    lm = _f02_logmom(closeadj, 252)
    vol = _f02_vol(closeadj, 252)
    tstat = lm / (vol * np.sqrt(252)).replace(0, np.nan)
    b = tstat - tstat.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- sequential momentum dispersion across four non-overlapping quarters (rotation breadth) ---
def f02mr_f02_momentum_rotation_seqmom_63d_base_v074_signal(closeadj):
    q1 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    q2 = np.log(closeadj.shift(63).replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    q3 = np.log(closeadj.shift(126).replace(0, np.nan) / closeadj.shift(189).replace(0, np.nan))
    q4 = np.log(closeadj.shift(189).replace(0, np.nan) / closeadj.shift(252).replace(0, np.nan))
    stacked = pd.concat([q1, q2, q3, q4], axis=1)
    b = stacked.std(axis=1) * np.sign(q1 - q4)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite rotation score: rank-weighted blend of short and long risk-adj mom ---
def f02mr_f02_momentum_rotation_rotscore_multi_base_v075_signal(closeadj):
    r21 = _rank(_f02_roc(closeadj, 21), 252)
    r252 = _rank(_f02_roc(closeadj, 252), 504)
    radj = _f02_roc(closeadj, 63) / (_f02_vol(closeadj, 63) * np.sqrt(63)).replace(0, np.nan)
    b = 0.5 * (r21 - r252) + 0.5 * np.tanh(radj)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02mr_f02_momentum_rotation_roc_5d_base_v001_signal,
    f02mr_f02_momentum_rotation_roc_21d_base_v002_signal,
    f02mr_f02_momentum_rotation_roc_63d_base_v003_signal,
    f02mr_f02_momentum_rotation_roc_126d_base_v004_signal,
    f02mr_f02_momentum_rotation_roc_252d_base_v005_signal,
    f02mr_f02_momentum_rotation_logmomz_63d_base_v006_signal,
    f02mr_f02_momentum_rotation_logmomz_126d_base_v007_signal,
    f02mr_f02_momentum_rotation_mom12m1_252d_base_v008_signal,
    f02mr_f02_momentum_rotation_mom12m1z_252d_base_v009_signal,
    f02mr_f02_momentum_rotation_mom6m1_126d_base_v010_signal,
    f02mr_f02_momentum_rotation_radjmom_21d_base_v011_signal,
    f02mr_f02_momentum_rotation_radjmom_63d_base_v012_signal,
    f02mr_f02_momentum_rotation_radjmom_126d_base_v013_signal,
    f02mr_f02_momentum_rotation_radjmom_252d_base_v014_signal,
    f02mr_f02_momentum_rotation_sortino_63d_base_v015_signal,
    f02mr_f02_momentum_rotation_sortino_126d_base_v016_signal,
    f02mr_f02_momentum_rotation_sharpe_21d_base_v017_signal,
    f02mr_f02_momentum_rotation_sharpe_63d_base_v018_signal,
    f02mr_f02_momentum_rotation_momconc_126d_base_v019_signal,
    f02mr_f02_momentum_rotation_hitrate_21d_base_v020_signal,
    f02mr_f02_momentum_rotation_hitrate_63d_base_v021_signal,
    f02mr_f02_momentum_rotation_hitrate_126d_base_v022_signal,
    f02mr_f02_momentum_rotation_consist_63d_base_v023_signal,
    f02mr_f02_momentum_rotation_gainloss_63d_base_v024_signal,
    f02mr_f02_momentum_rotation_rocrank_63d_base_v025_signal,
    f02mr_f02_momentum_rotation_rocrank_126d_base_v026_signal,
    f02mr_f02_momentum_rotation_rocrank_252d_base_v027_signal,
    f02mr_f02_momentum_rotation_mtspr_21v252_base_v028_signal,
    f02mr_f02_momentum_rotation_mtspr_63v252_base_v029_signal,
    f02mr_f02_momentum_rotation_mtspr_21v63_base_v030_signal,
    f02mr_f02_momentum_rotation_momdisp_multi_base_v031_signal,
    f02mr_f02_momentum_rotation_momtslope_multi_base_v032_signal,
    f02mr_f02_momentum_rotation_rocaccel_63d_base_v033_signal,
    f02mr_f02_momentum_rotation_rocaccel_126d_base_v034_signal,
    f02mr_f02_momentum_rotation_ewmamom_21d_base_v035_signal,
    f02mr_f02_momentum_rotation_ewmamom_63d_base_v036_signal,
    f02mr_f02_momentum_rotation_logslope_63d_base_v037_signal,
    f02mr_f02_momentum_rotation_logslope_126d_base_v038_signal,
    f02mr_f02_momentum_rotation_signmag_63d_base_v039_signal,
    f02mr_f02_momentum_rotation_tanhmom_21d_base_v040_signal,
    f02mr_f02_momentum_rotation_momdolvol_63d_base_v041_signal,
    f02mr_f02_momentum_rotation_volconfirm_63d_base_v042_signal,
    f02mr_f02_momentum_rotation_calmar_126d_base_v043_signal,
    f02mr_f02_momentum_rotation_retstability_63d_base_v044_signal,
    f02mr_f02_momentum_rotation_upstreak_63d_base_v045_signal,
    f02mr_f02_momentum_rotation_rankspr_63v252_base_v046_signal,
    f02mr_f02_momentum_rotation_momconvex_63d_base_v047_signal,
    f02mr_f02_momentum_rotation_wkmomz_5d_base_v048_signal,
    f02mr_f02_momentum_rotation_excessmom_252d_base_v049_signal,
    f02mr_f02_momentum_rotation_momdiffuse_multi_base_v050_signal,
    f02mr_f02_momentum_rotation_accelratio_21v126_base_v051_signal,
    f02mr_f02_momentum_rotation_radj12m1_252d_base_v052_signal,
    f02mr_f02_momentum_rotation_patheff_63d_base_v053_signal,
    f02mr_f02_momentum_rotation_patheff_126d_base_v054_signal,
    f02mr_f02_momentum_rotation_revtilt_21v252_base_v055_signal,
    f02mr_f02_momentum_rotation_micromom_5d_base_v056_signal,
    f02mr_f02_momentum_rotation_retskew_63d_base_v057_signal,
    f02mr_f02_momentum_rotation_diffstrength_63d_base_v058_signal,
    f02mr_f02_momentum_rotation_momdisp_63d_base_v059_signal,
    f02mr_f02_momentum_rotation_bestworst_multi_base_v060_signal,
    f02mr_f02_momentum_rotation_momac_63d_base_v061_signal,
    f02mr_f02_momentum_rotation_volregmom_63d_base_v062_signal,
    f02mr_f02_momentum_rotation_slopespr_63v126_base_v063_signal,
    f02mr_f02_momentum_rotation_volmomflow_126d_base_v064_signal,
    f02mr_f02_momentum_rotation_momhalflife_base_v065_signal,
    f02mr_f02_momentum_rotation_rocrank_21d_base_v066_signal,
    f02mr_f02_momentum_rotation_radj6m1_126d_base_v067_signal,
    f02mr_f02_momentum_rotation_signagree_multi_base_v068_signal,
    f02mr_f02_momentum_rotation_dnfreqmom_63d_base_v069_signal,
    f02mr_f02_momentum_rotation_choppen_63d_base_v070_signal,
    f02mr_f02_momentum_rotation_momcurv_multi_base_v071_signal,
    f02mr_f02_momentum_rotation_voltarget_63d_base_v072_signal,
    f02mr_f02_momentum_rotation_momtstat_252d_base_v073_signal,
    f02mr_f02_momentum_rotation_seqmom_63d_base_v074_signal,
    f02mr_f02_momentum_rotation_rotscore_multi_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_MOMENTUM_ROTATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f02_momentum_rotation_base_001_075_claude: %d features pass" % n_features)
