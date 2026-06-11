"""blowoff_climax_composite d1 features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket H: Volume-climax composites.
Bucket I: Momentum-climax composites.
Bucket J: Range / wide-bar climax composites.
Bucket K: Extension + climax composites.
Bucket L: Sentiment / breadth proxies.
Bucket M: Multi-condition counts / dwell.
Bucket N: Final composites & saturation indicators.

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
    return 100.0 - 100.0 / (1.0 + _safe_div(ps, ns))


def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _new_high_252(high):
    return (high >= high.rolling(YDAYS, min_periods=QDAYS).max())


def _signal_sum(high, low, close, volume):
    """Sum of {new 252d high, vol>2x252d avg, RSI>80, TR>2xATR21, CLV>0.5} as float, NaN-safe."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return ((high >= high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0)
            + (_safe_div(volume, volume.rolling(YDAYS, min_periods=QDAYS).mean()) > 2.0).astype(float).fillna(0)
            + (_rsi(close, 14) > 80.0).astype(float).fillna(0)
            + (_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)) > 2.0).astype(float).fillna(0)
            + (clv > 0.5).astype(float).fillna(0))


def _intensity_score(high, low, close, volume):
    """Weighted intensity = 2*(RSI/100) + 2*new_high + vol_z + range_z + CLV."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return (2.0 * _rsi(close, 14) / 100.0
            + 2.0 * (high >= high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
            + _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
            + _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
            + clv)


# ============================================================
# Bucket H — Volume-climax composites (076-088)
# ============================================================


def f49_bcco_076_vol_zscore_over_3_and_new_21d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if vol z-score (252d) > 3 AND new 21d high — extreme-vol monthly blowoff."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((vz > 3.0) & new_high).astype(float).where(vz.notna(), np.nan)).diff()


def f49_bcco_077_vol_zscore_over_3_and_new_252d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if vol z-score (252d) > 3 AND new 252d high — heavy buying at top."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return (((vz > 3.0) & _new_high_252(high)).astype(float).where(vz.notna(), np.nan)).diff()


def f49_bcco_078_3bar_vol_sum_3x_63d_avg_and_new_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3-bar vol sum > 3x (63d avg of 3-bar vol sum) AND new 21d high."""
    v3 = volume.rolling(3, min_periods=2).sum()
    base = v3.rolling(QDAYS, min_periods=MDAYS).mean()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((v3 > 3.0 * base) & new_high).astype(float).where(base.notna(), np.nan)).diff()


def f49_bcco_079_5bar_vol_sum_5x_63d_avg_and_new_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5-bar vol sum > 5x (63d avg of 5-bar vol sum) AND new 21d high."""
    v5 = volume.rolling(WDAYS, min_periods=2).sum()
    base = v5.rolling(QDAYS, min_periods=MDAYS).mean()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((v5 > 5.0 * base) & new_high).astype(float).where(base.notna(), np.nan)).diff()


def f49_bcco_080_top5_vol_days_within_21_of_now_and_at_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if today is within 21 bars of any of the top-5 highest-volume days in past 252 AND close at/near 21d high.

    Implementation: count high-vol-rank<=5 events in past 21; non-zero AND new 21d high."""
    rank = volume.rolling(YDAYS, min_periods=QDAYS).rank(ascending=False)
    top5_recent = (rank <= 5).astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return ((top5_recent & new_high).astype(float).where(rank.notna(), np.nan)).diff()


def f49_bcco_081_alltime_vol_high_and_new_252d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if volume at its cumulative max (all-time-high vol) AND new 252d price high."""
    return (((volume >= volume.cummax()) & _new_high_252(high)).astype(float)).diff()


def f49_bcco_082_dollar_vol_3x_median_and_new_high_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if dollar-volume > 3x its 63d median AND new 252d price high."""
    dv = close * volume
    med = dv.rolling(QDAYS, min_periods=MDAYS).median()
    return (((dv > 3.0 * med) & _new_high_252(high)).astype(float).where(med.notna(), np.nan)).diff()


def f49_bcco_083_dollar_vol_zscore_over_3_and_new_high_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if dollar-vol z-score (252d) > 3 AND new 252d price high."""
    dvz = _rolling_zscore(close * volume, YDAYS, min_periods=QDAYS)
    return (((dvz > 3.0) & _new_high_252(high)).astype(float).where(dvz.notna(), np.nan)).diff()


def f49_bcco_084_vol_at_63d_max_and_new_252d_high_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if vol at 63d max AND new 252d price high."""
    return (((volume >= volume.rolling(QDAYS, min_periods=MDAYS).max()) & _new_high_252(high)).astype(float).where(volume.rolling(QDAYS, min_periods=MDAYS).max().notna(), np.nan)).diff()


def f49_bcco_085_climax_then_fade_flag_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (vol > 3x 21d avg) AND new 21d high on prior bar AND vol < 21d median this bar — climax-then-fade pattern."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    new_high_prev = (high.shift(1) >= high.shift(1).rolling(MDAYS, min_periods=WDAYS).max())
    climax_prev = (volume.shift(1) > 3.0 * v_avg.shift(1))
    fade_now = (volume < v_med)
    return ((new_high_prev & climax_prev & fade_now).astype(float).where(v_avg.notna() & v_med.notna(), np.nan)).diff()


def f49_bcco_086_climax_then_fade_count_252_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of climax-then-fade events."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    new_high_prev = (high.shift(1) >= high.shift(1).rolling(MDAYS, min_periods=WDAYS).max())
    climax_prev = (volume.shift(1) > 3.0 * v_avg.shift(1))
    fade_now = (volume < v_med)
    ev = (new_high_prev & climax_prev & fade_now).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(v_avg.notna() & v_med.notna(), np.nan)).diff()


def f49_bcco_087_bars_since_last_climax_bar_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last bar with (vol > 3x 21d avg AND new 21d high) — climax-bar recency."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    cond = (volume > 3.0 * v_avg) & new_high
    return (_bars_since_true(cond)).diff()


def f49_bcco_088_climax_bar_count_252_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of climax bars (vol > 3x 21d avg AND new 21d high)."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    cond = ((volume > 3.0 * v_avg) & new_high).astype(float)
    return (cond.rolling(YDAYS, min_periods=QDAYS).sum().where(v_avg.notna(), np.nan)).diff()


def f49_bcco_089_rsi_over_90_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 90 AND new 252d high — extreme-OB at annual high."""
    return (((_rsi(close, 14) > 90.0) & _new_high_252(high)).astype(float).where(_rsi(close, 14).notna(), np.nan)).diff()


def f49_bcco_090_rsi_over_95_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 95 AND new 252d high — superextreme-OB at annual high."""
    return (((_rsi(close, 14) > 95.0) & _new_high_252(high)).astype(float).where(_rsi(close, 14).notna(), np.nan)).diff()


def f49_bcco_091_stoch_k_over_95_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K(14) > 95 AND new 252d high — extreme Stoch at annual high."""
    return (((_stoch_k(high, low, close, 14) > 95.0) & _new_high_252(high)).astype(float).where(_stoch_k(high, low, close, 14).notna(), np.nan)).diff()


def f49_bcco_092_mfi_over_90_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14) > 90 AND new 252d high — extreme vol-confirmed-OB at annual high."""
    return (((_mfi(high, low, close, volume, 14) > 90.0) & _new_high_252(high)).astype(float).where(_mfi(high, low, close, volume, 14).notna(), np.nan)).diff()


def f49_bcco_093_roc21_over_25pct_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d ROC > 25% AND new 252d high."""
    return (((close.pct_change(MDAYS) > 0.25) & _new_high_252(high)).astype(float).where(close.pct_change(MDAYS).notna(), np.nan)).diff()


def f49_bcco_094_roc63_over_75pct_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d ROC > 75% AND new 252d high."""
    return (((close.pct_change(QDAYS) > 0.75) & _new_high_252(high)).astype(float).where(close.pct_change(QDAYS).notna(), np.nan)).diff()


def f49_bcco_095_rsi_5d_rising_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI(14) rose >5 points in past 5 bars AND new 252d high — fast-rising-RSI at top."""
    r = _rsi(close, 14)
    rising = (r - r.shift(WDAYS)) > 5.0
    return ((rising & _new_high_252(high)).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_096_rsi_21d_max_at_252d_max_value_d1(close: pd.Series) -> pd.Series:
    """1 if 21d max of RSI equals its 252d max — RSI peak occurred within past 21 bars."""
    r = _rsi(close, 14)
    return ((r.rolling(MDAYS, min_periods=WDAYS).max() == r.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_097_three_momentum_ob_signals_with_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {RSI>80, Stoch K>90, MFI>80} >= 3 AND new 252d high — 3+ momentum-OBs with annual high."""
    c = ((_rsi(close, 14) > 80.0).astype(float).fillna(0)
         + (_stoch_k(high, low, close, 14) > 90.0).astype(float).fillna(0)
         + (_mfi(high, low, close, volume, 14) > 80.0).astype(float).fillna(0))
    return (((c >= 3) & _new_high_252(high)).astype(float)).diff()


def f49_bcco_098_all_four_momentum_indicators_ob_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI>80 AND Stoch K>80 AND MFI>80 AND Williams %R > -20 — all 4 momentum-indicators OB."""
    return (((_rsi(close, 14) > 80.0)
            & (_stoch_k(high, low, close, 14) > 80.0)
            & (_mfi(high, low, close, volume, 14) > 80.0)
            & (_williams_r(high, low, close, 14) > -20.0)).astype(float)).diff()


def f49_bcco_099_momentum_saturation_avg_over_09_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if mean of normalized {RSI/100, Stoch K/100, MFI/100, (Williams+100)/100} > 0.9 — momentum saturation."""
    m = (_rsi(close, 14) / 100.0 + _stoch_k(high, low, close, 14) / 100.0
         + _mfi(high, low, close, volume, 14) / 100.0 + (_williams_r(high, low, close, 14) + 100.0) / 100.0) / 4.0
    return ((m > 0.9).astype(float).where(m.notna(), np.nan)).diff()


def f49_bcco_100_rsi_over_80_for_10_bars_and_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI(14) > 80 for 10+ consecutive bars AND new 252d high — sustained-OB at peak."""
    r = _rsi(close, 14)
    sus = (_streak_true(r > 80.0) >= 10)
    return ((sus & _new_high_252(high)).astype(float).where(r.notna(), np.nan)).diff()


def f49_bcco_101_tr_over_3x_atr21_and_new_21d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 3x ATR21 AND new 21d high — extreme-wide bar at monthly high."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((rng_ratio > 3.0) & new_high).astype(float).where(rng_ratio.notna(), np.nan)).diff()


def f49_bcco_102_tr_over_3x_atr21_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 3x ATR21 AND new 252d high — extreme-wide bar at annual high."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (((rng_ratio > 3.0) & _new_high_252(high)).astype(float).where(rng_ratio.notna(), np.nan)).diff()


def f49_bcco_103_tr_over_5x_atr21_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 5x ATR21 AND new 252d high — superextreme-wide bar at annual high."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    return (((rng_ratio > 5.0) & _new_high_252(high)).astype(float).where(rng_ratio.notna(), np.nan)).diff()


def f49_bcco_104_hl_range_2x_mean_hl_and_new_high_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if HL range > 2x mean HL range (63d) AND new 21d high."""
    r = high - low
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((r > 2.0 * r.rolling(QDAYS, min_periods=MDAYS).mean()) & new_high).astype(float)).diff()


def f49_bcco_105_3bar_avg_tr_over_2x_21d_avg_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3-bar avg TR > 2x 21d avg TR AND new 21d high — sustained wide-range run at high."""
    tr = _true_range(high, low, close)
    base = tr.rolling(MDAYS, min_periods=WDAYS).mean()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((tr.rolling(3, min_periods=2).mean() > 2.0 * base) & new_high).astype(float).where(base.notna(), np.nan)).diff()


def f49_bcco_106_5bar_max_tr_over_3x_atr63_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if max(TR, past 5) > 3x ATR63 AND new 21d high."""
    tr = _true_range(high, low, close)
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((tr.rolling(WDAYS, min_periods=2).max() > 3.0 * _atr(high, low, close, QDAYS)) & new_high).astype(float)).diff()


def f49_bcco_107_tr_double_prior_tr_and_new_21d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > 2x prior TR AND new 21d high — sudden range-expansion at high."""
    tr = _true_range(high, low, close)
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((tr > 2.0 * tr.shift(1)) & new_high).astype(float).where(tr.shift(1).notna(), np.nan)).diff()


def f49_bcco_108_hl_range_pct_close_above_15pct_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if HL range > 15% of close AND new 21d high."""
    rp = _safe_div(high - low, close)
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((rp > 0.15) & new_high).astype(float).where(rp.notna(), np.nan)).diff()


def f49_bcco_109_three_consecutive_widening_tr_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > TR[t-1] > TR[t-2] (3 days widening) AND new 21d high."""
    tr = _true_range(high, low, close)
    widening = (tr > tr.shift(1)) & (tr.shift(1) > tr.shift(2))
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return ((widening & new_high).astype(float).where(tr.notna(), np.nan)).diff()


def f49_bcco_110_tr_at_21d_max_and_new_21d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR equals 21d max of TR AND new 21d high — peak-range bar at peak-price."""
    tr = _true_range(high, low, close)
    tr_max = tr.rolling(MDAYS, min_periods=WDAYS).max()
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return (((tr == tr_max) & new_high).astype(float).where(tr_max.notna(), np.nan)).diff()


def f49_bcco_111_ext_sma21_atr21_over_3_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close-SMA21)/ATR21 > 3 AND new 252d high — strong monthly overextension at annual high."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (((e > 3.0) & _new_high_252(high)).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_112_ext_sma200_atr21_over_5_and_new_252d_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close-SMA200)/ATR21 > 5 AND new 252d high — far-above-SMA200 at annual high."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (((e > 5.0) & _new_high_252(high)).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_113_ext_sma252_atr21_over_5_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close-SMA252)/ATR21 > 5 — extreme annual MA-overextension (climax)."""
    e = _safe_div(close - _sma(close, YDAYS), _atr(high, low, close, MDAYS))
    return ((e > 5.0).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_114_ext_252d_low_atr252_over_10_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close - 252d low)/ATR252 > 10 — huge extension above annual support in ATR units."""
    e = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(), _atr(high, low, close, YDAYS))
    return ((e > 10.0).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_115_pct_dist_sma200_over_50_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close/SMA200 - 1) > 0.5 (50% above SMA200) AND new 252d high."""
    e = _safe_div(close, _sma(close, 200)) - 1.0
    return (((e > 0.5) & _new_high_252(high)).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_116_pct_dist_sma252_over_100_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (close/SMA252 - 1) > 1.0 (100% above SMA252) AND new 252d high."""
    e = _safe_div(close, _sma(close, YDAYS)) - 1.0
    return (((e > 1.0) & _new_high_252(high)).astype(float).where(e.notna(), np.nan)).diff()


def f49_bcco_117_zscore_ext_sma200_atr21_over_25_and_new_high_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if z-score (252d) of (close-SMA200)/ATR21 > 2.5 AND new 252d high."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    ez = _rolling_zscore(e, YDAYS, min_periods=QDAYS)
    return (((ez > 2.5) & _new_high_252(high)).astype(float).where(ez.notna(), np.nan)).diff()


def f49_bcco_118_log_price_2nd_diff_above_1sigma_d1(close: pd.Series) -> pd.Series:
    """1 if 2nd-diff of log-close > its 63d std (parabolic acceleration > 1 sigma) — parabolic-accel flag."""
    lp = _safe_log(close)
    accel = lp.diff().diff()
    s = accel.rolling(QDAYS, min_periods=MDAYS).std()
    return ((accel > s).astype(float).where(s.notna(), np.nan)).diff()


def f49_bcco_119_log_price_3rd_diff_above_1sigma_and_new_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3rd-diff of log-close > its 63d std AND new 252d high — jerk-extreme at peak."""
    lp = _safe_log(close)
    jerk = lp.diff().diff().diff()
    s = jerk.rolling(QDAYS, min_periods=MDAYS).std()
    return (((jerk > s) & _new_high_252(high)).astype(float).where(s.notna(), np.nan)).diff()


def f49_bcco_120_hyperbolic_singularity_time_proxy_d1(close: pd.Series) -> pd.Series:
    """Time-to-singularity proxy: log(close)/slope(log(close), 63). Smaller (positive) = closer to singularity.
    Negative or NaN when slope <= 0."""
    lp = _safe_log(close)
    sl = _rolling_slope(lp, QDAYS)
    return (_safe_div(lp, sl.where(sl > 0, np.nan))).diff()


def f49_bcco_121_5d_cum_abs_ret_over_30pct_d1(close: pd.Series) -> pd.Series:
    """1 if 5d cumulative |daily return| > 30% — vol-explosion proxy."""
    ar = close.pct_change().abs()
    return ((ar.rolling(WDAYS, min_periods=2).sum() > 0.30).astype(float).where(ar.notna(), np.nan)).diff()


def f49_bcco_122_5d_count_new_21d_highs_ge_4_d1(high: pd.Series) -> pd.Series:
    """1 if 4+ new 21d highs in past 5 bars — sustained breakout count."""
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    return ((new_high.rolling(WDAYS, min_periods=2).sum() >= 4).astype(float).where(new_high.notna(), np.nan)).diff()


def f49_bcco_123_21d_count_new_21d_highs_ge_12_d1(high: pd.Series) -> pd.Series:
    """1 if 12+ new 21d highs in past 21 bars — breakout-heavy month."""
    new_high = (high >= high.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    return ((new_high.rolling(MDAYS, min_periods=WDAYS).sum() >= 12).astype(float).where(new_high.notna(), np.nan)).diff()


def f49_bcco_124_count_up_gap_2pct_past_21_d1(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 21 bars with open-gap >2% — frequency of up-gap openings."""
    g = _safe_div(open_ - close.shift(1), close.shift(1))
    return ((g > 0.02).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(g.notna(), np.nan)).diff()


def f49_bcco_125_longest_up_close_streak_past_63_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive up-close streak in past 63 bars."""
    s = _streak_true(close > close.shift(1))
    return (s.rolling(QDAYS, min_periods=MDAYS).max().where(close.shift(1).notna(), np.nan)).diff()


def f49_bcco_126_up_streak_5_with_new_252d_high_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5+ consecutive up-close AND new 252d high."""
    return (((_streak_true(close > close.shift(1)) >= 5) & _new_high_252(high)).astype(float).where(close.shift(1).notna(), np.nan)).diff()


def f49_bcco_127_max_up_streak_past_252_d1(close: pd.Series) -> pd.Series:
    """Max up-close streak in past 252 bars — best-streak feature."""
    s = _streak_true(close > close.shift(1))
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(close.shift(1).notna(), np.nan)).diff()


def f49_bcco_128_up_down_day_ratio_21_over_3_d1(close: pd.Series) -> pd.Series:
    """1 if up-day count / (down-day count + 1) > 3 in past 21 — exhausted up-bias."""
    up_cnt = (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_cnt = (close < close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((_safe_div(up_cnt, dn_cnt + 1.0) > 3.0).astype(float).where(close.shift(1).notna(), np.nan)).diff()


def f49_bcco_129_up_down_vol_ratio_21_over_3_and_new_high_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if up-vol / down-vol > 3 in past 21 AND new 252d high — heavy up-vol with annual high."""
    up = (close > close.shift(1)).astype(float)
    dn = (close < close.shift(1)).astype(float)
    uv = (up * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dv = (dn * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return (((_safe_div(uv, dv + 1.0) > 3.0) & _new_high_252(high)).astype(float).where(uv.notna(), np.nan)).diff()


def f49_bcco_130_frac_close_top_quartile_range_past_21_over_08_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if fraction past 21 days closing in top-25% of day's range > 0.8 — sustained-strong-close regime."""
    rng = (high - low).replace(0, np.nan)
    top25 = ((close - low) / rng > 0.75).astype(float)
    return ((top25.rolling(MDAYS, min_periods=WDAYS).mean() > 0.8).astype(float).where(rng.notna(), np.nan)).diff()


def f49_bcco_131_signal_count_sum_past_5_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of bar-level signal-count over past 5 bars — short-horizon signal density."""
    s = _signal_sum(high, low, close, volume)
    return (s.rolling(WDAYS, min_periods=2).sum()).diff()


def f49_bcco_132_signal_count_sum_past_21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of bar-level signal-count over past 21 bars — monthly signal density."""
    return (_signal_sum(high, low, close, volume).rolling(MDAYS, min_periods=WDAYS).sum()).diff()


def f49_bcco_133_signal_count_sum_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Quarterly sum of bar-level signal-count."""
    return (_signal_sum(high, low, close, volume).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f49_bcco_134_signal_count_sum_past_252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual sum of bar-level signal-count."""
    return (_signal_sum(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f49_bcco_135_frac_past_21_any_signal_active_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 21 bars with at least one blowoff signal active — broad monthly activity."""
    s = _signal_sum(high, low, close, volume)
    return ((s > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().where(s.notna(), np.nan)).diff()


def f49_bcco_136_frac_past_63_any_signal_active_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 63 bars with any blowoff signal active."""
    s = _signal_sum(high, low, close, volume)
    return ((s > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)).diff()


def f49_bcco_137_max_signal_count_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max bar-level signal-count seen in past 63 — peak-density seen recently."""
    return (_signal_sum(high, low, close, volume).rolling(QDAYS, min_periods=MDAYS).max()).diff()


def f49_bcco_138_dwell_signal_count_ge_3_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 63 bars with signal-count >= 3 — multi-signal dwell."""
    s = _signal_sum(high, low, close, volume)
    return ((s >= 3).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)).diff()


def f49_bcco_139_longest_signal_count_ge_2_streak_past_252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest consecutive run of bars with signal-count >= 2 in past 252."""
    s = _signal_sum(high, low, close, volume)
    st = _streak_true(s >= 2)
    return (st.rolling(YDAYS, min_periods=QDAYS).max().where(s.notna(), np.nan)).diff()


def f49_bcco_140_blowoff_intensity_weighted_score_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted intensity = 2*(RSI/100) + 2*new_high + vol_z + range_z + CLV — scaled blowoff intensity."""
    return (_intensity_score(high, low, close, volume)).diff()


def f49_bcco_141_blowoff_regime_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if intensity-score > 3.5 — blowoff regime indicator."""
    return ((_intensity_score(high, low, close, volume) > 3.5).astype(float)).diff()


def f49_bcco_142_blowoff_regime_dwell_past_21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 21 in blowoff regime."""
    r = (_intensity_score(high, low, close, volume) > 3.5).astype(float)
    return (r.rolling(MDAYS, min_periods=WDAYS).mean().where(r.notna(), np.nan)).diff()


def f49_bcco_143_blowoff_regime_dwell_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 63 in blowoff regime."""
    r = (_intensity_score(high, low, close, volume) > 3.5).astype(float)
    return (r.rolling(QDAYS, min_periods=MDAYS).mean().where(r.notna(), np.nan)).diff()


def f49_bcco_144_regime_entry_recency_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since blowoff regime was last entered (intensity crossed above 3.5 from below)."""
    sc = _intensity_score(high, low, close, volume)
    enter = (sc.shift(1) <= 3.5) & (sc > 3.5)
    return (_bars_since_true(enter)).diff()


def f49_bcco_145_regime_exit_recency_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since blowoff regime was last exited (intensity crossed below 3.5 from above)."""
    sc = _intensity_score(high, low, close, volume)
    exit_ = (sc.shift(1) > 3.5) & (sc <= 3.5)
    return (_bars_since_true(exit_)).diff()


def f49_bcco_146_peak_intensity_past_21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max intensity score past 21 bars."""
    return (_intensity_score(high, low, close, volume).rolling(MDAYS, min_periods=WDAYS).max()).diff()


def f49_bcco_147_peak_intensity_past_252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual peak intensity score."""
    return (_intensity_score(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).max()).diff()


def f49_bcco_148_intensity_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of intensity score."""
    return (_rolling_zscore(_intensity_score(high, low, close, volume), YDAYS, min_periods=QDAYS)).diff()


def f49_bcco_149_intensity_pct_rank_252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of intensity score vs trailing 252d distribution."""
    return (_intensity_score(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f49_bcco_150_terminal_climax_score_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Terminal-climax = max(parabolic_z, vol_z, rsi_norm, range_z) where parabolic_z = z(63d return),
    given new 252d high — composite at-peak indicator."""
    new_high = (high >= high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    par_z = _rolling_zscore(close.pct_change(QDAYS), YDAYS, min_periods=QDAYS).clip(-3, 3)
    vol_z = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).clip(-3, 3)
    rsi_n = (_rsi(close, 14) - 50.0) / 50.0
    rng_z = _rolling_zscore(_safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS)), YDAYS, min_periods=QDAYS).clip(-3, 3)
    m = pd.concat([par_z.rename("p"), vol_z.rename("v"), rsi_n.rename("r"), rng_z.rename("g")], axis=1).max(axis=1)
    return (m * new_high).diff()


# ============================================================
#                         REGISTRY 076-150 (d1)
# ============================================================

_HV = ["high", "volume"]
_HC = ["high", "close"]
_HCV = ["high", "close", "volume"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_HL = ["high", "low"]
_OC = ["open", "close"]
_CV = ["close", "volume"]

BLOWOFF_CLIMAX_COMPOSITE_D1_REGISTRY_076_150 = {
    "f49_bcco_076_vol_zscore_over_3_and_new_21d_high_d1": {"inputs": _HV, "func": f49_bcco_076_vol_zscore_over_3_and_new_21d_high_d1},
    "f49_bcco_077_vol_zscore_over_3_and_new_252d_high_d1": {"inputs": _HV, "func": f49_bcco_077_vol_zscore_over_3_and_new_252d_high_d1},
    "f49_bcco_078_3bar_vol_sum_3x_63d_avg_and_new_high_d1": {"inputs": _HV, "func": f49_bcco_078_3bar_vol_sum_3x_63d_avg_and_new_high_d1},
    "f49_bcco_079_5bar_vol_sum_5x_63d_avg_and_new_high_d1": {"inputs": _HV, "func": f49_bcco_079_5bar_vol_sum_5x_63d_avg_and_new_high_d1},
    "f49_bcco_080_top5_vol_days_within_21_of_now_and_at_high_d1": {"inputs": _HV, "func": f49_bcco_080_top5_vol_days_within_21_of_now_and_at_high_d1},
    "f49_bcco_081_alltime_vol_high_and_new_252d_high_d1": {"inputs": _HV, "func": f49_bcco_081_alltime_vol_high_and_new_252d_high_d1},
    "f49_bcco_082_dollar_vol_3x_median_and_new_high_d1": {"inputs": _HCV, "func": f49_bcco_082_dollar_vol_3x_median_and_new_high_d1},
    "f49_bcco_083_dollar_vol_zscore_over_3_and_new_high_d1": {"inputs": _HCV, "func": f49_bcco_083_dollar_vol_zscore_over_3_and_new_high_d1},
    "f49_bcco_084_vol_at_63d_max_and_new_252d_high_d1": {"inputs": _HV, "func": f49_bcco_084_vol_at_63d_max_and_new_252d_high_d1},
    "f49_bcco_085_climax_then_fade_flag_d1": {"inputs": _HV, "func": f49_bcco_085_climax_then_fade_flag_d1},
    "f49_bcco_086_climax_then_fade_count_252_d1": {"inputs": _HV, "func": f49_bcco_086_climax_then_fade_count_252_d1},
    "f49_bcco_087_bars_since_last_climax_bar_d1": {"inputs": _HV, "func": f49_bcco_087_bars_since_last_climax_bar_d1},
    "f49_bcco_088_climax_bar_count_252_d1": {"inputs": _HV, "func": f49_bcco_088_climax_bar_count_252_d1},
    "f49_bcco_089_rsi_over_90_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_089_rsi_over_90_and_new_252d_high_d1},
    "f49_bcco_090_rsi_over_95_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_090_rsi_over_95_and_new_252d_high_d1},
    "f49_bcco_091_stoch_k_over_95_and_new_252d_high_d1": {"inputs": _HLC, "func": f49_bcco_091_stoch_k_over_95_and_new_252d_high_d1},
    "f49_bcco_092_mfi_over_90_and_new_252d_high_d1": {"inputs": _HLCV, "func": f49_bcco_092_mfi_over_90_and_new_252d_high_d1},
    "f49_bcco_093_roc21_over_25pct_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_093_roc21_over_25pct_and_new_252d_high_d1},
    "f49_bcco_094_roc63_over_75pct_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_094_roc63_over_75pct_and_new_252d_high_d1},
    "f49_bcco_095_rsi_5d_rising_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_095_rsi_5d_rising_and_new_252d_high_d1},
    "f49_bcco_096_rsi_21d_max_at_252d_max_value_d1": {"inputs": ["close"], "func": f49_bcco_096_rsi_21d_max_at_252d_max_value_d1},
    "f49_bcco_097_three_momentum_ob_signals_with_new_high_d1": {"inputs": _HLCV, "func": f49_bcco_097_three_momentum_ob_signals_with_new_high_d1},
    "f49_bcco_098_all_four_momentum_indicators_ob_d1": {"inputs": _HLCV, "func": f49_bcco_098_all_four_momentum_indicators_ob_d1},
    "f49_bcco_099_momentum_saturation_avg_over_09_d1": {"inputs": _HLCV, "func": f49_bcco_099_momentum_saturation_avg_over_09_d1},
    "f49_bcco_100_rsi_over_80_for_10_bars_and_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_100_rsi_over_80_for_10_bars_and_new_252d_high_d1},
    "f49_bcco_101_tr_over_3x_atr21_and_new_21d_high_d1": {"inputs": _HLC, "func": f49_bcco_101_tr_over_3x_atr21_and_new_21d_high_d1},
    "f49_bcco_102_tr_over_3x_atr21_and_new_252d_high_d1": {"inputs": _HLC, "func": f49_bcco_102_tr_over_3x_atr21_and_new_252d_high_d1},
    "f49_bcco_103_tr_over_5x_atr21_and_new_252d_high_d1": {"inputs": _HLC, "func": f49_bcco_103_tr_over_5x_atr21_and_new_252d_high_d1},
    "f49_bcco_104_hl_range_2x_mean_hl_and_new_high_d1": {"inputs": _HL, "func": f49_bcco_104_hl_range_2x_mean_hl_and_new_high_d1},
    "f49_bcco_105_3bar_avg_tr_over_2x_21d_avg_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_105_3bar_avg_tr_over_2x_21d_avg_and_new_high_d1},
    "f49_bcco_106_5bar_max_tr_over_3x_atr63_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_106_5bar_max_tr_over_3x_atr63_and_new_high_d1},
    "f49_bcco_107_tr_double_prior_tr_and_new_21d_high_d1": {"inputs": _HLC, "func": f49_bcco_107_tr_double_prior_tr_and_new_21d_high_d1},
    "f49_bcco_108_hl_range_pct_close_above_15pct_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_108_hl_range_pct_close_above_15pct_and_new_high_d1},
    "f49_bcco_109_three_consecutive_widening_tr_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_109_three_consecutive_widening_tr_and_new_high_d1},
    "f49_bcco_110_tr_at_21d_max_and_new_21d_high_d1": {"inputs": _HLC, "func": f49_bcco_110_tr_at_21d_max_and_new_21d_high_d1},
    "f49_bcco_111_ext_sma21_atr21_over_3_and_new_252d_high_d1": {"inputs": _HLC, "func": f49_bcco_111_ext_sma21_atr21_over_3_and_new_252d_high_d1},
    "f49_bcco_112_ext_sma200_atr21_over_5_and_new_252d_high_d1": {"inputs": _HLC, "func": f49_bcco_112_ext_sma200_atr21_over_5_and_new_252d_high_d1},
    "f49_bcco_113_ext_sma252_atr21_over_5_d1": {"inputs": _HLC, "func": f49_bcco_113_ext_sma252_atr21_over_5_d1},
    "f49_bcco_114_ext_252d_low_atr252_over_10_d1": {"inputs": _HLC, "func": f49_bcco_114_ext_252d_low_atr252_over_10_d1},
    "f49_bcco_115_pct_dist_sma200_over_50_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_115_pct_dist_sma200_over_50_and_new_high_d1},
    "f49_bcco_116_pct_dist_sma252_over_100_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_116_pct_dist_sma252_over_100_and_new_high_d1},
    "f49_bcco_117_zscore_ext_sma200_atr21_over_25_and_new_high_d1": {"inputs": _HLC, "func": f49_bcco_117_zscore_ext_sma200_atr21_over_25_and_new_high_d1},
    "f49_bcco_118_log_price_2nd_diff_above_1sigma_d1": {"inputs": ["close"], "func": f49_bcco_118_log_price_2nd_diff_above_1sigma_d1},
    "f49_bcco_119_log_price_3rd_diff_above_1sigma_and_new_high_d1": {"inputs": _HC, "func": f49_bcco_119_log_price_3rd_diff_above_1sigma_and_new_high_d1},
    "f49_bcco_120_hyperbolic_singularity_time_proxy_d1": {"inputs": ["close"], "func": f49_bcco_120_hyperbolic_singularity_time_proxy_d1},
    "f49_bcco_121_5d_cum_abs_ret_over_30pct_d1": {"inputs": ["close"], "func": f49_bcco_121_5d_cum_abs_ret_over_30pct_d1},
    "f49_bcco_122_5d_count_new_21d_highs_ge_4_d1": {"inputs": ["high"], "func": f49_bcco_122_5d_count_new_21d_highs_ge_4_d1},
    "f49_bcco_123_21d_count_new_21d_highs_ge_12_d1": {"inputs": ["high"], "func": f49_bcco_123_21d_count_new_21d_highs_ge_12_d1},
    "f49_bcco_124_count_up_gap_2pct_past_21_d1": {"inputs": _OC, "func": f49_bcco_124_count_up_gap_2pct_past_21_d1},
    "f49_bcco_125_longest_up_close_streak_past_63_d1": {"inputs": ["close"], "func": f49_bcco_125_longest_up_close_streak_past_63_d1},
    "f49_bcco_126_up_streak_5_with_new_252d_high_d1": {"inputs": _HC, "func": f49_bcco_126_up_streak_5_with_new_252d_high_d1},
    "f49_bcco_127_max_up_streak_past_252_d1": {"inputs": ["close"], "func": f49_bcco_127_max_up_streak_past_252_d1},
    "f49_bcco_128_up_down_day_ratio_21_over_3_d1": {"inputs": ["close"], "func": f49_bcco_128_up_down_day_ratio_21_over_3_d1},
    "f49_bcco_129_up_down_vol_ratio_21_over_3_and_new_high_d1": {"inputs": _HCV, "func": f49_bcco_129_up_down_vol_ratio_21_over_3_and_new_high_d1},
    "f49_bcco_130_frac_close_top_quartile_range_past_21_over_08_d1": {"inputs": _HLC, "func": f49_bcco_130_frac_close_top_quartile_range_past_21_over_08_d1},
    "f49_bcco_131_signal_count_sum_past_5_d1": {"inputs": _HLCV, "func": f49_bcco_131_signal_count_sum_past_5_d1},
    "f49_bcco_132_signal_count_sum_past_21_d1": {"inputs": _HLCV, "func": f49_bcco_132_signal_count_sum_past_21_d1},
    "f49_bcco_133_signal_count_sum_past_63_d1": {"inputs": _HLCV, "func": f49_bcco_133_signal_count_sum_past_63_d1},
    "f49_bcco_134_signal_count_sum_past_252_d1": {"inputs": _HLCV, "func": f49_bcco_134_signal_count_sum_past_252_d1},
    "f49_bcco_135_frac_past_21_any_signal_active_d1": {"inputs": _HLCV, "func": f49_bcco_135_frac_past_21_any_signal_active_d1},
    "f49_bcco_136_frac_past_63_any_signal_active_d1": {"inputs": _HLCV, "func": f49_bcco_136_frac_past_63_any_signal_active_d1},
    "f49_bcco_137_max_signal_count_past_63_d1": {"inputs": _HLCV, "func": f49_bcco_137_max_signal_count_past_63_d1},
    "f49_bcco_138_dwell_signal_count_ge_3_past_63_d1": {"inputs": _HLCV, "func": f49_bcco_138_dwell_signal_count_ge_3_past_63_d1},
    "f49_bcco_139_longest_signal_count_ge_2_streak_past_252_d1": {"inputs": _HLCV, "func": f49_bcco_139_longest_signal_count_ge_2_streak_past_252_d1},
    "f49_bcco_140_blowoff_intensity_weighted_score_d1": {"inputs": _HLCV, "func": f49_bcco_140_blowoff_intensity_weighted_score_d1},
    "f49_bcco_141_blowoff_regime_indicator_d1": {"inputs": _HLCV, "func": f49_bcco_141_blowoff_regime_indicator_d1},
    "f49_bcco_142_blowoff_regime_dwell_past_21_d1": {"inputs": _HLCV, "func": f49_bcco_142_blowoff_regime_dwell_past_21_d1},
    "f49_bcco_143_blowoff_regime_dwell_past_63_d1": {"inputs": _HLCV, "func": f49_bcco_143_blowoff_regime_dwell_past_63_d1},
    "f49_bcco_144_regime_entry_recency_d1": {"inputs": _HLCV, "func": f49_bcco_144_regime_entry_recency_d1},
    "f49_bcco_145_regime_exit_recency_d1": {"inputs": _HLCV, "func": f49_bcco_145_regime_exit_recency_d1},
    "f49_bcco_146_peak_intensity_past_21_d1": {"inputs": _HLCV, "func": f49_bcco_146_peak_intensity_past_21_d1},
    "f49_bcco_147_peak_intensity_past_252_d1": {"inputs": _HLCV, "func": f49_bcco_147_peak_intensity_past_252_d1},
    "f49_bcco_148_intensity_zscore_252_d1": {"inputs": _HLCV, "func": f49_bcco_148_intensity_zscore_252_d1},
    "f49_bcco_149_intensity_pct_rank_252_d1": {"inputs": _HLCV, "func": f49_bcco_149_intensity_pct_rank_252_d1},
    "f49_bcco_150_terminal_climax_score_d1": {"inputs": _HLCV, "func": f49_bcco_150_terminal_climax_score_d1},
}
