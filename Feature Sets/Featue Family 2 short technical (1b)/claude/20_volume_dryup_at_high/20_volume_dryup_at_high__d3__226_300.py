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


def _corwin_schultz_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    lh = _safe_log(high) - _safe_log(low)
    beta_pit = (lh.shift(1) ** 2) + (lh ** 2)
    pair_high = pd.concat([high.shift(1), high], axis=1).max(axis=1)
    pair_low = pd.concat([low.shift(1), low], axis=1).min(axis=1)
    gamma = (_safe_log(pair_high) - _safe_log(pair_low)) ** 2
    denom_a = 3.0 - 2.0 * np.sqrt(2.0)
    alpha_num = np.sqrt(2.0 * beta_pit) - np.sqrt(beta_pit)
    alpha = (alpha_num / denom_a) - np.sqrt(gamma / denom_a)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def _shannon_entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    if p.size == 0:
        return 0.0
    return float(-(p * np.log(p)).sum())


def _mutual_info_binned(x, y, bins=8):
    mask = (~np.isnan(x)) & (~np.isnan(y))
    if mask.sum() < 4 * bins:
        return np.nan
    x = x[mask]; y = y[mask]
    if x.size == 0 or x.max() == x.min() or y.max() == y.min():
        return np.nan
    xe = np.linspace(x.min(), x.max(), bins + 1)
    ye = np.linspace(y.min(), y.max(), bins + 1)
    hxy, _, _ = np.histogram2d(x, y, bins=[xe, ye])
    pxy = hxy / hxy.sum()
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    Hxy = _shannon_entropy(pxy.ravel())
    Hx = _shannon_entropy(px)
    Hy = _shannon_entropy(py)
    return float(Hx + Hy - Hxy)


def f20_vdah_226_corwin_schultz_spread_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    return _corwin_schultz_spread(high, low)


def f20_vdah_227_corwin_schultz_spread_21d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    return _corwin_schultz_spread(high, low).rolling(MDAYS, min_periods=WDAYS).mean()


def f20_vdah_228_corwin_schultz_spread_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    return _rolling_zscore(_corwin_schultz_spread(high, low), YDAYS)


def f20_vdah_229_spread_proxy_gated_at_252d_high_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    sp = _corwin_schultz_spread(high, low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return sp.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_230_spread_zscore_at_high_minus_baseline(high: pd.Series, low: pd.Series) -> pd.Series:
    sp = _corwin_schultz_spread(high, low)
    z = _rolling_zscore(sp, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_high_mean = z.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall_mean = z.rolling(YDAYS, min_periods=QDAYS).mean()
    return at_high_mean - overall_mean


def f20_vdah_231_amihud_proxy_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).astype(float)
    amihud = _safe_div(close.pct_change().abs(), dv)
    return amihud.rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_232_amihud_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = (close * volume).astype(float)
    amihud = _safe_div(close.pct_change().abs(), dv)
    return _rolling_zscore(amihud, YDAYS)


def f20_vdah_233_spread_to_atr_ratio_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sp = _corwin_schultz_spread(high, low)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(sp, atr).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_234_log_high_low_spread_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    return _rolling_pct_rank(_safe_log(high) - _safe_log(low), YDAYS)


def f20_vdah_235_spread_widening_streak_above_q75(high: pd.Series, low: pd.Series) -> pd.Series:
    sp = _corwin_schultz_spread(high, low)
    q = _rolling_quantile(sp, YDAYS, 0.75)
    return _consecutive_true_streak(sp > q).astype(float)


def f20_vdah_236_single_stock_trin_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    ad_ratio = _safe_div(up, dn + 1.0)
    vol_ratio = _safe_div(up_v, dn_v + 1.0)
    return _safe_div(ad_ratio, vol_ratio + 1e-9)


def f20_vdah_237_single_stock_trin_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(_safe_div(up, dn + 1.0), _safe_div(up_v, dn_v + 1.0) + 1e-9)


def f20_vdah_238_single_stock_trin_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(_safe_div(up, dn + 1.0), _safe_div(up_v, dn_v + 1.0) + 1e-9)


def f20_vdah_239_single_stock_trin_above_1_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    trin = _safe_div(_safe_div(up, dn + 1.0), _safe_div(up_v, dn_v + 1.0) + 1e-9)
    return (trin > 1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_240_trin_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    trin = _safe_div(_safe_div(up, dn + 1.0), _safe_div(up_v, dn_v + 1.0) + 1e-9)
    return _rolling_zscore(trin, YDAYS)


def f20_vdah_241_up_vol_to_total_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_v, tot)


def f20_vdah_242_down_vol_to_total_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn_v, tot)


def f20_vdah_243_down_vol_share_at_252d_high_only_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = close >= 0.95 * rmax
    sgn = np.sign(close.diff())
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    share = _safe_div(dn_v, tot)
    return share.where(flag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_244_supply_dominance_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    net = _safe_div(dn_v - up_v, tot)
    return net.rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_245_breadth_proxy_count_dryup_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    share = _safe_div(up_v, tot)
    return (share < 0.40).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_246_mutual_info_logvol_logreturn_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume); lr = _safe_log(close).diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        x = lv.iloc[i - QDAYS + 1 : i + 1].values
        y = lr.iloc[i - QDAYS + 1 : i + 1].values
        out.iloc[i] = _mutual_info_binned(x, y, bins=6)
    return out


def f20_vdah_247_mutual_info_logvol_absreturn_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume); ar = _safe_log(close).diff().abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        x = lv.iloc[i - QDAYS + 1 : i + 1].values
        y = ar.iloc[i - QDAYS + 1 : i + 1].values
        out.iloc[i] = _mutual_info_binned(x, y, bins=6)
    return out


def f20_vdah_248_mi_logvol_absreturn_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume); ar = _safe_log(close).diff().abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x = lv.iloc[i - YDAYS + 1 : i + 1].values
        y = ar.iloc[i - YDAYS + 1 : i + 1].values
        out.iloc[i] = _mutual_info_binned(x, y, bins=8)
    return out


def f20_vdah_249_mi_change_63_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume); ar = _safe_log(close).diff().abs()
    out63 = pd.Series(np.nan, index=close.index, dtype=float)
    out252 = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x63 = lv.iloc[i - QDAYS + 1 : i + 1].values
        y63 = ar.iloc[i - QDAYS + 1 : i + 1].values
        out63.iloc[i] = _mutual_info_binned(x63, y63, bins=6)
        x252 = lv.iloc[i - YDAYS + 1 : i + 1].values
        y252 = ar.iloc[i - YDAYS + 1 : i + 1].values
        out252.iloc[i] = _mutual_info_binned(x252, y252, bins=8)
    return out63 - out252


def f20_vdah_250_cross_entropy_logvol_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    bins = 10
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    n = len(volume)
    for i in range(YDAYS - 1, n):
        x252 = lv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        x63 = lv.iloc[i - QDAYS + 1 : i + 1].dropna().values
        if x252.size < 50 or x63.size < 20 or x252.max() == x252.min():
            continue
        edges = np.linspace(x252.min(), x252.max(), bins + 1)
        q, _ = np.histogram(x252, bins=edges)
        q = q.astype(float) / max(q.sum(), 1)
        p, _ = np.histogram(x63, bins=edges)
        p = p.astype(float) / max(p.sum(), 1)
        q = np.where(q == 0, 1e-9, q)
        out.iloc[i] = float(-(p * np.log(q)).sum())
    return out


def f20_vdah_251_transfer_entropy_proxy_vol_to_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv_lag = _safe_log(volume).shift(1)
    ar = _safe_log(close).diff().abs()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS, n):
        x = lv_lag.iloc[i - QDAYS + 1 : i + 1].values
        y = ar.iloc[i - QDAYS + 1 : i + 1].values
        out.iloc[i] = _mutual_info_binned(x, y, bins=6)
    return out


def f20_vdah_252_kl_divergence_recent_vs_baseline_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    bins = 8
    out = pd.Series(np.nan, index=volume.index, dtype=float)
    n = len(volume)
    for i in range(YDAYS - 1, n):
        x252 = lv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        x21 = lv.iloc[i - MDAYS + 1 : i + 1].dropna().values
        if x252.size < 50 or x21.size < 10 or x252.max() == x252.min():
            continue
        edges = np.linspace(x252.min(), x252.max(), bins + 1)
        q, _ = np.histogram(x252, bins=edges)
        q = q.astype(float) / max(q.sum(), 1)
        p, _ = np.histogram(x21, bins=edges)
        p = p.astype(float) / max(p.sum(), 1)
        q = np.where(q == 0, 1e-9, q)
        p_pos = p > 0
        out.iloc[i] = float((p[p_pos] * np.log(p[p_pos] / q[p_pos])).sum())
    return out


def f20_vdah_253_shannon_entropy_signed_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    sv = sgn * volume
    bins = 10
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        v = sv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        if v.size < 50 or v.max() == v.min():
            continue
        edges = np.linspace(v.min(), v.max(), bins + 1)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / max(h.sum(), 1)
        p = p[p > 0]
        out.iloc[i] = float(-(p * np.log(p)).sum())
    return out


def f20_vdah_254_joint_entropy_close_volume_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        c = close.iloc[i - YDAYS + 1 : i + 1].values
        v = lv.iloc[i - YDAYS + 1 : i + 1].values
        mask = (~np.isnan(c)) & (~np.isnan(v))
        if mask.sum() < 50:
            continue
        c = c[mask]; v = v[mask]
        if c.max() == c.min() or v.max() == v.min():
            continue
        ce = np.linspace(c.min(), c.max(), bins + 1)
        ve = np.linspace(v.min(), v.max(), bins + 1)
        h, _, _ = np.histogram2d(c, v, bins=[ce, ve])
        p = h.ravel() / max(h.sum(), 1)
        p = p[p > 0]
        out.iloc[i] = float(-(p * np.log(p)).sum())
    return out


def f20_vdah_255_conditional_entropy_volume_given_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        c = close.iloc[i - YDAYS + 1 : i + 1].values
        v = lv.iloc[i - YDAYS + 1 : i + 1].values
        mask = (~np.isnan(c)) & (~np.isnan(v))
        if mask.sum() < 50:
            continue
        c = c[mask]; v = v[mask]
        if c.max() == c.min() or v.max() == v.min():
            continue
        ce = np.linspace(c.min(), c.max(), bins + 1)
        ve = np.linspace(v.min(), v.max(), bins + 1)
        hcv, _, _ = np.histogram2d(c, v, bins=[ce, ve])
        pcv = hcv / max(hcv.sum(), 1)
        pc = pcv.sum(axis=1)
        pc_nz = pc > 0
        h_v_given_c = 0.0
        for j in np.where(pc_nz)[0]:
            cond = pcv[j, :] / pc[j]
            cond = cond[cond > 0]
            h_v_given_c += pc[j] * float(-(cond * np.log(cond)).sum())
        out.iloc[i] = h_v_given_c
    return out


def f20_vdah_256_haar_wavelet_level1_logvol_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    detail = (lv - lv.shift(1)) / np.sqrt(2.0)
    return detail.rolling(YDAYS, min_periods=QDAYS).std()


def f20_vdah_257_haar_wavelet_level2_logvol_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    smooth1 = (lv + lv.shift(1)) / np.sqrt(2.0)
    detail2 = (smooth1 - smooth1.shift(2)) / np.sqrt(2.0)
    return detail2.rolling(YDAYS, min_periods=QDAYS).std()


def f20_vdah_258_haar_wavelet_level3_logvol_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    s1 = (lv + lv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    detail3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    return detail3.rolling(YDAYS, min_periods=QDAYS).std()


def f20_vdah_259_wavelet_low_to_high_ratio_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    detail1 = (lv - lv.shift(1)) / np.sqrt(2.0)
    s1 = (lv + lv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    detail3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    s1_std = detail1.rolling(YDAYS, min_periods=QDAYS).std()
    s3_std = detail3.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s3_std, s1_std)


def f20_vdah_260_logvol_smooth_minus_raw_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    smoothed = lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return _rolling_zscore(smoothed - lv, YDAYS)


def f20_vdah_261_logvol_decay_constant_emadiff_21d_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    return lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() - lv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()


def f20_vdah_262_logvol_decay_constant_emadiff_63d_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    return lv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean() - lv.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()


def f20_vdah_263_logvol_multi_horizon_zscore_aggregate(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    return (_rolling_zscore(lv, MDAYS) + _rolling_zscore(lv, QDAYS) + _rolling_zscore(lv, YDAYS)) / 3.0


def f20_vdah_264_logvol_multi_horizon_zscore_dispersion(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    z21 = _rolling_zscore(lv, MDAYS); z63 = _rolling_zscore(lv, QDAYS); z252 = _rolling_zscore(lv, YDAYS)
    return pd.concat([z21, z63, z252], axis=1).std(axis=1)


def f20_vdah_265_logvol_hp_filter_proxy_residual_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    trend = lv.ewm(span=QDAYS * 2, min_periods=QDAYS, adjust=False).mean()
    return (lv - trend).rolling(YDAYS, min_periods=QDAYS).std()


def f20_vdah_266_logvol_har_residual_t(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    f5 = lv.rolling(WDAYS, min_periods=2).mean().shift(1)
    f21 = lv.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    f252 = lv.rolling(YDAYS, min_periods=QDAYS).mean().shift(1)
    def _res(idx):
        y = lv.iloc[idx].values
        X = np.column_stack([np.ones(len(idx)), f5.iloc[idx].values, f21.iloc[idx].values, f252.iloc[idx].values])
        mask = (~np.isnan(y)) & (~np.isnan(X).any(axis=1))
        if mask.sum() < 30:
            return np.nan
        Xm = X[mask]; ym = y[mask]
        try:
            coef, *_ = np.linalg.lstsq(Xm, ym, rcond=None)
        except Exception:
            return np.nan
        x_last = X[-1]
        if np.isnan(x_last).any() or np.isnan(y[-1]):
            return np.nan
        return float(y[-1] - x_last @ coef)
    out = pd.Series(np.nan, index=lv.index, dtype=float)
    n = len(lv)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_267_logvol_har_residual_zscore_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    f5 = lv.rolling(WDAYS, min_periods=2).mean().shift(1)
    f21 = lv.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    f252 = lv.rolling(YDAYS, min_periods=QDAYS).mean().shift(1)
    def _res(idx):
        y = lv.iloc[idx].values
        X = np.column_stack([np.ones(len(idx)), f5.iloc[idx].values, f21.iloc[idx].values, f252.iloc[idx].values])
        mask = (~np.isnan(y)) & (~np.isnan(X).any(axis=1))
        if mask.sum() < 30:
            return np.nan
        Xm = X[mask]; ym = y[mask]
        try:
            coef, *_ = np.linalg.lstsq(Xm, ym, rcond=None)
        except Exception:
            return np.nan
        x_last = X[-1]
        if np.isnan(x_last).any() or np.isnan(y[-1]):
            return np.nan
        return float(y[-1] - x_last @ coef)
    residual = pd.Series(np.nan, index=lv.index, dtype=float)
    n = len(lv)
    for i in range(YDAYS - 1, n):
        residual.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    return _rolling_zscore(residual, YDAYS)


def f20_vdah_268_count_volume_shocks_residual_z_below_neg1_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    f5 = lv.rolling(WDAYS, min_periods=2).mean().shift(1)
    f21 = lv.rolling(MDAYS, min_periods=WDAYS).mean().shift(1)
    f252 = lv.rolling(YDAYS, min_periods=QDAYS).mean().shift(1)
    def _res(idx):
        y = lv.iloc[idx].values
        X = np.column_stack([np.ones(len(idx)), f5.iloc[idx].values, f21.iloc[idx].values, f252.iloc[idx].values])
        mask = (~np.isnan(y)) & (~np.isnan(X).any(axis=1))
        if mask.sum() < 30:
            return np.nan
        try:
            coef, *_ = np.linalg.lstsq(X[mask], y[mask], rcond=None)
        except Exception:
            return np.nan
        x_last = X[-1]
        if np.isnan(x_last).any() or np.isnan(y[-1]):
            return np.nan
        return float(y[-1] - x_last @ coef)
    residual = pd.Series(np.nan, index=lv.index, dtype=float)
    n = len(lv)
    for i in range(YDAYS - 1, n):
        residual.iloc[i] = _res(range(i - YDAYS + 1, i + 1))
    z = _rolling_zscore(residual, YDAYS)
    return (z < -1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_269_volume_overnight_gap_proxy_zscore_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    shock = overnight * _safe_log(volume)
    return _rolling_zscore(shock, YDAYS)


def f20_vdah_270_log_volume_innovation_persistence_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ar1(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        a = v[:-1] - v[:-1].mean()
        b = v[1:] - v[1:].mean()
        d = (a * a).sum()
        return float((a * b).sum() / d) if d > 0 else np.nan
    return lv.rolling(QDAYS, min_periods=MDAYS).apply(_ar1, raw=True)


def f20_vdah_271_logvol_innovation_variance_decay_63d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _innov_var(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        a = v[:-1] - v[:-1].mean()
        b = v[1:] - v[1:].mean()
        d = (a * a).sum()
        ar = ((a * b).sum() / d) if d > 0 else 0.0
        innov = v[1:] - ar * v[:-1]
        return float(innov.var(ddof=1))
    return lv.rolling(QDAYS, min_periods=MDAYS).apply(_innov_var, raw=True)


def f20_vdah_272_logvol_innovation_kurt_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    trend = lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return (lv - trend).rolling(YDAYS, min_periods=QDAYS).kurt()


def f20_vdah_273_logvol_shock_negative_skew_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    trend = lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return (lv - trend).rolling(YDAYS, min_periods=QDAYS).skew()


def f20_vdah_274_volume_shock_overnight_morningstar_proxy(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    overnight = (_safe_log(open) - _safe_log(close.shift(1))).abs()
    shock = overnight * volume
    z = _rolling_zscore(shock, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    return z.where(rp >= 0.90, np.nan)


def f20_vdah_275_logvol_innovation_max_drawdown_252d(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    trend = lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    innov = lv - trend
    cum = innov.cumsum()
    def _mdd(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        rmax = np.maximum.accumulate(v)
        dd = v - rmax
        return float(dd.min())
    return cum.rolling(YDAYS, min_periods=QDAYS).apply(_mdd, raw=True)


def f20_vdah_276_avg_inter_arrival_3sigma_vol_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _mean_iat(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return float(v.size)
        return float(np.mean(np.diff(pos)))
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_mean_iat, raw=True)


def f20_vdah_277_std_inter_arrival_3sigma_vol_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _std_iat(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 3:
            return 0.0
        return float(np.std(np.diff(pos)))
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_std_iat, raw=True)


def f20_vdah_278_hazard_rate_3sigma_vol_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)


def f20_vdah_279_time_to_next_burst_pred_exponential_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rate = (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)
    return _safe_div(pd.Series(1.0, index=volume.index), rate)


def f20_vdah_280_burst_arrival_clustering_index_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _cv(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 3:
            return np.nan
        diffs = np.diff(pos)
        m = diffs.mean()
        if m <= 0:
            return np.nan
        return float(diffs.std() / m)
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_cv, raw=True)


def f20_vdah_281_dryup_event_arrival_rate_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (z < -1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)


def f20_vdah_282_ratio_burst_arrival_to_dryup_arrival_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    bursts = (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dryup = (z < -1.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(bursts, dryup + 1.0)


def f20_vdah_283_max_inter_arrival_burst_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _max_iat(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 2:
            return float(v.size)
        return float(np.max(np.diff(pos)))
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_max_iat, raw=True)


def f20_vdah_284_burst_to_dryup_time_balance_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    burst = (z > 3.0).astype(float).rolling(WDAYS, min_periods=1).max()
    dryup = (z < -1.0).astype(float).rolling(WDAYS, min_periods=1).max()
    return burst.rolling(YDAYS, min_periods=QDAYS).mean() - dryup.rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_285_burst_iat_pct_rank_252d(volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    def _pr(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        pos = np.where(v > 3.0)[0]
        if pos.size < 3:
            return np.nan
        diffs = np.diff(pos)
        return float((diffs <= diffs[-1]).sum() / diffs.size)
    return z.rolling(YDAYS, min_periods=QDAYS).apply(_pr, raw=True)


def f20_vdah_286_wyckoff_phase_b_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    cond = (rp >= 0.90) & (z < 0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f20_vdah_287_wyckoff_phase_c_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    flag = (new_high & closed_weak & vol_high & (rp >= 0.85)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_288_wyckoff_phase_d_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    flag = (pc < -0.02) & (volume > 1.5 * med21)
    return flag.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_289_wyckoff_phase_e_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return ((close < ema63) & (z > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f20_vdah_290_wyckoff_composite_distribution_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    phase_b = ((rp >= 0.90) & (z < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    phase_c = (new_high & closed_weak & vol_high & (rp >= 0.85)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    phase_d = ((pc < -0.02) & (volume > 1.5 * med21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    phase_e = ((close < ema63) & (z > 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return phase_b + phase_c + phase_d + phase_e


def f20_vdah_291_composite_dryup_breadth_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up = (sgn > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (sgn < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    up_v = volume.where(sgn > 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    trin = _safe_div(_safe_div(up, dn + 1.0), _safe_div(up_v, dn_v + 1.0) + 1e-9)
    med252 = volume.rolling(YDAYS, min_periods=QDAYS).median()
    frac_below = (volume < med252).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    base = volume.rolling(QDAYS * 4, min_periods=QDAYS).mean()
    shock = (volume - base).clip(lower=0.0)
    ema21 = shock.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    ema63 = shock.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    hawkes_ratio = _safe_div(ema21, ema63)
    return ((trin > 1).astype(float)
            + (frac_below > 0.5).astype(float)
            + (hawkes_ratio < 1.0).astype(float))


def f20_vdah_292_dryup_distribution_compound_index_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    phase_b = ((rp >= 0.90) & (z < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    phase_d = ((pc < -0.02) & (volume > 1.5 * med21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    med252 = volume.rolling(YDAYS, min_periods=QDAYS).median()
    frac_below = (volume < med252).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return (phase_b + phase_d) * frac_below


def f20_vdah_293_distribution_composite_signal_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut_recent = (new_high & closed_weak & vol_high).astype(float).rolling(MDAYS, min_periods=1).max()
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    dd_cluster = (dd.rolling(25, min_periods=10).sum() >= 4).astype(float)
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    nd_vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    nd_recent = (up & narrow & near_high & nd_vol_low).astype(float).rolling(MDAYS, min_periods=1).max()
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    lpsy_recent = (breakdown & rally_5d & vol_low).astype(float).rolling(MDAYS, min_periods=1).max()
    return ut_recent + dd_cluster + nd_recent + lpsy_recent


def f20_vdah_294_dryup_after_climax_signature_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    had_burst = (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
    cur_low = volume.rolling(MDAYS, min_periods=WDAYS).mean() < volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((had_burst > 0) & cur_low).astype(float).where(had_burst.notna(), np.nan)


def f20_vdah_295_dryup_intensity_weighted_by_close_at_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin).fillna(0.0)
    def _pr(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    pr_v = volume.rolling(YDAYS, min_periods=QDAYS).apply(_pr, raw=True).fillna(0.5)
    return ((rp ** 2) * (1.0 - pr_v)).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_296_supply_overhang_proxy_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    dn = close < close.shift(1)
    return volume.where((rp >= 0.90) & dn, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_297_distribution_volume_to_advance_volume_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    top = rp >= 0.90
    up = close > close.shift(1)
    dn = close < close.shift(1)
    up_v = volume.where(top & up, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    dn_v = volume.where(top & dn, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dn_v, up_v + 1.0)


def f20_vdah_298_buying_climax_followed_by_dryup_within_63d_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    climax = (z > 3.0) & (high >= rmax)
    had = climax.astype(float).rolling(QDAYS, min_periods=MDAYS).max()
    cur_low = volume.rolling(MDAYS, min_periods=WDAYS).mean() < volume.rolling(YDAYS, min_periods=QDAYS).median()
    return ((had > 0) & cur_low).astype(float)


def f20_vdah_299_vsa_climax_dryup_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    climax = (z > 3.0) & (high >= rmax)
    had = climax.astype(float).rolling(QDAYS, min_periods=MDAYS).max()
    cur_low = volume.rolling(MDAYS, min_periods=WDAYS).mean() < volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((had > 0) & cur_low).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_300_overall_distribution_certainty_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    phase_b = ((rp >= 0.90) & (z < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    phase_d = ((pc < -0.02) & (volume > 1.5 * med21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = close < close.shift(1)
    overhang = volume.where((rp >= 0.90) & dn, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    overhang_scaled = _rolling_zscore(overhang, YDAYS).fillna(0.0)
    churn = _safe_div(volume, close.diff().abs())
    churn_z = _rolling_zscore(churn, YDAYS).fillna(0.0)
    had_burst = (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
    cur_low = (volume.rolling(MDAYS, min_periods=WDAYS).mean() < volume.rolling(YDAYS, min_periods=QDAYS).median()).astype(float)
    dryup_after = had_burst * cur_low
    return phase_b + phase_d / 10.0 + overhang_scaled + churn_z.clip(lower=-3.0, upper=3.0) + 2.0 * dryup_after


def f20_vdah_226_corwin_schultz_spread_daily_d3(high, low):
    return f20_vdah_226_corwin_schultz_spread_daily(high, low).diff().diff().diff()


def f20_vdah_227_corwin_schultz_spread_21d_mean_d3(high, low):
    return f20_vdah_227_corwin_schultz_spread_21d_mean(high, low).diff().diff().diff()


def f20_vdah_228_corwin_schultz_spread_zscore_252d_d3(high, low):
    return f20_vdah_228_corwin_schultz_spread_zscore_252d(high, low).diff().diff().diff()


def f20_vdah_229_spread_proxy_gated_at_252d_high_mean_d3(high, low):
    return f20_vdah_229_spread_proxy_gated_at_252d_high_mean(high, low).diff().diff().diff()


def f20_vdah_230_spread_zscore_at_high_minus_baseline_d3(high, low):
    return f20_vdah_230_spread_zscore_at_high_minus_baseline(high, low).diff().diff().diff()


def f20_vdah_231_amihud_proxy_252d_mean_d3(close, volume):
    return f20_vdah_231_amihud_proxy_252d_mean(close, volume).diff().diff().diff()


def f20_vdah_232_amihud_proxy_zscore_252d_d3(close, volume):
    return f20_vdah_232_amihud_proxy_zscore_252d(close, volume).diff().diff().diff()


def f20_vdah_233_spread_to_atr_ratio_252d_mean_d3(high, low, close):
    return f20_vdah_233_spread_to_atr_ratio_252d_mean(high, low, close).diff().diff().diff()


def f20_vdah_234_log_high_low_spread_pct_rank_252d_d3(high, low):
    return f20_vdah_234_log_high_low_spread_pct_rank_252d(high, low).diff().diff().diff()


def f20_vdah_235_spread_widening_streak_above_q75_d3(high, low):
    return f20_vdah_235_spread_widening_streak_above_q75(high, low).diff().diff().diff()


def f20_vdah_236_single_stock_trin_21d_d3(close, volume):
    return f20_vdah_236_single_stock_trin_21d(close, volume).diff().diff().diff()


def f20_vdah_237_single_stock_trin_63d_d3(close, volume):
    return f20_vdah_237_single_stock_trin_63d(close, volume).diff().diff().diff()


def f20_vdah_238_single_stock_trin_252d_d3(close, volume):
    return f20_vdah_238_single_stock_trin_252d(close, volume).diff().diff().diff()


def f20_vdah_239_single_stock_trin_above_1_dwell_252d_d3(close, volume):
    return f20_vdah_239_single_stock_trin_above_1_dwell_252d(close, volume).diff().diff().diff()


def f20_vdah_240_trin_zscore_252d_d3(close, volume):
    return f20_vdah_240_trin_zscore_252d(close, volume).diff().diff().diff()


def f20_vdah_241_up_vol_to_total_vol_ratio_21d_d3(close, volume):
    return f20_vdah_241_up_vol_to_total_vol_ratio_21d(close, volume).diff().diff().diff()


def f20_vdah_242_down_vol_to_total_vol_ratio_21d_d3(close, volume):
    return f20_vdah_242_down_vol_to_total_vol_ratio_21d(close, volume).diff().diff().diff()


def f20_vdah_243_down_vol_share_at_252d_high_only_252d_d3(high, close, volume):
    return f20_vdah_243_down_vol_share_at_252d_high_only_252d(high, close, volume).diff().diff().diff()


def f20_vdah_244_supply_dominance_intensity_252d_d3(close, volume):
    return f20_vdah_244_supply_dominance_intensity_252d(close, volume).diff().diff().diff()


def f20_vdah_245_breadth_proxy_count_dryup_252d_d3(close, volume):
    return f20_vdah_245_breadth_proxy_count_dryup_252d(close, volume).diff().diff().diff()


def f20_vdah_246_mutual_info_logvol_logreturn_63d_d3(close, volume):
    return f20_vdah_246_mutual_info_logvol_logreturn_63d(close, volume).diff().diff().diff()


def f20_vdah_247_mutual_info_logvol_absreturn_63d_d3(close, volume):
    return f20_vdah_247_mutual_info_logvol_absreturn_63d(close, volume).diff().diff().diff()


def f20_vdah_248_mi_logvol_absreturn_252d_d3(close, volume):
    return f20_vdah_248_mi_logvol_absreturn_252d(close, volume).diff().diff().diff()


def f20_vdah_249_mi_change_63_minus_252_d3(close, volume):
    return f20_vdah_249_mi_change_63_minus_252(close, volume).diff().diff().diff()


def f20_vdah_250_cross_entropy_logvol_252d_d3(volume):
    return f20_vdah_250_cross_entropy_logvol_252d(volume).diff().diff().diff()


def f20_vdah_251_transfer_entropy_proxy_vol_to_return_63d_d3(close, volume):
    return f20_vdah_251_transfer_entropy_proxy_vol_to_return_63d(close, volume).diff().diff().diff()


def f20_vdah_252_kl_divergence_recent_vs_baseline_252d_d3(volume):
    return f20_vdah_252_kl_divergence_recent_vs_baseline_252d(volume).diff().diff().diff()


def f20_vdah_253_shannon_entropy_signed_volume_252d_d3(close, volume):
    return f20_vdah_253_shannon_entropy_signed_volume_252d(close, volume).diff().diff().diff()


def f20_vdah_254_joint_entropy_close_volume_252d_d3(close, volume):
    return f20_vdah_254_joint_entropy_close_volume_252d(close, volume).diff().diff().diff()


def f20_vdah_255_conditional_entropy_volume_given_price_252d_d3(close, volume):
    return f20_vdah_255_conditional_entropy_volume_given_price_252d(close, volume).diff().diff().diff()


def f20_vdah_256_haar_wavelet_level1_logvol_252d_d3(volume):
    return f20_vdah_256_haar_wavelet_level1_logvol_252d(volume).diff().diff().diff()


def f20_vdah_257_haar_wavelet_level2_logvol_252d_d3(volume):
    return f20_vdah_257_haar_wavelet_level2_logvol_252d(volume).diff().diff().diff()


def f20_vdah_258_haar_wavelet_level3_logvol_252d_d3(volume):
    return f20_vdah_258_haar_wavelet_level3_logvol_252d(volume).diff().diff().diff()


def f20_vdah_259_wavelet_low_to_high_ratio_252d_d3(volume):
    return f20_vdah_259_wavelet_low_to_high_ratio_252d(volume).diff().diff().diff()


def f20_vdah_260_logvol_smooth_minus_raw_252d_d3(volume):
    return f20_vdah_260_logvol_smooth_minus_raw_252d(volume).diff().diff().diff()


def f20_vdah_261_logvol_decay_constant_emadiff_21d_63d_d3(volume):
    return f20_vdah_261_logvol_decay_constant_emadiff_21d_63d(volume).diff().diff().diff()


def f20_vdah_262_logvol_decay_constant_emadiff_63d_252d_d3(volume):
    return f20_vdah_262_logvol_decay_constant_emadiff_63d_252d(volume).diff().diff().diff()


def f20_vdah_263_logvol_multi_horizon_zscore_aggregate_d3(volume):
    return f20_vdah_263_logvol_multi_horizon_zscore_aggregate(volume).diff().diff().diff()


def f20_vdah_264_logvol_multi_horizon_zscore_dispersion_d3(volume):
    return f20_vdah_264_logvol_multi_horizon_zscore_dispersion(volume).diff().diff().diff()


def f20_vdah_265_logvol_hp_filter_proxy_residual_252d_d3(volume):
    return f20_vdah_265_logvol_hp_filter_proxy_residual_252d(volume).diff().diff().diff()


def f20_vdah_266_logvol_har_residual_t_d3(volume):
    return f20_vdah_266_logvol_har_residual_t(volume).diff().diff().diff()


def f20_vdah_267_logvol_har_residual_zscore_252d_d3(volume):
    return f20_vdah_267_logvol_har_residual_zscore_252d(volume).diff().diff().diff()


def f20_vdah_268_count_volume_shocks_residual_z_below_neg1_63d_d3(volume):
    return f20_vdah_268_count_volume_shocks_residual_z_below_neg1_63d(volume).diff().diff().diff()


def f20_vdah_269_volume_overnight_gap_proxy_zscore_252d_d3(open, close, volume):
    return f20_vdah_269_volume_overnight_gap_proxy_zscore_252d(open, close, volume).diff().diff().diff()


def f20_vdah_270_log_volume_innovation_persistence_63d_d3(volume):
    return f20_vdah_270_log_volume_innovation_persistence_63d(volume).diff().diff().diff()


def f20_vdah_271_logvol_innovation_variance_decay_63d_d3(volume):
    return f20_vdah_271_logvol_innovation_variance_decay_63d(volume).diff().diff().diff()


def f20_vdah_272_logvol_innovation_kurt_252d_d3(volume):
    return f20_vdah_272_logvol_innovation_kurt_252d(volume).diff().diff().diff()


def f20_vdah_273_logvol_shock_negative_skew_252d_d3(volume):
    return f20_vdah_273_logvol_shock_negative_skew_252d(volume).diff().diff().diff()


def f20_vdah_274_volume_shock_overnight_morningstar_proxy_d3(open, high, low, close, volume):
    return f20_vdah_274_volume_shock_overnight_morningstar_proxy(open, high, low, close, volume).diff().diff().diff()


def f20_vdah_275_logvol_innovation_max_drawdown_252d_d3(volume):
    return f20_vdah_275_logvol_innovation_max_drawdown_252d(volume).diff().diff().diff()


def f20_vdah_276_avg_inter_arrival_3sigma_vol_252d_d3(volume):
    return f20_vdah_276_avg_inter_arrival_3sigma_vol_252d(volume).diff().diff().diff()


def f20_vdah_277_std_inter_arrival_3sigma_vol_252d_d3(volume):
    return f20_vdah_277_std_inter_arrival_3sigma_vol_252d(volume).diff().diff().diff()


def f20_vdah_278_hazard_rate_3sigma_vol_252d_d3(volume):
    return f20_vdah_278_hazard_rate_3sigma_vol_252d(volume).diff().diff().diff()


def f20_vdah_279_time_to_next_burst_pred_exponential_252d_d3(volume):
    return f20_vdah_279_time_to_next_burst_pred_exponential_252d(volume).diff().diff().diff()


def f20_vdah_280_burst_arrival_clustering_index_252d_d3(volume):
    return f20_vdah_280_burst_arrival_clustering_index_252d(volume).diff().diff().diff()


def f20_vdah_281_dryup_event_arrival_rate_252d_d3(volume):
    return f20_vdah_281_dryup_event_arrival_rate_252d(volume).diff().diff().diff()


def f20_vdah_282_ratio_burst_arrival_to_dryup_arrival_252d_d3(volume):
    return f20_vdah_282_ratio_burst_arrival_to_dryup_arrival_252d(volume).diff().diff().diff()


def f20_vdah_283_max_inter_arrival_burst_252d_d3(volume):
    return f20_vdah_283_max_inter_arrival_burst_252d(volume).diff().diff().diff()


def f20_vdah_284_burst_to_dryup_time_balance_252d_d3(volume):
    return f20_vdah_284_burst_to_dryup_time_balance_252d(volume).diff().diff().diff()


def f20_vdah_285_burst_iat_pct_rank_252d_d3(volume):
    return f20_vdah_285_burst_iat_pct_rank_252d(volume).diff().diff().diff()


def f20_vdah_286_wyckoff_phase_b_score_252d_d3(high, low, close, volume):
    return f20_vdah_286_wyckoff_phase_b_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_287_wyckoff_phase_c_score_252d_d3(high, low, close, volume):
    return f20_vdah_287_wyckoff_phase_c_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_288_wyckoff_phase_d_score_252d_d3(high, low, close, volume):
    return f20_vdah_288_wyckoff_phase_d_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_289_wyckoff_phase_e_score_252d_d3(high, low, close, volume):
    return f20_vdah_289_wyckoff_phase_e_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_290_wyckoff_composite_distribution_score_252d_d3(high, low, close, volume):
    return f20_vdah_290_wyckoff_composite_distribution_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_291_composite_dryup_breadth_score_252d_d3(high, low, close, volume):
    return f20_vdah_291_composite_dryup_breadth_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_292_dryup_distribution_compound_index_252d_d3(high, low, close, volume):
    return f20_vdah_292_dryup_distribution_compound_index_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_293_distribution_composite_signal_252d_d3(high, low, close, volume):
    return f20_vdah_293_distribution_composite_signal_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_294_dryup_after_climax_signature_score_252d_d3(high, low, close, volume):
    return f20_vdah_294_dryup_after_climax_signature_score_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_295_dryup_intensity_weighted_by_close_at_high_252d_d3(high, low, close, volume):
    return f20_vdah_295_dryup_intensity_weighted_by_close_at_high_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_296_supply_overhang_proxy_252d_d3(high, low, close, volume):
    return f20_vdah_296_supply_overhang_proxy_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_297_distribution_volume_to_advance_volume_ratio_252d_d3(high, low, close, volume):
    return f20_vdah_297_distribution_volume_to_advance_volume_ratio_252d(high, low, close, volume).diff().diff().diff()


def f20_vdah_298_buying_climax_followed_by_dryup_within_63d_indicator_d3(high, close, volume):
    return f20_vdah_298_buying_climax_followed_by_dryup_within_63d_indicator(high, close, volume).diff().diff().diff()


def f20_vdah_299_vsa_climax_dryup_count_252d_d3(high, close, volume):
    return f20_vdah_299_vsa_climax_dryup_count_252d(high, close, volume).diff().diff().diff()


def f20_vdah_300_overall_distribution_certainty_score_252d_d3(high, low, close, volume):
    return f20_vdah_300_overall_distribution_certainty_score_252d(high, low, close, volume).diff().diff().diff()


VOLUME_DRYUP_AT_HIGH_D3_REGISTRY_226_300 = {
    "f20_vdah_226_corwin_schultz_spread_daily_d3": {"inputs": ["high", "low"], "func": f20_vdah_226_corwin_schultz_spread_daily_d3},
    "f20_vdah_227_corwin_schultz_spread_21d_mean_d3": {"inputs": ["high", "low"], "func": f20_vdah_227_corwin_schultz_spread_21d_mean_d3},
    "f20_vdah_228_corwin_schultz_spread_zscore_252d_d3": {"inputs": ["high", "low"], "func": f20_vdah_228_corwin_schultz_spread_zscore_252d_d3},
    "f20_vdah_229_spread_proxy_gated_at_252d_high_mean_d3": {"inputs": ["high", "low"], "func": f20_vdah_229_spread_proxy_gated_at_252d_high_mean_d3},
    "f20_vdah_230_spread_zscore_at_high_minus_baseline_d3": {"inputs": ["high", "low"], "func": f20_vdah_230_spread_zscore_at_high_minus_baseline_d3},
    "f20_vdah_231_amihud_proxy_252d_mean_d3": {"inputs": ["close", "volume"], "func": f20_vdah_231_amihud_proxy_252d_mean_d3},
    "f20_vdah_232_amihud_proxy_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_232_amihud_proxy_zscore_252d_d3},
    "f20_vdah_233_spread_to_atr_ratio_252d_mean_d3": {"inputs": ["high", "low", "close"], "func": f20_vdah_233_spread_to_atr_ratio_252d_mean_d3},
    "f20_vdah_234_log_high_low_spread_pct_rank_252d_d3": {"inputs": ["high", "low"], "func": f20_vdah_234_log_high_low_spread_pct_rank_252d_d3},
    "f20_vdah_235_spread_widening_streak_above_q75_d3": {"inputs": ["high", "low"], "func": f20_vdah_235_spread_widening_streak_above_q75_d3},
    "f20_vdah_236_single_stock_trin_21d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_236_single_stock_trin_21d_d3},
    "f20_vdah_237_single_stock_trin_63d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_237_single_stock_trin_63d_d3},
    "f20_vdah_238_single_stock_trin_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_238_single_stock_trin_252d_d3},
    "f20_vdah_239_single_stock_trin_above_1_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_239_single_stock_trin_above_1_dwell_252d_d3},
    "f20_vdah_240_trin_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_240_trin_zscore_252d_d3},
    "f20_vdah_241_up_vol_to_total_vol_ratio_21d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_241_up_vol_to_total_vol_ratio_21d_d3},
    "f20_vdah_242_down_vol_to_total_vol_ratio_21d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_242_down_vol_to_total_vol_ratio_21d_d3},
    "f20_vdah_243_down_vol_share_at_252d_high_only_252d_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_243_down_vol_share_at_252d_high_only_252d_d3},
    "f20_vdah_244_supply_dominance_intensity_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_244_supply_dominance_intensity_252d_d3},
    "f20_vdah_245_breadth_proxy_count_dryup_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_245_breadth_proxy_count_dryup_252d_d3},
    "f20_vdah_246_mutual_info_logvol_logreturn_63d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_246_mutual_info_logvol_logreturn_63d_d3},
    "f20_vdah_247_mutual_info_logvol_absreturn_63d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_247_mutual_info_logvol_absreturn_63d_d3},
    "f20_vdah_248_mi_logvol_absreturn_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_248_mi_logvol_absreturn_252d_d3},
    "f20_vdah_249_mi_change_63_minus_252_d3": {"inputs": ["close", "volume"], "func": f20_vdah_249_mi_change_63_minus_252_d3},
    "f20_vdah_250_cross_entropy_logvol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_250_cross_entropy_logvol_252d_d3},
    "f20_vdah_251_transfer_entropy_proxy_vol_to_return_63d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_251_transfer_entropy_proxy_vol_to_return_63d_d3},
    "f20_vdah_252_kl_divergence_recent_vs_baseline_252d_d3": {"inputs": ["volume"], "func": f20_vdah_252_kl_divergence_recent_vs_baseline_252d_d3},
    "f20_vdah_253_shannon_entropy_signed_volume_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_253_shannon_entropy_signed_volume_252d_d3},
    "f20_vdah_254_joint_entropy_close_volume_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_254_joint_entropy_close_volume_252d_d3},
    "f20_vdah_255_conditional_entropy_volume_given_price_252d_d3": {"inputs": ["close", "volume"], "func": f20_vdah_255_conditional_entropy_volume_given_price_252d_d3},
    "f20_vdah_256_haar_wavelet_level1_logvol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_256_haar_wavelet_level1_logvol_252d_d3},
    "f20_vdah_257_haar_wavelet_level2_logvol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_257_haar_wavelet_level2_logvol_252d_d3},
    "f20_vdah_258_haar_wavelet_level3_logvol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_258_haar_wavelet_level3_logvol_252d_d3},
    "f20_vdah_259_wavelet_low_to_high_ratio_252d_d3": {"inputs": ["volume"], "func": f20_vdah_259_wavelet_low_to_high_ratio_252d_d3},
    "f20_vdah_260_logvol_smooth_minus_raw_252d_d3": {"inputs": ["volume"], "func": f20_vdah_260_logvol_smooth_minus_raw_252d_d3},
    "f20_vdah_261_logvol_decay_constant_emadiff_21d_63d_d3": {"inputs": ["volume"], "func": f20_vdah_261_logvol_decay_constant_emadiff_21d_63d_d3},
    "f20_vdah_262_logvol_decay_constant_emadiff_63d_252d_d3": {"inputs": ["volume"], "func": f20_vdah_262_logvol_decay_constant_emadiff_63d_252d_d3},
    "f20_vdah_263_logvol_multi_horizon_zscore_aggregate_d3": {"inputs": ["volume"], "func": f20_vdah_263_logvol_multi_horizon_zscore_aggregate_d3},
    "f20_vdah_264_logvol_multi_horizon_zscore_dispersion_d3": {"inputs": ["volume"], "func": f20_vdah_264_logvol_multi_horizon_zscore_dispersion_d3},
    "f20_vdah_265_logvol_hp_filter_proxy_residual_252d_d3": {"inputs": ["volume"], "func": f20_vdah_265_logvol_hp_filter_proxy_residual_252d_d3},
    "f20_vdah_266_logvol_har_residual_t_d3": {"inputs": ["volume"], "func": f20_vdah_266_logvol_har_residual_t_d3},
    "f20_vdah_267_logvol_har_residual_zscore_252d_d3": {"inputs": ["volume"], "func": f20_vdah_267_logvol_har_residual_zscore_252d_d3},
    "f20_vdah_268_count_volume_shocks_residual_z_below_neg1_63d_d3": {"inputs": ["volume"], "func": f20_vdah_268_count_volume_shocks_residual_z_below_neg1_63d_d3},
    "f20_vdah_269_volume_overnight_gap_proxy_zscore_252d_d3": {"inputs": ["open", "close", "volume"], "func": f20_vdah_269_volume_overnight_gap_proxy_zscore_252d_d3},
    "f20_vdah_270_log_volume_innovation_persistence_63d_d3": {"inputs": ["volume"], "func": f20_vdah_270_log_volume_innovation_persistence_63d_d3},
    "f20_vdah_271_logvol_innovation_variance_decay_63d_d3": {"inputs": ["volume"], "func": f20_vdah_271_logvol_innovation_variance_decay_63d_d3},
    "f20_vdah_272_logvol_innovation_kurt_252d_d3": {"inputs": ["volume"], "func": f20_vdah_272_logvol_innovation_kurt_252d_d3},
    "f20_vdah_273_logvol_shock_negative_skew_252d_d3": {"inputs": ["volume"], "func": f20_vdah_273_logvol_shock_negative_skew_252d_d3},
    "f20_vdah_274_volume_shock_overnight_morningstar_proxy_d3": {"inputs": ["open", "high", "low", "close", "volume"], "func": f20_vdah_274_volume_shock_overnight_morningstar_proxy_d3},
    "f20_vdah_275_logvol_innovation_max_drawdown_252d_d3": {"inputs": ["volume"], "func": f20_vdah_275_logvol_innovation_max_drawdown_252d_d3},
    "f20_vdah_276_avg_inter_arrival_3sigma_vol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_276_avg_inter_arrival_3sigma_vol_252d_d3},
    "f20_vdah_277_std_inter_arrival_3sigma_vol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_277_std_inter_arrival_3sigma_vol_252d_d3},
    "f20_vdah_278_hazard_rate_3sigma_vol_252d_d3": {"inputs": ["volume"], "func": f20_vdah_278_hazard_rate_3sigma_vol_252d_d3},
    "f20_vdah_279_time_to_next_burst_pred_exponential_252d_d3": {"inputs": ["volume"], "func": f20_vdah_279_time_to_next_burst_pred_exponential_252d_d3},
    "f20_vdah_280_burst_arrival_clustering_index_252d_d3": {"inputs": ["volume"], "func": f20_vdah_280_burst_arrival_clustering_index_252d_d3},
    "f20_vdah_281_dryup_event_arrival_rate_252d_d3": {"inputs": ["volume"], "func": f20_vdah_281_dryup_event_arrival_rate_252d_d3},
    "f20_vdah_282_ratio_burst_arrival_to_dryup_arrival_252d_d3": {"inputs": ["volume"], "func": f20_vdah_282_ratio_burst_arrival_to_dryup_arrival_252d_d3},
    "f20_vdah_283_max_inter_arrival_burst_252d_d3": {"inputs": ["volume"], "func": f20_vdah_283_max_inter_arrival_burst_252d_d3},
    "f20_vdah_284_burst_to_dryup_time_balance_252d_d3": {"inputs": ["volume"], "func": f20_vdah_284_burst_to_dryup_time_balance_252d_d3},
    "f20_vdah_285_burst_iat_pct_rank_252d_d3": {"inputs": ["volume"], "func": f20_vdah_285_burst_iat_pct_rank_252d_d3},
    "f20_vdah_286_wyckoff_phase_b_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_286_wyckoff_phase_b_score_252d_d3},
    "f20_vdah_287_wyckoff_phase_c_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_287_wyckoff_phase_c_score_252d_d3},
    "f20_vdah_288_wyckoff_phase_d_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_288_wyckoff_phase_d_score_252d_d3},
    "f20_vdah_289_wyckoff_phase_e_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_289_wyckoff_phase_e_score_252d_d3},
    "f20_vdah_290_wyckoff_composite_distribution_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_290_wyckoff_composite_distribution_score_252d_d3},
    "f20_vdah_291_composite_dryup_breadth_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_291_composite_dryup_breadth_score_252d_d3},
    "f20_vdah_292_dryup_distribution_compound_index_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_292_dryup_distribution_compound_index_252d_d3},
    "f20_vdah_293_distribution_composite_signal_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_293_distribution_composite_signal_252d_d3},
    "f20_vdah_294_dryup_after_climax_signature_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_294_dryup_after_climax_signature_score_252d_d3},
    "f20_vdah_295_dryup_intensity_weighted_by_close_at_high_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_295_dryup_intensity_weighted_by_close_at_high_252d_d3},
    "f20_vdah_296_supply_overhang_proxy_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_296_supply_overhang_proxy_252d_d3},
    "f20_vdah_297_distribution_volume_to_advance_volume_ratio_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_297_distribution_volume_to_advance_volume_ratio_252d_d3},
    "f20_vdah_298_buying_climax_followed_by_dryup_within_63d_indicator_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_298_buying_climax_followed_by_dryup_within_63d_indicator_d3},
    "f20_vdah_299_vsa_climax_dryup_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f20_vdah_299_vsa_climax_dryup_count_252d_d3},
    "f20_vdah_300_overall_distribution_certainty_score_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_300_overall_distribution_certainty_score_252d_d3},
}
