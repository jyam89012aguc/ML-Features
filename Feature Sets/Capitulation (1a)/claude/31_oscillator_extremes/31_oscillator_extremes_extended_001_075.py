"""
31_oscillator_extremes — Extended Features osc_ext_001-075
Domain: oscillator extreme/oversold readings — deeper variants + new oscillators + confluence
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

New oscillators: TSI (True Strength Index), Elder Force Index, Balance of Power,
Vortex Indicator (negative), Williams Accumulation/Distribution Oscillator.
Deeper variants: z-scores, percentile ranks, time-since-extreme, signal-line crosses,
multi-period rolling-min, and oversold-streak on thinly covered oscillators.
Multi-oscillator confluence: count and weighted agreement scores.
Rate-of-change and acceleration on new oscillators.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _bars_since(cond: pd.Series) -> pd.Series:
    """Number of bars since last True; NaN if never True up to that point."""
    idx = np.arange(len(cond))
    out = np.full(len(cond), np.nan)
    last = -1
    for i, v in enumerate(cond):
        if v:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=cond.index)


# ── Oscillator helpers ────────────────────────────────────────────────────────

def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((close - ll) * 100.0, hh - ll)


def _williams_r(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((hh - close) * -100.0, hh - ll)


def _cci(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    tp = (high + low + close) / 3.0
    tp_mean = _rolling_mean(tp, w)
    mad = tp.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: np.mean(np.abs(x - x.mean())), raw=True
    )
    return _safe_div(tp - tp_mean, 0.015 * mad)


def _mfi(high: pd.Series, low: pd.Series, close: pd.Series,
         volume: pd.Series, w: int) -> pd.Series:
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos_mf = mf.where(tp > tp.shift(1), 0.0)
    neg_mf = mf.where(tp < tp.shift(1), 0.0)
    pos_sum = _rolling_sum(pos_mf, w)
    neg_sum = _rolling_sum(neg_mf, w)
    mfr = _safe_div(pos_sum, neg_sum)
    return 100.0 - _safe_div(100.0, 1.0 + mfr)


def _stoch_rsi(close: pd.Series, rsi_w: int, stoch_w: int) -> pd.Series:
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    avg_loss = loss.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    rs = _safe_div(avg_gain, avg_loss)
    rsi = 100.0 - _safe_div(100.0, 1.0 + rs)
    rsi_min = _rolling_min(rsi, stoch_w)
    rsi_max = _rolling_max(rsi, stoch_w)
    return _safe_div((rsi - rsi_min) * 100.0, rsi_max - rsi_min)


def _ultimate_osc(high: pd.Series, low: pd.Series, close: pd.Series,
                  w1: int = 7, w2: int = 14, w3: int = 28) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_close).abs(),
                    (low - prev_close).abs()], axis=1).max(axis=1)
    bp = close - pd.concat([low, prev_close], axis=1).min(axis=1)
    avg1 = _safe_div(_rolling_sum(bp, w1), _rolling_sum(tr, w1))
    avg2 = _safe_div(_rolling_sum(bp, w2), _rolling_sum(tr, w2))
    avg3 = _safe_div(_rolling_sum(bp, w3), _rolling_sum(tr, w3))
    return (4.0 * avg1 + 2.0 * avg2 + avg3) / 7.0 * 100.0


def _cmo(close: pd.Series, n: int) -> pd.Series:
    delta = close.diff(1)
    up = delta.clip(lower=0.0)
    dn = (-delta).clip(lower=0.0)
    return _safe_div(100.0 * (_rolling_sum(up, n) - _rolling_sum(dn, n)),
                     _rolling_sum(up, n) + _rolling_sum(dn, n))


def _trix(close: pd.Series, n: int) -> pd.Series:
    log_c = np.log(close.replace(0, np.nan))
    ema1 = _ewm_mean(log_c, n)
    ema2 = _ewm_mean(ema1, n)
    ema3 = _ewm_mean(ema2, n)
    return _safe_div(ema3 - ema3.shift(1), ema3.shift(1)) * 100.0


def _fisher_transform(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    rng = (hh - ll).replace(0, np.nan)
    val = (2.0 * ((close - ll) / rng) - 1.0).clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + val) / (1.0 - val))


def _ppo(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    return _safe_div((ema_f - ema_s), ema_s) * 100.0


def _kst(close: pd.Series) -> pd.Series:
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    r1 = _rolling_mean(_roc(close, 10), 10)
    r2 = _rolling_mean(_roc(close, 15), 10)
    r3 = _rolling_mean(_roc(close, 20), 10)
    r4 = _rolling_mean(_roc(close, 30), 15)
    return r1 * 1.0 + r2 * 2.0 + r3 * 3.0 + r4 * 4.0


def _coppock(close: pd.Series) -> pd.Series:
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    combined = _roc(close, 14) + _roc(close, 11)
    w = 10
    def _wma(x):
        if len(x) < w // 2:
            return np.nan
        wts = np.arange(1, len(x) + 1, dtype=float)
        return float(np.dot(x, wts) / wts.sum())
    return combined.rolling(w, min_periods=max(1, w // 2)).apply(_wma, raw=True)


def _smi(high: pd.Series, low: pd.Series, close: pd.Series, n: int,
         smooth1: int = 3, smooth2: int = 3) -> pd.Series:
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    midpoint = (hh + ll) / 2.0
    diff = close - midpoint
    half_range = (hh - ll) / 2.0
    diff_sm = _ewm_mean(_ewm_mean(diff, smooth1), smooth2)
    range_sm = _ewm_mean(_ewm_mean(half_range, smooth1), smooth2)
    return _safe_div(diff_sm, range_sm) * 100.0


def _schaff_trend_cycle(close: pd.Series, fast: int = 23, slow: int = 50,
                        cycle: int = 10) -> pd.Series:
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    macd = ema_f - ema_s
    m_min = _rolling_min(macd, cycle)
    m_max = _rolling_max(macd, cycle)
    stoch1 = _safe_div((macd - m_min) * 100.0, m_max - m_min)
    f1 = _ewm_mean(stoch1, 2)
    f1_min = _rolling_min(f1, cycle)
    f1_max = _rolling_max(f1, cycle)
    stoch2 = _safe_div((f1 - f1_min) * 100.0, f1_max - f1_min)
    return _ewm_mean(stoch2, 2)


def _klinger(high: pd.Series, low: pd.Series, close: pd.Series,
             volume: pd.Series) -> pd.Series:
    tp = high + low + close
    trend = pd.Series(np.where(tp > tp.shift(1), 1.0, -1.0), index=close.index)
    dm = high - low
    sv = volume * trend * 2.0 * _safe_div(dm, (high - low).replace(0, np.nan))
    return _ewm_mean(sv, 34) - _ewm_mean(sv, 55)


def _rvi(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series,
         n: int = 10) -> pd.Series:
    num = close - open_
    den = high - low
    def _sym4(s: pd.Series) -> pd.Series:
        return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0
    ratio = _safe_div(_sym4(num), _sym4(den).replace(0, np.nan))
    return _rolling_mean(ratio, n)


# ── NEW oscillator helpers ────────────────────────────────────────────────────

def _tsi(close: pd.Series, r: int = 25, s: int = 13) -> pd.Series:
    """True Strength Index: double-smoothed price change / double-smoothed abs change."""
    delta = close.diff(1)
    ds1 = _ewm_mean(delta, r)
    ds2 = _ewm_mean(ds1, s)
    abs_ds1 = _ewm_mean(delta.abs(), r)
    abs_ds2 = _ewm_mean(abs_ds1, s)
    return _safe_div(ds2, abs_ds2) * 100.0


def _elder_force_index(close: pd.Series, volume: pd.Series, n: int = 13) -> pd.Series:
    """Elder Force Index: EMA of (close_change * volume)."""
    raw = close.diff(1) * volume
    return _ewm_mean(raw, n)


def _balance_of_power(open_: pd.Series, high: pd.Series, low: pd.Series,
                      close: pd.Series, n: int = 14) -> pd.Series:
    """Balance of Power: SMA((close - open)/(high - low), n)."""
    raw = _safe_div(close - open_, (high - low).replace(0, np.nan))
    return _rolling_mean(raw, n)


def _vortex_neg(high: pd.Series, low: pd.Series, close: pd.Series,
                n: int = 14) -> pd.Series:
    """Vortex Indicator negative line: sum(|low - prev_high|) / ATR_sum over n."""
    prev_high = high.shift(1)
    prev_low = low.shift(1)
    prev_close = close.shift(1)
    vm_neg = (low - prev_high).abs()
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return _safe_div(_rolling_sum(vm_neg, n), _rolling_sum(tr, n))


def _vortex_pos(high: pd.Series, low: pd.Series, close: pd.Series,
                n: int = 14) -> pd.Series:
    """Vortex Indicator positive line: sum(|high - prev_low|) / ATR_sum over n."""
    prev_low = low.shift(1)
    prev_close = close.shift(1)
    vm_pos = (high - prev_low).abs()
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return _safe_div(_rolling_sum(vm_pos, n), _rolling_sum(tr, n))


def _williams_ad(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams Accumulation/Distribution: cumulative buying/selling pressure."""
    prev_close = close.shift(1)
    true_range_high = pd.concat([high, prev_close], axis=1).max(axis=1)
    true_range_low = pd.concat([low, prev_close], axis=1).min(axis=1)
    ad = pd.Series(0.0, index=close.index)
    cond_up = close > prev_close
    cond_dn = close < prev_close
    ad = pd.Series(
        np.where(cond_up, close - true_range_low,
                 np.where(cond_dn, close - true_range_high, 0.0)),
        index=close.index
    )
    return ad.cumsum()


# ── Feature functions osc_ext_001 – osc_ext_075 ──────────────────────────────

# --- Group A (001-012): True Strength Index (TSI) — fully new oscillator ---

def osc_ext_001_tsi_25_13_raw(close: pd.Series) -> pd.Series:
    """TSI (r=25, s=13) raw value; below -25 = oversold zone."""
    return _tsi(close, 25, 13)


def osc_ext_002_tsi_25_13_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: TSI (25,13) < -25 (oversold)."""
    return (_tsi(close, 25, 13) < -25.0).astype(float)


def osc_ext_003_tsi_25_13_extreme_flag(close: pd.Series) -> pd.Series:
    """Binary flag: TSI (25,13) < -50 (extreme oversold)."""
    return (_tsi(close, 25, 13) < -50.0).astype(float)


def osc_ext_004_tsi_25_13_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of TSI (25,13) below -25 threshold."""
    return (_tsi(close, 25, 13) + 25.0).clip(upper=0.0).abs()


def osc_ext_005_tsi_25_13_signal_line(close: pd.Series) -> pd.Series:
    """TSI (25,13) signal line: 7-period EMA of TSI."""
    return _ewm_mean(_tsi(close, 25, 13), 7)


def osc_ext_006_tsi_25_13_signal_cross_below(close: pd.Series) -> pd.Series:
    """Flag: TSI crossed below its signal line (bearish cross, 1 on cross day)."""
    tsi = _tsi(close, 25, 13)
    sig = _ewm_mean(tsi, 7)
    above_prev = (tsi.shift(1) >= sig.shift(1))
    below_now = (tsi < sig)
    return (above_prev & below_now).astype(float)


def osc_ext_007_tsi_25_13_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of TSI (25,13)."""
    return _rolling_min(_tsi(close, 25, 13), _TD_MON)


def osc_ext_008_tsi_25_13_min_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of TSI (25,13)."""
    return _rolling_min(_tsi(close, 25, 13), _TD_QTR)


def osc_ext_009_tsi_25_13_consec_oversold(close: pd.Series) -> pd.Series:
    """Consecutive days with TSI (25,13) < -25."""
    return _consec_streak(_tsi(close, 25, 13) < -25.0)


def osc_ext_010_tsi_25_13_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of TSI (25,13) in trailing 252 days."""
    return _tsi(close, 25, 13).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_ext_011_tsi_25_13_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of TSI (25,13) over trailing 252 days."""
    t = _tsi(close, 25, 13)
    return _safe_div(t - _rolling_mean(t, _TD_YEAR), _rolling_std(t, _TD_YEAR))


def osc_ext_012_tsi_25_13_bars_since_extreme(close: pd.Series) -> pd.Series:
    """Bars since TSI (25,13) last was < -50 (time since extreme oversold)."""
    return _bars_since(_tsi(close, 25, 13) < -50.0)


# --- Group B (013-020): Elder Force Index — fully new oscillator ---

def osc_ext_013_efi_13_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder Force Index (13-period EMA) raw value; negative = bearish pressure."""
    return _elder_force_index(close, volume, 13)


def osc_ext_014_efi_13_negative_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: EFI (13-period) < 0 (bearish)."""
    return (_elder_force_index(close, volume, 13) < 0.0).astype(float)


def osc_ext_015_efi_13_consec_negative(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with EFI (13-period) < 0."""
    return _consec_streak(_elder_force_index(close, volume, 13) < 0.0)


def osc_ext_016_efi_13_min_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of EFI (13-period)."""
    return _rolling_min(_elder_force_index(close, volume, 13), _TD_MON)


def osc_ext_017_efi_13_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of EFI (13-period) over trailing 252 days."""
    e = _elder_force_index(close, volume, 13)
    return _safe_div(e - _rolling_mean(e, _TD_YEAR), _rolling_std(e, _TD_YEAR))


def osc_ext_018_efi_2_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder Force Index (2-period EMA) — short-term selling pressure."""
    return _elder_force_index(close, volume, 2)


def osc_ext_019_efi_2_negative_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: EFI (2-period) < 0."""
    return (_elder_force_index(close, volume, 2) < 0.0).astype(float)


def osc_ext_020_efi_13_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of EFI (13-period) in trailing 252 days."""
    return _elder_force_index(close, volume, 13).rolling(
        _TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (021-027): Balance of Power — fully new oscillator ---

def osc_ext_021_bop_14_raw(open_: pd.Series, high: pd.Series,
                            low: pd.Series, close: pd.Series) -> pd.Series:
    """Balance of Power (14-day SMA) raw; negative = sellers dominating."""
    return _balance_of_power(open_, high, low, close, 14)


def osc_ext_022_bop_14_negative_flag(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: BOP (14-day) < 0 (net selling pressure)."""
    return (_balance_of_power(open_, high, low, close, 14) < 0.0).astype(float)


def osc_ext_023_bop_14_extreme_neg_flag(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: BOP (14-day) < -0.5 (extreme selling dominance)."""
    return (_balance_of_power(open_, high, low, close, 14) < -0.5).astype(float)


def osc_ext_024_bop_14_min_21d(open_: pd.Series, high: pd.Series,
                                low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of BOP (14-day)."""
    return _rolling_min(_balance_of_power(open_, high, low, close, 14), _TD_MON)


def osc_ext_025_bop_14_consec_negative(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with BOP (14-day) < 0."""
    return _consec_streak(_balance_of_power(open_, high, low, close, 14) < 0.0)


def osc_ext_026_bop_14_zscore_252d(open_: pd.Series, high: pd.Series,
                                    low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of BOP (14-day) over trailing 252 days."""
    b = _balance_of_power(open_, high, low, close, 14)
    return _safe_div(b - _rolling_mean(b, _TD_YEAR), _rolling_std(b, _TD_YEAR))


def osc_ext_027_bop_5_raw(open_: pd.Series, high: pd.Series,
                           low: pd.Series, close: pd.Series) -> pd.Series:
    """Balance of Power (5-day SMA) — short-term selling pressure."""
    return _balance_of_power(open_, high, low, close, 5)


# --- Group D (028-034): Vortex Indicator Negative — fully new oscillator ---

def osc_ext_028_vortex_neg_14_raw(high: pd.Series, low: pd.Series,
                                   close: pd.Series) -> pd.Series:
    """Vortex Indicator negative line VI- (14-period); high = downtrend strength."""
    return _vortex_neg(high, low, close, 14)


def osc_ext_029_vortex_neg_14_extreme_flag(high: pd.Series, low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """Binary flag: VI- (14) > 1.2 (strong downtrend / oversold pressure)."""
    return (_vortex_neg(high, low, close, 14) > 1.2).astype(float)


def osc_ext_030_vortex_neg_minus_pos_14(high: pd.Series, low: pd.Series,
                                         close: pd.Series) -> pd.Series:
    """VI- minus VI+ (14-period): positive = downtrend dominating."""
    return _vortex_neg(high, low, close, 14) - _vortex_pos(high, low, close, 14)


def osc_ext_031_vortex_neg_gt_pos_flag(high: pd.Series, low: pd.Series,
                                        close: pd.Series) -> pd.Series:
    """Binary flag: VI- > VI+ (14-period) — downtrend momentum dominating."""
    return (_vortex_neg(high, low, close, 14) > _vortex_pos(high, low, close, 14)).astype(float)


def osc_ext_032_vortex_neg_14_consec_above1(high: pd.Series, low: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """Consecutive days with VI- (14) > 1.0."""
    return _consec_streak(_vortex_neg(high, low, close, 14) > 1.0)


def osc_ext_033_vortex_neg_14_max_21d(high: pd.Series, low: pd.Series,
                                       close: pd.Series) -> pd.Series:
    """Rolling 21-day maximum of VI- (14-period) — peak downtrend in past month."""
    return _rolling_max(_vortex_neg(high, low, close, 14), _TD_MON)


def osc_ext_034_vortex_neg_14_zscore_252d(high: pd.Series, low: pd.Series,
                                           close: pd.Series) -> pd.Series:
    """Z-score of VI- (14) over trailing 252 days."""
    v = _vortex_neg(high, low, close, 14)
    return _safe_div(v - _rolling_mean(v, _TD_YEAR), _rolling_std(v, _TD_YEAR))


# --- Group E (035-040): Williams A/D Oscillator — fully new oscillator ---

def osc_ext_035_williams_ad_roc_21d(high: pd.Series, low: pd.Series,
                                     close: pd.Series) -> pd.Series:
    """Williams A/D 21-day rate of change — negative = accumulation eroding."""
    wad = _williams_ad(high, low, close)
    return _safe_div(wad - wad.shift(_TD_MON), wad.shift(_TD_MON).abs() + _EPS) * 100.0


def osc_ext_036_williams_ad_negative_roc_flag(high: pd.Series, low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """Flag: Williams A/D 21-day ROC < 0 (distribution phase)."""
    wad = _williams_ad(high, low, close)
    roc = _safe_div(wad - wad.shift(_TD_MON), wad.shift(_TD_MON).abs() + _EPS) * 100.0
    return (roc < 0.0).astype(float)


def osc_ext_037_williams_ad_5d_diff(high: pd.Series, low: pd.Series,
                                     close: pd.Series) -> pd.Series:
    """5-day diff of Williams A/D — short-term flow direction."""
    return _williams_ad(high, low, close).diff(_TD_WEEK)


def osc_ext_038_williams_ad_zscore_252d(high: pd.Series, low: pd.Series,
                                         close: pd.Series) -> pd.Series:
    """Z-score of Williams A/D 5-day diff over trailing 252 days."""
    wad5 = _williams_ad(high, low, close).diff(_TD_WEEK)
    return _safe_div(wad5 - _rolling_mean(wad5, _TD_YEAR), _rolling_std(wad5, _TD_YEAR))


def osc_ext_039_williams_ad_consec_negative_flow(high: pd.Series, low: pd.Series,
                                                   close: pd.Series) -> pd.Series:
    """Consecutive days with Williams A/D daily increment < 0 (distribution)."""
    wad_daily = _williams_ad(high, low, close).diff(1)
    return _consec_streak(wad_daily < 0.0)


def osc_ext_040_williams_ad_neg_flow_count_21d(high: pd.Series, low: pd.Series,
                                                close: pd.Series) -> pd.Series:
    """Count of days with negative Williams A/D daily flow in trailing 21 days."""
    wad_daily = _williams_ad(high, low, close).diff(1)
    return _rolling_count_true(wad_daily < 0.0, _TD_MON)


# --- Group F (041-048): Deeper CMO/TRIX/Fisher/Schaff variants ---

def osc_ext_041_cmo_14_extreme_flag(close: pd.Series) -> pd.Series:
    """Binary flag: CMO (14-day) < -70 (extreme capitulation-level reading)."""
    return (_cmo(close, 14) < -70.0).astype(float)


def osc_ext_042_cmo_14_min_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of CMO (14-day) — worst quarterly reading."""
    return _rolling_min(_cmo(close, 14), _TD_QTR)


def osc_ext_043_cmo_14_bars_since_extreme(close: pd.Series) -> pd.Series:
    """Bars since CMO (14-day) last < -50 (time since extreme oversold)."""
    return _bars_since(_cmo(close, 14) < -50.0)


def osc_ext_044_trix_14_extreme_neg_flag(close: pd.Series) -> pd.Series:
    """Binary flag: TRIX (14) < -0.5 (extreme negative — deep bearish triple EMA)."""
    return (_trix(close, 14) < -0.5).astype(float)


def osc_ext_045_trix_14_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of TRIX (14) over trailing 252 days."""
    t = _trix(close, 14)
    return _safe_div(t - _rolling_mean(t, _TD_YEAR), _rolling_std(t, _TD_YEAR))


def osc_ext_046_trix_14_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of TRIX (14) in trailing 252 days."""
    return _trix(close, 14).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_ext_047_fisher_10_zscore_252d(high: pd.Series, low: pd.Series,
                                       close: pd.Series) -> pd.Series:
    """Z-score of Fisher Transform (10-day) over trailing 252 days."""
    f = _fisher_transform(high, low, close, 10)
    return _safe_div(f - _rolling_mean(f, _TD_YEAR), _rolling_std(f, _TD_YEAR))


def osc_ext_048_schaff_extreme_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Schaff Trend Cycle < 10 (extreme oversold reading)."""
    return (_schaff_trend_cycle(close) < 10.0).astype(float)


# --- Group G (049-055): Deeper PPO/KST/Coppock/SMI/Klinger/RVI variants ---

def osc_ext_049_ppo_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of PPO (12/26) over trailing 252 days."""
    p = _ppo(close)
    return _safe_div(p - _rolling_mean(p, _TD_YEAR), _rolling_std(p, _TD_YEAR))


def osc_ext_050_ppo_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of PPO (12/26) in trailing 252 days."""
    return _ppo(close).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_ext_051_kst_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of KST over trailing 252 days."""
    k = _kst(close)
    return _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))


def osc_ext_052_kst_bars_since_below_signal(close: pd.Series) -> pd.Series:
    """Bars since KST crossed below its 9-period SMA signal (bearish cross)."""
    k = _kst(close)
    sig = _rolling_mean(k, 9)
    cross_below = (k.shift(1) >= sig.shift(1)) & (k < sig)
    return _bars_since(cross_below)


def osc_ext_053_coppock_min_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of Coppock Curve."""
    return _rolling_min(_coppock(close), _TD_QTR)


def osc_ext_054_coppock_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Coppock Curve over trailing 252 days."""
    c = _coppock(close)
    return _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))


def osc_ext_055_smi_14_zscore_252d(high: pd.Series, low: pd.Series,
                                    close: pd.Series) -> pd.Series:
    """Z-score of SMI (14-day) over trailing 252 days."""
    s = _smi(high, low, close, 14)
    return _safe_div(s - _rolling_mean(s, _TD_YEAR), _rolling_std(s, _TD_YEAR))


# --- Group H (056-061): Deeper Klinger/RVI/Schaff variants ---

def osc_ext_056_klinger_signal_line(high: pd.Series, low: pd.Series,
                                     close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator signal line: 13-period EMA of KVO."""
    return _ewm_mean(_klinger(high, low, close, volume), 13)


def osc_ext_057_klinger_signal_cross_below(high: pd.Series, low: pd.Series,
                                            close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: KVO crossed below its 13-period signal (bearish cross)."""
    kvo = _klinger(high, low, close, volume)
    sig = _ewm_mean(kvo, 13)
    return ((kvo.shift(1) >= sig.shift(1)) & (kvo < sig)).astype(float)


def osc_ext_058_klinger_consec_below_signal(high: pd.Series, low: pd.Series,
                                             close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with KVO below its 13-period signal line."""
    kvo = _klinger(high, low, close, volume)
    sig = _ewm_mean(kvo, 13)
    return _consec_streak(kvo < sig)


def osc_ext_059_rvi_oversold_flag(open_: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: RVI (10-period) < 0 (negative vigor — sellers dominating)."""
    return (_rvi(open_, high, low, close, 10) < 0.0).astype(float)


def osc_ext_060_rvi_signal_cross_below(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: RVI crossed below its 4-bar symmetric signal (bearish cross)."""
    r = _rvi(open_, high, low, close, 10)
    # Standard RVI signal = symmetric 4-bar weighted sum of RVI
    sig = (r + 2.0 * r.shift(1) + 2.0 * r.shift(2) + r.shift(3)) / 6.0
    return ((r.shift(1) >= sig.shift(1)) & (r < sig)).astype(float)


def osc_ext_061_schaff_consec_oversold(close: pd.Series) -> pd.Series:
    """Consecutive days with Schaff Trend Cycle < 25 (oversold streak)."""
    return _consec_streak(_schaff_trend_cycle(close) < 25.0)


# --- Group I (062-068): Multi-oscillator confluence & agreement scores ---

def osc_ext_062_multi_osc_count_oversold_6panel(
        high: pd.Series, low: pd.Series, close: pd.Series,
        volume: pd.Series) -> pd.Series:
    """Count of 6 oscillators simultaneously oversold: %K<20, WR<-80,
    CCI<-100, MFI<20, StochRSI<20, UltOsc<30 (0-6 scale)."""
    s1 = (_stoch_k(high, low, close, 14) < 20.0).astype(int)
    s2 = (_williams_r(high, low, close, 14) < -80.0).astype(int)
    s3 = (_cci(high, low, close, 14) < -100.0).astype(int)
    s4 = (_mfi(high, low, close, volume, 14) < 20.0).astype(int)
    s5 = (_stoch_rsi(close, 14, 14) < 20.0).astype(int)
    s6 = (_ultimate_osc(high, low, close) < 30.0).astype(int)
    return (s1 + s2 + s3 + s4 + s5 + s6).astype(float)


def osc_ext_063_multi_osc_count_oversold_new3(
        close: pd.Series, volume: pd.Series,
        open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 3 new oscillators in bearish zone: TSI<-25, EFI<0, BOP<0 (0-3)."""
    s1 = (_tsi(close, 25, 13) < -25.0).astype(int)
    s2 = (_elder_force_index(close, volume, 13) < 0.0).astype(int)
    s3 = (_balance_of_power(open_, high, low, close, 14) < 0.0).astype(int)
    return (s1 + s2 + s3).astype(float)


def osc_ext_064_multi_osc_extreme_all4_flag(
        high: pd.Series, low: pd.Series,
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: all 4 momentum oscillators at extremes simultaneously
    (CMO<-50, TRIX<0, PPO<0, KST<0)."""
    s1 = _cmo(close, 14) < -50.0
    s2 = _trix(close, 14) < 0.0
    s3 = _ppo(close) < 0.0
    s4 = _kst(close) < 0.0
    return (s1 & s2 & s3 & s4).astype(float)


def osc_ext_065_multi_osc_weighted_oversold_score(
        high: pd.Series, low: pd.Series,
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Weighted oversold score across 8 oscillators (0-8 scale).
    %K, WR, CCI, MFI each weight 1; CMO, TRIX, PPO, KST each weight 1."""
    s1 = (_stoch_k(high, low, close, 14) < 20.0).astype(float)
    s2 = (_williams_r(high, low, close, 14) < -80.0).astype(float)
    s3 = (_cci(high, low, close, 14) < -100.0).astype(float)
    s4 = (_mfi(high, low, close, volume, 14) < 20.0).astype(float)
    s5 = (_cmo(close, 14) < -50.0).astype(float)
    s6 = (_trix(close, 14) < 0.0).astype(float)
    s7 = (_ppo(close) < 0.0).astype(float)
    s8 = (_kst(close) < 0.0).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8


def osc_ext_066_multi_osc_all_bearish_10panel(
        high: pd.Series, low: pd.Series,
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 10-oscillator panel all in bearish territory (0-10).
    Stoch%K, WR, CCI, MFI, StochRSI, CMO, TRIX, PPO, KST, Coppock."""
    s1 = (_stoch_k(high, low, close, 14) < 20.0).astype(int)
    s2 = (_williams_r(high, low, close, 14) < -80.0).astype(int)
    s3 = (_cci(high, low, close, 14) < -100.0).astype(int)
    s4 = (_mfi(high, low, close, volume, 14) < 20.0).astype(int)
    s5 = (_stoch_rsi(close, 14, 14) < 20.0).astype(int)
    s6 = (_cmo(close, 14) < -50.0).astype(int)
    s7 = (_trix(close, 14) < 0.0).astype(int)
    s8 = (_ppo(close) < 0.0).astype(int)
    s9 = (_kst(close) < 0.0).astype(int)
    s10 = (_coppock(close) < 0.0).astype(int)
    return (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10).astype(float)


def osc_ext_067_multi_osc_all10_count_21d_max(
        high: pd.Series, low: pd.Series,
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day maximum of the 10-oscillator bearish count (peak confluence)."""
    count = osc_ext_066_multi_osc_all_bearish_10panel(high, low, close, volume)
    return _rolling_max(count, _TD_MON)


def osc_ext_068_confluence_tsi_bop_vortex(
        high: pd.Series, low: pd.Series,
        close: pd.Series, volume: pd.Series,
        open_: pd.Series) -> pd.Series:
    """Count of 3 new oscillators oversold simultaneously: TSI<-25, BOP<0, VI->VI+ (0-3)."""
    s1 = (_tsi(close, 25, 13) < -25.0).astype(int)
    s2 = (_balance_of_power(open_, high, low, close, 14) < 0.0).astype(int)
    s3 = (_vortex_neg(high, low, close, 14) > _vortex_pos(high, low, close, 14)).astype(int)
    return (s1 + s2 + s3).astype(float)


# --- Group J (069-075): ROC & acceleration variants on new oscillators ---

def osc_ext_069_tsi_25_13_5d_roc(close: pd.Series) -> pd.Series:
    """5-day rate of change of TSI (25,13) — velocity of true strength."""
    return _tsi(close, 25, 13).diff(_TD_WEEK)


def osc_ext_070_tsi_25_13_21d_roc(close: pd.Series) -> pd.Series:
    """21-day rate of change of TSI (25,13) — monthly velocity."""
    return _tsi(close, 25, 13).diff(_TD_MON)


def osc_ext_071_efi_13_5d_roc(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate of change of EFI (13-period) — velocity of force index."""
    return _elder_force_index(close, volume, 13).diff(_TD_WEEK)


def osc_ext_072_bop_14_5d_roc(open_: pd.Series, high: pd.Series,
                                low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rate of change of BOP (14-day) — velocity of balance of power."""
    return _balance_of_power(open_, high, low, close, 14).diff(_TD_WEEK)


def osc_ext_073_vortex_neg_minus_pos_5d_roc(high: pd.Series, low: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """5-day ROC of (VI- - VI+) — acceleration of downtrend dominance."""
    spread = _vortex_neg(high, low, close, 14) - _vortex_pos(high, low, close, 14)
    return spread.diff(_TD_WEEK)


def osc_ext_074_tsi_25_13_5d_roc_5d_roc(close: pd.Series) -> pd.Series:
    """Second 5-day diff of TSI (25,13) — acceleration of true strength velocity."""
    vel = _tsi(close, 25, 13).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_ext_075_efi_13_5d_roc_5d_roc(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EFI (13-period) — acceleration of force index velocity."""
    vel = _elder_force_index(close, volume, 13).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_EXTENDED_REGISTRY_001_075 = {
    "osc_ext_001_tsi_25_13_raw": {
        "inputs": ["close"], "func": osc_ext_001_tsi_25_13_raw},
    "osc_ext_002_tsi_25_13_oversold_flag": {
        "inputs": ["close"], "func": osc_ext_002_tsi_25_13_oversold_flag},
    "osc_ext_003_tsi_25_13_extreme_flag": {
        "inputs": ["close"], "func": osc_ext_003_tsi_25_13_extreme_flag},
    "osc_ext_004_tsi_25_13_depth_below25": {
        "inputs": ["close"], "func": osc_ext_004_tsi_25_13_depth_below25},
    "osc_ext_005_tsi_25_13_signal_line": {
        "inputs": ["close"], "func": osc_ext_005_tsi_25_13_signal_line},
    "osc_ext_006_tsi_25_13_signal_cross_below": {
        "inputs": ["close"], "func": osc_ext_006_tsi_25_13_signal_cross_below},
    "osc_ext_007_tsi_25_13_min_21d": {
        "inputs": ["close"], "func": osc_ext_007_tsi_25_13_min_21d},
    "osc_ext_008_tsi_25_13_min_63d": {
        "inputs": ["close"], "func": osc_ext_008_tsi_25_13_min_63d},
    "osc_ext_009_tsi_25_13_consec_oversold": {
        "inputs": ["close"], "func": osc_ext_009_tsi_25_13_consec_oversold},
    "osc_ext_010_tsi_25_13_pct_rank_252d": {
        "inputs": ["close"], "func": osc_ext_010_tsi_25_13_pct_rank_252d},
    "osc_ext_011_tsi_25_13_zscore_252d": {
        "inputs": ["close"], "func": osc_ext_011_tsi_25_13_zscore_252d},
    "osc_ext_012_tsi_25_13_bars_since_extreme": {
        "inputs": ["close"], "func": osc_ext_012_tsi_25_13_bars_since_extreme},
    "osc_ext_013_efi_13_raw": {
        "inputs": ["close", "volume"], "func": osc_ext_013_efi_13_raw},
    "osc_ext_014_efi_13_negative_flag": {
        "inputs": ["close", "volume"], "func": osc_ext_014_efi_13_negative_flag},
    "osc_ext_015_efi_13_consec_negative": {
        "inputs": ["close", "volume"], "func": osc_ext_015_efi_13_consec_negative},
    "osc_ext_016_efi_13_min_21d": {
        "inputs": ["close", "volume"], "func": osc_ext_016_efi_13_min_21d},
    "osc_ext_017_efi_13_zscore_252d": {
        "inputs": ["close", "volume"], "func": osc_ext_017_efi_13_zscore_252d},
    "osc_ext_018_efi_2_raw": {
        "inputs": ["close", "volume"], "func": osc_ext_018_efi_2_raw},
    "osc_ext_019_efi_2_negative_flag": {
        "inputs": ["close", "volume"], "func": osc_ext_019_efi_2_negative_flag},
    "osc_ext_020_efi_13_pct_rank_252d": {
        "inputs": ["close", "volume"], "func": osc_ext_020_efi_13_pct_rank_252d},
    "osc_ext_021_bop_14_raw": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_021_bop_14_raw},
    "osc_ext_022_bop_14_negative_flag": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_022_bop_14_negative_flag},
    "osc_ext_023_bop_14_extreme_neg_flag": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_023_bop_14_extreme_neg_flag},
    "osc_ext_024_bop_14_min_21d": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_024_bop_14_min_21d},
    "osc_ext_025_bop_14_consec_negative": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_025_bop_14_consec_negative},
    "osc_ext_026_bop_14_zscore_252d": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_026_bop_14_zscore_252d},
    "osc_ext_027_bop_5_raw": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_027_bop_5_raw},
    "osc_ext_028_vortex_neg_14_raw": {
        "inputs": ["high", "low", "close"], "func": osc_ext_028_vortex_neg_14_raw},
    "osc_ext_029_vortex_neg_14_extreme_flag": {
        "inputs": ["high", "low", "close"], "func": osc_ext_029_vortex_neg_14_extreme_flag},
    "osc_ext_030_vortex_neg_minus_pos_14": {
        "inputs": ["high", "low", "close"], "func": osc_ext_030_vortex_neg_minus_pos_14},
    "osc_ext_031_vortex_neg_gt_pos_flag": {
        "inputs": ["high", "low", "close"], "func": osc_ext_031_vortex_neg_gt_pos_flag},
    "osc_ext_032_vortex_neg_14_consec_above1": {
        "inputs": ["high", "low", "close"], "func": osc_ext_032_vortex_neg_14_consec_above1},
    "osc_ext_033_vortex_neg_14_max_21d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_033_vortex_neg_14_max_21d},
    "osc_ext_034_vortex_neg_14_zscore_252d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_034_vortex_neg_14_zscore_252d},
    "osc_ext_035_williams_ad_roc_21d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_035_williams_ad_roc_21d},
    "osc_ext_036_williams_ad_negative_roc_flag": {
        "inputs": ["high", "low", "close"], "func": osc_ext_036_williams_ad_negative_roc_flag},
    "osc_ext_037_williams_ad_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_ext_037_williams_ad_5d_diff},
    "osc_ext_038_williams_ad_zscore_252d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_038_williams_ad_zscore_252d},
    "osc_ext_039_williams_ad_consec_negative_flow": {
        "inputs": ["high", "low", "close"], "func": osc_ext_039_williams_ad_consec_negative_flow},
    "osc_ext_040_williams_ad_neg_flow_count_21d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_040_williams_ad_neg_flow_count_21d},
    "osc_ext_041_cmo_14_extreme_flag": {
        "inputs": ["close"], "func": osc_ext_041_cmo_14_extreme_flag},
    "osc_ext_042_cmo_14_min_63d": {
        "inputs": ["close"], "func": osc_ext_042_cmo_14_min_63d},
    "osc_ext_043_cmo_14_bars_since_extreme": {
        "inputs": ["close"], "func": osc_ext_043_cmo_14_bars_since_extreme},
    "osc_ext_044_trix_14_extreme_neg_flag": {
        "inputs": ["close"], "func": osc_ext_044_trix_14_extreme_neg_flag},
    "osc_ext_045_trix_14_zscore_252d": {
        "inputs": ["close"], "func": osc_ext_045_trix_14_zscore_252d},
    "osc_ext_046_trix_14_pct_rank_252d": {
        "inputs": ["close"], "func": osc_ext_046_trix_14_pct_rank_252d},
    "osc_ext_047_fisher_10_zscore_252d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_047_fisher_10_zscore_252d},
    "osc_ext_048_schaff_extreme_flag": {
        "inputs": ["close"], "func": osc_ext_048_schaff_extreme_flag},
    "osc_ext_049_ppo_zscore_252d": {
        "inputs": ["close"], "func": osc_ext_049_ppo_zscore_252d},
    "osc_ext_050_ppo_pct_rank_252d": {
        "inputs": ["close"], "func": osc_ext_050_ppo_pct_rank_252d},
    "osc_ext_051_kst_zscore_252d": {
        "inputs": ["close"], "func": osc_ext_051_kst_zscore_252d},
    "osc_ext_052_kst_bars_since_below_signal": {
        "inputs": ["close"], "func": osc_ext_052_kst_bars_since_below_signal},
    "osc_ext_053_coppock_min_63d": {
        "inputs": ["close"], "func": osc_ext_053_coppock_min_63d},
    "osc_ext_054_coppock_zscore_252d": {
        "inputs": ["close"], "func": osc_ext_054_coppock_zscore_252d},
    "osc_ext_055_smi_14_zscore_252d": {
        "inputs": ["high", "low", "close"], "func": osc_ext_055_smi_14_zscore_252d},
    "osc_ext_056_klinger_signal_line": {
        "inputs": ["high", "low", "close", "volume"], "func": osc_ext_056_klinger_signal_line},
    "osc_ext_057_klinger_signal_cross_below": {
        "inputs": ["high", "low", "close", "volume"], "func": osc_ext_057_klinger_signal_cross_below},
    "osc_ext_058_klinger_consec_below_signal": {
        "inputs": ["high", "low", "close", "volume"], "func": osc_ext_058_klinger_consec_below_signal},
    "osc_ext_059_rvi_oversold_flag": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_059_rvi_oversold_flag},
    "osc_ext_060_rvi_signal_cross_below": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_060_rvi_signal_cross_below},
    "osc_ext_061_schaff_consec_oversold": {
        "inputs": ["close"], "func": osc_ext_061_schaff_consec_oversold},
    "osc_ext_062_multi_osc_count_oversold_6panel": {
        "inputs": ["high", "low", "close", "volume"],
        "func": osc_ext_062_multi_osc_count_oversold_6panel},
    "osc_ext_063_multi_osc_count_oversold_new3": {
        "inputs": ["close", "volume", "open", "high", "low"],
        "func": osc_ext_063_multi_osc_count_oversold_new3},
    "osc_ext_064_multi_osc_extreme_all4_flag": {
        "inputs": ["high", "low", "close", "volume"],
        "func": osc_ext_064_multi_osc_extreme_all4_flag},
    "osc_ext_065_multi_osc_weighted_oversold_score": {
        "inputs": ["high", "low", "close", "volume"],
        "func": osc_ext_065_multi_osc_weighted_oversold_score},
    "osc_ext_066_multi_osc_all_bearish_10panel": {
        "inputs": ["high", "low", "close", "volume"],
        "func": osc_ext_066_multi_osc_all_bearish_10panel},
    "osc_ext_067_multi_osc_all10_count_21d_max": {
        "inputs": ["high", "low", "close", "volume"],
        "func": osc_ext_067_multi_osc_all10_count_21d_max},
    "osc_ext_068_confluence_tsi_bop_vortex": {
        "inputs": ["high", "low", "close", "volume", "open"],
        "func": osc_ext_068_confluence_tsi_bop_vortex},
    "osc_ext_069_tsi_25_13_5d_roc": {
        "inputs": ["close"], "func": osc_ext_069_tsi_25_13_5d_roc},
    "osc_ext_070_tsi_25_13_21d_roc": {
        "inputs": ["close"], "func": osc_ext_070_tsi_25_13_21d_roc},
    "osc_ext_071_efi_13_5d_roc": {
        "inputs": ["close", "volume"], "func": osc_ext_071_efi_13_5d_roc},
    "osc_ext_072_bop_14_5d_roc": {
        "inputs": ["open", "high", "low", "close"], "func": osc_ext_072_bop_14_5d_roc},
    "osc_ext_073_vortex_neg_minus_pos_5d_roc": {
        "inputs": ["high", "low", "close"], "func": osc_ext_073_vortex_neg_minus_pos_5d_roc},
    "osc_ext_074_tsi_25_13_5d_roc_5d_roc": {
        "inputs": ["close"], "func": osc_ext_074_tsi_25_13_5d_roc_5d_roc},
    "osc_ext_075_efi_13_5d_roc_5d_roc": {
        "inputs": ["close", "volume"], "func": osc_ext_075_efi_13_5d_roc_5d_roc},
}
