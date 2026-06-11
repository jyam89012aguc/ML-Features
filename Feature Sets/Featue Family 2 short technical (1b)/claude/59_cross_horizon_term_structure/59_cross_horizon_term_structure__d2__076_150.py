"""cross_horizon_term_structure d2 076-150 - 1b-technical."""
import numpy as np
import pandas as pd

YDAYS = 252; QDAYS = 63; MDAYS = 21; WDAYS = 5
DDAYS_2Y = 504; DDAYS_3Y = 756; DDAYS_5Y = 1260


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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum(); den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _sma(s, n, mp=None):
    if mp is None: mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None: min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _bars_since_last_event(ind):
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan, dtype=float); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    a = up.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()
    b = dn.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + a / b)


def _obv(close, volume):
    return (np.sign(close.diff()).fillna(0.0) * volume).cumsum()


def _macd(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)

def _drawdown_log_n(close, n):
    mp = max(n // 3, 20)
    lc = _safe_log(close)
    def _md(w):
        v = w[~np.isnan(w)]
        if v.size < 10: return np.nan
        cm = np.maximum.accumulate(v)
        return float((v - cm).min())
    return lc.rolling(n, min_periods=mp).apply(_md, raw=True)


def _sharpe_n(close, n):
    r = _log_ret(close)
    mp = max(n // 3, 10)
    mu = r.rolling(n, min_periods=mp).mean()
    sd = r.rolling(n, min_periods=mp).std()
    return _safe_div(mu, sd)


def _sortino_n(close, n):
    r = _log_ret(close)
    mp = max(n // 3, 10)
    mu = r.rolling(n, min_periods=mp).mean()
    neg = (-r).clip(lower=0.0)
    dd = np.sqrt((neg ** 2).rolling(n, min_periods=mp).mean())
    return _safe_div(mu, dd)


def _acf_lag1_n(s, n):
    mp = max(n // 3, 10)
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20: return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0: return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return s.rolling(n, min_periods=mp).apply(_ac, raw=True)


def _amihud_n(close, volume, n):
    r = _log_ret(close).abs()
    dv = (close * volume).replace(0, np.nan)
    return _safe_div(r, dv).rolling(n, min_periods=max(n // 3, 10)).mean()


def _ts_slope(h_short, h_med, h_long):
    """Log-log slope of (metric @ h_short, h_med, h_long). Inputs are Series of metric values at each horizon."""
    df = pd.concat([h_short.rename("a"), h_med.rename("b"), h_long.rename("c")], axis=1)
    x = np.log(np.array([21.0, 63.0, 252.0]))
    xm = x.mean(); sxx = ((x - xm) ** 2).sum()
    def _sl(row):
        if np.isnan(row).any(): return np.nan
        y = np.log(np.maximum(row, 1e-12))
        ym = y.mean()
        return float(((x - xm) * (y - ym)).sum() / sxx) if sxx > 0 else np.nan
    vals = df.values
    out = np.array([_sl(vals[i]) for i in range(len(vals))], dtype=float)
    return pd.Series(out, index=df.index)


def _ts_convexity(h_short, h_med, h_long):
    """h_short - 2*h_med + h_long (curvature)."""
    return h_short - 2.0 * h_med + h_long


def _ts_inversion(h_short, h_med, h_long):
    """Sign of (h_short - h_long) - inversion indicator."""
    return np.sign(h_short - h_long)


def f59_chts_076_amihud_ts_log_slope_21_63_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-log slope of Amihud TS."""
    a1 = _amihud_n(close, volume, MDAYS); a2 = _amihud_n(close, volume, QDAYS); a3 = _amihud_n(close, volume, YDAYS)
    return (_ts_slope(a1, a2, a3)).diff().diff()

def f59_chts_077_amihud_ts_convexity_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud convexity."""
    a1 = _amihud_n(close, volume, MDAYS); a2 = _amihud_n(close, volume, QDAYS); a3 = _amihud_n(close, volume, YDAYS)
    return (_ts_convexity(a1, a2, a3)).diff().diff()

def f59_chts_078_amihud_ts_ratio_above_2_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud(21)/Amihud(252) > 2 (liquidity drying up)."""
    rt = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))
    return ((rt > 2.0).astype(float).where(rt.notna(), np.nan)).diff().diff()

def f59_chts_079_amihud_ts_at_252h_above_2_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud ratio > 2 AND close = 252d max (illiquid at top)."""
    rt = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((rt > 2.0) & (close >= rmax - 1e-12)).astype(float).where(rt.notna(), np.nan)).diff().diff()

def f59_chts_080_amihud_ts_drop_z_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z-score of (Amihud21 - Amihud252) over 252d."""
    diff = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_081_log_vol_ts_21d_mean_d2(volume: pd.Series) -> pd.Series:
    """Mean log-volume 21d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(MDAYS, min_periods=10).mean()).diff().diff()

def f59_chts_082_log_vol_ts_63d_mean_d2(volume: pd.Series) -> pd.Series:
    """Mean log-volume 63d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f59_chts_083_log_vol_ts_252d_mean_d2(volume: pd.Series) -> pd.Series:
    """Mean log-volume 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_084_log_vol_ts_short_minus_long_21_252_d2(volume: pd.Series) -> pd.Series:
    """log_vol(21)-log_vol(252) - volume regime shift."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_085_log_vol_ts_convexity_d2(volume: pd.Series) -> pd.Series:
    """Vol convexity."""
    lv = _safe_log(volume.replace(0, np.nan))
    v1 = lv.rolling(MDAYS, min_periods=10).mean(); v2 = lv.rolling(QDAYS, min_periods=MDAYS).mean(); v3 = lv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_ts_convexity(v1, v2, v3)).diff().diff()

def f59_chts_086_log_vol_ts_inversion_sign_d2(volume: pd.Series) -> pd.Series:
    """Sign(logvol21-logvol252) - volume regime direction."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (np.sign(lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff()

def f59_chts_087_log_vol_std_ts_21d_d2(volume: pd.Series) -> pd.Series:
    """Std log-volume 21d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(MDAYS, min_periods=10).std()).diff().diff()

def f59_chts_088_log_vol_std_ts_252d_d2(volume: pd.Series) -> pd.Series:
    """Std log-volume 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f59_chts_089_log_vol_std_ts_short_minus_long_21_252_d2(volume: pd.Series) -> pd.Series:
    """Vol-of-vol short minus long."""
    lv = _safe_log(volume.replace(0, np.nan))
    return (lv.rolling(MDAYS, min_periods=10).std() - lv.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f59_chts_090_log_vol_ts_drop_z_252d_d2(volume: pd.Series) -> pd.Series:
    """z-score of (logvol21 - logvol252) over 252d."""
    lv = _safe_log(volume.replace(0, np.nan))
    diff = lv.rolling(MDAYS, min_periods=10).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_091_hurst_simple_ts_63d_d2(close: pd.Series) -> pd.Series:
    """Simple R/S Hurst 63d."""
    r = _log_ret(close)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 40: return np.nan
        chunks = [c for c in [8, 16, 32] if c <= v.size // 2]
        if len(chunks) < 2: return np.nan
        rs = []
        for c in chunks:
            u = (v.size // c) * c
            sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1); ok = sd > 0
            if ok.sum() > 0:
                rs.append(float((rng[ok] / sd[ok]).mean()))
        if len(rs) < 2: return np.nan
        x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))
        return float(np.polyfit(x, y, 1)[0])
    res = r.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True)
    return (res).diff().diff()

def f59_chts_092_hurst_simple_ts_252d_d2(close: pd.Series) -> pd.Series:
    """Simple R/S Hurst 252d."""
    r = _log_ret(close)
    def _h(w):
        v = w[~np.isnan(w)]
        if v.size < 60: return np.nan
        chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]
        if len(chunks) < 3: return np.nan
        rs = []
        for c in chunks:
            u = (v.size // c) * c
            sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1); ok = sd > 0
            if ok.sum() > 0:
                rs.append(float((rng[ok] / sd[ok]).mean()))
        if len(rs) < 3: return np.nan
        x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))
        return float(np.polyfit(x, y, 1)[0])
    res = r.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)
    return (res).diff().diff()

def f59_chts_093_hurst_ts_short_minus_long_63_252_d2(close: pd.Series) -> pd.Series:
    """Hurst(63) - Hurst(252)."""
    r = _log_ret(close)
    def _hr(w, c_max):
        v = w[~np.isnan(w)]
        if v.size < 40: return np.nan
        chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]
        if len(chunks) < 2: return np.nan
        rs = []
        for c in chunks:
            u = (v.size // c) * c
            sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1); ok = sd > 0
            if ok.sum() > 0:
                rs.append(float((rng[ok] / sd[ok]).mean()))
        if len(rs) < 2: return np.nan
        x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))
        return float(np.polyfit(x, y, 1)[0])
    h63 = r.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: _hr(w, 32), raw=True)
    h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _hr(w, 64), raw=True)
    return (h63 - h252).diff().diff()

def f59_chts_094_hurst_ts_drop_below_half_indicator_d2(close: pd.Series) -> pd.Series:
    """Hurst(63) < 0.5 AND Hurst(252) > 0.5 (recent anti-persistent while long trend)."""
    r = _log_ret(close)
    def _hr(w):
        v = w[~np.isnan(w)]
        if v.size < 40: return np.nan
        chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]
        if len(chunks) < 2: return np.nan
        rs = []
        for c in chunks:
            u = (v.size // c) * c
            sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1); ok = sd > 0
            if ok.sum() > 0:
                rs.append(float((rng[ok] / sd[ok]).mean()))
        if len(rs) < 2: return np.nan
        x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))
        return float(np.polyfit(x, y, 1)[0])
    h63 = r.rolling(QDAYS, min_periods=MDAYS).apply(_hr, raw=True); h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(_hr, raw=True)
    return (((h63 < 0.5) & (h252 > 0.5)).astype(float).where(h63.notna() & h252.notna(), np.nan)).diff().diff()

def f59_chts_095_hurst_ts_at_252h_drop_indicator_d2(close: pd.Series) -> pd.Series:
    """Hurst(63)<0.5 AND H(252)>0.5 AND at 252d max."""
    r = _log_ret(close)
    def _hr(w):
        v = w[~np.isnan(w)]
        if v.size < 40: return np.nan
        chunks = [c for c in [8, 16, 32, 64] if c <= v.size // 2]
        if len(chunks) < 2: return np.nan
        rs = []
        for c in chunks:
            u = (v.size // c) * c
            sub = v[:u].reshape(-1, c); mu = sub.mean(axis=1, keepdims=True)
            cs = (sub - mu).cumsum(axis=1); rng = cs.max(axis=1) - cs.min(axis=1)
            sd = sub.std(axis=1, ddof=1); ok = sd > 0
            if ok.sum() > 0:
                rs.append(float((rng[ok] / sd[ok]).mean()))
        if len(rs) < 2: return np.nan
        x = np.log(np.array(chunks[:len(rs)], dtype=float)); y = np.log(np.array(rs, dtype=float))
        return float(np.polyfit(x, y, 1)[0])
    h63 = r.rolling(QDAYS, min_periods=MDAYS).apply(_hr, raw=True); h252 = r.rolling(YDAYS, min_periods=QDAYS).apply(_hr, raw=True)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((h63 < 0.5) & (h252 > 0.5) & (close >= rmax - 1e-12)).astype(float).where(h63.notna() & h252.notna(), np.nan)).diff().diff()

def f59_chts_096_trend_slope_log_close_ts_21d_d2(close: pd.Series) -> pd.Series:
    """Slope log-close 21d."""
    lc = _safe_log(close)
    return (_rolling_slope(lc, MDAYS)).diff().diff()

def f59_chts_097_trend_slope_log_close_ts_63d_d2(close: pd.Series) -> pd.Series:
    """Slope log-close 63d."""
    lc = _safe_log(close)
    return (_rolling_slope(lc, QDAYS)).diff().diff()

def f59_chts_098_trend_slope_log_close_ts_252d_d2(close: pd.Series) -> pd.Series:
    """Slope log-close 252d."""
    lc = _safe_log(close)
    return (_rolling_slope(lc, YDAYS)).diff().diff()

def f59_chts_099_trend_slope_short_minus_long_log_close_d2(close: pd.Series) -> pd.Series:
    """Slope(21) - Slope(252) on log-close."""
    lc = _safe_log(close)
    return (_rolling_slope(lc, MDAYS) - _rolling_slope(lc, YDAYS)).diff().diff()

def f59_chts_100_trend_slope_sign_flip_indicator_d2(close: pd.Series) -> pd.Series:
    """Sign(slope_21) != Sign(slope_252) on log-close."""
    lc = _safe_log(close)
    s1 = _rolling_slope(lc, MDAYS); s2 = _rolling_slope(lc, YDAYS)
    return ((np.sign(s1) != np.sign(s2)).astype(float).where(s1.notna() & s2.notna(), np.nan)).diff().diff()

def f59_chts_101_ts_negative_alignment_score_252d_d2(close: pd.Series) -> pd.Series:
    """Sum of: Sharpe(21)<0, Sortino(21)<0, |MaxDD21|/|MaxDD252|>1, slope21<slope252."""
    s1 = _sharpe_n(close, MDAYS); so1 = _sortino_n(close, MDAYS)
    d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); rd = _safe_div(d1, d3)
    lc = _safe_log(close); sl1 = _rolling_slope(lc, MDAYS); sl3 = _rolling_slope(lc, YDAYS)
    return (((s1 < 0).astype(float) + (so1 < 0).astype(float) + (rd > 1.0).astype(float) + (sl1 < sl3).astype(float))).diff().diff()

def f59_chts_102_ts_negative_alignment_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """TS negative-alignment score = 4 AND close = 252d max."""
    s1 = _sharpe_n(close, MDAYS); so1 = _sortino_n(close, MDAYS)
    d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); rd = _safe_div(d1, d3)
    lc = _safe_log(close); sl1 = _rolling_slope(lc, MDAYS); sl3 = _rolling_slope(lc, YDAYS)
    cnt = ((s1 < 0).astype(float) + (so1 < 0).astype(float) + (rd > 1.0).astype(float) + (sl1 < sl3).astype(float))
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((cnt >= 4) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & so1.notna(), np.nan)).diff().diff()

def f59_chts_103_ts_inversion_count_at_high_252d_d2(close: pd.Series) -> pd.Series:
    """Count of bars in 252d with (vol-TS inverted) AND (close=252d max)."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ev = ((v21 > v252) & (close >= rmax - 1e-12)).astype(float).where(v252.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f59_chts_104_ts_skew_kurt_alignment_bearish_indicator_d2(close: pd.Series) -> pd.Series:
    """Skew(21)<-0.5 AND Kurt(21)>5 AND Sharpe(21)<0 - bearish distributional triple."""
    r = _log_ret(close)
    sk = r.rolling(MDAYS, min_periods=10).skew(); kt = r.rolling(MDAYS, min_periods=10).kurt(); sh = _sharpe_n(close, MDAYS)
    return (((sk < -0.5) & (kt > 5.0) & (sh < 0)).astype(float).where(sk.notna() & kt.notna() & sh.notna(), np.nan)).diff().diff()

def f59_chts_105_ts_multi_horizon_drawdown_ratio_increase_indicator_d2(close: pd.Series) -> pd.Series:
    """MaxDD21/MaxDD63 AND MaxDD63/MaxDD252 both > 1 (DD accelerating across horizons)."""
    d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)
    return (((_safe_div(d1, d2) > 1.0) & (_safe_div(d2, d3) > 1.0)).astype(float).where(d3.notna(), np.nan)).diff().diff()

def f59_chts_106_ts_liquidity_volatility_inverse_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud(21)/Amihud(252) > 1.5 AND Vol(21)/Vol(252) > 1.5 - liquidity collapse + vol expansion."""
    ar = _safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))
    r = _log_ret(close); vr = _safe_div(r.rolling(MDAYS, min_periods=10).std(), r.rolling(YDAYS, min_periods=QDAYS).std())
    return (((ar > 1.5) & (vr > 1.5)).astype(float).where(ar.notna() & vr.notna(), np.nan)).diff().diff()

def f59_chts_107_ts_average_z_score_5_metrics_252d_d2(close: pd.Series) -> pd.Series:
    """Mean of z-scores of TS slopes for: vol, sharpe, sortino, skew, kurt over 252d."""
    r = _log_ret(close)
    v1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()
    vs = _ts_slope(v1, v2, v3)
    zv = _rolling_zscore(vs, YDAYS)
    ss = _sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS); zs = _rolling_zscore(ss, YDAYS)
    so = _sortino_n(close, MDAYS) - _sortino_n(close, YDAYS); zo = _rolling_zscore(so, YDAYS)
    sk = r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(); zk = _rolling_zscore(sk, YDAYS)
    kt = r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt(); zt = _rolling_zscore(kt, YDAYS)
    return ((zv.fillna(0) + zs.fillna(0) + zo.fillna(0) + zk.fillna(0) + zt.fillna(0)) / 5.0).diff().diff()

def f59_chts_108_ts_term_structure_shape_change_speed_21d_d2(close: pd.Series) -> pd.Series:
    """21-bar change in vol-TS log-slope."""
    r = _log_ret(close)
    v1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()
    sl = _ts_slope(v1, v2, v3)
    return (sl - sl.shift(MDAYS)).diff().diff()

def f59_chts_109_ts_vol_amihud_combined_z_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(vol-TS-short minus long) + z(amihud-TS-short minus long)."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std()
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)
    return (_rolling_zscore(vd, YDAYS).fillna(0) + _rolling_zscore(ad, YDAYS).fillna(0)).diff().diff()

def f59_chts_110_ts_inversion_persistence_63d_d2(close: pd.Series) -> pd.Series:
    """Fraction of last 63d with (V21 > V252) inversion."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return ((v21 > v252).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f59_chts_111_rsi_ts_21d_d2(close: pd.Series) -> pd.Series:
    """RSI14 mean over 21d."""
    rsi = _rsi(close, 14)
    return (rsi.rolling(MDAYS, min_periods=10).mean()).diff().diff()

def f59_chts_112_rsi_ts_63d_d2(close: pd.Series) -> pd.Series:
    """RSI14 mean over 63d."""
    rsi = _rsi(close, 14)
    return (rsi.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f59_chts_113_rsi_ts_252d_d2(close: pd.Series) -> pd.Series:
    """RSI14 mean over 252d."""
    rsi = _rsi(close, 14)
    return (rsi.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_114_rsi_ts_short_minus_long_drop_d2(close: pd.Series) -> pd.Series:
    """RSI(21) - RSI(252)."""
    rsi = _rsi(close, 14)
    return (rsi.rolling(MDAYS, min_periods=10).mean() - rsi.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_115_rsi_ts_above_70_short_below_70_long_indicator_d2(close: pd.Series) -> pd.Series:
    """RSI21>70 AND RSI252<70 (recent OB on top of cool long-term)."""
    rsi = _rsi(close, 14)
    ra = rsi.rolling(MDAYS, min_periods=10).mean(); rl = rsi.rolling(YDAYS, min_periods=QDAYS).mean()
    return (((ra > 70.0) & (rl < 70.0)).astype(float).where(ra.notna() & rl.notna(), np.nan)).diff().diff()

def f59_chts_116_macd_ts_21d_d2(close: pd.Series) -> pd.Series:
    """MACD-line mean 21d."""
    m = _macd(close)
    return (m.rolling(MDAYS, min_periods=10).mean()).diff().diff()

def f59_chts_117_macd_ts_252d_d2(close: pd.Series) -> pd.Series:
    """MACD-line mean 252d."""
    m = _macd(close)
    return (m.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_118_macd_ts_short_minus_long_d2(close: pd.Series) -> pd.Series:
    """MACD(21d-mean) - MACD(252d-mean)."""
    m = _macd(close)
    return (m.rolling(MDAYS, min_periods=10).mean() - m.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_119_obv_pct_change_ts_21d_minus_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV-21d-pct-change - OBV-252d-pct-change."""
    o = _obv(close, volume)
    return (o.pct_change(MDAYS) - o.pct_change(YDAYS)).diff().diff()

def f59_chts_120_range_norm_ts_21d_minus_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (H-L)/close 21d - mean 252d."""
    rn = _safe_div(high - low, close)
    return (rn.rolling(MDAYS, min_periods=10).mean() - rn.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f59_chts_121_vol_AND_amihud_AND_skew_TS_all_inverted_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol inversion AND Amihud inversion AND Skew inversion all bearish."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    a21 = _amihud_n(close, volume, MDAYS); a252 = _amihud_n(close, volume, YDAYS)
    sk21 = r.rolling(MDAYS, min_periods=10).skew(); sk252 = r.rolling(YDAYS, min_periods=QDAYS).skew()
    return (((v21 > v252) & (a21 > a252) & (sk21 < sk252)).astype(float).where(v252.notna() & a252.notna() & sk252.notna(), np.nan)).diff().diff()

def f59_chts_122_ts_inversion_count_3of5_at_252h_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """>=3 of 5 TS inversions (vol, amihud, sharpe-drop, sortino-drop, skew-drop) AND close=252d max."""
    r = _log_ret(close)
    i_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)
    i_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)
    i_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)
    i_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)
    i_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)
    cnt = i_v + i_a + i_s + i_so + i_sk
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((cnt >= 3) & (close >= rmax - 1e-12)).astype(float)).diff().diff()

def f59_chts_123_ts_inversion_count_4of5_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """>=4 of 5 TS inversions simultaneously."""
    r = _log_ret(close)
    i_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)
    i_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)
    i_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)
    i_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)
    i_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)
    return (((i_v + i_a + i_s + i_so + i_sk) >= 4).astype(float).where(i_v.notna() & i_a.notna(), np.nan)).diff().diff()

def f59_chts_124_ts_inversion_count_all_5_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """All 5 TS inversions simultaneously (extreme regime alignment)."""
    r = _log_ret(close)
    i_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)
    i_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)
    i_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)
    i_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)
    i_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)
    return (((i_v + i_a + i_s + i_so + i_sk) >= 5).astype(float).where(i_v.notna() & i_a.notna(), np.nan)).diff().diff()

def f59_chts_125_ts_inversion_persistence_3of5_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d with >=3 of 5 TS inversions."""
    r = _log_ret(close)
    i_v = (r.rolling(MDAYS, min_periods=10).std() > r.rolling(YDAYS, min_periods=QDAYS).std()).astype(float)
    i_a = (_amihud_n(close, volume, MDAYS) > _amihud_n(close, volume, YDAYS)).astype(float)
    i_s = (_sharpe_n(close, MDAYS) < _sharpe_n(close, YDAYS)).astype(float)
    i_so = (_sortino_n(close, MDAYS) < _sortino_n(close, YDAYS)).astype(float)
    i_sk = (r.rolling(MDAYS, min_periods=10).skew() < r.rolling(YDAYS, min_periods=QDAYS).skew()).astype(float)
    cnt = i_v + i_a + i_s + i_so + i_sk
    ind = (cnt >= 3).astype(float).where(i_v.notna() & i_a.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f59_chts_126_ts_4y_drawdown_ratio_252_vs_504_d2(close: pd.Series) -> pd.Series:
    """MaxDD(252) / MaxDD(504) - recent drawdown depth vs 2yr baseline."""
    return (_safe_div(_drawdown_log_n(close, YDAYS), _drawdown_log_n(close, DDAYS_2Y))).diff().diff()

def f59_chts_127_ts_vol_at_high_relative_to_vol_at_low_252d_d2(close: pd.Series) -> pd.Series:
    """Mean vol when close in top decile / mean vol when close in bottom decile over 252d."""
    r = _log_ret(close); v = r.rolling(MDAYS, min_periods=10).std()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin)
    vh = v.where(pr > 0.9, np.nan); vl = v.where(pr < 0.1, np.nan)
    mh = vh.rolling(YDAYS, min_periods=QDAYS).mean(); ml = vl.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(mh, ml)).diff().diff()

def f59_chts_128_ts_sharpe_decay_rate_252d_d2(close: pd.Series) -> pd.Series:
    """(Sharpe(252) - Sharpe(63)) / 63 - per-bar decay rate of Sharpe with horizon."""
    s3 = _sharpe_n(close, YDAYS); s2 = _sharpe_n(close, QDAYS)
    return ((s3 - s2) / float(QDAYS)).diff().diff()

def f59_chts_129_ts_drawdown_acceleration_index_252d_d2(close: pd.Series) -> pd.Series:
    """(MaxDD21/MaxDD252) / (MaxDD63/MaxDD252) - acceleration ratio."""
    d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)
    r1 = _safe_div(d1, d3); r2 = _safe_div(d2, d3)
    return (_safe_div(r1, r2)).diff().diff()

def f59_chts_130_ts_distress_signal_composite_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-sum of: vol-TS-shift + amihud-TS-shift + sharpe-degradation + skew-drop + DD-accel."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    skd = -(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()); zk = _rolling_zscore(skd, YDAYS)
    d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); dr = _safe_div(d1, d3); zd = _rolling_zscore(dr, YDAYS)
    return (zv.fillna(0) + za.fillna(0) + zs.fillna(0) + zk.fillna(0) + zd.fillna(0)).diff().diff()

def f59_chts_131_ts_distress_composite_above_p90_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TS distress composite > 252d-p90 indicator."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0)
    p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((z > p90).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f59_chts_132_ts_distress_composite_at_252h_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TS distress composite > 252d-p90 AND close = 252d max."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0)
    p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f59_chts_133_ts_distress_persistence_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d with TS distress > 252d-mean."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0); mu = z.rolling(YDAYS, min_periods=QDAYS).mean()
    ind = (z > mu).astype(float).where(mu.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f59_chts_134_ts_distress_acceleration_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-bar change in TS distress composite."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0)
    return (z - z.shift(MDAYS)).diff().diff()

def f59_chts_135_ts_distress_max_in_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max TS distress in last 63d."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0)
    return (z.rolling(QDAYS, min_periods=MDAYS).max()).diff().diff()

def f59_chts_136_ts_distress_bars_since_above_p90_capped_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since TS distress was last >252d-p90 (capped 252)."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ev = (z > p90).astype(float).where(p90.notna(), np.nan)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff().diff()

def f59_chts_137_ts_distress_count_above_p90_in_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in 252d with TS distress > 252d-p90."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ev = (z > p90).astype(float).where(p90.notna(), np.nan)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f59_chts_138_ts_distress_count_at_high_in_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in 252d where TS distress > 252d-p90 AND close=252d max."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0); p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ev = ((z > p90) & (close >= rmax - 1e-12)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f59_chts_139_ts_distress_minus_long_term_mean_504d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TS distress composite minus 504d-mean of itself."""
    r = _log_ret(close)
    vd = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(); zv = _rolling_zscore(vd, YDAYS)
    ad = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS); za = _rolling_zscore(ad, YDAYS)
    sd = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)); zs = _rolling_zscore(sd, YDAYS)
    z = zv.fillna(0) + za.fillna(0) + zs.fillna(0); mu = z.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return (z - mu).diff().diff()

def f59_chts_140_ts_inversion_intensity_composite_z_score_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z-sum of TS-inversion counts: vol, amihud, sharpe (each as 21d minus 252d)."""
    r = _log_ret(close)
    i1 = r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std()
    i2 = _amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)
    i3 = -(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS))
    return (_rolling_zscore(i1, YDAYS).fillna(0) + _rolling_zscore(i2, YDAYS).fillna(0) + _rolling_zscore(i3, YDAYS).fillna(0)).diff().diff()

def f59_chts_141_master_term_structure_inversion_score_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """z-sum of TS-inversion magnitudes across vol/amihud/sharpe/sortino/skew over 252d."""
    r = _log_ret(close)
    z1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)
    z2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)
    z3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)
    z4 = -_rolling_zscore(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS), YDAYS)
    z5 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0)).diff().diff()

def f59_chts_142_master_ts_inversion_at_252h_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master TS-inversion score > 252d-p90 AND close=252d max."""
    r = _log_ret(close)
    z = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)
    + _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0)
    - _rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS).fillna(0))
    p90 = z.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f59_chts_143_ts_compound_blowoff_risk_score_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mayer*MasterTSInversion - extension * regime-fragility composite."""
    mayer = _safe_div(close, _sma(close, 200))
    r = _log_ret(close)
    z = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)
    + _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0))
    return (mayer * z).diff().diff()

def f59_chts_144_ts_compound_blowoff_at_252h_above_p90_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Compound blowoff risk > 252d-p90 AND close = 252d max."""
    mayer = _safe_div(close, _sma(close, 200))
    r = _log_ret(close)
    z = (_rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS).fillna(0)
    + _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS).fillna(0))
    comp = mayer * z
    p90 = comp.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((comp > p90) & (close >= rmax - 1e-12)).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f59_chts_145_ts_5horizon_vol_dispersion_252d_d2(close: pd.Series) -> pd.Series:
    """Std of vol across horizons {5,21,63,126,252} - vol disagreement across horizons."""
    r = _log_ret(close)
    v5 = r.rolling(5, min_periods=3).std(); v21 = r.rolling(MDAYS, min_periods=10).std(); v63 = r.rolling(QDAYS, min_periods=MDAYS).std(); v126 = r.rolling(126, min_periods=QDAYS).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    df = pd.concat([v5.rename('a'), v21.rename('b'), v63.rename('c'), v126.rename('d'), v252.rename('e')], axis=1)
    return (df.std(axis=1)).diff().diff()

def f59_chts_146_ts_5horizon_vol_max_minus_min_252d_d2(close: pd.Series) -> pd.Series:
    """Range of vol across 5 horizons."""
    r = _log_ret(close)
    v5 = r.rolling(5, min_periods=3).std(); v21 = r.rolling(MDAYS, min_periods=10).std(); v63 = r.rolling(QDAYS, min_periods=MDAYS).std(); v126 = r.rolling(126, min_periods=QDAYS).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    df = pd.concat([v5.rename('a'), v21.rename('b'), v63.rename('c'), v126.rename('d'), v252.rename('e')], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()

def f59_chts_147_ts_5horizon_close_position_range_d2(close: pd.Series) -> pd.Series:
    """Range of (close/SMA_n - 1) across n in {20, 50, 100, 200} - extension dispersion."""
    e1 = _safe_div(close, _sma(close, 20)) - 1.0; e2 = _safe_div(close, _sma(close, 50)) - 1.0; e3 = _safe_div(close, _sma(close, 100)) - 1.0; e4 = _safe_div(close, _sma(close, 200)) - 1.0
    df = pd.concat([e1.rename('a'), e2.rename('b'), e3.rename('c'), e4.rename('d')], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff()

def f59_chts_148_ts_blowoff_imminence_composite_score_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined: Mayer * (vol-TS-shift z + amihud-TS-shift z) * (close/252d-max)."""
    mayer = _safe_div(close, _sma(close, 200))
    r = _log_ret(close)
    z1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)
    z2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); ratio = _safe_div(close, rmax)
    return (mayer * (z1.fillna(0) + z2.fillna(0)) * ratio).diff().diff()

def f59_chts_149_ts_extreme_alignment_4metrics_at_252h_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-TS shift, Amihud shift, Sharpe drop, Skew drop all simultaneously in top-quartile AND close=252d max."""
    r = _log_ret(close)
    z1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)
    z2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)
    z3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)
    z4 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z1 > 0.674) & (z2 > 0.674) & (z3 > 0.674) & (z4 > 0.674) & (close >= rmax - 1e-12)).astype(float).where(z1.notna() & z2.notna() & z3.notna() & z4.notna(), np.nan)).diff().diff()

def f59_chts_150_master_ts_term_structure_signature_score_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-sum of 7 TS shifts: vol, amihud, sharpe, sortino, skew, kurt, slope - master TS regime score."""
    r = _log_ret(close)
    z1 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).std() - r.rolling(YDAYS, min_periods=QDAYS).std(), YDAYS)
    z2 = _rolling_zscore(_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS), YDAYS)
    z3 = -_rolling_zscore(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS), YDAYS)
    z4 = -_rolling_zscore(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS), YDAYS)
    z5 = -_rolling_zscore(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew(), YDAYS)
    z6 = _rolling_zscore(r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt(), YDAYS)
    lc = _safe_log(close); z7 = -_rolling_zscore(_rolling_slope(lc, MDAYS) - _rolling_slope(lc, YDAYS), YDAYS)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) + z5.fillna(0) + z6.fillna(0) + z7.fillna(0)).diff().diff()


CROSS_HORIZON_TERM_STRUCTURE_D2_REGISTRY_076_150 = {
    "f59_chts_076_amihud_ts_log_slope_21_63_252_d2": {"inputs": ["close", "volume"], "func": f59_chts_076_amihud_ts_log_slope_21_63_252_d2},
    "f59_chts_077_amihud_ts_convexity_d2": {"inputs": ["close", "volume"], "func": f59_chts_077_amihud_ts_convexity_d2},
    "f59_chts_078_amihud_ts_ratio_above_2_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_078_amihud_ts_ratio_above_2_indicator_d2},
    "f59_chts_079_amihud_ts_at_252h_above_2_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_079_amihud_ts_at_252h_above_2_indicator_d2},
    "f59_chts_080_amihud_ts_drop_z_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_080_amihud_ts_drop_z_252d_d2},
    "f59_chts_081_log_vol_ts_21d_mean_d2": {"inputs": ["volume"], "func": f59_chts_081_log_vol_ts_21d_mean_d2},
    "f59_chts_082_log_vol_ts_63d_mean_d2": {"inputs": ["volume"], "func": f59_chts_082_log_vol_ts_63d_mean_d2},
    "f59_chts_083_log_vol_ts_252d_mean_d2": {"inputs": ["volume"], "func": f59_chts_083_log_vol_ts_252d_mean_d2},
    "f59_chts_084_log_vol_ts_short_minus_long_21_252_d2": {"inputs": ["volume"], "func": f59_chts_084_log_vol_ts_short_minus_long_21_252_d2},
    "f59_chts_085_log_vol_ts_convexity_d2": {"inputs": ["volume"], "func": f59_chts_085_log_vol_ts_convexity_d2},
    "f59_chts_086_log_vol_ts_inversion_sign_d2": {"inputs": ["volume"], "func": f59_chts_086_log_vol_ts_inversion_sign_d2},
    "f59_chts_087_log_vol_std_ts_21d_d2": {"inputs": ["volume"], "func": f59_chts_087_log_vol_std_ts_21d_d2},
    "f59_chts_088_log_vol_std_ts_252d_d2": {"inputs": ["volume"], "func": f59_chts_088_log_vol_std_ts_252d_d2},
    "f59_chts_089_log_vol_std_ts_short_minus_long_21_252_d2": {"inputs": ["volume"], "func": f59_chts_089_log_vol_std_ts_short_minus_long_21_252_d2},
    "f59_chts_090_log_vol_ts_drop_z_252d_d2": {"inputs": ["volume"], "func": f59_chts_090_log_vol_ts_drop_z_252d_d2},
    "f59_chts_091_hurst_simple_ts_63d_d2": {"inputs": ["close"], "func": f59_chts_091_hurst_simple_ts_63d_d2},
    "f59_chts_092_hurst_simple_ts_252d_d2": {"inputs": ["close"], "func": f59_chts_092_hurst_simple_ts_252d_d2},
    "f59_chts_093_hurst_ts_short_minus_long_63_252_d2": {"inputs": ["close"], "func": f59_chts_093_hurst_ts_short_minus_long_63_252_d2},
    "f59_chts_094_hurst_ts_drop_below_half_indicator_d2": {"inputs": ["close"], "func": f59_chts_094_hurst_ts_drop_below_half_indicator_d2},
    "f59_chts_095_hurst_ts_at_252h_drop_indicator_d2": {"inputs": ["close"], "func": f59_chts_095_hurst_ts_at_252h_drop_indicator_d2},
    "f59_chts_096_trend_slope_log_close_ts_21d_d2": {"inputs": ["close"], "func": f59_chts_096_trend_slope_log_close_ts_21d_d2},
    "f59_chts_097_trend_slope_log_close_ts_63d_d2": {"inputs": ["close"], "func": f59_chts_097_trend_slope_log_close_ts_63d_d2},
    "f59_chts_098_trend_slope_log_close_ts_252d_d2": {"inputs": ["close"], "func": f59_chts_098_trend_slope_log_close_ts_252d_d2},
    "f59_chts_099_trend_slope_short_minus_long_log_close_d2": {"inputs": ["close"], "func": f59_chts_099_trend_slope_short_minus_long_log_close_d2},
    "f59_chts_100_trend_slope_sign_flip_indicator_d2": {"inputs": ["close"], "func": f59_chts_100_trend_slope_sign_flip_indicator_d2},
    "f59_chts_101_ts_negative_alignment_score_252d_d2": {"inputs": ["close"], "func": f59_chts_101_ts_negative_alignment_score_252d_d2},
    "f59_chts_102_ts_negative_alignment_at_252h_indicator_d2": {"inputs": ["close"], "func": f59_chts_102_ts_negative_alignment_at_252h_indicator_d2},
    "f59_chts_103_ts_inversion_count_at_high_252d_d2": {"inputs": ["close"], "func": f59_chts_103_ts_inversion_count_at_high_252d_d2},
    "f59_chts_104_ts_skew_kurt_alignment_bearish_indicator_d2": {"inputs": ["close"], "func": f59_chts_104_ts_skew_kurt_alignment_bearish_indicator_d2},
    "f59_chts_105_ts_multi_horizon_drawdown_ratio_increase_indicator_d2": {"inputs": ["close"], "func": f59_chts_105_ts_multi_horizon_drawdown_ratio_increase_indicator_d2},
    "f59_chts_106_ts_liquidity_volatility_inverse_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_106_ts_liquidity_volatility_inverse_indicator_d2},
    "f59_chts_107_ts_average_z_score_5_metrics_252d_d2": {"inputs": ["close"], "func": f59_chts_107_ts_average_z_score_5_metrics_252d_d2},
    "f59_chts_108_ts_term_structure_shape_change_speed_21d_d2": {"inputs": ["close"], "func": f59_chts_108_ts_term_structure_shape_change_speed_21d_d2},
    "f59_chts_109_ts_vol_amihud_combined_z_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_109_ts_vol_amihud_combined_z_252d_d2},
    "f59_chts_110_ts_inversion_persistence_63d_d2": {"inputs": ["close"], "func": f59_chts_110_ts_inversion_persistence_63d_d2},
    "f59_chts_111_rsi_ts_21d_d2": {"inputs": ["close"], "func": f59_chts_111_rsi_ts_21d_d2},
    "f59_chts_112_rsi_ts_63d_d2": {"inputs": ["close"], "func": f59_chts_112_rsi_ts_63d_d2},
    "f59_chts_113_rsi_ts_252d_d2": {"inputs": ["close"], "func": f59_chts_113_rsi_ts_252d_d2},
    "f59_chts_114_rsi_ts_short_minus_long_drop_d2": {"inputs": ["close"], "func": f59_chts_114_rsi_ts_short_minus_long_drop_d2},
    "f59_chts_115_rsi_ts_above_70_short_below_70_long_indicator_d2": {"inputs": ["close"], "func": f59_chts_115_rsi_ts_above_70_short_below_70_long_indicator_d2},
    "f59_chts_116_macd_ts_21d_d2": {"inputs": ["close"], "func": f59_chts_116_macd_ts_21d_d2},
    "f59_chts_117_macd_ts_252d_d2": {"inputs": ["close"], "func": f59_chts_117_macd_ts_252d_d2},
    "f59_chts_118_macd_ts_short_minus_long_d2": {"inputs": ["close"], "func": f59_chts_118_macd_ts_short_minus_long_d2},
    "f59_chts_119_obv_pct_change_ts_21d_minus_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_119_obv_pct_change_ts_21d_minus_252d_d2},
    "f59_chts_120_range_norm_ts_21d_minus_252d_d2": {"inputs": ["high", "low", "close"], "func": f59_chts_120_range_norm_ts_21d_minus_252d_d2},
    "f59_chts_121_vol_AND_amihud_AND_skew_TS_all_inverted_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_121_vol_AND_amihud_AND_skew_TS_all_inverted_indicator_d2},
    "f59_chts_122_ts_inversion_count_3of5_at_252h_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_122_ts_inversion_count_3of5_at_252h_indicator_d2},
    "f59_chts_123_ts_inversion_count_4of5_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_123_ts_inversion_count_4of5_indicator_d2},
    "f59_chts_124_ts_inversion_count_all_5_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_124_ts_inversion_count_all_5_indicator_d2},
    "f59_chts_125_ts_inversion_persistence_3of5_63d_d2": {"inputs": ["close", "volume"], "func": f59_chts_125_ts_inversion_persistence_3of5_63d_d2},
    "f59_chts_126_ts_4y_drawdown_ratio_252_vs_504_d2": {"inputs": ["close"], "func": f59_chts_126_ts_4y_drawdown_ratio_252_vs_504_d2},
    "f59_chts_127_ts_vol_at_high_relative_to_vol_at_low_252d_d2": {"inputs": ["close"], "func": f59_chts_127_ts_vol_at_high_relative_to_vol_at_low_252d_d2},
    "f59_chts_128_ts_sharpe_decay_rate_252d_d2": {"inputs": ["close"], "func": f59_chts_128_ts_sharpe_decay_rate_252d_d2},
    "f59_chts_129_ts_drawdown_acceleration_index_252d_d2": {"inputs": ["close"], "func": f59_chts_129_ts_drawdown_acceleration_index_252d_d2},
    "f59_chts_130_ts_distress_signal_composite_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_130_ts_distress_signal_composite_252d_d2},
    "f59_chts_131_ts_distress_composite_above_p90_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_131_ts_distress_composite_above_p90_indicator_d2},
    "f59_chts_132_ts_distress_composite_at_252h_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_132_ts_distress_composite_at_252h_indicator_d2},
    "f59_chts_133_ts_distress_persistence_63d_d2": {"inputs": ["close", "volume"], "func": f59_chts_133_ts_distress_persistence_63d_d2},
    "f59_chts_134_ts_distress_acceleration_21d_d2": {"inputs": ["close", "volume"], "func": f59_chts_134_ts_distress_acceleration_21d_d2},
    "f59_chts_135_ts_distress_max_in_63d_d2": {"inputs": ["close", "volume"], "func": f59_chts_135_ts_distress_max_in_63d_d2},
    "f59_chts_136_ts_distress_bars_since_above_p90_capped_d2": {"inputs": ["close", "volume"], "func": f59_chts_136_ts_distress_bars_since_above_p90_capped_d2},
    "f59_chts_137_ts_distress_count_above_p90_in_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_137_ts_distress_count_above_p90_in_252d_d2},
    "f59_chts_138_ts_distress_count_at_high_in_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_138_ts_distress_count_at_high_in_252d_d2},
    "f59_chts_139_ts_distress_minus_long_term_mean_504d_d2": {"inputs": ["close", "volume"], "func": f59_chts_139_ts_distress_minus_long_term_mean_504d_d2},
    "f59_chts_140_ts_inversion_intensity_composite_z_score_d2": {"inputs": ["close", "volume"], "func": f59_chts_140_ts_inversion_intensity_composite_z_score_d2},
    "f59_chts_141_master_term_structure_inversion_score_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_141_master_term_structure_inversion_score_252d_d2},
    "f59_chts_142_master_ts_inversion_at_252h_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_142_master_ts_inversion_at_252h_indicator_d2},
    "f59_chts_143_ts_compound_blowoff_risk_score_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_143_ts_compound_blowoff_risk_score_252d_d2},
    "f59_chts_144_ts_compound_blowoff_at_252h_above_p90_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_144_ts_compound_blowoff_at_252h_above_p90_indicator_d2},
    "f59_chts_145_ts_5horizon_vol_dispersion_252d_d2": {"inputs": ["close"], "func": f59_chts_145_ts_5horizon_vol_dispersion_252d_d2},
    "f59_chts_146_ts_5horizon_vol_max_minus_min_252d_d2": {"inputs": ["close"], "func": f59_chts_146_ts_5horizon_vol_max_minus_min_252d_d2},
    "f59_chts_147_ts_5horizon_close_position_range_d2": {"inputs": ["close"], "func": f59_chts_147_ts_5horizon_close_position_range_d2},
    "f59_chts_148_ts_blowoff_imminence_composite_score_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_148_ts_blowoff_imminence_composite_score_252d_d2},
    "f59_chts_149_ts_extreme_alignment_4metrics_at_252h_indicator_d2": {"inputs": ["close", "volume"], "func": f59_chts_149_ts_extreme_alignment_4metrics_at_252h_indicator_d2},
    "f59_chts_150_master_ts_term_structure_signature_score_252d_d2": {"inputs": ["close", "volume"], "func": f59_chts_150_master_ts_term_structure_signature_score_252d_d2},
}
