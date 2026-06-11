"""
110_tail_risk_evt — 3rd Derivatives (Features evt_drv3_001-025)
Domain: rate of change of 2nd-derivative tail-risk features — acceleration of
        VaR velocity, ES velocity, Hill-index velocity, and downside-risk velocity.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _neg_returns(close: pd.Series) -> pd.Series:
    return -_log_returns(close)


def _rolling_var(close: pd.Series, w: int, q: float) -> pd.Series:
    r = _neg_returns(close)
    return r.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _rolling_es(close: pd.Series, w: int, q: float) -> pd.Series:
    r = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        threshold = np.quantile(x, q)
        tail = x[x >= threshold]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return r.rolling(w, min_periods=max(2, w // 2)).apply(_es, raw=True)


def _rolling_hill(close: pd.Series, w: int, k: int) -> pd.Series:
    losses = _neg_returns(close)
    def _hill(x):
        x = x[~np.isnan(x)]
        if len(x) < k + 2 or k < 1:
            return np.nan
        xs = np.sort(x)[::-1]
        xk1 = xs[k]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:k] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    return losses.rolling(w, min_periods=max(k + 2, w // 2)).apply(_hill, raw=True)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def evt_drv3_001_var95_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of VaR95(63d) — acceleration of medium-term VaR velocity."""
    vel = _rolling_var(close, _TD_QTR, 0.95).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_002_var95_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of VaR95(21d) — acceleration of short-term VaR velocity."""
    vel = _rolling_var(close, _TD_MON, 0.95).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_003_var99_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of VaR99(63d) — acceleration of 99th-percentile loss velocity."""
    vel = _rolling_var(close, _TD_QTR, 0.99).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_004_es95_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of ES95(63d) — acceleration of CVaR expansion velocity."""
    vel = _rolling_es(close, _TD_QTR, 0.95).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_005_es99_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of ES99(63d) — acceleration of extreme CVaR expansion."""
    vel = _rolling_es(close, _TD_QTR, 0.99).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_006_hill_63d_k10_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Hill index(63d,k=10) — acceleration of tail-index velocity."""
    vel = _rolling_hill(close, _TD_QTR, 10).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_007_max_loss_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day max loss — acceleration of loss-record change."""
    ml = _rolling_max(_neg_returns(close), _TD_QTR)
    vel = ml.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_008_var95_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in VaR95(21d) — jerk in monthly VaR change."""
    vel21 = _rolling_var(close, _TD_MON, 0.95).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def evt_drv3_009_es95_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of ES95(21d) — acceleration of short-term CVaR velocity."""
    vel = _rolling_es(close, _TD_MON, 0.95).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_010_loss_skew_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day return skewness — acceleration of skewness deepening."""
    r = _log_returns(close)
    skew = r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_011_loss_kurt_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day kurtosis — acceleration of fat-tail build-up."""
    r = _log_returns(close)
    kurt = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    vel = kurt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_012_downside_dev_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of downside deviation (63d) — acceleration of semi-vol expansion."""
    r = _log_returns(close)
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * _TD_YEAR)
    vel = semi_std.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_013_var_ratio_21vs63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of VaR95(21d)/VaR95(63d) — acceleration of short vs medium VaR divergence."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    ratio = _safe_div(v21, v63.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_014_es_vs_var_ratio_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of ES95(63d)/VaR95(63d) — acceleration of tail shape change."""
    es = _rolling_es(close, _TD_QTR, 0.95)
    var = _rolling_var(close, _TD_QTR, 0.95)
    ratio = _safe_div(es, var.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_015_var95_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in VaR95(63d) — jerk in monthly medium-term VaR."""
    vel21 = _rolling_var(close, _TD_QTR, 0.95).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def evt_drv3_016_neg_ret_frac_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day negative-return fraction — acceleration of loss-day frequency."""
    r = _log_returns(close)
    frac = _rolling_sum((r < 0.0).astype(float), _TD_QTR) / _TD_QTR
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_017_hill_252d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in Hill(252d,k=20) — jerk in long-run tail index."""
    vel21 = _rolling_hill(close, _TD_YEAR, 20).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def evt_drv3_018_var95_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of VaR95(63d)."""
    vel = _rolling_var(close, _TD_QTR, 0.95).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def evt_drv3_019_es95_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of ES95(63d)."""
    vel = _rolling_es(close, _TD_QTR, 0.95).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def evt_drv3_020_hill_63d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of Hill(63d,k=10) — rate of slope change."""
    slope21 = _linslope(_rolling_hill(close, _TD_QTR, 10), _TD_MON)
    return slope21.diff(_TD_WEEK)


def evt_drv3_021_omega_ratio_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Omega ratio — acceleration of gain/loss balance change."""
    r = _log_returns(close)
    gains = r.where(r > 0.0, 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    losses = r.where(r < 0.0, 0.0).abs().rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    omega = _safe_div(gains, losses.clip(lower=_EPS))
    vel = omega.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_022_sortino_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Sortino ratio (63d) — acceleration of risk-adj return deterioration."""
    r = _log_returns(close)
    mean_ret = _rolling_mean(r, _TD_QTR) * _TD_YEAR
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * _TD_YEAR)
    sortino = _safe_div(mean_ret, semi_std.clip(lower=_EPS))
    vel = sortino.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_023_max_loss_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 63-day max loss."""
    ml = _rolling_max(_neg_returns(close), _TD_QTR)
    vel = ml.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def evt_drv3_024_tail_conc_95_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of tail concentration (63d) — acceleration of loss mass concentration."""
    losses = _neg_returns(close)
    def _tail_conc(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail_sum = np.sum(x[x >= thr])
        total = np.sum(x)
        return float(tail_sum / (total + _EPS))
    tc = losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_tail_conc, raw=True)
    vel = tc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def evt_drv3_025_hill_ratio_63vs252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Hill(63d)/Hill(252d) ratio — acceleration of tail divergence."""
    h63 = _rolling_hill(close, _TD_QTR, 10)
    h252 = _rolling_hill(close, _TD_YEAR, 15)
    ratio = _safe_div(h63, h252.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

TAIL_RISK_EVT_REGISTRY_3RD_DERIVATIVES = {
    "evt_drv3_001_var95_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_001_var95_63d_5d_diff_5d_diff},
    "evt_drv3_002_var95_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_002_var95_21d_5d_diff_5d_diff},
    "evt_drv3_003_var99_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_003_var99_63d_5d_diff_5d_diff},
    "evt_drv3_004_es95_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_004_es95_63d_5d_diff_5d_diff},
    "evt_drv3_005_es99_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_005_es99_63d_5d_diff_5d_diff},
    "evt_drv3_006_hill_63d_k10_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_006_hill_63d_k10_5d_diff_5d_diff},
    "evt_drv3_007_max_loss_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_007_max_loss_63d_5d_diff_5d_diff},
    "evt_drv3_008_var95_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_008_var95_21d_21d_diff_5d_diff},
    "evt_drv3_009_es95_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_009_es95_21d_5d_diff_5d_diff},
    "evt_drv3_010_loss_skew_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_010_loss_skew_63d_5d_diff_5d_diff},
    "evt_drv3_011_loss_kurt_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_011_loss_kurt_63d_5d_diff_5d_diff},
    "evt_drv3_012_downside_dev_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_012_downside_dev_63d_5d_diff_5d_diff},
    "evt_drv3_013_var_ratio_21vs63_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_013_var_ratio_21vs63_5d_diff_5d_diff},
    "evt_drv3_014_es_vs_var_ratio_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_014_es_vs_var_ratio_5d_diff_5d_diff},
    "evt_drv3_015_var95_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_015_var95_63d_21d_diff_5d_diff},
    "evt_drv3_016_neg_ret_frac_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_016_neg_ret_frac_63d_5d_diff_5d_diff},
    "evt_drv3_017_hill_252d_21d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_017_hill_252d_21d_diff_5d_diff},
    "evt_drv3_018_var95_63d_slope_21d": {"inputs": ["close"], "func": evt_drv3_018_var95_63d_slope_21d},
    "evt_drv3_019_es95_63d_slope_21d": {"inputs": ["close"], "func": evt_drv3_019_es95_63d_slope_21d},
    "evt_drv3_020_hill_63d_slope_5d_diff": {"inputs": ["close"], "func": evt_drv3_020_hill_63d_slope_5d_diff},
    "evt_drv3_021_omega_ratio_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_021_omega_ratio_63d_5d_diff_5d_diff},
    "evt_drv3_022_sortino_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_022_sortino_63d_5d_diff_5d_diff},
    "evt_drv3_023_max_loss_63d_slope_21d": {"inputs": ["close"], "func": evt_drv3_023_max_loss_63d_slope_21d},
    "evt_drv3_024_tail_conc_95_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_024_tail_conc_95_63d_5d_diff_5d_diff},
    "evt_drv3_025_hill_ratio_63vs252_5d_diff_5d_diff": {"inputs": ["close"], "func": evt_drv3_025_hill_ratio_63vs252_5d_diff_5d_diff},
}
