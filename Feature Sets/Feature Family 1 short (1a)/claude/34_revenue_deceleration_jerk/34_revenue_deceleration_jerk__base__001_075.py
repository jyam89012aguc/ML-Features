"""revenue_deceleration_jerk base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Per HANDOFF §6 (families 29-36 special rule): base features are PATTERN-DETECTION
HYPOTHESES about JERK (3rd-order) dynamics of the revenue trajectory — NOT raw
3rd derivatives. Distinct from family 21 (rgdc, trajectory) and family 29 (rdac,
acceleration patterns): rdjk targets the SHAPE OF CHANGE-IN-ACCELERATION —
sudden shifts in deceleration rate, acceleration-regime flips, inflection events.

Inputs: SF1 quarterly (revenue, netinc, ebit, ebitda, fcf, cashneq, shareswa,
debt, receivables, inventory). Quarterly cadence. PIT-clean.
"""
import numpy as np
import pandas as pd

Q = 1
Y = 4
Y2 = 8
Y3 = 12
Y4 = 16


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


def _structural_break_score(s, n):
    return _rolling_slope(s, n) - _rolling_slope(s.shift(n), n)


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f34_rdjk_001_jerk_onset_after_dormancy_8q(revenue: pd.Series) -> pd.Series:
    """Onset event: |jerk z(8Q)|>3 after prior 4Q calm (|z|<1 for >=75% of bars)."""
    jerk = revenue.diff().diff().diff()
    jerk_z = _rolling_zscore(jerk, 8)
    prior_calm = (jerk_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (jerk_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(jerk_z.notna(), np.nan)


def f34_rdjk_002_log_jerk_cliff_after_calm_8q(revenue: pd.Series) -> pd.Series:
    """Cliff event: |log-jerk z(8Q)|>2.5 with prior 4Q std < 0.5 * 8Q std."""
    log_rev = _safe_log(revenue)
    log_jerk = log_rev.diff().diff().diff()
    jerk_z = _rolling_zscore(log_jerk, 8)
    prior_var = log_jerk.shift(1).rolling(4, min_periods=3).std()
    recent_var = log_jerk.rolling(8, min_periods=4).std()
    cliff = (jerk_z.abs() > 2.5) & (prior_var < 0.5 * recent_var)
    return cliff.astype(float).where(jerk_z.notna(), np.nan)


def f34_rdjk_003_revenue_jerk_cliff_8q(revenue: pd.Series) -> pd.Series:
    """1Q revenue jerk / 8Q std of jerks — cliff-edge in jerk."""
    j = revenue.diff().diff().diff()
    sd = j.rolling(Y2, min_periods=3).std()
    return j / sd.replace(0, np.nan)


def f34_rdjk_004_revenue_jerk_structural_break_8q(revenue: pd.Series) -> pd.Series:
    """Recent 8Q jerk slope minus prior 8Q jerk slope."""
    j = revenue.diff().diff().diff()
    return _structural_break_score(j, Y2)


def f34_rdjk_005_quarters_since_revenue_jerk_positive(revenue: pd.Series) -> pd.Series:
    """Quarters since last positive jerk — recency of acceleration-up event."""
    j = revenue.diff().diff().diff()
    flag = (j > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f34_rdjk_006_quarters_since_revenue_jerk_negative(revenue: pd.Series) -> pd.Series:
    """Quarters since last negative jerk — recency of acceleration-down event."""
    j = revenue.diff().diff().diff()
    flag = (j < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f34_rdjk_007_jerk_sustained_3consec_neg_indicator(revenue: pd.Series) -> pd.Series:
    """1 when last 3 bars all have jerk z(8Q) < -1 — sustained negative jerk streak."""
    jerk = revenue.diff().diff().diff()
    jerk_z = _rolling_zscore(jerk, 8)
    neg = (jerk_z < -1).astype(int)
    streak3 = neg.rolling(3, min_periods=3).sum()
    return (streak3 >= 3).astype(float).where(jerk_z.notna(), np.nan)


def f34_rdjk_008_jerk_magnitude_conditional_on_neg_accel_16q(revenue: pd.Series) -> pd.Series:
    """Max |yoy-jerk| over 16Q conditional on yoy-accel<0 — jerk size during deceleration."""
    yoy = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    accel = yoy.diff().diff()
    jerk = yoy.diff().diff().diff()
    cond = accel < 0
    cond_jerk_abs = jerk.abs().where(cond, np.nan)
    return cond_jerk_abs.rolling(16, min_periods=4).max()


def f34_rdjk_009_revenue_jerk_lead_lag_cov_with_yoy_lag1_8q(revenue: pd.Series) -> pd.Series:
    """8Q mean of jerk*jerk.shift(1) on yoy series — lagged auto-covariance of yoy-jerk."""
    yoy = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    jerk = yoy.diff().diff().diff()
    return (jerk * jerk.shift(1)).rolling(8, min_periods=4).mean()


def f34_rdjk_010_revenue_jerk_2sigma_count_16q(revenue: pd.Series) -> pd.Series:
    """Count of last 16Q with |jerk z| > 2."""
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f34_rdjk_011_revenue_jerk_4q_recent_minus_prior_4q(revenue: pd.Series) -> pd.Series:
    """Mean jerk last 4Q minus mean jerk prior 4Q."""
    j = revenue.diff().diff().diff()
    a = j.rolling(Y, min_periods=2).mean()
    b = j.shift(Y).rolling(Y, min_periods=2).mean()
    return a - b


def f34_rdjk_012_revenue_jerk_inflection_sign_flip_8q(revenue: pd.Series) -> pd.Series:
    """Sign-flip count of jerk vs its EMA-smoothed version over 8Q."""
    j = revenue.diff().diff().diff()
    sm = j.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(j - sm) != np.sign((j - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_013_revenue_jerk_slope_8q(revenue: pd.Series) -> pd.Series:
    """Slope of jerk over 8Q — change-rate of jerk."""
    return _rolling_slope(revenue.diff().diff().diff(), Y2)


def f34_rdjk_014_log_revenue_jerk_slope_8q(revenue: pd.Series) -> pd.Series:
    """Slope of log-revenue jerk over 8Q."""
    return _rolling_slope(_safe_log(revenue).diff().diff().diff(), Y2)


def f34_rdjk_015_cumulative_log_revenue_jerk_8q(revenue: pd.Series) -> pd.Series:
    """Cumulative sum of log-revenue jerk over 8Q."""
    return _safe_log(revenue).diff().diff().diff().rolling(Y2, min_periods=3).sum()


def f34_rdjk_016_revenue_jerk_arc_area_8q(revenue: pd.Series) -> pd.Series:
    """Sum of positive jerk residuals above 8Q linear fit."""
    j = revenue.diff().diff().diff()
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return j.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f34_rdjk_017_revenue_jerk_excess_above_8q_linear(revenue: pd.Series) -> pd.Series:
    """Sum of (jerk - 8Q linear fit) over 8Q."""
    j = revenue.diff().diff().diff()
    def _ex(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float((w - (c1 * x + c0)).sum())
    return j.rolling(Y2, min_periods=4).apply(_ex, raw=True)


def f34_rdjk_018_yoy_growth_jerk_z_16q(revenue: pd.Series) -> pd.Series:
    """Z-score of 3rd diff of YoY growth (revenue.pct_change(4)) over 16Q."""
    yoy = revenue.pct_change(Y)
    return _rolling_zscore(yoy.diff().diff().diff(), Y4)


def f34_rdjk_019_yoy_growth_jerk_cliff_8q(revenue: pd.Series) -> pd.Series:
    """1Q YoY-growth-jerk / 8Q std of YoY-growth-jerks."""
    yoy = revenue.pct_change(Y)
    j = yoy.diff().diff().diff()
    sd = j.rolling(Y2, min_periods=3).std()
    return j / sd.replace(0, np.nan)


def f34_rdjk_020_yoy_growth_jerk_structural_break_8q(revenue: pd.Series) -> pd.Series:
    """YoY-growth-jerk 8Q recent slope minus prior 8Q slope."""
    yoy = revenue.pct_change(Y)
    j = yoy.diff().diff().diff()
    return _structural_break_score(j, Y2)


def f34_rdjk_021_yoy_growth_jerk_slope_8q(revenue: pd.Series) -> pd.Series:
    """Slope of YoY-growth-jerk over 8Q."""
    yoy = revenue.pct_change(Y)
    return _rolling_slope(yoy.diff().diff().diff(), Y2)


def f34_rdjk_022_jerk_onset_multi_horizon_consistency_4_8_12q(revenue: pd.Series) -> pd.Series:
    """Count of horizons (4Q,8Q,12Q) where |jerk z|>3 — multi-horizon onset consistency."""
    jerk = revenue.diff().diff().diff()
    o4 = (_rolling_zscore(jerk, 4).abs() > 3).astype(float)
    o8 = (_rolling_zscore(jerk, 8).abs() > 3).astype(float)
    o12 = (_rolling_zscore(jerk, 12).abs() > 3).astype(float)
    return o4.fillna(0) + o8.fillna(0) + o12.fillna(0)


def f34_rdjk_023_revenue_jerk_dispersion_cv_8q(revenue: pd.Series) -> pd.Series:
    """CV of jerk series over 8Q."""
    j = revenue.diff().diff().diff()
    return _safe_div(j.rolling(Y2, min_periods=3).std(), j.rolling(Y2, min_periods=3).mean().abs())


def f34_rdjk_024_revenue_jerk_percentile_rank_16q(revenue: pd.Series) -> pd.Series:
    """Percentile rank of current jerk within 16Q distribution."""
    j = revenue.diff().diff().diff()
    return j.rolling(Y4, min_periods=6).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f34_rdjk_025_revenue_jerk_cumulative_excess_8q(revenue: pd.Series) -> pd.Series:
    """Sum 8Q of (jerk - 16Q-median jerk) — sustained jerk excess."""
    j = revenue.diff().diff().diff()
    med = j.rolling(Y4, min_periods=6).median()
    return (j - med).rolling(Y2, min_periods=3).sum()


def f34_rdjk_026_accel_sign_flip_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of sign changes of revenue 2nd-diff over 8Q — acceleration-regime changes."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_027_accel_sign_flip_count_16q(revenue: pd.Series) -> pd.Series:
    """Same as 026 over 16Q."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum()


def f34_rdjk_028_quarters_since_accel_last_flipped(revenue: pd.Series) -> pd.Series:
    """Quarters since acceleration sign last flipped."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    last = pd.Series(np.where(flip > 0, np.arange(len(flip)), np.nan), index=flip.index).ffill()
    return pd.Series(np.arange(len(flip)), index=flip.index) - last


def f34_rdjk_029_accel_regime_duration_mean_16q(revenue: pd.Series) -> pd.Series:
    """Mean run length between accel sign flips in last 16Q."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(int)
    grp = flip.cumsum()
    run = grp.groupby(grp).cumcount() + 1
    return run.rolling(Y4, min_periods=6).mean()


def f34_rdjk_030_accel_volatility_8q(revenue: pd.Series) -> pd.Series:
    """Std of 2nd-diff over 8Q — acceleration volatility."""
    return revenue.diff().diff().rolling(Y2, min_periods=3).std()


def f34_rdjk_031_accel_volatility_16q(revenue: pd.Series) -> pd.Series:
    """Std of 2nd-diff over 16Q."""
    return revenue.diff().diff().rolling(Y4, min_periods=6).std()


def f34_rdjk_032_accel_4q_recent_minus_prior_4q(revenue: pd.Series) -> pd.Series:
    """Mean 2nd-diff last 4Q minus mean prior 4Q."""
    d2 = revenue.diff().diff()
    return d2.rolling(Y, min_periods=2).mean() - d2.shift(Y).rolling(Y, min_periods=2).mean()


def f34_rdjk_033_accel_range_8q(revenue: pd.Series) -> pd.Series:
    """Max - min of 2nd-diff over 8Q — acceleration range."""
    d2 = revenue.diff().diff()
    return d2.rolling(Y2, min_periods=3).max() - d2.rolling(Y2, min_periods=3).min()


def f34_rdjk_034_accel_slope_8q(revenue: pd.Series) -> pd.Series:
    """Slope of 2nd-diff over 8Q — same as jerk averaged over 8Q (different formulation)."""
    return _rolling_slope(revenue.diff().diff(), Y2)


def f34_rdjk_035_accel_slope_normalized_8q(revenue: pd.Series) -> pd.Series:
    """Slope of 2nd-diff over 8Q normalized by 8Q std of 2nd-diff."""
    d2 = revenue.diff().diff()
    return _safe_div(_rolling_slope(d2, Y2), d2.rolling(Y2, min_periods=3).std())


def f34_rdjk_036_accel_cliff_max_1q_chg_8q(revenue: pd.Series) -> pd.Series:
    """Max |1Q change in 2nd-diff| over 8Q — single-bar acceleration jump."""
    d2 = revenue.diff().diff()
    return d2.diff().abs().rolling(Y2, min_periods=3).max()


def f34_rdjk_037_negative_accel_streak_max_8q(revenue: pd.Series) -> pd.Series:
    """Max consecutive negative-acceleration streak length in 8Q."""
    d2 = revenue.diff().diff()
    neg = (d2 < 0).astype(int)
    grp = (neg == 0).cumsum()
    streak = neg.groupby(grp).cumsum()
    return streak.rolling(Y2, min_periods=3).max()


def f34_rdjk_038_positive_accel_streak_max_8q(revenue: pd.Series) -> pd.Series:
    """Max consecutive positive-acceleration streak length in 8Q."""
    d2 = revenue.diff().diff()
    pos = (d2 > 0).astype(int)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak.rolling(Y2, min_periods=3).max()


def f34_rdjk_039_accel_regime_mismatch_4q_vs_12q(revenue: pd.Series) -> pd.Series:
    """Sign(mean 4Q d2) - sign(mean 12Q d2) — regime mismatch indicator."""
    d2 = revenue.diff().diff()
    return np.sign(d2.rolling(Y, min_periods=2).mean()) - np.sign(d2.rolling(Y3, min_periods=4).mean())


def f34_rdjk_040_accel_regime_zscore_deviation(revenue: pd.Series) -> pd.Series:
    """(Current d2 z) - (4Q mean of d2 z) — recent deviation from short baseline."""
    d2 = revenue.diff().diff()
    z = _rolling_zscore(d2, Y4)
    return z - z.rolling(Y, min_periods=2).mean()


def f34_rdjk_041_accel_quadratic_c2_8q(revenue: pd.Series) -> pd.Series:
    """Quadratic c2 of 2nd-diff series over 8Q — convexity of acceleration trajectory."""
    d2 = revenue.diff().diff()
    def _c2(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x = np.arange(len(w))
        try:
            c2, _, _ = np.polyfit(x, w, 2)
            return float(c2)
        except Exception:
            return np.nan
    return d2.rolling(Y2, min_periods=4).apply(_c2, raw=True)


def f34_rdjk_042_compound_jerk_cash_burn_4q(revenue: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Count 4Q with revenue jerk<0 AND cash falling — compound deterioration."""
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_043_compound_jerk_dilution_4q(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Count 4Q with revenue jerk<0 AND shares rising — jerk + dilution coincidence."""
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (shareswa.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_044_compound_jerk_margin_compression_4q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Count 4Q with revenue jerk<0 AND margin (netinc/revenue) falling."""
    j = revenue.diff().diff().diff()
    margin = _safe_div(netinc, revenue)
    flag = ((j < 0) & (margin.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_045_compound_jerk_debt_up_4q(revenue: pd.Series, debt: pd.Series) -> pd.Series:
    """Count 4Q with revenue jerk<0 AND debt rising."""
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_046_compound_jerk_inst_value_down_4q(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    """Count 4Q with revenue jerk<0 AND ebit jerk<0 — joint operating jerk deterioration."""
    j = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    flag = ((j < 0) & (je < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_047_jerk_dispersion_across_periods_8q(revenue: pd.Series) -> pd.Series:
    """Std of (jerk - 4Q rolling-mean jerk) over 8Q — sub-window dispersion of jerk."""
    j = revenue.diff().diff().diff()
    centered = j - j.rolling(Y, min_periods=2).mean()
    return centered.rolling(Y2, min_periods=3).std()


def f34_rdjk_048_jerk_vs_baseline_composite_z_4q(revenue: pd.Series) -> pd.Series:
    """Mean 4Q of z(jerk) vs 16Q distribution."""
    return _rolling_zscore(revenue.diff().diff().diff(), Y4).rolling(Y, min_periods=2).mean()


def f34_rdjk_049_jerk_regime_tail_indicator(revenue: pd.Series) -> pd.Series:
    """1 if current |jerk| above 95th pct of 16Q, 0 otherwise."""
    j = revenue.diff().diff().diff().abs()
    p = j.rolling(Y4, min_periods=6).quantile(0.95)
    return (j >= p).astype(float)


def f34_rdjk_050_jerk_consistency_index_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of last 8Q where jerk has same sign as 4Q-mean jerk."""
    j = revenue.diff().diff().diff()
    m = j.rolling(Y, min_periods=2).mean()
    flag = (np.sign(j) == np.sign(m)).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f34_rdjk_051_d2_inflection_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of sign-flips of 2nd-diff inside last 8Q (acceleration inflections)."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_052_d2_inflection_probability_8q(revenue: pd.Series) -> pd.Series:
    """Mean of d2 sign-flip indicator over 8Q (inflection probability)."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).mean()


def f34_rdjk_053_d2_sign_flip_cumulative_16q(revenue: pd.Series) -> pd.Series:
    """Cumulative count of d2 sign-flips over 16Q."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum()


def f34_rdjk_054_d2_ema_vs_raw_sign_flip_8q(revenue: pd.Series) -> pd.Series:
    """Sign-flip count of d2 vs EMA-smoothed d2 over 8Q."""
    d2 = revenue.diff().diff()
    sm = d2.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(d2 - sm) != np.sign((d2 - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_055_d2_smoothed_raw_divergence_z(revenue: pd.Series) -> pd.Series:
    """Z-score of (d2 - EMA-d2) over 16Q — magnitude of inflection-like divergence."""
    d2 = revenue.diff().diff()
    sm = d2.ewm(span=4, adjust=False, min_periods=2).mean()
    return _rolling_zscore(d2 - sm, Y4)


def f34_rdjk_056_quarters_since_d2_last_flipped(revenue: pd.Series) -> pd.Series:
    """Quarters since d2 last changed sign."""
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    last = pd.Series(np.where(flip > 0, np.arange(len(flip)), np.nan), index=flip.index).ffill()
    return pd.Series(np.arange(len(flip)), index=flip.index) - last


def f34_rdjk_057_quarters_since_d2_went_negative(revenue: pd.Series) -> pd.Series:
    """Quarters since d2 last became negative (onset of deceleration)."""
    d2 = revenue.diff().diff()
    flag = ((d2 < 0) & (d2.shift(1) >= 0)).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f34_rdjk_058_quarters_since_d2_below_minus_1sigma(revenue: pd.Series) -> pd.Series:
    """Quarters since d2 last fell below -1σ (vs 16Q dist)."""
    d2 = revenue.diff().diff()
    z = _rolling_zscore(d2, Y4)
    flag = (z < -1.0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f34_rdjk_059_accel_inflection_composite_8q(revenue: pd.Series) -> pd.Series:
    """Sum 8Q of (d2 sign-flip + jerk sign-flip)."""
    d2 = revenue.diff().diff()
    j = revenue.diff().diff().diff()
    f1 = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    f2 = (np.sign(j) != np.sign(j.shift(1))).astype(float)
    return (f1 + f2).rolling(Y2, min_periods=3).sum()


def f34_rdjk_060_accel_inflection_magnitude(revenue: pd.Series) -> pd.Series:
    """|d2 - d2.shift(1)| on most recent sign-flip bar — size of recent inflection."""
    d2 = revenue.diff().diff()
    flip = np.sign(d2) != np.sign(d2.shift(1))
    return (d2 - d2.shift(1)).abs().where(flip).ffill()


def f34_rdjk_061_revenue_chg_sign_flip_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of revenue 1Q-change sign-flips inside 8Q."""
    chg = revenue.diff()
    flip = (np.sign(chg) != np.sign(chg.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_062_revenue_chg_slope_flip_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of revenue-slope (4Q slope) sign-flips inside 8Q."""
    sl = _rolling_slope(revenue, Y)
    flip = (np.sign(sl) != np.sign(sl.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_063_revenue_chg_zscore_flip_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of revenue 1Q-chg z-score sign-flips inside 8Q."""
    z = _rolling_zscore(revenue.diff(), Y4)
    flip = (np.sign(z) != np.sign(z.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_064_revenue_chg_ema_raw_spread_8q(revenue: pd.Series) -> pd.Series:
    """Mean 8Q of (revenue 1Q chg - EMA-smoothed 1Q chg) — raw-vs-smoothed gap."""
    chg = revenue.diff()
    sm = chg.ewm(span=4, adjust=False, min_periods=2).mean()
    return (chg - sm).rolling(Y2, min_periods=3).mean()


def f34_rdjk_065_d2_onset_detector_1sigma(revenue: pd.Series) -> pd.Series:
    """First 1Q jerk > 1σ after a stable period (jerk |z|<1 for 4Q) — onset event."""
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(j, Y4)
    stable = (z.abs() < 1.0).rolling(Y, min_periods=2).sum() == Y
    onset = ((z.abs() > 1.0) & stable.shift(1).fillna(False)).astype(float)
    return onset


def f34_rdjk_066_d2_onset_confirmation_2consecutive(revenue: pd.Series) -> pd.Series:
    """1 if jerk |z|>1 for 2 consecutive Q — confirmed onset of jerk regime."""
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(j, Y4)
    flag = ((z.abs() > 1.0) & (z.shift(1).abs() > 1.0)).astype(float)
    return flag


def f34_rdjk_067_d2_onset_confirmation_4q_count(revenue: pd.Series) -> pd.Series:
    """Count of 4Q bars with jerk |z|>1 — sustained-jerk indicator."""
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(j, Y4)
    flag = (z.abs() > 1.0).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f34_rdjk_068_accel_deviation_from_16q_baseline(revenue: pd.Series) -> pd.Series:
    """Current d2 minus 16Q-mean d2 — deviation from long baseline."""
    d2 = revenue.diff().diff()
    return d2 - d2.rolling(Y4, min_periods=6).mean()


def f34_rdjk_069_accel_cum_z_4q(revenue: pd.Series) -> pd.Series:
    """Sum 4Q of d2 z-score."""
    return _rolling_zscore(revenue.diff().diff(), Y4).rolling(Y, min_periods=2).sum()


def f34_rdjk_070_accel_cum_z_8q(revenue: pd.Series) -> pd.Series:
    """Sum 8Q of d2 z-score."""
    return _rolling_zscore(revenue.diff().diff(), Y4).rolling(Y2, min_periods=3).sum()


def f34_rdjk_071_accel_arc_area_8q(revenue: pd.Series) -> pd.Series:
    """Arc area of d2 above 8Q linear fit."""
    d2 = revenue.diff().diff()
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return d2.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f34_rdjk_072_accel_exp_fit_r2_8q(revenue: pd.Series) -> pd.Series:
    """R² of |d2|+1 log-linear fit over 8Q — exponential acceleration-magnitude growth."""
    la = _safe_log(revenue.diff().diff().abs() + 1.0)
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return la.rolling(Y2, min_periods=4).apply(_r2, raw=True)


def f34_rdjk_073_accel_quadratic_fit_r2_8q(revenue: pd.Series) -> pd.Series:
    """R² of quadratic fit of d2 over 8Q."""
    d2 = revenue.diff().diff()
    def _r2q(w):
        if np.isnan(w).any() or len(w) < 4:
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        coef = np.polyfit(x, w, 2)
        pred = np.polyval(coef, x)
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return d2.rolling(Y2, min_periods=4).apply(_r2q, raw=True)


def f34_rdjk_074_yoy_growth_d2_sign_flip_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of YoY-growth 2nd-diff sign-flips over 8Q."""
    yoy_d2 = revenue.pct_change(Y).diff().diff()
    flip = (np.sign(yoy_d2) != np.sign(yoy_d2.shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f34_rdjk_075_yoy_growth_d2_onset_detector(revenue: pd.Series) -> pd.Series:
    """Onset of YoY-growth d2 < -1σ after stable period."""
    yoy_d2 = revenue.pct_change(Y).diff().diff()
    z = _rolling_zscore(yoy_d2, Y4)
    stable = (z.abs() < 1.0).rolling(Y, min_periods=2).sum() == Y
    onset = ((z < -1.0) & stable.shift(1).fillna(False)).astype(float)
    return onset


# ============================================================
#                        REGISTRY
# ============================================================

REVENUE_DECELERATION_JERK_BASE_REGISTRY_001_075 = {
    "f34_rdjk_001_jerk_onset_after_dormancy_8q": {"inputs": ["revenue"], "func": f34_rdjk_001_jerk_onset_after_dormancy_8q},
    "f34_rdjk_002_log_jerk_cliff_after_calm_8q": {"inputs": ["revenue"], "func": f34_rdjk_002_log_jerk_cliff_after_calm_8q},
    "f34_rdjk_003_revenue_jerk_cliff_8q": {"inputs": ["revenue"], "func": f34_rdjk_003_revenue_jerk_cliff_8q},
    "f34_rdjk_004_revenue_jerk_structural_break_8q": {"inputs": ["revenue"], "func": f34_rdjk_004_revenue_jerk_structural_break_8q},
    "f34_rdjk_005_quarters_since_revenue_jerk_positive": {"inputs": ["revenue"], "func": f34_rdjk_005_quarters_since_revenue_jerk_positive},
    "f34_rdjk_006_quarters_since_revenue_jerk_negative": {"inputs": ["revenue"], "func": f34_rdjk_006_quarters_since_revenue_jerk_negative},
    "f34_rdjk_007_jerk_sustained_3consec_neg_indicator": {"inputs": ["revenue"], "func": f34_rdjk_007_jerk_sustained_3consec_neg_indicator},
    "f34_rdjk_008_jerk_magnitude_conditional_on_neg_accel_16q": {"inputs": ["revenue"], "func": f34_rdjk_008_jerk_magnitude_conditional_on_neg_accel_16q},
    "f34_rdjk_009_revenue_jerk_lead_lag_cov_with_yoy_lag1_8q": {"inputs": ["revenue"], "func": f34_rdjk_009_revenue_jerk_lead_lag_cov_with_yoy_lag1_8q},
    "f34_rdjk_010_revenue_jerk_2sigma_count_16q": {"inputs": ["revenue"], "func": f34_rdjk_010_revenue_jerk_2sigma_count_16q},
    "f34_rdjk_011_revenue_jerk_4q_recent_minus_prior_4q": {"inputs": ["revenue"], "func": f34_rdjk_011_revenue_jerk_4q_recent_minus_prior_4q},
    "f34_rdjk_012_revenue_jerk_inflection_sign_flip_8q": {"inputs": ["revenue"], "func": f34_rdjk_012_revenue_jerk_inflection_sign_flip_8q},
    "f34_rdjk_013_revenue_jerk_slope_8q": {"inputs": ["revenue"], "func": f34_rdjk_013_revenue_jerk_slope_8q},
    "f34_rdjk_014_log_revenue_jerk_slope_8q": {"inputs": ["revenue"], "func": f34_rdjk_014_log_revenue_jerk_slope_8q},
    "f34_rdjk_015_cumulative_log_revenue_jerk_8q": {"inputs": ["revenue"], "func": f34_rdjk_015_cumulative_log_revenue_jerk_8q},
    "f34_rdjk_016_revenue_jerk_arc_area_8q": {"inputs": ["revenue"], "func": f34_rdjk_016_revenue_jerk_arc_area_8q},
    "f34_rdjk_017_revenue_jerk_excess_above_8q_linear": {"inputs": ["revenue"], "func": f34_rdjk_017_revenue_jerk_excess_above_8q_linear},
    "f34_rdjk_018_yoy_growth_jerk_z_16q": {"inputs": ["revenue"], "func": f34_rdjk_018_yoy_growth_jerk_z_16q},
    "f34_rdjk_019_yoy_growth_jerk_cliff_8q": {"inputs": ["revenue"], "func": f34_rdjk_019_yoy_growth_jerk_cliff_8q},
    "f34_rdjk_020_yoy_growth_jerk_structural_break_8q": {"inputs": ["revenue"], "func": f34_rdjk_020_yoy_growth_jerk_structural_break_8q},
    "f34_rdjk_021_yoy_growth_jerk_slope_8q": {"inputs": ["revenue"], "func": f34_rdjk_021_yoy_growth_jerk_slope_8q},
    "f34_rdjk_022_jerk_onset_multi_horizon_consistency_4_8_12q": {"inputs": ["revenue"], "func": f34_rdjk_022_jerk_onset_multi_horizon_consistency_4_8_12q},
    "f34_rdjk_023_revenue_jerk_dispersion_cv_8q": {"inputs": ["revenue"], "func": f34_rdjk_023_revenue_jerk_dispersion_cv_8q},
    "f34_rdjk_024_revenue_jerk_percentile_rank_16q": {"inputs": ["revenue"], "func": f34_rdjk_024_revenue_jerk_percentile_rank_16q},
    "f34_rdjk_025_revenue_jerk_cumulative_excess_8q": {"inputs": ["revenue"], "func": f34_rdjk_025_revenue_jerk_cumulative_excess_8q},
    "f34_rdjk_026_accel_sign_flip_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_026_accel_sign_flip_count_8q},
    "f34_rdjk_027_accel_sign_flip_count_16q": {"inputs": ["revenue"], "func": f34_rdjk_027_accel_sign_flip_count_16q},
    "f34_rdjk_028_quarters_since_accel_last_flipped": {"inputs": ["revenue"], "func": f34_rdjk_028_quarters_since_accel_last_flipped},
    "f34_rdjk_029_accel_regime_duration_mean_16q": {"inputs": ["revenue"], "func": f34_rdjk_029_accel_regime_duration_mean_16q},
    "f34_rdjk_030_accel_volatility_8q": {"inputs": ["revenue"], "func": f34_rdjk_030_accel_volatility_8q},
    "f34_rdjk_031_accel_volatility_16q": {"inputs": ["revenue"], "func": f34_rdjk_031_accel_volatility_16q},
    "f34_rdjk_032_accel_4q_recent_minus_prior_4q": {"inputs": ["revenue"], "func": f34_rdjk_032_accel_4q_recent_minus_prior_4q},
    "f34_rdjk_033_accel_range_8q": {"inputs": ["revenue"], "func": f34_rdjk_033_accel_range_8q},
    "f34_rdjk_034_accel_slope_8q": {"inputs": ["revenue"], "func": f34_rdjk_034_accel_slope_8q},
    "f34_rdjk_035_accel_slope_normalized_8q": {"inputs": ["revenue"], "func": f34_rdjk_035_accel_slope_normalized_8q},
    "f34_rdjk_036_accel_cliff_max_1q_chg_8q": {"inputs": ["revenue"], "func": f34_rdjk_036_accel_cliff_max_1q_chg_8q},
    "f34_rdjk_037_negative_accel_streak_max_8q": {"inputs": ["revenue"], "func": f34_rdjk_037_negative_accel_streak_max_8q},
    "f34_rdjk_038_positive_accel_streak_max_8q": {"inputs": ["revenue"], "func": f34_rdjk_038_positive_accel_streak_max_8q},
    "f34_rdjk_039_accel_regime_mismatch_4q_vs_12q": {"inputs": ["revenue"], "func": f34_rdjk_039_accel_regime_mismatch_4q_vs_12q},
    "f34_rdjk_040_accel_regime_zscore_deviation": {"inputs": ["revenue"], "func": f34_rdjk_040_accel_regime_zscore_deviation},
    "f34_rdjk_041_accel_quadratic_c2_8q": {"inputs": ["revenue"], "func": f34_rdjk_041_accel_quadratic_c2_8q},
    "f34_rdjk_042_compound_jerk_cash_burn_4q": {"inputs": ["revenue", "cashneq"], "func": f34_rdjk_042_compound_jerk_cash_burn_4q},
    "f34_rdjk_043_compound_jerk_dilution_4q": {"inputs": ["revenue", "shareswa"], "func": f34_rdjk_043_compound_jerk_dilution_4q},
    "f34_rdjk_044_compound_jerk_margin_compression_4q": {"inputs": ["revenue", "netinc"], "func": f34_rdjk_044_compound_jerk_margin_compression_4q},
    "f34_rdjk_045_compound_jerk_debt_up_4q": {"inputs": ["revenue", "debt"], "func": f34_rdjk_045_compound_jerk_debt_up_4q},
    "f34_rdjk_046_compound_jerk_inst_value_down_4q": {"inputs": ["revenue", "ebit"], "func": f34_rdjk_046_compound_jerk_inst_value_down_4q},
    "f34_rdjk_047_jerk_dispersion_across_periods_8q": {"inputs": ["revenue"], "func": f34_rdjk_047_jerk_dispersion_across_periods_8q},
    "f34_rdjk_048_jerk_vs_baseline_composite_z_4q": {"inputs": ["revenue"], "func": f34_rdjk_048_jerk_vs_baseline_composite_z_4q},
    "f34_rdjk_049_jerk_regime_tail_indicator": {"inputs": ["revenue"], "func": f34_rdjk_049_jerk_regime_tail_indicator},
    "f34_rdjk_050_jerk_consistency_index_8q": {"inputs": ["revenue"], "func": f34_rdjk_050_jerk_consistency_index_8q},
    "f34_rdjk_051_d2_inflection_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_051_d2_inflection_count_8q},
    "f34_rdjk_052_d2_inflection_probability_8q": {"inputs": ["revenue"], "func": f34_rdjk_052_d2_inflection_probability_8q},
    "f34_rdjk_053_d2_sign_flip_cumulative_16q": {"inputs": ["revenue"], "func": f34_rdjk_053_d2_sign_flip_cumulative_16q},
    "f34_rdjk_054_d2_ema_vs_raw_sign_flip_8q": {"inputs": ["revenue"], "func": f34_rdjk_054_d2_ema_vs_raw_sign_flip_8q},
    "f34_rdjk_055_d2_smoothed_raw_divergence_z": {"inputs": ["revenue"], "func": f34_rdjk_055_d2_smoothed_raw_divergence_z},
    "f34_rdjk_056_quarters_since_d2_last_flipped": {"inputs": ["revenue"], "func": f34_rdjk_056_quarters_since_d2_last_flipped},
    "f34_rdjk_057_quarters_since_d2_went_negative": {"inputs": ["revenue"], "func": f34_rdjk_057_quarters_since_d2_went_negative},
    "f34_rdjk_058_quarters_since_d2_below_minus_1sigma": {"inputs": ["revenue"], "func": f34_rdjk_058_quarters_since_d2_below_minus_1sigma},
    "f34_rdjk_059_accel_inflection_composite_8q": {"inputs": ["revenue"], "func": f34_rdjk_059_accel_inflection_composite_8q},
    "f34_rdjk_060_accel_inflection_magnitude": {"inputs": ["revenue"], "func": f34_rdjk_060_accel_inflection_magnitude},
    "f34_rdjk_061_revenue_chg_sign_flip_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_061_revenue_chg_sign_flip_count_8q},
    "f34_rdjk_062_revenue_chg_slope_flip_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_062_revenue_chg_slope_flip_count_8q},
    "f34_rdjk_063_revenue_chg_zscore_flip_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_063_revenue_chg_zscore_flip_count_8q},
    "f34_rdjk_064_revenue_chg_ema_raw_spread_8q": {"inputs": ["revenue"], "func": f34_rdjk_064_revenue_chg_ema_raw_spread_8q},
    "f34_rdjk_065_d2_onset_detector_1sigma": {"inputs": ["revenue"], "func": f34_rdjk_065_d2_onset_detector_1sigma},
    "f34_rdjk_066_d2_onset_confirmation_2consecutive": {"inputs": ["revenue"], "func": f34_rdjk_066_d2_onset_confirmation_2consecutive},
    "f34_rdjk_067_d2_onset_confirmation_4q_count": {"inputs": ["revenue"], "func": f34_rdjk_067_d2_onset_confirmation_4q_count},
    "f34_rdjk_068_accel_deviation_from_16q_baseline": {"inputs": ["revenue"], "func": f34_rdjk_068_accel_deviation_from_16q_baseline},
    "f34_rdjk_069_accel_cum_z_4q": {"inputs": ["revenue"], "func": f34_rdjk_069_accel_cum_z_4q},
    "f34_rdjk_070_accel_cum_z_8q": {"inputs": ["revenue"], "func": f34_rdjk_070_accel_cum_z_8q},
    "f34_rdjk_071_accel_arc_area_8q": {"inputs": ["revenue"], "func": f34_rdjk_071_accel_arc_area_8q},
    "f34_rdjk_072_accel_exp_fit_r2_8q": {"inputs": ["revenue"], "func": f34_rdjk_072_accel_exp_fit_r2_8q},
    "f34_rdjk_073_accel_quadratic_fit_r2_8q": {"inputs": ["revenue"], "func": f34_rdjk_073_accel_quadratic_fit_r2_8q},
    "f34_rdjk_074_yoy_growth_d2_sign_flip_count_8q": {"inputs": ["revenue"], "func": f34_rdjk_074_yoy_growth_d2_sign_flip_count_8q},
    "f34_rdjk_075_yoy_growth_d2_onset_detector": {"inputs": ["revenue"], "func": f34_rdjk_075_yoy_growth_d2_onset_detector},
}
