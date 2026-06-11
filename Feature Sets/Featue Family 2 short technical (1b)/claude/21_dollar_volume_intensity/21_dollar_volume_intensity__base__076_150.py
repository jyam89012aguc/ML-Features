"""dollar_volume_intensity base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across base__001_075 and base__076_150. Each feature
encodes a *different concept* in the dollar-volume-intensity theme:
extremes / regime / concentration / dispersion / persistence / divergence —
all in $-volume units (close × volume).

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
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


# ---------------------------- family helpers ----------------------------

def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _dollar_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).astype(float)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rolling_hurst(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 20)
    def _h(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < min_periods:
            return np.nan
        lags = [2, 4, 8, 16, 32]
        lags = [l for l in lags if l < n // 2]
        if len(lags) < 2:
            return np.nan
        tau = []
        for lag in lags:
            d = v[lag:] - v[:-lag]
            sd = d.std()
            if sd <= 0 or not np.isfinite(sd):
                return np.nan
            tau.append(sd)
        try:
            return float(np.polyfit(np.log(lags), np.log(tau), 1)[0])
        except Exception:
            return np.nan
    return s.rolling(window, min_periods=min_periods).apply(_h, raw=True)


def _rolling_dfa_alpha(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 2, 32)
    def _dfa(w):
        v = w[~np.isnan(w)]
        n = v.size
        if n < min_periods:
            return np.nan
        y = np.cumsum(v - v.mean())
        scales = [4, 8, 16, 32, 64]
        scales = [s for s in scales if s <= n // 4]
        if len(scales) < 2:
            return np.nan
        F = []
        for sc in scales:
            nb = n // sc
            if nb < 1:
                return np.nan
            seg = y[: nb * sc].reshape(nb, sc)
            x = np.arange(sc, dtype=float)
            xm = x.mean()
            dx = x - xm
            denom = (dx * dx).sum()
            fluct = []
            for i in range(nb):
                ym = seg[i].mean()
                slope = ((dx * (seg[i] - ym)).sum()) / denom if denom > 0 else 0.0
                resid = seg[i] - (ym + slope * dx)
                fluct.append((resid * resid).mean())
            F.append(np.sqrt(np.mean(fluct)))
        try:
            return float(np.polyfit(np.log(scales), np.log(F), 1)[0])
        except Exception:
            return np.nan
    return s.rolling(window, min_periods=min_periods).apply(_dfa, raw=True)


# ============================================================
# Bucket L — Regime ratios across horizons (076-082)
# ============================================================

def f21_dvit_076_ratio_dv_p90_21d_to_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 90%-quantile dv(21d) to 90%-quantile dv(252d) — recent upper-band vs long upper-band."""
    dv = _dollar_vol(close, volume)
    p21 = _rolling_quantile(dv, MDAYS, 0.90)
    p252 = _rolling_quantile(dv, YDAYS, 0.90)
    return _safe_div(p21, p252)


def f21_dvit_077_ratio_dv_p10_21d_to_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 10%-quantile dv(21d) to 10%-quantile dv(252d) — recent lower-band vs long lower-band."""
    dv = _dollar_vol(close, volume)
    p21 = _rolling_quantile(dv, MDAYS, 0.10)
    p252 = _rolling_quantile(dv, YDAYS, 0.10)
    return _safe_div(p21, p252)


def f21_dvit_078_ratio_dv_iqr_63_to_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of dv IQR(63d) to IQR(252d) — recent dispersion vs long dispersion."""
    dv = _dollar_vol(close, volume)
    iqr63 = _rolling_quantile(dv, QDAYS, 0.75) - _rolling_quantile(dv, QDAYS, 0.25)
    iqr252 = _rolling_quantile(dv, YDAYS, 0.75) - _rolling_quantile(dv, YDAYS, 0.25)
    return _safe_div(iqr63, iqr252)


def f21_dvit_079_ratio_dv_std_logdv_63_to_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of std of log-dv(63d) to std of log-dv(252d) — log-scale dispersion shift."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s63 = ldv.rolling(QDAYS, min_periods=MDAYS).std()
    s252 = ldv.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s63, s252)


def f21_dvit_080_ratio_dv_mean_5y_to_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dv(5y) divided by mean dv(21d) — > 1 = recent regime shrunk vs structural baseline."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    m5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return _safe_div(m5y, m21)


def f21_dvit_081_dv_regime_zshift_252_vs_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-dv mean(252d) z-scored against (mean(5y), std-of-mean over 5y) — regime z-shift."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m252 = ldv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _rolling_zscore(m252, DDAYS_5Y)


def f21_dvit_082_dv_regime_zshift_63_vs_504(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-dv mean(63d) z-scored against (mean and std over 504d) — short regime shift vs biennial."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m63 = ldv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m63, DDAYS_2Y)


# ============================================================
# Bucket M — Conditional on price in top decile (083-090)
# ============================================================

def f21_dvit_083_dv_pct_rank_when_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dv pct rank(252d) on bars when close in top decile of 252d closes — conditional intensity."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_dv = _rolling_pct_rank(dv, YDAYS)
    return pr_dv.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_084_dv_pct_rank_when_close_in_top_5pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dv pct rank(252d) on bars when close in top 5% of 252d closes."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_dv = _rolling_pct_rank(dv, YDAYS)
    return pr_dv.where(pr_c >= 0.95, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_085_dv_pct_rank_when_close_in_top_1pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dv pct rank(252d) on bars when close in top 1% of 252d closes."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    pr_dv = _rolling_pct_rank(dv, YDAYS)
    return pr_dv.where(pr_c >= 0.99, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_086_median_dv_when_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median dollar-volume on top-decile-close bars over trailing 252d."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    return dv.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).median()


def f21_dvit_087_mean_dv_when_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dollar-volume on top-decile-close bars over trailing 252d."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    return dv.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_088_dv_zscore_when_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log-dv z-score(252d) on top-decile-close bars over trailing 252d."""
    dv = _dollar_vol(close, volume)
    z = _rolling_zscore(_safe_log(dv), YDAYS)
    pr_c = _rolling_pct_rank(close, YDAYS)
    return z.where(pr_c >= 0.90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_089_count_dv_extreme_when_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d with close in top decile AND log-dv z(252d) > 2."""
    dv = _dollar_vol(close, volume)
    z = _rolling_zscore(_safe_log(dv), YDAYS)
    pr_c = _rolling_pct_rank(close, YDAYS)
    return ((pr_c >= 0.90) & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_090_dv_pct_rank_when_close_at_252d_high(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dv pct rank(252d) on bars where high equals 252d trailing max."""
    dv = _dollar_vol(close, volume)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pr_dv = _rolling_pct_rank(dv, YDAYS)
    return pr_dv.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket N — Burst events / post-burst dwell (091-098)
# ============================================================

def f21_dvit_091_bars_since_last_3sigma_dv_burst_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last log-dv z(252d) > 3 event, capped at 252."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = (z > 3.0).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f21_dvit_092_bars_since_last_p99_dv_burst_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last dv >= 99%-quantile of trailing 252d, capped at 252."""
    dv = _dollar_vol(close, volume)
    q = _rolling_quantile(dv, YDAYS, 0.99)
    flag = (dv >= q).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f21_dvit_093_post_burst_dv_decay_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dv divided by max dv in trailing 21d — fraction-of-recent-peak."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(dv, rmax)


def f21_dvit_094_post_burst_dv_half_life_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from 63d-trailing-max dv to first bar with dv <= 0.5 * peak, within 63d window."""
    dv = _dollar_vol(close, volume)
    def _hl(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        target = peak / 2.0
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= target:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_hl, raw=True)


def f21_dvit_095_post_burst_close_below_burst_close_indicator_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when a 3-sigma dv burst occurred in past 5d AND close is now below the burst-bar close."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst = z > 3.0
    burst_close = close.where(burst, np.nan).ffill()
    days_since = (~burst).astype(int).groupby(burst.cumsum()).cumsum()
    cond = (days_since <= 5) & (close < burst_close.shift(1))
    return cond.astype(float)


def f21_dvit_096_count_bursts_followed_by_failure_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count bursts (z>3) in trailing 252d that were followed within 21d by close < burst-bar close."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst = z > 3.0
    def _check(idx):
        z_w = z.iloc[idx]; c_w = close.iloc[idx]
        b = burst.iloc[idx]
        n = len(b)
        bpos = np.where(b.values)[0]
        cnt = 0
        for bp in bpos:
            if bp >= n - 1:
                continue
            base = c_w.iloc[bp]
            window_end = min(n, bp + 22)
            seg = c_w.iloc[bp + 1 : window_end].dropna()
            if seg.size == 0:
                continue
            if (seg < base).any():
                cnt += 1
        return float(cnt)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _check(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_097_cum_post_burst_decay_excess_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative (peak_dv - current_dv) sum across days since last 252d-trailing dv peak."""
    dv = _dollar_vol(close, volume)
    def _cd(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak):
            return np.nan
        seg = w[peak_idx + 1 :]
        seg = seg[~np.isnan(seg)]
        if seg.size == 0:
            return 0.0
        return float(np.sum(peak - seg))
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_cd, raw=True)


def f21_dvit_098_burst_amplitude_252d_max_z(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max log-dv z(252d) over trailing 252d — single biggest spike magnitude."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket O — Regime persistence (Hurst / DFA) (099-102)
# ============================================================

def f21_dvit_099_hurst_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent of log dollar-volume over 252d — persistence of intensity regime."""
    return _rolling_hurst(_safe_log(_dollar_vol(close, volume)), YDAYS)


def f21_dvit_100_hurst_log_dv_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling Hurst exponent of log dollar-volume over 504d — long-horizon persistence."""
    return _rolling_hurst(_safe_log(_dollar_vol(close, volume)), DDAYS_2Y)


def f21_dvit_101_dfa_alpha_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Detrended fluctuation analysis alpha exponent of log dollar-volume over 252d."""
    return _rolling_dfa_alpha(_safe_log(_dollar_vol(close, volume)), YDAYS)


def f21_dvit_102_variance_ratio_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Variance-ratio test (Lo & MacKinlay style) — var(log_dv lag-q sums) / (q * var(log_dv lag-1)), q=2, over 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    def _vr(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        q = 2
        v_q = np.array([v[i] + v[i + 1] for i in range(v.size - 1)])
        var1 = np.var(v, ddof=1)
        varq = np.var(v_q, ddof=1)
        if var1 <= 0:
            return np.nan
        return float(varq / (q * var1))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_vr, raw=True)


# ============================================================
# Bucket P — $-vol vs ATR / realized-vol ratios (103-108)
# ============================================================

def f21_dvit_103_dollar_vol_per_atr_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (dollar_vol / ATR21) — $ per unit volatility."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(dv, atr).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_104_dollar_vol_per_atr_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 63d of (dollar_vol / ATR21)."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(dv, atr).rolling(QDAYS, min_periods=MDAYS).mean()


def f21_dvit_105_ratio_dv_per_atr_63_to_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean(dv/ATR21)(63d) to mean(dv/ATR21)(252d) — short-vs-long intensity-per-vol."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(dv, atr)
    return _safe_div(ratio.rolling(QDAYS, min_periods=MDAYS).mean(), ratio.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_106_dollar_vol_per_atr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (dollar_vol / ATR21) over trailing 252d."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _rolling_zscore(_safe_div(dv, atr), YDAYS)


def f21_dvit_107_dollar_vol_per_realized_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (dollar_vol / annualized realized vol from log-returns)."""
    dv = _dollar_vol(close, volume)
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(dv, rv).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_108_dollar_vol_per_realized_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 63d of (dollar_vol / annualized realized vol from log-returns)."""
    dv = _dollar_vol(close, volume)
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(dv, rv).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket Q — $-vol max-drawdown post-peak (109-114)
# ============================================================

def f21_dvit_109_log_dv_drawdown_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log_dv minus 252d trailing max log_dv (drawdown in log-space)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv - ldv.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_110_bars_since_log_dv_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 252d-trailing log_dv maximum."""
    ldv = _safe_log(_dollar_vol(close, volume))
    def _b(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return ldv.rolling(YDAYS, min_periods=QDAYS).apply(_b, raw=True)


def f21_dvit_111_post_peak_dv_recovery_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if current dv has returned to within 10% of 252d trailing peak dv, else 0."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(dv, rmax) >= 0.90).astype(float)


def f21_dvit_112_cum_post_peak_dv_deficit_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative (252d-trailing-max-dv minus current-dv) over trailing 252d — area-under deficit."""
    dv = _dollar_vol(close, volume)
    rmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return (rmax - dv).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_113_dv_drawdown_atr_norm_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(dv minus 252d trailing max dv) divided by ATR21 — ATR-normalized $-vol deficit."""
    dv = _dollar_vol(close, volume)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(dv - dv.rolling(YDAYS, min_periods=QDAYS).max(), atr)


def f21_dvit_114_log_dv_drawdown_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (over 252d) of log-dv drawdown-from-running-max."""
    ldv = _safe_log(_dollar_vol(close, volume))
    dd = ldv - ldv.rolling(YDAYS, min_periods=QDAYS).max()
    return _rolling_zscore(dd, YDAYS)


# ============================================================
# Bucket R — Kurtosis / skew of log-dv (115-120)
# ============================================================

def f21_dvit_115_skew_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of log dollar-volume over 252d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(YDAYS, min_periods=QDAYS).skew()


def f21_dvit_116_kurt_log_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of log dollar-volume over 252d — tail-heaviness."""
    return _safe_log(_dollar_vol(close, volume)).rolling(YDAYS, min_periods=QDAYS).kurt()


def f21_dvit_117_skew_log_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of log dollar-volume over 63d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(QDAYS, min_periods=MDAYS).skew()


def f21_dvit_118_kurt_log_dv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling excess kurtosis of log dollar-volume over 63d."""
    return _safe_log(_dollar_vol(close, volume)).rolling(QDAYS, min_periods=MDAYS).kurt()


def f21_dvit_119_tail_index_log_dv_q99_to_q50_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """99%-quantile divided by 50%-quantile of log-dv over 252d — right-tail concentration."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _safe_div(_rolling_quantile(ldv, YDAYS, 0.99), _rolling_quantile(ldv, YDAYS, 0.50))


def f21_dvit_120_tail_index_log_dv_q01_to_q50_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1%-quantile divided by 50%-quantile of log-dv over 252d — left-tail concentration."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _safe_div(_rolling_quantile(ldv, YDAYS, 0.01), _rolling_quantile(ldv, YDAYS, 0.50))


# ============================================================
# Bucket S — Rank correlation (121-126)
# ============================================================

def f21_dvit_121_spearman_dv_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation between dollar-vol and close over 252d (annual frame)."""
    dv = _dollar_vol(close, volume)
    return dv.rolling(YDAYS, min_periods=QDAYS).rank().rolling(YDAYS, min_periods=QDAYS).corr(close.rolling(YDAYS, min_periods=QDAYS).rank())


def f21_dvit_122_spearman_dv_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman rank correlation between dollar-vol and close over 63d (quarterly frame)."""
    dv = _dollar_vol(close, volume)
    return dv.rolling(QDAYS, min_periods=MDAYS).rank().rolling(QDAYS, min_periods=MDAYS).corr(close.rolling(QDAYS, min_periods=MDAYS).rank())


def f21_dvit_123_kendall_dv_close_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rank-correlation proxy for Kendall's tau: sign(dv-rank diff) * sign(close-rank diff), trailing 252d mean."""
    dv = _dollar_vol(close, volume)
    rdv = dv.rank(method='average')
    rc = close.rank(method='average')
    return (np.sign(rdv.diff()) * np.sign(rc.diff())).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_124_spearman_dv_close_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman correlation of dv-rank vs close-rank computed only on top-decile-close bars in trailing 252d."""
    dv = _dollar_vol(close, volume)
    pr_c = _rolling_pct_rank(close, YDAYS)
    def _sp(idx):
        m = (pr_c.iloc[idx] >= 0.90)
        sub = pd.DataFrame({"dv": dv.iloc[idx], "c": close.iloc[idx]}).loc[m]
        if sub.shape[0] < 10:
            return np.nan
        return float(sub["dv"].rank().corr(sub["c"].rank()))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _sp(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_125_rank_corr_dv_price_change_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman correlation between dv and 5-day log-return over trailing 252d."""
    dv = _dollar_vol(close, volume)
    r5 = _safe_log(close).diff(5)
    return dv.rolling(YDAYS, min_periods=QDAYS).rank().rolling(YDAYS, min_periods=QDAYS).corr(r5.rolling(YDAYS, min_periods=QDAYS).rank())


def f21_dvit_126_rolling_rank_corr_diff_short_long_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spearman(dv, close)(63d) minus Spearman(dv, close)(252d) — coupling-shift."""
    dv = _dollar_vol(close, volume)
    s63 = dv.rolling(QDAYS, min_periods=MDAYS).rank().rolling(QDAYS, min_periods=MDAYS).corr(close.rolling(QDAYS, min_periods=MDAYS).rank())
    s252 = dv.rolling(YDAYS, min_periods=QDAYS).rank().rolling(YDAYS, min_periods=QDAYS).corr(close.rolling(YDAYS, min_periods=QDAYS).rank())
    return s63 - s252


# ============================================================
# Bucket T — Divergence detection (127-132)
# ============================================================

def f21_dvit_127_price_up_dv_down_indicator_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 5d close ROC > 0 AND 5d dv ROC < 0 — short-window divergence flag."""
    dv = _dollar_vol(close, volume)
    pr = _safe_log(close).diff(WDAYS)
    dr = _safe_log(dv).diff(WDAYS)
    return ((pr > 0) & (dr < 0)).astype(float)


def f21_dvit_128_count_price_up_dv_down_bars_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where 5d close ROC > 0 AND 5d dv ROC < 0."""
    dv = _dollar_vol(close, volume)
    pr = _safe_log(close).diff(WDAYS)
    dr = _safe_log(dv).diff(WDAYS)
    flag = ((pr > 0) & (dr < 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_129_ratio_price_up_dv_down_to_price_up_dv_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """In trailing 252d, ratio of (5d-price-up + 5d-dv-down) bars to (5d-price-up + 5d-dv-up) bars — divergence ratio."""
    dv = _dollar_vol(close, volume)
    pr = _safe_log(close).diff(WDAYS)
    dr = _safe_log(dv).diff(WDAYS)
    a = ((pr > 0) & (dr < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    b = ((pr > 0) & (dr > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b + 1.0)


def f21_dvit_130_dv_minus_price_slope_252d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(slope of log-dv, 252d) minus (slope of log-close, 252d) — slope divergence."""
    dv = _dollar_vol(close, volume)
    return _rolling_slope(_safe_log(dv), YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


def f21_dvit_131_residual_logdv_predicted_from_logprice_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d OLS residual: log-dv minus (a + b*log-close), where a/b fit on the window."""
    ldv = _safe_log(_dollar_vol(close, volume))
    lp = _safe_log(close)
    def _res(idx):
        x = lp.iloc[idx]; y = ldv.iloc[idx]
        mask = x.notna() & y.notna()
        if mask.sum() < 30:
            return np.nan
        xv = x[mask].values; yv = y[mask].values
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((xv - xm) * (yv - ym)).sum() / sxx
        a = ym - b * xm
        last_x = x.iloc[-1]; last_y = y.iloc[-1]
        if not (np.isfinite(last_x) and np.isfinite(last_y)):
            return np.nan
        return float(last_y - (a + b * last_x))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_132_dv_failure_to_confirm_high_indicator_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when new 252d high prints with log-dv z(252d) < 0 — failure to confirm with intensity."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((high >= rmax) & (z < 0.0)).astype(float)


# ============================================================
# Bucket U — Composite / other primitives (133-150)
# ============================================================

def f21_dvit_133_dv_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (vs 252d) of daily dv change (dv_t - dv_{t-1})."""
    dv = _dollar_vol(close, volume)
    return _rolling_zscore(dv.diff(), YDAYS)


def f21_dvit_134_cum_log_dv_excess_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 252d of (log_dv - 252d-median-log_dv) — net excess in log-space."""
    ldv = _safe_log(_dollar_vol(close, volume))
    med = ldv.rolling(YDAYS, min_periods=QDAYS).median()
    return (ldv - med).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_135_dv_decile_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Decile score (0-9) of dv pct-rank over trailing 252d — coarse intensity bucket."""
    dv = _dollar_vol(close, volume)
    pr = _rolling_pct_rank(dv, YDAYS)
    return (pr * 10.0).clip(upper=9.999)


def f21_dvit_136_composite_intensity_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of binary intensity indicators: z>2, pct_rank>0.95, dv/median252>3, in-top10-share-of-252."""
    dv = _dollar_vol(close, volume)
    z = _rolling_zscore(_safe_log(dv), YDAYS)
    pr = _rolling_pct_rank(dv, YDAYS)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    q90 = _rolling_quantile(dv, YDAYS, 0.90)
    return ((z > 2.0).astype(float)
            + (pr > 0.95).astype(float)
            + (_safe_div(dv, med) > 3.0).astype(float)
            + (dv >= q90).astype(float))


def f21_dvit_137_log_dv_zscore_diff_252_minus_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-dv z(252d) minus z(5y) — annual extreme vs multi-year baseline."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv, YDAYS) - _rolling_zscore(ldv, DDAYS_5Y)


def f21_dvit_138_log_dv_pct_rank_diff_252_minus_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-dv pct-rank(252d) minus pct-rank(5y) — short-vs-long rank gap."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_pct_rank(ldv, YDAYS) - _rolling_pct_rank(ldv, DDAYS_5Y)


def f21_dvit_139_dv_at_alltime_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close >= expanding max AND log-dv z(252d) > 3 — climax at all-time-high."""
    rmax = close.expanding(min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close >= rmax) & (z > 3.0)).astype(float)


def f21_dvit_140_dv_3sigma_at_new_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when current bar prints new 252d high AND log-dv z(252d) > 3."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((high >= rmax) & (z > 3.0)).astype(float)


def f21_dvit_141_count_3sigma_dv_at_new_high_in_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with (new 252d high AND log-dv z > 3)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((high >= rmax) & (z > 3.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_142_dv_burst_overshoot_252d_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """For bars with z>2 in trailing 252d, mean of (z - 2) — average overshoot beyond typical spike."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    over = (z - 2.0).where(z > 2.0, np.nan)
    return over.rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_143_longest_runs_above_LR_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar run length of dv above 252d trailing average, in trailing 252d."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    streak = _consecutive_true_streak(dv > avg).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_144_longest_runs_below_LR_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar run length of dv below 252d trailing average, in trailing 252d."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    streak = _consecutive_true_streak(dv < avg).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_145_ratio_above_to_below_LR_runs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of (max above-avg run length) to (max below-avg run length) in trailing 252d."""
    dv = _dollar_vol(close, volume)
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    sup = _consecutive_true_streak(dv > avg).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
    sdn = _consecutive_true_streak(dv < avg).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(sup, sdn + 1.0)


def f21_dvit_146_cum_time_above_q90_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv >= 90%-quantile of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q = _rolling_quantile(dv, YDAYS, 0.90)
    return (dv >= q).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_147_cum_time_below_q10_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv <= 10%-quantile of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q = _rolling_quantile(dv, YDAYS, 0.10)
    return (dv <= q).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_148_dv_vol_of_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d standard deviation of the rolling 21d standard deviation of log-dv — vol of vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s21 = ldv.rolling(MDAYS, min_periods=WDAYS).std()
    return s21.rolling(YDAYS, min_periods=QDAYS).std()


def f21_dvit_149_log_dv_range_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-dv 252d-max minus log-dv 252d-min — log-range of intensity."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv.rolling(YDAYS, min_periods=QDAYS).max() - ldv.rolling(YDAYS, min_periods=QDAYS).min()


def f21_dvit_150_composite_climax_intensity_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dummies: dv in top1 of 252, close at 252-high, log-dv z>3, ATR z>2 — total climax index."""
    dv = _dollar_vol(close, volume)
    pr_dv = _rolling_pct_rank(dv, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    z = _rolling_zscore(_safe_log(dv), YDAYS)
    atr = _atr(high, low, close, n=MDAYS)
    zatr = _rolling_zscore(atr, YDAYS)
    return ((pr_dv >= 0.99).astype(float)
            + (high >= rmax).astype(float)
            + (z > 3.0).astype(float)
            + (zatr > 2.0).astype(float))


# ============================================================
#                         REGISTRY 076-150
# ============================================================

DOLLAR_VOLUME_INTENSITY_BASE_REGISTRY_076_150 = {
    "f21_dvit_076_ratio_dv_p90_21d_to_252d": {"inputs": ["close", "volume"], "func": f21_dvit_076_ratio_dv_p90_21d_to_252d},
    "f21_dvit_077_ratio_dv_p10_21d_to_252d": {"inputs": ["close", "volume"], "func": f21_dvit_077_ratio_dv_p10_21d_to_252d},
    "f21_dvit_078_ratio_dv_iqr_63_to_252": {"inputs": ["close", "volume"], "func": f21_dvit_078_ratio_dv_iqr_63_to_252},
    "f21_dvit_079_ratio_dv_std_logdv_63_to_252": {"inputs": ["close", "volume"], "func": f21_dvit_079_ratio_dv_std_logdv_63_to_252},
    "f21_dvit_080_ratio_dv_mean_5y_to_21d": {"inputs": ["close", "volume"], "func": f21_dvit_080_ratio_dv_mean_5y_to_21d},
    "f21_dvit_081_dv_regime_zshift_252_vs_5y": {"inputs": ["close", "volume"], "func": f21_dvit_081_dv_regime_zshift_252_vs_5y},
    "f21_dvit_082_dv_regime_zshift_63_vs_504": {"inputs": ["close", "volume"], "func": f21_dvit_082_dv_regime_zshift_63_vs_504},
    "f21_dvit_083_dv_pct_rank_when_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_083_dv_pct_rank_when_close_in_top_decile_252d},
    "f21_dvit_084_dv_pct_rank_when_close_in_top_5pct_252d": {"inputs": ["close", "volume"], "func": f21_dvit_084_dv_pct_rank_when_close_in_top_5pct_252d},
    "f21_dvit_085_dv_pct_rank_when_close_in_top_1pct_252d": {"inputs": ["close", "volume"], "func": f21_dvit_085_dv_pct_rank_when_close_in_top_1pct_252d},
    "f21_dvit_086_median_dv_when_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_086_median_dv_when_close_in_top_decile_252d},
    "f21_dvit_087_mean_dv_when_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_087_mean_dv_when_close_in_top_decile_252d},
    "f21_dvit_088_dv_zscore_when_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_088_dv_zscore_when_close_in_top_decile_252d},
    "f21_dvit_089_count_dv_extreme_when_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_089_count_dv_extreme_when_close_in_top_decile_252d},
    "f21_dvit_090_dv_pct_rank_when_close_at_252d_high": {"inputs": ["high", "close", "volume"], "func": f21_dvit_090_dv_pct_rank_when_close_at_252d_high},
    "f21_dvit_091_bars_since_last_3sigma_dv_burst_252d": {"inputs": ["close", "volume"], "func": f21_dvit_091_bars_since_last_3sigma_dv_burst_252d},
    "f21_dvit_092_bars_since_last_p99_dv_burst_252d": {"inputs": ["close", "volume"], "func": f21_dvit_092_bars_since_last_p99_dv_burst_252d},
    "f21_dvit_093_post_burst_dv_decay_ratio_21d": {"inputs": ["close", "volume"], "func": f21_dvit_093_post_burst_dv_decay_ratio_21d},
    "f21_dvit_094_post_burst_dv_half_life_63d": {"inputs": ["close", "volume"], "func": f21_dvit_094_post_burst_dv_half_life_63d},
    "f21_dvit_095_post_burst_close_below_burst_close_indicator_5d": {"inputs": ["close", "volume"], "func": f21_dvit_095_post_burst_close_below_burst_close_indicator_5d},
    "f21_dvit_096_count_bursts_followed_by_failure_252d": {"inputs": ["close", "volume"], "func": f21_dvit_096_count_bursts_followed_by_failure_252d},
    "f21_dvit_097_cum_post_burst_decay_excess_252d": {"inputs": ["close", "volume"], "func": f21_dvit_097_cum_post_burst_decay_excess_252d},
    "f21_dvit_098_burst_amplitude_252d_max_z": {"inputs": ["close", "volume"], "func": f21_dvit_098_burst_amplitude_252d_max_z},
    "f21_dvit_099_hurst_log_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_099_hurst_log_dv_252d},
    "f21_dvit_100_hurst_log_dv_504d": {"inputs": ["close", "volume"], "func": f21_dvit_100_hurst_log_dv_504d},
    "f21_dvit_101_dfa_alpha_log_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_101_dfa_alpha_log_dv_252d},
    "f21_dvit_102_variance_ratio_log_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_102_variance_ratio_log_dv_252d},
    "f21_dvit_103_dollar_vol_per_atr_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_103_dollar_vol_per_atr_252d},
    "f21_dvit_104_dollar_vol_per_atr_63d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_104_dollar_vol_per_atr_63d},
    "f21_dvit_105_ratio_dv_per_atr_63_to_252": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_105_ratio_dv_per_atr_63_to_252},
    "f21_dvit_106_dollar_vol_per_atr_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_106_dollar_vol_per_atr_zscore_252d},
    "f21_dvit_107_dollar_vol_per_realized_vol_252d": {"inputs": ["close", "volume"], "func": f21_dvit_107_dollar_vol_per_realized_vol_252d},
    "f21_dvit_108_dollar_vol_per_realized_vol_63d": {"inputs": ["close", "volume"], "func": f21_dvit_108_dollar_vol_per_realized_vol_63d},
    "f21_dvit_109_log_dv_drawdown_252d": {"inputs": ["close", "volume"], "func": f21_dvit_109_log_dv_drawdown_252d},
    "f21_dvit_110_bars_since_log_dv_max_252d": {"inputs": ["close", "volume"], "func": f21_dvit_110_bars_since_log_dv_max_252d},
    "f21_dvit_111_post_peak_dv_recovery_indicator_252d": {"inputs": ["close", "volume"], "func": f21_dvit_111_post_peak_dv_recovery_indicator_252d},
    "f21_dvit_112_cum_post_peak_dv_deficit_252d": {"inputs": ["close", "volume"], "func": f21_dvit_112_cum_post_peak_dv_deficit_252d},
    "f21_dvit_113_dv_drawdown_atr_norm_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_113_dv_drawdown_atr_norm_252d},
    "f21_dvit_114_log_dv_drawdown_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_114_log_dv_drawdown_zscore_252d},
    "f21_dvit_115_skew_log_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_115_skew_log_dv_252d},
    "f21_dvit_116_kurt_log_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_116_kurt_log_dv_252d},
    "f21_dvit_117_skew_log_dv_63d": {"inputs": ["close", "volume"], "func": f21_dvit_117_skew_log_dv_63d},
    "f21_dvit_118_kurt_log_dv_63d": {"inputs": ["close", "volume"], "func": f21_dvit_118_kurt_log_dv_63d},
    "f21_dvit_119_tail_index_log_dv_q99_to_q50_252d": {"inputs": ["close", "volume"], "func": f21_dvit_119_tail_index_log_dv_q99_to_q50_252d},
    "f21_dvit_120_tail_index_log_dv_q01_to_q50_252d": {"inputs": ["close", "volume"], "func": f21_dvit_120_tail_index_log_dv_q01_to_q50_252d},
    "f21_dvit_121_spearman_dv_close_252d": {"inputs": ["close", "volume"], "func": f21_dvit_121_spearman_dv_close_252d},
    "f21_dvit_122_spearman_dv_close_63d": {"inputs": ["close", "volume"], "func": f21_dvit_122_spearman_dv_close_63d},
    "f21_dvit_123_kendall_dv_close_proxy_252d": {"inputs": ["close", "volume"], "func": f21_dvit_123_kendall_dv_close_proxy_252d},
    "f21_dvit_124_spearman_dv_close_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_124_spearman_dv_close_in_top_decile_252d},
    "f21_dvit_125_rank_corr_dv_price_change_252d": {"inputs": ["close", "volume"], "func": f21_dvit_125_rank_corr_dv_price_change_252d},
    "f21_dvit_126_rolling_rank_corr_diff_short_long_252d": {"inputs": ["close", "volume"], "func": f21_dvit_126_rolling_rank_corr_diff_short_long_252d},
    "f21_dvit_127_price_up_dv_down_indicator_5d": {"inputs": ["close", "volume"], "func": f21_dvit_127_price_up_dv_down_indicator_5d},
    "f21_dvit_128_count_price_up_dv_down_bars_63d": {"inputs": ["close", "volume"], "func": f21_dvit_128_count_price_up_dv_down_bars_63d},
    "f21_dvit_129_ratio_price_up_dv_down_to_price_up_dv_up_252d": {"inputs": ["close", "volume"], "func": f21_dvit_129_ratio_price_up_dv_down_to_price_up_dv_up_252d},
    "f21_dvit_130_dv_minus_price_slope_252d_norm": {"inputs": ["close", "volume"], "func": f21_dvit_130_dv_minus_price_slope_252d_norm},
    "f21_dvit_131_residual_logdv_predicted_from_logprice_252d": {"inputs": ["close", "volume"], "func": f21_dvit_131_residual_logdv_predicted_from_logprice_252d},
    "f21_dvit_132_dv_failure_to_confirm_high_indicator_252d": {"inputs": ["high", "close", "volume"], "func": f21_dvit_132_dv_failure_to_confirm_high_indicator_252d},
    "f21_dvit_133_dv_change_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_133_dv_change_zscore_252d},
    "f21_dvit_134_cum_log_dv_excess_252d": {"inputs": ["close", "volume"], "func": f21_dvit_134_cum_log_dv_excess_252d},
    "f21_dvit_135_dv_decile_score_252d": {"inputs": ["close", "volume"], "func": f21_dvit_135_dv_decile_score_252d},
    "f21_dvit_136_composite_intensity_score_252d": {"inputs": ["close", "volume"], "func": f21_dvit_136_composite_intensity_score_252d},
    "f21_dvit_137_log_dv_zscore_diff_252_minus_5y": {"inputs": ["close", "volume"], "func": f21_dvit_137_log_dv_zscore_diff_252_minus_5y},
    "f21_dvit_138_log_dv_pct_rank_diff_252_minus_5y": {"inputs": ["close", "volume"], "func": f21_dvit_138_log_dv_pct_rank_diff_252_minus_5y},
    "f21_dvit_139_dv_at_alltime_high_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_139_dv_at_alltime_high_indicator},
    "f21_dvit_140_dv_3sigma_at_new_252d_high_indicator": {"inputs": ["high", "close", "volume"], "func": f21_dvit_140_dv_3sigma_at_new_252d_high_indicator},
    "f21_dvit_141_count_3sigma_dv_at_new_high_in_252d": {"inputs": ["high", "close", "volume"], "func": f21_dvit_141_count_3sigma_dv_at_new_high_in_252d},
    "f21_dvit_142_dv_burst_overshoot_252d_zscore": {"inputs": ["close", "volume"], "func": f21_dvit_142_dv_burst_overshoot_252d_zscore},
    "f21_dvit_143_longest_runs_above_LR_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_143_longest_runs_above_LR_dv_252d},
    "f21_dvit_144_longest_runs_below_LR_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_144_longest_runs_below_LR_dv_252d},
    "f21_dvit_145_ratio_above_to_below_LR_runs_252d": {"inputs": ["close", "volume"], "func": f21_dvit_145_ratio_above_to_below_LR_runs_252d},
    "f21_dvit_146_cum_time_above_q90_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_146_cum_time_above_q90_dv_252d},
    "f21_dvit_147_cum_time_below_q10_dv_252d": {"inputs": ["close", "volume"], "func": f21_dvit_147_cum_time_below_q10_dv_252d},
    "f21_dvit_148_dv_vol_of_vol_252d": {"inputs": ["close", "volume"], "func": f21_dvit_148_dv_vol_of_vol_252d},
    "f21_dvit_149_log_dv_range_252d": {"inputs": ["close", "volume"], "func": f21_dvit_149_log_dv_range_252d},
    "f21_dvit_150_composite_climax_intensity_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_150_composite_climax_intensity_score_252d},
}
