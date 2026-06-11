"""margin_collapse_jerk d2 features 001_075 — short blowup pipeline 1a-inverse.

Margin jerk pattern detection: turning points, cliffs, regime shifts in the third difference of margin trajectories.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
SF1 quarterly cadence (lags 1, 4, 8, 12, 16, 20 quarters).
"""
import numpy as np
import pandas as pd


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_mad_z(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median().replace(0, np.nan)
    return (s - med) / (1.4826 * mad)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


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


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _sign_safe(s):
    return np.sign(s).where(s.notna(), np.nan)


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool)
    grp = (~b).cumsum()
    return b.astype(int).groupby(grp).cumsum()


def _max_consec_true(b, window):
    return _consec_true_streak(b).rolling(window, min_periods=1).max()


def _rolling_count(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).sum()


def _rolling_frac(b, window):
    return b.fillna(False).astype(float).rolling(window, min_periods=1).mean()


def _winsorize(s, lo=0.1, hi=0.9, window=8, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    qlo = s.rolling(window, min_periods=min_periods).quantile(lo)
    qhi = s.rolling(window, min_periods=min_periods).quantile(hi)
    return s.clip(lower=qlo, upper=qhi)


def _jerk(s):
    """Quarter-over-quarter-over-quarter-over-quarter jerk (third diff)."""
    return s.diff().diff().diff()


def _accel(s):
    return s.diff().diff()


def _gm(revenue, gp):
    return _safe_div(gp, revenue.abs())


def _om(revenue, opinc):
    return _safe_div(opinc, revenue.abs())


def _em(revenue, ebitda):
    return _safe_div(ebitda, revenue.abs())


def _nm(revenue, netinc):
    return _safe_div(netinc, revenue.abs())


def _gm_ttm(revenue, gp):
    return _safe_div(_ttm(gp), _ttm(revenue).abs())


def _om_ttm(revenue, opinc):
    return _safe_div(_ttm(opinc), _ttm(revenue).abs())


def _em_ttm(revenue, ebitda):
    return _safe_div(_ttm(ebitda), _ttm(revenue).abs())


def _nm_ttm(revenue, netinc):
    return _safe_div(_ttm(netinc), _ttm(revenue).abs())


def _cusum(s, window):
    """Rolling CUSUM around mean — peak absolute excursion in window."""
    m = s.rolling(window, min_periods=max(window // 3, 2)).mean()
    dev = s - m
    return dev.rolling(window, min_periods=max(window // 3, 2)).apply(
        lambda w: float(np.nanmax(np.abs(np.nancumsum(w)))) if not np.all(np.isnan(w)) else np.nan, raw=True
    )


# ============================================================
#                    D2 FEATURES 001-075
# ============================================================

def _onset_after_dormancy(margin_series: pd.Series) -> pd.Series:
    """Pattern: |jerk z(8q)| > 3 in current q AND prior 4q calm (|z|<1 ≥75% of time)."""
    j = _jerk(margin_series)
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def _cliff_conditional_low_margin(margin_series: pd.Series) -> pd.Series:
    """Pattern: |jerk| max over 8q, restricted to quarters where margin is in bottom 30% of 12q."""
    j = _jerk(margin_series)
    low = margin_series < margin_series.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def _three_consec_neg_streak_max(margin_series: pd.Series) -> pd.Series:
    """Pattern: 3-consecutive-neg jerk-z streak qualifier, max run over 16q."""
    j = _jerk(margin_series)
    j_z = _rolling_zscore(j, 8)
    neg = (j_z < -1).astype(int)
    streak3 = neg.rolling(3, min_periods=3).sum()
    qual = (streak3 >= 3).astype(int)

    def _maxrun(w):
        if np.all(np.isnan(w)):
            return np.nan
        w = np.nan_to_num(w, nan=0).astype(int)
        best = cur = 0
        for v in w:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        return float(best)

    return qual.rolling(16, min_periods=4).apply(_maxrun, raw=True)


def _multi_horizon_onset(margin_series: pd.Series) -> pd.Series:
    """Pattern: count of horizons (4q/8q/12q) at which |jerk z| > 3 fires this quarter."""
    j = _jerk(margin_series)
    o4 = (_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
    o8 = (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
    o12 = (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0)
    return o4 + o8 + o12


def _lead_lag_cov_jerks(margin_A: pd.Series, margin_B: pd.Series) -> pd.Series:
    """Pattern: cov(jerk_A_t, jerk_B_{t-1}) over 8q — positive => A leads B by 1q."""
    jA = _jerk(margin_A)
    jB = _jerk(margin_B)
    return (jA * jB.shift(1)).rolling(8, min_periods=4).mean()


def f35_mcjk_001_gm_jerk_onset_after_dormancy_4q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    return _onset_after_dormancy(_gm(revenue, gp)).diff().diff()


def f35_mcjk_002_om_jerk_onset_after_dormancy_4q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    return _onset_after_dormancy(_om(revenue, opinc)).diff().diff()


def f35_mcjk_003_em_jerk_onset_after_dormancy_4q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _onset_after_dormancy(_em(revenue, ebitda)).diff().diff()


def f35_mcjk_004_nm_jerk_onset_after_dormancy_4q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    return _onset_after_dormancy(_nm(revenue, netinc)).diff().diff()


def f35_mcjk_005_gm_jerk_cliff_conditional_on_low_margin_8q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    return _cliff_conditional_low_margin(_gm(revenue, gp)).diff().diff()


def f35_mcjk_006_om_jerk_cliff_conditional_on_low_margin_8q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    return _cliff_conditional_low_margin(_om(revenue, opinc)).diff().diff()


def f35_mcjk_007_em_jerk_cliff_conditional_on_low_margin_8q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _cliff_conditional_low_margin(_em(revenue, ebitda)).diff().diff()


def f35_mcjk_008_nm_jerk_cliff_conditional_on_low_margin_8q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    return _cliff_conditional_low_margin(_nm(revenue, netinc)).diff().diff()


def f35_mcjk_009_gm_jerk_3consec_neg_streak_max_16q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    return _three_consec_neg_streak_max(_gm(revenue, gp)).diff().diff()


def f35_mcjk_010_om_jerk_3consec_neg_streak_max_16q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    return _three_consec_neg_streak_max(_om(revenue, opinc)).diff().diff()


def f35_mcjk_011_em_jerk_3consec_neg_streak_max_16q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _three_consec_neg_streak_max(_em(revenue, ebitda)).diff().diff()


def f35_mcjk_012_nm_jerk_3consec_neg_streak_max_16q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    return _three_consec_neg_streak_max(_nm(revenue, netinc)).diff().diff()


def f35_mcjk_013_gm_jerk_multi_horizon_onset_4_8_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    return _multi_horizon_onset(_gm(revenue, gp)).diff().diff()


def f35_mcjk_014_om_jerk_multi_horizon_onset_4_8_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    return _multi_horizon_onset(_om(revenue, opinc)).diff().diff()


def f35_mcjk_015_em_jerk_multi_horizon_onset_4_8_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _multi_horizon_onset(_em(revenue, ebitda)).diff().diff()


def f35_mcjk_016_nm_jerk_multi_horizon_onset_4_8_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    return _multi_horizon_onset(_nm(revenue, netinc)).diff().diff()


def f35_mcjk_017_gm_om_jerk_lead_lag_cov_lag1_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series) -> pd.Series:
    return _lead_lag_cov_jerks(_gm(revenue, gp), _om(revenue, opinc)).diff().diff()


def f35_mcjk_018_om_nm_jerk_lead_lag_cov_lag1_8q_d2(revenue: pd.Series, opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    return _lead_lag_cov_jerks(_om(revenue, opinc), _nm(revenue, netinc)).diff().diff()


def f35_mcjk_019_gm_nm_jerk_lead_lag_cov_lag1_8q_d2(revenue: pd.Series, gp: pd.Series, netinc: pd.Series) -> pd.Series:
    return _lead_lag_cov_jerks(_gm(revenue, gp), _nm(revenue, netinc)).diff().diff()


def f35_mcjk_020_multi_margin_jerk_simultaneous_break_count_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    b_gm = (_rolling_zscore(_jerk(_gm(revenue, gp)), 8).abs() > 2).astype(float).fillna(0)
    b_om = (_rolling_zscore(_jerk(_om(revenue, opinc)), 8).abs() > 2).astype(float).fillna(0)
    b_em = (_rolling_zscore(_jerk(_em(revenue, ebitda)), 8).abs() > 2).astype(float).fillna(0)
    b_nm = (_rolling_zscore(_jerk(_nm(revenue, netinc)), 8).abs() > 2).astype(float).fillna(0)
    return (b_gm + b_om + b_em + b_nm).diff().diff()


def f35_mcjk_021_gm_jerk_signflip_count_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return (_rolling_count(flips, 12)).diff().diff()


def f35_mcjk_022_om_jerk_signflip_count_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return (_rolling_count(flips, 12)).diff().diff()


def f35_mcjk_023_em_jerk_signflip_count_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return (_rolling_count(flips, 12)).diff().diff()


def f35_mcjk_024_nm_jerk_signflip_count_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return (_rolling_count(flips, 12)).diff().diff()


def f35_mcjk_025_gm_jerk_neg_streak_max_16q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    return (_max_consec_true(j < 0, 16)).diff().diff()


def f35_mcjk_026_om_jerk_neg_streak_max_16q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    return (_max_consec_true(j < 0, 16)).diff().diff()


def f35_mcjk_027_em_jerk_neg_streak_max_16q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    return (_max_consec_true(j < 0, 16)).diff().diff()


def f35_mcjk_028_nm_jerk_neg_streak_max_16q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    return (_max_consec_true(j < 0, 16)).diff().diff()


def f35_mcjk_029_gm_jerk_flip_pos_to_neg_4q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    flip = (j < 0) & (j.shift(1) > 0)
    return (_rolling_count(flip, 4)).diff().diff()


def f35_mcjk_030_om_jerk_flip_pos_to_neg_4q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    flip = (j < 0) & (j.shift(1) > 0)
    return (_rolling_count(flip, 4)).diff().diff()


def f35_mcjk_031_em_jerk_flip_pos_to_neg_4q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    flip = (j < 0) & (j.shift(1) > 0)
    return (_rolling_count(flip, 4)).diff().diff()


def f35_mcjk_032_nm_jerk_flip_pos_to_neg_4q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    flip = (j < 0) & (j.shift(1) > 0)
    return (_rolling_count(flip, 4)).diff().diff()


def f35_mcjk_033_gm_jerk_neg_streak_ge3_count_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    streak = _consec_true_streak(j < 0)
    return (_rolling_count(streak == 3, 12)).diff().diff()


def f35_mcjk_034_om_jerk_neg_streak_ge3_count_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    streak = _consec_true_streak(j < 0)
    return (_rolling_count(streak == 3, 12)).diff().diff()


def f35_mcjk_035_em_jerk_neg_streak_ge3_count_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    streak = _consec_true_streak(j < 0)
    return (_rolling_count(streak == 3, 12)).diff().diff()


def f35_mcjk_036_nm_jerk_neg_streak_ge3_count_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    streak = _consec_true_streak(j < 0)
    return (_rolling_count(streak == 3, 12)).diff().diff()


def f35_mcjk_037_gm_jerk_below_median_count_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    med = j.rolling(20, min_periods=5).median()
    return (_rolling_count(j < med, 12)).diff().diff()


def f35_mcjk_038_om_jerk_below_median_count_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    med = j.rolling(20, min_periods=5).median()
    return (_rolling_count(j < med, 12)).diff().diff()


def f35_mcjk_039_em_jerk_below_median_count_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    med = j.rolling(20, min_periods=5).median()
    return (_rolling_count(j < med, 12)).diff().diff()


def f35_mcjk_040_nm_jerk_below_median_count_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    med = j.rolling(20, min_periods=5).median()
    return (_rolling_count(j < med, 12)).diff().diff()


def f35_mcjk_041_gm_jerk_cliff_one_q_2mad_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (((j - med).abs() > 2 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_042_om_jerk_cliff_one_q_2mad_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (((j - med).abs() > 2 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_043_em_jerk_cliff_one_q_2mad_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (((j - med).abs() > 2 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_044_nm_jerk_cliff_one_q_2mad_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (((j - med).abs() > 2 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_045_gm_jerk_cliff_count_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return (_rolling_count(cliff, 12)).diff().diff()


def f35_mcjk_046_om_jerk_cliff_count_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return (_rolling_count(cliff, 12)).diff().diff()


def f35_mcjk_047_em_jerk_cliff_count_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return (_rolling_count(cliff, 12)).diff().diff()


def f35_mcjk_048_nm_jerk_cliff_count_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return (_rolling_count(cliff, 12)).diff().diff()


def f35_mcjk_049_gm_jerk_drawdown_from_8q_max_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    return (j - j.rolling(8, min_periods=3).max()).diff().diff()


def f35_mcjk_050_om_jerk_drawdown_from_8q_max_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    return (j - j.rolling(8, min_periods=3).max()).diff().diff()


def f35_mcjk_051_em_jerk_drawdown_from_8q_max_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    return (j - j.rolling(8, min_periods=3).max()).diff().diff()


def f35_mcjk_052_nm_jerk_drawdown_from_8q_max_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    return (j - j.rolling(8, min_periods=3).max()).diff().diff()


def f35_mcjk_053_gm_jerk_step_down_indicator_8q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    dj = j.diff()
    sd = dj.rolling(8, min_periods=3).std()
    return ((dj < -sd).astype(float)).diff().diff()


def f35_mcjk_054_om_jerk_step_down_indicator_8q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    dj = j.diff()
    sd = dj.rolling(8, min_periods=3).std()
    return ((dj < -sd).astype(float)).diff().diff()


def f35_mcjk_055_em_jerk_step_down_indicator_8q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    dj = j.diff()
    sd = dj.rolling(8, min_periods=3).std()
    return ((dj < -sd).astype(float)).diff().diff()


def f35_mcjk_056_nm_jerk_step_down_indicator_8q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    dj = j.diff()
    sd = dj.rolling(8, min_periods=3).std()
    return ((dj < -sd).astype(float)).diff().diff()


def f35_mcjk_057_gm_jerk_hampel_neg_outlier_12q_d2(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    j = _jerk(_gm(revenue, gp))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j < med - 3 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_058_om_jerk_hampel_neg_outlier_12q_d2(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    j = _jerk(_om(revenue, opinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j < med - 3 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_059_em_jerk_hampel_neg_outlier_12q_d2(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    j = _jerk(_em(revenue, ebitda))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j < med - 3 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_060_nm_jerk_hampel_neg_outlier_12q_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    j = _jerk(_nm(revenue, netinc))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j < med - 3 * 1.4826 * mad).astype(float)).diff().diff()


def f35_mcjk_061_4margin_jerk_all_neg_count_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    all_neg = (g < 0) & (o < 0) & (e < 0) & (n < 0)
    return (_rolling_count(all_neg, 8)).diff().diff()


def f35_mcjk_062_3margin_jerk_all_neg_count_12q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); n = _jerk(_nm(revenue, netinc))
    all_neg = (g < 0) & (o < 0) & (n < 0)
    return (_rolling_count(all_neg, 12)).diff().diff()


def f35_mcjk_063_4margin_jerk_neg_fraction_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    return (((g < 0).astype(float) + (o < 0).astype(float) + (e < 0).astype(float) + (n < 0).astype(float)).rolling(8, min_periods=3).mean() / 4.0).diff().diff()


def f35_mcjk_064_4margin_jerk_concordance_count_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _sign_safe(_jerk(_gm(revenue, gp))); o = _sign_safe(_jerk(_om(revenue, opinc))); e = _sign_safe(_jerk(_em(revenue, ebitda))); n = _sign_safe(_jerk(_nm(revenue, netinc)))
    same = (g == o) & (o == e) & (e == n) & g.notna()
    return (_rolling_count(same, 8)).diff().diff()


def f35_mcjk_065_4margin_jerk_dispersion_z_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    disp = pd.concat([g, o, e, n], axis=1).std(axis=1)
    return (_rolling_zscore(disp, 8)).diff().diff()


def f35_mcjk_066_4margin_jerk_min_signed_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    worst = pd.concat([g, o, e, n], axis=1).min(axis=1)
    return (worst.rolling(8, min_periods=3).mean()).diff().diff()


def f35_mcjk_067_4margin_jerk_compound_score_signed_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _rolling_zscore(_jerk(_gm(revenue, gp)), 8); o = _rolling_zscore(_jerk(_om(revenue, opinc)), 8); e = _rolling_zscore(_jerk(_em(revenue, ebitda)), 8); n = _rolling_zscore(_jerk(_nm(revenue, netinc)), 8)
    return (g + o + e + n).diff().diff()


def f35_mcjk_068_4margin_jerk_compound_score_abs_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _rolling_zscore(_jerk(_gm(revenue, gp)), 8).abs(); o = _rolling_zscore(_jerk(_om(revenue, opinc)), 8).abs(); e = _rolling_zscore(_jerk(_em(revenue, ebitda)), 8).abs(); n = _rolling_zscore(_jerk(_nm(revenue, netinc)), 8).abs()
    return (g + o + e + n).diff().diff()


def f35_mcjk_069_gm_om_jerk_cascade_corr_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc))
    return (g.shift(2).rolling(8, min_periods=3).corr(o)).diff().diff()


def f35_mcjk_070_om_nm_jerk_cascade_corr_8q_d2(revenue: pd.Series, opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    o = _jerk(_om(revenue, opinc)); n = _jerk(_nm(revenue, netinc))
    return (o.shift(1).rolling(8, min_periods=3).corr(n)).diff().diff()


def f35_mcjk_071_gm_jerk_minus_nm_jerk_z_8q_d2(revenue: pd.Series, gp: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _rolling_zscore(_jerk(_gm(revenue, gp)), 8); n = _rolling_zscore(_jerk(_nm(revenue, netinc)), 8)
    return (g - n).diff().diff()


def f35_mcjk_072_4margin_jerk_sign_agreement_count_12q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _sign_safe(_jerk(_gm(revenue, gp))); o = _sign_safe(_jerk(_om(revenue, opinc))); e = _sign_safe(_jerk(_em(revenue, ebitda))); n = _sign_safe(_jerk(_nm(revenue, netinc)))
    same = ((g == o).astype(int) + (o == e).astype(int) + (e == n).astype(int) + (g == n).astype(int)) >= 3
    return (_rolling_count(same, 12)).diff().diff()


def f35_mcjk_073_4margin_jerk_dispersion_diff_8q_vs_16q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    disp = pd.concat([g, o, e, n], axis=1).std(axis=1)
    return (disp.rolling(8, min_periods=3).mean() - disp.rolling(16, min_periods=6).mean()).diff().diff()


def f35_mcjk_074_4margin_jerk_majority_negative_streak_max_12q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)) < 0; o = _jerk(_om(revenue, opinc)) < 0; e = _jerk(_em(revenue, ebitda)) < 0; n = _jerk(_nm(revenue, netinc)) < 0
    majority = (g.astype(int) + o.astype(int) + e.astype(int) + n.astype(int)) >= 3
    return (_max_consec_true(majority, 12)).diff().diff()


def f35_mcjk_075_4margin_jerk_worst_minus_best_8q_d2(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, netinc: pd.Series) -> pd.Series:
    g = _jerk(_gm(revenue, gp)); o = _jerk(_om(revenue, opinc)); e = _jerk(_em(revenue, ebitda)); n = _jerk(_nm(revenue, netinc))
    rng = pd.concat([g, o, e, n], axis=1).max(axis=1) - pd.concat([g, o, e, n], axis=1).min(axis=1)
    return (rng.rolling(8, min_periods=3).mean()).diff().diff()


MARGIN_COLLAPSE_JERK_D2_REGISTRY_001_075 = {
    "f35_mcjk_001_gm_jerk_onset_after_dormancy_4q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_001_gm_jerk_onset_after_dormancy_4q_d2},
    "f35_mcjk_002_om_jerk_onset_after_dormancy_4q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_002_om_jerk_onset_after_dormancy_4q_d2},
    "f35_mcjk_003_em_jerk_onset_after_dormancy_4q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_003_em_jerk_onset_after_dormancy_4q_d2},
    "f35_mcjk_004_nm_jerk_onset_after_dormancy_4q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_004_nm_jerk_onset_after_dormancy_4q_d2},
    "f35_mcjk_005_gm_jerk_cliff_conditional_on_low_margin_8q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_005_gm_jerk_cliff_conditional_on_low_margin_8q_d2},
    "f35_mcjk_006_om_jerk_cliff_conditional_on_low_margin_8q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_006_om_jerk_cliff_conditional_on_low_margin_8q_d2},
    "f35_mcjk_007_em_jerk_cliff_conditional_on_low_margin_8q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_007_em_jerk_cliff_conditional_on_low_margin_8q_d2},
    "f35_mcjk_008_nm_jerk_cliff_conditional_on_low_margin_8q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_008_nm_jerk_cliff_conditional_on_low_margin_8q_d2},
    "f35_mcjk_009_gm_jerk_3consec_neg_streak_max_16q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_009_gm_jerk_3consec_neg_streak_max_16q_d2},
    "f35_mcjk_010_om_jerk_3consec_neg_streak_max_16q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_010_om_jerk_3consec_neg_streak_max_16q_d2},
    "f35_mcjk_011_em_jerk_3consec_neg_streak_max_16q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_011_em_jerk_3consec_neg_streak_max_16q_d2},
    "f35_mcjk_012_nm_jerk_3consec_neg_streak_max_16q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_012_nm_jerk_3consec_neg_streak_max_16q_d2},
    "f35_mcjk_013_gm_jerk_multi_horizon_onset_4_8_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_013_gm_jerk_multi_horizon_onset_4_8_12q_d2},
    "f35_mcjk_014_om_jerk_multi_horizon_onset_4_8_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_014_om_jerk_multi_horizon_onset_4_8_12q_d2},
    "f35_mcjk_015_em_jerk_multi_horizon_onset_4_8_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_015_em_jerk_multi_horizon_onset_4_8_12q_d2},
    "f35_mcjk_016_nm_jerk_multi_horizon_onset_4_8_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_016_nm_jerk_multi_horizon_onset_4_8_12q_d2},
    "f35_mcjk_017_gm_om_jerk_lead_lag_cov_lag1_8q_d2": {"inputs": ["revenue", "gp", "opinc"], "func": f35_mcjk_017_gm_om_jerk_lead_lag_cov_lag1_8q_d2},
    "f35_mcjk_018_om_nm_jerk_lead_lag_cov_lag1_8q_d2": {"inputs": ["revenue", "opinc", "netinc"], "func": f35_mcjk_018_om_nm_jerk_lead_lag_cov_lag1_8q_d2},
    "f35_mcjk_019_gm_nm_jerk_lead_lag_cov_lag1_8q_d2": {"inputs": ["revenue", "gp", "netinc"], "func": f35_mcjk_019_gm_nm_jerk_lead_lag_cov_lag1_8q_d2},
    "f35_mcjk_020_multi_margin_jerk_simultaneous_break_count_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_020_multi_margin_jerk_simultaneous_break_count_8q_d2},
    "f35_mcjk_021_gm_jerk_signflip_count_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_021_gm_jerk_signflip_count_12q_d2},
    "f35_mcjk_022_om_jerk_signflip_count_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_022_om_jerk_signflip_count_12q_d2},
    "f35_mcjk_023_em_jerk_signflip_count_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_023_em_jerk_signflip_count_12q_d2},
    "f35_mcjk_024_nm_jerk_signflip_count_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_024_nm_jerk_signflip_count_12q_d2},
    "f35_mcjk_025_gm_jerk_neg_streak_max_16q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_025_gm_jerk_neg_streak_max_16q_d2},
    "f35_mcjk_026_om_jerk_neg_streak_max_16q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_026_om_jerk_neg_streak_max_16q_d2},
    "f35_mcjk_027_em_jerk_neg_streak_max_16q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_027_em_jerk_neg_streak_max_16q_d2},
    "f35_mcjk_028_nm_jerk_neg_streak_max_16q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_028_nm_jerk_neg_streak_max_16q_d2},
    "f35_mcjk_029_gm_jerk_flip_pos_to_neg_4q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_029_gm_jerk_flip_pos_to_neg_4q_d2},
    "f35_mcjk_030_om_jerk_flip_pos_to_neg_4q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_030_om_jerk_flip_pos_to_neg_4q_d2},
    "f35_mcjk_031_em_jerk_flip_pos_to_neg_4q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_031_em_jerk_flip_pos_to_neg_4q_d2},
    "f35_mcjk_032_nm_jerk_flip_pos_to_neg_4q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_032_nm_jerk_flip_pos_to_neg_4q_d2},
    "f35_mcjk_033_gm_jerk_neg_streak_ge3_count_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_033_gm_jerk_neg_streak_ge3_count_12q_d2},
    "f35_mcjk_034_om_jerk_neg_streak_ge3_count_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_034_om_jerk_neg_streak_ge3_count_12q_d2},
    "f35_mcjk_035_em_jerk_neg_streak_ge3_count_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_035_em_jerk_neg_streak_ge3_count_12q_d2},
    "f35_mcjk_036_nm_jerk_neg_streak_ge3_count_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_036_nm_jerk_neg_streak_ge3_count_12q_d2},
    "f35_mcjk_037_gm_jerk_below_median_count_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_037_gm_jerk_below_median_count_12q_d2},
    "f35_mcjk_038_om_jerk_below_median_count_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_038_om_jerk_below_median_count_12q_d2},
    "f35_mcjk_039_em_jerk_below_median_count_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_039_em_jerk_below_median_count_12q_d2},
    "f35_mcjk_040_nm_jerk_below_median_count_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_040_nm_jerk_below_median_count_12q_d2},
    "f35_mcjk_041_gm_jerk_cliff_one_q_2mad_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_041_gm_jerk_cliff_one_q_2mad_d2},
    "f35_mcjk_042_om_jerk_cliff_one_q_2mad_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_042_om_jerk_cliff_one_q_2mad_d2},
    "f35_mcjk_043_em_jerk_cliff_one_q_2mad_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_043_em_jerk_cliff_one_q_2mad_d2},
    "f35_mcjk_044_nm_jerk_cliff_one_q_2mad_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_044_nm_jerk_cliff_one_q_2mad_d2},
    "f35_mcjk_045_gm_jerk_cliff_count_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_045_gm_jerk_cliff_count_12q_d2},
    "f35_mcjk_046_om_jerk_cliff_count_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_046_om_jerk_cliff_count_12q_d2},
    "f35_mcjk_047_em_jerk_cliff_count_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_047_em_jerk_cliff_count_12q_d2},
    "f35_mcjk_048_nm_jerk_cliff_count_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_048_nm_jerk_cliff_count_12q_d2},
    "f35_mcjk_049_gm_jerk_drawdown_from_8q_max_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_049_gm_jerk_drawdown_from_8q_max_d2},
    "f35_mcjk_050_om_jerk_drawdown_from_8q_max_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_050_om_jerk_drawdown_from_8q_max_d2},
    "f35_mcjk_051_em_jerk_drawdown_from_8q_max_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_051_em_jerk_drawdown_from_8q_max_d2},
    "f35_mcjk_052_nm_jerk_drawdown_from_8q_max_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_052_nm_jerk_drawdown_from_8q_max_d2},
    "f35_mcjk_053_gm_jerk_step_down_indicator_8q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_053_gm_jerk_step_down_indicator_8q_d2},
    "f35_mcjk_054_om_jerk_step_down_indicator_8q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_054_om_jerk_step_down_indicator_8q_d2},
    "f35_mcjk_055_em_jerk_step_down_indicator_8q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_055_em_jerk_step_down_indicator_8q_d2},
    "f35_mcjk_056_nm_jerk_step_down_indicator_8q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_056_nm_jerk_step_down_indicator_8q_d2},
    "f35_mcjk_057_gm_jerk_hampel_neg_outlier_12q_d2": {"inputs": ["revenue", "gp"], "func": f35_mcjk_057_gm_jerk_hampel_neg_outlier_12q_d2},
    "f35_mcjk_058_om_jerk_hampel_neg_outlier_12q_d2": {"inputs": ["revenue", "opinc"], "func": f35_mcjk_058_om_jerk_hampel_neg_outlier_12q_d2},
    "f35_mcjk_059_em_jerk_hampel_neg_outlier_12q_d2": {"inputs": ["revenue", "ebitda"], "func": f35_mcjk_059_em_jerk_hampel_neg_outlier_12q_d2},
    "f35_mcjk_060_nm_jerk_hampel_neg_outlier_12q_d2": {"inputs": ["revenue", "netinc"], "func": f35_mcjk_060_nm_jerk_hampel_neg_outlier_12q_d2},
    "f35_mcjk_061_4margin_jerk_all_neg_count_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_061_4margin_jerk_all_neg_count_8q_d2},
    "f35_mcjk_062_3margin_jerk_all_neg_count_12q_d2": {"inputs": ["revenue", "gp", "opinc", "netinc"], "func": f35_mcjk_062_3margin_jerk_all_neg_count_12q_d2},
    "f35_mcjk_063_4margin_jerk_neg_fraction_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_063_4margin_jerk_neg_fraction_8q_d2},
    "f35_mcjk_064_4margin_jerk_concordance_count_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_064_4margin_jerk_concordance_count_8q_d2},
    "f35_mcjk_065_4margin_jerk_dispersion_z_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_065_4margin_jerk_dispersion_z_8q_d2},
    "f35_mcjk_066_4margin_jerk_min_signed_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_066_4margin_jerk_min_signed_8q_d2},
    "f35_mcjk_067_4margin_jerk_compound_score_signed_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_067_4margin_jerk_compound_score_signed_8q_d2},
    "f35_mcjk_068_4margin_jerk_compound_score_abs_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_068_4margin_jerk_compound_score_abs_8q_d2},
    "f35_mcjk_069_gm_om_jerk_cascade_corr_8q_d2": {"inputs": ["revenue", "gp", "opinc"], "func": f35_mcjk_069_gm_om_jerk_cascade_corr_8q_d2},
    "f35_mcjk_070_om_nm_jerk_cascade_corr_8q_d2": {"inputs": ["revenue", "opinc", "netinc"], "func": f35_mcjk_070_om_nm_jerk_cascade_corr_8q_d2},
    "f35_mcjk_071_gm_jerk_minus_nm_jerk_z_8q_d2": {"inputs": ["revenue", "gp", "netinc"], "func": f35_mcjk_071_gm_jerk_minus_nm_jerk_z_8q_d2},
    "f35_mcjk_072_4margin_jerk_sign_agreement_count_12q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_072_4margin_jerk_sign_agreement_count_12q_d2},
    "f35_mcjk_073_4margin_jerk_dispersion_diff_8q_vs_16q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_073_4margin_jerk_dispersion_diff_8q_vs_16q_d2},
    "f35_mcjk_074_4margin_jerk_majority_negative_streak_max_12q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_074_4margin_jerk_majority_negative_streak_max_12q_d2},
    "f35_mcjk_075_4margin_jerk_worst_minus_best_8q_d2": {"inputs": ["revenue", "gp", "opinc", "ebitda", "netinc"], "func": f35_mcjk_075_4margin_jerk_worst_minus_best_8q_d2},
}
