"""27_macd_topping_dynamics d1 features 451-525 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260
_BFS = [(5, 35), (12, 26), (19, 39), (50, 200)]

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

def _slope_inner(w):
    valid = ~np.isnan(w)
    if valid.sum() < 2:
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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(_slope_inner, raw=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()

def _macd(close, fast=12, slow=26, signal=9):
    macd = _ema(close, fast) - _ema(close, slow)
    sig = _ema(macd, signal)
    histo = macd - sig
    return (macd, sig, histo)

def _ppo(close, fast=12, slow=26, signal=9):
    ef = _ema(close, fast)
    es = _ema(close, slow)
    ppo = 100.0 * _safe_div(ef - es, es)
    sig = _ema(ppo, signal)
    histo = ppo - sig
    return (ppo, sig, histo)

def _bars_since_true(mask: pd.Series) -> pd.Series:
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

def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)

def _rsi_wilder(s, n=14):
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = (-d).clip(lower=0.0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)

def _stoch_pct(s, n=14):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return 100.0 * _safe_div(s - lo, hi - lo)

def _williams_r(s, n=14):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hi - s, hi - lo)

def _trix(s, n=15):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()

def _tsi(s, r=25, ss=13):
    d = s.diff()
    da = d.abs()
    ee = _ema(_ema(d, r), ss)
    aa = _ema(_ema(da, r), ss)
    return 100.0 * _safe_div(ee, aa)

def _cci_of(s, n=20):
    sd = s.rolling(n, min_periods=max(n // 3, 2)).std()
    sm = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(s - sm, 0.015 * sd)

def _cmo(s, n=14):
    d = s.diff()
    up = d.clip(lower=0.0).rolling(n, min_periods=max(n // 3, 2)).sum()
    dn = (-d).clip(lower=0.0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(up - dn, up + dn)

def _fisher_transform(s, n=10):
    lo = s.rolling(n, min_periods=max(n // 3, 2)).min()
    hi = s.rolling(n, min_periods=max(n // 3, 2)).max()
    raw = 2.0 * _safe_div(s - lo, hi - lo) - 1.0
    raw = raw.clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + raw) / (1.0 - raw))

def _inverse_fisher(s):
    s2 = s.clip(-10.0, 10.0)
    e = np.exp(2.0 * s2)
    return _safe_div(e - 1.0, e + 1.0)

def _quantile_normal_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    rank = float((v <= last).sum()) / float(nn + 1)
    rank = min(max(rank, 0.0001), 1 - 0.0001)
    return float(np.sqrt(2.0) * _erfinv_scalar(2.0 * rank - 1.0))

def _erfinv_scalar(x):
    a = 0.147
    ln = np.log(1.0 - x * x)
    t = 2.0 / (np.pi * a) + ln / 2.0
    return float(np.sign(x) * np.sqrt(np.sqrt(t * t - ln / a) - t))

def _quantile_uniform_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    return float((v <= last).sum()) / float(nn + 1)

def _mad_zscore_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    med = np.median(v)
    mad = np.median(np.abs(v - med))
    if mad <= 0:
        return np.nan
    return float((last - med) / (1.4826 * mad))

def _iqr_zscore_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    q1, q3 = np.quantile(v, [0.25, 0.75])
    iqr = q3 - q1
    if iqr <= 0:
        return np.nan
    return float((last - np.median(v)) / (iqr / 1.349))

def _winsorized_zscore_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    lo, hi = np.quantile(v, [0.05, 0.95])
    vw = np.clip(v, lo, hi)
    sd = vw.std()
    if sd <= 0:
        return np.nan
    return float((last - vw.mean()) / sd)

def _band_position_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < MDAYS:
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    q10, q90 = np.quantile(v, [0.1, 0.9])
    if q90 == q10:
        return np.nan
    return float((last - q10) / (q90 - q10))

def _pct_rank_window(w):
    if np.isnan(w).all():
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[~np.isnan(w)]
    if v.size == 0:
        return np.nan
    return float((v <= last).sum()) / float(v.size)

def _rolling_resid_inner(arr):
    pass

def _rolling_regression_residual(y, x, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 5)
    mx = x.rolling(n, min_periods=min_periods).mean()
    my = y.rolling(n, min_periods=min_periods).mean()
    cov = (x * y).rolling(n, min_periods=min_periods).mean() - mx * my
    var = (x * x).rolling(n, min_periods=min_periods).mean() - mx * mx
    beta = _safe_div(cov, var)
    alpha = my - beta * mx
    return y - (alpha + beta * x)

def _rolling_regression_beta(y, x, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 5)
    mx = x.rolling(n, min_periods=min_periods).mean()
    my = y.rolling(n, min_periods=min_periods).mean()
    cov = (x * y).rolling(n, min_periods=min_periods).mean() - mx * my
    var = (x * x).rolling(n, min_periods=min_periods).mean() - mx * mx
    return _safe_div(cov, var)

def _path_length_window(w):
    v = w[~np.isnan(w)]
    if v.size < 2:
        return np.nan
    return float(np.abs(np.diff(v)).sum())

def _path_curvature_window(w):
    v = w[~np.isnan(w)]
    if v.size < 3:
        return np.nan
    return float(np.abs(np.diff(np.diff(v))).sum())

def _path_complexity_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 4:
        return np.nan
    pl = np.abs(np.diff(v)).sum()
    rng = v.max() - v.min()
    if rng <= 0:
        return np.nan
    return float(pl / rng)

def _path_entropy_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 4:
        return np.nan
    d = np.diff(v)
    sg = np.sign(d)
    up = float((sg > 0).sum())
    dn = float((sg < 0).sum())
    zr = float((sg == 0).sum())
    tot = up + dn + zr
    if tot <= 0:
        return np.nan
    ps = [p / tot for p in [up, dn, zr] if p > 0]
    return float(-sum((p * np.log(p) for p in ps)))

def _amplitude_persistence_window(w):
    v = w[~np.isnan(w)]
    if v.size < 4:
        return np.nan
    d = np.diff(v)
    sg = np.sign(d)
    same = sg[:-1] == sg[1:]
    if same.size == 0:
        return np.nan
    return float(np.abs(d[1:][same]).sum() / (np.abs(d).sum() + 1e-12))

def _amplitude_index_window(w):
    v = w[~np.isnan(w)]
    if v.size < 2:
        return np.nan
    rng = v.max() - v.min()
    sd = v.std()
    if sd <= 0:
        return np.nan
    return float(rng / sd)

def _decay_index_window(w):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 4:
        return np.nan
    half = nn // 2
    a = np.abs(v[:half]).mean()
    b = np.abs(v[half:]).mean()
    if a <= 0:
        return np.nan
    return float((a - b) / a)

def _dtw_to_template_window(w, template):
    v = w[~np.isnan(w)]
    nn = v.size
    if nn < 8 or nn != template.size:
        return np.nan
    INF = 1e+18
    band = max(3, nn // 8)
    D = np.full((nn + 1, nn + 1), INF)
    D[0, 0] = 0.0
    for i in range(1, nn + 1):
        jlo = max(1, i - band)
        jhi = min(nn, i + band)
        for j in range(jlo, jhi + 1):
            cost = abs(v[i - 1] - template[j - 1])
            D[i, j] = cost + min(D[i - 1, j], D[i, j - 1], D[i - 1, j - 1])
    return float(D[nn, nn] / nn)

def _template_breakdown(n):
    x = np.linspace(0.0, 1.0, n)
    return -1.0 * (1.0 - np.exp(-3.0 * x))

def _template_50pct_dd(n):
    x = np.linspace(0.0, 1.0, n)
    return 0.5 * np.cos(np.pi * x) - 0.5

def _coskew(x, y, n):
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    num = ((x - mx) * (y - my) * (y - my)).rolling(n, min_periods=max(n // 3, 2)).mean()
    den = sx * sy * sy
    return _safe_div(num, den)

def _cokurt(x, y, n):
    mx = x.rolling(n, min_periods=max(n // 3, 2)).mean()
    my = y.rolling(n, min_periods=max(n // 3, 2)).mean()
    sx = x.rolling(n, min_periods=max(n // 3, 2)).std()
    sy = y.rolling(n, min_periods=max(n // 3, 2)).std()
    num = ((x - mx) * (y - my) * (y - my) * (y - my)).rolling(n, min_periods=max(n // 3, 2)).mean()
    den = sx * (sy * sy * sy)
    return _safe_div(num, den)

def _h_orthogonal_score(close):
    """Returns z-scored aggregate of orthogonal MACD-derived signals."""
    m, _, h = _macd(close)
    z_m = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    z_h = _rolling_zscore(h, YDAYS, min_periods=QDAYS)
    sl = _rolling_slope(m, MDAYS)
    z_sl = _rolling_zscore(sl, YDAYS, min_periods=QDAYS)
    return ((-z_m).fillna(0) + (-z_h).fillna(0) + (-z_sl).fillna(0)) / 3.0

def _h_basket_zscore_max(close):
    zs = []
    for f, sl_p in _BFS:
        mm = _ema(close, f) - _ema(close, sl_p)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    return pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).max(axis=1)

def _h_recall_v4_components(close, high):
    m, s, h = _macd(close)
    d = m - s
    cross = ((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    macd_neg = m < 0
    histo_neg = h < 0
    rsi_m = _rsi_wilder(m, 14)
    rsi_ob_exit = (rsi_m.shift(1) > 70) & (rsi_m <= 70)
    pct = m.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank_window, raw=True)
    extreme = pct > 0.95
    return (cross, div, macd_neg, histo_neg, rsi_ob_exit, extreme)

def _h_precision_v4_components(close, high):
    m, s, _ = _macd(close)
    d = m - s
    cross = ((d.shift(1) > 0) & (d <= 0)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    div = (p_new & (m < prior_max)).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    macd_neg = m < 0
    sl = _rolling_slope(m, MDAYS)
    sl_neg = sl < 0
    zm = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    extreme_low = zm < -1.5
    return (cross, div, macd_neg, sl_neg, extreme_low)

def f27_mcdt_451_rsi_of_macd_line_14_d1(close: pd.Series) -> pd.Series:
    """14-period RSI applied to the MACD line — momentum of momentum."""
    m, _, _ = _macd(close)
    return _rsi_wilder(m, 14).diff()

def f27_mcdt_452_rsi_of_macd_histogram_14_d1(close: pd.Series) -> pd.Series:
    """14-period RSI applied to the MACD histogram — second-derivative momentum."""
    _, _, h = _macd(close)
    return _rsi_wilder(h, 14).diff()

def f27_mcdt_453_stoch_of_macd_line_14_d1(close: pd.Series) -> pd.Series:
    """14-period Stochastic %K applied to the MACD line — position in MACD range."""
    m, _, _ = _macd(close)
    return _stoch_pct(m, 14).diff()

def f27_mcdt_454_stoch_of_macd_histogram_14_d1(close: pd.Series) -> pd.Series:
    """14-period Stochastic %K applied to the MACD histogram."""
    _, _, h = _macd(close)
    return _stoch_pct(h, 14).diff()

def f27_mcdt_455_williams_r_of_macd_line_14_d1(close: pd.Series) -> pd.Series:
    """14-period Williams %R applied to the MACD line."""
    m, _, _ = _macd(close)
    return _williams_r(m, 14).diff()

def f27_mcdt_456_trix_of_macd_line_15_d1(close: pd.Series) -> pd.Series:
    """TRIX(15) applied to MACD line — smoothed momentum-of-momentum oscillator."""
    m, _, _ = _macd(close)
    return _trix(m, 15).diff()

def f27_mcdt_457_tsi_of_macd_line_25_13_d1(close: pd.Series) -> pd.Series:
    """True Strength Index (25, 13) applied to MACD line."""
    m, _, _ = _macd(close)
    return _tsi(m, 25, 13).diff()

def f27_mcdt_458_cci_of_macd_line_20_d1(close: pd.Series) -> pd.Series:
    """20-period CCI applied to MACD line."""
    m, _, _ = _macd(close)
    return _cci_of(m, 20).diff()

def f27_mcdt_459_cmo_of_macd_line_14_d1(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (14) applied to MACD line."""
    m, _, _ = _macd(close)
    return _cmo(m, 14).diff()

def f27_mcdt_460_macd_of_ppo_12_26_d1(close: pd.Series) -> pd.Series:
    """MACD applied to PPO series — cycle-of-cycle structure."""
    p, _, _ = _ppo(close, 12, 26, 9)
    return (_ema(p, 12) - _ema(p, 26)).diff()

def f27_mcdt_461_stoch_of_ppo_14_d1(close: pd.Series) -> pd.Series:
    """14-period Stochastic %K applied to PPO."""
    p, _, _ = _ppo(close, 12, 26, 9)
    return _stoch_pct(p, 14).diff()

def f27_mcdt_462_rsi_of_macd_signal_14_d1(close: pd.Series) -> pd.Series:
    """14-period RSI applied to MACD signal line."""
    _, s, _ = _macd(close)
    return _rsi_wilder(s, 14).diff()

def f27_mcdt_463_ema_of_macd_minus_sma_of_macd_14_d1(close: pd.Series) -> pd.Series:
    """EMA14(MACD) - SMA14(MACD) — second-order signal-line divergence."""
    m, _, _ = _macd(close)
    e = _ema(m, 14)
    sm = m.rolling(14, min_periods=5).mean()
    return (e - sm).diff()

def f27_mcdt_464_fisher_transform_of_macd_10_d1(close: pd.Series) -> pd.Series:
    """Fisher transform (10) applied to normalized MACD — sharpens turning points."""
    m, _, _ = _macd(close)
    return _fisher_transform(m, 10).diff()

def f27_mcdt_465_inverse_fisher_transform_of_macd_normalized_d1(close: pd.Series) -> pd.Series:
    """Inverse Fisher transform of z-normalized MACD — bounded oscillator (-1, +1)."""
    m, _, _ = _macd(close)
    z = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    return _inverse_fisher(z).diff()

def f27_mcdt_466_macd_when_dd_5_to_10pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD over past 63d when drawdown from 252d high is between 5-10%."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = (dd >= 0.05) & (dd < 0.1)
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_467_macd_when_dd_10_to_20pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD over past 63d when drawdown is between 10-20%."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = (dd >= 0.1) & (dd < 0.2)
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_468_macd_when_dd_above_20pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD over past 63d when drawdown is >= 20%."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = dd >= 0.2
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_469_macd_change_at_first_dd_above_10pct_post_peak_d1(close: pd.Series) -> pd.Series:
    """MACD value minus its value 21d prior, at first bar where dd>=10% after most recent 252d peak."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    at_peak = close == rmax
    bs_peak = _bars_since_true(at_peak)
    first10 = (dd >= 0.1) & (dd.shift(1) < 0.1)
    valid = first10 & (bs_peak <= 252)
    chg = m - m.shift(MDAYS)
    return chg.where(valid, np.nan).ffill(limit=63).diff()

def f27_mcdt_470_macd_change_at_first_dd_above_20pct_post_peak_d1(close: pd.Series) -> pd.Series:
    """MACD value minus value 21d prior, at first bar where dd>=20% post 252d peak."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    at_peak = close == rmax
    bs_peak = _bars_since_true(at_peak)
    first20 = (dd >= 0.2) & (dd.shift(1) < 0.2)
    valid = first20 & (bs_peak <= 252)
    chg = m - m.shift(MDAYS)
    return chg.where(valid, np.nan).ffill(limit=63).diff()

def f27_mcdt_471_macd_at_first_dd_above_30pct_value_d1(close: pd.Series) -> pd.Series:
    """MACD value at first bar where dd >= 30% from 252d high; carried forward up to 126 bars."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    first30 = (dd >= 0.3) & (dd.shift(1) < 0.3)
    return m.where(first30, np.nan).ffill(limit=126).diff()

def f27_mcdt_472_ppo_at_first_dd_above_30pct_value_d1(close: pd.Series) -> pd.Series:
    """PPO value at first bar where dd >= 30% (carried forward 126 bars)."""
    p, _, _ = _ppo(close, 12, 26, 9)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    first30 = (dd >= 0.3) & (dd.shift(1) < 0.3)
    return p.where(first30, np.nan).ffill(limit=126).diff()

def f27_mcdt_473_histogram_when_dd_above_20pct_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD histogram over past 63d when drawdown >= 20%."""
    _, _, h = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = dd >= 0.2
    return h.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_474_macd_recovery_pattern_post_dd_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD over past 63d conditioned on bars in a partial recovery state
    (dd >= 10% and price > price 21d ago)."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    rec = (dd >= 0.1) & (close > close.shift(MDAYS))
    return m.where(rec, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_475_macd_hysteresis_indicator_252_d1(close: pd.Series) -> pd.Series:
    """Hysteresis: mean MACD on up-ticks minus mean MACD on down-ticks over 252d."""
    m, _, _ = _macd(close)
    up_mask = close.diff() > 0
    dn_mask = close.diff() < 0
    up_mean = m.where(up_mask, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn_mean = m.where(dn_mask, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (up_mean - dn_mean).diff()

def f27_mcdt_476_macd_path_dependence_from_peak_d1(close: pd.Series) -> pd.Series:
    """Cumulative MACD over 252d divided by 252 — path-integrated mean for stuck stocks goes negative."""
    m, _, _ = _macd(close)
    return (m.rolling(YDAYS, min_periods=QDAYS).sum() / float(YDAYS)).diff()

def f27_mcdt_477_macd_asymmetry_up_down_d1(close: pd.Series) -> pd.Series:
    """Mean of MACD when MACD>0 (252d) minus |mean MACD when MACD<0|."""
    m, _, _ = _macd(close)
    p_mean = m.where(m > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    n_mean = m.where(m < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    return (p_mean - n_mean).diff()

def f27_mcdt_478_macd_conditional_std_at_dd_above_20pct_d1(close: pd.Series) -> pd.Series:
    """Std of MACD over past 63d conditioned on dd >= 20% — variability under stress."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    cond = dd >= 0.2
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).std().diff()

def f27_mcdt_479_macd_distribution_shift_pre_post_dd_zscore_d1(close: pd.Series) -> pd.Series:
    """Z-score of (MACD avg under dd-state) minus (MACD avg under no-dd-state) normalized by total std."""
    m, _, _ = _macd(close)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    a = m.where(dd >= 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    b = m.where(dd < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    sd = m.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(a - b, sd).diff()

def f27_mcdt_480_macd_during_extreme_return_tail_avg_63_d1(close: pd.Series) -> pd.Series:
    """Avg MACD over 63d on bars where 1-day return is below 5th percentile of 252d returns."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    q5 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    cond = r < q5
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_481_macd_quantile_normal_transform_252_d1(close: pd.Series) -> pd.Series:
    """Inverse-normal CDF of empirical 252d rank of MACD — heavy-tail-robust transform."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_quantile_normal_window, raw=True).diff()

def f27_mcdt_482_macd_uniform_quantile_transform_252_d1(close: pd.Series) -> pd.Series:
    """Uniform empirical 252d quantile of MACD (0..1)."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_quantile_uniform_window, raw=True).diff()

def f27_mcdt_483_macd_robust_zscore_mad_504_d1(close: pd.Series) -> pd.Series:
    """504d robust z-score of MACD using MAD."""
    m, _, _ = _macd(close)
    return m.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_mad_zscore_window, raw=True).diff()

def f27_mcdt_484_macd_modified_zscore_iqr_252_d1(close: pd.Series) -> pd.Series:
    """252d modified z-score of MACD using IQR — quartile-based scale."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_iqr_zscore_window, raw=True).diff()

def f27_mcdt_485_multi_window_macd_rank_avg_5_21_63_d1(close: pd.Series) -> pd.Series:
    """Average percent-rank of MACD across 5/21/63 windows — multi-horizon agreement."""
    m, _, _ = _macd(close)
    r5 = m.rolling(WDAYS, min_periods=2).apply(_pct_rank_window, raw=True)
    r21 = m.rolling(MDAYS, min_periods=WDAYS).apply(_pct_rank_window, raw=True)
    r63 = m.rolling(QDAYS, min_periods=MDAYS).apply(_pct_rank_window, raw=True)
    return ((r5 + r21 + r63) / 3.0).diff()

def f27_mcdt_486_multi_window_macd_rank_std_5_21_63_d1(close: pd.Series) -> pd.Series:
    """Std of percent-ranks across 5/21/63 windows — multi-horizon disagreement."""
    m, _, _ = _macd(close)
    r5 = m.rolling(WDAYS, min_periods=2).apply(_pct_rank_window, raw=True)
    r21 = m.rolling(MDAYS, min_periods=WDAYS).apply(_pct_rank_window, raw=True)
    r63 = m.rolling(QDAYS, min_periods=MDAYS).apply(_pct_rank_window, raw=True)
    df = pd.concat([r5.rename(0), r21.rename(1), r63.rename(2)], axis=1)
    return df.std(axis=1).diff()

def f27_mcdt_487_macd_winsorized_5pct_zscore_252_d1(close: pd.Series) -> pd.Series:
    """252d z-score of MACD computed after 5/95% winsorization."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_winsorized_zscore_window, raw=True).diff()

def f27_mcdt_488_ppo_quantile_normal_252_d1(close: pd.Series) -> pd.Series:
    """Inverse-normal CDF of 252d rank of PPO."""
    p, _, _ = _ppo(close, 12, 26, 9)
    return p.rolling(YDAYS, min_periods=QDAYS).apply(_quantile_normal_window, raw=True).diff()

def f27_mcdt_489_macd_double_normalized_zscore_504_d1(close: pd.Series) -> pd.Series:
    """504d z-score of (252d z-score of MACD) — second-order standardization."""
    m, _, _ = _macd(close)
    z1 = _rolling_zscore(m, YDAYS, min_periods=QDAYS)
    return _rolling_zscore(z1, DDAYS_2Y, min_periods=YDAYS).diff()

def f27_mcdt_490_macd_rolling_quantile_band_position_252_d1(close: pd.Series) -> pd.Series:
    """Position of MACD between 10th and 90th 252d percentiles, in (0,1) bounded by 10/90 band."""
    m, _, _ = _macd(close)
    return m.rolling(YDAYS, min_periods=QDAYS).apply(_band_position_window, raw=True).diff()

def f27_mcdt_491_macd_classical_residual_after_removing_fast_63_d1(close: pd.Series) -> pd.Series:
    """63d regression residual of classical (12,26) MACD on fast (5,35) MACD."""
    m_cl, _, _ = _macd(close, 12, 26, 9)
    m_fast = _ema(close, 5) - _ema(close, 35)
    return _rolling_regression_residual(m_cl, m_fast, QDAYS).diff()

def f27_mcdt_492_macd_classical_residual_after_removing_slow_63_d1(close: pd.Series) -> pd.Series:
    """63d residual of classical MACD on slow (19,39) MACD."""
    m_cl, _, _ = _macd(close, 12, 26, 9)
    m_slow = _ema(close, 19) - _ema(close, 39)
    return _rolling_regression_residual(m_cl, m_slow, QDAYS).diff()

def f27_mcdt_493_macd_classical_residual_after_removing_long_63_d1(close: pd.Series) -> pd.Series:
    """63d residual of classical MACD on long (50,200) MACD."""
    m_cl, _, _ = _macd(close, 12, 26, 9)
    m_long = _ema(close, 50) - _ema(close, 200)
    return _rolling_regression_residual(m_cl, m_long, QDAYS).diff()

def f27_mcdt_494_multi_macd_first_pc_proxy_d1(close: pd.Series) -> pd.Series:
    """First-PC proxy: average of z-scores across basket configs."""
    zs = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    return pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).mean(axis=1).diff()

def f27_mcdt_495_multi_macd_second_pc_proxy_d1(close: pd.Series) -> pd.Series:
    """Second-PC proxy: residual of classical-z after removing first-PC proxy (63d regression)."""
    zs = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        zs.append(_rolling_zscore(mm, YDAYS, min_periods=QDAYS))
    pc1 = pd.concat([zs[i].rename(i) for i in range(len(zs))], axis=1).mean(axis=1)
    z_classical = zs[1]
    return _rolling_regression_residual(z_classical, pc1, QDAYS).diff()

def f27_mcdt_496_macd_pair_corr_fast_slow_63_d1(close: pd.Series) -> pd.Series:
    """63d rolling correlation between fast (5,35) and slow (19,39) MACDs."""
    m_fast = _ema(close, 5) - _ema(close, 35)
    m_slow = _ema(close, 19) - _ema(close, 39)
    return m_fast.rolling(QDAYS, min_periods=MDAYS).corr(m_slow).diff()

def f27_mcdt_497_macd_pair_spread_fast_slow_zscore_252_d1(close: pd.Series) -> pd.Series:
    """252d z-score of (fast MACD - slow MACD) spread."""
    m_fast = _ema(close, 5) - _ema(close, 35)
    m_slow = _ema(close, 19) - _ema(close, 39)
    return _rolling_zscore(m_fast - m_slow, YDAYS, min_periods=QDAYS).diff()

def f27_mcdt_498_macd_divergence_regression_residual_63_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """63d residual of MACD on log-high (close-normalized) — divergence as orthogonal residual."""
    m, _, _ = _macd(close)
    lh = _safe_log(high)
    return _rolling_regression_residual(m, lh, QDAYS).diff()

def f27_mcdt_499_cross_macd_beta_to_classical_63_d1(close: pd.Series) -> pd.Series:
    """63d rolling beta of fast MACD to classical MACD."""
    m_cl, _, _ = _macd(close, 12, 26, 9)
    m_fast = _ema(close, 5) - _ema(close, 35)
    return _rolling_regression_beta(m_fast, m_cl, QDAYS).diff()

def f27_mcdt_500_cross_macd_residual_variance_63_d1(close: pd.Series) -> pd.Series:
    """63d rolling variance of residual (classical MACD regressed on slow MACD) — orthogonal energy."""
    m_cl, _, _ = _macd(close, 12, 26, 9)
    m_slow = _ema(close, 19) - _ema(close, 39)
    resid = _rolling_regression_residual(m_cl, m_slow, QDAYS)
    return resid.rolling(QDAYS, min_periods=MDAYS).var().diff()

def f27_mcdt_501_dtw_distance_macd_to_50pct_dd_template_63_d1(close: pd.Series) -> pd.Series:
    """63d DTW distance from normalized MACD to a synthetic 50% drawdown template."""
    m, _, _ = _macd(close)
    tpl = _template_50pct_dd(QDAYS)

    def _fn(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        sd = v.std()
        if sd <= 0:
            return np.nan
        vz = (v - v.mean()) / sd
        if vz.size != tpl.size:
            return np.nan
        return _dtw_to_template_window(vz, tpl)
    return m.rolling(QDAYS, min_periods=QDAYS).apply(_fn, raw=True).diff()

def f27_mcdt_502_dtw_distance_macd_to_252h_breakdown_template_63_d1(close: pd.Series) -> pd.Series:
    """63d DTW distance from MACD to a synthetic post-252-high breakdown template."""
    m, _, _ = _macd(close)
    tpl = _template_breakdown(QDAYS)

    def _fn(w):
        v = w[~np.isnan(w)]
        if v.size < 8:
            return np.nan
        sd = v.std()
        if sd <= 0:
            return np.nan
        vz = (v - v.mean()) / sd
        if vz.size != tpl.size:
            return np.nan
        return _dtw_to_template_window(vz, tpl)
    return m.rolling(QDAYS, min_periods=QDAYS).apply(_fn, raw=True).diff()

def f27_mcdt_503_macd_path_length_63_d1(close: pd.Series) -> pd.Series:
    """63d sum of |MACD.diff()| — total path length."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_path_length_window, raw=True).diff()

def f27_mcdt_504_macd_path_length_zscore_252_d1(close: pd.Series) -> pd.Series:
    """252d z-score of 63d MACD path length."""
    m, _, _ = _macd(close)
    pl = m.rolling(QDAYS, min_periods=MDAYS).apply(_path_length_window, raw=True)
    return _rolling_zscore(pl, YDAYS, min_periods=QDAYS).diff()

def f27_mcdt_505_macd_path_curvature_63_d1(close: pd.Series) -> pd.Series:
    """63d sum of |MACD.diff().diff()| — total curvature (turns + reversals)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_path_curvature_window, raw=True).diff()

def f27_mcdt_506_macd_path_complexity_score_63_d1(close: pd.Series) -> pd.Series:
    """63d path length divided by 63d range — complexity per unit displacement."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_path_complexity_window, raw=True).diff()

def f27_mcdt_507_macd_path_entropy_63_d1(close: pd.Series) -> pd.Series:
    """63d Shannon entropy of MACD-diff sign sequence (up/down/flat)."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_path_entropy_window, raw=True).diff()

def f27_mcdt_508_macd_persistence_amplitude_weighted_63_d1(close: pd.Series) -> pd.Series:
    """63d fraction of total |diff| contributed by same-sign successive moves — amplitude-weighted persistence."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_amplitude_persistence_window, raw=True).diff()

def f27_mcdt_509_macd_path_amplitude_index_63_d1(close: pd.Series) -> pd.Series:
    """63d (max-min)/std of MACD path — peakedness ratio."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_amplitude_index_window, raw=True).diff()

def f27_mcdt_510_macd_path_decay_index_63_d1(close: pd.Series) -> pd.Series:
    """63d decay index: (first-half |MACD| mean - second-half |MACD| mean) / first-half mean."""
    m, _, _ = _macd(close)
    return m.rolling(QDAYS, min_periods=MDAYS).apply(_decay_index_window, raw=True).diff()

def f27_mcdt_511_coskew_macd_returns_21_d1(close: pd.Series) -> pd.Series:
    """21d coskewness of MACD with returns (E[(M-meanM)(R-meanR)^2]/stdM*stdR^2)."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    return _coskew(m, r, MDAYS).diff()

def f27_mcdt_512_cokurt_macd_returns_21_d1(close: pd.Series) -> pd.Series:
    """21d cokurtosis of MACD with returns."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    return _cokurt(m, r, MDAYS).diff()

def f27_mcdt_513_macd_in_extreme_return_tail_avg_63_d1(close: pd.Series) -> pd.Series:
    """Average MACD value over 63d when |return| > 252d 95th percentile — tail-event MACD level."""
    m, _, _ = _macd(close)
    r = close.pct_change().abs()
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    cond = r > q95
    return m.where(cond, np.nan).rolling(QDAYS, min_periods=WDAYS).mean().diff()

def f27_mcdt_514_corr_abs_returns_macd_lag1_63_d1(close: pd.Series) -> pd.Series:
    """63d correlation between |returns| and MACD lagged by 1 — vol-leverage proxy."""
    m, _, _ = _macd(close)
    r = close.pct_change().abs()
    return r.rolling(QDAYS, min_periods=MDAYS).corr(m.shift(1)).diff()

def f27_mcdt_515_coskew_at_252h_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d coskewness of MACD with returns, sampled only on 252d-high bars (carried forward 63 bars)."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    ck = _coskew(m, r, MDAYS)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ck.where(at_252h, np.nan).ffill(limit=63).diff()

def f27_mcdt_516_cokurt_at_252h_value_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """21d cokurtosis of MACD with returns sampled at 252d-high bars (ffill 63)."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    ck = _cokurt(m, r, MDAYS)
    at_252h = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return ck.where(at_252h, np.nan).ffill(limit=63).diff()

def f27_mcdt_517_asymmetric_corr_up_vs_down_63_d1(close: pd.Series) -> pd.Series:
    """63d corr(MACD, returns) on up-return bars MINUS corr on down-return bars — asymmetric coupling."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    up = r > 0
    dn = r < 0
    up_corr = m.where(up, np.nan).rolling(QDAYS, min_periods=MDAYS).corr(r.where(up, np.nan))
    dn_corr = m.where(dn, np.nan).rolling(QDAYS, min_periods=MDAYS).corr(r.where(dn, np.nan))
    return (up_corr - dn_corr).diff()

def f27_mcdt_518_macd_tail_dependence_proxy_63_d1(close: pd.Series) -> pd.Series:
    """63d count of joint bottom-decile events (MACD<q10 AND return<q10) / count of return<q10 — lower-tail dependence."""
    m, _, _ = _macd(close)
    r = close.pct_change()
    qm = m.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    qr = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    a = ((m < qm) & (r < qr)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    b = (r < qr).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b).diff()

def f27_mcdt_519_ppo_coskew_returns_21_d1(close: pd.Series) -> pd.Series:
    """21d coskewness of PPO with returns."""
    p, _, _ = _ppo(close, 12, 26, 9)
    r = close.pct_change()
    return _coskew(p, r, MDAYS).diff()

def f27_mcdt_520_cross_macd_coskew_returns_21_d1(close: pd.Series) -> pd.Series:
    """Avg across basket of 21d coskewness of each MACD config with returns."""
    r = close.pct_change()
    parts = []
    for f, sl in _BFS:
        mm = _ema(close, f) - _ema(close, sl)
        parts.append(_coskew(mm, r, MDAYS))
    return (sum(parts) / float(len(parts))).diff()

def f27_mcdt_521_batch_4_macd_orthogonal_aggregate_zscore_252_d1(close: pd.Series) -> pd.Series:
    """252d z-score of orthogonal MACD aggregate (line + histo + slope, all inverted)."""
    score = _h_orthogonal_score(close)
    return _rolling_zscore(score, YDAYS, min_periods=QDAYS).diff()

def f27_mcdt_522_macd_recall_optimized_v4_score_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Recall v4: sum of ANY-of-many topping signals incl. RSI-of-MACD overbought-exit and extreme rank."""
    cross, div, macd_neg, histo_neg, rsi_ob_exit, extreme = _h_recall_v4_components(close, high)
    return (cross.astype(float).fillna(0) + div.astype(float).fillna(0) + macd_neg.astype(float).fillna(0) + histo_neg.astype(float).fillna(0) + rsi_ob_exit.astype(float).fillna(0) + extreme.astype(float).fillna(0)).diff()

def f27_mcdt_523_macd_precision_optimized_v4_score_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Precision v4: 1 only when ALL of {bearish cross, divergence, MACD<0, slope<0, extreme-low z<-1.5}."""
    cross, div, macd_neg, sl_neg, extreme_low = _h_precision_v4_components(close, high)
    return (cross & div & macd_neg & sl_neg & extreme_low).astype(float).diff()

def f27_mcdt_524_macd_topping_master_v4_score_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Topping master v4: sum of {recall v4 sum >= 3, precision v4 == 1, basket z-max > 1.5,
    orthogonal aggregate z > 1.5}."""
    cross, div, macd_neg, histo_neg, rsi_ob_exit, extreme = _h_recall_v4_components(close, high)
    recall_sum = cross.astype(float).fillna(0) + div.astype(float).fillna(0) + macd_neg.astype(float).fillna(0) + histo_neg.astype(float).fillna(0) + rsi_ob_exit.astype(float).fillna(0) + extreme.astype(float).fillna(0)
    a = (recall_sum >= 3).astype(float)
    cr, dv, mn, sn, el = _h_precision_v4_components(close, high)
    b = (cr & dv & mn & sn & el).astype(float)
    c = (_h_basket_zscore_max(close) > 1.5).astype(float).fillna(0)
    d = (_rolling_zscore(_h_orthogonal_score(close), YDAYS, min_periods=QDAYS) > 1.5).astype(float).fillna(0)
    return (a + b + c + d).diff()

def f27_mcdt_525_absolute_terminal_macd_v4_indicator_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute terminal v4: 1 only when ALL of {precision v4, orthogonal-z > 1.5, basket-z-max > 2.0}."""
    cr, dv, mn, sn, el = _h_precision_v4_components(close, high)
    a = cr & dv & mn & sn & el
    b = _rolling_zscore(_h_orthogonal_score(close), YDAYS, min_periods=QDAYS) > 1.5
    c = _h_basket_zscore_max(close) > 2.0
    return (a & b & c).astype(float).diff()
MACD_TOPPING_DYNAMICS_D1_REGISTRY_451_525 = {'f27_mcdt_451_rsi_of_macd_line_14_d1': {'inputs': ['close'], 'func': f27_mcdt_451_rsi_of_macd_line_14_d1}, 'f27_mcdt_452_rsi_of_macd_histogram_14_d1': {'inputs': ['close'], 'func': f27_mcdt_452_rsi_of_macd_histogram_14_d1}, 'f27_mcdt_453_stoch_of_macd_line_14_d1': {'inputs': ['close'], 'func': f27_mcdt_453_stoch_of_macd_line_14_d1}, 'f27_mcdt_454_stoch_of_macd_histogram_14_d1': {'inputs': ['close'], 'func': f27_mcdt_454_stoch_of_macd_histogram_14_d1}, 'f27_mcdt_455_williams_r_of_macd_line_14_d1': {'inputs': ['close'], 'func': f27_mcdt_455_williams_r_of_macd_line_14_d1}, 'f27_mcdt_456_trix_of_macd_line_15_d1': {'inputs': ['close'], 'func': f27_mcdt_456_trix_of_macd_line_15_d1}, 'f27_mcdt_457_tsi_of_macd_line_25_13_d1': {'inputs': ['close'], 'func': f27_mcdt_457_tsi_of_macd_line_25_13_d1}, 'f27_mcdt_458_cci_of_macd_line_20_d1': {'inputs': ['close'], 'func': f27_mcdt_458_cci_of_macd_line_20_d1}, 'f27_mcdt_459_cmo_of_macd_line_14_d1': {'inputs': ['close'], 'func': f27_mcdt_459_cmo_of_macd_line_14_d1}, 'f27_mcdt_460_macd_of_ppo_12_26_d1': {'inputs': ['close'], 'func': f27_mcdt_460_macd_of_ppo_12_26_d1}, 'f27_mcdt_461_stoch_of_ppo_14_d1': {'inputs': ['close'], 'func': f27_mcdt_461_stoch_of_ppo_14_d1}, 'f27_mcdt_462_rsi_of_macd_signal_14_d1': {'inputs': ['close'], 'func': f27_mcdt_462_rsi_of_macd_signal_14_d1}, 'f27_mcdt_463_ema_of_macd_minus_sma_of_macd_14_d1': {'inputs': ['close'], 'func': f27_mcdt_463_ema_of_macd_minus_sma_of_macd_14_d1}, 'f27_mcdt_464_fisher_transform_of_macd_10_d1': {'inputs': ['close'], 'func': f27_mcdt_464_fisher_transform_of_macd_10_d1}, 'f27_mcdt_465_inverse_fisher_transform_of_macd_normalized_d1': {'inputs': ['close'], 'func': f27_mcdt_465_inverse_fisher_transform_of_macd_normalized_d1}, 'f27_mcdt_466_macd_when_dd_5_to_10pct_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_466_macd_when_dd_5_to_10pct_avg_63_d1}, 'f27_mcdt_467_macd_when_dd_10_to_20pct_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_467_macd_when_dd_10_to_20pct_avg_63_d1}, 'f27_mcdt_468_macd_when_dd_above_20pct_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_468_macd_when_dd_above_20pct_avg_63_d1}, 'f27_mcdt_469_macd_change_at_first_dd_above_10pct_post_peak_d1': {'inputs': ['close'], 'func': f27_mcdt_469_macd_change_at_first_dd_above_10pct_post_peak_d1}, 'f27_mcdt_470_macd_change_at_first_dd_above_20pct_post_peak_d1': {'inputs': ['close'], 'func': f27_mcdt_470_macd_change_at_first_dd_above_20pct_post_peak_d1}, 'f27_mcdt_471_macd_at_first_dd_above_30pct_value_d1': {'inputs': ['close'], 'func': f27_mcdt_471_macd_at_first_dd_above_30pct_value_d1}, 'f27_mcdt_472_ppo_at_first_dd_above_30pct_value_d1': {'inputs': ['close'], 'func': f27_mcdt_472_ppo_at_first_dd_above_30pct_value_d1}, 'f27_mcdt_473_histogram_when_dd_above_20pct_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_473_histogram_when_dd_above_20pct_avg_63_d1}, 'f27_mcdt_474_macd_recovery_pattern_post_dd_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_474_macd_recovery_pattern_post_dd_avg_63_d1}, 'f27_mcdt_475_macd_hysteresis_indicator_252_d1': {'inputs': ['close'], 'func': f27_mcdt_475_macd_hysteresis_indicator_252_d1}, 'f27_mcdt_476_macd_path_dependence_from_peak_d1': {'inputs': ['close'], 'func': f27_mcdt_476_macd_path_dependence_from_peak_d1}, 'f27_mcdt_477_macd_asymmetry_up_down_d1': {'inputs': ['close'], 'func': f27_mcdt_477_macd_asymmetry_up_down_d1}, 'f27_mcdt_478_macd_conditional_std_at_dd_above_20pct_d1': {'inputs': ['close'], 'func': f27_mcdt_478_macd_conditional_std_at_dd_above_20pct_d1}, 'f27_mcdt_479_macd_distribution_shift_pre_post_dd_zscore_d1': {'inputs': ['close'], 'func': f27_mcdt_479_macd_distribution_shift_pre_post_dd_zscore_d1}, 'f27_mcdt_480_macd_during_extreme_return_tail_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_480_macd_during_extreme_return_tail_avg_63_d1}, 'f27_mcdt_481_macd_quantile_normal_transform_252_d1': {'inputs': ['close'], 'func': f27_mcdt_481_macd_quantile_normal_transform_252_d1}, 'f27_mcdt_482_macd_uniform_quantile_transform_252_d1': {'inputs': ['close'], 'func': f27_mcdt_482_macd_uniform_quantile_transform_252_d1}, 'f27_mcdt_483_macd_robust_zscore_mad_504_d1': {'inputs': ['close'], 'func': f27_mcdt_483_macd_robust_zscore_mad_504_d1}, 'f27_mcdt_484_macd_modified_zscore_iqr_252_d1': {'inputs': ['close'], 'func': f27_mcdt_484_macd_modified_zscore_iqr_252_d1}, 'f27_mcdt_485_multi_window_macd_rank_avg_5_21_63_d1': {'inputs': ['close'], 'func': f27_mcdt_485_multi_window_macd_rank_avg_5_21_63_d1}, 'f27_mcdt_486_multi_window_macd_rank_std_5_21_63_d1': {'inputs': ['close'], 'func': f27_mcdt_486_multi_window_macd_rank_std_5_21_63_d1}, 'f27_mcdt_487_macd_winsorized_5pct_zscore_252_d1': {'inputs': ['close'], 'func': f27_mcdt_487_macd_winsorized_5pct_zscore_252_d1}, 'f27_mcdt_488_ppo_quantile_normal_252_d1': {'inputs': ['close'], 'func': f27_mcdt_488_ppo_quantile_normal_252_d1}, 'f27_mcdt_489_macd_double_normalized_zscore_504_d1': {'inputs': ['close'], 'func': f27_mcdt_489_macd_double_normalized_zscore_504_d1}, 'f27_mcdt_490_macd_rolling_quantile_band_position_252_d1': {'inputs': ['close'], 'func': f27_mcdt_490_macd_rolling_quantile_band_position_252_d1}, 'f27_mcdt_491_macd_classical_residual_after_removing_fast_63_d1': {'inputs': ['close'], 'func': f27_mcdt_491_macd_classical_residual_after_removing_fast_63_d1}, 'f27_mcdt_492_macd_classical_residual_after_removing_slow_63_d1': {'inputs': ['close'], 'func': f27_mcdt_492_macd_classical_residual_after_removing_slow_63_d1}, 'f27_mcdt_493_macd_classical_residual_after_removing_long_63_d1': {'inputs': ['close'], 'func': f27_mcdt_493_macd_classical_residual_after_removing_long_63_d1}, 'f27_mcdt_494_multi_macd_first_pc_proxy_d1': {'inputs': ['close'], 'func': f27_mcdt_494_multi_macd_first_pc_proxy_d1}, 'f27_mcdt_495_multi_macd_second_pc_proxy_d1': {'inputs': ['close'], 'func': f27_mcdt_495_multi_macd_second_pc_proxy_d1}, 'f27_mcdt_496_macd_pair_corr_fast_slow_63_d1': {'inputs': ['close'], 'func': f27_mcdt_496_macd_pair_corr_fast_slow_63_d1}, 'f27_mcdt_497_macd_pair_spread_fast_slow_zscore_252_d1': {'inputs': ['close'], 'func': f27_mcdt_497_macd_pair_spread_fast_slow_zscore_252_d1}, 'f27_mcdt_498_macd_divergence_regression_residual_63_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_498_macd_divergence_regression_residual_63_d1}, 'f27_mcdt_499_cross_macd_beta_to_classical_63_d1': {'inputs': ['close'], 'func': f27_mcdt_499_cross_macd_beta_to_classical_63_d1}, 'f27_mcdt_500_cross_macd_residual_variance_63_d1': {'inputs': ['close'], 'func': f27_mcdt_500_cross_macd_residual_variance_63_d1}, 'f27_mcdt_501_dtw_distance_macd_to_50pct_dd_template_63_d1': {'inputs': ['close'], 'func': f27_mcdt_501_dtw_distance_macd_to_50pct_dd_template_63_d1}, 'f27_mcdt_502_dtw_distance_macd_to_252h_breakdown_template_63_d1': {'inputs': ['close'], 'func': f27_mcdt_502_dtw_distance_macd_to_252h_breakdown_template_63_d1}, 'f27_mcdt_503_macd_path_length_63_d1': {'inputs': ['close'], 'func': f27_mcdt_503_macd_path_length_63_d1}, 'f27_mcdt_504_macd_path_length_zscore_252_d1': {'inputs': ['close'], 'func': f27_mcdt_504_macd_path_length_zscore_252_d1}, 'f27_mcdt_505_macd_path_curvature_63_d1': {'inputs': ['close'], 'func': f27_mcdt_505_macd_path_curvature_63_d1}, 'f27_mcdt_506_macd_path_complexity_score_63_d1': {'inputs': ['close'], 'func': f27_mcdt_506_macd_path_complexity_score_63_d1}, 'f27_mcdt_507_macd_path_entropy_63_d1': {'inputs': ['close'], 'func': f27_mcdt_507_macd_path_entropy_63_d1}, 'f27_mcdt_508_macd_persistence_amplitude_weighted_63_d1': {'inputs': ['close'], 'func': f27_mcdt_508_macd_persistence_amplitude_weighted_63_d1}, 'f27_mcdt_509_macd_path_amplitude_index_63_d1': {'inputs': ['close'], 'func': f27_mcdt_509_macd_path_amplitude_index_63_d1}, 'f27_mcdt_510_macd_path_decay_index_63_d1': {'inputs': ['close'], 'func': f27_mcdt_510_macd_path_decay_index_63_d1}, 'f27_mcdt_511_coskew_macd_returns_21_d1': {'inputs': ['close'], 'func': f27_mcdt_511_coskew_macd_returns_21_d1}, 'f27_mcdt_512_cokurt_macd_returns_21_d1': {'inputs': ['close'], 'func': f27_mcdt_512_cokurt_macd_returns_21_d1}, 'f27_mcdt_513_macd_in_extreme_return_tail_avg_63_d1': {'inputs': ['close'], 'func': f27_mcdt_513_macd_in_extreme_return_tail_avg_63_d1}, 'f27_mcdt_514_corr_abs_returns_macd_lag1_63_d1': {'inputs': ['close'], 'func': f27_mcdt_514_corr_abs_returns_macd_lag1_63_d1}, 'f27_mcdt_515_coskew_at_252h_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_515_coskew_at_252h_value_d1}, 'f27_mcdt_516_cokurt_at_252h_value_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_516_cokurt_at_252h_value_d1}, 'f27_mcdt_517_asymmetric_corr_up_vs_down_63_d1': {'inputs': ['close'], 'func': f27_mcdt_517_asymmetric_corr_up_vs_down_63_d1}, 'f27_mcdt_518_macd_tail_dependence_proxy_63_d1': {'inputs': ['close'], 'func': f27_mcdt_518_macd_tail_dependence_proxy_63_d1}, 'f27_mcdt_519_ppo_coskew_returns_21_d1': {'inputs': ['close'], 'func': f27_mcdt_519_ppo_coskew_returns_21_d1}, 'f27_mcdt_520_cross_macd_coskew_returns_21_d1': {'inputs': ['close'], 'func': f27_mcdt_520_cross_macd_coskew_returns_21_d1}, 'f27_mcdt_521_batch_4_macd_orthogonal_aggregate_zscore_252_d1': {'inputs': ['close'], 'func': f27_mcdt_521_batch_4_macd_orthogonal_aggregate_zscore_252_d1}, 'f27_mcdt_522_macd_recall_optimized_v4_score_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_522_macd_recall_optimized_v4_score_d1}, 'f27_mcdt_523_macd_precision_optimized_v4_score_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_523_macd_precision_optimized_v4_score_d1}, 'f27_mcdt_524_macd_topping_master_v4_score_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_524_macd_topping_master_v4_score_d1}, 'f27_mcdt_525_absolute_terminal_macd_v4_indicator_d1': {'inputs': ['high', 'close'], 'func': f27_mcdt_525_absolute_terminal_macd_v4_indicator_d1}}