"""
78_marketcap_destruction — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative market-cap destruction features — acceleration of velocity
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
  NO raw price/volume or quarterly SF1 fundamental inputs.
Each feature computes a further .diff(n) or slope/pct-change of a 2nd-derivative concept.
All features are strictly backward-looking; no forward information is used.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   = 63
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

# ── Utility helpers ────────────────────────────────────────────────────────────

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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar per window)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi   = np.arange(n, dtype=float)
        xi_m = xi.mean()
        xm   = x.mean()
        num  = ((xi - xi_m) * (x - xm)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── 3rd-Derivative Feature Functions ──────────────────────────────────────────

def mcd_drv3_001_mc_dd_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc drawdown) — acceleration of drawdown velocity."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    vel   = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_002_mc_dd_ath_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of ATH mc drawdown) — acceleration of ATH distress velocity."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_003_mc_dd_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day mc drawdown) — acceleration of quarterly velocity."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_004_mc_log_dd_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log 252-day mc drawdown) — log acceleration."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    logdd = _log_safe(marketcap) - _log_safe(pk)
    vel   = logdd.diff(5)
    return vel.diff(5)


def mcd_drv3_005_mc_log_dd_ath_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of log ATH mc drawdown) — acceleration of monthly log velocity."""
    pk    = marketcap.expanding(min_periods=1).max()
    logdd = _log_safe(marketcap) - _log_safe(pk)
    vel   = logdd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_006_mc_dd_vol_adj_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of vol-adj 252-day mc dd) — acceleration of vol-adj velocity."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), _TD_YEAR)
    ddv = _safe_div(dd, vol)
    vel = ddv.diff(5)
    return vel.diff(5)


def mcd_drv3_007_mc_underwater_frac_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day underwater fraction) — acceleration of distress-day growth."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    below = (dd < 0).astype(float)
    frac  = _rolling_mean(below, _TD_YEAR)
    vel   = frac.diff(5)
    return vel.diff(5)


def mcd_drv3_008_mc_avg_dd_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of rolling-mean 252-day mc dd) — acceleration of avg-dd worsening."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    avg = _rolling_mean(dd, _TD_YEAR)
    vel = avg.diff(5)
    return vel.diff(5)


def mcd_drv3_009_mc_dd_zscore_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc drawdown z-score) — acceleration of statistical extremity."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    z   = _zscore_rolling(dd, _TD_YEAR)
    vel = z.diff(5)
    return vel.diff(5)


def mcd_drv3_010_mc_252d_pct_change_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 252-day mc pct-change) — 3rd-order annual destruction signal."""
    chg252 = marketcap.pct_change(_TD_YEAR)
    vel    = chg252.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_011_mc_21d_pct_change_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day mc pct-change) — acceleration of monthly decay rate."""
    chg21 = marketcap.pct_change(_TD_MON)
    vel   = chg21.diff(5)
    return vel.diff(5)


def mcd_drv3_012_mc_dd_252d_21d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day mc dd over 21d (curvature of deterioration trend)."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_MON)
    return slope.diff(5)


def mcd_drv3_013_mc_dd_ath_63d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of ATH mc dd over 63d (curvature of quarterly ATH trend)."""
    pk    = marketcap.expanding(min_periods=1).max()
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_QTR)
    return slope.diff(5)


def mcd_drv3_014_mc_daily_vol_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day annualized mc vol) — vol acceleration of vol."""
    chg = marketcap.pct_change(1)
    vol = _rolling_std(chg, _TD_QTR) * np.sqrt(_TD_YEAR)
    vel = vol.diff(5)
    return vel.diff(5)


def mcd_drv3_015_mc_down_frac_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day down-day fraction) — acceleration of down-day growth."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_QTR)
    vel  = frac.diff(5)
    return vel.diff(5)


def mcd_drv3_016_mc_vs_sma252_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of mc vs 252-day SMA deviation) — acceleration of SMA compression."""
    ma  = _rolling_mean(marketcap, _TD_YEAR)
    dev = _safe_div(marketcap - ma, ma)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_017_mc_dd_pct_rank_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of percentile rank of 252-day mc dd) — rank acceleration."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    rank = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel  = rank.diff(5)
    return vel.diff(5)


def mcd_drv3_018_mc_dd_area_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day mc dd area) — area accumulation acceleration."""
    pk   = _rolling_max(marketcap, _TD_QTR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_QTR)
    vel  = area.diff(5)
    return vel.diff(5)


def mcd_drv3_019_ev_dd_252d_5d_diff_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day EV drawdown) — acceleration of EV destruction."""
    pk  = _rolling_max(ev, _TD_YEAR)
    dd  = _safe_div(ev - pk, pk)
    vel = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_020_mc_dd_252d_63d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day mc dd over 63d (curvature of quarterly trend)."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_QTR)
    return slope.diff(5)


def mcd_drv3_021_mc_worst_21d_drop_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of worst-21d-drop in 252d window) — curvature of worst-drop trend."""
    chg   = marketcap.pct_change(_TD_MON)
    worst = chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    vel   = worst.diff(5)
    return vel.diff(5)


def mcd_drv3_022_mc_log_level_vs_252d_avg_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-mc vs log-252d-avg) — 3rd-order compression acceleration."""
    dev = _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, _TD_YEAR))
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_023_mc_dd_convexity_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc dd convexity) — higher-order convexity change."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    avg  = _rolling_mean(dd, _TD_YEAR)
    mxdd = _rolling_min(dd, _TD_YEAR)
    cvx  = _safe_div(avg, mxdd)
    vel  = cvx.diff(5)
    return vel.diff(5)


def mcd_drv3_024_mc_ev_combined_dd_5d_diff_5d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of avg mc+EV 252-day drawdown) — combined destruction acceleration."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    combo = (dd_mc + dd_ev) / 2.0
    vel   = combo.diff(5)
    return vel.diff(5)


def mcd_drv3_025_mc_dd_252d_21d_slope_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (OLS slope over 21 days of 252-day mc dd) — curvature of curvature."""
    pk     = _rolling_max(marketcap, _TD_YEAR)
    dd     = _safe_div(marketcap - pk, pk)
    slope1 = _linslope(dd, _TD_MON)
    return _linslope(slope1, _TD_MON)


# --- 3rd Derivative Extensions (drv3_026 - drv3_075) ---

def mcd_drv3_026_mc_dd_252d_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 252-day mc dd) — 3rd-order monthly deterioration."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_027_mc_dd_ath_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of ATH mc dd) — 3rd-order ATH monthly velocity."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_028_mc_dd_63d_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 63-day mc dd) — acceleration of quarterly monthly velocity."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_029_mc_dd_252d_63d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (63-day diff of 252-day mc dd) — acceleration of quarterly annual velocity."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_QTR)
    return vel.diff(5)


def mcd_drv3_030_mc_dd_ath_63d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (63-day diff of ATH mc dd) — acceleration of ATH quarterly velocity."""
    pk  = marketcap.expanding(min_periods=1).max()
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_QTR)
    return vel.diff(5)


def mcd_drv3_031_mc_63d_pct_change_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day mc pct-change) — acceleration of quarterly decay rate."""
    chg = marketcap.pct_change(_TD_QTR)
    vel = chg.diff(5)
    return vel.diff(5)


def mcd_drv3_032_mc_126d_pct_change_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 126-day mc pct-change) — acceleration of half-year decay rate."""
    chg = marketcap.pct_change(_TD_HALF)
    vel = chg.diff(5)
    return vel.diff(5)


def mcd_drv3_033_mc_dd_126d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 126-day mc dd) — acceleration of half-year drawdown velocity."""
    pk  = _rolling_max(marketcap, _TD_HALF)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_034_mc_dd_504d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 504-day mc dd) — acceleration of 2-year drawdown velocity."""
    pk  = _rolling_max(marketcap, 504)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(5)
    return vel.diff(5)


def mcd_drv3_035_mc_down_frac_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day down-day fraction) — acceleration of annual distress growth."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_YEAR)
    vel  = frac.diff(5)
    return vel.diff(5)


def mcd_drv3_036_mc_underwater_frac_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day underwater fraction) — acceleration of quarterly submersion."""
    pk    = _rolling_max(marketcap, _TD_QTR)
    below = (marketcap < pk).astype(float)
    frac  = _rolling_mean(below, _TD_QTR)
    vel   = frac.diff(5)
    return vel.diff(5)


def mcd_drv3_037_mc_avg_dd_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of mean 63-day mc dd) — acceleration of quarterly avg-dd worsening."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    avg = _rolling_mean(dd, _TD_QTR)
    vel = avg.diff(5)
    return vel.diff(5)


def mcd_drv3_038_mc_daily_vol_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day annualized mc vol) — vol-of-vol acceleration."""
    chg = marketcap.pct_change(1)
    vol = _rolling_std(chg, _TD_YEAR) * np.sqrt(_TD_YEAR)
    vel = vol.diff(5)
    return vel.diff(5)


def mcd_drv3_039_mc_vs_sma63_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of mc vs 63-day SMA deviation) — acceleration of quarterly SMA compression."""
    ma  = _rolling_mean(marketcap, _TD_QTR)
    dev = _safe_div(marketcap - ma, ma)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_040_mc_vs_ema21_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of mc vs 21-day EMA deviation) — acceleration of short EMA compression."""
    ma  = _ewm_mean(marketcap, _TD_MON)
    dev = _safe_div(marketcap - ma, ma)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_041_mc_vs_ema63_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of mc vs 63-day EMA deviation) — acceleration of quarterly EMA compression."""
    ma  = _ewm_mean(marketcap, _TD_QTR)
    dev = _safe_div(marketcap - ma, ma)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_042_mc_dd_area_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc dd area) — area accumulation acceleration."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_YEAR)
    vel  = area.diff(5)
    return vel.diff(5)


def mcd_drv3_043_mc_dd_252d_126d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day mc dd over 126d (curvature of half-year trend)."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_HALF)
    return slope.diff(5)


def mcd_drv3_044_mc_dd_ath_21d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of ATH mc dd over 21d (curvature of short ATH trend)."""
    pk    = marketcap.expanding(min_periods=1).max()
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_MON)
    return slope.diff(5)


def mcd_drv3_045_mc_dd_126d_21d_slope_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 126-day mc dd over 21d (curvature of half-year short trend)."""
    pk    = _rolling_max(marketcap, _TD_HALF)
    dd    = _safe_div(marketcap - pk, pk)
    slope = _linslope(dd, _TD_MON)
    return slope.diff(5)


def mcd_drv3_046_mc_zscore_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc z-score) — acceleration of z-score deterioration."""
    z   = _zscore_rolling(marketcap, _TD_YEAR)
    vel = z.diff(5)
    return vel.diff(5)


def mcd_drv3_047_mc_pct_rank_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc percentile rank) — rank acceleration."""
    rank = marketcap.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel  = rank.diff(5)
    return vel.diff(5)


def mcd_drv3_048_mc_worst_5d_drop_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of worst-5d-drop in 252d) — curvature of worst-drop trend."""
    chg   = marketcap.pct_change(5)
    worst = chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    vel   = worst.diff(5)
    return vel.diff(5)


def mcd_drv3_049_mc_sum_neg_1d_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of sum of negative daily mc changes over 63d) — 3rd-order damage."""
    chg  = marketcap.pct_change(1)
    neg  = chg.where(chg < 0, other=0.0)
    ssum = _rolling_sum(neg, _TD_QTR)
    vel  = ssum.diff(5)
    return vel.diff(5)


def mcd_drv3_050_mc_dd_vol_of_dd_63d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of std-dev of 63-day mc dd) — volatility-of-volatility acceleration."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(dd, _TD_QTR)
    vel = vol.diff(5)
    return vel.diff(5)


def mcd_drv3_051_ev_dd_252d_21d_diff_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 252-day EV dd) — acceleration of monthly EV velocity."""
    pk  = _rolling_max(ev, _TD_YEAR)
    dd  = _safe_div(ev - pk, pk)
    vel = dd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_052_ev_dd_252d_63d_slope_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day EV dd over 63d — curvature of EV quarterly trend."""
    pk    = _rolling_max(ev, _TD_YEAR)
    dd    = _safe_div(ev - pk, pk)
    slope = _linslope(dd, _TD_QTR)
    return slope.diff(5)


def mcd_drv3_053_ev_vs_sma252_5d_diff_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EV vs 252-day SMA deviation) — acceleration of EV SMA compression."""
    ma  = _rolling_mean(ev, _TD_YEAR)
    dev = _safe_div(ev - ma, ma)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_054_mc_dd_zscore_504d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 504-day mc dd z-score) — long-window z-score curvature."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    z   = _zscore_rolling(dd, 504)
    vel = z.diff(5)
    return vel.diff(5)


def mcd_drv3_055_mc_ewm_dd_peak_21d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-21d-smoothed 252d-dd) — acceleration of smooth drawdown."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    edd = _ewm_mean(dd, _TD_MON)
    vel = edd.diff(5)
    return vel.diff(5)


def mcd_drv3_056_mc_dd_intensity_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day mc dd intensity) — curvature of intensity ratio."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    mxdd = _rolling_min(dd, _TD_YEAR)
    intn = _safe_div(dd, mxdd)
    vel  = intn.diff(5)
    return vel.diff(5)


def mcd_drv3_057_mc_sma21_vs_sma63_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day vs 63-day SMA spread) — acceleration of short-vs-medium compression."""
    s21 = _rolling_mean(marketcap, _TD_MON)
    s63 = _rolling_mean(marketcap, _TD_QTR)
    dev = _safe_div(s21 - s63, s63)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_058_mc_sma63_vs_sma252_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day vs 252-day SMA spread) — acceleration of medium-vs-annual compression."""
    s63  = _rolling_mean(marketcap, _TD_QTR)
    s252 = _rolling_mean(marketcap, _TD_YEAR)
    dev  = _safe_div(s63 - s252, s252)
    vel  = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_059_mc_dd_ratio_63d_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d/252d mc dd ratio) — acceleration of ratio change."""
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    rat   = _safe_div(dd63, dd252)
    vel   = rat.diff(5)
    return vel.diff(5)


def mcd_drv3_060_mc_dd_composite_weighted_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite mc dd 50/30/20) — acceleration of composite destruction."""
    pk21  = _rolling_max(marketcap, _TD_MON)
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd21  = _safe_div(marketcap - pk21,  pk21)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    combo = 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252
    vel   = combo.diff(5)
    return vel.diff(5)


def mcd_drv3_061_mc_ev_ratio_5d_diff_5d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of MC/EV ratio) — acceleration of leverage-cap fraction change."""
    ratio = _safe_div(marketcap, ev)
    vel   = ratio.diff(5)
    return vel.diff(5)


def mcd_drv3_062_mc_ev_combined_dd_21d_diff_5d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of avg mc+EV 252d dd) — acceleration of combined monthly velocity."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    combo = (dd_mc + dd_ev) / 2.0
    vel   = combo.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_063_mc_dd_252d_1d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (1-day diff of 252-day mc dd) — acceleration of daily drawdown changes."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(1)
    return vel.diff(5)


def mcd_drv3_064_mc_pct_above_252d_low_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of pct-above-252d-low) — acceleration of trough approach."""
    lo  = _rolling_min(marketcap, _TD_YEAR)
    dev = _safe_div(marketcap - lo, lo)
    vel = dev.diff(5)
    return vel.diff(5)


def mcd_drv3_065_mc_log_spread_252d_peak_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log distance to 252-day peak) — acceleration of log spread worsening."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    spd = _log_safe(pk) - _log_safe(marketcap)
    vel = spd.diff(5)
    return vel.diff(5)


def mcd_drv3_066_mc_loss_vol_ratio_63_252_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63d/252d vol ratio) — curvature of vol regime shift."""
    chg  = marketcap.pct_change(1)
    v63  = _rolling_std(chg, _TD_QTR)
    v252 = _rolling_std(chg, _TD_YEAR)
    rat  = _safe_div(v63, v252)
    vel  = rat.diff(5)
    return vel.diff(5)


def mcd_drv3_067_mc_rolling_sharpe_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day rolling Sharpe) — acceleration of Sharpe deterioration."""
    chg   = marketcap.pct_change(1)
    mu    = _rolling_mean(chg, _TD_YEAR)
    sigma = _rolling_std(chg, _TD_YEAR)
    shrp  = _safe_div(mu, sigma)
    vel   = shrp.diff(5)
    return vel.diff(5)


def mcd_drv3_068_mc_dd_252d_21d_slope_63d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 63d of (OLS slope over 21d of 252-day mc dd) — quarterly curvature of deterioration."""
    pk     = _rolling_max(marketcap, _TD_YEAR)
    dd     = _safe_div(marketcap - pk, pk)
    slope1 = _linslope(dd, _TD_MON)
    return _linslope(slope1, _TD_QTR)


def mcd_drv3_069_mc_dd_ath_63d_slope_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21d of (OLS slope over 63d of ATH mc dd) — short curvature of quarterly ATH trend."""
    pk     = marketcap.expanding(min_periods=1).max()
    dd     = _safe_div(marketcap - pk, pk)
    slope1 = _linslope(dd, _TD_QTR)
    return _linslope(slope1, _TD_MON)


def mcd_drv3_070_mc_dd_252d_63d_slope_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21d of (OLS slope over 63d of 252-day mc dd) — short curvature of quarterly trend."""
    pk     = _rolling_max(marketcap, _TD_YEAR)
    dd     = _safe_div(marketcap - pk, pk)
    slope1 = _linslope(dd, _TD_QTR)
    return _linslope(slope1, _TD_MON)


def mcd_drv3_071_mc_down_frac_21d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day down-day fraction) — acceleration of short-window distress growth."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_MON)
    vel  = frac.diff(5)
    return vel.diff(5)


def mcd_drv3_072_mc_dd_area_63d_5d_diff_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21d of (5-day diff of 63-day mc dd area) — trend of area accumulation velocity."""
    pk   = _rolling_max(marketcap, _TD_QTR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_QTR)
    vel  = area.diff(5)
    return _linslope(vel, _TD_MON)


def mcd_drv3_073_mc_log_dd_252d_21d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of log-space 252-day mc dd) — acceleration of log monthly velocity."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    logdd = _log_safe(marketcap) - _log_safe(pk)
    vel   = logdd.diff(_TD_MON)
    return vel.diff(5)


def mcd_drv3_074_mc_dd_vol_of_dd_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of std-dev of 252-day mc dd) — acceleration of long vol-of-dd."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(dd, _TD_YEAR)
    vel = vol.diff(5)
    return vel.diff(5)


def mcd_drv3_075_mc_dd_252d_21d_diff_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of (21-day diff of 252-day mc dd) — monthly acceleration of monthly velocity."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vel = dd.diff(_TD_MON)
    return vel.diff(_TD_MON)


# ── Registry ───────────────────────────────────────────────────────────────────

MARKETCAP_DESTRUCTION_REGISTRY_3RD_DERIVATIVES = {
    "mcd_drv3_001_mc_dd_252d_5d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_001_mc_dd_252d_5d_diff_5d_diff},
    "mcd_drv3_002_mc_dd_ath_5d_diff_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv3_002_mc_dd_ath_5d_diff_5d_diff},
    "mcd_drv3_003_mc_dd_63d_5d_diff_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv3_003_mc_dd_63d_5d_diff_5d_diff},
    "mcd_drv3_004_mc_log_dd_252d_5d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_004_mc_log_dd_252d_5d_diff_5d_diff},
    "mcd_drv3_005_mc_log_dd_ath_21d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_005_mc_log_dd_ath_21d_diff_5d_diff},
    "mcd_drv3_006_mc_dd_vol_adj_5d_diff_5d_diff":        {"inputs": ["marketcap"], "func": mcd_drv3_006_mc_dd_vol_adj_5d_diff_5d_diff},
    "mcd_drv3_007_mc_underwater_frac_5d_diff_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv3_007_mc_underwater_frac_5d_diff_5d_diff},
    "mcd_drv3_008_mc_avg_dd_252d_5d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_008_mc_avg_dd_252d_5d_diff_5d_diff},
    "mcd_drv3_009_mc_dd_zscore_5d_diff_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_009_mc_dd_zscore_5d_diff_5d_diff},
    "mcd_drv3_010_mc_252d_pct_change_21d_diff_5d_diff":  {"inputs": ["marketcap"], "func": mcd_drv3_010_mc_252d_pct_change_21d_diff_5d_diff},
    "mcd_drv3_011_mc_21d_pct_change_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_011_mc_21d_pct_change_5d_diff_5d_diff},
    "mcd_drv3_012_mc_dd_252d_21d_slope_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_012_mc_dd_252d_21d_slope_5d_diff},
    "mcd_drv3_013_mc_dd_ath_63d_slope_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_013_mc_dd_ath_63d_slope_5d_diff},
    "mcd_drv3_014_mc_daily_vol_63d_5d_diff_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv3_014_mc_daily_vol_63d_5d_diff_5d_diff},
    "mcd_drv3_015_mc_down_frac_63d_5d_diff_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv3_015_mc_down_frac_63d_5d_diff_5d_diff},
    "mcd_drv3_016_mc_vs_sma252_5d_diff_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_016_mc_vs_sma252_5d_diff_5d_diff},
    "mcd_drv3_017_mc_dd_pct_rank_5d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_017_mc_dd_pct_rank_5d_diff_5d_diff},
    "mcd_drv3_018_mc_dd_area_63d_5d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_018_mc_dd_area_63d_5d_diff_5d_diff},
    "mcd_drv3_019_ev_dd_252d_5d_diff_5d_diff":           {"inputs": ["ev"],        "func": mcd_drv3_019_ev_dd_252d_5d_diff_5d_diff},
    "mcd_drv3_020_mc_dd_252d_63d_slope_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_020_mc_dd_252d_63d_slope_5d_diff},
    "mcd_drv3_021_mc_worst_21d_drop_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_021_mc_worst_21d_drop_252d_5d_diff_5d_diff},
    "mcd_drv3_022_mc_log_level_vs_252d_avg_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_022_mc_log_level_vs_252d_avg_5d_diff_5d_diff},
    "mcd_drv3_023_mc_dd_convexity_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_023_mc_dd_convexity_252d_5d_diff_5d_diff},
    "mcd_drv3_024_mc_ev_combined_dd_5d_diff_5d_diff":    {"inputs": ["marketcap", "ev"], "func": mcd_drv3_024_mc_ev_combined_dd_5d_diff_5d_diff},
    "mcd_drv3_025_mc_dd_252d_21d_slope_21d_slope":       {"inputs": ["marketcap"], "func": mcd_drv3_025_mc_dd_252d_21d_slope_21d_slope},
    "mcd_drv3_026_mc_dd_252d_21d_diff_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_026_mc_dd_252d_21d_diff_5d_diff},
    "mcd_drv3_027_mc_dd_ath_21d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_027_mc_dd_ath_21d_diff_5d_diff},
    "mcd_drv3_028_mc_dd_63d_21d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_028_mc_dd_63d_21d_diff_5d_diff},
    "mcd_drv3_029_mc_dd_252d_63d_diff_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_029_mc_dd_252d_63d_diff_5d_diff},
    "mcd_drv3_030_mc_dd_ath_63d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_030_mc_dd_ath_63d_diff_5d_diff},
    "mcd_drv3_031_mc_63d_pct_change_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_031_mc_63d_pct_change_5d_diff_5d_diff},
    "mcd_drv3_032_mc_126d_pct_change_5d_diff_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv3_032_mc_126d_pct_change_5d_diff_5d_diff},
    "mcd_drv3_033_mc_dd_126d_5d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_033_mc_dd_126d_5d_diff_5d_diff},
    "mcd_drv3_034_mc_dd_504d_5d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_034_mc_dd_504d_5d_diff_5d_diff},
    "mcd_drv3_035_mc_down_frac_252d_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_035_mc_down_frac_252d_5d_diff_5d_diff},
    "mcd_drv3_036_mc_underwater_frac_63d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_036_mc_underwater_frac_63d_5d_diff_5d_diff},
    "mcd_drv3_037_mc_avg_dd_63d_5d_diff_5d_diff":        {"inputs": ["marketcap"], "func": mcd_drv3_037_mc_avg_dd_63d_5d_diff_5d_diff},
    "mcd_drv3_038_mc_daily_vol_252d_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_038_mc_daily_vol_252d_5d_diff_5d_diff},
    "mcd_drv3_039_mc_vs_sma63_5d_diff_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_039_mc_vs_sma63_5d_diff_5d_diff},
    "mcd_drv3_040_mc_vs_ema21_5d_diff_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_040_mc_vs_ema21_5d_diff_5d_diff},
    "mcd_drv3_041_mc_vs_ema63_5d_diff_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_041_mc_vs_ema63_5d_diff_5d_diff},
    "mcd_drv3_042_mc_dd_area_252d_5d_diff_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv3_042_mc_dd_area_252d_5d_diff_5d_diff},
    "mcd_drv3_043_mc_dd_252d_126d_slope_5d_diff":        {"inputs": ["marketcap"], "func": mcd_drv3_043_mc_dd_252d_126d_slope_5d_diff},
    "mcd_drv3_044_mc_dd_ath_21d_slope_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv3_044_mc_dd_ath_21d_slope_5d_diff},
    "mcd_drv3_045_mc_dd_126d_21d_slope_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_045_mc_dd_126d_21d_slope_5d_diff},
    "mcd_drv3_046_mc_zscore_252d_5d_diff_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv3_046_mc_zscore_252d_5d_diff_5d_diff},
    "mcd_drv3_047_mc_pct_rank_252d_5d_diff_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv3_047_mc_pct_rank_252d_5d_diff_5d_diff},
    "mcd_drv3_048_mc_worst_5d_drop_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_048_mc_worst_5d_drop_252d_5d_diff_5d_diff},
    "mcd_drv3_049_mc_sum_neg_1d_63d_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_049_mc_sum_neg_1d_63d_5d_diff_5d_diff},
    "mcd_drv3_050_mc_dd_vol_of_dd_63d_5d_diff_5d_diff":  {"inputs": ["marketcap"], "func": mcd_drv3_050_mc_dd_vol_of_dd_63d_5d_diff_5d_diff},
    "mcd_drv3_051_ev_dd_252d_21d_diff_5d_diff":          {"inputs": ["ev"],        "func": mcd_drv3_051_ev_dd_252d_21d_diff_5d_diff},
    "mcd_drv3_052_ev_dd_252d_63d_slope_5d_diff":         {"inputs": ["ev"],        "func": mcd_drv3_052_ev_dd_252d_63d_slope_5d_diff},
    "mcd_drv3_053_ev_vs_sma252_5d_diff_5d_diff":         {"inputs": ["ev"],        "func": mcd_drv3_053_ev_vs_sma252_5d_diff_5d_diff},
    "mcd_drv3_054_mc_dd_zscore_504d_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_054_mc_dd_zscore_504d_5d_diff_5d_diff},
    "mcd_drv3_055_mc_ewm_dd_peak_21d_5d_diff_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv3_055_mc_ewm_dd_peak_21d_5d_diff_5d_diff},
    "mcd_drv3_056_mc_dd_intensity_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_056_mc_dd_intensity_252d_5d_diff_5d_diff},
    "mcd_drv3_057_mc_sma21_vs_sma63_5d_diff_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv3_057_mc_sma21_vs_sma63_5d_diff_5d_diff},
    "mcd_drv3_058_mc_sma63_vs_sma252_5d_diff_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv3_058_mc_sma63_vs_sma252_5d_diff_5d_diff},
    "mcd_drv3_059_mc_dd_ratio_63d_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_059_mc_dd_ratio_63d_252d_5d_diff_5d_diff},
    "mcd_drv3_060_mc_dd_composite_weighted_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_060_mc_dd_composite_weighted_5d_diff_5d_diff},
    "mcd_drv3_061_mc_ev_ratio_5d_diff_5d_diff":          {"inputs": ["marketcap", "ev"], "func": mcd_drv3_061_mc_ev_ratio_5d_diff_5d_diff},
    "mcd_drv3_062_mc_ev_combined_dd_21d_diff_5d_diff":   {"inputs": ["marketcap", "ev"], "func": mcd_drv3_062_mc_ev_combined_dd_21d_diff_5d_diff},
    "mcd_drv3_063_mc_dd_252d_1d_diff_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv3_063_mc_dd_252d_1d_diff_5d_diff},
    "mcd_drv3_064_mc_pct_above_252d_low_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_064_mc_pct_above_252d_low_5d_diff_5d_diff},
    "mcd_drv3_065_mc_log_spread_252d_peak_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_065_mc_log_spread_252d_peak_5d_diff_5d_diff},
    "mcd_drv3_066_mc_loss_vol_ratio_63_252_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_066_mc_loss_vol_ratio_63_252_5d_diff_5d_diff},
    "mcd_drv3_067_mc_rolling_sharpe_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_067_mc_rolling_sharpe_252d_5d_diff_5d_diff},
    "mcd_drv3_068_mc_dd_252d_21d_slope_63d_slope":       {"inputs": ["marketcap"], "func": mcd_drv3_068_mc_dd_252d_21d_slope_63d_slope},
    "mcd_drv3_069_mc_dd_ath_63d_slope_21d_slope":        {"inputs": ["marketcap"], "func": mcd_drv3_069_mc_dd_ath_63d_slope_21d_slope},
    "mcd_drv3_070_mc_dd_252d_63d_slope_21d_slope":       {"inputs": ["marketcap"], "func": mcd_drv3_070_mc_dd_252d_63d_slope_21d_slope},
    "mcd_drv3_071_mc_down_frac_21d_5d_diff_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv3_071_mc_down_frac_21d_5d_diff_5d_diff},
    "mcd_drv3_072_mc_dd_area_63d_5d_diff_21d_slope":     {"inputs": ["marketcap"], "func": mcd_drv3_072_mc_dd_area_63d_5d_diff_21d_slope},
    "mcd_drv3_073_mc_log_dd_252d_21d_diff_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv3_073_mc_log_dd_252d_21d_diff_5d_diff},
    "mcd_drv3_074_mc_dd_vol_of_dd_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv3_074_mc_dd_vol_of_dd_252d_5d_diff_5d_diff},
    "mcd_drv3_075_mc_dd_252d_21d_diff_21d_diff":         {"inputs": ["marketcap"], "func": mcd_drv3_075_mc_dd_252d_21d_diff_21d_diff},
}
