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


def _vroc(vol, n):
    return _safe_div(vol - vol.shift(n), vol.shift(n))


def _pivot_high_event(high, lookback=3):
    n = len(high)
    arr = high.values
    out = np.zeros(n, dtype=float)
    for i in range(lookback, n - lookback):
        win = arr[i - lookback:i + lookback + 1]
        if np.isnan(win).any():
            continue
        if arr[i] == win.max() and (win == arr[i]).sum() == 1:
            if i + lookback < n:
                out[i + lookback] = 1.0
    return pd.Series(out, index=high.index)


def _pivot_low_event(low, lookback=3):
    n = len(low)
    arr = low.values
    out = np.zeros(n, dtype=float)
    for i in range(lookback, n - lookback):
        win = arr[i - lookback:i + lookback + 1]
        if np.isnan(win).any():
            continue
        if arr[i] == win.min() and (win == arr[i]).sum() == 1:
            if i + lookback < n:
                out[i + lookback] = 1.0
    return pd.Series(out, index=low.index)


def _bbands(close, n=20, k=2.0):
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    upper = m + k * sd
    lower = m - k * sd
    width = (upper - lower) / m.replace(0, np.nan)
    return upper, lower, width


def _keltner(high, low, close, n=20, k=2.0):
    m = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n=n)
    return m + k * atr, m - k * atr


def f20_vdah_301_minervini_vcp_contraction_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9)
    h = high.values; l = low.values; n = len(h)
    out = np.full(n, np.nan, dtype=float)
    for i in range(QDAYS - 1, n):
        if not bool(in_top.iat[i]) or np.isnan(h[i]) or np.isnan(l[i]):
            continue
        segs = []
        for s0 in range(i - QDAYS + 1, i + 1, MDAYS):
            s1 = min(s0 + MDAYS, i + 1)
            hi = h[s0:s1]; lo = l[s0:s1]
            if hi.size == 0 or np.isnan(hi).all() or np.isnan(lo).all():
                continue
            r = np.nanmax(hi) - np.nanmin(lo)
            segs.append(r)
        if len(segs) < 2:
            out[i] = 0.0
            continue
        c = 0
        for j in range(1, len(segs)):
            if segs[j - 1] > 0 and segs[j] <= 0.9 * segs[j - 1]:
                c += 1
        out[i] = float(c)
    return pd.Series(out, index=close.index)


def f20_vdah_302_minervini_vcp_each_contraction_vol_lower_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9)
    v = volume.values; n = len(v)
    out = np.full(n, np.nan, dtype=float)
    for i in range(QDAYS - 1, n):
        if not bool(in_top.iat[i]):
            continue
        means = []
        for s0 in range(i - QDAYS + 1, i + 1, MDAYS):
            s1 = min(s0 + MDAYS, i + 1)
            seg = v[s0:s1]
            if seg.size == 0 or np.isnan(seg).all():
                continue
            means.append(np.nanmean(seg))
        if len(means) < 2:
            continue
        ok = all(means[j] < means[j - 1] for j in range(1, len(means)))
        out[i] = 1.0 if ok else 0.0
    return pd.Series(out, index=close.index)


def f20_vdah_303_minervini_vcp_final_pivot_vol_pct_rank_63d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9)
    piv_mean = volume.rolling(WDAYS, min_periods=2).mean()
    rnk = _rolling_pct_rank(piv_mean, QDAYS)
    return rnk.where(in_top, np.nan)


def f20_vdah_304_oneil_handle_low_vol_dryup_score(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9)
    handle = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cup = volume.shift(MDAYS).rolling(84, min_periods=MDAYS).mean()
    out = _safe_div(handle, cup)
    return out.where(in_top, np.nan)


def f20_vdah_305_oneil_three_weeks_tight_low_vol_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    wk_max = close.rolling(WDAYS, min_periods=2).max()
    wk_min = close.rolling(WDAYS, min_periods=2).min()
    rng = _safe_div(wk_max - wk_min, wk_min)
    tight = (rng <= 0.01)
    three_tight = tight.rolling(15, min_periods=10).sum() >= 12
    v_wk = volume.rolling(WDAYS, min_periods=2).mean()
    v_med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_vol = v_wk < v_med
    return (three_tight & low_vol).astype(float).where(tight.notna(), np.nan)


def f20_vdah_306_kacher_undercut_dryup_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    piv = _pivot_low_event(low, lookback=3)
    last_piv_low = low.where(piv > 0).ffill().shift(1)
    undercut = (low < last_piv_low) & (low >= 0.98 * last_piv_low)
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < 0.6 * v_med
    return (undercut & low_vol).astype(float).where(v_med.notna() & last_piv_low.notna(), np.nan)


def f20_vdah_307_kacher_inverse_pocket_pivot_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_up = (close > close.shift(1)).values
    is_dn = (close < close.shift(1)).values
    v = volume.values; n = len(close)
    out = np.full(n, np.nan, dtype=float)
    for i in range(10, n):
        dn_vols = []
        j = i - 1
        while j >= 0 and len(dn_vols) < 10:
            if is_dn[j] and not np.isnan(v[j]):
                dn_vols.append(v[j])
            j -= 1
        if len(dn_vols) < 10:
            continue
        out[i] = 1.0 if (is_up[i] and not np.isnan(v[i]) and v[i] < min(dn_vols)) else 0.0
    s = pd.Series(out, index=close.index)
    return s.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_308_williams_vsa_no_demand_after_upthrust_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    narrow = rng < 0.7 * atr21
    pos_in_bar = _safe_div(close - low, rng)
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < v_med
    no_demand = narrow & (pos_in_bar >= 0.5) & low_vol
    rmax21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pierce = high > rmax21
    high_vol = volume > 1.5 * v_med
    upthrust = pierce & (pos_in_bar < 0.5) & high_vol
    ut5 = upthrust.shift(1).rolling(WDAYS, min_periods=1).max().fillna(0)
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * rmax252
    out = (no_demand & (ut5 > 0) & at_top).astype(float)
    return out.where(volume.notna(), np.nan)


def f20_vdah_309_williams_squat_bar_indicator(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_max5 = volume.rolling(WDAYS, min_periods=2).max()
    rng = high - low
    q20_5 = rng.rolling(WDAYS, min_periods=2).quantile(0.2)
    return ((volume >= v_max5) & (rng <= q20_5)).astype(float).where(v_max5.notna(), np.nan)


def f20_vdah_310_williams_squat_count_at_252d_high_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_max5 = volume.rolling(WDAYS, min_periods=2).max()
    rng = high - low
    q20_5 = rng.rolling(WDAYS, min_periods=2).quantile(0.2)
    squat = (volume >= v_max5) & (rng <= q20_5)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * rmax
    return (squat & at_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_311_williams_two_bar_reversal_low_vol_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    yest_up_wide = (close.shift(1) > close.shift(2)) & (rng.shift(1) > 1.2 * atr21)
    today_dn_narrow = (close < close.shift(1)) & (rng < 0.8 * atr21)
    lower_vol = volume < volume.shift(1)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high.shift(1) >= 0.95 * rmax.shift(1)
    return (yest_up_wide & today_dn_narrow & lower_vol & at_top).astype(float).where(atr21.notna(), np.nan)


def f20_vdah_312_coulling_background_volume_compression_ratio(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v20 = volume.rolling(20, min_periods=10).mean()
    v60 = volume.rolling(60, min_periods=20).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = high >= 0.99 * rmax
    return _safe_div(v20, v60).where(at_high, np.nan)


def _weis_pivots(s: pd.Series, lookback: int = 3) -> np.ndarray:
    ph = _pivot_high_event(s, lookback=lookback).values
    pl = _pivot_low_event(s, lookback=lookback).values
    n = len(s)
    ev = np.zeros(n, dtype=int)
    for i in range(n):
        if ph[i] > 0:
            ev[i] = 1
        elif pl[i] > 0:
            ev[i] = -1
    return ev


def f20_vdah_313_weis_wave_up_wave_volume_minus_down_wave_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ev = _weis_pivots(close, lookback=3)
    v = volume.values; n = len(close)
    out = np.full(n, np.nan, dtype=float)
    for i in range(QDAYS - 1, n):
        up_sum = 0.0; dn_sum = 0.0; cd = 0; sv = 0.0
        for k in range(i - QDAYS + 1, i + 1):
            if not np.isnan(v[k]):
                sv += v[k]
            if ev[k] == 1 and cd == -1:
                up_sum += sv; sv = 0.0; cd = 1
            elif ev[k] == -1 and cd == 1:
                dn_sum += sv; sv = 0.0; cd = -1
            elif ev[k] != 0 and cd == 0:
                cd = ev[k]; sv = 0.0
        out[i] = up_sum - dn_sum
    return pd.Series(out, index=close.index)


def f20_vdah_314_weis_wave_up_vol_decline_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    ev = _weis_pivots(close, lookback=3)
    v = volume.values; n = len(close)
    uv = []; ue = []
    cd = 0; sv = 0.0
    for k in range(n):
        if not np.isnan(v[k]):
            sv += v[k]
        if ev[k] == 1 and cd == -1:
            uv.append(sv); ue.append(k); sv = 0.0; cd = 1
        elif ev[k] == -1 and cd == 1:
            sv = 0.0; cd = -1
        elif ev[k] != 0 and cd == 0:
            cd = ev[k]; sv = 0.0
    out = np.full(n, np.nan, dtype=float)
    streak = 0; j = 0
    for i in range(n):
        while j < len(ue) and ue[j] <= i:
            streak = (streak + 1) if (j > 0 and uv[j] < uv[j - 1]) else (0 if j == 0 else 0)
            j += 1
        if j > 0:
            out[i] = float(streak)
    return pd.Series(out, index=close.index)


def f20_vdah_315_weis_wave_last_up_wave_vol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ev = _weis_pivots(close, lookback=3)
    v = volume.values; n = len(close)
    luv = np.full(n, np.nan, dtype=float)
    cd = 0; sv = 0.0; cur = np.nan
    for k in range(n):
        if not np.isnan(v[k]):
            sv += v[k]
        if ev[k] == 1 and cd == -1:
            cur = sv; sv = 0.0; cd = 1
        elif ev[k] == -1 and cd == 1:
            sv = 0.0; cd = -1
        elif ev[k] != 0 and cd == 0:
            cd = ev[k]; sv = 0.0
        luv[k] = cur
    return _rolling_pct_rank(pd.Series(luv, index=close.index), YDAYS)


def f20_vdah_316_wyckoff_phase_b_creek_low_vol_test_count(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    piv_h = _pivot_high_event(high, lookback=3)
    last_piv_high = high.where(piv_h > 0).ffill().shift(1)
    atr21 = _atr(high, low, high, n=MDAYS)
    probe = (high > last_piv_high) & (high < last_piv_high + atr21)
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med
    return (probe & quiet).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_317_wyckoff_sign_of_weakness_volume_to_jump_volume_ratio(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    sow = close < (rmin + 0.1 * (rmax - rmin))
    ret = close.pct_change()
    joc_max = ret.rolling(MDAYS, min_periods=WDAYS).max()
    joc_bar = (ret == joc_max)
    joc_vol = volume.where(joc_bar).ffill(limit=MDAYS)
    sow_vol = volume.where(sow)
    return _safe_div(sow_vol, joc_vol).ffill(limit=QDAYS)


def f20_vdah_318_wyckoff_automatic_reaction_dryup_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    v_max = volume.rolling(YDAYS, min_periods=QDAYS).max()
    rng = high - low
    bc_bar = volume >= v_max
    climax_vol = volume.where(bc_bar).ffill(limit=QDAYS)
    climax_rng = rng.where(bc_bar).ffill(limit=QDAYS)
    is_dn = close < close.shift(1)
    cond = is_dn & (volume < 0.5 * climax_vol) & (rng < 0.5 * climax_rng)
    return cond.astype(float).where(climax_vol.notna(), np.nan)


def f20_vdah_319_minervini_stage3_topping_vol_signature_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    atr21 = _atr(high, low, close, n=MDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    churn = ((v_z > 0) & (ret < 0.5 * _safe_div(atr21, close))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    rng = high - low
    dist = ((close < close.shift(1)) & (volume > 1.4 * volume.rolling(MDAYS, min_periods=WDAYS).mean()) & (rng > atr21)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(churn + 1.5 * dist, YDAYS)


def f20_vdah_320_oneil_late_stage_base_dryup_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ph = _pivot_high_event(high, lookback=10).values
    v = volume.values; n = len(close)
    out = np.full(n, np.nan, dtype=float)
    cv = volume.rolling(QDAYS, min_periods=MDAYS).mean().values
    for i in range(DDAYS_5Y, n):
        idxs = [k for k in range(i - DDAYS_5Y + 1, i + 1) if ph[k] > 0]
        if len(idxs) < 4:
            continue
        f0 = idxs[0]
        fv = np.nanmean(v[max(0, f0 - QDAYS // 2):min(n, f0 + QDAYS // 2 + 1)])
        out[i] = 1.0 if (not np.isnan(fv) and fv > 0 and cv[i] < 0.7 * fv) else 0.0
    return pd.Series(out, index=close.index)


def f20_vdah_321_oneil_climax_top_followed_by_dryup_3wks(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    climax = (rng > 2 * atr21) & (close > close.shift(1)) & (v_z > 2.0)
    pre_v21 = volume.shift(1).rolling(MDAYS, min_periods=WDAYS).mean()
    last_pre = pre_v21.where(climax).ffill(limit=15)
    post_mean = volume.rolling(15, min_periods=5).mean()
    bars_since = pd.Series(np.where(climax, 0.0, np.nan), index=close.index).ffill(limit=15)
    cond = (post_mean < last_pre) & (bars_since.notna())
    return cond.astype(float).where(last_pre.notna(), np.nan)


def f20_vdah_322_holiday_proximate_dryup_normalization(close: pd.Series, volume: pd.Series) -> pd.Series:
    if not isinstance(close.index, pd.DatetimeIndex):
        return pd.Series(np.nan, index=close.index)
    idx = close.index
    is_holiday_proxy = pd.Series(
        ((idx.month == 12) & (idx.day >= 23))
        | ((idx.month == 7) & (idx.day == 3))
        | ((idx.month == 11) & (idx.weekday == 3) & (idx.day >= 22) & (idx.day <= 28)),
        index=idx,
    )
    mask_vol = volume.where(~is_holiday_proxy)
    m = mask_vol.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = mask_vol.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(volume - m, sd)


def f20_vdah_323_dryup_at_round_number_proximity_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pos_close = close.where(close > 0, np.nan)
    mag = 10 ** np.floor(np.log10(pos_close))
    cols = []
    for m in (0.05, 0.1, 0.25, 0.5, 1.0):
        scale = (m * mag)
        nearest = (close / scale).round() * scale
        cols.append((nearest - close).abs().rename(f"d{m}"))
    candidates = pd.concat(cols, axis=1)
    nearest_dist = candidates.min(axis=1)
    near = _safe_div(nearest_dist, close) < 0.01
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    low_vol = volume < q25
    return (near & low_vol).astype(float).where(q25.notna(), np.nan)


def f20_vdah_324_dryup_at_prior_year_high_proximity_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    anchor = high.shift(YDAYS)
    near = _safe_div((close - anchor).abs(), anchor) < 0.02
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    low_vol = volume < q25
    return (near & low_vol).astype(float).where(anchor.notna() & q25.notna(), np.nan)


def f20_vdah_325_days_since_last_high_vol_at_252d_high(volume: pd.Series, high: pd.Series) -> pd.Series:
    v_z = _rolling_zscore(volume, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ev = (v_z > 1.0) & (high >= 0.95 * rmax)
    n = len(volume); arr = ev.values
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if not np.isnan(rmax.iat[i]):
            if arr[i]:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=volume.index)


def f20_vdah_326_avg_vol_pct_rank_during_top_decile_dwell_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = (pos >= 0.9)
    rnk = _rolling_pct_rank(volume, YDAYS)
    return rnk.where(in_top).rolling(MDAYS, min_periods=WDAYS).mean()


def f20_vdah_327_largest_single_bar_vol_collapse_in_252d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    drop = _safe_div(volume, volume.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_q4 = (pos >= 0.75)
    masked = drop.where(in_q4)
    return -masked.rolling(YDAYS, min_periods=QDAYS).min()


def f20_vdah_328_negative_vroc_event_count_63d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vr = _vroc(volume, WDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return ((vr < -0.5) & (pos >= 0.9)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_329_vol_collapse_then_failed_rally_indicator(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    vr = _vroc(volume, WDAYS)
    drop = vr < -0.5
    atr21 = _atr(high, low, close, n=MDAYS)
    adv = close - close.shift(WDAYS)
    weak_rally = adv < 0.5 * atr21
    return (drop.shift(WDAYS) & weak_rally).astype(float).where(atr21.notna(), np.nan)


def f20_vdah_330_vol_dryup_with_narrow_range_coincidence_63d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    q25_v = _rolling_quantile(volume, YDAYS, 0.25)
    tr = _true_range(high, low, close)
    q25_r = _rolling_quantile(tr, YDAYS, 0.25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    cond = (volume < q25_v) & (tr < q25_r) & (pos >= 0.9)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_331_count_inside_bars_with_low_vol_at_high_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    inside = (high <= high.shift(1)) & (low >= low.shift(1))
    v_med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med21
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div((high + low) / 2 - rmin, rmax - rmin)
    in_top = pos >= 0.9
    return (inside & quiet & in_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_332_count_nr7_low_vol_at_high_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    min7 = rng.rolling(7, min_periods=4).min()
    nr7 = rng <= min7
    v_med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med21
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_top = high >= 0.9 * rmax
    return (nr7 & quiet & in_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_333_nr4_low_vol_streak_at_high(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    min4 = rng.rolling(4, min_periods=3).min()
    nr4 = rng <= min4
    v_med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med21
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_top = high >= 0.9 * rmax
    flag = (nr4 & quiet & in_top)
    streak = _consecutive_true_streak(flag).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_334_consecutive_doji_low_vol_streak(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    body = (close - open_).abs()
    doji = body < 0.1 * rng
    v_med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med21
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_top = high >= 0.9 * rmax
    flag = doji & quiet & in_top
    return _consecutive_true_streak(flag).astype(float)


def f20_vdah_335_post_climax_vol_half_life_in_bars_after_fam19_blowoff(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    climax = (rng > 2 * atr21) & (v_z > 2.0)
    n = len(volume); arr = climax.values
    bs = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            bs[i] = float(i - last)
    lv = _safe_log(volume)
    sl = _rolling_slope(lv, QDAYS)
    hl = -np.log(2.0) / sl
    out = hl.where(sl < 0, np.nan)
    bs_s = pd.Series(bs, index=volume.index)
    return out.where(bs_s <= QDAYS, np.nan)


def f20_vdah_336_post_climax_first_3day_vol_rank_252d(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    climax = (rng > 2 * atr21) & (v_z > 2.0)
    cl3 = climax.shift(3).fillna(False)
    post3 = volume.rolling(3, min_periods=2).mean()
    val = post3.where(cl3)
    return _rolling_pct_rank(val.ffill(limit=QDAYS), YDAYS)


def f20_vdah_337_vol_collapse_rate_21d_over_252d_gated_at_high(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    return _safe_div(v21, v252).where(in_top, np.nan)


def f20_vdah_338_entropy_collapse_rate_21d_over_252d_gated_at_high(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        h, _ = np.histogram(v, bins=np.linspace(v.min(), v.max() + 1e-9, 8))
        s = h.sum()
        if s <= 0:
            return np.nan
        p = h[h > 0] / s
        return float(-(p * np.log(p)).sum()) if p.size > 0 else np.nan
    e21 = lv.rolling(MDAYS, min_periods=WDAYS).apply(_ent, raw=True)
    e252 = lv.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return _safe_div(e21, e252).where(pos >= 0.9, np.nan)


def f20_vdah_339_vol_dryup_during_base_formation_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng_h = high.rolling(45, min_periods=20).max()
    rng_l = low.rolling(45, min_periods=20).min()
    flat = _safe_div(rng_h - rng_l, rng_l) < 0.10
    med_v = volume.rolling(45, min_periods=20).median()
    q20 = _rolling_quantile(volume, YDAYS, 0.20)
    quiet = med_v < q20
    return (flat & quiet).astype(float).where(q20.notna(), np.nan)


def f20_vdah_340_base_handle_vol_to_base_left_side_vol_ratio(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    handle = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    left = volume.shift(84).rolling(42, min_periods=20).mean()
    return _safe_div(handle, left)


def f20_vdah_341_vol_dryup_at_breakout_pivot_with_close_in_upper_third(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h20 = high.shift(1).rolling(20, min_periods=10).max()
    bk = close > h20
    pos_in_bar = _safe_div(close - low, high - low)
    upper3 = pos_in_bar >= (2.0 / 3.0)
    v50 = volume.rolling(50, min_periods=20).mean()
    weak_vol = volume < 1.4 * v50
    return (bk & upper3 & weak_vol).astype(float).where(v50.notna(), np.nan)


def f20_vdah_342_breakout_vol_pct_rank_at_252d_breakout(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > rmax
    rnk = _rolling_pct_rank(volume, YDAYS)
    return rnk.where(new_high).ffill(limit=MDAYS)


def f20_vdah_343_post_breakout_vol_dryup_5d(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > rmax
    pre = volume.shift(1).rolling(MDAYS, min_periods=WDAYS).mean()
    pre_at_bk = pre.where(new_high).ffill(limit=20)
    post5 = volume.rolling(WDAYS, min_periods=2).mean()
    bk_recent = new_high.rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    return _safe_div(post5, pre_at_bk).where(bk_recent, np.nan)


def f20_vdah_344_count_low_vol_thrust_failures_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    atr21 = _atr(high, low, close, n=MDAYS)
    thrust = (close - close.shift(1)) > atr21
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    weak = volume < v_med
    return (thrust & weak).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_345_low_vol_gap_up_filled_within_5d_count_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_up = open_ > high.shift(1)
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < v_med
    fill_window_low = low.rolling(WDAYS, min_periods=1).min()
    prior_close = close.shift(WDAYS)
    filled_at_t = fill_window_low <= prior_close
    event_at_t_minus_5 = (gap_up.shift(WDAYS) & low_vol.shift(WDAYS)).fillna(False)
    flag = event_at_t_minus_5 & filled_at_t
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_346_low_vol_with_upper_shadow_dominant_count_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    body = (close - open_).abs()
    upper_shadow = high - pd.concat([open_, close], axis=1).max(axis=1)
    cond_shadow = upper_shadow > 2 * body
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < v_med
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    return (cond_shadow & low_vol & in_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_347_low_vol_outside_bar_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    outside = (high > high.shift(1)) & (low < low.shift(1))
    pos_in_bar = _safe_div(close - low, high - low)
    near_low = pos_in_bar < 0.5
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < v_med
    return (outside & near_low & low_vol).astype(float).where(v_med.notna(), np.nan)


def f20_vdah_348_dryup_bandwidth_collapse_compound_atr_vol(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr21 = _atr(high, low, close, n=MDAYS)
    atr252 = _atr(high, low, close, n=YDAYS)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    return (_safe_div(atr21, atr252) * _safe_div(v21, v252)).where(in_top, np.nan)


def f20_vdah_349_dryup_bollinger_band_pinch_x_low_vol(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    _, _, bw = _bbands(close, n=20, k=2.0)
    q20_bw = _rolling_quantile(bw, YDAYS, 0.20)
    q20_v = _rolling_quantile(volume, YDAYS, 0.20)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    cond = (bw < q20_bw) & (volume < q20_v) & in_top
    return cond.astype(float).where(q20_bw.notna() & q20_v.notna(), np.nan)


def f20_vdah_350_keltner_squeeze_low_vol_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    bb_u, bb_l, _ = _bbands(close, n=20, k=2.0)
    kc_u, kc_l = _keltner(high, low, close, n=20, k=2.0)
    squeeze = (kc_u <= bb_u) & (kc_l >= bb_l)
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    low_vol = volume < v_med
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * rmax
    return (squeeze & low_vol & at_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_351_vol_dryup_with_lower_high_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    lh3 = (high < high.shift(1)) & (high.shift(1) < high.shift(2))
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet3 = (volume < v_med) & (volume.shift(1) < v_med.shift(1)) & (volume.shift(2) < v_med.shift(2))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    in_top = high >= 0.9 * rmax
    return (lh3 & quiet3 & in_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_352_dryup_to_vol_burst_recurrence_rate_252d(volume: pd.Series) -> pd.Series:
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    q75 = _rolling_quantile(volume, YDAYS, 0.75)
    state = pd.Series(0, index=volume.index, dtype=int)
    state[volume < q25] = -1
    state[volume > q75] = 1
    trans = ((state.shift(1) == -1) & (state == 1)) | ((state.shift(1) == 1) & (state == -1))
    return trans.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_353_longest_interval_between_above_avg_vol_bars_at_high(volume: pd.Series, high: pd.Series) -> pd.Series:
    above = volume > volume.rolling(MDAYS, min_periods=WDAYS).mean()
    at_top = high >= 0.9 * high.rolling(YDAYS, min_periods=QDAYS).max()
    arr = (above & at_top).astype(float).values
    n = len(volume); out = np.full(n, np.nan, dtype=float)
    for i in range(YDAYS - 1, n):
        idxs = np.where(arr[i - YDAYS + 1:i + 1] > 0)[0]
        out[i] = float(np.diff(idxs).max()) if idxs.size >= 2 else float(YDAYS)
    return pd.Series(out, index=volume.index)


def f20_vdah_354_cv_vol_during_top_decile_dwell(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    masked = volume.where(in_top)
    m = masked.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = masked.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(sd, m)


def f20_vdah_355_vol_to_range_compression_ratio_during_dryup(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    ratio = _safe_div(volume, tr)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    in_top = pos >= 0.9
    top_mean = ratio.where(in_top).rolling(MDAYS, min_periods=WDAYS).mean()
    base = ratio.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(top_mean, base)


def f20_vdah_356_relative_vol_vs_industry_proxy_market_pct_rank_63d(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_pct_rank(v21, YDAYS)


def f20_vdah_357_vol_climax_to_dryup_transition_sharpness_score(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _sharp(w):
        if np.isnan(w).all():
            return np.nan
        i_max = int(np.nanargmax(w))
        seg = w[i_max:]
        if seg.size < 2 or np.isnan(seg).all():
            return np.nan
        i_min = int(np.nanargmin(seg))
        if i_min == 0:
            return 0.0
        drop = w[i_max] - seg[i_min]
        return float(drop / i_min)
    return lv.rolling(21, min_periods=10).apply(_sharp, raw=True)


def f20_vdah_358_dryup_persistence_index_via_runs_test(volume: pd.Series) -> pd.Series:
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    sign = (volume > med).astype(float).where(med.notna(), np.nan)
    def _runs_z(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        n1 = int(v.sum()); n0 = int(v.size - n1)
        if n1 == 0 or n0 == 0:
            return np.nan
        N = n1 + n0
        runs = 1 + int((np.diff(v) != 0).sum())
        mu = 2.0 * n1 * n0 / N + 1.0
        var = (2.0 * n1 * n0 * (2.0 * n1 * n0 - N)) / (N * N * (N - 1.0))
        return (runs - mu) / np.sqrt(var) if var > 0 else np.nan
    return sign.rolling(YDAYS, min_periods=QDAYS).apply(_runs_z, raw=True)


def f20_vdah_359_low_vol_at_high_relative_to_own_prior_year_high_visit(volume: pd.Series, high: pd.Series) -> pd.Series:
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * rmax
    cur = v21.where(at_top)
    prior = cur.shift(YDAYS)
    return _safe_div(cur, prior)


def f20_vdah_360_dryup_score_at_new_alltime_high_only(volume: pd.Series, high: pd.Series) -> pd.Series:
    ath = high.expanding(min_periods=QDAYS).max()
    new_ath = high >= ath
    z = _rolling_zscore(volume, YDAYS)
    return z.where(new_ath, np.nan)


def f20_vdah_361_post_ath_first_30bar_vol_mean_pct_rank(volume: pd.Series, high: pd.Series) -> pd.Series:
    ath = high.expanding(min_periods=QDAYS).max()
    new_ath = high >= ath
    pre30 = volume.rolling(30, min_periods=10).mean()
    capt = pre30.where(new_ath).ffill(limit=30)
    return _rolling_pct_rank(capt, YDAYS)


def f20_vdah_362_consecutive_new_highs_with_each_vol_lower_streak(high: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    is_nh = (high > rmax21).values
    v = volume.values; n = len(high)
    out = np.full(n, np.nan, dtype=float)
    streak = 0; prev_v = np.nan
    for i in range(n):
        if not is_nh[i]:
            out[i] = float(streak); continue
        if np.isnan(v[i]):
            streak = 0; prev_v = np.nan
        elif np.isnan(prev_v) or v[i] >= prev_v:
            streak = 1; prev_v = v[i]
        else:
            streak += 1; prev_v = v[i]
        out[i] = float(streak)
    return pd.Series(out, index=high.index)


def f20_vdah_363_vol_zscore_on_failed_high_attempts_mean_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pierce = high > rmax21
    pos_in_bar = _safe_div(close - low, high - low)
    failed = pierce & (pos_in_bar < 0.5)
    z = _rolling_zscore(volume, YDAYS)
    return z.where(failed).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_364_silent_pullback_low_vol_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pullback = (close < close.shift(1)) & (close >= 0.99 * close.shift(1))
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med
    return (pullback & quiet).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_365_silent_pullback_to_silent_rally_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    quiet = volume < v_med
    pullback = (close < close.shift(1)) & (close >= 0.99 * close.shift(1)) & quiet
    rally = (close > close.shift(1)) & (close <= 1.01 * close.shift(1)) & quiet
    pcnt = pullback.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    rcnt = rally.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(pcnt, rcnt)


def f20_vdah_366_dryup_above_50d_ma_only_dwell_share(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma50 = close.rolling(50, min_periods=20).mean()
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    cond = (close > sma50) & (volume < q25)
    return cond.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_367_dryup_above_200d_ma_only_dwell_share(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma200 = close.rolling(200, min_periods=60).mean()
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    cond = (close > sma200) & (volume < q25)
    return cond.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_368_vol_below_50d_avg_for_n_consec_days_max_streak_252d(volume: pd.Series) -> pd.Series:
    v50 = volume.rolling(50, min_periods=20).mean()
    below = volume < v50
    streak = _consecutive_true_streak(below).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_369_vol_zscore_on_test_of_prior_breakout_pivot(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h20 = high.shift(1).rolling(20, min_periods=10).max()
    piv = h20.where(high > h20).ffill().shift(1)
    atr21 = _atr(high, low, close, n=MDAYS)
    near = (low <= piv + atr21) & (low >= piv - atr21)
    above = close > piv
    z = _rolling_zscore(volume, YDAYS)
    return z.where(near & above, np.nan)


def f20_vdah_370_supply_test_count_williams_definition_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    piv_l = _pivot_low_event(low, lookback=3)
    last_piv_low = low.where(piv_l > 0).ffill().shift(1)
    pen = low < last_piv_low
    pos_in_bar = _safe_div(close - low, high - low)
    upper_half = pos_in_bar > 0.5
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    low_vol = volume < q25
    cond = pen & upper_half & low_vol
    return cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_371_supply_test_success_within_3bars_rate(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    piv_l = _pivot_low_event(low, lookback=3)
    last_piv_low = low.where(piv_l > 0).ffill().shift(1)
    pen = low < last_piv_low
    pos_in_bar = _safe_div(close - low, high - low)
    upper_half = pos_in_bar > 0.5
    q25 = _rolling_quantile(volume, YDAYS, 0.25)
    low_vol = volume < q25
    test = pen & upper_half & low_vol
    test_lag3 = test.shift(3).fillna(False)
    test_high_lag3 = high.shift(3).where(test_lag3)
    succ = close > test_high_lag3
    succ_flag = (test_lag3 & succ).astype(float)
    test_count = test.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    succ_count = succ_flag.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(succ_count, test_count)


def f20_vdah_372_vol_dryup_x_atr_compression_x_close_at_high_3way_compound(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rnk_v = _rolling_pct_rank(volume, YDAYS)
    atr21 = _atr(high, low, close, n=MDAYS)
    rnk_a = _rolling_pct_rank(atr21, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return (1.0 - rnk_v) * (1.0 - rnk_a) * pos


def f20_vdah_373_vol_dryup_post_distribution_day_cluster(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_dd = (close < close.shift(1)) & (volume > volume.shift(1))
    cnt25 = is_dd.astype(float).rolling(25, min_periods=10).sum()
    cluster = cnt25 >= 4
    pre = volume.shift(25).rolling(MDAYS, min_periods=WDAYS).mean()
    post = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cluster_recent = cluster.rolling(MDAYS, min_periods=1).max().fillna(0) > 0
    cond = cluster_recent & (post < 0.8 * pre)
    return cond.astype(float).where(pre.notna(), np.nan)


def f20_vdah_374_vol_dryup_intensity_weighted_by_distance_to_alltime_high(volume: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    ath = high.expanding(min_periods=QDAYS).max()
    dist = _safe_div(ath - close, ath).clip(lower=0)
    w = np.exp(-5.0 * dist.fillna(1.0))
    rnk_v = _rolling_pct_rank(volume, YDAYS)
    return (1.0 - rnk_v) * w


def f20_vdah_375_williams_vsa_composite_topping_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    atr21 = _atr(high, low, close, n=MDAYS)
    narrow = rng < 0.7 * atr21
    pos_in_bar = _safe_div(close - low, rng)
    v_med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    no_demand = (narrow & (pos_in_bar >= 0.5) & (volume < v_med21)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    upthrust = ((high > rmax21) & (pos_in_bar < 0.5) & (volume > 1.5 * v_med21)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    v_max5 = volume.rolling(WDAYS, min_periods=2).max()
    q20_5 = rng.rolling(WDAYS, min_periods=2).quantile(0.2)
    squat = ((volume >= v_max5) & (rng <= q20_5)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    piv_l = _pivot_low_event(low, lookback=3)
    last_piv_low = low.where(piv_l > 0).ffill().shift(1)
    q25v = _rolling_quantile(volume, YDAYS, 0.25)
    st = ((low < last_piv_low) & (pos_in_bar > 0.5) & (volume < q25v)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (_rolling_zscore(no_demand, YDAYS)
            + _rolling_zscore(upthrust, YDAYS)
            + _rolling_zscore(squat, YDAYS)
            + _rolling_zscore(st, YDAYS))


def f20_vdah_301_minervini_vcp_contraction_count_63d_d1(high, low, close):
    return f20_vdah_301_minervini_vcp_contraction_count_63d(high, low, close).diff()


def f20_vdah_302_minervini_vcp_each_contraction_vol_lower_indicator_d1(high, low, close, volume):
    return f20_vdah_302_minervini_vcp_each_contraction_vol_lower_indicator(high, low, close, volume).diff()


def f20_vdah_303_minervini_vcp_final_pivot_vol_pct_rank_63d_d1(volume, high, low, close):
    return f20_vdah_303_minervini_vcp_final_pivot_vol_pct_rank_63d(volume, high, low, close).diff()


def f20_vdah_304_oneil_handle_low_vol_dryup_score_d1(volume, high, low, close):
    return f20_vdah_304_oneil_handle_low_vol_dryup_score(volume, high, low, close).diff()


def f20_vdah_305_oneil_three_weeks_tight_low_vol_indicator_d1(close, volume):
    return f20_vdah_305_oneil_three_weeks_tight_low_vol_indicator(close, volume).diff()


def f20_vdah_306_kacher_undercut_dryup_indicator_d1(low, close, volume):
    return f20_vdah_306_kacher_undercut_dryup_indicator(low, close, volume).diff()


def f20_vdah_307_kacher_inverse_pocket_pivot_count_63d_d1(close, volume):
    return f20_vdah_307_kacher_inverse_pocket_pivot_count_63d(close, volume).diff()


def f20_vdah_308_williams_vsa_no_demand_after_upthrust_5d_d1(high, low, close, volume):
    return f20_vdah_308_williams_vsa_no_demand_after_upthrust_5d(high, low, close, volume).diff()


def f20_vdah_309_williams_squat_bar_indicator_d1(high, low, volume):
    return f20_vdah_309_williams_squat_bar_indicator(high, low, volume).diff()


def f20_vdah_310_williams_squat_count_at_252d_high_63d_d1(high, low, volume):
    return f20_vdah_310_williams_squat_count_at_252d_high_63d(high, low, volume).diff()


def f20_vdah_311_williams_two_bar_reversal_low_vol_indicator_d1(high, low, close, volume):
    return f20_vdah_311_williams_two_bar_reversal_low_vol_indicator(high, low, close, volume).diff()


def f20_vdah_312_coulling_background_volume_compression_ratio_d1(volume, high, low, close):
    return f20_vdah_312_coulling_background_volume_compression_ratio(volume, high, low, close).diff()


def f20_vdah_313_weis_wave_up_wave_volume_minus_down_wave_volume_63d_d1(close, volume):
    return f20_vdah_313_weis_wave_up_wave_volume_minus_down_wave_volume_63d(close, volume).diff()


def f20_vdah_314_weis_wave_up_vol_decline_streak_d1(close, volume):
    return f20_vdah_314_weis_wave_up_vol_decline_streak(close, volume).diff()


def f20_vdah_315_weis_wave_last_up_wave_vol_pct_rank_252d_d1(close, volume):
    return f20_vdah_315_weis_wave_last_up_wave_vol_pct_rank_252d(close, volume).diff()


def f20_vdah_316_wyckoff_phase_b_creek_low_vol_test_count_d1(high, low, volume):
    return f20_vdah_316_wyckoff_phase_b_creek_low_vol_test_count(high, low, volume).diff()


def f20_vdah_317_wyckoff_sign_of_weakness_volume_to_jump_volume_ratio_d1(high, low, close, volume):
    return f20_vdah_317_wyckoff_sign_of_weakness_volume_to_jump_volume_ratio(high, low, close, volume).diff()


def f20_vdah_318_wyckoff_automatic_reaction_dryup_indicator_d1(high, low, close, volume):
    return f20_vdah_318_wyckoff_automatic_reaction_dryup_indicator(high, low, close, volume).diff()


def f20_vdah_319_minervini_stage3_topping_vol_signature_score_d1(high, low, close, volume):
    return f20_vdah_319_minervini_stage3_topping_vol_signature_score(high, low, close, volume).diff()


def f20_vdah_320_oneil_late_stage_base_dryup_indicator_d1(high, low, close, volume):
    return f20_vdah_320_oneil_late_stage_base_dryup_indicator(high, low, close, volume).diff()


def f20_vdah_321_oneil_climax_top_followed_by_dryup_3wks_d1(high, low, close, volume):
    return f20_vdah_321_oneil_climax_top_followed_by_dryup_3wks(high, low, close, volume).diff()


def f20_vdah_322_holiday_proximate_dryup_normalization_d1(close, volume):
    return f20_vdah_322_holiday_proximate_dryup_normalization(close, volume).diff()


def f20_vdah_323_dryup_at_round_number_proximity_indicator_d1(close, volume):
    return f20_vdah_323_dryup_at_round_number_proximity_indicator(close, volume).diff()


def f20_vdah_324_dryup_at_prior_year_high_proximity_indicator_d1(high, close, volume):
    return f20_vdah_324_dryup_at_prior_year_high_proximity_indicator(high, close, volume).diff()


def f20_vdah_325_days_since_last_high_vol_at_252d_high_d1(volume, high):
    return f20_vdah_325_days_since_last_high_vol_at_252d_high(volume, high).diff()


def f20_vdah_326_avg_vol_pct_rank_during_top_decile_dwell_21d_d1(high, low, close, volume):
    return f20_vdah_326_avg_vol_pct_rank_during_top_decile_dwell_21d(high, low, close, volume).diff()


def f20_vdah_327_largest_single_bar_vol_collapse_in_252d_d1(volume, high, low, close):
    return f20_vdah_327_largest_single_bar_vol_collapse_in_252d(volume, high, low, close).diff()


def f20_vdah_328_negative_vroc_event_count_63d_d1(volume, high, low, close):
    return f20_vdah_328_negative_vroc_event_count_63d(volume, high, low, close).diff()


def f20_vdah_329_vol_collapse_then_failed_rally_indicator_d1(close, volume, high, low):
    return f20_vdah_329_vol_collapse_then_failed_rally_indicator(close, volume, high, low).diff()


def f20_vdah_330_vol_dryup_with_narrow_range_coincidence_63d_d1(volume, high, low, close):
    return f20_vdah_330_vol_dryup_with_narrow_range_coincidence_63d(volume, high, low, close).diff()


def f20_vdah_331_count_inside_bars_with_low_vol_at_high_63d_d1(high, low, volume):
    return f20_vdah_331_count_inside_bars_with_low_vol_at_high_63d(high, low, volume).diff()


def f20_vdah_332_count_nr7_low_vol_at_high_63d_d1(high, low, volume):
    return f20_vdah_332_count_nr7_low_vol_at_high_63d(high, low, volume).diff()


def f20_vdah_333_nr4_low_vol_streak_at_high_d1(high, low, volume):
    return f20_vdah_333_nr4_low_vol_streak_at_high(high, low, volume).diff()


def f20_vdah_334_consecutive_doji_low_vol_streak_d1(open_, high, low, close, volume):
    return f20_vdah_334_consecutive_doji_low_vol_streak(open_, high, low, close, volume).diff()


def f20_vdah_335_post_climax_vol_half_life_in_bars_after_fam19_blowoff_d1(volume, high, low, close):
    return f20_vdah_335_post_climax_vol_half_life_in_bars_after_fam19_blowoff(volume, high, low, close).diff()


def f20_vdah_336_post_climax_first_3day_vol_rank_252d_d1(volume, high, low, close):
    return f20_vdah_336_post_climax_first_3day_vol_rank_252d(volume, high, low, close).diff()


def f20_vdah_337_vol_collapse_rate_21d_over_252d_gated_at_high_d1(volume, high, low, close):
    return f20_vdah_337_vol_collapse_rate_21d_over_252d_gated_at_high(volume, high, low, close).diff()


def f20_vdah_338_entropy_collapse_rate_21d_over_252d_gated_at_high_d1(volume, high, low, close):
    return f20_vdah_338_entropy_collapse_rate_21d_over_252d_gated_at_high(volume, high, low, close).diff()


def f20_vdah_339_vol_dryup_during_base_formation_indicator_d1(high, low, close, volume):
    return f20_vdah_339_vol_dryup_during_base_formation_indicator(high, low, close, volume).diff()


def f20_vdah_340_base_handle_vol_to_base_left_side_vol_ratio_d1(volume, high, low, close):
    return f20_vdah_340_base_handle_vol_to_base_left_side_vol_ratio(volume, high, low, close).diff()


def f20_vdah_341_vol_dryup_at_breakout_pivot_with_close_in_upper_third_d1(high, low, close, volume):
    return f20_vdah_341_vol_dryup_at_breakout_pivot_with_close_in_upper_third(high, low, close, volume).diff()


def f20_vdah_342_breakout_vol_pct_rank_at_252d_breakout_d1(high, volume):
    return f20_vdah_342_breakout_vol_pct_rank_at_252d_breakout(high, volume).diff()


def f20_vdah_343_post_breakout_vol_dryup_5d_d1(high, volume):
    return f20_vdah_343_post_breakout_vol_dryup_5d(high, volume).diff()


def f20_vdah_344_count_low_vol_thrust_failures_63d_d1(close, high, low, volume):
    return f20_vdah_344_count_low_vol_thrust_failures_63d(close, high, low, volume).diff()


def f20_vdah_345_low_vol_gap_up_filled_within_5d_count_252d_d1(open_, high, low, close, volume):
    return f20_vdah_345_low_vol_gap_up_filled_within_5d_count_252d(open_, high, low, close, volume).diff()


def f20_vdah_346_low_vol_with_upper_shadow_dominant_count_63d_d1(open_, high, low, close, volume):
    return f20_vdah_346_low_vol_with_upper_shadow_dominant_count_63d(open_, high, low, close, volume).diff()


def f20_vdah_347_low_vol_outside_bar_failure_indicator_d1(high, low, close, volume):
    return f20_vdah_347_low_vol_outside_bar_failure_indicator(high, low, close, volume).diff()


def f20_vdah_348_dryup_bandwidth_collapse_compound_atr_vol_d1(high, low, close, volume):
    return f20_vdah_348_dryup_bandwidth_collapse_compound_atr_vol(high, low, close, volume).diff()


def f20_vdah_349_dryup_bollinger_band_pinch_x_low_vol_d1(high, low, close, volume):
    return f20_vdah_349_dryup_bollinger_band_pinch_x_low_vol(high, low, close, volume).diff()


def f20_vdah_350_keltner_squeeze_low_vol_count_63d_d1(high, low, close, volume):
    return f20_vdah_350_keltner_squeeze_low_vol_count_63d(high, low, close, volume).diff()


def f20_vdah_351_vol_dryup_with_lower_high_count_63d_d1(high, low, close, volume):
    return f20_vdah_351_vol_dryup_with_lower_high_count_63d(high, low, close, volume).diff()


def f20_vdah_352_dryup_to_vol_burst_recurrence_rate_252d_d1(volume):
    return f20_vdah_352_dryup_to_vol_burst_recurrence_rate_252d(volume).diff()


def f20_vdah_353_longest_interval_between_above_avg_vol_bars_at_high_d1(volume, high):
    return f20_vdah_353_longest_interval_between_above_avg_vol_bars_at_high(volume, high).diff()


def f20_vdah_354_cv_vol_during_top_decile_dwell_d1(high, low, close, volume):
    return f20_vdah_354_cv_vol_during_top_decile_dwell(high, low, close, volume).diff()


def f20_vdah_355_vol_to_range_compression_ratio_during_dryup_d1(volume, high, low, close):
    return f20_vdah_355_vol_to_range_compression_ratio_during_dryup(volume, high, low, close).diff()


def f20_vdah_356_relative_vol_vs_industry_proxy_market_pct_rank_63d_d1(volume):
    return f20_vdah_356_relative_vol_vs_industry_proxy_market_pct_rank_63d(volume).diff()


def f20_vdah_357_vol_climax_to_dryup_transition_sharpness_score_d1(volume, high, low, close):
    return f20_vdah_357_vol_climax_to_dryup_transition_sharpness_score(volume, high, low, close).diff()


def f20_vdah_358_dryup_persistence_index_via_runs_test_d1(volume):
    return f20_vdah_358_dryup_persistence_index_via_runs_test(volume).diff()


def f20_vdah_359_low_vol_at_high_relative_to_own_prior_year_high_visit_d1(volume, high):
    return f20_vdah_359_low_vol_at_high_relative_to_own_prior_year_high_visit(volume, high).diff()


def f20_vdah_360_dryup_score_at_new_alltime_high_only_d1(volume, high):
    return f20_vdah_360_dryup_score_at_new_alltime_high_only(volume, high).diff()


def f20_vdah_361_post_ath_first_30bar_vol_mean_pct_rank_d1(volume, high):
    return f20_vdah_361_post_ath_first_30bar_vol_mean_pct_rank(volume, high).diff()


def f20_vdah_362_consecutive_new_highs_with_each_vol_lower_streak_d1(high, volume):
    return f20_vdah_362_consecutive_new_highs_with_each_vol_lower_streak(high, volume).diff()


def f20_vdah_363_vol_zscore_on_failed_high_attempts_mean_252d_d1(high, low, close, volume):
    return f20_vdah_363_vol_zscore_on_failed_high_attempts_mean_252d(high, low, close, volume).diff()


def f20_vdah_364_silent_pullback_low_vol_count_63d_d1(close, volume):
    return f20_vdah_364_silent_pullback_low_vol_count_63d(close, volume).diff()


def f20_vdah_365_silent_pullback_to_silent_rally_ratio_63d_d1(close, volume):
    return f20_vdah_365_silent_pullback_to_silent_rally_ratio_63d(close, volume).diff()


def f20_vdah_366_dryup_above_50d_ma_only_dwell_share_d1(close, volume):
    return f20_vdah_366_dryup_above_50d_ma_only_dwell_share(close, volume).diff()


def f20_vdah_367_dryup_above_200d_ma_only_dwell_share_d1(close, volume):
    return f20_vdah_367_dryup_above_200d_ma_only_dwell_share(close, volume).diff()


def f20_vdah_368_vol_below_50d_avg_for_n_consec_days_max_streak_252d_d1(volume):
    return f20_vdah_368_vol_below_50d_avg_for_n_consec_days_max_streak_252d(volume).diff()


def f20_vdah_369_vol_zscore_on_test_of_prior_breakout_pivot_d1(high, low, close, volume):
    return f20_vdah_369_vol_zscore_on_test_of_prior_breakout_pivot(high, low, close, volume).diff()


def f20_vdah_370_supply_test_count_williams_definition_252d_d1(high, low, close, volume):
    return f20_vdah_370_supply_test_count_williams_definition_252d(high, low, close, volume).diff()


def f20_vdah_371_supply_test_success_within_3bars_rate_d1(high, low, close, volume):
    return f20_vdah_371_supply_test_success_within_3bars_rate(high, low, close, volume).diff()


def f20_vdah_372_vol_dryup_x_atr_compression_x_close_at_high_3way_compound_d1(high, low, close, volume):
    return f20_vdah_372_vol_dryup_x_atr_compression_x_close_at_high_3way_compound(high, low, close, volume).diff()


def f20_vdah_373_vol_dryup_post_distribution_day_cluster_d1(close, volume):
    return f20_vdah_373_vol_dryup_post_distribution_day_cluster(close, volume).diff()


def f20_vdah_374_vol_dryup_intensity_weighted_by_distance_to_alltime_high_d1(volume, high, close):
    return f20_vdah_374_vol_dryup_intensity_weighted_by_distance_to_alltime_high(volume, high, close).diff()


def f20_vdah_375_williams_vsa_composite_topping_score_252d_d1(high, low, close, volume):
    return f20_vdah_375_williams_vsa_composite_topping_score_252d(high, low, close, volume).diff()


VOLUME_DRYUP_AT_HIGH_D1_REGISTRY_301_375 = {
    "f20_vdah_301_minervini_vcp_contraction_count_63d_d1": {"inputs": ["high", "low", "close"], "func": f20_vdah_301_minervini_vcp_contraction_count_63d_d1},
    "f20_vdah_302_minervini_vcp_each_contraction_vol_lower_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_302_minervini_vcp_each_contraction_vol_lower_indicator_d1},
    "f20_vdah_303_minervini_vcp_final_pivot_vol_pct_rank_63d_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_303_minervini_vcp_final_pivot_vol_pct_rank_63d_d1},
    "f20_vdah_304_oneil_handle_low_vol_dryup_score_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_304_oneil_handle_low_vol_dryup_score_d1},
    "f20_vdah_305_oneil_three_weeks_tight_low_vol_indicator_d1": {"inputs": ["close", "volume"], "func": f20_vdah_305_oneil_three_weeks_tight_low_vol_indicator_d1},
    "f20_vdah_306_kacher_undercut_dryup_indicator_d1": {"inputs": ["low", "close", "volume"], "func": f20_vdah_306_kacher_undercut_dryup_indicator_d1},
    "f20_vdah_307_kacher_inverse_pocket_pivot_count_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_307_kacher_inverse_pocket_pivot_count_63d_d1},
    "f20_vdah_308_williams_vsa_no_demand_after_upthrust_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_308_williams_vsa_no_demand_after_upthrust_5d_d1},
    "f20_vdah_309_williams_squat_bar_indicator_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_309_williams_squat_bar_indicator_d1},
    "f20_vdah_310_williams_squat_count_at_252d_high_63d_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_310_williams_squat_count_at_252d_high_63d_d1},
    "f20_vdah_311_williams_two_bar_reversal_low_vol_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_311_williams_two_bar_reversal_low_vol_indicator_d1},
    "f20_vdah_312_coulling_background_volume_compression_ratio_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_312_coulling_background_volume_compression_ratio_d1},
    "f20_vdah_313_weis_wave_up_wave_volume_minus_down_wave_volume_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_313_weis_wave_up_wave_volume_minus_down_wave_volume_63d_d1},
    "f20_vdah_314_weis_wave_up_vol_decline_streak_d1": {"inputs": ["close", "volume"], "func": f20_vdah_314_weis_wave_up_vol_decline_streak_d1},
    "f20_vdah_315_weis_wave_last_up_wave_vol_pct_rank_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_315_weis_wave_last_up_wave_vol_pct_rank_252d_d1},
    "f20_vdah_316_wyckoff_phase_b_creek_low_vol_test_count_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_316_wyckoff_phase_b_creek_low_vol_test_count_d1},
    "f20_vdah_317_wyckoff_sign_of_weakness_volume_to_jump_volume_ratio_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_317_wyckoff_sign_of_weakness_volume_to_jump_volume_ratio_d1},
    "f20_vdah_318_wyckoff_automatic_reaction_dryup_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_318_wyckoff_automatic_reaction_dryup_indicator_d1},
    "f20_vdah_319_minervini_stage3_topping_vol_signature_score_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_319_minervini_stage3_topping_vol_signature_score_d1},
    "f20_vdah_320_oneil_late_stage_base_dryup_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_320_oneil_late_stage_base_dryup_indicator_d1},
    "f20_vdah_321_oneil_climax_top_followed_by_dryup_3wks_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_321_oneil_climax_top_followed_by_dryup_3wks_d1},
    "f20_vdah_322_holiday_proximate_dryup_normalization_d1": {"inputs": ["close", "volume"], "func": f20_vdah_322_holiday_proximate_dryup_normalization_d1},
    "f20_vdah_323_dryup_at_round_number_proximity_indicator_d1": {"inputs": ["close", "volume"], "func": f20_vdah_323_dryup_at_round_number_proximity_indicator_d1},
    "f20_vdah_324_dryup_at_prior_year_high_proximity_indicator_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_324_dryup_at_prior_year_high_proximity_indicator_d1},
    "f20_vdah_325_days_since_last_high_vol_at_252d_high_d1": {"inputs": ["volume", "high"], "func": f20_vdah_325_days_since_last_high_vol_at_252d_high_d1},
    "f20_vdah_326_avg_vol_pct_rank_during_top_decile_dwell_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_326_avg_vol_pct_rank_during_top_decile_dwell_21d_d1},
    "f20_vdah_327_largest_single_bar_vol_collapse_in_252d_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_327_largest_single_bar_vol_collapse_in_252d_d1},
    "f20_vdah_328_negative_vroc_event_count_63d_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_328_negative_vroc_event_count_63d_d1},
    "f20_vdah_329_vol_collapse_then_failed_rally_indicator_d1": {"inputs": ["close", "volume", "high", "low"], "func": f20_vdah_329_vol_collapse_then_failed_rally_indicator_d1},
    "f20_vdah_330_vol_dryup_with_narrow_range_coincidence_63d_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_330_vol_dryup_with_narrow_range_coincidence_63d_d1},
    "f20_vdah_331_count_inside_bars_with_low_vol_at_high_63d_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_331_count_inside_bars_with_low_vol_at_high_63d_d1},
    "f20_vdah_332_count_nr7_low_vol_at_high_63d_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_332_count_nr7_low_vol_at_high_63d_d1},
    "f20_vdah_333_nr4_low_vol_streak_at_high_d1": {"inputs": ["high", "low", "volume"], "func": f20_vdah_333_nr4_low_vol_streak_at_high_d1},
    "f20_vdah_334_consecutive_doji_low_vol_streak_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f20_vdah_334_consecutive_doji_low_vol_streak_d1},
    "f20_vdah_335_post_climax_vol_half_life_in_bars_after_fam19_blowoff_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_335_post_climax_vol_half_life_in_bars_after_fam19_blowoff_d1},
    "f20_vdah_336_post_climax_first_3day_vol_rank_252d_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_336_post_climax_first_3day_vol_rank_252d_d1},
    "f20_vdah_337_vol_collapse_rate_21d_over_252d_gated_at_high_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_337_vol_collapse_rate_21d_over_252d_gated_at_high_d1},
    "f20_vdah_338_entropy_collapse_rate_21d_over_252d_gated_at_high_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_338_entropy_collapse_rate_21d_over_252d_gated_at_high_d1},
    "f20_vdah_339_vol_dryup_during_base_formation_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_339_vol_dryup_during_base_formation_indicator_d1},
    "f20_vdah_340_base_handle_vol_to_base_left_side_vol_ratio_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_340_base_handle_vol_to_base_left_side_vol_ratio_d1},
    "f20_vdah_341_vol_dryup_at_breakout_pivot_with_close_in_upper_third_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_341_vol_dryup_at_breakout_pivot_with_close_in_upper_third_d1},
    "f20_vdah_342_breakout_vol_pct_rank_at_252d_breakout_d1": {"inputs": ["high", "volume"], "func": f20_vdah_342_breakout_vol_pct_rank_at_252d_breakout_d1},
    "f20_vdah_343_post_breakout_vol_dryup_5d_d1": {"inputs": ["high", "volume"], "func": f20_vdah_343_post_breakout_vol_dryup_5d_d1},
    "f20_vdah_344_count_low_vol_thrust_failures_63d_d1": {"inputs": ["close", "high", "low", "volume"], "func": f20_vdah_344_count_low_vol_thrust_failures_63d_d1},
    "f20_vdah_345_low_vol_gap_up_filled_within_5d_count_252d_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f20_vdah_345_low_vol_gap_up_filled_within_5d_count_252d_d1},
    "f20_vdah_346_low_vol_with_upper_shadow_dominant_count_63d_d1": {"inputs": ["open", "high", "low", "close", "volume"], "func": f20_vdah_346_low_vol_with_upper_shadow_dominant_count_63d_d1},
    "f20_vdah_347_low_vol_outside_bar_failure_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_347_low_vol_outside_bar_failure_indicator_d1},
    "f20_vdah_348_dryup_bandwidth_collapse_compound_atr_vol_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_348_dryup_bandwidth_collapse_compound_atr_vol_d1},
    "f20_vdah_349_dryup_bollinger_band_pinch_x_low_vol_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_349_dryup_bollinger_band_pinch_x_low_vol_d1},
    "f20_vdah_350_keltner_squeeze_low_vol_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_350_keltner_squeeze_low_vol_count_63d_d1},
    "f20_vdah_351_vol_dryup_with_lower_high_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_351_vol_dryup_with_lower_high_count_63d_d1},
    "f20_vdah_352_dryup_to_vol_burst_recurrence_rate_252d_d1": {"inputs": ["volume"], "func": f20_vdah_352_dryup_to_vol_burst_recurrence_rate_252d_d1},
    "f20_vdah_353_longest_interval_between_above_avg_vol_bars_at_high_d1": {"inputs": ["volume", "high"], "func": f20_vdah_353_longest_interval_between_above_avg_vol_bars_at_high_d1},
    "f20_vdah_354_cv_vol_during_top_decile_dwell_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_354_cv_vol_during_top_decile_dwell_d1},
    "f20_vdah_355_vol_to_range_compression_ratio_during_dryup_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_355_vol_to_range_compression_ratio_during_dryup_d1},
    "f20_vdah_356_relative_vol_vs_industry_proxy_market_pct_rank_63d_d1": {"inputs": ["volume"], "func": f20_vdah_356_relative_vol_vs_industry_proxy_market_pct_rank_63d_d1},
    "f20_vdah_357_vol_climax_to_dryup_transition_sharpness_score_d1": {"inputs": ["volume", "high", "low", "close"], "func": f20_vdah_357_vol_climax_to_dryup_transition_sharpness_score_d1},
    "f20_vdah_358_dryup_persistence_index_via_runs_test_d1": {"inputs": ["volume"], "func": f20_vdah_358_dryup_persistence_index_via_runs_test_d1},
    "f20_vdah_359_low_vol_at_high_relative_to_own_prior_year_high_visit_d1": {"inputs": ["volume", "high"], "func": f20_vdah_359_low_vol_at_high_relative_to_own_prior_year_high_visit_d1},
    "f20_vdah_360_dryup_score_at_new_alltime_high_only_d1": {"inputs": ["volume", "high"], "func": f20_vdah_360_dryup_score_at_new_alltime_high_only_d1},
    "f20_vdah_361_post_ath_first_30bar_vol_mean_pct_rank_d1": {"inputs": ["volume", "high"], "func": f20_vdah_361_post_ath_first_30bar_vol_mean_pct_rank_d1},
    "f20_vdah_362_consecutive_new_highs_with_each_vol_lower_streak_d1": {"inputs": ["high", "volume"], "func": f20_vdah_362_consecutive_new_highs_with_each_vol_lower_streak_d1},
    "f20_vdah_363_vol_zscore_on_failed_high_attempts_mean_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_363_vol_zscore_on_failed_high_attempts_mean_252d_d1},
    "f20_vdah_364_silent_pullback_low_vol_count_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_364_silent_pullback_low_vol_count_63d_d1},
    "f20_vdah_365_silent_pullback_to_silent_rally_ratio_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_365_silent_pullback_to_silent_rally_ratio_63d_d1},
    "f20_vdah_366_dryup_above_50d_ma_only_dwell_share_d1": {"inputs": ["close", "volume"], "func": f20_vdah_366_dryup_above_50d_ma_only_dwell_share_d1},
    "f20_vdah_367_dryup_above_200d_ma_only_dwell_share_d1": {"inputs": ["close", "volume"], "func": f20_vdah_367_dryup_above_200d_ma_only_dwell_share_d1},
    "f20_vdah_368_vol_below_50d_avg_for_n_consec_days_max_streak_252d_d1": {"inputs": ["volume"], "func": f20_vdah_368_vol_below_50d_avg_for_n_consec_days_max_streak_252d_d1},
    "f20_vdah_369_vol_zscore_on_test_of_prior_breakout_pivot_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_369_vol_zscore_on_test_of_prior_breakout_pivot_d1},
    "f20_vdah_370_supply_test_count_williams_definition_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_370_supply_test_count_williams_definition_252d_d1},
    "f20_vdah_371_supply_test_success_within_3bars_rate_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_371_supply_test_success_within_3bars_rate_d1},
    "f20_vdah_372_vol_dryup_x_atr_compression_x_close_at_high_3way_compound_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_372_vol_dryup_x_atr_compression_x_close_at_high_3way_compound_d1},
    "f20_vdah_373_vol_dryup_post_distribution_day_cluster_d1": {"inputs": ["close", "volume"], "func": f20_vdah_373_vol_dryup_post_distribution_day_cluster_d1},
    "f20_vdah_374_vol_dryup_intensity_weighted_by_distance_to_alltime_high_d1": {"inputs": ["volume", "high", "close"], "func": f20_vdah_374_vol_dryup_intensity_weighted_by_distance_to_alltime_high_d1},
    "f20_vdah_375_williams_vsa_composite_topping_score_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_375_williams_vsa_composite_topping_score_252d_d1},
}
