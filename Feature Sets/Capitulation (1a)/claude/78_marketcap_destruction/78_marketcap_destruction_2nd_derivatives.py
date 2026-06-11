"""
78_marketcap_destruction — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base market-cap destruction features — velocity of destruction
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
  NO raw price/volume or quarterly SF1 fundamental inputs.
Each feature computes a .diff(n), slope, or pct-change of a base-feature concept.
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


# ── 2nd-Derivative Feature Functions ──────────────────────────────────────────

def mcd_drv2_001_mc_dd_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day first difference of 252-day mc drawdown (velocity of deterioration)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(5)


def mcd_drv2_002_mc_dd_ath_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day first difference of ATH mc drawdown (velocity of ATH distress)."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(5)


def mcd_drv2_003_mc_dd_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day first difference of 63-day mc drawdown."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(5)


def mcd_drv2_004_mc_log_dd_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of log-space 252-day mc drawdown (log-velocity of decline)."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    logdd = _log_safe(marketcap) - _log_safe(pk)
    return logdd.diff(5)


def mcd_drv2_005_mc_log_dd_ath_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of log ATH mc drawdown (monthly worsening in log-distance from peak)."""
    pk    = marketcap.expanding(min_periods=1).max()
    logdd = _log_safe(marketcap) - _log_safe(pk)
    return logdd.diff(_TD_MON)


def mcd_drv2_006_mc_dd_vol_adj_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of volatility-adjusted 252-day mc drawdown."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(marketcap.pct_change(1), _TD_YEAR)
    ddv = _safe_div(dd, vol)
    return ddv.diff(5)


def mcd_drv2_007_mc_underwater_frac_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc underwater fraction (pace of increasing distress days)."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    dd    = _safe_div(marketcap - pk, pk)
    below = (dd < 0).astype(float)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5)


def mcd_drv2_008_mc_avg_dd_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of rolling-mean 252-day mc drawdown (pace of worsening average)."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    avg = _rolling_mean(dd, _TD_YEAR)
    return avg.diff(5)


def mcd_drv2_009_mc_dd_area_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day mc drawdown area (acceleration of area accumulation)."""
    pk   = _rolling_max(marketcap, _TD_QTR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_QTR)
    return area.diff(5)


def mcd_drv2_010_mc_dd_zscore_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc drawdown z-score (acceleration of statistical extremity)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    z  = _zscore_rolling(dd, _TD_YEAR)
    return z.diff(5)


def mcd_drv2_011_mc_252d_pct_change_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day mc pct-change (acceleration of annual destruction rate)."""
    chg252 = marketcap.pct_change(_TD_YEAR)
    return chg252.diff(_TD_MON)


def mcd_drv2_012_mc_21d_pct_change_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day mc pct-change (weekly acceleration of monthly decay)."""
    chg21 = marketcap.pct_change(_TD_MON)
    return chg21.diff(5)


def mcd_drv2_013_mc_dd_252d_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of 252-day mc drawdown over trailing 21 days (short-term trend)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_MON)


def mcd_drv2_014_mc_dd_ath_63d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of ATH mc drawdown over trailing 63 days."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_QTR)


def mcd_drv2_015_mc_log_dd_ath_5d_pct_change(marketcap: pd.Series) -> pd.Series:
    """5-day pct change in ATH log-mc-drawdown magnitude (relative worsening rate)."""
    pk    = marketcap.expanding(min_periods=1).max()
    logdd = (_log_safe(pk) - _log_safe(marketcap)).clip(lower=_EPS)
    return _safe_div(logdd - logdd.shift(5), logdd.shift(5).abs())


def mcd_drv2_016_mc_dd_convexity_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc drawdown convexity (avg-dd / max-dd ratio evolution)."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    avg  = _rolling_mean(dd, _TD_YEAR)
    mxdd = _rolling_min(dd, _TD_YEAR)
    cvx  = _safe_div(avg, mxdd)
    return cvx.diff(5)


def mcd_drv2_017_ev_dd_252d_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day first difference of 252-day EV drawdown (velocity of EV destruction)."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return dd.diff(5)


def mcd_drv2_018_mc_daily_vol_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day annualized mc vol (acceleration of volatility expansion)."""
    chg = marketcap.pct_change(1)
    vol = _rolling_std(chg, _TD_QTR) * np.sqrt(_TD_YEAR)
    return vol.diff(5)


def mcd_drv2_019_mc_down_frac_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day mc down-day fraction (pace of increasing down-days)."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_QTR)
    return frac.diff(5)


def mcd_drv2_020_mc_vs_sma252_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of mc deviation from 252-day SMA (speed of SMA compression)."""
    ma  = _rolling_mean(marketcap, _TD_YEAR)
    dev = _safe_div(marketcap - ma, ma)
    return dev.diff(5)


def mcd_drv2_021_mc_dd_pct_rank_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of 252-day mc drawdown."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    rank = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(5)


def mcd_drv2_022_mc_worst_21d_drop_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of worst-21d-drop within 252d rolling window."""
    chg   = marketcap.pct_change(_TD_MON)
    worst = chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return worst.diff(5)


def mcd_drv2_023_mc_log_level_vs_252d_avg_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of log-mc minus log-252d-avg (acceleration of compression from mean)."""
    dev = _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, _TD_YEAR))
    return dev.diff(5)


def mcd_drv2_024_mc_ev_combined_dd_5d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """5-day diff of average 252-day mc+EV drawdown (combined destruction velocity)."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    combo = (dd_mc + dd_ev) / 2.0
    return combo.diff(5)


def mcd_drv2_025_mc_dd_252d_63d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of 252-day mc drawdown over trailing 63 days (quarterly trend)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_QTR)


# --- 2nd Derivative Extensions (drv2_026 - drv2_075) ---

def mcd_drv2_026_mc_dd_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day mc drawdown (monthly velocity of deterioration)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_MON)


def mcd_drv2_027_mc_dd_ath_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of ATH mc drawdown (monthly velocity of ATH distress)."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_MON)


def mcd_drv2_028_mc_dd_63d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 63-day mc drawdown (monthly velocity of quarterly drawdown)."""
    pk = _rolling_max(marketcap, _TD_QTR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_MON)


def mcd_drv2_029_mc_log_dd_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of log-space 252-day mc drawdown."""
    pk    = _rolling_max(marketcap, _TD_YEAR)
    logdd = _log_safe(marketcap) - _log_safe(pk)
    return logdd.diff(_TD_MON)


def mcd_drv2_030_mc_dd_252d_63d_diff(marketcap: pd.Series) -> pd.Series:
    """63-day diff of 252-day mc drawdown (quarterly velocity of annual drawdown)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_QTR)


def mcd_drv2_031_mc_dd_ath_63d_diff(marketcap: pd.Series) -> pd.Series:
    """63-day diff of ATH mc drawdown (quarterly velocity of ATH distress)."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_QTR)


def mcd_drv2_032_mc_63d_pct_change_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day mc pct-change (weekly acceleration of quarterly decay)."""
    chg63 = marketcap.pct_change(_TD_QTR)
    return chg63.diff(5)


def mcd_drv2_033_mc_126d_pct_change_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 126-day mc pct-change (weekly acceleration of half-year decay)."""
    chg126 = marketcap.pct_change(_TD_HALF)
    return chg126.diff(5)


def mcd_drv2_034_mc_126d_pct_change_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 126-day mc pct-change (monthly acceleration of half-year decay)."""
    chg126 = marketcap.pct_change(_TD_HALF)
    return chg126.diff(_TD_MON)


def mcd_drv2_035_mc_dd_126d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 126-day mc drawdown (weekly velocity of half-year drawdown)."""
    pk = _rolling_max(marketcap, _TD_HALF)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(5)


def mcd_drv2_036_mc_dd_504d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 504-day mc drawdown."""
    pk = _rolling_max(marketcap, 504)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(5)


def mcd_drv2_037_mc_dd_504d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 504-day mc drawdown (monthly velocity of 2-year drawdown)."""
    pk = _rolling_max(marketcap, 504)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(_TD_MON)


def mcd_drv2_038_mc_down_frac_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc down-day fraction."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_YEAR)
    return frac.diff(5)


def mcd_drv2_039_mc_underwater_frac_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day mc underwater fraction."""
    pk    = _rolling_max(marketcap, _TD_QTR)
    below = (marketcap < pk).astype(float)
    frac  = _rolling_mean(below, _TD_QTR)
    return frac.diff(5)


def mcd_drv2_040_mc_avg_dd_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of rolling-mean 63-day mc drawdown."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    avg = _rolling_mean(dd, _TD_QTR)
    return avg.diff(5)


def mcd_drv2_041_mc_daily_vol_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day annualized mc vol (acceleration of long-term volatility)."""
    chg = marketcap.pct_change(1)
    vol = _rolling_std(chg, _TD_YEAR) * np.sqrt(_TD_YEAR)
    return vol.diff(5)


def mcd_drv2_042_mc_vs_sma63_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of mc deviation from 63-day SMA."""
    ma  = _rolling_mean(marketcap, _TD_QTR)
    dev = _safe_div(marketcap - ma, ma)
    return dev.diff(5)


def mcd_drv2_043_mc_vs_sma21_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of mc deviation from 21-day SMA (short-term SMA compression speed)."""
    ma  = _rolling_mean(marketcap, _TD_MON)
    dev = _safe_div(marketcap - ma, ma)
    return dev.diff(5)


def mcd_drv2_044_mc_vs_ema21_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of mc deviation from 21-day EMA."""
    ma  = _ewm_mean(marketcap, _TD_MON)
    dev = _safe_div(marketcap - ma, ma)
    return dev.diff(5)


def mcd_drv2_045_mc_vs_ema63_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of mc deviation from 63-day EMA."""
    ma  = _ewm_mean(marketcap, _TD_QTR)
    dev = _safe_div(marketcap - ma, ma)
    return dev.diff(5)


def mcd_drv2_046_mc_dd_area_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc drawdown area (sum of dd over 252d)."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    area = _rolling_sum(dd, _TD_YEAR)
    return area.diff(5)


def mcd_drv2_047_mc_dd_252d_126d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of 252-day mc drawdown over trailing 126 days (half-year trend)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_HALF)


def mcd_drv2_048_mc_dd_ath_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of ATH mc drawdown over trailing 21 days (short-term ATH trend)."""
    pk = marketcap.expanding(min_periods=1).max()
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_MON)


def mcd_drv2_049_mc_dd_126d_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope of 126-day mc drawdown over trailing 21 days."""
    pk = _rolling_max(marketcap, _TD_HALF)
    dd = _safe_div(marketcap - pk, pk)
    return _linslope(dd, _TD_MON)


def mcd_drv2_050_mc_zscore_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc z-score (velocity of z-score deterioration)."""
    z = _zscore_rolling(marketcap, _TD_YEAR)
    return z.diff(5)


def mcd_drv2_051_mc_pct_rank_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day mc percentile rank."""
    rank = marketcap.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_MON)


def mcd_drv2_052_mc_worst_5d_drop_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of worst-5d-drop within 252d rolling window."""
    chg   = marketcap.pct_change(5)
    worst = chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return worst.diff(5)


def mcd_drv2_053_mc_worst_1d_drop_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of worst-1d-drop within 252d window."""
    chg   = marketcap.pct_change(1)
    worst = chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return worst.diff(5)


def mcd_drv2_054_mc_sum_neg_1d_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of sum of negative daily mc changes over 63-day window."""
    chg  = marketcap.pct_change(1)
    neg  = chg.where(chg < 0, other=0.0)
    ssum = _rolling_sum(neg, _TD_QTR)
    return ssum.diff(5)


def mcd_drv2_055_mc_dd_vol_of_dd_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of std dev of 63-day mc drawdown (volatility of drawdown changes)."""
    pk  = _rolling_max(marketcap, _TD_QTR)
    dd  = _safe_div(marketcap - pk, pk)
    vol = _rolling_std(dd, _TD_QTR)
    return vol.diff(5)


def mcd_drv2_056_ev_dd_252d_21d_diff(ev: pd.Series) -> pd.Series:
    """21-day diff of 252-day EV drawdown (monthly EV destruction velocity)."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return dd.diff(_TD_MON)


def mcd_drv2_057_ev_dd_252d_63d_slope(ev: pd.Series) -> pd.Series:
    """OLS slope of 252-day EV drawdown over trailing 63 days."""
    pk = _rolling_max(ev, _TD_YEAR)
    dd = _safe_div(ev - pk, pk)
    return _linslope(dd, _TD_QTR)


def mcd_drv2_058_ev_vs_sma252_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of EV deviation from 252-day SMA."""
    ma  = _rolling_mean(ev, _TD_YEAR)
    dev = _safe_div(ev - ma, ma)
    return dev.diff(5)


def mcd_drv2_059_mc_dd_zscore_504d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 504-day mc drawdown z-score."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    z  = _zscore_rolling(dd, 504)
    return z.diff(5)


def mcd_drv2_060_mc_ewm_dd_peak_21d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of EWM-smoothed (21d) drawdown from 252-day peak."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    dd  = _safe_div(marketcap - pk, pk)
    edd = _ewm_mean(dd, _TD_MON)
    return edd.diff(5)


def mcd_drv2_061_mc_dd_pct_rank_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of percentile rank of 252-day mc drawdown."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    rank = dd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_MON)


def mcd_drv2_062_mc_sma21_vs_sma63_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (21-day SMA minus 63-day SMA) / 63-day SMA."""
    s21 = _rolling_mean(marketcap, _TD_MON)
    s63 = _rolling_mean(marketcap, _TD_QTR)
    dev = _safe_div(s21 - s63, s63)
    return dev.diff(5)


def mcd_drv2_063_mc_sma63_vs_sma252_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (63-day SMA minus 252-day SMA) / 252-day SMA."""
    s63  = _rolling_mean(marketcap, _TD_QTR)
    s252 = _rolling_mean(marketcap, _TD_YEAR)
    dev  = _safe_div(s63 - s252, s252)
    return dev.diff(5)


def mcd_drv2_064_mc_log_level_vs_504d_avg_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of log-mc minus log-504d-avg."""
    dev = _log_safe(marketcap) - _log_safe(_rolling_mean(marketcap, 504))
    return dev.diff(5)


def mcd_drv2_065_mc_down_frac_21d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day mc down-day fraction."""
    down = (marketcap.diff(1) < 0).astype(float)
    frac = _rolling_mean(down, _TD_MON)
    return frac.diff(5)


def mcd_drv2_066_mc_dd_intensity_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mc drawdown intensity (current dd / max-dd ratio)."""
    pk   = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - pk, pk)
    mxdd = _rolling_min(dd, _TD_YEAR)
    intn = _safe_div(dd, mxdd)
    return intn.diff(5)


def mcd_drv2_067_mc_dd_ratio_63d_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of ratio of 63-day mc dd to 252-day mc dd."""
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    ratio = _safe_div(dd63, dd252)
    return ratio.diff(5)


def mcd_drv2_068_mc_dd_composite_weighted_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of composite mc drawdown (50% 21d + 30% 63d + 20% 252d)."""
    pk21  = _rolling_max(marketcap, _TD_MON)
    pk63  = _rolling_max(marketcap, _TD_QTR)
    pk252 = _rolling_max(marketcap, _TD_YEAR)
    dd21  = _safe_div(marketcap - pk21,  pk21)
    dd63  = _safe_div(marketcap - pk63,  pk63)
    dd252 = _safe_div(marketcap - pk252, pk252)
    combo = 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252
    return combo.diff(5)


def mcd_drv2_069_mc_ev_ratio_5d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """5-day diff of MC/EV ratio (speed of leverage-adjusted cap fraction change)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(5)


def mcd_drv2_070_mc_ev_combined_dd_21d_diff(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """21-day diff of average 252-day mc+EV drawdown."""
    pk_mc = _rolling_max(marketcap, _TD_YEAR)
    pk_ev = _rolling_max(ev, _TD_YEAR)
    dd_mc = _safe_div(marketcap - pk_mc, pk_mc)
    dd_ev = _safe_div(ev - pk_ev, pk_ev)
    combo = (dd_mc + dd_ev) / 2.0
    return combo.diff(_TD_MON)


def mcd_drv2_071_mc_dd_252d_1d_diff(marketcap: pd.Series) -> pd.Series:
    """1-day first difference of 252-day mc drawdown (daily velocity of deterioration)."""
    pk = _rolling_max(marketcap, _TD_YEAR)
    dd = _safe_div(marketcap - pk, pk)
    return dd.diff(1)


def mcd_drv2_072_mc_pct_above_252d_low_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of pct-above-252d-low (speed of approach toward trough)."""
    lo  = _rolling_min(marketcap, _TD_YEAR)
    dev = _safe_div(marketcap - lo, lo)
    return dev.diff(5)


def mcd_drv2_073_mc_log_spread_252d_peak_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of log distance from current mc to 252-day peak."""
    pk  = _rolling_max(marketcap, _TD_YEAR)
    spd = _log_safe(pk) - _log_safe(marketcap)
    return spd.diff(5)


def mcd_drv2_074_mc_loss_vol_ratio_63_252_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of ratio of 63-day to 252-day mc annualized vol."""
    chg  = marketcap.pct_change(1)
    v63  = _rolling_std(chg, _TD_QTR)
    v252 = _rolling_std(chg, _TD_YEAR)
    rat  = _safe_div(v63, v252)
    return rat.diff(5)


def mcd_drv2_075_mc_rolling_sharpe_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling Sharpe of daily mc pct changes."""
    chg   = marketcap.pct_change(1)
    mu    = _rolling_mean(chg, _TD_YEAR)
    sigma = _rolling_std(chg, _TD_YEAR)
    shrp  = _safe_div(mu, sigma)
    return shrp.diff(5)


# ── Registry ───────────────────────────────────────────────────────────────────

MARKETCAP_DESTRUCTION_REGISTRY_2ND_DERIVATIVES = {
    "mcd_drv2_001_mc_dd_252d_5d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_001_mc_dd_252d_5d_diff},
    "mcd_drv2_002_mc_dd_ath_5d_diff":              {"inputs": ["marketcap"], "func": mcd_drv2_002_mc_dd_ath_5d_diff},
    "mcd_drv2_003_mc_dd_63d_5d_diff":              {"inputs": ["marketcap"], "func": mcd_drv2_003_mc_dd_63d_5d_diff},
    "mcd_drv2_004_mc_log_dd_252d_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv2_004_mc_log_dd_252d_5d_diff},
    "mcd_drv2_005_mc_log_dd_ath_21d_diff":         {"inputs": ["marketcap"], "func": mcd_drv2_005_mc_log_dd_ath_21d_diff},
    "mcd_drv2_006_mc_dd_vol_adj_252d_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv2_006_mc_dd_vol_adj_252d_5d_diff},
    "mcd_drv2_007_mc_underwater_frac_252d_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_007_mc_underwater_frac_252d_5d_diff},
    "mcd_drv2_008_mc_avg_dd_252d_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv2_008_mc_avg_dd_252d_5d_diff},
    "mcd_drv2_009_mc_dd_area_63d_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv2_009_mc_dd_area_63d_5d_diff},
    "mcd_drv2_010_mc_dd_zscore_252d_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_010_mc_dd_zscore_252d_5d_diff},
    "mcd_drv2_011_mc_252d_pct_change_21d_diff":    {"inputs": ["marketcap"], "func": mcd_drv2_011_mc_252d_pct_change_21d_diff},
    "mcd_drv2_012_mc_21d_pct_change_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_012_mc_21d_pct_change_5d_diff},
    "mcd_drv2_013_mc_dd_252d_21d_slope":           {"inputs": ["marketcap"], "func": mcd_drv2_013_mc_dd_252d_21d_slope},
    "mcd_drv2_014_mc_dd_ath_63d_slope":            {"inputs": ["marketcap"], "func": mcd_drv2_014_mc_dd_ath_63d_slope},
    "mcd_drv2_015_mc_log_dd_ath_5d_pct_change":    {"inputs": ["marketcap"], "func": mcd_drv2_015_mc_log_dd_ath_5d_pct_change},
    "mcd_drv2_016_mc_dd_convexity_252d_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv2_016_mc_dd_convexity_252d_5d_diff},
    "mcd_drv2_017_ev_dd_252d_5d_diff":             {"inputs": ["ev"],        "func": mcd_drv2_017_ev_dd_252d_5d_diff},
    "mcd_drv2_018_mc_daily_vol_63d_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv2_018_mc_daily_vol_63d_5d_diff},
    "mcd_drv2_019_mc_down_frac_63d_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv2_019_mc_down_frac_63d_5d_diff},
    "mcd_drv2_020_mc_vs_sma252_5d_diff":           {"inputs": ["marketcap"], "func": mcd_drv2_020_mc_vs_sma252_5d_diff},
    "mcd_drv2_021_mc_dd_pct_rank_252d_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv2_021_mc_dd_pct_rank_252d_5d_diff},
    "mcd_drv2_022_mc_worst_21d_drop_252d_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_022_mc_worst_21d_drop_252d_5d_diff},
    "mcd_drv2_023_mc_log_level_vs_252d_avg_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_023_mc_log_level_vs_252d_avg_5d_diff},
    "mcd_drv2_024_mc_ev_combined_dd_5d_diff":      {"inputs": ["marketcap", "ev"], "func": mcd_drv2_024_mc_ev_combined_dd_5d_diff},
    "mcd_drv2_025_mc_dd_252d_63d_slope":           {"inputs": ["marketcap"], "func": mcd_drv2_025_mc_dd_252d_63d_slope},
    "mcd_drv2_026_mc_dd_252d_21d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_026_mc_dd_252d_21d_diff},
    "mcd_drv2_027_mc_dd_ath_21d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_027_mc_dd_ath_21d_diff},
    "mcd_drv2_028_mc_dd_63d_21d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_028_mc_dd_63d_21d_diff},
    "mcd_drv2_029_mc_log_dd_252d_21d_diff":        {"inputs": ["marketcap"], "func": mcd_drv2_029_mc_log_dd_252d_21d_diff},
    "mcd_drv2_030_mc_dd_252d_63d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_030_mc_dd_252d_63d_diff},
    "mcd_drv2_031_mc_dd_ath_63d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_031_mc_dd_ath_63d_diff},
    "mcd_drv2_032_mc_63d_pct_change_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_032_mc_63d_pct_change_5d_diff},
    "mcd_drv2_033_mc_126d_pct_change_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv2_033_mc_126d_pct_change_5d_diff},
    "mcd_drv2_034_mc_126d_pct_change_21d_diff":    {"inputs": ["marketcap"], "func": mcd_drv2_034_mc_126d_pct_change_21d_diff},
    "mcd_drv2_035_mc_dd_126d_5d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_035_mc_dd_126d_5d_diff},
    "mcd_drv2_036_mc_dd_504d_5d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_036_mc_dd_504d_5d_diff},
    "mcd_drv2_037_mc_dd_504d_21d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_037_mc_dd_504d_21d_diff},
    "mcd_drv2_038_mc_down_frac_252d_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_038_mc_down_frac_252d_5d_diff},
    "mcd_drv2_039_mc_underwater_frac_63d_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_039_mc_underwater_frac_63d_5d_diff},
    "mcd_drv2_040_mc_avg_dd_63d_5d_diff":          {"inputs": ["marketcap"], "func": mcd_drv2_040_mc_avg_dd_63d_5d_diff},
    "mcd_drv2_041_mc_daily_vol_252d_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_041_mc_daily_vol_252d_5d_diff},
    "mcd_drv2_042_mc_vs_sma63_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_042_mc_vs_sma63_5d_diff},
    "mcd_drv2_043_mc_vs_sma21_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_043_mc_vs_sma21_5d_diff},
    "mcd_drv2_044_mc_vs_ema21_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_044_mc_vs_ema21_5d_diff},
    "mcd_drv2_045_mc_vs_ema63_5d_diff":            {"inputs": ["marketcap"], "func": mcd_drv2_045_mc_vs_ema63_5d_diff},
    "mcd_drv2_046_mc_dd_area_252d_5d_diff":        {"inputs": ["marketcap"], "func": mcd_drv2_046_mc_dd_area_252d_5d_diff},
    "mcd_drv2_047_mc_dd_252d_126d_slope":          {"inputs": ["marketcap"], "func": mcd_drv2_047_mc_dd_252d_126d_slope},
    "mcd_drv2_048_mc_dd_ath_21d_slope":            {"inputs": ["marketcap"], "func": mcd_drv2_048_mc_dd_ath_21d_slope},
    "mcd_drv2_049_mc_dd_126d_21d_slope":           {"inputs": ["marketcap"], "func": mcd_drv2_049_mc_dd_126d_21d_slope},
    "mcd_drv2_050_mc_zscore_252d_5d_diff":         {"inputs": ["marketcap"], "func": mcd_drv2_050_mc_zscore_252d_5d_diff},
    "mcd_drv2_051_mc_pct_rank_252d_21d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_051_mc_pct_rank_252d_21d_diff},
    "mcd_drv2_052_mc_worst_5d_drop_252d_5d_diff":  {"inputs": ["marketcap"], "func": mcd_drv2_052_mc_worst_5d_drop_252d_5d_diff},
    "mcd_drv2_053_mc_worst_1d_drop_252d_5d_diff":  {"inputs": ["marketcap"], "func": mcd_drv2_053_mc_worst_1d_drop_252d_5d_diff},
    "mcd_drv2_054_mc_sum_neg_1d_63d_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_054_mc_sum_neg_1d_63d_5d_diff},
    "mcd_drv2_055_mc_dd_vol_of_dd_63d_5d_diff":    {"inputs": ["marketcap"], "func": mcd_drv2_055_mc_dd_vol_of_dd_63d_5d_diff},
    "mcd_drv2_056_ev_dd_252d_21d_diff":            {"inputs": ["ev"],        "func": mcd_drv2_056_ev_dd_252d_21d_diff},
    "mcd_drv2_057_ev_dd_252d_63d_slope":           {"inputs": ["ev"],        "func": mcd_drv2_057_ev_dd_252d_63d_slope},
    "mcd_drv2_058_ev_vs_sma252_5d_diff":           {"inputs": ["ev"],        "func": mcd_drv2_058_ev_vs_sma252_5d_diff},
    "mcd_drv2_059_mc_dd_zscore_504d_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_059_mc_dd_zscore_504d_5d_diff},
    "mcd_drv2_060_mc_ewm_dd_peak_21d_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv2_060_mc_ewm_dd_peak_21d_5d_diff},
    "mcd_drv2_061_mc_dd_pct_rank_252d_21d_diff":   {"inputs": ["marketcap"], "func": mcd_drv2_061_mc_dd_pct_rank_252d_21d_diff},
    "mcd_drv2_062_mc_sma21_vs_sma63_5d_diff":      {"inputs": ["marketcap"], "func": mcd_drv2_062_mc_sma21_vs_sma63_5d_diff},
    "mcd_drv2_063_mc_sma63_vs_sma252_5d_diff":     {"inputs": ["marketcap"], "func": mcd_drv2_063_mc_sma63_vs_sma252_5d_diff},
    "mcd_drv2_064_mc_log_level_vs_504d_avg_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_064_mc_log_level_vs_504d_avg_5d_diff},
    "mcd_drv2_065_mc_down_frac_21d_5d_diff":       {"inputs": ["marketcap"], "func": mcd_drv2_065_mc_down_frac_21d_5d_diff},
    "mcd_drv2_066_mc_dd_intensity_252d_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv2_066_mc_dd_intensity_252d_5d_diff},
    "mcd_drv2_067_mc_dd_ratio_63d_252d_5d_diff":   {"inputs": ["marketcap"], "func": mcd_drv2_067_mc_dd_ratio_63d_252d_5d_diff},
    "mcd_drv2_068_mc_dd_composite_weighted_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_068_mc_dd_composite_weighted_5d_diff},
    "mcd_drv2_069_mc_ev_ratio_5d_diff":            {"inputs": ["marketcap", "ev"], "func": mcd_drv2_069_mc_ev_ratio_5d_diff},
    "mcd_drv2_070_mc_ev_combined_dd_21d_diff":     {"inputs": ["marketcap", "ev"], "func": mcd_drv2_070_mc_ev_combined_dd_21d_diff},
    "mcd_drv2_071_mc_dd_252d_1d_diff":             {"inputs": ["marketcap"], "func": mcd_drv2_071_mc_dd_252d_1d_diff},
    "mcd_drv2_072_mc_pct_above_252d_low_5d_diff":  {"inputs": ["marketcap"], "func": mcd_drv2_072_mc_pct_above_252d_low_5d_diff},
    "mcd_drv2_073_mc_log_spread_252d_peak_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_073_mc_log_spread_252d_peak_5d_diff},
    "mcd_drv2_074_mc_loss_vol_ratio_63_252_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_074_mc_loss_vol_ratio_63_252_5d_diff},
    "mcd_drv2_075_mc_rolling_sharpe_252d_5d_diff": {"inputs": ["marketcap"], "func": mcd_drv2_075_mc_rolling_sharpe_252d_5d_diff},
}
