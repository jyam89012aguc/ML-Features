"""cash_burn_jerk base features 001_075 — short blowup pipeline 1a-inverse.

Cash-flow jerk pattern detection: turning points, cliffs, regime shifts in the third difference of cash-flow trajectories.
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
#                    BASE FEATURES 001-075
# ============================================================

def f36_cbjk_001_ncfo_jerk_onset_after_dormancy_4q(ncfo: pd.Series) -> pd.Series:
    """Pattern: NCFO jerk extreme onset after 4q of calm (|z|<1 for >=75% of prior 4q)."""
    j = _jerk(ncfo)
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f36_cbjk_002_fcf_jerk_onset_after_dormancy_4q(fcf: pd.Series) -> pd.Series:
    """Pattern: FCF jerk extreme onset after 4q of calm."""
    j = _jerk(fcf)
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f36_cbjk_003_cashneq_jerk_onset_after_dormancy_4q(cashneq: pd.Series) -> pd.Series:
    """Pattern: cashneq jerk extreme onset after 4q of calm."""
    j = _jerk(cashneq)
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f36_cbjk_004_fcf_to_assets_jerk_onset_after_dormancy_4q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: FCF/assets jerk extreme onset after 4q of calm."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f36_cbjk_005_ncfo_to_assets_jerk_onset_after_dormancy_4q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: NCFO/assets jerk extreme onset after 4q of calm."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    j_z = _rolling_zscore(j, 8)
    prior_calm = (j_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    fire = (j_z.abs() > 3) & (prior_calm >= 0.75)
    return fire.astype(float).where(j_z.notna(), np.nan)


def f36_cbjk_006_ncfo_jerk_cliff_conditional_on_low_level_8q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pattern: |NCFO jerk| conditional on NCFO/revenue being in bottom 30% of trailing 12q; rolling 8q max."""
    ratio = _safe_div(ncfo, revenue.abs())
    j = _jerk(ncfo)
    low = ratio < ratio.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def f36_cbjk_007_fcf_jerk_cliff_conditional_on_low_level_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pattern: |FCF jerk| conditional on FCF/revenue being in bottom 30% of trailing 12q; rolling 8q max."""
    ratio = _safe_div(fcf, revenue.abs())
    j = _jerk(fcf)
    low = ratio < ratio.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def f36_cbjk_008_cashneq_jerk_cliff_conditional_on_low_runway_8q(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """Pattern: |cashneq jerk| conditional on runway (cashneq/|fcf|) being in bottom 30% of 12q; rolling 8q max."""
    runway = _safe_div(cashneq, fcf.abs())
    j = _jerk(cashneq)
    low = runway < runway.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def f36_cbjk_009_fcf_to_assets_jerk_cliff_conditional_on_low_level_8q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: |FCF/assets jerk| conditional on FCF/assets being in bottom 30% of 12q; rolling 8q max."""
    ratio = _safe_div(fcf, assets.abs())
    j = _jerk(ratio)
    low = ratio < ratio.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def f36_cbjk_010_ncfo_to_assets_jerk_cliff_conditional_on_low_level_8q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: |NCFO/assets jerk| conditional on NCFO/assets being in bottom 30% of 12q; rolling 8q max."""
    ratio = _safe_div(ncfo, assets.abs())
    j = _jerk(ratio)
    low = ratio < ratio.rolling(12, min_periods=4).quantile(0.30)
    return j.abs().where(low, np.nan).rolling(8, min_periods=3).max()


def f36_cbjk_011_ncfo_jerk_3consec_neg_streak_max_16q(ncfo: pd.Series) -> pd.Series:
    """Pattern: max run of 3+ consecutive quarters with NCFO jerk z < -1, over 16q."""
    j = _jerk(ncfo)
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


def f36_cbjk_012_fcf_jerk_3consec_neg_streak_max_16q(fcf: pd.Series) -> pd.Series:
    """Pattern: max run of 3+ consecutive quarters with FCF jerk z < -1, over 16q."""
    j = _jerk(fcf)
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


def f36_cbjk_013_cashneq_jerk_3consec_neg_streak_max_16q(cashneq: pd.Series) -> pd.Series:
    """Pattern: max run of 3+ consecutive quarters with cashneq jerk z < -1, over 16q."""
    j = _jerk(cashneq)
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


def f36_cbjk_014_fcf_to_assets_jerk_3consec_neg_streak_max_16q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: max run of 3+ consecutive quarters with FCF/assets jerk z < -1, over 16q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
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


def f36_cbjk_015_ncfo_to_assets_jerk_3consec_neg_streak_max_16q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: max run of 3+ consecutive quarters with NCFO/assets jerk z < -1, over 16q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
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


def f36_cbjk_016_ncfo_jerk_multi_horizon_onset_4_8_12q(ncfo: pd.Series) -> pd.Series:
    """Pattern: sum of NCFO jerk-z >3 indicators across 4q/8q/12q horizons."""
    j = _jerk(ncfo)
    return ((_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0))


def f36_cbjk_017_fcf_jerk_multi_horizon_onset_4_8_12q(fcf: pd.Series) -> pd.Series:
    """Pattern: sum of FCF jerk-z >3 indicators across 4q/8q/12q horizons."""
    j = _jerk(fcf)
    return ((_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0))


def f36_cbjk_018_cashneq_jerk_multi_horizon_onset_4_8_12q(cashneq: pd.Series) -> pd.Series:
    """Pattern: sum of cashneq jerk-z >3 indicators across 4q/8q/12q horizons."""
    j = _jerk(cashneq)
    return ((_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0))


def f36_cbjk_019_fcf_to_assets_jerk_multi_horizon_onset_4_8_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: sum of FCF/assets jerk-z >3 indicators across 4q/8q/12q horizons."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    return ((_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0))


def f36_cbjk_020_ncfo_to_assets_jerk_multi_horizon_onset_4_8_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Pattern: sum of NCFO/assets jerk-z >3 indicators across 4q/8q/12q horizons."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return ((_rolling_zscore(j, 4).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 8).abs() > 3).astype(float).fillna(0)
            + (_rolling_zscore(j, 12).abs() > 3).astype(float).fillna(0))


def f36_cbjk_021_ncfo_jerk_lead_lag_cov_with_revenue_yoy_8q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pattern: 8q rolling mean of NCFO jerk * lag-1 revenue yoy_pct (lead-lag covariance)."""
    j_primary = _jerk(ncfo)
    yoy_peer = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    return (j_primary * yoy_peer.shift(1)).rolling(8, min_periods=4).mean()


def f36_cbjk_022_fcf_jerk_lead_lag_cov_with_revenue_yoy_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pattern: 8q rolling mean of FCF jerk * lag-1 revenue yoy_pct."""
    j_primary = _jerk(fcf)
    yoy_peer = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    return (j_primary * yoy_peer.shift(1)).rolling(8, min_periods=4).mean()


def f36_cbjk_023_cashneq_jerk_lead_lag_cov_with_debt_yoy_8q(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Pattern: 8q rolling mean of cashneq jerk * lag-1 debt yoy_pct."""
    j_primary = _jerk(cashneq)
    yoy_peer = _safe_div(debt.diff(4), debt.shift(4).abs())
    return (j_primary * yoy_peer.shift(1)).rolling(8, min_periods=4).mean()


def f36_cbjk_024_fcf_to_assets_jerk_lead_lag_cov_with_capex_yoy_8q(fcf: pd.Series, assets: pd.Series, capex: pd.Series) -> pd.Series:
    """Pattern: 8q rolling mean of FCF/assets jerk * lag-1 capex yoy_pct."""
    j_primary = _jerk(_safe_div(fcf, assets.abs()))
    yoy_peer = _safe_div(capex.diff(4), capex.shift(4).abs())
    return (j_primary * yoy_peer.shift(1)).rolling(8, min_periods=4).mean()


def f36_cbjk_025_ncfo_to_assets_jerk_lead_lag_cov_with_netinc_yoy_8q(ncfo: pd.Series, assets: pd.Series, netinc: pd.Series) -> pd.Series:
    """Pattern: 8q rolling mean of NCFO/assets jerk * lag-1 netinc yoy_pct."""
    j_primary = _jerk(_safe_div(ncfo, assets.abs()))
    yoy_peer = _safe_div(netinc.diff(4), netinc.shift(4).abs())
    return (j_primary * yoy_peer.shift(1)).rolling(8, min_periods=4).mean()


def f36_cbjk_026_ncfo_jerk_signflip_count_12q(ncfo: pd.Series) -> pd.Series:
    """Count of ncfo jerk sign-flips in trailing 12q."""
    j = _jerk(ncfo)
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return _rolling_count(flips, 12)


def f36_cbjk_027_fcf_jerk_signflip_count_12q(fcf: pd.Series) -> pd.Series:
    """Count of fcf jerk sign-flips in trailing 12q."""
    j = _jerk(fcf)
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return _rolling_count(flips, 12)


def f36_cbjk_028_cashneq_jerk_signflip_count_12q(cashneq: pd.Series) -> pd.Series:
    """Count of cashneq jerk sign-flips in trailing 12q."""
    j = _jerk(cashneq)
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return _rolling_count(flips, 12)


def f36_cbjk_029_ncfo_a_jerk_signflip_count_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of ncfo_a jerk sign-flips in trailing 12q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return _rolling_count(flips, 12)


def f36_cbjk_030_fcf_a_jerk_signflip_count_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of fcf_a jerk sign-flips in trailing 12q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    s = _sign_safe(j)
    flips = (s != s.shift(1)) & s.shift(1).notna()
    return _rolling_count(flips, 12)


def f36_cbjk_031_ncfo_jerk_neg_streak_max_16q(ncfo: pd.Series) -> pd.Series:
    """Max consecutive negative-jerk quarters in 16q for ncfo."""
    j = _jerk(ncfo)
    return _max_consec_true(j < 0, 16)


def f36_cbjk_032_fcf_jerk_neg_streak_max_16q(fcf: pd.Series) -> pd.Series:
    """Max consecutive negative-jerk quarters in 16q for fcf."""
    j = _jerk(fcf)
    return _max_consec_true(j < 0, 16)


def f36_cbjk_033_cashneq_jerk_neg_streak_max_16q(cashneq: pd.Series) -> pd.Series:
    """Max consecutive negative-jerk quarters in 16q for cashneq."""
    j = _jerk(cashneq)
    return _max_consec_true(j < 0, 16)


def f36_cbjk_034_ncfo_a_jerk_neg_streak_max_16q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Max consecutive negative-jerk quarters in 16q for ncfo_a."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return _max_consec_true(j < 0, 16)


def f36_cbjk_035_fcf_a_jerk_neg_streak_max_16q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Max consecutive negative-jerk quarters in 16q for fcf_a."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    return _max_consec_true(j < 0, 16)


def f36_cbjk_036_ncfo_jerk_flip_pos_to_neg_4q(ncfo: pd.Series) -> pd.Series:
    """Count of ncfo jerk pos-to-neg flips in last 4q."""
    j = _jerk(ncfo)
    flip = (j < 0) & (j.shift(1) > 0)
    return _rolling_count(flip, 4)


def f36_cbjk_037_fcf_jerk_flip_pos_to_neg_4q(fcf: pd.Series) -> pd.Series:
    """Count of fcf jerk pos-to-neg flips in last 4q."""
    j = _jerk(fcf)
    flip = (j < 0) & (j.shift(1) > 0)
    return _rolling_count(flip, 4)


def f36_cbjk_038_cashneq_jerk_flip_pos_to_neg_4q(cashneq: pd.Series) -> pd.Series:
    """Count of cashneq jerk pos-to-neg flips in last 4q."""
    j = _jerk(cashneq)
    flip = (j < 0) & (j.shift(1) > 0)
    return _rolling_count(flip, 4)


def f36_cbjk_039_ncfo_a_jerk_flip_pos_to_neg_4q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of ncfo_a jerk pos-to-neg flips in last 4q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    flip = (j < 0) & (j.shift(1) > 0)
    return _rolling_count(flip, 4)


def f36_cbjk_040_fcf_a_jerk_flip_pos_to_neg_4q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of fcf_a jerk pos-to-neg flips in last 4q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    flip = (j < 0) & (j.shift(1) > 0)
    return _rolling_count(flip, 4)


def f36_cbjk_041_ncfo_jerk_below_median_count_12q(ncfo: pd.Series) -> pd.Series:
    """Count quarters in last 12q where ncfo jerk was below 20q median."""
    j = _jerk(ncfo)
    med = j.rolling(20, min_periods=5).median()
    return _rolling_count(j < med, 12)


def f36_cbjk_042_fcf_jerk_below_median_count_12q(fcf: pd.Series) -> pd.Series:
    """Count quarters in last 12q where fcf jerk was below 20q median."""
    j = _jerk(fcf)
    med = j.rolling(20, min_periods=5).median()
    return _rolling_count(j < med, 12)


def f36_cbjk_043_cashneq_jerk_below_median_count_12q(cashneq: pd.Series) -> pd.Series:
    """Count quarters in last 12q where cashneq jerk was below 20q median."""
    j = _jerk(cashneq)
    med = j.rolling(20, min_periods=5).median()
    return _rolling_count(j < med, 12)


def f36_cbjk_044_ncfo_a_jerk_below_median_count_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Count quarters in last 12q where ncfo_a jerk was below 20q median."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    med = j.rolling(20, min_periods=5).median()
    return _rolling_count(j < med, 12)


def f36_cbjk_045_fcf_a_jerk_below_median_count_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Count quarters in last 12q where fcf_a jerk was below 20q median."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    med = j.rolling(20, min_periods=5).median()
    return _rolling_count(j < med, 12)


def f36_cbjk_046_ncfo_jerk_neg_streak_ge3_count_12q(ncfo: pd.Series) -> pd.Series:
    """Count of ncfo jerk-neg streaks of length >=3 in 12q."""
    j = _jerk(ncfo)
    streak = _consec_true_streak(j < 0)
    return _rolling_count(streak == 3, 12)


def f36_cbjk_047_fcf_jerk_neg_streak_ge3_count_12q(fcf: pd.Series) -> pd.Series:
    """Count of fcf jerk-neg streaks of length >=3 in 12q."""
    j = _jerk(fcf)
    streak = _consec_true_streak(j < 0)
    return _rolling_count(streak == 3, 12)


def f36_cbjk_048_cashneq_jerk_neg_streak_ge3_count_12q(cashneq: pd.Series) -> pd.Series:
    """Count of cashneq jerk-neg streaks of length >=3 in 12q."""
    j = _jerk(cashneq)
    streak = _consec_true_streak(j < 0)
    return _rolling_count(streak == 3, 12)


def f36_cbjk_049_ncfo_a_jerk_neg_streak_ge3_count_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of ncfo_a jerk-neg streaks of length >=3 in 12q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    streak = _consec_true_streak(j < 0)
    return _rolling_count(streak == 3, 12)


def f36_cbjk_050_fcf_a_jerk_neg_streak_ge3_count_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of fcf_a jerk-neg streaks of length >=3 in 12q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    streak = _consec_true_streak(j < 0)
    return _rolling_count(streak == 3, 12)


def f36_cbjk_051_ncfo_jerk_cliff_one_q_2mad(ncfo: pd.Series) -> pd.Series:
    """Indicator: latest ncfo jerk exceeded 2*MAD over 12q."""
    j = _jerk(ncfo)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j - med).abs() > 2 * 1.4826 * mad).astype(float)


def f36_cbjk_052_fcf_jerk_cliff_one_q_2mad(fcf: pd.Series) -> pd.Series:
    """Indicator: latest fcf jerk exceeded 2*MAD over 12q."""
    j = _jerk(fcf)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j - med).abs() > 2 * 1.4826 * mad).astype(float)


def f36_cbjk_053_cashneq_jerk_cliff_one_q_2mad(cashneq: pd.Series) -> pd.Series:
    """Indicator: latest cashneq jerk exceeded 2*MAD over 12q."""
    j = _jerk(cashneq)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j - med).abs() > 2 * 1.4826 * mad).astype(float)


def f36_cbjk_054_ncfo_a_jerk_cliff_one_q_2mad(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: latest ncfo_a jerk exceeded 2*MAD over 12q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j - med).abs() > 2 * 1.4826 * mad).astype(float)


def f36_cbjk_055_fcf_a_jerk_cliff_one_q_2mad(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: latest fcf_a jerk exceeded 2*MAD over 12q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return ((j - med).abs() > 2 * 1.4826 * mad).astype(float)


def f36_cbjk_056_ncfo_jerk_cliff_count_12q(ncfo: pd.Series) -> pd.Series:
    """Count of ncfo jerk cliffs (|jerk|>2*MAD) over trailing 12q."""
    j = _jerk(ncfo)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


def f36_cbjk_057_fcf_jerk_cliff_count_12q(fcf: pd.Series) -> pd.Series:
    """Count of fcf jerk cliffs (|jerk|>2*MAD) over trailing 12q."""
    j = _jerk(fcf)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


def f36_cbjk_058_cashneq_jerk_cliff_count_12q(cashneq: pd.Series) -> pd.Series:
    """Count of cashneq jerk cliffs (|jerk|>2*MAD) over trailing 12q."""
    j = _jerk(cashneq)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


def f36_cbjk_059_ncfo_a_jerk_cliff_count_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of ncfo_a jerk cliffs (|jerk|>2*MAD) over trailing 12q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


def f36_cbjk_060_fcf_a_jerk_cliff_count_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of fcf_a jerk cliffs (|jerk|>2*MAD) over trailing 12q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    cliff = (j - med).abs() > 2 * 1.4826 * mad
    return _rolling_count(cliff, 12)


def f36_cbjk_061_ncfo_jerk_drawdown_from_8q_max(ncfo: pd.Series) -> pd.Series:
    """ncfo jerk minus its 8q rolling max."""
    j = _jerk(ncfo)
    return j - j.rolling(8, min_periods=3).max()


def f36_cbjk_062_fcf_jerk_drawdown_from_8q_max(fcf: pd.Series) -> pd.Series:
    """fcf jerk minus its 8q rolling max."""
    j = _jerk(fcf)
    return j - j.rolling(8, min_periods=3).max()


def f36_cbjk_063_cashneq_jerk_drawdown_from_8q_max(cashneq: pd.Series) -> pd.Series:
    """cashneq jerk minus its 8q rolling max."""
    j = _jerk(cashneq)
    return j - j.rolling(8, min_periods=3).max()


def f36_cbjk_064_ncfo_a_jerk_drawdown_from_8q_max(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """ncfo_a jerk minus its 8q rolling max."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    return j - j.rolling(8, min_periods=3).max()


def f36_cbjk_065_fcf_a_jerk_drawdown_from_8q_max(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """fcf_a jerk minus its 8q rolling max."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    return j - j.rolling(8, min_periods=3).max()


def f36_cbjk_066_ncfo_jerk_hampel_neg_outlier_12q(ncfo: pd.Series) -> pd.Series:
    """Indicator: ncfo jerk below med - 3*MAD over 12q."""
    j = _jerk(ncfo)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (j < med - 3 * 1.4826 * mad).astype(float)


def f36_cbjk_067_fcf_jerk_hampel_neg_outlier_12q(fcf: pd.Series) -> pd.Series:
    """Indicator: fcf jerk below med - 3*MAD over 12q."""
    j = _jerk(fcf)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (j < med - 3 * 1.4826 * mad).astype(float)


def f36_cbjk_068_cashneq_jerk_hampel_neg_outlier_12q(cashneq: pd.Series) -> pd.Series:
    """Indicator: cashneq jerk below med - 3*MAD over 12q."""
    j = _jerk(cashneq)
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (j < med - 3 * 1.4826 * mad).astype(float)


def f36_cbjk_069_ncfo_a_jerk_hampel_neg_outlier_12q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: ncfo_a jerk below med - 3*MAD over 12q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (j < med - 3 * 1.4826 * mad).astype(float)


def f36_cbjk_070_fcf_a_jerk_hampel_neg_outlier_12q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: fcf_a jerk below med - 3*MAD over 12q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    med = j.rolling(12, min_periods=4).median()
    mad = (j - med).abs().rolling(12, min_periods=4).median().replace(0, np.nan)
    return (j < med - 3 * 1.4826 * mad).astype(float)


def f36_cbjk_071_ncfo_jerk_step_down_indicator_8q(ncfo: pd.Series) -> pd.Series:
    """Indicator: jerk's qoq change was below -1*sigma over 8q."""
    j = _jerk(ncfo)
    dj = j.diff(); sd = dj.rolling(8, min_periods=3).std()
    return (dj < -sd).astype(float)


def f36_cbjk_072_fcf_jerk_step_down_indicator_8q(fcf: pd.Series) -> pd.Series:
    """Indicator: jerk's qoq change was below -1*sigma over 8q."""
    j = _jerk(fcf)
    dj = j.diff(); sd = dj.rolling(8, min_periods=3).std()
    return (dj < -sd).astype(float)


def f36_cbjk_073_cashneq_jerk_step_down_indicator_8q(cashneq: pd.Series) -> pd.Series:
    """Indicator: jerk's qoq change was below -1*sigma over 8q."""
    j = _jerk(cashneq)
    dj = j.diff(); sd = dj.rolling(8, min_periods=3).std()
    return (dj < -sd).astype(float)


def f36_cbjk_074_ncfo_a_jerk_step_down_indicator_8q(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: jerk's qoq change was below -1*sigma over 8q."""
    j = _jerk(_safe_div(ncfo, assets.abs()))
    dj = j.diff(); sd = dj.rolling(8, min_periods=3).std()
    return (dj < -sd).astype(float)


def f36_cbjk_075_fcf_a_jerk_step_down_indicator_8q(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Indicator: jerk's qoq change was below -1*sigma over 8q."""
    j = _jerk(_safe_div(fcf, assets.abs()))
    dj = j.diff(); sd = dj.rolling(8, min_periods=3).std()
    return (dj < -sd).astype(float)


CASH_BURN_JERK_BASE_REGISTRY_001_075 = {
    "f36_cbjk_001_ncfo_jerk_onset_after_dormancy_4q": {"inputs": ["ncfo"], "func": f36_cbjk_001_ncfo_jerk_onset_after_dormancy_4q},
    "f36_cbjk_002_fcf_jerk_onset_after_dormancy_4q": {"inputs": ["fcf"], "func": f36_cbjk_002_fcf_jerk_onset_after_dormancy_4q},
    "f36_cbjk_003_cashneq_jerk_onset_after_dormancy_4q": {"inputs": ["cashneq"], "func": f36_cbjk_003_cashneq_jerk_onset_after_dormancy_4q},
    "f36_cbjk_004_fcf_to_assets_jerk_onset_after_dormancy_4q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_004_fcf_to_assets_jerk_onset_after_dormancy_4q},
    "f36_cbjk_005_ncfo_to_assets_jerk_onset_after_dormancy_4q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_005_ncfo_to_assets_jerk_onset_after_dormancy_4q},
    "f36_cbjk_006_ncfo_jerk_cliff_conditional_on_low_level_8q": {"inputs": ["ncfo", "revenue"], "func": f36_cbjk_006_ncfo_jerk_cliff_conditional_on_low_level_8q},
    "f36_cbjk_007_fcf_jerk_cliff_conditional_on_low_level_8q": {"inputs": ["fcf", "revenue"], "func": f36_cbjk_007_fcf_jerk_cliff_conditional_on_low_level_8q},
    "f36_cbjk_008_cashneq_jerk_cliff_conditional_on_low_runway_8q": {"inputs": ["cashneq", "fcf"], "func": f36_cbjk_008_cashneq_jerk_cliff_conditional_on_low_runway_8q},
    "f36_cbjk_009_fcf_to_assets_jerk_cliff_conditional_on_low_level_8q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_009_fcf_to_assets_jerk_cliff_conditional_on_low_level_8q},
    "f36_cbjk_010_ncfo_to_assets_jerk_cliff_conditional_on_low_level_8q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_010_ncfo_to_assets_jerk_cliff_conditional_on_low_level_8q},
    "f36_cbjk_011_ncfo_jerk_3consec_neg_streak_max_16q": {"inputs": ["ncfo"], "func": f36_cbjk_011_ncfo_jerk_3consec_neg_streak_max_16q},
    "f36_cbjk_012_fcf_jerk_3consec_neg_streak_max_16q": {"inputs": ["fcf"], "func": f36_cbjk_012_fcf_jerk_3consec_neg_streak_max_16q},
    "f36_cbjk_013_cashneq_jerk_3consec_neg_streak_max_16q": {"inputs": ["cashneq"], "func": f36_cbjk_013_cashneq_jerk_3consec_neg_streak_max_16q},
    "f36_cbjk_014_fcf_to_assets_jerk_3consec_neg_streak_max_16q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_014_fcf_to_assets_jerk_3consec_neg_streak_max_16q},
    "f36_cbjk_015_ncfo_to_assets_jerk_3consec_neg_streak_max_16q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_015_ncfo_to_assets_jerk_3consec_neg_streak_max_16q},
    "f36_cbjk_016_ncfo_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["ncfo"], "func": f36_cbjk_016_ncfo_jerk_multi_horizon_onset_4_8_12q},
    "f36_cbjk_017_fcf_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["fcf"], "func": f36_cbjk_017_fcf_jerk_multi_horizon_onset_4_8_12q},
    "f36_cbjk_018_cashneq_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["cashneq"], "func": f36_cbjk_018_cashneq_jerk_multi_horizon_onset_4_8_12q},
    "f36_cbjk_019_fcf_to_assets_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_019_fcf_to_assets_jerk_multi_horizon_onset_4_8_12q},
    "f36_cbjk_020_ncfo_to_assets_jerk_multi_horizon_onset_4_8_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_020_ncfo_to_assets_jerk_multi_horizon_onset_4_8_12q},
    "f36_cbjk_021_ncfo_jerk_lead_lag_cov_with_revenue_yoy_8q": {"inputs": ["ncfo", "revenue"], "func": f36_cbjk_021_ncfo_jerk_lead_lag_cov_with_revenue_yoy_8q},
    "f36_cbjk_022_fcf_jerk_lead_lag_cov_with_revenue_yoy_8q": {"inputs": ["fcf", "revenue"], "func": f36_cbjk_022_fcf_jerk_lead_lag_cov_with_revenue_yoy_8q},
    "f36_cbjk_023_cashneq_jerk_lead_lag_cov_with_debt_yoy_8q": {"inputs": ["cashneq", "debt"], "func": f36_cbjk_023_cashneq_jerk_lead_lag_cov_with_debt_yoy_8q},
    "f36_cbjk_024_fcf_to_assets_jerk_lead_lag_cov_with_capex_yoy_8q": {"inputs": ["fcf", "assets", "capex"], "func": f36_cbjk_024_fcf_to_assets_jerk_lead_lag_cov_with_capex_yoy_8q},
    "f36_cbjk_025_ncfo_to_assets_jerk_lead_lag_cov_with_netinc_yoy_8q": {"inputs": ["ncfo", "assets", "netinc"], "func": f36_cbjk_025_ncfo_to_assets_jerk_lead_lag_cov_with_netinc_yoy_8q},
    "f36_cbjk_026_ncfo_jerk_signflip_count_12q": {"inputs": ["ncfo"], "func": f36_cbjk_026_ncfo_jerk_signflip_count_12q},
    "f36_cbjk_027_fcf_jerk_signflip_count_12q": {"inputs": ["fcf"], "func": f36_cbjk_027_fcf_jerk_signflip_count_12q},
    "f36_cbjk_028_cashneq_jerk_signflip_count_12q": {"inputs": ["cashneq"], "func": f36_cbjk_028_cashneq_jerk_signflip_count_12q},
    "f36_cbjk_029_ncfo_a_jerk_signflip_count_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_029_ncfo_a_jerk_signflip_count_12q},
    "f36_cbjk_030_fcf_a_jerk_signflip_count_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_030_fcf_a_jerk_signflip_count_12q},
    "f36_cbjk_031_ncfo_jerk_neg_streak_max_16q": {"inputs": ["ncfo"], "func": f36_cbjk_031_ncfo_jerk_neg_streak_max_16q},
    "f36_cbjk_032_fcf_jerk_neg_streak_max_16q": {"inputs": ["fcf"], "func": f36_cbjk_032_fcf_jerk_neg_streak_max_16q},
    "f36_cbjk_033_cashneq_jerk_neg_streak_max_16q": {"inputs": ["cashneq"], "func": f36_cbjk_033_cashneq_jerk_neg_streak_max_16q},
    "f36_cbjk_034_ncfo_a_jerk_neg_streak_max_16q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_034_ncfo_a_jerk_neg_streak_max_16q},
    "f36_cbjk_035_fcf_a_jerk_neg_streak_max_16q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_035_fcf_a_jerk_neg_streak_max_16q},
    "f36_cbjk_036_ncfo_jerk_flip_pos_to_neg_4q": {"inputs": ["ncfo"], "func": f36_cbjk_036_ncfo_jerk_flip_pos_to_neg_4q},
    "f36_cbjk_037_fcf_jerk_flip_pos_to_neg_4q": {"inputs": ["fcf"], "func": f36_cbjk_037_fcf_jerk_flip_pos_to_neg_4q},
    "f36_cbjk_038_cashneq_jerk_flip_pos_to_neg_4q": {"inputs": ["cashneq"], "func": f36_cbjk_038_cashneq_jerk_flip_pos_to_neg_4q},
    "f36_cbjk_039_ncfo_a_jerk_flip_pos_to_neg_4q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_039_ncfo_a_jerk_flip_pos_to_neg_4q},
    "f36_cbjk_040_fcf_a_jerk_flip_pos_to_neg_4q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_040_fcf_a_jerk_flip_pos_to_neg_4q},
    "f36_cbjk_041_ncfo_jerk_below_median_count_12q": {"inputs": ["ncfo"], "func": f36_cbjk_041_ncfo_jerk_below_median_count_12q},
    "f36_cbjk_042_fcf_jerk_below_median_count_12q": {"inputs": ["fcf"], "func": f36_cbjk_042_fcf_jerk_below_median_count_12q},
    "f36_cbjk_043_cashneq_jerk_below_median_count_12q": {"inputs": ["cashneq"], "func": f36_cbjk_043_cashneq_jerk_below_median_count_12q},
    "f36_cbjk_044_ncfo_a_jerk_below_median_count_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_044_ncfo_a_jerk_below_median_count_12q},
    "f36_cbjk_045_fcf_a_jerk_below_median_count_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_045_fcf_a_jerk_below_median_count_12q},
    "f36_cbjk_046_ncfo_jerk_neg_streak_ge3_count_12q": {"inputs": ["ncfo"], "func": f36_cbjk_046_ncfo_jerk_neg_streak_ge3_count_12q},
    "f36_cbjk_047_fcf_jerk_neg_streak_ge3_count_12q": {"inputs": ["fcf"], "func": f36_cbjk_047_fcf_jerk_neg_streak_ge3_count_12q},
    "f36_cbjk_048_cashneq_jerk_neg_streak_ge3_count_12q": {"inputs": ["cashneq"], "func": f36_cbjk_048_cashneq_jerk_neg_streak_ge3_count_12q},
    "f36_cbjk_049_ncfo_a_jerk_neg_streak_ge3_count_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_049_ncfo_a_jerk_neg_streak_ge3_count_12q},
    "f36_cbjk_050_fcf_a_jerk_neg_streak_ge3_count_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_050_fcf_a_jerk_neg_streak_ge3_count_12q},
    "f36_cbjk_051_ncfo_jerk_cliff_one_q_2mad": {"inputs": ["ncfo"], "func": f36_cbjk_051_ncfo_jerk_cliff_one_q_2mad},
    "f36_cbjk_052_fcf_jerk_cliff_one_q_2mad": {"inputs": ["fcf"], "func": f36_cbjk_052_fcf_jerk_cliff_one_q_2mad},
    "f36_cbjk_053_cashneq_jerk_cliff_one_q_2mad": {"inputs": ["cashneq"], "func": f36_cbjk_053_cashneq_jerk_cliff_one_q_2mad},
    "f36_cbjk_054_ncfo_a_jerk_cliff_one_q_2mad": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_054_ncfo_a_jerk_cliff_one_q_2mad},
    "f36_cbjk_055_fcf_a_jerk_cliff_one_q_2mad": {"inputs": ["fcf", "assets"], "func": f36_cbjk_055_fcf_a_jerk_cliff_one_q_2mad},
    "f36_cbjk_056_ncfo_jerk_cliff_count_12q": {"inputs": ["ncfo"], "func": f36_cbjk_056_ncfo_jerk_cliff_count_12q},
    "f36_cbjk_057_fcf_jerk_cliff_count_12q": {"inputs": ["fcf"], "func": f36_cbjk_057_fcf_jerk_cliff_count_12q},
    "f36_cbjk_058_cashneq_jerk_cliff_count_12q": {"inputs": ["cashneq"], "func": f36_cbjk_058_cashneq_jerk_cliff_count_12q},
    "f36_cbjk_059_ncfo_a_jerk_cliff_count_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_059_ncfo_a_jerk_cliff_count_12q},
    "f36_cbjk_060_fcf_a_jerk_cliff_count_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_060_fcf_a_jerk_cliff_count_12q},
    "f36_cbjk_061_ncfo_jerk_drawdown_from_8q_max": {"inputs": ["ncfo"], "func": f36_cbjk_061_ncfo_jerk_drawdown_from_8q_max},
    "f36_cbjk_062_fcf_jerk_drawdown_from_8q_max": {"inputs": ["fcf"], "func": f36_cbjk_062_fcf_jerk_drawdown_from_8q_max},
    "f36_cbjk_063_cashneq_jerk_drawdown_from_8q_max": {"inputs": ["cashneq"], "func": f36_cbjk_063_cashneq_jerk_drawdown_from_8q_max},
    "f36_cbjk_064_ncfo_a_jerk_drawdown_from_8q_max": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_064_ncfo_a_jerk_drawdown_from_8q_max},
    "f36_cbjk_065_fcf_a_jerk_drawdown_from_8q_max": {"inputs": ["fcf", "assets"], "func": f36_cbjk_065_fcf_a_jerk_drawdown_from_8q_max},
    "f36_cbjk_066_ncfo_jerk_hampel_neg_outlier_12q": {"inputs": ["ncfo"], "func": f36_cbjk_066_ncfo_jerk_hampel_neg_outlier_12q},
    "f36_cbjk_067_fcf_jerk_hampel_neg_outlier_12q": {"inputs": ["fcf"], "func": f36_cbjk_067_fcf_jerk_hampel_neg_outlier_12q},
    "f36_cbjk_068_cashneq_jerk_hampel_neg_outlier_12q": {"inputs": ["cashneq"], "func": f36_cbjk_068_cashneq_jerk_hampel_neg_outlier_12q},
    "f36_cbjk_069_ncfo_a_jerk_hampel_neg_outlier_12q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_069_ncfo_a_jerk_hampel_neg_outlier_12q},
    "f36_cbjk_070_fcf_a_jerk_hampel_neg_outlier_12q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_070_fcf_a_jerk_hampel_neg_outlier_12q},
    "f36_cbjk_071_ncfo_jerk_step_down_indicator_8q": {"inputs": ["ncfo"], "func": f36_cbjk_071_ncfo_jerk_step_down_indicator_8q},
    "f36_cbjk_072_fcf_jerk_step_down_indicator_8q": {"inputs": ["fcf"], "func": f36_cbjk_072_fcf_jerk_step_down_indicator_8q},
    "f36_cbjk_073_cashneq_jerk_step_down_indicator_8q": {"inputs": ["cashneq"], "func": f36_cbjk_073_cashneq_jerk_step_down_indicator_8q},
    "f36_cbjk_074_ncfo_a_jerk_step_down_indicator_8q": {"inputs": ["ncfo", "assets"], "func": f36_cbjk_074_ncfo_a_jerk_step_down_indicator_8q},
    "f36_cbjk_075_fcf_a_jerk_step_down_indicator_8q": {"inputs": ["fcf", "assets"], "func": f36_cbjk_075_fcf_a_jerk_step_down_indicator_8q},
}
