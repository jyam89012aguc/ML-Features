import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _new_high_252(high):
    return high >= high.rolling(YDAYS, min_periods=QDAYS).max()


def _adx(high, low, close, n=14):
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
    adx = dx.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return adx, plus_di, minus_di


def _aroon_up(high, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        idx_max = int(np.nanargmax(w))
        return 100.0 * idx_max / (len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _vortex(high, low, close, n=14):
    pc = close.shift(1)
    vmp = (high - low.shift(1)).abs()
    vmm = (low - high.shift(1)).abs()
    tr = _true_range(high, low, close)
    vip = vmp.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    vin = vmm.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    return vip, vin


def _mass_index(high, low, n=9, n2=25):
    rng = high - low
    e1 = rng.ewm(span=n, adjust=False, min_periods=n).mean()
    e2 = e1.ewm(span=n, adjust=False, min_periods=n).mean()
    ratio = _safe_div(e1, e2)
    return ratio.rolling(n2, min_periods=n2 // 2).sum()


def _klinger_kvo(high, low, close, volume, fast=34, slow=55):
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).fillna(0.0)
    dm = (high - low)
    cm_raw = dm.where(trend == trend.shift(1), dm + dm.shift(1))
    vf = volume * trend * (2.0 * _safe_div(dm, cm_raw.replace(0, np.nan)) - 1.0) * 100.0
    ef = vf.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = vf.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return ef - es


def _force_index(close, volume, n=13):
    return (close.diff() * volume).ewm(span=n, adjust=False, min_periods=n).mean()


def _obv(close, volume):
    sign = np.sign(close.diff()).fillna(0.0)
    return (sign * volume).cumsum()


def _coppock(close, roc_long=14, roc_short=11, wma_n=10):
    r1 = close.pct_change(roc_long) * 100.0
    r2 = close.pct_change(roc_short) * 100.0
    s = r1 + r2
    weights = np.arange(1, wma_n + 1, dtype=float)
    def _f(w):
        nw = len(w)
        valid = ~np.isnan(w)
        if valid.sum() < max(wma_n // 3, 2):
            return np.nan
        x = w.copy()
        x[~valid] = 0.0
        wv = np.arange(1, nw + 1, dtype=float)
        wv[~valid] = 0.0
        ws = wv.sum()
        return (x * wv).sum() / ws if ws != 0 else np.nan
    return s.rolling(wma_n, min_periods=max(wma_n // 3, 2)).apply(_f, raw=True)


def _kst(close, r1=10, r2=15, r3=20, r4=30, w1=10, w2=10, w3=10, w4=15):
    roc1 = close.pct_change(r1) * 100.0
    roc2 = close.pct_change(r2) * 100.0
    roc3 = close.pct_change(r3) * 100.0
    roc4 = close.pct_change(r4) * 100.0
    return (_sma(roc1, w1) + 2.0 * _sma(roc2, w2) + 3.0 * _sma(roc3, w3) + 4.0 * _sma(roc4, w4))


def _choppiness(high, low, close, n=14):
    tr = _true_range(high, low, close)
    sum_tr = tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(np.log(_safe_div(sum_tr, hh - ll)), np.log(n))


def _williams_r(high, low, close, n=14):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma_tp = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma_tp).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma_tp, 0.015 * mad)


def f49_bcco_301_golden_cross_within_21_and_new_252d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cross = (s50.shift(1) <= s200.shift(1)) & (s50 > s200)
    recent = cross.astype(float).rolling(MDAYS, min_periods=1).max() > 0
    return (recent & _new_high_252(high)).astype(float).where(s200.notna(), np.nan)


def f49_bcco_302_golden_cross_count_252(close: pd.Series) -> pd.Series:
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    cross = ((s50.shift(1) <= s200.shift(1)) & (s50 > s200)).astype(float)
    return cross.rolling(YDAYS, min_periods=QDAYS).sum().where(s200.notna(), np.nan)


def f49_bcco_303_short_cross_above_medium_and_new_21d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    s21 = _sma(close, MDAYS); s63 = _sma(close, QDAYS)
    cross = (s21.shift(1) <= s63.shift(1)) & (s21 > s63)
    recent = cross.astype(float).rolling(WDAYS, min_periods=1).max() > 0
    return (recent & _new_high_21(high)).astype(float).where(s63.notna(), np.nan)


def f49_bcco_304_short_cross_count_with_new_high_63(high: pd.Series, close: pd.Series) -> pd.Series:
    s21 = _sma(close, MDAYS); s63 = _sma(close, QDAYS)
    cross = (s21.shift(1) <= s63.shift(1)) & (s21 > s63)
    ev = (cross & _new_high_21(high)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(s63.notna(), np.nan)


def f49_bcco_305_macd_signal_cross_and_new_252d_high(high: pd.Series, close: pd.Series) -> pd.Series:
    macd = _ema(close, 12) - _ema(close, 26)
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    diff = macd - sig
    cross = (diff.shift(1) <= 0) & (diff > 0)
    return (cross & _new_high_252(high)).astype(float).where(diff.notna(), np.nan)


def f49_bcco_306_psar_flip_up_and_new_252d_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    stop = low.rolling(10, min_periods=3).min()
    cross = (close.shift(1) <= stop.shift(1)) & (close > stop)
    return (cross & _new_high_252(high)).astype(float).where(stop.notna(), np.nan)


def f49_bcco_307_supertrend_flip_up_and_new_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mid = _ema(close, 20)
    a = _atr(high, low, close, 20)
    lower_band = mid - 2.0 * a
    cross_up = (close.shift(1) <= lower_band.shift(1)) & (close > lower_band)
    return (cross_up & _new_high_21(high)).astype(float).where(lower_band.notna(), np.nan)


def f49_bcco_308_full_ma_stack_and_new_252d_high(close: pd.Series, high: pd.Series) -> pd.Series:
    s5 = _sma(close, WDAYS); s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    stack = (s5 > s21) & (s21 > s50) & (s50 > s200)
    return (stack & _new_high_252(high)).astype(float).where(s200.notna(), np.nan)


def f49_bcco_309_full_ma_stack_and_rsi_above_70(close: pd.Series) -> pd.Series:
    s5 = _sma(close, WDAYS); s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    stack = (s5 > s21) & (s21 > s50) & (s50 > s200)
    return (stack & (_rsi(close, 14) > 70.0)).astype(float).where(s200.notna(), np.nan)


def f49_bcco_310_full_ma_stack_and_vol_z_2_and_new_high(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    s5 = _sma(close, WDAYS); s21 = _sma(close, MDAYS); s50 = _sma(close, 50); s200 = _sma(close, 200)
    stack = (s5 > s21) & (s21 > s50) & (s50 > s200)
    return (stack & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0) & _new_high_252(high)).astype(float).where(s200.notna(), np.nan)


def f49_bcco_311_vol_in_top_25pct_21d_range_past_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos > 0.75)
    return (volume.where(cond, 0.0)).rolling(QDAYS, min_periods=MDAYS).sum().where(pos.notna(), np.nan)


def f49_bcco_312_vol_in_top_25pct_252d_range_past_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos > 0.75)
    return (volume.where(cond, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum().where(pos.notna(), np.nan)


def f49_bcco_313_top_25_vol_fraction_past_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos > 0.75)
    num = (volume.where(cond, 0.0)).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f49_bcco_314_top_25_vol_fraction_past_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    cond = (pos > 0.75)
    num = (volume.where(cond, 0.0)).rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


def f49_bcco_315_peak_vol_day_position_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    def _f_pos(w_pos, w_vol):
        valid = ~(np.isnan(w_pos) | np.isnan(w_vol))
        if valid.sum() < WDAYS:
            return np.nan
        p = w_pos[valid]; v = w_vol[valid]
        if v.size == 0:
            return np.nan
        return float(p[int(np.argmax(v))])
    n = len(close)
    out = np.full(n, np.nan)
    pos_arr = pos.to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - MDAYS + 1)
        out[t] = _f_pos(pos_arr[lo : t + 1], vol_arr[lo : t + 1])
    return pd.Series(out, index=close.index)


def f49_bcco_316_peak_vol_day_position_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    n = len(close)
    out = np.full(n, np.nan)
    pos_arr = pos.to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - QDAYS + 1)
        w_pos = pos_arr[lo : t + 1]
        w_vol = vol_arr[lo : t + 1]
        valid = ~(np.isnan(w_pos) | np.isnan(w_vol))
        if valid.sum() < MDAYS:
            continue
        p = w_pos[valid]; v = w_vol[valid]
        if v.size == 0:
            continue
        out[t] = float(p[int(np.argmax(v))])
    return pd.Series(out, index=close.index)


def f49_bcco_317_cum_vol_from_21d_low(low: pd.Series, volume: pd.Series) -> pd.Series:
    n = len(low)
    out = np.full(n, np.nan)
    low_arr = low.to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - MDAYS + 1)
        w = low_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmin(w))
        k = lo + rel
        out[t] = float(np.nansum(vol_arr[k : t + 1]))
    return pd.Series(out, index=low.index)


def f49_bcco_318_cum_vol_from_21d_low_fraction(low: pd.Series, volume: pd.Series) -> pd.Series:
    n = len(low)
    num_arr = np.full(n, np.nan)
    low_arr = low.to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    for t in range(n):
        lo = max(0, t - MDAYS + 1)
        w = low_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmin(w))
        k = lo + rel
        num_arr[t] = float(np.nansum(vol_arr[k : t + 1]))
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(pd.Series(num_arr, index=low.index), den)


def f49_bcco_319_new_252d_high_and_ret21_over_30pct_and_vol_z(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_new_high_252(high)
            & (close.pct_change(MDAYS) > 0.30)
            & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0)).astype(float)


def f49_bcco_320_new_252d_high_and_5pct_pullback_from_recent_high(high: pd.Series, close: pd.Series) -> pd.Series:
    rh5 = high.rolling(WDAYS, min_periods=2).max()
    return (_new_high_252(high) & ((close / rh5 - 1.0) < -0.05)).astype(float).where(rh5.notna(), np.nan)


def f49_bcco_321_new_252d_high_and_williams_r_above_neg5(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_new_high_252(high) & (_williams_r(high, low, close, 14) > -5.0)).astype(float)


def f49_bcco_322_new_252d_high_and_coppock_positive_and_rising(high: pd.Series, close: pd.Series) -> pd.Series:
    c = _coppock(close)
    return (_new_high_252(high) & (c > 0) & (c > c.shift(1))).astype(float).where(c.notna(), np.nan)


def f49_bcco_323_new_252d_high_and_kst_positive_and_rising(high: pd.Series, close: pd.Series) -> pd.Series:
    k = _kst(close)
    return (_new_high_252(high) & (k > 0) & (k > k.shift(1))).astype(float).where(k.notna(), np.nan)


def f49_bcco_324_new_252d_high_and_choppiness_below_38(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ch = _choppiness(high, low, close, 14)
    return (_new_high_252(high) & (ch < 38.0)).astype(float).where(ch.notna(), np.nan)


def f49_bcco_325_new_252d_high_and_adx_over_40(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adx, _, _ = _adx(high, low, close, 14)
    return (_new_high_252(high) & (adx > 40.0)).astype(float).where(adx.notna(), np.nan)


def f49_bcco_326_new_252d_high_and_adx_over_50(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adx, _, _ = _adx(high, low, close, 14)
    return (_new_high_252(high) & (adx > 50.0)).astype(float).where(adx.notna(), np.nan)


def f49_bcco_327_new_252d_high_and_aroon_up_100(high: pd.Series) -> pd.Series:
    return (_new_high_252(high) & (_aroon_up(high, MDAYS) >= 100.0)).astype(float).where(_aroon_up(high, MDAYS).notna(), np.nan)


def f49_bcco_328_new_252d_high_and_dmi_diff_over_30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    _, plus_di, minus_di = _adx(high, low, close, 14)
    return (_new_high_252(high) & ((plus_di - minus_di) > 30.0)).astype(float).where(plus_di.notna(), np.nan)


def f49_bcco_329_new_252d_high_and_vortex_pos_above_neg_extreme(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vip, vin = _vortex(high, low, close, 14)
    return (_new_high_252(high) & ((vip - vin) > 0.3)).astype(float).where(vip.notna(), np.nan)


def f49_bcco_330_new_252d_high_and_mass_index_above_27(high: pd.Series, low: pd.Series) -> pd.Series:
    return (_new_high_252(high) & (_mass_index(high, low) > 27.0)).astype(float).where(_mass_index(high, low).notna(), np.nan)


def f49_bcco_331_new_252d_high_and_kvo_above_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    kvo = _klinger_kvo(high, low, close, volume)
    sig = kvo.ewm(span=13, adjust=False, min_periods=13).mean()
    return (_new_high_252(high) & (kvo > sig)).astype(float).where(sig.notna(), np.nan)


def f49_bcco_332_new_252d_high_and_force_index_z_over_2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    fi = _force_index(close, volume, 13)
    fiz = _rolling_zscore(fi, YDAYS, min_periods=QDAYS)
    return (_new_high_252(high) & (fiz > 2.0)).astype(float).where(fiz.notna(), np.nan)


def f49_bcco_333_new_252d_high_and_obv_at_252d_max(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (_new_high_252(high) & (obv >= obv.rolling(YDAYS, min_periods=QDAYS).max())).astype(float).where(obv.notna(), np.nan)


def f49_bcco_334_new_252d_high_and_obv_at_504d_max(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (_new_high_252(high) & (obv >= obv.rolling(DDAYS_2Y, min_periods=YDAYS).max())).astype(float).where(obv.notna(), np.nan)


def f49_bcco_335_marubozu_at_new_21d_high(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_pct = body / rng
    return (_new_high_21(high) & (body_pct > 0.9)).astype(float).where(rng.notna(), np.nan)


def f49_bcco_336_spinning_top_after_3_strong_close(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    cl = _clv(high, low, close)
    strong_3 = (cl.shift(1) > 0.5) & (cl.shift(2) > 0.5) & (cl.shift(3) > 0.5)
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    body_pct = body / rng
    upper = high - pd.concat([open_, close], axis=1).max(axis=1)
    lower = pd.concat([open_, close], axis=1).min(axis=1) - low
    spinning = (body_pct < 0.3) & (upper > body) & (lower > body)
    return (strong_3 & spinning).astype(float).where(cl.notna() & rng.notna(), np.nan)


def f49_bcco_337_three_line_strike_at_new_high(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    bull3 = (close.shift(1) > open_.shift(1)) & (close.shift(2) > open_.shift(2)) & (close.shift(3) > open_.shift(3))
    bear_today = (close < open_)
    engulfs = close < open_.shift(3)
    nh_recent = _new_high_21(high).rolling(3, min_periods=1).max() > 0
    return (bull3 & bear_today & engulfs & nh_recent).astype(float).where(open_.shift(3).notna(), np.nan)


def f49_bcco_338_bullish_then_bearish_2bar_at_new_high(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    body1 = (close.shift(1) - open_.shift(1))
    body0 = (open_ - close)
    nh = _new_high_21(high).rolling(2, min_periods=1).max() > 0
    return ((body1 > 0) & (body0 > 0) & nh & ((body0 + body1) > 0)).astype(float).where(body1.notna(), np.nan)


def f49_bcco_339_belt_hold_bullish_at_new_252d_high(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    open_at_low = (_safe_div(open_ - low, close).abs() < 0.005)
    strong_bull = (close - open_) > 0.5 * rng
    return (_new_high_252(high) & open_at_low & strong_bull).astype(float).where(rng.notna(), np.nan)


def f49_bcco_340_kicker_bullish_at_new_252d_high(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    prior_bear = close.shift(1) < open_.shift(1)
    gap_kicker = open_ > open_.shift(1)
    bull_today = close > open_
    return (prior_bear & gap_kicker & bull_today & _new_high_252(high)).astype(float).where(open_.shift(1).notna(), np.nan)


def f49_bcco_341_upside_tasuki_gap_at_new_high(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    bull_2 = close.shift(2) > open_.shift(2)
    gap_up_1 = (open_.shift(1) > close.shift(2)) & (close.shift(1) > open_.shift(1))
    today_in_prior_body = (open_ > open_.shift(1)) & (open_ < close.shift(1))
    today_in_gap = (close < open_.shift(1)) & (close > close.shift(2))
    return (bull_2 & gap_up_1 & today_in_prior_body & today_in_gap & _new_high_21(high)).astype(float).where(open_.shift(2).notna(), np.nan)


def f49_bcco_342_ha_bullish_to_bearish_flip_at_new_252d_high(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ha_close = (open_ + high + low + close) / 4.0
    arr_o = open_.to_numpy(dtype=float)
    arr_c = close.to_numpy(dtype=float)
    ha_c_arr = ha_close.to_numpy(dtype=float)
    ha_o = np.full(arr_o.shape, np.nan)
    if arr_o.size > 0:
        ha_o[0] = (arr_o[0] + arr_c[0]) / 2.0 if not (np.isnan(arr_o[0]) or np.isnan(arr_c[0])) else np.nan
        for i in range(1, arr_o.size):
            if np.isnan(ha_o[i - 1]) or np.isnan(ha_c_arr[i - 1]):
                ha_o[i] = (arr_o[i] + arr_c[i]) / 2.0 if not (np.isnan(arr_o[i]) or np.isnan(arr_c[i])) else np.nan
            else:
                ha_o[i] = (ha_o[i - 1] + ha_c_arr[i - 1]) / 2.0
    ha_open_s = pd.Series(ha_o, index=open_.index)
    ha_bull_prev = ha_close.shift(1) > ha_open_s.shift(1)
    ha_bear_now = ha_close < ha_open_s
    nh_recent = _new_high_252(high).rolling(WDAYS, min_periods=1).max() > 0
    return (ha_bull_prev & ha_bear_now & nh_recent).astype(float).where(ha_open_s.notna(), np.nan)


def f49_bcco_343_td_9_setup_count_with_new_252d_high(close: pd.Series, high: pd.Series) -> pd.Series:
    cond_bar = close > close.shift(4)
    streak = _streak_true(cond_bar)
    return ((streak >= 9) & _new_high_252(high)).astype(float).where(cond_bar.notna(), np.nan)


def f49_bcco_344_td_9_setup_count_252(close: pd.Series) -> pd.Series:
    cond = close > close.shift(4)
    s = _streak_true(cond)
    ev = ((s == 9) & (s.shift(1) == 8)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(cond.notna(), np.nan)


def f49_bcco_345_new_252d_high_and_td_13_countdown_proxy(close: pd.Series, high: pd.Series) -> pd.Series:
    cond = close > high.shift(2)
    cnt = cond.astype(float).rolling(30, min_periods=10).sum()
    return ((cnt >= 13) & _new_high_252(high)).astype(float).where(cond.notna(), np.nan)


def f49_bcco_346_td_13_proxy_count_252(close: pd.Series, high: pd.Series) -> pd.Series:
    cond = close > high.shift(2)
    cnt = cond.astype(float).rolling(30, min_periods=10).sum()
    ev = ((cnt >= 13) & (cnt.shift(1) < 13)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(cond.notna(), np.nan)


def f49_bcco_347_close_above_high_4_ago_streak(close: pd.Series, high: pd.Series) -> pd.Series:
    return _streak_true(close > high.shift(4))


def f49_bcco_348_td_perfected_setup_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cond = close > close.shift(4)
    s = _streak_true(cond)
    perfected = (low <= low.shift(2)) | (low <= low.shift(3))
    return ((s >= 9) & perfected).astype(float).where(cond.notna(), np.nan)


def f49_bcco_349_reverse_td_9_setup_count_252(close: pd.Series) -> pd.Series:
    cond = close < close.shift(4)
    s = _streak_true(cond)
    ev = ((s == 9) & (s.shift(1) == 8)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(cond.notna(), np.nan)


def f49_bcco_350_td_sequential_top_signals_count_252(close: pd.Series, high: pd.Series) -> pd.Series:
    cond = close > close.shift(4)
    s = _streak_true(cond)
    ev = ((s >= 9) & _new_high_252(high)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(cond.notna(), np.nan)


def _rolling_slope_close(s, n):
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        num = ((x - xm) * (w - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_slope, raw=True)


def f49_bcco_351_new_252d_high_and_252_slope_sign_flip(high: pd.Series, close: pd.Series) -> pd.Series:
    sl = _rolling_slope_close(close, YDAYS)
    sgn = np.sign(sl)
    flip_recent = ((sgn != sgn.shift(1)).astype(float).rolling(MDAYS, min_periods=1).max() > 0)
    return (_new_high_252(high) & flip_recent).astype(float).where(sl.notna(), np.nan)


def f49_bcco_352_new_252d_high_and_63_slope_sign_flip(high: pd.Series, close: pd.Series) -> pd.Series:
    sl = _rolling_slope_close(close, QDAYS)
    sgn = np.sign(sl)
    flip_recent = ((sgn != sgn.shift(1)).astype(float).rolling(10, min_periods=1).max() > 0)
    return (_new_high_252(high) & flip_recent).astype(float).where(sl.notna(), np.nan)


def f49_bcco_353_williams_fractal_high_at_new_252d_high(high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    return (fractal & _new_high_252(high)).astype(float).where(high.shift(4).notna(), np.nan)


def f49_bcco_354_fractal_high_count_63(high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    return fractal.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(high.shift(4).notna(), np.nan)


def f49_bcco_355_fractal_high_count_252(high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    return fractal.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(high.shift(4).notna(), np.nan)


def f49_bcco_356_peak_density_past_21(high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    return fractal.astype(float).rolling(MDAYS, min_periods=WDAYS).sum().where(high.shift(4).notna(), np.nan)


def f49_bcco_357_bars_since_last_fractal_high(high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    return _bars_since_true(fractal)


def f49_bcco_358_longest_down_streak_after_fractal_high(close: pd.Series, high: pd.Series) -> pd.Series:
    fractal = ((high.shift(2) > high.shift(4)) & (high.shift(2) > high.shift(3))
               & (high.shift(2) > high.shift(1)) & (high.shift(2) > high))
    had_fractal = fractal.astype(float).rolling(MDAYS, min_periods=WDAYS).sum() > 0
    down_streak = _streak_true(close < close.shift(1))
    max_down = down_streak.rolling(MDAYS, min_periods=WDAYS).max()
    return max_down.where(had_fractal, np.nan)


def f49_bcco_359_new_252d_high_and_rsi_80_stoch_80_cci_200(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_new_high_252(high)
            & (_rsi(close, 14) > 80.0)
            & (_stoch_k(high, low, close, 14) > 80.0)
            & (_cci(high, low, close, 20) > 200.0)).astype(float)


def f49_bcco_360_new_252d_high_and_rsi_70_macd_hist_top_decile_vol_z(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    macd = _ema(close, 12) - _ema(close, 26)
    sig = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = macd - sig
    q90 = hist.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (_new_high_252(high)
            & (_rsi(close, 14) > 70.0)
            & (hist > q90)
            & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0)).astype(float).where(q90.notna(), np.nan)


def f49_bcco_361_new_252d_high_and_close_over_15x_sma200_rsi_80(high: pd.Series, close: pd.Series) -> pd.Series:
    return (_new_high_252(high) & (close > 1.5 * _sma(close, 200)) & (_rsi(close, 14) > 80.0)).astype(float).where(_sma(close, 200).notna(), np.nan)


def f49_bcco_362_new_252d_high_and_in_top_10pct_of_252d_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return (_new_high_252(high) & (pos > 0.90)).astype(float).where(pos.notna(), np.nan)


def f49_bcco_363_four_of_five_momentum_at_252d_max(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rsi = _rsi(close, 14)
    k = _stoch_k(high, low, close, 14)
    mfi = _mfi(high, low, close, volume, 14)
    cci = _cci(high, low, close, 20)
    wr = _williams_r(high, low, close, 14)
    c = ((rsi >= rsi.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0)
         + (k >= k.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0)
         + (mfi >= mfi.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0)
         + (cci >= cci.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0)
         + (wr >= wr.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).fillna(0))
    return (c >= 4).astype(float)


def f49_bcco_364_new_252d_high_atr_252d_max_rsi_70_vol_z(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    return (_new_high_252(high)
            & (a >= a.rolling(YDAYS, min_periods=QDAYS).max())
            & (_rsi(close, 14) > 70.0)
            & (_rolling_zscore(volume, YDAYS, min_periods=QDAYS) > 2.0)).astype(float)


def f49_bcco_365_connors_rsi_above_95_and_new_252d_high(close: pd.Series, high: pd.Series) -> pd.Series:
    a = _rsi(close, 3)
    diff = close.diff()
    arr = diff.to_numpy(dtype=float)
    streak = np.zeros(arr.shape, dtype=float)
    c = 0.0
    for i in range(arr.size):
        x = arr[i]
        if np.isnan(x):
            c = 0.0
        elif x > 0:
            c = c + 1.0 if c >= 0 else 1.0
        elif x < 0:
            c = c - 1.0 if c <= 0 else -1.0
        else:
            c = 0.0
        streak[i] = c
    streak_s = pd.Series(streak, index=close.index)
    b = _rsi(streak_s, 2)
    pr_ret = close.pct_change()
    cprank = pr_ret.rolling(100, min_periods=33).rank(pct=True) * 100.0
    connors = (a + b + cprank) / 3.0
    return ((connors > 95.0) & _new_high_252(high)).astype(float).where(connors.notna(), np.nan)


def f49_bcco_366_schaff_trend_cycle_above_90_at_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    macd = _ema(close, 23) - _ema(close, 50)
    macd_min = macd.rolling(10, min_periods=3).min()
    macd_max = macd.rolling(10, min_periods=3).max()
    k1 = 100.0 * _safe_div(macd - macd_min, macd_max - macd_min)
    d1 = k1.ewm(span=3, adjust=False, min_periods=3).mean()
    d1_min = d1.rolling(10, min_periods=3).min()
    d1_max = d1.rolling(10, min_periods=3).max()
    k2 = 100.0 * _safe_div(d1 - d1_min, d1_max - d1_min)
    stc = k2.ewm(span=3, adjust=False, min_periods=3).mean()
    return ((stc > 90.0) & _new_high_252(high)).astype(float).where(stc.notna(), np.nan)


def f49_bcco_367_vortex_pos_at_252d_max_and_new_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vip, _ = _vortex(high, low, close, 14)
    return ((vip >= vip.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(vip.notna(), np.nan)


def f49_bcco_368_mass_index_extreme_and_new_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return ((_mass_index(high, low) > 27.0) & _new_high_252(high)).astype(float).where(_mass_index(high, low).notna(), np.nan)


def f49_bcco_369_vol_of_vol_at_252d_max_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    return ((vov >= vov.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(vov.notna(), np.nan)


def f49_bcco_370_vol_of_vol_pct_rank_over_90_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    pr = vov.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((pr > 0.90) & _new_high_252(high)).astype(float).where(pr.notna(), np.nan)


def f49_bcco_371_realized_vol_21_at_252d_max_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return ((rv >= rv.rolling(YDAYS, min_periods=QDAYS).max()) & _new_high_252(high)).astype(float).where(rv.notna(), np.nan)


def f49_bcco_372_atr_pct_rank_99_and_new_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    a = _atr(high, low, close, MDAYS)
    pr = a.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((pr > 0.99) & _new_high_252(high)).astype(float).where(pr.notna(), np.nan)


def f49_bcco_373_vol_horizons_stacking_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv5 = close.pct_change().rolling(WDAYS, min_periods=2).std()
    rv21 = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    rv63 = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    return ((rv5 > rv21) & (rv21 > rv63) & _new_high_252(high)).astype(float).where(rv63.notna(), np.nan)


def f49_bcco_374_all_vol_horizons_top_decile_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv5 = close.pct_change().rolling(WDAYS, min_periods=2).std()
    rv21 = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    rv63 = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    pr5 = rv5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    pr21 = rv21.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    pr63 = rv63.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((pr5 > 0.90) & (pr21 > 0.90) & (pr63 > 0.90) & _new_high_252(high)).astype(float).where(pr63.notna(), np.nan)


def f49_bcco_375_5d_realized_vol_zscore_over_3_and_new_high(close: pd.Series, high: pd.Series) -> pd.Series:
    rv5 = close.pct_change().rolling(WDAYS, min_periods=2).std()
    rz = _rolling_zscore(rv5, YDAYS, min_periods=QDAYS)
    return ((rz > 3.0) & _new_high_252(high)).astype(float).where(rz.notna(), np.nan)


def f49_bcco_301_golden_cross_within_21_and_new_252d_high_d3(high, close):
    return f49_bcco_301_golden_cross_within_21_and_new_252d_high(high, close).diff().diff().diff()


def f49_bcco_302_golden_cross_count_252_d3(close):
    return f49_bcco_302_golden_cross_count_252(close).diff().diff().diff()


def f49_bcco_303_short_cross_above_medium_and_new_21d_high_d3(high, close):
    return f49_bcco_303_short_cross_above_medium_and_new_21d_high(high, close).diff().diff().diff()


def f49_bcco_304_short_cross_count_with_new_high_63_d3(high, close):
    return f49_bcco_304_short_cross_count_with_new_high_63(high, close).diff().diff().diff()


def f49_bcco_305_macd_signal_cross_and_new_252d_high_d3(high, close):
    return f49_bcco_305_macd_signal_cross_and_new_252d_high(high, close).diff().diff().diff()


def f49_bcco_306_psar_flip_up_and_new_252d_high_d3(high, low, close):
    return f49_bcco_306_psar_flip_up_and_new_252d_high(high, low, close).diff().diff().diff()


def f49_bcco_307_supertrend_flip_up_and_new_high_d3(high, low, close):
    return f49_bcco_307_supertrend_flip_up_and_new_high(high, low, close).diff().diff().diff()


def f49_bcco_308_full_ma_stack_and_new_252d_high_d3(close, high):
    return f49_bcco_308_full_ma_stack_and_new_252d_high(close, high).diff().diff().diff()


def f49_bcco_309_full_ma_stack_and_rsi_above_70_d3(close):
    return f49_bcco_309_full_ma_stack_and_rsi_above_70(close).diff().diff().diff()


def f49_bcco_310_full_ma_stack_and_vol_z_2_and_new_high_d3(high, close, volume):
    return f49_bcco_310_full_ma_stack_and_vol_z_2_and_new_high(high, close, volume).diff().diff().diff()


def f49_bcco_311_vol_in_top_25pct_21d_range_past_63_d3(high, low, close, volume):
    return f49_bcco_311_vol_in_top_25pct_21d_range_past_63(high, low, close, volume).diff().diff().diff()


def f49_bcco_312_vol_in_top_25pct_252d_range_past_252_d3(high, low, close, volume):
    return f49_bcco_312_vol_in_top_25pct_252d_range_past_252(high, low, close, volume).diff().diff().diff()


def f49_bcco_313_top_25_vol_fraction_past_63_d3(high, low, close, volume):
    return f49_bcco_313_top_25_vol_fraction_past_63(high, low, close, volume).diff().diff().diff()


def f49_bcco_314_top_25_vol_fraction_past_252_d3(high, low, close, volume):
    return f49_bcco_314_top_25_vol_fraction_past_252(high, low, close, volume).diff().diff().diff()


def f49_bcco_315_peak_vol_day_position_21_d3(high, low, close, volume):
    return f49_bcco_315_peak_vol_day_position_21(high, low, close, volume).diff().diff().diff()


def f49_bcco_316_peak_vol_day_position_63_d3(high, low, close, volume):
    return f49_bcco_316_peak_vol_day_position_63(high, low, close, volume).diff().diff().diff()


def f49_bcco_317_cum_vol_from_21d_low_d3(low, volume):
    return f49_bcco_317_cum_vol_from_21d_low(low, volume).diff().diff().diff()


def f49_bcco_318_cum_vol_from_21d_low_fraction_d3(low, volume):
    return f49_bcco_318_cum_vol_from_21d_low_fraction(low, volume).diff().diff().diff()


def f49_bcco_319_new_252d_high_and_ret21_over_30pct_and_vol_z_d3(high, close, volume):
    return f49_bcco_319_new_252d_high_and_ret21_over_30pct_and_vol_z(high, close, volume).diff().diff().diff()


def f49_bcco_320_new_252d_high_and_5pct_pullback_from_recent_high_d3(high, close):
    return f49_bcco_320_new_252d_high_and_5pct_pullback_from_recent_high(high, close).diff().diff().diff()


def f49_bcco_321_new_252d_high_and_williams_r_above_neg5_d3(high, low, close):
    return f49_bcco_321_new_252d_high_and_williams_r_above_neg5(high, low, close).diff().diff().diff()


def f49_bcco_322_new_252d_high_and_coppock_positive_and_rising_d3(high, close):
    return f49_bcco_322_new_252d_high_and_coppock_positive_and_rising(high, close).diff().diff().diff()


def f49_bcco_323_new_252d_high_and_kst_positive_and_rising_d3(high, close):
    return f49_bcco_323_new_252d_high_and_kst_positive_and_rising(high, close).diff().diff().diff()


def f49_bcco_324_new_252d_high_and_choppiness_below_38_d3(high, low, close):
    return f49_bcco_324_new_252d_high_and_choppiness_below_38(high, low, close).diff().diff().diff()


def f49_bcco_325_new_252d_high_and_adx_over_40_d3(high, low, close):
    return f49_bcco_325_new_252d_high_and_adx_over_40(high, low, close).diff().diff().diff()


def f49_bcco_326_new_252d_high_and_adx_over_50_d3(high, low, close):
    return f49_bcco_326_new_252d_high_and_adx_over_50(high, low, close).diff().diff().diff()


def f49_bcco_327_new_252d_high_and_aroon_up_100_d3(high):
    return f49_bcco_327_new_252d_high_and_aroon_up_100(high).diff().diff().diff()


def f49_bcco_328_new_252d_high_and_dmi_diff_over_30_d3(high, low, close):
    return f49_bcco_328_new_252d_high_and_dmi_diff_over_30(high, low, close).diff().diff().diff()


def f49_bcco_329_new_252d_high_and_vortex_pos_above_neg_extreme_d3(high, low, close):
    return f49_bcco_329_new_252d_high_and_vortex_pos_above_neg_extreme(high, low, close).diff().diff().diff()


def f49_bcco_330_new_252d_high_and_mass_index_above_27_d3(high, low):
    return f49_bcco_330_new_252d_high_and_mass_index_above_27(high, low).diff().diff().diff()


def f49_bcco_331_new_252d_high_and_kvo_above_signal_d3(high, low, close, volume):
    return f49_bcco_331_new_252d_high_and_kvo_above_signal(high, low, close, volume).diff().diff().diff()


def f49_bcco_332_new_252d_high_and_force_index_z_over_2_d3(close, volume, high):
    return f49_bcco_332_new_252d_high_and_force_index_z_over_2(close, volume, high).diff().diff().diff()


def f49_bcco_333_new_252d_high_and_obv_at_252d_max_d3(close, volume, high):
    return f49_bcco_333_new_252d_high_and_obv_at_252d_max(close, volume, high).diff().diff().diff()


def f49_bcco_334_new_252d_high_and_obv_at_504d_max_d3(close, volume, high):
    return f49_bcco_334_new_252d_high_and_obv_at_504d_max(close, volume, high).diff().diff().diff()


def f49_bcco_335_marubozu_at_new_21d_high_d3(open_, high, low, close):
    return f49_bcco_335_marubozu_at_new_21d_high(open_, high, low, close).diff().diff().diff()


def f49_bcco_336_spinning_top_after_3_strong_close_d3(high, low, open_, close):
    return f49_bcco_336_spinning_top_after_3_strong_close(high, low, open_, close).diff().diff().diff()


def f49_bcco_337_three_line_strike_at_new_high_d3(open_, close, high):
    return f49_bcco_337_three_line_strike_at_new_high(open_, close, high).diff().diff().diff()


def f49_bcco_338_bullish_then_bearish_2bar_at_new_high_d3(open_, close, high):
    return f49_bcco_338_bullish_then_bearish_2bar_at_new_high(open_, close, high).diff().diff().diff()


def f49_bcco_339_belt_hold_bullish_at_new_252d_high_d3(open_, high, low, close):
    return f49_bcco_339_belt_hold_bullish_at_new_252d_high(open_, high, low, close).diff().diff().diff()


def f49_bcco_340_kicker_bullish_at_new_252d_high_d3(open_, close, high):
    return f49_bcco_340_kicker_bullish_at_new_252d_high(open_, close, high).diff().diff().diff()


def f49_bcco_341_upside_tasuki_gap_at_new_high_d3(open_, high, low, close):
    return f49_bcco_341_upside_tasuki_gap_at_new_high(open_, high, low, close).diff().diff().diff()


def f49_bcco_342_ha_bullish_to_bearish_flip_at_new_252d_high_d3(open_, high, low, close):
    return f49_bcco_342_ha_bullish_to_bearish_flip_at_new_252d_high(open_, high, low, close).diff().diff().diff()


def f49_bcco_343_td_9_setup_count_with_new_252d_high_d3(close, high):
    return f49_bcco_343_td_9_setup_count_with_new_252d_high(close, high).diff().diff().diff()


def f49_bcco_344_td_9_setup_count_252_d3(close):
    return f49_bcco_344_td_9_setup_count_252(close).diff().diff().diff()


def f49_bcco_345_new_252d_high_and_td_13_countdown_proxy_d3(close, high):
    return f49_bcco_345_new_252d_high_and_td_13_countdown_proxy(close, high).diff().diff().diff()


def f49_bcco_346_td_13_proxy_count_252_d3(close, high):
    return f49_bcco_346_td_13_proxy_count_252(close, high).diff().diff().diff()


def f49_bcco_347_close_above_high_4_ago_streak_d3(close, high):
    return f49_bcco_347_close_above_high_4_ago_streak(close, high).diff().diff().diff()


def f49_bcco_348_td_perfected_setup_proxy_d3(high, low, close):
    return f49_bcco_348_td_perfected_setup_proxy(high, low, close).diff().diff().diff()


def f49_bcco_349_reverse_td_9_setup_count_252_d3(close):
    return f49_bcco_349_reverse_td_9_setup_count_252(close).diff().diff().diff()


def f49_bcco_350_td_sequential_top_signals_count_252_d3(close, high):
    return f49_bcco_350_td_sequential_top_signals_count_252(close, high).diff().diff().diff()


def f49_bcco_351_new_252d_high_and_252_slope_sign_flip_d3(high, close):
    return f49_bcco_351_new_252d_high_and_252_slope_sign_flip(high, close).diff().diff().diff()


def f49_bcco_352_new_252d_high_and_63_slope_sign_flip_d3(high, close):
    return f49_bcco_352_new_252d_high_and_63_slope_sign_flip(high, close).diff().diff().diff()


def f49_bcco_353_williams_fractal_high_at_new_252d_high_d3(high):
    return f49_bcco_353_williams_fractal_high_at_new_252d_high(high).diff().diff().diff()


def f49_bcco_354_fractal_high_count_63_d3(high):
    return f49_bcco_354_fractal_high_count_63(high).diff().diff().diff()


def f49_bcco_355_fractal_high_count_252_d3(high):
    return f49_bcco_355_fractal_high_count_252(high).diff().diff().diff()


def f49_bcco_356_peak_density_past_21_d3(high):
    return f49_bcco_356_peak_density_past_21(high).diff().diff().diff()


def f49_bcco_357_bars_since_last_fractal_high_d3(high):
    return f49_bcco_357_bars_since_last_fractal_high(high).diff().diff().diff()


def f49_bcco_358_longest_down_streak_after_fractal_high_d3(close, high):
    return f49_bcco_358_longest_down_streak_after_fractal_high(close, high).diff().diff().diff()


def f49_bcco_359_new_252d_high_and_rsi_80_stoch_80_cci_200_d3(high, low, close):
    return f49_bcco_359_new_252d_high_and_rsi_80_stoch_80_cci_200(high, low, close).diff().diff().diff()


def f49_bcco_360_new_252d_high_and_rsi_70_macd_hist_top_decile_vol_z_d3(high, close, volume):
    return f49_bcco_360_new_252d_high_and_rsi_70_macd_hist_top_decile_vol_z(high, close, volume).diff().diff().diff()


def f49_bcco_361_new_252d_high_and_close_over_15x_sma200_rsi_80_d3(high, close):
    return f49_bcco_361_new_252d_high_and_close_over_15x_sma200_rsi_80(high, close).diff().diff().diff()


def f49_bcco_362_new_252d_high_and_in_top_10pct_of_252d_range_d3(high, low, close):
    return f49_bcco_362_new_252d_high_and_in_top_10pct_of_252d_range(high, low, close).diff().diff().diff()


def f49_bcco_363_four_of_five_momentum_at_252d_max_d3(high, low, close, volume):
    return f49_bcco_363_four_of_five_momentum_at_252d_max(high, low, close, volume).diff().diff().diff()


def f49_bcco_364_new_252d_high_atr_252d_max_rsi_70_vol_z_d3(high, low, close, volume):
    return f49_bcco_364_new_252d_high_atr_252d_max_rsi_70_vol_z(high, low, close, volume).diff().diff().diff()


def f49_bcco_365_connors_rsi_above_95_and_new_252d_high_d3(close, high):
    return f49_bcco_365_connors_rsi_above_95_and_new_252d_high(close, high).diff().diff().diff()


def f49_bcco_366_schaff_trend_cycle_above_90_at_new_high_d3(close, high):
    return f49_bcco_366_schaff_trend_cycle_above_90_at_new_high(close, high).diff().diff().diff()


def f49_bcco_367_vortex_pos_at_252d_max_and_new_high_d3(high, low, close):
    return f49_bcco_367_vortex_pos_at_252d_max_and_new_high(high, low, close).diff().diff().diff()


def f49_bcco_368_mass_index_extreme_and_new_high_d3(high, low, close):
    return f49_bcco_368_mass_index_extreme_and_new_high(high, low, close).diff().diff().diff()


def f49_bcco_369_vol_of_vol_at_252d_max_and_new_high_d3(close, high):
    return f49_bcco_369_vol_of_vol_at_252d_max_and_new_high(close, high).diff().diff().diff()


def f49_bcco_370_vol_of_vol_pct_rank_over_90_and_new_high_d3(close, high):
    return f49_bcco_370_vol_of_vol_pct_rank_over_90_and_new_high(close, high).diff().diff().diff()


def f49_bcco_371_realized_vol_21_at_252d_max_and_new_high_d3(close, high):
    return f49_bcco_371_realized_vol_21_at_252d_max_and_new_high(close, high).diff().diff().diff()


def f49_bcco_372_atr_pct_rank_99_and_new_high_d3(high, low, close):
    return f49_bcco_372_atr_pct_rank_99_and_new_high(high, low, close).diff().diff().diff()


def f49_bcco_373_vol_horizons_stacking_and_new_high_d3(close, high):
    return f49_bcco_373_vol_horizons_stacking_and_new_high(close, high).diff().diff().diff()


def f49_bcco_374_all_vol_horizons_top_decile_and_new_high_d3(close, high):
    return f49_bcco_374_all_vol_horizons_top_decile_and_new_high(close, high).diff().diff().diff()


def f49_bcco_375_5d_realized_vol_zscore_over_3_and_new_high_d3(close, high):
    return f49_bcco_375_5d_realized_vol_zscore_over_3_and_new_high(close, high).diff().diff().diff()


_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_HCV = ["high", "close", "volume"]
_HV = ["high", "volume"]
_OC = ["open", "close"]
_OHC = ["open", "high", "close"]
_OHLC = ["open", "high", "low", "close"]
_LV = ["low", "volume"]
_OHLCV = ["open", "high", "low", "close", "volume"]


BLOWOFF_CLIMAX_COMPOSITE_D3_REGISTRY_301_375 = {
    "f49_bcco_301_golden_cross_within_21_and_new_252d_high_d3": {"inputs": _HC, "func": f49_bcco_301_golden_cross_within_21_and_new_252d_high_d3},
    "f49_bcco_302_golden_cross_count_252_d3": {"inputs": ["close"], "func": f49_bcco_302_golden_cross_count_252_d3},
    "f49_bcco_303_short_cross_above_medium_and_new_21d_high_d3": {"inputs": _HC, "func": f49_bcco_303_short_cross_above_medium_and_new_21d_high_d3},
    "f49_bcco_304_short_cross_count_with_new_high_63_d3": {"inputs": _HC, "func": f49_bcco_304_short_cross_count_with_new_high_63_d3},
    "f49_bcco_305_macd_signal_cross_and_new_252d_high_d3": {"inputs": _HC, "func": f49_bcco_305_macd_signal_cross_and_new_252d_high_d3},
    "f49_bcco_306_psar_flip_up_and_new_252d_high_d3": {"inputs": _HLC, "func": f49_bcco_306_psar_flip_up_and_new_252d_high_d3},
    "f49_bcco_307_supertrend_flip_up_and_new_high_d3": {"inputs": _HLC, "func": f49_bcco_307_supertrend_flip_up_and_new_high_d3},
    "f49_bcco_308_full_ma_stack_and_new_252d_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_308_full_ma_stack_and_new_252d_high_d3},
    "f49_bcco_309_full_ma_stack_and_rsi_above_70_d3": {"inputs": ["close"], "func": f49_bcco_309_full_ma_stack_and_rsi_above_70_d3},
    "f49_bcco_310_full_ma_stack_and_vol_z_2_and_new_high_d3": {"inputs": _HCV, "func": f49_bcco_310_full_ma_stack_and_vol_z_2_and_new_high_d3},
    "f49_bcco_311_vol_in_top_25pct_21d_range_past_63_d3": {"inputs": _HLCV, "func": f49_bcco_311_vol_in_top_25pct_21d_range_past_63_d3},
    "f49_bcco_312_vol_in_top_25pct_252d_range_past_252_d3": {"inputs": _HLCV, "func": f49_bcco_312_vol_in_top_25pct_252d_range_past_252_d3},
    "f49_bcco_313_top_25_vol_fraction_past_63_d3": {"inputs": _HLCV, "func": f49_bcco_313_top_25_vol_fraction_past_63_d3},
    "f49_bcco_314_top_25_vol_fraction_past_252_d3": {"inputs": _HLCV, "func": f49_bcco_314_top_25_vol_fraction_past_252_d3},
    "f49_bcco_315_peak_vol_day_position_21_d3": {"inputs": _HLCV, "func": f49_bcco_315_peak_vol_day_position_21_d3},
    "f49_bcco_316_peak_vol_day_position_63_d3": {"inputs": _HLCV, "func": f49_bcco_316_peak_vol_day_position_63_d3},
    "f49_bcco_317_cum_vol_from_21d_low_d3": {"inputs": _LV, "func": f49_bcco_317_cum_vol_from_21d_low_d3},
    "f49_bcco_318_cum_vol_from_21d_low_fraction_d3": {"inputs": _LV, "func": f49_bcco_318_cum_vol_from_21d_low_fraction_d3},
    "f49_bcco_319_new_252d_high_and_ret21_over_30pct_and_vol_z_d3": {"inputs": _HCV, "func": f49_bcco_319_new_252d_high_and_ret21_over_30pct_and_vol_z_d3},
    "f49_bcco_320_new_252d_high_and_5pct_pullback_from_recent_high_d3": {"inputs": _HC, "func": f49_bcco_320_new_252d_high_and_5pct_pullback_from_recent_high_d3},
    "f49_bcco_321_new_252d_high_and_williams_r_above_neg5_d3": {"inputs": _HLC, "func": f49_bcco_321_new_252d_high_and_williams_r_above_neg5_d3},
    "f49_bcco_322_new_252d_high_and_coppock_positive_and_rising_d3": {"inputs": _HC, "func": f49_bcco_322_new_252d_high_and_coppock_positive_and_rising_d3},
    "f49_bcco_323_new_252d_high_and_kst_positive_and_rising_d3": {"inputs": _HC, "func": f49_bcco_323_new_252d_high_and_kst_positive_and_rising_d3},
    "f49_bcco_324_new_252d_high_and_choppiness_below_38_d3": {"inputs": _HLC, "func": f49_bcco_324_new_252d_high_and_choppiness_below_38_d3},
    "f49_bcco_325_new_252d_high_and_adx_over_40_d3": {"inputs": _HLC, "func": f49_bcco_325_new_252d_high_and_adx_over_40_d3},
    "f49_bcco_326_new_252d_high_and_adx_over_50_d3": {"inputs": _HLC, "func": f49_bcco_326_new_252d_high_and_adx_over_50_d3},
    "f49_bcco_327_new_252d_high_and_aroon_up_100_d3": {"inputs": ["high"], "func": f49_bcco_327_new_252d_high_and_aroon_up_100_d3},
    "f49_bcco_328_new_252d_high_and_dmi_diff_over_30_d3": {"inputs": _HLC, "func": f49_bcco_328_new_252d_high_and_dmi_diff_over_30_d3},
    "f49_bcco_329_new_252d_high_and_vortex_pos_above_neg_extreme_d3": {"inputs": _HLC, "func": f49_bcco_329_new_252d_high_and_vortex_pos_above_neg_extreme_d3},
    "f49_bcco_330_new_252d_high_and_mass_index_above_27_d3": {"inputs": ["high", "low"], "func": f49_bcco_330_new_252d_high_and_mass_index_above_27_d3},
    "f49_bcco_331_new_252d_high_and_kvo_above_signal_d3": {"inputs": _HLCV, "func": f49_bcco_331_new_252d_high_and_kvo_above_signal_d3},
    "f49_bcco_332_new_252d_high_and_force_index_z_over_2_d3": {"inputs": ["close", "volume", "high"], "func": f49_bcco_332_new_252d_high_and_force_index_z_over_2_d3},
    "f49_bcco_333_new_252d_high_and_obv_at_252d_max_d3": {"inputs": ["close", "volume", "high"], "func": f49_bcco_333_new_252d_high_and_obv_at_252d_max_d3},
    "f49_bcco_334_new_252d_high_and_obv_at_504d_max_d3": {"inputs": ["close", "volume", "high"], "func": f49_bcco_334_new_252d_high_and_obv_at_504d_max_d3},
    "f49_bcco_335_marubozu_at_new_21d_high_d3": {"inputs": _OHLC, "func": f49_bcco_335_marubozu_at_new_21d_high_d3},
    "f49_bcco_336_spinning_top_after_3_strong_close_d3": {"inputs": ["high", "low", "open", "close"], "func": f49_bcco_336_spinning_top_after_3_strong_close_d3},
    "f49_bcco_337_three_line_strike_at_new_high_d3": {"inputs": ["open", "close", "high"], "func": f49_bcco_337_three_line_strike_at_new_high_d3},
    "f49_bcco_338_bullish_then_bearish_2bar_at_new_high_d3": {"inputs": ["open", "close", "high"], "func": f49_bcco_338_bullish_then_bearish_2bar_at_new_high_d3},
    "f49_bcco_339_belt_hold_bullish_at_new_252d_high_d3": {"inputs": _OHLC, "func": f49_bcco_339_belt_hold_bullish_at_new_252d_high_d3},
    "f49_bcco_340_kicker_bullish_at_new_252d_high_d3": {"inputs": ["open", "close", "high"], "func": f49_bcco_340_kicker_bullish_at_new_252d_high_d3},
    "f49_bcco_341_upside_tasuki_gap_at_new_high_d3": {"inputs": _OHLC, "func": f49_bcco_341_upside_tasuki_gap_at_new_high_d3},
    "f49_bcco_342_ha_bullish_to_bearish_flip_at_new_252d_high_d3": {"inputs": _OHLC, "func": f49_bcco_342_ha_bullish_to_bearish_flip_at_new_252d_high_d3},
    "f49_bcco_343_td_9_setup_count_with_new_252d_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_343_td_9_setup_count_with_new_252d_high_d3},
    "f49_bcco_344_td_9_setup_count_252_d3": {"inputs": ["close"], "func": f49_bcco_344_td_9_setup_count_252_d3},
    "f49_bcco_345_new_252d_high_and_td_13_countdown_proxy_d3": {"inputs": ["close", "high"], "func": f49_bcco_345_new_252d_high_and_td_13_countdown_proxy_d3},
    "f49_bcco_346_td_13_proxy_count_252_d3": {"inputs": ["close", "high"], "func": f49_bcco_346_td_13_proxy_count_252_d3},
    "f49_bcco_347_close_above_high_4_ago_streak_d3": {"inputs": ["close", "high"], "func": f49_bcco_347_close_above_high_4_ago_streak_d3},
    "f49_bcco_348_td_perfected_setup_proxy_d3": {"inputs": _HLC, "func": f49_bcco_348_td_perfected_setup_proxy_d3},
    "f49_bcco_349_reverse_td_9_setup_count_252_d3": {"inputs": ["close"], "func": f49_bcco_349_reverse_td_9_setup_count_252_d3},
    "f49_bcco_350_td_sequential_top_signals_count_252_d3": {"inputs": ["close", "high"], "func": f49_bcco_350_td_sequential_top_signals_count_252_d3},
    "f49_bcco_351_new_252d_high_and_252_slope_sign_flip_d3": {"inputs": _HC, "func": f49_bcco_351_new_252d_high_and_252_slope_sign_flip_d3},
    "f49_bcco_352_new_252d_high_and_63_slope_sign_flip_d3": {"inputs": _HC, "func": f49_bcco_352_new_252d_high_and_63_slope_sign_flip_d3},
    "f49_bcco_353_williams_fractal_high_at_new_252d_high_d3": {"inputs": ["high"], "func": f49_bcco_353_williams_fractal_high_at_new_252d_high_d3},
    "f49_bcco_354_fractal_high_count_63_d3": {"inputs": ["high"], "func": f49_bcco_354_fractal_high_count_63_d3},
    "f49_bcco_355_fractal_high_count_252_d3": {"inputs": ["high"], "func": f49_bcco_355_fractal_high_count_252_d3},
    "f49_bcco_356_peak_density_past_21_d3": {"inputs": ["high"], "func": f49_bcco_356_peak_density_past_21_d3},
    "f49_bcco_357_bars_since_last_fractal_high_d3": {"inputs": ["high"], "func": f49_bcco_357_bars_since_last_fractal_high_d3},
    "f49_bcco_358_longest_down_streak_after_fractal_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_358_longest_down_streak_after_fractal_high_d3},
    "f49_bcco_359_new_252d_high_and_rsi_80_stoch_80_cci_200_d3": {"inputs": _HLC, "func": f49_bcco_359_new_252d_high_and_rsi_80_stoch_80_cci_200_d3},
    "f49_bcco_360_new_252d_high_and_rsi_70_macd_hist_top_decile_vol_z_d3": {"inputs": _HCV, "func": f49_bcco_360_new_252d_high_and_rsi_70_macd_hist_top_decile_vol_z_d3},
    "f49_bcco_361_new_252d_high_and_close_over_15x_sma200_rsi_80_d3": {"inputs": _HC, "func": f49_bcco_361_new_252d_high_and_close_over_15x_sma200_rsi_80_d3},
    "f49_bcco_362_new_252d_high_and_in_top_10pct_of_252d_range_d3": {"inputs": _HLC, "func": f49_bcco_362_new_252d_high_and_in_top_10pct_of_252d_range_d3},
    "f49_bcco_363_four_of_five_momentum_at_252d_max_d3": {"inputs": _HLCV, "func": f49_bcco_363_four_of_five_momentum_at_252d_max_d3},
    "f49_bcco_364_new_252d_high_atr_252d_max_rsi_70_vol_z_d3": {"inputs": _HLCV, "func": f49_bcco_364_new_252d_high_atr_252d_max_rsi_70_vol_z_d3},
    "f49_bcco_365_connors_rsi_above_95_and_new_252d_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_365_connors_rsi_above_95_and_new_252d_high_d3},
    "f49_bcco_366_schaff_trend_cycle_above_90_at_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_366_schaff_trend_cycle_above_90_at_new_high_d3},
    "f49_bcco_367_vortex_pos_at_252d_max_and_new_high_d3": {"inputs": _HLC, "func": f49_bcco_367_vortex_pos_at_252d_max_and_new_high_d3},
    "f49_bcco_368_mass_index_extreme_and_new_high_d3": {"inputs": _HLC, "func": f49_bcco_368_mass_index_extreme_and_new_high_d3},
    "f49_bcco_369_vol_of_vol_at_252d_max_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_369_vol_of_vol_at_252d_max_and_new_high_d3},
    "f49_bcco_370_vol_of_vol_pct_rank_over_90_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_370_vol_of_vol_pct_rank_over_90_and_new_high_d3},
    "f49_bcco_371_realized_vol_21_at_252d_max_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_371_realized_vol_21_at_252d_max_and_new_high_d3},
    "f49_bcco_372_atr_pct_rank_99_and_new_high_d3": {"inputs": _HLC, "func": f49_bcco_372_atr_pct_rank_99_and_new_high_d3},
    "f49_bcco_373_vol_horizons_stacking_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_373_vol_horizons_stacking_and_new_high_d3},
    "f49_bcco_374_all_vol_horizons_top_decile_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_374_all_vol_horizons_top_decile_and_new_high_d3},
    "f49_bcco_375_5d_realized_vol_zscore_over_3_and_new_high_d3": {"inputs": ["close", "high"], "func": f49_bcco_375_5d_realized_vol_zscore_over_3_and_new_high_d3},
}
