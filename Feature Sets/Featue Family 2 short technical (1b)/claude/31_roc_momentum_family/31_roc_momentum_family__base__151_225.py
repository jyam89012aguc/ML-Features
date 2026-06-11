"""roc_momentum_family base features 151-225 — Pipeline 1b-technical (gap-fill).

Continuation of 001-150. Buckets in this file:
I (academic momentum factor definitions: 12-1 skip, 36-12 long-term reversal,
1-month reversal, FIP information discreteness, path-dependence), 151-170;
J (risk-adjusted momentum: Sharpe-mom, Sortino-mom, Calmar-mom, info-ratio
volatility-adjusted ROC), 171-190; K (smoothness / consistency / hit-rate /
path tortuosity / K-ratio / MAE-MFE ratios), 191-210; L beginning of
drawdown-aware momentum (max DD, underwater duration, recovery half-life,
Calmar variants), 211-225.

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


def _rolling_drawdown(close, n, min_periods=None):
    """Max drawdown (negative or zero) over trailing n bars, defined as
    min over the window of (close - running max so far) / running max so far."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _md(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nanmin(dd))
    return close.rolling(n, min_periods=min_periods).apply(_md, raw=True)


# ============================================================
# Bucket I — Academic momentum factor definitions (151-170)
# Each is a distinct, citable hypothesis from the academic literature.
# ============================================================

def f31_rcmf_151_momentum_12_1_skip(close: pd.Series) -> pd.Series:
    """Jegadeesh-Titman 12-1: cumulative return from t-252 to t-21 (skip last 21 days)."""
    return _safe_div(close.shift(MDAYS), close.shift(YDAYS)) - 1.0


def f31_rcmf_152_momentum_12_2_skip(close: pd.Series) -> pd.Series:
    """Variant: cumulative return from t-252 to t-42 (skip last 2 months)."""
    return _safe_div(close.shift(42), close.shift(YDAYS)) - 1.0


def f31_rcmf_153_momentum_9_1_skip(close: pd.Series) -> pd.Series:
    """9-1 momentum: return from t-189 to t-21 — shorter intermediate-term momentum."""
    return _safe_div(close.shift(MDAYS), close.shift(189)) - 1.0


def f31_rcmf_154_momentum_6_1_skip(close: pd.Series) -> pd.Series:
    """6-1 momentum: return from t-126 to t-21 — short intermediate momentum."""
    return _safe_div(close.shift(MDAYS), close.shift(126)) - 1.0


def f31_rcmf_155_long_term_reversal_36_12(close: pd.Series) -> pd.Series:
    """De Bondt-Thaler long-term reversal: return from t-756 to t-252 (3yr to 1yr ago)."""
    return _safe_div(close.shift(YDAYS), close.shift(DDAYS_3Y)) - 1.0


def f31_rcmf_156_long_term_reversal_60_12(close: pd.Series) -> pd.Series:
    """5yr-to-1yr long-term reversal: return from t-1260 to t-252."""
    return _safe_div(close.shift(YDAYS), close.shift(DDAYS_5Y)) - 1.0


def f31_rcmf_157_short_term_reversal_1m(close: pd.Series) -> pd.Series:
    """Jegadeesh short-term reversal: negative of trailing 21d ROC (sign-flipped signal)."""
    return -close.pct_change(MDAYS)


def f31_rcmf_158_short_term_reversal_5d(close: pd.Series) -> pd.Series:
    """Lehmann/Lo-MacKinlay weekly reversal: negative of trailing 5d ROC."""
    return -close.pct_change(WDAYS)


def f31_rcmf_159_fip_information_discreteness(close: pd.Series) -> pd.Series:
    """Da-Gurun-Warachka frog-in-the-pan: sign(ret_252) * (%neg − %pos) over 252d.
    More negative = more continuous information; more positive = more discrete (jumpy)."""
    r = close.pct_change(1)
    pos = (r > 0).astype(float)
    neg = (r < 0).astype(float)
    val = r.notna().astype(float)
    n = val.rolling(YDAYS, min_periods=QDAYS).sum()
    p = pos.rolling(YDAYS, min_periods=QDAYS).sum()
    m = neg.rolling(YDAYS, min_periods=QDAYS).sum()
    pct_neg = _safe_div(m, n)
    pct_pos = _safe_div(p, n)
    sign_ret = np.sign(close.pct_change(YDAYS))
    return sign_ret * (pct_neg - pct_pos)


def f31_rcmf_160_fip_information_discreteness_126d(close: pd.Series) -> pd.Series:
    """FIP variant: sign(ret_126) * (%neg − %pos) over trailing 126d — half-year FIP."""
    r = close.pct_change(1)
    pos = (r > 0).astype(float)
    neg = (r < 0).astype(float)
    val = r.notna().astype(float)
    n = val.rolling(126, min_periods=42).sum()
    p = pos.rolling(126, min_periods=42).sum()
    m = neg.rolling(126, min_periods=42).sum()
    pct_neg = _safe_div(m, n)
    pct_pos = _safe_div(p, n)
    sign_ret = np.sign(close.pct_change(126))
    return sign_ret * (pct_neg - pct_pos)


def f31_rcmf_161_fip_signed_id_252d(close: pd.Series) -> pd.Series:
    """Signed FIP (no sign multiplier): %positive − %negative over trailing 252d — raw
    information-discreteness direction independent of overall return sign."""
    r = close.pct_change(1)
    pos = (r > 0).astype(float)
    neg = (r < 0).astype(float)
    val = r.notna().astype(float)
    n = val.rolling(YDAYS, min_periods=QDAYS).sum()
    p = pos.rolling(YDAYS, min_periods=QDAYS).sum()
    m = neg.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(p - m, n)


def f31_rcmf_162_path_smoothness_weighted_12_1(close: pd.Series) -> pd.Series:
    """Path-smoothness weighted 12-1: (ret_12_1) divided by sum(|daily_ret|) over the formation
    window — momentum scaled by total path activity (continuous-info enhancement)."""
    ret_12_1 = _safe_div(close.shift(MDAYS), close.shift(YDAYS)) - 1.0
    abs_r = close.pct_change(1).abs()
    activity = abs_r.shift(MDAYS).rolling(YDAYS - MDAYS, min_periods=QDAYS).sum()
    return _safe_div(ret_12_1, activity)


def f31_rcmf_163_intermediate_horizon_252_126(close: pd.Series) -> pd.Series:
    """Asness intermediate-horizon: return from t-252 to t-126 — first-half-of-year return."""
    return _safe_div(close.shift(126), close.shift(YDAYS)) - 1.0


def f31_rcmf_164_recent_horizon_126_0(close: pd.Series) -> pd.Series:
    """Second-half-of-year return: t-126 to t-0 — recent half-year (complement of 163)."""
    return close.pct_change(126)


def f31_rcmf_165_echo_momentum_year_2(close: pd.Series) -> pd.Series:
    """Heston-Sadka echo: return in year 2 ago (t-504 to t-252) — same-month seasonality proxy."""
    return _safe_div(close.shift(YDAYS), close.shift(DDAYS_2Y)) - 1.0


def f31_rcmf_166_echo_momentum_year_3(close: pd.Series) -> pd.Series:
    """Echo year-3: return in year 3 ago (t-756 to t-504) — deep echo proxy."""
    return _safe_div(close.shift(DDAYS_2Y), close.shift(DDAYS_3Y)) - 1.0


def f31_rcmf_167_echo_to_recent_ratio(close: pd.Series) -> pd.Series:
    """Echo (year-2) divided by recent (year-1) — relative strength of seasonality vs current trend."""
    echo = _safe_div(close.shift(YDAYS), close.shift(DDAYS_2Y)) - 1.0
    recent = close.pct_change(YDAYS)
    return _safe_div(echo, recent)


def f31_rcmf_168_industry_momentum_proxy(close: pd.Series) -> pd.Series:
    """Moskowitz-Grinblatt intermediate-term proxy (no industry data): smoothed 252d log-return
    using an exponential 21d half-life — captures trending-but-not-just-recent component."""
    r = _safe_log(close).diff(YDAYS)
    return r.ewm(halflife=MDAYS, min_periods=WDAYS, adjust=False).mean()


def f31_rcmf_169_double_skip_momentum_12_3(close: pd.Series) -> pd.Series:
    """12-3 skip momentum (Asness adjusted): return from t-252 to t-63 — skip last quarter."""
    return _safe_div(close.shift(QDAYS), close.shift(YDAYS)) - 1.0


def f31_rcmf_170_residual_recent_minus_skip(close: pd.Series) -> pd.Series:
    """ret_252 − ret_12_1: the 'skip month' contribution — short-term reversal embedded in 12m."""
    full = close.pct_change(YDAYS)
    skipped = _safe_div(close.shift(MDAYS), close.shift(YDAYS)) - 1.0
    return full - skipped


# ============================================================
# Bucket J — Risk-adjusted momentum (171-190)
# Each = ret_N / risk-statistic_N with different risk denominators.
# ============================================================

def f31_rcmf_171_sharpe_momentum_21d(close: pd.Series) -> pd.Series:
    """Sharpe-momentum: 21d ROC divided by 21d std of 1d returns — vol-adjusted monthly momentum."""
    r = close.pct_change(MDAYS)
    sigma = close.pct_change(1).rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(r, sigma)


def f31_rcmf_172_sharpe_momentum_63d(close: pd.Series) -> pd.Series:
    """Sharpe-momentum: 63d ROC divided by 63d std of 1d returns — vol-adjusted quarterly momentum."""
    r = close.pct_change(QDAYS)
    sigma = close.pct_change(1).rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(r, sigma)


def f31_rcmf_173_sharpe_momentum_252d(close: pd.Series) -> pd.Series:
    """Sharpe-momentum: 252d ROC divided by 252d std of 1d returns — vol-adjusted annual momentum."""
    r = close.pct_change(YDAYS)
    sigma = close.pct_change(1).rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(r, sigma)


def f31_rcmf_174_sortino_momentum_21d(close: pd.Series) -> pd.Series:
    """Sortino-momentum: 21d ROC / 21d downside std (negative-day returns only)."""
    r = close.pct_change(1)
    down = r.where(r < 0, 0.0)
    dn_sd = down.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(close.pct_change(MDAYS), dn_sd)


def f31_rcmf_175_sortino_momentum_63d(close: pd.Series) -> pd.Series:
    """Sortino-momentum: 63d ROC / 63d downside std."""
    r = close.pct_change(1)
    down = r.where(r < 0, 0.0)
    dn_sd = down.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(close.pct_change(QDAYS), dn_sd)


def f31_rcmf_176_sortino_momentum_252d(close: pd.Series) -> pd.Series:
    """Sortino-momentum: 252d ROC / 252d downside std — annual downside-vol-adjusted momentum."""
    r = close.pct_change(1)
    down = r.where(r < 0, 0.0)
    dn_sd = down.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(close.pct_change(YDAYS), dn_sd)


def f31_rcmf_177_calmar_momentum_63d(close: pd.Series) -> pd.Series:
    """Calmar-momentum: 63d ROC / |max drawdown over 63d| — quarterly drawdown-adjusted momentum."""
    r = close.pct_change(QDAYS)
    dd = _rolling_drawdown(close, QDAYS)
    return _safe_div(r, dd.abs())


def f31_rcmf_178_calmar_momentum_252d(close: pd.Series) -> pd.Series:
    """Calmar-momentum: 252d ROC / |max drawdown over 252d| — annual drawdown-adjusted momentum."""
    r = close.pct_change(YDAYS)
    dd = _rolling_drawdown(close, YDAYS)
    return _safe_div(r, dd.abs())


def f31_rcmf_179_calmar_momentum_504d(close: pd.Series) -> pd.Series:
    """Calmar-momentum: 504d ROC / |max drawdown over 504d| — biennial drawdown-adjusted momentum."""
    r = close.pct_change(DDAYS_2Y)
    dd = _rolling_drawdown(close, DDAYS_2Y)
    return _safe_div(r, dd.abs())


def f31_rcmf_180_info_ratio_drift_to_activity_63d(close: pd.Series) -> pd.Series:
    """Drift/activity info ratio: ret_63 / sum(|ret_1|_over_63) — net drift per unit path activity."""
    r = close.pct_change(QDAYS)
    abs_act = close.pct_change(1).abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(r, abs_act)


def f31_rcmf_181_info_ratio_drift_to_activity_252d(close: pd.Series) -> pd.Series:
    """Drift/activity info ratio over 252d — annual net drift per unit path activity."""
    r = close.pct_change(YDAYS)
    abs_act = close.pct_change(1).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(r, abs_act)


def f31_rcmf_182_atr_normalized_roc_21d(close: pd.Series) -> pd.Series:
    """ROC_21 normalized by 21d trailing-mean of |1d returns| — momentum-per-unit-noise (alternate)."""
    r = close.pct_change(MDAYS)
    noise = close.pct_change(1).abs().rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(r, noise)


def f31_rcmf_183_atr_normalized_roc_63d(close: pd.Series) -> pd.Series:
    """ROC_63 normalized by 63d trailing-mean of |1d returns|."""
    r = close.pct_change(QDAYS)
    noise = close.pct_change(1).abs().rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(r, noise)


def f31_rcmf_184_atr_normalized_roc_252d(close: pd.Series) -> pd.Series:
    """ROC_252 normalized by 252d trailing-mean of |1d returns|."""
    r = close.pct_change(YDAYS)
    noise = close.pct_change(1).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(r, noise)


def f31_rcmf_185_upside_sharpe_252d(close: pd.Series) -> pd.Series:
    """Upside-Sharpe: 252d ROC / 252d upside-std (positive-day returns only)."""
    r = close.pct_change(1)
    up = r.where(r > 0, 0.0)
    up_sd = up.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(close.pct_change(YDAYS), up_sd)


def f31_rcmf_186_omega_ratio_proxy_63d(close: pd.Series) -> pd.Series:
    """Omega-ratio proxy: sum(positive 1d returns) / sum(|negative 1d returns|) over 63d."""
    r = close.pct_change(1)
    up = r.clip(lower=0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = (-r.clip(upper=0)).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up, dn)


def f31_rcmf_187_omega_ratio_proxy_252d(close: pd.Series) -> pd.Series:
    """Omega-ratio proxy over 252d — annual upside/downside cumulative payoff ratio."""
    r = close.pct_change(1)
    up = r.clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (-r.clip(upper=0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up, dn)


def f31_rcmf_188_gain_to_pain_ratio_252d(close: pd.Series) -> pd.Series:
    """Gain-to-pain (Schwager): net return / sum(|negative 1d returns|) over 252d."""
    r = close.pct_change(1)
    net = r.rolling(YDAYS, min_periods=QDAYS).sum()
    pain = (-r.clip(upper=0)).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, pain)


def f31_rcmf_189_sharpe_minus_sortino_252d(close: pd.Series) -> pd.Series:
    """Sharpe-momentum minus Sortino-momentum at 252d — downside-vs-total vol asymmetry indicator."""
    r = close.pct_change(1)
    full_sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    down = r.where(r < 0, 0.0)
    dn_sd = down.rolling(YDAYS, min_periods=QDAYS).std()
    roc = close.pct_change(YDAYS)
    return _safe_div(roc, full_sd) - _safe_div(roc, dn_sd)


def f31_rcmf_190_burke_ratio_proxy_252d(close: pd.Series) -> pd.Series:
    """Burke-ratio proxy: 252d ROC / sqrt of sum-of-squared rolling drawdowns over 252d."""
    r = close.pct_change(YDAYS)
    def _bd(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.sqrt(np.nansum(dd ** 2)))
    rmsd = close.rolling(YDAYS, min_periods=QDAYS).apply(_bd, raw=True)
    return _safe_div(r, rmsd)


# ============================================================
# Bucket K — Smoothness / consistency / hit-rate / K-ratio (191-210)
# ============================================================

def f31_rcmf_191_momentum_consistency_subperiod_252d(close: pd.Series) -> pd.Series:
    """Frazzini-Pedersen consistency: fraction of 21d subperiod returns positive over the past 252d."""
    r = close.pct_change(MDAYS)
    pos = (r > 0).astype(float)
    valid = r.notna().astype(float)
    return _safe_div(pos.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())


def f31_rcmf_192_momentum_consistency_subperiod_504d(close: pd.Series) -> pd.Series:
    """Consistency over 2 years: fraction of 63d-subperiod returns positive over 504d."""
    r = close.pct_change(QDAYS)
    pos = (r > 0).astype(float)
    valid = r.notna().astype(float)
    return _safe_div(pos.rolling(DDAYS_2Y, min_periods=YDAYS).sum(), valid.rolling(DDAYS_2Y, min_periods=YDAYS).sum())


def f31_rcmf_193_hit_rate_5d_returns_63d(close: pd.Series) -> pd.Series:
    """Hit rate: fraction of 5d returns positive over trailing 63d."""
    r = close.pct_change(WDAYS)
    pos = (r > 0).astype(float)
    valid = r.notna().astype(float)
    return _safe_div(pos.rolling(QDAYS, min_periods=MDAYS).sum(), valid.rolling(QDAYS, min_periods=MDAYS).sum())


def f31_rcmf_194_hit_rate_21d_returns_252d(close: pd.Series) -> pd.Series:
    """Hit rate: fraction of 21d returns positive over trailing 252d."""
    r = close.pct_change(MDAYS)
    pos = (r > 0).astype(float)
    valid = r.notna().astype(float)
    return _safe_div(pos.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum())


def f31_rcmf_195_path_tortuosity_252d(close: pd.Series) -> pd.Series:
    """Path tortuosity: |log_ret_252| / sum(|log_ret_1|) over 252d — net move vs total path length.
    Near 1 = straight-line trend; near 0 = chop. Distinct from drift/activity (uses log).
    """
    lr = _safe_log(close).diff(1)
    abs_path = lr.abs().rolling(YDAYS, min_periods=QDAYS).sum()
    net = _safe_log(close).diff(YDAYS).abs()
    return _safe_div(net, abs_path)


def f31_rcmf_196_path_tortuosity_63d(close: pd.Series) -> pd.Series:
    """Quarterly path tortuosity: |log_ret_63| / sum(|log_ret_1|) over 63d."""
    lr = _safe_log(close).diff(1)
    abs_path = lr.abs().rolling(QDAYS, min_periods=MDAYS).sum()
    net = _safe_log(close).diff(QDAYS).abs()
    return _safe_div(net, abs_path)


def f31_rcmf_197_k_ratio_log_price_63d(close: pd.Series) -> pd.Series:
    """Kestner K-ratio over 63d: slope of log price / std-error of slope over the window."""
    lp = _safe_log(close)
    n = QDAYS
    def _k(w):
        valid = ~np.isnan(w)
        if valid.sum() < MDAYS:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        slope = ((x - xm) * (w - wm)).sum() / sxx
        residuals = w - (wm + slope * (x - xm))
        nn = len(x)
        if nn <= 2:
            return np.nan
        sigma2 = (residuals ** 2).sum() / (nn - 2)
        se_slope = np.sqrt(sigma2 / sxx) if sigma2 > 0 else np.nan
        if not np.isfinite(se_slope) or se_slope == 0:
            return np.nan
        return slope / se_slope
    return lp.rolling(n, min_periods=MDAYS).apply(_k, raw=True)


def f31_rcmf_198_k_ratio_log_price_252d(close: pd.Series) -> pd.Series:
    """Kestner K-ratio over 252d — annual horizon K-ratio (trend quality, slope/SE)."""
    lp = _safe_log(close)
    n = YDAYS
    def _k(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        slope = ((x - xm) * (w - wm)).sum() / sxx
        residuals = w - (wm + slope * (x - xm))
        nn = len(x)
        if nn <= 2:
            return np.nan
        sigma2 = (residuals ** 2).sum() / (nn - 2)
        se_slope = np.sqrt(sigma2 / sxx) if sigma2 > 0 else np.nan
        if not np.isfinite(se_slope) or se_slope == 0:
            return np.nan
        return slope / se_slope
    return lp.rolling(n, min_periods=QDAYS).apply(_k, raw=True)


def f31_rcmf_199_k_ratio_log_price_504d(close: pd.Series) -> pd.Series:
    """Kestner K-ratio over 504d — biennial trend-quality measure."""
    lp = _safe_log(close)
    n = DDAYS_2Y
    def _k(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        slope = ((x - xm) * (w - wm)).sum() / sxx
        residuals = w - (wm + slope * (x - xm))
        nn = len(x)
        if nn <= 2:
            return np.nan
        sigma2 = (residuals ** 2).sum() / (nn - 2)
        se_slope = np.sqrt(sigma2 / sxx) if sigma2 > 0 else np.nan
        if not np.isfinite(se_slope) or se_slope == 0:
            return np.nan
        return slope / se_slope
    return lp.rolling(n, min_periods=YDAYS).apply(_k, raw=True)


def f31_rcmf_200_mfe_to_net_ratio_63d(close: pd.Series) -> pd.Series:
    """MFE/net: (max(close in 63d) − close[63d ago]) / (close − close[63d ago]) — favorable
    excursion vs realized net. Large = gave back gains. Sign reflects underlying direction.
    """
    start = close.shift(QDAYS)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    mfe = rmax - start
    net = close - start
    return _safe_div(mfe, net)


def f31_rcmf_201_mae_to_net_ratio_63d(close: pd.Series) -> pd.Series:
    """MAE/net: (min(close in 63d) − close[63d ago]) / (close − close[63d ago]) — adverse
    excursion vs realized net (path-pain to net-result ratio).
    """
    start = close.shift(QDAYS)
    rmin = close.rolling(QDAYS, min_periods=MDAYS).min()
    mae = rmin - start
    net = close - start
    return _safe_div(mae, net)


def f31_rcmf_202_mfe_minus_mae_252d(close: pd.Series) -> pd.Series:
    """(max − min) / start over 252d — total amplitude of price excursion in the year."""
    start = close.shift(YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(rmax - rmin, start)


def f31_rcmf_203_mfe_over_mae_252d(close: pd.Series) -> pd.Series:
    """|MFE| / |MAE| over 252d — favorable vs adverse excursion size ratio."""
    start = close.shift(YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    mfe = (rmax - start).abs()
    mae = (rmin - start).abs()
    return _safe_div(mfe, mae)


def f31_rcmf_204_efficiency_ratio_kaufman_63d(close: pd.Series) -> pd.Series:
    """Kaufman's Efficiency Ratio over 63d: |close - close.shift(63)| / sum(|1d diff|) over 63d."""
    net = (close - close.shift(QDAYS)).abs()
    abs_path = close.diff(1).abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, abs_path)


def f31_rcmf_205_efficiency_ratio_kaufman_252d(close: pd.Series) -> pd.Series:
    """Kaufman's Efficiency Ratio over 252d — annual price-path efficiency."""
    net = (close - close.shift(YDAYS)).abs()
    abs_path = close.diff(1).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, abs_path)


def f31_rcmf_206_efficiency_ratio_kaufman_504d(close: pd.Series) -> pd.Series:
    """Kaufman's Efficiency Ratio over 504d — biennial trend efficiency."""
    net = (close - close.shift(DDAYS_2Y)).abs()
    abs_path = close.diff(1).abs().rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(net, abs_path)


def f31_rcmf_207_signed_efficiency_ratio_252d(close: pd.Series) -> pd.Series:
    """Signed Kaufman ER: (close - close.shift(252)) / sum(|1d diff|) — directional ER."""
    net = close - close.shift(YDAYS)
    abs_path = close.diff(1).abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, abs_path)


def f31_rcmf_208_log_efficiency_ratio_252d(close: pd.Series) -> pd.Series:
    """Log-ER: |log_ret_252| / sum(|log_ret_1|) over 252d — efficiency in log space."""
    lr = _safe_log(close).diff(1)
    net = _safe_log(close).diff(YDAYS).abs()
    abs_path = lr.abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, abs_path)


def f31_rcmf_209_monotonicity_score_63d(close: pd.Series) -> pd.Series:
    """Monotonicity: (# positive 1d returns - # negative 1d returns) / 63 over trailing 63d."""
    r = close.pct_change(1)
    p = (r > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    n = (r < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(p - n, float(QDAYS))


def f31_rcmf_210_log_price_residual_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (log price − fitted-line value) over 252d — current deviation from linear trend
    standardized by residual std. Smoothness companion to K-ratio.
    """
    lp = _safe_log(close)
    n = YDAYS
    def _resid_z(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            xv = x[valid]; wv = w[valid]
        else:
            xv = x; wv = w
        xm = xv.mean(); wm = wv.mean()
        sxx = ((xv - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        slope = ((xv - xm) * (wv - wm)).sum() / sxx
        intercept = wm - slope * xm
        fitted_full = intercept + slope * x
        resid = w - fitted_full
        rsd = np.nanstd(resid, ddof=1)
        if not np.isfinite(rsd) or rsd == 0:
            return np.nan
        last = w[-1]
        last_fit = fitted_full[-1]
        if not np.isfinite(last) or not np.isfinite(last_fit):
            return np.nan
        return (last - last_fit) / rsd
    return lp.rolling(n, min_periods=QDAYS).apply(_resid_z, raw=True)


# ============================================================
# Bucket L — Drawdown-aware momentum (211-225 here, continues in 226-300 file)
# ============================================================

def f31_rcmf_211_max_drawdown_63d(close: pd.Series) -> pd.Series:
    """Maximum drawdown of close over trailing 63d (negative or zero)."""
    return _rolling_drawdown(close, QDAYS)


def f31_rcmf_212_max_drawdown_252d(close: pd.Series) -> pd.Series:
    """Maximum drawdown of close over trailing 252d (negative or zero)."""
    return _rolling_drawdown(close, YDAYS)


def f31_rcmf_213_max_drawdown_504d(close: pd.Series) -> pd.Series:
    """Maximum drawdown of close over trailing 504d (negative or zero)."""
    return _rolling_drawdown(close, DDAYS_2Y)


def f31_rcmf_214_max_drawdown_1260d(close: pd.Series) -> pd.Series:
    """Maximum drawdown of close over trailing 1260d (negative or zero) — 5y MDD."""
    return _rolling_drawdown(close, DDAYS_5Y)


def f31_rcmf_215_current_drawdown_from_252d_high(close: pd.Series) -> pd.Series:
    """Current drawdown from 252d high: close / max_252 − 1 (≤ 0)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(close, rmax) - 1.0


def f31_rcmf_216_current_drawdown_from_1260d_high(close: pd.Series) -> pd.Series:
    """Current drawdown from 1260d high: close / max_1260 − 1 (≤ 0) — 5y running-peak drawdown."""
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_div(close, rmax) - 1.0


def f31_rcmf_217_underwater_duration_252d(close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d high — underwater duration in days."""
    n = YDAYS
    def _u(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return close.rolling(n, min_periods=QDAYS).apply(_u, raw=True)


def f31_rcmf_218_underwater_duration_1260d(close: pd.Series) -> pd.Series:
    """Bars since the trailing-1260d high — 5y underwater duration."""
    n = DDAYS_5Y
    def _u(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        idx = int(np.nanargmax(w))
        return float(len(w) - 1 - idx)
    return close.rolling(n, min_periods=YDAYS).apply(_u, raw=True)


def f31_rcmf_219_recovery_half_life_252d(close: pd.Series) -> pd.Series:
    """Recovery half-life proxy: (1 + max_drawdown_252) / (close/min_252_post_dd - 1) approximated
    as |current_drawdown| / |max_drawdown_252| in (0,1]; near 1 = at trough, near 0 = recovered."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    cur_dd = _safe_div(close, rmax) - 1.0
    max_dd = _rolling_drawdown(close, YDAYS)
    return _safe_div(cur_dd, max_dd)


def f31_rcmf_220_days_since_max_drawdown_trough_252d(close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d argmin of close — days since deepest annual trough."""
    n = YDAYS
    def _b(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        idx = int(np.nanargmin(w))
        return float(len(w) - 1 - idx)
    return close.rolling(n, min_periods=QDAYS).apply(_b, raw=True)


def f31_rcmf_221_drawdown_to_volatility_ratio_252d(close: pd.Series) -> pd.Series:
    """|MaxDD_252| divided by 252d annualized return-vol — drawdown size in vol units."""
    dd = _rolling_drawdown(close, YDAYS).abs()
    sigma = close.pct_change(1).rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(dd, sigma)


def f31_rcmf_222_count_drawdowns_below_5pct_252d(close: pd.Series) -> pd.Series:
    """Number of distinct drawdowns deeper than −5% in trailing 252d (counts new trough beneath
    threshold after recovery above peak). Path-statistic of pullback frequency."""
    n = YDAYS
    def _cd(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = -np.inf
        in_dd = False
        count = 0
        for v in w:
            if not np.isfinite(v):
                continue
            if v >= peak:
                peak = v
                in_dd = False
            else:
                dd = v / peak - 1.0 if peak > 0 else 0.0
                if dd <= -0.05 and not in_dd:
                    count += 1
                    in_dd = True
        return float(count)
    return close.rolling(n, min_periods=QDAYS).apply(_cd, raw=True)


def f31_rcmf_223_count_drawdowns_below_10pct_504d(close: pd.Series) -> pd.Series:
    """Number of distinct drawdowns deeper than −10% in trailing 504d."""
    n = DDAYS_2Y
    def _cd(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        peak = -np.inf
        in_dd = False
        count = 0
        for v in w:
            if not np.isfinite(v):
                continue
            if v >= peak:
                peak = v
                in_dd = False
            else:
                dd = v / peak - 1.0 if peak > 0 else 0.0
                if dd <= -0.10 and not in_dd:
                    count += 1
                    in_dd = True
        return float(count)
    return close.rolling(n, min_periods=YDAYS).apply(_cd, raw=True)


def f31_rcmf_224_avg_drawdown_depth_252d(close: pd.Series) -> pd.Series:
    """Mean of trailing-252d daily drawdown-from-running-peak series — average underwater depth."""
    n = YDAYS
    def _a(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nanmean(dd))
    return close.rolling(n, min_periods=QDAYS).apply(_a, raw=True)


def f31_rcmf_225_pain_index_252d(close: pd.Series) -> pd.Series:
    """Becker's Pain Index over 252d: mean of |daily-drawdown-from-running-peak| (≥ 0)."""
    n = YDAYS
    def _p(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        peak = np.maximum.accumulate(w)
        dd = (w - peak) / np.where(peak == 0, np.nan, peak)
        return float(np.nanmean(np.abs(dd)))
    return close.rolling(n, min_periods=QDAYS).apply(_p, raw=True)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

ROC_MOMENTUM_FAMILY_BASE_REGISTRY_151_225 = {
    "f31_rcmf_151_momentum_12_1_skip": {"inputs": ["close"], "func": f31_rcmf_151_momentum_12_1_skip},
    "f31_rcmf_152_momentum_12_2_skip": {"inputs": ["close"], "func": f31_rcmf_152_momentum_12_2_skip},
    "f31_rcmf_153_momentum_9_1_skip": {"inputs": ["close"], "func": f31_rcmf_153_momentum_9_1_skip},
    "f31_rcmf_154_momentum_6_1_skip": {"inputs": ["close"], "func": f31_rcmf_154_momentum_6_1_skip},
    "f31_rcmf_155_long_term_reversal_36_12": {"inputs": ["close"], "func": f31_rcmf_155_long_term_reversal_36_12},
    "f31_rcmf_156_long_term_reversal_60_12": {"inputs": ["close"], "func": f31_rcmf_156_long_term_reversal_60_12},
    "f31_rcmf_157_short_term_reversal_1m": {"inputs": ["close"], "func": f31_rcmf_157_short_term_reversal_1m},
    "f31_rcmf_158_short_term_reversal_5d": {"inputs": ["close"], "func": f31_rcmf_158_short_term_reversal_5d},
    "f31_rcmf_159_fip_information_discreteness": {"inputs": ["close"], "func": f31_rcmf_159_fip_information_discreteness},
    "f31_rcmf_160_fip_information_discreteness_126d": {"inputs": ["close"], "func": f31_rcmf_160_fip_information_discreteness_126d},
    "f31_rcmf_161_fip_signed_id_252d": {"inputs": ["close"], "func": f31_rcmf_161_fip_signed_id_252d},
    "f31_rcmf_162_path_smoothness_weighted_12_1": {"inputs": ["close"], "func": f31_rcmf_162_path_smoothness_weighted_12_1},
    "f31_rcmf_163_intermediate_horizon_252_126": {"inputs": ["close"], "func": f31_rcmf_163_intermediate_horizon_252_126},
    "f31_rcmf_164_recent_horizon_126_0": {"inputs": ["close"], "func": f31_rcmf_164_recent_horizon_126_0},
    "f31_rcmf_165_echo_momentum_year_2": {"inputs": ["close"], "func": f31_rcmf_165_echo_momentum_year_2},
    "f31_rcmf_166_echo_momentum_year_3": {"inputs": ["close"], "func": f31_rcmf_166_echo_momentum_year_3},
    "f31_rcmf_167_echo_to_recent_ratio": {"inputs": ["close"], "func": f31_rcmf_167_echo_to_recent_ratio},
    "f31_rcmf_168_industry_momentum_proxy": {"inputs": ["close"], "func": f31_rcmf_168_industry_momentum_proxy},
    "f31_rcmf_169_double_skip_momentum_12_3": {"inputs": ["close"], "func": f31_rcmf_169_double_skip_momentum_12_3},
    "f31_rcmf_170_residual_recent_minus_skip": {"inputs": ["close"], "func": f31_rcmf_170_residual_recent_minus_skip},
    "f31_rcmf_171_sharpe_momentum_21d": {"inputs": ["close"], "func": f31_rcmf_171_sharpe_momentum_21d},
    "f31_rcmf_172_sharpe_momentum_63d": {"inputs": ["close"], "func": f31_rcmf_172_sharpe_momentum_63d},
    "f31_rcmf_173_sharpe_momentum_252d": {"inputs": ["close"], "func": f31_rcmf_173_sharpe_momentum_252d},
    "f31_rcmf_174_sortino_momentum_21d": {"inputs": ["close"], "func": f31_rcmf_174_sortino_momentum_21d},
    "f31_rcmf_175_sortino_momentum_63d": {"inputs": ["close"], "func": f31_rcmf_175_sortino_momentum_63d},
    "f31_rcmf_176_sortino_momentum_252d": {"inputs": ["close"], "func": f31_rcmf_176_sortino_momentum_252d},
    "f31_rcmf_177_calmar_momentum_63d": {"inputs": ["close"], "func": f31_rcmf_177_calmar_momentum_63d},
    "f31_rcmf_178_calmar_momentum_252d": {"inputs": ["close"], "func": f31_rcmf_178_calmar_momentum_252d},
    "f31_rcmf_179_calmar_momentum_504d": {"inputs": ["close"], "func": f31_rcmf_179_calmar_momentum_504d},
    "f31_rcmf_180_info_ratio_drift_to_activity_63d": {"inputs": ["close"], "func": f31_rcmf_180_info_ratio_drift_to_activity_63d},
    "f31_rcmf_181_info_ratio_drift_to_activity_252d": {"inputs": ["close"], "func": f31_rcmf_181_info_ratio_drift_to_activity_252d},
    "f31_rcmf_182_atr_normalized_roc_21d": {"inputs": ["close"], "func": f31_rcmf_182_atr_normalized_roc_21d},
    "f31_rcmf_183_atr_normalized_roc_63d": {"inputs": ["close"], "func": f31_rcmf_183_atr_normalized_roc_63d},
    "f31_rcmf_184_atr_normalized_roc_252d": {"inputs": ["close"], "func": f31_rcmf_184_atr_normalized_roc_252d},
    "f31_rcmf_185_upside_sharpe_252d": {"inputs": ["close"], "func": f31_rcmf_185_upside_sharpe_252d},
    "f31_rcmf_186_omega_ratio_proxy_63d": {"inputs": ["close"], "func": f31_rcmf_186_omega_ratio_proxy_63d},
    "f31_rcmf_187_omega_ratio_proxy_252d": {"inputs": ["close"], "func": f31_rcmf_187_omega_ratio_proxy_252d},
    "f31_rcmf_188_gain_to_pain_ratio_252d": {"inputs": ["close"], "func": f31_rcmf_188_gain_to_pain_ratio_252d},
    "f31_rcmf_189_sharpe_minus_sortino_252d": {"inputs": ["close"], "func": f31_rcmf_189_sharpe_minus_sortino_252d},
    "f31_rcmf_190_burke_ratio_proxy_252d": {"inputs": ["close"], "func": f31_rcmf_190_burke_ratio_proxy_252d},
    "f31_rcmf_191_momentum_consistency_subperiod_252d": {"inputs": ["close"], "func": f31_rcmf_191_momentum_consistency_subperiod_252d},
    "f31_rcmf_192_momentum_consistency_subperiod_504d": {"inputs": ["close"], "func": f31_rcmf_192_momentum_consistency_subperiod_504d},
    "f31_rcmf_193_hit_rate_5d_returns_63d": {"inputs": ["close"], "func": f31_rcmf_193_hit_rate_5d_returns_63d},
    "f31_rcmf_194_hit_rate_21d_returns_252d": {"inputs": ["close"], "func": f31_rcmf_194_hit_rate_21d_returns_252d},
    "f31_rcmf_195_path_tortuosity_252d": {"inputs": ["close"], "func": f31_rcmf_195_path_tortuosity_252d},
    "f31_rcmf_196_path_tortuosity_63d": {"inputs": ["close"], "func": f31_rcmf_196_path_tortuosity_63d},
    "f31_rcmf_197_k_ratio_log_price_63d": {"inputs": ["close"], "func": f31_rcmf_197_k_ratio_log_price_63d},
    "f31_rcmf_198_k_ratio_log_price_252d": {"inputs": ["close"], "func": f31_rcmf_198_k_ratio_log_price_252d},
    "f31_rcmf_199_k_ratio_log_price_504d": {"inputs": ["close"], "func": f31_rcmf_199_k_ratio_log_price_504d},
    "f31_rcmf_200_mfe_to_net_ratio_63d": {"inputs": ["close"], "func": f31_rcmf_200_mfe_to_net_ratio_63d},
    "f31_rcmf_201_mae_to_net_ratio_63d": {"inputs": ["close"], "func": f31_rcmf_201_mae_to_net_ratio_63d},
    "f31_rcmf_202_mfe_minus_mae_252d": {"inputs": ["close"], "func": f31_rcmf_202_mfe_minus_mae_252d},
    "f31_rcmf_203_mfe_over_mae_252d": {"inputs": ["close"], "func": f31_rcmf_203_mfe_over_mae_252d},
    "f31_rcmf_204_efficiency_ratio_kaufman_63d": {"inputs": ["close"], "func": f31_rcmf_204_efficiency_ratio_kaufman_63d},
    "f31_rcmf_205_efficiency_ratio_kaufman_252d": {"inputs": ["close"], "func": f31_rcmf_205_efficiency_ratio_kaufman_252d},
    "f31_rcmf_206_efficiency_ratio_kaufman_504d": {"inputs": ["close"], "func": f31_rcmf_206_efficiency_ratio_kaufman_504d},
    "f31_rcmf_207_signed_efficiency_ratio_252d": {"inputs": ["close"], "func": f31_rcmf_207_signed_efficiency_ratio_252d},
    "f31_rcmf_208_log_efficiency_ratio_252d": {"inputs": ["close"], "func": f31_rcmf_208_log_efficiency_ratio_252d},
    "f31_rcmf_209_monotonicity_score_63d": {"inputs": ["close"], "func": f31_rcmf_209_monotonicity_score_63d},
    "f31_rcmf_210_log_price_residual_zscore_252d": {"inputs": ["close"], "func": f31_rcmf_210_log_price_residual_zscore_252d},
    "f31_rcmf_211_max_drawdown_63d": {"inputs": ["close"], "func": f31_rcmf_211_max_drawdown_63d},
    "f31_rcmf_212_max_drawdown_252d": {"inputs": ["close"], "func": f31_rcmf_212_max_drawdown_252d},
    "f31_rcmf_213_max_drawdown_504d": {"inputs": ["close"], "func": f31_rcmf_213_max_drawdown_504d},
    "f31_rcmf_214_max_drawdown_1260d": {"inputs": ["close"], "func": f31_rcmf_214_max_drawdown_1260d},
    "f31_rcmf_215_current_drawdown_from_252d_high": {"inputs": ["close"], "func": f31_rcmf_215_current_drawdown_from_252d_high},
    "f31_rcmf_216_current_drawdown_from_1260d_high": {"inputs": ["close"], "func": f31_rcmf_216_current_drawdown_from_1260d_high},
    "f31_rcmf_217_underwater_duration_252d": {"inputs": ["close"], "func": f31_rcmf_217_underwater_duration_252d},
    "f31_rcmf_218_underwater_duration_1260d": {"inputs": ["close"], "func": f31_rcmf_218_underwater_duration_1260d},
    "f31_rcmf_219_recovery_half_life_252d": {"inputs": ["close"], "func": f31_rcmf_219_recovery_half_life_252d},
    "f31_rcmf_220_days_since_max_drawdown_trough_252d": {"inputs": ["close"], "func": f31_rcmf_220_days_since_max_drawdown_trough_252d},
    "f31_rcmf_221_drawdown_to_volatility_ratio_252d": {"inputs": ["close"], "func": f31_rcmf_221_drawdown_to_volatility_ratio_252d},
    "f31_rcmf_222_count_drawdowns_below_5pct_252d": {"inputs": ["close"], "func": f31_rcmf_222_count_drawdowns_below_5pct_252d},
    "f31_rcmf_223_count_drawdowns_below_10pct_504d": {"inputs": ["close"], "func": f31_rcmf_223_count_drawdowns_below_10pct_504d},
    "f31_rcmf_224_avg_drawdown_depth_252d": {"inputs": ["close"], "func": f31_rcmf_224_avg_drawdown_depth_252d},
    "f31_rcmf_225_pain_index_252d": {"inputs": ["close"], "func": f31_rcmf_225_pain_index_252d},
}
