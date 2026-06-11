"""short_squeeze_aftermath d3 (third-diff) features 001-075 — Pipeline 1a-inverse short-side blowup family.

Third-difference (.diff().diff().diff()) of each corresponding base feature — captures jerk.
Inputs: NSIR (shortinterest, daystocover, shortpctfloat, shortpctshares,
shortinterestpriormonth) and SEP OHLCV (close, high, low, open, volume).
Detects POST-squeeze aftermath: covering exhausted, momentum fading, price
about to break down. Distinct from family #16 (snapshot SI structure) and
#25 (pre-peak SI buildup). PIT-clean: right-anchored rolling, explicit
min_periods, no centered windows, no .shift(-N). NSIR is sparse; pandas
rolling naturally skips NaN — no internal forward-fill.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 3, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _rolling_max(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).max()


def _rolling_min(s, w, mp=None):
    if mp is None:
        mp = max(w // 3, 2)
    return s.rolling(w, min_periods=mp).min()


def _pct_change(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


# ============================================================
#                    FEATURES 001-075
# ============================================================


def f49_ssaf_001_squeeze_event_50d_price_rip_x_si_level_d3(close, shortinterest):
    rmin = close.rolling(50, min_periods=10).min()
    rip = _safe_div(close - rmin, rmin)
    si_norm = _safe_div(shortinterest, shortinterest.rolling(252, min_periods=42).mean())
    return (rip * si_norm).diff().diff().diff()


def f49_ssaf_002_squeeze_event_21d_price_rip_x_dtc_d3(close, daystocover):
    rmin = close.rolling(21, min_periods=5).min()
    rip = _safe_div(close - rmin, rmin)
    return (rip * daystocover).diff().diff().diff()


def f49_ssaf_003_squeeze_strength_63d_close_minus_pre_d3(close):
    pre = close.shift(63).rolling(21, min_periods=5).mean()
    return (_safe_div(close - pre, pre)).diff().diff().diff()


def f49_ssaf_004_squeeze_event_high_extension_x_spfloat_d3(high, shortpctfloat):
    rmax = _rolling_max(high, 63, mp=10)
    ext = _safe_div(high - rmax.shift(21), rmax.shift(21))
    return (ext * shortpctfloat).diff().diff().diff()


def f49_ssaf_005_squeeze_event_log_volume_spike_x_si_drop_d3(volume, shortinterest):
    vmean = volume.rolling(63, min_periods=10).mean()
    vspike = _safe_log(_safe_div(volume, vmean))
    si_drop = -_pct_change(shortinterest, 21)
    return (vspike * si_drop).diff().diff().diff()


def f49_ssaf_006_squeeze_event_intraday_range_x_si_level_d3(high, low, close, shortpctshares):
    rng = _safe_div(high - low, close)
    rng_z = _rolling_zscore(rng, 63)
    return (rng_z * shortpctshares).diff().diff().diff()


def f49_ssaf_007_squeeze_window_max_5d_return_x_si_d3(close, shortinterest):
    r5 = _pct_change(close, 5)
    max5 = r5.rolling(63, min_periods=10).max()
    si_norm = _safe_div(shortinterest, shortinterest.rolling(126, min_periods=20).mean())
    return (max5 * si_norm).diff().diff().diff()


def f49_ssaf_008_squeeze_peak_age_63d_window_d3(high):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    age = high.rolling(63, min_periods=10).apply(_bsm, raw=True)
    return (age).diff().diff().diff()


def f49_ssaf_009_squeeze_event_3sigma_close_jump_d3(close):
    lr = _safe_log(close).diff()
    sd = lr.rolling(63, min_periods=10).std()
    norm = _safe_div(lr, sd)
    return (norm.rolling(63, min_periods=10).max()).diff().diff().diff()


def f49_ssaf_010_squeeze_event_count_5pct_days_21d_d3(close):
    lr = _safe_log(close).diff()
    big = (lr > 0.05).astype(float)
    return (big.rolling(21, min_periods=5).sum()).diff().diff().diff()


def f49_ssaf_011_squeeze_event_max_oc_gap_21d_x_si_d3(open, close, shortinterest):
    gap = _safe_div(open - close.shift(1), close.shift(1))
    mgap = gap.rolling(21, min_periods=5).max()
    si_norm = _safe_div(shortinterest, shortinterest.rolling(252, min_periods=42).mean())
    return (mgap * si_norm).diff().diff().diff()


def f49_ssaf_012_squeeze_breadth_pct_up_days_21d_post_signal_d3(close, shortpctfloat):
    up = (close.diff() > 0).astype(float)
    frac = up.rolling(21, min_periods=5).mean()
    return (frac * shortpctfloat).diff().diff().diff()


def f49_ssaf_013_squeeze_event_kurtosis_proxy_63d_d3(close):
    lr = _safe_log(close).diff()
    mx = lr.rolling(63, min_periods=10).max()
    sd = lr.rolling(63, min_periods=10).std()
    return (_safe_div(mx, sd)).diff().diff().diff()


def f49_ssaf_014_squeeze_event_close_to_252d_atr_dist_d3(close, high, low):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=5).mean()
    ymin = close.rolling(252, min_periods=42).min()
    return (_safe_div(close - ymin, atr)).diff().diff().diff()


def f49_ssaf_015_squeeze_concurrent_si_rise_then_drop_d3(shortinterest):
    rise_42_to_21 = _pct_change(shortinterest.shift(21), 21)
    drop_21_to_0 = -_pct_change(shortinterest, 21)
    return (rise_42_to_21 * drop_21_to_0).diff().diff().diff()


def f49_ssaf_016_si_drop_21d_after_peak_d3(shortinterest):
    si_peak = _rolling_max(shortinterest, 63, mp=10)
    rel = _safe_div(shortinterest - si_peak, si_peak)
    return (rel).diff().diff().diff()


def f49_ssaf_017_si_covering_velocity_log_drop_21d_d3(shortinterest):
    ls = _safe_log(shortinterest)
    return (ls.shift(21) - ls).diff().diff().diff()


def f49_ssaf_018_si_covering_velocity_log_drop_63d_d3(shortinterest):
    ls = _safe_log(shortinterest)
    return (ls.shift(63) - ls).diff().diff().diff()


def f49_ssaf_019_si_drop_from_63d_peak_pct_d3(shortinterest):
    pk = _rolling_max(shortinterest, 63, mp=10)
    return (_safe_div(pk - shortinterest, pk)).diff().diff().diff()


def f49_ssaf_020_si_drop_from_126d_peak_pct_d3(shortinterest):
    pk = _rolling_max(shortinterest, 126, mp=21)
    return (_safe_div(pk - shortinterest, pk)).diff().diff().diff()


def f49_ssaf_021_si_covering_streak_consecutive_negatives_d3(shortinterest):
    d = shortinterest.diff()
    neg = (d < 0).astype(float)
    grp = (neg == 0).cumsum()
    return (neg.groupby(grp).cumsum()).diff().diff().diff()


def f49_ssaf_022_si_priormonth_above_current_gap_d3(shortinterest, shortinterestpriormonth):
    return (_safe_div(shortinterestpriormonth - shortinterest, shortinterestpriormonth)).diff().diff().diff()


def f49_ssaf_023_si_ema_fast_minus_slow_crossover_d3(shortinterest):
    fast = _ema(shortinterest, 10, min_periods=3)
    slow = _ema(shortinterest, 42, min_periods=8)
    return (_safe_div(fast - slow, slow)).diff().diff().diff()


def f49_ssaf_024_si_zscore_collapse_63d_d3(shortinterest):
    return (-_rolling_zscore(shortinterest, 63)).diff().diff().diff()


def f49_ssaf_025_si_drop_acceleration_proxy_d3(shortinterest):
    d21 = shortinterest.diff(21)
    d63 = shortinterest.diff(63)
    return (_safe_div(d21, d63.abs())).diff().diff().diff()


def f49_ssaf_026_si_fraction_of_21d_high_lost_d3(shortinterest):
    hi = _rolling_max(shortinterest, 21, mp=5)
    return (_safe_div(hi - shortinterest, hi)).diff().diff().diff()


def f49_ssaf_027_si_covering_burst_intensity_5d_d3(shortinterest):
    d5 = shortinterest.diff(5)
    sd = shortinterest.diff().rolling(63, min_periods=10).std()
    return (_safe_div(-d5, sd)).diff().diff().diff()


def f49_ssaf_028_spfloat_drop_42d_post_squeeze_d3(shortpctfloat):
    return (-(shortpctfloat - shortpctfloat.shift(42))).diff().diff().diff()


def f49_ssaf_029_spshares_drop_42d_post_squeeze_d3(shortpctshares):
    return (-(shortpctshares - shortpctshares.shift(42))).diff().diff().diff()


def f49_ssaf_030_si_log_drop_vs_log_ema_spread_d3(shortinterest):
    ls = _safe_log(shortinterest)
    ema = _ema(ls, 63, min_periods=10)
    return (ema - ls).diff().diff().diff()


def f49_ssaf_031_dtc_drop_from_63d_peak_d3(daystocover):
    pk = _rolling_max(daystocover, 63, mp=10)
    return (_safe_div(pk - daystocover, pk)).diff().diff().diff()


def f49_ssaf_032_dtc_pct_change_21d_neg_d3(daystocover):
    return (-_pct_change(daystocover, 21)).diff().diff().diff()


def f49_ssaf_033_dtc_ema_spread_negative_d3(daystocover):
    fast = _ema(daystocover, 10, min_periods=3)
    slow = _ema(daystocover, 42, min_periods=8)
    return (_safe_div(slow - fast, slow)).diff().diff().diff()


def f49_ssaf_034_dtc_zscore_below_252d_mean_d3(daystocover):
    return (-_rolling_zscore(daystocover, 252)).diff().diff().diff()


def f49_ssaf_035_dtc_consecutive_drop_streak_d3(daystocover):
    d = daystocover.diff()
    neg = (d < 0).astype(float)
    grp = (neg == 0).cumsum()
    return (neg.groupby(grp).cumsum()).diff().diff().diff()


def f49_ssaf_036_dtc_log_compression_63d_d3(daystocover):
    return (_safe_log(daystocover).shift(63) - _safe_log(daystocover)).diff().diff().diff()


def f49_ssaf_037_dtc_below_pre_squeeze_baseline_d3(daystocover):
    base = daystocover.shift(126).rolling(63, min_periods=10).mean()
    return (_safe_div(base - daystocover, base)).diff().diff().diff()


def f49_ssaf_038_dtc_max63_now_minus_now_to_atr_proxy_d3(daystocover):
    pk = _rolling_max(daystocover, 63, mp=10)
    sd = daystocover.diff().rolling(63, min_periods=10).std()
    return (_safe_div(pk - daystocover, sd)).diff().diff().diff()


def f49_ssaf_039_dtc_drop_x_log_si_drop_compound_d3(daystocover, shortinterest):
    dtc_drop = -_pct_change(daystocover, 21)
    si_drop = -_pct_change(shortinterest, 21)
    return (dtc_drop * si_drop).diff().diff().diff()


def f49_ssaf_040_dtc_unwind_age_since_63d_peak_d3(daystocover):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    return (daystocover.rolling(63, min_periods=10).apply(_bsm, raw=True)).diff().diff().diff()


def f49_ssaf_041_si_drop_price_held_decorrel_21d_d3(shortinterest, close):
    si_drop = -_pct_change(shortinterest, 21)
    px_chg = _pct_change(close, 21)
    return (si_drop * (1 + px_chg)).diff().diff().diff()


def f49_ssaf_042_rolling_corr_dlog_si_dlog_close_63d_d3(shortinterest, close):
    dls = _safe_log(shortinterest).diff()
    dlc = _safe_log(close).diff()
    return (dls.rolling(63, min_periods=10).corr(dlc)).diff().diff().diff()


def f49_ssaf_043_si_change_minus_price_change_normalized_d3(shortinterest, close):
    dsi = _pct_change(shortinterest, 21)
    dpx = _pct_change(close, 21)
    return (dpx - dsi).diff().diff().diff()


def f49_ssaf_044_covering_without_price_drop_indicator_d3(shortinterest, close):
    si_dn = (shortinterest.diff(21) < 0).astype(float)
    px_up = (close.diff(21) > 0).astype(float)
    return (si_dn * px_up).diff().diff().diff()


def f49_ssaf_045_decorrel_si_rising_price_rising_then_diverging_d3(shortinterest, close):
    dlc = _safe_log(close).diff(21)
    dls = _safe_log(shortinterest).diff(21)
    return (dlc - dls).diff().diff().diff()


def f49_ssaf_046_price_overhang_si_already_left_63d_d3(close, shortinterest):
    px_z = _rolling_zscore(_safe_log(close), 63)
    si_z = _rolling_zscore(_safe_log(shortinterest), 63)
    return (px_z - si_z).diff().diff().diff()


def f49_ssaf_047_lag_corr_si_to_price_42d_d3(shortinterest, close):
    dls = _safe_log(shortinterest).diff()
    dlc = _safe_log(close).diff()
    return (dls.shift(21).rolling(42, min_periods=8).corr(dlc)).diff().diff().diff()


def f49_ssaf_048_shortpctfloat_collapse_price_premium_d3(shortpctfloat, close):
    spf_chg = shortpctfloat - shortpctfloat.shift(42)
    px_ret = _pct_change(close, 42)
    return ((-spf_chg) * (1 + px_ret)).diff().diff().diff()


def f49_ssaf_049_si_vs_close_rank_decoupling_63d_d3(shortinterest, close):
    sr = shortinterest.rolling(63, min_periods=10).rank(pct=True)
    cr = close.rolling(63, min_periods=10).rank(pct=True)
    return (cr - sr).diff().diff().diff()


def f49_ssaf_050_covering_exhausted_price_stalled_21d_d3(shortinterest, close):
    si_dropped = (_pct_change(shortinterest, 42) < -0.1).astype(float)
    px_flat = (_pct_change(close, 21).abs() < 0.03).astype(float)
    return (si_dropped * px_flat).diff().diff().diff()


def f49_ssaf_051_neg_corr_si_change_price_change_63d_d3(shortinterest, close):
    dsi = shortinterest.diff()
    dpx = close.diff()
    return (-dsi.rolling(63, min_periods=10).corr(dpx)).diff().diff().diff()


def f49_ssaf_052_log_si_residual_after_price_regression_63d_d3(shortinterest, close):
    ls = _safe_log(shortinterest)
    lc = _safe_log(close)
    ls_m = ls.rolling(63, min_periods=10).mean()
    lc_m = lc.rolling(63, min_periods=10).mean()
    cov = ((ls - ls_m) * (lc - lc_m)).rolling(63, min_periods=10).mean()
    var = ((lc - lc_m) ** 2).rolling(63, min_periods=10).mean()
    beta = _safe_div(cov, var)
    return (ls - (ls_m + beta * (lc - lc_m))).diff().diff().diff()


def f49_ssaf_053_si_drop_size_minus_price_drop_size_21d_d3(shortinterest, close):
    return ((-_pct_change(shortinterest, 21)) - (-_pct_change(close, 21))).diff().diff().diff()


def f49_ssaf_054_volume_thinning_vs_squeeze_peak_42d_d3(volume):
    vmax = _rolling_max(volume, 63, mp=10)
    return (_safe_div(volume, vmax)).diff().diff().diff()


def f49_ssaf_055_volume_decay_log_vs_peak_63d_d3(volume):
    vmax = _rolling_max(volume, 63, mp=10)
    return (_safe_log(volume) - _safe_log(vmax)).diff().diff().diff()


def f49_ssaf_056_volume_ema_fast_below_slow_d3(volume):
    fast = _ema(volume, 10, min_periods=3)
    slow = _ema(volume, 42, min_periods=8)
    return (_safe_div(fast - slow, slow)).diff().diff().diff()


def f49_ssaf_057_post_peak_volume_zscore_d3(volume):
    return (_rolling_zscore(_safe_log(volume), 63)).diff().diff().diff()


def f49_ssaf_058_volume_drop_x_close_below_peak_d3(volume, close):
    vdrop = -_pct_change(volume.rolling(5, min_periods=2).mean(), 21)
    pmax = _rolling_max(close, 63, mp=10)
    px_under = _safe_div(pmax - close, pmax)
    return (vdrop * px_under).diff().diff().diff()


def f49_ssaf_059_volume_to_252d_median_d3(volume):
    med = volume.rolling(252, min_periods=42).median()
    return (_safe_div(volume, med)).diff().diff().diff()


def f49_ssaf_060_rolling_volume_kurt_compression_proxy_d3(volume):
    v_lg = _safe_log(volume)
    mx = v_lg.rolling(63, min_periods=10).max()
    mn = v_lg.rolling(63, min_periods=10).min()
    sd = v_lg.rolling(63, min_periods=10).std()
    return (_safe_div(mx - mn, sd)).diff().diff().diff()


def f49_ssaf_061_volume_z_lower_band_proxy_d3(volume):
    return (-_rolling_zscore(volume, 21)).diff().diff().diff()


def f49_ssaf_062_dollar_volume_decay_42d_d3(close, volume):
    dv = close * volume
    pk = _rolling_max(dv, 63, mp=10)
    return (_safe_log(dv) - _safe_log(pk)).diff().diff().diff()


def f49_ssaf_063_up_day_volume_vs_down_day_volume_21d_d3(close, volume):
    d = close.diff()
    up_v = volume.where(d > 0, 0.0).rolling(21, min_periods=5).sum()
    dn_v = volume.where(d < 0, 0.0).rolling(21, min_periods=5).sum()
    return (_safe_div(up_v - dn_v, up_v + dn_v)).diff().diff().diff()


def f49_ssaf_064_volume_post_peak_atr_normalized_d3(volume, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=5).mean()
    return (_safe_div(volume, atr * close)).diff().diff().diff()


def f49_ssaf_065_volume_spike_age_since_63d_peak_d3(volume):
    def _bsm(w): return (len(w) - 1) - int(np.argmax(w))
    return (volume.rolling(63, min_periods=10).apply(_bsm, raw=True)).diff().diff().diff()


def f49_ssaf_066_range_compression_atr_drop_21d_vs_63d_d3(high, low, close):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a21 = tr.rolling(21, min_periods=5).mean()
    a63 = tr.rolling(63, min_periods=10).mean()
    return (_safe_div(a21, a63)).diff().diff().diff()


def f49_ssaf_067_high_low_range_compression_log_d3(high, low):
    rng = _safe_log(high) - _safe_log(low)
    rng_z = _rolling_zscore(rng, 63)
    return (-rng_z).diff().diff().diff()


def f49_ssaf_068_intraday_range_ema_collapse_21d_d3(high, low, close):
    rng = _safe_div(high - low, close)
    fast = _ema(rng, 10, min_periods=3)
    slow = _ema(rng, 42, min_periods=8)
    return (_safe_div(slow - fast, slow)).diff().diff().diff()


def f49_ssaf_069_close_to_close_std_compression_21d_post_squeeze_d3(close):
    lr = _safe_log(close).diff()
    s21 = lr.rolling(21, min_periods=5).std()
    s63 = lr.rolling(63, min_periods=10).std()
    return (_safe_div(s63 - s21, s63)).diff().diff().diff()


def f49_ssaf_070_narrow_range_day_count_21d_after_high_d3(high, low, close):
    rng = _safe_div(high - low, close)
    avg = rng.rolling(63, min_periods=10).mean()
    narrow = (rng < 0.5 * avg).astype(float)
    return (narrow.rolling(21, min_periods=5).sum()).diff().diff().diff()


def f49_ssaf_071_bbwidth_collapse_proxy_21d_d3(close):
    m = close.rolling(21, min_periods=5).mean()
    sd = close.rolling(21, min_periods=5).std()
    bw = _safe_div(2 * sd, m)
    return (-_rolling_zscore(bw, 63)).diff().diff().diff()


def f49_ssaf_072_true_range_minus_close_movement_21d_d3(high, low, close):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    cm = (close - pc).abs()
    return (_safe_div(tr - cm, tr).rolling(21, min_periods=5).mean()).diff().diff().diff()


def f49_ssaf_073_failed_retest_close_below_prior_high_after_approach_d3(close, high):
    pk = _rolling_max(high, 63, mp=10).shift(21)
    approach = _safe_div(close - pk, pk)
    return ((-approach).rolling(21, min_periods=5).max()).diff().diff().diff()


def f49_ssaf_074_lower_high_formation_post_squeeze_d3(high):
    pk1 = _rolling_max(high, 63, mp=10).shift(42)
    pk2 = _rolling_max(high, 42, mp=10)
    return (_safe_div(pk2 - pk1, pk1)).diff().diff().diff()


def f49_ssaf_075_retest_volume_failure_proxy_21d_d3(high, volume):
    pk = _rolling_max(high, 63, mp=10).shift(21)
    near = (_safe_div(high, pk) > 0.97).astype(float)
    vbase = volume.rolling(63, min_periods=10).mean()
    return (near * _safe_div(vbase - volume, vbase)).diff().diff().diff()


SHORT_SQUEEZE_AFTERMATH_D3_REGISTRY_001_075 = {
    "f49_ssaf_001_squeeze_event_50d_price_rip_x_si_level_d3": {"inputs": ["close", "shortinterest"], "func": f49_ssaf_001_squeeze_event_50d_price_rip_x_si_level_d3},
    "f49_ssaf_002_squeeze_event_21d_price_rip_x_dtc_d3": {"inputs": ["close", "daystocover"], "func": f49_ssaf_002_squeeze_event_21d_price_rip_x_dtc_d3},
    "f49_ssaf_003_squeeze_strength_63d_close_minus_pre_d3": {"inputs": ["close"], "func": f49_ssaf_003_squeeze_strength_63d_close_minus_pre_d3},
    "f49_ssaf_004_squeeze_event_high_extension_x_spfloat_d3": {"inputs": ["high", "shortpctfloat"], "func": f49_ssaf_004_squeeze_event_high_extension_x_spfloat_d3},
    "f49_ssaf_005_squeeze_event_log_volume_spike_x_si_drop_d3": {"inputs": ["volume", "shortinterest"], "func": f49_ssaf_005_squeeze_event_log_volume_spike_x_si_drop_d3},
    "f49_ssaf_006_squeeze_event_intraday_range_x_si_level_d3": {"inputs": ["high", "low", "close", "shortpctshares"], "func": f49_ssaf_006_squeeze_event_intraday_range_x_si_level_d3},
    "f49_ssaf_007_squeeze_window_max_5d_return_x_si_d3": {"inputs": ["close", "shortinterest"], "func": f49_ssaf_007_squeeze_window_max_5d_return_x_si_d3},
    "f49_ssaf_008_squeeze_peak_age_63d_window_d3": {"inputs": ["high"], "func": f49_ssaf_008_squeeze_peak_age_63d_window_d3},
    "f49_ssaf_009_squeeze_event_3sigma_close_jump_d3": {"inputs": ["close"], "func": f49_ssaf_009_squeeze_event_3sigma_close_jump_d3},
    "f49_ssaf_010_squeeze_event_count_5pct_days_21d_d3": {"inputs": ["close"], "func": f49_ssaf_010_squeeze_event_count_5pct_days_21d_d3},
    "f49_ssaf_011_squeeze_event_max_oc_gap_21d_x_si_d3": {"inputs": ["open", "close", "shortinterest"], "func": f49_ssaf_011_squeeze_event_max_oc_gap_21d_x_si_d3},
    "f49_ssaf_012_squeeze_breadth_pct_up_days_21d_post_signal_d3": {"inputs": ["close", "shortpctfloat"], "func": f49_ssaf_012_squeeze_breadth_pct_up_days_21d_post_signal_d3},
    "f49_ssaf_013_squeeze_event_kurtosis_proxy_63d_d3": {"inputs": ["close"], "func": f49_ssaf_013_squeeze_event_kurtosis_proxy_63d_d3},
    "f49_ssaf_014_squeeze_event_close_to_252d_atr_dist_d3": {"inputs": ["close", "high", "low"], "func": f49_ssaf_014_squeeze_event_close_to_252d_atr_dist_d3},
    "f49_ssaf_015_squeeze_concurrent_si_rise_then_drop_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_015_squeeze_concurrent_si_rise_then_drop_d3},
    "f49_ssaf_016_si_drop_21d_after_peak_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_016_si_drop_21d_after_peak_d3},
    "f49_ssaf_017_si_covering_velocity_log_drop_21d_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_017_si_covering_velocity_log_drop_21d_d3},
    "f49_ssaf_018_si_covering_velocity_log_drop_63d_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_018_si_covering_velocity_log_drop_63d_d3},
    "f49_ssaf_019_si_drop_from_63d_peak_pct_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_019_si_drop_from_63d_peak_pct_d3},
    "f49_ssaf_020_si_drop_from_126d_peak_pct_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_020_si_drop_from_126d_peak_pct_d3},
    "f49_ssaf_021_si_covering_streak_consecutive_negatives_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_021_si_covering_streak_consecutive_negatives_d3},
    "f49_ssaf_022_si_priormonth_above_current_gap_d3": {"inputs": ["shortinterest", "shortinterestpriormonth"], "func": f49_ssaf_022_si_priormonth_above_current_gap_d3},
    "f49_ssaf_023_si_ema_fast_minus_slow_crossover_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_023_si_ema_fast_minus_slow_crossover_d3},
    "f49_ssaf_024_si_zscore_collapse_63d_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_024_si_zscore_collapse_63d_d3},
    "f49_ssaf_025_si_drop_acceleration_proxy_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_025_si_drop_acceleration_proxy_d3},
    "f49_ssaf_026_si_fraction_of_21d_high_lost_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_026_si_fraction_of_21d_high_lost_d3},
    "f49_ssaf_027_si_covering_burst_intensity_5d_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_027_si_covering_burst_intensity_5d_d3},
    "f49_ssaf_028_spfloat_drop_42d_post_squeeze_d3": {"inputs": ["shortpctfloat"], "func": f49_ssaf_028_spfloat_drop_42d_post_squeeze_d3},
    "f49_ssaf_029_spshares_drop_42d_post_squeeze_d3": {"inputs": ["shortpctshares"], "func": f49_ssaf_029_spshares_drop_42d_post_squeeze_d3},
    "f49_ssaf_030_si_log_drop_vs_log_ema_spread_d3": {"inputs": ["shortinterest"], "func": f49_ssaf_030_si_log_drop_vs_log_ema_spread_d3},
    "f49_ssaf_031_dtc_drop_from_63d_peak_d3": {"inputs": ["daystocover"], "func": f49_ssaf_031_dtc_drop_from_63d_peak_d3},
    "f49_ssaf_032_dtc_pct_change_21d_neg_d3": {"inputs": ["daystocover"], "func": f49_ssaf_032_dtc_pct_change_21d_neg_d3},
    "f49_ssaf_033_dtc_ema_spread_negative_d3": {"inputs": ["daystocover"], "func": f49_ssaf_033_dtc_ema_spread_negative_d3},
    "f49_ssaf_034_dtc_zscore_below_252d_mean_d3": {"inputs": ["daystocover"], "func": f49_ssaf_034_dtc_zscore_below_252d_mean_d3},
    "f49_ssaf_035_dtc_consecutive_drop_streak_d3": {"inputs": ["daystocover"], "func": f49_ssaf_035_dtc_consecutive_drop_streak_d3},
    "f49_ssaf_036_dtc_log_compression_63d_d3": {"inputs": ["daystocover"], "func": f49_ssaf_036_dtc_log_compression_63d_d3},
    "f49_ssaf_037_dtc_below_pre_squeeze_baseline_d3": {"inputs": ["daystocover"], "func": f49_ssaf_037_dtc_below_pre_squeeze_baseline_d3},
    "f49_ssaf_038_dtc_max63_now_minus_now_to_atr_proxy_d3": {"inputs": ["daystocover"], "func": f49_ssaf_038_dtc_max63_now_minus_now_to_atr_proxy_d3},
    "f49_ssaf_039_dtc_drop_x_log_si_drop_compound_d3": {"inputs": ["daystocover", "shortinterest"], "func": f49_ssaf_039_dtc_drop_x_log_si_drop_compound_d3},
    "f49_ssaf_040_dtc_unwind_age_since_63d_peak_d3": {"inputs": ["daystocover"], "func": f49_ssaf_040_dtc_unwind_age_since_63d_peak_d3},
    "f49_ssaf_041_si_drop_price_held_decorrel_21d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_041_si_drop_price_held_decorrel_21d_d3},
    "f49_ssaf_042_rolling_corr_dlog_si_dlog_close_63d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_042_rolling_corr_dlog_si_dlog_close_63d_d3},
    "f49_ssaf_043_si_change_minus_price_change_normalized_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_043_si_change_minus_price_change_normalized_d3},
    "f49_ssaf_044_covering_without_price_drop_indicator_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_044_covering_without_price_drop_indicator_d3},
    "f49_ssaf_045_decorrel_si_rising_price_rising_then_diverging_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_045_decorrel_si_rising_price_rising_then_diverging_d3},
    "f49_ssaf_046_price_overhang_si_already_left_63d_d3": {"inputs": ["close", "shortinterest"], "func": f49_ssaf_046_price_overhang_si_already_left_63d_d3},
    "f49_ssaf_047_lag_corr_si_to_price_42d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_047_lag_corr_si_to_price_42d_d3},
    "f49_ssaf_048_shortpctfloat_collapse_price_premium_d3": {"inputs": ["shortpctfloat", "close"], "func": f49_ssaf_048_shortpctfloat_collapse_price_premium_d3},
    "f49_ssaf_049_si_vs_close_rank_decoupling_63d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_049_si_vs_close_rank_decoupling_63d_d3},
    "f49_ssaf_050_covering_exhausted_price_stalled_21d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_050_covering_exhausted_price_stalled_21d_d3},
    "f49_ssaf_051_neg_corr_si_change_price_change_63d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_051_neg_corr_si_change_price_change_63d_d3},
    "f49_ssaf_052_log_si_residual_after_price_regression_63d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_052_log_si_residual_after_price_regression_63d_d3},
    "f49_ssaf_053_si_drop_size_minus_price_drop_size_21d_d3": {"inputs": ["shortinterest", "close"], "func": f49_ssaf_053_si_drop_size_minus_price_drop_size_21d_d3},
    "f49_ssaf_054_volume_thinning_vs_squeeze_peak_42d_d3": {"inputs": ["volume"], "func": f49_ssaf_054_volume_thinning_vs_squeeze_peak_42d_d3},
    "f49_ssaf_055_volume_decay_log_vs_peak_63d_d3": {"inputs": ["volume"], "func": f49_ssaf_055_volume_decay_log_vs_peak_63d_d3},
    "f49_ssaf_056_volume_ema_fast_below_slow_d3": {"inputs": ["volume"], "func": f49_ssaf_056_volume_ema_fast_below_slow_d3},
    "f49_ssaf_057_post_peak_volume_zscore_d3": {"inputs": ["volume"], "func": f49_ssaf_057_post_peak_volume_zscore_d3},
    "f49_ssaf_058_volume_drop_x_close_below_peak_d3": {"inputs": ["volume", "close"], "func": f49_ssaf_058_volume_drop_x_close_below_peak_d3},
    "f49_ssaf_059_volume_to_252d_median_d3": {"inputs": ["volume"], "func": f49_ssaf_059_volume_to_252d_median_d3},
    "f49_ssaf_060_rolling_volume_kurt_compression_proxy_d3": {"inputs": ["volume"], "func": f49_ssaf_060_rolling_volume_kurt_compression_proxy_d3},
    "f49_ssaf_061_volume_z_lower_band_proxy_d3": {"inputs": ["volume"], "func": f49_ssaf_061_volume_z_lower_band_proxy_d3},
    "f49_ssaf_062_dollar_volume_decay_42d_d3": {"inputs": ["close", "volume"], "func": f49_ssaf_062_dollar_volume_decay_42d_d3},
    "f49_ssaf_063_up_day_volume_vs_down_day_volume_21d_d3": {"inputs": ["close", "volume"], "func": f49_ssaf_063_up_day_volume_vs_down_day_volume_21d_d3},
    "f49_ssaf_064_volume_post_peak_atr_normalized_d3": {"inputs": ["volume", "high", "low", "close"], "func": f49_ssaf_064_volume_post_peak_atr_normalized_d3},
    "f49_ssaf_065_volume_spike_age_since_63d_peak_d3": {"inputs": ["volume"], "func": f49_ssaf_065_volume_spike_age_since_63d_peak_d3},
    "f49_ssaf_066_range_compression_atr_drop_21d_vs_63d_d3": {"inputs": ["high", "low", "close"], "func": f49_ssaf_066_range_compression_atr_drop_21d_vs_63d_d3},
    "f49_ssaf_067_high_low_range_compression_log_d3": {"inputs": ["high", "low"], "func": f49_ssaf_067_high_low_range_compression_log_d3},
    "f49_ssaf_068_intraday_range_ema_collapse_21d_d3": {"inputs": ["high", "low", "close"], "func": f49_ssaf_068_intraday_range_ema_collapse_21d_d3},
    "f49_ssaf_069_close_to_close_std_compression_21d_post_squeeze_d3": {"inputs": ["close"], "func": f49_ssaf_069_close_to_close_std_compression_21d_post_squeeze_d3},
    "f49_ssaf_070_narrow_range_day_count_21d_after_high_d3": {"inputs": ["high", "low", "close"], "func": f49_ssaf_070_narrow_range_day_count_21d_after_high_d3},
    "f49_ssaf_071_bbwidth_collapse_proxy_21d_d3": {"inputs": ["close"], "func": f49_ssaf_071_bbwidth_collapse_proxy_21d_d3},
    "f49_ssaf_072_true_range_minus_close_movement_21d_d3": {"inputs": ["high", "low", "close"], "func": f49_ssaf_072_true_range_minus_close_movement_21d_d3},
    "f49_ssaf_073_failed_retest_close_below_prior_high_after_approach_d3": {"inputs": ["close", "high"], "func": f49_ssaf_073_failed_retest_close_below_prior_high_after_approach_d3},
    "f49_ssaf_074_lower_high_formation_post_squeeze_d3": {"inputs": ["high"], "func": f49_ssaf_074_lower_high_formation_post_squeeze_d3},
    "f49_ssaf_075_retest_volume_failure_proxy_21d_d3": {"inputs": ["high", "volume"], "func": f49_ssaf_075_retest_volume_failure_proxy_21d_d3},
}
