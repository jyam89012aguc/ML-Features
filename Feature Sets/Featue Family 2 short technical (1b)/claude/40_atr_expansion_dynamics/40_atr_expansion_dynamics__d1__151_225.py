"""atr_expansion_dynamics d1 features 151-225 — Pipeline 1b-technical extension.

75 NEW distinct hypotheses extending the 150 in __base__001_075.py and __base__076_150.py.
Drawn from gap analysis of ATR / range literature: Wilder RMA-ATR, double-
smoothed (Ehlers) ATR, median TR, MAD-TR; Keltner / Starc band geometry;
Chandelier exit & Parabolic SAR distance; Wilder DMI/DX/ADX TR-decomposition;
Crabel / Cooper NR4/NR7/WR7 narrow-wide range bars; ADR (gap-stripped);
DeMark REI; multi-bar true range overlap; Kaufman ER; Chande VIDYA-ATR;
TTM-squeeze regime; ATR-cone aperture and slope; OHLC bar-anatomy (upper-
shadow/lower-shadow/body fractions of TR); realized range; ATR term-structure
geometry (curvature, inversion flag, PCA loadings); signed TR; Vortex VI±.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import math
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


def _wilder_atr(high, low, close, n=21):
    """Wilder RMA smoothing: σ_t = ((n-1)·σ_{t-1} + TR_t) / n."""
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()


def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()


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


def _longest_run(w: np.ndarray) -> float:
    m = 0; c = 0
    for v in w:
        if v > 0.5:
            c += 1; m = c if c > m else m
        else:
            c = 0
    return float(m)


# ============================================================
# Bucket Z1 — Smoothing & estimator variants (151-155)
# ============================================================

def f40_atxd_151_wilder_atr21_minus_sma_atr21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder RMA-ATR(21) − SMA-ATR(21): persistence-decay bias of recursive vs simple smoothing."""
    return _wilder_atr(high, low, close, MDAYS) - _atr(high, low, close, MDAYS)


def f40_atxd_152_ema_atr_over_wilder_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EMA-ATR(21) / Wilder-ATR(21) ratio — lag-profile comparison."""
    tr = _true_range(high, low, close)
    ema_atr = _ema(tr, MDAYS)
    return _safe_div(ema_atr, _wilder_atr(high, low, close, MDAYS))


def f40_atxd_153_double_smoothed_atr_ehlers_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ehlers double-smoothed ATR: EMA(EMA(TR,21), 21) — ATR cycle phase exposure."""
    tr = _true_range(high, low, close)
    return _ema(_ema(tr, MDAYS), MDAYS)


def f40_atxd_154_median_true_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median True Range over 21d — robust ATR alternative less perturbed by single shocks."""
    return _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).median()


def f40_atxd_155_mad_tr_around_median_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median Absolute Deviation of TR around its rolling median over 21d — robust dispersion."""
    tr = _true_range(high, low, close)
    med = tr.rolling(MDAYS, min_periods=WDAYS).median()
    return (tr - med).abs().rolling(MDAYS, min_periods=WDAYS).median()


# ============================================================
# Bucket Z2 — Channel / band geometry in ATR space (156-159)
# ============================================================

def f40_atxd_156_keltner_channel_width_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner Channel width = 2·k·ATR(21) where k=2; raw band width."""
    return 4.0 * _atr(high, low, close, MDAYS)


def f40_atxd_157_pct_position_in_keltner_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close's normalized position within EMA ± 2·ATR Keltner Channel (-1..+1)."""
    ema = _ema(close, MDAYS)
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(close - ema, 2.0 * atr)


def f40_atxd_158_bars_outside_keltner_upper_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where close > EMA + 2·ATR (above upper Keltner band) over 63d."""
    ema = _ema(close, MDAYS)
    atr = _atr(high, low, close, MDAYS)
    return (close > ema + 2.0 * atr).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_159_starc_band_width_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Starc Band width: SMA(close,21) ± 1.33·ATR(15), raw band width = 2.66·ATR(15)."""
    return 2.66 * _atr(high, low, close, 15)


# ============================================================
# Bucket Z3 — Trailing-stop / SAR distance (160-163)
# ============================================================

def f40_atxd_160_chandelier_long_distance_22d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Chandelier-exit-long distance: HighestHigh(22) − 3·ATR(22) − close, normalized by close."""
    hh = high.rolling(22, min_periods=WDAYS).max()
    atr = _atr(high, low, close, 22)
    stop = hh - 3.0 * atr
    return _safe_div(stop - close, close)


def f40_atxd_161_bars_since_chandelier_long_violation_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since close last crossed BELOW Chandelier-long stop within 252d window."""
    hh = high.rolling(22, min_periods=WDAYS).max()
    atr = _atr(high, low, close, 22)
    stop = hh - 3.0 * atr
    below = (close < stop).astype(int).fillna(0).values
    out = np.full(len(below), np.nan)
    bars = np.nan
    for i, v in enumerate(below):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


def f40_atxd_162_psar_to_close_in_atr_units_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|Parabolic-SAR proxy − close| / ATR(21) over 21d (SAR proxy = HighestHigh(21) for longs)."""
    sar_proxy = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div((sar_proxy - close).abs(), _atr(high, low, close, MDAYS))


def f40_atxd_163_atr_trailing_stop_giveback_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-trailing-stop give-back: (HighestClose(252) − 3·ATR(22)) / HighestClose(252) — potential DD."""
    hc = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, 22)
    return _safe_div(3.0 * atr, hc)


# ============================================================
# Bucket Z4 — Wilder DMI / DX TR-decomposition (164-167)
# ============================================================

def f40_atxd_164_plus_dm_share_of_tr_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+DM / TR share over 14d: fraction of TR attributable to upward directional moves."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    plus_dm = plus_dm.where(plus_dm > minus_dm, 0.0)
    tr = _true_range(high, low, close)
    sum_plus_dm = plus_dm.rolling(14, min_periods=WDAYS).sum()
    sum_tr = tr.rolling(14, min_periods=WDAYS).sum()
    return _safe_div(sum_plus_dm, sum_tr)


def f40_atxd_165_minus_dm_share_of_tr_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """−DM / TR share over 14d: fraction attributable to downward directional moves."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    minus_dm = minus_dm.where(minus_dm > plus_dm, 0.0)
    tr = _true_range(high, low, close)
    sum_minus_dm = minus_dm.rolling(14, min_periods=WDAYS).sum()
    sum_tr = tr.rolling(14, min_periods=WDAYS).sum()
    return _safe_div(sum_minus_dm, sum_tr)


def f40_atxd_166_dx_raw_directional_purity_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pre-ADX DX raw: |+DI − −DI| / (+DI + −DI) over 14d (directional purity ratio)."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    plus_dm_only = plus_dm.where(plus_dm > minus_dm, 0.0)
    minus_dm_only = minus_dm.where(minus_dm > plus_dm, 0.0)
    tr = _true_range(high, low, close)
    plus_di = 100.0 * _safe_div(plus_dm_only.rolling(14, min_periods=WDAYS).sum(), tr.rolling(14, min_periods=WDAYS).sum())
    minus_di = 100.0 * _safe_div(minus_dm_only.rolling(14, min_periods=WDAYS).sum(), tr.rolling(14, min_periods=WDAYS).sum())
    return _safe_div((plus_di - minus_di).abs(), plus_di + minus_di)


def f40_atxd_167_adx_rate_of_change_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADX rate-of-change: Δ-ADX over 14d (peaking ADX often precedes exhaustion)."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    plus_dm_only = plus_dm.where(plus_dm > minus_dm, 0.0)
    minus_dm_only = minus_dm.where(minus_dm > plus_dm, 0.0)
    tr = _true_range(high, low, close)
    plus_di = 100.0 * _safe_div(plus_dm_only.rolling(14, min_periods=WDAYS).sum(), tr.rolling(14, min_periods=WDAYS).sum())
    minus_di = 100.0 * _safe_div(minus_dm_only.rolling(14, min_periods=WDAYS).sum(), tr.rolling(14, min_periods=WDAYS).sum())
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), plus_di + minus_di)
    adx = dx.ewm(alpha=1.0 / 14, min_periods=14, adjust=False).mean()
    return adx - adx.shift(14)


# ============================================================
# Bucket Z5 — Narrow / wide range bar patterns (168-172)
# ============================================================

def f40_atxd_168_nr4_indicator_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 bars (today's range narrowest of last 4) within 63d."""
    rng = high - low
    nr4 = (rng == rng.rolling(4, min_periods=4).min()).astype(float)
    return nr4.rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_169_nr7_indicator_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 bars (today's range narrowest of last 7) within 63d."""
    rng = high - low
    nr7 = (rng == rng.rolling(7, min_periods=7).min()).astype(float)
    return nr7.rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_170_wr7_indicator_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR7 bars (today's range widest of last 7) within 63d — climactic-bar marker."""
    rng = high - low
    wr7 = (rng == rng.rolling(7, min_periods=7).max()).astype(float)
    return wr7.rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_171_inside_day_after_nr7_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of (inside-day AND NR7) compounded compression patterns over 252d."""
    rng = high - low
    nr7 = (rng == rng.rolling(7, min_periods=7).min())
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (nr7 & inside).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f40_atxd_172_id_nr4_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of ID/NR4 (Inside-Day AND NR4) bars within 252d — Crabel squeeze trigger."""
    rng = high - low
    nr4 = (rng == rng.rolling(4, min_periods=4).min())
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (nr4 & inside).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z6 — ADR & gap-stripped range (173-175)
# ============================================================

def f40_atxd_173_adr_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Average Daily Range (gap-stripped): mean(H-L) over 21d — no gap component."""
    return (high - low).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_174_adr_over_atr_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADR / ATR ratio over 21d — measures contribution of overnight gaps + prior-close clamps."""
    adr = (high - low).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(adr, _atr(high, low, close, MDAYS))


def f40_atxd_175_adr_pct_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ADR% = ADR(21) / close — gap-stripped daily range as fraction of price."""
    adr = (high - low).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(adr, close)


# ============================================================
# Bucket Z7 — DeMark / Range Expansion Index (176-177)
# ============================================================

def f40_atxd_176_demark_rei_8d(high: pd.Series, low: pd.Series) -> pd.Series:
    """DeMark Range Expansion Index over 8d: Σ conditional (H_t−H_{t-2}) + (L_t−L_{t-2}) normalized."""
    h_diff = high - high.shift(2)
    l_diff = low - low.shift(2)
    s_diff = h_diff + l_diff
    num = s_diff.rolling(8, min_periods=4).sum()
    den = (h_diff.abs() + l_diff.abs()).rolling(8, min_periods=4).sum()
    return _safe_div(num, den) * 100.0


def f40_atxd_177_demark_pressure_proxy_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """DeMark TD-Pressure proxy: rolling 5d mean of (C-O)/(H-L) — directional pressure inside range."""
    return _safe_div(close - open, high - low).rolling(WDAYS, min_periods=2).mean()


# ============================================================
# Bucket Z8 — Multi-bar composite range (178-180)
# ============================================================

def f40_atxd_178_nbar_true_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar true range: max(H[t-20..t]) − min(L[t-20..t]) — composite envelope."""
    return high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()


def f40_atxd_179_tr_overlap_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR overlap ratio: 21-bar true-range / Σ TR over 21d (overlap = mean-reversion, stack = trend)."""
    composite = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    return _safe_div(composite, _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum())


def f40_atxd_180_kaufman_er_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kaufman ER in range space: |H_t − L_{t-20}| / Σ|barmoves| over 21d."""
    net = (high - low.shift(MDAYS)).abs()
    summed = (high - low).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, summed)


# ============================================================
# Bucket Z9 — Chande adaptive ATR (181-182)
# ============================================================

def f40_atxd_181_vidya_style_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Chande VIDYA-style ATR: ATR smoothing α scaled by Σ|Δr|/Σ|r| CMO-like factor over 21d."""
    tr = _true_range(high, low, close)
    r = close.diff()
    cmo = _safe_div(r.rolling(21, min_periods=WDAYS).sum().abs(),
                    r.abs().rolling(21, min_periods=WDAYS).sum())
    # alpha proportional to abs(cmo)
    alpha = (2.0 / (MDAYS + 1)) * cmo.abs().clip(upper=1.0, lower=0.05)
    out = pd.Series(np.nan, index=close.index)
    val = np.nan
    for i in range(len(tr)):
        if np.isnan(tr.iloc[i]) or np.isnan(alpha.iloc[i]):
            out.iloc[i] = val
            continue
        if np.isnan(val):
            val = tr.iloc[i]
        else:
            val = alpha.iloc[i] * tr.iloc[i] + (1 - alpha.iloc[i]) * val
        out.iloc[i] = val
    return out


def f40_atxd_182_chande_trend_adjusted_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Chande trend-adjusted ATR: mean TR restricted to bars in dominant trend direction (sign of 21d ret), over 21d."""
    tr = _true_range(high, low, close)
    trend_sign = np.sign(close - close.shift(MDAYS))
    bar_sign = np.sign(close - close.shift(1))
    aligned = (trend_sign == bar_sign) & (trend_sign != 0)
    sel = tr.where(aligned, np.nan)
    return sel.rolling(MDAYS, min_periods=WDAYS).mean()


# ============================================================
# Bucket Z10 — Volatility-state / compression geometry (183-186)
# ============================================================

def f40_atxd_183_ttm_squeeze_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TTM-squeeze (ATR-vs-σ): 1 if BB-width(20,2σ) < KC-width(20,2ATR) — vol-compression boolean."""
    sma = close.rolling(20, min_periods=WDAYS).mean()
    sigma = close.rolling(20, min_periods=WDAYS).std()
    bb_width = 4.0 * sigma  # ±2σ → total 4σ
    atr = _atr(high, low, close, 20)
    kc_width = 4.0 * atr  # ±2ATR → total 4 ATR
    return (bb_width < kc_width).astype(float)


def f40_atxd_184_bars_since_ttm_squeeze_release(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since TTM-squeeze last released (BB flipped from inside KC to outside)."""
    sma = close.rolling(20, min_periods=WDAYS).mean()
    sigma = close.rolling(20, min_periods=WDAYS).std()
    atr = _atr(high, low, close, 20)
    inside = (4.0 * sigma < 4.0 * atr).astype(int)
    # release: inside_{t-1}=1 AND inside_t=0
    release = ((inside == 0) & (inside.shift(1) == 1)).astype(int).fillna(0).values
    out = np.full(len(release), np.nan)
    bars = np.nan
    for i, v in enumerate(release):
        if v == 1:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=close.index)


def f40_atxd_185_atr_cone_aperture_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR cone aperture: (p90 ATR(21) − p10 ATR(21)) over rolling 252d — width of the cone itself."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)


def f40_atxd_186_atr_cone_slope_diff_p90_p10(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR cone slope difference: rolling 63d slope of (p90 − p10) cone width — aperture expansion rate."""
    a = _atr(high, low, close, MDAYS)
    aperture = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.90) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return _rolling_slope(aperture, QDAYS)


# ============================================================
# Bucket Z11 — Bar anatomy (range decomposition) (187-191)
# ============================================================

def f40_atxd_187_upper_shadow_over_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (H − max(O,C)) / TR over 21d — rejection-wick share of range."""
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    return _safe_div(high - body_hi, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_188_lower_shadow_over_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (min(O,C) − L) / TR over 21d — demand-tail share."""
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    return _safe_div(body_lo - low, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_189_body_over_tr_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |C-O| / TR over 21d — marubozu-share of range (trending-bar fraction)."""
    return _safe_div((close - open).abs(), _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_190_close_position_in_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (C - L) / (H - L) over 21d — bull/bear close-bias inside the bar (CLV centered around 0.5)."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div(close - low, rng).rolling(MDAYS, min_periods=WDAYS).mean()


def f40_atxd_191_mean_intrabar_gap_clamp_share_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ((H − pc)+ + (pc − L)+ − (H − L))+ / TR over 21d — prior-close-outside-HL clamp share."""
    pc = close.shift(1)
    clamp = ((high - pc).clip(lower=0.0) + (pc - low).clip(lower=0.0) - (high - low)).clip(lower=0.0)
    return _safe_div(clamp, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean()


# ============================================================
# Bucket Z12 — Realized range / range-based jump (192-193)
# ============================================================

def f40_atxd_192_realized_range_christensen_podolskij_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Realized range estimator (CP): Σ (H-L)² / (4·log 2) over 21d — range-vol fingerprint."""
    return ((high - low) ** 2 / (4.0 * np.log(2.0))).rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_193_range_jump_abdl_proxy_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ABDL-style range-based jump test: Σ TR² − k·(H-L)² over 21d — isolates overnight-jump component."""
    tr = _true_range(high, low, close)
    k = 1.0 / (4.0 * np.log(2.0))
    return ((tr ** 2) - k * ((high - low) ** 2)).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket Z13 — ATR term-structure geometry (194-196)
# ============================================================

def f40_atxd_194_atr_term_structure_curvature(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR term-structure curvature: ATR(63) − 0.5·(ATR(21)+ATR(252)) — butterfly of the ATR curve."""
    return _atr(high, low, close, QDAYS) - 0.5 * (_atr(high, low, close, MDAYS) + _atr(high, low, close, YDAYS))


def f40_atxd_195_atr_term_structure_inversion_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR full inversion: 1 if ATR(5)>ATR(21)>ATR(63)>ATR(252) simultaneously."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    a252 = _atr(high, low, close, YDAYS)
    return ((a5 > a21) & (a21 > a63) & (a63 > a252)).astype(float)


def f40_atxd_196_atr_term_structure_pc1_level(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-curve level (first PC proxy): mean of ATR(5)/close, ATR(21)/close, ATR(63)/close, ATR(252)/close."""
    n5 = _safe_div(_atr(high, low, close, WDAYS), close)
    n21 = _safe_div(_atr(high, low, close, MDAYS), close)
    n63 = _safe_div(_atr(high, low, close, QDAYS), close)
    n252 = _safe_div(_atr(high, low, close, YDAYS), close)
    return (n5 + n21 + n63 + n252) / 4.0


# ============================================================
# Bucket Z14 — Signed TR (197-198)
# ============================================================

def f40_atxd_197_signed_tr_close_open_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of signed TR using sign(C-O) over 21d — directional range accumulator."""
    tr = _true_range(high, low, close)
    return (np.sign(close - open) * tr).rolling(MDAYS, min_periods=WDAYS).sum()


def f40_atxd_198_signed_tr_close_prev_close_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of signed TR using sign(C - prev C) over 21d — direction-integrator."""
    tr = _true_range(high, low, close)
    return (np.sign(close - close.shift(1)) * tr).rolling(MDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket Z15 — Vortex Indicator (199-200)
# ============================================================

def f40_atxd_199_vortex_vi_plus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI+ (raw) over 14d: Σ|H_t − L_{t-1}| / Σ TR — directional-range bull component."""
    num = (high - low.shift(1)).abs()
    return _safe_div(num.rolling(14, min_periods=WDAYS).sum(),
                     _true_range(high, low, close).rolling(14, min_periods=WDAYS).sum())


def f40_atxd_200_vortex_vi_minus_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex VI− (raw) over 14d: Σ|L_t − H_{t-1}| / Σ TR — directional-range bear component."""
    num = (low - high.shift(1)).abs()
    return _safe_div(num.rolling(14, min_periods=WDAYS).sum(),
                     _true_range(high, low, close).rolling(14, min_periods=WDAYS).sum())


# ============================================================
# Bucket Z16 — Range concentration / power laws (201-203)
# ============================================================

def f40_atxd_201_gini_tr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gini coefficient of TR distribution over 252d — concentration of single-bar TRs."""
    tr = _true_range(high, low, close)

    def _gini(w):
        x = w[~np.isnan(w)]
        n = len(x)
        if n < 30 or x.sum() <= 0:
            return np.nan
        x = np.sort(x)
        i = np.arange(1, n + 1)
        return float((2 * (i * x).sum() - (n + 1) * x.sum()) / (n * x.sum()))
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_gini, raw=True)


def f40_atxd_202_top5_bar_tr_share_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Top-5-bar TR share of 252d Σ TR — annual range concentration."""
    tr = _true_range(high, low, close)

    def _share(w):
        x = w[~np.isnan(w)]
        if len(x) < 30 or x.sum() <= 0:
            return np.nan
        top5 = np.sort(x)[-5:].sum()
        return float(top5 / x.sum())
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_share, raw=True)


def f40_atxd_203_hill_tail_index_tr_top10_1260d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hill tail-index (top 10%) of raw single-bar TR distribution over 1260d (distinct from ATR-Hill)."""
    tr = _true_range(high, low, close)

    def _hill(w):
        arr = w[~np.isnan(w)]
        if len(arr) < 60:
            return np.nan
        k = max(int(len(arr) * 0.10), 5)
        top = np.sort(arr)[-k:]
        th = top[0]
        if th <= 0:
            return np.nan
        lg = np.log(top / th)
        val = lg[1:].mean() if len(lg) > 1 else np.nan
        return float(val) if np.isfinite(val) and val > 0 else np.nan
    return tr.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).apply(_hill, raw=True)


# ============================================================
# Bucket Z17 — Conditional / event-driven range (204-206)
# ============================================================

def f40_atxd_204_atr_up_vs_down_days_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of mean TR on up-days (C>prev_C) vs down-days (C<prev_C) over 21d — range asymmetry."""
    tr = _true_range(high, low, close)
    up = tr.where(close > close.shift(1), np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    dn = tr.where(close < close.shift(1), np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(up, dn)


def f40_atxd_205_mean_tr_gap_up_vs_gap_down_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR ratio on gap-up vs gap-down days (open > prev close vs open < prev close) over 63d."""
    tr = _true_range(high, low, close)
    gu = tr.where(open > close.shift(1), np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    gd = tr.where(open < close.shift(1), np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(gu, gd)


def f40_atxd_206_day_after_shock_tr_mean_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR_t conditional on TR_{t-1} > 2·ATR(21).shift(2) — post-shock follow-through over 63d."""
    tr = _true_range(high, low, close)
    shock = (tr.shift(1) > 2.0 * _atr(high, low, close, MDAYS).shift(2))
    sel = tr.where(shock, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket Z18 — Wilder DMI range internals (207-209)
# ============================================================

def f40_atxd_207_tr_up_move_share_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR-share of true-up move: Σ(UpMove)+ / Σ TR over 21d (Wilder DMI internal)."""
    up_move = (high - high.shift(1)).clip(lower=0.0)
    tr = _true_range(high, low, close)
    return _safe_div(up_move.rolling(MDAYS, min_periods=WDAYS).sum(),
                     tr.rolling(MDAYS, min_periods=WDAYS).sum())


def f40_atxd_208_plus_dm_streak_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Longest consecutive +DM-dominant bars (where +DM > −DM) within 21d window."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    dom = (plus_dm > minus_dm).astype(float).fillna(0.0)
    return dom.rolling(MDAYS, min_periods=WDAYS).apply(_longest_run, raw=True)


def f40_atxd_209_minus_dm_streak_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Longest consecutive −DM-dominant bars within 21d window."""
    plus_dm = (high - high.shift(1)).clip(lower=0.0)
    minus_dm = (low.shift(1) - low).clip(lower=0.0)
    dom = (minus_dm > plus_dm).astype(float).fillna(0.0)
    return dom.rolling(MDAYS, min_periods=WDAYS).apply(_longest_run, raw=True)


# ============================================================
# Bucket Z19 — Range-vs-return coupling (210-212)
# ============================================================

def f40_atxd_210_range_to_return_efficiency_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kaufman ER on close vs Σ TR: |C_t − C_{t-20}| / Σ TR over 21d — net-extracted-from-range ratio."""
    net = (close - close.shift(MDAYS)).abs()
    summed = _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, summed)


def f40_atxd_211_abs_ret_over_tr_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |C-pc| / TR over 63d — close-vs-range bias (intraday round-trip share)."""
    return _safe_div((close - close.shift(1)).abs(),
                     _true_range(high, low, close)).rolling(QDAYS, min_periods=MDAYS).mean()


def f40_atxd_212_atr_normalized_close_change_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized 21d close change: (C_t − C_{t-21}) / ATR(21)."""
    return _safe_div(close - close.shift(MDAYS), _atr(high, low, close, MDAYS))


# ============================================================
# Bucket Z20 — Adaptive / cycle-phase ATR (213-215)
# ============================================================

def f40_atxd_213_mesa_phase_log_atr_proxy_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MESA/Ehlers phase proxy: atan2(detrended_log_ATR, detrended_log_ATR.shift(1)) over 252d window."""
    la = _safe_log(_atr(high, low, close, MDAYS))
    # Detrend with rolling 63d mean
    detr = la - la.rolling(QDAYS, min_periods=MDAYS).mean()
    return np.arctan2(detr, detr.shift(1)) / np.pi  # normalized to [-1, 1]


def f40_atxd_214_atr_cycle_expansion_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR cycle expansion: 1 if ATR(21) > its EMA-21 of past values (expansion quarter)."""
    a = _atr(high, low, close, MDAYS)
    return (a > _ema(a, MDAYS)).astype(float)


def f40_atxd_215_atr_acceleration_cycle_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sign-change count of ATR(21) acceleration (Δ²ATR sign changes) over 252d — cycle frequency."""
    a = _atr(high, low, close, MDAYS)
    accel = a.diff().diff()
    return np.sign(accel).diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket Z21 — More variants for 75 (216-225)
# ============================================================

def f40_atxd_216_atr_pos_vs_neg_close_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR on bars where close>open / mean ATR on close<open over 252d (intraday-bull-vs-bear range)."""
    tr = _true_range(high, low, close)
    pos = tr.where(close > close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    neg = tr.where(close < close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(pos, neg)


def f40_atxd_217_atr_compression_event_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-compression events: count of bars where ATR(5) < 0.5·ATR(63) within 63d."""
    a5 = _atr(high, low, close, WDAYS)
    a63 = _atr(high, low, close, QDAYS)
    return (a5 < 0.5 * a63).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f40_atxd_218_atr_oscillator_macd_style_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR oscillator (MACD-style): EMA(ATR(21),12) − EMA(ATR(21),26) over 21d."""
    a = _atr(high, low, close, MDAYS)
    return _ema(a, 12) - _ema(a, 26)


def f40_atxd_219_atr_oscillator_signal_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-oscillator histogram: ATR-MACD line − its 9-period EMA — divergence flag."""
    a = _atr(high, low, close, MDAYS)
    macd = _ema(a, 12) - _ema(a, 26)
    return macd - _ema(macd, 9)


def f40_atxd_220_atr_smoothing_dispersion(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Smoothing dispersion: std across {Wilder-ATR, SMA-ATR, EMA-ATR, MTR} over 252d."""
    tr = _true_range(high, low, close)
    smoothers = pd.concat([
        _wilder_atr(high, low, close, MDAYS),
        _atr(high, low, close, MDAYS),
        _ema(tr, MDAYS),
        tr.rolling(MDAYS, min_periods=WDAYS).median(),
    ], axis=1)
    return smoothers.std(axis=1)


def f40_atxd_221_avg_tr_in_high_volume_decile_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean TR on top-decile-volume bars within 252d (range-volume coupling distinct from existing 135)."""
    tr = _true_range(high, low, close)
    pv90 = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.90).shift(1)
    sel = tr.where(volume > pv90, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f40_atxd_222_atr_squeeze_release_strength_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-squeeze-release strength: max(ATR(5)/ATR(63)) − min(ATR(5)/ATR(63)) within 63d."""
    ratio = _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, QDAYS))
    return ratio.rolling(QDAYS, min_periods=MDAYS).max() - ratio.rolling(QDAYS, min_periods=MDAYS).min()


def f40_atxd_223_atr_volatility_smile_curvature(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR vol-smile curvature: ATR(21) − 0.5·(ATR(5)+ATR(63)) — concavity in middle of curve."""
    return _atr(high, low, close, MDAYS) - 0.5 * (_atr(high, low, close, WDAYS) + _atr(high, low, close, QDAYS))


def f40_atxd_224_natr_ema_smoothed_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EMA-smoothed NATR(21): EMA(ATR/close, 21) — smoothed close-normalized vol."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    return _ema(natr, MDAYS)


def f40_atxd_225_atr_envelope_breach_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where close > EMA(close,21) + 3·ATR(21) (extreme upper-envelope breach) over 63d."""
    ema = _ema(close, MDAYS)
    atr = _atr(high, low, close, MDAYS)
    return (close > ema + 3.0 * atr).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f40_atxd_151_wilder_atr21_minus_sma_atr21_d1(high, low, close):
    return f40_atxd_151_wilder_atr21_minus_sma_atr21(high, low, close).diff()


def f40_atxd_152_ema_atr_over_wilder_atr_21d_d1(high, low, close):
    return f40_atxd_152_ema_atr_over_wilder_atr_21d(high, low, close).diff()


def f40_atxd_153_double_smoothed_atr_ehlers_21d_d1(high, low, close):
    return f40_atxd_153_double_smoothed_atr_ehlers_21d(high, low, close).diff()


def f40_atxd_154_median_true_range_21d_d1(high, low, close):
    return f40_atxd_154_median_true_range_21d(high, low, close).diff()


def f40_atxd_155_mad_tr_around_median_21d_d1(high, low, close):
    return f40_atxd_155_mad_tr_around_median_21d(high, low, close).diff()


def f40_atxd_156_keltner_channel_width_21d_d1(high, low, close):
    return f40_atxd_156_keltner_channel_width_21d(high, low, close).diff()


def f40_atxd_157_pct_position_in_keltner_21d_d1(high, low, close):
    return f40_atxd_157_pct_position_in_keltner_21d(high, low, close).diff()


def f40_atxd_158_bars_outside_keltner_upper_63d_d1(high, low, close):
    return f40_atxd_158_bars_outside_keltner_upper_63d(high, low, close).diff()


def f40_atxd_159_starc_band_width_21d_d1(high, low, close):
    return f40_atxd_159_starc_band_width_21d(high, low, close).diff()


def f40_atxd_160_chandelier_long_distance_22d_d1(high, low, close):
    return f40_atxd_160_chandelier_long_distance_22d(high, low, close).diff()


def f40_atxd_161_bars_since_chandelier_long_violation_252d_d1(high, low, close):
    return f40_atxd_161_bars_since_chandelier_long_violation_252d(high, low, close).diff()


def f40_atxd_162_psar_to_close_in_atr_units_21d_d1(high, low, close):
    return f40_atxd_162_psar_to_close_in_atr_units_21d(high, low, close).diff()


def f40_atxd_163_atr_trailing_stop_giveback_252d_d1(high, low, close):
    return f40_atxd_163_atr_trailing_stop_giveback_252d(high, low, close).diff()


def f40_atxd_164_plus_dm_share_of_tr_14d_d1(high, low, close):
    return f40_atxd_164_plus_dm_share_of_tr_14d(high, low, close).diff()


def f40_atxd_165_minus_dm_share_of_tr_14d_d1(high, low, close):
    return f40_atxd_165_minus_dm_share_of_tr_14d(high, low, close).diff()


def f40_atxd_166_dx_raw_directional_purity_14d_d1(high, low, close):
    return f40_atxd_166_dx_raw_directional_purity_14d(high, low, close).diff()


def f40_atxd_167_adx_rate_of_change_14d_d1(high, low, close):
    return f40_atxd_167_adx_rate_of_change_14d(high, low, close).diff()


def f40_atxd_168_nr4_indicator_count_63d_d1(high, low):
    return f40_atxd_168_nr4_indicator_count_63d(high, low).diff()


def f40_atxd_169_nr7_indicator_count_63d_d1(high, low):
    return f40_atxd_169_nr7_indicator_count_63d(high, low).diff()


def f40_atxd_170_wr7_indicator_count_63d_d1(high, low):
    return f40_atxd_170_wr7_indicator_count_63d(high, low).diff()


def f40_atxd_171_inside_day_after_nr7_count_252d_d1(high, low):
    return f40_atxd_171_inside_day_after_nr7_count_252d(high, low).diff()


def f40_atxd_172_id_nr4_count_252d_d1(high, low):
    return f40_atxd_172_id_nr4_count_252d(high, low).diff()


def f40_atxd_173_adr_21d_d1(high, low):
    return f40_atxd_173_adr_21d(high, low).diff()


def f40_atxd_174_adr_over_atr_ratio_21d_d1(high, low, close):
    return f40_atxd_174_adr_over_atr_ratio_21d(high, low, close).diff()


def f40_atxd_175_adr_pct_21d_d1(high, low, close):
    return f40_atxd_175_adr_pct_21d(high, low, close).diff()


def f40_atxd_176_demark_rei_8d_d1(high, low):
    return f40_atxd_176_demark_rei_8d(high, low).diff()


def f40_atxd_177_demark_pressure_proxy_5d_d1(open, high, low, close):
    return f40_atxd_177_demark_pressure_proxy_5d(open, high, low, close).diff()


def f40_atxd_178_nbar_true_range_21d_d1(high, low, close):
    return f40_atxd_178_nbar_true_range_21d(high, low, close).diff()


def f40_atxd_179_tr_overlap_ratio_21d_d1(high, low, close):
    return f40_atxd_179_tr_overlap_ratio_21d(high, low, close).diff()


def f40_atxd_180_kaufman_er_range_21d_d1(high, low, close):
    return f40_atxd_180_kaufman_er_range_21d(high, low, close).diff()


def f40_atxd_181_vidya_style_atr_21d_d1(high, low, close):
    return f40_atxd_181_vidya_style_atr_21d(high, low, close).diff()


def f40_atxd_182_chande_trend_adjusted_atr_21d_d1(high, low, close):
    return f40_atxd_182_chande_trend_adjusted_atr_21d(high, low, close).diff()


def f40_atxd_183_ttm_squeeze_indicator_d1(high, low, close):
    return f40_atxd_183_ttm_squeeze_indicator(high, low, close).diff()


def f40_atxd_184_bars_since_ttm_squeeze_release_d1(high, low, close):
    return f40_atxd_184_bars_since_ttm_squeeze_release(high, low, close).diff()


def f40_atxd_185_atr_cone_aperture_252d_d1(high, low, close):
    return f40_atxd_185_atr_cone_aperture_252d(high, low, close).diff()


def f40_atxd_186_atr_cone_slope_diff_p90_p10_d1(high, low, close):
    return f40_atxd_186_atr_cone_slope_diff_p90_p10(high, low, close).diff()


def f40_atxd_187_upper_shadow_over_tr_21d_d1(open, high, low, close):
    return f40_atxd_187_upper_shadow_over_tr_21d(open, high, low, close).diff()


def f40_atxd_188_lower_shadow_over_tr_21d_d1(open, high, low, close):
    return f40_atxd_188_lower_shadow_over_tr_21d(open, high, low, close).diff()


def f40_atxd_189_body_over_tr_21d_d1(open, high, low, close):
    return f40_atxd_189_body_over_tr_21d(open, high, low, close).diff()


def f40_atxd_190_close_position_in_range_21d_d1(high, low, close):
    return f40_atxd_190_close_position_in_range_21d(high, low, close).diff()


def f40_atxd_191_mean_intrabar_gap_clamp_share_21d_d1(high, low, close):
    return f40_atxd_191_mean_intrabar_gap_clamp_share_21d(high, low, close).diff()


def f40_atxd_192_realized_range_christensen_podolskij_21d_d1(high, low):
    return f40_atxd_192_realized_range_christensen_podolskij_21d(high, low).diff()


def f40_atxd_193_range_jump_abdl_proxy_21d_d1(high, low, close):
    return f40_atxd_193_range_jump_abdl_proxy_21d(high, low, close).diff()


def f40_atxd_194_atr_term_structure_curvature_d1(high, low, close):
    return f40_atxd_194_atr_term_structure_curvature(high, low, close).diff()


def f40_atxd_195_atr_term_structure_inversion_flag_d1(high, low, close):
    return f40_atxd_195_atr_term_structure_inversion_flag(high, low, close).diff()


def f40_atxd_196_atr_term_structure_pc1_level_d1(high, low, close):
    return f40_atxd_196_atr_term_structure_pc1_level(high, low, close).diff()


def f40_atxd_197_signed_tr_close_open_21d_d1(open, high, low, close):
    return f40_atxd_197_signed_tr_close_open_21d(open, high, low, close).diff()


def f40_atxd_198_signed_tr_close_prev_close_21d_d1(high, low, close):
    return f40_atxd_198_signed_tr_close_prev_close_21d(high, low, close).diff()


def f40_atxd_199_vortex_vi_plus_14d_d1(high, low, close):
    return f40_atxd_199_vortex_vi_plus_14d(high, low, close).diff()


def f40_atxd_200_vortex_vi_minus_14d_d1(high, low, close):
    return f40_atxd_200_vortex_vi_minus_14d(high, low, close).diff()


def f40_atxd_201_gini_tr_252d_d1(high, low, close):
    return f40_atxd_201_gini_tr_252d(high, low, close).diff()


def f40_atxd_202_top5_bar_tr_share_252d_d1(high, low, close):
    return f40_atxd_202_top5_bar_tr_share_252d(high, low, close).diff()


def f40_atxd_203_hill_tail_index_tr_top10_1260d_d1(high, low, close):
    return f40_atxd_203_hill_tail_index_tr_top10_1260d(high, low, close).diff()


def f40_atxd_204_atr_up_vs_down_days_ratio_21d_d1(high, low, close):
    return f40_atxd_204_atr_up_vs_down_days_ratio_21d(high, low, close).diff()


def f40_atxd_205_mean_tr_gap_up_vs_gap_down_63d_d1(open, high, low, close):
    return f40_atxd_205_mean_tr_gap_up_vs_gap_down_63d(open, high, low, close).diff()


def f40_atxd_206_day_after_shock_tr_mean_63d_d1(high, low, close):
    return f40_atxd_206_day_after_shock_tr_mean_63d(high, low, close).diff()


def f40_atxd_207_tr_up_move_share_21d_d1(high, low, close):
    return f40_atxd_207_tr_up_move_share_21d(high, low, close).diff()


def f40_atxd_208_plus_dm_streak_count_21d_d1(high, low):
    return f40_atxd_208_plus_dm_streak_count_21d(high, low).diff()


def f40_atxd_209_minus_dm_streak_count_21d_d1(high, low):
    return f40_atxd_209_minus_dm_streak_count_21d(high, low).diff()


def f40_atxd_210_range_to_return_efficiency_21d_d1(high, low, close):
    return f40_atxd_210_range_to_return_efficiency_21d(high, low, close).diff()


def f40_atxd_211_abs_ret_over_tr_ratio_63d_d1(high, low, close):
    return f40_atxd_211_abs_ret_over_tr_ratio_63d(high, low, close).diff()


def f40_atxd_212_atr_normalized_close_change_21d_d1(high, low, close):
    return f40_atxd_212_atr_normalized_close_change_21d(high, low, close).diff()


def f40_atxd_213_mesa_phase_log_atr_proxy_252d_d1(high, low, close):
    return f40_atxd_213_mesa_phase_log_atr_proxy_252d(high, low, close).diff()


def f40_atxd_214_atr_cycle_expansion_indicator_d1(high, low, close):
    return f40_atxd_214_atr_cycle_expansion_indicator(high, low, close).diff()


def f40_atxd_215_atr_acceleration_cycle_252d_d1(high, low, close):
    return f40_atxd_215_atr_acceleration_cycle_252d(high, low, close).diff()


def f40_atxd_216_atr_pos_vs_neg_close_ratio_252d_d1(high, low, close):
    return f40_atxd_216_atr_pos_vs_neg_close_ratio_252d(high, low, close).diff()


def f40_atxd_217_atr_compression_event_count_63d_d1(high, low, close):
    return f40_atxd_217_atr_compression_event_count_63d(high, low, close).diff()


def f40_atxd_218_atr_oscillator_macd_style_21d_d1(high, low, close):
    return f40_atxd_218_atr_oscillator_macd_style_21d(high, low, close).diff()


def f40_atxd_219_atr_oscillator_signal_252d_d1(high, low, close):
    return f40_atxd_219_atr_oscillator_signal_252d(high, low, close).diff()


def f40_atxd_220_atr_smoothing_dispersion_d1(high, low, close):
    return f40_atxd_220_atr_smoothing_dispersion(high, low, close).diff()


def f40_atxd_221_avg_tr_in_high_volume_decile_252d_d1(high, low, close, volume):
    return f40_atxd_221_avg_tr_in_high_volume_decile_252d(high, low, close, volume).diff()


def f40_atxd_222_atr_squeeze_release_strength_63d_d1(high, low, close):
    return f40_atxd_222_atr_squeeze_release_strength_63d(high, low, close).diff()


def f40_atxd_223_atr_volatility_smile_curvature_d1(high, low, close):
    return f40_atxd_223_atr_volatility_smile_curvature(high, low, close).diff()


def f40_atxd_224_natr_ema_smoothed_21d_d1(high, low, close):
    return f40_atxd_224_natr_ema_smoothed_21d(high, low, close).diff()


def f40_atxd_225_atr_envelope_breach_count_63d_d1(high, low, close):
    return f40_atxd_225_atr_envelope_breach_count_63d(high, low, close).diff()


ATR_EXPANSION_DYNAMICS_D1_REGISTRY_151_225 = {
    "f40_atxd_151_wilder_atr21_minus_sma_atr21_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_151_wilder_atr21_minus_sma_atr21_d1},
    "f40_atxd_152_ema_atr_over_wilder_atr_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_152_ema_atr_over_wilder_atr_21d_d1},
    "f40_atxd_153_double_smoothed_atr_ehlers_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_153_double_smoothed_atr_ehlers_21d_d1},
    "f40_atxd_154_median_true_range_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_154_median_true_range_21d_d1},
    "f40_atxd_155_mad_tr_around_median_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_155_mad_tr_around_median_21d_d1},
    "f40_atxd_156_keltner_channel_width_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_156_keltner_channel_width_21d_d1},
    "f40_atxd_157_pct_position_in_keltner_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_157_pct_position_in_keltner_21d_d1},
    "f40_atxd_158_bars_outside_keltner_upper_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_158_bars_outside_keltner_upper_63d_d1},
    "f40_atxd_159_starc_band_width_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_159_starc_band_width_21d_d1},
    "f40_atxd_160_chandelier_long_distance_22d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_160_chandelier_long_distance_22d_d1},
    "f40_atxd_161_bars_since_chandelier_long_violation_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_161_bars_since_chandelier_long_violation_252d_d1},
    "f40_atxd_162_psar_to_close_in_atr_units_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_162_psar_to_close_in_atr_units_21d_d1},
    "f40_atxd_163_atr_trailing_stop_giveback_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_163_atr_trailing_stop_giveback_252d_d1},
    "f40_atxd_164_plus_dm_share_of_tr_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_164_plus_dm_share_of_tr_14d_d1},
    "f40_atxd_165_minus_dm_share_of_tr_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_165_minus_dm_share_of_tr_14d_d1},
    "f40_atxd_166_dx_raw_directional_purity_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_166_dx_raw_directional_purity_14d_d1},
    "f40_atxd_167_adx_rate_of_change_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_167_adx_rate_of_change_14d_d1},
    "f40_atxd_168_nr4_indicator_count_63d_d1": {"inputs": ["high", "low"], "func": f40_atxd_168_nr4_indicator_count_63d_d1},
    "f40_atxd_169_nr7_indicator_count_63d_d1": {"inputs": ["high", "low"], "func": f40_atxd_169_nr7_indicator_count_63d_d1},
    "f40_atxd_170_wr7_indicator_count_63d_d1": {"inputs": ["high", "low"], "func": f40_atxd_170_wr7_indicator_count_63d_d1},
    "f40_atxd_171_inside_day_after_nr7_count_252d_d1": {"inputs": ["high", "low"], "func": f40_atxd_171_inside_day_after_nr7_count_252d_d1},
    "f40_atxd_172_id_nr4_count_252d_d1": {"inputs": ["high", "low"], "func": f40_atxd_172_id_nr4_count_252d_d1},
    "f40_atxd_173_adr_21d_d1": {"inputs": ["high", "low"], "func": f40_atxd_173_adr_21d_d1},
    "f40_atxd_174_adr_over_atr_ratio_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_174_adr_over_atr_ratio_21d_d1},
    "f40_atxd_175_adr_pct_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_175_adr_pct_21d_d1},
    "f40_atxd_176_demark_rei_8d_d1": {"inputs": ["high", "low"], "func": f40_atxd_176_demark_rei_8d_d1},
    "f40_atxd_177_demark_pressure_proxy_5d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_177_demark_pressure_proxy_5d_d1},
    "f40_atxd_178_nbar_true_range_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_178_nbar_true_range_21d_d1},
    "f40_atxd_179_tr_overlap_ratio_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_179_tr_overlap_ratio_21d_d1},
    "f40_atxd_180_kaufman_er_range_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_180_kaufman_er_range_21d_d1},
    "f40_atxd_181_vidya_style_atr_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_181_vidya_style_atr_21d_d1},
    "f40_atxd_182_chande_trend_adjusted_atr_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_182_chande_trend_adjusted_atr_21d_d1},
    "f40_atxd_183_ttm_squeeze_indicator_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_183_ttm_squeeze_indicator_d1},
    "f40_atxd_184_bars_since_ttm_squeeze_release_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_184_bars_since_ttm_squeeze_release_d1},
    "f40_atxd_185_atr_cone_aperture_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_185_atr_cone_aperture_252d_d1},
    "f40_atxd_186_atr_cone_slope_diff_p90_p10_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_186_atr_cone_slope_diff_p90_p10_d1},
    "f40_atxd_187_upper_shadow_over_tr_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_187_upper_shadow_over_tr_21d_d1},
    "f40_atxd_188_lower_shadow_over_tr_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_188_lower_shadow_over_tr_21d_d1},
    "f40_atxd_189_body_over_tr_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_189_body_over_tr_21d_d1},
    "f40_atxd_190_close_position_in_range_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_190_close_position_in_range_21d_d1},
    "f40_atxd_191_mean_intrabar_gap_clamp_share_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_191_mean_intrabar_gap_clamp_share_21d_d1},
    "f40_atxd_192_realized_range_christensen_podolskij_21d_d1": {"inputs": ["high", "low"], "func": f40_atxd_192_realized_range_christensen_podolskij_21d_d1},
    "f40_atxd_193_range_jump_abdl_proxy_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_193_range_jump_abdl_proxy_21d_d1},
    "f40_atxd_194_atr_term_structure_curvature_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_194_atr_term_structure_curvature_d1},
    "f40_atxd_195_atr_term_structure_inversion_flag_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_195_atr_term_structure_inversion_flag_d1},
    "f40_atxd_196_atr_term_structure_pc1_level_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_196_atr_term_structure_pc1_level_d1},
    "f40_atxd_197_signed_tr_close_open_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_197_signed_tr_close_open_21d_d1},
    "f40_atxd_198_signed_tr_close_prev_close_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_198_signed_tr_close_prev_close_21d_d1},
    "f40_atxd_199_vortex_vi_plus_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_199_vortex_vi_plus_14d_d1},
    "f40_atxd_200_vortex_vi_minus_14d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_200_vortex_vi_minus_14d_d1},
    "f40_atxd_201_gini_tr_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_201_gini_tr_252d_d1},
    "f40_atxd_202_top5_bar_tr_share_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_202_top5_bar_tr_share_252d_d1},
    "f40_atxd_203_hill_tail_index_tr_top10_1260d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_203_hill_tail_index_tr_top10_1260d_d1},
    "f40_atxd_204_atr_up_vs_down_days_ratio_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_204_atr_up_vs_down_days_ratio_21d_d1},
    "f40_atxd_205_mean_tr_gap_up_vs_gap_down_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f40_atxd_205_mean_tr_gap_up_vs_gap_down_63d_d1},
    "f40_atxd_206_day_after_shock_tr_mean_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_206_day_after_shock_tr_mean_63d_d1},
    "f40_atxd_207_tr_up_move_share_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_207_tr_up_move_share_21d_d1},
    "f40_atxd_208_plus_dm_streak_count_21d_d1": {"inputs": ["high", "low"], "func": f40_atxd_208_plus_dm_streak_count_21d_d1},
    "f40_atxd_209_minus_dm_streak_count_21d_d1": {"inputs": ["high", "low"], "func": f40_atxd_209_minus_dm_streak_count_21d_d1},
    "f40_atxd_210_range_to_return_efficiency_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_210_range_to_return_efficiency_21d_d1},
    "f40_atxd_211_abs_ret_over_tr_ratio_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_211_abs_ret_over_tr_ratio_63d_d1},
    "f40_atxd_212_atr_normalized_close_change_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_212_atr_normalized_close_change_21d_d1},
    "f40_atxd_213_mesa_phase_log_atr_proxy_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_213_mesa_phase_log_atr_proxy_252d_d1},
    "f40_atxd_214_atr_cycle_expansion_indicator_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_214_atr_cycle_expansion_indicator_d1},
    "f40_atxd_215_atr_acceleration_cycle_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_215_atr_acceleration_cycle_252d_d1},
    "f40_atxd_216_atr_pos_vs_neg_close_ratio_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_216_atr_pos_vs_neg_close_ratio_252d_d1},
    "f40_atxd_217_atr_compression_event_count_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_217_atr_compression_event_count_63d_d1},
    "f40_atxd_218_atr_oscillator_macd_style_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_218_atr_oscillator_macd_style_21d_d1},
    "f40_atxd_219_atr_oscillator_signal_252d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_219_atr_oscillator_signal_252d_d1},
    "f40_atxd_220_atr_smoothing_dispersion_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_220_atr_smoothing_dispersion_d1},
    "f40_atxd_221_avg_tr_in_high_volume_decile_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f40_atxd_221_avg_tr_in_high_volume_decile_252d_d1},
    "f40_atxd_222_atr_squeeze_release_strength_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_222_atr_squeeze_release_strength_63d_d1},
    "f40_atxd_223_atr_volatility_smile_curvature_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_223_atr_volatility_smile_curvature_d1},
    "f40_atxd_224_natr_ema_smoothed_21d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_224_natr_ema_smoothed_21d_d1},
    "f40_atxd_225_atr_envelope_breach_count_63d_d1": {"inputs": ["high", "low", "close"], "func": f40_atxd_225_atr_envelope_breach_count_63d_d1},
}
