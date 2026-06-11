"""roc_momentum_family d2 features 226-300 — Pipeline 1b-technical (gap-fill).

Continuation of 151-225. Buckets in this file:
L continued (drawdown-aware: time-since-X% drawdown, ulcer index), 226-235;
M (path-statistic / runs / streak sequence stats), 236-250;
N (cross-horizon coherence: cascade tests, sign-agreement, rank-order), 251-265;
O (time-weighted / exp-weighted / triangular-weighted returns), 266-280;
P (rank-based and robust momentum: Spearman, Mann-Kendall, Hurst-style),
281-295;
Q (closing composites: 52-week-high distance, last-leg-up, dual momentum),
296-300.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


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


# ============================================================
# Bucket L continued — Drawdown-aware momentum (226-235)
# ============================================================

def f31_rcmf_226_ulcer_index_252d_d2(close: pd.Series) -> pd.Series:
    """Ulcer Index over 252d: sqrt(mean of squared % drawdowns-from-peak) — Martin's stress index."""
    n = YDAYS
    def _u(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak) * 100.0
        return float(np.sqrt(np.nanmean(dd ** 2)))
    return (close.rolling(n, min_periods=QDAYS).apply(_u, raw=True)).diff().diff()


def f31_rcmf_227_ulcer_index_504d_d2(close: pd.Series) -> pd.Series:
    """Ulcer Index over 504d — biennial Martin stress index."""
    n = DDAYS_2Y
    def _u(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak) * 100.0
        return float(np.sqrt(np.nanmean(dd ** 2)))
    return (close.rolling(n, min_periods=YDAYS).apply(_u, raw=True)).diff().diff()


def f31_rcmf_228_martin_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """Martin ratio: 252d ROC / Ulcer Index over 252d — return per unit stress."""
    r = close.pct_change(YDAYS)
    n = YDAYS
    def _u(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak) * 100.0
        return float(np.sqrt(np.nanmean(dd ** 2)))
    ulcer = close.rolling(n, min_periods=QDAYS).apply(_u, raw=True)
    return (_safe_div(r, ulcer)).diff().diff()


def f31_rcmf_229_time_since_5pct_drawdown_ended_d2(close: pd.Series) -> pd.Series:
    """Days since last close exceeded its prior 252d running peak by ≥0 after being ≤-5%
    drawdown — bars since last 'recovery completion' from a ≥5% pullback."""
    n = YDAYS
    def _t(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = -np.inf
        was_below = False
        last_recover = -1
        for i, v in enumerate(w):
            if not np.isfinite(v):
                continue
            if v >= peak:
                if was_below:
                    last_recover = i
                peak = v
                was_below = False
            else:
                dd = v / peak - 1.0 if peak > 0 else 0.0
                if dd <= -0.05:
                    was_below = True
        if last_recover < 0:
            return float(len(w) - 1)
        return float(len(w) - 1 - last_recover)
    return (close.rolling(n, min_periods=QDAYS).apply(_t, raw=True)).diff().diff()


def f31_rcmf_230_time_since_10pct_drawdown_ended_d2(close: pd.Series) -> pd.Series:
    """Days since last full recovery from a ≥10% drawdown within trailing 504d."""
    n = DDAYS_2Y
    def _t(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        peak = -np.inf
        was_below = False
        last_recover = -1
        for i, v in enumerate(w):
            if not np.isfinite(v):
                continue
            if v >= peak:
                if was_below:
                    last_recover = i
                peak = v
                was_below = False
            else:
                dd = v / peak - 1.0 if peak > 0 else 0.0
                if dd <= -0.10:
                    was_below = True
        if last_recover < 0:
            return float(len(w) - 1)
        return float(len(w) - 1 - last_recover)
    return (close.rolling(n, min_periods=YDAYS).apply(_t, raw=True)).diff().diff()


def f31_rcmf_231_drawdown_to_peak_ratio_252d_d2(close: pd.Series) -> pd.Series:
    """|MaxDD_252| / (max_252 / min_252 − 1) — fraction of full-range amplitude that is drawdown."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    amplitude = _safe_div(rmax, rmin) - 1.0
    n = YDAYS
    def _md(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nanmin(dd))
    dd = close.rolling(n, min_periods=QDAYS).apply(_md, raw=True).abs()
    return (_safe_div(dd, amplitude)).diff().diff()


def f31_rcmf_232_underwater_amplitude_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of negative drawdown-from-peak values over trailing 252d — total underwater 'area'."""
    n = YDAYS
    def _sa(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nansum(dd))
    return (close.rolling(n, min_periods=QDAYS).apply(_sa, raw=True)).diff().diff()


def f31_rcmf_233_max_underwater_streak_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive run of strictly-below-peak bars within trailing 252d — peak underwater streak."""
    n = YDAYS
    def _ms(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = -np.inf
        run = 0
        best = 0
        for v in w:
            if not np.isfinite(v):
                continue
            if v >= peak:
                peak = v
                run = 0
            else:
                run += 1
                if run > best:
                    best = run
        return float(best)
    return (close.rolling(n, min_periods=QDAYS).apply(_ms, raw=True)).diff().diff()


def f31_rcmf_234_max_drawdown_252d_minus_max_drawdown_1260d_d2(close: pd.Series) -> pd.Series:
    """Max DD over 252d minus max DD over 1260d — recent-vs-historical drawdown anomaly."""
    n1 = YDAYS
    n2 = DDAYS_5Y
    def _md(w, mp):
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nanmin(dd))
    dd1 = close.rolling(n1, min_periods=QDAYS).apply(lambda w: _md(w, QDAYS), raw=True)
    dd2 = close.rolling(n2, min_periods=YDAYS).apply(lambda w: _md(w, YDAYS), raw=True)
    return (dd1 - dd2).diff().diff()


def f31_rcmf_235_recovery_speed_from_max_dd_252d_d2(close: pd.Series) -> pd.Series:
    """(close − trough_252) / bars_since_trough — recovery rate from deepest annual trough."""
    n = YDAYS
    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idx = int(np.nanargmin(w))
        return float(len(w) - 1 - idx)
    bars_since = close.rolling(n, min_periods=QDAYS).apply(_bs, raw=True)
    rmin = close.rolling(n, min_periods=QDAYS).min()
    return (_safe_div(_safe_div(close, rmin) - 1.0, bars_since.replace(0, np.nan))).diff().diff()


# ============================================================
# Bucket M — Path-statistic / runs / streak sequence stats (236-250)
# ============================================================

def f31_rcmf_236_longest_positive_streak_in_63d_d2(close: pd.Series) -> pd.Series:
    """Longest run of consecutive positive 1d returns within trailing 63d."""
    r = close.pct_change(1)
    sign = (r > 0).astype(float).where(r.notna(), np.nan)
    def _ls(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        best = 0; run = 0
        for v in w:
            if not np.isfinite(v):
                run = 0
                continue
            if v > 0:
                run += 1
                if run > best:
                    best = run
            else:
                run = 0
        return float(best)
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_ls, raw=True)).diff().diff()


def f31_rcmf_237_longest_negative_streak_in_63d_d2(close: pd.Series) -> pd.Series:
    """Longest run of consecutive negative 1d returns within trailing 63d."""
    r = close.pct_change(1)
    sign = (r < 0).astype(float).where(r.notna(), np.nan)
    def _ls(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        best = 0; run = 0
        for v in w:
            if not np.isfinite(v):
                run = 0
                continue
            if v > 0:
                run += 1
                if run > best:
                    best = run
            else:
                run = 0
        return float(best)
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_ls, raw=True)).diff().diff()


def f31_rcmf_238_longest_positive_streak_in_252d_d2(close: pd.Series) -> pd.Series:
    """Longest run of consecutive positive 1d returns within trailing 252d."""
    r = close.pct_change(1)
    sign = (r > 0).astype(float).where(r.notna(), np.nan)
    def _ls(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        best = 0; run = 0
        for v in w:
            if not np.isfinite(v):
                run = 0
                continue
            if v > 0:
                run += 1
                if run > best:
                    best = run
            else:
                run = 0
        return float(best)
    return (sign.rolling(YDAYS, min_periods=QDAYS).apply(_ls, raw=True)).diff().diff()


def f31_rcmf_239_count_positive_runs_in_63d_d2(close: pd.Series) -> pd.Series:
    """Number of distinct positive-run clusters in trailing 63d — clustering of up days."""
    r = close.pct_change(1)
    sign = (r > 0).astype(float).where(r.notna(), np.nan)
    def _cr(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        count = 0; in_run = False
        for v in w:
            if not np.isfinite(v):
                in_run = False
                continue
            if v > 0:
                if not in_run:
                    count += 1
                    in_run = True
            else:
                in_run = False
        return float(count)
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_cr, raw=True)).diff().diff()


def f31_rcmf_240_count_negative_runs_in_63d_d2(close: pd.Series) -> pd.Series:
    """Number of distinct negative-run clusters in trailing 63d — clustering of down days."""
    r = close.pct_change(1)
    sign = (r < 0).astype(float).where(r.notna(), np.nan)
    def _cr(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        count = 0; in_run = False
        for v in w:
            if not np.isfinite(v):
                in_run = False
                continue
            if v > 0:
                if not in_run:
                    count += 1
                    in_run = True
            else:
                in_run = False
        return float(count)
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_cr, raw=True)).diff().diff()


def f31_rcmf_241_avg_positive_run_length_63d_d2(close: pd.Series) -> pd.Series:
    """Mean length of positive-run clusters in trailing 63d — average up-day cluster size."""
    r = close.pct_change(1)
    sign = (r > 0).astype(float).where(r.notna(), np.nan)
    def _avg(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        runs = []
        cur = 0
        for v in w:
            if not np.isfinite(v):
                if cur > 0:
                    runs.append(cur); cur = 0
                continue
            if v > 0:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if not runs:
            return 0.0
        return float(np.mean(runs))
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_avg, raw=True)).diff().diff()


def f31_rcmf_242_avg_negative_run_length_63d_d2(close: pd.Series) -> pd.Series:
    """Mean length of negative-run clusters in trailing 63d — average down-day cluster size."""
    r = close.pct_change(1)
    sign = (r < 0).astype(float).where(r.notna(), np.nan)
    def _avg(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        runs = []
        cur = 0
        for v in w:
            if not np.isfinite(v):
                if cur > 0:
                    runs.append(cur); cur = 0
                continue
            if v > 0:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if not runs:
            return 0.0
        return float(np.mean(runs))
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_avg, raw=True)).diff().diff()


def f31_rcmf_243_avg_pos_minus_avg_neg_run_length_63d_d2(close: pd.Series) -> pd.Series:
    """Difference: mean positive-run length − mean negative-run length over 63d — run-asymmetry."""
    r = close.pct_change(1)
    def _avg(w, pos):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        runs = []
        cur = 0
        for v in w:
            if not np.isfinite(v):
                if cur > 0:
                    runs.append(cur); cur = 0
                continue
            cond = (v > 0) if pos else (v < 0)
            if cond:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        if not runs:
            return 0.0
        return float(np.mean(runs))
    raw_r = r.where(r.notna(), np.nan)
    pos_avg = raw_r.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _avg(w, True), raw=True)
    neg_avg = raw_r.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _avg(w, False), raw=True)
    return (pos_avg - neg_avg).diff().diff()


def f31_rcmf_244_runs_test_z_63d_d2(close: pd.Series) -> pd.Series:
    """Wald-Wolfowitz runs-test z statistic on sign of 1d returns over trailing 63d
    — distinguishes trending (few runs) vs mean-reverting (many runs) regime."""
    r = close.pct_change(1)
    sign = np.sign(r).where(r != 0, np.nan)
    def _rz(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        s = w[valid]
        n1 = int((s > 0).sum())
        n2 = int((s < 0).sum())
        n = n1 + n2
        if n1 == 0 or n2 == 0:
            return np.nan
        runs = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                runs += 1
        mean = (2.0 * n1 * n2) / n + 1.0
        var = (2.0 * n1 * n2 * (2.0 * n1 * n2 - n)) / (n * n * (n - 1)) if n > 1 else np.nan
        if not np.isfinite(var) or var <= 0:
            return np.nan
        return (runs - mean) / np.sqrt(var)
    return (sign.rolling(QDAYS, min_periods=MDAYS).apply(_rz, raw=True)).diff().diff()


def f31_rcmf_245_sign_autocorrelation_1d_63d_d2(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of sign(1d return) over trailing 63d — short-term momentum vs reversal."""
    s = np.sign(close.pct_change(1))
    sl = s.shift(1)
    def _ac(w):
        return np.nan if len(w) < 2 else float(np.nan)
    # Vectorized rolling corr is easier:
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(sl)).diff().diff()


def f31_rcmf_246_return_autocorrelation_1d_63d_d2(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of 1d returns over trailing 63d — short-term return persistence."""
    r = close.pct_change(1)
    return (r.rolling(QDAYS, min_periods=MDAYS).corr(r.shift(1))).diff().diff()


def f31_rcmf_247_return_autocorrelation_5d_252d_d2(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of (non-overlapping-ish) 5d returns over 252d — weekly persistence."""
    r = close.pct_change(WDAYS)
    return (r.rolling(YDAYS, min_periods=QDAYS).corr(r.shift(WDAYS))).diff().diff()


def f31_rcmf_248_return_autocorrelation_21d_504d_d2(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of 21d returns over 504d — monthly-return persistence (momentum)."""
    r = close.pct_change(MDAYS)
    return (r.rolling(DDAYS_2Y, min_periods=YDAYS).corr(r.shift(MDAYS))).diff().diff()


def f31_rcmf_249_variance_ratio_lo_mackinlay_2_to_1_d2(close: pd.Series) -> pd.Series:
    """Lo-MacKinlay variance ratio: Var(5d ret)/(5*Var(1d ret)) over 252d. >1 = momentum, <1 = mean-rev."""
    r1 = close.pct_change(1)
    r5 = close.pct_change(WDAYS)
    v1 = r1.rolling(YDAYS, min_periods=QDAYS).var()
    v5 = r5.rolling(YDAYS, min_periods=QDAYS).var()
    return (_safe_div(v5, WDAYS * v1)).diff().diff()


def f31_rcmf_250_variance_ratio_lo_mackinlay_4_to_1_d2(close: pd.Series) -> pd.Series:
    """Variance ratio Var(21d ret)/(21*Var(1d ret)) over 504d — long-horizon momentum vs mean-rev."""
    r1 = close.pct_change(1)
    r21 = close.pct_change(MDAYS)
    v1 = r1.rolling(DDAYS_2Y, min_periods=YDAYS).var()
    v21 = r21.rolling(DDAYS_2Y, min_periods=YDAYS).var()
    return (_safe_div(v21, MDAYS * v1)).diff().diff()


# ============================================================
# Bucket N — Cross-horizon coherence (251-265)
# ============================================================

def f31_rcmf_251_sign_agreement_count_5_horizons_d2(close: pd.Series) -> pd.Series:
    """Number of sign-matches between consecutive horizons in {5,21,63,252,756} — coherence count.
    Counts how many adjacent pairs (in horizon-order) share sign."""
    h = [close.pct_change(WDAYS), close.pct_change(MDAYS), close.pct_change(QDAYS),
         close.pct_change(YDAYS), close.pct_change(DDAYS_3Y)]
    signs = [np.sign(x) for x in h]
    pairs = [(signs[i] == signs[i + 1]).astype(float) for i in range(4)]
    valid = h[0].notna()
    for x in h[1:]:
        valid = valid & x.notna()
    return (sum(pairs).where(valid, np.nan)).diff().diff()


def f31_rcmf_252_strict_bullish_cascade_d2(close: pd.Series) -> pd.Series:
    """Indicator: ret_252 > ret_126 > ret_63 > ret_21 > 0 — strict increasing-momentum cascade."""
    r252 = close.pct_change(YDAYS)
    r126 = close.pct_change(126)
    r63 = close.pct_change(QDAYS)
    r21 = close.pct_change(MDAYS)
    cond = (r252 > r126) & (r126 > r63) & (r63 > r21) & (r21 > 0)
    valid = r252.notna() & r126.notna() & r63.notna() & r21.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f31_rcmf_253_strict_bearish_cascade_d2(close: pd.Series) -> pd.Series:
    """Indicator: ret_252 < ret_126 < ret_63 < ret_21 < 0 — strict decreasing-momentum cascade."""
    r252 = close.pct_change(YDAYS)
    r126 = close.pct_change(126)
    r63 = close.pct_change(QDAYS)
    r21 = close.pct_change(MDAYS)
    cond = (r252 < r126) & (r126 < r63) & (r63 < r21) & (r21 < 0)
    valid = r252.notna() & r126.notna() & r63.notna() & r21.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f31_rcmf_254_inverse_cascade_short_above_long_d2(close: pd.Series) -> pd.Series:
    """Indicator: ret_21 > ret_63 > ret_252 (short-horizon strongest, long weakest) — short-end rally."""
    r252 = close.pct_change(YDAYS)
    r63 = close.pct_change(QDAYS)
    r21 = close.pct_change(MDAYS)
    cond = (r21 > r63) & (r63 > r252)
    valid = r252.notna() & r63.notna() & r21.notna()
    return (cond.astype(float).where(valid, np.nan)).diff().diff()


def f31_rcmf_255_horizon_rank_correlation_with_log_horizon_d2(close: pd.Series) -> pd.Series:
    """Spearman-like rank correlation between {5,21,63,252,756} horizons (in log h) and their ROC values
    — coherence between time-scale and momentum magnitude."""
    h_vals = np.log(np.array([WDAYS, MDAYS, QDAYS, YDAYS, DDAYS_3Y], dtype=float))
    h_ranks = pd.Series(h_vals).rank().values
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
        close.pct_change(DDAYS_3Y).rename("h756"),
    ], axis=1)
    arr = parts.values
    n_rows = arr.shape[0]
    out = np.full(n_rows, np.nan, dtype=float)
    for i in range(n_rows):
        row = arr[i]
        valid = np.isfinite(row)
        if valid.sum() < 3:
            continue
        vr = pd.Series(row[valid]).rank().values
        hr = pd.Series(h_vals[valid]).rank().values
        if len(vr) < 2:
            continue
        c = np.corrcoef(vr, hr)
        if np.isfinite(c[0, 1]):
            out[i] = c[0, 1]
    return (pd.Series(out, index=close.index)).diff().diff()


def f31_rcmf_256_horizon_argmax_dominant_d2(close: pd.Series) -> pd.Series:
    """Index of dominant horizon (argmax) among {21d,63d,252d,756d} — which scale leads."""
    parts = pd.concat([
        close.pct_change(MDAYS).rename(0),
        close.pct_change(QDAYS).rename(1),
        close.pct_change(YDAYS).rename(2),
        close.pct_change(DDAYS_3Y).rename(3),
    ], axis=1)
    any_valid = parts.notna().any(axis=1)
    return (parts.fillna(-np.inf).idxmax(axis=1).where(any_valid, np.nan).astype(float)).diff().diff()


def f31_rcmf_257_horizon_argmin_weakest_d2(close: pd.Series) -> pd.Series:
    """Index of weakest-horizon (argmin) among {21d,63d,252d,756d} — which scale lags."""
    parts = pd.concat([
        close.pct_change(MDAYS).rename(0),
        close.pct_change(QDAYS).rename(1),
        close.pct_change(YDAYS).rename(2),
        close.pct_change(DDAYS_3Y).rename(3),
    ], axis=1)
    any_valid = parts.notna().any(axis=1)
    return (parts.fillna(np.inf).idxmin(axis=1).where(any_valid, np.nan).astype(float)).diff().diff()


def f31_rcmf_258_sign_agreement_count_6_horizons_d2(close: pd.Series) -> pd.Series:
    """Count of positive signs among ROC at {5,21,63,126,252,756} — broader coherence count."""
    horizons = [WDAYS, MDAYS, QDAYS, 126, YDAYS, DDAYS_3Y]
    parts = []
    for h in horizons:
        parts.append((close.pct_change(h) > 0).astype(float))
    s = sum(parts)
    valid = close.pct_change(horizons[0]).notna()
    for h in horizons[1:]:
        valid = valid & close.pct_change(h).notna()
    return (s.where(valid, np.nan)).diff().diff()


def f31_rcmf_259_term_structure_convexity_4_horizons_d2(close: pd.Series) -> pd.Series:
    """0.5*(ROC_5+ROC_252) − ROC_63 — convexity at middle horizon (alt sign vs concavity 090)."""
    return (0.5 * (close.pct_change(WDAYS) + close.pct_change(YDAYS)) - close.pct_change(QDAYS)).diff().diff()


def f31_rcmf_260_consistency_of_sign_252d_d2(close: pd.Series) -> pd.Series:
    """For each bar, fraction of bars in trailing 252d where sign(roc_21) == sign(roc_252) — coherence dwell."""
    s21 = np.sign(close.pct_change(MDAYS))
    s252 = np.sign(close.pct_change(YDAYS))
    match = (s21 == s252).astype(float).where(s21.notna() & s252.notna(), np.nan)
    valid = match.notna().astype(float)
    return (_safe_div(match.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())).diff().diff()


def f31_rcmf_261_sign_agreement_short_vs_long_504d_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 504d where sign(roc_5) == sign(roc_252) — multi-scale coherence dwell."""
    s5 = np.sign(close.pct_change(WDAYS))
    s252 = np.sign(close.pct_change(YDAYS))
    match = (s5 == s252).astype(float).where(s5.notna() & s252.notna(), np.nan)
    valid = match.notna().astype(float)
    return (_safe_div(match.rolling(DDAYS_2Y, min_periods=YDAYS).sum(), valid.rolling(DDAYS_2Y, min_periods=YDAYS).sum())).diff().diff()


def f31_rcmf_262_horizon_dispersion_5_horizons_d2(close: pd.Series) -> pd.Series:
    """Std-dev of ROCs at {5,21,63,252,756} — broader dispersion than 088 (5 horizons not 4)."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
        close.pct_change(DDAYS_3Y).rename("h756"),
    ], axis=1)
    return (parts.std(axis=1)).diff().diff()


def f31_rcmf_263_horizon_range_5_horizons_d2(close: pd.Series) -> pd.Series:
    """Max − min across horizons {5,21,63,252,756} — max-min spread of momentum term-structure."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
        close.pct_change(DDAYS_3Y).rename("h756"),
    ], axis=1)
    return (parts.max(axis=1) - parts.min(axis=1)).diff().diff()


def f31_rcmf_264_horizon_median_ROC_d2(close: pd.Series) -> pd.Series:
    """Median ROC across {5,21,63,252,756} — robust central tendency of momentum term-structure."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
        close.pct_change(DDAYS_3Y).rename("h756"),
    ], axis=1)
    return (parts.median(axis=1)).diff().diff()


def f31_rcmf_265_horizon_iqr_5_horizons_d2(close: pd.Series) -> pd.Series:
    """Interquartile range of ROCs across {5,21,63,252,756} — robust dispersion of term-structure."""
    parts = pd.concat([
        close.pct_change(WDAYS).rename("h5"),
        close.pct_change(MDAYS).rename("h21"),
        close.pct_change(QDAYS).rename("h63"),
        close.pct_change(YDAYS).rename("h252"),
        close.pct_change(DDAYS_3Y).rename("h756"),
    ], axis=1)
    return (parts.quantile(0.75, axis=1) - parts.quantile(0.25, axis=1)).diff().diff()


# ============================================================
# Bucket O — Time-weighted / exp-weighted / triangular-weighted returns (266-280)
# ============================================================

def f31_rcmf_266_linearly_weighted_return_21d_d2(close: pd.Series) -> pd.Series:
    """Linearly time-weighted mean of 1d returns over 21d — recent weighted higher (1..21 weights)."""
    r = close.pct_change(1)
    weights = np.arange(1, MDAYS + 1, dtype=float)
    weights = weights / weights.sum()
    def _w(w):
        valid = ~np.isnan(w)
        if valid.sum() < WDAYS:
            return np.nan
        rw = weights[-len(w):]
        if not valid.all():
            rw = np.where(valid, rw, 0.0)
            denom = rw.sum()
            if denom == 0:
                return np.nan
            rw = rw / denom
            v = np.where(valid, w, 0.0)
            return float((v * rw).sum())
        return float((w * rw).sum())
    return (r.rolling(MDAYS, min_periods=WDAYS).apply(_w, raw=True)).diff().diff()


def f31_rcmf_267_linearly_weighted_return_63d_d2(close: pd.Series) -> pd.Series:
    """Linearly time-weighted mean of 1d returns over 63d — quarterly recent-heavy mean."""
    r = close.pct_change(1)
    weights = np.arange(1, QDAYS + 1, dtype=float)
    weights = weights / weights.sum()
    def _w(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        rw = weights[-len(w):]
        if not valid.all():
            rw = np.where(valid, rw, 0.0)
            denom = rw.sum()
            if denom == 0:
                return np.nan
            rw = rw / denom
            v = np.where(valid, w, 0.0)
            return float((v * rw).sum())
        return float((w * rw).sum())
    return (r.rolling(QDAYS, min_periods=MDAYS).apply(_w, raw=True)).diff().diff()


def f31_rcmf_268_linearly_weighted_return_252d_d2(close: pd.Series) -> pd.Series:
    """Linearly time-weighted mean of 1d returns over 252d — annual recent-heavy mean."""
    r = close.pct_change(1)
    weights = np.arange(1, YDAYS + 1, dtype=float)
    weights = weights / weights.sum()
    def _w(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        rw = weights[-len(w):]
        if not valid.all():
            rw = np.where(valid, rw, 0.0)
            denom = rw.sum()
            if denom == 0:
                return np.nan
            rw = rw / denom
            v = np.where(valid, w, 0.0)
            return float((v * rw).sum())
        return float((w * rw).sum())
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_w, raw=True)).diff().diff()


def f31_rcmf_269_ewma_return_halflife_5d_d2(close: pd.Series) -> pd.Series:
    """EWMA of 1d returns with 5d half-life — short-half-life recent-weighted drift."""
    return (close.pct_change(1).ewm(halflife=WDAYS, min_periods=2, adjust=False).mean()).diff().diff()


def f31_rcmf_270_ewma_return_halflife_21d_d2(close: pd.Series) -> pd.Series:
    """EWMA of 1d returns with 21d half-life — monthly half-life recent-weighted drift."""
    return (close.pct_change(1).ewm(halflife=MDAYS, min_periods=WDAYS, adjust=False).mean()).diff().diff()


def f31_rcmf_271_ewma_return_halflife_63d_d2(close: pd.Series) -> pd.Series:
    """EWMA of 1d returns with 63d half-life — quarterly half-life drift."""
    return (close.pct_change(1).ewm(halflife=QDAYS, min_periods=MDAYS, adjust=False).mean()).diff().diff()


def f31_rcmf_272_ewma_return_halflife_126d_d2(close: pd.Series) -> pd.Series:
    """EWMA of 1d returns with 126d half-life — half-year half-life drift."""
    return (close.pct_change(1).ewm(halflife=126, min_periods=MDAYS, adjust=False).mean()).diff().diff()


def f31_rcmf_273_ewma_return_halflife_252d_d2(close: pd.Series) -> pd.Series:
    """EWMA of 1d returns with 252d half-life — annual half-life slow-drift."""
    return (close.pct_change(1).ewm(halflife=YDAYS, min_periods=QDAYS, adjust=False).mean()).diff().diff()


def f31_rcmf_274_triangular_weighted_return_63d_d2(close: pd.Series) -> pd.Series:
    """Triangular-weighted (peak in middle) mean of 1d returns over 63d — middle weighted highest."""
    r = close.pct_change(1)
    n = QDAYS
    mid = (n - 1) / 2.0
    weights = (n / 2.0) - np.abs(np.arange(n) - mid)
    weights = np.clip(weights, 0, None)
    weights = weights / weights.sum()
    def _w(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        rw = weights[-len(w):]
        if not valid.all():
            rw = np.where(valid, rw, 0.0)
            denom = rw.sum()
            if denom == 0:
                return np.nan
            rw = rw / denom
            v = np.where(valid, w, 0.0)
            return float((v * rw).sum())
        return float((w * rw).sum())
    return (r.rolling(n, min_periods=MDAYS).apply(_w, raw=True)).diff().diff()


def f31_rcmf_275_exp_decay_signed_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of exp(-decay*age) * sign(1d_return) over trailing 252d, decay=ln(2)/63 — recent-signed
    information accumulation in [-sum_weights, +sum_weights] units."""
    r = close.pct_change(1)
    decay = np.log(2) / QDAYS
    n = YDAYS
    weights = np.exp(-decay * np.arange(n - 1, -1, -1))
    def _w(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        rw = weights[-len(w):]
        s = np.where(np.isnan(w), 0.0, np.sign(w))
        return float((s * rw).sum())
    return (r.rolling(n, min_periods=QDAYS).apply(_w, raw=True)).diff().diff()


def f31_rcmf_276_geometric_compound_return_63d_d2(close: pd.Series) -> pd.Series:
    """Geometric compounding: prod(1 + 1d_returns)^(1/63) − 1 over trailing 63d — daily geom mean.
    Distinct from pct_change(63) (which is total) — this is the per-day geometric mean."""
    lr = _safe_log(close).diff(1)
    n = QDAYS
    s = lr.rolling(n, min_periods=MDAYS).sum()
    return (np.exp(_safe_div(s, float(n))) - 1.0).diff().diff()


def f31_rcmf_277_geometric_compound_return_252d_d2(close: pd.Series) -> pd.Series:
    """Per-day geometric mean of returns over trailing 252d — daily geom mean annualized horizon."""
    lr = _safe_log(close).diff(1)
    n = YDAYS
    s = lr.rolling(n, min_periods=QDAYS).sum()
    return (np.exp(_safe_div(s, float(n))) - 1.0).diff().diff()


def f31_rcmf_278_weighted_avg_horizon_signal_strength_d2(close: pd.Series) -> pd.Series:
    """Mean of |ROC_h| / h-weighting over h∈{5,21,63,252} — magnitude per unit time horizon."""
    parts = pd.concat([
        (close.pct_change(WDAYS).abs() / WDAYS).rename("h5"),
        (close.pct_change(MDAYS).abs() / MDAYS).rename("h21"),
        (close.pct_change(QDAYS).abs() / QDAYS).rename("h63"),
        (close.pct_change(YDAYS).abs() / YDAYS).rename("h252"),
    ], axis=1)
    return (parts.mean(axis=1)).diff().diff()


def f31_rcmf_279_ewma_minus_sma_return_63d_d2(close: pd.Series) -> pd.Series:
    """EWMA(1d ret, hl=21) − SMA(1d ret, 63d) — recency premium of returns over equal-weighted mean."""
    r = close.pct_change(1)
    ewma = r.ewm(halflife=MDAYS, min_periods=WDAYS, adjust=False).mean()
    sma = r.rolling(QDAYS, min_periods=MDAYS).mean()
    return (ewma - sma).diff().diff()


def f31_rcmf_280_double_exp_smoothed_return_63d_d2(close: pd.Series) -> pd.Series:
    """Doubly-EWMA-smoothed 1d returns: ewm(ewm(ret,hl=21),hl=21) over trailing series — Holt-like
    trend smoother (denoised drift)."""
    r = close.pct_change(1)
    first = r.ewm(halflife=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return (first.ewm(halflife=MDAYS, min_periods=WDAYS, adjust=False).mean()).diff().diff()


# ============================================================
# Bucket P — Rank-based and robust momentum (281-295)
# ============================================================

def f31_rcmf_281_spearman_rank_corr_price_vs_time_63d_d2(close: pd.Series) -> pd.Series:
    """Spearman rank correlation of (1..N) vs price ranks over trailing 63d — robust trend strength."""
    n = QDAYS
    def _sp(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        v = w[valid]
        if len(v) < 3:
            return np.nan
        x = np.arange(len(w), dtype=float)[valid]
        rx = pd.Series(x).rank().values
        ry = pd.Series(v).rank().values
        c = np.corrcoef(rx, ry)
        return float(c[0, 1]) if np.isfinite(c[0, 1]) else np.nan
    return (close.rolling(n, min_periods=MDAYS).apply(_sp, raw=True)).diff().diff()


def f31_rcmf_282_spearman_rank_corr_price_vs_time_252d_d2(close: pd.Series) -> pd.Series:
    """Spearman rank correlation over 252d — robust annual trend strength."""
    n = YDAYS
    def _sp(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        v = w[valid]
        if len(v) < 3:
            return np.nan
        x = np.arange(len(w), dtype=float)[valid]
        rx = pd.Series(x).rank().values
        ry = pd.Series(v).rank().values
        c = np.corrcoef(rx, ry)
        return float(c[0, 1]) if np.isfinite(c[0, 1]) else np.nan
    return (close.rolling(n, min_periods=QDAYS).apply(_sp, raw=True)).diff().diff()


def f31_rcmf_283_mann_kendall_s_63d_d2(close: pd.Series) -> pd.Series:
    """Mann-Kendall S statistic on close over 63d — robust monotonic-trend indicator."""
    n = QDAYS
    def _mk(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        v = w[valid]
        s = 0
        for i in range(len(v) - 1):
            d = v[i + 1:] - v[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return float(s)
    return (close.rolling(n, min_periods=MDAYS).apply(_mk, raw=True)).diff().diff()


def f31_rcmf_284_mann_kendall_s_normalized_252d_d2(close: pd.Series) -> pd.Series:
    """Mann-Kendall S statistic on close over 252d normalized by n(n-1)/2 to give Kendall tau."""
    n = YDAYS
    def _mk(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < QDAYS:
            return np.nan
        v = w[valid]
        s = 0
        for i in range(len(v) - 1):
            d = v[i + 1:] - v[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        denom = nv * (nv - 1) / 2.0
        return float(s) / denom if denom > 0 else np.nan
    return (close.rolling(n, min_periods=QDAYS).apply(_mk, raw=True)).diff().diff()


def f31_rcmf_285_theil_sen_slope_63d_d2(close: pd.Series) -> pd.Series:
    """Theil-Sen median slope of close vs time over trailing 63d — robust trend slope."""
    n = QDAYS
    def _ts(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        v = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        slopes = []
        for i in range(len(v)):
            dx = x[i + 1:] - x[i]
            dy = v[i + 1:] - v[i]
            mask = dx != 0
            if mask.any():
                slopes.extend((dy[mask] / dx[mask]).tolist())
        if not slopes:
            return np.nan
        return float(np.median(slopes))
    return (close.rolling(n, min_periods=MDAYS).apply(_ts, raw=True)).diff().diff()


def f31_rcmf_286_hurst_proxy_variance_aggregation_252d_d2(close: pd.Series) -> pd.Series:
    """Hurst exponent proxy via variance-aggregation: slope of log(Var(k-day return))/log(k) for
    k in {1,2,5,10,21} over trailing 252d — >0.5 momentum, <0.5 mean-reversion."""
    n = YDAYS
    ks = [1, 2, 5, 10, MDAYS]
    def _hr(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        log_v = []
        log_k = []
        for k in ks:
            if len(w) <= k:
                continue
            rk = w[k:] - w[:-k]
            rk = rk[np.isfinite(rk)]
            if len(rk) < 3:
                continue
            v = float(np.var(rk, ddof=1))
            if v <= 0:
                continue
            log_v.append(np.log(v))
            log_k.append(np.log(k))
        if len(log_k) < 2:
            return np.nan
        log_k = np.asarray(log_k); log_v = np.asarray(log_v)
        xm = log_k.mean(); ym = log_v.mean()
        sxx = ((log_k - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        slope = ((log_k - xm) * (log_v - ym)).sum() / sxx
        return float(slope / 2.0)
    return (_safe_log(close).rolling(n, min_periods=QDAYS).apply(_hr, raw=True)).diff().diff()


def f31_rcmf_287_conditional_roc_given_prior_up_21d_d2(close: pd.Series) -> pd.Series:
    """Mean of 21d ROC values in trailing 252d where prior 21d ROC was positive — conditional momentum
    persistence (return given prior bullish state)."""
    r = close.pct_change(MDAYS)
    cond = (r.shift(MDAYS) > 0).astype(float)
    masked = r.where(cond == 1.0)
    valid = cond.where(cond == 1.0)
    return (_safe_div(masked.rolling(YDAYS, min_periods=QDAYS).sum(),
                     valid.rolling(YDAYS, min_periods=QDAYS).count())).diff().diff()


def f31_rcmf_288_conditional_roc_given_prior_down_21d_d2(close: pd.Series) -> pd.Series:
    """Mean of 21d ROC values in trailing 252d where prior 21d ROC was negative — conditional bounce."""
    r = close.pct_change(MDAYS)
    cond = (r.shift(MDAYS) < 0).astype(float)
    masked = r.where(cond == 1.0)
    valid = cond.where(cond == 1.0)
    return (_safe_div(masked.rolling(YDAYS, min_periods=QDAYS).sum(),
                     valid.rolling(YDAYS, min_periods=QDAYS).count())).diff().diff()


def f31_rcmf_289_tail_mean_top_10pct_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of the top 10% of 1d returns over trailing 252d — upside tail-return magnitude."""
    r = close.pct_change(1)
    def _tm(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        v = w[valid]
        k = max(1, int(np.ceil(len(v) * 0.10)))
        return float(np.mean(np.partition(v, -k)[-k:]))
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_tm, raw=True)).diff().diff()


def f31_rcmf_290_tail_mean_bottom_10pct_returns_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of the bottom 10% of 1d returns over trailing 252d — downside tail-return magnitude."""
    r = close.pct_change(1)
    def _tm(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        v = w[valid]
        k = max(1, int(np.ceil(len(v) * 0.10)))
        return float(np.mean(np.partition(v, k - 1)[:k]))
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_tm, raw=True)).diff().diff()


def f31_rcmf_291_mean_positive_day_return_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of positive-only 1d returns over trailing 252d — typical up-day magnitude."""
    r = close.pct_change(1)
    pos = r.where(r > 0)
    valid = pos.notna().astype(float)
    return (_safe_div(pos.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())).diff().diff()


def f31_rcmf_292_mean_negative_day_return_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of negative-only 1d returns over trailing 252d — typical down-day magnitude."""
    r = close.pct_change(1)
    neg = r.where(r < 0)
    valid = neg.notna().astype(float)
    return (_safe_div(neg.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())).diff().diff()


def f31_rcmf_293_days_since_top_decile_return_252d_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent 1d return at or above the trailing 252d 90th percentile — age
    of last extreme-up-day relative to 252d distribution."""
    r = close.pct_change(1)
    q90 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    flag = (r >= q90) & r.notna() & q90.notna()
    n = YDAYS
    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idxs = np.where(w == 1)[0]
        if len(idxs) == 0:
            return float(len(w))
        return float(len(w) - 1 - idxs[-1])
    return (flag.astype(float).rolling(n, min_periods=QDAYS).apply(_bs, raw=True)).diff().diff()


def f31_rcmf_294_days_since_bottom_decile_return_252d_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent 1d return at or below the trailing 252d 10th percentile."""
    r = close.pct_change(1)
    q10 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    flag = (r <= q10) & r.notna() & q10.notna()
    n = YDAYS
    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idxs = np.where(w == 1)[0]
        if len(idxs) == 0:
            return float(len(w))
        return float(len(w) - 1 - idxs[-1])
    return (flag.astype(float).rolling(n, min_periods=QDAYS).apply(_bs, raw=True)).diff().diff()


def f31_rcmf_295_days_since_99th_percentile_return_756d_d2(close: pd.Series) -> pd.Series:
    """Bars since the most recent 1d return at or above the trailing 756d 99th percentile — age
    of last extreme-up-day relative to 3y distribution."""
    r = close.pct_change(1)
    q99 = r.rolling(DDAYS_3Y, min_periods=YDAYS).quantile(0.99)
    flag = (r >= q99) & r.notna() & q99.notna()
    n = DDAYS_3Y
    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        idxs = np.where(w == 1)[0]
        if len(idxs) == 0:
            return float(len(w))
        return float(len(w) - 1 - idxs[-1])
    return (flag.astype(float).rolling(n, min_periods=YDAYS).apply(_bs, raw=True)).diff().diff()


# ============================================================
# Bucket Q — Closing composites & dual-momentum / 52w-high (296-300)
# ============================================================

def f31_rcmf_296_distance_to_252d_high_pct_d2(close: pd.Series) -> pd.Series:
    """George-Hwang 52-week-high indicator: close / max_252 − 1 — distance to 52w high (≤ 0).
    Distinct from family-01 because here we use close (not high) and family-31's momentum focus."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(close, rmax) - 1.0).diff().diff()


def f31_rcmf_297_antonacci_dual_momentum_indicator_d2(close: pd.Series) -> pd.Series:
    """Antonacci dual momentum: sign(ret_252) * sign(ret_42) — both positive = +1 (dual confirm),
    both negative = +1 (dual confirm), mixed = -1 (disagreement)."""
    s252 = np.sign(close.pct_change(YDAYS))
    s42 = np.sign(close.pct_change(42))
    valid = close.pct_change(YDAYS).notna() & close.pct_change(42).notna()
    return ((s252 * s42).where(valid, np.nan)).diff().diff()


def f31_rcmf_298_faber_above_10mo_ma_x_signed_252d_d2(close: pd.Series) -> pd.Series:
    """Faber 10-month MA tactical: (close > 210d-SMA) indicator × sign(ret_252) — combined trend filter."""
    sma = close.rolling(210, min_periods=63).mean()
    above = (close > sma).astype(float)
    sign252 = np.sign(close.pct_change(YDAYS))
    valid = close.notna() & sma.notna() & close.pct_change(YDAYS).notna()
    return ((above * sign252).where(valid, np.nan)).diff().diff()


def f31_rcmf_299_late_stage_momentum_indicator_d2(close: pd.Series) -> pd.Series:
    """Late-stage momentum: 5d ROC value when 252d ROC > 0.3, else NaN — 'last leg up' fingerprint.
    Captures short-horizon momentum specifically in already-strong-trend regimes."""
    r5 = close.pct_change(WDAYS)
    r252 = close.pct_change(YDAYS)
    return (r5.where(r252 > 0.30, np.nan)).diff().diff()


def f31_rcmf_300_blowoff_pace_acceleration_indicator_d2(close: pd.Series) -> pd.Series:
    """Blowoff-pace: when ret_252 > 0.50, compute ret_21 / ret_252 (ratio of last month to year)
    — fraction of annual gain accruing in the last month during strong-trend regime. Higher = more
    parabolic/late-stage acceleration."""
    r21 = close.pct_change(MDAYS)
    r252 = close.pct_change(YDAYS)
    ratio = _safe_div(r21, r252)
    return (ratio.where(r252 > 0.50, np.nan)).diff().diff()


# ============================================================
#                         REGISTRY 226-300
# ============================================================

ROC_MOMENTUM_FAMILY_D2_REGISTRY_226_300 = {
    "f31_rcmf_226_ulcer_index_252d_d2": {"inputs": ["close"], "func": f31_rcmf_226_ulcer_index_252d_d2},
    "f31_rcmf_227_ulcer_index_504d_d2": {"inputs": ["close"], "func": f31_rcmf_227_ulcer_index_504d_d2},
    "f31_rcmf_228_martin_ratio_252d_d2": {"inputs": ["close"], "func": f31_rcmf_228_martin_ratio_252d_d2},
    "f31_rcmf_229_time_since_5pct_drawdown_ended_d2": {"inputs": ["close"], "func": f31_rcmf_229_time_since_5pct_drawdown_ended_d2},
    "f31_rcmf_230_time_since_10pct_drawdown_ended_d2": {"inputs": ["close"], "func": f31_rcmf_230_time_since_10pct_drawdown_ended_d2},
    "f31_rcmf_231_drawdown_to_peak_ratio_252d_d2": {"inputs": ["close"], "func": f31_rcmf_231_drawdown_to_peak_ratio_252d_d2},
    "f31_rcmf_232_underwater_amplitude_252d_d2": {"inputs": ["close"], "func": f31_rcmf_232_underwater_amplitude_252d_d2},
    "f31_rcmf_233_max_underwater_streak_252d_d2": {"inputs": ["close"], "func": f31_rcmf_233_max_underwater_streak_252d_d2},
    "f31_rcmf_234_max_drawdown_252d_minus_max_drawdown_1260d_d2": {"inputs": ["close"], "func": f31_rcmf_234_max_drawdown_252d_minus_max_drawdown_1260d_d2},
    "f31_rcmf_235_recovery_speed_from_max_dd_252d_d2": {"inputs": ["close"], "func": f31_rcmf_235_recovery_speed_from_max_dd_252d_d2},
    "f31_rcmf_236_longest_positive_streak_in_63d_d2": {"inputs": ["close"], "func": f31_rcmf_236_longest_positive_streak_in_63d_d2},
    "f31_rcmf_237_longest_negative_streak_in_63d_d2": {"inputs": ["close"], "func": f31_rcmf_237_longest_negative_streak_in_63d_d2},
    "f31_rcmf_238_longest_positive_streak_in_252d_d2": {"inputs": ["close"], "func": f31_rcmf_238_longest_positive_streak_in_252d_d2},
    "f31_rcmf_239_count_positive_runs_in_63d_d2": {"inputs": ["close"], "func": f31_rcmf_239_count_positive_runs_in_63d_d2},
    "f31_rcmf_240_count_negative_runs_in_63d_d2": {"inputs": ["close"], "func": f31_rcmf_240_count_negative_runs_in_63d_d2},
    "f31_rcmf_241_avg_positive_run_length_63d_d2": {"inputs": ["close"], "func": f31_rcmf_241_avg_positive_run_length_63d_d2},
    "f31_rcmf_242_avg_negative_run_length_63d_d2": {"inputs": ["close"], "func": f31_rcmf_242_avg_negative_run_length_63d_d2},
    "f31_rcmf_243_avg_pos_minus_avg_neg_run_length_63d_d2": {"inputs": ["close"], "func": f31_rcmf_243_avg_pos_minus_avg_neg_run_length_63d_d2},
    "f31_rcmf_244_runs_test_z_63d_d2": {"inputs": ["close"], "func": f31_rcmf_244_runs_test_z_63d_d2},
    "f31_rcmf_245_sign_autocorrelation_1d_63d_d2": {"inputs": ["close"], "func": f31_rcmf_245_sign_autocorrelation_1d_63d_d2},
    "f31_rcmf_246_return_autocorrelation_1d_63d_d2": {"inputs": ["close"], "func": f31_rcmf_246_return_autocorrelation_1d_63d_d2},
    "f31_rcmf_247_return_autocorrelation_5d_252d_d2": {"inputs": ["close"], "func": f31_rcmf_247_return_autocorrelation_5d_252d_d2},
    "f31_rcmf_248_return_autocorrelation_21d_504d_d2": {"inputs": ["close"], "func": f31_rcmf_248_return_autocorrelation_21d_504d_d2},
    "f31_rcmf_249_variance_ratio_lo_mackinlay_2_to_1_d2": {"inputs": ["close"], "func": f31_rcmf_249_variance_ratio_lo_mackinlay_2_to_1_d2},
    "f31_rcmf_250_variance_ratio_lo_mackinlay_4_to_1_d2": {"inputs": ["close"], "func": f31_rcmf_250_variance_ratio_lo_mackinlay_4_to_1_d2},
    "f31_rcmf_251_sign_agreement_count_5_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_251_sign_agreement_count_5_horizons_d2},
    "f31_rcmf_252_strict_bullish_cascade_d2": {"inputs": ["close"], "func": f31_rcmf_252_strict_bullish_cascade_d2},
    "f31_rcmf_253_strict_bearish_cascade_d2": {"inputs": ["close"], "func": f31_rcmf_253_strict_bearish_cascade_d2},
    "f31_rcmf_254_inverse_cascade_short_above_long_d2": {"inputs": ["close"], "func": f31_rcmf_254_inverse_cascade_short_above_long_d2},
    "f31_rcmf_255_horizon_rank_correlation_with_log_horizon_d2": {"inputs": ["close"], "func": f31_rcmf_255_horizon_rank_correlation_with_log_horizon_d2},
    "f31_rcmf_256_horizon_argmax_dominant_d2": {"inputs": ["close"], "func": f31_rcmf_256_horizon_argmax_dominant_d2},
    "f31_rcmf_257_horizon_argmin_weakest_d2": {"inputs": ["close"], "func": f31_rcmf_257_horizon_argmin_weakest_d2},
    "f31_rcmf_258_sign_agreement_count_6_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_258_sign_agreement_count_6_horizons_d2},
    "f31_rcmf_259_term_structure_convexity_4_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_259_term_structure_convexity_4_horizons_d2},
    "f31_rcmf_260_consistency_of_sign_252d_d2": {"inputs": ["close"], "func": f31_rcmf_260_consistency_of_sign_252d_d2},
    "f31_rcmf_261_sign_agreement_short_vs_long_504d_d2": {"inputs": ["close"], "func": f31_rcmf_261_sign_agreement_short_vs_long_504d_d2},
    "f31_rcmf_262_horizon_dispersion_5_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_262_horizon_dispersion_5_horizons_d2},
    "f31_rcmf_263_horizon_range_5_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_263_horizon_range_5_horizons_d2},
    "f31_rcmf_264_horizon_median_ROC_d2": {"inputs": ["close"], "func": f31_rcmf_264_horizon_median_ROC_d2},
    "f31_rcmf_265_horizon_iqr_5_horizons_d2": {"inputs": ["close"], "func": f31_rcmf_265_horizon_iqr_5_horizons_d2},
    "f31_rcmf_266_linearly_weighted_return_21d_d2": {"inputs": ["close"], "func": f31_rcmf_266_linearly_weighted_return_21d_d2},
    "f31_rcmf_267_linearly_weighted_return_63d_d2": {"inputs": ["close"], "func": f31_rcmf_267_linearly_weighted_return_63d_d2},
    "f31_rcmf_268_linearly_weighted_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_268_linearly_weighted_return_252d_d2},
    "f31_rcmf_269_ewma_return_halflife_5d_d2": {"inputs": ["close"], "func": f31_rcmf_269_ewma_return_halflife_5d_d2},
    "f31_rcmf_270_ewma_return_halflife_21d_d2": {"inputs": ["close"], "func": f31_rcmf_270_ewma_return_halflife_21d_d2},
    "f31_rcmf_271_ewma_return_halflife_63d_d2": {"inputs": ["close"], "func": f31_rcmf_271_ewma_return_halflife_63d_d2},
    "f31_rcmf_272_ewma_return_halflife_126d_d2": {"inputs": ["close"], "func": f31_rcmf_272_ewma_return_halflife_126d_d2},
    "f31_rcmf_273_ewma_return_halflife_252d_d2": {"inputs": ["close"], "func": f31_rcmf_273_ewma_return_halflife_252d_d2},
    "f31_rcmf_274_triangular_weighted_return_63d_d2": {"inputs": ["close"], "func": f31_rcmf_274_triangular_weighted_return_63d_d2},
    "f31_rcmf_275_exp_decay_signed_252d_d2": {"inputs": ["close"], "func": f31_rcmf_275_exp_decay_signed_252d_d2},
    "f31_rcmf_276_geometric_compound_return_63d_d2": {"inputs": ["close"], "func": f31_rcmf_276_geometric_compound_return_63d_d2},
    "f31_rcmf_277_geometric_compound_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_277_geometric_compound_return_252d_d2},
    "f31_rcmf_278_weighted_avg_horizon_signal_strength_d2": {"inputs": ["close"], "func": f31_rcmf_278_weighted_avg_horizon_signal_strength_d2},
    "f31_rcmf_279_ewma_minus_sma_return_63d_d2": {"inputs": ["close"], "func": f31_rcmf_279_ewma_minus_sma_return_63d_d2},
    "f31_rcmf_280_double_exp_smoothed_return_63d_d2": {"inputs": ["close"], "func": f31_rcmf_280_double_exp_smoothed_return_63d_d2},
    "f31_rcmf_281_spearman_rank_corr_price_vs_time_63d_d2": {"inputs": ["close"], "func": f31_rcmf_281_spearman_rank_corr_price_vs_time_63d_d2},
    "f31_rcmf_282_spearman_rank_corr_price_vs_time_252d_d2": {"inputs": ["close"], "func": f31_rcmf_282_spearman_rank_corr_price_vs_time_252d_d2},
    "f31_rcmf_283_mann_kendall_s_63d_d2": {"inputs": ["close"], "func": f31_rcmf_283_mann_kendall_s_63d_d2},
    "f31_rcmf_284_mann_kendall_s_normalized_252d_d2": {"inputs": ["close"], "func": f31_rcmf_284_mann_kendall_s_normalized_252d_d2},
    "f31_rcmf_285_theil_sen_slope_63d_d2": {"inputs": ["close"], "func": f31_rcmf_285_theil_sen_slope_63d_d2},
    "f31_rcmf_286_hurst_proxy_variance_aggregation_252d_d2": {"inputs": ["close"], "func": f31_rcmf_286_hurst_proxy_variance_aggregation_252d_d2},
    "f31_rcmf_287_conditional_roc_given_prior_up_21d_d2": {"inputs": ["close"], "func": f31_rcmf_287_conditional_roc_given_prior_up_21d_d2},
    "f31_rcmf_288_conditional_roc_given_prior_down_21d_d2": {"inputs": ["close"], "func": f31_rcmf_288_conditional_roc_given_prior_down_21d_d2},
    "f31_rcmf_289_tail_mean_top_10pct_returns_252d_d2": {"inputs": ["close"], "func": f31_rcmf_289_tail_mean_top_10pct_returns_252d_d2},
    "f31_rcmf_290_tail_mean_bottom_10pct_returns_252d_d2": {"inputs": ["close"], "func": f31_rcmf_290_tail_mean_bottom_10pct_returns_252d_d2},
    "f31_rcmf_291_mean_positive_day_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_291_mean_positive_day_return_252d_d2},
    "f31_rcmf_292_mean_negative_day_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_292_mean_negative_day_return_252d_d2},
    "f31_rcmf_293_days_since_top_decile_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_293_days_since_top_decile_return_252d_d2},
    "f31_rcmf_294_days_since_bottom_decile_return_252d_d2": {"inputs": ["close"], "func": f31_rcmf_294_days_since_bottom_decile_return_252d_d2},
    "f31_rcmf_295_days_since_99th_percentile_return_756d_d2": {"inputs": ["close"], "func": f31_rcmf_295_days_since_99th_percentile_return_756d_d2},
    "f31_rcmf_296_distance_to_252d_high_pct_d2": {"inputs": ["close"], "func": f31_rcmf_296_distance_to_252d_high_pct_d2},
    "f31_rcmf_297_antonacci_dual_momentum_indicator_d2": {"inputs": ["close"], "func": f31_rcmf_297_antonacci_dual_momentum_indicator_d2},
    "f31_rcmf_298_faber_above_10mo_ma_x_signed_252d_d2": {"inputs": ["close"], "func": f31_rcmf_298_faber_above_10mo_ma_x_signed_252d_d2},
    "f31_rcmf_299_late_stage_momentum_indicator_d2": {"inputs": ["close"], "func": f31_rcmf_299_late_stage_momentum_indicator_d2},
    "f31_rcmf_300_blowoff_pace_acceleration_indicator_d2": {"inputs": ["close"], "func": f31_rcmf_300_blowoff_pace_acceleration_indicator_d2},
}