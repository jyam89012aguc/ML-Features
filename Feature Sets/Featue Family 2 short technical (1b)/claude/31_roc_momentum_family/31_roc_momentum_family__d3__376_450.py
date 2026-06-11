"""roc_momentum_family base features 376-450 — Pipeline 1b-technical (batch 3).

Third pass continuation. Buckets in this file:
U continued (open/close intraday: skew + canonical exhaustion-gap composites), 376-380;
V (volume-confirmed momentum atomic), 381-400;
W (recent-return shape & moments not yet covered), 401-415;
X (tight-base / volatility-contraction events), 416-425;
Y (climax / late-stage canonical composites), 426-435;
Z (long-window forensic / time-to-event), 436-450.

Inputs: SEP OHLCV. PIT-clean. Atomic-leaning. ~15% canonical composites only
(VDU, pocket-pivot, distribution-day, two/three-weeks-tight, climax-run,
exhaustion-gap, Stage-3/4) — practitioner-named patterns.
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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _bars_since_event(flag: pd.Series, window: int, min_periods: int) -> pd.Series:

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        idxs = np.where(w == 1)[0]
        if len(idxs) == 0:
            return float(len(w))
        return float(len(w) - 1 - idxs[-1])
    return flag.astype(float).rolling(window, min_periods=min_periods).apply(_bs, raw=True)

def f31_rcmf_376_skew_intraday_returns_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of intraday (open-to-close) returns over trailing 63d."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(QDAYS, min_periods=MDAYS).skew().diff().diff().diff()

def f31_rcmf_377_skew_gap_returns_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of overnight gap returns over trailing 63d."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(QDAYS, min_periods=MDAYS).skew().diff().diff().diff()

def f31_rcmf_378_exhaustion_gap_up_at_252d_high_indicator_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical composite (O'Neil exhaustion gap): gap-up at the 99th-percentile of trailing
    252d gap distribution AND today's close at trailing 252d-close-max. Practitioner-named
    blowoff-fingerprint event."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    q99 = g.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (g >= q99) & (close >= rmax)
    valid = g.notna() & q99.notna() & rmax.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_379_breakaway_gap_down_from_252d_high_indicator_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-down ≤ −3% within 5 bars of having been at the trailing 252d-close-high
    — classic distribution-phase breakaway-gap-down event after a top."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high_recent = (close >= rmax).rolling(WDAYS, min_periods=2).max()
    cond = (g <= -0.03) & (at_high_recent.shift(1) > 0)
    return cond.astype(float).where(g.notna(), np.nan).diff().diff().diff()

def f31_rcmf_380_bars_since_5pct_gap_up_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the most recent gap-up ≥ +5% in trailing 252d."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    flag = (g >= 0.05) & g.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_381_volume_weighted_return_5d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 5d return: sum(r_i * v_i) / sum(v_i) over trailing 5d.
    Atomic VWAP-style return statistic."""
    r = close.pct_change(1)
    rw = (r * volume).rolling(WDAYS, min_periods=2).sum()
    vs = volume.rolling(WDAYS, min_periods=2).sum()
    return _safe_div(rw, vs).diff().diff().diff()

def f31_rcmf_382_volume_weighted_return_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21d return."""
    r = close.pct_change(1)
    rw = (r * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    vs = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(rw, vs).diff().diff().diff()

def f31_rcmf_383_volume_weighted_return_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 63d return — quarterly volume-weighted drift."""
    r = close.pct_change(1)
    rw = (r * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    vs = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(rw, vs).diff().diff().diff()

def f31_rcmf_384_up_down_volume_ratio_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(vol on up days) / sum(vol on down days) over trailing 21d."""
    r = close.pct_change(1)
    upv = volume.where(r > 0, 0.0)
    dnv = volume.where(r < 0, 0.0)
    return _safe_div(upv.rolling(MDAYS, min_periods=WDAYS).sum(), dnv.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()

def f31_rcmf_385_up_down_volume_ratio_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up/down volume ratio over trailing 63d."""
    r = close.pct_change(1)
    upv = volume.where(r > 0, 0.0)
    dnv = volume.where(r < 0, 0.0)
    return _safe_div(upv.rolling(QDAYS, min_periods=MDAYS).sum(), dnv.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f31_rcmf_386_up_down_volume_ratio_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up/down volume ratio over trailing 252d — annual buying-pressure quality."""
    r = close.pct_change(1)
    upv = volume.where(r > 0, 0.0)
    dnv = volume.where(r < 0, 0.0)
    return _safe_div(upv.rolling(YDAYS, min_periods=QDAYS).sum(), dnv.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f31_rcmf_387_volume_zscore_on_best_21d_day_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on the bar where trailing-252d best-21d-return ended.
    Atomic confirmation-volume statistic for the year's biggest rally bar."""
    r21 = close.pct_change(MDAYS)
    n = YDAYS
    vz = _rolling_zscore(volume, YDAYS)

    def _v(w, vzw):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        if np.isnan(vzw[idx]):
            return np.nan
        return float(vzw[idx])
    r21v = r21.values
    vzv = vz.values
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        sl = slice(i - n + 1, i + 1)
        w = r21v[sl]
        if np.sum(~np.isnan(w)) < QDAYS:
            continue
        wv = np.where(~np.isnan(w), w, -np.inf)
        idx = int(np.argmax(wv))
        v = vzv[sl][idx]
        if not np.isnan(v):
            out[i] = v
    return pd.Series(out, index=close.index).diff().diff().diff()

def f31_rcmf_388_volume_zscore_on_worst_21d_day_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on the bar where trailing-252d worst-21d-return ended."""
    r21 = close.pct_change(MDAYS)
    n = YDAYS
    vz = _rolling_zscore(volume, YDAYS)
    r21v = r21.values
    vzv = vz.values
    out = np.full(len(close), np.nan)
    for i in range(n - 1, len(close)):
        sl = slice(i - n + 1, i + 1)
        w = r21v[sl]
        if np.sum(~np.isnan(w)) < QDAYS:
            continue
        wv = np.where(~np.isnan(w), w, np.inf)
        idx = int(np.argmin(wv))
        v = vzv[sl][idx]
        if not np.isnan(v):
            out[i] = v
    return pd.Series(out, index=close.index).diff().diff().diff()

def f31_rcmf_389_pocket_pivot_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Canonical composite (Kacher/Morales pocket pivot): today's volume > max volume of any
    down day in trailing 10 bars, AND today's 1d return > 0. Atomic event of institutional
    accumulation footprint."""
    r = close.pct_change(1)
    down_vol = volume.where(r < 0, np.nan)
    max_down_vol_10 = down_vol.rolling(10, min_periods=1).max()
    cond = (r > 0) & (volume > max_down_vol_10)
    valid = r.notna() & volume.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_390_pocket_pivot_count_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of pocket-pivot events in trailing 21d — concentration of institutional-buying
    fingerprints."""
    r = close.pct_change(1)
    down_vol = volume.where(r < 0, np.nan)
    max_down_vol_10 = down_vol.rolling(10, min_periods=1).max()
    flag = ((r > 0) & (volume > max_down_vol_10)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_391_distribution_day_count_25d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Canonical composite (O'Neil distribution day count): count of bars in last 25d where
    1d return < 0 AND volume > 1.2 × 21d-mean. ≥4-6 in a few weeks signals institutional
    distribution (per O'Neil's IBD rules)."""
    r = close.pct_change(1)
    vol_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((r < 0) & (volume > 1.2 * vol_mean)).astype(float)
    return flag.rolling(25, min_periods=10).sum().diff().diff().diff()

def f31_rcmf_392_vdu_indicator_d3(volume: pd.Series) -> pd.Series:
    """Canonical composite (Minervini VDU — volume dry-up): today's volume < 0.5 × 50d-mean
    volume. Late-stage pre-breakout fingerprint."""
    vol_mean = volume.rolling(50, min_periods=10).mean()
    cond = volume < 0.5 * vol_mean
    valid = volume.notna() & vol_mean.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_393_vdu_count_21d_d3(volume: pd.Series) -> pd.Series:
    """Count of VDU days in trailing 21d."""
    vol_mean = volume.rolling(50, min_periods=10).mean()
    flag = (volume < 0.5 * vol_mean).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_394_vol_on_5pct_up_minus_5pct_down_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on +5% days minus mean volume on −5% days in last 21d — directional-extreme
    volume asymmetry."""
    r = close.pct_change(1)
    up_v = volume.where(r >= 0.05, np.nan)
    dn_v = volume.where(r <= -0.05, np.nan)
    return (up_v.rolling(MDAYS, min_periods=2).mean() - dn_v.rolling(MDAYS, min_periods=2).mean()).diff().diff().diff()

def f31_rcmf_395_mean_vol_up_minus_down_ratio_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(vol on up days) / mean(vol on down days) in trailing 63d."""
    r = close.pct_change(1)
    up_v = volume.where(r > 0, np.nan)
    dn_v = volume.where(r < 0, np.nan)
    return _safe_div(up_v.rolling(QDAYS, min_periods=MDAYS).mean(), dn_v.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f31_rcmf_396_largest_1d_volume_zscore_21d_d3(volume: pd.Series) -> pd.Series:
    """Max 1d-volume z-score (z computed vs 252d) observed in trailing 21d — biggest volume
    spike of the month."""
    vz = _rolling_zscore(volume, YDAYS)
    return vz.rolling(MDAYS, min_periods=WDAYS).max().diff().diff().diff()

def f31_rcmf_397_signed_volume_sum_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of sign(ret_1d) × volume over trailing 21d — net directional volume."""
    r = close.pct_change(1)
    sv = np.sign(r) * volume
    return sv.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_398_signed_volume_sum_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of sign(ret_1d) × volume over trailing 63d."""
    r = close.pct_change(1)
    sv = np.sign(r) * volume
    return sv.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f31_rcmf_399_volume_zscore_on_252d_close_high_event_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score on the most recent bar that printed a 252d close-high.
    Atomic 'how much volume confirmed the breakout' statistic."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (close >= rmax) & rmax.notna()
    vz = _rolling_zscore(volume, YDAYS)
    masked = vz.where(at_high)
    return masked.ffill(limit=YDAYS).diff().diff().diff()

def f31_rcmf_400_cumulative_signed_volume_slope_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope (per bar) of cumulative-signed-volume over trailing 63d.
    OBV-style trend, but atomic (one statistic) and unrelated to family-22 OBV concept variants
    because here we use a cumulative-signed-volume series freshly rebased within each 63d window
    via differencing in the slope calc."""
    r = close.pct_change(1)
    sv = np.sign(r) * volume
    cum = sv.cumsum()
    return _rolling_slope(cum, QDAYS).diff().diff().diff()

def f31_rcmf_401_kurt_1d_returns_63d_d3(close: pd.Series) -> pd.Series:
    """Kurtosis (excess) of 1d returns in trailing 63d — atomic distribution-shape moment."""
    r = close.pct_change(1)
    return r.rolling(QDAYS, min_periods=MDAYS).kurt().diff().diff().diff()

def f31_rcmf_402_kurt_1d_returns_252d_d3(close: pd.Series) -> pd.Series:
    """Kurtosis (excess) of 1d returns in trailing 252d."""
    r = close.pct_change(1)
    return r.rolling(YDAYS, min_periods=QDAYS).kurt().diff().diff().diff()

def f31_rcmf_403_skew_5d_returns_252d_d3(close: pd.Series) -> pd.Series:
    """Skew of overlapping 5d returns over trailing 252d — weekly-horizon distribution skew."""
    r5 = close.pct_change(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f31_rcmf_404_pos_neg_std_ratio_63d_d3(close: pd.Series) -> pd.Series:
    """Std(positive 1d returns) / std(negative 1d returns) over trailing 63d
    — distinct from existing upside/downside capture (mean-based)."""
    r = close.pct_change(1)
    rp = r.where(r > 0)
    rn = r.where(r < 0)
    return _safe_div(rp.rolling(QDAYS, min_periods=MDAYS).std(), rn.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff().diff()

def f31_rcmf_405_pos_neg_std_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Std(positive 1d returns) / std(negative 1d returns) over trailing 252d."""
    r = close.pct_change(1)
    rp = r.where(r > 0)
    rn = r.where(r < 0)
    return _safe_div(rp.rolling(YDAYS, min_periods=QDAYS).std(), rn.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f31_rcmf_406_range_max_min_1d_in_21d_d3(close: pd.Series) -> pd.Series:
    """max(1d return) − min(1d return) in trailing 21d — monthly span of single-day moves.
    Distinct from existing 079 (63d window)."""
    r = close.pct_change(1)
    return (r.rolling(MDAYS, min_periods=WDAYS).max() - r.rolling(MDAYS, min_periods=WDAYS).min()).diff().diff().diff()

def f31_rcmf_407_std_5d_returns_252d_d3(close: pd.Series) -> pd.Series:
    """Std of overlapping 5d returns in trailing 252d — weekly-horizon vol."""
    r5 = close.pct_change(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).std().diff().diff().diff()

def f31_rcmf_408_std_21d_returns_504d_d3(close: pd.Series) -> pd.Series:
    """Std of overlapping 21d returns in trailing 504d — monthly-horizon vol."""
    r21 = close.pct_change(MDAYS)
    return r21.rolling(DDAYS_2Y, min_periods=YDAYS).std().diff().diff().diff()

def f31_rcmf_409_coef_var_abs_1d_63d_d3(close: pd.Series) -> pd.Series:
    """Coefficient of variation of |1d return| over trailing 63d — std(|r|) / mean(|r|).
    Atomic absolute-amplitude-dispersion measure."""
    r = close.pct_change(1).abs()
    return _safe_div(r.rolling(QDAYS, min_periods=MDAYS).std(), r.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()

def f31_rcmf_410_vol_regime_ratio_21_to_252_d3(close: pd.Series) -> pd.Series:
    """std(1d, 21d) / std(1d, 252d) — recent-vs-trailing-year vol-regime ratio."""
    r = close.pct_change(1)
    return _safe_div(r.rolling(MDAYS, min_periods=WDAYS).std(), r.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()

def f31_rcmf_411_range_21d_returns_in_252d_d3(close: pd.Series) -> pd.Series:
    """max(21d return, in 252d) − min(21d return, in 252d) — trailing-year monthly-return range."""
    r21 = close.pct_change(MDAYS)
    return (r21.rolling(YDAYS, min_periods=QDAYS).max() - r21.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f31_rcmf_412_range_63d_returns_in_504d_d3(close: pd.Series) -> pd.Series:
    """max(63d return, in 504d) − min(63d return, in 504d) — biennial quarterly-return range."""
    r63 = close.pct_change(QDAYS)
    return (r63.rolling(DDAYS_2Y, min_periods=YDAYS).max() - r63.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff().diff().diff()

def f31_rcmf_413_range_compression_21_over_252_d3(close: pd.Series) -> pd.Series:
    """(High−Low close range over 21d) / (High−Low close range over 252d) — monthly compression
    of close-range relative to year. Lower = compression. Range based on close (not OHLC) to
    keep distinct from family-37/40 OHLC-range estimators."""
    rng21 = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    rng252 = close.rolling(YDAYS, min_periods=QDAYS).max() - close.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(rng21, rng252).diff().diff().diff()

def f31_rcmf_414_vol_contraction_event_indicator_d3(close: pd.Series) -> pd.Series:
    """Canonical composite (Minervini volatility-contraction event): std(1d, 10d)
    < 0.5 × std(1d, 252d). Atomic event flag for volatility contraction."""
    r = close.pct_change(1)
    s10 = r.rolling(10, min_periods=5).std()
    s252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    cond = s10 < 0.5 * s252
    return cond.astype(float).where(s10.notna() & s252.notna(), np.nan).diff().diff().diff()

def f31_rcmf_415_downside_std_63d_d3(close: pd.Series) -> pd.Series:
    """Std of negative 1d returns only over trailing 63d — downside-only realized vol.
    Distinct from existing semi-variance (which is mean-squared); this is std."""
    r = close.pct_change(1)
    rn = r.where(r < 0)
    return rn.rolling(QDAYS, min_periods=MDAYS).std().diff().diff().diff()

def f31_rcmf_416_two_weeks_tight_indicator_d3(close: pd.Series) -> pd.Series:
    """Canonical (Minervini): (max(close,10d) − min(close,10d)) / close_today < 5%.
    Two-week tight base."""
    rmax = close.rolling(10, min_periods=5).max()
    rmin = close.rolling(10, min_periods=5).min()
    rng_pct = _safe_div(rmax - rmin, close)
    cond = rng_pct < 0.05
    return cond.astype(float).where(rng_pct.notna(), np.nan).diff().diff().diff()

def f31_rcmf_417_three_weeks_tight_indicator_d3(close: pd.Series) -> pd.Series:
    """Canonical (Minervini): 15d range / close_today < 7%. Three-weeks-tight base."""
    rmax = close.rolling(15, min_periods=7).max()
    rmin = close.rolling(15, min_periods=7).min()
    rng_pct = _safe_div(rmax - rmin, close)
    cond = rng_pct < 0.07
    return cond.astype(float).where(rng_pct.notna(), np.nan).diff().diff().diff()

def f31_rcmf_418_four_weeks_tight_indicator_d3(close: pd.Series) -> pd.Series:
    """Four-weeks-tight: 20d range / close_today < 10%."""
    rmax = close.rolling(20, min_periods=10).max()
    rmin = close.rolling(20, min_periods=10).min()
    rng_pct = _safe_div(rmax - rmin, close)
    cond = rng_pct < 0.1
    return cond.astype(float).where(rng_pct.notna(), np.nan).diff().diff().diff()

def f31_rcmf_419_range_compression_10_over_252_d3(close: pd.Series) -> pd.Series:
    """10d close-range / 252d close-range — biweekly compression ratio. Lower = tighter."""
    rng10 = close.rolling(10, min_periods=5).max() - close.rolling(10, min_periods=5).min()
    rng252 = close.rolling(YDAYS, min_periods=QDAYS).max() - close.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(rng10, rng252).diff().diff().diff()

def f31_rcmf_420_range_compression_5_over_252_d3(close: pd.Series) -> pd.Series:
    """5d close-range / 252d close-range — weekly compression ratio."""
    rng5 = close.rolling(WDAYS, min_periods=2).max() - close.rolling(WDAYS, min_periods=2).min()
    rng252 = close.rolling(YDAYS, min_periods=QDAYS).max() - close.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(rng5, rng252).diff().diff().diff()

def f31_rcmf_421_weekly_contraction_count_63d_d3(close: pd.Series) -> pd.Series:
    """Count of weeks (non-overlapping 5d blocks across last 63d, sampled every 5 bars) where
    that week's 5d range is < prior 5d range — number of contractions."""
    rng5 = close.rolling(WDAYS, min_periods=2).max() - close.rolling(WDAYS, min_periods=2).min()
    cond = rng5 < rng5.shift(WDAYS)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f31_rcmf_422_progressive_contraction_indicator_d3(close: pd.Series) -> pd.Series:
    """Canonical (Minervini VCP): each of the last 4 weekly ranges (5d) smaller than the prior
    one — strict monotonic contraction over 4 weeks. Atomic event flag."""
    rng5 = close.rolling(WDAYS, min_periods=2).max() - close.rolling(WDAYS, min_periods=2).min()
    r0 = rng5
    r1 = rng5.shift(WDAYS)
    r2 = rng5.shift(2 * WDAYS)
    r3 = rng5.shift(3 * WDAYS)
    cond = (r0 < r1) & (r1 < r2) & (r2 < r3)
    valid = r0.notna() & r1.notna() & r2.notna() & r3.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_423_tennis_ball_day_count_21d_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical (Minervini 'tennis ball'): count of days in 21d where 1d return > 0 AND
    close-in-range = (close − low) / (high − low) > 0.7 (close near top of bar)."""
    r = close.pct_change(1)
    rng = high - low
    pos = _safe_div(close - low, rng)
    flag = ((r > 0) & (pos > 0.7)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_424_pivot_churning_indicator_d3(close: pd.Series) -> pd.Series:
    """Churning canonical composite: 5d range / close > 5% but |5d return| < 1% — high
    volatility with no net price change (institutional absorption/distribution)."""
    rmax = close.rolling(WDAYS, min_periods=2).max()
    rmin = close.rolling(WDAYS, min_periods=2).min()
    rng = _safe_div(rmax - rmin, close)
    r5 = close.pct_change(WDAYS).abs()
    cond = (rng > 0.05) & (r5 < 0.01)
    return cond.astype(float).where(rng.notna() & r5.notna(), np.nan).diff().diff().diff()

def f31_rcmf_425_bars_since_three_weeks_tight_event_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since most recent three-weeks-tight indicator firing in last 252d."""
    rmax = close.rolling(15, min_periods=7).max()
    rmin = close.rolling(15, min_periods=7).min()
    rng_pct = _safe_div(rmax - rmin, close)
    flag = (rng_pct < 0.07) & rng_pct.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_426_climax_run_21d_at_252d_high_d3(close: pd.Series) -> pd.Series:
    """Canonical (O'Neil climax run): ret_21d > 0.25 AND close at trailing 252d-close-max.
    Atomic event indicator."""
    r21 = close.pct_change(MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    cond = (r21 > 0.25) & (close >= rmax)
    valid = r21.notna() & rmax.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_427_climax_run_15d_severe_d3(close: pd.Series) -> pd.Series:
    """Canonical (O'Neil severe climax): ret_15d > 0.30 — 1-2 week 25-50% acceleration."""
    r15 = close.pct_change(15)
    cond = r15 > 0.3
    return cond.astype(float).where(r15.notna(), np.nan).diff().diff().diff()

def f31_rcmf_428_blowoff_pace_10d_share_of_annual_d3(close: pd.Series) -> pd.Series:
    """Blowoff-pace atomic: ret_10d / ret_252d, conditional on ret_252d > +50%. Fraction of
    annual gain accruing in last 10 bars during already-strong regime. Distinct from existing
    300 (which uses 21d/252d)."""
    r10 = close.pct_change(10)
    r252 = close.pct_change(YDAYS)
    ratio = _safe_div(r10, r252)
    return ratio.where(r252 > 0.5, np.nan).diff().diff().diff()

def f31_rcmf_429_exhaustion_gap_classic_indicator_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical (O'Neil exhaustion gap): gap-up ≥ 95th-percentile of trailing 252d gaps AND
    today is a new 252d close-high AND close in lower half of bar (filled-bar exhaustion).
    Composite alternative variant to 378."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    q95 = g.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rng = high - low
    pos = _safe_div(close - low, rng)
    cond = (g >= q95) & (close >= rmax) & (pos < 0.5)
    valid = g.notna() & q95.notna() & rmax.notna() & pos.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_430_low_volume_at_new_252d_high_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Canonical (late-stage low-volume new-high): close at trailing 252d-max AND volume <
    0.8 × 21d-mean-volume. Smart-money-absent breakout indicator."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    vol_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (close >= rmax) & (volume < 0.8 * vol_mean)
    valid = rmax.notna() & vol_mean.notna() & volume.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_431_top_tail_volatility_spike_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Canonical (top-tail volatility spike): true-range on day of 252d-close-high > 2 × ATR21.
    Atomic single-day-extreme-range fingerprint at a top."""
    tr = _true_range(high, low, close)
    atr21 = _atr(high, low, close, n=MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = close >= rmax
    cond = at_high & (tr > 2.0 * atr21)
    valid = tr.notna() & atr21.notna() & rmax.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_432_vertical_move_15d_indicator_d3(close: pd.Series) -> pd.Series:
    """Atomic vertical-move event: ret_15d > +50% (extreme 3-week run)."""
    r15 = close.pct_change(15)
    cond = r15 > 0.5
    return cond.astype(float).where(r15.notna(), np.nan).diff().diff().diff()

def f31_rcmf_433_five_consecutive_up_at_252d_high_d3(close: pd.Series) -> pd.Series:
    """Composite: 5 consecutive 1d positive returns AND today is at 252d close-high
    — parabolic-finish fingerprint."""
    r = close.pct_change(1)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    five_up = (r > 0) & (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0) & (r.shift(4) > 0)
    cond = five_up & (close >= rmax)
    return cond.astype(float).where(r.notna() & rmax.notna(), np.nan).diff().diff().diff()

def f31_rcmf_434_stage3_distribution_proxy_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Canonical (Weinstein Stage 3 proxy): close within 5% of trailing 252d-max AND |ret_21d|
    < 5% AND volume > 1.2 × 21d-mean. Plateauing-at-high with elevated volume."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_high = _safe_div(close, rmax) > 0.95
    r21 = close.pct_change(MDAYS).abs()
    vol_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    hot_vol = volume > 1.2 * vol_mean
    cond = near_high & (r21 < 0.05) & hot_vol
    valid = rmax.notna() & r21.notna() & vol_mean.notna() & volume.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_435_stage4_trigger_indicator_d3(close: pd.Series) -> pd.Series:
    """Canonical (Weinstein Stage 4 trigger): close < 150d-SMA AND 150d-SMA slope (50d) < 0.
    Per Weinstein, 30-week (≈150d) MA roll-over with price below confirms markdown.
    Uses 150d to avoid duplicating family-13/14 specific MAs."""
    sma = close.rolling(150, min_periods=50).mean()
    slope = sma.diff(50)
    cond = (close < sma) & (slope < 0)
    valid = sma.notna() & slope.notna()
    return cond.astype(float).where(valid, np.nan).diff().diff().diff()

def f31_rcmf_436_bars_since_252d_high_argmax_d3(close: pd.Series) -> pd.Series:
    """Bars-since-argmax(close, 252d) — distance from today to the position of trailing-year peak.
    Distinct from 334 which counts bars-since-event (>= rmax); this is positional argmax."""
    n = YDAYS

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        return float(len(w) - 1 - int(np.argmax(wv)))
    return close.rolling(n, min_periods=QDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_437_bars_since_1260d_high_argmax_d3(close: pd.Series) -> pd.Series:
    """Bars-since-argmax(close, 1260d) — distance from today to 5y peak position."""
    n = DDAYS_5Y

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        return float(len(w) - 1 - int(np.argmax(wv)))
    return close.rolling(n, min_periods=YDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_438_bars_252d_high_to_first_5pct_dd_d3(close: pd.Series) -> pd.Series:
    """Within trailing 504d: bars between the most-recent 252d-close-high event and the first
    subsequent bar that closed ≥ 5% below it. NaN if no such drawdown bar yet."""
    n = DDAYS_2Y

    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        rmax_so_far = np.maximum.accumulate(np.where(valid, w, -np.inf))
        eq = np.where(valid, w, -np.inf) == rmax_so_far
        idxs = np.where(eq)[0]
        if len(idxs) == 0:
            return np.nan
        last_high_idx = idxs[-1]
        peak = w[last_high_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        post = w[last_high_idx + 1:]
        for j, v in enumerate(post):
            if np.isfinite(v) and v / peak - 1.0 <= -0.05:
                return float(j + 1)
        return np.nan
    return close.rolling(n, min_periods=YDAYS).apply(_f, raw=True).diff().diff().diff()

def f31_rcmf_439_bars_252d_high_to_first_10pct_dd_d3(close: pd.Series) -> pd.Series:
    """Bars between last 252d-close-high event and first subsequent ≥10% drawdown bar
    within trailing 504d."""
    n = DDAYS_2Y

    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        rmax_so_far = np.maximum.accumulate(np.where(valid, w, -np.inf))
        eq = np.where(valid, w, -np.inf) == rmax_so_far
        idxs = np.where(eq)[0]
        if len(idxs) == 0:
            return np.nan
        last_high_idx = idxs[-1]
        peak = w[last_high_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        post = w[last_high_idx + 1:]
        for j, v in enumerate(post):
            if np.isfinite(v) and v / peak - 1.0 <= -0.1:
                return float(j + 1)
        return np.nan
    return close.rolling(n, min_periods=YDAYS).apply(_f, raw=True).diff().diff().diff()

def f31_rcmf_440_count_new_252d_highs_in_252d_d3(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where close equalled the running 252d max of that
    inner window — frequency of new-yearly-high prints."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f31_rcmf_441_count_new_1260d_highs_in_1260d_d3(close: pd.Series) -> pd.Series:
    """Count of bars in trailing 1260d where close equalled the rolling-1260d max."""
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    flag = (close >= rmax).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f31_rcmf_442_count_failed_new_high_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of failed-new-high events in trailing 252d: close >= 252d running max AND
    close < open (intraday rejection) — outside-day rejection at a high."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((close >= rmax) & (close < open_)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f31_rcmf_443_count_new_21d_highs_in_63d_d3(close: pd.Series) -> pd.Series:
    """Count of new-21d-close-highs in trailing 63d — short-horizon-high frequency."""
    rmax = close.rolling(MDAYS, min_periods=WDAYS).max()
    flag = (close >= rmax).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f31_rcmf_444_count_new_63d_highs_in_252d_d3(close: pd.Series) -> pd.Series:
    """Count of new-63d-close-highs in trailing 252d — quarterly-high frequency."""
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    flag = (close >= rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f31_rcmf_445_recent_high_pace_21d_to_63d_d3(close: pd.Series) -> pd.Series:
    """(count new-21d-highs in last 21d) / (count new-21d-highs in prior 63d).
    Acceleration in new-high prints."""
    rmax = close.rolling(MDAYS, min_periods=WDAYS).max()
    flag = (close >= rmax).astype(float)
    recent = flag.rolling(MDAYS, min_periods=WDAYS).sum()
    prior = flag.shift(MDAYS).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(recent, prior).diff().diff().diff()

def f31_rcmf_446_fraction_bars_within_2pct_of_252d_high_63d_d3(close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 63d where close was within 2% of its trailing-252d max
    — quarterly time-near-highs."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near = (_safe_div(close, rmax) > 0.98).astype(float)
    valid = (rmax.notna() & close.notna()).astype(float)
    return _safe_div(near.rolling(QDAYS, min_periods=MDAYS).sum(), valid.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f31_rcmf_447_fraction_bars_within_5pct_of_252d_high_252d_d3(close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 252d where close was within 5% of its trailing-252d max."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near = (_safe_div(close, rmax) > 0.95).astype(float)
    valid = (rmax.notna() & close.notna()).astype(float)
    return _safe_div(near.rolling(YDAYS, min_periods=QDAYS).sum(), valid.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()

def f31_rcmf_448_longest_streak_within_5pct_of_252d_high_252d_d3(close: pd.Series) -> pd.Series:
    """Longest consecutive streak of bars within 5% of trailing-252d max, over trailing 252d
    — longest 'dwell-near-high' run (canonical distribution-base persistence)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near = (_safe_div(close, rmax) > 0.95).astype(float)
    n = YDAYS

    def _l(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        best = 0
        cur = 0
        for v in w:
            if v == 1:
                cur += 1
                if cur > best:
                    best = cur
            elif np.isfinite(v):
                cur = 0
        return float(best)
    return near.rolling(n, min_periods=QDAYS).apply(_l, raw=True).diff().diff().diff()

def f31_rcmf_449_dwell_21bars_within_2pct_of_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: in the last 21 bars, every bar was within 2% of its trailing-252d-close-max
    — extended consolidation at top (Stage-3 fingerprint)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    near = (_safe_div(close, rmax) > 0.98).astype(float)
    streak_ok = near.rolling(MDAYS, min_periods=MDAYS).min() == 1.0
    return streak_ok.astype(float).where(near.notna(), np.nan).diff().diff().diff()

def f31_rcmf_450_first_down_quarter_after_four_up_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today's ret_63d < 0 AND each of the prior 4 non-overlapping 63d returns
    (lagged 63, 126, 189, 252 bars) was > 0 — first down quarter after 4 up quarters."""
    r63 = close.pct_change(QDAYS)
    cond = (r63 < 0) & (r63.shift(QDAYS) > 0) & (r63.shift(2 * QDAYS) > 0) & (r63.shift(3 * QDAYS) > 0) & (r63.shift(4 * QDAYS) > 0)
    return cond.astype(float).where(r63.notna(), np.nan).diff().diff().diff()
ROC_MOMENTUM_FAMILY_D3_REGISTRY_376_450 = {'f31_rcmf_376_skew_intraday_returns_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_376_skew_intraday_returns_63d_d3}, 'f31_rcmf_377_skew_gap_returns_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_377_skew_gap_returns_63d_d3}, 'f31_rcmf_378_exhaustion_gap_up_at_252d_high_indicator_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_378_exhaustion_gap_up_at_252d_high_indicator_d3}, 'f31_rcmf_379_breakaway_gap_down_from_252d_high_indicator_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_379_breakaway_gap_down_from_252d_high_indicator_d3}, 'f31_rcmf_380_bars_since_5pct_gap_up_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_380_bars_since_5pct_gap_up_252d_d3}, 'f31_rcmf_381_volume_weighted_return_5d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_381_volume_weighted_return_5d_d3}, 'f31_rcmf_382_volume_weighted_return_21d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_382_volume_weighted_return_21d_d3}, 'f31_rcmf_383_volume_weighted_return_63d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_383_volume_weighted_return_63d_d3}, 'f31_rcmf_384_up_down_volume_ratio_21d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_384_up_down_volume_ratio_21d_d3}, 'f31_rcmf_385_up_down_volume_ratio_63d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_385_up_down_volume_ratio_63d_d3}, 'f31_rcmf_386_up_down_volume_ratio_252d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_386_up_down_volume_ratio_252d_d3}, 'f31_rcmf_387_volume_zscore_on_best_21d_day_252d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_387_volume_zscore_on_best_21d_day_252d_d3}, 'f31_rcmf_388_volume_zscore_on_worst_21d_day_252d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_388_volume_zscore_on_worst_21d_day_252d_d3}, 'f31_rcmf_389_pocket_pivot_indicator_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_389_pocket_pivot_indicator_d3}, 'f31_rcmf_390_pocket_pivot_count_21d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_390_pocket_pivot_count_21d_d3}, 'f31_rcmf_391_distribution_day_count_25d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_391_distribution_day_count_25d_d3}, 'f31_rcmf_392_vdu_indicator_d3': {'inputs': ['volume'], 'func': f31_rcmf_392_vdu_indicator_d3}, 'f31_rcmf_393_vdu_count_21d_d3': {'inputs': ['volume'], 'func': f31_rcmf_393_vdu_count_21d_d3}, 'f31_rcmf_394_vol_on_5pct_up_minus_5pct_down_21d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_394_vol_on_5pct_up_minus_5pct_down_21d_d3}, 'f31_rcmf_395_mean_vol_up_minus_down_ratio_63d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_395_mean_vol_up_minus_down_ratio_63d_d3}, 'f31_rcmf_396_largest_1d_volume_zscore_21d_d3': {'inputs': ['volume'], 'func': f31_rcmf_396_largest_1d_volume_zscore_21d_d3}, 'f31_rcmf_397_signed_volume_sum_21d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_397_signed_volume_sum_21d_d3}, 'f31_rcmf_398_signed_volume_sum_63d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_398_signed_volume_sum_63d_d3}, 'f31_rcmf_399_volume_zscore_on_252d_close_high_event_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_399_volume_zscore_on_252d_close_high_event_d3}, 'f31_rcmf_400_cumulative_signed_volume_slope_63d_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_400_cumulative_signed_volume_slope_63d_d3}, 'f31_rcmf_401_kurt_1d_returns_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_401_kurt_1d_returns_63d_d3}, 'f31_rcmf_402_kurt_1d_returns_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_402_kurt_1d_returns_252d_d3}, 'f31_rcmf_403_skew_5d_returns_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_403_skew_5d_returns_252d_d3}, 'f31_rcmf_404_pos_neg_std_ratio_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_404_pos_neg_std_ratio_63d_d3}, 'f31_rcmf_405_pos_neg_std_ratio_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_405_pos_neg_std_ratio_252d_d3}, 'f31_rcmf_406_range_max_min_1d_in_21d_d3': {'inputs': ['close'], 'func': f31_rcmf_406_range_max_min_1d_in_21d_d3}, 'f31_rcmf_407_std_5d_returns_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_407_std_5d_returns_252d_d3}, 'f31_rcmf_408_std_21d_returns_504d_d3': {'inputs': ['close'], 'func': f31_rcmf_408_std_21d_returns_504d_d3}, 'f31_rcmf_409_coef_var_abs_1d_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_409_coef_var_abs_1d_63d_d3}, 'f31_rcmf_410_vol_regime_ratio_21_to_252_d3': {'inputs': ['close'], 'func': f31_rcmf_410_vol_regime_ratio_21_to_252_d3}, 'f31_rcmf_411_range_21d_returns_in_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_411_range_21d_returns_in_252d_d3}, 'f31_rcmf_412_range_63d_returns_in_504d_d3': {'inputs': ['close'], 'func': f31_rcmf_412_range_63d_returns_in_504d_d3}, 'f31_rcmf_413_range_compression_21_over_252_d3': {'inputs': ['close'], 'func': f31_rcmf_413_range_compression_21_over_252_d3}, 'f31_rcmf_414_vol_contraction_event_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_414_vol_contraction_event_indicator_d3}, 'f31_rcmf_415_downside_std_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_415_downside_std_63d_d3}, 'f31_rcmf_416_two_weeks_tight_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_416_two_weeks_tight_indicator_d3}, 'f31_rcmf_417_three_weeks_tight_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_417_three_weeks_tight_indicator_d3}, 'f31_rcmf_418_four_weeks_tight_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_418_four_weeks_tight_indicator_d3}, 'f31_rcmf_419_range_compression_10_over_252_d3': {'inputs': ['close'], 'func': f31_rcmf_419_range_compression_10_over_252_d3}, 'f31_rcmf_420_range_compression_5_over_252_d3': {'inputs': ['close'], 'func': f31_rcmf_420_range_compression_5_over_252_d3}, 'f31_rcmf_421_weekly_contraction_count_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_421_weekly_contraction_count_63d_d3}, 'f31_rcmf_422_progressive_contraction_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_422_progressive_contraction_indicator_d3}, 'f31_rcmf_423_tennis_ball_day_count_21d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f31_rcmf_423_tennis_ball_day_count_21d_d3}, 'f31_rcmf_424_pivot_churning_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_424_pivot_churning_indicator_d3}, 'f31_rcmf_425_bars_since_three_weeks_tight_event_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_425_bars_since_three_weeks_tight_event_252d_d3}, 'f31_rcmf_426_climax_run_21d_at_252d_high_d3': {'inputs': ['close'], 'func': f31_rcmf_426_climax_run_21d_at_252d_high_d3}, 'f31_rcmf_427_climax_run_15d_severe_d3': {'inputs': ['close'], 'func': f31_rcmf_427_climax_run_15d_severe_d3}, 'f31_rcmf_428_blowoff_pace_10d_share_of_annual_d3': {'inputs': ['close'], 'func': f31_rcmf_428_blowoff_pace_10d_share_of_annual_d3}, 'f31_rcmf_429_exhaustion_gap_classic_indicator_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f31_rcmf_429_exhaustion_gap_classic_indicator_d3}, 'f31_rcmf_430_low_volume_at_new_252d_high_indicator_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_430_low_volume_at_new_252d_high_indicator_d3}, 'f31_rcmf_431_top_tail_volatility_spike_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f31_rcmf_431_top_tail_volatility_spike_indicator_d3}, 'f31_rcmf_432_vertical_move_15d_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_432_vertical_move_15d_indicator_d3}, 'f31_rcmf_433_five_consecutive_up_at_252d_high_d3': {'inputs': ['close'], 'func': f31_rcmf_433_five_consecutive_up_at_252d_high_d3}, 'f31_rcmf_434_stage3_distribution_proxy_indicator_d3': {'inputs': ['close', 'volume'], 'func': f31_rcmf_434_stage3_distribution_proxy_indicator_d3}, 'f31_rcmf_435_stage4_trigger_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_435_stage4_trigger_indicator_d3}, 'f31_rcmf_436_bars_since_252d_high_argmax_d3': {'inputs': ['close'], 'func': f31_rcmf_436_bars_since_252d_high_argmax_d3}, 'f31_rcmf_437_bars_since_1260d_high_argmax_d3': {'inputs': ['close'], 'func': f31_rcmf_437_bars_since_1260d_high_argmax_d3}, 'f31_rcmf_438_bars_252d_high_to_first_5pct_dd_d3': {'inputs': ['close'], 'func': f31_rcmf_438_bars_252d_high_to_first_5pct_dd_d3}, 'f31_rcmf_439_bars_252d_high_to_first_10pct_dd_d3': {'inputs': ['close'], 'func': f31_rcmf_439_bars_252d_high_to_first_10pct_dd_d3}, 'f31_rcmf_440_count_new_252d_highs_in_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_440_count_new_252d_highs_in_252d_d3}, 'f31_rcmf_441_count_new_1260d_highs_in_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_441_count_new_1260d_highs_in_1260d_d3}, 'f31_rcmf_442_count_failed_new_high_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_442_count_failed_new_high_252d_d3}, 'f31_rcmf_443_count_new_21d_highs_in_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_443_count_new_21d_highs_in_63d_d3}, 'f31_rcmf_444_count_new_63d_highs_in_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_444_count_new_63d_highs_in_252d_d3}, 'f31_rcmf_445_recent_high_pace_21d_to_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_445_recent_high_pace_21d_to_63d_d3}, 'f31_rcmf_446_fraction_bars_within_2pct_of_252d_high_63d_d3': {'inputs': ['close'], 'func': f31_rcmf_446_fraction_bars_within_2pct_of_252d_high_63d_d3}, 'f31_rcmf_447_fraction_bars_within_5pct_of_252d_high_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_447_fraction_bars_within_5pct_of_252d_high_252d_d3}, 'f31_rcmf_448_longest_streak_within_5pct_of_252d_high_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_448_longest_streak_within_5pct_of_252d_high_252d_d3}, 'f31_rcmf_449_dwell_21bars_within_2pct_of_252d_high_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_449_dwell_21bars_within_2pct_of_252d_high_indicator_d3}, 'f31_rcmf_450_first_down_quarter_after_four_up_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_450_first_down_quarter_after_four_up_indicator_d3}}