"""short_squeeze_aftermath_technical base features 376-450 — Pipeline 1b-technical.

Fourth gap-fill batch. Independent predictive angles distinct from 001-375:
SI-price correlation & divergence patterns, Calmar/Ulcer/pain-index ratio
variants, run-length / Wald-Wolfowitz sequencing tests, GARCH-like vol-clustering
proxies, profit-factor / hit-rate ratios, conditional drawdown-by-NSIR-regime,
trend-rank percentiles, pre-collapse composite scoring, and terminal-phase
volume drying patterns.

Bucket MM: SI-price correlation & divergence (376-385).
Bucket NN: Calmar / Ulcer / pain-index variants (386-393).
Bucket OO: Run-lengths / sequencing tests (394-402).
Bucket PP: Vol-clustering / GARCH proxies (403-410).
Bucket QQ: Profit factor & ratios (411-418).
Bucket RR: Conditional drawdown / drawup events (419-426).
Bucket SS: Trend rank / multi-horizon disagreement (427-434).
Bucket TT: Pre-collapse signature scoring (435-443).
Bucket UU: Volume-pattern terminal-phase (444-450).

Inputs: SEP OHLCV + NSIR (NaN-stubbed when absent). Self-contained; PIT-clean.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


# ============================================================
# Bucket MM — SI-price correlation & divergence (376-385)
# ============================================================

def f48_ssat_376_si_close_corr_63(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d correlation between SI and close — direct relationship measure."""
    return shortinterest.astype(float).rolling(QDAYS, min_periods=MDAYS).corr(close)


def f48_ssat_377_si_close_corr_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d correlation between SI and close — annual relationship."""
    return shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).corr(close)


def f48_ssat_378_si_chg_return_corr_63(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr(SI 5d change, 5d return) — flow-return relationship."""
    return shortinterest.astype(float).diff(WDAYS).rolling(QDAYS, min_periods=MDAYS).corr(close.pct_change(WDAYS))


def f48_ssat_379_si_chg_return_corr_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d corr(SI 5d change, 5d return) — annual flow-return correlation."""
    return shortinterest.astype(float).diff(WDAYS).rolling(YDAYS, min_periods=QDAYS).corr(close.pct_change(WDAYS))


def f48_ssat_380_si_down_price_down_joint_state(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI 21d slope < 0 AND close 21d slope < 0 — joint downward NSIR + price."""
    si_sl = _rolling_slope(shortinterest.astype(float), MDAYS)
    pr_sl = _rolling_slope(close, MDAYS)
    return ((si_sl < 0) & (pr_sl < 0)).astype(float).where(si_sl.notna() & pr_sl.notna(), np.nan)


def f48_ssat_381_si_declined_20pct_from_252max_state(shortinterest: pd.Series) -> pd.Series:
    """1 if SI has fallen >20% from its 252d max."""
    s = shortinterest.astype(float)
    return (s < 0.8 * s.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(s.notna(), np.nan)


def f48_ssat_382_si_declined_50pct_from_252max_state(shortinterest: pd.Series) -> pd.Series:
    """1 if SI has fallen >50% from its 252d max — heavy unwind."""
    s = shortinterest.astype(float)
    return (s < 0.5 * s.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(s.notna(), np.nan)


def f48_ssat_383_si_over_252d_mean_ratio(shortinterest: pd.Series) -> pd.Series:
    """SI / 252d-mean-SI — current SI vs own annual mean."""
    s = shortinterest.astype(float)
    return _safe_div(s, s.rolling(YDAYS, min_periods=QDAYS).mean())


def f48_ssat_384_bars_since_si_change_above_21d_mean_chg(shortinterest: pd.Series) -> pd.Series:
    """Bars since SI diff was above 21d-mean of SI diffs (i.e., above-average increase)."""
    s = shortinterest.astype(float)
    diff = s.diff()
    avg_diff = diff.rolling(MDAYS, min_periods=WDAYS).mean()
    return _bars_since_true(diff > avg_diff)


def f48_ssat_385_si_close_cum_rank_corr_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252d Spearman-like correlation (correlation of ranks) — robust SI-price relationship."""
    s = shortinterest.astype(float)
    s_r = s.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    c_r = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return s_r.rolling(YDAYS, min_periods=QDAYS).corr(c_r)


# ============================================================
# Bucket NN — Calmar / Ulcer / pain-index variants (386-393)
# ============================================================

def f48_ssat_386_calmar_ratio_252(close: pd.Series) -> pd.Series:
    """252d return / |max drawdown past 252| — Calmar ratio."""
    ret = close.pct_change(YDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    max_dd = dd.rolling(YDAYS, min_periods=QDAYS).min().abs()
    return _safe_div(ret, max_dd)


def f48_ssat_387_calmar_ratio_504(close: pd.Series) -> pd.Series:
    """504d return / |max drawdown past 504| — multi-year Calmar."""
    ret = close.pct_change(DDAYS_2Y)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    max_dd = dd.rolling(DDAYS_2Y, min_periods=YDAYS).min().abs()
    return _safe_div(ret, max_dd)


def f48_ssat_388_ulcer_index_63(close: pd.Series) -> pd.Series:
    """RMS of drawdown past 63 — Ulcer Index (Peter Martin), quarterly."""
    cummax = close.cummax()
    dd = (close / cummax - 1.0) * 100.0
    return (dd ** 2).rolling(QDAYS, min_periods=MDAYS).mean().pow(0.5)


def f48_ssat_389_ulcer_index_252(close: pd.Series) -> pd.Series:
    """Annual Ulcer Index."""
    cummax = close.cummax()
    dd = (close / cummax - 1.0) * 100.0
    return (dd ** 2).rolling(YDAYS, min_periods=QDAYS).mean().pow(0.5)


def f48_ssat_390_pain_index_252(close: pd.Series) -> pd.Series:
    """Mean |drawdown| past 252 — Pain Index (avg pain experienced)."""
    cummax = close.cummax()
    dd = (close / cummax - 1.0).abs()
    return dd.rolling(YDAYS, min_periods=QDAYS).mean()


def f48_ssat_391_martin_ratio_252(close: pd.Series) -> pd.Series:
    """252d return / Ulcer Index 252 — Martin (UPI) ratio."""
    ret = close.pct_change(YDAYS)
    cummax = close.cummax()
    dd = (close / cummax - 1.0) * 100.0
    ui = (dd ** 2).rolling(YDAYS, min_periods=QDAYS).mean().pow(0.5)
    return _safe_div(ret, ui)


def f48_ssat_392_sterling_ratio_252(close: pd.Series) -> pd.Series:
    """252d return / (|max drawdown| - 10%) — Sterling ratio (annual)."""
    ret = close.pct_change(YDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    max_dd = dd.rolling(YDAYS, min_periods=QDAYS).min().abs()
    return _safe_div(ret, max_dd - 0.10)


def f48_ssat_393_burke_ratio_variant_252(close: pd.Series) -> pd.Series:
    """252d return / sqrt(sum of squared drawdowns past 252) — Burke ratio variant."""
    ret = close.pct_change(YDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    sum_sq = (dd ** 2).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(ret, np.sqrt(sum_sq))


# ============================================================
# Bucket OO — Run lengths / sequencing tests (394-402)
# ============================================================

def f48_ssat_394_longest_down_day_streak_252(close: pd.Series) -> pd.Series:
    """Longest consecutive down-close streak in past 252."""
    dn = (close < close.shift(1))
    s = _streak_true(dn)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(dn.notna(), np.nan)


def f48_ssat_395_longest_lower_low_sequential_streak_252(low: pd.Series) -> pd.Series:
    """Longest consecutive bars where low < prior low — sequential-lower-low streak."""
    cond = (low < low.shift(1))
    s = _streak_true(cond)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(cond.notna(), np.nan)


def f48_ssat_396_longest_lower_high_sequential_streak_252(high: pd.Series) -> pd.Series:
    """Longest consecutive bars where high < prior high."""
    cond = (high < high.shift(1))
    s = _streak_true(cond)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(cond.notna(), np.nan)


def f48_ssat_397_count_3plus_down_streaks_252(close: pd.Series) -> pd.Series:
    """Annual count of distinct 3+ down-day streak events."""
    dn = (close < close.shift(1))
    s = _streak_true(dn)
    ev = ((s == 3) & (s.shift(1) == 2)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(dn.notna(), np.nan)


def f48_ssat_398_count_5plus_down_streaks_252(close: pd.Series) -> pd.Series:
    """Annual count of distinct 5+ down-day streak events."""
    dn = (close < close.shift(1))
    s = _streak_true(dn)
    ev = ((s == 5) & (s.shift(1) == 4)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(dn.notna(), np.nan)


def f48_ssat_399_longest_above_sma50_streak_252(close: pd.Series) -> pd.Series:
    """Longest above-SMA50 streak in past 252 — uptrend persistence."""
    sma = _sma(close, 50)
    s = _streak_true(close > sma)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(sma.notna(), np.nan)


def f48_ssat_400_longest_below_sma50_streak_252(close: pd.Series) -> pd.Series:
    """Longest below-SMA50 streak in past 252."""
    sma = _sma(close, 50)
    s = _streak_true(close < sma)
    return s.rolling(YDAYS, min_periods=QDAYS).max().where(sma.notna(), np.nan)


def f48_ssat_401_wald_wolfowitz_runs_z_63(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs test z-score on return-signs past 63 — positive=clustered, negative=mean-reverting."""
    r = close.pct_change()
    sgn = np.sign(r).fillna(0)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        v = (v > 0).astype(int)
        n1 = int((v == 1).sum()); n2 = int((v == 0).sum())
        if n1 == 0 or n2 == 0:
            return np.nan
        # count runs
        runs = 1 + int(np.sum(v[1:] != v[:-1]))
        n = n1 + n2
        mean = (2 * n1 * n2) / n + 1
        var = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n ** 2 * (n - 1)) if n > 1 else 0.0
        if var <= 0:
            return np.nan
        return float((runs - mean) / np.sqrt(var))
    return sgn.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f48_ssat_402_return_sign_autocorr_lag1_63(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of return signs past 63 — sequence persistence (positive=trend, negative=alternating)."""
    r = close.pct_change()
    sgn = np.sign(r)
    return sgn.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: float(pd.Series(w).autocorr(lag=1)) if pd.Series(w).std() > 0 else np.nan, raw=True)


# ============================================================
# Bucket PP — Vol-clustering / GARCH proxies (403-410)
# ============================================================

def f48_ssat_403_squared_return_ac_lag1_63(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of squared returns past 63 — volatility-clustering measure."""
    r2 = close.pct_change() ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: float(pd.Series(w).autocorr(lag=1)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f48_ssat_404_squared_return_ac_lag5_63(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of squared returns past 63."""
    r2 = close.pct_change() ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: float(pd.Series(w).autocorr(lag=5)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f48_ssat_405_abs_return_ac_lag1_252(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of |returns| past 252 — annual vol-clustering measure."""
    ar = close.pct_change().abs()
    return ar.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: float(pd.Series(w).autocorr(lag=1)) if pd.Series(w).std() > 0 else np.nan, raw=True)


def f48_ssat_406_arch_1_proxy_var_squared_returns_63(close: pd.Series) -> pd.Series:
    """Variance of squared returns past 63 — ARCH-1 effect proxy (higher = more clustering)."""
    r2 = close.pct_change() ** 2
    return r2.rolling(QDAYS, min_periods=MDAYS).var()


def f48_ssat_407_garch_persistence_proxy(close: pd.Series) -> pd.Series:
    """EWMA-vol-21 / EWMA-vol-63 — short-vs-long EWMA-vol ratio (proxy for vol persistence)."""
    r = close.pct_change()
    a21 = 1.0 - 0.5 ** (1.0 / WDAYS)
    a63 = 1.0 - 0.5 ** (1.0 / MDAYS)
    v21 = r.ewm(alpha=a21, adjust=False, min_periods=WDAYS).std()
    v63 = r.ewm(alpha=a63, adjust=False, min_periods=MDAYS).std()
    return _safe_div(v21, v63)


def f48_ssat_408_vol_of_vol_of_vol_63(close: pd.Series) -> pd.Series:
    """3rd-order vol: std of (21d-std of (21d-std of returns)) past 63 — vol-of-vol-of-vol."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(QDAYS, min_periods=MDAYS).std()


def f48_ssat_409_vol_spike_count_252(close: pd.Series) -> pd.Series:
    """Annual count of bars with |return| > 3 * 21d-std — vol-spike frequency."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return (r.abs() > 3.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s.notna(), np.nan)


def f48_ssat_410_vol_spike_count_504(close: pd.Series) -> pd.Series:
    """2-year vol-spike count."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    return (r.abs() > 3.0 * s).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(s.notna(), np.nan)


# ============================================================
# Bucket QQ — Profit factor & ratios (411-418)
# ============================================================

def f48_ssat_411_profit_factor_21(close: pd.Series) -> pd.Series:
    """Sum of positive returns / sum of |negative returns| past 21."""
    r = close.pct_change()
    pos = r.where(r > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(pos, neg)


def f48_ssat_412_profit_factor_63(close: pd.Series) -> pd.Series:
    """Quarterly profit factor."""
    r = close.pct_change()
    pos = r.where(r > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(pos, neg)


def f48_ssat_413_profit_factor_252(close: pd.Series) -> pd.Series:
    """Annual profit factor."""
    r = close.pct_change()
    pos = r.where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(pos, neg)


def f48_ssat_414_hit_rate_21(close: pd.Series) -> pd.Series:
    """Fraction of past 21 returns > 0."""
    r = close.pct_change()
    return (r > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(r.notna(), np.nan)


def f48_ssat_415_hit_rate_63(close: pd.Series) -> pd.Series:
    """Quarterly hit rate."""
    r = close.pct_change()
    return (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)


def f48_ssat_416_avg_gain_over_avg_loss_252(close: pd.Series) -> pd.Series:
    """Mean(positive returns) / |mean(negative returns)| past 252 — payoff ratio."""
    r = close.pct_change()
    pos = r.where(r > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    neg = r.where(r < 0).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    return _safe_div(pos, neg)


def f48_ssat_417_skew_adjusted_profit_ratio_252(close: pd.Series) -> pd.Series:
    """Profit factor * (1 + skew/2) past 252 — skew-adjusted profit ratio."""
    r = close.pct_change()
    pos = r.where(r > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = r.where(r < 0, 0.0).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    pf = _safe_div(pos, neg)
    skew = r.rolling(YDAYS, min_periods=QDAYS).skew()
    return pf * (1.0 + skew / 2.0)


def f48_ssat_418_kelly_fraction_proxy_252(close: pd.Series) -> pd.Series:
    """Kelly fraction proxy: (hit-rate * avg-win - (1-hit-rate) * avg-loss) / avg-win, past 252."""
    r = close.pct_change()
    hit = (r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    avg_win = r.where(r > 0).rolling(YDAYS, min_periods=QDAYS).mean()
    avg_loss = r.where(r < 0).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    return _safe_div(hit * avg_win - (1.0 - hit) * avg_loss, avg_win)


# ============================================================
# Bucket RR — Conditional drawdown / drawup events (419-426)
# ============================================================

def f48_ssat_419_mean_dd_when_si_rising_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Mean drawdown past 252 conditional on SI 21d slope > 0 (SI rising regime)."""
    s = shortinterest.astype(float)
    si_sl = _rolling_slope(s, MDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    return dd.where(si_sl > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f48_ssat_420_mean_dd_when_si_falling_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Mean drawdown past 252 conditional on SI 21d slope < 0 (SI unwinding)."""
    s = shortinterest.astype(float)
    si_sl = _rolling_slope(s, MDAYS)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    return dd.where(si_sl < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f48_ssat_421_max_dd_when_si_above_median_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Min drawdown past 252 conditioned on SI > 252d median — worst dd during high-SI regime."""
    s = shortinterest.astype(float)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    cummax = close.cummax()
    dd = close / cummax - 1.0
    return dd.where(s > med, np.nan).rolling(YDAYS, min_periods=QDAYS).min()


def f48_ssat_422_max_dd_when_si_below_median_252(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """Min drawdown past 252 conditioned on SI < 252d median — worst dd during low-SI regime."""
    s = shortinterest.astype(float)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    cummax = close.cummax()
    dd = close / cummax - 1.0
    return dd.where(s < med, np.nan).rolling(YDAYS, min_periods=QDAYS).min()


def f48_ssat_423_dd_velocity_at_si_peak_event(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1-bar drawdown change conditional on SI just hit 252d max (within past 5 bars)."""
    s = shortinterest.astype(float)
    si_peak_recent = (s == s.rolling(YDAYS, min_periods=QDAYS).max()).rolling(WDAYS, min_periods=1).max() > 0
    cummax = close.cummax()
    dd = close / cummax - 1.0
    return dd.diff().where(si_peak_recent, np.nan)


def f48_ssat_424_drawdown_then_recovery_count_252(close: pd.Series) -> pd.Series:
    """Count past 252 of distinct events: drawdown crossed below -10% then back above -5% within 21 bars."""
    cummax = close.cummax()
    dd = close / cummax - 1.0
    entered = (dd.shift(1) >= -0.10) & (dd < -0.10)
    recovered_5d = entered.shift(MDAYS) & (dd > -0.05)
    return recovered_5d.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(dd.notna(), np.nan)


def f48_ssat_425_bars_since_recovery_attempt_63(close: pd.Series) -> pd.Series:
    """Bars since last 5d-return > 5% — recency of recovery attempt."""
    return _bars_since_true(close.pct_change(WDAYS) > 0.05)


def f48_ssat_426_max_dd_rebound_failure_flag(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if drawdown was once <-50% in past 252 AND today's drawdown is STILL <-50% — recovery failure."""
    cummax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = close / cummax - 1.0
    was_severe = (dd.rolling(YDAYS, min_periods=QDAYS).min() <= -0.50)
    return (was_severe & (dd <= -0.50)).astype(float).where(dd.notna(), np.nan)


# ============================================================
# Bucket SS — Trend rank / multi-horizon disagreement (427-434)
# ============================================================

def f48_ssat_427_trend_strength_21_pct_rank_252(close: pd.Series) -> pd.Series:
    """Pct rank of 21d slope vs 252d distribution of 21d slopes."""
    sl = _rolling_slope(close, MDAYS)
    return sl.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f48_ssat_428_trend_strength_63_pct_rank_252(close: pd.Series) -> pd.Series:
    """Pct rank of 63d slope vs 252d distribution."""
    sl = _rolling_slope(close, QDAYS)
    return sl.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f48_ssat_429_trend_strength_252_pct_rank_504(close: pd.Series) -> pd.Series:
    """Pct rank of 252d slope vs 504d distribution."""
    sl = _rolling_slope(close, YDAYS)
    return sl.rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)


def f48_ssat_430_multi_horizon_trend_disagreement_count(close: pd.Series) -> pd.Series:
    """Number of sign-flips across slopes of 5/21/63/252 horizons — 0-3, higher = more disagreement."""
    sl5 = np.sign(_rolling_slope(close, WDAYS))
    sl21 = np.sign(_rolling_slope(close, MDAYS))
    sl63 = np.sign(_rolling_slope(close, QDAYS))
    sl252 = np.sign(_rolling_slope(close, YDAYS))
    return ((sl5 != sl21).astype(float) + (sl21 != sl63).astype(float) + (sl63 != sl252).astype(float))


def f48_ssat_431_trend_slope_21_sign_flip_count_63(close: pd.Series) -> pd.Series:
    """Count past 63 of 21d slope sign-flips — trend-instability indicator."""
    sl = _rolling_slope(close, MDAYS)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)


def f48_ssat_432_trend_slope_63_sign_flip_count_252(close: pd.Series) -> pd.Series:
    """Annual count of 63d slope sign-flips."""
    sl = _rolling_slope(close, QDAYS)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().where(sl.notna(), np.nan)


def f48_ssat_433_trend_coherence_score(close: pd.Series) -> pd.Series:
    """Count of same-sign slopes across 5/21/63/252 / 4 — trend coherence (1=fully aligned, 0=fully disaligned)."""
    s5 = np.sign(_rolling_slope(close, WDAYS))
    s21 = np.sign(_rolling_slope(close, MDAYS))
    s63 = np.sign(_rolling_slope(close, QDAYS))
    s252 = np.sign(_rolling_slope(close, YDAYS))
    bull_count = ((s5 > 0).astype(float) + (s21 > 0).astype(float) + (s63 > 0).astype(float) + (s252 > 0).astype(float))
    bear_count = ((s5 < 0).astype(float) + (s21 < 0).astype(float) + (s63 < 0).astype(float) + (s252 < 0).astype(float))
    return pd.concat([bull_count, bear_count], axis=1).max(axis=1) / 4.0


def f48_ssat_434_trend_of_trend_21d(close: pd.Series) -> pd.Series:
    """21d slope of (21d slope of close) — trend-of-trend (positive = trend strengthening)."""
    sl = _rolling_slope(close, MDAYS)
    return _rolling_slope(sl, MDAYS)


# ============================================================
# Bucket TT — Pre-collapse signature scoring (435-443)
# ============================================================

def f48_ssat_435_composite_bear_pressure_score(close: pd.Series) -> pd.Series:
    """Sum of bear-conditions: {SMA21<SMA50, RSI<50, close<SMA200, 21d ret<0, drawdown<-10%} — score 0-5."""
    sma21 = _sma(close, MDAYS); sma50 = _sma(close, 50); sma200 = _sma(close, 200)
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    ad = dn.ewm(alpha=1.0 / 14, adjust=False, min_periods=14).mean()
    rsi = 100.0 - 100.0 / (1.0 + _safe_div(au, ad))
    cummax = close.cummax()
    dd = close / cummax - 1.0
    score = ((sma21 < sma50).astype(float).fillna(0)
             + (rsi < 50).astype(float).fillna(0)
             + (close < sma200).astype(float).fillna(0)
             + (close.pct_change(MDAYS) < 0).astype(float).fillna(0)
             + (dd < -0.10).astype(float).fillna(0))
    return score


def f48_ssat_436_composite_pre_collapse_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of {dist-day-cluster, prior-parabolic-run, ATR-expansion, drawdown >10%} — pre-collapse score."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    cluster_5 = ((down & bigvol).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() >= 5)
    prior_parabolic = (close.pct_change(QDAYS).rolling(YDAYS, min_periods=QDAYS).max() > 1.0)
    atr_expansion = (_safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS)) > 1.5)
    cummax = close.cummax()
    dd = close / cummax - 1.0
    dd_10 = (dd < -0.10)
    return (cluster_5.astype(float).fillna(0)
            + prior_parabolic.astype(float).fillna(0)
            + atr_expansion.astype(float).fillna(0)
            + dd_10.astype(float).fillna(0))


def f48_ssat_437_count_high_vol_down_3sigma_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 21 of bars with return < -3*21d-std AND vol > 1.5x 21d avg — high-vol panic events."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (r < -3.0 * s) & (volume > 1.5 * v_avg)
    return cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(s.notna() & v_avg.notna(), np.nan)


def f48_ssat_438_count_high_vol_down_3sigma_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Quarterly count of high-vol-3σ-down events."""
    r = close.pct_change()
    s = r.rolling(MDAYS, min_periods=WDAYS).std()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (r < -3.0 * s) & (volume > 1.5 * v_avg)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(s.notna() & v_avg.notna(), np.nan)


def f48_ssat_439_top3_down_days_vol_share_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Sum of vol on 3 worst down-bars past 63) / (sum vol past 63) — concentration on heaviest decline days."""
    r = close.pct_change()
    n = len(close); out = np.full(n, np.nan)
    r_arr = r.to_numpy(dtype=float); v_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - QDAYS + 1)
        rw = r_arr[lo : t + 1]; vw = v_arr[lo : t + 1]
        valid = ~(np.isnan(rw) | np.isnan(vw))
        if valid.sum() < MDAYS:
            continue
        rv = rw[valid]; vv = vw[valid]
        if rv.size < 3:
            continue
        idx_sorted = np.argsort(rv)[:3]
        top3_vol = float(vv[idx_sorted].sum())
        total = float(vv.sum())
        if total == 0:
            continue
        out[t] = top3_vol / total
    return pd.Series(out, index=close.index)


def f48_ssat_440_top3_down_days_vol_share_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual variant — concentration of vol on 3 worst down-bars past 252."""
    r = close.pct_change()
    n = len(close); out = np.full(n, np.nan)
    r_arr = r.to_numpy(dtype=float); v_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - YDAYS + 1)
        rw = r_arr[lo : t + 1]; vw = v_arr[lo : t + 1]
        valid = ~(np.isnan(rw) | np.isnan(vw))
        if valid.sum() < QDAYS:
            continue
        rv = rw[valid]; vv = vw[valid]
        if rv.size < 3:
            continue
        idx_sorted = np.argsort(rv)[:3]
        top3_vol = float(vv[idx_sorted].sum())
        total = float(vv.sum())
        if total == 0:
            continue
        out[t] = top3_vol / total
    return pd.Series(out, index=close.index)


def f48_ssat_441_mar_ratio_proxy_252(close: pd.Series) -> pd.Series:
    """Max-drawdown / annualized-vol past 252 — Mar-like ratio (negative for losing periods)."""
    cummax = close.cummax()
    dd = (close / cummax - 1.0).rolling(YDAYS, min_periods=QDAYS).min()
    ann_vol = close.pct_change().rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(dd, ann_vol)


def f48_ssat_442_capit_followed_by_lower_low_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 252 of capitulation bars followed by lower-low within 5 bars."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    # at t: was there a capit bar at t-5 AND today's low < low[t-5]?
    cap_5_ago = capit.shift(WDAYS)
    lower_low = (low < low.shift(WDAYS))
    return (cap_5_ago & lower_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna(), np.nan)


def f48_ssat_443_capit_followed_by_5d_decline_10pct_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 252 of capitulation bars followed by 5d cum return < -10%."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    cap_5_ago = capit.shift(WDAYS)
    decline = (close.pct_change(WDAYS) < -0.10)
    return (cap_5_ago & decline).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(a.notna(), np.nan)


# ============================================================
# Bucket UU — Volume-pattern terminal-phase (444-450)
# ============================================================

def f48_ssat_444_vol_trend_slope_63(volume: pd.Series) -> pd.Series:
    """63d rolling slope of volume — drying trend (negative = volume drying)."""
    return _rolling_slope(volume, QDAYS)


def f48_ssat_445_vol_trend_slope_252(volume: pd.Series) -> pd.Series:
    """Annual rolling slope of volume."""
    return _rolling_slope(volume, YDAYS)


def f48_ssat_446_vol_cv_63_alt(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume past 63 — vol variability."""
    return _safe_div(volume.rolling(QDAYS, min_periods=MDAYS).std(), volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f48_ssat_447_vol_5d_over_63d_mean_ratio(volume: pd.Series) -> pd.Series:
    """5d-mean vol / 63d-mean vol — terminal drying (low value)."""
    return _safe_div(volume.rolling(WDAYS, min_periods=2).mean(), volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f48_ssat_448_bars_since_volume_252d_max(volume: pd.Series) -> pd.Series:
    """Bars since volume reached its 252d max."""
    return _bars_since_true(volume == volume.rolling(YDAYS, min_periods=QDAYS).max())


def f48_ssat_449_count_low_vol_below_half_median_63(volume: pd.Series) -> pd.Series:
    """Count past 63 of bars with vol < 50% of 252d median — drought count."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (volume < 0.5 * med).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f48_ssat_450_count_low_vol_below_half_median_252(volume: pd.Series) -> pd.Series:
    """Annual count of low-vol bars."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return (volume < 0.5 * med).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(med.notna(), np.nan)


# ============================================================
#                         REGISTRY 376-450
# ============================================================

_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_BASE_REGISTRY_376_450 = {
    "f48_ssat_376_si_close_corr_63": {"inputs": ["shortinterest", "close"], "func": f48_ssat_376_si_close_corr_63},
    "f48_ssat_377_si_close_corr_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_377_si_close_corr_252},
    "f48_ssat_378_si_chg_return_corr_63": {"inputs": ["shortinterest", "close"], "func": f48_ssat_378_si_chg_return_corr_63},
    "f48_ssat_379_si_chg_return_corr_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_379_si_chg_return_corr_252},
    "f48_ssat_380_si_down_price_down_joint_state": {"inputs": ["shortinterest", "close"], "func": f48_ssat_380_si_down_price_down_joint_state},
    "f48_ssat_381_si_declined_20pct_from_252max_state": {"inputs": ["shortinterest"], "func": f48_ssat_381_si_declined_20pct_from_252max_state},
    "f48_ssat_382_si_declined_50pct_from_252max_state": {"inputs": ["shortinterest"], "func": f48_ssat_382_si_declined_50pct_from_252max_state},
    "f48_ssat_383_si_over_252d_mean_ratio": {"inputs": ["shortinterest"], "func": f48_ssat_383_si_over_252d_mean_ratio},
    "f48_ssat_384_bars_since_si_change_above_21d_mean_chg": {"inputs": ["shortinterest"], "func": f48_ssat_384_bars_since_si_change_above_21d_mean_chg},
    "f48_ssat_385_si_close_cum_rank_corr_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_385_si_close_cum_rank_corr_252},
    "f48_ssat_386_calmar_ratio_252": {"inputs": ["close"], "func": f48_ssat_386_calmar_ratio_252},
    "f48_ssat_387_calmar_ratio_504": {"inputs": ["close"], "func": f48_ssat_387_calmar_ratio_504},
    "f48_ssat_388_ulcer_index_63": {"inputs": ["close"], "func": f48_ssat_388_ulcer_index_63},
    "f48_ssat_389_ulcer_index_252": {"inputs": ["close"], "func": f48_ssat_389_ulcer_index_252},
    "f48_ssat_390_pain_index_252": {"inputs": ["close"], "func": f48_ssat_390_pain_index_252},
    "f48_ssat_391_martin_ratio_252": {"inputs": ["close"], "func": f48_ssat_391_martin_ratio_252},
    "f48_ssat_392_sterling_ratio_252": {"inputs": ["close"], "func": f48_ssat_392_sterling_ratio_252},
    "f48_ssat_393_burke_ratio_variant_252": {"inputs": ["close"], "func": f48_ssat_393_burke_ratio_variant_252},
    "f48_ssat_394_longest_down_day_streak_252": {"inputs": ["close"], "func": f48_ssat_394_longest_down_day_streak_252},
    "f48_ssat_395_longest_lower_low_sequential_streak_252": {"inputs": ["low"], "func": f48_ssat_395_longest_lower_low_sequential_streak_252},
    "f48_ssat_396_longest_lower_high_sequential_streak_252": {"inputs": ["high"], "func": f48_ssat_396_longest_lower_high_sequential_streak_252},
    "f48_ssat_397_count_3plus_down_streaks_252": {"inputs": ["close"], "func": f48_ssat_397_count_3plus_down_streaks_252},
    "f48_ssat_398_count_5plus_down_streaks_252": {"inputs": ["close"], "func": f48_ssat_398_count_5plus_down_streaks_252},
    "f48_ssat_399_longest_above_sma50_streak_252": {"inputs": ["close"], "func": f48_ssat_399_longest_above_sma50_streak_252},
    "f48_ssat_400_longest_below_sma50_streak_252": {"inputs": ["close"], "func": f48_ssat_400_longest_below_sma50_streak_252},
    "f48_ssat_401_wald_wolfowitz_runs_z_63": {"inputs": ["close"], "func": f48_ssat_401_wald_wolfowitz_runs_z_63},
    "f48_ssat_402_return_sign_autocorr_lag1_63": {"inputs": ["close"], "func": f48_ssat_402_return_sign_autocorr_lag1_63},
    "f48_ssat_403_squared_return_ac_lag1_63": {"inputs": ["close"], "func": f48_ssat_403_squared_return_ac_lag1_63},
    "f48_ssat_404_squared_return_ac_lag5_63": {"inputs": ["close"], "func": f48_ssat_404_squared_return_ac_lag5_63},
    "f48_ssat_405_abs_return_ac_lag1_252": {"inputs": ["close"], "func": f48_ssat_405_abs_return_ac_lag1_252},
    "f48_ssat_406_arch_1_proxy_var_squared_returns_63": {"inputs": ["close"], "func": f48_ssat_406_arch_1_proxy_var_squared_returns_63},
    "f48_ssat_407_garch_persistence_proxy": {"inputs": ["close"], "func": f48_ssat_407_garch_persistence_proxy},
    "f48_ssat_408_vol_of_vol_of_vol_63": {"inputs": ["close"], "func": f48_ssat_408_vol_of_vol_of_vol_63},
    "f48_ssat_409_vol_spike_count_252": {"inputs": ["close"], "func": f48_ssat_409_vol_spike_count_252},
    "f48_ssat_410_vol_spike_count_504": {"inputs": ["close"], "func": f48_ssat_410_vol_spike_count_504},
    "f48_ssat_411_profit_factor_21": {"inputs": ["close"], "func": f48_ssat_411_profit_factor_21},
    "f48_ssat_412_profit_factor_63": {"inputs": ["close"], "func": f48_ssat_412_profit_factor_63},
    "f48_ssat_413_profit_factor_252": {"inputs": ["close"], "func": f48_ssat_413_profit_factor_252},
    "f48_ssat_414_hit_rate_21": {"inputs": ["close"], "func": f48_ssat_414_hit_rate_21},
    "f48_ssat_415_hit_rate_63": {"inputs": ["close"], "func": f48_ssat_415_hit_rate_63},
    "f48_ssat_416_avg_gain_over_avg_loss_252": {"inputs": ["close"], "func": f48_ssat_416_avg_gain_over_avg_loss_252},
    "f48_ssat_417_skew_adjusted_profit_ratio_252": {"inputs": ["close"], "func": f48_ssat_417_skew_adjusted_profit_ratio_252},
    "f48_ssat_418_kelly_fraction_proxy_252": {"inputs": ["close"], "func": f48_ssat_418_kelly_fraction_proxy_252},
    "f48_ssat_419_mean_dd_when_si_rising_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_419_mean_dd_when_si_rising_252},
    "f48_ssat_420_mean_dd_when_si_falling_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_420_mean_dd_when_si_falling_252},
    "f48_ssat_421_max_dd_when_si_above_median_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_421_max_dd_when_si_above_median_252},
    "f48_ssat_422_max_dd_when_si_below_median_252": {"inputs": ["shortinterest", "close"], "func": f48_ssat_422_max_dd_when_si_below_median_252},
    "f48_ssat_423_dd_velocity_at_si_peak_event": {"inputs": ["shortinterest", "close"], "func": f48_ssat_423_dd_velocity_at_si_peak_event},
    "f48_ssat_424_drawdown_then_recovery_count_252": {"inputs": ["close"], "func": f48_ssat_424_drawdown_then_recovery_count_252},
    "f48_ssat_425_bars_since_recovery_attempt_63": {"inputs": ["close"], "func": f48_ssat_425_bars_since_recovery_attempt_63},
    "f48_ssat_426_max_dd_rebound_failure_flag": {"inputs": _HC, "func": f48_ssat_426_max_dd_rebound_failure_flag},
    "f48_ssat_427_trend_strength_21_pct_rank_252": {"inputs": ["close"], "func": f48_ssat_427_trend_strength_21_pct_rank_252},
    "f48_ssat_428_trend_strength_63_pct_rank_252": {"inputs": ["close"], "func": f48_ssat_428_trend_strength_63_pct_rank_252},
    "f48_ssat_429_trend_strength_252_pct_rank_504": {"inputs": ["close"], "func": f48_ssat_429_trend_strength_252_pct_rank_504},
    "f48_ssat_430_multi_horizon_trend_disagreement_count": {"inputs": ["close"], "func": f48_ssat_430_multi_horizon_trend_disagreement_count},
    "f48_ssat_431_trend_slope_21_sign_flip_count_63": {"inputs": ["close"], "func": f48_ssat_431_trend_slope_21_sign_flip_count_63},
    "f48_ssat_432_trend_slope_63_sign_flip_count_252": {"inputs": ["close"], "func": f48_ssat_432_trend_slope_63_sign_flip_count_252},
    "f48_ssat_433_trend_coherence_score": {"inputs": ["close"], "func": f48_ssat_433_trend_coherence_score},
    "f48_ssat_434_trend_of_trend_21d": {"inputs": ["close"], "func": f48_ssat_434_trend_of_trend_21d},
    "f48_ssat_435_composite_bear_pressure_score": {"inputs": ["close"], "func": f48_ssat_435_composite_bear_pressure_score},
    "f48_ssat_436_composite_pre_collapse_score": {"inputs": _HLCV, "func": f48_ssat_436_composite_pre_collapse_score},
    "f48_ssat_437_count_high_vol_down_3sigma_21": {"inputs": _CV, "func": f48_ssat_437_count_high_vol_down_3sigma_21},
    "f48_ssat_438_count_high_vol_down_3sigma_63": {"inputs": _CV, "func": f48_ssat_438_count_high_vol_down_3sigma_63},
    "f48_ssat_439_top3_down_days_vol_share_63": {"inputs": _CV, "func": f48_ssat_439_top3_down_days_vol_share_63},
    "f48_ssat_440_top3_down_days_vol_share_252": {"inputs": _CV, "func": f48_ssat_440_top3_down_days_vol_share_252},
    "f48_ssat_441_mar_ratio_proxy_252": {"inputs": ["close"], "func": f48_ssat_441_mar_ratio_proxy_252},
    "f48_ssat_442_capit_followed_by_lower_low_count_252": {"inputs": _HLCV, "func": f48_ssat_442_capit_followed_by_lower_low_count_252},
    "f48_ssat_443_capit_followed_by_5d_decline_10pct_count_252": {"inputs": _HLCV, "func": f48_ssat_443_capit_followed_by_5d_decline_10pct_count_252},
    "f48_ssat_444_vol_trend_slope_63": {"inputs": ["volume"], "func": f48_ssat_444_vol_trend_slope_63},
    "f48_ssat_445_vol_trend_slope_252": {"inputs": ["volume"], "func": f48_ssat_445_vol_trend_slope_252},
    "f48_ssat_446_vol_cv_63_alt": {"inputs": ["volume"], "func": f48_ssat_446_vol_cv_63_alt},
    "f48_ssat_447_vol_5d_over_63d_mean_ratio": {"inputs": ["volume"], "func": f48_ssat_447_vol_5d_over_63d_mean_ratio},
    "f48_ssat_448_bars_since_volume_252d_max": {"inputs": ["volume"], "func": f48_ssat_448_bars_since_volume_252d_max},
    "f48_ssat_449_count_low_vol_below_half_median_63": {"inputs": ["volume"], "func": f48_ssat_449_count_low_vol_below_half_median_63},
    "f48_ssat_450_count_low_vol_below_half_median_252": {"inputs": ["volume"], "func": f48_ssat_450_count_low_vol_below_half_median_252},
}
