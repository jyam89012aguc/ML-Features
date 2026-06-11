"""volume_dryup_at_high base features 151-225 — Pipeline 1b-technical (extension).

Gapless extension building on 001-150. New buckets cover concepts identified
via deep literature review that were absent from the original 150:
- VSA "No Demand" / "No Supply" / "Upthrust" signals (Tom Williams)
- Stalling / churn at the high (price flat on high vol)
- Effort-vs-result divergence (volume vs price-spread)
- Distribution-day (O'Neil) construction
- LPSY (Last Point of Supply) weak-rally detection
- Volume profile POC approximation on daily OHLCV
- Hawkes self-exciting volume cluster decay
- Bid-ask spread proxies from H-L (Corwin-Schultz style) at the high

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


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _ema_volume_intensity(volume: pd.Series, span: int) -> pd.Series:
    """Hawkes-style decaying intensity: EMA of squared shocks (vol - rolling mean)."""
    base = volume.rolling(span * 4, min_periods=span).mean()
    shock = (volume - base).clip(lower=0.0)
    return shock.ewm(span=span, min_periods=max(span // 3, 2), adjust=False).mean()


def _corwin_schultz_spread_proxy(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz (2012) bid-ask spread proxy from daily H/L. Returns daily spread estimate."""
    lh = _safe_log(high) - _safe_log(low)
    beta = (lh ** 2) + (lh.shift(1) ** 2)
    # Use the right-anchored 2-bar variant: beta = lh(t-1)^2 + lh(t)^2  (PIT-clean)
    beta_pit = (lh.shift(1) ** 2) + (lh ** 2)
    pair_high = pd.concat([high.shift(1), high], axis=1).max(axis=1)
    pair_low = pd.concat([low.shift(1), low], axis=1).min(axis=1)
    gamma = (_safe_log(pair_high) - _safe_log(pair_low)) ** 2
    denom_a = 3.0 - 2.0 * np.sqrt(2.0)
    alpha_num = np.sqrt(2.0 * beta_pit) - np.sqrt(beta_pit)
    alpha = (alpha_num / denom_a) - np.sqrt(gamma / denom_a)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


# ============================================================
# Bucket V — VSA No-Demand / No-Supply signals (151-160)
# ============================================================

def f20_vdah_151_vsa_no_demand_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VSA 'No Demand' bar: narrow up-bar (TR < 0.5*ATR21), close near high, volume < both prior 2 bars' volume."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    return (up & narrow & near_high & vol_low).astype(float)


def f20_vdah_152_vsa_no_demand_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of VSA No-Demand bars — frequency of weak-buying signals."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    flag = (up & narrow & near_high & vol_low).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_153_vsa_no_demand_streak(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of VSA No-Demand bars."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    cond = up & narrow & near_high & vol_low
    return _consecutive_true_streak(cond).astype(float)


def f20_vdah_154_vsa_no_supply_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VSA 'No Supply' bar: narrow down-bar (TR < 0.5*ATR21), close near low, volume < both prior 2 bars."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    dn = close < close.shift(1)
    narrow = tr < 0.5 * atr
    near_low = pos <= 0.4
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    return (dn & narrow & near_low & vol_low).astype(float)


def f20_vdah_155_vsa_test_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VSA 'Test' bar: dip below prior bar's low intraday but close back into prior range, on volume below 252d median."""
    prior_low = low.shift(1); prior_high = high.shift(1)
    dipped = low < prior_low
    closed_back = (close >= prior_low) & (close <= prior_high)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_low = volume < med
    return (dipped & closed_back & vol_low).astype(float)


def f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d count of No-Demand / 63d count of No-Supply. High = distribution-leaning."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    dn = close < close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    near_low = pos <= 0.4
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    nd = (up & narrow & near_high & vol_low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ns = (dn & narrow & near_low & vol_low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nd, ns + 1.0)


def f20_vdah_157_vsa_no_demand_gated_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """No-Demand indicator gated to bars where close is in top decile of trailing 252d range."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    range_pos = _safe_div(close - rmin, rmax - rmin)
    cond = up & narrow & near_high & vol_low & (range_pos >= 0.90)
    return cond.astype(float)


def f20_vdah_158_vsa_no_demand_at_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of No-Demand bars occurring when close is in top decile of 252d range."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    range_pos = _safe_div(close - rmin, rmax - rmin)
    flag = (up & narrow & near_high & vol_low & (range_pos >= 0.90)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d sum of No-Demand indicator weighted by (range_pos)^2 — emphasizes No-Demand exactly at the high."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    flag = (up & narrow & near_high & vol_low).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin).fillna(0.0)
    return (flag * (rp ** 2)).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_160_vsa_pseudo_supply_test_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of 'Test' bars (intraday dip with close back into range, low vol)."""
    prior_low = low.shift(1); prior_high = high.shift(1)
    dipped = low < prior_low
    closed_back = (close >= prior_low) & (close <= prior_high)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_low = volume < med
    flag = (dipped & closed_back & vol_low).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket W — VSA Upthrust / failed-up-bar at high (161-170)
# ============================================================

def f20_vdah_161_vsa_upthrust_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VSA Upthrust: new 21d high intraday but close in bottom half of bar, on volume above 252d median."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high & closed_weak & vol_high).astype(float)


def f20_vdah_162_vsa_upthrust_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Upthrust gated to bars where high exceeds trailing 252d max."""
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    new_high_252 = high > rmax252
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high_252 & closed_weak & vol_high).astype(float)


def f20_vdah_163_vsa_upthrust_after_distribution_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """UTAD score: Upthrust bar that occurs AFTER a 63d period in which close was largely in top decile of 252d range."""
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    rmin252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    new_high = high > rmax252
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    range_pos = _safe_div(close - rmin252, rmax252 - rmin252)
    in_dist = (range_pos >= 0.90).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    ut = (new_high & closed_weak & vol_high).astype(float)
    return ut * in_dist.fillna(0.0)


def f20_vdah_164_count_upthrusts_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of Upthrust bars."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high & closed_weak & vol_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_165_upthrust_max_volume_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max log-vol z(252d) observed on any Upthrust bar in trailing 252d — peak distribution intensity."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    cond = new_high & closed_weak & vol_high
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return z.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_166_bars_since_last_upthrust_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last Upthrust event (capped at 252)."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    flag = (new_high & closed_weak & vol_high).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_167_upthrust_with_followthrough_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when prior 5d had an Upthrust AND current close is below the Upthrust-bar low."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = new_high & closed_weak & vol_high
    ut_low = low.where(ut, np.nan).ffill()
    days_since = (~ut).astype(int).groupby(ut.cumsum()).cumsum()
    return ((days_since <= 5) & (close < ut_low.shift(1))).astype(float)


def f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 252d of (volume / ATR21) on Upthrust bars only — supply absorption intensity."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    cond = new_high & closed_weak & vol_high
    atr = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(volume, atr)
    return ratio.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_169_upthrust_followed_by_lower_high_within_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of Upthrusts followed within 5 days by a lower 5d high."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = new_high & closed_weak & vol_high
    ut_high = high.where(ut, np.nan).ffill()
    days_since = (~ut).astype(int).groupby(ut.cumsum()).cumsum()
    # follow-through failure: at any bar within 5d of ut, current high < ut_high
    fail_event = ((days_since <= 5) & (high < ut_high.shift(1))).astype(float)
    return fail_event.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_170_double_upthrust_indicator_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when current bar is an Upthrust AND another Upthrust occurred within the trailing 5 bars."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = (new_high & closed_weak & vol_high).astype(float)
    prior_ut = ut.shift(1).rolling(WDAYS, min_periods=1).sum()
    return ((ut > 0) & (prior_ut > 0)).astype(float)


# ============================================================
# Bucket X — Stalling / churn at the high (171-180)
# ============================================================

def f20_vdah_171_stalling_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stalling bar: close ≈ prior close (|pct_change|<0.5%) on volume > 1.5x 21d-median volume."""
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_high = volume > 1.5 * med21
    flat = pc < 0.005
    return (flat & vol_high).astype(float)


def f20_vdah_172_stalling_bar_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of stalling bars — churn frequency."""
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    flag = ((pc < 0.005) & (volume > 1.5 * med21)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_173_stalling_bar_at_252d_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of stalling bars when high is at trailing 252d max."""
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((pc < 0.005) & (volume > 1.5 * med21) & (high >= rmax)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_174_churn_effort_to_result_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d sum of volume divided by 21d sum of |close.diff()| — effort per unit result; high = churn."""
    eff = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    res = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_175_churn_effort_to_result_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d sum of volume divided by 63d sum of |close.diff()| — quarterly churn."""
    eff = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    res = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_176_churn_effort_to_range_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d sum of volume divided by 21d sum of (high - low) — churn via range absorption."""
    eff = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    res = (high - low).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_177_top_decile_dwell_with_churn_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where close in top decile of 252d AND volume above 2x 21d median AND |close pct_change|<0.5%."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    flag = ((rp >= 0.90) & (volume > 2.0 * med21) & (pc < 0.005)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_178_churn_intensity_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (volume / |close.diff()|) — extreme churn signal."""
    return _rolling_zscore(_safe_div(volume, close.diff().abs()), YDAYS)


def f20_vdah_179_max_churn_streak_at_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak with (close in top decile of 252d AND churn_indicator) in trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    cond = (rp >= 0.90) & (volume > 1.5 * med21) & (pc < 0.01)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_180_churn_to_breakout_failure_ratio_252d(high: pd.Series, volume: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d ratio of (churn-stall-at-high count) to (new-252d-high count). High = top-fight churn."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    churn = ((rp >= 0.90) & (volume > 1.5 * med21) & (pc < 0.01)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    new_h = (high >= rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(churn, new_h + 1.0)


# ============================================================
# Bucket Y — Effort vs Result divergence (181-190)
# ============================================================

def f20_vdah_181_effort_minus_result_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(21d) of log_volume minus z-score(21d) of |close.diff()| — effort outpacing result."""
    eff_z = _rolling_zscore(_safe_log(volume), MDAYS)
    res_z = _rolling_zscore(close.diff().abs(), MDAYS)
    return eff_z - res_z


def f20_vdah_182_effort_minus_result_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(63d) of log_vol minus z-score(63d) of |close.diff()|."""
    eff_z = _rolling_zscore(_safe_log(volume), QDAYS)
    res_z = _rolling_zscore(close.diff().abs(), QDAYS)
    return eff_z - res_z


def f20_vdah_183_effort_minus_result_at_252d_high_only(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Effort-minus-result z(21d) masked to bars where high equals 252d max."""
    eff_z = _rolling_zscore(_safe_log(volume), MDAYS)
    res_z = _rolling_zscore(close.diff().abs(), MDAYS)
    diff = eff_z - res_z
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return diff.where(high >= rmax, np.nan)


def f20_vdah_184_effort_result_corr_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d Pearson correlation between log_vol and |close.diff()|. Low = effort-result decoupled."""
    return _safe_log(volume).rolling(YDAYS, min_periods=QDAYS).corr(close.diff().abs())


def f20_vdah_185_volume_per_unit_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (volume / (high - low)) — supply absorption intensity per unit range."""
    return _rolling_zscore(_safe_div(volume, high - low), YDAYS)


def f20_vdah_186_count_high_effort_low_result_bars_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with log-vol z(252d) > 1 AND |close pct_change| < 0.5%."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    pc = close.pct_change().abs()
    return ((z > 1.0) & (pc < 0.005)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_187_high_effort_low_result_max_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak of (log-vol z>1 AND |pct_change|<0.5%) in trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    pc = close.pct_change().abs()
    cond = (z > 1.0) & (pc < 0.005)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_188_effort_result_ratio_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank(252d) of (volume / |close.diff()| ratio) — high rank = unusual effort vs result."""
    return _rolling_pct_rank(_safe_div(volume, close.diff().abs()), YDAYS)


def f20_vdah_189_volume_excess_when_range_compressed_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (volume z(252d)) on bars where range is in bottom quintile of 252d range distribution."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rng = high - low
    q20 = _rolling_quantile(rng, YDAYS, 0.20)
    flag = rng <= q20
    return z.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_190_effort_result_decoupling_index_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 minus rolling 252d corr(log_vol, |close.diff()|), clipped [0,2]. High = decoupled (suspect)."""
    c = _safe_log(volume).rolling(YDAYS, min_periods=QDAYS).corr(close.diff().abs())
    return (1.0 - c).clip(lower=-1.0, upper=2.0)


# ============================================================
# Bucket Z — LPSY (Last Point of Supply) — weak rally detection (191-200)
# ============================================================

def f20_vdah_191_weak_rally_after_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when: trailing 21d had a >5% drop from 21d-high (breakdown) AND current 5d rally has vol below 21d median."""
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float)


def f20_vdah_192_lpsy_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of LPSY (weak-rally-after-breakdown) indicators."""
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_193_post_drawdown_rally_volume_decay_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on up-bars in trailing 21d divided by mean volume on down-bars — < 1 means down-vol-heavy."""
    up = close > close.shift(1)
    dn = close < close.shift(1)
    up_v = volume.where(up, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    dn_v = volume.where(dn, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(up_v, dn_v)


def f20_vdah_194_post_peak_rally_low_vol_strength_index(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over trailing 63d of (close.diff() / 21d-volume-median) on up bars after a 252d high — rally strength per supply."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    past_peak = rmax.shift(QDAYS) >= rmax  # within last 63d, an earlier 252d high existed
    up = close > close.shift(1)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    contrib = _safe_div(close.diff(), med21)
    return contrib.where(up & past_peak, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_195_lpsy_failure_to_retake_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 21d rally close is below trailing-63d high AND the rally happened on below-21d-median volume."""
    h63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    rally_5d = close > close.shift(WDAYS)
    fail = close < h63
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (rally_5d & fail & vol_low).astype(float)


def f20_vdah_196_count_lpsy_failure_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of LPSY-failure-to-retake-high events."""
    h63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    rally_5d = close > close.shift(WDAYS)
    fail = close < h63
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (rally_5d & fail & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_197_rally_volume_zscore_post_252d_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log-vol z(252d) on up-close bars in the trailing 63d, after the 252d high was at least 63d ago."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = high >= rmax
    bars_since_peak = (~is_peak).astype(int).groupby(is_peak.cumsum()).cumsum()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    up = close > close.shift(1)
    flag = up & (bars_since_peak > QDAYS)
    return z.where(flag, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f20_vdah_198_lpsy_lower_high_pattern_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where a 21d local-max high is lower than the prior 21d local-max high."""
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return (h21 < h21.shift(MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_199_post_distribution_rally_failure_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: (LPSY count 252d) + (Upthrust count 252d) + (No-Demand count 252d) — distribution-phase intensity."""
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    lpsy = (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = (new_high & closed_weak & vol_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos2 = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos2 >= 0.6
    nd_vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    nd = (up & narrow & near_high & nd_vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return lpsy + ut + nd


def f20_vdah_200_lpsy_dwell_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in 'weak rally after a recent 63d-drop' state."""
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket AA — Distribution day (O'Neil-style) (201-210)
# ============================================================

def f20_vdah_201_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """O'Neil-style distribution day: close down >0.2% AND volume > prior bar's volume."""
    pc = close.pct_change()
    return ((pc < -0.002) & (volume > volume.shift(1))).astype(float)


def f20_vdah_202_distribution_day_count_25d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """O'Neil-style trailing 25-bar distribution day count."""
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(25, min_periods=10).sum()


def f20_vdah_203_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d distribution day count."""
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_204_strict_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict variant: close down >1% AND volume > 1.5x 21d median."""
    pc = close.pct_change()
    med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.01) & (volume > 1.5 * med)).astype(float)


def f20_vdah_205_strict_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d strict-distribution-day count."""
    pc = close.pct_change()
    med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.01) & (volume > 1.5 * med)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_206_distribution_to_accumulation_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d distribution day count) / (63d accumulation day count: close up>0.2%, vol > prior)."""
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ad = ((pc > 0.002) & (volume > volume.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dd, ad + 1.0)


def f20_vdah_207_consec_distribution_days_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of distribution days."""
    pc = close.pct_change()
    cond = (pc < -0.002) & (volume > volume.shift(1))
    return _consecutive_true_streak(cond).astype(float)


def f20_vdah_208_distribution_day_severity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of |close pct_change| × (volume / 21d-median-volume) on distribution days only."""
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    severity = pc.abs() * _safe_div(volume, med21)
    flag = (pc < -0.002) & (volume > volume.shift(1))
    return severity.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_209_distribution_day_clustered_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when there have been >=4 distribution days in the trailing 25 bars (O'Neil warning threshold)."""
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    cnt = flag.rolling(25, min_periods=10).sum()
    return (cnt >= 4).astype(float)


def f20_vdah_210_distribution_day_after_252d_high_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of distribution days where the trailing 21d already contained a 252d-high event."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).astype(float).rolling(MDAYS, min_periods=WDAYS).max() > 0
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1)) & recent_peak
    return dd.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket AB — Volume profile POC approximation on daily OHLCV (211-220)
# ============================================================

def f20_vdah_211_poc_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Approximate volume-profile POC: trailing 252d price-bin midpoint with highest cumulative dollar-volume."""
    def _poc(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        cv = c[mask].values; vv = v[mask].values
        lo, hi = cv.min(), cv.max()
        if hi <= lo:
            return float(cv.mean())
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        return float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _poc(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_212_log_dist_close_to_poc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(close) - log(POC_252d). Positive = above value area; sustained > 0 with low vol = exhaustion."""
    def _poc(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        cv = c[mask].values; vv = v[mask].values
        lo, hi = cv.min(), cv.max()
        if hi <= lo:
            return float(cv.mean())
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        return float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
    poc = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        poc.iloc[i] = _poc(range(i - YDAYS + 1, i + 1))
    return _safe_log(close) - _safe_log(poc)


def f20_vdah_213_value_area_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Value area high (VAH): smallest price s.t. 85% of cum vol falls below it, in trailing 252d."""
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.85 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_214_value_area_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Value area low (VAL): smallest price s.t. 15% of cum vol falls below it, in trailing 252d."""
    def _val(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.15 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _val(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_215_log_dist_close_to_vah_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(close) - log(value-area-high 252d). Positive sustained = single-print exhaustion zone."""
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.85 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return _safe_log(close) - _safe_log(vah)


def f20_vdah_216_log_value_area_width_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(VAH) - log(VAL) in trailing 252d — value area width."""
    def _vp(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return (np.nan, np.nan)
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return (np.nan, np.nan)
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        val_i = min(int(np.searchsorted(cum, 0.15 * tot)), cv.size - 1)
        return (float(cv[vah_i]), float(cv[val_i]))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vh, vl = _vp(range(i - YDAYS + 1, i + 1))
        if vl is not None and vh is not None and vl > 0 and vh > 0:
            out.iloc[i] = float(np.log(vh) - np.log(vl))
    return out


def f20_vdah_217_single_print_dwell_above_vah_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars where close > VAH(252d)."""
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        return float(cv[vah_i])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return (close > vah).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_218_poc_age_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the POC-bar (the single bar in trailing 252d with the highest volume that anchors POC)."""
    def _age(idx):
        v = volume.iloc[idx]
        if v.notna().sum() < 30:
            return np.nan
        vv = v.values
        return float(len(vv) - 1 - int(np.argmax(vv)))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _age(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_219_volume_above_vah_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on bars with close > VAH(252d) divided by total trailing 252d volume."""
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        return float(cv[vah_i])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    above = volume.where(close > vah, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(above, tot)


def f20_vdah_220_value_area_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(VAH - POC) - (POC - VAL): positive = skewed up (single-print exhaustion zone above POC)."""
    def _vp(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return (np.nan, np.nan, np.nan)
        cv_arr = c[mask].values; vv_arr = v[mask].values
        lo, hi = cv_arr.min(), cv_arr.max()
        if hi <= lo:
            return (lo, lo, lo)
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv_arr, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv_arr, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        poc_px = float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
        order = np.argsort(cv_arr)
        cv_sorted = cv_arr[order]; vv_sorted = vv_arr[order]
        cum = np.cumsum(vv_sorted)
        tot = cum[-1]
        if tot <= 0:
            return (poc_px, poc_px, poc_px)
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv_sorted.size - 1)
        val_i = min(int(np.searchsorted(cum, 0.15 * tot)), cv_sorted.size - 1)
        return (poc_px, float(cv_sorted[vah_i]), float(cv_sorted[val_i]))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        poc, vh, vl = _vp(range(i - YDAYS + 1, i + 1))
        if not (np.isnan(poc) or np.isnan(vh) or np.isnan(vl)):
            out.iloc[i] = float((vh - poc) - (poc - vl))
    return out


# ============================================================
# Bucket AC — Hawkes self-exciting volume cluster decay (221-225)
# ============================================================

def f20_vdah_221_hawkes_volume_intensity_21d(volume: pd.Series) -> pd.Series:
    """Hawkes-style intensity: EMA(span=21) of positive volume shocks (vol - 84d-mean)+."""
    return _ema_volume_intensity(volume, span=MDAYS)


def f20_vdah_222_hawkes_volume_intensity_63d(volume: pd.Series) -> pd.Series:
    """Hawkes-style intensity: EMA(span=63) of positive volume shocks (vol - 252d-mean)+."""
    return _ema_volume_intensity(volume, span=QDAYS)


def f20_vdah_223_hawkes_volume_decay_ratio_21_to_63(volume: pd.Series) -> pd.Series:
    """Hawkes intensity ratio: span-21 / span-63 — short cluster intensity vs longer."""
    return _safe_div(_ema_volume_intensity(volume, span=MDAYS), _ema_volume_intensity(volume, span=QDAYS))


def f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90(volume: pd.Series) -> pd.Series:
    """Bars since Hawkes intensity(21) last crossed above its trailing 252d 90%-quantile."""
    inten = _ema_volume_intensity(volume, span=MDAYS)
    q = _rolling_quantile(inten, YDAYS, 0.90)
    flag = (inten > q).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_225_hawkes_volume_intensity_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of Hawkes-style 21d intensity."""
    return _rolling_zscore(_ema_volume_intensity(volume, span=MDAYS), YDAYS)


# ============================================================
#                         REGISTRY 151-225
# ============================================================

VOLUME_DRYUP_AT_HIGH_BASE_REGISTRY_151_225 = {
    "f20_vdah_151_vsa_no_demand_bar_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_151_vsa_no_demand_bar_indicator},
    "f20_vdah_152_vsa_no_demand_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_152_vsa_no_demand_count_63d},
    "f20_vdah_153_vsa_no_demand_streak": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_153_vsa_no_demand_streak},
    "f20_vdah_154_vsa_no_supply_bar_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_154_vsa_no_supply_bar_indicator},
    "f20_vdah_155_vsa_test_bar_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_155_vsa_test_bar_indicator},
    "f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d},
    "f20_vdah_157_vsa_no_demand_gated_at_high": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_157_vsa_no_demand_gated_at_high},
    "f20_vdah_158_vsa_no_demand_at_high_count_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_158_vsa_no_demand_at_high_count_252d},
    "f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high},
    "f20_vdah_160_vsa_pseudo_supply_test_count_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_160_vsa_pseudo_supply_test_count_252d},
    "f20_vdah_161_vsa_upthrust_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_161_vsa_upthrust_indicator},
    "f20_vdah_162_vsa_upthrust_at_252d_high_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_162_vsa_upthrust_at_252d_high_indicator},
    "f20_vdah_163_vsa_upthrust_after_distribution_score": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_163_vsa_upthrust_after_distribution_score},
    "f20_vdah_164_count_upthrusts_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_164_count_upthrusts_252d},
    "f20_vdah_165_upthrust_max_volume_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_165_upthrust_max_volume_zscore_252d},
    "f20_vdah_166_bars_since_last_upthrust_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_166_bars_since_last_upthrust_252d},
    "f20_vdah_167_upthrust_with_followthrough_failure_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_167_upthrust_with_followthrough_failure_indicator},
    "f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean},
    "f20_vdah_169_upthrust_followed_by_lower_high_within_5d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_169_upthrust_followed_by_lower_high_within_5d},
    "f20_vdah_170_double_upthrust_indicator_5d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_170_double_upthrust_indicator_5d},
    "f20_vdah_171_stalling_bar_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_171_stalling_bar_indicator},
    "f20_vdah_172_stalling_bar_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_172_stalling_bar_count_63d},
    "f20_vdah_173_stalling_bar_at_252d_high_count_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_173_stalling_bar_at_252d_high_count_252d},
    "f20_vdah_174_churn_effort_to_result_ratio_21d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_174_churn_effort_to_result_ratio_21d},
    "f20_vdah_175_churn_effort_to_result_ratio_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_175_churn_effort_to_result_ratio_63d},
    "f20_vdah_176_churn_effort_to_range_ratio_21d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_176_churn_effort_to_range_ratio_21d},
    "f20_vdah_177_top_decile_dwell_with_churn_indicator_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_177_top_decile_dwell_with_churn_indicator_252d},
    "f20_vdah_178_churn_intensity_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_178_churn_intensity_zscore_252d},
    "f20_vdah_179_max_churn_streak_at_high_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_179_max_churn_streak_at_high_252d},
    "f20_vdah_180_churn_to_breakout_failure_ratio_252d": {"inputs": ["high", "volume", "low", "close"], "func": f20_vdah_180_churn_to_breakout_failure_ratio_252d},
    "f20_vdah_181_effort_minus_result_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_181_effort_minus_result_zscore_21d},
    "f20_vdah_182_effort_minus_result_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_182_effort_minus_result_zscore_63d},
    "f20_vdah_183_effort_minus_result_at_252d_high_only": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_183_effort_minus_result_at_252d_high_only},
    "f20_vdah_184_effort_result_corr_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_184_effort_result_corr_252d},
    "f20_vdah_185_volume_per_unit_range_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_185_volume_per_unit_range_zscore_252d},
    "f20_vdah_186_count_high_effort_low_result_bars_63d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_186_count_high_effort_low_result_bars_63d},
    "f20_vdah_187_high_effort_low_result_max_streak_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_187_high_effort_low_result_max_streak_252d},
    "f20_vdah_188_effort_result_ratio_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_188_effort_result_ratio_pct_rank_252d},
    "f20_vdah_189_volume_excess_when_range_compressed_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_189_volume_excess_when_range_compressed_252d},
    "f20_vdah_190_effort_result_decoupling_index_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_190_effort_result_decoupling_index_252d},
    "f20_vdah_191_weak_rally_after_breakdown_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_191_weak_rally_after_breakdown_indicator},
    "f20_vdah_192_lpsy_count_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_192_lpsy_count_252d},
    "f20_vdah_193_post_drawdown_rally_volume_decay_21d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_193_post_drawdown_rally_volume_decay_21d},
    "f20_vdah_194_post_peak_rally_low_vol_strength_index": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_194_post_peak_rally_low_vol_strength_index},
    "f20_vdah_195_lpsy_failure_to_retake_high_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_195_lpsy_failure_to_retake_high_indicator},
    "f20_vdah_196_count_lpsy_failure_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_196_count_lpsy_failure_252d},
    "f20_vdah_197_rally_volume_zscore_post_252d_high": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_197_rally_volume_zscore_post_252d_high},
    "f20_vdah_198_lpsy_lower_high_pattern_count_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_198_lpsy_lower_high_pattern_count_252d},
    "f20_vdah_199_post_distribution_rally_failure_score": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_199_post_distribution_rally_failure_score},
    "f20_vdah_200_lpsy_dwell_score_252d": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_200_lpsy_dwell_score_252d},
    "f20_vdah_201_distribution_day_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_201_distribution_day_indicator},
    "f20_vdah_202_distribution_day_count_25d": {"inputs": ["close", "volume"], "func": f20_vdah_202_distribution_day_count_25d},
    "f20_vdah_203_distribution_day_count_63d": {"inputs": ["close", "volume"], "func": f20_vdah_203_distribution_day_count_63d},
    "f20_vdah_204_strict_distribution_day_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_204_strict_distribution_day_indicator},
    "f20_vdah_205_strict_distribution_day_count_63d": {"inputs": ["close", "volume"], "func": f20_vdah_205_strict_distribution_day_count_63d},
    "f20_vdah_206_distribution_to_accumulation_ratio_63d": {"inputs": ["close", "volume"], "func": f20_vdah_206_distribution_to_accumulation_ratio_63d},
    "f20_vdah_207_consec_distribution_days_streak": {"inputs": ["close", "volume"], "func": f20_vdah_207_consec_distribution_days_streak},
    "f20_vdah_208_distribution_day_severity_252d": {"inputs": ["close", "volume"], "func": f20_vdah_208_distribution_day_severity_252d},
    "f20_vdah_209_distribution_day_clustered_5d_indicator": {"inputs": ["close", "volume"], "func": f20_vdah_209_distribution_day_clustered_5d_indicator},
    "f20_vdah_210_distribution_day_after_252d_high_count_63d": {"inputs": ["high", "close", "volume"], "func": f20_vdah_210_distribution_day_after_252d_high_count_63d},
    "f20_vdah_211_poc_price_252d": {"inputs": ["close", "volume"], "func": f20_vdah_211_poc_price_252d},
    "f20_vdah_212_log_dist_close_to_poc_252d": {"inputs": ["close", "volume"], "func": f20_vdah_212_log_dist_close_to_poc_252d},
    "f20_vdah_213_value_area_high_252d": {"inputs": ["close", "volume"], "func": f20_vdah_213_value_area_high_252d},
    "f20_vdah_214_value_area_low_252d": {"inputs": ["close", "volume"], "func": f20_vdah_214_value_area_low_252d},
    "f20_vdah_215_log_dist_close_to_vah_252d": {"inputs": ["close", "volume"], "func": f20_vdah_215_log_dist_close_to_vah_252d},
    "f20_vdah_216_log_value_area_width_252d": {"inputs": ["close", "volume"], "func": f20_vdah_216_log_value_area_width_252d},
    "f20_vdah_217_single_print_dwell_above_vah_252d": {"inputs": ["close", "volume"], "func": f20_vdah_217_single_print_dwell_above_vah_252d},
    "f20_vdah_218_poc_age_in_252d": {"inputs": ["close", "volume"], "func": f20_vdah_218_poc_age_in_252d},
    "f20_vdah_219_volume_above_vah_share_252d": {"inputs": ["close", "volume"], "func": f20_vdah_219_volume_above_vah_share_252d},
    "f20_vdah_220_value_area_skew_252d": {"inputs": ["close", "volume"], "func": f20_vdah_220_value_area_skew_252d},
    "f20_vdah_221_hawkes_volume_intensity_21d": {"inputs": ["volume"], "func": f20_vdah_221_hawkes_volume_intensity_21d},
    "f20_vdah_222_hawkes_volume_intensity_63d": {"inputs": ["volume"], "func": f20_vdah_222_hawkes_volume_intensity_63d},
    "f20_vdah_223_hawkes_volume_decay_ratio_21_to_63": {"inputs": ["volume"], "func": f20_vdah_223_hawkes_volume_decay_ratio_21_to_63},
    "f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90": {"inputs": ["volume"], "func": f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90},
    "f20_vdah_225_hawkes_volume_intensity_zscore_252d": {"inputs": ["volume"], "func": f20_vdah_225_hawkes_volume_intensity_zscore_252d},
}
