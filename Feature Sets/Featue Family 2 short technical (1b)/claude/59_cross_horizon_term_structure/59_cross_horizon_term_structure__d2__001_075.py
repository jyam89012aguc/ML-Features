"""cross_horizon_term_structure d2 001-075 - 1b-technical."""
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


def f59_chts_001_vol_ts_21d_value_d2(close: pd.Series) -> pd.Series:
    """Realized vol 21d."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=10).std()).diff().diff()

def f59_chts_002_vol_ts_63d_value_d2(close: pd.Series) -> pd.Series:
    """Realized vol 63d."""
    r = _log_ret(close)
    return (r.rolling(QDAYS, min_periods=MDAYS).std()).diff().diff()

def f59_chts_003_vol_ts_252d_value_d2(close: pd.Series) -> pd.Series:
    """Realized vol 252d."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f59_chts_004_vol_ts_short_minus_long_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Vol(21d) - Vol(252d) - level-shift indicator."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (v21 - v252).diff().diff()

def f59_chts_005_vol_ts_ratio_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Vol(21d) / Vol(252d)."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(v21, v252)).diff().diff()

def f59_chts_006_vol_ts_log_slope_21_63_252_d2(close: pd.Series) -> pd.Series:
    """Log-log slope of vol term-structure."""
    r = _log_ret(close)
    v1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_ts_slope(v1, v2, v3)).diff().diff()

def f59_chts_007_vol_ts_convexity_21_63_252_d2(close: pd.Series) -> pd.Series:
    """Convexity: V21 - 2*V63 + V252."""
    r = _log_ret(close)
    v1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_ts_convexity(v1, v2, v3)).diff().diff()

def f59_chts_008_vol_ts_inversion_sign_indicator_d2(close: pd.Series) -> pd.Series:
    """Sign(V21 - V252) - +1 = inverted (short>long vol)."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (np.sign(v21 - v252)).diff().diff()

def f59_chts_009_vol_ts_inversion_indicator_at_high_d2(close: pd.Series) -> pd.Series:
    """Vol inversion (V21>V252) AND close = 252d max."""
    r = _log_ret(close)
    v21 = r.rolling(MDAYS, min_periods=10).std(); v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((v21 > v252) & (close >= rmax - 1e-12)).astype(float).where(v252.notna(), np.nan)).diff().diff()

def f59_chts_010_vol_ts_slope_z_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of vol-TS log-log slope over 252d."""
    r = _log_ret(close)
    v1 = r.rolling(MDAYS, min_periods=10).std(); v2 = r.rolling(QDAYS, min_periods=MDAYS).std(); v3 = r.rolling(YDAYS, min_periods=QDAYS).std()
    sl = _ts_slope(v1, v2, v3)
    return (_rolling_zscore(sl, YDAYS)).diff().diff()

def f59_chts_011_sharpe_ts_21d_value_d2(close: pd.Series) -> pd.Series:
    """Daily Sharpe 21d."""
    return (_sharpe_n(close, MDAYS)).diff().diff()

def f59_chts_012_sharpe_ts_63d_value_d2(close: pd.Series) -> pd.Series:
    """Daily Sharpe 63d."""
    return (_sharpe_n(close, QDAYS)).diff().diff()

def f59_chts_013_sharpe_ts_252d_value_d2(close: pd.Series) -> pd.Series:
    """Daily Sharpe 252d."""
    return (_sharpe_n(close, YDAYS)).diff().diff()

def f59_chts_014_sharpe_ts_short_minus_long_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Sharpe(21) - Sharpe(252)."""
    return (_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)).diff().diff()

def f59_chts_015_sharpe_ts_ratio_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Sharpe(21) / Sharpe(252)."""
    return (_safe_div(_sharpe_n(close, MDAYS), _sharpe_n(close, YDAYS))).diff().diff()

def f59_chts_016_sharpe_ts_convexity_21_63_252_d2(close: pd.Series) -> pd.Series:
    """Sharpe convexity S(21)-2*S(63)+S(252)."""
    s1 = _sharpe_n(close, MDAYS); s2 = _sharpe_n(close, QDAYS); s3 = _sharpe_n(close, YDAYS)
    return (_ts_convexity(s1, s2, s3)).diff().diff()

def f59_chts_017_sharpe_ts_inversion_sign_d2(close: pd.Series) -> pd.Series:
    """Sign(Sharpe21 - Sharpe252)."""
    return (np.sign(_sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS))).diff().diff()

def f59_chts_018_sharpe_ts_degradation_indicator_d2(close: pd.Series) -> pd.Series:
    """Sharpe(21) < 0 AND Sharpe(252) > 0 (short-term degradation while long is positive)."""
    s1 = _sharpe_n(close, MDAYS); s3 = _sharpe_n(close, YDAYS)
    return (((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_019_sharpe_ts_degradation_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """Sharpe degradation AND close = 252d max."""
    s1 = _sharpe_n(close, MDAYS); s3 = _sharpe_n(close, YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_020_sharpe_ts_short_drop_z_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of (Sharpe(21) - Sharpe(252)) over 252d."""
    diff = _sharpe_n(close, MDAYS) - _sharpe_n(close, YDAYS)
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_021_sortino_ts_21d_value_d2(close: pd.Series) -> pd.Series:
    """Sortino 21d."""
    return (_sortino_n(close, MDAYS)).diff().diff()

def f59_chts_022_sortino_ts_63d_value_d2(close: pd.Series) -> pd.Series:
    """Sortino 63d."""
    return (_sortino_n(close, QDAYS)).diff().diff()

def f59_chts_023_sortino_ts_252d_value_d2(close: pd.Series) -> pd.Series:
    """Sortino 252d."""
    return (_sortino_n(close, YDAYS)).diff().diff()

def f59_chts_024_sortino_ts_short_minus_long_d2(close: pd.Series) -> pd.Series:
    """Sortino(21) - Sortino(252)."""
    return (_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS)).diff().diff()

def f59_chts_025_sortino_ts_ratio_21_252_d2(close: pd.Series) -> pd.Series:
    """Sortino(21) / Sortino(252)."""
    return (_safe_div(_sortino_n(close, MDAYS), _sortino_n(close, YDAYS))).diff().diff()

def f59_chts_026_sortino_ts_convexity_21_63_252_d2(close: pd.Series) -> pd.Series:
    """Sortino convexity."""
    s1 = _sortino_n(close, MDAYS); s2 = _sortino_n(close, QDAYS); s3 = _sortino_n(close, YDAYS)
    return (_ts_convexity(s1, s2, s3)).diff().diff()

def f59_chts_027_sortino_ts_inversion_sign_d2(close: pd.Series) -> pd.Series:
    """Sign(Sortino21 - Sortino252)."""
    return (np.sign(_sortino_n(close, MDAYS) - _sortino_n(close, YDAYS))).diff().diff()

def f59_chts_028_sortino_ts_degradation_indicator_d2(close: pd.Series) -> pd.Series:
    """Sortino(21) < 0 AND Sortino(252) > 0."""
    s1 = _sortino_n(close, MDAYS); s3 = _sortino_n(close, YDAYS)
    return (((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_029_sortino_ts_degradation_at_252h_d2(close: pd.Series) -> pd.Series:
    """Sortino degradation AND at 252d max."""
    s1 = _sortino_n(close, MDAYS); s3 = _sortino_n(close, YDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_030_sortino_ts_drop_z_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of Sortino(21)-Sortino(252) over 252d."""
    diff = _sortino_n(close, MDAYS) - _sortino_n(close, YDAYS)
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_031_max_dd_21d_value_d2(close: pd.Series) -> pd.Series:
    """Max DD 21d (negative log value)."""
    return (_drawdown_log_n(close, MDAYS)).diff().diff()

def f59_chts_032_max_dd_63d_value_d2(close: pd.Series) -> pd.Series:
    """Max DD 63d."""
    return (_drawdown_log_n(close, QDAYS)).diff().diff()

def f59_chts_033_max_dd_252d_value_d2(close: pd.Series) -> pd.Series:
    """Max DD 252d."""
    return (_drawdown_log_n(close, YDAYS)).diff().diff()

def f59_chts_034_max_dd_504d_value_d2(close: pd.Series) -> pd.Series:
    """Max DD 504d."""
    return (_drawdown_log_n(close, DDAYS_2Y)).diff().diff()

def f59_chts_035_max_dd_ts_ratio_21_252_d2(close: pd.Series) -> pd.Series:
    """|MaxDD21| / |MaxDD252|."""
    d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS)
    return (_safe_div(d1, d3)).diff().diff()

def f59_chts_036_max_dd_ts_ratio_63_252_d2(close: pd.Series) -> pd.Series:
    """|MaxDD63| / |MaxDD252|."""
    d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)
    return (_safe_div(d2, d3)).diff().diff()

def f59_chts_037_max_dd_ts_short_minus_long_252_504_d2(close: pd.Series) -> pd.Series:
    """|MaxDD252| - |MaxDD504| - recent DD severity vs long-term."""
    d3 = -_drawdown_log_n(close, YDAYS); d4 = -_drawdown_log_n(close, DDAYS_2Y)
    return (d3 - d4).diff().diff()

def f59_chts_038_max_dd_ts_convexity_21_63_252_d2(close: pd.Series) -> pd.Series:
    """MaxDD convexity (DD21 - 2*DD63 + DD252) - on magnitude."""
    d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS); d3 = -_drawdown_log_n(close, YDAYS)
    return (_ts_convexity(d1, d2, d3)).diff().diff()

def f59_chts_039_max_dd_acceleration_21d_252d_d2(close: pd.Series) -> pd.Series:
    """(|MaxDD21| - |MaxDD63|) - acceleration of drawdown."""
    d1 = -_drawdown_log_n(close, MDAYS); d2 = -_drawdown_log_n(close, QDAYS)
    return (d1 - d2).diff().diff()

def f59_chts_040_max_dd_ratio_above_1_5_indicator_d2(close: pd.Series) -> pd.Series:
    """|MaxDD21| / |MaxDD252| > 1.5 (recent DD bigger than long-term - acute stress)."""
    d1 = -_drawdown_log_n(close, MDAYS); d3 = -_drawdown_log_n(close, YDAYS); r = _safe_div(d1, d3)
    return ((r > 1.5).astype(float).where(r.notna(), np.nan)).diff().diff()

def f59_chts_041_skew_ts_21d_value_d2(close: pd.Series) -> pd.Series:
    """Skew of log-returns 21d."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=10).skew()).diff().diff()

def f59_chts_042_skew_ts_63d_value_d2(close: pd.Series) -> pd.Series:
    """Skew 63d."""
    r = _log_ret(close)
    return (r.rolling(QDAYS, min_periods=MDAYS).skew()).diff().diff()

def f59_chts_043_skew_ts_252d_value_d2(close: pd.Series) -> pd.Series:
    """Skew 252d."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=QDAYS).skew()).diff().diff()

def f59_chts_044_skew_ts_short_minus_long_d2(close: pd.Series) -> pd.Series:
    """Skew(21) - Skew(252)."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()).diff().diff()

def f59_chts_045_skew_ts_convexity_21_63_252_d2(close: pd.Series) -> pd.Series:
    """Skew convexity S(21) - 2*S(63) + S(252)."""
    r = _log_ret(close)
    s1 = r.rolling(MDAYS, min_periods=10).skew(); s2 = r.rolling(QDAYS, min_periods=MDAYS).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()
    return (_ts_convexity(s1, s2, s3)).diff().diff()

def f59_chts_046_skew_ts_inversion_sign_d2(close: pd.Series) -> pd.Series:
    """Sign(Skew21 - Skew252) - skew regime alignment."""
    r = _log_ret(close)
    return (np.sign(r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew())).diff().diff()

def f59_chts_047_skew_ts_sign_flip_indicator_d2(close: pd.Series) -> pd.Series:
    """Skew(21)<0 AND Skew(252)>0 (recent negative skew while long-term positive)."""
    r = _log_ret(close)
    s1 = r.rolling(MDAYS, min_periods=10).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()
    return (((s1 < 0) & (s3 > 0)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_048_skew_ts_sign_flip_at_252h_indicator_d2(close: pd.Series) -> pd.Series:
    """Skew sign-flip AND close = 252d max."""
    r = _log_ret(close)
    s1 = r.rolling(MDAYS, min_periods=10).skew(); s3 = r.rolling(YDAYS, min_periods=QDAYS).skew()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((s1 < 0) & (s3 > 0) & (close >= rmax - 1e-12)).astype(float).where(s1.notna() & s3.notna(), np.nan)).diff().diff()

def f59_chts_049_skew_ts_log_slope_d2(close: pd.Series) -> pd.Series:
    """Log-log slope of |skew| TS."""
    r = _log_ret(close)
    s1 = r.rolling(MDAYS, min_periods=10).skew().abs() + 1e-6
    s2 = r.rolling(QDAYS, min_periods=MDAYS).skew().abs() + 1e-6
    s3 = r.rolling(YDAYS, min_periods=QDAYS).skew().abs() + 1e-6
    return (_ts_slope(s1, s2, s3)).diff().diff()

def f59_chts_050_skew_ts_drop_z_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of (Skew21 - Skew252) over 252d."""
    r = _log_ret(close)
    diff = r.rolling(MDAYS, min_periods=10).skew() - r.rolling(YDAYS, min_periods=QDAYS).skew()
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_051_kurt_ts_21d_value_d2(close: pd.Series) -> pd.Series:
    """Excess kurt 21d."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=10).kurt()).diff().diff()

def f59_chts_052_kurt_ts_63d_value_d2(close: pd.Series) -> pd.Series:
    """Excess kurt 63d."""
    r = _log_ret(close)
    return (r.rolling(QDAYS, min_periods=MDAYS).kurt()).diff().diff()

def f59_chts_053_kurt_ts_252d_value_d2(close: pd.Series) -> pd.Series:
    """Excess kurt 252d."""
    r = _log_ret(close)
    return (r.rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff()

def f59_chts_054_kurt_ts_short_minus_long_d2(close: pd.Series) -> pd.Series:
    """Kurt(21) - Kurt(252)."""
    r = _log_ret(close)
    return (r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff()

def f59_chts_055_kurt_ts_ratio_21_252_d2(close: pd.Series) -> pd.Series:
    """Kurt(21) / Kurt(252)."""
    r = _log_ret(close)
    return (_safe_div(r.rolling(MDAYS, min_periods=10).kurt(), r.rolling(YDAYS, min_periods=QDAYS).kurt())).diff().diff()

def f59_chts_056_kurt_ts_convexity_d2(close: pd.Series) -> pd.Series:
    """Kurt convexity."""
    r = _log_ret(close)
    k1 = r.rolling(MDAYS, min_periods=10).kurt(); k2 = r.rolling(QDAYS, min_periods=MDAYS).kurt(); k3 = r.rolling(YDAYS, min_periods=QDAYS).kurt()
    return (_ts_convexity(k1, k2, k3)).diff().diff()

def f59_chts_057_kurt_ts_above_5_at_short_d2(close: pd.Series) -> pd.Series:
    """Kurt(21) > 5 indicator (recent fat tails)."""
    r = _log_ret(close)
    k = r.rolling(MDAYS, min_periods=10).kurt()
    return ((k > 5.0).astype(float).where(k.notna(), np.nan)).diff().diff()

def f59_chts_058_kurt_ts_above_5_at_short_AND_at_252h_d2(close: pd.Series) -> pd.Series:
    """Recent kurt>5 AND close = 252d max (heavy tails forming at top)."""
    r = _log_ret(close)
    k = r.rolling(MDAYS, min_periods=10).kurt()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((k > 5.0) & (close >= rmax - 1e-12)).astype(float).where(k.notna(), np.nan)).diff().diff()

def f59_chts_059_kurt_ts_log_slope_d2(close: pd.Series) -> pd.Series:
    """Log-log slope of |kurt|+1 TS."""
    r = _log_ret(close)
    k1 = (r.rolling(MDAYS, min_periods=10).kurt().abs() + 1.0); k2 = (r.rolling(QDAYS, min_periods=MDAYS).kurt().abs() + 1.0); k3 = (r.rolling(YDAYS, min_periods=QDAYS).kurt().abs() + 1.0)
    return (_ts_slope(k1, k2, k3)).diff().diff()

def f59_chts_060_kurt_ts_drop_z_252d_d2(close: pd.Series) -> pd.Series:
    """z-score of (Kurt21 - Kurt252) over 252d."""
    r = _log_ret(close)
    diff = r.rolling(MDAYS, min_periods=10).kurt() - r.rolling(YDAYS, min_periods=QDAYS).kurt()
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_061_acf_lag1_ts_21d_value_log_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of log-returns 21d."""
    r = _log_ret(close)
    return (_acf_lag1_n(r, MDAYS)).diff().diff()

def f59_chts_062_acf_lag1_ts_63d_value_log_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of log-returns 63d."""
    r = _log_ret(close)
    return (_acf_lag1_n(r, QDAYS)).diff().diff()

def f59_chts_063_acf_lag1_ts_252d_value_log_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of log-returns 252d."""
    r = _log_ret(close)
    return (_acf_lag1_n(r, YDAYS)).diff().diff()

def f59_chts_064_acf_lag1_ts_short_minus_long_log_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(21) - ACF(252)."""
    r = _log_ret(close)
    return (_acf_lag1_n(r, MDAYS) - _acf_lag1_n(r, YDAYS)).diff().diff()

def f59_chts_065_acf_lag1_ts_convexity_log_ret_d2(close: pd.Series) -> pd.Series:
    """ACF convexity (a21 - 2*a63 + a252) over log-returns."""
    r = _log_ret(close)
    a1 = _acf_lag1_n(r, MDAYS); a2 = _acf_lag1_n(r, QDAYS); a3 = _acf_lag1_n(r, YDAYS)
    return (_ts_convexity(a1, a2, a3)).diff().diff()

def f59_chts_066_acf_lag1_ts_21d_abs_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of |r| 21d (vol clustering)."""
    x = _log_ret(close).abs()
    return (_acf_lag1_n(x, MDAYS)).diff().diff()

def f59_chts_067_acf_lag1_ts_63d_abs_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of |r| 63d."""
    x = _log_ret(close).abs()
    return (_acf_lag1_n(x, QDAYS)).diff().diff()

def f59_chts_068_acf_lag1_ts_252d_abs_ret_d2(close: pd.Series) -> pd.Series:
    """ACF(1) of |r| 252d."""
    x = _log_ret(close).abs()
    return (_acf_lag1_n(x, YDAYS)).diff().diff()

def f59_chts_069_acf_lag1_ts_short_minus_long_abs_ret_d2(close: pd.Series) -> pd.Series:
    """ACF21(|r|) - ACF252(|r|)."""
    x = _log_ret(close).abs()
    return (_acf_lag1_n(x, MDAYS) - _acf_lag1_n(x, YDAYS)).diff().diff()

def f59_chts_070_acf_lag1_ts_drop_z_252d_log_ret_d2(close: pd.Series) -> pd.Series:
    """z-score of (ACF21 - ACF252) over 252d."""
    r = _log_ret(close)
    diff = _acf_lag1_n(r, MDAYS) - _acf_lag1_n(r, YDAYS)
    return (_rolling_zscore(diff, YDAYS)).diff().diff()

def f59_chts_071_amihud_ts_21d_value_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity 21d."""
    return (_amihud_n(close, volume, MDAYS)).diff().diff()

def f59_chts_072_amihud_ts_63d_value_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity 63d."""
    return (_amihud_n(close, volume, QDAYS)).diff().diff()

def f59_chts_073_amihud_ts_252d_value_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity 252d."""
    return (_amihud_n(close, volume, YDAYS)).diff().diff()

def f59_chts_074_amihud_ts_short_minus_long_21_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud(21) - Amihud(252)."""
    return (_amihud_n(close, volume, MDAYS) - _amihud_n(close, volume, YDAYS)).diff().diff()

def f59_chts_075_amihud_ts_ratio_21_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud(21) / Amihud(252) - liquidity-regime shift."""
    return (_safe_div(_amihud_n(close, volume, MDAYS), _amihud_n(close, volume, YDAYS))).diff().diff()


CROSS_HORIZON_TERM_STRUCTURE_D2_REGISTRY_001_075 = {
    "f59_chts_001_vol_ts_21d_value_d2": {"inputs": ["close"], "func": f59_chts_001_vol_ts_21d_value_d2},
    "f59_chts_002_vol_ts_63d_value_d2": {"inputs": ["close"], "func": f59_chts_002_vol_ts_63d_value_d2},
    "f59_chts_003_vol_ts_252d_value_d2": {"inputs": ["close"], "func": f59_chts_003_vol_ts_252d_value_d2},
    "f59_chts_004_vol_ts_short_minus_long_21d_252d_d2": {"inputs": ["close"], "func": f59_chts_004_vol_ts_short_minus_long_21d_252d_d2},
    "f59_chts_005_vol_ts_ratio_21d_252d_d2": {"inputs": ["close"], "func": f59_chts_005_vol_ts_ratio_21d_252d_d2},
    "f59_chts_006_vol_ts_log_slope_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_006_vol_ts_log_slope_21_63_252_d2},
    "f59_chts_007_vol_ts_convexity_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_007_vol_ts_convexity_21_63_252_d2},
    "f59_chts_008_vol_ts_inversion_sign_indicator_d2": {"inputs": ["close"], "func": f59_chts_008_vol_ts_inversion_sign_indicator_d2},
    "f59_chts_009_vol_ts_inversion_indicator_at_high_d2": {"inputs": ["close"], "func": f59_chts_009_vol_ts_inversion_indicator_at_high_d2},
    "f59_chts_010_vol_ts_slope_z_252d_d2": {"inputs": ["close"], "func": f59_chts_010_vol_ts_slope_z_252d_d2},
    "f59_chts_011_sharpe_ts_21d_value_d2": {"inputs": ["close"], "func": f59_chts_011_sharpe_ts_21d_value_d2},
    "f59_chts_012_sharpe_ts_63d_value_d2": {"inputs": ["close"], "func": f59_chts_012_sharpe_ts_63d_value_d2},
    "f59_chts_013_sharpe_ts_252d_value_d2": {"inputs": ["close"], "func": f59_chts_013_sharpe_ts_252d_value_d2},
    "f59_chts_014_sharpe_ts_short_minus_long_21d_252d_d2": {"inputs": ["close"], "func": f59_chts_014_sharpe_ts_short_minus_long_21d_252d_d2},
    "f59_chts_015_sharpe_ts_ratio_21d_252d_d2": {"inputs": ["close"], "func": f59_chts_015_sharpe_ts_ratio_21d_252d_d2},
    "f59_chts_016_sharpe_ts_convexity_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_016_sharpe_ts_convexity_21_63_252_d2},
    "f59_chts_017_sharpe_ts_inversion_sign_d2": {"inputs": ["close"], "func": f59_chts_017_sharpe_ts_inversion_sign_d2},
    "f59_chts_018_sharpe_ts_degradation_indicator_d2": {"inputs": ["close"], "func": f59_chts_018_sharpe_ts_degradation_indicator_d2},
    "f59_chts_019_sharpe_ts_degradation_at_252h_indicator_d2": {"inputs": ["close"], "func": f59_chts_019_sharpe_ts_degradation_at_252h_indicator_d2},
    "f59_chts_020_sharpe_ts_short_drop_z_252d_d2": {"inputs": ["close"], "func": f59_chts_020_sharpe_ts_short_drop_z_252d_d2},
    "f59_chts_021_sortino_ts_21d_value_d2": {"inputs": ["close"], "func": f59_chts_021_sortino_ts_21d_value_d2},
    "f59_chts_022_sortino_ts_63d_value_d2": {"inputs": ["close"], "func": f59_chts_022_sortino_ts_63d_value_d2},
    "f59_chts_023_sortino_ts_252d_value_d2": {"inputs": ["close"], "func": f59_chts_023_sortino_ts_252d_value_d2},
    "f59_chts_024_sortino_ts_short_minus_long_d2": {"inputs": ["close"], "func": f59_chts_024_sortino_ts_short_minus_long_d2},
    "f59_chts_025_sortino_ts_ratio_21_252_d2": {"inputs": ["close"], "func": f59_chts_025_sortino_ts_ratio_21_252_d2},
    "f59_chts_026_sortino_ts_convexity_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_026_sortino_ts_convexity_21_63_252_d2},
    "f59_chts_027_sortino_ts_inversion_sign_d2": {"inputs": ["close"], "func": f59_chts_027_sortino_ts_inversion_sign_d2},
    "f59_chts_028_sortino_ts_degradation_indicator_d2": {"inputs": ["close"], "func": f59_chts_028_sortino_ts_degradation_indicator_d2},
    "f59_chts_029_sortino_ts_degradation_at_252h_d2": {"inputs": ["close"], "func": f59_chts_029_sortino_ts_degradation_at_252h_d2},
    "f59_chts_030_sortino_ts_drop_z_252d_d2": {"inputs": ["close"], "func": f59_chts_030_sortino_ts_drop_z_252d_d2},
    "f59_chts_031_max_dd_21d_value_d2": {"inputs": ["close"], "func": f59_chts_031_max_dd_21d_value_d2},
    "f59_chts_032_max_dd_63d_value_d2": {"inputs": ["close"], "func": f59_chts_032_max_dd_63d_value_d2},
    "f59_chts_033_max_dd_252d_value_d2": {"inputs": ["close"], "func": f59_chts_033_max_dd_252d_value_d2},
    "f59_chts_034_max_dd_504d_value_d2": {"inputs": ["close"], "func": f59_chts_034_max_dd_504d_value_d2},
    "f59_chts_035_max_dd_ts_ratio_21_252_d2": {"inputs": ["close"], "func": f59_chts_035_max_dd_ts_ratio_21_252_d2},
    "f59_chts_036_max_dd_ts_ratio_63_252_d2": {"inputs": ["close"], "func": f59_chts_036_max_dd_ts_ratio_63_252_d2},
    "f59_chts_037_max_dd_ts_short_minus_long_252_504_d2": {"inputs": ["close"], "func": f59_chts_037_max_dd_ts_short_minus_long_252_504_d2},
    "f59_chts_038_max_dd_ts_convexity_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_038_max_dd_ts_convexity_21_63_252_d2},
    "f59_chts_039_max_dd_acceleration_21d_252d_d2": {"inputs": ["close"], "func": f59_chts_039_max_dd_acceleration_21d_252d_d2},
    "f59_chts_040_max_dd_ratio_above_1_5_indicator_d2": {"inputs": ["close"], "func": f59_chts_040_max_dd_ratio_above_1_5_indicator_d2},
    "f59_chts_041_skew_ts_21d_value_d2": {"inputs": ["close"], "func": f59_chts_041_skew_ts_21d_value_d2},
    "f59_chts_042_skew_ts_63d_value_d2": {"inputs": ["close"], "func": f59_chts_042_skew_ts_63d_value_d2},
    "f59_chts_043_skew_ts_252d_value_d2": {"inputs": ["close"], "func": f59_chts_043_skew_ts_252d_value_d2},
    "f59_chts_044_skew_ts_short_minus_long_d2": {"inputs": ["close"], "func": f59_chts_044_skew_ts_short_minus_long_d2},
    "f59_chts_045_skew_ts_convexity_21_63_252_d2": {"inputs": ["close"], "func": f59_chts_045_skew_ts_convexity_21_63_252_d2},
    "f59_chts_046_skew_ts_inversion_sign_d2": {"inputs": ["close"], "func": f59_chts_046_skew_ts_inversion_sign_d2},
    "f59_chts_047_skew_ts_sign_flip_indicator_d2": {"inputs": ["close"], "func": f59_chts_047_skew_ts_sign_flip_indicator_d2},
    "f59_chts_048_skew_ts_sign_flip_at_252h_indicator_d2": {"inputs": ["close"], "func": f59_chts_048_skew_ts_sign_flip_at_252h_indicator_d2},
    "f59_chts_049_skew_ts_log_slope_d2": {"inputs": ["close"], "func": f59_chts_049_skew_ts_log_slope_d2},
    "f59_chts_050_skew_ts_drop_z_252d_d2": {"inputs": ["close"], "func": f59_chts_050_skew_ts_drop_z_252d_d2},
    "f59_chts_051_kurt_ts_21d_value_d2": {"inputs": ["close"], "func": f59_chts_051_kurt_ts_21d_value_d2},
    "f59_chts_052_kurt_ts_63d_value_d2": {"inputs": ["close"], "func": f59_chts_052_kurt_ts_63d_value_d2},
    "f59_chts_053_kurt_ts_252d_value_d2": {"inputs": ["close"], "func": f59_chts_053_kurt_ts_252d_value_d2},
    "f59_chts_054_kurt_ts_short_minus_long_d2": {"inputs": ["close"], "func": f59_chts_054_kurt_ts_short_minus_long_d2},
    "f59_chts_055_kurt_ts_ratio_21_252_d2": {"inputs": ["close"], "func": f59_chts_055_kurt_ts_ratio_21_252_d2},
    "f59_chts_056_kurt_ts_convexity_d2": {"inputs": ["close"], "func": f59_chts_056_kurt_ts_convexity_d2},
    "f59_chts_057_kurt_ts_above_5_at_short_d2": {"inputs": ["close"], "func": f59_chts_057_kurt_ts_above_5_at_short_d2},
    "f59_chts_058_kurt_ts_above_5_at_short_AND_at_252h_d2": {"inputs": ["close"], "func": f59_chts_058_kurt_ts_above_5_at_short_AND_at_252h_d2},
    "f59_chts_059_kurt_ts_log_slope_d2": {"inputs": ["close"], "func": f59_chts_059_kurt_ts_log_slope_d2},
    "f59_chts_060_kurt_ts_drop_z_252d_d2": {"inputs": ["close"], "func": f59_chts_060_kurt_ts_drop_z_252d_d2},
    "f59_chts_061_acf_lag1_ts_21d_value_log_ret_d2": {"inputs": ["close"], "func": f59_chts_061_acf_lag1_ts_21d_value_log_ret_d2},
    "f59_chts_062_acf_lag1_ts_63d_value_log_ret_d2": {"inputs": ["close"], "func": f59_chts_062_acf_lag1_ts_63d_value_log_ret_d2},
    "f59_chts_063_acf_lag1_ts_252d_value_log_ret_d2": {"inputs": ["close"], "func": f59_chts_063_acf_lag1_ts_252d_value_log_ret_d2},
    "f59_chts_064_acf_lag1_ts_short_minus_long_log_ret_d2": {"inputs": ["close"], "func": f59_chts_064_acf_lag1_ts_short_minus_long_log_ret_d2},
    "f59_chts_065_acf_lag1_ts_convexity_log_ret_d2": {"inputs": ["close"], "func": f59_chts_065_acf_lag1_ts_convexity_log_ret_d2},
    "f59_chts_066_acf_lag1_ts_21d_abs_ret_d2": {"inputs": ["close"], "func": f59_chts_066_acf_lag1_ts_21d_abs_ret_d2},
    "f59_chts_067_acf_lag1_ts_63d_abs_ret_d2": {"inputs": ["close"], "func": f59_chts_067_acf_lag1_ts_63d_abs_ret_d2},
    "f59_chts_068_acf_lag1_ts_252d_abs_ret_d2": {"inputs": ["close"], "func": f59_chts_068_acf_lag1_ts_252d_abs_ret_d2},
    "f59_chts_069_acf_lag1_ts_short_minus_long_abs_ret_d2": {"inputs": ["close"], "func": f59_chts_069_acf_lag1_ts_short_minus_long_abs_ret_d2},
    "f59_chts_070_acf_lag1_ts_drop_z_252d_log_ret_d2": {"inputs": ["close"], "func": f59_chts_070_acf_lag1_ts_drop_z_252d_log_ret_d2},
    "f59_chts_071_amihud_ts_21d_value_d2": {"inputs": ["close", "volume"], "func": f59_chts_071_amihud_ts_21d_value_d2},
    "f59_chts_072_amihud_ts_63d_value_d2": {"inputs": ["close", "volume"], "func": f59_chts_072_amihud_ts_63d_value_d2},
    "f59_chts_073_amihud_ts_252d_value_d2": {"inputs": ["close", "volume"], "func": f59_chts_073_amihud_ts_252d_value_d2},
    "f59_chts_074_amihud_ts_short_minus_long_21_252_d2": {"inputs": ["close", "volume"], "func": f59_chts_074_amihud_ts_short_minus_long_21_252_d2},
    "f59_chts_075_amihud_ts_ratio_21_252_d2": {"inputs": ["close", "volume"], "func": f59_chts_075_amihud_ts_ratio_21_252_d2},
}
