"""
110_tail_risk_evt — Extended Features 001-075
Domain: extreme-value / tail-risk — deeper variants: multi-block extremes,
        GEV/block-maxima style measures, spectral risk measures, higher-order
        tail moments, cross-period extreme event co-occurrence, conditional
        VaR/ES under high-volume regimes, tail decay rate proxies, and
        extreme coherence across OHLC price series.
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
        thr = np.quantile(x, q)
        tail = x[x >= thr]
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-015): Block-maxima / GEV-style measures ---

def evt_ext_001_block_max_loss_5d_mean_63d(close: pd.Series) -> pd.Series:
    """Mean of 5-day block-maxima of losses over 63-day window (GEV-style aggregation)."""
    losses = _neg_returns(close)
    block_max = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    return _rolling_mean(block_max, _TD_QTR)


def evt_ext_002_block_max_loss_5d_std_63d(close: pd.Series) -> pd.Series:
    """Std of 5-day block-maxima of losses over 63-day window."""
    losses = _neg_returns(close)
    block_max = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    return _rolling_std(block_max, _TD_QTR)


def evt_ext_003_block_max_loss_21d_mean_252d(close: pd.Series) -> pd.Series:
    """Mean of 21-day block-maxima of losses over 252-day window."""
    losses = _neg_returns(close)
    block_max = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).max()
    return _rolling_mean(block_max, _TD_YEAR)


def evt_ext_004_block_max_loss_21d_max_252d(close: pd.Series) -> pd.Series:
    """Maximum of 21-day block-maxima of losses over 252-day window."""
    losses = _neg_returns(close)
    block_max = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).max()
    return _rolling_max(block_max, _TD_YEAR)


def evt_ext_005_block_max_loss_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day max loss within 252-day history."""
    losses = _neg_returns(close)
    block_max = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    return block_max.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def evt_ext_006_block_mean_loss_5d_63d(close: pd.Series) -> pd.Series:
    """Mean of 5-day average losses over 63-day window (block-mean aggregation)."""
    losses = _neg_returns(close)
    block_mean = _rolling_mean(losses, _TD_WEEK)
    return _rolling_mean(block_mean, _TD_QTR)


def evt_ext_007_block_sum_loss_5d_max_63d(close: pd.Series) -> pd.Series:
    """Maximum 5-day cumulative loss over trailing 63-day window."""
    losses = _neg_returns(close)
    block_sum = _rolling_sum(losses, _TD_WEEK)
    return _rolling_max(block_sum, _TD_QTR)


def evt_ext_008_block_max_loss_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day max loss vs its 252-day distribution."""
    losses = _neg_returns(close)
    bmax = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    m = _rolling_mean(bmax, _TD_YEAR)
    s = _rolling_std(bmax, _TD_YEAR)
    return _safe_div(bmax - m, s.clip(lower=_EPS))


def evt_ext_009_block_max_consecutive_new_high_63d(close: pd.Series) -> pd.Series:
    """Count of 5-day blocks where max loss exceeds prior block max (escalating losses), 63d."""
    losses = _neg_returns(close)
    bmax = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    new_high = (bmax > bmax.shift(_TD_WEEK)).astype(float)
    return _rolling_sum(new_high, _TD_QTR)


def evt_ext_010_range_of_block_maxima_21d_252d(close: pd.Series) -> pd.Series:
    """Range (max - min) of 21-day block maxima over 252-day window."""
    losses = _neg_returns(close)
    bmax = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).max()
    return _rolling_max(bmax, _TD_YEAR) - _rolling_min(bmax, _TD_YEAR)


def evt_ext_011_block_var95_5d_63d(close: pd.Series) -> pd.Series:
    """95th percentile of 5-day block-sum losses over 63-day window."""
    losses = _neg_returns(close)
    block_sum = _rolling_sum(losses, _TD_WEEK)
    return block_sum.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_ext_012_block_var99_5d_252d(close: pd.Series) -> pd.Series:
    """99th percentile of 5-day block-sum losses over 252-day window."""
    losses = _neg_returns(close)
    block_sum = _rolling_sum(losses, _TD_WEEK)
    return block_sum.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.99)


def evt_ext_013_block_es95_5d_63d(close: pd.Series) -> pd.Series:
    """Expected shortfall at 95% of 5-day block-sum losses over 63-day window."""
    losses = _neg_returns(close)
    block_sum = _rolling_sum(losses, _TD_WEEK)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return block_sum.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)


def evt_ext_014_block_hill_5d_63d(close: pd.Series) -> pd.Series:
    """Hill tail index of 5-day block-maxima distribution over 63-day window (k=5)."""
    losses = _neg_returns(close)
    bmax = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    def _hill5(x):
        x = x[~np.isnan(x)]
        if len(x) < 7 or 5 < 1:
            return np.nan
        xs = np.sort(x)[::-1]
        xk1 = xs[5]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:5] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    return bmax.rolling(_TD_QTR, min_periods=max(7, _TD_QTR // 2)).apply(_hill5, raw=True)


def evt_ext_015_block_max_loss_5d_ema63(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) 5-day block-max loss — trend in short-horizon tail risk."""
    losses = _neg_returns(close)
    bmax = losses.rolling(_TD_WEEK, min_periods=max(2, _TD_WEEK // 2)).max()
    return bmax.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


# --- Group B (016-030): High-order tail moments and spectral risk ---

def evt_ext_016_tail_third_moment_63d(close: pd.Series) -> pd.Series:
    """Third central moment of losses in top-10% tail over 63-day window."""
    losses = _neg_returns(close)
    def _third_mom(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.90)
        tail = x[x >= thr]
        if len(tail) < 2:
            return np.nan
        mu = np.mean(tail)
        return float(np.mean((tail - mu) ** 3))
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_third_mom, raw=True)


def evt_ext_017_tail_fourth_moment_63d(close: pd.Series) -> pd.Series:
    """Fourth central moment of losses in top-10% tail over 63-day window."""
    losses = _neg_returns(close)
    def _fourth_mom(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.90)
        tail = x[x >= thr]
        if len(tail) < 2:
            return np.nan
        mu = np.mean(tail)
        return float(np.mean((tail - mu) ** 4))
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_fourth_mom, raw=True)


def evt_ext_018_spectral_risk_measure_lambda05_63d(close: pd.Series) -> pd.Series:
    """Spectral risk measure with exponential weighting (lambda=0.5) over 63 days.
    Weights tail losses exponentially; approximates a risk-averse ES."""
    losses = _neg_returns(close)
    def _spectral(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        n = len(x)
        x_sorted = np.sort(x)  # ascending
        # weight function: phi(p) ~ exp(0.5*(p - 1)) for p in (0,1)
        # approximate via order statistics
        p = (np.arange(1, n + 1) - 0.5) / n
        phi = np.exp(0.5 * (p - 1.0))
        phi = phi / phi.sum()
        return float(np.dot(phi, x_sorted))
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_spectral, raw=True)


def evt_ext_019_spectral_risk_measure_lambda2_63d(close: pd.Series) -> pd.Series:
    """Spectral risk measure with strong exponential weighting (lambda=2.0) over 63 days."""
    losses = _neg_returns(close)
    def _spectral_l2(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        n = len(x)
        x_sorted = np.sort(x)
        p = (np.arange(1, n + 1) - 0.5) / n
        phi = np.exp(2.0 * (p - 1.0))
        phi = phi / phi.sum()
        return float(np.dot(phi, x_sorted))
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_spectral_l2, raw=True)


def evt_ext_020_loss_cvar_spread_63d_126d(close: pd.Series) -> pd.Series:
    """Spread: ES95(63d) - ES95(126d) — recent vs medium-term CVaR divergence."""
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    es126 = _rolling_es(close, _TD_HALF, 0.95)
    return es63 - es126


def evt_ext_021_tail_l_moment_ratio_63d(close: pd.Series) -> pd.Series:
    """L-moment ratio (tau3 = L-skewness) of losses over 63-day window."""
    losses = _neg_returns(close)
    def _l_skew(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 4:
            return np.nan
        xs = np.sort(x)
        n = len(xs)
        l1 = np.mean(xs)
        c2 = np.array([1 if i > j else 0 for i in range(n) for j in range(n)]).reshape(n, n)
        # simplified: use pwm approach
        b0 = np.mean(xs)
        b1 = np.mean(xs * np.arange(n) / max(n - 1, 1))
        b2 = np.mean(xs * np.arange(n) * (np.arange(n) - 1) / max((n - 1) * (n - 2), 1))
        l2 = 2 * b1 - b0
        l3 = 6 * b2 - 6 * b1 + b0
        if abs(l2) < _EPS:
            return np.nan
        return float(l3 / l2)
    return losses.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(_l_skew, raw=True)


def evt_ext_022_loss_gini_coefficient_63d(close: pd.Series) -> pd.Series:
    """Gini coefficient of positive losses over 63 days (inequality of loss distribution)."""
    losses = _neg_returns(close)
    def _gini(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 2:
            return np.nan
        xs = np.sort(x)
        n = len(xs)
        cum = np.cumsum(xs)
        total = cum[-1]
        if total <= 0:
            return np.nan
        idx = np.arange(1, n + 1)
        return float((2 * np.sum(idx * xs) / (n * total)) - (n + 1) / n)
    return losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_gini, raw=True)


def evt_ext_023_tail_pareto_scale_63d(close: pd.Series) -> pd.Series:
    """Pareto-distribution scale parameter proxy: mean of top-20% losses over 63 days."""
    losses = _neg_returns(close)
    def _pareto_scale(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 3:
            return np.nan
        thr = np.quantile(x, 0.80)
        tail = x[x >= thr]
        if len(tail) < 2:
            return np.nan
        return float(np.mean(tail) - thr)
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_pareto_scale, raw=True)


def evt_ext_024_tail_pareto_scale_252d(close: pd.Series) -> pd.Series:
    """Pareto-distribution scale parameter proxy over 252 days."""
    losses = _neg_returns(close)
    def _pareto_scale(x):
        x = x[~np.isnan(x)]
        x = x[x > 0]
        if len(x) < 5:
            return np.nan
        thr = np.quantile(x, 0.80)
        tail = x[x >= thr]
        if len(tail) < 2:
            return np.nan
        return float(np.mean(tail) - thr)
    return losses.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).apply(_pareto_scale, raw=True)


def evt_ext_025_loss_cv_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of positive losses over 63 days (dispersion relative to mean)."""
    losses = _neg_returns(close)
    pos = losses.where(losses > 0, np.nan)
    mean_l = pos.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    std_l = pos.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()
    return _safe_div(std_l, mean_l.clip(lower=_EPS))


# --- Group C (026-040): OHLC-derived tail measures ---

def evt_ext_026_high_low_range_pct_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum daily high-low range as pct of close over 63 days (intraday tail risk)."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_max(hl_range, _TD_QTR)


def evt_ext_027_high_low_range_pct_q95_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """95th percentile of daily high-low range pct over 63 days."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return hl_range.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_ext_028_close_to_low_tail_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """95th percentile of close-to-low distance pct over 63 days (intraday downside tail)."""
    c2l = _safe_div(close - low, close.clip(lower=_EPS))
    return c2l.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_ext_029_open_gap_down_tail_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """95th percentile of downward open gaps (open below prior close) over 63 days."""
    gap_down = (close.shift(1) - open_).clip(lower=0.0)
    gap_pct = _safe_div(gap_down, close.shift(1).clip(lower=_EPS))
    return gap_pct.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


def evt_ext_030_open_gap_down_sum_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Sum of downward open gaps over 63 days (cumulative overnight downside)."""
    gap_down = (close.shift(1) - open_).clip(lower=0.0)
    gap_pct = _safe_div(gap_down, close.shift(1).clip(lower=_EPS))
    return _rolling_sum(gap_pct, _TD_QTR)


def evt_ext_031_high_low_range_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Kurtosis of high-low range pct over 63 days (fat-tail of intraday volatility)."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    return hl_range.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def evt_ext_032_close_vs_low_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's close-to-low distance within 252-day history."""
    c2l = _safe_div(close - low, close.clip(lower=_EPS))
    return c2l.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def evt_ext_033_hl_range_vs_median_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of current high-low range pct to its 63-day median."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    med = hl_range.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).median()
    return _safe_div(hl_range, med.clip(lower=_EPS))


def evt_ext_034_hl_extreme_range_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where high-low range pct exceeds 2x its 63-day median, trailing 63 days."""
    hl_range = _safe_div(high - low, close.clip(lower=_EPS))
    med = hl_range.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).median()
    threshold = 2.0 * med.clip(lower=_EPS)
    return _rolling_sum((hl_range > threshold).astype(float), _TD_QTR)


def evt_ext_035_open_close_loss_q95_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """95th percentile of open-to-close loss (open > close) pct over 63 days."""
    oc_loss = (open_ - close).clip(lower=0.0)
    oc_pct = _safe_div(oc_loss, open_.clip(lower=_EPS))
    return oc_pct.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)


# --- Group D (036-050): Conditional VaR/ES under volume regime ---

def evt_ext_036_es95_high_vol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ES95 of losses restricted to high-volume days over 63-day window."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    masked = losses.where(volume > med_vol, np.nan)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return masked.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)


def evt_ext_037_var99_high_vol_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VaR99 of losses on high-volume days over 63-day window."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    masked = losses.where(volume > med_vol, np.nan)
    return masked.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.99)


def evt_ext_038_es_high_vs_low_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of ES95 on high-vol days to ES95 on low-vol days over 63 days."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    high = losses.where(volume > med_vol, np.nan)
    low = losses.where(volume <= med_vol, np.nan)
    def _es(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.95)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    es_h = high.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    es_l = low.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es, raw=True)
    return _safe_div(es_h, es_l.clip(lower=_EPS))


def evt_ext_039_vol_weighted_es99_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted ES99 over 63 days — volume-scaled extreme CVaR."""
    losses = _neg_returns(close)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    scaled = losses * vol_norm
    def _es99(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        thr = np.quantile(x, 0.99)
        tail = x[x >= thr]
        return float(np.mean(tail)) if len(tail) > 0 else np.nan
    return scaled.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_es99, raw=True)


def evt_ext_040_max_loss_on_high_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum loss on high-volume days over 63-day window."""
    losses = _neg_returns(close)
    med_vol = _rolling_mean(volume, _TD_QTR)
    masked = losses.where(volume > med_vol, np.nan)
    return _rolling_max(masked, _TD_QTR)


def evt_ext_041_tail_vol_correlation_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day Pearson correlation between daily loss and log-volume (tail-vol link)."""
    losses = _neg_returns(close)
    log_vol = np.log(volume.clip(lower=_EPS))
    losses.name = 'loss'
    log_vol.name = 'lvol'
    return losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).corr(log_vol)


def evt_ext_042_loss_vol_correlation_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between daily loss magnitude and volume."""
    losses = _neg_returns(close)
    losses.name = 'loss'
    vol_s = volume.copy()
    vol_s.name = 'vol'
    return losses.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).corr(vol_s)


def evt_ext_043_extreme_loss_vol_amplification_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume ratio on days where loss > VaR95(63d), trailing 63 days."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_QTR, 0.95)
    med_vol = _rolling_mean(volume, _TD_QTR)
    vol_ratio = _safe_div(volume, med_vol.clip(lower=_EPS))
    on_extreme = vol_ratio.where(losses > var95.shift(1), np.nan)
    return _rolling_mean(on_extreme, _TD_QTR)


# --- Group E (044-060): Tail decay and persistence measures ---

def evt_ext_044_tail_decay_rate_63d(close: pd.Series) -> pd.Series:
    """Rate of loss tail decay: diff of Hill(63d,k=10) vs Hill(63d,k=5)."""
    losses = _neg_returns(close)
    def _hill_k(x, k):
        x = x[~np.isnan(x)]
        if len(x) < k + 2:
            return np.nan
        xs = np.sort(x)[::-1]
        xk1 = xs[k]
        if xk1 <= 0:
            return np.nan
        lr = np.log(xs[:k] / (xk1 + _EPS))
        ml = np.mean(lr)
        return 1.0 / ml if ml > 0 else np.nan
    h10 = losses.rolling(_TD_QTR, min_periods=max(13, _TD_QTR // 2)).apply(lambda x: _hill_k(x, 10), raw=True)
    h5 = losses.rolling(_TD_QTR, min_periods=max(8, _TD_QTR // 2)).apply(lambda x: _hill_k(x, 5), raw=True)
    return h10 - h5


def evt_ext_045_var95_autocorr_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation lag-1 of VaR95(21d) series over 252-day window (VaR clustering)."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    def _ac1(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        xc = x - x.mean()
        d = np.dot(xc, xc)
        if d <= 0:
            return np.nan
        return float(np.dot(xc[:-1], xc[1:]) / d)
    return v21.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).apply(_ac1, raw=True)


def evt_ext_046_es99_autocorr_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation lag-1 of ES99(63d) series over 252-day window."""
    es99 = _rolling_es(close, _TD_QTR, 0.99)
    def _ac1(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        xc = x - x.mean()
        d = np.dot(xc, xc)
        if d <= 0:
            return np.nan
        return float(np.dot(xc[:-1], xc[1:]) / d)
    return es99.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).apply(_ac1, raw=True)


def evt_ext_047_var_hurst_proxy_252d(close: pd.Series) -> pd.Series:
    """RS-statistic proxy for VaR95(21d) — Hurst-like tail persistence over 252 days."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    def _rs(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        xc = x - x.mean()
        cum = np.cumsum(xc)
        R = np.max(cum) - np.min(cum)
        S = np.std(x, ddof=1)
        if S <= 0:
            return np.nan
        return float(R / S)
    return v21.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).apply(_rs, raw=True)


def evt_ext_048_loss_extremogram_lag5_63d(close: pd.Series) -> pd.Series:
    """Extremogram at lag 5: P(loss(t)>q95 | loss(t-5)>q95) over 63-day window."""
    losses = _neg_returns(close)
    thr = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    exceed = (losses > thr.shift(1)).astype(float)
    lag5_exceed = exceed.shift(_TD_WEEK)
    joint = (exceed * lag5_exceed)
    return _safe_div(
        _rolling_sum(joint, _TD_QTR),
        _rolling_sum(lag5_exceed, _TD_QTR).clip(lower=_EPS)
    )


def evt_ext_049_loss_extremogram_lag1_63d(close: pd.Series) -> pd.Series:
    """Extremogram at lag 1: P(loss(t)>q95 | loss(t-1)>q95) over 63-day window."""
    losses = _neg_returns(close)
    thr = losses.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.95)
    exceed = (losses > thr.shift(1)).astype(float)
    lag1 = exceed.shift(1)
    joint = (exceed * lag1)
    return _safe_div(
        _rolling_sum(joint, _TD_QTR),
        _rolling_sum(lag1, _TD_QTR).clip(lower=_EPS)
    )


def evt_ext_050_tail_fading_rate_21d(close: pd.Series) -> pd.Series:
    """Rate at which extreme losses fade: mean loss on day after a top-5% loss day, 21 days."""
    losses = _neg_returns(close)
    thr = losses.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).quantile(0.95)
    was_extreme = (losses > thr.shift(1)).shift(1).astype(float)
    next_loss = losses * was_extreme
    count = _rolling_sum(was_extreme, _TD_MON)
    return _safe_div(_rolling_sum(next_loss, _TD_MON), count.clip(lower=_EPS))


# --- Group F (051-060): Multi-period extreme concordance ---

def evt_ext_051_joint_extreme_21d_63d_count(close: pd.Series) -> pd.Series:
    """Count of days where BOTH VaR95(21d) AND VaR95(63d) are in top-10% of their history."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    r21 = v21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r63 = v63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    joint = ((r21 > 0.90) & (r63 > 0.90)).astype(float)
    return _rolling_sum(joint, _TD_QTR)


def evt_ext_052_tail_regime_concordance_63d(close: pd.Series) -> pd.Series:
    """Count of days where Hill(63d), VaR95(63d), and ES95(63d) all indicate elevated risk."""
    h63 = _rolling_hill(close, _TD_QTR, 10)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    h_hi = (h63 < h63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.30)).astype(float)  # low alpha = heavy tail
    v_hi = (v63 > v63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.70)).astype(float)
    es_hi = (es63 > es63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.70)).astype(float)
    return _rolling_sum(h_hi * v_hi * es_hi, _TD_QTR)


def evt_ext_053_tail_signal_agreement_score(close: pd.Series) -> pd.Series:
    """Sum of z-scores: z(VaR95_63d) + z(ES95_63d) + z(-Hill_63d) — composite tail alarm."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    h63 = _rolling_hill(close, _TD_QTR, 10)

    def _z(s):
        m = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd.clip(lower=_EPS))

    return _z(v63) + _z(es63) + _z(-h63)


def evt_ext_054_var_above_es_flag(close: pd.Series) -> pd.Series:
    """Flag days where VaR99(63d) > ES95(63d) — degenerate tail signal."""
    v99 = _rolling_var(close, _TD_QTR, 0.99)
    es95 = _rolling_es(close, _TD_QTR, 0.95)
    return (v99 > es95).astype(float)


def evt_ext_055_extreme_var_consecutive_days(close: pd.Series) -> pd.Series:
    """Consecutive days where VaR95(63d) exceeds its 252-day 80th percentile."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    thr = v63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    return _consec_streak(v63 > thr.shift(1))


def evt_ext_056_extreme_es_consecutive_days(close: pd.Series) -> pd.Series:
    """Consecutive days where ES95(63d) exceeds its 252-day 80th percentile."""
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    thr = es63.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.80)
    return _consec_streak(es63 > thr.shift(1))


def evt_ext_057_simultaneous_var_breach_5d(close: pd.Series) -> pd.Series:
    """Days in trailing 5d where VaR95(21d) AND VaR99(63d) both breached."""
    losses = _neg_returns(close)
    v21_95 = _rolling_var(close, _TD_MON, 0.95)
    v63_99 = _rolling_var(close, _TD_QTR, 0.99)
    b1 = (losses > v21_95.shift(1)).astype(float)
    b2 = (losses > v63_99.shift(1)).astype(float)
    return _rolling_sum(b1 * b2, _TD_WEEK)


def evt_ext_058_multi_scale_tail_stress_index(close: pd.Series) -> pd.Series:
    """Multi-scale tail stress: VaR95(21d) + VaR95(63d) + VaR95(252d) normalized sum."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    v252 = _rolling_var(close, _TD_YEAR, 0.95)
    return v21 + v63 + v252


def evt_ext_059_tail_momentum_63d(close: pd.Series) -> pd.Series:
    """EWM momentum of ES95(63d): current ES vs EWM(21) of ES (trend in tail risk)."""
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    ewm_es = _ewm_mean(es63, _TD_MON)
    return es63 - ewm_es


def evt_ext_060_tail_risk_new_high_252d_flag(close: pd.Series) -> pd.Series:
    """Flag: current VaR95(63d) is the highest in trailing 252 days."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    prev_max = v63.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (v63 > prev_max).astype(float)


# --- Group G (061-075): Normalized / ratio-form variants for robustness ---

def evt_ext_061_var95_63d_over_vol_ratio(close: pd.Series) -> pd.Series:
    """VaR95(63d) / annualized vol (63d): tail severity relative to vol regime."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    vol63 = _rolling_std(_log_returns(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    return _safe_div(v63, vol63.clip(lower=_EPS))


def evt_ext_062_es99_over_var95_252d(close: pd.Series) -> pd.Series:
    """ES99(252d) / VaR95(252d): long-horizon tail shape ratio."""
    es99 = _rolling_es(close, _TD_YEAR, 0.99)
    v95 = _rolling_var(close, _TD_YEAR, 0.95)
    return _safe_div(es99, v95.clip(lower=_EPS))


def evt_ext_063_hill_normalized_by_vol_63d(close: pd.Series) -> pd.Series:
    """Hill index (63d, k=10) normalized by 63-day annualized vol."""
    h63 = _rolling_hill(close, _TD_QTR, 10)
    vol63 = _rolling_std(_log_returns(close), _TD_QTR) * np.sqrt(_TD_YEAR)
    return _safe_div(h63, vol63.clip(lower=_EPS))


def evt_ext_064_max_loss_over_avg_loss_63d(close: pd.Series) -> pd.Series:
    """Max daily loss / mean daily loss over 63 days (extreme-to-average loss ratio)."""
    losses = _neg_returns(close)
    max_l = _rolling_max(losses, _TD_QTR)
    mean_l = losses.where(losses > 0).rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()
    return _safe_div(max_l, mean_l.clip(lower=_EPS))


def evt_ext_065_loss_skew_normalized_63d(close: pd.Series) -> pd.Series:
    """Skewness of losses normalized by kurtosis over 63 days (relative skew signal)."""
    losses = _neg_returns(close)
    skew = losses.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    kurt = losses.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt().abs()
    return _safe_div(skew, kurt.clip(lower=_EPS))


def evt_ext_066_var99_63d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of VaR99(63d) — historically extreme VaR."""
    v99 = _rolling_var(close, _TD_QTR, 0.99)
    return v99.expanding(min_periods=1).rank(pct=True)


def evt_ext_067_es95_63d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of ES95(63d)."""
    es95 = _rolling_es(close, _TD_QTR, 0.95)
    return es95.expanding(min_periods=1).rank(pct=True)


def evt_ext_068_max_loss_252d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 252-day max loss."""
    ml = _rolling_max(_neg_returns(close), _TD_YEAR)
    return ml.expanding(min_periods=1).rank(pct=True)


def evt_ext_069_tail_risk_percentile_composite(close: pd.Series) -> pd.Series:
    """Mean of expanding pct ranks of VaR95(63d), ES95(63d), max_loss(252d)."""
    v63 = _rolling_var(close, _TD_QTR, 0.95).expanding(min_periods=1).rank(pct=True)
    es63 = _rolling_es(close, _TD_QTR, 0.95).expanding(min_periods=1).rank(pct=True)
    ml252 = _rolling_max(_neg_returns(close), _TD_YEAR).expanding(min_periods=1).rank(pct=True)
    return (v63 + es63 + ml252) / 3.0


def evt_ext_070_var_breach_intensity_63d(close: pd.Series) -> pd.Series:
    """Mean magnitude of VaR95(63d) breaches over 63-day window."""
    losses = _neg_returns(close)
    var95 = _rolling_var(close, _TD_QTR, 0.95)
    excess = (losses - var95.shift(1)).clip(lower=0.0)
    breach = (losses > var95.shift(1)).astype(float)
    count = _rolling_sum(breach, _TD_QTR)
    return _safe_div(_rolling_sum(excess, _TD_QTR), count.clip(lower=_EPS))


def evt_ext_071_hill_63d_volatility_adjusted(close: pd.Series) -> pd.Series:
    """Hill index (63d) minus Hill index (252d): tail-exponent regime shift."""
    h63 = _rolling_hill(close, _TD_QTR, 10)
    h252 = _rolling_hill(close, _TD_YEAR, 15)
    return h63 - h252


def evt_ext_072_tail_risk_acceleration_composite(close: pd.Series) -> pd.Series:
    """Composite acceleration: 5d diff of (VaR95_21d + ES95_63d + max_loss_21d)."""
    v21 = _rolling_var(close, _TD_MON, 0.95)
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    ml21 = _rolling_max(_neg_returns(close), _TD_MON)
    composite = v21 + es63 + ml21
    return composite.diff(_TD_WEEK)


def evt_ext_073_downside_risk_persistence_score(close: pd.Series) -> pd.Series:
    """Fraction of 252-day window where VaR95(63d) exceeds its trailing median."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    med = v63.rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    above = (v63 > med.shift(1)).astype(float)
    return _rolling_sum(above, _TD_YEAR) / _TD_YEAR


def evt_ext_074_tail_risk_ewm_momentum_63d(close: pd.Series) -> pd.Series:
    """EWM momentum of VaR95(63d): current - EWM(63) of VaR95(63d)."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    ewm_v = v63.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return v63 - ewm_v


def evt_ext_075_tail_risk_regime_flag(close: pd.Series) -> pd.Series:
    """Binary flag: VaR95(63d) in top-20% of 252-day history AND ES95(63d) in top-20%."""
    v63 = _rolling_var(close, _TD_QTR, 0.95)
    es63 = _rolling_es(close, _TD_QTR, 0.95)
    v_hi = v63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) > 0.80
    es_hi = es63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) > 0.80
    return (v_hi & es_hi).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

TAIL_RISK_EVT_EXTENDED_REGISTRY_001_075 = {
    "evt_ext_001_block_max_loss_5d_mean_63d": {"inputs": ["close"], "func": evt_ext_001_block_max_loss_5d_mean_63d},
    "evt_ext_002_block_max_loss_5d_std_63d": {"inputs": ["close"], "func": evt_ext_002_block_max_loss_5d_std_63d},
    "evt_ext_003_block_max_loss_21d_mean_252d": {"inputs": ["close"], "func": evt_ext_003_block_max_loss_21d_mean_252d},
    "evt_ext_004_block_max_loss_21d_max_252d": {"inputs": ["close"], "func": evt_ext_004_block_max_loss_21d_max_252d},
    "evt_ext_005_block_max_loss_5d_pct_rank_252d": {"inputs": ["close"], "func": evt_ext_005_block_max_loss_5d_pct_rank_252d},
    "evt_ext_006_block_mean_loss_5d_63d": {"inputs": ["close"], "func": evt_ext_006_block_mean_loss_5d_63d},
    "evt_ext_007_block_sum_loss_5d_max_63d": {"inputs": ["close"], "func": evt_ext_007_block_sum_loss_5d_max_63d},
    "evt_ext_008_block_max_loss_5d_zscore_252d": {"inputs": ["close"], "func": evt_ext_008_block_max_loss_5d_zscore_252d},
    "evt_ext_009_block_max_consecutive_new_high_63d": {"inputs": ["close"], "func": evt_ext_009_block_max_consecutive_new_high_63d},
    "evt_ext_010_range_of_block_maxima_21d_252d": {"inputs": ["close"], "func": evt_ext_010_range_of_block_maxima_21d_252d},
    "evt_ext_011_block_var95_5d_63d": {"inputs": ["close"], "func": evt_ext_011_block_var95_5d_63d},
    "evt_ext_012_block_var99_5d_252d": {"inputs": ["close"], "func": evt_ext_012_block_var99_5d_252d},
    "evt_ext_013_block_es95_5d_63d": {"inputs": ["close"], "func": evt_ext_013_block_es95_5d_63d},
    "evt_ext_014_block_hill_5d_63d": {"inputs": ["close"], "func": evt_ext_014_block_hill_5d_63d},
    "evt_ext_015_block_max_loss_5d_ema63": {"inputs": ["close"], "func": evt_ext_015_block_max_loss_5d_ema63},
    "evt_ext_016_tail_third_moment_63d": {"inputs": ["close"], "func": evt_ext_016_tail_third_moment_63d},
    "evt_ext_017_tail_fourth_moment_63d": {"inputs": ["close"], "func": evt_ext_017_tail_fourth_moment_63d},
    "evt_ext_018_spectral_risk_measure_lambda05_63d": {"inputs": ["close"], "func": evt_ext_018_spectral_risk_measure_lambda05_63d},
    "evt_ext_019_spectral_risk_measure_lambda2_63d": {"inputs": ["close"], "func": evt_ext_019_spectral_risk_measure_lambda2_63d},
    "evt_ext_020_loss_cvar_spread_63d_126d": {"inputs": ["close"], "func": evt_ext_020_loss_cvar_spread_63d_126d},
    "evt_ext_021_tail_l_moment_ratio_63d": {"inputs": ["close"], "func": evt_ext_021_tail_l_moment_ratio_63d},
    "evt_ext_022_loss_gini_coefficient_63d": {"inputs": ["close"], "func": evt_ext_022_loss_gini_coefficient_63d},
    "evt_ext_023_tail_pareto_scale_63d": {"inputs": ["close"], "func": evt_ext_023_tail_pareto_scale_63d},
    "evt_ext_024_tail_pareto_scale_252d": {"inputs": ["close"], "func": evt_ext_024_tail_pareto_scale_252d},
    "evt_ext_025_loss_cv_63d": {"inputs": ["close"], "func": evt_ext_025_loss_cv_63d},
    "evt_ext_026_high_low_range_pct_max_63d": {"inputs": ["close", "high", "low"], "func": evt_ext_026_high_low_range_pct_max_63d},
    "evt_ext_027_high_low_range_pct_q95_63d": {"inputs": ["close", "high", "low"], "func": evt_ext_027_high_low_range_pct_q95_63d},
    "evt_ext_028_close_to_low_tail_63d": {"inputs": ["close", "low"], "func": evt_ext_028_close_to_low_tail_63d},
    "evt_ext_029_open_gap_down_tail_63d": {"inputs": ["close", "open"], "func": evt_ext_029_open_gap_down_tail_63d},
    "evt_ext_030_open_gap_down_sum_63d": {"inputs": ["close", "open"], "func": evt_ext_030_open_gap_down_sum_63d},
    "evt_ext_031_high_low_range_kurt_63d": {"inputs": ["close", "high", "low"], "func": evt_ext_031_high_low_range_kurt_63d},
    "evt_ext_032_close_vs_low_pct_rank_252d": {"inputs": ["close", "low"], "func": evt_ext_032_close_vs_low_pct_rank_252d},
    "evt_ext_033_hl_range_vs_median_ratio_63d": {"inputs": ["close", "high", "low"], "func": evt_ext_033_hl_range_vs_median_ratio_63d},
    "evt_ext_034_hl_extreme_range_count_63d": {"inputs": ["close", "high", "low"], "func": evt_ext_034_hl_extreme_range_count_63d},
    "evt_ext_035_open_close_loss_q95_63d": {"inputs": ["close", "open"], "func": evt_ext_035_open_close_loss_q95_63d},
    "evt_ext_036_es95_high_vol_days_63d": {"inputs": ["close", "volume"], "func": evt_ext_036_es95_high_vol_days_63d},
    "evt_ext_037_var99_high_vol_days_63d": {"inputs": ["close", "volume"], "func": evt_ext_037_var99_high_vol_days_63d},
    "evt_ext_038_es_high_vs_low_vol_ratio_63d": {"inputs": ["close", "volume"], "func": evt_ext_038_es_high_vs_low_vol_ratio_63d},
    "evt_ext_039_vol_weighted_es99_63d": {"inputs": ["close", "volume"], "func": evt_ext_039_vol_weighted_es99_63d},
    "evt_ext_040_max_loss_on_high_vol_63d": {"inputs": ["close", "volume"], "func": evt_ext_040_max_loss_on_high_vol_63d},
    "evt_ext_041_tail_vol_correlation_63d": {"inputs": ["close", "volume"], "func": evt_ext_041_tail_vol_correlation_63d},
    "evt_ext_042_loss_vol_correlation_21d": {"inputs": ["close", "volume"], "func": evt_ext_042_loss_vol_correlation_21d},
    "evt_ext_043_extreme_loss_vol_amplification_63d": {"inputs": ["close", "volume"], "func": evt_ext_043_extreme_loss_vol_amplification_63d},
    "evt_ext_044_tail_decay_rate_63d": {"inputs": ["close"], "func": evt_ext_044_tail_decay_rate_63d},
    "evt_ext_045_var95_autocorr_lag1_252d": {"inputs": ["close"], "func": evt_ext_045_var95_autocorr_lag1_252d},
    "evt_ext_046_es99_autocorr_lag1_252d": {"inputs": ["close"], "func": evt_ext_046_es99_autocorr_lag1_252d},
    "evt_ext_047_var_hurst_proxy_252d": {"inputs": ["close"], "func": evt_ext_047_var_hurst_proxy_252d},
    "evt_ext_048_loss_extremogram_lag5_63d": {"inputs": ["close"], "func": evt_ext_048_loss_extremogram_lag5_63d},
    "evt_ext_049_loss_extremogram_lag1_63d": {"inputs": ["close"], "func": evt_ext_049_loss_extremogram_lag1_63d},
    "evt_ext_050_tail_fading_rate_21d": {"inputs": ["close"], "func": evt_ext_050_tail_fading_rate_21d},
    "evt_ext_051_joint_extreme_21d_63d_count": {"inputs": ["close"], "func": evt_ext_051_joint_extreme_21d_63d_count},
    "evt_ext_052_tail_regime_concordance_63d": {"inputs": ["close"], "func": evt_ext_052_tail_regime_concordance_63d},
    "evt_ext_053_tail_signal_agreement_score": {"inputs": ["close"], "func": evt_ext_053_tail_signal_agreement_score},
    "evt_ext_054_var_above_es_flag": {"inputs": ["close"], "func": evt_ext_054_var_above_es_flag},
    "evt_ext_055_extreme_var_consecutive_days": {"inputs": ["close"], "func": evt_ext_055_extreme_var_consecutive_days},
    "evt_ext_056_extreme_es_consecutive_days": {"inputs": ["close"], "func": evt_ext_056_extreme_es_consecutive_days},
    "evt_ext_057_simultaneous_var_breach_5d": {"inputs": ["close"], "func": evt_ext_057_simultaneous_var_breach_5d},
    "evt_ext_058_multi_scale_tail_stress_index": {"inputs": ["close"], "func": evt_ext_058_multi_scale_tail_stress_index},
    "evt_ext_059_tail_momentum_63d": {"inputs": ["close"], "func": evt_ext_059_tail_momentum_63d},
    "evt_ext_060_tail_risk_new_high_252d_flag": {"inputs": ["close"], "func": evt_ext_060_tail_risk_new_high_252d_flag},
    "evt_ext_061_var95_63d_over_vol_ratio": {"inputs": ["close"], "func": evt_ext_061_var95_63d_over_vol_ratio},
    "evt_ext_062_es99_over_var95_252d": {"inputs": ["close"], "func": evt_ext_062_es99_over_var95_252d},
    "evt_ext_063_hill_normalized_by_vol_63d": {"inputs": ["close"], "func": evt_ext_063_hill_normalized_by_vol_63d},
    "evt_ext_064_max_loss_over_avg_loss_63d": {"inputs": ["close"], "func": evt_ext_064_max_loss_over_avg_loss_63d},
    "evt_ext_065_loss_skew_normalized_63d": {"inputs": ["close"], "func": evt_ext_065_loss_skew_normalized_63d},
    "evt_ext_066_var99_63d_expanding_pct_rank": {"inputs": ["close"], "func": evt_ext_066_var99_63d_expanding_pct_rank},
    "evt_ext_067_es95_63d_expanding_pct_rank": {"inputs": ["close"], "func": evt_ext_067_es95_63d_expanding_pct_rank},
    "evt_ext_068_max_loss_252d_expanding_pct_rank": {"inputs": ["close"], "func": evt_ext_068_max_loss_252d_expanding_pct_rank},
    "evt_ext_069_tail_risk_percentile_composite": {"inputs": ["close"], "func": evt_ext_069_tail_risk_percentile_composite},
    "evt_ext_070_var_breach_intensity_63d": {"inputs": ["close"], "func": evt_ext_070_var_breach_intensity_63d},
    "evt_ext_071_hill_63d_volatility_adjusted": {"inputs": ["close"], "func": evt_ext_071_hill_63d_volatility_adjusted},
    "evt_ext_072_tail_risk_acceleration_composite": {"inputs": ["close"], "func": evt_ext_072_tail_risk_acceleration_composite},
    "evt_ext_073_downside_risk_persistence_score": {"inputs": ["close"], "func": evt_ext_073_downside_risk_persistence_score},
    "evt_ext_074_tail_risk_ewm_momentum_63d": {"inputs": ["close"], "func": evt_ext_074_tail_risk_ewm_momentum_63d},
    "evt_ext_075_tail_risk_regime_flag": {"inputs": ["close"], "func": evt_ext_075_tail_risk_regime_flag},
}
