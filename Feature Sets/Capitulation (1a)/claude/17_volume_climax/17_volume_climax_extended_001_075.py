"""
17_volume_climax — Extended Features 001-075 (Churn / Effort-vs-Result)
Domain: single-day extreme volume events — churn / effort-vs-result: bars with high
volume ("effort") but small price change or small body ("poor result") — the classic
distribution / absorption signature. Also covers climax-then-no-follow-through,
intraday reversal on climax, two-bar climax clusters, climax exhaustion, and
rate-of-change of climax intensity.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    """Rolling z-score of volume within trailing w periods."""
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s)


def _body(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute candle body size."""
    return (close - open).abs()


def _range_hl(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday high-low range."""
    return high - low


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Effort-vs-result ratio (single-bar) ---

def vcx_ext_001_effort_result_ratio_return_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (21d) divided by abs(close return).
    High ratio = heavy volume produced little price movement (churn signal).
    """
    vol_z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    return _safe_div(vol_z, ret_abs)


def vcx_ext_002_effort_result_ratio_return_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (63d) divided by abs(close return).
    High ratio = heavy volume produced little price movement (churn signal).
    """
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    return _safe_div(vol_z, ret_abs)


def vcx_ext_003_effort_result_ratio_body_21d(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (21d) divided by abs(body/open).
    Uses candle body as the result measure instead of close-to-close return.
    """
    vol_z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    body_pct = _safe_div(_body(close, open), open.replace(0, np.nan))
    return _safe_div(vol_z, body_pct.replace(0, np.nan))


def vcx_ext_004_effort_result_ratio_body_63d(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (63d) divided by abs(body/open).
    """
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    body_pct = _safe_div(_body(close, open), open.replace(0, np.nan))
    return _safe_div(vol_z, body_pct.replace(0, np.nan))


def vcx_ext_005_effort_result_ratio_range_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (21d) divided by normalized HL range.
    High value = wide volume, narrow range = stalling / distribution.
    """
    vol_z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    rng_pct = _safe_div(_range_hl(high, low), close.shift(1).replace(0, np.nan))
    return _safe_div(vol_z, rng_pct.replace(0, np.nan))


def vcx_ext_006_effort_result_ratio_range_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Effort-vs-result ratio: volume z-score (63d) divided by normalized HL range.
    """
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    rng_pct = _safe_div(_range_hl(high, low), close.shift(1).replace(0, np.nan))
    return _safe_div(vol_z, rng_pct.replace(0, np.nan))


def vcx_ext_007_effort_result_zscore_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Z-score of daily effort-vs-result ratio (vol_multiple / abs_return) over 21d.
    Normalizes the ratio to detect when it is unusually high vs recent history.
    """
    vol_mult = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    raw = _safe_div(vol_mult, ret_abs)
    m = _rolling_mean(raw, _TD_MON)
    s = _rolling_std(raw, _TD_MON)
    return _safe_div(raw - m, s)


def vcx_ext_008_effort_result_zscore_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Z-score of daily effort-vs-result ratio (vol_multiple / abs_return) over 63d.
    """
    vol_mult = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    raw = _safe_div(vol_mult, ret_abs)
    m = _rolling_mean(raw, _TD_QTR)
    s = _rolling_std(raw, _TD_QTR)
    return _safe_div(raw - m, s)


def vcx_ext_009_price_progress_per_unit_volume_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Price progress (abs cumulative return over 21d) divided by cumulative volume (21d).
    Low value = lots of volume, little net price progress (absorption / churn).
    """
    ret_abs_cum = close.pct_change(1).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vol_cum = _rolling_sum(volume, _TD_MON)
    return _safe_div(ret_abs_cum, vol_cum)


def vcx_ext_010_price_progress_per_unit_volume_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Abs cumulative return over 63d divided by cumulative volume.
    """
    ret_abs_cum = close.pct_change(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vol_cum = _rolling_sum(volume, _TD_QTR)
    return _safe_div(ret_abs_cum, vol_cum)


# --- Group B (011-022): Churn flags and counts ---

def vcx_ext_011_churn_flag_vol2x_ret05pct(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Churn flag: volume >= 2x rolling 21d mean AND abs(return) <= 0.5%.
    Classic distribution or absorption bar — heavy volume, flat close.
    """
    high_vol = volume >= 2.0 * _rolling_mean(volume, _TD_MON)
    low_ret = close.pct_change(1).abs() <= 0.005
    return (high_vol & low_ret).astype(float)


def vcx_ext_012_churn_flag_vol2x_body05pct(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Churn flag: volume >= 2x rolling 21d mean AND abs(body/open) <= 0.5%.
    Uses body size as the result measure.
    """
    high_vol = volume >= 2.0 * _rolling_mean(volume, _TD_MON)
    low_body = _safe_div(_body(close, open), open.replace(0, np.nan)) <= 0.005
    return (high_vol & low_body).astype(float)


def vcx_ext_013_churn_flag_vol3x_ret1pct(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Stricter churn flag: volume >= 3x rolling 21d mean AND abs(return) <= 1%.
    """
    high_vol = volume >= 3.0 * _rolling_mean(volume, _TD_MON)
    low_ret = close.pct_change(1).abs() <= 0.01
    return (high_vol & low_ret).astype(float)


def vcx_ext_014_churn_count_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of churn bars (vol>=2x mean, |ret|<=0.5%) in trailing 21 days.
    """
    flag = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)
    return flag.rolling(_TD_MON, min_periods=1).sum()


def vcx_ext_015_churn_count_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of churn bars (vol>=2x mean, |ret|<=0.5%) in trailing 63 days.
    """
    flag = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_016_churn_count_252d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of churn bars (vol>=2x mean, |ret|<=0.5%) in trailing 252 days.
    """
    flag = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)
    return flag.rolling(_TD_YEAR, min_periods=1).sum()


def vcx_ext_017_churn_body_count_21d(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of body-churn bars (vol>=2x mean, |body/open|<=0.5%) in 21 days.
    """
    flag = vcx_ext_012_churn_flag_vol2x_body05pct(close, open, volume)
    return flag.rolling(_TD_MON, min_periods=1).sum()


def vcx_ext_018_churn_body_count_63d(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of body-churn bars (vol>=2x mean, |body/open|<=0.5%) in 63 days.
    """
    flag = vcx_ext_012_churn_flag_vol2x_body05pct(close, open, volume)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_019_churn_pct_of_high_vol_days_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Of days with vol>=2x mean in 63d window, fraction that were also churn days.
    Measures how often extreme volume produced no price follow-through.
    """
    high_vol = (volume >= 2.0 * _rolling_mean(volume, _TD_MON)).astype(float)
    churn = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)
    hv_count = high_vol.rolling(_TD_QTR, min_periods=1).sum().replace(0, np.nan)
    churn_count = churn.rolling(_TD_QTR, min_periods=1).sum()
    return _safe_div(churn_count, hv_count)


def vcx_ext_020_days_since_last_churn(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Days since the most recent churn bar (vol>=2x mean, |ret|<=0.5%).
    Low values: recent churn = potential distribution or absorption ongoing.
    """
    flag = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)

    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))

    return flag.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)


def vcx_ext_021_days_since_last_churn_body(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Days since the most recent body-churn bar (vol>=2x mean, |body/open|<=0.5%).
    """
    flag = vcx_ext_012_churn_flag_vol2x_body05pct(close, open, volume)

    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))

    return flag.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)


def vcx_ext_022_churn_vol_share_of_total_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Fraction of 63-day cumulative volume attributable to churn bars.
    High value = most extreme volume came on no-progress days (distribution signature).
    """
    flag = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume)
    churn_vol = (volume * flag).rolling(_TD_QTR, min_periods=1).sum()
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(churn_vol, total_vol)


# --- Group C (023-034): Churn at/near lows ---

def vcx_ext_023_churn_at_low_flag_21d(
    close: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Churn at a 21-day low: churn bar AND close is within 2% of rolling 21d low.
    Classic absorption / selling exhaustion at the lows.
    """
    churn = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume).astype(bool)
    low21 = _rolling_min(close, _TD_MON)
    near_low = (close <= low21 * 1.02)
    return (churn & near_low).astype(float)


def vcx_ext_024_churn_at_low_flag_63d(
    close: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Churn at a 63-day low: churn bar AND close within 2% of rolling 63d low.
    """
    churn = vcx_ext_011_churn_flag_vol2x_ret05pct(close, volume).astype(bool)
    low63 = _rolling_min(close, _TD_QTR)
    near_low = (close <= low63 * 1.02)
    return (churn & near_low).astype(float)


def vcx_ext_025_churn_at_low_count_63d(
    close: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of churn-at-63d-low bars occurring in trailing 63 days.
    """
    flag = vcx_ext_024_churn_at_low_flag_63d(close, low, volume)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_026_churn_at_low_count_252d(
    close: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of churn-at-63d-low bars occurring in trailing 252 days.
    """
    flag = vcx_ext_024_churn_at_low_flag_63d(close, low, volume)
    return flag.rolling(_TD_YEAR, min_periods=1).sum()


def vcx_ext_027_churn_near_low_vol_share_63d(
    close: pd.Series, low: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Volume on churn-at-63d-low bars as fraction of total 63d volume.
    """
    flag = vcx_ext_024_churn_at_low_flag_63d(close, low, volume)
    churn_vol = (volume * flag).rolling(_TD_QTR, min_periods=1).sum()
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(churn_vol, total_vol)


def vcx_ext_028_vol_up_price_flat_flag(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Volume-up-but-price-flat flag: today's volume > yesterday's AND |return| < 0.3%.
    Detects single-bar absorption / no-follow-through when volume surges.
    """
    vol_up = volume > volume.shift(1)
    price_flat = close.pct_change(1).abs() < 0.003
    return (vol_up & price_flat).astype(float)


def vcx_ext_029_vol_up_price_flat_count_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of vol-up-price-flat bars in trailing 21 days.
    """
    flag = vcx_ext_028_vol_up_price_flat_flag(close, volume)
    return flag.rolling(_TD_MON, min_periods=1).sum()


def vcx_ext_030_vol_up_price_flat_count_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of vol-up-price-flat bars in trailing 63 days.
    """
    flag = vcx_ext_028_vol_up_price_flat_flag(close, volume)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_031_net_price_move_per_cumvol_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Net signed price change over 21d divided by cumulative 21d volume.
    Distinct from ext_009: uses net (signed) rather than abs cumulative return.
    Measures price efficiency of volume — near zero = whipsaw/churn.
    """
    net_ret = close.pct_change(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vol_cum = _rolling_sum(volume, _TD_MON)
    return _safe_div(net_ret, vol_cum)


def vcx_ext_032_net_price_move_per_cumvol_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Net signed price change over 63d divided by cumulative 63d volume.
    """
    net_ret = close.pct_change(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vol_cum = _rolling_sum(volume, _TD_QTR)
    return _safe_div(net_ret, vol_cum)


def vcx_ext_033_price_range_per_cumvol_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Rolling 21d (max_close - min_close) / cumulative_volume.
    How much total price territory was covered per unit of cumulative volume.
    Low = lots of volume for narrow net territory = churn / congestion.
    """
    price_range = (
        close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max()
        - close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    )
    vol_cum = _rolling_sum(volume, _TD_MON)
    return _safe_div(price_range, vol_cum)


def vcx_ext_034_price_range_per_cumvol_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Rolling 63d (max_close - min_close) / cumulative_volume.
    """
    price_range = (
        close.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
        - close.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    )
    vol_cum = _rolling_sum(volume, _TD_QTR)
    return _safe_div(price_range, vol_cum)


# --- Group D (035-046): Climax-then-no-follow-through ---

def vcx_ext_035_climax_no_followthrough_1d_flag(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Flag: 63-day peak-volume day occurred yesterday (today = day after climax)
    AND today's close-to-close return is <= 0 (no upside follow-through).
    Detects failure to follow through on the session after a volume climax.
    """
    mx = _rolling_max(volume, _TD_QTR)
    was_climax_yesterday = (volume.shift(1) >= mx.shift(1))
    no_followthrough = (close.pct_change(1) <= 0.0)
    return (was_climax_yesterday & no_followthrough).astype(float)


def vcx_ext_036_climax_no_followthrough_1d_magnitude(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Next-bar return after 63d climax, clipped to negative values only.
    Captures how bad the no-follow-through reversal was.
    """
    mx = _rolling_max(volume, _TD_QTR)
    was_climax = (volume >= mx)
    ret_next = close.pct_change(1).shift(-1)
    val = ret_next.where(was_climax, np.nan).ffill().clip(upper=0.0)
    return val


def vcx_ext_037_climax_no_followthrough_5d_flag(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Flag: 63d peak-volume day occurred within last 5 days AND the 5-day cumulative
    return since that climax is <= 0 (no medium-term follow-through).
    """
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx).astype(float)
    climax_in_5d = is_climax.rolling(_TD_WEEK, min_periods=1).max()
    ret5 = close.pct_change(5)
    return ((climax_in_5d > 0) & (ret5 <= 0.0)).astype(float)


def vcx_ext_038_climax_followthrough_return_5d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    5-day forward return starting from the day after the most recent 63d climax.
    Carried forward for comparison. Measures follow-through quality.
    NB: uses shift(-5) internally but only reads past prices forward-shifted to look backward.
    Uses the climax day's 5-period-ahead return (backward-carried from future obs).
    Implementation: at climax bar, record ret5 = close[t+5]/close[t]-1, then ffill.
    Since we cannot shift forward, we compute 5d trailing return and lag by 5.
    """
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    ret5 = close.pct_change(5).shift(-5)
    val = ret5.where(is_climax, np.nan).ffill()
    return val


def vcx_ext_039_climax_vol_vs_window_total_21d(
    volume: pd.Series
) -> pd.Series:
    """
    Single-bar climax volume as a fraction of the entire 21d window's total volume.
    Different from vcx_073: uses today's volume, not rolling max, vs the window total.
    Measures today's volume dominance within the recent window.
    """
    total = _rolling_sum(volume, _TD_MON)
    return _safe_div(volume, total)


def vcx_ext_040_climax_vol_vs_window_total_63d(
    volume: pd.Series
) -> pd.Series:
    """
    Today's volume as fraction of the 63d window's total volume.
    """
    total = _rolling_sum(volume, _TD_QTR)
    return _safe_div(volume, total)


def vcx_ext_041_two_bar_climax_cluster_flag_21d(
    volume: pd.Series
) -> pd.Series:
    """
    Two-bar cluster flag: both today AND yesterday had volume >= 2x 21d rolling mean.
    Consecutive extreme volume days signal sustained institutional activity.
    """
    mean21 = _rolling_mean(volume, _TD_MON)
    high_today = volume >= 2.0 * mean21
    high_yest = volume.shift(1) >= 2.0 * mean21.shift(1)
    return (high_today & high_yest).astype(float)


def vcx_ext_042_two_bar_climax_cluster_flag_63d(
    volume: pd.Series
) -> pd.Series:
    """
    Two-bar cluster flag: both today and yesterday hit 63d rolling max volume.
    """
    mx = _rolling_max(volume, _TD_QTR)
    high_today = volume >= mx
    high_yest = volume.shift(1) >= mx.shift(1)
    return (high_today & high_yest).astype(float)


def vcx_ext_043_two_bar_cluster_count_63d(
    volume: pd.Series
) -> pd.Series:
    """
    Count of two-bar climax cluster days (vol>=2x mean) in trailing 63 days.
    """
    flag = vcx_ext_041_two_bar_climax_cluster_flag_21d(volume)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_044_climax_then_collapse_vol_flag(
    volume: pd.Series
) -> pd.Series:
    """
    Climax exhaustion flag: yesterday was a 21d volume climax AND today's volume
    is below the 21d rolling mean (volume collapsed after climax = exhaustion).
    """
    mx = _rolling_max(volume, _TD_MON)
    was_climax = (volume.shift(1) >= mx.shift(1))
    vol_collapsed = (volume < _rolling_mean(volume, _TD_MON))
    return (was_climax & vol_collapsed).astype(float)


def vcx_ext_045_climax_exhaustion_vol_ratio(
    volume: pd.Series
) -> pd.Series:
    """
    Volume-collapse ratio: today's volume divided by yesterday's, carried forward
    only on days following a 21d climax. Low values = steep post-climax fade.
    """
    mx = _rolling_max(volume, _TD_MON)
    was_climax = (volume.shift(1) >= mx.shift(1))
    ratio = _safe_div(volume, volume.shift(1))
    return ratio.where(was_climax, np.nan).ffill()


def vcx_ext_046_climax_exhaustion_5d_vol_decay(
    volume: pd.Series
) -> pd.Series:
    """
    5-day volume decay after a 21d climax: (5d future mean vol) / (climax vol).
    Carried forward from the climax day. Low = rapid post-climax volume collapse.
    Uses backward approach: 5d-ahead mean is lagged 5 days (shift(-5)) avoided;
    instead we compute trailing 5d mean after any climax event.
    """
    mx = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx)
    climax_vol = volume.where(is_climax, np.nan).ffill()
    mean5_trailing = _rolling_mean(volume, _TD_WEEK)
    return _safe_div(mean5_trailing, climax_vol)


# --- Group E (047-057): Intraday reversal on climax bars ---

def vcx_ext_047_climax_intraday_reversal_score_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    On the 21d peak-volume day: intraday reversal = (high - close) / (high - low).
    Near 1 = closed at the low (bearish reversal from high); near 0 = held gains.
    Carried forward between climax days.
    """
    rng = (high - low).replace(0, np.nan)
    reversal = _safe_div(high - close, rng)
    mx = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx)
    return reversal.where(is_climax, np.nan).ffill()


def vcx_ext_048_climax_intraday_reversal_score_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    On the 63d peak-volume day: intraday reversal = (high - close) / (high - low).
    """
    rng = (high - low).replace(0, np.nan)
    reversal = _safe_div(high - close, rng)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return reversal.where(is_climax, np.nan).ffill()


def vcx_ext_049_climax_intraday_reversal_flag_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Flag: the 21d peak-volume day also had a significant intraday reversal
    (closed in the bottom 30% of its range), suggesting selling into strength.
    """
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    reversal_flag = (pos <= 0.30)
    mx = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx)
    flag = (is_climax & reversal_flag).astype(float)
    return flag.where(is_climax, np.nan).ffill()


def vcx_ext_050_climax_intraday_reversal_flag_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Flag: the 63d peak-volume day had a significant intraday reversal
    (closed in the bottom 30% of its range).
    """
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    reversal_flag = (pos <= 0.30)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    flag = (is_climax & reversal_flag).astype(float)
    return flag.where(is_climax, np.nan).ffill()


def vcx_ext_051_climax_open_to_high_vs_high_to_close_21d(
    high: pd.Series, close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    On the 21d peak-volume day: (high - open) / (high - close).
    High ratio = price was pushed to the high then reversed hard to close = distribution.
    """
    num = (high - open).clip(lower=0)
    den = (high - close).clip(lower=_EPS)
    ratio = _safe_div(num, den)
    mx = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx)
    return ratio.where(is_climax, np.nan).ffill()


def vcx_ext_052_climax_open_to_high_vs_high_to_close_63d(
    high: pd.Series, close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    On the 63d peak-volume day: (high - open) / (high - close).
    """
    num = (high - open).clip(lower=0)
    den = (high - close).clip(lower=_EPS)
    ratio = _safe_div(num, den)
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    return ratio.where(is_climax, np.nan).ffill()


def vcx_ext_053_today_intraday_reversal_vol_weighted_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Rolling 21d mean of (intraday reversal score * volume_z_score).
    Captures how much reversal activity is volume-weighted — heavy volume + reversal = churn.
    """
    rng = (high - low).replace(0, np.nan)
    reversal = _safe_div(high - close, rng)
    vol_z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    combined = reversal * vol_z
    return _rolling_mean(combined, _TD_MON)


def vcx_ext_054_today_intraday_reversal_vol_weighted_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Rolling 63d mean of (intraday reversal score * volume_z_score).
    """
    rng = (high - low).replace(0, np.nan)
    reversal = _safe_div(high - close, rng)
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    combined = reversal * vol_z
    return _rolling_mean(combined, _TD_QTR)


# --- Group F (055-065): Climax magnitude and intensity rate-of-change ---

def vcx_ext_055_largest_vol_bar_vs_window_mean_21d(
    volume: pd.Series
) -> pd.Series:
    """
    The magnitude of the single largest volume bar in 21d vs the window mean.
    Distinct from vcx_005: measures raw multiple, not rolling max vs mean of same window.
    Uses current bar's volume multiple to assess today's spike magnitude directly.
    """
    return _safe_div(volume, _rolling_mean(volume, _TD_MON))


def vcx_ext_056_largest_vol_bar_vs_window_mean_63d(
    volume: pd.Series
) -> pd.Series:
    """
    Today's volume as multiple of the 63d window mean.
    """
    return _safe_div(volume, _rolling_mean(volume, _TD_QTR))


def vcx_ext_057_climax_intensity_roc_5d(
    volume: pd.Series
) -> pd.Series:
    """
    Rate of change of (today's volume z-score over 63d) over the last 5 days.
    Captures whether climax intensity is accelerating or decelerating.
    """
    z = _vol_zscore(volume, _TD_QTR)
    return z - z.shift(_TD_WEEK)


def vcx_ext_058_climax_intensity_roc_21d(
    volume: pd.Series
) -> pd.Series:
    """
    Rate of change of (today's volume z-score over 63d) over the last 21 days.
    """
    z = _vol_zscore(volume, _TD_QTR)
    return z - z.shift(_TD_MON)


def vcx_ext_059_effort_result_roc_5d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    5-day rate of change of the effort-vs-result ratio (vcx_ext_002 style).
    Rising = volume increasingly failing to move price.
    """
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    ratio = _safe_div(vol_z, ret_abs)
    return ratio - ratio.shift(_TD_WEEK)


def vcx_ext_060_effort_result_roc_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    21-day rate of change of the effort-vs-result ratio.
    """
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs().replace(0, np.nan)
    ratio = _safe_div(vol_z, ret_abs)
    return ratio - ratio.shift(_TD_MON)


def vcx_ext_061_climax_vol_multiple_ewm_trend(
    volume: pd.Series
) -> pd.Series:
    """
    EWM(21d) of (vol / 63d-mean-vol) — smoothed trend of single-bar climax multiple.
    Captures whether single-bar extremity is trending up (escalating distress).
    """
    mult = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return _ewm_mean(mult, _TD_MON)


def vcx_ext_062_climax_window_vol_share_trend_5d(
    volume: pd.Series
) -> pd.Series:
    """
    5-day diff of (today's vol / 21d-total-vol) share.
    Rising = today is capturing an increasing share of window volume (escalating climax).
    """
    share = _safe_div(volume, _rolling_sum(volume, _TD_MON))
    return share - share.shift(_TD_WEEK)


def vcx_ext_063_climax_intensity_ewm_crossover(
    volume: pd.Series
) -> pd.Series:
    """
    Fast EWM(5d) minus slow EWM(21d) of (vol / 63d-mean-vol).
    Positive = short-term climax intensity accelerating vs medium-term level.
    """
    mult = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    fast = _ewm_mean(mult, _TD_WEEK)
    slow = _ewm_mean(mult, _TD_MON)
    return fast - slow


# --- Group G (064-075): Composite / advanced churn and effort-result signals ---

def vcx_ext_064_churn_composite_score_21d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Composite churn score: vol_multiple * (1 - abs_return_pct) * (1 - body_pct_range).
    High = extreme volume, tiny return, tiny body = strongest churn signal.
    All sub-components clipped to [0, 1] before multiplication.
    """
    vol_mult = _safe_div(volume, _rolling_mean(volume, _TD_MON)).clip(lower=0.0, upper=10.0)
    ret_inv = (1.0 - close.pct_change(1).abs().clip(0.0, 1.0))
    rng = (high - low).replace(0, np.nan)
    body_frac = _safe_div(_body(close, open), rng).fillna(0.0).clip(0.0, 1.0)
    body_inv = 1.0 - body_frac
    return vol_mult * ret_inv * body_inv


def vcx_ext_065_churn_composite_score_63d(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Composite churn score using 63d volume mean baseline.
    """
    vol_mult = _safe_div(volume, _rolling_mean(volume, _TD_QTR)).clip(lower=0.0, upper=10.0)
    ret_inv = (1.0 - close.pct_change(1).abs().clip(0.0, 1.0))
    rng = (high - low).replace(0, np.nan)
    body_frac = _safe_div(_body(close, open), rng).fillna(0.0).clip(0.0, 1.0)
    body_inv = 1.0 - body_frac
    return vol_mult * ret_inv * body_inv


def vcx_ext_066_churn_score_21d_rolling_mean(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    21-day rolling mean of the daily composite churn score (21d baseline).
    A sustained elevated score indicates ongoing churn / distribution.
    """
    score = vcx_ext_064_churn_composite_score_21d(close, high, low, open, volume)
    return _rolling_mean(score, _TD_MON)


def vcx_ext_067_churn_score_63d_rolling_mean(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    63-day rolling mean of the daily composite churn score (63d baseline).
    """
    score = vcx_ext_065_churn_composite_score_63d(close, high, low, open, volume)
    return _rolling_mean(score, _TD_QTR)


def vcx_ext_068_climax_bar_effort_vs_window_effort_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    On the most recent 21d climax bar: ratio of climax-day effort (vol_z * abs_ret)
    to the window's average daily effort.
    Near 1 = climax was only as productive as an average day despite extreme volume.
    """
    mx = _rolling_max(volume, _TD_MON)
    is_climax = (volume >= mx)
    vol_z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs()
    daily_effort = vol_z * ret_abs
    climax_effort = daily_effort.where(is_climax, np.nan).ffill()
    mean_effort = _rolling_mean(daily_effort, _TD_MON)
    return _safe_div(climax_effort, mean_effort)


def vcx_ext_069_climax_bar_effort_vs_window_effort_63d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    On the most recent 63d climax bar: climax-day effort vs 63d window mean effort.
    """
    mx = _rolling_max(volume, _TD_QTR)
    is_climax = (volume >= mx)
    vol_z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    ret_abs = close.pct_change(1).abs()
    daily_effort = vol_z * ret_abs
    climax_effort = daily_effort.where(is_climax, np.nan).ffill()
    mean_effort = _rolling_mean(daily_effort, _TD_QTR)
    return _safe_div(climax_effort, mean_effort)


def vcx_ext_070_high_vol_low_range_count_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of bars in 21d where volume >= 2x mean AND HL range < 50% of 21d ATR.
    Measures bars with extreme volume but compressed range (stalling/absorption).
    """
    high_vol = volume >= 2.0 * _rolling_mean(volume, _TD_MON)
    atr21 = _rolling_mean(_range_hl(high, low), _TD_MON)
    narrow_range = _range_hl(high, low) < 0.5 * atr21
    flag = (high_vol & narrow_range).astype(float)
    return flag.rolling(_TD_MON, min_periods=1).sum()


def vcx_ext_071_high_vol_low_range_count_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Count of bars in 63d where volume >= 2x mean AND HL range < 50% of 63d ATR.
    """
    high_vol = volume >= 2.0 * _rolling_mean(volume, _TD_QTR)
    atr63 = _rolling_mean(_range_hl(high, low), _TD_QTR)
    narrow_range = _range_hl(high, low) < 0.5 * atr63
    flag = (high_vol & narrow_range).astype(float)
    return flag.rolling(_TD_QTR, min_periods=1).sum()


def vcx_ext_072_effort_result_body_zscore_63d(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Z-score of daily (vol_mult / body_pct) ratio within 63d window.
    High z-score = today's volume produced an unusually tiny body vs recent history.
    """
    vol_mult = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    body_pct = _safe_div(_body(close, open), open.replace(0, np.nan)).replace(0, np.nan)
    raw = _safe_div(vol_mult, body_pct)
    m = _rolling_mean(raw, _TD_QTR)
    s = _rolling_std(raw, _TD_QTR)
    return _safe_div(raw - m, s)


def vcx_ext_073_churn_at_low_composite_score(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Composite churn-at-low score: churn_score_21d * near_low_flag (within 3% of 63d low).
    Highest when distribution/absorption occurs near multi-month price lows.
    """
    churn = vcx_ext_064_churn_composite_score_21d(close, high, low, open, volume)
    low63 = _rolling_min(close, _TD_QTR)
    near_low = (close <= low63 * 1.03).astype(float)
    return churn * near_low


def vcx_ext_074_cumvol_progress_ratio_trend_21d(
    close: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    21-day trend slope of (abs_ret_cumsum / cum_volume) — whether price efficiency
    of volume is deteriorating (declining slope = increasing churn over time).
    """
    daily_eff = _safe_div(close.pct_change(1).abs(), volume.replace(0, np.nan))
    return _rolling_mean(daily_eff, _TD_MON)


def vcx_ext_075_churn_exhaustion_composite(
    close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series,
    volume: pd.Series
) -> pd.Series:
    """
    Final composite: churn_score_63d * climax_exhaustion_vol_ratio (5d decay).
    Peaks when heavy churn is followed by an immediate volume collapse —
    the strongest signature of distribution / selling exhaustion.
    """
    churn = vcx_ext_065_churn_composite_score_63d(close, high, low, open, volume)
    exhaustion = vcx_ext_046_climax_exhaustion_5d_vol_decay(volume)
    inv_exhaust = (1.0 - exhaustion.clip(0.0, 1.0))
    return churn * inv_exhaust


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CLIMAX_EXTENDED_REGISTRY_001_075 = {
    "vcx_ext_001_effort_result_ratio_return_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_001_effort_result_ratio_return_21d},
    "vcx_ext_002_effort_result_ratio_return_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_002_effort_result_ratio_return_63d},
    "vcx_ext_003_effort_result_ratio_body_21d": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_003_effort_result_ratio_body_21d},
    "vcx_ext_004_effort_result_ratio_body_63d": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_004_effort_result_ratio_body_63d},
    "vcx_ext_005_effort_result_ratio_range_21d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_005_effort_result_ratio_range_21d},
    "vcx_ext_006_effort_result_ratio_range_63d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_006_effort_result_ratio_range_63d},
    "vcx_ext_007_effort_result_zscore_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_007_effort_result_zscore_21d},
    "vcx_ext_008_effort_result_zscore_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_008_effort_result_zscore_63d},
    "vcx_ext_009_price_progress_per_unit_volume_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_009_price_progress_per_unit_volume_21d},
    "vcx_ext_010_price_progress_per_unit_volume_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_010_price_progress_per_unit_volume_63d},
    "vcx_ext_011_churn_flag_vol2x_ret05pct": {
        "inputs": ["close", "volume"], "func": vcx_ext_011_churn_flag_vol2x_ret05pct},
    "vcx_ext_012_churn_flag_vol2x_body05pct": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_012_churn_flag_vol2x_body05pct},
    "vcx_ext_013_churn_flag_vol3x_ret1pct": {
        "inputs": ["close", "volume"], "func": vcx_ext_013_churn_flag_vol3x_ret1pct},
    "vcx_ext_014_churn_count_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_014_churn_count_21d},
    "vcx_ext_015_churn_count_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_015_churn_count_63d},
    "vcx_ext_016_churn_count_252d": {
        "inputs": ["close", "volume"], "func": vcx_ext_016_churn_count_252d},
    "vcx_ext_017_churn_body_count_21d": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_017_churn_body_count_21d},
    "vcx_ext_018_churn_body_count_63d": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_018_churn_body_count_63d},
    "vcx_ext_019_churn_pct_of_high_vol_days_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_019_churn_pct_of_high_vol_days_63d},
    "vcx_ext_020_days_since_last_churn": {
        "inputs": ["close", "volume"], "func": vcx_ext_020_days_since_last_churn},
    "vcx_ext_021_days_since_last_churn_body": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_021_days_since_last_churn_body},
    "vcx_ext_022_churn_vol_share_of_total_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_022_churn_vol_share_of_total_63d},
    "vcx_ext_023_churn_at_low_flag_21d": {
        "inputs": ["close", "low", "volume"], "func": vcx_ext_023_churn_at_low_flag_21d},
    "vcx_ext_024_churn_at_low_flag_63d": {
        "inputs": ["close", "low", "volume"], "func": vcx_ext_024_churn_at_low_flag_63d},
    "vcx_ext_025_churn_at_low_count_63d": {
        "inputs": ["close", "low", "volume"], "func": vcx_ext_025_churn_at_low_count_63d},
    "vcx_ext_026_churn_at_low_count_252d": {
        "inputs": ["close", "low", "volume"], "func": vcx_ext_026_churn_at_low_count_252d},
    "vcx_ext_027_churn_near_low_vol_share_63d": {
        "inputs": ["close", "low", "volume"], "func": vcx_ext_027_churn_near_low_vol_share_63d},
    "vcx_ext_028_vol_up_price_flat_flag": {
        "inputs": ["close", "volume"], "func": vcx_ext_028_vol_up_price_flat_flag},
    "vcx_ext_029_vol_up_price_flat_count_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_029_vol_up_price_flat_count_21d},
    "vcx_ext_030_vol_up_price_flat_count_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_030_vol_up_price_flat_count_63d},
    "vcx_ext_031_net_price_move_per_cumvol_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_031_net_price_move_per_cumvol_21d},
    "vcx_ext_032_net_price_move_per_cumvol_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_032_net_price_move_per_cumvol_63d},
    "vcx_ext_033_price_range_per_cumvol_21d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_033_price_range_per_cumvol_21d},
    "vcx_ext_034_price_range_per_cumvol_63d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_034_price_range_per_cumvol_63d},
    "vcx_ext_035_climax_no_followthrough_1d_flag": {
        "inputs": ["close", "volume"], "func": vcx_ext_035_climax_no_followthrough_1d_flag},
    "vcx_ext_036_climax_no_followthrough_1d_magnitude": {
        "inputs": ["close", "volume"], "func": vcx_ext_036_climax_no_followthrough_1d_magnitude},
    "vcx_ext_037_climax_no_followthrough_5d_flag": {
        "inputs": ["close", "volume"], "func": vcx_ext_037_climax_no_followthrough_5d_flag},
    "vcx_ext_038_climax_followthrough_return_5d": {
        "inputs": ["close", "volume"], "func": vcx_ext_038_climax_followthrough_return_5d},
    "vcx_ext_039_climax_vol_vs_window_total_21d": {
        "inputs": ["volume"], "func": vcx_ext_039_climax_vol_vs_window_total_21d},
    "vcx_ext_040_climax_vol_vs_window_total_63d": {
        "inputs": ["volume"], "func": vcx_ext_040_climax_vol_vs_window_total_63d},
    "vcx_ext_041_two_bar_climax_cluster_flag_21d": {
        "inputs": ["volume"], "func": vcx_ext_041_two_bar_climax_cluster_flag_21d},
    "vcx_ext_042_two_bar_climax_cluster_flag_63d": {
        "inputs": ["volume"], "func": vcx_ext_042_two_bar_climax_cluster_flag_63d},
    "vcx_ext_043_two_bar_cluster_count_63d": {
        "inputs": ["volume"], "func": vcx_ext_043_two_bar_cluster_count_63d},
    "vcx_ext_044_climax_then_collapse_vol_flag": {
        "inputs": ["volume"], "func": vcx_ext_044_climax_then_collapse_vol_flag},
    "vcx_ext_045_climax_exhaustion_vol_ratio": {
        "inputs": ["volume"], "func": vcx_ext_045_climax_exhaustion_vol_ratio},
    "vcx_ext_046_climax_exhaustion_5d_vol_decay": {
        "inputs": ["volume"], "func": vcx_ext_046_climax_exhaustion_5d_vol_decay},
    "vcx_ext_047_climax_intraday_reversal_score_21d": {
        "inputs": ["high", "low", "close", "open", "volume"], "func": vcx_ext_047_climax_intraday_reversal_score_21d},
    "vcx_ext_048_climax_intraday_reversal_score_63d": {
        "inputs": ["high", "low", "close", "open", "volume"], "func": vcx_ext_048_climax_intraday_reversal_score_63d},
    "vcx_ext_049_climax_intraday_reversal_flag_21d": {
        "inputs": ["high", "low", "close", "open", "volume"], "func": vcx_ext_049_climax_intraday_reversal_flag_21d},
    "vcx_ext_050_climax_intraday_reversal_flag_63d": {
        "inputs": ["high", "low", "close", "open", "volume"], "func": vcx_ext_050_climax_intraday_reversal_flag_63d},
    "vcx_ext_051_climax_open_to_high_vs_high_to_close_21d": {
        "inputs": ["high", "close", "open", "volume"], "func": vcx_ext_051_climax_open_to_high_vs_high_to_close_21d},
    "vcx_ext_052_climax_open_to_high_vs_high_to_close_63d": {
        "inputs": ["high", "close", "open", "volume"], "func": vcx_ext_052_climax_open_to_high_vs_high_to_close_63d},
    "vcx_ext_053_today_intraday_reversal_vol_weighted_21d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_053_today_intraday_reversal_vol_weighted_21d},
    "vcx_ext_054_today_intraday_reversal_vol_weighted_63d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_054_today_intraday_reversal_vol_weighted_63d},
    "vcx_ext_055_largest_vol_bar_vs_window_mean_21d": {
        "inputs": ["volume"], "func": vcx_ext_055_largest_vol_bar_vs_window_mean_21d},
    "vcx_ext_056_largest_vol_bar_vs_window_mean_63d": {
        "inputs": ["volume"], "func": vcx_ext_056_largest_vol_bar_vs_window_mean_63d},
    "vcx_ext_057_climax_intensity_roc_5d": {
        "inputs": ["volume"], "func": vcx_ext_057_climax_intensity_roc_5d},
    "vcx_ext_058_climax_intensity_roc_21d": {
        "inputs": ["volume"], "func": vcx_ext_058_climax_intensity_roc_21d},
    "vcx_ext_059_effort_result_roc_5d": {
        "inputs": ["close", "volume"], "func": vcx_ext_059_effort_result_roc_5d},
    "vcx_ext_060_effort_result_roc_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_060_effort_result_roc_21d},
    "vcx_ext_061_climax_vol_multiple_ewm_trend": {
        "inputs": ["volume"], "func": vcx_ext_061_climax_vol_multiple_ewm_trend},
    "vcx_ext_062_climax_window_vol_share_trend_5d": {
        "inputs": ["volume"], "func": vcx_ext_062_climax_window_vol_share_trend_5d},
    "vcx_ext_063_climax_intensity_ewm_crossover": {
        "inputs": ["volume"], "func": vcx_ext_063_climax_intensity_ewm_crossover},
    "vcx_ext_064_churn_composite_score_21d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_064_churn_composite_score_21d},
    "vcx_ext_065_churn_composite_score_63d": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_065_churn_composite_score_63d},
    "vcx_ext_066_churn_score_21d_rolling_mean": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_066_churn_score_21d_rolling_mean},
    "vcx_ext_067_churn_score_63d_rolling_mean": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_067_churn_score_63d_rolling_mean},
    "vcx_ext_068_climax_bar_effort_vs_window_effort_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_068_climax_bar_effort_vs_window_effort_21d},
    "vcx_ext_069_climax_bar_effort_vs_window_effort_63d": {
        "inputs": ["close", "volume"], "func": vcx_ext_069_climax_bar_effort_vs_window_effort_63d},
    "vcx_ext_070_high_vol_low_range_count_21d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_070_high_vol_low_range_count_21d},
    "vcx_ext_071_high_vol_low_range_count_63d": {
        "inputs": ["high", "low", "close", "volume"], "func": vcx_ext_071_high_vol_low_range_count_63d},
    "vcx_ext_072_effort_result_body_zscore_63d": {
        "inputs": ["close", "open", "volume"], "func": vcx_ext_072_effort_result_body_zscore_63d},
    "vcx_ext_073_churn_at_low_composite_score": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_073_churn_at_low_composite_score},
    "vcx_ext_074_cumvol_progress_ratio_trend_21d": {
        "inputs": ["close", "volume"], "func": vcx_ext_074_cumvol_progress_ratio_trend_21d},
    "vcx_ext_075_churn_exhaustion_composite": {
        "inputs": ["close", "high", "low", "open", "volume"], "func": vcx_ext_075_churn_exhaustion_composite},
}
