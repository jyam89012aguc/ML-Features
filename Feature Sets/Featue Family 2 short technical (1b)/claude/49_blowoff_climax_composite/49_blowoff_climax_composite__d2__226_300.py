"""blowoff_climax_composite d2 features 226-300 — Pipeline 1b-technical.

Second gap-fill batch. New angles distinct from 001-225:
- Coil-and-release variants (Keltner squeeze, ADX-rising-from-low)
- Multi-indicator confluence at peak (all-of-N momentum/vol triggers)
- Multi-day climax sequences (different lengths/thresholds)
- More statistical-extreme composites (different windows/percentiles)
- More candle-pattern climax confirmations (engulfings, three-black-crows, etc.)
- Failed-breakout/false-positive composites (different lookback windows)
- Vol/breadth climax (gap-up counts, up-bar fractions)
- VWAP-cross composites (multiple VWAP timeframes + new high)

Bucket W: Coil-and-release composites (226-233).
Bucket X: Multi-indicator climax confluence (234-243).
Bucket Y: Multi-day climax sequences (244-253).
Bucket Z: More statistical extreme composites (254-263).
Bucket AA: Candle-pattern climax confirmations (264-273).
Bucket BB: Failed-breakout / false-positive composites (274-281).
Bucket CC: Vol / breadth climax (282-291).
Bucket DD: VWAP cross-composites (292-300).

Inputs: SEP OHLCV. Self-contained; PIT-clean.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


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


def _clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _new_high_21(high):
    return high >= high.rolling(MDAYS, min_periods=WDAYS).max()


def _new_high_63(high):
    return high >= high.rolling(QDAYS, min_periods=MDAYS).max()


def _new_high_252(high):
    return high >= high.rolling(YDAYS, min_periods=QDAYS).max()


def _adx(high, low, close, n=14):
    """ADX(n) — Wilder's average directional index."""
    pc = close.shift(1)
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
    tr = _true_range(high, low, close)
    atr_n = tr.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    plus_di = 100.0 * _safe_div(plus_dm.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean(), atr_n)
    minus_di = 100.0 * _safe_div(minus_dm.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean(), atr_n)
    dx = 100.0 * _safe_div((plus_di - minus_di).abs(), plus_di + minus_di)
    return dx.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()


def _rolling_vwap(close, volume, n):
    num = (close * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


# ============================================================
# Bucket W — Coil-and-release composites (226-233)
# ============================================================


def f49_bcco_226_keltner_squeeze_release_with_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Keltner-channel width was in lowest decile in past 10 bars AND new 21d high today."""
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    width = 4.0 * a
    q10 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    squeeze_recent = (width <= q10).astype(float).rolling(10, min_periods=1).max() > 0
    return ((squeeze_recent & _new_high_21(high)).astype(float).where(q10.notna(), np.nan)).diff().diff()


def f49_bcco_227_adx_rising_from_below_20_with_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ADX(14) was <20 in past 21 bars AND today ADX > 25 AND new 21d high — coiled trend breakout."""
    a = _adx(high, low, close, 14)
    low_recent = (a.rolling(MDAYS, min_periods=WDAYS).min() < 20)
    return ((low_recent & (a > 25) & _new_high_21(high)).astype(float).where(a.notna(), np.nan)).diff().diff()


def f49_bcco_228_atr_pct_close_in_lowest_quartile_then_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (ATR21/close) was in lowest 25% of trailing 252d for past 10 bars AND new 21d high — quiet-then-loud."""
    ratio = _safe_div(_atr(high, low, close, MDAYS), close)
    q25 = ratio.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    quiet_recent = (ratio <= q25).astype(float).rolling(10, min_periods=1).max() > 0
    return ((quiet_recent & _new_high_21(high)).astype(float).where(q25.notna(), np.nan)).diff().diff()


def f49_bcco_229_low_vol_5_days_then_vol_spike_new_high_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if past 5 bars all had vol < 70% of 21d avg AND today vol > 2x AND new 21d high — drought-then-spike + breakout."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    dry_5 = ((volume.shift(1) < 0.7 * v_avg.shift(1))
             & (volume.shift(2) < 0.7 * v_avg.shift(2))
             & (volume.shift(3) < 0.7 * v_avg.shift(3))
             & (volume.shift(4) < 0.7 * v_avg.shift(4))
             & (volume.shift(5) < 0.7 * v_avg.shift(5)))
    return ((dry_5 & (volume > 2.0 * v_avg) & _new_high_21(high)).astype(float).where(v_avg.notna(), np.nan)).diff().diff()


def f49_bcco_230_donchian20_width_in_lowest_decile_then_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Donchian-20 width in lowest decile of 252d past 10 bars AND new 21d high."""
    hh = high.rolling(20, min_periods=10).max()
    ll = low.rolling(20, min_periods=10).min()
    w = hh - ll
    q10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    coil = (w <= q10).astype(float).rolling(10, min_periods=1).max() > 0
    return ((coil & _new_high_21(high)).astype(float).where(q10.notna(), np.nan)).diff().diff()


def f49_bcco_231_close_pos_in_21d_range_q10_then_jump_to_q95_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5 bars ago position-in-21d-range was <10% AND today position > 95% — coil-bottom to breakout-top jump."""
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return (((pos.shift(WDAYS) < 0.10) & (pos > 0.95)).astype(float).where(pos.notna(), np.nan)).diff().diff()


def f49_bcco_232_bb_squeeze_5days_then_close_above_upper_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BB bandwidth in lowest decile for 5 consecutive prior bars AND today close > BB upper."""
    sd = close.rolling(20, min_periods=10).std()
    bw = sd * 4.0
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    squeeze_5 = ((bw.shift(1) <= q10.shift(1))
                 & (bw.shift(2) <= q10.shift(2))
                 & (bw.shift(3) <= q10.shift(3))
                 & (bw.shift(4) <= q10.shift(4))
                 & (bw.shift(5) <= q10.shift(5)))
    m = close.rolling(20, min_periods=10).mean()
    return ((squeeze_5 & (close > (m + 2.0 * sd))).astype(float).where(sd.notna() & q10.notna(), np.nan)).diff().diff()


def f49_bcco_233_atr_doubled_in_5_bars_with_new_252d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 > 2x its value 5 bars ago AND new 252d high — sudden vol-expansion at peak."""
    a = _atr(high, low, close, MDAYS)
    return (((a > 2.0 * a.shift(WDAYS)) & _new_high_252(high)).astype(float).where(a.shift(WDAYS).notna(), np.nan)).diff().diff()


def f49_bcco_234_all_4_momentum_ob_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI>70 AND Stoch K>80 AND MFI>70 AND new 252d high."""
    return (((_rsi(close, 14) > 70.0)
            & (_stoch_k(high, low, close, 14) > 80.0)
            & (_mfi(high, low, close, volume, 14) > 70.0)
            & _new_high_252(high)).astype(float)).diff().diff()


def f49_bcco_235_all_5_extreme_ob_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI>80 AND Stoch K>90 AND MFI>80 AND Williams %R > -10 AND new 252d high."""
    ll = low.rolling(14, min_periods=5).min()
    hh = high.rolling(14, min_periods=5).max()
    wr = -100.0 * _safe_div(hh - close, hh - ll)
    return (((_rsi(close, 14) > 80.0)
            & (_stoch_k(high, low, close, 14) > 90.0)
            & (_mfi(high, low, close, volume, 14) > 80.0)
            & (wr > -10.0)
            & _new_high_252(high)).astype(float)).diff().diff()


def f49_bcco_236_any_3_of_5_signals_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if any 3 of {RSI>80, Stoch>90, MFI>80, ROC21>20%, vol z>2} AND new 252d high."""
    cnt = ((_rsi(close, 14) > 80.0).astype(float).fillna(0)
           + (_stoch_k(high, low, close, 14) > 90.0).astype(float).fillna(0)
           + (_mfi(high, low, close, volume, 14) > 80.0).astype(float).fillna(0)
           + (close.pct_change(MDAYS) > 0.20).astype(float).fillna(0)
           + (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0).astype(float).fillna(0))
    return (((cnt >= 3) & _new_high_252(high)).astype(float)).diff().diff()


def f49_bcco_237_5plus_indicators_climax_dwell_21_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction past 21 bars where >= 3 of 5 multi-signals were firing."""
    cnt = ((_rsi(close, 14) > 80.0).astype(float).fillna(0)
           + (_stoch_k(high, low, close, 14) > 90.0).astype(float).fillna(0)
           + (_mfi(high, low, close, volume, 14) > 80.0).astype(float).fillna(0)
           + (close.pct_change(MDAYS) > 0.20).astype(float).fillna(0)
           + (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0).astype(float).fillna(0))
    return ((cnt >= 3).astype(float).rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()


def f49_bcco_238_normalized_momentum_mean_over_80_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if mean of {RSI, Stoch K, MFI} > 80 AND new 252d high — momentum consensus."""
    avg = (_rsi(close, 14) + _stoch_k(high, low, close, 14) + _mfi(high, low, close, volume, 14)) / 3.0
    return (((avg > 80.0) & _new_high_252(high)).astype(float).where(avg.notna(), np.nan)).diff().diff()


def f49_bcco_239_rsi_stoch_corr_high_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if rolling 21d corr(RSI, Stoch K) > 0.9 AND new 252d high — high cross-indicator agreement at peak."""
    r = _rsi(close, 14)
    k = _stoch_k(high, low, close, 14)
    c = r.rolling(MDAYS, min_periods=WDAYS).corr(k)
    return (((c > 0.9) & _new_high_252(high)).astype(float).where(c.notna(), np.nan)).diff().diff()


def f49_bcco_240_rsi_stoch_mfi_all_above_80_and_atr_z_2_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI > 80 AND Stoch > 80 AND MFI > 80 AND ATR21 z-score > 2."""
    az = _rolling_zscore(_atr(high, low, close, MDAYS), YDAYS, min_periods=QDAYS)
    return (((_rsi(close, 14) > 80.0)
            & (_stoch_k(high, low, close, 14) > 80.0)
            & (_mfi(high, low, close, volume, 14) > 80.0)
            & (az > 2.0)).astype(float)).diff().diff()


def f49_bcco_241_rsi_zscore_252_over_2_5_and_new_252d_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI z-score (252d) > 2.5 AND new 252d high."""
    rz = _rolling_zscore(_rsi(close, 14), YDAYS, min_periods=QDAYS)
    return (((rz > 2.5) & _new_high_252(high)).astype(float).where(rz.notna(), np.nan)).diff().diff()


def f49_bcco_242_stoch_k_zscore_252_over_2_5_and_new_252d_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Stoch K z-score (252d) > 2.5 AND new 252d high."""
    kz = _rolling_zscore(_stoch_k(high, low, close, 14), YDAYS, min_periods=QDAYS)
    return (((kz > 2.5) & _new_high_252(high)).astype(float).where(kz.notna(), np.nan)).diff().diff()


def f49_bcco_243_all_3_momentum_at_252d_max_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if RSI, Stoch K, MFI all at their trailing 252d max AND new 252d high — peak-of-all-momentum."""
    r = _rsi(close, 14); k = _stoch_k(high, low, close, 14); m = _mfi(high, low, close, volume, 14)
    return (((r >= r.rolling(YDAYS, min_periods=QDAYS).max())
            & (k >= k.rolling(YDAYS, min_periods=QDAYS).max())
            & (m >= m.rolling(YDAYS, min_periods=QDAYS).max())
            & _new_high_252(high)).astype(float).where(r.notna() & k.notna() & m.notna(), np.nan)).diff().diff()


def f49_bcco_244_3_consecutive_new_21d_highs_d2(high: pd.Series) -> pd.Series:
    """1 if today and prior 2 bars all new 21d highs — short-horizon sustained-breakout."""
    nh = _new_high_21(high)
    return ((nh & nh.shift(1) & nh.shift(2)).astype(float).where(nh.notna(), np.nan)).diff().diff()


def f49_bcco_245_3_wide_range_and_3_new_highs_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3 consecutive wide-range bars AND 3 consecutive new 21d highs."""
    rng_ratio = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    wide_3 = (rng_ratio > 2.0) & (rng_ratio.shift(1) > 2.0) & (rng_ratio.shift(2) > 2.0)
    nh = _new_high_21(high)
    nh_3 = nh & nh.shift(1) & nh.shift(2)
    return ((wide_3 & nh_3).astype(float).where(rng_ratio.notna(), np.nan)).diff().diff()


def f49_bcco_246_5d_count_vol_z_over_2_ge_3_and_new_252d_high_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3+ vol z>2 bars in past 5 AND new 252d high — heavy-vol-cluster + peak."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    cnt = (vz > 2.0).astype(float).rolling(WDAYS, min_periods=2).sum()
    return (((cnt >= 3) & _new_high_252(high)).astype(float).where(vz.notna(), np.nan)).diff().diff()


def f49_bcco_247_5_consecutive_rsi_over_80_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI > 80 for past 5 consecutive bars AND new 252d high — sustained extreme momentum at peak."""
    r = _rsi(close, 14)
    rsi_5 = (r > 80.0) & (r.shift(1) > 80.0) & (r.shift(2) > 80.0) & (r.shift(3) > 80.0) & (r.shift(4) > 80.0)
    return ((rsi_5 & _new_high_252(high)).astype(float).where(r.notna(), np.nan)).diff().diff()


def f49_bcco_248_5_consecutive_tr_over_atr21_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if TR > ATR21 for 5 consecutive bars AND new 21d high."""
    a = _atr(high, low, close, MDAYS)
    tr = _true_range(high, low, close)
    cond = (tr > a) & (tr.shift(1) > a.shift(1)) & (tr.shift(2) > a.shift(2)) & (tr.shift(3) > a.shift(3)) & (tr.shift(4) > a.shift(4))
    return ((cond & _new_high_21(high)).astype(float).where(a.notna(), np.nan)).diff().diff()


def f49_bcco_249_5_consecutive_body_over_half_range_and_new_high_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if body/range > 0.5 for 5 consecutive bars AND new 21d high — strong-body persistence + breakout."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    cond = (br > 0.5) & (br.shift(1) > 0.5) & (br.shift(2) > 0.5) & (br.shift(3) > 0.5) & (br.shift(4) > 0.5)
    return ((cond & _new_high_21(high)).astype(float).where(br.notna(), np.nan)).diff().diff()


def f49_bcco_250_rising_rsi_5d_streak_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RSI rose monotonically for past 5 days AND new 252d high — accelerating momentum + peak."""
    r = _rsi(close, 14)
    rising_5 = (r > r.shift(1)) & (r.shift(1) > r.shift(2)) & (r.shift(2) > r.shift(3)) & (r.shift(3) > r.shift(4)) & (r.shift(4) > r.shift(5))
    return ((rising_5 & _new_high_252(high)).astype(float).where(r.notna(), np.nan)).diff().diff()


def f49_bcco_251_3_consecutive_vol_2x_avg_and_new_high_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3 consecutive bars with vol > 2x 21d-avg AND new 252d high."""
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (volume > 2.0 * v_avg) & (volume.shift(1) > 2.0 * v_avg.shift(1)) & (volume.shift(2) > 2.0 * v_avg.shift(2))
    return ((cond & _new_high_252(high)).astype(float).where(v_avg.notna(), np.nan)).diff().diff()


def f49_bcco_252_5d_cum_vol_zscore_over_5_and_new_high_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5-day cumulative vol z-score (252d) > 5 AND new 252d high — cumulative-vol-flood + peak."""
    vz_sum = _rolling_zscore(volume, YDAYS, min_periods=QDAYS).rolling(WDAYS, min_periods=2).sum()
    return (((vz_sum > 5.0) & _new_high_252(high)).astype(float).where(vz_sum.notna(), np.nan)).diff().diff()


def f49_bcco_253_5d_cum_return_zscore_over_3_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5-day cum return z-score (252d) > 3 AND new 252d high — extreme cumulative-strength + peak."""
    rz_sum = _rolling_zscore(close.pct_change(), YDAYS, min_periods=QDAYS).rolling(WDAYS, min_periods=2).sum()
    return (((rz_sum > 3.0) & _new_high_252(high)).astype(float).where(rz_sum.notna(), np.nan)).diff().diff()


def f49_bcco_254_1bar_return_zscore_over_3_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 1-bar return z-score (252d) > 3 AND new 252d high — single-bar panic-buying + peak."""
    rz = _rolling_zscore(close.pct_change(), YDAYS, min_periods=QDAYS)
    return (((rz > 3.0) & _new_high_252(high)).astype(float).where(rz.notna(), np.nan)).diff().diff()


def f49_bcco_255_1bar_return_zscore_over_4_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 1-bar return z > 4 AND new 252d high — extreme single-bar buy."""
    rz = _rolling_zscore(close.pct_change(), YDAYS, min_periods=QDAYS)
    return (((rz > 4.0) & _new_high_252(high)).astype(float).where(rz.notna(), np.nan)).diff().diff()


def f49_bcco_256_5d_sharpe_like_over_3_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5d cum return / 5d std-of-returns > 3 AND new 252d high — weekly-sharpe extreme."""
    r = close.pct_change()
    sh = _safe_div(r.rolling(WDAYS, min_periods=2).sum(), r.rolling(WDAYS, min_periods=2).std())
    return (((sh > 3.0) & _new_high_252(high)).astype(float).where(sh.notna(), np.nan)).diff().diff()


def f49_bcco_257_21d_return_pct_rank_504_over_99_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d return percentile rank > 99% over 504d AND new 252d high."""
    pr = close.pct_change(MDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)
    return (((pr > 0.99) & _new_high_252(high)).astype(float).where(pr.notna(), np.nan)).diff().diff()


def f49_bcco_258_5d_cum_return_over_30pct_d2(close: pd.Series) -> pd.Series:
    """1 if 5-day cumulative return > 30% — extreme weekly gain (climax intensity)."""
    return ((close.pct_change(WDAYS) > 0.30).astype(float).where(close.pct_change(WDAYS).notna(), np.nan)).diff().diff()


def f49_bcco_259_21d_cum_return_at_252d_max_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 21d cumulative return at 252d max AND new 252d high — peak-monthly-acceleration."""
    r21 = close.pct_change(MDAYS)
    return (((r21 >= r21.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(r21.notna(), np.nan)).diff().diff()


def f49_bcco_260_63d_cum_return_at_252d_max_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 63d cum return at 252d max AND new 252d high — peak-quarterly-acceleration."""
    r63 = close.pct_change(QDAYS)
    return (((r63 >= r63.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(r63.notna(), np.nan)).diff().diff()


def f49_bcco_261_1bar_return_pct_rank_252_over_99_and_new_high_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 1-bar return percentile rank > 99% past 252 AND new 252d high — extreme single-bar buy at peak."""
    pr = close.pct_change().rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (((pr > 0.99) & _new_high_252(high)).astype(float).where(pr.notna(), np.nan)).diff().diff()


def f49_bcco_262_1bar_return_over_4sigma_annual_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """1 if 1-bar return > 4 sigma (annual std, sqrt(252) scaled) AND new 252d high."""
    r = close.pct_change()
    s_ann = r.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)
    s_daily = s_ann / np.sqrt(YDAYS)
    return (((r > 4.0 * s_daily) & _new_high_252(high)).astype(float).where(s_daily.notna(), np.nan)).diff().diff()


def f49_bcco_263_peak_1d_return_past_21_over_peak_252_ratio_d2(close: pd.Series) -> pd.Series:
    """(max 1-bar return past 21) / (max 1-bar return past 252) — recency-of-extreme-buy ratio.

    High value (close to 1) = the largest 1-bar gain seen in the past year happened recently.
    """
    r = close.pct_change()
    return (_safe_div(r.rolling(MDAYS, min_periods=WDAYS).max(), r.rolling(YDAYS, min_periods=QDAYS).max())).diff().diff()


def f49_bcco_264_shooting_star_at_new_252d_high_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND small body (<0.3 range) AND upper shadow > 2*body — shooting star at peak."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    return ((_new_high_252(high) & (body < 0.3 * rng) & (upper > 2.0 * body)).astype(float).where(rng.notna(), np.nan)).diff().diff()


def f49_bcco_265_hanging_man_at_new_252d_high_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if new 252d high AND small body AND lower shadow > 2*body — hanging-man at peak."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    lower = pd.concat([open_, close], axis=1).min(axis=1) - low
    return ((_new_high_252(high) & (body < 0.3 * rng) & (lower > 2.0 * body)).astype(float).where(rng.notna(), np.nan)).diff().diff()


def f49_bcco_266_dark_cloud_after_new_high_gap_then_below_mid_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar was new 252d high AND today opened above prior high AND closed below prior bar's midpoint — dark-cloud cover."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    nh = (high.shift(1) >= rmax_prev)
    gap_above = (open_ > high.shift(1))
    mid_prev = (high.shift(1) + low.shift(1)) / 2.0
    return ((nh & gap_above & (close < mid_prev)).astype(float).where(rmax_prev.notna(), np.nan)).diff().diff()


def f49_bcco_267_bearish_engulfing_after_new_252d_high_strong_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prior bar new 252d high AND prior bullish AND today's body > 1.5x prior body AND today bear engulfs."""
    rmax_prev = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    nh = (high.shift(1) >= rmax_prev)
    prior_bull = close.shift(1) > open_.shift(1)
    today_bear = close < open_
    body_today = (open_ - close).abs()
    body_prev = (close.shift(1) - open_.shift(1)).abs()
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1)) & (body_today > 1.5 * body_prev)
    return ((nh & prior_bull & today_bear & engulf).astype(float).where(rmax_prev.notna(), np.nan)).diff().diff()


def f49_bcco_268_tweezer_top_3_bar_d2(high: pd.Series) -> pd.Series:
    """1 if today's, prior, and 2-bars-ago highs all within 0.5% of each other — 3-bar tweezer top."""
    h1 = (high - high.shift(1)).abs() / high.shift(1)
    h2 = (high - high.shift(2)).abs() / high.shift(2)
    return (((h1 < 0.005) & (h2 < 0.005)).astype(float).where(high.shift(2).notna(), np.nan)).diff().diff()


def f49_bcco_269_long_upper_shadow_3x_body_count_21_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 21 of bars with upper shadow > 3x body — rejection-bar frequency."""
    body = (close - open_).abs()
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    return ((upper > 3.0 * body).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(body.notna(), np.nan)).diff().diff()


def f49_bcco_270_gravestone_doji_count_63_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of gravestone-doji bars — peak-pattern frequency."""
    body_pct = _safe_div((close - open_).abs(), close)
    low_pct = _safe_div(open_ - low, close)
    cond = (body_pct < 0.005) & (low_pct < 0.005)
    return (cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(low.notna(), np.nan)).diff().diff()


def f49_bcco_271_evening_star_full_3bar_pattern_count_252_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of evening-star 3-bar reversal patterns at new 252d highs (bullish, doji, wide-down)."""
    body2 = (close.shift(2) - open_.shift(2))
    rng2 = (high.shift(2) - low.shift(2))
    body1 = (close.shift(1) - open_.shift(1)).abs()
    rng1 = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    rmax2 = high.shift(2).rolling(YDAYS, min_periods=QDAYS).max()
    nh_2 = (high.shift(2) >= rmax2)
    bull_2 = body2 > 0.5 * rng2
    small_1 = body1 < 0.3 * rng1
    mid_2 = (high.shift(2) + low.shift(2)) / 2.0
    bear_now = (close < open_) & (close < mid_2)
    ev = (nh_2 & bull_2 & small_1 & bear_now).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(rng1.notna() & rmax2.notna(), np.nan)).diff().diff()


def f49_bcco_272_inverted_hammer_count_63_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of inverted-hammer bars near recent highs (CLV > 0.7 with long upper wick)."""
    body = (close - open_).abs()
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    near_top = _clv(high, low, close) > 0.7
    cond = (upper > 2.0 * body) & near_top
    return (cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(body.notna(), np.nan)).diff().diff()


def f49_bcco_273_three_black_crows_after_new_high_count_63_d2(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of 3-black-crows patterns (3 consecutive bear bars) following any new-252d-high in past 5 bars."""
    bear_3 = (close < open_) & (close.shift(1) < open_.shift(1)) & (close.shift(2) < open_.shift(2))
    nh_5_ago = _new_high_252(high).shift(3).rolling(WDAYS, min_periods=1).max() > 0
    return ((bear_3 & nh_5_ago).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(open_.shift(2).notna(), np.nan)).diff().diff()


def f49_bcco_274_failed_breakout_within_5_count_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where new 252d high was reached 5 bars ago AND close has dropped below that high since."""
    rmax_5 = high.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    nh_5 = (high.shift(WDAYS) >= rmax_5)
    failed = nh_5 & (close < high.shift(WDAYS))
    return (failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(rmax_5.notna(), np.nan)).diff().diff()


def f49_bcco_275_failed_breakout_within_21_count_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 252 of failed-breakout-within-21-bars events."""
    rmax_21 = high.shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).max()
    nh_21 = (high.shift(MDAYS) >= rmax_21)
    failed = nh_21 & (close < high.shift(MDAYS))
    return (failed.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rmax_21.notna(), np.nan)).diff().diff()


def f49_bcco_276_false_new_high_count_63_d2(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where today is new 252d high AND close < open AND close < prior close — false new-high."""
    nh = _new_high_252(high)
    fail = nh & (close < open_) & (close < close.shift(1))
    return (fail.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(nh.notna(), np.nan)).diff().diff()


def f49_bcco_277_false_new_high_count_252_d2(open_: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual false-new-high count."""
    nh = _new_high_252(high)
    fail = nh & (close < open_) & (close < close.shift(1))
    return (fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(nh.notna(), np.nan)).diff().diff()


def f49_bcco_278_failed_rally_count_252_d2(close: pd.Series) -> pd.Series:
    """Count past 252 of bars where 21 bars ago had 5d-rally > 10% AND today's close < close 26 bars ago."""
    rally_21_ago = (close.pct_change(WDAYS).shift(MDAYS) > 0.10)
    return ((rally_21_ago & (close < close.shift(MDAYS + WDAYS))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rally_21_ago.notna(), np.nan)).diff().diff()


def f49_bcco_279_new_high_then_5bar_return_below_neg5pct_count_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 252 of bars where 5d-prior was new 252d high AND today's 5d return < -5%."""
    nh_5 = _new_high_252(high).shift(WDAYS)
    return ((nh_5 & (close.pct_change(WDAYS) < -0.05)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(nh_5.notna(), np.nan)).diff().diff()


def f49_bcco_280_bull_trap_intraday_new_high_close_red_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if intraday high touched 252d max AND close < prior close — bull-trap intraday."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    intraday_nh = (high >= rmax) & (close < close.shift(1))
    return (intraday_nh.astype(float).where(rmax.notna(), np.nan)).diff().diff()


def f49_bcco_281_bull_trap_count_252_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Annual count of bull-trap-intraday events."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bt = (high >= rmax) & (close < close.shift(1))
    return (bt.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rmax.notna(), np.nan)).diff().diff()


def f49_bcco_282_21d_count_new_252d_highs_ge_5_d2(high: pd.Series) -> pd.Series:
    """1 if 5+ new 252d highs in past 21 bars — sustained-breakout regime."""
    cnt = _new_high_252(high).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 5).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f49_bcco_283_21d_count_new_252d_highs_ge_10_d2(high: pd.Series) -> pd.Series:
    """1 if 10+ new 252d highs in past 21 bars — heavy-breakout regime."""
    cnt = _new_high_252(high).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 10).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f49_bcco_284_21d_count_vol_z_over_2_ge_7_d2(volume: pd.Series) -> pd.Series:
    """1 if 7+ bars with vol z>2 in past 21 — heavy-buying regime."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    cnt = (vz > 2.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 7).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f49_bcco_285_21d_count_strong_close_ge_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 14+ bars with CLV > 0.5 in past 21 — sustained-buying-pressure regime."""
    cl = _clv(high, low, close)
    cnt = (cl > 0.5).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 14).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f49_bcco_286_5d_cum_vol_over_63d_5d_avg_vol_d2(volume: pd.Series) -> pd.Series:
    """(5-bar cum vol) / (63d avg of 5-bar cum vol) — relative vol pickup."""
    v5 = volume.rolling(WDAYS, min_periods=2).sum()
    return (_safe_div(v5, v5.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff()


def f49_bcco_287_5d_gap_up_count_ge_3_d2(open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 3+ gap-ups (open > prev close by > 0.5%) in past 5 bars — gap-up cluster."""
    g = _safe_div(open_ - close.shift(1), close.shift(1))
    cnt = (g > 0.005).astype(float).rolling(WDAYS, min_periods=2).sum()
    return ((cnt >= 3).astype(float).where(g.notna(), np.nan)).diff().diff()


def f49_bcco_288_21d_up_gap_2pct_count_ge_5_d2(open_: pd.Series, close: pd.Series) -> pd.Series:
    """1 if 5+ up-gaps > 2% in past 21 bars — frequent strong-gap regime."""
    g = _safe_div(open_ - close.shift(1), close.shift(1))
    cnt = (g > 0.02).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 5).astype(float).where(g.notna(), np.nan)).diff().diff()


def f49_bcco_289_21d_up_bar_fraction_over_70pct_d2(close: pd.Series) -> pd.Series:
    """1 if up-bar count / 21 > 0.7 — extreme bull-bias regime."""
    cnt = (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((_safe_div(cnt, MDAYS) > 0.7).astype(float).where(cnt.notna(), np.nan)).diff().diff()


def f49_bcco_290_21d_max_strong_close_streak_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max of (CLV>0.5 streak) past 21 bars — longest sustained-strong-close streak."""
    cl = _clv(high, low, close)
    s = _streak_true(cl > 0.5)
    return (s.rolling(MDAYS, min_periods=WDAYS).max().where(cl.notna(), np.nan)).diff().diff()


def f49_bcco_291_21d_strong_close_and_new_21d_high_count_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 21 of bars with CLV > 0.5 AND new 21d high — strong-close-on-breakout count."""
    cond = (_clv(high, low, close) > 0.5) & _new_high_21(high)
    return (cond.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(_clv(high, low, close).notna(), np.nan)).diff().diff()


def f49_bcco_292_close_above_vwap21_and_new_252d_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > rolling VWAP21 AND new 252d high — VWAP-trending breakout."""
    return (((close > _rolling_vwap(close, volume, MDAYS)) & _new_high_252(high)).astype(float).where(_rolling_vwap(close, volume, MDAYS).notna(), np.nan)).diff().diff()


def f49_bcco_293_close_above_vwap63_for_21bars_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > VWAP63 for 21 consecutive bars AND new 252d high — sustained VWAP-bull + breakout."""
    vwap63 = _rolling_vwap(close, volume, QDAYS)
    streak = _streak_true(close > vwap63)
    return (((streak >= MDAYS) & _new_high_252(high)).astype(float).where(vwap63.notna(), np.nan)).diff().diff()


def f49_bcco_294_close_minus_vwap63_atr21_over_2_and_new_high_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (close - VWAP63)/ATR21 > 2 AND new 252d high — far above quarterly VWAP at peak."""
    e = _safe_div(close - _rolling_vwap(close, volume, QDAYS), _atr(high, low, close, MDAYS))
    return (((e > 2.0) & _new_high_252(high)).astype(float).where(e.notna(), np.nan)).diff().diff()


def f49_bcco_295_vwap21_above_vwap63_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VWAP21 > VWAP63 (short VWAP > long VWAP, bullish stack) AND new 252d high."""
    return (((_rolling_vwap(close, volume, MDAYS) > _rolling_vwap(close, volume, QDAYS)) & _new_high_252(high)).astype(float).where(_rolling_vwap(close, volume, QDAYS).notna(), np.nan)).diff().diff()


def f49_bcco_296_close_above_avwap_from_21d_low_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close > anchored-VWAP-from-21d-low AND new 252d high — anchored-bullish + breakout."""
    close_arr = close.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    avwap = np.full(close_arr.size, np.nan)
    for t in range(close_arr.size):
        lo = max(0, t - MDAYS + 1)
        w = close_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmin(w))
        k = lo + rel
        sum_pv = np.nansum(pv[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        avwap[t] = sum_pv / sum_v
    avwap_s = pd.Series(avwap, index=close.index)
    return (((close > avwap_s) & _new_high_252(high)).astype(float).where(avwap_s.notna(), np.nan)).diff().diff()


def f49_bcco_297_cumulative_vwap_below_close_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if cumulative VWAP < close (close above cum-VWAP) AND new 252d high."""
    cv = _safe_div((close * volume).cumsum(), volume.cumsum())
    return (((cv < close) & _new_high_252(high)).astype(float).where(cv.notna(), np.nan)).diff().diff()


def f49_bcco_298_vwap21_zscore_252_over_2_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VWAP21 z-score (252d) > 2 AND new 252d high — extreme VWAP-level + peak."""
    vwap_z = _rolling_zscore(_rolling_vwap(close, volume, MDAYS), YDAYS, min_periods=QDAYS)
    return (((vwap_z > 2.0) & _new_high_252(high)).astype(float).where(vwap_z.notna(), np.nan)).diff().diff()


def f49_bcco_299_cumulative_vwap_rising_slope_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 21d slope of cumulative VWAP > 0 AND new 252d high — rising long-term VWAP + breakout."""
    cv = _safe_div((close * volume).cumsum(), volume.cumsum())
    sl = _rolling_slope(cv, MDAYS)
    return (((sl > 0) & _new_high_252(high)).astype(float).where(sl.notna(), np.nan)).diff().diff()


def f49_bcco_300_vwap252_at_252d_max_and_new_high_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if VWAP252 equals its trailing 252d max AND new 252d price high — VWAP-peak + price-peak."""
    vwap252 = _rolling_vwap(close, volume, YDAYS)
    return (((vwap252 >= vwap252.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(vwap252.notna(), np.nan)).diff().diff()


# ============================================================
#                         REGISTRY 226-300 (d2)
# ============================================================

_HV = ["high", "volume"]
_HC = ["high", "close"]
_HCV = ["high", "close", "volume"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_HL = ["high", "low"]
_OC = ["open", "close"]
_OHC = ["open", "high", "close"]
_CV = ["close", "volume"]
_OHLC = ["open", "high", "low", "close"]
_OHLCV = ["open", "high", "low", "close", "volume"]

BLOWOFF_CLIMAX_COMPOSITE_D2_REGISTRY_226_300 = {
    "f49_bcco_226_keltner_squeeze_release_with_new_high_d2": {"inputs": _HLC, "func": f49_bcco_226_keltner_squeeze_release_with_new_high_d2},
    "f49_bcco_227_adx_rising_from_below_20_with_new_high_d2": {"inputs": _HLC, "func": f49_bcco_227_adx_rising_from_below_20_with_new_high_d2},
    "f49_bcco_228_atr_pct_close_in_lowest_quartile_then_new_high_d2": {"inputs": _HLC, "func": f49_bcco_228_atr_pct_close_in_lowest_quartile_then_new_high_d2},
    "f49_bcco_229_low_vol_5_days_then_vol_spike_new_high_d2": {"inputs": _HV, "func": f49_bcco_229_low_vol_5_days_then_vol_spike_new_high_d2},
    "f49_bcco_230_donchian20_width_in_lowest_decile_then_new_high_d2": {"inputs": _HLC, "func": f49_bcco_230_donchian20_width_in_lowest_decile_then_new_high_d2},
    "f49_bcco_231_close_pos_in_21d_range_q10_then_jump_to_q95_d2": {"inputs": _HLC, "func": f49_bcco_231_close_pos_in_21d_range_q10_then_jump_to_q95_d2},
    "f49_bcco_232_bb_squeeze_5days_then_close_above_upper_d2": {"inputs": _HC, "func": f49_bcco_232_bb_squeeze_5days_then_close_above_upper_d2},
    "f49_bcco_233_atr_doubled_in_5_bars_with_new_252d_high_d2": {"inputs": _HLC, "func": f49_bcco_233_atr_doubled_in_5_bars_with_new_252d_high_d2},
    "f49_bcco_234_all_4_momentum_ob_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_234_all_4_momentum_ob_and_new_high_d2},
    "f49_bcco_235_all_5_extreme_ob_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_235_all_5_extreme_ob_and_new_high_d2},
    "f49_bcco_236_any_3_of_5_signals_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_236_any_3_of_5_signals_and_new_high_d2},
    "f49_bcco_237_5plus_indicators_climax_dwell_21_d2": {"inputs": _HLCV, "func": f49_bcco_237_5plus_indicators_climax_dwell_21_d2},
    "f49_bcco_238_normalized_momentum_mean_over_80_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_238_normalized_momentum_mean_over_80_and_new_high_d2},
    "f49_bcco_239_rsi_stoch_corr_high_and_new_high_d2": {"inputs": _HLC, "func": f49_bcco_239_rsi_stoch_corr_high_and_new_high_d2},
    "f49_bcco_240_rsi_stoch_mfi_all_above_80_and_atr_z_2_d2": {"inputs": _HLCV, "func": f49_bcco_240_rsi_stoch_mfi_all_above_80_and_atr_z_2_d2},
    "f49_bcco_241_rsi_zscore_252_over_2_5_and_new_252d_high_d2": {"inputs": _HC, "func": f49_bcco_241_rsi_zscore_252_over_2_5_and_new_252d_high_d2},
    "f49_bcco_242_stoch_k_zscore_252_over_2_5_and_new_252d_high_d2": {"inputs": _HLC, "func": f49_bcco_242_stoch_k_zscore_252_over_2_5_and_new_252d_high_d2},
    "f49_bcco_243_all_3_momentum_at_252d_max_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_243_all_3_momentum_at_252d_max_and_new_high_d2},
    "f49_bcco_244_3_consecutive_new_21d_highs_d2": {"inputs": ["high"], "func": f49_bcco_244_3_consecutive_new_21d_highs_d2},
    "f49_bcco_245_3_wide_range_and_3_new_highs_d2": {"inputs": _HLC, "func": f49_bcco_245_3_wide_range_and_3_new_highs_d2},
    "f49_bcco_246_5d_count_vol_z_over_2_ge_3_and_new_252d_high_d2": {"inputs": _HV, "func": f49_bcco_246_5d_count_vol_z_over_2_ge_3_and_new_252d_high_d2},
    "f49_bcco_247_5_consecutive_rsi_over_80_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_247_5_consecutive_rsi_over_80_and_new_high_d2},
    "f49_bcco_248_5_consecutive_tr_over_atr21_and_new_high_d2": {"inputs": _HLC, "func": f49_bcco_248_5_consecutive_tr_over_atr21_and_new_high_d2},
    "f49_bcco_249_5_consecutive_body_over_half_range_and_new_high_d2": {"inputs": _OHLC, "func": f49_bcco_249_5_consecutive_body_over_half_range_and_new_high_d2},
    "f49_bcco_250_rising_rsi_5d_streak_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_250_rising_rsi_5d_streak_and_new_high_d2},
    "f49_bcco_251_3_consecutive_vol_2x_avg_and_new_high_d2": {"inputs": _HV, "func": f49_bcco_251_3_consecutive_vol_2x_avg_and_new_high_d2},
    "f49_bcco_252_5d_cum_vol_zscore_over_5_and_new_high_d2": {"inputs": _HV, "func": f49_bcco_252_5d_cum_vol_zscore_over_5_and_new_high_d2},
    "f49_bcco_253_5d_cum_return_zscore_over_3_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_253_5d_cum_return_zscore_over_3_and_new_high_d2},
    "f49_bcco_254_1bar_return_zscore_over_3_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_254_1bar_return_zscore_over_3_and_new_high_d2},
    "f49_bcco_255_1bar_return_zscore_over_4_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_255_1bar_return_zscore_over_4_and_new_high_d2},
    "f49_bcco_256_5d_sharpe_like_over_3_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_256_5d_sharpe_like_over_3_and_new_high_d2},
    "f49_bcco_257_21d_return_pct_rank_504_over_99_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_257_21d_return_pct_rank_504_over_99_and_new_high_d2},
    "f49_bcco_258_5d_cum_return_over_30pct_d2": {"inputs": ["close"], "func": f49_bcco_258_5d_cum_return_over_30pct_d2},
    "f49_bcco_259_21d_cum_return_at_252d_max_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_259_21d_cum_return_at_252d_max_and_new_high_d2},
    "f49_bcco_260_63d_cum_return_at_252d_max_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_260_63d_cum_return_at_252d_max_and_new_high_d2},
    "f49_bcco_261_1bar_return_pct_rank_252_over_99_and_new_high_d2": {"inputs": _HC, "func": f49_bcco_261_1bar_return_pct_rank_252_over_99_and_new_high_d2},
    "f49_bcco_262_1bar_return_over_4sigma_annual_d2": {"inputs": ["close", "high"], "func": f49_bcco_262_1bar_return_over_4sigma_annual_d2},
    "f49_bcco_263_peak_1d_return_past_21_over_peak_252_ratio_d2": {"inputs": ["close"], "func": f49_bcco_263_peak_1d_return_past_21_over_peak_252_ratio_d2},
    "f49_bcco_264_shooting_star_at_new_252d_high_d2": {"inputs": _OHLC, "func": f49_bcco_264_shooting_star_at_new_252d_high_d2},
    "f49_bcco_265_hanging_man_at_new_252d_high_d2": {"inputs": _OHLC, "func": f49_bcco_265_hanging_man_at_new_252d_high_d2},
    "f49_bcco_266_dark_cloud_after_new_high_gap_then_below_mid_d2": {"inputs": _OHLC, "func": f49_bcco_266_dark_cloud_after_new_high_gap_then_below_mid_d2},
    "f49_bcco_267_bearish_engulfing_after_new_252d_high_strong_d2": {"inputs": _OHLC, "func": f49_bcco_267_bearish_engulfing_after_new_252d_high_strong_d2},
    "f49_bcco_268_tweezer_top_3_bar_d2": {"inputs": ["high"], "func": f49_bcco_268_tweezer_top_3_bar_d2},
    "f49_bcco_269_long_upper_shadow_3x_body_count_21_d2": {"inputs": _OHLC, "func": f49_bcco_269_long_upper_shadow_3x_body_count_21_d2},
    "f49_bcco_270_gravestone_doji_count_63_d2": {"inputs": _OHLC, "func": f49_bcco_270_gravestone_doji_count_63_d2},
    "f49_bcco_271_evening_star_full_3bar_pattern_count_252_d2": {"inputs": _OHLC, "func": f49_bcco_271_evening_star_full_3bar_pattern_count_252_d2},
    "f49_bcco_272_inverted_hammer_count_63_d2": {"inputs": _OHLC, "func": f49_bcco_272_inverted_hammer_count_63_d2},
    "f49_bcco_273_three_black_crows_after_new_high_count_63_d2": {"inputs": _OHLC, "func": f49_bcco_273_three_black_crows_after_new_high_count_63_d2},
    "f49_bcco_274_failed_breakout_within_5_count_63_d2": {"inputs": _HC, "func": f49_bcco_274_failed_breakout_within_5_count_63_d2},
    "f49_bcco_275_failed_breakout_within_21_count_252_d2": {"inputs": _HC, "func": f49_bcco_275_failed_breakout_within_21_count_252_d2},
    "f49_bcco_276_false_new_high_count_63_d2": {"inputs": _OHC, "func": f49_bcco_276_false_new_high_count_63_d2},
    "f49_bcco_277_false_new_high_count_252_d2": {"inputs": _OHC, "func": f49_bcco_277_false_new_high_count_252_d2},
    "f49_bcco_278_failed_rally_count_252_d2": {"inputs": ["close"], "func": f49_bcco_278_failed_rally_count_252_d2},
    "f49_bcco_279_new_high_then_5bar_return_below_neg5pct_count_252_d2": {"inputs": _HC, "func": f49_bcco_279_new_high_then_5bar_return_below_neg5pct_count_252_d2},
    "f49_bcco_280_bull_trap_intraday_new_high_close_red_d2": {"inputs": _HC, "func": f49_bcco_280_bull_trap_intraday_new_high_close_red_d2},
    "f49_bcco_281_bull_trap_count_252_d2": {"inputs": _HC, "func": f49_bcco_281_bull_trap_count_252_d2},
    "f49_bcco_282_21d_count_new_252d_highs_ge_5_d2": {"inputs": ["high"], "func": f49_bcco_282_21d_count_new_252d_highs_ge_5_d2},
    "f49_bcco_283_21d_count_new_252d_highs_ge_10_d2": {"inputs": ["high"], "func": f49_bcco_283_21d_count_new_252d_highs_ge_10_d2},
    "f49_bcco_284_21d_count_vol_z_over_2_ge_7_d2": {"inputs": ["volume"], "func": f49_bcco_284_21d_count_vol_z_over_2_ge_7_d2},
    "f49_bcco_285_21d_count_strong_close_ge_14_d2": {"inputs": _HLC, "func": f49_bcco_285_21d_count_strong_close_ge_14_d2},
    "f49_bcco_286_5d_cum_vol_over_63d_5d_avg_vol_d2": {"inputs": ["volume"], "func": f49_bcco_286_5d_cum_vol_over_63d_5d_avg_vol_d2},
    "f49_bcco_287_5d_gap_up_count_ge_3_d2": {"inputs": _OC, "func": f49_bcco_287_5d_gap_up_count_ge_3_d2},
    "f49_bcco_288_21d_up_gap_2pct_count_ge_5_d2": {"inputs": _OC, "func": f49_bcco_288_21d_up_gap_2pct_count_ge_5_d2},
    "f49_bcco_289_21d_up_bar_fraction_over_70pct_d2": {"inputs": ["close"], "func": f49_bcco_289_21d_up_bar_fraction_over_70pct_d2},
    "f49_bcco_290_21d_max_strong_close_streak_d2": {"inputs": _HLC, "func": f49_bcco_290_21d_max_strong_close_streak_d2},
    "f49_bcco_291_21d_strong_close_and_new_21d_high_count_d2": {"inputs": _HLC, "func": f49_bcco_291_21d_strong_close_and_new_21d_high_count_d2},
    "f49_bcco_292_close_above_vwap21_and_new_252d_high_d2": {"inputs": _HCV, "func": f49_bcco_292_close_above_vwap21_and_new_252d_high_d2},
    "f49_bcco_293_close_above_vwap63_for_21bars_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_293_close_above_vwap63_for_21bars_and_new_high_d2},
    "f49_bcco_294_close_minus_vwap63_atr21_over_2_and_new_high_d2": {"inputs": _HLCV, "func": f49_bcco_294_close_minus_vwap63_atr21_over_2_and_new_high_d2},
    "f49_bcco_295_vwap21_above_vwap63_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_295_vwap21_above_vwap63_and_new_high_d2},
    "f49_bcco_296_close_above_avwap_from_21d_low_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_296_close_above_avwap_from_21d_low_and_new_high_d2},
    "f49_bcco_297_cumulative_vwap_below_close_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_297_cumulative_vwap_below_close_and_new_high_d2},
    "f49_bcco_298_vwap21_zscore_252_over_2_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_298_vwap21_zscore_252_over_2_and_new_high_d2},
    "f49_bcco_299_cumulative_vwap_rising_slope_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_299_cumulative_vwap_rising_slope_and_new_high_d2},
    "f49_bcco_300_vwap252_at_252d_max_and_new_high_d2": {"inputs": _HCV, "func": f49_bcco_300_vwap252_at_252d_max_and_new_high_d2},
}
