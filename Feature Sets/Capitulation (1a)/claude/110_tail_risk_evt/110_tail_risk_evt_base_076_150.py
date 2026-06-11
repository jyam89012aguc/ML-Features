"""
110_tail_risk_evt — Base Features 076-150
Domain: extreme-value / tail-risk statistics of returns — tail dependence, conditional
        tail measures, Pickands estimator, moment ratio estimators, tail concentration
        metrics, multi-scale tail comparison, extreme event clustering, parametric
        tail fits, and downside risk composites.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _neg_returns(close: pd.Series) -> pd.Series:
    """Losses as positive values."""
    return -_log_returns(close)


def _rolling_var(close: pd.Series, w: int, q: float) -> pd.Series:
    """Rolling empirical VaR at quantile q (loss convention)."""
    r = _neg_returns(close)
    return r.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _pickands_estimator(losses: np.ndarray, k: int) -> float:
    """Pickands (1975) tail index estimator.
    Uses order statistics X(n-k+1), X(n-2k+1), X(n-4k+1) in descending sort."""
    x = losses[~np.isnan(losses)]
    if len(x) < 4 * k + 1 or k < 1:
        return np.nan
    x_sorted = np.sort(x)[::-1]
    x1 = x_sorted[k - 1]
    x2 = x_sorted[2 * k - 1]
    x4 = x_sorted[4 * k - 1]
    denom = x2 - x4
    if denom <= 0:
        return np.nan
    ratio = (x1 - x2) / denom
    if ratio <= 0:
        return np.nan
    return np.log(ratio) / np.log(2.0)


def _moment_ratio_estimator(losses: np.ndarray, k: int) -> float:
    """Dekkers-Einmahl-de Haan moment ratio estimator of tail index."""
    x = losses[~np.isnan(losses)]
    if len(x) < k + 2 or k < 2:
        return np.nan
    x_sorted = np.sort(x)[::-1]
    x_k1 = x_sorted[k]
    if x_k1 <= 0:
        return np.nan
    log_ratios = np.log(x_sorted[:k] / (x_k1 + _EPS))
    M1 = np.mean(log_ratios)
    M2 = np.mean(log_ratios ** 2)
    if M1 <= 0:
        return np.nan
    return M1 + 1.0 - 0.5 / (1.0 - M1 ** 2 / M2) if M2 > 0 else np.nan


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Pickands estimator variants ---

def evt_076_pickands_63d_k5(close: pd.Series) -> pd.Series:
    """Pickands tail-index estimator over 63-day window, k=5."""
    losses = _neg_returns(close)
    def _apply(x):
        return _pickands_estimator(x, 5)
    return losses.rolling(_TD_QTR, min_periods=max(25, _TD_QTR // 2)).apply(_apply, raw=True)


def evt_077_pickands_126d_k8(close: pd.Series) -> pd.Series:
    """Pickands tail-index estimator over 126-day window, k=8."""
    losses = _neg_returns(close)
    def _apply(x):
        return _pickands_estimator(x, 8)
    return losses.rolling(_TD_HALF, min_periods=max(40, _TD_HALF // 2)).apply(_apply, raw=True)


def evt_078_pickands_252d_k10(close: pd.Series) -> pd.Series:
    """Pickands tail-index estimator over 252-day window, k=10."""
    losses = _neg_returns(close)
    def _apply(x):
        return _pickands_estimator(x, 10)
    return losses.rolling(_TD_YEAR, min_periods=max(50, _TD_YEAR // 2)).apply(_apply, raw=True)


def evt_079_moment_ratio_63d_k10(close: pd.Series) -> pd.Series:
    """Dekkers-Einmahl-de Haan moment ratio estimator over 63-day window, k=10."""
    losses = _neg_returns(close)
    def _apply(x):
        return _moment_ratio_estimator(x, 10)
    return losses.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_apply, raw=True)


def evt_080_moment_ratio_126d_k15(close: pd.Series) -> pd.Series:
    """Moment ratio estimator over 126-day window, k=15."""
    losses = _neg_returns(close)
    def _apply(x):
        return _moment_ratio_estimator(x, 15)
    return losses.rolling(_TD_HALF, min_periods=max(20, _TD_HALF // 2)).apply(_apply, raw=True)


def evt_081_moment_ratio_252d_k20(close: pd.Series) -> pd.Series:
    """Moment ratio estimator over 252-day window, k=20."""
    losses = _neg_returns(close)
    def _apply(x):
        return _moment_ratio_estimator(x, 20)
    return losses.rolling(_TD_YEAR, min_periods=max(30, _TD_YEAR // 2)).apply(_apply, raw=True)


def evt_082_pickands_vs_hill_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of Pickands(63d,k=5) to Hill(63d,k=10): estimator agreement signal."""
    losses = _neg_returns(close)
    def _pick(x):
        return _pickands_estimator(x, 5)
    def _hill(x):
        from numpy import nan
        x2 = x[~np.isnan(x)]
        if len(x2) < 12 or 10 < 1:
            return nan
        xs = np.sort(x2)[::-1]
        top = xs[:10]
        xk1 = xs[10]
        if xk1 <= 0:
            return nan
        lr = np.log(top / (xk1 + _EPS))
        ml = np.mean(lr)
        if ml <= 0:
            return nan
        return 1.0 / ml
    pk = losses.rolling(_TD_QTR, min_periods=max(25, _TD_QTR // 2)).apply(_pick, raw=True)
    hl = losses.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_hill, raw=True)
    return _safe_div(pk, hl.clip(lower=_EPS))


def evt_083_tail_index_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM-smoothed Hill tail index (span=63) — tracks recent tail heaviness."""
    losses = _neg_returns(close)
    def _hill_k10(x):
        x2 = x[~np.isnan(x)]
        if len(x2) < 12:
            return np.nan
        xs = np.sort(x2)[::-1]
        xk1 = xs[10]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:10] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    rolling_hill = losses.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_hill_k10, raw=True)
    return rolling_hill.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def evt_084_tail_index_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding minimum of Hill index(63d,k=10) — minimum recorded tail exponent."""
    losses = _neg_returns(close)
    def _hill_k10(x):
        x2 = x[~np.isnan(x)]
        if len(x2) < 12:
            return np.nan
        xs = np.sort(x2)[::-1]
        xk1 = xs[10]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:10] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    rh = losses.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_hill_k10, raw=True)
    return rh.expanding(min_periods=1).min()


def evt_085_tail_index_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Hill index(63d,k=10) within its 252-day history."""
    losses = _neg_returns(close)
    def _hill_k10(x):
        x2 = x[~np.isnan(x)]
        if len(x2) < 12:
            return np.nan
        xs = np.sort(x2)[::-1]
        xk1 = xs[10]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:10] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    rh = losses.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_hill_k10, raw=True)
    return rh.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group I (086-095): Conditional tail and extremal dependence ---

def evt_086_tail_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation lag-1 of tail-exceedance indicator (tail clustering) over 63 days."""
    losses = _neg_returns(close)
    thr = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.90)
    exceed = (losses > thr.shift(1)).astype(float)
    def _autocorr1(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        x_c = x - x.mean()
        denom = np.dot(x_c, x_c)
        if denom <= 0:
            return np.nan
        return np.dot(x_c[:-1], x_c[1:]) / denom
    return exceed.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_autocorr1, raw=True)


def evt_087_extreme_drawup_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of max single-day loss to max single-day gain over 63 days."""
    losses = _neg_returns(close)
    gains = _log_returns(close).clip(lower=0.0)
    max_loss = _rolling_max(losses, _TD_QTR)
    max_gain = _rolling_max(gains, _TD_QTR)
    return _safe_div(max_loss, max_gain.clip(lower=_EPS))


def evt_088_consecutive_loss_days_21d(close: pd.Series) -> pd.Series:
    """Consecutive days with negative log-return (running streak to current row)."""
    r = _log_returns(close)
    return _consec_streak(r < 0.0)


def evt_089_loss_run_length_mean_63d(close: pd.Series) -> pd.Series:
    """Mean run-length of consecutive losing days over 63-day window."""
    r = _log_returns(close)
    is_loss = (r < 0.0).astype(float)
    def _mean_run(x):
        x = x[~np.isnan(x)]
        if len(x) == 0:
            return np.nan
        runs = []
        run = 0
        for v in x:
            if v == 1.0:
                run += 1
            else:
                if run > 0:
                    runs.append(run)
                    run = 0
        if run > 0:
            runs.append(run)
        return float(np.mean(runs)) if runs else 0.0
    return is_loss.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_mean_run, raw=True)


def evt_090_loss_run_max_length_63d(close: pd.Series) -> pd.Series:
    """Maximum run-length of consecutive losing days over 63-day window."""
    r = _log_returns(close)
    is_loss = (r < 0.0).astype(float)
    def _max_run(x):
        x = x[~np.isnan(x)]
        max_r = 0
        run = 0
        for v in x:
            if v == 1.0:
                run += 1
                max_r = max(max_r, run)
            else:
                run = 0
        return float(max_r)
    return is_loss.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_max_run, raw=True)


def evt_091_extreme_loss_runs_63d(close: pd.Series) -> pd.Series:
    """Count of extreme loss runs (>=3 consecutive days) over 63-day window."""
    r = _log_returns(close)
    is_loss = (r < 0.0).astype(float)
    def _count_runs3(x):
        x = x[~np.isnan(x)]
        count = 0
        run = 0
        for v in x:
            if v == 1.0:
                run += 1
            else:
                if run >= 3:
                    count += 1
                run = 0
        if run >= 3:
            count += 1
        return float(count)
    return is_loss.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_count_runs3, raw=True)


def evt_092_tail_concentration_95_63d(close: pd.Series) -> pd.Series:
    """Fraction of total loss mass in top 5th percentile losses, over 63 days."""
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
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_tail_conc, raw=True)


def evt_093_tail_concentration_90_252d(close: pd.Series) -> pd.Series:
    """Fraction of total loss mass in top 10th percentile losses, over 252 days."""
    losses = _neg_returns(close)
    def _tail_conc90(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 5:
            return np.nan
        thr = np.quantile(x, 0.90)
        tail_sum = np.sum(x[x >= thr])
        total = np.sum(x)
        return float(tail_sum / (total + _EPS))
    return losses.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).apply(_tail_conc90, raw=True)


def evt_094_tail_mean_over_mean_loss_63d(close: pd.Series) -> pd.Series:
    """Ratio of top-10% loss mean to overall loss mean over 63 days."""
    losses = _neg_returns(close)
    def _ratio(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.90)
        tail = x[x >= thr]
        if len(tail) == 0:
            return np.nan
        return float(np.mean(tail) / (np.mean(x) + _EPS))
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_ratio, raw=True)


def evt_095_extreme_loss_entropy_63d(close: pd.Series) -> pd.Series:
    """Entropy of loss rank-distribution over 63 days (concentration = low entropy)."""
    losses = _neg_returns(close)
    def _entropy(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        x_sum = np.sum(x)
        if x_sum <= 0:
            return np.nan
        p = x / x_sum
        ent = -np.sum(p * np.log(p + _EPS))
        return float(ent)
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_entropy, raw=True)


# --- Group J (096-110): Multi-scale VaR and ES comparisons ---

def evt_096_var_ratio_21d_vs_63d_q95(close: pd.Series) -> pd.Series:
    """Ratio of VaR95(21d) to VaR95(63d): short vs medium tail risk."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    return _safe_div(v21, v63.clip(lower=_EPS))


def evt_097_var_ratio_63d_vs_252d_q95(close: pd.Series) -> pd.Series:
    """Ratio of VaR95(63d) to VaR95(252d): medium vs long tail risk."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    v252 = _rolling_var(close, _TD_YEAR, 0.95)
    return _safe_div(v63, v252.clip(lower=_EPS))


def evt_098_var_ratio_q99_vs_q95_63d(close: pd.Series) -> pd.Series:
    """Ratio of VaR99(63d) to VaR95(63d): tail shape above 95th."""
    v99 = _rolling_var(close, _TD_QTR, 0.99)
    v95 = _rolling_var(close, _TD_QTR, 0.95)
    return _safe_div(v99, v95.clip(lower=_EPS))


def evt_099_var_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of VaR95(63d) in its 252-day rolling distribution."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    m = _rolling_mean(v63, _TD_YEAR)
    s = _rolling_std(v63, _TD_YEAR)
    return _safe_div(v63 - m, s.clip(lower=_EPS))


def evt_100_var_pct_rank_252d_q95(close: pd.Series) -> pd.Series:
    """Percentile rank of VaR95(63d) in its trailing 252-day history."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    return v63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def evt_101_es_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of ES95(63d) in its 252-day rolling distribution."""
    r = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es63 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    m = _rolling_mean(es63, _TD_YEAR)
    s = _rolling_std(es63, _TD_YEAR)
    return _safe_div(es63 - m, s.clip(lower=_EPS))


def evt_102_es_minus_var_spread_95_63d(close: pd.Series) -> pd.Series:
    """ES95(63d) minus VaR95(63d): absolute tail premium beyond VaR."""
    r = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es63 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    return es63 - v63


def evt_103_var_expansion_rate_21d(close: pd.Series) -> pd.Series:
    """5-day change in VaR95(21d): rate of VaR expansion."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    return v21.diff(_TD_WEEK)


def evt_104_var_expansion_rate_63d(close: pd.Series) -> pd.Series:
    """21-day change in VaR95(63d): rate of medium-term VaR expansion."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    return v63.diff(_TD_MON)


def evt_105_es_expansion_rate_63d(close: pd.Series) -> pd.Series:
    """21-day change in ES95(63d): rate of CVaR expansion."""
    r = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es63 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    return es63.diff(_TD_MON)


# --- Group K (106-120): Normal-vs-actual tail divergence, sigma events ---

def evt_106_sigma3_event_count_63d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding 3 rolling-std events over 63-day window."""
    r = _log_returns(close)
    losses = _neg_returns(close)
    mu = _rolling_mean(r, _TD_QTR)
    sig = _rolling_std(r, _TD_QTR)
    threshold = mu.abs() + 3.0 * sig
    return _rolling_sum((losses > threshold).astype(float), _TD_QTR)


def evt_107_sigma4_event_count_252d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding 4 rolling-std events over 252-day window."""
    r = _log_returns(close)
    losses = _neg_returns(close)
    mu = _rolling_mean(r, _TD_YEAR)
    sig = _rolling_std(r, _TD_YEAR)
    threshold = mu.abs() + 4.0 * sig
    return _rolling_sum((losses > threshold).astype(float), _TD_YEAR)


def evt_108_sigma2_event_count_21d(close: pd.Series) -> pd.Series:
    """Count of daily losses exceeding 2 rolling-std events over 21-day window."""
    r = _log_returns(close)
    losses = _neg_returns(close)
    mu = _rolling_mean(r, _TD_MON)
    sig = _rolling_std(r, _TD_MON)
    threshold = mu.abs() + 2.0 * sig
    return _rolling_sum((losses > threshold).astype(float), _TD_MON)


def evt_109_actual_vs_normal_tail_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of actual 95th-loss percentile to Gaussian 95th-loss percentile over 63 days."""
    losses = _neg_returns(close)
    actual_q = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    mu = _rolling_mean(_log_returns(close), _TD_QTR)
    sig = _rolling_std(_log_returns(close), _TD_QTR)
    # Gaussian 95th percentile of losses: mu - 1.645*sig (negative, so loss = |mu| + 1.645*sig)
    normal_q = (1.645 * sig - mu).clip(lower=_EPS)
    return _safe_div(actual_q, normal_q)


def evt_110_gauss_shortfall_factor_99_63d(close: pd.Series) -> pd.Series:
    """Ratio of actual 99th-loss percentile to Gaussian 99th-loss percentile over 63 days."""
    losses = _neg_returns(close)
    actual_q = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.99)
    mu = _rolling_mean(_log_returns(close), _TD_QTR)
    sig = _rolling_std(_log_returns(close), _TD_QTR)
    normal_q = (2.326 * sig - mu).clip(lower=_EPS)
    return _safe_div(actual_q, normal_q)


def evt_111_loss_quantile_spacing_63d(close: pd.Series) -> pd.Series:
    """Spacing between 99th and 95th percentile losses over 63 days (tail shape)."""
    losses = _neg_returns(close)
    q99 = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.99)
    q95 = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    return (q99 - q95).clip(lower=0.0)


def evt_112_loss_quantile_spacing_252d(close: pd.Series) -> pd.Series:
    """Spacing between 99th and 95th percentile losses over 252 days."""
    losses = _neg_returns(close)
    q99 = losses.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.99)
    q95 = losses.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.95)
    return (q99 - q95).clip(lower=0.0)


def evt_113_loss_percentile_25_63d(close: pd.Series) -> pd.Series:
    """25th percentile of losses (left-quarter tail) over 63 days."""
    losses = _neg_returns(close)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.25)


def evt_114_loss_percentile_10_63d(close: pd.Series) -> pd.Series:
    """10th percentile of losses over 63 days (mild loss threshold)."""
    losses = _neg_returns(close)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.10)


def evt_115_loss_iqr_63d(close: pd.Series) -> pd.Series:
    """Interquartile range of losses over 63 days (central loss dispersion)."""
    losses = _neg_returns(close)
    q75 = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.75)
    q25 = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.25)
    return (q75 - q25).clip(lower=0.0)


# --- Group L (116-130): Drawdown-of-returns, compound loss sequences ---

def evt_116_cumret_min_21d(close: pd.Series) -> pd.Series:
    """Minimum cumulative log-return (trough of return path) over 21-day window."""
    r = _log_returns(close)
    def _cum_min(x):
        x = x[~np.isnan(x)]
        if len(x) == 0:
            return np.nan
        return float(np.min(np.cumsum(x)))
    return r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_cum_min, raw=True)


def evt_117_cumret_min_63d(close: pd.Series) -> pd.Series:
    """Minimum cumulative log-return over 63-day window."""
    r = _log_returns(close)
    def _cum_min(x):
        x = x[~np.isnan(x)]
        if len(x) == 0:
            return np.nan
        return float(np.min(np.cumsum(x)))
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_cum_min, raw=True)


def evt_118_drawdown_of_returns_max_63d(close: pd.Series) -> pd.Series:
    """Max drawdown of cumulative log-returns within 63-day window."""
    r = _log_returns(close)
    def _max_dd(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        cum = np.cumsum(x)
        peak = np.maximum.accumulate(cum)
        return float(np.min(cum - peak))
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_max_dd, raw=True)


def evt_119_drawdown_of_returns_max_21d(close: pd.Series) -> pd.Series:
    """Max drawdown of cumulative log-returns within 21-day window."""
    r = _log_returns(close)
    def _max_dd(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        cum = np.cumsum(x)
        peak = np.maximum.accumulate(cum)
        return float(np.min(cum - peak))
    return r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_max_dd, raw=True)


def evt_120_sum_neg_returns_21d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns (aggregate loss) over 21 days."""
    r = _log_returns(close)
    neg = r.where(r < 0.0, 0.0)
    return _rolling_sum(neg, _TD_MON)


def evt_121_sum_neg_returns_63d(close: pd.Series) -> pd.Series:
    """Sum of all negative log-returns over 63 days."""
    r = _log_returns(close)
    neg = r.where(r < 0.0, 0.0)
    return _rolling_sum(neg, _TD_QTR)


def evt_122_neg_return_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of negative-return days over 21-day window."""
    r = _log_returns(close)
    return _rolling_sum((r < 0.0).astype(float), _TD_MON) / _TD_MON


def evt_123_neg_return_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of negative-return days over 63-day window."""
    r = _log_returns(close)
    return _rolling_sum((r < 0.0).astype(float), _TD_QTR) / _TD_QTR


def evt_124_neg_return_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of negative-return days over 252-day window."""
    r = _log_returns(close)
    return _rolling_sum((r < 0.0).astype(float), _TD_YEAR) / _TD_YEAR


def evt_125_loss_gain_asymmetry_63d(close: pd.Series) -> pd.Series:
    """Mean loss divided by mean gain over 63 days (asymmetry ratio)."""
    r = _log_returns(close)
    mean_loss = r.where(r < 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean().abs()
    mean_gain = r.where(r > 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return _safe_div(mean_loss, mean_gain.clip(lower=_EPS))


# --- Group M (126-140): Volume-conditioned tail measures ---

def evt_126_large_loss_on_high_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with loss > 2% AND volume > median volume, trailing 21 days."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_MON)
    high_vol = volume > med_vol
    big_loss = losses > 0.02
    return _rolling_sum((high_vol & big_loss).astype(float), _TD_MON)


def evt_127_large_loss_on_high_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with loss > 2% AND volume > median volume, trailing 63 days."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    high_vol = volume > med_vol
    big_loss = losses > 0.02
    return _rolling_sum((high_vol & big_loss).astype(float), _TD_QTR)


def evt_128_vol_weighted_loss_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of daily losses over 21 days."""
    losses = _neg_returns(close)
    vol_loss = losses * volume
    sum_vol_loss = _rolling_sum(vol_loss, _TD_MON)
    sum_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(sum_vol_loss, sum_vol.clip(lower=_EPS))


def evt_129_vol_weighted_loss_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of daily losses over 63 days."""
    losses = _neg_returns(close)
    vol_loss = losses * volume
    sum_vol_loss = _rolling_sum(vol_loss, _TD_QTR)
    sum_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(sum_vol_loss, sum_vol.clip(lower=_EPS))


def evt_130_vol_spike_on_loss_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean ratio of volume to 21d median volume on days with losses > 1% (panic signal)."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, med_vol.clip(lower=_EPS))
    is_loss_day = (losses > 0.01).astype(float)
    vol_ratio_on_loss = vol_ratio * is_loss_day
    count_loss = _rolling_sum(is_loss_day, _TD_MON)
    sum_vol_ratio = _rolling_sum(vol_ratio_on_loss, _TD_MON)
    return _safe_div(sum_vol_ratio, count_loss.clip(lower=_EPS))


def evt_131_var_95_high_volume_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """95th-percentile loss restricted to days with above-median volume, 63-day window."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    high_vol_loss = losses.where(volume > med_vol, np.nan)
    return high_vol_loss.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_132_extreme_down_vol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with loss > 3% AND volume > 1.5x median, trailing 63 days."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    return _rolling_sum(
        ((losses > 0.03) & (volume > 1.5 * med_vol)).astype(float), _TD_QTR
    )


def evt_133_loss_on_volume_shrink_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean loss on days when volume is below its 21d median (dryup loss days)."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_MON)
    low_vol_loss = losses.where(volume < med_vol, np.nan)
    return low_vol_loss.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).mean()


def evt_134_vol_weighted_var95_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted VaR95 over 63 days — loss at 95th percentile of vol-weighted losses."""
    losses = _neg_returns(close)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    scaled_losses = losses * vol_norm
    return scaled_losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_135_high_vol_extreme_loss_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of extreme losses (top-5%) that occur on high-volume days, 63-day window."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    def _frac(arr):
        arr = arr[~np.isnan(arr)]
        if len(arr) < 3:
            return np.nan
        return arr[-1]
    # Build combined series: for each row, fraction of top-5% losses on high-vol days
    def _frac_apply(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        # x here is just losses; need vol, not easily done in apply
        return np.nan
    # Use aligned approach
    high_vol = (volume > med_vol).astype(float)
    thr = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    extreme = (losses > thr.shift(1)).astype(float)
    extreme_high_vol = (extreme * high_vol)
    return _safe_div(
        _rolling_sum(extreme_high_vol, _TD_QTR),
        _rolling_sum(extreme, _TD_QTR).clip(lower=_EPS)
    )


# --- Group N (136-150): Downside risk composites and normalized measures ---

def evt_136_sortino_ratio_21d(close: pd.Series) -> pd.Series:
    """Sortino ratio over 21 days (mean return / downside deviation), annualized."""
    r = _log_returns(close)
    mean_ret = _rolling_mean(r, _TD_MON) * _TD_YEAR
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).mean() * _TD_YEAR)
    return _safe_div(mean_ret, semi_std.clip(lower=_EPS))


def evt_137_sortino_ratio_63d(close: pd.Series) -> pd.Series:
    """Sortino ratio over 63 days, annualized."""
    r = _log_returns(close)
    mean_ret = _rolling_mean(r, _TD_QTR) * _TD_YEAR
    sq = (r.where(r < 0.0, 0.0)) ** 2
    semi_std = np.sqrt(sq.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean() * _TD_YEAR)
    return _safe_div(mean_ret, semi_std.clip(lower=_EPS))


def evt_138_upside_capture_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of mean positive return to mean negative return (abs) over 63 days."""
    r = _log_returns(close)
    up = r.where(r > 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    dn = r.where(r < 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean().abs()
    return _safe_div(up, dn.clip(lower=_EPS))


def evt_139_calmar_proxy_63d(close: pd.Series) -> pd.Series:
    """Calmar-proxy: annualized return over max single-day loss, 63-day window."""
    r = _log_returns(close)
    ann_ret = _rolling_mean(r, _TD_QTR) * _TD_YEAR
    max_loss = _rolling_max(_neg_returns(close), _TD_QTR)
    return _safe_div(ann_ret, max_loss.clip(lower=_EPS))


def evt_140_omega_ratio_63d(close: pd.Series) -> pd.Series:
    """Omega ratio over 63 days: sum of gains / sum of losses (abs)."""
    r = _log_returns(close)
    gains_sum = r.where(r > 0.0, 0.0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    loss_sum = r.where(r < 0.0, 0.0).abs().rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    return _safe_div(gains_sum, loss_sum.clip(lower=_EPS))


def evt_141_upside_downside_std_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of upside std to downside std of returns over 63 days."""
    r = _log_returns(close)
    up_std = r.where(r > 0.0, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    dn_std = r.where(r < 0.0, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    return _safe_div(up_std, dn_std.clip(lower=_EPS))


def evt_142_negative_semi_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Kurtosis of the negative-only returns (lower partial distribution) over 63 days."""
    r = _log_returns(close)
    neg_r = r.where(r < 0.0, np.nan)
    return neg_r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def evt_143_loss_accel_21d(close: pd.Series) -> pd.Series:
    """Mean first-difference of losses over 21 days (acceleration of losses)."""
    losses = _neg_returns(close)
    dloss = losses.diff(1)
    return _rolling_mean(dloss, _TD_MON)


def evt_144_loss_accel_63d(close: pd.Series) -> pd.Series:
    """Mean first-difference of losses over 63 days (medium-term loss acceleration)."""
    losses = _neg_returns(close)
    dloss = losses.diff(1)
    return _rolling_mean(dloss, _TD_QTR)


def evt_145_tail_persistence_index_63d(close: pd.Series) -> pd.Series:
    """Hurst-proxy of tail indicator: ratio of range to std of exceedance indicator over 63d."""
    losses = _neg_returns(close)
    thr = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.90)
    exceed = (losses > thr.shift(1)).astype(float)
    cum = exceed.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).sum()
    rng = _rolling_max(cum, _TD_QTR) - _rolling_min(cum, _TD_QTR)
    std = _rolling_std(exceed, _TD_QTR)
    return _safe_div(rng, std.clip(lower=_EPS))


def evt_146_var95_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of VaR95(21d) within its 252-day history."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    return v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def evt_147_max_loss_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of max 5-day loss to max 63-day loss (recent spike indicator)."""
    losses = _neg_returns(close)
    m5 = _rolling_max(losses, _TD_WEEK)
    m63 = _rolling_max(losses, _TD_QTR)
    return _safe_div(m5, m63.clip(lower=_EPS))


def evt_148_es99_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of ES99(63d) — how extreme is current ES historically."""
    r = _neg_returns(close)
    def _es99(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.99)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es63 = r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es99, raw=True)
    return es63.expanding(min_periods=1).rank(pct=True)


def evt_149_tail_risk_composite_score(close: pd.Series) -> pd.Series:
    """Composite tail-risk score: z-score sum of VaR95(63d), ES95(63d), max_loss(63d)."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    losses = _neg_returns(close)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es63 = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    ml63 = _rolling_max(losses, _TD_QTR)

    def _zscore(s):
        m = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd.clip(lower=_EPS))

    return _zscore(v63) + _zscore(es63) + _zscore(ml63)


def evt_150_downside_beta_proxy_63d(close: pd.Series) -> pd.Series:
    """Proxy for downside beta: std of negative returns / std of all returns over 63 days."""
    r = _log_returns(close)
    dn_std = r.where(r < 0.0, np.nan).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    all_std = _rolling_std(r, _TD_QTR)
    return _safe_div(dn_std, all_std.clip(lower=_EPS))


# ── Registry ──────────────────────────────────────────────────────────────────

TAIL_RISK_EVT_REGISTRY_076_150 = {
    "evt_076_pickands_63d_k5": {"inputs": ["close"], "func": evt_076_pickands_63d_k5},
    "evt_077_pickands_126d_k8": {"inputs": ["close"], "func": evt_077_pickands_126d_k8},
    "evt_078_pickands_252d_k10": {"inputs": ["close"], "func": evt_078_pickands_252d_k10},
    "evt_079_moment_ratio_63d_k10": {"inputs": ["close"], "func": evt_079_moment_ratio_63d_k10},
    "evt_080_moment_ratio_126d_k15": {"inputs": ["close"], "func": evt_080_moment_ratio_126d_k15},
    "evt_081_moment_ratio_252d_k20": {"inputs": ["close"], "func": evt_081_moment_ratio_252d_k20},
    "evt_082_pickands_vs_hill_ratio_63d": {"inputs": ["close"], "func": evt_082_pickands_vs_hill_ratio_63d},
    "evt_083_tail_index_ewm_span63": {"inputs": ["close"], "func": evt_083_tail_index_ewm_span63},
    "evt_084_tail_index_expanding_min": {"inputs": ["close"], "func": evt_084_tail_index_expanding_min},
    "evt_085_tail_index_pct_rank_252d": {"inputs": ["close"], "func": evt_085_tail_index_pct_rank_252d},
    "evt_086_tail_autocorr_lag1_63d": {"inputs": ["close"], "func": evt_086_tail_autocorr_lag1_63d},
    "evt_087_extreme_drawup_ratio_63d": {"inputs": ["close"], "func": evt_087_extreme_drawup_ratio_63d},
    "evt_088_consecutive_loss_days_21d": {"inputs": ["close"], "func": evt_088_consecutive_loss_days_21d},
    "evt_089_loss_run_length_mean_63d": {"inputs": ["close"], "func": evt_089_loss_run_length_mean_63d},
    "evt_090_loss_run_max_length_63d": {"inputs": ["close"], "func": evt_090_loss_run_max_length_63d},
    "evt_091_extreme_loss_runs_63d": {"inputs": ["close"], "func": evt_091_extreme_loss_runs_63d},
    "evt_092_tail_concentration_95_63d": {"inputs": ["close"], "func": evt_092_tail_concentration_95_63d},
    "evt_093_tail_concentration_90_252d": {"inputs": ["close"], "func": evt_093_tail_concentration_90_252d},
    "evt_094_tail_mean_over_mean_loss_63d": {"inputs": ["close"], "func": evt_094_tail_mean_over_mean_loss_63d},
    "evt_095_extreme_loss_entropy_63d": {"inputs": ["close"], "func": evt_095_extreme_loss_entropy_63d},
    "evt_096_var_ratio_21d_vs_63d_q95": {"inputs": ["close"], "func": evt_096_var_ratio_21d_vs_63d_q95},
    "evt_097_var_ratio_63d_vs_252d_q95": {"inputs": ["close"], "func": evt_097_var_ratio_63d_vs_252d_q95},
    "evt_098_var_ratio_q99_vs_q95_63d": {"inputs": ["close"], "func": evt_098_var_ratio_q99_vs_q95_63d},
    "evt_099_var_zscore_63d_in_252d": {"inputs": ["close"], "func": evt_099_var_zscore_63d_in_252d},
    "evt_100_var_pct_rank_252d_q95": {"inputs": ["close"], "func": evt_100_var_pct_rank_252d_q95},
    "evt_101_es_zscore_63d_in_252d": {"inputs": ["close"], "func": evt_101_es_zscore_63d_in_252d},
    "evt_102_es_minus_var_spread_95_63d": {"inputs": ["close"], "func": evt_102_es_minus_var_spread_95_63d},
    "evt_103_var_expansion_rate_21d": {"inputs": ["close"], "func": evt_103_var_expansion_rate_21d},
    "evt_104_var_expansion_rate_63d": {"inputs": ["close"], "func": evt_104_var_expansion_rate_63d},
    "evt_105_es_expansion_rate_63d": {"inputs": ["close"], "func": evt_105_es_expansion_rate_63d},
    "evt_106_sigma3_event_count_63d": {"inputs": ["close"], "func": evt_106_sigma3_event_count_63d},
    "evt_107_sigma4_event_count_252d": {"inputs": ["close"], "func": evt_107_sigma4_event_count_252d},
    "evt_108_sigma2_event_count_21d": {"inputs": ["close"], "func": evt_108_sigma2_event_count_21d},
    "evt_109_actual_vs_normal_tail_ratio_63d": {"inputs": ["close"], "func": evt_109_actual_vs_normal_tail_ratio_63d},
    "evt_110_gauss_shortfall_factor_99_63d": {"inputs": ["close"], "func": evt_110_gauss_shortfall_factor_99_63d},
    "evt_111_loss_quantile_spacing_63d": {"inputs": ["close"], "func": evt_111_loss_quantile_spacing_63d},
    "evt_112_loss_quantile_spacing_252d": {"inputs": ["close"], "func": evt_112_loss_quantile_spacing_252d},
    "evt_113_loss_percentile_25_63d": {"inputs": ["close"], "func": evt_113_loss_percentile_25_63d},
    "evt_114_loss_percentile_10_63d": {"inputs": ["close"], "func": evt_114_loss_percentile_10_63d},
    "evt_115_loss_iqr_63d": {"inputs": ["close"], "func": evt_115_loss_iqr_63d},
    "evt_116_cumret_min_21d": {"inputs": ["close"], "func": evt_116_cumret_min_21d},
    "evt_117_cumret_min_63d": {"inputs": ["close"], "func": evt_117_cumret_min_63d},
    "evt_118_drawdown_of_returns_max_63d": {"inputs": ["close"], "func": evt_118_drawdown_of_returns_max_63d},
    "evt_119_drawdown_of_returns_max_21d": {"inputs": ["close"], "func": evt_119_drawdown_of_returns_max_21d},
    "evt_120_sum_neg_returns_21d": {"inputs": ["close"], "func": evt_120_sum_neg_returns_21d},
    "evt_121_sum_neg_returns_63d": {"inputs": ["close"], "func": evt_121_sum_neg_returns_63d},
    "evt_122_neg_return_fraction_21d": {"inputs": ["close"], "func": evt_122_neg_return_fraction_21d},
    "evt_123_neg_return_fraction_63d": {"inputs": ["close"], "func": evt_123_neg_return_fraction_63d},
    "evt_124_neg_return_fraction_252d": {"inputs": ["close"], "func": evt_124_neg_return_fraction_252d},
    "evt_125_loss_gain_asymmetry_63d": {"inputs": ["close"], "func": evt_125_loss_gain_asymmetry_63d},
    "evt_126_large_loss_on_high_vol_21d": {"inputs": ["close", "volume"], "func": evt_126_large_loss_on_high_vol_21d},
    "evt_127_large_loss_on_high_vol_63d": {"inputs": ["close", "volume"], "func": evt_127_large_loss_on_high_vol_63d},
    "evt_128_vol_weighted_loss_mean_21d": {"inputs": ["close", "volume"], "func": evt_128_vol_weighted_loss_mean_21d},
    "evt_129_vol_weighted_loss_mean_63d": {"inputs": ["close", "volume"], "func": evt_129_vol_weighted_loss_mean_63d},
    "evt_130_vol_spike_on_loss_day_21d": {"inputs": ["close", "volume"], "func": evt_130_vol_spike_on_loss_day_21d},
    "evt_131_var_95_high_volume_days_63d": {"inputs": ["close", "volume"], "func": evt_131_var_95_high_volume_days_63d},
    "evt_132_extreme_down_vol_days_63d": {"inputs": ["close", "volume"], "func": evt_132_extreme_down_vol_days_63d},
    "evt_133_loss_on_volume_shrink_21d": {"inputs": ["close", "volume"], "func": evt_133_loss_on_volume_shrink_21d},
    "evt_134_vol_weighted_var95_63d": {"inputs": ["close", "volume"], "func": evt_134_vol_weighted_var95_63d},
    "evt_135_high_vol_extreme_loss_fraction_63d": {"inputs": ["close", "volume"], "func": evt_135_high_vol_extreme_loss_fraction_63d},
    "evt_136_sortino_ratio_21d": {"inputs": ["close"], "func": evt_136_sortino_ratio_21d},
    "evt_137_sortino_ratio_63d": {"inputs": ["close"], "func": evt_137_sortino_ratio_63d},
    "evt_138_upside_capture_ratio_63d": {"inputs": ["close"], "func": evt_138_upside_capture_ratio_63d},
    "evt_139_calmar_proxy_63d": {"inputs": ["close"], "func": evt_139_calmar_proxy_63d},
    "evt_140_omega_ratio_63d": {"inputs": ["close"], "func": evt_140_omega_ratio_63d},
    "evt_141_upside_downside_std_ratio_63d": {"inputs": ["close"], "func": evt_141_upside_downside_std_ratio_63d},
    "evt_142_negative_semi_kurtosis_63d": {"inputs": ["close"], "func": evt_142_negative_semi_kurtosis_63d},
    "evt_143_loss_accel_21d": {"inputs": ["close"], "func": evt_143_loss_accel_21d},
    "evt_144_loss_accel_63d": {"inputs": ["close"], "func": evt_144_loss_accel_63d},
    "evt_145_tail_persistence_index_63d": {"inputs": ["close"], "func": evt_145_tail_persistence_index_63d},
    "evt_146_var95_21d_pct_rank_252d": {"inputs": ["close"], "func": evt_146_var95_21d_pct_rank_252d},
    "evt_147_max_loss_ratio_5d_vs_63d": {"inputs": ["close"], "func": evt_147_max_loss_ratio_5d_vs_63d},
    "evt_148_es99_expanding_pct_rank": {"inputs": ["close"], "func": evt_148_es99_expanding_pct_rank},
    "evt_149_tail_risk_composite_score": {"inputs": ["close"], "func": evt_149_tail_risk_composite_score},
    "evt_150_downside_beta_proxy_63d": {"inputs": ["close"], "func": evt_150_downside_beta_proxy_63d},
}
