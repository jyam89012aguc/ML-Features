"""
110_tail_risk_evt — 2nd Derivatives (Features evt_drv2_001-025)
Domain: rate of change of base tail-risk / extreme-value features —
        velocity of VaR, ES, Hill index, POT counts, and downside-risk measures.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def evt_drv2_001_var95_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of VaR95(63d) — velocity of medium-term tail-risk expansion."""
    return _rolling_var(close, _TD_QTR, 0.95).diff(_TD_WEEK)


def evt_drv2_002_var95_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of VaR95(21d) — velocity of short-term tail-risk expansion."""
    return _rolling_var(close, _TD_MON, 0.95).diff(_TD_WEEK)


def evt_drv2_003_var99_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of VaR99(63d) — velocity of 99th-percentile loss."""
    return _rolling_var(close, _TD_QTR, 0.99).diff(_TD_WEEK)


def evt_drv2_004_es95_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ES95(63d) — velocity of CVaR expansion."""
    return _rolling_es(close, _TD_QTR, 0.95).diff(_TD_WEEK)


def evt_drv2_005_es99_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ES99(63d) — velocity of extreme CVaR expansion."""
    return _rolling_es(close, _TD_QTR, 0.99).diff(_TD_WEEK)


def evt_drv2_006_hill_63d_k10_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Hill index(63d,k=10) — velocity of tail-index change."""
    return _rolling_hill(close, _TD_QTR, 10).diff(_TD_WEEK)


def evt_drv2_007_hill_252d_k20_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of Hill index(252d,k=20) — monthly velocity of long-run tail index."""
    return _rolling_hill(close, _TD_YEAR, 20).diff(_TD_MON)


def evt_drv2_008_max_loss_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day max loss — how fast the max loss record is changing."""
    ml = _rolling_max(_neg_returns(close), _TD_QTR)
    return ml.diff(_TD_WEEK)


def evt_drv2_009_max_loss_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day max loss."""
    ml = _rolling_max(_neg_returns(close), _TD_MON)
    return ml.diff(_TD_WEEK)


def evt_drv2_010_var95_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of VaR95(21d) — monthly velocity of short-term VaR."""
    return _rolling_var(close, _TD_MON, 0.95).diff(_TD_MON)


def evt_drv2_011_es95_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ES95(21d) — velocity of short-term CVaR."""
    return _rolling_es(close, _TD_MON, 0.95).diff(_TD_WEEK)


def evt_drv2_012_loss_skew_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day return skewness — velocity of skewness deepening."""
    r = _log_returns(close)
    skew = r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    return skew.diff(_TD_WEEK)


def evt_drv2_013_loss_kurt_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day return kurtosis — velocity of kurtosis increase."""
    r = _log_returns(close)
    kurt = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    return kurt.diff(_TD_WEEK)


def evt_drv2_014_downside_dev_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of annualized downside deviation (63d) — velocity of semi-vol expansion."""
    r = _log_returns(close)
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * _TD_YEAR)
    return semi_std.diff(_TD_WEEK)


def evt_drv2_015_var_ratio_21vs63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of VaR95(21d)/VaR95(63d) ratio — velocity of short-term tail spike."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    ratio = _safe_div(v21, v63.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def evt_drv2_016_hill_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63d Hill index (trend in tail heaviness)."""
    return _linslope(_rolling_hill(close, _TD_QTR, 10), _TD_MON)


def evt_drv2_017_es_vs_var_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of ES95(63d)/VaR95(63d) — velocity of tail shape change."""
    es = _rolling_es(close, _TD_QTR, 0.95)
    var = _rolling_var(close, _TD_QTR, 0.95)
    ratio = _safe_div(es, var.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def evt_drv2_018_var95_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of VaR95(63d) — monthly velocity of medium-term VaR."""
    return _rolling_var(close, _TD_QTR, 0.95).diff(_TD_MON)


def evt_drv2_019_neg_return_frac_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day fraction of negative-return days."""
    r = _log_returns(close)
    frac = _rolling_sum((r < 0.0).astype(float), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_WEEK)


def evt_drv2_020_loss_gain_asymm_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day loss/gain asymmetry ratio."""
    r = _log_returns(close)
    mean_loss = r.where(r < 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean().abs()
    mean_gain = r.where(r > 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    ratio = _safe_div(mean_loss, mean_gain.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def evt_drv2_021_omega_ratio_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Omega ratio (gains/losses sum ratio)."""
    r = _log_returns(close)
    gains = r.where(r > 0.0, 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    losses = r.where(r < 0.0, 0.0).abs().rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    omega = _safe_div(gains, losses.clip(lower=_EPS))
    return omega.diff(_TD_WEEK)


def evt_drv2_022_sortino_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Sortino ratio (63d) — velocity of risk-adjusted return deterioration."""
    r = _log_returns(close)
    mean_ret = _rolling_mean(r, _TD_QTR) * _TD_YEAR
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * _TD_YEAR)
    sortino = _safe_div(mean_ret, semi_std.clip(lower=_EPS))
    return sortino.diff(_TD_WEEK)


def evt_drv2_023_tail_concentration_95_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of tail concentration (fraction of loss mass in top-5%), 63-day window."""
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
    return tc.diff(_TD_WEEK)


def evt_drv2_024_max_loss_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day max loss — monthly velocity of annual tail-risk record."""
    ml = _rolling_max(_neg_returns(close), _TD_YEAR)
    return ml.diff(_TD_MON)


def evt_drv2_025_hill_ratio_63_vs_252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Hill(63d)/Hill(252d) ratio — velocity of recent vs long-run tail divergence."""
    h63 = _rolling_hill(close, _TD_QTR, 10)
    h252 = _rolling_hill(close, _TD_YEAR, 15)
    ratio = _safe_div(h63, h252.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

TAIL_RISK_EVT_REGISTRY_2ND_DERIVATIVES = {
    "evt_drv2_001_var95_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_001_var95_63d_5d_diff},
    "evt_drv2_002_var95_21d_5d_diff": {"inputs": ["close"], "func": evt_drv2_002_var95_21d_5d_diff},
    "evt_drv2_003_var99_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_003_var99_63d_5d_diff},
    "evt_drv2_004_es95_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_004_es95_63d_5d_diff},
    "evt_drv2_005_es99_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_005_es99_63d_5d_diff},
    "evt_drv2_006_hill_63d_k10_5d_diff": {"inputs": ["close"], "func": evt_drv2_006_hill_63d_k10_5d_diff},
    "evt_drv2_007_hill_252d_k20_21d_diff": {"inputs": ["close"], "func": evt_drv2_007_hill_252d_k20_21d_diff},
    "evt_drv2_008_max_loss_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_008_max_loss_63d_5d_diff},
    "evt_drv2_009_max_loss_21d_5d_diff": {"inputs": ["close"], "func": evt_drv2_009_max_loss_21d_5d_diff},
    "evt_drv2_010_var95_21d_21d_diff": {"inputs": ["close"], "func": evt_drv2_010_var95_21d_21d_diff},
    "evt_drv2_011_es95_21d_5d_diff": {"inputs": ["close"], "func": evt_drv2_011_es95_21d_5d_diff},
    "evt_drv2_012_loss_skew_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_012_loss_skew_63d_5d_diff},
    "evt_drv2_013_loss_kurt_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_013_loss_kurt_63d_5d_diff},
    "evt_drv2_014_downside_dev_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_014_downside_dev_63d_5d_diff},
    "evt_drv2_015_var_ratio_21vs63_5d_diff": {"inputs": ["close"], "func": evt_drv2_015_var_ratio_21vs63_5d_diff},
    "evt_drv2_016_hill_63d_slope_21d": {"inputs": ["close"], "func": evt_drv2_016_hill_63d_slope_21d},
    "evt_drv2_017_es_vs_var_ratio_5d_diff": {"inputs": ["close"], "func": evt_drv2_017_es_vs_var_ratio_5d_diff},
    "evt_drv2_018_var95_63d_21d_diff": {"inputs": ["close"], "func": evt_drv2_018_var95_63d_21d_diff},
    "evt_drv2_019_neg_return_frac_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_019_neg_return_frac_63d_5d_diff},
    "evt_drv2_020_loss_gain_asymm_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_020_loss_gain_asymm_63d_5d_diff},
    "evt_drv2_021_omega_ratio_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_021_omega_ratio_63d_5d_diff},
    "evt_drv2_022_sortino_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_022_sortino_63d_5d_diff},
    "evt_drv2_023_tail_concentration_95_63d_5d_diff": {"inputs": ["close"], "func": evt_drv2_023_tail_concentration_95_63d_5d_diff},
    "evt_drv2_024_max_loss_252d_21d_diff": {"inputs": ["close"], "func": evt_drv2_024_max_loss_252d_21d_diff},
    "evt_drv2_025_hill_ratio_63_vs_252_5d_diff": {"inputs": ["close"], "func": evt_drv2_025_hill_ratio_63_vs_252_5d_diff},
}
