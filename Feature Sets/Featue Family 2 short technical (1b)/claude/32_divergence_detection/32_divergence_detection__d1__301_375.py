"""32_divergence_detection d1 features 301-375 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)

def _macd_line(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)

def _macd_hist(close, fast=12, slow=26, sig=9):
    line = _macd_line(close, fast, slow)
    return line - _ema(line, sig)

def _obv(close, volume):
    return (np.sign(close.diff().fillna(0)) * volume).cumsum()

def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    return (mfm * volume).fillna(0).cumsum()

def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)

def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    neg = rmf.where(delta < 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(pos, neg)
    return 100.0 - 100.0 / (1.0 + mr)

def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)

def _trix(close, n=15):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return e3.pct_change() * 100.0

def _tsi(close, r=25, s=13):
    m = close.diff()
    am = m.abs()
    return 100.0 * _safe_div(_ema(_ema(m, r), s), _ema(_ema(am, r), s))

def _roc(close, n=12):
    return close.pct_change(n) * 100.0

def _uo(high, low, close, n1=7, n2=14, n3=28):
    pc = close.shift(1)
    bp = close - pd.concat([low, pc], axis=1).min(axis=1)
    tr = _true_range(high, low, close)

    def _avg(n):
        return _safe_div(bp.rolling(n, min_periods=max(n // 3, 2)).sum(), tr.rolling(n, min_periods=max(n // 3, 2)).sum())
    return 100.0 * (4.0 * _avg(n1) + 2.0 * _avg(n2) + _avg(n3)) / 7.0

def _williams_r(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return -100.0 * _safe_div(hh - close, hh - ll)

def _cmf(high, low, close, volume, n=20):
    rng = (high - low).replace(0, np.nan)
    mfm = (close - low - (high - close)) / rng
    mfv = (mfm * volume).fillna(0)
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(), volume.rolling(n, min_periods=max(n // 3, 2)).sum())

def _welch_t_stat_slope_diff(price, osc, n):
    """Welch's t-statistic for difference in rolling-slope between log-price and standardized
    oscillator. Signed: positive when price slope > osc slope (bearish divergence direction).
    Approximate (uses pooled rolling std of slope-by-window-of-windows). Higher |t| = more
    statistically significant divergence."""
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(_rolling_zscore(osc, n), n)
    diff = ps - osl
    sd = diff.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(diff, sd / np.sqrt(n))

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    return ((ps > 0) & (osl < 0)).astype(float).where(ps.notna() & osl.notna(), np.nan)

def _body(open_, close):
    return close - open_

def _bar_range(high, low):
    return high - low

def _upper_wick(open_, close, high):
    return high - pd.concat([open_, close], axis=1).max(axis=1)

def _lower_wick(open_, close, low):
    return pd.concat([open_, close], axis=1).min(axis=1) - low

def _is_doji(open_, close, high, low, body_max_frac=0.1):
    rng = _bar_range(high, low).replace(0, np.nan)
    return (_body(open_, close).abs() / rng < body_max_frac).astype(float).where(rng.notna(), np.nan)

def _is_shooting_star(open_, close, high, low):
    rng = _bar_range(high, low).replace(0, np.nan)
    uw = _upper_wick(open_, close, high) / rng
    lw = _lower_wick(open_, close, low) / rng
    body = _body(open_, close).abs() / rng
    return ((uw > 0.6) & (lw < 0.1) & (body < 0.3)).astype(float).where(rng.notna(), np.nan)

def _is_hanging_man(open_, close, high, low):
    rng = _bar_range(high, low).replace(0, np.nan)
    lw = _lower_wick(open_, close, low) / rng
    uw = _upper_wick(open_, close, high) / rng
    body = _body(open_, close).abs() / rng
    return ((lw > 0.6) & (uw < 0.1) & (body < 0.3)).astype(float).where(rng.notna(), np.nan)

def _is_bearish_engulfing(open_, close):
    pc = close.shift(1)
    po = open_.shift(1)
    return ((pc > po) & (close < open_) & (close < po) & (open_ > pc)).astype(float).where(pc.notna() & po.notna(), np.nan)

def _is_dark_cloud_cover(open_, close, high):
    pc = close.shift(1)
    po = open_.shift(1)
    ph = high.shift(1)
    midbody = (pc + po) / 2.0
    return ((pc > po) & (open_ > ph) & (close < midbody) & (close > po)).astype(float).where(pc.notna() & po.notna(), np.nan)

def _is_3_black_crows(close, open_):
    return ((close < open_) & (close.shift(1) < open_.shift(1)) & (close.shift(2) < open_.shift(2)) & (close < close.shift(1)) & (close.shift(1) < close.shift(2))).astype(float).where(close.shift(2).notna(), np.nan)

def _is_evening_star(open_, close):
    c1 = close.shift(2)
    o1 = open_.shift(2)
    c2 = close.shift(1)
    o2 = open_.shift(1)
    big_up1 = c1 - o1 > c1 * 0.005
    small_body2 = (c2 - o2).abs() < (c1 - o1) * 0.3
    big_down3 = open_ - close > (c1 - o1) * 0.5
    gap_up = pd.concat([o2, c2], axis=1).min(axis=1) > c1
    return (big_up1 & small_body2 & big_down3 & gap_up).astype(float).where(c1.notna(), np.nan)

def _is_bearish_harami(open_, close):
    pc = close.shift(1)
    po = open_.shift(1)
    prior_bull = pc > po
    cur_bear = close < open_
    body_inside = (open_ < pc) & (close > po) & (open_ > po) & (close < pc)
    return (prior_bull & cur_bear & body_inside).astype(float).where(pc.notna() & po.notna(), np.nan)

def _is_gap_up(open_, high):
    return (open_ > high.shift(1)).astype(float).where(high.shift(1).notna(), np.nan)

def _is_wide_range_bar(high, low, n_window):
    """+1 when current bar's range > 1.5 × n-bar mean range."""
    rng = high - low
    return (rng > 1.5 * rng.rolling(n_window, min_periods=max(n_window // 3, 2)).mean()).astype(float)

def _is_narrow_range_bar(high, low, n_window):
    """+1 when current bar's range < 0.5 × n-bar mean range."""
    rng = high - low
    return (rng < 0.5 * rng.rolling(n_window, min_periods=max(n_window // 3, 2)).mean()).astype(float)

def _is_gravestone_doji(open_, close, high, low):
    rng = _bar_range(high, low).replace(0, np.nan)
    body = (open_ - close).abs() / rng
    lw = _lower_wick(open_, close, low) / rng
    uw = _upper_wick(open_, close, high) / rng
    return ((body < 0.1) & (lw < 0.1) & (uw > 0.7)).astype(float).where(rng.notna(), np.nan)

def _rsi_div_flag(close):
    return (_slope_div_sign(close, _rsi_wilder(close, 14), QDAYS) > 0).astype(float)

def _shift_div_bearish_indicator(price, osc, k):
    pp = price.shift(k)
    op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)

def f32_divd_301_welch_t_stat_div_rsi14_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat of (price slope - RSI14 slope) over 63d. Signed; |t|>2 = significant divergence."""
    return _welch_t_stat_slope_diff(close, _rsi_wilder(close, 14), QDAYS).diff()

def f32_divd_302_welch_t_stat_div_macdline_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat of slope-diff: close vs MACD line, 63d."""
    return _welch_t_stat_slope_diff(close, _macd_line(close, 12, 26), QDAYS).diff()

def f32_divd_303_welch_t_stat_div_macdhist_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat of slope-diff: close vs MACD histogram, 63d."""
    return _welch_t_stat_slope_diff(close, _macd_hist(close, 12, 26, 9), QDAYS).diff()

def f32_divd_304_welch_t_stat_div_obv_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Welch t-stat: close vs OBV, 63d."""
    return _welch_t_stat_slope_diff(close, _obv(close, volume), QDAYS).diff()

def f32_divd_305_welch_t_stat_div_adline_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Welch t-stat: close vs A/D Chaikin, 63d."""
    return _welch_t_stat_slope_diff(close, _ad_line(high, low, close, volume), QDAYS).diff()

def f32_divd_306_welch_t_stat_div_stochk_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs Stoch %K, 63d."""
    return _welch_t_stat_slope_diff(close, _stoch_k(high, low, close, 14), QDAYS).diff()

def f32_divd_307_welch_t_stat_div_mfi_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Welch t-stat: close vs MFI, 63d."""
    return _welch_t_stat_slope_diff(close, _mfi(high, low, close, volume, 14), QDAYS).diff()

def f32_divd_308_welch_t_stat_div_cci_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs CCI, 63d."""
    return _welch_t_stat_slope_diff(close, _cci(high, low, close, 20), QDAYS).diff()

def f32_divd_309_welch_t_stat_div_trix_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs TRIX, 63d."""
    return _welch_t_stat_slope_diff(close, _trix(close, 15), QDAYS).diff()

def f32_divd_310_welch_t_stat_div_tsi_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs TSI, 63d."""
    return _welch_t_stat_slope_diff(close, _tsi(close, 25, 13), QDAYS).diff()

def f32_divd_311_welch_t_stat_div_roc12_63d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs ROC(12), 63d."""
    return _welch_t_stat_slope_diff(close, _roc(close, 12), QDAYS).diff()

def f32_divd_312_welch_t_stat_div_williamsr_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs Williams %R, 63d."""
    return _welch_t_stat_slope_diff(close, _williams_r(high, low, close, 14), QDAYS).diff()

def f32_divd_313_welch_t_stat_div_cmf_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Welch t-stat: close vs CMF, 63d."""
    return _welch_t_stat_slope_diff(close, _cmf(high, low, close, volume, 20), QDAYS).diff()

def f32_divd_314_welch_t_stat_div_uo_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs Ultimate Oscillator, 63d."""
    return _welch_t_stat_slope_diff(close, _uo(high, low, close), QDAYS).diff()

def f32_divd_315_welch_t_stat_div_rsi14_252d_d1(close: pd.Series) -> pd.Series:
    """Welch t-stat: close vs RSI14, 252d (secular significance test)."""
    return _welch_t_stat_slope_diff(close, _rsi_wilder(close, 14), YDAYS).diff()

def f32_divd_316_rsi_div_dwell_time_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where RSI 63d-slope-div sign is bearish (+1)."""
    return _slope_div_sign(close, _rsi_wilder(close, 14), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_317_macdline_div_dwell_time_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where MACD-line 63d-slope-div is bearish."""
    return _slope_div_sign(close, _macd_line(close, 12, 26), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_318_macdhist_div_dwell_time_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where MACD-hist 63d-slope-div is bearish."""
    return _slope_div_sign(close, _macd_hist(close, 12, 26, 9), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_319_obv_div_dwell_time_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where OBV 63d-slope-div is bearish."""
    return _slope_div_sign(close, _obv(close, volume), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_320_adline_div_dwell_time_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where A/D 63d-slope-div is bearish."""
    return _slope_div_sign(close, _ad_line(high, low, close, volume), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_321_stochk_div_dwell_time_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where Stoch %K 63d-slope-div is bearish."""
    return _slope_div_sign(close, _stoch_k(high, low, close, 14), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_322_mfi_div_dwell_time_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where MFI 63d-slope-div is bearish."""
    return _slope_div_sign(close, _mfi(high, low, close, volume, 14), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_323_cci_div_dwell_time_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where CCI 63d-slope-div is bearish."""
    return _slope_div_sign(close, _cci(high, low, close, 20), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_324_trix_div_dwell_time_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TRIX 63d-slope-div is bearish."""
    return _slope_div_sign(close, _trix(close, 15), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_325_tsi_div_dwell_time_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where TSI 63d-slope-div is bearish."""
    return _slope_div_sign(close, _tsi(close, 25, 13), QDAYS).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_326_rsi_div_x_doji_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish slope-div fires AND current bar is a doji."""
    return (_rsi_div_flag(close) * _is_doji(open, close, high, low)).where(close.notna(), np.nan).diff()

def f32_divd_327_rsi_div_x_shooting_star_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND current bar is a shooting star."""
    return (_rsi_div_flag(close) * _is_shooting_star(open, close, high, low)).where(close.notna(), np.nan).diff()

def f32_divd_328_rsi_div_x_hanging_man_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND current bar is a hanging-man pattern."""
    return (_rsi_div_flag(close) * _is_hanging_man(open, close, high, low)).where(close.notna(), np.nan).diff()

def f32_divd_329_rsi_div_x_bearish_engulfing_indicator_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND current bar is bearish engulfing."""
    return (_rsi_div_flag(close) * _is_bearish_engulfing(open, close)).where(close.notna(), np.nan).diff()

def f32_divd_330_rsi_div_x_dark_cloud_cover_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND dark-cloud-cover pattern fires."""
    return (_rsi_div_flag(close) * _is_dark_cloud_cover(open, close, high)).where(close.notna(), np.nan).diff()

def f32_divd_331_rsi_div_x_3_black_crows_indicator_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND 3-black-crows pattern fires."""
    return (_rsi_div_flag(close) * _is_3_black_crows(close, open)).where(close.notna(), np.nan).diff()

def f32_divd_332_rsi_div_x_evening_star_indicator_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND evening-star pattern fires."""
    return (_rsi_div_flag(close) * _is_evening_star(open, close)).where(close.notna(), np.nan).diff()

def f32_divd_333_rsi_div_x_bearish_harami_indicator_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND bearish-harami pattern fires."""
    return (_rsi_div_flag(close) * _is_bearish_harami(open, close)).where(close.notna(), np.nan).diff()

def f32_divd_334_rsi_div_x_gap_up_bar_indicator_d1(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today opens above prior high (gap-up exhaustion)."""
    return (_rsi_div_flag(close) * _is_gap_up(open, high)).where(close.notna(), np.nan).diff()

def f32_divd_335_rsi_div_x_wide_range_bar_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today's range > 1.5 × 21d-mean range (volatility expansion)."""
    return (_rsi_div_flag(close) * _is_wide_range_bar(high, low, MDAYS)).where(close.notna(), np.nan).diff()

def f32_divd_336_rsi_div_x_narrow_range_bar_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today's range < 0.5 × 21d-mean (compression at top)."""
    return (_rsi_div_flag(close) * _is_narrow_range_bar(high, low, MDAYS)).where(close.notna(), np.nan).diff()

def f32_divd_337_rsi_div_x_gravestone_doji_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND gravestone doji pattern fires."""
    return (_rsi_div_flag(close) * _is_gravestone_doji(open, close, high, low)).where(close.notna(), np.nan).diff()

def f32_divd_338_rsi_div_x_close_in_lower_quartile_of_range_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND close in lower 25% of today's bar range."""
    rng = (high - low).replace(0, np.nan)
    close_pos = _safe_div(close - low, rng)
    return (_rsi_div_flag(close) * (close_pos < 0.25).astype(float)).where(close.notna(), np.nan).diff()

def f32_divd_339_rsi_div_x_outside_down_bar_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today's high > prior high AND low < prior low AND close < open (outside-bar bearish)."""
    outside_down = ((high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1))).astype(float)
    return (_rsi_div_flag(close) * outside_down).where(close.notna(), np.nan).diff()

def f32_divd_340_rsi_div_x_close_below_prior_low_indicator_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today's close < prior low (breakdown confirmation)."""
    return (_rsi_div_flag(close) * (close < low.shift(1)).astype(float)).where(close.notna(), np.nan).diff()

def f32_divd_341_rsi14_shift_div_5d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs RSI14, 5d lookback (weekly horizon)."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), WDAYS).diff()

def f32_divd_342_rsi14_shift_div_8d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs RSI14, 8d lookback (Fibonacci-13 family)."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), 8).diff()

def f32_divd_343_rsi14_shift_div_13d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs RSI14, 13d lookback."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), 13).diff()

def f32_divd_344_rsi14_shift_div_34d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs RSI14, 34d lookback (Fibonacci horizon)."""
    return _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), 34).diff()

def f32_divd_345_macdline_shift_div_5d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs MACD line, 5d lookback."""
    return _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), WDAYS).diff()

def f32_divd_346_macdhist_shift_div_5d_d1(close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs MACD histogram, 5d lookback."""
    return _shift_div_bearish_indicator(close, _macd_hist(close, 12, 26, 9), WDAYS).diff()

def f32_divd_347_obv_shift_div_5d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs OBV, 5d lookback."""
    return _shift_div_bearish_indicator(close, _obv(close, volume), WDAYS).diff()

def f32_divd_348_obv_shift_div_8d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs OBV, 8d lookback."""
    return _shift_div_bearish_indicator(close, _obv(close, volume), 8).diff()

def f32_divd_349_mfi_shift_div_5d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs MFI, 5d lookback."""
    return _shift_div_bearish_indicator(close, _mfi(high, low, close, volume, 14), WDAYS).diff()

def f32_divd_350_stochk_shift_div_5d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Two-point bearish divergence — close vs Stoch %K, 5d lookback."""
    return _shift_div_bearish_indicator(close, _stoch_k(high, low, close, 14), WDAYS).diff()

def f32_divd_351_rsi_div_event_ema_count_21d_d1(close: pd.Series) -> pd.Series:
    """EMA-21d weighted count of RSI 21d-shift-div events (recent weighted heavier)."""
    flag = _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    return _ema(flag, MDAYS).diff()

def f32_divd_352_rsi_div_event_ema_count_63d_d1(close: pd.Series) -> pd.Series:
    """EMA-63d weighted count of RSI 21d-shift-div events."""
    flag = _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    return _ema(flag, QDAYS).diff()

def f32_divd_353_macdline_div_event_ema_count_63d_d1(close: pd.Series) -> pd.Series:
    """EMA-63d weighted count of MACD-line 21d-shift-div events."""
    flag = _shift_div_bearish_indicator(close, _macd_line(close, 12, 26), MDAYS).fillna(0)
    return _ema(flag, QDAYS).diff()

def f32_divd_354_obv_div_event_ema_count_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA-63d weighted count of OBV 21d-shift-div events."""
    flag = _shift_div_bearish_indicator(close, _obv(close, volume), MDAYS).fillna(0)
    return _ema(flag, QDAYS).diff()

def f32_divd_355_rsi_div_magnitude_ema_21d_d1(close: pd.Series) -> pd.Series:
    """EMA-21d of RSI 21d-shift-div magnitude (recent magnitude weighted heavier)."""
    rsi = _rsi_wilder(close, 14)
    pp = close.shift(MDAYS)
    op = rsi.shift(MDAYS)
    pxch = _safe_div(close - pp, pp.abs())
    flag = (close > pp) & (rsi < op)
    mag = pxch.where(flag, 0.0)
    return _ema(mag.fillna(0), MDAYS).diff()

def f32_divd_356_rsi_div_magnitude_ema_63d_d1(close: pd.Series) -> pd.Series:
    """EMA-63d of RSI 21d-shift-div magnitude."""
    rsi = _rsi_wilder(close, 14)
    pp = close.shift(MDAYS)
    op = rsi.shift(MDAYS)
    pxch = _safe_div(close - pp, pp.abs())
    flag = (close > pp) & (rsi < op)
    mag = pxch.where(flag, 0.0)
    return _ema(mag.fillna(0), QDAYS).diff()

def f32_divd_357_macdhist_div_magnitude_ema_21d_d1(close: pd.Series) -> pd.Series:
    """EMA-21d of MACD-hist 21d-shift-div magnitude."""
    mh = _macd_hist(close, 12, 26, 9)
    pp = close.shift(MDAYS)
    op = mh.shift(MDAYS)
    pxch = _safe_div(close - pp, pp.abs())
    flag = (close > pp) & (mh < op)
    mag = pxch.where(flag, 0.0)
    return _ema(mag.fillna(0), MDAYS).diff()

def f32_divd_358_obv_div_magnitude_ema_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA-63d of OBV 21d-shift-div magnitude."""
    o = _obv(close, volume)
    pp = close.shift(MDAYS)
    op = o.shift(MDAYS)
    pxch = _safe_div(close - pp, pp.abs())
    flag = (close > pp) & (o < op)
    mag = pxch.where(flag, 0.0)
    return _ema(mag.fillna(0), QDAYS).diff()

def f32_divd_359_rsi_div_half_life_decayed_recency_d1(close: pd.Series) -> pd.Series:
    """Recency-weighted age: 0.5^(bars-since/3) for last RSI 21d-shift-div — half-life 3 bars (very recent emphasis)."""
    flag = _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    idx = np.arange(len(flag))
    last = np.where(flag.values > 0, idx, np.nan)
    last_ff = pd.Series(last, index=flag.index).ffill()
    age = pd.Series(idx, index=flag.index) - last_ff
    return (0.5 ** (age / 3.0)).diff()

def f32_divd_360_rsi_div_half_life_decayed_21d_recency_d1(close: pd.Series) -> pd.Series:
    """Recency-weighted age: 0.5^(bars-since/21) for last RSI 21d-shift-div — half-life 21 bars."""
    flag = _shift_div_bearish_indicator(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    idx = np.arange(len(flag))
    last = np.where(flag.values > 0, idx, np.nan)
    last_ff = pd.Series(last, index=flag.index).ffill()
    age = pd.Series(idx, index=flag.index) - last_ff
    return (0.5 ** (age / float(MDAYS))).diff()

def f32_divd_361_rsi_div_on_top_decile_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish slope-div fires AND today's volume is in trailing-252d top decile."""
    div = _rsi_div_flag(close)
    vrk = _pct_rank(volume, YDAYS)
    return (div * (vrk >= 0.9).astype(float)).where(div.notna() & vrk.notna(), np.nan).diff()

def f32_divd_362_rsi_div_on_bottom_decile_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish slope-div fires AND today's volume is in trailing-252d bottom decile (suspect div)."""
    div = _rsi_div_flag(close)
    vrk = _pct_rank(volume, YDAYS)
    return (div * (vrk <= 0.1).astype(float)).where(div.notna() & vrk.notna(), np.nan).diff()

def f32_divd_363_macdline_div_on_top_decile_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when MACD-line 63d bearish div fires AND today's volume in top decile of 252d."""
    div = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    vrk = _pct_rank(volume, YDAYS)
    return (div * (vrk >= 0.9).astype(float)).where(div.notna() & vrk.notna(), np.nan).diff()

def f32_divd_364_obv_div_on_top_decile_volume_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 63d bearish div fires AND today's volume in top decile of 252d."""
    div = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0).astype(float)
    vrk = _pct_rank(volume, YDAYS)
    return (div * (vrk >= 0.9).astype(float)).where(div.notna() & vrk.notna(), np.nan).diff()

def f32_divd_365_mfi_div_on_top_decile_volume_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when MFI 63d bearish div fires AND today's volume in top decile of 252d."""
    div = (_slope_div_sign(close, _mfi(high, low, close, volume, 14), QDAYS) > 0).astype(float)
    vrk = _pct_rank(volume, YDAYS)
    return (div * (vrk >= 0.9).astype(float)).where(div.notna() & vrk.notna(), np.nan).diff()

def f32_divd_366_rsi_div_on_rising_volume_trend_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div fires AND 21d-volume-slope > 0 (rising volume regime)."""
    div = _rsi_div_flag(close)
    v_slope = _rolling_slope(volume, MDAYS)
    return (div * (v_slope > 0).astype(float)).where(div.notna() & v_slope.notna(), np.nan).diff()

def f32_divd_367_rsi_div_on_falling_volume_trend_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div fires AND 21d-volume-slope < 0 (vol-dryup regime)."""
    div = _rsi_div_flag(close)
    v_slope = _rolling_slope(volume, MDAYS)
    return (div * (v_slope < 0).astype(float)).where(div.notna() & v_slope.notna(), np.nan).diff()

def f32_divd_368_rsi_div_on_5d_vol_expansion_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div fires AND 5d-volume-mean > 1.5 × 63d-volume-mean."""
    div = _rsi_div_flag(close)
    v5 = volume.rolling(WDAYS, min_periods=1).mean()
    v63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    expand = (v5 > 1.5 * v63).astype(float)
    return (div * expand).where(div.notna() & expand.notna(), np.nan).diff()

def f32_divd_369_rsi_div_on_21d_vol_dryup_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div fires AND 21d-volume-mean < 0.7 × 63d-volume-mean."""
    div = _rsi_div_flag(close)
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    dryup = (v21 < 0.7 * v63).astype(float)
    return (div * dryup).where(div.notna() & dryup.notna(), np.nan).diff()

def f32_divd_370_rsi_div_on_dollar_vol_top_decile_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND dollar-volume in 252d top decile."""
    div = _rsi_div_flag(close)
    dvol = close * volume
    dr = _pct_rank(dvol, YDAYS)
    return (div * (dr >= 0.9).astype(float)).where(div.notna() & dr.notna(), np.nan).diff()

def f32_divd_371_rsi_div_on_dollar_vol_bottom_decile_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND dollar-volume in 252d bottom decile (low-conviction div)."""
    div = _rsi_div_flag(close)
    dvol = close * volume
    dr = _pct_rank(dvol, YDAYS)
    return (div * (dr <= 0.1).astype(float)).where(div.notna() & dr.notna(), np.nan).diff()

def f32_divd_372_rsi_div_on_highest_vol_of_21d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND today's volume == 21d-trailing-max (peak-volume div)."""
    div = _rsi_div_flag(close)
    is_max = (volume == volume.rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    return (div * is_max).where(div.notna() & is_max.notna(), np.nan).diff()

def f32_divd_373_macdline_div_on_lowest_vol_of_21d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when MACD-line 63d bearish div AND today's volume == 21d-trailing-min (no-confirmation div)."""
    div = (_slope_div_sign(close, _macd_line(close, 12, 26), QDAYS) > 0).astype(float)
    is_min = (volume == volume.rolling(MDAYS, min_periods=WDAYS).min()).astype(float)
    return (div * is_min).where(div.notna() & is_min.notna(), np.nan).diff()

def f32_divd_374_obv_div_on_vol_below_21d_mean_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 63d bearish div AND today's vol < 21d-mean."""
    div = (_slope_div_sign(close, _obv(close, volume), QDAYS) > 0).astype(float)
    below = (volume < volume.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float)
    return (div * below).where(div.notna() & below.notna(), np.nan).diff()

def f32_divd_375_rsi_div_on_vol_zscore_above_2_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when RSI 63d bearish div AND vol z-score(63) > 2 (extreme-vol div)."""
    div = _rsi_div_flag(close)
    vz = _rolling_zscore(volume, QDAYS)
    return (div * (vz > 2.0).astype(float)).where(div.notna() & vz.notna(), np.nan).diff()
DIVERGENCE_DETECTION_D1_REGISTRY_301_375 = {'f32_divd_301_welch_t_stat_div_rsi14_63d_d1': {'inputs': ['close'], 'func': f32_divd_301_welch_t_stat_div_rsi14_63d_d1}, 'f32_divd_302_welch_t_stat_div_macdline_63d_d1': {'inputs': ['close'], 'func': f32_divd_302_welch_t_stat_div_macdline_63d_d1}, 'f32_divd_303_welch_t_stat_div_macdhist_63d_d1': {'inputs': ['close'], 'func': f32_divd_303_welch_t_stat_div_macdhist_63d_d1}, 'f32_divd_304_welch_t_stat_div_obv_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_304_welch_t_stat_div_obv_63d_d1}, 'f32_divd_305_welch_t_stat_div_adline_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_305_welch_t_stat_div_adline_63d_d1}, 'f32_divd_306_welch_t_stat_div_stochk_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_306_welch_t_stat_div_stochk_63d_d1}, 'f32_divd_307_welch_t_stat_div_mfi_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_307_welch_t_stat_div_mfi_63d_d1}, 'f32_divd_308_welch_t_stat_div_cci_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_308_welch_t_stat_div_cci_63d_d1}, 'f32_divd_309_welch_t_stat_div_trix_63d_d1': {'inputs': ['close'], 'func': f32_divd_309_welch_t_stat_div_trix_63d_d1}, 'f32_divd_310_welch_t_stat_div_tsi_63d_d1': {'inputs': ['close'], 'func': f32_divd_310_welch_t_stat_div_tsi_63d_d1}, 'f32_divd_311_welch_t_stat_div_roc12_63d_d1': {'inputs': ['close'], 'func': f32_divd_311_welch_t_stat_div_roc12_63d_d1}, 'f32_divd_312_welch_t_stat_div_williamsr_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_312_welch_t_stat_div_williamsr_63d_d1}, 'f32_divd_313_welch_t_stat_div_cmf_63d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_313_welch_t_stat_div_cmf_63d_d1}, 'f32_divd_314_welch_t_stat_div_uo_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_314_welch_t_stat_div_uo_63d_d1}, 'f32_divd_315_welch_t_stat_div_rsi14_252d_d1': {'inputs': ['close'], 'func': f32_divd_315_welch_t_stat_div_rsi14_252d_d1}, 'f32_divd_316_rsi_div_dwell_time_21d_d1': {'inputs': ['close'], 'func': f32_divd_316_rsi_div_dwell_time_21d_d1}, 'f32_divd_317_macdline_div_dwell_time_21d_d1': {'inputs': ['close'], 'func': f32_divd_317_macdline_div_dwell_time_21d_d1}, 'f32_divd_318_macdhist_div_dwell_time_21d_d1': {'inputs': ['close'], 'func': f32_divd_318_macdhist_div_dwell_time_21d_d1}, 'f32_divd_319_obv_div_dwell_time_21d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_319_obv_div_dwell_time_21d_d1}, 'f32_divd_320_adline_div_dwell_time_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_320_adline_div_dwell_time_21d_d1}, 'f32_divd_321_stochk_div_dwell_time_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_321_stochk_div_dwell_time_21d_d1}, 'f32_divd_322_mfi_div_dwell_time_21d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_322_mfi_div_dwell_time_21d_d1}, 'f32_divd_323_cci_div_dwell_time_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_323_cci_div_dwell_time_21d_d1}, 'f32_divd_324_trix_div_dwell_time_21d_d1': {'inputs': ['close'], 'func': f32_divd_324_trix_div_dwell_time_21d_d1}, 'f32_divd_325_tsi_div_dwell_time_21d_d1': {'inputs': ['close'], 'func': f32_divd_325_tsi_div_dwell_time_21d_d1}, 'f32_divd_326_rsi_div_x_doji_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_326_rsi_div_x_doji_indicator_d1}, 'f32_divd_327_rsi_div_x_shooting_star_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_327_rsi_div_x_shooting_star_indicator_d1}, 'f32_divd_328_rsi_div_x_hanging_man_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_328_rsi_div_x_hanging_man_indicator_d1}, 'f32_divd_329_rsi_div_x_bearish_engulfing_indicator_d1': {'inputs': ['open', 'close'], 'func': f32_divd_329_rsi_div_x_bearish_engulfing_indicator_d1}, 'f32_divd_330_rsi_div_x_dark_cloud_cover_indicator_d1': {'inputs': ['open', 'close', 'high'], 'func': f32_divd_330_rsi_div_x_dark_cloud_cover_indicator_d1}, 'f32_divd_331_rsi_div_x_3_black_crows_indicator_d1': {'inputs': ['open', 'close'], 'func': f32_divd_331_rsi_div_x_3_black_crows_indicator_d1}, 'f32_divd_332_rsi_div_x_evening_star_indicator_d1': {'inputs': ['open', 'close'], 'func': f32_divd_332_rsi_div_x_evening_star_indicator_d1}, 'f32_divd_333_rsi_div_x_bearish_harami_indicator_d1': {'inputs': ['open', 'close'], 'func': f32_divd_333_rsi_div_x_bearish_harami_indicator_d1}, 'f32_divd_334_rsi_div_x_gap_up_bar_indicator_d1': {'inputs': ['open', 'high', 'close'], 'func': f32_divd_334_rsi_div_x_gap_up_bar_indicator_d1}, 'f32_divd_335_rsi_div_x_wide_range_bar_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_335_rsi_div_x_wide_range_bar_indicator_d1}, 'f32_divd_336_rsi_div_x_narrow_range_bar_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_336_rsi_div_x_narrow_range_bar_indicator_d1}, 'f32_divd_337_rsi_div_x_gravestone_doji_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_337_rsi_div_x_gravestone_doji_indicator_d1}, 'f32_divd_338_rsi_div_x_close_in_lower_quartile_of_range_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_338_rsi_div_x_close_in_lower_quartile_of_range_indicator_d1}, 'f32_divd_339_rsi_div_x_outside_down_bar_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_339_rsi_div_x_outside_down_bar_indicator_d1}, 'f32_divd_340_rsi_div_x_close_below_prior_low_indicator_d1': {'inputs': ['close', 'low'], 'func': f32_divd_340_rsi_div_x_close_below_prior_low_indicator_d1}, 'f32_divd_341_rsi14_shift_div_5d_d1': {'inputs': ['close'], 'func': f32_divd_341_rsi14_shift_div_5d_d1}, 'f32_divd_342_rsi14_shift_div_8d_d1': {'inputs': ['close'], 'func': f32_divd_342_rsi14_shift_div_8d_d1}, 'f32_divd_343_rsi14_shift_div_13d_d1': {'inputs': ['close'], 'func': f32_divd_343_rsi14_shift_div_13d_d1}, 'f32_divd_344_rsi14_shift_div_34d_d1': {'inputs': ['close'], 'func': f32_divd_344_rsi14_shift_div_34d_d1}, 'f32_divd_345_macdline_shift_div_5d_d1': {'inputs': ['close'], 'func': f32_divd_345_macdline_shift_div_5d_d1}, 'f32_divd_346_macdhist_shift_div_5d_d1': {'inputs': ['close'], 'func': f32_divd_346_macdhist_shift_div_5d_d1}, 'f32_divd_347_obv_shift_div_5d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_347_obv_shift_div_5d_d1}, 'f32_divd_348_obv_shift_div_8d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_348_obv_shift_div_8d_d1}, 'f32_divd_349_mfi_shift_div_5d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_349_mfi_shift_div_5d_d1}, 'f32_divd_350_stochk_shift_div_5d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_350_stochk_shift_div_5d_d1}, 'f32_divd_351_rsi_div_event_ema_count_21d_d1': {'inputs': ['close'], 'func': f32_divd_351_rsi_div_event_ema_count_21d_d1}, 'f32_divd_352_rsi_div_event_ema_count_63d_d1': {'inputs': ['close'], 'func': f32_divd_352_rsi_div_event_ema_count_63d_d1}, 'f32_divd_353_macdline_div_event_ema_count_63d_d1': {'inputs': ['close'], 'func': f32_divd_353_macdline_div_event_ema_count_63d_d1}, 'f32_divd_354_obv_div_event_ema_count_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_354_obv_div_event_ema_count_63d_d1}, 'f32_divd_355_rsi_div_magnitude_ema_21d_d1': {'inputs': ['close'], 'func': f32_divd_355_rsi_div_magnitude_ema_21d_d1}, 'f32_divd_356_rsi_div_magnitude_ema_63d_d1': {'inputs': ['close'], 'func': f32_divd_356_rsi_div_magnitude_ema_63d_d1}, 'f32_divd_357_macdhist_div_magnitude_ema_21d_d1': {'inputs': ['close'], 'func': f32_divd_357_macdhist_div_magnitude_ema_21d_d1}, 'f32_divd_358_obv_div_magnitude_ema_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_358_obv_div_magnitude_ema_63d_d1}, 'f32_divd_359_rsi_div_half_life_decayed_recency_d1': {'inputs': ['close'], 'func': f32_divd_359_rsi_div_half_life_decayed_recency_d1}, 'f32_divd_360_rsi_div_half_life_decayed_21d_recency_d1': {'inputs': ['close'], 'func': f32_divd_360_rsi_div_half_life_decayed_21d_recency_d1}, 'f32_divd_361_rsi_div_on_top_decile_volume_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_361_rsi_div_on_top_decile_volume_indicator_d1}, 'f32_divd_362_rsi_div_on_bottom_decile_volume_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_362_rsi_div_on_bottom_decile_volume_indicator_d1}, 'f32_divd_363_macdline_div_on_top_decile_volume_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_363_macdline_div_on_top_decile_volume_indicator_d1}, 'f32_divd_364_obv_div_on_top_decile_volume_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_364_obv_div_on_top_decile_volume_indicator_d1}, 'f32_divd_365_mfi_div_on_top_decile_volume_indicator_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f32_divd_365_mfi_div_on_top_decile_volume_indicator_d1}, 'f32_divd_366_rsi_div_on_rising_volume_trend_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_366_rsi_div_on_rising_volume_trend_indicator_d1}, 'f32_divd_367_rsi_div_on_falling_volume_trend_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_367_rsi_div_on_falling_volume_trend_indicator_d1}, 'f32_divd_368_rsi_div_on_5d_vol_expansion_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_368_rsi_div_on_5d_vol_expansion_indicator_d1}, 'f32_divd_369_rsi_div_on_21d_vol_dryup_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_369_rsi_div_on_21d_vol_dryup_indicator_d1}, 'f32_divd_370_rsi_div_on_dollar_vol_top_decile_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_370_rsi_div_on_dollar_vol_top_decile_indicator_d1}, 'f32_divd_371_rsi_div_on_dollar_vol_bottom_decile_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_371_rsi_div_on_dollar_vol_bottom_decile_indicator_d1}, 'f32_divd_372_rsi_div_on_highest_vol_of_21d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_372_rsi_div_on_highest_vol_of_21d_indicator_d1}, 'f32_divd_373_macdline_div_on_lowest_vol_of_21d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_373_macdline_div_on_lowest_vol_of_21d_indicator_d1}, 'f32_divd_374_obv_div_on_vol_below_21d_mean_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_374_obv_div_on_vol_below_21d_mean_indicator_d1}, 'f32_divd_375_rsi_div_on_vol_zscore_above_2_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_375_rsi_div_on_vol_zscore_above_2_indicator_d1}}