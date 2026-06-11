"""dollar_volume_intensity d3 features 151-225 — Pipeline 1b-technical (extension).

Gapless extension building on 001-150. New buckets identified via literature review:
- Pastor-Stambaugh-style $-vol-return covariance + liquidity beta proxy
- Regime-switching detection via Hidden-Markov-Model thresholds + transition counts
- Hawkes-style self-exciting $-vol cluster intensity & decay
- Jump detection (Lee-Mykland, Barndorff-Nielsen-Shephard) applied to log-$-vol
- Overnight-shock $-vol signature (close-to-open + volume)
- Liquidity dry-up early warning composite signals
- VPT (Price-Volume-Trend) cumulative — distinct from OBV/CMF/AD/Klinger

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

def _dollar_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (close * volume).astype(float)


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


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


# ============================================================
# Bucket L — Pastor-Stambaugh style $-vol-return relationship (151-160)
# ============================================================

def f21_dvit_151_dv_return_signed_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pastor-Stambaugh-style: signed_dollar_volume = sign(log_return) * log(1 + dollar_volume). Used for liquidity-beta calc."""
    dv = _dollar_vol(close, volume)
    r = _safe_log(close).diff()
    sv = np.sign(r) * np.log1p(dv)
    return sv


def f21_dvit_152_dv_pastor_stambaugh_gamma_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pastor-Stambaugh gamma (63d): coef of next-day-return on (signed log-$-vol) — PIT-safe via lagged regressor."""
    dv = _dollar_vol(close, volume)
    r = _safe_log(close).diff()
    sv_lag = (np.sign(r.shift(1)) * np.log1p(dv.shift(1)))
    def _g(idx):
        x = sv_lag.iloc[idx].values; y = r.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 20:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        return float(((xv - xm) * (yv - ym)).sum() / sxx)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS, n):
        out.iloc[i] = _g(range(i - QDAYS + 1, i + 1))
    return out


def f21_dvit_153_dv_pastor_stambaugh_gamma_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pastor-Stambaugh gamma (252d): annual liquidity-reversal coefficient."""
    dv = _dollar_vol(close, volume)
    r = _safe_log(close).diff()
    sv_lag = (np.sign(r.shift(1)) * np.log1p(dv.shift(1)))
    def _g(idx):
        x = sv_lag.iloc[idx].values; y = r.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 30:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        return float(((xv - xm) * (yv - ym)).sum() / sxx)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS, n):
        out.iloc[i] = _g(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_154_dv_return_covariance_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d covariance between log-$-vol and log-return — flow-return coupling."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    return ldv.rolling(YDAYS, min_periods=QDAYS).cov(r)


def f21_dvit_155_dv_volatility_per_unit_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of log-$-vol(63d) / std of log-return(63d) — vol-of-flow per vol-of-return."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    return _safe_div(ldv.rolling(QDAYS, min_periods=MDAYS).std(), r.rolling(QDAYS, min_periods=MDAYS).std())


def f21_dvit_156_dv_vs_return_beta_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Beta of log-$-vol on log-return over 252d (OLS slope) — flow-return sensitivity."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    def _b(idx):
        x = r.iloc[idx].values; y = ldv.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 30:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        return float(((xv - xm) * (yv - ym)).sum() / sxx)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _b(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_157_dv_idiosyncratic_return_residual_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of residual from regression of log-return on log-$-vol — unexpected return given flow."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    def _res(idx):
        x = ldv.iloc[idx].values; y = r.iloc[idx].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 30:
            return np.nan
        xv = x[mask]; yv = y[mask]
        xm = xv.mean(); ym = yv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((xv - xm) * (yv - ym)).sum() / sxx
        a = ym - b * xm
        last_x = x[-1]; last_y = y[-1]
        if np.isnan(last_x) or np.isnan(last_y):
            return np.nan
        return float(last_y - (a + b * last_x))
    res = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        res.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return _rolling_zscore(res, YDAYS)


def f21_dvit_158_dv_return_sign_disagreement_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where sign($-vol change) != sign(return) — flow-return disagreement."""
    dv = _dollar_vol(close, volume)
    dv_chg = dv.diff()
    r = close.diff()
    return (np.sign(dv_chg) != np.sign(r)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_159_dv_return_sign_agreement_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars where sign(log-$-vol change) == sign(log-return) — flow-return coupling rate."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    return (np.sign(ldv.diff()) == np.sign(r)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_160_dv_per_return_amplitude_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (|$-vol z(252d)|) / (|log-return z(252d)|) — flow amplitude per return amplitude."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = _safe_log(close).diff()
    return _safe_div(_rolling_zscore(ldv, YDAYS).abs(), _rolling_zscore(r, YDAYS).abs()).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket M — Regime-switching: HMM proxy via z-thresholds (161-170)
# ============================================================

def f21_dvit_161_dv_regime_label_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3-state regime label from z-score(log_dv, 252d): -1 (low, z<-0.5), 0 (mid), +1 (high, z>0.5)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0))


def f21_dvit_162_dv_regime_transitions_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of regime transitions (label changes)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    trans = (label != label.shift(1)).astype(float)
    return trans.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_163_dv_high_regime_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in high-$-vol regime (z>0.5)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_164_dv_low_regime_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in low-$-vol regime (z<-0.5)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_165_dv_regime_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean run length of current $-vol regime label over trailing 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    runs = (label != label.shift(1)).cumsum()
    def _mean_run(idx):
        v = runs.iloc[idx]
        return float(len(idx) / max(v.iloc[-1] - v.iloc[0] + 1, 1))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _mean_run(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_166_dv_high_to_low_regime_transition_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of high→low regime transitions."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    trans = ((label.shift(1) == 1) & (label == -1)).astype(float)
    return trans.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_167_dv_low_to_high_regime_transition_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of low→high regime transitions."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    trans = ((label.shift(1) == -1) & (label == 1)).astype(float)
    return trans.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_168_dv_regime_entropy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of regime-label distribution over trailing 252d. High = labels diverse; low = single regime dominates."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    def _ent(idx):
        v = label.iloc[idx].dropna().values
        if v.size < 30:
            return np.nan
        n = v.size
        p = np.array([np.mean(v == -1), np.mean(v == 0), np.mean(v == 1)])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _ent(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_169_dv_regime_current_label(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current regime label (-1 low / 0 mid / +1 high) for inclusion as ordinal feature."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0))


def f21_dvit_170_dv_regime_current_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in current regime — staleness of current state."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = (label != label.shift(1))
    grp = diff.cumsum()
    return label.groupby(grp).cumcount().astype(float)


# ============================================================
# Bucket N — Hawkes-style self-exciting $-vol cluster intensity (171-180)
# ============================================================

def f21_dvit_171_hawkes_dv_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes-style intensity: EMA(21) of positive $-vol shocks (dv - 84d-mean)+."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    return shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()


def f21_dvit_172_hawkes_dv_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes-style intensity: EMA(63) of positive $-vol shocks."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(QDAYS * 4, min_periods=QDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    return shock.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f21_dvit_173_hawkes_dv_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes-style intensity: EMA(252) of positive $-vol shocks."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    return shock.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()


def f21_dvit_174_hawkes_dv_decay_ratio_21_to_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes intensity ratio: span-21 / span-63 — short-cluster vs medium intensity."""
    dv = _dollar_vol(close, volume)
    base_m = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock_m = (dv - base_m).clip(lower=0.0)
    base_q = dv.rolling(QDAYS * 4, min_periods=QDAYS).mean()
    shock_q = (dv - base_q).clip(lower=0.0)
    return _safe_div(
        shock_m.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean(),
        shock_q.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean(),
    )


def f21_dvit_175_hawkes_dv_intensity_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of Hawkes-style 21d $-vol intensity."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    return _rolling_zscore(shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean(), YDAYS)


def f21_dvit_176_hawkes_dv_cluster_count_above_3sigma_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where Hawkes intensity z(252d) > 3."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    inten = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    z = _rolling_zscore(inten, YDAYS)
    return (z > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_177_hawkes_dv_branching_ratio_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Branching-ratio proxy: var(EMA21 shock series) / mean(shock series) — > 1 = clustering."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    inten = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _safe_div(
        inten.rolling(YDAYS, min_periods=QDAYS).var(),
        inten.rolling(YDAYS, min_periods=QDAYS).mean(),
    )


def f21_dvit_178_hawkes_dv_silence_bars_since_intensity_p90(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since Hawkes intensity last exceeded its 252d 90%-quantile."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    inten = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    q = _rolling_quantile(inten, YDAYS, 0.90)
    flag = (inten > q).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f21_dvit_179_hawkes_dv_intensity_drawdown_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes-21d intensity minus 252d trailing max — cluster decay magnitude."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    inten = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return inten - inten.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_180_hawkes_dv_intensity_ratio_to_baseline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hawkes-21d intensity / mean-of-Hawkes-intensity(252d) — normalized cluster intensity."""
    dv = _dollar_vol(close, volume)
    base = dv.rolling(MDAYS * 4, min_periods=MDAYS).mean()
    shock = (dv - base).clip(lower=0.0)
    inten = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _safe_div(inten, inten.rolling(YDAYS, min_periods=QDAYS).mean())


# ============================================================
# Bucket O — Jump detection on log-$-vol (181-190)
# ============================================================

def f21_dvit_181_lee_mykland_jump_stat_logdv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lee-Mykland statistic on log-$-vol returns over 21d: |r_t| / sqrt(local bipower variation)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    return _safe_div(r.abs(), sigma)


def f21_dvit_182_lee_mykland_jump_count_above_4_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where Lee-Mykland jump stat > 4 — strong jump events."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    return (jstat > 4.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_183_lee_mykland_jump_count_above_3_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where Lee-Mykland jump stat > 3."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    return (jstat > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_184_bnstest_jump_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Barndorff-Nielsen-Shephard test proxy: (RV - BV) / RV where RV = realized var(log_dv returns)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    bv = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    return _safe_div(rv - bv, rv)


def f21_dvit_185_bnstest_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of BNS jump-component-to-RV ratio."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    rv = (r ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    bv = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    ratio = _safe_div(rv - bv, rv)
    return _rolling_zscore(ratio, YDAYS)


def f21_dvit_186_jump_intensity_cum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (Lee-Mykland jump stat)+ — cumulative jump magnitude."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    return jstat.clip(lower=0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_187_jump_clustering_iat_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean inter-arrival time of LM-jump events (stat>3) in trailing 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    def _miat(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return float(v.size)
        return float(np.mean(np.diff(pos)))
    return jstat.rolling(YDAYS, min_periods=QDAYS).apply(_miat, raw=True)


def f21_dvit_188_signed_jump_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d signed jump sum: sum of sign(log_dv return) * |LM stat| only on jump bars (>3)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    signed = np.sign(r) * jstat
    return signed.where(jstat > 3.0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_189_positive_jump_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of positive log-$-vol jumps (LM stat > 3 AND r > 0)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    return ((jstat > 3.0) & (r > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_190_negative_jump_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of negative log-$-vol jumps (LM stat > 3 AND r < 0)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    bp = (r.abs() * r.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(r.abs(), sigma)
    return ((jstat > 3.0) & (r < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket P — Overnight $-vol shock signature (191-200)
# ============================================================

def f21_dvit_191_overnight_dv_shock_zscore_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (|log(open/prev_close)| × log(1 + dollar_volume)) — overnight $-shock proxy."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    dv = _dollar_vol(close, volume)
    shock = overnight * np.log1p(dv)
    return _rolling_zscore(shock, YDAYS)


def f21_dvit_192_overnight_dv_shock_count_above_3_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where overnight $-shock z > 3."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    dv = _dollar_vol(close, volume)
    shock = overnight * np.log1p(dv)
    z = _rolling_zscore(shock, YDAYS)
    return (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_193_overnight_dv_to_intraday_dv_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d mean of (|gap| / |intraday_close_open|) — overnight share of price action."""
    gap = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    intra = (_safe_log(close) - _safe_log(open)).abs()
    return _safe_div(gap, intra).rolling(MDAYS, min_periods=WDAYS).mean()


def f21_dvit_194_overnight_gap_signed_dv_sum_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of sign(open - prev_close) × dollar_volume — net overnight signed flow."""
    gap_sign = np.sign(open - close.shift(1)).fillna(0.0)
    dv = _dollar_vol(close, volume)
    return (gap_sign * dv).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_195_overnight_negative_gap_dv_count_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (open < 0.99 * prev_close AND $-vol z(252d) > 2)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    gap_down = open < 0.99 * close.shift(1)
    return (gap_down & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_196_overnight_positive_gap_dv_count_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (open > 1.01 * prev_close AND $-vol z(252d) > 2)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    gap_up = open > 1.01 * close.shift(1)
    return (gap_up & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_197_overnight_dv_shock_at_high_only_count_252d(open: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of overnight $-vol shocks (z>3) gated to bars where high is at 252d max."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    dv = _dollar_vol(close, volume)
    shock = overnight * np.log1p(dv)
    z = _rolling_zscore(shock, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((z > 3.0) & (high >= rmax)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_198_overnight_gap_z_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score(252d) of log overnight return (|log(open/prev_close)|)."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    return _rolling_zscore(overnight, YDAYS)


def f21_dvit_199_max_overnight_dv_shock_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max overnight $-shock z(252d) observed in trailing 252d — single-event max signature."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    dv = _dollar_vol(close, volume)
    shock = overnight * np.log1p(dv)
    z = _rolling_zscore(shock, YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_200_bars_since_last_overnight_dv_shock(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last overnight $-vol shock with z > 3."""
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    dv = _dollar_vol(close, volume)
    shock = overnight * np.log1p(dv)
    z = _rolling_zscore(shock, YDAYS)
    flag = (z > 3.0).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


# ============================================================
# Bucket Q — Liquidity dry-up early warning composites (201-210)
# ============================================================

def f21_dvit_201_dv_dryup_composite_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: sum of (z(log_dv,252d) < -1) + (HL spread > 252d q75) + (Amihud > 252d q75)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    hl_spread = (high - low) / close
    sp_q75 = _rolling_quantile(hl_spread, YDAYS, 0.75)
    dv = _dollar_vol(close, volume)
    amihud = _safe_div(close.pct_change().abs(), dv)
    am_q75 = _rolling_quantile(amihud, YDAYS, 0.75)
    return ((z < -1.0).astype(float)
            + (hl_spread > sp_q75).astype(float)
            + (amihud > am_q75).astype(float))


def f21_dvit_202_dv_dryup_composite_streak(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where composite dryup score >= 2."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    hl_spread = (high - low) / close
    sp_q75 = _rolling_quantile(hl_spread, YDAYS, 0.75)
    dv = _dollar_vol(close, volume)
    amihud = _safe_div(close.pct_change().abs(), dv)
    am_q75 = _rolling_quantile(amihud, YDAYS, 0.75)
    score = ((z < -1.0).astype(float)
             + (hl_spread > sp_q75).astype(float)
             + (amihud > am_q75).astype(float))
    return _consecutive_true_streak(score >= 2).astype(float)


def f21_dvit_203_dv_dryup_composite_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where composite dryup score >= 2."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    hl_spread = (high - low) / close
    sp_q75 = _rolling_quantile(hl_spread, YDAYS, 0.75)
    dv = _dollar_vol(close, volume)
    amihud = _safe_div(close.pct_change().abs(), dv)
    am_q75 = _rolling_quantile(amihud, YDAYS, 0.75)
    score = ((z < -1.0).astype(float)
             + (hl_spread > sp_q75).astype(float)
             + (amihud > am_q75).astype(float))
    return (score >= 2).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_204_dv_oscillation_amplitude_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of (log_dv - 21d EMA log_dv) over 63d — oscillation amplitude (volatility-of-flow proxy)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    detrend = ldv - ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return detrend.rolling(QDAYS, min_periods=MDAYS).std()


def f21_dvit_205_dv_dryup_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in low-$-vol regime (z<-0.5) — persistence of dryup state."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_206_dv_silence_during_pullback_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where close < 21d-EMA close AND log-dv z(252d) < -1 — silent pullback."""
    ema21c = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close < ema21c) & (z < -1.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_207_dv_active_to_silent_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(count bars with z>1) / (count bars with z<-1), trailing 252d — active vs silent count ratio."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    act = (z > 1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    sil = (z < -1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(act, sil + 1.0)


def f21_dvit_208_dv_compression_indicator_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when std of log-$-vol(21d) is in bottom decile of trailing 252d 21d-stds."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s21 = ldv.rolling(MDAYS, min_periods=WDAYS).std()
    pr = _rolling_pct_rank(s21, YDAYS)
    return (pr <= 0.10).astype(float)


def f21_dvit_209_dv_compression_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars where 21d-std of log-$-vol is in bottom decile of trailing 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s21 = ldv.rolling(MDAYS, min_periods=WDAYS).std()
    pr = _rolling_pct_rank(s21, YDAYS)
    return (pr <= 0.10).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_210_dv_dryup_early_warning_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master early-warning score: sum of {composite-dryup-score(t) + composite-count-trailing-21d > 5}."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    hl_spread = (high - low) / close
    sp_q75 = _rolling_quantile(hl_spread, YDAYS, 0.75)
    dv = _dollar_vol(close, volume)
    amihud = _safe_div(close.pct_change().abs(), dv)
    am_q75 = _rolling_quantile(amihud, YDAYS, 0.75)
    score = ((z < -1.0).astype(float)
             + (hl_spread > sp_q75).astype(float)
             + (amihud > am_q75).astype(float))
    cnt21 = (score >= 2).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return score + (cnt21 > 5).astype(float)


# ============================================================
# Bucket R — VPT (Price Volume Trend) cumulative — distinct from OBV/CMF/AD (211-220)
# ============================================================

def _vpt(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price Volume Trend: cumulative sum of (pct_change × volume)."""
    return (close.pct_change().fillna(0.0) * volume).cumsum()


def f21_dvit_211_vpt_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of VPT over 63d — pct-change-weighted cumulative-flow trend."""
    return _rolling_slope(_vpt(close, volume), QDAYS)


def f21_dvit_212_vpt_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of VPT over 252d — annual cumulative-flow trend."""
    return _rolling_slope(_vpt(close, volume), YDAYS)


def f21_dvit_213_vpt_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of VPT level."""
    return _rolling_zscore(_vpt(close, volume), YDAYS)


def f21_dvit_214_vpt_minus_price_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPT slope(252d) minus log-price slope(252d) — VPT-price divergence."""
    return _rolling_slope(_vpt(close, volume), YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


def f21_dvit_215_vpt_drawdown_from_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPT minus 252d-trailing-max VPT — cumulative-flow drawdown."""
    vpt = _vpt(close, volume)
    return vpt - vpt.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_216_vpt_age_of_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 252d-trailing VPT maximum."""
    vpt = _vpt(close, volume)
    def _a(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return vpt.rolling(YDAYS, min_periods=QDAYS).apply(_a, raw=True)


def f21_dvit_217_vpt_diff_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily VPT change (pct_change × volume) — flow-impulse magnitude."""
    return _rolling_zscore(_vpt(close, volume).diff(), YDAYS)


def f21_dvit_218_vpt_ema_distance_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPT minus its 63d EMA — short-term flow regime vs trend."""
    vpt = _vpt(close, volume)
    return vpt - vpt.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f21_dvit_219_vpt_consecutive_below_max_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak with VPT below its trailing 252d max — flow distribution persistence."""
    vpt = _vpt(close, volume)
    rmax = vpt.rolling(YDAYS, min_periods=QDAYS).max()
    return _consecutive_true_streak(vpt < rmax).astype(float)


def f21_dvit_220_vpt_corr_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation between VPT and close over trailing 252d."""
    return _vpt(close, volume).rolling(YDAYS, min_periods=QDAYS).corr(close)


# ============================================================
# Bucket S — $-vol vol-of-vol deeper measures (221-225)
# ============================================================

def f21_dvit_221_log_dv_vol_of_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std(63d) of rolling 21d-std of log-$-vol — short vol-of-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s21 = ldv.rolling(MDAYS, min_periods=WDAYS).std()
    return s21.rolling(QDAYS, min_periods=MDAYS).std()


def f21_dvit_222_log_dv_vol_of_vol_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of vol-of-vol of log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    s21 = ldv.rolling(MDAYS, min_periods=WDAYS).std()
    vov = s21.rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_zscore(vov, YDAYS)


def f21_dvit_223_log_dv_var_ratio_q_2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lo & MacKinlay variance ratio (q=2) on log-$-vol returns over 252d — < 1 means mean-reverting."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    def _vr(w, q=2):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v_q = np.array([v[i] + v[i + 1] for i in range(v.size - 1)])
        var1 = np.var(v, ddof=1)
        varq = np.var(v_q, ddof=1)
        if var1 <= 0:
            return np.nan
        return float(varq / (q * var1))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_vr, raw=True)


def f21_dvit_224_log_dv_var_ratio_q_5(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Variance ratio (q=5) on log-$-vol returns over 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    def _vr(w, q=5):
        v = w[~np.isnan(w)]
        if v.size < 40:
            return np.nan
        v_q = np.array([v[i:i + q].sum() for i in range(v.size - q + 1)])
        var1 = np.var(v, ddof=1)
        varq = np.var(v_q, ddof=1)
        if var1 <= 0:
            return np.nan
        return float(varq / (q * var1))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_vr, raw=True)


def f21_dvit_225_dv_volatility_persistence_garch_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """GARCH(1,1)-style persistence proxy: lag-1 autocorr of squared log-$-vol returns over 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    r = ldv.diff()
    sq = r ** 2
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1] - v[:-1].mean()
        b = v[1:] - v[1:].mean()
        d = np.sqrt((a * a).sum() * (b * b).sum())
        if d <= 0:
            return np.nan
        return float((a * b).sum() / d)
    return sq.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)


def f21_dvit_151_dv_return_signed_volume_252d_d3(close, volume):
    return f21_dvit_151_dv_return_signed_volume_252d(close, volume).diff().diff().diff()


def f21_dvit_152_dv_pastor_stambaugh_gamma_63d_d3(close, volume):
    return f21_dvit_152_dv_pastor_stambaugh_gamma_63d(close, volume).diff().diff().diff()


def f21_dvit_153_dv_pastor_stambaugh_gamma_252d_d3(close, volume):
    return f21_dvit_153_dv_pastor_stambaugh_gamma_252d(close, volume).diff().diff().diff()


def f21_dvit_154_dv_return_covariance_252d_d3(close, volume):
    return f21_dvit_154_dv_return_covariance_252d(close, volume).diff().diff().diff()


def f21_dvit_155_dv_volatility_per_unit_return_63d_d3(close, volume):
    return f21_dvit_155_dv_volatility_per_unit_return_63d(close, volume).diff().diff().diff()


def f21_dvit_156_dv_vs_return_beta_252d_d3(close, volume):
    return f21_dvit_156_dv_vs_return_beta_252d(close, volume).diff().diff().diff()


def f21_dvit_157_dv_idiosyncratic_return_residual_zscore_252d_d3(close, volume):
    return f21_dvit_157_dv_idiosyncratic_return_residual_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_158_dv_return_sign_disagreement_count_63d_d3(close, volume):
    return f21_dvit_158_dv_return_sign_disagreement_count_63d(close, volume).diff().diff().diff()


def f21_dvit_159_dv_return_sign_agreement_ratio_252d_d3(close, volume):
    return f21_dvit_159_dv_return_sign_agreement_ratio_252d(close, volume).diff().diff().diff()


def f21_dvit_160_dv_per_return_amplitude_252d_mean_d3(close, volume):
    return f21_dvit_160_dv_per_return_amplitude_252d_mean(close, volume).diff().diff().diff()


def f21_dvit_161_dv_regime_label_252d_d3(close, volume):
    return f21_dvit_161_dv_regime_label_252d(close, volume).diff().diff().diff()


def f21_dvit_162_dv_regime_transitions_count_252d_d3(close, volume):
    return f21_dvit_162_dv_regime_transitions_count_252d(close, volume).diff().diff().diff()


def f21_dvit_163_dv_high_regime_dwell_252d_d3(close, volume):
    return f21_dvit_163_dv_high_regime_dwell_252d(close, volume).diff().diff().diff()


def f21_dvit_164_dv_low_regime_dwell_252d_d3(close, volume):
    return f21_dvit_164_dv_low_regime_dwell_252d(close, volume).diff().diff().diff()


def f21_dvit_165_dv_regime_persistence_252d_d3(close, volume):
    return f21_dvit_165_dv_regime_persistence_252d(close, volume).diff().diff().diff()


def f21_dvit_166_dv_high_to_low_regime_transition_count_252d_d3(close, volume):
    return f21_dvit_166_dv_high_to_low_regime_transition_count_252d(close, volume).diff().diff().diff()


def f21_dvit_167_dv_low_to_high_regime_transition_count_252d_d3(close, volume):
    return f21_dvit_167_dv_low_to_high_regime_transition_count_252d(close, volume).diff().diff().diff()


def f21_dvit_168_dv_regime_entropy_252d_d3(close, volume):
    return f21_dvit_168_dv_regime_entropy_252d(close, volume).diff().diff().diff()


def f21_dvit_169_dv_regime_current_label_d3(close, volume):
    return f21_dvit_169_dv_regime_current_label(close, volume).diff().diff().diff()


def f21_dvit_170_dv_regime_current_age_d3(close, volume):
    return f21_dvit_170_dv_regime_current_age(close, volume).diff().diff().diff()


def f21_dvit_171_hawkes_dv_intensity_21d_d3(close, volume):
    return f21_dvit_171_hawkes_dv_intensity_21d(close, volume).diff().diff().diff()


def f21_dvit_172_hawkes_dv_intensity_63d_d3(close, volume):
    return f21_dvit_172_hawkes_dv_intensity_63d(close, volume).diff().diff().diff()


def f21_dvit_173_hawkes_dv_intensity_252d_d3(close, volume):
    return f21_dvit_173_hawkes_dv_intensity_252d(close, volume).diff().diff().diff()


def f21_dvit_174_hawkes_dv_decay_ratio_21_to_63_d3(close, volume):
    return f21_dvit_174_hawkes_dv_decay_ratio_21_to_63(close, volume).diff().diff().diff()


def f21_dvit_175_hawkes_dv_intensity_zscore_252d_d3(close, volume):
    return f21_dvit_175_hawkes_dv_intensity_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_176_hawkes_dv_cluster_count_above_3sigma_63d_d3(close, volume):
    return f21_dvit_176_hawkes_dv_cluster_count_above_3sigma_63d(close, volume).diff().diff().diff()


def f21_dvit_177_hawkes_dv_branching_ratio_proxy_252d_d3(close, volume):
    return f21_dvit_177_hawkes_dv_branching_ratio_proxy_252d(close, volume).diff().diff().diff()


def f21_dvit_178_hawkes_dv_silence_bars_since_intensity_p90_d3(close, volume):
    return f21_dvit_178_hawkes_dv_silence_bars_since_intensity_p90(close, volume).diff().diff().diff()


def f21_dvit_179_hawkes_dv_intensity_drawdown_252d_d3(close, volume):
    return f21_dvit_179_hawkes_dv_intensity_drawdown_252d(close, volume).diff().diff().diff()


def f21_dvit_180_hawkes_dv_intensity_ratio_to_baseline_252d_d3(close, volume):
    return f21_dvit_180_hawkes_dv_intensity_ratio_to_baseline_252d(close, volume).diff().diff().diff()


def f21_dvit_181_lee_mykland_jump_stat_logdv_21d_d3(close, volume):
    return f21_dvit_181_lee_mykland_jump_stat_logdv_21d(close, volume).diff().diff().diff()


def f21_dvit_182_lee_mykland_jump_count_above_4_252d_d3(close, volume):
    return f21_dvit_182_lee_mykland_jump_count_above_4_252d(close, volume).diff().diff().diff()


def f21_dvit_183_lee_mykland_jump_count_above_3_63d_d3(close, volume):
    return f21_dvit_183_lee_mykland_jump_count_above_3_63d(close, volume).diff().diff().diff()


def f21_dvit_184_bnstest_jump_proxy_252d_d3(close, volume):
    return f21_dvit_184_bnstest_jump_proxy_252d(close, volume).diff().diff().diff()


def f21_dvit_185_bnstest_zscore_252d_d3(close, volume):
    return f21_dvit_185_bnstest_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_186_jump_intensity_cum_252d_d3(close, volume):
    return f21_dvit_186_jump_intensity_cum_252d(close, volume).diff().diff().diff()


def f21_dvit_187_jump_clustering_iat_252d_d3(close, volume):
    return f21_dvit_187_jump_clustering_iat_252d(close, volume).diff().diff().diff()


def f21_dvit_188_signed_jump_252d_d3(close, volume):
    return f21_dvit_188_signed_jump_252d(close, volume).diff().diff().diff()


def f21_dvit_189_positive_jump_count_252d_d3(close, volume):
    return f21_dvit_189_positive_jump_count_252d(close, volume).diff().diff().diff()


def f21_dvit_190_negative_jump_count_252d_d3(close, volume):
    return f21_dvit_190_negative_jump_count_252d(close, volume).diff().diff().diff()


def f21_dvit_191_overnight_dv_shock_zscore_252d_d3(open, close, volume):
    return f21_dvit_191_overnight_dv_shock_zscore_252d(open, close, volume).diff().diff().diff()


def f21_dvit_192_overnight_dv_shock_count_above_3_252d_d3(open, close, volume):
    return f21_dvit_192_overnight_dv_shock_count_above_3_252d(open, close, volume).diff().diff().diff()


def f21_dvit_193_overnight_dv_to_intraday_dv_ratio_21d_d3(open, high, low, close, volume):
    return f21_dvit_193_overnight_dv_to_intraday_dv_ratio_21d(open, high, low, close, volume).diff().diff().diff()


def f21_dvit_194_overnight_gap_signed_dv_sum_252d_d3(open, close, volume):
    return f21_dvit_194_overnight_gap_signed_dv_sum_252d(open, close, volume).diff().diff().diff()


def f21_dvit_195_overnight_negative_gap_dv_count_252d_d3(open, close, volume):
    return f21_dvit_195_overnight_negative_gap_dv_count_252d(open, close, volume).diff().diff().diff()


def f21_dvit_196_overnight_positive_gap_dv_count_252d_d3(open, close, volume):
    return f21_dvit_196_overnight_positive_gap_dv_count_252d(open, close, volume).diff().diff().diff()


def f21_dvit_197_overnight_dv_shock_at_high_only_count_252d_d3(open, high, close, volume):
    return f21_dvit_197_overnight_dv_shock_at_high_only_count_252d(open, high, close, volume).diff().diff().diff()


def f21_dvit_198_overnight_gap_z_252d_d3(open, close):
    return f21_dvit_198_overnight_gap_z_252d(open, close).diff().diff().diff()


def f21_dvit_199_max_overnight_dv_shock_252d_d3(open, close, volume):
    return f21_dvit_199_max_overnight_dv_shock_252d(open, close, volume).diff().diff().diff()


def f21_dvit_200_bars_since_last_overnight_dv_shock_d3(open, close, volume):
    return f21_dvit_200_bars_since_last_overnight_dv_shock(open, close, volume).diff().diff().diff()


def f21_dvit_201_dv_dryup_composite_score_252d_d3(high, low, close, volume):
    return f21_dvit_201_dv_dryup_composite_score_252d(high, low, close, volume).diff().diff().diff()


def f21_dvit_202_dv_dryup_composite_streak_d3(high, low, close, volume):
    return f21_dvit_202_dv_dryup_composite_streak(high, low, close, volume).diff().diff().diff()


def f21_dvit_203_dv_dryup_composite_count_63d_d3(high, low, close, volume):
    return f21_dvit_203_dv_dryup_composite_count_63d(high, low, close, volume).diff().diff().diff()


def f21_dvit_204_dv_oscillation_amplitude_63d_d3(close, volume):
    return f21_dvit_204_dv_oscillation_amplitude_63d(close, volume).diff().diff().diff()


def f21_dvit_205_dv_dryup_persistence_252d_d3(close, volume):
    return f21_dvit_205_dv_dryup_persistence_252d(close, volume).diff().diff().diff()


def f21_dvit_206_dv_silence_during_pullback_252d_d3(close, volume):
    return f21_dvit_206_dv_silence_during_pullback_252d(close, volume).diff().diff().diff()


def f21_dvit_207_dv_active_to_silent_ratio_252d_d3(close, volume):
    return f21_dvit_207_dv_active_to_silent_ratio_252d(close, volume).diff().diff().diff()


def f21_dvit_208_dv_compression_indicator_21d_d3(close, volume):
    return f21_dvit_208_dv_compression_indicator_21d(close, volume).diff().diff().diff()


def f21_dvit_209_dv_compression_dwell_252d_d3(close, volume):
    return f21_dvit_209_dv_compression_dwell_252d(close, volume).diff().diff().diff()


def f21_dvit_210_dv_dryup_early_warning_score_d3(high, low, close, volume):
    return f21_dvit_210_dv_dryup_early_warning_score(high, low, close, volume).diff().diff().diff()


def f21_dvit_211_vpt_slope_63d_d3(close, volume):
    return f21_dvit_211_vpt_slope_63d(close, volume).diff().diff().diff()


def f21_dvit_212_vpt_slope_252d_d3(close, volume):
    return f21_dvit_212_vpt_slope_252d(close, volume).diff().diff().diff()


def f21_dvit_213_vpt_zscore_252d_d3(close, volume):
    return f21_dvit_213_vpt_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_214_vpt_minus_price_slope_252d_d3(close, volume):
    return f21_dvit_214_vpt_minus_price_slope_252d(close, volume).diff().diff().diff()


def f21_dvit_215_vpt_drawdown_from_max_252d_d3(close, volume):
    return f21_dvit_215_vpt_drawdown_from_max_252d(close, volume).diff().diff().diff()


def f21_dvit_216_vpt_age_of_max_252d_d3(close, volume):
    return f21_dvit_216_vpt_age_of_max_252d(close, volume).diff().diff().diff()


def f21_dvit_217_vpt_diff_zscore_252d_d3(close, volume):
    return f21_dvit_217_vpt_diff_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_218_vpt_ema_distance_63d_d3(close, volume):
    return f21_dvit_218_vpt_ema_distance_63d(close, volume).diff().diff().diff()


def f21_dvit_219_vpt_consecutive_below_max_streak_d3(close, volume):
    return f21_dvit_219_vpt_consecutive_below_max_streak(close, volume).diff().diff().diff()


def f21_dvit_220_vpt_corr_close_252d_d3(close, volume):
    return f21_dvit_220_vpt_corr_close_252d(close, volume).diff().diff().diff()


def f21_dvit_221_log_dv_vol_of_vol_63d_d3(close, volume):
    return f21_dvit_221_log_dv_vol_of_vol_63d(close, volume).diff().diff().diff()


def f21_dvit_222_log_dv_vol_of_vol_zscore_252d_d3(close, volume):
    return f21_dvit_222_log_dv_vol_of_vol_zscore_252d(close, volume).diff().diff().diff()


def f21_dvit_223_log_dv_var_ratio_q_2_d3(close, volume):
    return f21_dvit_223_log_dv_var_ratio_q_2(close, volume).diff().diff().diff()


def f21_dvit_224_log_dv_var_ratio_q_5_d3(close, volume):
    return f21_dvit_224_log_dv_var_ratio_q_5(close, volume).diff().diff().diff()


def f21_dvit_225_dv_volatility_persistence_garch_proxy_252d_d3(close, volume):
    return f21_dvit_225_dv_volatility_persistence_garch_proxy_252d(close, volume).diff().diff().diff()


# ============================================================
#                         REGISTRY 151-225
# ============================================================


DOLLAR_VOLUME_INTENSITY_D3_REGISTRY_151_225 = {
    "f21_dvit_151_dv_return_signed_volume_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_151_dv_return_signed_volume_252d_d3},
    "f21_dvit_152_dv_pastor_stambaugh_gamma_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_152_dv_pastor_stambaugh_gamma_63d_d3},
    "f21_dvit_153_dv_pastor_stambaugh_gamma_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_153_dv_pastor_stambaugh_gamma_252d_d3},
    "f21_dvit_154_dv_return_covariance_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_154_dv_return_covariance_252d_d3},
    "f21_dvit_155_dv_volatility_per_unit_return_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_155_dv_volatility_per_unit_return_63d_d3},
    "f21_dvit_156_dv_vs_return_beta_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_156_dv_vs_return_beta_252d_d3},
    "f21_dvit_157_dv_idiosyncratic_return_residual_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_157_dv_idiosyncratic_return_residual_zscore_252d_d3},
    "f21_dvit_158_dv_return_sign_disagreement_count_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_158_dv_return_sign_disagreement_count_63d_d3},
    "f21_dvit_159_dv_return_sign_agreement_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_159_dv_return_sign_agreement_ratio_252d_d3},
    "f21_dvit_160_dv_per_return_amplitude_252d_mean_d3": {"inputs": ["close", "volume"], "func": f21_dvit_160_dv_per_return_amplitude_252d_mean_d3},
    "f21_dvit_161_dv_regime_label_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_161_dv_regime_label_252d_d3},
    "f21_dvit_162_dv_regime_transitions_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_162_dv_regime_transitions_count_252d_d3},
    "f21_dvit_163_dv_high_regime_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_163_dv_high_regime_dwell_252d_d3},
    "f21_dvit_164_dv_low_regime_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_164_dv_low_regime_dwell_252d_d3},
    "f21_dvit_165_dv_regime_persistence_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_165_dv_regime_persistence_252d_d3},
    "f21_dvit_166_dv_high_to_low_regime_transition_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_166_dv_high_to_low_regime_transition_count_252d_d3},
    "f21_dvit_167_dv_low_to_high_regime_transition_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_167_dv_low_to_high_regime_transition_count_252d_d3},
    "f21_dvit_168_dv_regime_entropy_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_168_dv_regime_entropy_252d_d3},
    "f21_dvit_169_dv_regime_current_label_d3": {"inputs": ["close", "volume"], "func": f21_dvit_169_dv_regime_current_label_d3},
    "f21_dvit_170_dv_regime_current_age_d3": {"inputs": ["close", "volume"], "func": f21_dvit_170_dv_regime_current_age_d3},
    "f21_dvit_171_hawkes_dv_intensity_21d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_171_hawkes_dv_intensity_21d_d3},
    "f21_dvit_172_hawkes_dv_intensity_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_172_hawkes_dv_intensity_63d_d3},
    "f21_dvit_173_hawkes_dv_intensity_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_173_hawkes_dv_intensity_252d_d3},
    "f21_dvit_174_hawkes_dv_decay_ratio_21_to_63_d3": {"inputs": ["close", "volume"], "func": f21_dvit_174_hawkes_dv_decay_ratio_21_to_63_d3},
    "f21_dvit_175_hawkes_dv_intensity_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_175_hawkes_dv_intensity_zscore_252d_d3},
    "f21_dvit_176_hawkes_dv_cluster_count_above_3sigma_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_176_hawkes_dv_cluster_count_above_3sigma_63d_d3},
    "f21_dvit_177_hawkes_dv_branching_ratio_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_177_hawkes_dv_branching_ratio_proxy_252d_d3},
    "f21_dvit_178_hawkes_dv_silence_bars_since_intensity_p90_d3": {"inputs": ["close", "volume"], "func": f21_dvit_178_hawkes_dv_silence_bars_since_intensity_p90_d3},
    "f21_dvit_179_hawkes_dv_intensity_drawdown_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_179_hawkes_dv_intensity_drawdown_252d_d3},
    "f21_dvit_180_hawkes_dv_intensity_ratio_to_baseline_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_180_hawkes_dv_intensity_ratio_to_baseline_252d_d3},
    "f21_dvit_181_lee_mykland_jump_stat_logdv_21d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_181_lee_mykland_jump_stat_logdv_21d_d3},
    "f21_dvit_182_lee_mykland_jump_count_above_4_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_182_lee_mykland_jump_count_above_4_252d_d3},
    "f21_dvit_183_lee_mykland_jump_count_above_3_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_183_lee_mykland_jump_count_above_3_63d_d3},
    "f21_dvit_184_bnstest_jump_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_184_bnstest_jump_proxy_252d_d3},
    "f21_dvit_185_bnstest_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_185_bnstest_zscore_252d_d3},
    "f21_dvit_186_jump_intensity_cum_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_186_jump_intensity_cum_252d_d3},
    "f21_dvit_187_jump_clustering_iat_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_187_jump_clustering_iat_252d_d3},
    "f21_dvit_188_signed_jump_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_188_signed_jump_252d_d3},
    "f21_dvit_189_positive_jump_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_189_positive_jump_count_252d_d3},
    "f21_dvit_190_negative_jump_count_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_190_negative_jump_count_252d_d3},
    "f21_dvit_191_overnight_dv_shock_zscore_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_191_overnight_dv_shock_zscore_252d_d3},
    "f21_dvit_192_overnight_dv_shock_count_above_3_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_192_overnight_dv_shock_count_above_3_252d_d3},
    "f21_dvit_193_overnight_dv_to_intraday_dv_ratio_21d_d3": {"inputs": ["open", "high", "low", "close", "volume"], "func": f21_dvit_193_overnight_dv_to_intraday_dv_ratio_21d_d3},
    "f21_dvit_194_overnight_gap_signed_dv_sum_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_194_overnight_gap_signed_dv_sum_252d_d3},
    "f21_dvit_195_overnight_negative_gap_dv_count_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_195_overnight_negative_gap_dv_count_252d_d3},
    "f21_dvit_196_overnight_positive_gap_dv_count_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_196_overnight_positive_gap_dv_count_252d_d3},
    "f21_dvit_197_overnight_dv_shock_at_high_only_count_252d_d3": {"inputs": ["open", "high", "close", "volume"], "func": f21_dvit_197_overnight_dv_shock_at_high_only_count_252d_d3},
    "f21_dvit_198_overnight_gap_z_252d_d3": {"inputs": ["open", "close"], "func": f21_dvit_198_overnight_gap_z_252d_d3},
    "f21_dvit_199_max_overnight_dv_shock_252d_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_199_max_overnight_dv_shock_252d_d3},
    "f21_dvit_200_bars_since_last_overnight_dv_shock_d3": {"inputs": ["open", "close", "volume"], "func": f21_dvit_200_bars_since_last_overnight_dv_shock_d3},
    "f21_dvit_201_dv_dryup_composite_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_201_dv_dryup_composite_score_252d_d3},
    "f21_dvit_202_dv_dryup_composite_streak_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_202_dv_dryup_composite_streak_d3},
    "f21_dvit_203_dv_dryup_composite_count_63d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_203_dv_dryup_composite_count_63d_d3},
    "f21_dvit_204_dv_oscillation_amplitude_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_204_dv_oscillation_amplitude_63d_d3},
    "f21_dvit_205_dv_dryup_persistence_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_205_dv_dryup_persistence_252d_d3},
    "f21_dvit_206_dv_silence_during_pullback_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_206_dv_silence_during_pullback_252d_d3},
    "f21_dvit_207_dv_active_to_silent_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_207_dv_active_to_silent_ratio_252d_d3},
    "f21_dvit_208_dv_compression_indicator_21d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_208_dv_compression_indicator_21d_d3},
    "f21_dvit_209_dv_compression_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_209_dv_compression_dwell_252d_d3},
    "f21_dvit_210_dv_dryup_early_warning_score_d3": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_210_dv_dryup_early_warning_score_d3},
    "f21_dvit_211_vpt_slope_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_211_vpt_slope_63d_d3},
    "f21_dvit_212_vpt_slope_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_212_vpt_slope_252d_d3},
    "f21_dvit_213_vpt_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_213_vpt_zscore_252d_d3},
    "f21_dvit_214_vpt_minus_price_slope_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_214_vpt_minus_price_slope_252d_d3},
    "f21_dvit_215_vpt_drawdown_from_max_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_215_vpt_drawdown_from_max_252d_d3},
    "f21_dvit_216_vpt_age_of_max_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_216_vpt_age_of_max_252d_d3},
    "f21_dvit_217_vpt_diff_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_217_vpt_diff_zscore_252d_d3},
    "f21_dvit_218_vpt_ema_distance_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_218_vpt_ema_distance_63d_d3},
    "f21_dvit_219_vpt_consecutive_below_max_streak_d3": {"inputs": ["close", "volume"], "func": f21_dvit_219_vpt_consecutive_below_max_streak_d3},
    "f21_dvit_220_vpt_corr_close_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_220_vpt_corr_close_252d_d3},
    "f21_dvit_221_log_dv_vol_of_vol_63d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_221_log_dv_vol_of_vol_63d_d3},
    "f21_dvit_222_log_dv_vol_of_vol_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_222_log_dv_vol_of_vol_zscore_252d_d3},
    "f21_dvit_223_log_dv_var_ratio_q_2_d3": {"inputs": ["close", "volume"], "func": f21_dvit_223_log_dv_var_ratio_q_2_d3},
    "f21_dvit_224_log_dv_var_ratio_q_5_d3": {"inputs": ["close", "volume"], "func": f21_dvit_224_log_dv_var_ratio_q_5_d3},
    "f21_dvit_225_dv_volatility_persistence_garch_proxy_252d_d3": {"inputs": ["close", "volume"], "func": f21_dvit_225_dv_volatility_persistence_garch_proxy_252d_d3},
}
