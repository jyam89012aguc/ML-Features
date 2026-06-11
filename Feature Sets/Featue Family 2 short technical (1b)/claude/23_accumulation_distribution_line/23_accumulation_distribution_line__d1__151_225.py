"""accumulation_distribution_line d1 features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. DISTINCT concepts NOT covered:

- Bullish divergence (existing covers heavily bearish-only) and hidden divergences
- Ease of Movement (EMV) - Richard Arms
- Percentage Volume Oscillator (PVO) + signal + histogram + cross events
- Volume oscillator (difference between two volume MAs)
- Multi-indicator flow agreement / consensus / disagreement scores
- Time-decay (EWMA) weighted AD line / volume flows
- Anchored VWAP (anchored to 252d high) + distance metrics
- Volume profile proxies (volume above/below close, HVN/LVN distance)
- ROC velocity of CMF / MFI / Force Index / AD line
- AD line drawdown from peak / trendline break
- Distribution & accumulation WEEK / MONTH (longer-horizon windowed)
- Volume Spread Analysis (VSA): effort vs result, no-demand/no-supply, stopping volume
- Composite distribution/accumulation phase scores + flow regime classifier

Inputs: SEP OHLCV only. PIT-clean: right-anchored, explicit min_periods,
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


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


# ---- family-specific helpers (PIT-clean) ----

def _clv(high, low, close):
    """Close Location Value: ((C-L)-(H-C))/(H-L)."""
    return _safe_div(((close - low) - (high - close)), (high - low))


def _ad_line(high, low, close, volume):
    """Cumulative AD line: sum of CLV * Volume."""
    return (_clv(high, low, close) * volume).cumsum()


def _cmf(high, low, close, volume, n):
    """Chaikin Money Flow over n bars."""
    mfv = _clv(high, low, close) * volume
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     volume.rolling(n, min_periods=max(n // 3, 2)).sum())


def _mfi(high, low, close, volume, n=14):
    """Money Flow Index over n bars."""
    tp = (high + low + close) / 3
    rmf = tp * volume
    pmf = rmf.where(tp > tp.shift(1), 0.0)
    nmf = rmf.where(tp < tp.shift(1), 0.0)
    pmf_n = pmf.rolling(n, min_periods=max(n // 3, 2)).sum()
    nmf_n = nmf.rolling(n, min_periods=max(n // 3, 2)).sum()
    mfr = _safe_div(pmf_n, nmf_n)
    return 100.0 - 100.0 / (1.0 + mfr)


def _force_index(close, volume, n):
    """Force Index EMA-n of (close.diff() * volume)."""
    fi = (close.diff()) * volume
    return fi.ewm(span=n, min_periods=max(n // 3, 2), adjust=False).mean()


def _emv(high, low, volume):
    """Ease of Movement (Arms): ((H+L)/2 - (Hp+Lp)/2) / (Volume / (H-L))."""
    mid = (high + low) / 2.0
    mid_prev = mid.shift(1)
    box_ratio = _safe_div(volume, (high - low))
    return _safe_div(mid - mid_prev, box_ratio)


def _pvo(volume, fast=12, slow=26, signal=9):
    """Percentage Volume Oscillator: 100 * (EMA_fast - EMA_slow) / EMA_slow."""
    ef = volume.ewm(span=fast, min_periods=max(fast // 3, 2), adjust=False).mean()
    es = volume.ewm(span=slow, min_periods=max(slow // 3, 2), adjust=False).mean()
    pvo = _safe_div(100.0 * (ef - es), es)
    sig = pvo.ewm(span=signal, min_periods=max(signal // 3, 2), adjust=False).mean()
    return pvo, sig


def _div_bear_window(price, indicator, n):
    """Bearish divergence: price at new n-bar high BUT indicator value < its prior n-bar max."""
    p_max = price.rolling(n, min_periods=max(n // 3, 2)).max()
    p_at_high = price >= p_max
    ind_prev_max = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).max()
    return (p_at_high & (indicator < ind_prev_max)).astype(float)


def _div_bull_window(price, indicator, n):
    """Bullish divergence: price at new n-bar low BUT indicator > its prior n-bar min."""
    p_min = price.rolling(n, min_periods=max(n // 3, 2)).min()
    p_at_low = price <= p_min
    ind_prev_min = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    return (p_at_low & (indicator > ind_prev_min)).astype(float)


def _hidden_div_bear_window(price, indicator, n):
    """Hidden bearish divergence (continuation): price LOWER high, indicator HIGHER high."""
    p_prev_max = price.shift(1).rolling(n, min_periods=max(n // 3, 2)).max()
    p_lower_h = (price < p_prev_max)
    ind_prev_max = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).max()
    ind_higher_h = (indicator > ind_prev_max)
    return (p_lower_h & ind_higher_h).astype(float)


def _hidden_div_bull_window(price, indicator, n):
    """Hidden bullish divergence: price HIGHER low, indicator LOWER low."""
    p_prev_min = price.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    p_higher_l = (price > p_prev_min)
    ind_prev_min = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    ind_lower_l = (indicator < ind_prev_min)
    return (p_higher_l & ind_lower_l).astype(float)


# ============================================================
# Bucket A — Bullish divergence (mirror of existing bearish coverage) (151-157)
# ============================================================

def f23_adld_151_ad_bullish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bullish AD divergence event (63d): price new 63d low while AD > prior 63d AD min."""
    return _div_bull_window(close, _ad_line(high, low, close, volume), QDAYS)


def f23_adld_152_ad_bullish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bullish AD divergence event (252d)."""
    return _div_bull_window(close, _ad_line(high, low, close, volume), YDAYS)


def f23_adld_153_ad_bullish_div_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bullish AD divergence events in trailing 63d."""
    ev = _div_bull_window(close, _ad_line(high, low, close, volume), QDAYS)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_154_ad_bullish_div_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bullish AD divergence events in trailing 252d."""
    ev = _div_bull_window(close, _ad_line(high, low, close, volume), QDAYS)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f23_adld_155_bars_since_last_ad_bullish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the most recent bullish AD divergence event."""
    ev = _div_bull_window(close, _ad_line(high, low, close, volume), QDAYS).astype(bool)
    return _bars_since(ev)


def f23_adld_156_mfi_bullish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bullish MFI divergence (63d): price new 63d low while MFI14 > prior 63d MFI14 min."""
    return _div_bull_window(close, _mfi(high, low, close, volume, 14), QDAYS)


def f23_adld_157_mfi_bullish_div_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bullish MFI divergence events in 252d."""
    ev = _div_bull_window(close, _mfi(high, low, close, volume, 14), QDAYS)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket B — Hidden divergences (158-163)
# ============================================================

def f23_adld_158_ad_hidden_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish AD divergence (continuation bearish): price lower-high, AD higher-high."""
    return _hidden_div_bear_window(close, _ad_line(high, low, close, volume), QDAYS)


def f23_adld_159_ad_hidden_bullish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bullish AD divergence: price higher-low, AD lower-low."""
    return _hidden_div_bull_window(close, _ad_line(high, low, close, volume), QDAYS)


def f23_adld_160_cmf_hidden_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish CMF21 divergence."""
    return _hidden_div_bear_window(close, _cmf(high, low, close, volume, MDAYS), QDAYS)


def f23_adld_161_mfi_hidden_bullish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bullish MFI14 divergence."""
    return _hidden_div_bull_window(close, _mfi(high, low, close, volume, 14), QDAYS)


def f23_adld_162_force_index_hidden_bearish_div_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden bearish Force Index (ema13) divergence."""
    return _hidden_div_bear_window(close, _force_index(close, volume, 13), QDAYS)


def f23_adld_163_count_hidden_div_events_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total count of hidden-divergence events (AD bearish + AD bullish + CMF bearish + MFI bullish) in 252d."""
    ad = _ad_line(high, low, close, volume)
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14)
    a = _hidden_div_bear_window(close, ad, QDAYS)
    b = _hidden_div_bull_window(close, ad, QDAYS)
    c = _hidden_div_bear_window(close, cmf, QDAYS)
    d = _hidden_div_bull_window(close, mfi, QDAYS)
    return (a + b + c + d).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket C — Ease of Movement (EMV — Arms) (164-170)
# ============================================================

def f23_adld_164_emv_1bar(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Single-bar Ease of Movement: how easily price moved per unit volume."""
    return _emv(high, low, volume)


def f23_adld_165_emv_ema14(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA14 of single-bar EMV — standard Arms smoothing."""
    return _emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean()


def f23_adld_166_emv_ema63(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA63 of EMV — quarterly horizon."""
    return _emv(high, low, volume).ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f23_adld_167_emv_zscore_252(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of EMV-ema14 vs trailing 252d distribution."""
    return _rolling_zscore(_emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean(), YDAYS, min_periods=QDAYS)


def f23_adld_168_emv_above_zero_state(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: EMV-ema14 > 0 (price moving easily UP per unit volume)."""
    return (_emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean() > 0).astype(float)


def f23_adld_169_emv_dwell_below_zero_63(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d where EMV-ema14 < 0 (price moving with difficulty)."""
    return (_emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean() < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f23_adld_170_emv_bearish_div_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish EMV divergence: price new 63d high but EMV-ema14 lower than prior 63d max."""
    return _div_bear_window(close, _emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean(), QDAYS)


# ============================================================
# Bucket D — PVO (Percentage Volume Oscillator) (171-176)
# ============================================================

def f23_adld_171_pvo_12_26(volume: pd.Series) -> pd.Series:
    """Percentage Volume Oscillator (12,26): 100*(EMA12-EMA26)/EMA26 of volume."""
    pvo, _ = _pvo(volume, 12, 26, 9)
    return pvo


def f23_adld_172_pvo_signal(volume: pd.Series) -> pd.Series:
    """9-period EMA signal line of PVO(12,26)."""
    _, sig = _pvo(volume, 12, 26, 9)
    return sig


def f23_adld_173_pvo_histogram(volume: pd.Series) -> pd.Series:
    """PVO minus signal — histogram value."""
    pvo, sig = _pvo(volume, 12, 26, 9)
    return pvo - sig


def f23_adld_174_pvo_zscore_252(volume: pd.Series) -> pd.Series:
    """Z-score of PVO(12,26) vs 252d distribution."""
    pvo, _ = _pvo(volume, 12, 26, 9)
    return _rolling_zscore(pvo, YDAYS, min_periods=QDAYS)


def f23_adld_175_pvo_above_zero_state(volume: pd.Series) -> pd.Series:
    """Indicator: PVO > 0 (short-MA volume above long-MA volume — pickup in volume)."""
    pvo, _ = _pvo(volume, 12, 26, 9)
    return (pvo > 0).astype(float)


def f23_adld_176_pvo_bearish_cross_event(volume: pd.Series) -> pd.Series:
    """Indicator: today PVO crossed below signal line."""
    pvo, sig = _pvo(volume, 12, 26, 9)
    return ((pvo < sig) & (pvo.shift(1) >= sig.shift(1))).astype(float)


# ============================================================
# Bucket E — Volume oscillator (raw diff of MAs) (177-179)
# ============================================================

def f23_adld_177_volume_osc_short_long(volume: pd.Series) -> pd.Series:
    """Volume oscillator: 5d-SMA volume - 21d-SMA volume (raw difference)."""
    return volume.rolling(WDAYS, min_periods=WDAYS).mean() - volume.rolling(MDAYS, min_periods=WDAYS).mean()


def f23_adld_178_volume_osc_zscore_252(volume: pd.Series) -> pd.Series:
    """Z-score of volume oscillator vs 252d distribution."""
    osc = volume.rolling(WDAYS, min_periods=WDAYS).mean() - volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(osc, YDAYS, min_periods=QDAYS)


def f23_adld_179_volume_osc_bearish_cross_event(volume: pd.Series) -> pd.Series:
    """Indicator: volume osc just crossed below zero (volume contraction event)."""
    osc = volume.rolling(WDAYS, min_periods=WDAYS).mean() - volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return ((osc < 0) & (osc.shift(1) >= 0)).astype(float)


# ============================================================
# Bucket F — Multi-indicator flow agreement / consensus (180-187)
# ============================================================

def _flow_indicator_signs(high, low, close, volume):
    """Return DataFrame of sign(value) for CMF21, MFI14 (centered at 50), Force EMA13, EMV EMA14, KVO-line proxy.
    +1 = bullish, -1 = bearish, 0 = neutral."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14) - 50.0
    fi = _force_index(close, volume, 13)
    emv = _emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean()
    # KVO proxy: difference of trend EMAs of (close-diff sign * volume)
    flow = np.sign(close.diff()) * volume
    kvo = flow.ewm(span=34, min_periods=12, adjust=False).mean() - flow.ewm(span=55, min_periods=20, adjust=False).mean()
    parts = pd.concat([
        np.sign(cmf).rename('cmf'),
        np.sign(mfi).rename('mfi'),
        np.sign(fi).rename('fi'),
        np.sign(emv).rename('emv'),
        np.sign(kvo).rename('kvo'),
    ], axis=1)
    return parts


def f23_adld_180_flow_indicator_agreement_score_bearish(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of flow indicators (CMF/MFI/Force/EMV/KVO) currently bearish (sign = -1)."""
    return (_flow_indicator_signs(high, low, close, volume) == -1).sum(axis=1).astype(float)


def f23_adld_181_flow_indicator_agreement_score_bullish(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of flow indicators currently bullish (sign = +1)."""
    return (_flow_indicator_signs(high, low, close, volume) == 1).sum(axis=1).astype(float)


def f23_adld_182_flow_indicator_disagreement_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max - min of normalized z-scored flow indicators across 252d. High = strong disagreement."""
    cmf_z = _rolling_zscore(_cmf(high, low, close, volume, MDAYS), YDAYS, min_periods=QDAYS)
    mfi_z = _rolling_zscore(_mfi(high, low, close, volume, 14), YDAYS, min_periods=QDAYS)
    fi_z = _rolling_zscore(_force_index(close, volume, 13), YDAYS, min_periods=QDAYS)
    df = pd.concat([cmf_z.rename('c'), mfi_z.rename('m'), fi_z.rename('f')], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def f23_adld_183_multi_indicator_OB_count(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {CMF21 > 0.25, MFI14 > 80, EMV-ema14 in top decile 252d} currently OB."""
    cmf_ob = (_cmf(high, low, close, volume, MDAYS) > 0.25).astype(float)
    mfi_ob = (_mfi(high, low, close, volume, 14) > 80).astype(float)
    emv_ema = _emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean()
    emv_z = _rolling_zscore(emv_ema, YDAYS, min_periods=QDAYS)
    emv_ob = (emv_z > 1.28).astype(float)  # ~top decile
    return cmf_ob + mfi_ob + emv_ob


def f23_adld_184_multi_indicator_OS_count(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {CMF21 < -0.25, MFI14 < 20, EMV-ema14 in bottom decile 252d} currently OS."""
    cmf_os = (_cmf(high, low, close, volume, MDAYS) < -0.25).astype(float)
    mfi_os = (_mfi(high, low, close, volume, 14) < 20).astype(float)
    emv_ema = _emv(high, low, volume).ewm(span=14, min_periods=5, adjust=False).mean()
    emv_z = _rolling_zscore(emv_ema, YDAYS, min_periods=QDAYS)
    emv_os = (emv_z < -1.28).astype(float)
    return cmf_os + mfi_os + emv_os


def f23_adld_185_flow_signal_stability_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std dev of bullish agreement score over trailing 63d — low = stable consensus."""
    bullish = (_flow_indicator_signs(high, low, close, volume) == 1).sum(axis=1).astype(float)
    return bullish.rolling(QDAYS, min_periods=MDAYS).std()


def f23_adld_186_flow_signal_persistence_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest run in last 63d where bullish agreement >= 4 (strong consensus)."""
    bullish_strong = ((_flow_indicator_signs(high, low, close, volume) == 1).sum(axis=1) >= 4)
    grp = (~bullish_strong).cumsum()
    streak = bullish_strong.astype(int).groupby(grp).cumsum().astype(float)
    return streak.rolling(QDAYS, min_periods=MDAYS).max()


def f23_adld_187_flow_phase_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Categorical flow phase: 0=accumulation (bullish flows, flat price), 1=markup (bullish flows, rising price),
    2=distribution (bearish flows, flat price), 3=markdown (bearish flows, falling price)."""
    bullish = (_flow_indicator_signs(high, low, close, volume) == 1).sum(axis=1)
    bearish = (_flow_indicator_signs(high, low, close, volume) == -1).sum(axis=1)
    price_slope = close - close.shift(MDAYS)
    flow_bull = bullish > bearish
    rising = price_slope > 0
    n = len(close); out = np.full(n, np.nan)
    fb = flow_bull.to_numpy(); ri = rising.to_numpy()
    for i in range(n):
        if np.isnan(close.iloc[i]) or np.isnan(price_slope.iloc[i]): continue
        if fb[i] and not ri[i]: out[i] = 0
        elif fb[i] and ri[i]: out[i] = 1
        elif (not fb[i]) and not ri[i]: out[i] = 2
        else: out[i] = 3
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket G — Time-decay (EWMA) weighted flows (188-191)
# ============================================================

def f23_adld_188_ewma_weighted_ad_line_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWMA21 of money-flow volume (CLV × Vol) — recency-weighted AD."""
    mfv = _clv(high, low, close) * volume
    return mfv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()


def f23_adld_189_ewma_weighted_ad_line_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWMA63 of money-flow volume."""
    mfv = _clv(high, low, close) * volume
    return mfv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f23_adld_190_recent_vs_baseline_clv_ratio_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Recent (5d) mean CLV / 63d mean CLV — short vs long pressure."""
    clv = _clv(high, low, close)
    return _safe_div(clv.rolling(WDAYS, min_periods=WDAYS).mean(), clv.rolling(QDAYS, min_periods=MDAYS).mean())


def f23_adld_191_half_life_weighted_clv_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWMA of CLV with 30d half-life (alpha = 1 - 0.5^(1/30)) over 252d window."""
    clv = _clv(high, low, close)
    alpha = 1.0 - 0.5 ** (1.0 / 30.0)
    return clv.ewm(alpha=alpha, min_periods=MDAYS, adjust=False).mean()


# ============================================================
# Bucket H — Anchored VWAP + volume profile proxies (192-199)
# ============================================================

def f23_adld_192_anchored_vwap_252d_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWAP anchored to the most recent 252d-high bar. Carried forward until a NEW 252d-high resets the anchor."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_anchor = (high == rmax) & high.notna()
    grp = is_anchor.cumsum()
    tp = (high + low + close) / 3.0
    pv = (tp * volume).groupby(grp).cumsum()
    cv = volume.groupby(grp).cumsum()
    return _safe_div(pv, cv)


def f23_adld_193_price_vs_anchored_vwap_252d_high_log(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance close to anchored VWAP (from 252d high anchor). Negative = below VWAP since peak."""
    avwap = f23_adld_192_anchored_vwap_252d_high(high, low, close, volume)
    return _safe_log(close) - _safe_log(avwap)


def f23_adld_194_price_vs_anchored_vwap_252d_high_atr(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATR-normalized distance close to anchored VWAP from 252d high."""
    avwap = f23_adld_192_anchored_vwap_252d_high(high, low, close, volume)
    return _safe_div(close - avwap, _atr(high, low, close, n=MDAYS))


def f23_adld_195_volume_above_current_close_fraction_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d volume occurring on bars whose close was ABOVE the current close — overhead-supply volume."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - QDAYS + 1)
        if i < start: continue
        c_now = close_arr[i]
        if np.isnan(c_now): continue
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        tot = win_v[m].sum()
        if tot == 0: continue
        above = win_v[m & (win_c > c_now)].sum()
        out[i] = float(above / tot)
    return pd.Series(out, index=close.index)


def f23_adld_196_volume_below_current_close_fraction_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d volume on bars whose close was BELOW current close — buffer volume."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - QDAYS + 1)
        if i < start: continue
        c_now = close_arr[i]
        if np.isnan(c_now): continue
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        tot = win_v[m].sum()
        if tot == 0: continue
        below = win_v[m & (win_c < c_now)].sum()
        out[i] = float(below / tot)
    return pd.Series(out, index=close.index)


def f23_adld_197_high_volume_node_distance_log_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance from close to the highest-volume-bar's close in trailing 63d (HVN proxy)."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - QDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        idx = int(np.nanargmax(win_v))
        hvn = win_c[idx]; c_now = close_arr[i]
        if np.isnan(hvn) or np.isnan(c_now) or hvn <= 0 or c_now <= 0: continue
        out[i] = float(np.log(c_now) - np.log(hvn))
    return pd.Series(out, index=close.index)


def f23_adld_198_low_volume_node_distance_log_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log distance from close to the lowest-volume-bar's close in trailing 63d (LVN proxy)."""
    n = len(close); close_arr = close.to_numpy(); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - QDAYS + 1)
        win_c = close_arr[start:i + 1]; win_v = vol_arr[start:i + 1]
        m = ~np.isnan(win_c) & ~np.isnan(win_v)
        if not m.any(): continue
        idx = int(np.nanargmin(win_v))
        lvn = win_c[idx]; c_now = close_arr[i]
        if np.isnan(lvn) or np.isnan(c_now) or lvn <= 0 or c_now <= 0: continue
        out[i] = float(np.log(c_now) - np.log(lvn))
    return pd.Series(out, index=close.index)


def f23_adld_199_volume_concentration_top10_share_252(volume: pd.Series) -> pd.Series:
    """Fraction of total 252d volume occurring on the top 10 highest-volume bars — concentration index."""
    n = len(volume); vol_arr = volume.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win = vol_arr[start:i + 1]; win = win[~np.isnan(win)]
        if win.size < 10: continue
        tot = win.sum()
        if tot == 0: continue
        top10 = np.sort(win)[-10:].sum()
        out[i] = float(top10 / tot)
    return pd.Series(out, index=volume.index)


# ============================================================
# Bucket I — ROC velocity of flow indicators (200-205)
# ============================================================

def f23_adld_200_roc_cmf_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d rate-of-change of CMF21."""
    return _cmf(high, low, close, volume, MDAYS) - _cmf(high, low, close, volume, MDAYS).shift(MDAYS)


def f23_adld_201_roc_mfi_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d rate-of-change of MFI14."""
    mfi = _mfi(high, low, close, volume, 14)
    return mfi - mfi.shift(MDAYS)


def f23_adld_202_cmf_velocity_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d velocity of CMF21 — short-horizon flow acceleration."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    return cmf - cmf.shift(WDAYS)


def f23_adld_203_mfi_velocity_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d velocity of MFI14."""
    mfi = _mfi(high, low, close, volume, 14)
    return mfi - mfi.shift(WDAYS)


def f23_adld_204_force_index_acceleration_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d acceleration of Force Index EMA13 (2nd discrete diff)."""
    fi = _force_index(close, volume, 13)
    return fi.diff(WDAYS).diff(WDAYS)


def f23_adld_205_ad_line_velocity_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d velocity of cumulative AD line."""
    ad = _ad_line(high, low, close, volume)
    return ad - ad.shift(WDAYS)


# ============================================================
# Bucket J — AD line drawdown / trendline break (206-209)
# ============================================================

def f23_adld_206_ad_line_drawdown_from_peak_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drawdown of AD line from trailing 252d max in absolute units."""
    ad = _ad_line(high, low, close, volume)
    return ad - ad.rolling(YDAYS, min_periods=QDAYS).max()


def f23_adld_207_ad_line_drawdown_from_peak_pct_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drawdown of AD line from 252d peak as fraction (relative)."""
    ad = _ad_line(high, low, close, volume)
    ad_max = ad.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(ad - ad_max, ad_max.abs())


def f23_adld_208_ad_line_linear_fit_residual_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stdev of residuals of linear fit through AD line over last 63d — non-linearity indicator."""
    ad = _ad_line(high, low, close, volume)
    def _resid(w):
        if np.isnan(w).any(): return np.nan
        x = np.arange(len(w), dtype=float)
        xm = x.mean(); ym = w.mean()
        den = ((x - xm) ** 2).sum()
        if den == 0: return np.nan
        b = ((x - xm) * (w - ym)).sum() / den
        a = ym - b * xm
        return float(((w - (a + b * x)) ** 2).mean() ** 0.5)
    return ad.rolling(QDAYS, min_periods=MDAYS).apply(_resid, raw=True)


def f23_adld_209_ad_line_trendline_break_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: today's AD line below a linear-fit extrapolation by > 1 stdev of recent residuals."""
    ad = _ad_line(high, low, close, volume)
    slope = _rolling_slope(ad, QDAYS, min_periods=MDAYS)
    sma = ad.rolling(QDAYS, min_periods=MDAYS).mean()
    # extrapolated value: sma represents mean at center of window, slope per bar → today's predicted = sma + slope*(QDAYS/2)
    pred = sma + slope * (QDAYS / 2.0)
    resid_std = (ad - sma).rolling(QDAYS, min_periods=MDAYS).std()
    return (ad < (pred - resid_std)).astype(float)


# ============================================================
# Bucket K — Distribution / accumulation WEEK / MONTH (210-215)
# ============================================================

def f23_adld_210_distribution_week_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: last 5d total down-volume > up-volume AND close < close 5 bars ago — distribution week."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    dn_vol = volume.where(close < close.shift(1), 0.0)
    up5 = up_vol.rolling(WDAYS, min_periods=WDAYS).sum()
    dn5 = dn_vol.rolling(WDAYS, min_periods=WDAYS).sum()
    return ((dn5 > up5) & (close < close.shift(WDAYS))).astype(float)


def f23_adld_211_distribution_week_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-week events in trailing 252d."""
    return f23_adld_210_distribution_week_indicator(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


def f23_adld_212_accumulation_week_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: last 5d up-volume > down-volume AND close > close 5 bars ago."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    dn_vol = volume.where(close < close.shift(1), 0.0)
    up5 = up_vol.rolling(WDAYS, min_periods=WDAYS).sum()
    dn5 = dn_vol.rolling(WDAYS, min_periods=WDAYS).sum()
    return ((up5 > dn5) & (close > close.shift(WDAYS))).astype(float)


def f23_adld_213_accumulation_week_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of accumulation-week events in trailing 252d."""
    return f23_adld_212_accumulation_week_indicator(high, low, close, volume).rolling(YDAYS, min_periods=QDAYS).sum()


def f23_adld_214_distribution_month_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: trailing 21d down-volume > up-volume AND close < close 21 bars ago."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    dn_vol = volume.where(close < close.shift(1), 0.0)
    up21 = up_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    dn21 = dn_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    return ((dn21 > up21) & (close < close.shift(MDAYS))).astype(float)


def f23_adld_215_accumulation_month_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: trailing 21d up-volume > down-volume AND close > close 21 bars ago."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    dn_vol = volume.where(close < close.shift(1), 0.0)
    up21 = up_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    dn21 = dn_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    return ((up21 > dn21) & (close > close.shift(MDAYS))).astype(float)


# ============================================================
# Bucket L — Volume Spread Analysis (VSA) proxies (216-220)
# ============================================================

def f23_adld_216_effort_vs_result_divergence_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """High volume but small range (effort > result) divergence count in last 21d.
    Volume z-score > 1.0 AND range / atr < 0.7."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    rng = (high - low)
    atr = _atr(high, low, close, n=MDAYS)
    high_effort_low_result = (vz > 1.0) & (_safe_div(rng, atr) < 0.7)
    return high_effort_low_result.astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f23_adld_217_no_demand_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """No-demand bar: close UP from prior bar AND volume < 70% of 21d mean — half-hearted up move (VSA bearish in uptrend)."""
    v_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return ((close > close.shift(1)) & (volume < 0.7 * v_mean)).astype(float)


def f23_adld_218_no_supply_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """No-supply bar: close DOWN AND volume < 70% of 21d mean — half-hearted decline (VSA bullish in downtrend)."""
    v_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return ((close < close.shift(1)) & (volume < 0.7 * v_mean)).astype(float)


def f23_adld_219_stopping_volume_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stopping volume: very high volume (z > 2.0) but body / range < 0.3 — exhaustion of selling/buying pressure."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    body = (close - close.shift(1)).abs()
    rng = (high - low)
    return ((vz > 2.0) & (_safe_div(body, rng) < 0.3)).astype(float)


def f23_adld_220_climax_volume_with_wide_range_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in 252d with both volume z > 2.0 AND range > 2 × ATR — climax events."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    rng = (high - low)
    atr = _atr(high, low, close, n=MDAYS)
    return ((vz > 2.0) & (_safe_div(rng, atr) > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Composite scores (221-225)
# ============================================================

def f23_adld_221_distribution_phase_composite_score_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite distribution: distribution-week count + bearish flow agreement + AD bearish div count."""
    dw = f23_adld_211_distribution_week_count_252(high, low, close, volume).fillna(0)
    bearish_agree = ((_flow_indicator_signs(high, low, close, volume) == -1).sum(axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    ad_bear = _div_bear_window(close, _ad_line(high, low, close, volume), QDAYS).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return dw + 5.0 * bearish_agree + ad_bear


def f23_adld_222_accumulation_phase_composite_score_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite accumulation: accumulation-week count + bullish flow agreement + AD bullish div count."""
    aw = f23_adld_213_accumulation_week_count_252(high, low, close, volume).fillna(0)
    bullish_agree = ((_flow_indicator_signs(high, low, close, volume) == 1).sum(axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    ad_bull = _div_bull_window(close, _ad_line(high, low, close, volume), QDAYS).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return aw + 5.0 * bullish_agree + ad_bull


def f23_adld_223_flow_capitulation_composite_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation bottom: extreme negative Force AND extreme low CMF AND climax volume in last 21d."""
    fi = _force_index(close, volume, 13)
    fi_z = _rolling_zscore(fi, YDAYS, min_periods=QDAYS)
    cmf = _cmf(high, low, close, volume, MDAYS)
    cmf_low = (cmf < -0.25).astype(float)
    climax = f23_adld_220_climax_volume_with_wide_range_count_252(high, low, close, volume) > 0
    fi_extreme = (fi_z < -2.0).astype(float)
    recent_climax = climax.astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    return fi_extreme + cmf_low + recent_climax


def f23_adld_224_flow_topping_composite_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Topping composite: MFI > 80 + CMF > 0.25 + AD bearish divergence + price at new 252d high."""
    mfi = _mfi(high, low, close, volume, 14)
    cmf = _cmf(high, low, close, volume, MDAYS)
    ad_bear = _div_bear_window(close, _ad_line(high, low, close, volume), QDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (close >= rmax).astype(float)
    return (mfi > 80).astype(float) + (cmf > 0.25).astype(float) + ad_bear + at_high


def f23_adld_225_flow_regime_classifier_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Categorical regime: 0=accum, 1=markup, 2=distrib, 3=markdown, 4=transition."""
    return f23_adld_187_flow_phase_indicator(high, low, close, volume)


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f23_adld_151_ad_bullish_div_63_d1(high, low, close, volume):
    return f23_adld_151_ad_bullish_div_63(high, low, close, volume).diff()


def f23_adld_152_ad_bullish_div_252_d1(high, low, close, volume):
    return f23_adld_152_ad_bullish_div_252(high, low, close, volume).diff()


def f23_adld_153_ad_bullish_div_count_63_d1(high, low, close, volume):
    return f23_adld_153_ad_bullish_div_count_63(high, low, close, volume).diff()


def f23_adld_154_ad_bullish_div_count_252_d1(high, low, close, volume):
    return f23_adld_154_ad_bullish_div_count_252(high, low, close, volume).diff()


def f23_adld_155_bars_since_last_ad_bullish_div_63_d1(high, low, close, volume):
    return f23_adld_155_bars_since_last_ad_bullish_div_63(high, low, close, volume).diff()


def f23_adld_156_mfi_bullish_div_63_d1(high, low, close, volume):
    return f23_adld_156_mfi_bullish_div_63(high, low, close, volume).diff()


def f23_adld_157_mfi_bullish_div_count_252_d1(high, low, close, volume):
    return f23_adld_157_mfi_bullish_div_count_252(high, low, close, volume).diff()


def f23_adld_158_ad_hidden_bearish_div_63_d1(high, low, close, volume):
    return f23_adld_158_ad_hidden_bearish_div_63(high, low, close, volume).diff()


def f23_adld_159_ad_hidden_bullish_div_63_d1(high, low, close, volume):
    return f23_adld_159_ad_hidden_bullish_div_63(high, low, close, volume).diff()


def f23_adld_160_cmf_hidden_bearish_div_63_d1(high, low, close, volume):
    return f23_adld_160_cmf_hidden_bearish_div_63(high, low, close, volume).diff()


def f23_adld_161_mfi_hidden_bullish_div_63_d1(high, low, close, volume):
    return f23_adld_161_mfi_hidden_bullish_div_63(high, low, close, volume).diff()


def f23_adld_162_force_index_hidden_bearish_div_63_d1(close, volume):
    return f23_adld_162_force_index_hidden_bearish_div_63(close, volume).diff()


def f23_adld_163_count_hidden_div_events_252_d1(high, low, close, volume):
    return f23_adld_163_count_hidden_div_events_252(high, low, close, volume).diff()


def f23_adld_164_emv_1bar_d1(high, low, volume):
    return f23_adld_164_emv_1bar(high, low, volume).diff()


def f23_adld_165_emv_ema14_d1(high, low, volume):
    return f23_adld_165_emv_ema14(high, low, volume).diff()


def f23_adld_166_emv_ema63_d1(high, low, volume):
    return f23_adld_166_emv_ema63(high, low, volume).diff()


def f23_adld_167_emv_zscore_252_d1(high, low, volume):
    return f23_adld_167_emv_zscore_252(high, low, volume).diff()


def f23_adld_168_emv_above_zero_state_d1(high, low, volume):
    return f23_adld_168_emv_above_zero_state(high, low, volume).diff()


def f23_adld_169_emv_dwell_below_zero_63_d1(high, low, volume):
    return f23_adld_169_emv_dwell_below_zero_63(high, low, volume).diff()


def f23_adld_170_emv_bearish_div_63_d1(high, low, close, volume):
    return f23_adld_170_emv_bearish_div_63(high, low, close, volume).diff()


def f23_adld_171_pvo_12_26_d1(volume):
    return f23_adld_171_pvo_12_26(volume).diff()


def f23_adld_172_pvo_signal_d1(volume):
    return f23_adld_172_pvo_signal(volume).diff()


def f23_adld_173_pvo_histogram_d1(volume):
    return f23_adld_173_pvo_histogram(volume).diff()


def f23_adld_174_pvo_zscore_252_d1(volume):
    return f23_adld_174_pvo_zscore_252(volume).diff()


def f23_adld_175_pvo_above_zero_state_d1(volume):
    return f23_adld_175_pvo_above_zero_state(volume).diff()


def f23_adld_176_pvo_bearish_cross_event_d1(volume):
    return f23_adld_176_pvo_bearish_cross_event(volume).diff()


def f23_adld_177_volume_osc_short_long_d1(volume):
    return f23_adld_177_volume_osc_short_long(volume).diff()


def f23_adld_178_volume_osc_zscore_252_d1(volume):
    return f23_adld_178_volume_osc_zscore_252(volume).diff()


def f23_adld_179_volume_osc_bearish_cross_event_d1(volume):
    return f23_adld_179_volume_osc_bearish_cross_event(volume).diff()


def f23_adld_180_flow_indicator_agreement_score_bearish_d1(high, low, close, volume):
    return f23_adld_180_flow_indicator_agreement_score_bearish(high, low, close, volume).diff()


def f23_adld_181_flow_indicator_agreement_score_bullish_d1(high, low, close, volume):
    return f23_adld_181_flow_indicator_agreement_score_bullish(high, low, close, volume).diff()


def f23_adld_182_flow_indicator_disagreement_252_d1(high, low, close, volume):
    return f23_adld_182_flow_indicator_disagreement_252(high, low, close, volume).diff()


def f23_adld_183_multi_indicator_OB_count_d1(high, low, close, volume):
    return f23_adld_183_multi_indicator_OB_count(high, low, close, volume).diff()


def f23_adld_184_multi_indicator_OS_count_d1(high, low, close, volume):
    return f23_adld_184_multi_indicator_OS_count(high, low, close, volume).diff()


def f23_adld_185_flow_signal_stability_63_d1(high, low, close, volume):
    return f23_adld_185_flow_signal_stability_63(high, low, close, volume).diff()


def f23_adld_186_flow_signal_persistence_63_d1(high, low, close, volume):
    return f23_adld_186_flow_signal_persistence_63(high, low, close, volume).diff()


def f23_adld_187_flow_phase_indicator_d1(high, low, close, volume):
    return f23_adld_187_flow_phase_indicator(high, low, close, volume).diff()


def f23_adld_188_ewma_weighted_ad_line_21_d1(high, low, close, volume):
    return f23_adld_188_ewma_weighted_ad_line_21(high, low, close, volume).diff()


def f23_adld_189_ewma_weighted_ad_line_63_d1(high, low, close, volume):
    return f23_adld_189_ewma_weighted_ad_line_63(high, low, close, volume).diff()


def f23_adld_190_recent_vs_baseline_clv_ratio_63_d1(high, low, close):
    return f23_adld_190_recent_vs_baseline_clv_ratio_63(high, low, close).diff()


def f23_adld_191_half_life_weighted_clv_252_d1(high, low, close):
    return f23_adld_191_half_life_weighted_clv_252(high, low, close).diff()


def f23_adld_192_anchored_vwap_252d_high_d1(high, low, close, volume):
    return f23_adld_192_anchored_vwap_252d_high(high, low, close, volume).diff()


def f23_adld_193_price_vs_anchored_vwap_252d_high_log_d1(high, low, close, volume):
    return f23_adld_193_price_vs_anchored_vwap_252d_high_log(high, low, close, volume).diff()


def f23_adld_194_price_vs_anchored_vwap_252d_high_atr_d1(high, low, close, volume):
    return f23_adld_194_price_vs_anchored_vwap_252d_high_atr(high, low, close, volume).diff()


def f23_adld_195_volume_above_current_close_fraction_63_d1(close, volume):
    return f23_adld_195_volume_above_current_close_fraction_63(close, volume).diff()


def f23_adld_196_volume_below_current_close_fraction_63_d1(close, volume):
    return f23_adld_196_volume_below_current_close_fraction_63(close, volume).diff()


def f23_adld_197_high_volume_node_distance_log_63_d1(close, volume):
    return f23_adld_197_high_volume_node_distance_log_63(close, volume).diff()


def f23_adld_198_low_volume_node_distance_log_63_d1(close, volume):
    return f23_adld_198_low_volume_node_distance_log_63(close, volume).diff()


def f23_adld_199_volume_concentration_top10_share_252_d1(volume):
    return f23_adld_199_volume_concentration_top10_share_252(volume).diff()


def f23_adld_200_roc_cmf_21_d1(high, low, close, volume):
    return f23_adld_200_roc_cmf_21(high, low, close, volume).diff()


def f23_adld_201_roc_mfi_21_d1(high, low, close, volume):
    return f23_adld_201_roc_mfi_21(high, low, close, volume).diff()


def f23_adld_202_cmf_velocity_5d_d1(high, low, close, volume):
    return f23_adld_202_cmf_velocity_5d(high, low, close, volume).diff()


def f23_adld_203_mfi_velocity_5d_d1(high, low, close, volume):
    return f23_adld_203_mfi_velocity_5d(high, low, close, volume).diff()


def f23_adld_204_force_index_acceleration_5d_d1(close, volume):
    return f23_adld_204_force_index_acceleration_5d(close, volume).diff()


def f23_adld_205_ad_line_velocity_5d_d1(high, low, close, volume):
    return f23_adld_205_ad_line_velocity_5d(high, low, close, volume).diff()


def f23_adld_206_ad_line_drawdown_from_peak_252_d1(high, low, close, volume):
    return f23_adld_206_ad_line_drawdown_from_peak_252(high, low, close, volume).diff()


def f23_adld_207_ad_line_drawdown_from_peak_pct_252_d1(high, low, close, volume):
    return f23_adld_207_ad_line_drawdown_from_peak_pct_252(high, low, close, volume).diff()


def f23_adld_208_ad_line_linear_fit_residual_63_d1(high, low, close, volume):
    return f23_adld_208_ad_line_linear_fit_residual_63(high, low, close, volume).diff()


def f23_adld_209_ad_line_trendline_break_indicator_63_d1(high, low, close, volume):
    return f23_adld_209_ad_line_trendline_break_indicator_63(high, low, close, volume).diff()


def f23_adld_210_distribution_week_indicator_d1(high, low, close, volume):
    return f23_adld_210_distribution_week_indicator(high, low, close, volume).diff()


def f23_adld_211_distribution_week_count_252_d1(high, low, close, volume):
    return f23_adld_211_distribution_week_count_252(high, low, close, volume).diff()


def f23_adld_212_accumulation_week_indicator_d1(high, low, close, volume):
    return f23_adld_212_accumulation_week_indicator(high, low, close, volume).diff()


def f23_adld_213_accumulation_week_count_252_d1(high, low, close, volume):
    return f23_adld_213_accumulation_week_count_252(high, low, close, volume).diff()


def f23_adld_214_distribution_month_indicator_d1(high, low, close, volume):
    return f23_adld_214_distribution_month_indicator(high, low, close, volume).diff()


def f23_adld_215_accumulation_month_indicator_d1(high, low, close, volume):
    return f23_adld_215_accumulation_month_indicator(high, low, close, volume).diff()


def f23_adld_216_effort_vs_result_divergence_21_d1(high, low, close, volume):
    return f23_adld_216_effort_vs_result_divergence_21(high, low, close, volume).diff()


def f23_adld_217_no_demand_bar_indicator_d1(high, low, close, volume):
    return f23_adld_217_no_demand_bar_indicator(high, low, close, volume).diff()


def f23_adld_218_no_supply_bar_indicator_d1(high, low, close, volume):
    return f23_adld_218_no_supply_bar_indicator(high, low, close, volume).diff()


def f23_adld_219_stopping_volume_indicator_d1(high, low, close, volume):
    return f23_adld_219_stopping_volume_indicator(high, low, close, volume).diff()


def f23_adld_220_climax_volume_with_wide_range_count_252_d1(high, low, close, volume):
    return f23_adld_220_climax_volume_with_wide_range_count_252(high, low, close, volume).diff()


def f23_adld_221_distribution_phase_composite_score_252_d1(high, low, close, volume):
    return f23_adld_221_distribution_phase_composite_score_252(high, low, close, volume).diff()


def f23_adld_222_accumulation_phase_composite_score_252_d1(high, low, close, volume):
    return f23_adld_222_accumulation_phase_composite_score_252(high, low, close, volume).diff()


def f23_adld_223_flow_capitulation_composite_252_d1(high, low, close, volume):
    return f23_adld_223_flow_capitulation_composite_252(high, low, close, volume).diff()


def f23_adld_224_flow_topping_composite_252_d1(high, low, close, volume):
    return f23_adld_224_flow_topping_composite_252(high, low, close, volume).diff()


def f23_adld_225_flow_regime_classifier_252_d1(high, low, close, volume):
    return f23_adld_225_flow_regime_classifier_252(high, low, close, volume).diff()


ACCUMULATION_DISTRIBUTION_LINE_D1_REGISTRY_151_225 = {
    "f23_adld_151_ad_bullish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_151_ad_bullish_div_63_d1},
    "f23_adld_152_ad_bullish_div_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_152_ad_bullish_div_252_d1},
    "f23_adld_153_ad_bullish_div_count_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_153_ad_bullish_div_count_63_d1},
    "f23_adld_154_ad_bullish_div_count_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_154_ad_bullish_div_count_252_d1},
    "f23_adld_155_bars_since_last_ad_bullish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_155_bars_since_last_ad_bullish_div_63_d1},
    "f23_adld_156_mfi_bullish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_156_mfi_bullish_div_63_d1},
    "f23_adld_157_mfi_bullish_div_count_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_157_mfi_bullish_div_count_252_d1},
    "f23_adld_158_ad_hidden_bearish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_158_ad_hidden_bearish_div_63_d1},
    "f23_adld_159_ad_hidden_bullish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_159_ad_hidden_bullish_div_63_d1},
    "f23_adld_160_cmf_hidden_bearish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_160_cmf_hidden_bearish_div_63_d1},
    "f23_adld_161_mfi_hidden_bullish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_161_mfi_hidden_bullish_div_63_d1},
    "f23_adld_162_force_index_hidden_bearish_div_63_d1": {"inputs": ["close", "volume"], "func": f23_adld_162_force_index_hidden_bearish_div_63_d1},
    "f23_adld_163_count_hidden_div_events_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_163_count_hidden_div_events_252_d1},
    "f23_adld_164_emv_1bar_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_164_emv_1bar_d1},
    "f23_adld_165_emv_ema14_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_165_emv_ema14_d1},
    "f23_adld_166_emv_ema63_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_166_emv_ema63_d1},
    "f23_adld_167_emv_zscore_252_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_167_emv_zscore_252_d1},
    "f23_adld_168_emv_above_zero_state_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_168_emv_above_zero_state_d1},
    "f23_adld_169_emv_dwell_below_zero_63_d1": {"inputs": ["high", "low", "volume"], "func": f23_adld_169_emv_dwell_below_zero_63_d1},
    "f23_adld_170_emv_bearish_div_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_170_emv_bearish_div_63_d1},
    "f23_adld_171_pvo_12_26_d1": {"inputs": ["volume"], "func": f23_adld_171_pvo_12_26_d1},
    "f23_adld_172_pvo_signal_d1": {"inputs": ["volume"], "func": f23_adld_172_pvo_signal_d1},
    "f23_adld_173_pvo_histogram_d1": {"inputs": ["volume"], "func": f23_adld_173_pvo_histogram_d1},
    "f23_adld_174_pvo_zscore_252_d1": {"inputs": ["volume"], "func": f23_adld_174_pvo_zscore_252_d1},
    "f23_adld_175_pvo_above_zero_state_d1": {"inputs": ["volume"], "func": f23_adld_175_pvo_above_zero_state_d1},
    "f23_adld_176_pvo_bearish_cross_event_d1": {"inputs": ["volume"], "func": f23_adld_176_pvo_bearish_cross_event_d1},
    "f23_adld_177_volume_osc_short_long_d1": {"inputs": ["volume"], "func": f23_adld_177_volume_osc_short_long_d1},
    "f23_adld_178_volume_osc_zscore_252_d1": {"inputs": ["volume"], "func": f23_adld_178_volume_osc_zscore_252_d1},
    "f23_adld_179_volume_osc_bearish_cross_event_d1": {"inputs": ["volume"], "func": f23_adld_179_volume_osc_bearish_cross_event_d1},
    "f23_adld_180_flow_indicator_agreement_score_bearish_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_180_flow_indicator_agreement_score_bearish_d1},
    "f23_adld_181_flow_indicator_agreement_score_bullish_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_181_flow_indicator_agreement_score_bullish_d1},
    "f23_adld_182_flow_indicator_disagreement_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_182_flow_indicator_disagreement_252_d1},
    "f23_adld_183_multi_indicator_OB_count_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_183_multi_indicator_OB_count_d1},
    "f23_adld_184_multi_indicator_OS_count_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_184_multi_indicator_OS_count_d1},
    "f23_adld_185_flow_signal_stability_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_185_flow_signal_stability_63_d1},
    "f23_adld_186_flow_signal_persistence_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_186_flow_signal_persistence_63_d1},
    "f23_adld_187_flow_phase_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_187_flow_phase_indicator_d1},
    "f23_adld_188_ewma_weighted_ad_line_21_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_188_ewma_weighted_ad_line_21_d1},
    "f23_adld_189_ewma_weighted_ad_line_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_189_ewma_weighted_ad_line_63_d1},
    "f23_adld_190_recent_vs_baseline_clv_ratio_63_d1": {"inputs": ["high", "low", "close"], "func": f23_adld_190_recent_vs_baseline_clv_ratio_63_d1},
    "f23_adld_191_half_life_weighted_clv_252_d1": {"inputs": ["high", "low", "close"], "func": f23_adld_191_half_life_weighted_clv_252_d1},
    "f23_adld_192_anchored_vwap_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_192_anchored_vwap_252d_high_d1},
    "f23_adld_193_price_vs_anchored_vwap_252d_high_log_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_193_price_vs_anchored_vwap_252d_high_log_d1},
    "f23_adld_194_price_vs_anchored_vwap_252d_high_atr_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_194_price_vs_anchored_vwap_252d_high_atr_d1},
    "f23_adld_195_volume_above_current_close_fraction_63_d1": {"inputs": ["close", "volume"], "func": f23_adld_195_volume_above_current_close_fraction_63_d1},
    "f23_adld_196_volume_below_current_close_fraction_63_d1": {"inputs": ["close", "volume"], "func": f23_adld_196_volume_below_current_close_fraction_63_d1},
    "f23_adld_197_high_volume_node_distance_log_63_d1": {"inputs": ["close", "volume"], "func": f23_adld_197_high_volume_node_distance_log_63_d1},
    "f23_adld_198_low_volume_node_distance_log_63_d1": {"inputs": ["close", "volume"], "func": f23_adld_198_low_volume_node_distance_log_63_d1},
    "f23_adld_199_volume_concentration_top10_share_252_d1": {"inputs": ["volume"], "func": f23_adld_199_volume_concentration_top10_share_252_d1},
    "f23_adld_200_roc_cmf_21_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_200_roc_cmf_21_d1},
    "f23_adld_201_roc_mfi_21_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_201_roc_mfi_21_d1},
    "f23_adld_202_cmf_velocity_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_202_cmf_velocity_5d_d1},
    "f23_adld_203_mfi_velocity_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_203_mfi_velocity_5d_d1},
    "f23_adld_204_force_index_acceleration_5d_d1": {"inputs": ["close", "volume"], "func": f23_adld_204_force_index_acceleration_5d_d1},
    "f23_adld_205_ad_line_velocity_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_205_ad_line_velocity_5d_d1},
    "f23_adld_206_ad_line_drawdown_from_peak_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_206_ad_line_drawdown_from_peak_252_d1},
    "f23_adld_207_ad_line_drawdown_from_peak_pct_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_207_ad_line_drawdown_from_peak_pct_252_d1},
    "f23_adld_208_ad_line_linear_fit_residual_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_208_ad_line_linear_fit_residual_63_d1},
    "f23_adld_209_ad_line_trendline_break_indicator_63_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_209_ad_line_trendline_break_indicator_63_d1},
    "f23_adld_210_distribution_week_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_210_distribution_week_indicator_d1},
    "f23_adld_211_distribution_week_count_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_211_distribution_week_count_252_d1},
    "f23_adld_212_accumulation_week_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_212_accumulation_week_indicator_d1},
    "f23_adld_213_accumulation_week_count_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_213_accumulation_week_count_252_d1},
    "f23_adld_214_distribution_month_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_214_distribution_month_indicator_d1},
    "f23_adld_215_accumulation_month_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_215_accumulation_month_indicator_d1},
    "f23_adld_216_effort_vs_result_divergence_21_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_216_effort_vs_result_divergence_21_d1},
    "f23_adld_217_no_demand_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_217_no_demand_bar_indicator_d1},
    "f23_adld_218_no_supply_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_218_no_supply_bar_indicator_d1},
    "f23_adld_219_stopping_volume_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_219_stopping_volume_indicator_d1},
    "f23_adld_220_climax_volume_with_wide_range_count_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_220_climax_volume_with_wide_range_count_252_d1},
    "f23_adld_221_distribution_phase_composite_score_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_221_distribution_phase_composite_score_252_d1},
    "f23_adld_222_accumulation_phase_composite_score_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_222_accumulation_phase_composite_score_252_d1},
    "f23_adld_223_flow_capitulation_composite_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_223_flow_capitulation_composite_252_d1},
    "f23_adld_224_flow_topping_composite_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_224_flow_topping_composite_252_d1},
    "f23_adld_225_flow_regime_classifier_252_d1": {"inputs": ["high", "low", "close", "volume"], "func": f23_adld_225_flow_regime_classifier_252_d1},
}
