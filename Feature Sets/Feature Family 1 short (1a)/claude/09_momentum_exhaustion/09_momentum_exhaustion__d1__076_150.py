"""momentum_exhaustion d1 features 076_150 — short blowup pipeline 1a-inverse.

Momentum exhaustion signatures at multi-year peaks: oscillator overextension, divergence, thrust decay, and acceleration loss.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _rsi_wilder(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    ru = _wilder_rma(up, n)
    rd = _wilder_rma(dn, n)
    rs = ru / rd.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _rsi_cutler(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    ru = up.rolling(n, min_periods=max(n // 3, 2)).mean()
    rd = dn.rolling(n, min_periods=max(n // 3, 2)).mean()
    rs = ru / rd.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def _stoch_k(close, high, low, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)


def _stoch_d(close, high, low, n=14, d=3):
    k = _stoch_k(close, high, low, n)
    return k.rolling(d, min_periods=1).mean()


def _macd(close, fast=12, slow=26, signal=9):
    line = _ema(close, fast) - _ema(close, slow)
    sig = _ema(line, signal)
    hist = line - sig
    return line, sig, hist


def _trix(close, n):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return e3.pct_change() * 1000.0


def _tsi(close, r=25, s=13):
    m = close.diff()
    em1 = _ema(m, r); em2 = _ema(em1, s)
    am1 = _ema(m.abs(), r); am2 = _ema(am1, s)
    return 100.0 * _safe_div(em2, am2)


def _dmi(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    up = high.diff()
    dn = -low.diff()
    plus_dm = ((up > dn) & (up > 0)).astype(float) * up
    minus_dm = ((dn > up) & (dn > 0)).astype(float) * dn
    atr = _wilder_rma(tr, n)
    plus_di = 100.0 * _wilder_rma(plus_dm, n) / atr.replace(0, np.nan)
    minus_di = 100.0 * _wilder_rma(minus_dm, n) / atr.replace(0, np.nan)
    dx = 100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx = _wilder_rma(dx, n)
    return plus_di, minus_di, adx


def _aroon(high, low, n=25):
    def _idx_max(w):
        return (len(w) - 1) - int(np.argmax(w))
    def _idx_min(w):
        return (len(w) - 1) - int(np.argmin(w))
    bsm_h = high.rolling(n, min_periods=max(n // 3, 2)).apply(_idx_max, raw=True)
    bsm_l = low.rolling(n, min_periods=max(n // 3, 2)).apply(_idx_min, raw=True)
    up = 100.0 * (n - bsm_h) / n
    dn = 100.0 * (n - bsm_l) / n
    return up, dn


def _vortex(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    vmp = (high - low.shift(1)).abs()
    vmm = (low - high.shift(1)).abs()
    vip = vmp.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum().replace(0, np.nan)
    vim = vmm.rolling(n, min_periods=max(n // 3, 2)).sum() / tr.rolling(n, min_periods=max(n // 3, 2)).sum().replace(0, np.nan)
    return vip, vim


def _mass_index(high, low, n_ema=9, n_sum=25):
    rng = high - low
    e1 = _ema(rng, n_ema)
    e2 = _ema(e1, n_ema)
    ratio = e1 / e2.replace(0, np.nan)
    return ratio.rolling(n_sum, min_periods=max(n_sum // 3, 2)).sum()


def _choppiness(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr_sum = tr.rolling(n, min_periods=max(n // 3, 2)).sum()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    rng = hh - ll
    return 100.0 * np.log10(_safe_div(atr_sum, rng).replace(0, np.nan)) / np.log10(n)


def _ultimate(close, high, low, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = pd.concat([high, pc], axis=1).max(axis=1) - pd.concat([low, pc], axis=1).min(axis=1)
    avg = lambda w: bp.rolling(w, min_periods=max(w // 3, 2)).sum() / tr.rolling(w, min_periods=max(w // 3, 2)).sum().replace(0, np.nan)
    return 100.0 * (4 * avg(n1) + 2 * avg(n2) + avg(n3)) / 7.0


def _awesome(high, low, fast=5, slow=34):
    mp = (high + low) / 2.0
    return mp.rolling(fast, min_periods=max(fast // 3, 2)).mean() - mp.rolling(slow, min_periods=max(slow // 3, 2)).mean()


def _kst(close, r1=10, r2=15, r3=20, r4=30, s1=10, s2=10, s3=10, s4=15):
    roc = lambda n: close.pct_change(n)
    return (
        roc(r1).rolling(s1, min_periods=max(s1 // 3, 2)).mean() * 1
        + roc(r2).rolling(s2, min_periods=max(s2 // 3, 2)).mean() * 2
        + roc(r3).rolling(s3, min_periods=max(s3 // 3, 2)).mean() * 3
        + roc(r4).rolling(s4, min_periods=max(s4 // 3, 2)).mean() * 4
    )


def _dpo(close, n=21):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)


def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    dn = (-d).clip(lower=0).rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(up - dn, up + dn)


def _kvo(high, low, close, volume, fast=34, slow=55):
    hlc3 = (high + low + close) / 3.0
    trend = np.sign(hlc3.diff().fillna(0))
    sv = volume * trend
    return _ema(sv, fast) - _ema(sv, slow)


def _stc(close, fast=23, slow=50, cyc=10):
    macd = _ema(close, fast) - _ema(close, slow)
    lo = macd.rolling(cyc, min_periods=max(cyc // 3, 2)).min()
    hi = macd.rolling(cyc, min_periods=max(cyc // 3, 2)).max()
    k = 100.0 * _safe_div(macd - lo, hi - lo)
    return k.ewm(span=cyc, adjust=False, min_periods=max(cyc // 3, 2)).mean()


def _coppock(close, r1=14, r2=11, smooth=10):
    return (close.pct_change(r1) + close.pct_change(r2)).rolling(smooth, min_periods=max(smooth // 3, 2)).mean()


def _obv(close, volume):
    sign = np.sign(close.diff().fillna(0))
    return (sign * volume).cumsum()

# ============================================================
#                    D1 FEATURES 076-150
# ============================================================

def f09_mexh_076_aroon_oscillator_50_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    up, dn = _aroon(high, low, 50)
    return (up - dn).diff()


def f09_mexh_077_aroon_up_252_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    up, _d = _aroon(high, low, YDAYS)
    return (up).diff()


def f09_mexh_078_choppiness_14_zscore_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    c = _choppiness(high, low, close, 14)
    return (_rolling_zscore(c, YDAYS)).diff()


def f09_mexh_079_adx_14_pctrank_504d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    _p, _m, adx = _dmi(high, low, close, 14)
    return (_rolling_pctrank(adx, 504)).diff()


def f09_mexh_080_di_cross_count_252d_14_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    p, m, _a = _dmi(high, low, close, 14)
    sign = np.sign((p - m).fillna(0))
    crosses = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (crosses.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_081_price_rsi14_corr_63d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    return (close.pct_change().rolling(QDAYS, min_periods=MDAYS).corr(r.diff())).diff()


def f09_mexh_082_price_rsi25_corr_252d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 25)
    return (close.pct_change().rolling(YDAYS, min_periods=QDAYS).corr(r.diff())).diff()


def f09_mexh_083_macd_hist_divergence_63d_d1(close: pd.Series) -> pd.Series:
    _l, _s, h = _macd(close)
    hh_p = (close > close.rolling(MDAYS, min_periods=5).max().shift(1)).astype(int)
    lh_h = (h < h.rolling(MDAYS, min_periods=5).max().shift(1)).astype(int)
    div = (hh_p & lh_h).astype(float)
    return (div.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f09_mexh_084_macd_hist_divergence_252d_d1(close: pd.Series) -> pd.Series:
    _l, _s, h = _macd(close)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lh_h = (h < h.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lh_h).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_085_obv_price_divergence_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    osl = _rolling_slope(obv, MDAYS)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_obv = (osl < osl.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_obv).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_086_higher_high_lower_momentum63_count_252d_d1(close: pd.Series) -> pd.Series:
    mom = close.pct_change(QDAYS)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_m = (mom < mom.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_m).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_087_higher_high_lower_momentum252_count_504d_d1(close: pd.Series) -> pd.Series:
    mom = close.pct_change(YDAYS)
    hh_p = (close > close.rolling(YDAYS, min_periods=QDAYS).max().shift(1)).astype(int)
    lo_m = (mom < mom.rolling(YDAYS, min_periods=QDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_m).astype(float)
    return (div.rolling(504, min_periods=126).sum()).diff()


def f09_mexh_088_higher_high_lower_volume_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    vavg = volume.rolling(MDAYS, min_periods=5).mean()
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_v = (vavg < vavg.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_v).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_089_lower_high_lower_rsi14_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    lh_p = (close.rolling(MDAYS, min_periods=5).max() < close.rolling(MDAYS, min_periods=5).max().shift(MDAYS)).astype(int)
    lo_r = (r.rolling(MDAYS, min_periods=5).max() < r.rolling(MDAYS, min_periods=5).max().shift(MDAYS)).astype(int)
    div = (lh_p & lo_r).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_090_higher_high_lower_obv_volume_intensity_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    obv_chg = obv.diff(MDAYS)
    intensity = obv_chg / volume.rolling(MDAYS, min_periods=5).sum().replace(0, np.nan)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_i = (intensity < intensity.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_i).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_091_price_macd_corr_252d_d1(close: pd.Series) -> pd.Series:
    _l, _s, h = _macd(close)
    return (close.pct_change().rolling(YDAYS, min_periods=QDAYS).corr(h.diff())).diff()


def f09_mexh_092_rsi14_vs_price_zscore_div_63d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    return (_rolling_zscore(r, QDAYS) - _rolling_zscore(_safe_log(close), QDAYS)).diff()


def f09_mexh_093_rsi25_vs_price_zscore_div_252d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 25)
    return (_rolling_zscore(r, YDAYS) - _rolling_zscore(_safe_log(close), YDAYS)).diff()


def f09_mexh_094_macd_hist_zscore_minus_logret_zscore_63d_d1(close: pd.Series) -> pd.Series:
    _l, _s, h = _macd(close)
    return (_rolling_zscore(h, QDAYS) - _rolling_zscore(close.pct_change(), QDAYS)).diff()


def f09_mexh_095_higher_high_no_macd_higher_high_count_252d_d1(close: pd.Series) -> pd.Series:
    _l_unused, _s, _h = _macd(close)
    line = _ema(close, 12) - _ema(close, 26)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    nh_l = (line <= line.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & nh_l).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_096_higher_high_rsi14_under_70_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    weak = (r < 70).astype(int)
    div = (hh_p & weak).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_097_higher_high_adx14_falling_count_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    _p, _m, adx = _dmi(high, low, close, 14)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    weak = (adx < adx.shift(5)).astype(int)
    div = (hh_p & weak).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_098_rsi_vs_price_slope_gap_63d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    return (_rolling_slope(r, QDAYS) - _rolling_slope(_safe_log(close), QDAYS)).diff()


def f09_mexh_099_volume_weighted_rsi_divergence_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    vw_r = (r * volume).rolling(QDAYS, min_periods=MDAYS).sum() / volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    return (_rolling_zscore(vw_r, YDAYS) - _rolling_zscore(_safe_log(close), YDAYS)).diff()


def f09_mexh_100_three_way_divergence_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    vavg = volume.rolling(MDAYS, min_periods=5).mean()
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_r = (r < r.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_v = (vavg < vavg.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    triple = (hh_p & lo_r & lo_v).astype(float)
    return (triple.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_101_consec_decline_momentum_21d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    decl = (m < m.shift(1)).astype(int)
    grp = (decl.diff().ne(0)).cumsum()
    streak = decl.groupby(grp).cumsum() * decl
    return (streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)).diff()


def f09_mexh_102_consec_decline_momentum_63d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(QDAYS)
    decl = (m < m.shift(1)).astype(int)
    grp = (decl.diff().ne(0)).cumsum()
    streak = decl.groupby(grp).cumsum() * decl
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_103_momentum_slope_decline_21d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    return (_rolling_slope(m, MDAYS)).diff()


def f09_mexh_104_momentum_slope_decline_63d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(QDAYS)
    return (_rolling_slope(m, QDAYS)).diff()


def f09_mexh_105_fading_thrust_count_252d_d1(close: pd.Series) -> pd.Series:
    r5 = close.pct_change(5)
    d = (r5 < r5.shift(1)).astype(int)
    streak = d.rolling(3, min_periods=1).sum() == 3
    return (streak.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_106_roc63_declining_streak_max_252d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(QDAYS)
    dec = (m < m.shift(1)).astype(int)
    grp = (dec.diff().ne(0)).cumsum()
    streak = dec.groupby(grp).cumsum() * dec
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_107_momentum_pctile_decay_rate_63d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    pr = _rolling_pctrank(m, YDAYS)
    return (pr - pr.shift(QDAYS)).diff()


def f09_mexh_108_mean_reversion_timing_5d_after_extreme_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    zm = _rolling_zscore(m, YDAYS)
    cond = zm.shift(5) > 2
    r5 = _safe_log(close) - _safe_log(close.shift(5))
    return (r5.where(cond, np.nan)).diff()


def f09_mexh_109_smoothed_momentum_halflife_63d_d1(close: pd.Series) -> pd.Series:
    sm = _ema(close.pct_change(), 5)
    lag = sm.shift(1)
    cov = (sm * lag).rolling(QDAYS, min_periods=MDAYS).mean() - sm.rolling(QDAYS, min_periods=MDAYS).mean() * lag.rolling(QDAYS, min_periods=MDAYS).mean()
    var = lag.rolling(QDAYS, min_periods=MDAYS).var()
    phi = _safe_div(cov, var).clip(-0.999, 0.999)
    return (-np.log(2.0) / np.log(phi.abs().replace(0, np.nan))).diff()


def f09_mexh_110_momentum_compression_21_vs_252_d1(close: pd.Series) -> pd.Series:
    m21 = close.pct_change(MDAYS)
    m252 = close.pct_change(YDAYS)
    return (_safe_div(m21.rolling(YDAYS, min_periods=QDAYS).std(), m252.rolling(YDAYS, min_periods=QDAYS).std())).diff()


def f09_mexh_111_fresh_high_no_new_rsi_high_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    new_p = (close >= close.rolling(QDAYS, min_periods=MDAYS).max()).astype(int)
    new_r = (r >= r.rolling(QDAYS, min_periods=MDAYS).max()).astype(int)
    div = (new_p & (1 - new_r)).astype(float)
    return (div.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_112_roc21_decay_from_max_63d_d1(close: pd.Series) -> pd.Series:
    r = close.pct_change(MDAYS)
    return (r.rolling(QDAYS, min_periods=MDAYS).max() - r).diff()


def f09_mexh_113_roc63_decay_from_max_252d_d1(close: pd.Series) -> pd.Series:
    r = close.pct_change(QDAYS)
    return (r.rolling(YDAYS, min_periods=QDAYS).max() - r).diff()


def f09_mexh_114_momentum_velocity_curvature_21d_d1(close: pd.Series) -> pd.Series:
    return (_ema(close.pct_change(), 5).diff().diff()).diff()


def f09_mexh_115_consec_low_momentum_below_zero_63d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    neg = (m < 0).astype(int)
    grp = (neg.diff().ne(0)).cumsum()
    streak = neg.groupby(grp).cumsum() * neg
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_116_acceleration_loss_count_21d_d1(close: pd.Series) -> pd.Series:
    r5 = close.pct_change(5)
    acc = r5.diff(5)
    flip = ((acc < 0) & (acc.shift(1) >= 0)).astype(float)
    return (flip.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f09_mexh_117_thrust_loss_intensity_63d_d1(close: pd.Series) -> pd.Series:
    r5 = close.pct_change(5)
    drops = r5.diff().clip(upper=0).abs()
    return (drops.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f09_mexh_118_lower_thrust_intensity_252d_d1(close: pd.Series) -> pd.Series:
    r = close.pct_change(MDAYS)
    drops = r.diff().clip(upper=0).abs()
    return (drops.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_119_momentum_break_below_zero_count_252d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(QDAYS)
    cross = ((m < 0) & (m.shift(1) >= 0)).astype(float)
    return (cross.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_120_post_momentum_peak_decay_speed_63d_d1(close: pd.Series) -> pd.Series:
    m = close.pct_change(MDAYS)
    return (_rolling_slope(m, QDAYS)).diff()


def f09_mexh_121_roc_of_roc_jerk_zscore_63d_d1(close: pd.Series) -> pd.Series:
    r = close.pct_change(MDAYS)
    return (_rolling_zscore(r.pct_change(MDAYS), QDAYS)).diff()


def f09_mexh_122_dmi_strength_50_zscore_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    _p, _m, adx = _dmi(high, low, close, 50)
    return (_rolling_zscore(adx, YDAYS)).diff()


def f09_mexh_123_mom_252_zscore_504d_d1(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_safe_log(close) - _safe_log(close.shift(YDAYS)), 504)).diff()


def f09_mexh_124_mom_504_zscore_1260d_d1(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_safe_log(close) - _safe_log(close.shift(504)), 1260)).diff()


def f09_mexh_125_momentum_entropy_63d_d1(close: pd.Series) -> pd.Series:
    r = close.pct_change()
    def _h(w):
        v = w[~np.isnan(w)]
        if len(v) < 5:
            return np.nan
        bins = np.histogram(v, bins=5)[0].astype(float)
        s = bins.sum()
        if s == 0:
            return np.nan
        p = bins / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum()) if len(p) else np.nan
    return (r.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True)).diff()


def f09_mexh_126_exhaustion_composite_rsi_macd_adx_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 25)
    rsi_fade = r.rolling(QDAYS, min_periods=MDAYS).max() - r
    _l, _s, h = _macd(close)
    macd_neg = (-h).clip(lower=0)
    _p, _m, adx = _dmi(high, low, close, 14)
    adx_drop = adx.rolling(MDAYS, min_periods=5).max() - adx
    return (_rolling_zscore(rsi_fade, YDAYS) + _rolling_zscore(macd_neg, YDAYS) + _rolling_zscore(adx_drop, YDAYS)).diff()


def f09_mexh_127_momentum_in_high_vol_regime_21d_d1(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=5).std() * np.sqrt(YDAYS)
    med = rv.rolling(YDAYS, min_periods=QDAYS).median()
    cond = rv > med
    return (close.pct_change(MDAYS).where(cond, np.nan)).diff()


def f09_mexh_128_momentum_in_low_vol_regime_21d_d1(close: pd.Series) -> pd.Series:
    rv = close.pct_change().rolling(MDAYS, min_periods=5).std() * np.sqrt(YDAYS)
    med = rv.rolling(YDAYS, min_periods=QDAYS).median()
    cond = rv < med
    return (close.pct_change(MDAYS).where(cond, np.nan)).diff()


def f09_mexh_129_momentum_pctrank_504d_d1(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_safe_log(close) - _safe_log(close.shift(MDAYS)), 504)).diff()


def f09_mexh_130_ema_fast_minus_ema_slow_momentum_divergence_d1(close: pd.Series) -> pd.Series:
    return (_ema(close.pct_change(), 5) - _ema(close.pct_change(), MDAYS)).diff()


def f09_mexh_131_momentum_flatness_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close) - _safe_log(close.shift(5))
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    m = r.rolling(QDAYS, min_periods=MDAYS).mean().abs()
    return (_safe_div(sd, m)).diff()


def f09_mexh_132_slow_vs_fast_stoch_convergence_63d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    k14 = _stoch_k(close, high, low, 14)
    k63 = _stoch_k(close, high, low, 63)
    return ((k14 - k63).rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f09_mexh_133_momentum_minus_trend_strength_gap_14_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    rz = _rolling_zscore(_safe_log(close) - _safe_log(close.shift(MDAYS)), YDAYS)
    _p, _m, adx = _dmi(high, low, close, 14)
    return (rz - (adx / 100.0)).diff()


def f09_mexh_134_acceleration_decay_signature_21d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return ((a < 0).astype(float).rolling(MDAYS, min_periods=5).sum()).diff()


def f09_mexh_135_acceleration_decay_signature_63d_d1(close: pd.Series) -> pd.Series:
    a = _safe_log(close).diff().diff()
    return ((a < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f09_mexh_136_kvo_zero_cross_count_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    k = _kvo(high, low, close, volume, 34, 55)
    sign = np.sign(k.fillna(0))
    cross = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (cross.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_137_macd_hist_negative_streak_max_252d_d1(close: pd.Series) -> pd.Series:
    _l, _s, h = _macd(close)
    neg = (h < 0).astype(int)
    grp = (neg.diff().ne(0)).cumsum()
    streak = neg.groupby(grp).cumsum() * neg
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_138_rsi14_distance_from_50_persistence_63d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    return ((r - 50).abs().rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f09_mexh_139_rsi_acceleration_zscore_63d_d1(close: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    return (_rolling_zscore(r.diff().diff(), QDAYS)).diff()


def f09_mexh_140_macd_signal_line_distance_63d_mean_d1(close: pd.Series) -> pd.Series:
    l, s, _h = _macd(close)
    return ((l - s).rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f09_mexh_141_higher_high_lower_trix15_count_252d_d1(close: pd.Series) -> pd.Series:
    t = _trix(close, 15)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_t = (t < t.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    return ((hh_p & lo_t).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_142_three_oscillator_overbought_confluence_63d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    r = _rsi_wilder(close, 14)
    k = _stoch_k(close, high, low, 14)
    tp = (high + low + close) / 3.0
    sma = tp.rolling(20, min_periods=7).mean()
    md = (tp - sma).abs().rolling(20, min_periods=7).mean()
    cci = (tp - sma) / (0.015 * md.replace(0, np.nan))
    conf = ((r > 70) & (k > 80) & (cci > 100)).astype(float)
    return (conf.rolling(QDAYS, min_periods=MDAYS).sum()).diff()


def f09_mexh_143_aroon_oscillator_decline_streak_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    up, dn = _aroon(high, low, 25)
    osc = up - dn
    decl = (osc < osc.shift(1)).astype(int)
    grp = (decl.diff().ne(0)).cumsum()
    streak = decl.groupby(grp).cumsum() * decl
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_144_vortex_signal_change_count_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    p, m = _vortex(high, low, close, 14)
    sign = np.sign((p - m).fillna(0))
    cross = ((sign != sign.shift(1)) & sign.shift(1).ne(0)).astype(float)
    return (cross.rolling(YDAYS, min_periods=QDAYS).sum()).diff()


def f09_mexh_145_choppiness_rising_streak_max_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    c = _choppiness(high, low, close, 14)
    up = (c > c.shift(1)).astype(int)
    grp = (up.diff().ne(0)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_146_dpo_63_zscore_252d_d1(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_dpo(close, QDAYS), YDAYS)).diff()


def f09_mexh_147_kst_zscore_252d_d1(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_kst(close), YDAYS)).diff()


def f09_mexh_148_ultimate_below_30_streak_max_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    uo = _ultimate(close, high, low, 7, 14, 28)
    low_uo = (uo < 30).astype(int)
    grp = (low_uo.diff().ne(0)).cumsum()
    streak = low_uo.groupby(grp).cumsum() * low_uo
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff()


def f09_mexh_149_composite_thrust_decay_score_d1(close: pd.Series) -> pd.Series:
    r21 = close.pct_change(MDAYS)
    f1 = r21.rolling(QDAYS, min_periods=MDAYS).max() - r21
    r63 = close.pct_change(QDAYS)
    f2 = r63.rolling(YDAYS, min_periods=QDAYS).max() - r63
    decl = (r21 < r21.shift(1)).astype(int)
    grp = (decl.diff().ne(0)).cumsum()
    streak = (decl.groupby(grp).cumsum() * decl).astype(float)
    return (_rolling_zscore(f1, YDAYS) + _rolling_zscore(f2, YDAYS) + _rolling_zscore(streak, YDAYS)).diff()


def f09_mexh_150_composite_exhaustion_aggregate_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    r25 = _rsi_wilder(close, 25)
    rsi_fade = r25.rolling(QDAYS, min_periods=MDAYS).max() - r25
    k63 = _stoch_k(close, high, low, 63)
    stoch_fade = k63.rolling(QDAYS, min_periods=MDAYS).max() - k63
    _p, _m, adx = _dmi(high, low, close, 50)
    adx_drop = adx.rolling(MDAYS, min_periods=5).max() - adx
    r14 = _rsi_wilder(close, 14)
    hh_p = (close > close.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    lo_r = (r14 < r14.rolling(QDAYS, min_periods=MDAYS).max().shift(1)).astype(int)
    div = (hh_p & lo_r).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (_rolling_zscore(rsi_fade, YDAYS) + _rolling_zscore(stoch_fade, YDAYS) + _rolling_zscore(adx_drop, YDAYS) + _rolling_zscore(div, YDAYS)).diff()


MOMENTUM_EXHAUSTION_D1_REGISTRY_076_150 = {
    "f09_mexh_076_aroon_oscillator_50_d1": {"inputs": ["high", "low"], "func": f09_mexh_076_aroon_oscillator_50_d1},
    "f09_mexh_077_aroon_up_252_d1": {"inputs": ["high", "low"], "func": f09_mexh_077_aroon_up_252_d1},
    "f09_mexh_078_choppiness_14_zscore_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_078_choppiness_14_zscore_252d_d1},
    "f09_mexh_079_adx_14_pctrank_504d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_079_adx_14_pctrank_504d_d1},
    "f09_mexh_080_di_cross_count_252d_14_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_080_di_cross_count_252d_14_d1},
    "f09_mexh_081_price_rsi14_corr_63d_d1": {"inputs": ["close"], "func": f09_mexh_081_price_rsi14_corr_63d_d1},
    "f09_mexh_082_price_rsi25_corr_252d_d1": {"inputs": ["close"], "func": f09_mexh_082_price_rsi25_corr_252d_d1},
    "f09_mexh_083_macd_hist_divergence_63d_d1": {"inputs": ["close"], "func": f09_mexh_083_macd_hist_divergence_63d_d1},
    "f09_mexh_084_macd_hist_divergence_252d_d1": {"inputs": ["close"], "func": f09_mexh_084_macd_hist_divergence_252d_d1},
    "f09_mexh_085_obv_price_divergence_252d_d1": {"inputs": ["close", "volume"], "func": f09_mexh_085_obv_price_divergence_252d_d1},
    "f09_mexh_086_higher_high_lower_momentum63_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_086_higher_high_lower_momentum63_count_252d_d1},
    "f09_mexh_087_higher_high_lower_momentum252_count_504d_d1": {"inputs": ["close"], "func": f09_mexh_087_higher_high_lower_momentum252_count_504d_d1},
    "f09_mexh_088_higher_high_lower_volume_count_252d_d1": {"inputs": ["close", "volume"], "func": f09_mexh_088_higher_high_lower_volume_count_252d_d1},
    "f09_mexh_089_lower_high_lower_rsi14_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_089_lower_high_lower_rsi14_count_252d_d1},
    "f09_mexh_090_higher_high_lower_obv_volume_intensity_count_252d_d1": {"inputs": ["close", "volume"], "func": f09_mexh_090_higher_high_lower_obv_volume_intensity_count_252d_d1},
    "f09_mexh_091_price_macd_corr_252d_d1": {"inputs": ["close"], "func": f09_mexh_091_price_macd_corr_252d_d1},
    "f09_mexh_092_rsi14_vs_price_zscore_div_63d_d1": {"inputs": ["close"], "func": f09_mexh_092_rsi14_vs_price_zscore_div_63d_d1},
    "f09_mexh_093_rsi25_vs_price_zscore_div_252d_d1": {"inputs": ["close"], "func": f09_mexh_093_rsi25_vs_price_zscore_div_252d_d1},
    "f09_mexh_094_macd_hist_zscore_minus_logret_zscore_63d_d1": {"inputs": ["close"], "func": f09_mexh_094_macd_hist_zscore_minus_logret_zscore_63d_d1},
    "f09_mexh_095_higher_high_no_macd_higher_high_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_095_higher_high_no_macd_higher_high_count_252d_d1},
    "f09_mexh_096_higher_high_rsi14_under_70_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_096_higher_high_rsi14_under_70_count_252d_d1},
    "f09_mexh_097_higher_high_adx14_falling_count_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_097_higher_high_adx14_falling_count_252d_d1},
    "f09_mexh_098_rsi_vs_price_slope_gap_63d_d1": {"inputs": ["close"], "func": f09_mexh_098_rsi_vs_price_slope_gap_63d_d1},
    "f09_mexh_099_volume_weighted_rsi_divergence_63d_d1": {"inputs": ["close", "volume"], "func": f09_mexh_099_volume_weighted_rsi_divergence_63d_d1},
    "f09_mexh_100_three_way_divergence_count_252d_d1": {"inputs": ["close", "volume"], "func": f09_mexh_100_three_way_divergence_count_252d_d1},
    "f09_mexh_101_consec_decline_momentum_21d_d1": {"inputs": ["close"], "func": f09_mexh_101_consec_decline_momentum_21d_d1},
    "f09_mexh_102_consec_decline_momentum_63d_d1": {"inputs": ["close"], "func": f09_mexh_102_consec_decline_momentum_63d_d1},
    "f09_mexh_103_momentum_slope_decline_21d_d1": {"inputs": ["close"], "func": f09_mexh_103_momentum_slope_decline_21d_d1},
    "f09_mexh_104_momentum_slope_decline_63d_d1": {"inputs": ["close"], "func": f09_mexh_104_momentum_slope_decline_63d_d1},
    "f09_mexh_105_fading_thrust_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_105_fading_thrust_count_252d_d1},
    "f09_mexh_106_roc63_declining_streak_max_252d_d1": {"inputs": ["close"], "func": f09_mexh_106_roc63_declining_streak_max_252d_d1},
    "f09_mexh_107_momentum_pctile_decay_rate_63d_d1": {"inputs": ["close"], "func": f09_mexh_107_momentum_pctile_decay_rate_63d_d1},
    "f09_mexh_108_mean_reversion_timing_5d_after_extreme_d1": {"inputs": ["close"], "func": f09_mexh_108_mean_reversion_timing_5d_after_extreme_d1},
    "f09_mexh_109_smoothed_momentum_halflife_63d_d1": {"inputs": ["close"], "func": f09_mexh_109_smoothed_momentum_halflife_63d_d1},
    "f09_mexh_110_momentum_compression_21_vs_252_d1": {"inputs": ["close"], "func": f09_mexh_110_momentum_compression_21_vs_252_d1},
    "f09_mexh_111_fresh_high_no_new_rsi_high_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_111_fresh_high_no_new_rsi_high_count_252d_d1},
    "f09_mexh_112_roc21_decay_from_max_63d_d1": {"inputs": ["close"], "func": f09_mexh_112_roc21_decay_from_max_63d_d1},
    "f09_mexh_113_roc63_decay_from_max_252d_d1": {"inputs": ["close"], "func": f09_mexh_113_roc63_decay_from_max_252d_d1},
    "f09_mexh_114_momentum_velocity_curvature_21d_d1": {"inputs": ["close"], "func": f09_mexh_114_momentum_velocity_curvature_21d_d1},
    "f09_mexh_115_consec_low_momentum_below_zero_63d_d1": {"inputs": ["close"], "func": f09_mexh_115_consec_low_momentum_below_zero_63d_d1},
    "f09_mexh_116_acceleration_loss_count_21d_d1": {"inputs": ["close"], "func": f09_mexh_116_acceleration_loss_count_21d_d1},
    "f09_mexh_117_thrust_loss_intensity_63d_d1": {"inputs": ["close"], "func": f09_mexh_117_thrust_loss_intensity_63d_d1},
    "f09_mexh_118_lower_thrust_intensity_252d_d1": {"inputs": ["close"], "func": f09_mexh_118_lower_thrust_intensity_252d_d1},
    "f09_mexh_119_momentum_break_below_zero_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_119_momentum_break_below_zero_count_252d_d1},
    "f09_mexh_120_post_momentum_peak_decay_speed_63d_d1": {"inputs": ["close"], "func": f09_mexh_120_post_momentum_peak_decay_speed_63d_d1},
    "f09_mexh_121_roc_of_roc_jerk_zscore_63d_d1": {"inputs": ["close"], "func": f09_mexh_121_roc_of_roc_jerk_zscore_63d_d1},
    "f09_mexh_122_dmi_strength_50_zscore_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_122_dmi_strength_50_zscore_252d_d1},
    "f09_mexh_123_mom_252_zscore_504d_d1": {"inputs": ["close"], "func": f09_mexh_123_mom_252_zscore_504d_d1},
    "f09_mexh_124_mom_504_zscore_1260d_d1": {"inputs": ["close"], "func": f09_mexh_124_mom_504_zscore_1260d_d1},
    "f09_mexh_125_momentum_entropy_63d_d1": {"inputs": ["close"], "func": f09_mexh_125_momentum_entropy_63d_d1},
    "f09_mexh_126_exhaustion_composite_rsi_macd_adx_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_126_exhaustion_composite_rsi_macd_adx_d1},
    "f09_mexh_127_momentum_in_high_vol_regime_21d_d1": {"inputs": ["close"], "func": f09_mexh_127_momentum_in_high_vol_regime_21d_d1},
    "f09_mexh_128_momentum_in_low_vol_regime_21d_d1": {"inputs": ["close"], "func": f09_mexh_128_momentum_in_low_vol_regime_21d_d1},
    "f09_mexh_129_momentum_pctrank_504d_d1": {"inputs": ["close"], "func": f09_mexh_129_momentum_pctrank_504d_d1},
    "f09_mexh_130_ema_fast_minus_ema_slow_momentum_divergence_d1": {"inputs": ["close"], "func": f09_mexh_130_ema_fast_minus_ema_slow_momentum_divergence_d1},
    "f09_mexh_131_momentum_flatness_63d_d1": {"inputs": ["close"], "func": f09_mexh_131_momentum_flatness_63d_d1},
    "f09_mexh_132_slow_vs_fast_stoch_convergence_63d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_132_slow_vs_fast_stoch_convergence_63d_d1},
    "f09_mexh_133_momentum_minus_trend_strength_gap_14_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_133_momentum_minus_trend_strength_gap_14_d1},
    "f09_mexh_134_acceleration_decay_signature_21d_d1": {"inputs": ["close"], "func": f09_mexh_134_acceleration_decay_signature_21d_d1},
    "f09_mexh_135_acceleration_decay_signature_63d_d1": {"inputs": ["close"], "func": f09_mexh_135_acceleration_decay_signature_63d_d1},
    "f09_mexh_136_kvo_zero_cross_count_252d_d1": {"inputs": ["close", "high", "low", "volume"], "func": f09_mexh_136_kvo_zero_cross_count_252d_d1},
    "f09_mexh_137_macd_hist_negative_streak_max_252d_d1": {"inputs": ["close"], "func": f09_mexh_137_macd_hist_negative_streak_max_252d_d1},
    "f09_mexh_138_rsi14_distance_from_50_persistence_63d_d1": {"inputs": ["close"], "func": f09_mexh_138_rsi14_distance_from_50_persistence_63d_d1},
    "f09_mexh_139_rsi_acceleration_zscore_63d_d1": {"inputs": ["close"], "func": f09_mexh_139_rsi_acceleration_zscore_63d_d1},
    "f09_mexh_140_macd_signal_line_distance_63d_mean_d1": {"inputs": ["close"], "func": f09_mexh_140_macd_signal_line_distance_63d_mean_d1},
    "f09_mexh_141_higher_high_lower_trix15_count_252d_d1": {"inputs": ["close"], "func": f09_mexh_141_higher_high_lower_trix15_count_252d_d1},
    "f09_mexh_142_three_oscillator_overbought_confluence_63d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_142_three_oscillator_overbought_confluence_63d_d1},
    "f09_mexh_143_aroon_oscillator_decline_streak_252d_d1": {"inputs": ["high", "low"], "func": f09_mexh_143_aroon_oscillator_decline_streak_252d_d1},
    "f09_mexh_144_vortex_signal_change_count_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_144_vortex_signal_change_count_252d_d1},
    "f09_mexh_145_choppiness_rising_streak_max_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_145_choppiness_rising_streak_max_252d_d1},
    "f09_mexh_146_dpo_63_zscore_252d_d1": {"inputs": ["close"], "func": f09_mexh_146_dpo_63_zscore_252d_d1},
    "f09_mexh_147_kst_zscore_252d_d1": {"inputs": ["close"], "func": f09_mexh_147_kst_zscore_252d_d1},
    "f09_mexh_148_ultimate_below_30_streak_max_252d_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_148_ultimate_below_30_streak_max_252d_d1},
    "f09_mexh_149_composite_thrust_decay_score_d1": {"inputs": ["close"], "func": f09_mexh_149_composite_thrust_decay_score_d1},
    "f09_mexh_150_composite_exhaustion_aggregate_d1": {"inputs": ["close", "high", "low"], "func": f09_mexh_150_composite_exhaustion_aggregate_d1},
}
