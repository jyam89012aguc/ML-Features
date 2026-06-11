"""on_balance_volume_dynamics d2 features 151-225 — Pipeline 1b-technical (extension).

Gapless extension building on 001-150. New buckets identified via literature review:
- Cumulative Volume Delta (CVD) proxies using close-position-in-bar-range
- OBV-RSI / OBV-Stochastic / OBV-MACD oscillators (Wyckoff "effort-vs-result" overlays)
- OBV-Bollinger Bands envelope
- Wyckoff phase A/B/C/D/E proxy classifiers on OBV
- Distribution-day OBV variant (O'Neil-style close-down + OBV-down compound)
- OBV jump detection (Lee-Mykland on OBV-diff)
- Order flow imbalance proxy from OHLC (Lee-Ready-style on daily bars)

CAREFUL — sibling family 23 (accumulation_distribution_line) owns A/D, CMF, MFI, KVO,
Force. This file STRICTLY stays in sign-of-direction × volume cumulative territory.
CVD proxies here use close-position-in-bar-range as a DIRECT delta-up/delta-down split,
which is a different primitive from CMF's (close-low - high-close)/(high-low) weighting.

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


# ---------------------------- OBV primitives ----------------------------

def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Classic OBV: cumulative sum of signed volume."""
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _cvd_proxy(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative Volume Delta proxy: use close-position-in-bar-range to split each bar's volume into buy/sell halves.
    delta = (2 * (close - low) / (high - low) - 1) * volume = signed-volume scaled by close strength in bar.
    Cumsum yields the CVD proxy series. Distinct from CMF (which divides by total range volume sum)."""
    cpos = _safe_div(close - low, high - low)
    delta = (2.0 * cpos - 1.0) * volume
    return delta.cumsum()


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


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rolling_argmax_age(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _a(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return s.rolling(window, min_periods=min_periods).apply(_a, raw=True)


# ============================================================
# Bucket N — Cumulative Volume Delta (CVD) proxies (151-160)
# ============================================================

def f22_obvd_151_cvd_proxy_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of CVD proxy (close-position-weighted signed volume cumulative). Differs from OBV in granularity."""
    return _rolling_zscore(_cvd_proxy(high, low, close, volume), YDAYS)


def f22_obvd_152_cvd_proxy_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CVD proxy slope over 63d — close-strength-weighted cumulative-flow trend."""
    return _rolling_slope(_cvd_proxy(high, low, close, volume), QDAYS)


def f22_obvd_153_cvd_proxy_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CVD proxy slope over 252d — annual close-weighted cumulative-flow trend."""
    return _rolling_slope(_cvd_proxy(high, low, close, volume), YDAYS)


def f22_obvd_154_cvd_proxy_minus_obv_252d_norm(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(CVD proxy - OBV) z-scored(252d) — disagreement between close-position-weighted and sign-of-close cumulative flows."""
    diff = _cvd_proxy(high, low, close, volume) - _obv(close, volume)
    return _rolling_zscore(diff, YDAYS)


def f22_obvd_155_cvd_proxy_drawdown_from_max_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CVD proxy minus 252d trailing max — drawdown."""
    cvd = _cvd_proxy(high, low, close, volume)
    return cvd - cvd.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_156_cvd_proxy_age_of_max_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 252d-trailing CVD proxy max — flow-peak staleness."""
    return _rolling_argmax_age(_cvd_proxy(high, low, close, volume), YDAYS)


def f22_obvd_157_cvd_proxy_minus_price_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CVD proxy slope(252d) minus log-price slope(252d) — CVD-price divergence."""
    return _rolling_slope(_cvd_proxy(high, low, close, volume), YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


def f22_obvd_158_cvd_proxy_corr_close_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation of CVD proxy with close over 252d."""
    return _cvd_proxy(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).corr(close)


def f22_obvd_159_cvd_proxy_below_zero_dwell_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars with CVD proxy < 0 (net selling pressure cumulative)."""
    cvd = _cvd_proxy(high, low, close, volume)
    return (cvd < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_160_cvd_proxy_diff_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily CVD proxy change — close-weighted signed-vol per-bar impulse."""
    return _rolling_zscore(_cvd_proxy(high, low, close, volume).diff(), YDAYS)


# ============================================================
# Bucket O — OBV oscillators (RSI / Stochastic / MACD-style) (161-170)
# ============================================================

def f22_obvd_161_obv_rsi_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(14) applied to OBV-diff (signed volume). 100*(EMA gain) / (EMA gain + EMA loss)."""
    obv = _obv(close, volume)
    delta = obv.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    ag = gain.ewm(alpha=1.0 / 14, min_periods=14, adjust=False).mean()
    al = loss.ewm(alpha=1.0 / 14, min_periods=14, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)


def f22_obvd_162_obv_rsi_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(21) applied to OBV-diff."""
    obv = _obv(close, volume)
    delta = obv.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    ag = gain.ewm(alpha=1.0 / MDAYS, min_periods=MDAYS, adjust=False).mean()
    al = loss.ewm(alpha=1.0 / MDAYS, min_periods=MDAYS, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)


def f22_obvd_163_obv_stoch_k_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %K(14) applied to OBV level: (OBV - 14d-min) / (14d-max - 14d-min) × 100."""
    obv = _obv(close, volume)
    rmax = obv.rolling(14, min_periods=5).max()
    rmin = obv.rolling(14, min_periods=5).min()
    return 100.0 * _safe_div(obv - rmin, rmax - rmin)


def f22_obvd_164_obv_stoch_k_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %K(63) applied to OBV level."""
    obv = _obv(close, volume)
    rmax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return 100.0 * _safe_div(obv - rmin, rmax - rmin)


def f22_obvd_165_obv_stoch_d_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %D(14, smoothing 3) of OBV — smoothed %K."""
    obv = _obv(close, volume)
    rmax = obv.rolling(14, min_periods=5).max()
    rmin = obv.rolling(14, min_periods=5).min()
    k = 100.0 * _safe_div(obv - rmin, rmax - rmin)
    return k.rolling(3, min_periods=2).mean()


def f22_obvd_166_obv_macd_line_12_26(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD line on OBV: EMA(12, OBV) - EMA(26, OBV)."""
    obv = _obv(close, volume)
    return obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()


def f22_obvd_167_obv_macd_signal_12_26_9(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Signal line: 9-period EMA of OBV-MACD line."""
    obv = _obv(close, volume)
    macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    return macd.ewm(span=9, min_periods=4, adjust=False).mean()


def f22_obvd_168_obv_macd_histogram(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD histogram on OBV: MACD - signal."""
    obv = _obv(close, volume)
    macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    return macd - signal


def f22_obvd_169_obv_macd_hist_zerocross_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-MACD-histogram zero crossings — momentum-shift event count."""
    obv = _obv(close, volume)
    macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    hist = macd - signal
    cross = (np.sign(hist).diff().abs() > 0).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_170_obv_williams_r_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R(14) on OBV: -100 * (14d-max - OBV) / (14d-max - 14d-min)."""
    obv = _obv(close, volume)
    rmax = obv.rolling(14, min_periods=5).max()
    rmin = obv.rolling(14, min_periods=5).min()
    return -100.0 * _safe_div(rmax - obv, rmax - rmin)


# ============================================================
# Bucket P — OBV-Bollinger Bands envelope (171-180)
# ============================================================

def f22_obvd_171_obv_bb_upper_20d_2sigma_distance(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV - (OBV 20d-EMA + 2*OBV 20d-std). Positive = OBV above upper BB."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    return obv - (m + 2.0 * s)


def f22_obvd_172_obv_bb_lower_20d_2sigma_distance(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV - (20d-mean - 2*20d-std). Negative = OBV below lower BB."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    return obv - (m - 2.0 * s)


def f22_obvd_173_obv_bb_percent_b_20d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """%B for OBV BB(20, 2): (OBV - lower) / (upper - lower). 0 = at lower; 1 = at upper."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    return _safe_div(obv - (m - 2.0 * s), 4.0 * s)


def f22_obvd_174_obv_bb_bandwidth_20d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV BB bandwidth: 4*std / mean — relative volatility-of-OBV."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    return _safe_div(4.0 * s, m.abs() + 1.0)


def f22_obvd_175_obv_above_upper_bb_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV > upper-BB."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    return (obv > upper).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_176_obv_below_lower_bb_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV < lower-BB."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    lower = m - 2.0 * s
    return (obv < lower).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_177_obv_walking_upper_bb_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV has been above upper-BB for 3 consecutive bars — 'walking the band'."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    streak = _consecutive_true_streak(obv > upper).astype(float)
    return (streak >= 3).astype(float)


def f22_obvd_178_obv_bb_squeeze_indicator_20d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV BB bandwidth is in bottom decile of trailing 252d — flow-volatility compression."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    bw = _safe_div(4.0 * s, m.abs() + 1.0)
    pr = _rolling_pct_rank(bw, YDAYS)
    return (pr <= 0.10).astype(float)


def f22_obvd_179_obv_bb_break_to_walk_failure_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV crossed upper-BB but did NOT stay above for >= 3 bars."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    upper = m + 2.0 * s
    cur_above = obv > upper
    crossed = cur_above & (~cur_above.shift(1).fillna(False))
    streak = _consecutive_true_streak(cur_above).astype(float)
    fail = (crossed & (streak < 3))
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_180_obv_bb_percent_b_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank(252d) of OBV %B (20,2) — where current OBV sits in its trailing BB envelope distribution."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    pctb = _safe_div(obv - (m - 2.0 * s), 4.0 * s)
    return _rolling_pct_rank(pctb, YDAYS)


# ============================================================
# Bucket Q — Wyckoff phase classifiers on OBV (181-190)
# ============================================================

def f22_obvd_181_wyckoff_phase_a_obv_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-A (selling climax / AR): trailing 21d count of bars with OBV-diff z(252d) < -2."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z < -2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f22_obvd_182_wyckoff_phase_b_obv_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-B (cause-building): trailing 63d std(OBV-diff)/mean(|OBV-diff|) — high churn-like dispersion."""
    obv = _obv(close, volume)
    d = obv.diff()
    return _safe_div(d.rolling(QDAYS, min_periods=MDAYS).std(), d.abs().rolling(QDAYS, min_periods=MDAYS).mean())


def f22_obvd_183_wyckoff_phase_c_obv_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-C (UTAD on OBV): bars with new 63d-high price AND OBV not at new 63d-high — divergence count(63d)."""
    obv = _obv(close, volume)
    pmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    flag = ((high >= pmax63) & (obv < omax63)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_184_wyckoff_phase_d_obv_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-D (markdown begin): trailing 63d count of bars with OBV-diff z(252d) < -1.5 AND close < EMA63."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    ema63c = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    flag = ((z < -1.5) & (close < ema63c)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_185_wyckoff_phase_e_obv_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Phase-E (markdown continuation): trailing 63d fraction of bars with OBV below EMA63(OBV) AND close < EMA63(close)."""
    obv = _obv(close, volume)
    obv_ema63 = obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    ema63c = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    return ((obv < obv_ema63) & (close < ema63c)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f22_obvd_186_wyckoff_composite_phase_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of OBV Phase-B + Phase-C + Phase-D scores — overall distribution-phase intensity."""
    obv = _obv(close, volume)
    d = obv.diff()
    phase_b = _safe_div(d.rolling(QDAYS, min_periods=MDAYS).std(), d.abs().rolling(QDAYS, min_periods=MDAYS).mean()).fillna(0.0)
    pmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    phase_c = ((high >= pmax63) & (obv < omax63)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    z = _rolling_zscore(d, YDAYS)
    ema63c = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    phase_d = ((z < -1.5) & (close < ema63c)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return phase_b + phase_c / 10.0 + phase_d / 10.0


def f22_obvd_187_obv_trading_range_indicator_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV has been within ±1 std of 252d-mean for >= 21 consecutive bars — flat-range Wyckoff TR."""
    obv = _obv(close, volume)
    m = obv.rolling(YDAYS, min_periods=QDAYS).mean()
    s = obv.rolling(YDAYS, min_periods=QDAYS).std()
    cond = obv.between(m - s, m + s)
    streak = _consecutive_true_streak(cond).astype(float)
    return (streak >= MDAYS).astype(float)


def f22_obvd_188_obv_trading_range_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars where OBV is in ±1 std of 252d-mean (consolidation dwell)."""
    obv = _obv(close, volume)
    m = obv.rolling(YDAYS, min_periods=QDAYS).mean()
    s = obv.rolling(YDAYS, min_periods=QDAYS).std()
    return obv.between(m - s, m + s).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_189_obv_breakout_failure_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV broke above the upper-1-sigma band but returned within 5 bars."""
    obv = _obv(close, volume)
    m = obv.rolling(YDAYS, min_periods=QDAYS).mean()
    s = obv.rolling(YDAYS, min_periods=QDAYS).std()
    upper = m + s
    cross_up = (obv > upper) & (obv.shift(1) <= upper.shift(1))
    came_back = obv.shift(5) <= upper.shift(5)  # peek-back — replace with PIT-safe variant
    # PIT-safe: count cross-up events where OBV crossed back DOWN within trailing 5 of cross. Use rolling lookback.
    obv_above = obv > upper
    cross_back = (~obv_above) & obv_above.shift(1).fillna(False)
    fail_recent = (cross_back & cross_up.rolling(5, min_periods=1).max().astype(bool))
    return fail_recent.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_190_obv_lpsy_proxy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """LPSY proxy on OBV: trailing 63d count of bars where OBV up-streak shorter than 5 AND OBV below 21d-EMA."""
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    up_streak = _consecutive_true_streak(sgn > 0).astype(float)
    ema21 = obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    flag = ((up_streak > 0) & (up_streak < 5) & (obv < ema21)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket R — Distribution-day OBV variant (191-200)
# ============================================================

def f22_obvd_191_obv_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV distribution day: close down >0.2% AND OBV-diff < 0 (signed-vol confirms selling pressure)."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    return ((pc < -0.002) & (obv_d < 0)).astype(float)


def f22_obvd_192_obv_distribution_day_count_25d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 25d count of OBV distribution days."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    return ((pc < -0.002) & (obv_d < 0)).astype(float).rolling(25, min_periods=10).sum()


def f22_obvd_193_obv_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of OBV distribution days."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    return ((pc < -0.002) & (obv_d < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_194_obv_dd_severity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of |close pct_change| × |OBV-diff z(252d)| on OBV distribution days only."""
    pc = close.pct_change()
    obv = _obv(close, volume)
    obv_d = obv.diff()
    z = _rolling_zscore(obv_d, YDAYS)
    sev = pc.abs() * z.abs()
    flag = (pc < -0.002) & (obv_d < 0)
    return sev.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_195_consec_obv_dd_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of OBV distribution days."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    cond = (pc < -0.002) & (obv_d < 0)
    return _consecutive_true_streak(cond).astype(float)


def f22_obvd_196_obv_dd_cluster_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when >=4 OBV distribution days in trailing 25 bars."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    flag = ((pc < -0.002) & (obv_d < 0)).astype(float)
    return (flag.rolling(25, min_periods=10).sum() >= 4).astype(float)


def f22_obvd_197_obv_dd_after_252d_high_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of OBV distribution days occurring when prior 21d contained a 252d-high event."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).astype(float).rolling(MDAYS, min_periods=WDAYS).max() > 0
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    dd = (pc < -0.002) & (obv_d < 0) & recent_peak
    return dd.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_198_obv_dd_to_obv_ad_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d OBV-DD count) / (63d OBV accumulation day count: close up>0.2% AND OBV-diff>0)."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    dd = ((pc < -0.002) & (obv_d < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ad = ((pc > 0.002) & (obv_d > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dd, ad + 1.0)


def f22_obvd_199_obv_strict_dd_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict OBV-DD: close down >1% AND OBV-diff z(252d) < -1."""
    pc = close.pct_change()
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return ((pc < -0.01) & (z < -1.0)).astype(float)


def f22_obvd_200_obv_strict_dd_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of strict OBV distribution days."""
    pc = close.pct_change()
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return ((pc < -0.01) & (z < -1.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket S — OBV jump detection (Lee-Mykland) (201-210)
# ============================================================

def f22_obvd_201_lee_mykland_jump_stat_obvdiff_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lee-Mykland statistic on OBV-diff over 21d: |OBV-diff_t| / sqrt(local bipower variation)."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    return _safe_div(d.abs(), sigma)


def f22_obvd_202_lee_mykland_jump_count_above_4_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where LM stat on OBV-diff > 4 — major flow jumps."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    return (jstat > 4.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_203_signed_obv_jump_sum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of sign(OBV-diff) × LM stat on jump bars only (LM > 3)."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    signed = np.sign(d) * jstat
    return signed.where(jstat > 3.0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_204_positive_obv_jump_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of positive OBV-diff jumps (LM > 3 AND OBV-diff > 0)."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    return ((jstat > 3.0) & (d > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_205_negative_obv_jump_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of negative OBV-diff jumps (LM > 3 AND OBV-diff < 0)."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    return ((jstat > 3.0) & (d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_206_obv_jump_intensity_cum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (LM-stat)+ — cumulative OBV jump magnitude."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    return jstat.clip(lower=0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_207_obv_jump_negative_to_positive_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d count negative OBV jumps) / (252d count positive OBV jumps) — > 1 = distribution-leaning."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    pos = ((jstat > 3.0) & (d > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = ((jstat > 3.0) & (d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(neg, pos + 1.0)


def f22_obvd_208_obv_jump_clustering_iat_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean inter-arrival of OBV-jumps (LM>3) in trailing 252d."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    def _miat(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return float(v.size)
        return float(np.mean(np.diff(pos)))
    return jstat.rolling(YDAYS, min_periods=QDAYS).apply(_miat, raw=True)


def f22_obvd_209_obv_jump_z_at_price_high_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean LM-stat on bars where high is at trailing 252d max — flow-jump intensity at price peaks."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return jstat.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_210_bnstest_obv_jump_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Barndorff-Nielsen-Shephard test on OBV-diff: (RV - BV) / RV — jump-component share."""
    obv = _obv(close, volume)
    d = obv.diff()
    rv = (d ** 2).rolling(MDAYS, min_periods=WDAYS).sum()
    bv = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    return _safe_div(rv - bv, rv)


# ============================================================
# Bucket T — Order flow imbalance proxy from OHLC (Lee-Ready style) (211-220)
# ============================================================

def _lee_ready_proxy(close: pd.Series) -> pd.Series:
    """Lee-Ready proxy on daily bars: sign(close_t - close_{t-1}) if pct_change != 0 else last sign.
    Used as a daily-trade-direction estimator."""
    sgn = np.sign(close.diff()).replace(0.0, np.nan).ffill().fillna(0.0)
    return sgn


def f22_obvd_211_lee_ready_directional_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (Lee-Ready proxy × volume) over trailing 21d — short-horizon directional flow."""
    return (_lee_ready_proxy(close) * volume).rolling(MDAYS, min_periods=WDAYS).sum()


def f22_obvd_212_lee_ready_directional_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (Lee-Ready proxy × volume) over trailing 63d."""
    return (_lee_ready_proxy(close) * volume).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_213_lee_ready_signed_dv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (Lee-Ready proxy × dollar_vol) over trailing 252d — annual directional $-flow."""
    return (_lee_ready_proxy(close) * (close * volume)).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_214_order_flow_imbalance_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Order flow imbalance ratio = sum(Lee-Ready vol) / sum(total vol) over trailing 63d. Range [-1, 1]."""
    return _safe_div((_lee_ready_proxy(close) * volume).rolling(QDAYS, min_periods=MDAYS).sum(),
                     volume.rolling(QDAYS, min_periods=MDAYS).sum())


def f22_obvd_215_order_flow_imbalance_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Order flow imbalance ratio over 252d."""
    return _safe_div((_lee_ready_proxy(close) * volume).rolling(YDAYS, min_periods=QDAYS).sum(),
                     volume.rolling(YDAYS, min_periods=QDAYS).sum())


def f22_obvd_216_order_flow_imbalance_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily Lee-Ready signed-volume."""
    sv = _lee_ready_proxy(close) * volume
    return _rolling_zscore(sv, YDAYS)


def f22_obvd_217_order_flow_dispersion_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of Lee-Ready signed-volume over 63d — dispersion of directional flow."""
    sv = _lee_ready_proxy(close) * volume
    return sv.rolling(QDAYS, min_periods=MDAYS).std()


def f22_obvd_218_order_flow_signed_dollar_vol_252d_slope(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(252d) of cumulative Lee-Ready signed-$-vol — directional $-flow trend."""
    cum = (_lee_ready_proxy(close) * (close * volume)).cumsum()
    return _rolling_slope(cum, YDAYS)


def f22_obvd_219_negative_order_flow_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (vol on Lee-Ready-negative bars) — total selling-pressure proxy."""
    sv = _lee_ready_proxy(close) * volume
    return (-sv.where(sv < 0, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_220_directional_flow_failure_to_confirm_high_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (high = 252d-max) AND (order flow imbalance ratio 21d < 0)."""
    sv = _lee_ready_proxy(close) * volume
    ofi = _safe_div(sv.rolling(MDAYS, min_periods=WDAYS).sum(), volume.rolling(MDAYS, min_periods=WDAYS).sum())
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (ofi < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket U — Effort-vs-result on OBV (221-225)
# ============================================================

def f22_obvd_221_obv_diff_per_pct_change_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d mean of |OBV-diff| / |close pct_change| — effort (signed vol) per unit result (price move)."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs(), close.pct_change().abs()).rolling(MDAYS, min_periods=WDAYS).mean()


def f22_obvd_222_obv_diff_per_pct_change_252d_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily |OBV-diff| / |close pct_change|."""
    obv = _obv(close, volume)
    return _rolling_zscore(_safe_div(obv.diff().abs(), close.pct_change().abs()), YDAYS)


def f22_obvd_223_obv_effort_low_result_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where |OBV-diff| z(252d) > 1 AND |close pct_change| < 0.5%."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff().abs(), YDAYS)
    pc = close.pct_change().abs()
    return ((z > 1.0) & (pc < 0.005)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_224_obv_result_to_effort_corr_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d Pearson correlation between |OBV-diff| and |close pct_change|. Low = effort-result decoupled."""
    obv = _obv(close, volume)
    return obv.diff().abs().rolling(YDAYS, min_periods=QDAYS).corr(close.pct_change().abs())


def f22_obvd_225_obv_effort_overshoot_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (|OBV-diff| - 21d-rolling-mean |OBV-diff|) — effort spike vs trailing baseline."""
    obv = _obv(close, volume)
    d = obv.diff().abs()
    baseline = d.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(d - baseline, YDAYS)


def f22_obvd_151_cvd_proxy_zscore_252d_d2(high, low, close, volume):
    return f22_obvd_151_cvd_proxy_zscore_252d(high, low, close, volume).diff().diff()


def f22_obvd_152_cvd_proxy_slope_63d_d2(high, low, close, volume):
    return f22_obvd_152_cvd_proxy_slope_63d(high, low, close, volume).diff().diff()


def f22_obvd_153_cvd_proxy_slope_252d_d2(high, low, close, volume):
    return f22_obvd_153_cvd_proxy_slope_252d(high, low, close, volume).diff().diff()


def f22_obvd_154_cvd_proxy_minus_obv_252d_norm_d2(high, low, close, volume):
    return f22_obvd_154_cvd_proxy_minus_obv_252d_norm(high, low, close, volume).diff().diff()


def f22_obvd_155_cvd_proxy_drawdown_from_max_252d_d2(high, low, close, volume):
    return f22_obvd_155_cvd_proxy_drawdown_from_max_252d(high, low, close, volume).diff().diff()


def f22_obvd_156_cvd_proxy_age_of_max_252d_d2(high, low, close, volume):
    return f22_obvd_156_cvd_proxy_age_of_max_252d(high, low, close, volume).diff().diff()


def f22_obvd_157_cvd_proxy_minus_price_slope_252d_d2(high, low, close, volume):
    return f22_obvd_157_cvd_proxy_minus_price_slope_252d(high, low, close, volume).diff().diff()


def f22_obvd_158_cvd_proxy_corr_close_252d_d2(high, low, close, volume):
    return f22_obvd_158_cvd_proxy_corr_close_252d(high, low, close, volume).diff().diff()


def f22_obvd_159_cvd_proxy_below_zero_dwell_252d_d2(high, low, close, volume):
    return f22_obvd_159_cvd_proxy_below_zero_dwell_252d(high, low, close, volume).diff().diff()


def f22_obvd_160_cvd_proxy_diff_zscore_252d_d2(high, low, close, volume):
    return f22_obvd_160_cvd_proxy_diff_zscore_252d(high, low, close, volume).diff().diff()


def f22_obvd_161_obv_rsi_14d_d2(close, volume):
    return f22_obvd_161_obv_rsi_14d(close, volume).diff().diff()


def f22_obvd_162_obv_rsi_21d_d2(close, volume):
    return f22_obvd_162_obv_rsi_21d(close, volume).diff().diff()


def f22_obvd_163_obv_stoch_k_14d_d2(close, volume):
    return f22_obvd_163_obv_stoch_k_14d(close, volume).diff().diff()


def f22_obvd_164_obv_stoch_k_63d_d2(close, volume):
    return f22_obvd_164_obv_stoch_k_63d(close, volume).diff().diff()


def f22_obvd_165_obv_stoch_d_14d_d2(close, volume):
    return f22_obvd_165_obv_stoch_d_14d(close, volume).diff().diff()


def f22_obvd_166_obv_macd_line_12_26_d2(close, volume):
    return f22_obvd_166_obv_macd_line_12_26(close, volume).diff().diff()


def f22_obvd_167_obv_macd_signal_12_26_9_d2(close, volume):
    return f22_obvd_167_obv_macd_signal_12_26_9(close, volume).diff().diff()


def f22_obvd_168_obv_macd_histogram_d2(close, volume):
    return f22_obvd_168_obv_macd_histogram(close, volume).diff().diff()


def f22_obvd_169_obv_macd_hist_zerocross_count_252d_d2(close, volume):
    return f22_obvd_169_obv_macd_hist_zerocross_count_252d(close, volume).diff().diff()


def f22_obvd_170_obv_williams_r_14d_d2(close, volume):
    return f22_obvd_170_obv_williams_r_14d(close, volume).diff().diff()


def f22_obvd_171_obv_bb_upper_20d_2sigma_distance_d2(close, volume):
    return f22_obvd_171_obv_bb_upper_20d_2sigma_distance(close, volume).diff().diff()


def f22_obvd_172_obv_bb_lower_20d_2sigma_distance_d2(close, volume):
    return f22_obvd_172_obv_bb_lower_20d_2sigma_distance(close, volume).diff().diff()


def f22_obvd_173_obv_bb_percent_b_20d_d2(close, volume):
    return f22_obvd_173_obv_bb_percent_b_20d(close, volume).diff().diff()


def f22_obvd_174_obv_bb_bandwidth_20d_d2(close, volume):
    return f22_obvd_174_obv_bb_bandwidth_20d(close, volume).diff().diff()


def f22_obvd_175_obv_above_upper_bb_count_252d_d2(close, volume):
    return f22_obvd_175_obv_above_upper_bb_count_252d(close, volume).diff().diff()


def f22_obvd_176_obv_below_lower_bb_count_252d_d2(close, volume):
    return f22_obvd_176_obv_below_lower_bb_count_252d(close, volume).diff().diff()


def f22_obvd_177_obv_walking_upper_bb_indicator_d2(close, volume):
    return f22_obvd_177_obv_walking_upper_bb_indicator(close, volume).diff().diff()


def f22_obvd_178_obv_bb_squeeze_indicator_20d_d2(close, volume):
    return f22_obvd_178_obv_bb_squeeze_indicator_20d(close, volume).diff().diff()


def f22_obvd_179_obv_bb_break_to_walk_failure_252d_d2(close, volume):
    return f22_obvd_179_obv_bb_break_to_walk_failure_252d(close, volume).diff().diff()


def f22_obvd_180_obv_bb_percent_b_pct_rank_252d_d2(close, volume):
    return f22_obvd_180_obv_bb_percent_b_pct_rank_252d(close, volume).diff().diff()


def f22_obvd_181_wyckoff_phase_a_obv_score_252d_d2(close, volume):
    return f22_obvd_181_wyckoff_phase_a_obv_score_252d(close, volume).diff().diff()


def f22_obvd_182_wyckoff_phase_b_obv_score_252d_d2(close, volume):
    return f22_obvd_182_wyckoff_phase_b_obv_score_252d(close, volume).diff().diff()


def f22_obvd_183_wyckoff_phase_c_obv_score_252d_d2(high, close, volume):
    return f22_obvd_183_wyckoff_phase_c_obv_score_252d(high, close, volume).diff().diff()


def f22_obvd_184_wyckoff_phase_d_obv_score_252d_d2(close, volume):
    return f22_obvd_184_wyckoff_phase_d_obv_score_252d(close, volume).diff().diff()


def f22_obvd_185_wyckoff_phase_e_obv_score_252d_d2(close, volume):
    return f22_obvd_185_wyckoff_phase_e_obv_score_252d(close, volume).diff().diff()


def f22_obvd_186_wyckoff_composite_phase_score_252d_d2(high, close, volume):
    return f22_obvd_186_wyckoff_composite_phase_score_252d(high, close, volume).diff().diff()


def f22_obvd_187_obv_trading_range_indicator_252d_d2(close, volume):
    return f22_obvd_187_obv_trading_range_indicator_252d(close, volume).diff().diff()


def f22_obvd_188_obv_trading_range_dwell_252d_d2(close, volume):
    return f22_obvd_188_obv_trading_range_dwell_252d(close, volume).diff().diff()


def f22_obvd_189_obv_breakout_failure_count_252d_d2(close, volume):
    return f22_obvd_189_obv_breakout_failure_count_252d(close, volume).diff().diff()


def f22_obvd_190_obv_lpsy_proxy_252d_d2(close, volume):
    return f22_obvd_190_obv_lpsy_proxy_252d(close, volume).diff().diff()


def f22_obvd_191_obv_distribution_day_indicator_d2(close, volume):
    return f22_obvd_191_obv_distribution_day_indicator(close, volume).diff().diff()


def f22_obvd_192_obv_distribution_day_count_25d_d2(close, volume):
    return f22_obvd_192_obv_distribution_day_count_25d(close, volume).diff().diff()


def f22_obvd_193_obv_distribution_day_count_63d_d2(close, volume):
    return f22_obvd_193_obv_distribution_day_count_63d(close, volume).diff().diff()


def f22_obvd_194_obv_dd_severity_252d_d2(close, volume):
    return f22_obvd_194_obv_dd_severity_252d(close, volume).diff().diff()


def f22_obvd_195_consec_obv_dd_streak_d2(close, volume):
    return f22_obvd_195_consec_obv_dd_streak(close, volume).diff().diff()


def f22_obvd_196_obv_dd_cluster_5d_indicator_d2(close, volume):
    return f22_obvd_196_obv_dd_cluster_5d_indicator(close, volume).diff().diff()


def f22_obvd_197_obv_dd_after_252d_high_count_63d_d2(high, close, volume):
    return f22_obvd_197_obv_dd_after_252d_high_count_63d(high, close, volume).diff().diff()


def f22_obvd_198_obv_dd_to_obv_ad_ratio_63d_d2(close, volume):
    return f22_obvd_198_obv_dd_to_obv_ad_ratio_63d(close, volume).diff().diff()


def f22_obvd_199_obv_strict_dd_indicator_d2(close, volume):
    return f22_obvd_199_obv_strict_dd_indicator(close, volume).diff().diff()


def f22_obvd_200_obv_strict_dd_count_252d_d2(close, volume):
    return f22_obvd_200_obv_strict_dd_count_252d(close, volume).diff().diff()


def f22_obvd_201_lee_mykland_jump_stat_obvdiff_21d_d2(close, volume):
    return f22_obvd_201_lee_mykland_jump_stat_obvdiff_21d(close, volume).diff().diff()


def f22_obvd_202_lee_mykland_jump_count_above_4_252d_d2(close, volume):
    return f22_obvd_202_lee_mykland_jump_count_above_4_252d(close, volume).diff().diff()


def f22_obvd_203_signed_obv_jump_sum_252d_d2(close, volume):
    return f22_obvd_203_signed_obv_jump_sum_252d(close, volume).diff().diff()


def f22_obvd_204_positive_obv_jump_count_252d_d2(close, volume):
    return f22_obvd_204_positive_obv_jump_count_252d(close, volume).diff().diff()


def f22_obvd_205_negative_obv_jump_count_252d_d2(close, volume):
    return f22_obvd_205_negative_obv_jump_count_252d(close, volume).diff().diff()


def f22_obvd_206_obv_jump_intensity_cum_252d_d2(close, volume):
    return f22_obvd_206_obv_jump_intensity_cum_252d(close, volume).diff().diff()


def f22_obvd_207_obv_jump_negative_to_positive_ratio_252d_d2(close, volume):
    return f22_obvd_207_obv_jump_negative_to_positive_ratio_252d(close, volume).diff().diff()


def f22_obvd_208_obv_jump_clustering_iat_252d_d2(close, volume):
    return f22_obvd_208_obv_jump_clustering_iat_252d(close, volume).diff().diff()


def f22_obvd_209_obv_jump_z_at_price_high_252d_d2(high, close, volume):
    return f22_obvd_209_obv_jump_z_at_price_high_252d(high, close, volume).diff().diff()


def f22_obvd_210_bnstest_obv_jump_ratio_252d_d2(close, volume):
    return f22_obvd_210_bnstest_obv_jump_ratio_252d(close, volume).diff().diff()


def f22_obvd_211_lee_ready_directional_volume_21d_d2(close, volume):
    return f22_obvd_211_lee_ready_directional_volume_21d(close, volume).diff().diff()


def f22_obvd_212_lee_ready_directional_volume_63d_d2(close, volume):
    return f22_obvd_212_lee_ready_directional_volume_63d(close, volume).diff().diff()


def f22_obvd_213_lee_ready_signed_dv_252d_d2(close, volume):
    return f22_obvd_213_lee_ready_signed_dv_252d(close, volume).diff().diff()


def f22_obvd_214_order_flow_imbalance_ratio_63d_d2(close, volume):
    return f22_obvd_214_order_flow_imbalance_ratio_63d(close, volume).diff().diff()


def f22_obvd_215_order_flow_imbalance_ratio_252d_d2(close, volume):
    return f22_obvd_215_order_flow_imbalance_ratio_252d(close, volume).diff().diff()


def f22_obvd_216_order_flow_imbalance_zscore_252d_d2(close, volume):
    return f22_obvd_216_order_flow_imbalance_zscore_252d(close, volume).diff().diff()


def f22_obvd_217_order_flow_dispersion_63d_d2(close, volume):
    return f22_obvd_217_order_flow_dispersion_63d(close, volume).diff().diff()


def f22_obvd_218_order_flow_signed_dollar_vol_252d_slope_d2(close, volume):
    return f22_obvd_218_order_flow_signed_dollar_vol_252d_slope(close, volume).diff().diff()


def f22_obvd_219_negative_order_flow_intensity_252d_d2(close, volume):
    return f22_obvd_219_negative_order_flow_intensity_252d(close, volume).diff().diff()


def f22_obvd_220_directional_flow_failure_to_confirm_high_252d_d2(high, close, volume):
    return f22_obvd_220_directional_flow_failure_to_confirm_high_252d(high, close, volume).diff().diff()


def f22_obvd_221_obv_diff_per_pct_change_21d_mean_d2(close, volume):
    return f22_obvd_221_obv_diff_per_pct_change_21d_mean(close, volume).diff().diff()


def f22_obvd_222_obv_diff_per_pct_change_252d_zscore_d2(close, volume):
    return f22_obvd_222_obv_diff_per_pct_change_252d_zscore(close, volume).diff().diff()


def f22_obvd_223_obv_effort_low_result_count_63d_d2(close, volume):
    return f22_obvd_223_obv_effort_low_result_count_63d(close, volume).diff().diff()


def f22_obvd_224_obv_result_to_effort_corr_252d_d2(close, volume):
    return f22_obvd_224_obv_result_to_effort_corr_252d(close, volume).diff().diff()


def f22_obvd_225_obv_effort_overshoot_zscore_252d_d2(close, volume):
    return f22_obvd_225_obv_effort_overshoot_zscore_252d(close, volume).diff().diff()


# ============================================================
#                         REGISTRY 151-225
# ============================================================


ON_BALANCE_VOLUME_DYNAMICS_D2_REGISTRY_151_225 = {
    "f22_obvd_151_cvd_proxy_zscore_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_151_cvd_proxy_zscore_252d_d2},
    "f22_obvd_152_cvd_proxy_slope_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_152_cvd_proxy_slope_63d_d2},
    "f22_obvd_153_cvd_proxy_slope_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_153_cvd_proxy_slope_252d_d2},
    "f22_obvd_154_cvd_proxy_minus_obv_252d_norm_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_154_cvd_proxy_minus_obv_252d_norm_d2},
    "f22_obvd_155_cvd_proxy_drawdown_from_max_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_155_cvd_proxy_drawdown_from_max_252d_d2},
    "f22_obvd_156_cvd_proxy_age_of_max_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_156_cvd_proxy_age_of_max_252d_d2},
    "f22_obvd_157_cvd_proxy_minus_price_slope_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_157_cvd_proxy_minus_price_slope_252d_d2},
    "f22_obvd_158_cvd_proxy_corr_close_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_158_cvd_proxy_corr_close_252d_d2},
    "f22_obvd_159_cvd_proxy_below_zero_dwell_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_159_cvd_proxy_below_zero_dwell_252d_d2},
    "f22_obvd_160_cvd_proxy_diff_zscore_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_160_cvd_proxy_diff_zscore_252d_d2},
    "f22_obvd_161_obv_rsi_14d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_161_obv_rsi_14d_d2},
    "f22_obvd_162_obv_rsi_21d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_162_obv_rsi_21d_d2},
    "f22_obvd_163_obv_stoch_k_14d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_163_obv_stoch_k_14d_d2},
    "f22_obvd_164_obv_stoch_k_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_164_obv_stoch_k_63d_d2},
    "f22_obvd_165_obv_stoch_d_14d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_165_obv_stoch_d_14d_d2},
    "f22_obvd_166_obv_macd_line_12_26_d2": {"inputs": ["close", "volume"], "func": f22_obvd_166_obv_macd_line_12_26_d2},
    "f22_obvd_167_obv_macd_signal_12_26_9_d2": {"inputs": ["close", "volume"], "func": f22_obvd_167_obv_macd_signal_12_26_9_d2},
    "f22_obvd_168_obv_macd_histogram_d2": {"inputs": ["close", "volume"], "func": f22_obvd_168_obv_macd_histogram_d2},
    "f22_obvd_169_obv_macd_hist_zerocross_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_169_obv_macd_hist_zerocross_count_252d_d2},
    "f22_obvd_170_obv_williams_r_14d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_170_obv_williams_r_14d_d2},
    "f22_obvd_171_obv_bb_upper_20d_2sigma_distance_d2": {"inputs": ["close", "volume"], "func": f22_obvd_171_obv_bb_upper_20d_2sigma_distance_d2},
    "f22_obvd_172_obv_bb_lower_20d_2sigma_distance_d2": {"inputs": ["close", "volume"], "func": f22_obvd_172_obv_bb_lower_20d_2sigma_distance_d2},
    "f22_obvd_173_obv_bb_percent_b_20d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_173_obv_bb_percent_b_20d_d2},
    "f22_obvd_174_obv_bb_bandwidth_20d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_174_obv_bb_bandwidth_20d_d2},
    "f22_obvd_175_obv_above_upper_bb_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_175_obv_above_upper_bb_count_252d_d2},
    "f22_obvd_176_obv_below_lower_bb_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_176_obv_below_lower_bb_count_252d_d2},
    "f22_obvd_177_obv_walking_upper_bb_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_177_obv_walking_upper_bb_indicator_d2},
    "f22_obvd_178_obv_bb_squeeze_indicator_20d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_178_obv_bb_squeeze_indicator_20d_d2},
    "f22_obvd_179_obv_bb_break_to_walk_failure_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_179_obv_bb_break_to_walk_failure_252d_d2},
    "f22_obvd_180_obv_bb_percent_b_pct_rank_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_180_obv_bb_percent_b_pct_rank_252d_d2},
    "f22_obvd_181_wyckoff_phase_a_obv_score_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_181_wyckoff_phase_a_obv_score_252d_d2},
    "f22_obvd_182_wyckoff_phase_b_obv_score_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_182_wyckoff_phase_b_obv_score_252d_d2},
    "f22_obvd_183_wyckoff_phase_c_obv_score_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_183_wyckoff_phase_c_obv_score_252d_d2},
    "f22_obvd_184_wyckoff_phase_d_obv_score_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_184_wyckoff_phase_d_obv_score_252d_d2},
    "f22_obvd_185_wyckoff_phase_e_obv_score_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_185_wyckoff_phase_e_obv_score_252d_d2},
    "f22_obvd_186_wyckoff_composite_phase_score_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_186_wyckoff_composite_phase_score_252d_d2},
    "f22_obvd_187_obv_trading_range_indicator_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_187_obv_trading_range_indicator_252d_d2},
    "f22_obvd_188_obv_trading_range_dwell_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_188_obv_trading_range_dwell_252d_d2},
    "f22_obvd_189_obv_breakout_failure_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_189_obv_breakout_failure_count_252d_d2},
    "f22_obvd_190_obv_lpsy_proxy_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_190_obv_lpsy_proxy_252d_d2},
    "f22_obvd_191_obv_distribution_day_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_191_obv_distribution_day_indicator_d2},
    "f22_obvd_192_obv_distribution_day_count_25d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_192_obv_distribution_day_count_25d_d2},
    "f22_obvd_193_obv_distribution_day_count_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_193_obv_distribution_day_count_63d_d2},
    "f22_obvd_194_obv_dd_severity_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_194_obv_dd_severity_252d_d2},
    "f22_obvd_195_consec_obv_dd_streak_d2": {"inputs": ["close", "volume"], "func": f22_obvd_195_consec_obv_dd_streak_d2},
    "f22_obvd_196_obv_dd_cluster_5d_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_196_obv_dd_cluster_5d_indicator_d2},
    "f22_obvd_197_obv_dd_after_252d_high_count_63d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_197_obv_dd_after_252d_high_count_63d_d2},
    "f22_obvd_198_obv_dd_to_obv_ad_ratio_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_198_obv_dd_to_obv_ad_ratio_63d_d2},
    "f22_obvd_199_obv_strict_dd_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_199_obv_strict_dd_indicator_d2},
    "f22_obvd_200_obv_strict_dd_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_200_obv_strict_dd_count_252d_d2},
    "f22_obvd_201_lee_mykland_jump_stat_obvdiff_21d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_201_lee_mykland_jump_stat_obvdiff_21d_d2},
    "f22_obvd_202_lee_mykland_jump_count_above_4_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_202_lee_mykland_jump_count_above_4_252d_d2},
    "f22_obvd_203_signed_obv_jump_sum_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_203_signed_obv_jump_sum_252d_d2},
    "f22_obvd_204_positive_obv_jump_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_204_positive_obv_jump_count_252d_d2},
    "f22_obvd_205_negative_obv_jump_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_205_negative_obv_jump_count_252d_d2},
    "f22_obvd_206_obv_jump_intensity_cum_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_206_obv_jump_intensity_cum_252d_d2},
    "f22_obvd_207_obv_jump_negative_to_positive_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_207_obv_jump_negative_to_positive_ratio_252d_d2},
    "f22_obvd_208_obv_jump_clustering_iat_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_208_obv_jump_clustering_iat_252d_d2},
    "f22_obvd_209_obv_jump_z_at_price_high_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_209_obv_jump_z_at_price_high_252d_d2},
    "f22_obvd_210_bnstest_obv_jump_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_210_bnstest_obv_jump_ratio_252d_d2},
    "f22_obvd_211_lee_ready_directional_volume_21d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_211_lee_ready_directional_volume_21d_d2},
    "f22_obvd_212_lee_ready_directional_volume_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_212_lee_ready_directional_volume_63d_d2},
    "f22_obvd_213_lee_ready_signed_dv_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_213_lee_ready_signed_dv_252d_d2},
    "f22_obvd_214_order_flow_imbalance_ratio_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_214_order_flow_imbalance_ratio_63d_d2},
    "f22_obvd_215_order_flow_imbalance_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_215_order_flow_imbalance_ratio_252d_d2},
    "f22_obvd_216_order_flow_imbalance_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_216_order_flow_imbalance_zscore_252d_d2},
    "f22_obvd_217_order_flow_dispersion_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_217_order_flow_dispersion_63d_d2},
    "f22_obvd_218_order_flow_signed_dollar_vol_252d_slope_d2": {"inputs": ["close", "volume"], "func": f22_obvd_218_order_flow_signed_dollar_vol_252d_slope_d2},
    "f22_obvd_219_negative_order_flow_intensity_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_219_negative_order_flow_intensity_252d_d2},
    "f22_obvd_220_directional_flow_failure_to_confirm_high_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_220_directional_flow_failure_to_confirm_high_252d_d2},
    "f22_obvd_221_obv_diff_per_pct_change_21d_mean_d2": {"inputs": ["close", "volume"], "func": f22_obvd_221_obv_diff_per_pct_change_21d_mean_d2},
    "f22_obvd_222_obv_diff_per_pct_change_252d_zscore_d2": {"inputs": ["close", "volume"], "func": f22_obvd_222_obv_diff_per_pct_change_252d_zscore_d2},
    "f22_obvd_223_obv_effort_low_result_count_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_223_obv_effort_low_result_count_63d_d2},
    "f22_obvd_224_obv_result_to_effort_corr_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_224_obv_result_to_effort_corr_252d_d2},
    "f22_obvd_225_obv_effort_overshoot_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_225_obv_effort_overshoot_zscore_252d_d2},
}
