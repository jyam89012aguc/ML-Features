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


def _ema_volume_intensity(volume: pd.Series, span: int) -> pd.Series:
    base = volume.rolling(span * 4, min_periods=span).mean()
    shock = (volume - base).clip(lower=0.0)
    return shock.ewm(span=span, min_periods=max(span // 3, 2), adjust=False).mean()


def _corwin_schultz_spread_proxy(high: pd.Series, low: pd.Series) -> pd.Series:
    lh = _safe_log(high) - _safe_log(low)
    beta = (lh ** 2) + (lh.shift(1) ** 2)
    beta_pit = (lh.shift(1) ** 2) + (lh ** 2)
    pair_high = pd.concat([high.shift(1), high], axis=1).max(axis=1)
    pair_low = pd.concat([low.shift(1), low], axis=1).min(axis=1)
    gamma = (_safe_log(pair_high) - _safe_log(pair_low)) ** 2
    denom_a = 3.0 - 2.0 * np.sqrt(2.0)
    alpha_num = np.sqrt(2.0 * beta_pit) - np.sqrt(beta_pit)
    alpha = (alpha_num / denom_a) - np.sqrt(gamma / denom_a)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0.0)


def f20_vdah_151_vsa_no_demand_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    return (up & narrow & near_high & vol_low).astype(float)


def f20_vdah_152_vsa_no_demand_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    flag = (up & narrow & near_high & vol_low).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_153_vsa_no_demand_streak(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    cond = up & narrow & near_high & vol_low
    return _consecutive_true_streak(cond).astype(float)


def f20_vdah_154_vsa_no_supply_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    dn = close < close.shift(1)
    narrow = tr < 0.5 * atr
    near_low = pos <= 0.4
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    return (dn & narrow & near_low & vol_low).astype(float)


def f20_vdah_155_vsa_test_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_low = low.shift(1); prior_high = high.shift(1)
    dipped = low < prior_low
    closed_back = (close >= prior_low) & (close <= prior_high)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_low = volume < med
    return (dipped & closed_back & vol_low).astype(float)


def f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    dn = close < close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    near_low = pos <= 0.4
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    nd = (up & narrow & near_high & vol_low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ns = (dn & narrow & near_low & vol_low).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nd, ns + 1.0)


def f20_vdah_157_vsa_no_demand_gated_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    range_pos = _safe_div(close - rmin, rmax - rmin)
    cond = up & narrow & near_high & vol_low & (range_pos >= 0.90)
    return cond.astype(float)


def f20_vdah_158_vsa_no_demand_at_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    range_pos = _safe_div(close - rmin, rmax - rmin)
    flag = (up & narrow & near_high & vol_low & (range_pos >= 0.90)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos >= 0.6
    vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    flag = (up & narrow & near_high & vol_low).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin).fillna(0.0)
    return (flag * (rp ** 2)).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_160_vsa_pseudo_supply_test_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_low = low.shift(1); prior_high = high.shift(1)
    dipped = low < prior_low
    closed_back = (close >= prior_low) & (close <= prior_high)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_low = volume < med
    flag = (dipped & closed_back & vol_low).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_161_vsa_upthrust_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high & closed_weak & vol_high).astype(float)


def f20_vdah_162_vsa_upthrust_at_252d_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    new_high_252 = high > rmax252
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high_252 & closed_weak & vol_high).astype(float)


def f20_vdah_163_vsa_upthrust_after_distribution_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax252 = high.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    rmin252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    new_high = high > rmax252
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    range_pos = _safe_div(close - rmin252, rmax252 - rmin252)
    in_dist = (range_pos >= 0.90).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    ut = (new_high & closed_weak & vol_high).astype(float)
    return ut * in_dist.fillna(0.0)


def f20_vdah_164_count_upthrusts_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    return (new_high & closed_weak & vol_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_165_upthrust_max_volume_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    cond = new_high & closed_weak & vol_high
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return z.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_166_bars_since_last_upthrust_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    flag = (new_high & closed_weak & vol_high).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_167_upthrust_with_followthrough_failure_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = new_high & closed_weak & vol_high
    ut_low = low.where(ut, np.nan).ffill()
    days_since = (~ut).astype(int).groupby(ut.cumsum()).cumsum()
    return ((days_since <= 5) & (close < ut_low.shift(1))).astype(float)


def f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    cond = new_high & closed_weak & vol_high
    atr = _atr(high, low, close, n=MDAYS)
    ratio = _safe_div(volume, atr)
    return ratio.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_169_upthrust_followed_by_lower_high_within_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = new_high & closed_weak & vol_high
    ut_high = high.where(ut, np.nan).ffill()
    days_since = (~ut).astype(int).groupby(ut.cumsum()).cumsum()
    fail_event = ((days_since <= 5) & (high < ut_high.shift(1))).astype(float)
    return fail_event.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_170_double_upthrust_indicator_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = (new_high & closed_weak & vol_high).astype(float)
    prior_ut = ut.shift(1).rolling(WDAYS, min_periods=1).sum()
    return ((ut > 0) & (prior_ut > 0)).astype(float)


def f20_vdah_171_stalling_bar_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_high = volume > 1.5 * med21
    flat = pc < 0.005
    return (flat & vol_high).astype(float)


def f20_vdah_172_stalling_bar_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    flag = ((pc < 0.005) & (volume > 1.5 * med21)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_173_stalling_bar_at_252d_high_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change().abs()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((pc < 0.005) & (volume > 1.5 * med21) & (high >= rmax)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_174_churn_effort_to_result_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    res = close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_175_churn_effort_to_result_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    res = close.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_176_churn_effort_to_range_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    res = (high - low).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(eff, res)


def f20_vdah_177_top_decile_dwell_with_churn_indicator_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    flag = ((rp >= 0.90) & (volume > 2.0 * med21) & (pc < 0.005)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_178_churn_intensity_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(volume, close.diff().abs()), YDAYS)


def f20_vdah_179_max_churn_streak_at_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    cond = (rp >= 0.90) & (volume > 1.5 * med21) & (pc < 0.01)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_180_churn_to_breakout_failure_ratio_252d(high: pd.Series, volume: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rp = _safe_div(close - rmin, rmax - rmin)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    pc = close.pct_change().abs()
    churn = ((rp >= 0.90) & (volume > 1.5 * med21) & (pc < 0.01)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    new_h = (high >= rmax).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(churn, new_h + 1.0)


def f20_vdah_181_effort_minus_result_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff_z = _rolling_zscore(_safe_log(volume), MDAYS)
    res_z = _rolling_zscore(close.diff().abs(), MDAYS)
    return eff_z - res_z


def f20_vdah_182_effort_minus_result_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff_z = _rolling_zscore(_safe_log(volume), QDAYS)
    res_z = _rolling_zscore(close.diff().abs(), QDAYS)
    return eff_z - res_z


def f20_vdah_183_effort_minus_result_at_252d_high_only(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    eff_z = _rolling_zscore(_safe_log(volume), MDAYS)
    res_z = _rolling_zscore(close.diff().abs(), MDAYS)
    diff = eff_z - res_z
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return diff.where(high >= rmax, np.nan)


def f20_vdah_184_effort_result_corr_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _safe_log(volume).rolling(YDAYS, min_periods=QDAYS).corr(close.diff().abs())


def f20_vdah_185_volume_per_unit_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(volume, high - low), YDAYS)


def f20_vdah_186_count_high_effort_low_result_bars_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    pc = close.pct_change().abs()
    return ((z > 1.0) & (pc < 0.005)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_187_high_effort_low_result_max_streak_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    pc = close.pct_change().abs()
    cond = (z > 1.0) & (pc < 0.005)
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f20_vdah_188_effort_result_ratio_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _rolling_pct_rank(_safe_div(volume, close.diff().abs()), YDAYS)


def f20_vdah_189_volume_excess_when_range_compressed_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    rng = high - low
    q20 = _rolling_quantile(rng, YDAYS, 0.20)
    flag = rng <= q20
    return z.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_190_effort_result_decoupling_index_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    c = _safe_log(volume).rolling(YDAYS, min_periods=QDAYS).corr(close.diff().abs())
    return (1.0 - c).clip(lower=-1.0, upper=2.0)


def f20_vdah_191_weak_rally_after_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float)


def f20_vdah_192_lpsy_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_193_post_drawdown_rally_volume_decay_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    dn = close < close.shift(1)
    up_v = volume.where(up, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    dn_v = volume.where(dn, np.nan).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(up_v, dn_v)


def f20_vdah_194_post_peak_rally_low_vol_strength_index(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    past_peak = rmax.shift(QDAYS) >= rmax  # within last 63d, an earlier 252d high existed
    up = close > close.shift(1)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    contrib = _safe_div(close.diff(), med21)
    return contrib.where(up & past_peak, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_195_lpsy_failure_to_retake_high_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    rally_5d = close > close.shift(WDAYS)
    fail = close < h63
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (rally_5d & fail & vol_low).astype(float)


def f20_vdah_196_count_lpsy_failure_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    rally_5d = close > close.shift(WDAYS)
    fail = close < h63
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (rally_5d & fail & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_197_rally_volume_zscore_post_252d_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = high >= rmax
    bars_since_peak = (~is_peak).astype(int).groupby(is_peak.cumsum()).cumsum()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    up = close > close.shift(1)
    flag = up & (bars_since_peak > QDAYS)
    return z.where(flag, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()


def f20_vdah_198_lpsy_lower_high_pattern_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return (h21 < h21.shift(MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_199_post_distribution_rally_failure_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    lpsy = (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    new_high = high > rmax21
    pos = _safe_div(close - low, high - low)
    closed_weak = pos <= 0.5
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    vol_high = volume > med
    ut = (new_high & closed_weak & vol_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS)
    pos2 = _safe_div(close - low, high - low)
    up = close > close.shift(1)
    narrow = tr < 0.5 * atr
    near_high = pos2 >= 0.6
    nd_vol_low = (volume < volume.shift(1)) & (volume < volume.shift(2))
    nd = (up & narrow & near_high & nd_vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return lpsy + ut + nd


def f20_vdah_200_lpsy_dwell_score_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pc_21 = _safe_log(close) - _safe_log(close.rolling(MDAYS, min_periods=WDAYS).max().shift(WDAYS))
    breakdown = pc_21 < np.log(0.95)
    rally_5d = close > close.shift(WDAYS)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    vol_low = volume.rolling(WDAYS, min_periods=2).mean() < med21
    return (breakdown & rally_5d & vol_low).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_201_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    return ((pc < -0.002) & (volume > volume.shift(1))).astype(float)


def f20_vdah_202_distribution_day_count_25d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(25, min_periods=10).sum()


def f20_vdah_203_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_204_strict_distribution_day_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.01) & (volume > 1.5 * med)).astype(float)


def f20_vdah_205_strict_distribution_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((pc < -0.01) & (volume > 1.5 * med)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_206_distribution_to_accumulation_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    dd = ((pc < -0.002) & (volume > volume.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    ad = ((pc > 0.002) & (volume > volume.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dd, ad + 1.0)


def f20_vdah_207_consec_distribution_days_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    cond = (pc < -0.002) & (volume > volume.shift(1))
    return _consecutive_true_streak(cond).astype(float)


def f20_vdah_208_distribution_day_severity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    severity = pc.abs() * _safe_div(volume, med21)
    flag = (pc < -0.002) & (volume > volume.shift(1))
    return severity.where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f20_vdah_209_distribution_day_clustered_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    pc = close.pct_change()
    flag = ((pc < -0.002) & (volume > volume.shift(1))).astype(float)
    cnt = flag.rolling(25, min_periods=10).sum()
    return (cnt >= 4).astype(float)


def f20_vdah_210_distribution_day_after_252d_high_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    recent_peak = (high >= rmax).astype(float).rolling(MDAYS, min_periods=WDAYS).max() > 0
    pc = close.pct_change()
    dd = (pc < -0.002) & (volume > volume.shift(1)) & recent_peak
    return dd.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f20_vdah_211_poc_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _poc(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        cv = c[mask].values; vv = v[mask].values
        lo, hi = cv.min(), cv.max()
        if hi <= lo:
            return float(cv.mean())
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        return float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _poc(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_212_log_dist_close_to_poc_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _poc(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        cv = c[mask].values; vv = v[mask].values
        lo, hi = cv.min(), cv.max()
        if hi <= lo:
            return float(cv.mean())
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        return float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
    poc = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        poc.iloc[i] = _poc(range(i - YDAYS + 1, i + 1))
    return _safe_log(close) - _safe_log(poc)


def f20_vdah_213_value_area_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.85 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_214_value_area_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _val(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.15 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _val(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_215_log_dist_close_to_vah_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        thr = 0.85 * tot
        i_v = int(np.searchsorted(cum, thr))
        i_v = min(i_v, cv.size - 1)
        return float(cv[i_v])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return _safe_log(close) - _safe_log(vah)


def f20_vdah_216_log_value_area_width_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vp(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return (np.nan, np.nan)
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return (np.nan, np.nan)
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        val_i = min(int(np.searchsorted(cum, 0.15 * tot)), cv.size - 1)
        return (float(cv[vah_i]), float(cv[val_i]))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vh, vl = _vp(range(i - YDAYS + 1, i + 1))
        if vl is not None and vh is not None and vl > 0 and vh > 0:
            out.iloc[i] = float(np.log(vh) - np.log(vl))
    return out


def f20_vdah_217_single_print_dwell_above_vah_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        return float(cv[vah_i])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    return (close > vah).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f20_vdah_218_poc_age_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _age(idx):
        v = volume.iloc[idx]
        if v.notna().sum() < 30:
            return np.nan
        vv = v.values
        return float(len(vv) - 1 - int(np.argmax(vv)))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _age(range(i - YDAYS + 1, i + 1))
    return out


def f20_vdah_219_volume_above_vah_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vah(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return np.nan
        order = np.argsort(c[mask].values)
        cv = c[mask].values[order]; vv = v[mask].values[order]
        cum = np.cumsum(vv)
        tot = cum[-1]
        if tot <= 0:
            return np.nan
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv.size - 1)
        return float(cv[vah_i])
    vah = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        vah.iloc[i] = _vah(range(i - YDAYS + 1, i + 1))
    above = volume.where(close > vah, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(above, tot)


def f20_vdah_220_value_area_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _vp(idx):
        c = close.iloc[idx]; v = volume.iloc[idx]
        mask = c.notna() & v.notna()
        if mask.sum() < 30:
            return (np.nan, np.nan, np.nan)
        cv_arr = c[mask].values; vv_arr = v[mask].values
        lo, hi = cv_arr.min(), cv_arr.max()
        if hi <= lo:
            return (lo, lo, lo)
        bins = np.linspace(lo, hi, 21)
        idx_bin = np.clip(np.digitize(cv_arr, bins) - 1, 0, len(bins) - 2)
        sums = np.bincount(idx_bin, weights=vv_arr, minlength=len(bins) - 1)
        poc_bin = int(np.argmax(sums))
        poc_px = float((bins[poc_bin] + bins[poc_bin + 1]) / 2.0)
        order = np.argsort(cv_arr)
        cv_sorted = cv_arr[order]; vv_sorted = vv_arr[order]
        cum = np.cumsum(vv_sorted)
        tot = cum[-1]
        if tot <= 0:
            return (poc_px, poc_px, poc_px)
        vah_i = min(int(np.searchsorted(cum, 0.85 * tot)), cv_sorted.size - 1)
        val_i = min(int(np.searchsorted(cum, 0.15 * tot)), cv_sorted.size - 1)
        return (poc_px, float(cv_sorted[vah_i]), float(cv_sorted[val_i]))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        poc, vh, vl = _vp(range(i - YDAYS + 1, i + 1))
        if not (np.isnan(poc) or np.isnan(vh) or np.isnan(vl)):
            out.iloc[i] = float((vh - poc) - (poc - vl))
    return out


def f20_vdah_221_hawkes_volume_intensity_21d(volume: pd.Series) -> pd.Series:
    return _ema_volume_intensity(volume, span=MDAYS)


def f20_vdah_222_hawkes_volume_intensity_63d(volume: pd.Series) -> pd.Series:
    return _ema_volume_intensity(volume, span=QDAYS)


def f20_vdah_223_hawkes_volume_decay_ratio_21_to_63(volume: pd.Series) -> pd.Series:
    return _safe_div(_ema_volume_intensity(volume, span=MDAYS), _ema_volume_intensity(volume, span=QDAYS))


def f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90(volume: pd.Series) -> pd.Series:
    inten = _ema_volume_intensity(volume, span=MDAYS)
    q = _rolling_quantile(inten, YDAYS, 0.90)
    flag = (inten > q).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f20_vdah_225_hawkes_volume_intensity_zscore_252d(volume: pd.Series) -> pd.Series:
    return _rolling_zscore(_ema_volume_intensity(volume, span=MDAYS), YDAYS)


def f20_vdah_151_vsa_no_demand_bar_indicator_d1(high, low, close, volume):
    return f20_vdah_151_vsa_no_demand_bar_indicator(high, low, close, volume).diff()


def f20_vdah_152_vsa_no_demand_count_63d_d1(high, low, close, volume):
    return f20_vdah_152_vsa_no_demand_count_63d(high, low, close, volume).diff()


def f20_vdah_153_vsa_no_demand_streak_d1(high, low, close, volume):
    return f20_vdah_153_vsa_no_demand_streak(high, low, close, volume).diff()


def f20_vdah_154_vsa_no_supply_bar_indicator_d1(high, low, close, volume):
    return f20_vdah_154_vsa_no_supply_bar_indicator(high, low, close, volume).diff()


def f20_vdah_155_vsa_test_bar_indicator_d1(high, low, close, volume):
    return f20_vdah_155_vsa_test_bar_indicator(high, low, close, volume).diff()


def f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d_d1(high, low, close, volume):
    return f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d(high, low, close, volume).diff()


def f20_vdah_157_vsa_no_demand_gated_at_high_d1(high, low, close, volume):
    return f20_vdah_157_vsa_no_demand_gated_at_high(high, low, close, volume).diff()


def f20_vdah_158_vsa_no_demand_at_high_count_252d_d1(high, low, close, volume):
    return f20_vdah_158_vsa_no_demand_at_high_count_252d(high, low, close, volume).diff()


def f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high_d1(high, low, close, volume):
    return f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high(high, low, close, volume).diff()


def f20_vdah_160_vsa_pseudo_supply_test_count_252d_d1(high, low, close, volume):
    return f20_vdah_160_vsa_pseudo_supply_test_count_252d(high, low, close, volume).diff()


def f20_vdah_161_vsa_upthrust_indicator_d1(high, low, close, volume):
    return f20_vdah_161_vsa_upthrust_indicator(high, low, close, volume).diff()


def f20_vdah_162_vsa_upthrust_at_252d_high_indicator_d1(high, low, close, volume):
    return f20_vdah_162_vsa_upthrust_at_252d_high_indicator(high, low, close, volume).diff()


def f20_vdah_163_vsa_upthrust_after_distribution_score_d1(high, low, close, volume):
    return f20_vdah_163_vsa_upthrust_after_distribution_score(high, low, close, volume).diff()


def f20_vdah_164_count_upthrusts_252d_d1(high, low, close, volume):
    return f20_vdah_164_count_upthrusts_252d(high, low, close, volume).diff()


def f20_vdah_165_upthrust_max_volume_zscore_252d_d1(high, low, close, volume):
    return f20_vdah_165_upthrust_max_volume_zscore_252d(high, low, close, volume).diff()


def f20_vdah_166_bars_since_last_upthrust_252d_d1(high, low, close, volume):
    return f20_vdah_166_bars_since_last_upthrust_252d(high, low, close, volume).diff()


def f20_vdah_167_upthrust_with_followthrough_failure_indicator_d1(high, low, close, volume):
    return f20_vdah_167_upthrust_with_followthrough_failure_indicator(high, low, close, volume).diff()


def f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean_d1(high, low, close, volume):
    return f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean(high, low, close, volume).diff()


def f20_vdah_169_upthrust_followed_by_lower_high_within_5d_d1(high, low, close, volume):
    return f20_vdah_169_upthrust_followed_by_lower_high_within_5d(high, low, close, volume).diff()


def f20_vdah_170_double_upthrust_indicator_5d_d1(high, low, close, volume):
    return f20_vdah_170_double_upthrust_indicator_5d(high, low, close, volume).diff()


def f20_vdah_171_stalling_bar_indicator_d1(high, low, close, volume):
    return f20_vdah_171_stalling_bar_indicator(high, low, close, volume).diff()


def f20_vdah_172_stalling_bar_count_63d_d1(high, low, close, volume):
    return f20_vdah_172_stalling_bar_count_63d(high, low, close, volume).diff()


def f20_vdah_173_stalling_bar_at_252d_high_count_252d_d1(high, low, close, volume):
    return f20_vdah_173_stalling_bar_at_252d_high_count_252d(high, low, close, volume).diff()


def f20_vdah_174_churn_effort_to_result_ratio_21d_d1(high, low, close, volume):
    return f20_vdah_174_churn_effort_to_result_ratio_21d(high, low, close, volume).diff()


def f20_vdah_175_churn_effort_to_result_ratio_63d_d1(high, low, close, volume):
    return f20_vdah_175_churn_effort_to_result_ratio_63d(high, low, close, volume).diff()


def f20_vdah_176_churn_effort_to_range_ratio_21d_d1(high, low, close, volume):
    return f20_vdah_176_churn_effort_to_range_ratio_21d(high, low, close, volume).diff()


def f20_vdah_177_top_decile_dwell_with_churn_indicator_252d_d1(high, low, close, volume):
    return f20_vdah_177_top_decile_dwell_with_churn_indicator_252d(high, low, close, volume).diff()


def f20_vdah_178_churn_intensity_zscore_252d_d1(high, low, close, volume):
    return f20_vdah_178_churn_intensity_zscore_252d(high, low, close, volume).diff()


def f20_vdah_179_max_churn_streak_at_high_252d_d1(high, low, close, volume):
    return f20_vdah_179_max_churn_streak_at_high_252d(high, low, close, volume).diff()


def f20_vdah_180_churn_to_breakout_failure_ratio_252d_d1(high, volume, low, close):
    return f20_vdah_180_churn_to_breakout_failure_ratio_252d(high, volume, low, close).diff()


def f20_vdah_181_effort_minus_result_zscore_21d_d1(high, low, close, volume):
    return f20_vdah_181_effort_minus_result_zscore_21d(high, low, close, volume).diff()


def f20_vdah_182_effort_minus_result_zscore_63d_d1(high, low, close, volume):
    return f20_vdah_182_effort_minus_result_zscore_63d(high, low, close, volume).diff()


def f20_vdah_183_effort_minus_result_at_252d_high_only_d1(high, low, close, volume):
    return f20_vdah_183_effort_minus_result_at_252d_high_only(high, low, close, volume).diff()


def f20_vdah_184_effort_result_corr_252d_d1(high, low, close, volume):
    return f20_vdah_184_effort_result_corr_252d(high, low, close, volume).diff()


def f20_vdah_185_volume_per_unit_range_zscore_252d_d1(high, low, close, volume):
    return f20_vdah_185_volume_per_unit_range_zscore_252d(high, low, close, volume).diff()


def f20_vdah_186_count_high_effort_low_result_bars_63d_d1(high, low, close, volume):
    return f20_vdah_186_count_high_effort_low_result_bars_63d(high, low, close, volume).diff()


def f20_vdah_187_high_effort_low_result_max_streak_252d_d1(high, low, close, volume):
    return f20_vdah_187_high_effort_low_result_max_streak_252d(high, low, close, volume).diff()


def f20_vdah_188_effort_result_ratio_pct_rank_252d_d1(high, low, close, volume):
    return f20_vdah_188_effort_result_ratio_pct_rank_252d(high, low, close, volume).diff()


def f20_vdah_189_volume_excess_when_range_compressed_252d_d1(high, low, close, volume):
    return f20_vdah_189_volume_excess_when_range_compressed_252d(high, low, close, volume).diff()


def f20_vdah_190_effort_result_decoupling_index_252d_d1(high, low, close, volume):
    return f20_vdah_190_effort_result_decoupling_index_252d(high, low, close, volume).diff()


def f20_vdah_191_weak_rally_after_breakdown_indicator_d1(high, low, close, volume):
    return f20_vdah_191_weak_rally_after_breakdown_indicator(high, low, close, volume).diff()


def f20_vdah_192_lpsy_count_252d_d1(high, low, close, volume):
    return f20_vdah_192_lpsy_count_252d(high, low, close, volume).diff()


def f20_vdah_193_post_drawdown_rally_volume_decay_21d_d1(high, low, close, volume):
    return f20_vdah_193_post_drawdown_rally_volume_decay_21d(high, low, close, volume).diff()


def f20_vdah_194_post_peak_rally_low_vol_strength_index_d1(high, low, close, volume):
    return f20_vdah_194_post_peak_rally_low_vol_strength_index(high, low, close, volume).diff()


def f20_vdah_195_lpsy_failure_to_retake_high_indicator_d1(high, low, close, volume):
    return f20_vdah_195_lpsy_failure_to_retake_high_indicator(high, low, close, volume).diff()


def f20_vdah_196_count_lpsy_failure_252d_d1(high, low, close, volume):
    return f20_vdah_196_count_lpsy_failure_252d(high, low, close, volume).diff()


def f20_vdah_197_rally_volume_zscore_post_252d_high_d1(high, low, close, volume):
    return f20_vdah_197_rally_volume_zscore_post_252d_high(high, low, close, volume).diff()


def f20_vdah_198_lpsy_lower_high_pattern_count_252d_d1(high, low, close, volume):
    return f20_vdah_198_lpsy_lower_high_pattern_count_252d(high, low, close, volume).diff()


def f20_vdah_199_post_distribution_rally_failure_score_d1(high, low, close, volume):
    return f20_vdah_199_post_distribution_rally_failure_score(high, low, close, volume).diff()


def f20_vdah_200_lpsy_dwell_score_252d_d1(high, low, close, volume):
    return f20_vdah_200_lpsy_dwell_score_252d(high, low, close, volume).diff()


def f20_vdah_201_distribution_day_indicator_d1(close, volume):
    return f20_vdah_201_distribution_day_indicator(close, volume).diff()


def f20_vdah_202_distribution_day_count_25d_d1(close, volume):
    return f20_vdah_202_distribution_day_count_25d(close, volume).diff()


def f20_vdah_203_distribution_day_count_63d_d1(close, volume):
    return f20_vdah_203_distribution_day_count_63d(close, volume).diff()


def f20_vdah_204_strict_distribution_day_indicator_d1(close, volume):
    return f20_vdah_204_strict_distribution_day_indicator(close, volume).diff()


def f20_vdah_205_strict_distribution_day_count_63d_d1(close, volume):
    return f20_vdah_205_strict_distribution_day_count_63d(close, volume).diff()


def f20_vdah_206_distribution_to_accumulation_ratio_63d_d1(close, volume):
    return f20_vdah_206_distribution_to_accumulation_ratio_63d(close, volume).diff()


def f20_vdah_207_consec_distribution_days_streak_d1(close, volume):
    return f20_vdah_207_consec_distribution_days_streak(close, volume).diff()


def f20_vdah_208_distribution_day_severity_252d_d1(close, volume):
    return f20_vdah_208_distribution_day_severity_252d(close, volume).diff()


def f20_vdah_209_distribution_day_clustered_5d_indicator_d1(close, volume):
    return f20_vdah_209_distribution_day_clustered_5d_indicator(close, volume).diff()


def f20_vdah_210_distribution_day_after_252d_high_count_63d_d1(high, close, volume):
    return f20_vdah_210_distribution_day_after_252d_high_count_63d(high, close, volume).diff()


def f20_vdah_211_poc_price_252d_d1(close, volume):
    return f20_vdah_211_poc_price_252d(close, volume).diff()


def f20_vdah_212_log_dist_close_to_poc_252d_d1(close, volume):
    return f20_vdah_212_log_dist_close_to_poc_252d(close, volume).diff()


def f20_vdah_213_value_area_high_252d_d1(close, volume):
    return f20_vdah_213_value_area_high_252d(close, volume).diff()


def f20_vdah_214_value_area_low_252d_d1(close, volume):
    return f20_vdah_214_value_area_low_252d(close, volume).diff()


def f20_vdah_215_log_dist_close_to_vah_252d_d1(close, volume):
    return f20_vdah_215_log_dist_close_to_vah_252d(close, volume).diff()


def f20_vdah_216_log_value_area_width_252d_d1(close, volume):
    return f20_vdah_216_log_value_area_width_252d(close, volume).diff()


def f20_vdah_217_single_print_dwell_above_vah_252d_d1(close, volume):
    return f20_vdah_217_single_print_dwell_above_vah_252d(close, volume).diff()


def f20_vdah_218_poc_age_in_252d_d1(close, volume):
    return f20_vdah_218_poc_age_in_252d(close, volume).diff()


def f20_vdah_219_volume_above_vah_share_252d_d1(close, volume):
    return f20_vdah_219_volume_above_vah_share_252d(close, volume).diff()


def f20_vdah_220_value_area_skew_252d_d1(close, volume):
    return f20_vdah_220_value_area_skew_252d(close, volume).diff()


def f20_vdah_221_hawkes_volume_intensity_21d_d1(volume):
    return f20_vdah_221_hawkes_volume_intensity_21d(volume).diff()


def f20_vdah_222_hawkes_volume_intensity_63d_d1(volume):
    return f20_vdah_222_hawkes_volume_intensity_63d(volume).diff()


def f20_vdah_223_hawkes_volume_decay_ratio_21_to_63_d1(volume):
    return f20_vdah_223_hawkes_volume_decay_ratio_21_to_63(volume).diff()


def f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90_d1(volume):
    return f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90(volume).diff()


def f20_vdah_225_hawkes_volume_intensity_zscore_252d_d1(volume):
    return f20_vdah_225_hawkes_volume_intensity_zscore_252d(volume).diff()


VOLUME_DRYUP_AT_HIGH_D1_REGISTRY_151_225 = {
    "f20_vdah_151_vsa_no_demand_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_151_vsa_no_demand_bar_indicator_d1},
    "f20_vdah_152_vsa_no_demand_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_152_vsa_no_demand_count_63d_d1},
    "f20_vdah_153_vsa_no_demand_streak_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_153_vsa_no_demand_streak_d1},
    "f20_vdah_154_vsa_no_supply_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_154_vsa_no_supply_bar_indicator_d1},
    "f20_vdah_155_vsa_test_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_155_vsa_test_bar_indicator_d1},
    "f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_156_vsa_no_demand_to_no_supply_ratio_63d_d1},
    "f20_vdah_157_vsa_no_demand_gated_at_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_157_vsa_no_demand_gated_at_high_d1},
    "f20_vdah_158_vsa_no_demand_at_high_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_158_vsa_no_demand_at_high_count_252d_d1},
    "f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_159_vsa_no_demand_weighted_by_distance_to_high_d1},
    "f20_vdah_160_vsa_pseudo_supply_test_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_160_vsa_pseudo_supply_test_count_252d_d1},
    "f20_vdah_161_vsa_upthrust_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_161_vsa_upthrust_indicator_d1},
    "f20_vdah_162_vsa_upthrust_at_252d_high_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_162_vsa_upthrust_at_252d_high_indicator_d1},
    "f20_vdah_163_vsa_upthrust_after_distribution_score_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_163_vsa_upthrust_after_distribution_score_d1},
    "f20_vdah_164_count_upthrusts_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_164_count_upthrusts_252d_d1},
    "f20_vdah_165_upthrust_max_volume_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_165_upthrust_max_volume_zscore_252d_d1},
    "f20_vdah_166_bars_since_last_upthrust_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_166_bars_since_last_upthrust_252d_d1},
    "f20_vdah_167_upthrust_with_followthrough_failure_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_167_upthrust_with_followthrough_failure_indicator_d1},
    "f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_168_upthrust_volume_to_atr_ratio_252d_mean_d1},
    "f20_vdah_169_upthrust_followed_by_lower_high_within_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_169_upthrust_followed_by_lower_high_within_5d_d1},
    "f20_vdah_170_double_upthrust_indicator_5d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_170_double_upthrust_indicator_5d_d1},
    "f20_vdah_171_stalling_bar_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_171_stalling_bar_indicator_d1},
    "f20_vdah_172_stalling_bar_count_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_172_stalling_bar_count_63d_d1},
    "f20_vdah_173_stalling_bar_at_252d_high_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_173_stalling_bar_at_252d_high_count_252d_d1},
    "f20_vdah_174_churn_effort_to_result_ratio_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_174_churn_effort_to_result_ratio_21d_d1},
    "f20_vdah_175_churn_effort_to_result_ratio_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_175_churn_effort_to_result_ratio_63d_d1},
    "f20_vdah_176_churn_effort_to_range_ratio_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_176_churn_effort_to_range_ratio_21d_d1},
    "f20_vdah_177_top_decile_dwell_with_churn_indicator_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_177_top_decile_dwell_with_churn_indicator_252d_d1},
    "f20_vdah_178_churn_intensity_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_178_churn_intensity_zscore_252d_d1},
    "f20_vdah_179_max_churn_streak_at_high_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_179_max_churn_streak_at_high_252d_d1},
    "f20_vdah_180_churn_to_breakout_failure_ratio_252d_d1": {"inputs": ["high", "volume", "low", "close"], "func": f20_vdah_180_churn_to_breakout_failure_ratio_252d_d1},
    "f20_vdah_181_effort_minus_result_zscore_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_181_effort_minus_result_zscore_21d_d1},
    "f20_vdah_182_effort_minus_result_zscore_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_182_effort_minus_result_zscore_63d_d1},
    "f20_vdah_183_effort_minus_result_at_252d_high_only_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_183_effort_minus_result_at_252d_high_only_d1},
    "f20_vdah_184_effort_result_corr_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_184_effort_result_corr_252d_d1},
    "f20_vdah_185_volume_per_unit_range_zscore_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_185_volume_per_unit_range_zscore_252d_d1},
    "f20_vdah_186_count_high_effort_low_result_bars_63d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_186_count_high_effort_low_result_bars_63d_d1},
    "f20_vdah_187_high_effort_low_result_max_streak_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_187_high_effort_low_result_max_streak_252d_d1},
    "f20_vdah_188_effort_result_ratio_pct_rank_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_188_effort_result_ratio_pct_rank_252d_d1},
    "f20_vdah_189_volume_excess_when_range_compressed_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_189_volume_excess_when_range_compressed_252d_d1},
    "f20_vdah_190_effort_result_decoupling_index_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_190_effort_result_decoupling_index_252d_d1},
    "f20_vdah_191_weak_rally_after_breakdown_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_191_weak_rally_after_breakdown_indicator_d1},
    "f20_vdah_192_lpsy_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_192_lpsy_count_252d_d1},
    "f20_vdah_193_post_drawdown_rally_volume_decay_21d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_193_post_drawdown_rally_volume_decay_21d_d1},
    "f20_vdah_194_post_peak_rally_low_vol_strength_index_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_194_post_peak_rally_low_vol_strength_index_d1},
    "f20_vdah_195_lpsy_failure_to_retake_high_indicator_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_195_lpsy_failure_to_retake_high_indicator_d1},
    "f20_vdah_196_count_lpsy_failure_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_196_count_lpsy_failure_252d_d1},
    "f20_vdah_197_rally_volume_zscore_post_252d_high_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_197_rally_volume_zscore_post_252d_high_d1},
    "f20_vdah_198_lpsy_lower_high_pattern_count_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_198_lpsy_lower_high_pattern_count_252d_d1},
    "f20_vdah_199_post_distribution_rally_failure_score_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_199_post_distribution_rally_failure_score_d1},
    "f20_vdah_200_lpsy_dwell_score_252d_d1": {"inputs": ["high", "low", "close", "volume"], "func": f20_vdah_200_lpsy_dwell_score_252d_d1},
    "f20_vdah_201_distribution_day_indicator_d1": {"inputs": ["close", "volume"], "func": f20_vdah_201_distribution_day_indicator_d1},
    "f20_vdah_202_distribution_day_count_25d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_202_distribution_day_count_25d_d1},
    "f20_vdah_203_distribution_day_count_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_203_distribution_day_count_63d_d1},
    "f20_vdah_204_strict_distribution_day_indicator_d1": {"inputs": ["close", "volume"], "func": f20_vdah_204_strict_distribution_day_indicator_d1},
    "f20_vdah_205_strict_distribution_day_count_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_205_strict_distribution_day_count_63d_d1},
    "f20_vdah_206_distribution_to_accumulation_ratio_63d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_206_distribution_to_accumulation_ratio_63d_d1},
    "f20_vdah_207_consec_distribution_days_streak_d1": {"inputs": ["close", "volume"], "func": f20_vdah_207_consec_distribution_days_streak_d1},
    "f20_vdah_208_distribution_day_severity_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_208_distribution_day_severity_252d_d1},
    "f20_vdah_209_distribution_day_clustered_5d_indicator_d1": {"inputs": ["close", "volume"], "func": f20_vdah_209_distribution_day_clustered_5d_indicator_d1},
    "f20_vdah_210_distribution_day_after_252d_high_count_63d_d1": {"inputs": ["high", "close", "volume"], "func": f20_vdah_210_distribution_day_after_252d_high_count_63d_d1},
    "f20_vdah_211_poc_price_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_211_poc_price_252d_d1},
    "f20_vdah_212_log_dist_close_to_poc_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_212_log_dist_close_to_poc_252d_d1},
    "f20_vdah_213_value_area_high_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_213_value_area_high_252d_d1},
    "f20_vdah_214_value_area_low_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_214_value_area_low_252d_d1},
    "f20_vdah_215_log_dist_close_to_vah_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_215_log_dist_close_to_vah_252d_d1},
    "f20_vdah_216_log_value_area_width_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_216_log_value_area_width_252d_d1},
    "f20_vdah_217_single_print_dwell_above_vah_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_217_single_print_dwell_above_vah_252d_d1},
    "f20_vdah_218_poc_age_in_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_218_poc_age_in_252d_d1},
    "f20_vdah_219_volume_above_vah_share_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_219_volume_above_vah_share_252d_d1},
    "f20_vdah_220_value_area_skew_252d_d1": {"inputs": ["close", "volume"], "func": f20_vdah_220_value_area_skew_252d_d1},
    "f20_vdah_221_hawkes_volume_intensity_21d_d1": {"inputs": ["volume"], "func": f20_vdah_221_hawkes_volume_intensity_21d_d1},
    "f20_vdah_222_hawkes_volume_intensity_63d_d1": {"inputs": ["volume"], "func": f20_vdah_222_hawkes_volume_intensity_63d_d1},
    "f20_vdah_223_hawkes_volume_decay_ratio_21_to_63_d1": {"inputs": ["volume"], "func": f20_vdah_223_hawkes_volume_decay_ratio_21_to_63_d1},
    "f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90_d1": {"inputs": ["volume"], "func": f20_vdah_224_hawkes_volume_silence_bars_since_intensity_p90_d1},
    "f20_vdah_225_hawkes_volume_intensity_zscore_252d_d1": {"inputs": ["volume"], "func": f20_vdah_225_hawkes_volume_intensity_zscore_252d_d1},
}
