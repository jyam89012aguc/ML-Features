"""
34_velocity_inflection — Extended Features 001-075
Domain: velocity inflection extended variants — new smoothing methods (WMA, DEMA, TEMA,
        Hull MA velocity), velocity sign-flip counts on alternate price series (HL2, HLC3,
        OHLC4), EMA-velocity crossovers with additional spans, percentile ranks and z-scores
        on inflection density, curvature magnitude transforms, volume-surge at inflection,
        regime flags combining multi-span sign agreement, acceleration ratio features,
        inter-inflection duration statistics.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _velocity(close: pd.Series, span: int) -> pd.Series:
    """EMA-smoothed 1-day log-return (price velocity)."""
    lr = _log_safe(close).diff(1)
    return _ewm_mean(lr, span)


def _sign_flip(s: pd.Series) -> pd.Series:
    """Binary: 1 where sign of s differs from prior row."""
    sg = np.sign(s)
    return ((sg != sg.shift(1)) & sg.notna() & sg.shift(1).notna()).astype(float)


def _days_since_flip(flip: pd.Series) -> pd.Series:
    """Bars elapsed since last 1 in binary flip series (backward-looking)."""
    idx = np.arange(len(flip))
    last_flip_idx = pd.Series(np.where(flip.values == 1, idx, np.nan))
    last_flip_idx = last_flip_idx.ffill()
    result = pd.Series(idx, index=flip.index, dtype=float) - last_flip_idx.values
    result[last_flip_idx.isna().values] = np.nan
    return result


def _rolling_count(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_true(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _wma(s: pd.Series, w: int) -> pd.Series:
    """Weighted moving average (linearly-weighted, recent bar = highest weight)."""
    weights = np.arange(1, w + 1, dtype=float)
    def _wma_apply(x):
        if len(x) < max(1, w // 2):
            return np.nan
        wts = weights[-len(x):]
        return float(np.dot(x, wts) / wts.sum())
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_wma_apply, raw=True)


def _hull_ma(s: pd.Series, w: int) -> pd.Series:
    """Hull Moving Average of s over period w."""
    half_w = max(2, w // 2)
    sqrt_w = max(2, int(round(w ** 0.5)))
    wma_half = _wma(s, half_w)
    wma_full = _wma(s, w)
    raw = 2.0 * wma_half - wma_full
    return _wma(raw, sqrt_w)


def _dema(s: pd.Series, span: int) -> pd.Series:
    """Double EMA (DEMA = 2*EMA - EMA(EMA))."""
    e1 = _ewm_mean(s, span)
    e2 = _ewm_mean(e1, span)
    return 2.0 * e1 - e2


def _tema(s: pd.Series, span: int) -> pd.Series:
    """Triple EMA (TEMA = 3*EMA - 3*EMA(EMA) + EMA(EMA(EMA)))."""
    e1 = _ewm_mean(s, span)
    e2 = _ewm_mean(e1, span)
    e3 = _ewm_mean(e2, span)
    return 3.0 * e1 - 3.0 * e2 + e3


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Velocity using alternative smoothing: WMA, Hull, DEMA, TEMA ---

def vif_ext_001_wma5_vel_sign(close: pd.Series) -> pd.Series:
    """Sign of 1-day change in 5-bar WMA (WMA velocity direction)."""
    return np.sign(_wma(close, _TD_WEEK).diff(1)).astype(float)


def vif_ext_002_wma5_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: 5-bar WMA velocity (1-day diff) changed sign today."""
    return _sign_flip(_wma(close, _TD_WEEK).diff(1))


def vif_ext_003_wma21_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: 21-bar WMA velocity changed sign today."""
    return _sign_flip(_wma(close, _TD_MON).diff(1))


def vif_ext_004_hull5_vel_sign(close: pd.Series) -> pd.Series:
    """Sign of 1-day diff of Hull MA(5) — fast noise-reduced velocity direction."""
    return np.sign(_hull_ma(close, _TD_WEEK).diff(1)).astype(float)


def vif_ext_005_hull5_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: Hull MA(5) 1-day diff changed sign today."""
    return _sign_flip(_hull_ma(close, _TD_WEEK).diff(1))


def vif_ext_006_hull21_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: Hull MA(21) 1-day diff changed sign today."""
    return _sign_flip(_hull_ma(close, _TD_MON).diff(1))


def vif_ext_007_dema5_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: DEMA(5) slope changed sign today (double-smoothed inflection)."""
    return _sign_flip(_dema(close, _TD_WEEK).diff(1))


def vif_ext_008_dema21_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: DEMA(21) slope changed sign today."""
    return _sign_flip(_dema(close, _TD_MON).diff(1))


def vif_ext_009_tema5_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: TEMA(5) slope changed sign today (triple-smoothed inflection)."""
    return _sign_flip(_tema(close, _TD_WEEK).diff(1))


def vif_ext_010_tema21_vel_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: TEMA(21) slope changed sign today."""
    return _sign_flip(_tema(close, _TD_MON).diff(1))


def vif_ext_011_hull5_vel_flip_count_21d(close: pd.Series) -> pd.Series:
    """Count of Hull MA(5) velocity sign-flips in trailing 21 days."""
    return _rolling_count(_sign_flip(_hull_ma(close, _TD_WEEK).diff(1)), _TD_MON)


def vif_ext_012_hull21_vel_flip_count_63d(close: pd.Series) -> pd.Series:
    """Count of Hull MA(21) velocity sign-flips in trailing 63 days."""
    return _rolling_count(_sign_flip(_hull_ma(close, _TD_MON).diff(1)), _TD_QTR)


# --- Group B (013-022): Velocity on alternative price series (HL2, HLC3, OHLC4, typical) ---

def vif_ext_013_hl2_vel_ema5_flip_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity of HL2=(H+L)/2 changed sign today."""
    hl2 = (high + low) / 2.0
    return _sign_flip(_velocity(hl2, _TD_WEEK))


def vif_ext_014_hlc3_vel_ema5_flip_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity of HLC3=(H+L+C)/3 changed sign today."""
    hlc3 = (high + low + close) / 3.0
    return _sign_flip(_velocity(hlc3, _TD_WEEK))


def vif_ext_015_ohlc4_vel_ema5_flip_flag(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity of OHLC4=(O+H+L+C)/4 changed sign today."""
    ohlc4 = (open + high + low + close) / 4.0
    return _sign_flip(_velocity(ohlc4, _TD_WEEK))


def vif_ext_016_hl2_vel_ema21_flip_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity of HL2 changed sign today."""
    hl2 = (high + low) / 2.0
    return _sign_flip(_velocity(hl2, _TD_MON))


def vif_ext_017_hl2_vel_ema5_flip_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of EMA-5 HL2 velocity sign-flips in trailing 21 days."""
    hl2 = (high + low) / 2.0
    return _rolling_count(_sign_flip(_velocity(hl2, _TD_WEEK)), _TD_MON)


def vif_ext_018_hlc3_vel_ema5_flip_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of EMA-5 HLC3 velocity sign-flips in trailing 63 days."""
    hlc3 = (high + low + close) / 3.0
    return _rolling_count(_sign_flip(_velocity(hlc3, _TD_WEEK)), _TD_QTR)


def vif_ext_019_hl2_vel_sign_ema5(high: pd.Series, low: pd.Series) -> pd.Series:
    """Sign of current EMA-5 HL2 velocity (midpoint velocity regime)."""
    hl2 = (high + low) / 2.0
    return np.sign(_velocity(hl2, _TD_WEEK)).astype(float)


def vif_ext_020_wc4_vel_ema5_flip_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity of weighted close (H+L+2C)/4 changed sign today."""
    wc4 = (high + low + 2.0 * close) / 4.0
    return _sign_flip(_velocity(wc4, _TD_WEEK))


def vif_ext_021_hl2_ohlc4_vel_sign_agree(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: EMA-5 HL2 and OHLC4 velocities agree in sign (price structure alignment)."""
    hl2 = (high + low) / 2.0
    ohlc4 = (open + high + low + close) / 4.0
    return (np.sign(_velocity(hl2, _TD_WEEK)) == np.sign(_velocity(ohlc4, _TD_WEEK))).astype(float)


def vif_ext_022_hlc3_close_vel_spread_ema5(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EMA-5 velocity of close minus EMA-5 velocity of HLC3 (close vs typical divergence)."""
    hlc3 = (high + low + close) / 3.0
    return _velocity(close, _TD_WEEK) - _velocity(hlc3, _TD_WEEK)


# --- Group C (023-034): EMA-velocity cross-span features with new spans ---

def vif_ext_023_vel_ema10_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-10 velocity changed sign today (bi-weekly velocity flip)."""
    return _sign_flip(_velocity(close, 10))


def vif_ext_024_vel_ema15_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-15 velocity changed sign today."""
    return _sign_flip(_velocity(close, 15))


def vif_ext_025_vel_ema30_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-30 velocity changed sign today (6-week smoothing)."""
    return _sign_flip(_velocity(close, 30))


def vif_ext_026_vel_ema126_flip_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-126 velocity changed sign today (half-year smoothing)."""
    return _sign_flip(_velocity(close, _TD_HALF))


def vif_ext_027_vel_ema10_ema63_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: EMA-10 velocity crossed below EMA-63 velocity today."""
    v10 = _velocity(close, 10)
    v63 = _velocity(close, _TD_QTR)
    return ((v10 < v63) & (v10.shift(1) >= v63.shift(1))).astype(float)


def vif_ext_028_vel_ema10_ema63_cross_pos(close: pd.Series) -> pd.Series:
    """Binary: EMA-10 velocity crossed above EMA-63 velocity today."""
    v10 = _velocity(close, 10)
    v63 = _velocity(close, _TD_QTR)
    return ((v10 > v63) & (v10.shift(1) <= v63.shift(1))).astype(float)


def vif_ext_029_vel_ema21_ema126_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity crossed below EMA-126 velocity (medium-term death cross)."""
    v21 = _velocity(close, _TD_MON)
    v126 = _velocity(close, _TD_HALF)
    return ((v21 < v126) & (v21.shift(1) >= v126.shift(1))).astype(float)


def vif_ext_030_vel_ema5_ema126_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity crossed below EMA-126 velocity."""
    v5 = _velocity(close, _TD_WEEK)
    v126 = _velocity(close, _TD_HALF)
    return ((v5 < v126) & (v5.shift(1) >= v126.shift(1))).astype(float)


def vif_ext_031_vel_ema10_below_ema21_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-10 velocity currently below EMA-21 velocity."""
    return (_velocity(close, 10) < _velocity(close, _TD_MON)).astype(float)


def vif_ext_032_vel_ema10_below_ema63_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-10 velocity currently below EMA-63 velocity."""
    return (_velocity(close, 10) < _velocity(close, _TD_QTR)).astype(float)


def vif_ext_033_vel_ema10_flip_count_21d(close: pd.Series) -> pd.Series:
    """Count of EMA-10 velocity sign-flips in trailing 21 days."""
    return _rolling_count(_sign_flip(_velocity(close, 10)), _TD_MON)


def vif_ext_034_vel_ema15_flip_count_63d(close: pd.Series) -> pd.Series:
    """Count of EMA-15 velocity sign-flips in trailing 63 days."""
    return _rolling_count(_sign_flip(_velocity(close, 15)), _TD_QTR)


# --- Group D (035-046): Inflection density, z-scores, percentile ranks on new concepts ---

def vif_ext_035_inflection_density_ema5_126d(close: pd.Series) -> pd.Series:
    """EMA-5 flip count over trailing 126 days (half-year density)."""
    return _rolling_count(_sign_flip(_velocity(close, _TD_WEEK)), _TD_HALF)


def vif_ext_036_inflection_density_ema10_252d(close: pd.Series) -> pd.Series:
    """EMA-10 flip count over trailing 252 days (annual density)."""
    return _rolling_count(_sign_flip(_velocity(close, 10)), _TD_YEAR)


def vif_ext_037_vel_ema10_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-10 velocity vs trailing 252-day distribution."""
    v = _velocity(close, 10)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vif_ext_038_vel_ema63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-63 velocity vs trailing 252-day distribution."""
    v = _velocity(close, _TD_QTR)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vif_ext_039_vel_ema10_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA-10 velocity in trailing 252-day distribution."""
    v = _velocity(close, 10)
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_040_vel_ema63_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA-63 velocity in trailing 252-day distribution."""
    v = _velocity(close, _TD_QTR)
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_041_inflection_count_ema10_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day EMA-10 flip count in trailing 252-day distribution."""
    cnt = _rolling_count(_sign_flip(_velocity(close, 10)), _TD_MON)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_042_vel_ema5_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-5 velocity vs trailing 63-day distribution."""
    v = _velocity(close, _TD_WEEK)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    return _safe_div(v - m, s)


def vif_ext_043_vel_ema21_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-21 velocity vs trailing 63-day distribution."""
    v = _velocity(close, _TD_MON)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    return _safe_div(v - m, s)


def vif_ext_044_wma5_vel_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of WMA-5 velocity (1-day diff) in trailing 252 days."""
    vel = _wma(close, _TD_WEEK).diff(1)
    return vel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_045_hull5_vel_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Hull MA(5) 1-day diff in trailing 252-day distribution."""
    vel = _hull_ma(close, _TD_WEEK).diff(1)
    m = _rolling_mean(vel, _TD_YEAR)
    s = _rolling_std(vel, _TD_YEAR)
    return _safe_div(vel - m, s)


def vif_ext_046_inflection_density_ema5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day EMA-5 flip count vs trailing 252-day distribution."""
    cnt = _rolling_count(_sign_flip(_velocity(close, _TD_WEEK)), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


# --- Group E (047-057): Volume at inflection — volume surge/depletion on flip days ---

def vif_ext_047_vol_surge_at_ema5_flip(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on EMA-5 flip day vs 21-day avg vol, forward-filled."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    at_flip = ratio.where(flip == 1, np.nan).ffill()
    return at_flip


def vif_ext_048_vol_surge_at_ema21_flip(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio on EMA-21 flip day vs 21-day avg vol, forward-filled."""
    flip = _sign_flip(_velocity(close, _TD_MON))
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    at_flip = ratio.where(flip == 1, np.nan).ffill()
    return at_flip


def vif_ext_049_high_vol_inflection_ema5_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of EMA-5 flips with volume > 1.5x 21-day avg in trailing 21 days."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol_flip = (flip == 1) & (volume > 1.5 * avg_vol.shift(1).fillna(avg_vol))
    return _rolling_count(high_vol_flip.astype(float), _TD_MON)


def vif_ext_050_high_vol_inflection_ema21_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of EMA-21 flips with volume > 1.5x 21-day avg in trailing 63 days."""
    flip = _sign_flip(_velocity(close, _TD_MON))
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol_flip = (flip == 1) & (volume > 1.5 * avg_vol.shift(1).fillna(avg_vol))
    return _rolling_count(high_vol_flip.astype(float), _TD_QTR)


def vif_ext_051_low_vol_inflection_ema5_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of EMA-5 flips with volume < 0.75x 21-day avg in trailing 21 days (weak flips)."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    avg_vol = _rolling_mean(volume, _TD_MON)
    low_vol_flip = (flip == 1) & (volume < 0.75 * avg_vol.shift(1).fillna(avg_vol))
    return _rolling_count(low_vol_flip.astype(float), _TD_MON)


def vif_ext_052_avg_vol_surge_at_ema5_flip_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume ratio (vol/21d-avg-vol) on EMA-5 flip days over trailing 63 days."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    on_flip = ratio.where(flip == 1, np.nan)
    return on_flip.rolling(_TD_QTR, min_periods=1).mean()


def vif_ext_053_vol_at_neg_flip_ema5_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio at last bearish EMA-5 flip (negative-to-positive excluded), fwd-filled."""
    flip_neg = (np.sign(_velocity(close, _TD_WEEK)) < 0) & (np.sign(_velocity(close, _TD_WEEK)).shift(1) > 0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    at_neg_flip = ratio.where(flip_neg, np.nan).ffill()
    return at_neg_flip


def vif_ext_054_vol_at_pos_flip_ema5_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio at last bullish EMA-5 flip, forward-filled."""
    flip_pos = (np.sign(_velocity(close, _TD_WEEK)) > 0) & (np.sign(_velocity(close, _TD_WEEK)).shift(1) < 0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    at_pos_flip = ratio.where(flip_pos, np.nan).ffill()
    return at_pos_flip


def vif_ext_055_vol_ema21_neg_flip_vs_pos_flip_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg-vol-at-bearish-flip to avg-vol-at-bullish-flip over 252 days."""
    neg_flip = ((np.sign(_velocity(close, _TD_MON)) < 0) &
                (np.sign(_velocity(close, _TD_MON)).shift(1) > 0)).astype(float)
    pos_flip = ((np.sign(_velocity(close, _TD_MON)) > 0) &
                (np.sign(_velocity(close, _TD_MON)).shift(1) < 0)).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    ratio = _safe_div(volume, avg_vol)
    avg_neg = (ratio * neg_flip).rolling(_TD_YEAR, min_periods=1).sum() / (
        neg_flip.rolling(_TD_YEAR, min_periods=1).sum().replace(0, np.nan))
    avg_pos = (ratio * pos_flip).rolling(_TD_YEAR, min_periods=1).sum() / (
        pos_flip.rolling(_TD_YEAR, min_periods=1).sum().replace(0, np.nan))
    return _safe_div(avg_neg, avg_pos)


# --- Group F (056-063): Curvature magnitude and transform features ---

def vif_ext_056_curvature_ema5_abs_value(close: pd.Series) -> pd.Series:
    """Absolute magnitude of EMA-5 velocity 1-day change (unsigned curvature)."""
    v = _velocity(close, _TD_WEEK)
    return v.diff(1).abs()


def vif_ext_057_curvature_ema21_abs_value(close: pd.Series) -> pd.Series:
    """Absolute magnitude of EMA-21 velocity 1-day change (unsigned curvature)."""
    v = _velocity(close, _TD_MON)
    return v.diff(1).abs()


def vif_ext_058_curvature_ema5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-5 curvature (abs 1-day velocity change) vs 252-day distribution."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    m = _rolling_mean(curv, _TD_YEAR)
    s = _rolling_std(curv, _TD_YEAR)
    return _safe_div(curv - m, s)


def vif_ext_059_curvature_ema5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA-5 curvature magnitude in trailing 252 days."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    return curv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_060_curvature_ema21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA-21 curvature magnitude in trailing 252 days."""
    curv = _velocity(close, _TD_MON).diff(1).abs()
    return curv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_ext_061_curvature_ema5_avg_252d(close: pd.Series) -> pd.Series:
    """252-day rolling average of EMA-5 curvature magnitude (baseline curvature level)."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    return _rolling_mean(curv, _TD_YEAR)


def vif_ext_062_curvature_ema5_ratio_to_252d_avg(close: pd.Series) -> pd.Series:
    """Current EMA-5 curvature magnitude vs 252-day average (curvature spike ratio)."""
    curv = _velocity(close, _TD_WEEK).diff(1).abs()
    avg = _rolling_mean(curv, _TD_YEAR)
    return _safe_div(curv, avg)


def vif_ext_063_curvature_count_ema10_21d(close: pd.Series) -> pd.Series:
    """Count of EMA-10 curvature (2nd-deriv) zero-crossings in trailing 21 days."""
    v = _velocity(close, 10)
    curv = v.diff(1)
    return _rolling_count(_sign_flip(curv), _TD_MON)


# --- Group G (064-070): Inter-inflection duration statistics ---

def vif_ext_064_inter_flip_duration_ema5_avg_63d(close: pd.Series) -> pd.Series:
    """Avg days between EMA-5 velocity flips over trailing 63 days (regime persistence)."""
    flip = _sign_flip(_velocity(close, _TD_WEEK))
    cnt = _rolling_count(flip, _TD_QTR)
    return _safe_div(pd.Series(_TD_QTR, index=flip.index, dtype=float), cnt)


def vif_ext_065_inter_flip_duration_ema21_avg_252d(close: pd.Series) -> pd.Series:
    """Avg days between EMA-21 velocity flips over trailing 252 days."""
    flip = _sign_flip(_velocity(close, _TD_MON))
    cnt = _rolling_count(flip, _TD_YEAR)
    return _safe_div(pd.Series(_TD_YEAR, index=flip.index, dtype=float), cnt)


def vif_ext_066_days_since_ema10_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-10 velocity sign-flip."""
    return _days_since_flip(_sign_flip(_velocity(close, 10)))


def vif_ext_067_days_since_ema15_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-15 velocity sign-flip."""
    return _days_since_flip(_sign_flip(_velocity(close, 15)))


def vif_ext_068_days_since_ema126_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-126 velocity sign-flip (half-year smoothing)."""
    return _days_since_flip(_sign_flip(_velocity(close, _TD_HALF)))


def vif_ext_069_days_since_hull5_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last Hull MA(5) velocity sign-flip."""
    return _days_since_flip(_sign_flip(_hull_ma(close, _TD_WEEK).diff(1)))


def vif_ext_070_days_since_wma5_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last WMA-5 velocity sign-flip."""
    return _days_since_flip(_sign_flip(_wma(close, _TD_WEEK).diff(1)))


# --- Group H (071-075): Composite and regime feature extensions ---

def vif_ext_071_multi_span_vel_neg_count(close: pd.Series) -> pd.Series:
    """Count of spans with negative velocity: EMA-5/10/21/63/126 (0-5 score)."""
    v5 = (_velocity(close, _TD_WEEK) < 0).astype(float)
    v10 = (_velocity(close, 10) < 0).astype(float)
    v21 = (_velocity(close, _TD_MON) < 0).astype(float)
    v63 = (_velocity(close, _TD_QTR) < 0).astype(float)
    v126 = (_velocity(close, _TD_HALF) < 0).astype(float)
    return v5 + v10 + v21 + v63 + v126


def vif_ext_072_all_5spans_vel_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5/10/21/63/126 velocities all negative simultaneously (max distress)."""
    v5 = _velocity(close, _TD_WEEK)
    v10 = _velocity(close, 10)
    v21 = _velocity(close, _TD_MON)
    v63 = _velocity(close, _TD_QTR)
    v126 = _velocity(close, _TD_HALF)
    return ((v5 < 0) & (v10 < 0) & (v21 < 0) & (v63 < 0) & (v126 < 0)).astype(float)


def vif_ext_073_consec_neg_vel_ema63(close: pd.Series) -> pd.Series:
    """Consecutive days with negative EMA-63 velocity (long-term bear velocity streak)."""
    return _consec_true(_velocity(close, _TD_QTR) < 0)


def vif_ext_074_neg_inflection_after_high_vol_ema5(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: EMA-5 bearish velocity flip AND volume > 2x 21-day avg (capitulation signal)."""
    v = _velocity(close, _TD_WEEK)
    neg_flip = (np.sign(v) < 0) & (np.sign(v).shift(1) > 0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = volume > 2.0 * avg_vol.shift(1).fillna(avg_vol)
    return (neg_flip & high_vol).astype(float)


def vif_ext_075_capitulation_vel_composite_ext(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended capitulation composite: multi-span neg velocity score + curvature spike + vol surge.
    Combines normalized: (5-span neg count)/5 + curvature-z-score-clip/3 + vol-surge-flag."""
    neg_score = vif_ext_071_multi_span_vel_neg_count(close) / 5.0
    curv_z = vif_ext_058_curvature_ema5_zscore_252d(close).abs().clip(upper=3.0) / 3.0
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_surge = (_safe_div(volume, avg_vol) > 1.5).astype(float)
    return neg_score + curv_z.fillna(0.0) + vol_surge


# ── Registry ──────────────────────────────────────────────────────────────────

VELOCITY_INFLECTION_EXTENDED_REGISTRY_001_075 = {
    "vif_ext_001_wma5_vel_sign": {"inputs": ["close"], "func": vif_ext_001_wma5_vel_sign},
    "vif_ext_002_wma5_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_002_wma5_vel_flip_flag},
    "vif_ext_003_wma21_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_003_wma21_vel_flip_flag},
    "vif_ext_004_hull5_vel_sign": {"inputs": ["close"], "func": vif_ext_004_hull5_vel_sign},
    "vif_ext_005_hull5_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_005_hull5_vel_flip_flag},
    "vif_ext_006_hull21_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_006_hull21_vel_flip_flag},
    "vif_ext_007_dema5_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_007_dema5_vel_flip_flag},
    "vif_ext_008_dema21_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_008_dema21_vel_flip_flag},
    "vif_ext_009_tema5_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_009_tema5_vel_flip_flag},
    "vif_ext_010_tema21_vel_flip_flag": {"inputs": ["close"], "func": vif_ext_010_tema21_vel_flip_flag},
    "vif_ext_011_hull5_vel_flip_count_21d": {"inputs": ["close"], "func": vif_ext_011_hull5_vel_flip_count_21d},
    "vif_ext_012_hull21_vel_flip_count_63d": {"inputs": ["close"], "func": vif_ext_012_hull21_vel_flip_count_63d},
    "vif_ext_013_hl2_vel_ema5_flip_flag": {"inputs": ["high", "low"], "func": vif_ext_013_hl2_vel_ema5_flip_flag},
    "vif_ext_014_hlc3_vel_ema5_flip_flag": {"inputs": ["close", "high", "low"], "func": vif_ext_014_hlc3_vel_ema5_flip_flag},
    "vif_ext_015_ohlc4_vel_ema5_flip_flag": {"inputs": ["close", "high", "low", "open"], "func": vif_ext_015_ohlc4_vel_ema5_flip_flag},
    "vif_ext_016_hl2_vel_ema21_flip_flag": {"inputs": ["high", "low"], "func": vif_ext_016_hl2_vel_ema21_flip_flag},
    "vif_ext_017_hl2_vel_ema5_flip_count_21d": {"inputs": ["high", "low"], "func": vif_ext_017_hl2_vel_ema5_flip_count_21d},
    "vif_ext_018_hlc3_vel_ema5_flip_count_63d": {"inputs": ["close", "high", "low"], "func": vif_ext_018_hlc3_vel_ema5_flip_count_63d},
    "vif_ext_019_hl2_vel_sign_ema5": {"inputs": ["high", "low"], "func": vif_ext_019_hl2_vel_sign_ema5},
    "vif_ext_020_wc4_vel_ema5_flip_flag": {"inputs": ["close", "high", "low"], "func": vif_ext_020_wc4_vel_ema5_flip_flag},
    "vif_ext_021_hl2_ohlc4_vel_sign_agree": {"inputs": ["close", "high", "low", "open"], "func": vif_ext_021_hl2_ohlc4_vel_sign_agree},
    "vif_ext_022_hlc3_close_vel_spread_ema5": {"inputs": ["close", "high", "low"], "func": vif_ext_022_hlc3_close_vel_spread_ema5},
    "vif_ext_023_vel_ema10_flip_flag": {"inputs": ["close"], "func": vif_ext_023_vel_ema10_flip_flag},
    "vif_ext_024_vel_ema15_flip_flag": {"inputs": ["close"], "func": vif_ext_024_vel_ema15_flip_flag},
    "vif_ext_025_vel_ema30_flip_flag": {"inputs": ["close"], "func": vif_ext_025_vel_ema30_flip_flag},
    "vif_ext_026_vel_ema126_flip_flag": {"inputs": ["close"], "func": vif_ext_026_vel_ema126_flip_flag},
    "vif_ext_027_vel_ema10_ema63_cross_neg": {"inputs": ["close"], "func": vif_ext_027_vel_ema10_ema63_cross_neg},
    "vif_ext_028_vel_ema10_ema63_cross_pos": {"inputs": ["close"], "func": vif_ext_028_vel_ema10_ema63_cross_pos},
    "vif_ext_029_vel_ema21_ema126_cross_neg": {"inputs": ["close"], "func": vif_ext_029_vel_ema21_ema126_cross_neg},
    "vif_ext_030_vel_ema5_ema126_cross_neg": {"inputs": ["close"], "func": vif_ext_030_vel_ema5_ema126_cross_neg},
    "vif_ext_031_vel_ema10_below_ema21_flag": {"inputs": ["close"], "func": vif_ext_031_vel_ema10_below_ema21_flag},
    "vif_ext_032_vel_ema10_below_ema63_flag": {"inputs": ["close"], "func": vif_ext_032_vel_ema10_below_ema63_flag},
    "vif_ext_033_vel_ema10_flip_count_21d": {"inputs": ["close"], "func": vif_ext_033_vel_ema10_flip_count_21d},
    "vif_ext_034_vel_ema15_flip_count_63d": {"inputs": ["close"], "func": vif_ext_034_vel_ema15_flip_count_63d},
    "vif_ext_035_inflection_density_ema5_126d": {"inputs": ["close"], "func": vif_ext_035_inflection_density_ema5_126d},
    "vif_ext_036_inflection_density_ema10_252d": {"inputs": ["close"], "func": vif_ext_036_inflection_density_ema10_252d},
    "vif_ext_037_vel_ema10_zscore_252d": {"inputs": ["close"], "func": vif_ext_037_vel_ema10_zscore_252d},
    "vif_ext_038_vel_ema63_zscore_252d": {"inputs": ["close"], "func": vif_ext_038_vel_ema63_zscore_252d},
    "vif_ext_039_vel_ema10_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_039_vel_ema10_pct_rank_252d},
    "vif_ext_040_vel_ema63_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_040_vel_ema63_pct_rank_252d},
    "vif_ext_041_inflection_count_ema10_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_041_inflection_count_ema10_pct_rank_252d},
    "vif_ext_042_vel_ema5_zscore_63d": {"inputs": ["close"], "func": vif_ext_042_vel_ema5_zscore_63d},
    "vif_ext_043_vel_ema21_zscore_63d": {"inputs": ["close"], "func": vif_ext_043_vel_ema21_zscore_63d},
    "vif_ext_044_wma5_vel_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_044_wma5_vel_pct_rank_252d},
    "vif_ext_045_hull5_vel_zscore_252d": {"inputs": ["close"], "func": vif_ext_045_hull5_vel_zscore_252d},
    "vif_ext_046_inflection_density_ema5_zscore_252d": {"inputs": ["close"], "func": vif_ext_046_inflection_density_ema5_zscore_252d},
    "vif_ext_047_vol_surge_at_ema5_flip": {"inputs": ["close", "volume"], "func": vif_ext_047_vol_surge_at_ema5_flip},
    "vif_ext_048_vol_surge_at_ema21_flip": {"inputs": ["close", "volume"], "func": vif_ext_048_vol_surge_at_ema21_flip},
    "vif_ext_049_high_vol_inflection_ema5_21d": {"inputs": ["close", "volume"], "func": vif_ext_049_high_vol_inflection_ema5_21d},
    "vif_ext_050_high_vol_inflection_ema21_63d": {"inputs": ["close", "volume"], "func": vif_ext_050_high_vol_inflection_ema21_63d},
    "vif_ext_051_low_vol_inflection_ema5_21d": {"inputs": ["close", "volume"], "func": vif_ext_051_low_vol_inflection_ema5_21d},
    "vif_ext_052_avg_vol_surge_at_ema5_flip_63d": {"inputs": ["close", "volume"], "func": vif_ext_052_avg_vol_surge_at_ema5_flip_63d},
    "vif_ext_053_vol_at_neg_flip_ema5_norm": {"inputs": ["close", "volume"], "func": vif_ext_053_vol_at_neg_flip_ema5_norm},
    "vif_ext_054_vol_at_pos_flip_ema5_norm": {"inputs": ["close", "volume"], "func": vif_ext_054_vol_at_pos_flip_ema5_norm},
    "vif_ext_055_vol_ema21_neg_flip_vs_pos_flip_ratio": {"inputs": ["close", "volume"], "func": vif_ext_055_vol_ema21_neg_flip_vs_pos_flip_ratio},
    "vif_ext_056_curvature_ema5_abs_value": {"inputs": ["close"], "func": vif_ext_056_curvature_ema5_abs_value},
    "vif_ext_057_curvature_ema21_abs_value": {"inputs": ["close"], "func": vif_ext_057_curvature_ema21_abs_value},
    "vif_ext_058_curvature_ema5_zscore_252d": {"inputs": ["close"], "func": vif_ext_058_curvature_ema5_zscore_252d},
    "vif_ext_059_curvature_ema5_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_059_curvature_ema5_pct_rank_252d},
    "vif_ext_060_curvature_ema21_pct_rank_252d": {"inputs": ["close"], "func": vif_ext_060_curvature_ema21_pct_rank_252d},
    "vif_ext_061_curvature_ema5_avg_252d": {"inputs": ["close"], "func": vif_ext_061_curvature_ema5_avg_252d},
    "vif_ext_062_curvature_ema5_ratio_to_252d_avg": {"inputs": ["close"], "func": vif_ext_062_curvature_ema5_ratio_to_252d_avg},
    "vif_ext_063_curvature_count_ema10_21d": {"inputs": ["close"], "func": vif_ext_063_curvature_count_ema10_21d},
    "vif_ext_064_inter_flip_duration_ema5_avg_63d": {"inputs": ["close"], "func": vif_ext_064_inter_flip_duration_ema5_avg_63d},
    "vif_ext_065_inter_flip_duration_ema21_avg_252d": {"inputs": ["close"], "func": vif_ext_065_inter_flip_duration_ema21_avg_252d},
    "vif_ext_066_days_since_ema10_flip": {"inputs": ["close"], "func": vif_ext_066_days_since_ema10_flip},
    "vif_ext_067_days_since_ema15_flip": {"inputs": ["close"], "func": vif_ext_067_days_since_ema15_flip},
    "vif_ext_068_days_since_ema126_flip": {"inputs": ["close"], "func": vif_ext_068_days_since_ema126_flip},
    "vif_ext_069_days_since_hull5_flip": {"inputs": ["close"], "func": vif_ext_069_days_since_hull5_flip},
    "vif_ext_070_days_since_wma5_flip": {"inputs": ["close"], "func": vif_ext_070_days_since_wma5_flip},
    "vif_ext_071_multi_span_vel_neg_count": {"inputs": ["close"], "func": vif_ext_071_multi_span_vel_neg_count},
    "vif_ext_072_all_5spans_vel_neg_flag": {"inputs": ["close"], "func": vif_ext_072_all_5spans_vel_neg_flag},
    "vif_ext_073_consec_neg_vel_ema63": {"inputs": ["close"], "func": vif_ext_073_consec_neg_vel_ema63},
    "vif_ext_074_neg_inflection_after_high_vol_ema5": {"inputs": ["close", "volume"], "func": vif_ext_074_neg_inflection_after_high_vol_ema5},
    "vif_ext_075_capitulation_vel_composite_ext": {"inputs": ["close", "volume"], "func": vif_ext_075_capitulation_vel_composite_ext},
}
