"""blowoff_climax_composite base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. THEME:
multi-signal blowoff/climax composites. Each feature COMBINES two-or-more
independent signals (price + volume / price + momentum / price + range / etc.)
into a single indicator. Distinguished from family 02 (parabolic-only),
family 19 (volume-only blowoff), and family 25 (RSI-only) by requiring
multi-signal confluence.

Bucket A: 2-signal price + volume blowoff.
Bucket B: 2-signal price + momentum blowoff.
Bucket C: Sharpe-like / quality climax (return / std).
Bucket D: 3-signal composites (price + vol + momentum, etc.).
Bucket E: Sequence patterns of climax (multi-bar runs of co-occurring signals).
Bucket F: Post-climax confirmation signatures (failed-high, reversal day, etc.).
Bucket G: ATR / volatility composite blowoff.

Inputs: SEP OHLCV. Self-contained helpers; PIT-clean.
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


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0); dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0 / (1.0 + _safe_div(au, ad))


def _clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _stoch_k(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0.0)
    neg = rmf.where(delta < 0, 0.0)
    ps = pos.rolling(n, min_periods=max(n // 3, 2)).sum()
    ns = neg.rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(ps, ns)
    return 100.0 - 100.0 / (1.0 + mr)


# ============================================================
# Bucket A — 2-signal price + volume blowoff (001-012)
# ============================================================

def f49_bcco_001_new_21d_high_and_vol_2x_21d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 21d high AND volume > 2x 21d-avg volume — short-term price+vol blowoff."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return (new_high & (v_ratio > 2.0)).astype(float).where(v_ratio.notna(), np.nan)


def f49_bcco_002_new_63d_high_and_vol_3x_63d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 63d high AND volume > 3x 63d-avg volume."""
    new_high = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(QDAYS, min_periods=MDAYS).mean())
    return (new_high & (v_ratio > 3.0)).astype(float).where(v_ratio.notna(), np.nan)


def f49_bcco_003_new_252d_high_and_vol_2x_252d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND volume > 2x 252d-avg — annual blowoff."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    return (new_high & (v_ratio > 2.0)).astype(float).where(v_ratio.notna(), np.nan)


def f49_bcco_004_new_252d_high_and_vol_3x_252d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND volume > 3x 252d-avg — strong-vol blowoff."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    return (new_high & (v_ratio > 3.0)).astype(float).where(v_ratio.notna(), np.nan)


def f49_bcco_005_new_252d_high_and_tr_2x_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND TR > 2x ATR21 — annual high on wide-range bar."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (new_high & (rng_ratio > 2.0)).astype(float).where(rng_ratio.notna(), np.nan)


def f49_bcco_006_ret21_over_30pct_and_vol_2x_21d_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 21d return > 30% AND vol > 2x 21d avg — monthly parabolic with vol."""
    r = close.pct_change(MDAYS)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return ((r > 0.30) & (v_ratio > 2.0)).astype(float).where(r.notna() & v_ratio.notna(), np.nan)


def f49_bcco_007_ret63_over_100pct_and_vol_2x_63d_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 63d return > 100% AND vol > 2x 63d avg — quarterly parabolic with vol."""
    r = close.pct_change(QDAYS)
    v_ratio = _safe_div(volume, volume.rolling(QDAYS, min_periods=MDAYS).mean())
    return ((r > 1.0) & (v_ratio > 2.0)).astype(float).where(r.notna() & v_ratio.notna(), np.nan)


def f49_bcco_008_ret252_over_200pct_and_vol_2x_252d_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 252d return > 200% AND vol > 2x 252d avg — annual parabolic with vol."""
    r = close.pct_change(YDAYS)
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    return ((r > 2.0) & (v_ratio > 2.0)).astype(float).where(r.notna() & v_ratio.notna(), np.nan)


def f49_bcco_009_new_504d_high_and_vol_3x_504d_avg(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 504d high AND vol > 3x 504d-avg — multi-year blowoff."""
    new_high = high >= high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(DDAYS_2Y, min_periods=YDAYS).mean())
    return (new_high & (v_ratio > 3.0)).astype(float).where(v_ratio.notna(), np.nan)


def f49_bcco_010_new_252d_high_and_new_252d_atr_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d price high AND ATR21 at its 252d max — concurrent price+vol-of-price peak."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    a = _atr(high, low, close, MDAYS)
    atr_at_max = a >= a.rolling(YDAYS, min_periods=QDAYS).max()
    return (new_high & atr_at_max).astype(float).where(a.notna(), np.nan)


def f49_bcco_011_new_252d_high_and_prior_21d_ret_over_30pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND 21d return > 30% — annual high after strong run."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r = close.pct_change(MDAYS)
    return (new_high & (r > 0.30)).astype(float).where(r.notna(), np.nan)


def f49_bcco_012_new_252d_high_and_5_consecutive_up_closes(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND 5+ consecutive up-close days — momentum-confirmed annual blowoff."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    up_streak = _streak_true(close > close.shift(1))
    return (new_high & (up_streak >= 5)).astype(float).where(close.shift(1).notna(), np.nan)


# ============================================================
# Bucket B — 2-signal price + momentum blowoff (013-024)
# ============================================================

def f49_bcco_013_new_21d_high_and_rsi14_over_70(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND RSI(14) > 70 — short-term price+momentum OB."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r > 70.0)).astype(float).where(r.notna(), np.nan)


def f49_bcco_014_new_63d_high_and_rsi14_over_80(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 63d high AND RSI(14) > 80 — quarterly high with strong-OB."""
    new_high = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r > 80.0)).astype(float).where(r.notna(), np.nan)


def f49_bcco_015_new_252d_high_and_rsi14_over_70(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI(14) > 70 — annual high with OB."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r > 70.0)).astype(float).where(r.notna(), np.nan)


def f49_bcco_016_new_252d_high_and_rsi14_over_85(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI(14) > 85 — extreme-OB blowoff."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r > 85.0)).astype(float).where(r.notna(), np.nan)


def f49_bcco_017_new_252d_high_and_stoch_k_over_90(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND Stoch K(14) > 90 — annual high with extreme Stoch."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    k = _stoch_k(high, low, close, 14)
    return (new_high & (k > 90.0)).astype(float).where(k.notna(), np.nan)


def f49_bcco_018_new_252d_high_and_mfi_over_80(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND MFI(14) > 80 — annual high with vol-confirmed OB."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    m = _mfi(high, low, close, volume, 14)
    return (new_high & (m > 80.0)).astype(float).where(m.notna(), np.nan)


def f49_bcco_019_new_252d_high_and_roc63_over_100pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND ROC(63) > 100% — annual high with quarterly parabolic ROC."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    roc = close.pct_change(QDAYS)
    return (new_high & (roc > 1.0)).astype(float).where(roc.notna(), np.nan)


def f49_bcco_020_new_252d_high_and_macd_hist_top_decile_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND MACD-hist > its trailing 252d 90th-pct — annual high with top-decile MACD."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    macd = close.ewm(span=12, adjust=False, min_periods=12).mean() - close.ewm(span=26, adjust=False, min_periods=26).mean()
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = macd - sig
    q90 = hist.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (new_high & (hist > q90)).astype(float).where(q90.notna(), np.nan)


def f49_bcco_021_new_252d_high_and_rsi_zscore_over_2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI(14) z-score (252d) > 2 — annual high with extreme-RSI z."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    rz = _rolling_zscore(_rsi(close, 14), YDAYS, min_periods=QDAYS)
    return (new_high & (rz > 2.0)).astype(float).where(rz.notna(), np.nan)


def f49_bcco_022_new_21d_high_and_momentum_3rd_diff_positive(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND 3rd-derivative of close > 0 — short-term high with momentum jerk."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    jerk = close.diff().diff().diff()
    return (new_high & (jerk > 0)).astype(float).where(jerk.notna(), np.nan)


def f49_bcco_023_new_63d_high_and_price_slope_21d_above_1pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 63d high AND 21d slope of log-price > log(1.01) — strong-trend confirmation."""
    new_high = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    sl = _rolling_slope(_safe_log(close), MDAYS)
    return (new_high & (sl > np.log(1.01))).astype(float).where(sl.notna(), np.nan)


def f49_bcco_024_new_252d_high_and_21d_log_ret_over_30pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND 21d log-return > 0.30 — annual high after strong monthly log-return."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    lr = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return (new_high & (lr > 0.30)).astype(float).where(lr.notna(), np.nan)


# ============================================================
# Bucket C — Sharpe-like / quality climax (025-034)
# ============================================================

def f49_bcco_025_sharpe_21_over_3(close: pd.Series) -> pd.Series:
    """1 if 21d (mean return / std return) > 3 — extreme-sharpe monthly climax."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, sd)
    return (s > 3.0).astype(float).where(s.notna(), np.nan)


def f49_bcco_026_sharpe_21_over_4_extreme(close: pd.Series) -> pd.Series:
    """1 if 21d sharpe > 4 — extreme climax (distinct severity)."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, sd)
    return (s > 4.0).astype(float).where(s.notna(), np.nan)


def f49_bcco_027_sharpe_63_over_2(close: pd.Series) -> pd.Series:
    """1 if 63d sharpe > 2 — quarterly elevated sharpe."""
    r = close.pct_change()
    mn = r.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    s = _safe_div(mn, sd)
    return (s > 2.0).astype(float).where(s.notna(), np.nan)


def f49_bcco_028_sortino_21_over_5(close: pd.Series) -> pd.Series:
    """1 if 21d sortino (mean / downside-std) > 5 — sortino-climax."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    dsd = r.where(r < 0).rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, dsd)
    return (s > 5.0).astype(float).where(s.notna(), np.nan)


def f49_bcco_029_sortino_63_over_3(close: pd.Series) -> pd.Series:
    """1 if 63d sortino > 3 — quarterly sortino climax."""
    r = close.pct_change()
    mn = r.rolling(QDAYS, min_periods=MDAYS).mean()
    dsd = r.where(r < 0).rolling(QDAYS, min_periods=MDAYS).std()
    s = _safe_div(mn, dsd)
    return (s > 3.0).astype(float).where(s.notna(), np.nan)


def f49_bcco_030_max_sharpe_21_past_63(close: pd.Series) -> pd.Series:
    """Max 21d sharpe over past 63 bars — peak sharpe in recent quarter."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(mn, sd).rolling(QDAYS, min_periods=MDAYS).max()


def f49_bcco_031_max_sharpe_21_past_252(close: pd.Series) -> pd.Series:
    """Annual peak 21d sharpe — best monthly risk-adjusted return seen in the past year."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    return _safe_div(mn, sd).rolling(YDAYS, min_periods=QDAYS).max()


def f49_bcco_032_sharpe_above_2_dwell_21(close: pd.Series) -> pd.Series:
    """Fraction past 21 bars with 21d sharpe > 2 — sharpe-OB monthly dwell."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, sd)
    return (s > 2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(s.notna(), np.nan)


def f49_bcco_033_sharpe_above_2_dwell_63(close: pd.Series) -> pd.Series:
    """Quarterly sharpe-OB dwell."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, sd)
    return (s > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)


def f49_bcco_034_bars_since_sharpe_over_3(close: pd.Series) -> pd.Series:
    """Bars since 21d sharpe > 3 last fired — climax recency."""
    r = close.pct_change()
    mn = r.rolling(MDAYS, min_periods=WDAYS).mean()
    sd = r.rolling(MDAYS, min_periods=WDAYS).std()
    s = _safe_div(mn, sd)
    return _bars_since_true(s > 3.0)


# ============================================================
# Bucket D — 3-signal composites (035-046)
# ============================================================

def f49_bcco_035_triple_high_vol_rsi(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND vol > 2x avg AND RSI(14) > 80 — triple confluence."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    r = _rsi(close, 14)
    return (new_high & (v_ratio > 2.0) & (r > 80.0)).astype(float).where(v_ratio.notna() & r.notna(), np.nan)


def f49_bcco_036_triple_high_vol_range(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND vol > 3x avg AND TR > 2x ATR21 — high+vol+range triple."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (new_high & (v_ratio > 3.0) & (rng_ratio > 2.0)).astype(float).where(v_ratio.notna() & rng_ratio.notna(), np.nan)


def f49_bcco_037_triple_high_wide_strongclose(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND wide-range bar (TR > 2x ATR21) AND CLV > 0.5 — strong-close climax."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (new_high & (rng_ratio > 2.0) & (_clv(high, low, close) > 0.5)).astype(float).where(rng_ratio.notna(), np.nan)


def f49_bcco_038_triple_high_strong_ret_strong_rsi(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND 21d return > 30% AND RSI(14) > 80."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r21 = close.pct_change(MDAYS)
    rsi = _rsi(close, 14)
    return (new_high & (r21 > 0.30) & (rsi > 80.0)).astype(float).where(r21.notna() & rsi.notna(), np.nan)


def f49_bcco_039_triple_high_vol_jerk(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND vol > 2x avg AND 3rd-diff of close > 0 — high+vol+momentum-jerk."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    jerk = close.diff().diff().diff()
    return (new_high & (v_ratio > 2.0) & (jerk > 0)).astype(float).where(v_ratio.notna() & jerk.notna(), np.nan)


def f49_bcco_040_triple_parabolic_widerange_volspike(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 63d return > 50% AND TR > 2x ATR21 AND vol > 3x 21d-avg — parabolic+wide+vol-spike."""
    r = close.pct_change(QDAYS)
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return ((r > 0.5) & (rng_ratio > 2.0) & (v_ratio > 3.0)).astype(float).where(r.notna() & rng_ratio.notna() & v_ratio.notna(), np.nan)


def f49_bcco_041_triple_parabolic_rsi_atr_expanded(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d return > 50% AND RSI(14) > 80 AND ATR21/ATR63 > 1.5 — parabolic+OB+vol-expansion."""
    r = close.pct_change(QDAYS)
    rsi = _rsi(close, 14)
    atr_exp = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS))
    return ((r > 0.5) & (rsi > 80.0) & (atr_exp > 1.5)).astype(float).where(r.notna() & rsi.notna() & atr_exp.notna(), np.nan)


def f49_bcco_042_triple_parabolic_new504_high_strongclose(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d return > 50% AND new 504d high AND CLV > 0.7 — parabolic+multi-year-high+strong-close."""
    r = close.pct_change(QDAYS)
    new_504 = high >= high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return ((r > 0.5) & new_504 & (_clv(high, low, close) > 0.7)).astype(float).where(r.notna(), np.nan)


def f49_bcco_043_triple_parabolic_new252_high_extreme_rsi(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d return > 50% AND new 252d high AND RSI(14) > 90 — parabolic+annual-high+extreme-OB."""
    r = close.pct_change(QDAYS)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    rsi = _rsi(close, 14)
    return ((r > 0.5) & new_high & (rsi > 90.0)).astype(float).where(r.notna() & rsi.notna(), np.nan)


def f49_bcco_044_bull_trap_prior_new_high_then_wide_down(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's close < open AND TR > 2x ATR21 — bull-trap signature."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax.shift(1))
    today_bearish_wide = ((close < close.shift(1)) & (_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)) > 2.0))
    return (prior_new_high & today_bearish_wide).astype(float).where(rmax.shift(1).notna(), np.nan)


def f49_bcco_045_quadruple_high_vol_rsi_widerange(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 252d high AND vol > 2x AND RSI > 80 AND TR > 2x ATR21 — 4-signal blowoff."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean())
    r = _rsi(close, 14)
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (new_high & (v_ratio > 2.0) & (r > 80.0) & (rng_ratio > 2.0)).astype(float).where(v_ratio.notna() & r.notna() & rng_ratio.notna(), np.nan)


def f49_bcco_046_count_signals_at_bar(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count {new 252d high, vol>2x, RSI>80, TR>2xATR21, CLV>0.5} signals firing on current bar."""
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    v_ratio = (_safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean()) > 2.0).astype(float)
    r = (_rsi(close, 14) > 80.0).astype(float)
    rng_ratio = (_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)) > 2.0).astype(float)
    cl = (_clv(high, low, close) > 0.5).astype(float)
    return new_high.fillna(0) + v_ratio.fillna(0) + r.fillna(0) + rng_ratio.fillna(0) + cl.fillna(0)


# ============================================================
# Bucket E — Sequence patterns of climax (047-058)
# ============================================================

def f49_bcco_047_three_consecutive_new_21d_highs_rising_vol(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3 consecutive new 21d highs AND vol rising (vol > vol[t-3])."""
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max())
    cons = new_high & new_high.shift(1) & new_high.shift(2)
    return (cons & (volume > volume.shift(3))).astype(float).where(new_high.notna(), np.nan)


def f49_bcco_048_five_consecutive_new_21d_highs_rising_vol(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5 consecutive new 21d highs AND vol rising (vol > vol[t-5])."""
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max())
    cons = new_high & new_high.shift(1) & new_high.shift(2) & new_high.shift(3) & new_high.shift(4)
    return (cons & (volume > volume.shift(WDAYS))).astype(float).where(new_high.notna(), np.nan)


def f49_bcco_049_ten_consecutive_up_close_days(close: pd.Series) -> pd.Series:
    """1 if 10 consecutive up-close days — sustained-up-pressure run."""
    return (_streak_true(close > close.shift(1)) >= 10).astype(float).where(close.shift(1).notna(), np.nan)


def f49_bcco_050_five_consecutive_wide_range_bars(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5 consecutive bars with TR > 2x ATR21 — sustained wide-range run."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (_streak_true(rng_ratio > 2.0) >= 5).astype(float).where(rng_ratio.notna(), np.nan)


def f49_bcco_051_five_consecutive_strong_close_clv_above_half(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5 consecutive bars with CLV > 0.5 — sustained close-near-top run."""
    return (_streak_true(_clv(high, low, close) > 0.5) >= 5).astype(float)


def f49_bcco_052_new_21d_high_with_3bar_ema_vol_2x_63d_ema(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 21d high AND 3-bar EMA(vol) > 2x 63d EMA(vol)."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    v3 = volume.ewm(span=3, adjust=False, min_periods=3).mean()
    v63 = volume.ewm(span=QDAYS, adjust=False, min_periods=QDAYS).mean()
    return (new_high & (v3 > 2.0 * v63)).astype(float).where(v3.notna() & v63.notna(), np.nan)


def f49_bcco_053_new_252d_high_each_of_past_5_bars(high: pd.Series) -> pd.Series:
    """1 if new 252d high was achieved in EACH of past 5 bars — sustained breakout."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high >= rmax
    return (new_high & new_high.shift(1) & new_high.shift(2) & new_high.shift(3) & new_high.shift(4)).astype(float).where(rmax.notna(), np.nan)


def f49_bcco_054_new_21d_high_with_rising_rsi_t_minus_5(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND RSI(14) > RSI(14)[t-5] — high with rising momentum."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r > r.shift(WDAYS))).astype(float).where(r.notna(), np.nan)


def f49_bcco_055_new_252d_high_with_rsi_at_252d_max(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND RSI(14) at 252d max — price-momentum confluence at peak."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r >= r.rolling(YDAYS, min_periods=QDAYS).max())).astype(float).where(r.notna(), np.nan)


def f49_bcco_056_new_21d_high_with_rising_volume_t_minus_5(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if new 21d high AND volume > volume[t-5] — high with rising vol."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (new_high & (volume > volume.shift(WDAYS))).astype(float).where(volume.shift(WDAYS).notna(), np.nan)


def f49_bcco_057_5d_cum_ret_over_20pct_with_new_high_in_window(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5d cum return > 20% AND any new 21d high occurred in past 5 bars."""
    r5 = close.pct_change(WDAYS)
    new_high_21 = (high >= high.rolling(MDAYS, min_periods=WDAYS).max())
    any_new_high_5 = new_high_21.rolling(WDAYS, min_periods=1).max() > 0
    return ((r5 > 0.20) & any_new_high_5).astype(float).where(r5.notna(), np.nan)


def f49_bcco_058_10d_cum_ret_over_40pct_with_multiple_new_highs(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 10d cum return > 40% AND 3+ new 21d highs in past 10 bars."""
    r10 = close.pct_change(10)
    new_high_21 = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    count_10 = new_high_21.rolling(10, min_periods=3).sum()
    return ((r10 > 0.40) & (count_10 >= 3)).astype(float).where(r10.notna(), np.nan)


# ============================================================
# Bucket F — Post-climax confirmation signatures (059-068)
# ============================================================

def f49_bcco_059_failed_new_21d_high_with_close_below_open(high: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high made today AND close < open — failed-new-high bearish candle."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (new_high & (close < open_)).astype(float).where(new_high.notna(), np.nan)


def f49_bcco_060_failed_new_high_cluster_3_in_5(high: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3+ failed-new-high bars in past 5 — cluster of failed highs."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    failed = (new_high & (close < open_)).astype(float)
    return (failed.rolling(WDAYS, min_periods=2).sum() >= 3).astype(float).where(new_high.notna(), np.nan)


def f49_bcco_061_new_high_and_rsi_falling_bearish_div(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND RSI(14) < its 21d rolling max — bearish RSI divergence at high."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    r = _rsi(close, 14)
    return (new_high & (r < r.shift(1).rolling(MDAYS, min_periods=WDAYS).max())).astype(float).where(r.notna(), np.nan)


def f49_bcco_062_new_high_with_clv_below_02(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND CLV < 0.2 — high touched but closed weak (poor-close)."""
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (new_high & (_clv(high, low, close) < 0.2)).astype(float).where(new_high.notna(), np.nan)


def f49_bcco_063_reversal_day_new_21d_high_close_below_prev_low(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND close < prior bar's low — key reversal day."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (new_high & (close < low.shift(1))).astype(float).where(low.shift(1).notna(), np.nan)


def f49_bcco_064_reversal_day_count_past_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of reversal-day events in past 21 bars."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    rev = (new_high & (close < low.shift(1))).astype(float)
    return rev.rolling(MDAYS, min_periods=WDAYS).sum().where(low.shift(1).notna(), np.nan)


def f49_bcco_065_new_252d_high_then_next_bar_minus_5pct(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's return < -5% — climax-then-crash (PIT-safe, backward-looking)."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    return (prior_new_high & (close.pct_change() < -0.05)).astype(float).where(rmax_prev.notna(), np.nan)


def f49_bcco_066_exhaustion_gap_up_then_close_below_open(open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if open gap > 3% AND close < open — exhaustion gap-and-crap pattern."""
    pc = close.shift(1)
    gap = _safe_div(open_ - pc, pc)
    return ((gap > 0.03) & (close < open_)).astype(float).where(gap.notna(), np.nan)


def f49_bcco_067_bearish_engulfing_after_new_252d_high(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today's body engulfs prior body bearishly (today close<open, today's body > prior's body)."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    prior_new_high = (high.shift(1) >= rmax_prev)
    today_bear = (close < open_)
    today_body = (open_ - close).abs()
    prior_body = (open_.shift(1) - close.shift(1)).abs()
    engulf = (today_body > prior_body) & (open_ > close.shift(1)) & (close < open_.shift(1))
    return (prior_new_high & today_bear & engulf).astype(float).where(rmax_prev.notna(), np.nan)


def f49_bcco_068_blowoff_and_fade_new_21d_high_close_bottom_quartile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 21d high AND CLV < 0.25 — blowoff-and-fade (high reached, close in bottom-25%)."""
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (new_high & (_clv(high, low, close) < 0.25)).astype(float).where(new_high.notna(), np.nan)


# ============================================================
# Bucket G — ATR/volatility composite blowoff (069-075)
# ============================================================

def f49_bcco_069_atr21_at_252d_max_and_new_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 at its 252d max AND price at new 252d high."""
    a = _atr(high, low, close, MDAYS)
    atr_max = a >= a.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (atr_max & new_high).astype(float).where(a.notna(), np.nan)


def f49_bcco_070_atr21_at_504d_max_and_new_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 at 504d max AND price at new 252d high — multi-year vol peak with annual price peak."""
    a = _atr(high, low, close, MDAYS)
    atr_max = a >= a.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (atr_max & new_high).astype(float).where(a.notna(), np.nan)


def f49_bcco_071_atr_expand_and_parabolic_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21/ATR252 > 2 AND 63d return > 50% — vol-expansion+quarterly parabolic."""
    expansion = _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))
    r = close.pct_change(QDAYS)
    return ((expansion > 2.0) & (r > 0.5)).astype(float).where(expansion.notna() & r.notna(), np.nan)


def f49_bcco_072_realized_vol_21_at_252d_max_and_new_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d realized-vol at 252d max AND new 252d price high."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    rv_max = rv >= rv.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (rv_max & new_high).astype(float).where(rv.notna(), np.nan)


def f49_bcco_073_bollinger_upper_walk_5_bars(close: pd.Series) -> pd.Series:
    """1 if close > BB upper band (20, 2sigma) for 5+ consecutive bars — Bollinger-walk pattern."""
    m = close.rolling(20, min_periods=10).mean()
    s = close.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    return (_streak_true(close > upper) >= 5).astype(float).where(upper.notna(), np.nan)


def f49_bcco_074_bollinger_walk_with_new_252d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BB upper walk (5 bars) AND new 252d high — strong-trend climax."""
    m = close.rolling(20, min_periods=10).mean()
    s = close.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    walk = (_streak_true(close > upper) >= 5)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    return (walk & new_high).astype(float).where(upper.notna(), np.nan)


def f49_bcco_075_bollinger_walk_new_high_vol_spike(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if BB upper walk AND new 252d high AND vol > 2x 21d avg — multi-condition Bollinger climax."""
    m = close.rolling(20, min_periods=10).mean()
    s = close.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    walk = (_streak_true(close > upper) >= 5)
    new_high = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return (walk & new_high & (v_ratio > 2.0)).astype(float).where(upper.notna() & v_ratio.notna(), np.nan)


# ============================================================
#                         REGISTRY 001-075
# ============================================================

_HV = ["high", "volume"]
_HC = ["high", "close"]
_HCV = ["high", "close", "volume"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_OHLC = ["open", "high", "low", "close"]
_OC = ["open", "close"]
_OHC = ["open", "high", "close"]

BLOWOFF_CLIMAX_COMPOSITE_BASE_REGISTRY_001_075 = {
    "f49_bcco_001_new_21d_high_and_vol_2x_21d_avg": {"inputs": _HV, "func": f49_bcco_001_new_21d_high_and_vol_2x_21d_avg},
    "f49_bcco_002_new_63d_high_and_vol_3x_63d_avg": {"inputs": _HV, "func": f49_bcco_002_new_63d_high_and_vol_3x_63d_avg},
    "f49_bcco_003_new_252d_high_and_vol_2x_252d_avg": {"inputs": _HV, "func": f49_bcco_003_new_252d_high_and_vol_2x_252d_avg},
    "f49_bcco_004_new_252d_high_and_vol_3x_252d_avg": {"inputs": _HV, "func": f49_bcco_004_new_252d_high_and_vol_3x_252d_avg},
    "f49_bcco_005_new_252d_high_and_tr_2x_atr21": {"inputs": _HLC, "func": f49_bcco_005_new_252d_high_and_tr_2x_atr21},
    "f49_bcco_006_ret21_over_30pct_and_vol_2x_21d_avg": {"inputs": ["close", "volume"], "func": f49_bcco_006_ret21_over_30pct_and_vol_2x_21d_avg},
    "f49_bcco_007_ret63_over_100pct_and_vol_2x_63d_avg": {"inputs": ["close", "volume"], "func": f49_bcco_007_ret63_over_100pct_and_vol_2x_63d_avg},
    "f49_bcco_008_ret252_over_200pct_and_vol_2x_252d_avg": {"inputs": ["close", "volume"], "func": f49_bcco_008_ret252_over_200pct_and_vol_2x_252d_avg},
    "f49_bcco_009_new_504d_high_and_vol_3x_504d_avg": {"inputs": _HV, "func": f49_bcco_009_new_504d_high_and_vol_3x_504d_avg},
    "f49_bcco_010_new_252d_high_and_new_252d_atr_high": {"inputs": _HLC, "func": f49_bcco_010_new_252d_high_and_new_252d_atr_high},
    "f49_bcco_011_new_252d_high_and_prior_21d_ret_over_30pct": {"inputs": _HC, "func": f49_bcco_011_new_252d_high_and_prior_21d_ret_over_30pct},
    "f49_bcco_012_new_252d_high_and_5_consecutive_up_closes": {"inputs": _HC, "func": f49_bcco_012_new_252d_high_and_5_consecutive_up_closes},
    "f49_bcco_013_new_21d_high_and_rsi14_over_70": {"inputs": _HC, "func": f49_bcco_013_new_21d_high_and_rsi14_over_70},
    "f49_bcco_014_new_63d_high_and_rsi14_over_80": {"inputs": _HC, "func": f49_bcco_014_new_63d_high_and_rsi14_over_80},
    "f49_bcco_015_new_252d_high_and_rsi14_over_70": {"inputs": _HC, "func": f49_bcco_015_new_252d_high_and_rsi14_over_70},
    "f49_bcco_016_new_252d_high_and_rsi14_over_85": {"inputs": _HC, "func": f49_bcco_016_new_252d_high_and_rsi14_over_85},
    "f49_bcco_017_new_252d_high_and_stoch_k_over_90": {"inputs": _HLC, "func": f49_bcco_017_new_252d_high_and_stoch_k_over_90},
    "f49_bcco_018_new_252d_high_and_mfi_over_80": {"inputs": _HLCV, "func": f49_bcco_018_new_252d_high_and_mfi_over_80},
    "f49_bcco_019_new_252d_high_and_roc63_over_100pct": {"inputs": _HC, "func": f49_bcco_019_new_252d_high_and_roc63_over_100pct},
    "f49_bcco_020_new_252d_high_and_macd_hist_top_decile_252": {"inputs": _HC, "func": f49_bcco_020_new_252d_high_and_macd_hist_top_decile_252},
    "f49_bcco_021_new_252d_high_and_rsi_zscore_over_2": {"inputs": _HC, "func": f49_bcco_021_new_252d_high_and_rsi_zscore_over_2},
    "f49_bcco_022_new_21d_high_and_momentum_3rd_diff_positive": {"inputs": _HC, "func": f49_bcco_022_new_21d_high_and_momentum_3rd_diff_positive},
    "f49_bcco_023_new_63d_high_and_price_slope_21d_above_1pct": {"inputs": _HC, "func": f49_bcco_023_new_63d_high_and_price_slope_21d_above_1pct},
    "f49_bcco_024_new_252d_high_and_21d_log_ret_over_30pct": {"inputs": _HC, "func": f49_bcco_024_new_252d_high_and_21d_log_ret_over_30pct},
    "f49_bcco_025_sharpe_21_over_3": {"inputs": ["close"], "func": f49_bcco_025_sharpe_21_over_3},
    "f49_bcco_026_sharpe_21_over_4_extreme": {"inputs": ["close"], "func": f49_bcco_026_sharpe_21_over_4_extreme},
    "f49_bcco_027_sharpe_63_over_2": {"inputs": ["close"], "func": f49_bcco_027_sharpe_63_over_2},
    "f49_bcco_028_sortino_21_over_5": {"inputs": ["close"], "func": f49_bcco_028_sortino_21_over_5},
    "f49_bcco_029_sortino_63_over_3": {"inputs": ["close"], "func": f49_bcco_029_sortino_63_over_3},
    "f49_bcco_030_max_sharpe_21_past_63": {"inputs": ["close"], "func": f49_bcco_030_max_sharpe_21_past_63},
    "f49_bcco_031_max_sharpe_21_past_252": {"inputs": ["close"], "func": f49_bcco_031_max_sharpe_21_past_252},
    "f49_bcco_032_sharpe_above_2_dwell_21": {"inputs": ["close"], "func": f49_bcco_032_sharpe_above_2_dwell_21},
    "f49_bcco_033_sharpe_above_2_dwell_63": {"inputs": ["close"], "func": f49_bcco_033_sharpe_above_2_dwell_63},
    "f49_bcco_034_bars_since_sharpe_over_3": {"inputs": ["close"], "func": f49_bcco_034_bars_since_sharpe_over_3},
    "f49_bcco_035_triple_high_vol_rsi": {"inputs": _HCV, "func": f49_bcco_035_triple_high_vol_rsi},
    "f49_bcco_036_triple_high_vol_range": {"inputs": _HLCV, "func": f49_bcco_036_triple_high_vol_range},
    "f49_bcco_037_triple_high_wide_strongclose": {"inputs": _HLC, "func": f49_bcco_037_triple_high_wide_strongclose},
    "f49_bcco_038_triple_high_strong_ret_strong_rsi": {"inputs": _HC, "func": f49_bcco_038_triple_high_strong_ret_strong_rsi},
    "f49_bcco_039_triple_high_vol_jerk": {"inputs": _HCV, "func": f49_bcco_039_triple_high_vol_jerk},
    "f49_bcco_040_triple_parabolic_widerange_volspike": {"inputs": _HLCV, "func": f49_bcco_040_triple_parabolic_widerange_volspike},
    "f49_bcco_041_triple_parabolic_rsi_atr_expanded": {"inputs": _HLC, "func": f49_bcco_041_triple_parabolic_rsi_atr_expanded},
    "f49_bcco_042_triple_parabolic_new504_high_strongclose": {"inputs": _HLC, "func": f49_bcco_042_triple_parabolic_new504_high_strongclose},
    "f49_bcco_043_triple_parabolic_new252_high_extreme_rsi": {"inputs": _HC, "func": f49_bcco_043_triple_parabolic_new252_high_extreme_rsi},
    "f49_bcco_044_bull_trap_prior_new_high_then_wide_down": {"inputs": _HLC, "func": f49_bcco_044_bull_trap_prior_new_high_then_wide_down},
    "f49_bcco_045_quadruple_high_vol_rsi_widerange": {"inputs": _HLCV, "func": f49_bcco_045_quadruple_high_vol_rsi_widerange},
    "f49_bcco_046_count_signals_at_bar": {"inputs": _HLCV, "func": f49_bcco_046_count_signals_at_bar},
    "f49_bcco_047_three_consecutive_new_21d_highs_rising_vol": {"inputs": _HV, "func": f49_bcco_047_three_consecutive_new_21d_highs_rising_vol},
    "f49_bcco_048_five_consecutive_new_21d_highs_rising_vol": {"inputs": _HV, "func": f49_bcco_048_five_consecutive_new_21d_highs_rising_vol},
    "f49_bcco_049_ten_consecutive_up_close_days": {"inputs": ["close"], "func": f49_bcco_049_ten_consecutive_up_close_days},
    "f49_bcco_050_five_consecutive_wide_range_bars": {"inputs": _HLC, "func": f49_bcco_050_five_consecutive_wide_range_bars},
    "f49_bcco_051_five_consecutive_strong_close_clv_above_half": {"inputs": _HLC, "func": f49_bcco_051_five_consecutive_strong_close_clv_above_half},
    "f49_bcco_052_new_21d_high_with_3bar_ema_vol_2x_63d_ema": {"inputs": _HV, "func": f49_bcco_052_new_21d_high_with_3bar_ema_vol_2x_63d_ema},
    "f49_bcco_053_new_252d_high_each_of_past_5_bars": {"inputs": ["high"], "func": f49_bcco_053_new_252d_high_each_of_past_5_bars},
    "f49_bcco_054_new_21d_high_with_rising_rsi_t_minus_5": {"inputs": _HC, "func": f49_bcco_054_new_21d_high_with_rising_rsi_t_minus_5},
    "f49_bcco_055_new_252d_high_with_rsi_at_252d_max": {"inputs": _HC, "func": f49_bcco_055_new_252d_high_with_rsi_at_252d_max},
    "f49_bcco_056_new_21d_high_with_rising_volume_t_minus_5": {"inputs": _HV, "func": f49_bcco_056_new_21d_high_with_rising_volume_t_minus_5},
    "f49_bcco_057_5d_cum_ret_over_20pct_with_new_high_in_window": {"inputs": _HC, "func": f49_bcco_057_5d_cum_ret_over_20pct_with_new_high_in_window},
    "f49_bcco_058_10d_cum_ret_over_40pct_with_multiple_new_highs": {"inputs": _HC, "func": f49_bcco_058_10d_cum_ret_over_40pct_with_multiple_new_highs},
    "f49_bcco_059_failed_new_21d_high_with_close_below_open": {"inputs": _OHC, "func": f49_bcco_059_failed_new_21d_high_with_close_below_open},
    "f49_bcco_060_failed_new_high_cluster_3_in_5": {"inputs": _OHC, "func": f49_bcco_060_failed_new_high_cluster_3_in_5},
    "f49_bcco_061_new_high_and_rsi_falling_bearish_div": {"inputs": _HC, "func": f49_bcco_061_new_high_and_rsi_falling_bearish_div},
    "f49_bcco_062_new_high_with_clv_below_02": {"inputs": _HLC, "func": f49_bcco_062_new_high_with_clv_below_02},
    "f49_bcco_063_reversal_day_new_21d_high_close_below_prev_low": {"inputs": _HLC, "func": f49_bcco_063_reversal_day_new_21d_high_close_below_prev_low},
    "f49_bcco_064_reversal_day_count_past_21": {"inputs": _HLC, "func": f49_bcco_064_reversal_day_count_past_21},
    "f49_bcco_065_new_252d_high_then_next_bar_minus_5pct": {"inputs": _HC, "func": f49_bcco_065_new_252d_high_then_next_bar_minus_5pct},
    "f49_bcco_066_exhaustion_gap_up_then_close_below_open": {"inputs": _OC, "func": f49_bcco_066_exhaustion_gap_up_then_close_below_open},
    "f49_bcco_067_bearish_engulfing_after_new_252d_high": {"inputs": _OHLC, "func": f49_bcco_067_bearish_engulfing_after_new_252d_high},
    "f49_bcco_068_blowoff_and_fade_new_21d_high_close_bottom_quartile": {"inputs": _HLC, "func": f49_bcco_068_blowoff_and_fade_new_21d_high_close_bottom_quartile},
    "f49_bcco_069_atr21_at_252d_max_and_new_252d_high": {"inputs": _HLC, "func": f49_bcco_069_atr21_at_252d_max_and_new_252d_high},
    "f49_bcco_070_atr21_at_504d_max_and_new_252d_high": {"inputs": _HLC, "func": f49_bcco_070_atr21_at_504d_max_and_new_252d_high},
    "f49_bcco_071_atr_expand_and_parabolic_63": {"inputs": _HLC, "func": f49_bcco_071_atr_expand_and_parabolic_63},
    "f49_bcco_072_realized_vol_21_at_252d_max_and_new_high": {"inputs": _HC, "func": f49_bcco_072_realized_vol_21_at_252d_max_and_new_high},
    "f49_bcco_073_bollinger_upper_walk_5_bars": {"inputs": ["close"], "func": f49_bcco_073_bollinger_upper_walk_5_bars},
    "f49_bcco_074_bollinger_walk_with_new_252d_high": {"inputs": _HC, "func": f49_bcco_074_bollinger_walk_with_new_252d_high},
    "f49_bcco_075_bollinger_walk_new_high_vol_spike": {"inputs": _HCV, "func": f49_bcco_075_bollinger_walk_new_high_vol_spike},
}
