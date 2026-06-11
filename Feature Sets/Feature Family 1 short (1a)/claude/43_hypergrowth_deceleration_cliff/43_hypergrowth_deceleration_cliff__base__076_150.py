"""hypergrowth_deceleration_cliff base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py — covers growth-trajectory shape
(regression slopes / oscillation / inflection), quality-of-growth (revenue
vs AR/inventory/sgna/rnd/capex), quarterly-step cliff detectors, and
composite topping/blowoff scores. Inputs: SF1 ARQ columns. PIT-clean.
"""
import numpy as np
import pandas as pd

QDAYS = 63
YDAYS = 252
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_log_signed(s):
    return np.sign(s) * np.log1p(s.abs())


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


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


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


def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)


def _max_streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        best = cur = 0
        for v in w:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag_series.rolling(window, min_periods=min_periods).apply(_ms, raw=True)


def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f43_hdcl_076_revenue_growth_trajectory_slope_8q(revenue: pd.Series) -> pd.Series:
    """Regression slope of YoY growth over trailing 8q (2y) — short-horizon growth-rate trajectory."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_2Y)


def f43_hdcl_077_revenue_growth_trajectory_slope_20q(revenue: pd.Series) -> pd.Series:
    """Regression slope of YoY growth over trailing 20q (5y) — long-horizon growth-rate trajectory."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_5Y)


def f43_hdcl_078_revenue_growth_trajectory_curvature_8q(revenue: pd.Series) -> pd.Series:
    """8q slope of (8q slope of YoY) — curvature (acceleration) of trajectory."""
    yoy = _safe_log(revenue).diff(YDAYS)
    slope8 = _rolling_slope(yoy, DDAYS_2Y)
    return _rolling_slope(slope8, DDAYS_2Y)


def f43_hdcl_079_revenue_growth_jump_count_negative_8q(revenue: pd.Series) -> pd.Series:
    """Bars in last 8q where QoQ-of-QoQ < trailing-5y mean − 2σ — large negative growth jumps."""
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS)
    m = accel.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = accel.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    flag = (accel < (m - 2.0 * sd)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_080_revenue_growth_step_change_negative_indicator(revenue: pd.Series) -> pd.Series:
    """1 if today's QoQ-of-QoQ is below trailing-5y mean − 2σ — current-bar step-change-down event."""
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS)
    m = accel.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = accel.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    return ((accel < (m - 2.0 * sd))).astype(float).where(accel.notna() & sd.notna(), np.nan)


def f43_hdcl_081_revenue_growth_zscore_change_4q(revenue: pd.Series) -> pd.Series:
    """Δ in (YoY z-score vs 5y) over 252d — change of growth-rate z-position."""
    z = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return z.diff(YDAYS)


def f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q(revenue: pd.Series) -> pd.Series:
    """Second 252d diff of (YoY z-score) — acceleration of growth-rate z-position."""
    z = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return z.diff(YDAYS).diff(YDAYS)


def f43_hdcl_083_revenue_yoy_distribution_skewness_20q(revenue: pd.Series) -> pd.Series:
    """Skewness of YoY growth distribution over trailing 20q (5y) — directional asymmetry."""
    yoy = _safe_log(revenue).diff(YDAYS)
    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / (sd ** 3))
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_sk, raw=True)


def f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q(revenue: pd.Series) -> pd.Series:
    """Excess kurtosis of YoY growth over 20q — fat-tailed growth regime."""
    yoy = _safe_log(revenue).diff(YDAYS)
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_k, raw=True)


def f43_hdcl_085_revenue_yoy_distribution_minimum_20q(revenue: pd.Series) -> pd.Series:
    """Min YoY growth in trailing 20q — worst-5y reading."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).min()


def f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q(revenue: pd.Series) -> pd.Series:
    """IQR (p75 − p25) of YoY growth in 20q — interquartile spread of growth."""
    yoy = _safe_log(revenue).diff(YDAYS)
    p75 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    p25 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    return p75 - p25


def f43_hdcl_087_revenue_growth_persistence_above_zero_streak(revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where YoY > 0 — positive-growth run length."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_088_revenue_growth_persistence_below_zero_streak(revenue: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where YoY < 0 — negative-growth run length."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_089_revenue_growth_oscillation_count_8q(revenue: pd.Series) -> pd.Series:
    """Count of QoQ growth sign-flips over trailing 8q — choppiness of sequential growth."""
    qoq = _safe_log(revenue).diff(QDAYS)
    sg = np.sign(qoq.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return flip.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_090_revenue_growth_directional_consistency_8q(revenue: pd.Series) -> pd.Series:
    """|mean sign(QoQ)| over 8q — 1 = monotonic, 0 = oscillating."""
    qoq = _safe_log(revenue).diff(QDAYS)
    sg = np.sign(qoq)
    return sg.rolling(DDAYS_2Y, min_periods=YDAYS).mean().abs()


def f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q(revenue: pd.Series) -> pd.Series:
    """EMA(5q)/EMA(20q) of YoY growth − 1 — smoothed short-vs-long growth gap."""
    yoy = _safe_log(revenue).diff(YDAYS)
    e5q = _ema(yoy, QDAYS * 5)
    e20q = _ema(yoy, DDAYS_5Y)
    return _safe_div(e5q, e20q) - 1.0


def f43_hdcl_092_revenue_growth_ema5q_decel_thrust(revenue: pd.Series) -> pd.Series:
    """5q-EMA of YoY now − 5q-EMA of YoY 5q ago — smoothed deceleration thrust."""
    yoy = _safe_log(revenue).diff(YDAYS)
    e = _ema(yoy, QDAYS * 5)
    return e - e.shift(QDAYS * 5)


def f43_hdcl_093_revenue_growth_pivot_signal(revenue: pd.Series) -> pd.Series:
    """(max 8q YoY − current YoY) / std 5y YoY — magnitude of pivot from peak in σ-units."""
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    sd = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    return _safe_div(mx - yoy, sd)


def f43_hdcl_094_revenue_growth_inflection_recency_5y(revenue: pd.Series) -> pd.Series:
    """Bars since last sign-flip of (5q slope of YoY) within 5y — trajectory inflection recency."""
    yoy = _safe_log(revenue).diff(YDAYS)
    slope = _rolling_slope(yoy, QDAYS * 5)
    sg = np.sign(slope.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return _recency_since_event(flip, DDAYS_5Y)


def f43_hdcl_095_revenue_growth_break_below_mean_recency_5y(revenue: pd.Series) -> pd.Series:
    """Bars since the last bar where YoY crossed below its 5y mean — break-below-baseline recency."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((yoy < m) & (yoy.shift(1) >= m.shift(1))).astype(float)
    return _recency_since_event(flag, DDAYS_5Y)


def f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y(revenue: pd.Series) -> pd.Series:
    """Bars since the last bar where YoY crossed below 0.05 (5%) within 5y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy < 0.05) & (yoy.shift(1) >= 0.05)).astype(float)
    return _recency_since_event(flag, DDAYS_5Y)


def f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q(revenue: pd.Series) -> pd.Series:
    """(YoY now − min 8q YoY) / (max 8q YoY − min 8q YoY) — current position in 8q growth range (0=trough, 1=peak)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    mn = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(yoy - mn, mx - mn)


def f43_hdcl_098_revenue_growth_trajectory_zscore_combination(revenue: pd.Series) -> pd.Series:
    """Z-score of YoY vs 5y minus z-score of YoY vs 2y — short-baseline-faster-decay differential."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_zscore(yoy, DDAYS_5Y) - _rolling_zscore(yoy, DDAYS_2Y)


def f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff(revenue: pd.Series) -> pd.Series:
    """(3y slope of YoY) − (5y slope of YoY) — more-recent vs longer trajectory differential."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_3Y) - _rolling_slope(yoy, DDAYS_5Y)


def f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q(revenue: pd.Series) -> pd.Series:
    """Trailing-2q mean YoY − trailing-8q mean YoY — recent-half-quarter vs 2y baseline."""
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(QDAYS * 2, min_periods=QDAYS).mean() - yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − AR YoY) — AR growing faster than revenue (negative) = quality concern."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(accountsreceivable).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − inventory YoY) — inventory build-up indicator when negative."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(inventory).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − capex YoY) — capex outpacing revenue when negative (over-investment)."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(capex).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − sgna YoY) — opex growing faster than revenue when negative."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(sgna).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − rnd YoY) — R&D outpacing revenue when negative."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(rnd).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_106_revenue_per_sgna_change_yoy(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    """YoY change in (revenue / sgna) — productivity proxy YoY change."""
    prod = _safe_div(revenue, sgna)
    return _safe_log(prod).diff(YDAYS)


def f43_hdcl_107_working_capital_growth_outpacing_revenue_streak(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where working-capital YoY > revenue YoY — efficiency loss persistence."""
    flag = (_safe_log_signed(workingcapital).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_108_inventory_growth_outpacing_revenue_streak(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Current streak where inventory YoY > revenue YoY — inventory build-up persistence."""
    flag = (_safe_log(inventory).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_109_ar_growth_outpacing_revenue_streak(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    """Current streak where AR YoY > revenue YoY — receivables-quality concern persistence."""
    flag = (_safe_log(accountsreceivable).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_110_sgna_growth_outpacing_revenue_streak(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    """Current streak where sgna YoY > revenue YoY — operating-leverage breakdown persistence."""
    flag = (_safe_log(sgna).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_111_capex_growth_outpacing_revenue_streak(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Current streak where capex YoY > revenue YoY — over-investment persistence."""
    flag = (_safe_log_signed(capex).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_112_revenue_growth_quality_score_8q(revenue: pd.Series, accountsreceivable: pd.Series, inventory: pd.Series) -> pd.Series:
    """Mean over 8q of (revenue YoY > 0) AND (AR YoY ≤ revenue YoY) AND (inventory YoY ≤ revenue YoY)."""
    ryoy = _safe_log(revenue).diff(YDAYS)
    aryoy = _safe_log(accountsreceivable).diff(YDAYS)
    inyoy = _safe_log(inventory).diff(YDAYS)
    flag = ((ryoy > 0) & (aryoy <= ryoy) & (inyoy <= ryoy)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_113_cash_conversion_with_revenue_growth_change(revenue: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Δ in (fcf/netinc) over 252d, combined with revenue YoY direction — cash-quality change in growth regime."""
    cc = _safe_div(fcf, netinc)
    cc_chg = cc.diff(YDAYS)
    ryoy = _safe_log(revenue).diff(YDAYS)
    return cc_chg * np.sign(ryoy)


def f43_hdcl_114_ebitda_to_revenue_growth_decay_8q(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − ebitda YoY) — EBITDA leverage decay vs revenue."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(ebitda).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_115_fcf_to_revenue_growth_decay_8q(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − fcf YoY) — FCF leverage decay vs revenue."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(fcf).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_116_gp_to_revenue_growth_decay_8q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Trailing-8q mean (revenue YoY − gp YoY) — GP leverage decay vs revenue."""
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(gp).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_117_incremental_revenue_per_incremental_capex_8q(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    """Δrevenue(8q) / Δcapex(8q) — marginal-revenue-per-marginal-capex-dollar."""
    dr = revenue - revenue.shift(DDAYS_2Y)
    dc = capex - capex.shift(DDAYS_2Y)
    return _safe_div(dr, dc)


def f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    """Δrevenue(8q) / Δrnd(8q) — marginal revenue per marginal R&D dollar."""
    dr = revenue - revenue.shift(DDAYS_2Y)
    dr_rnd = rnd - rnd.shift(DDAYS_2Y)
    return _safe_div(dr, dr_rnd)


def f43_hdcl_119_incremental_margin_decay_8q(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Δgp(8q) / Δrevenue(8q) — incremental gross-margin contribution (declining = decay)."""
    dg = gp - gp.shift(DDAYS_2Y)
    dr = revenue - revenue.shift(DDAYS_2Y)
    return _safe_div(dg, dr)


def f43_hdcl_120_capital_intensity_change_yoy(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in (capex/revenue) — capital intensity drift."""
    ci = _safe_div(capex, revenue)
    return ci.diff(YDAYS)


def f43_hdcl_121_operating_leverage_breakdown_indicator(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """1 if revenue YoY > 0.10 AND opinc YoY < 0 — fast top-line but operating-income declining."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0.10) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(float)
    return flag.where(revenue.notna() & opinc.notna(), np.nan)


def f43_hdcl_122_negative_operating_leverage_streak(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Current streak where revenue YoY > 0 AND opinc YoY < 0 — sustained negative operating leverage."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Bars in trailing 8q where revenue YoY > 0 AND opinc < 0 — growing-while-loss-making count."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (opinc < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Bars in trailing 8q where revenue YoY > 0 AND fcf < 0 — growing-while-cash-burning count."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (fcf < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Bars in trailing 8q where revenue YoY > 0 AND netinc < 0 — growing-while-net-loss count."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (netinc < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator(revenue: pd.Series) -> pd.Series:
    """1 if (YoY 63d ago − YoY now) > 0.05 — 1q step-down in growth rate of ≥5pp."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.05).astype(float).where(drop.notna(), np.nan)


def f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator(revenue: pd.Series) -> pd.Series:
    """1 if 1q step-down in YoY ≥ 10pp."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.10).astype(float).where(drop.notna(), np.nan)


def f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator(revenue: pd.Series) -> pd.Series:
    """1 if 1q step-down in YoY ≥ 20pp."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.20).astype(float).where(drop.notna(), np.nan)


def f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator(revenue: pd.Series) -> pd.Series:
    """1 if 2q step-down in YoY ≥ 5pp."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return (drop > 0.05).astype(float).where(drop.notna(), np.nan)


def f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator(revenue: pd.Series) -> pd.Series:
    """1 if 2q step-down in YoY ≥ 10pp."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return (drop > 0.10).astype(float).where(drop.notna(), np.nan)


def f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator(revenue: pd.Series) -> pd.Series:
    """1 if (YoY 252d ago) > 0.30 AND (YoY now) < 0.05 — hypergrowth → near-zero transition."""
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy.shift(YDAYS) > 0.30) & (yoy < 0.05)).astype(float)
    return flag.where(yoy.notna() & yoy.shift(YDAYS).notna(), np.nan)


def f43_hdcl_132_max_single_q_yoy_drop_8q(revenue: pd.Series) -> pd.Series:
    """Max 1q (YoY shift(63) − YoY now) over trailing 8q — worst single-quarter step-down."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return drop.rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f43_hdcl_133_max_2q_yoy_drop_8q(revenue: pd.Series) -> pd.Series:
    """Max 2q (YoY shift(126) − YoY now) over trailing 8q — worst 2q step-down."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return drop.rolling(DDAYS_2Y, min_periods=YDAYS).max()


def f43_hdcl_134_max_4q_yoy_drop_20q(revenue: pd.Series) -> pd.Series:
    """Max 4q (YoY 252d ago − YoY now) over trailing 5y — worst 4q step-down."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(YDAYS) - yoy
    return drop.rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f43_hdcl_135_cliff_breadth_count_4q(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Bars in trailing 4q where (revenue YoY < 0) + (opinc YoY < 0) + (fcf YoY < 0) + (netinc YoY < 0) ≥ 3."""
    r_neg = (_safe_log(revenue).diff(YDAYS) < 0).astype(int)
    o_neg = (_safe_log_signed(opinc).diff(YDAYS) < 0).astype(int)
    f_neg = (_safe_log_signed(fcf).diff(YDAYS) < 0).astype(int)
    n_neg = (_safe_log_signed(netinc).diff(YDAYS) < 0).astype(int)
    total = (r_neg + o_neg + f_neg + n_neg).astype(float)
    flag = (total >= 3).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator(revenue: pd.Series) -> pd.Series:
    """1 if QoQ < 0 for 4 consecutive quarters (~252 daily bars worth of negative QoQ)."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(int)
    streak = _streak_above_zero(flag, YDAYS)
    return (streak >= 4 * QDAYS).astype(float).where(streak.notna(), np.nan)


def f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator(revenue: pd.Series) -> pd.Series:
    """1 if QoQ < 0 for 2 consecutive quarters."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(int)
    streak = _streak_above_zero(flag, YDAYS)
    return (streak >= 2 * QDAYS).astype(float).where(streak.notna(), np.nan)


def f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q with QoQ < 0 — sequential-decline persistence."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y(revenue: pd.Series) -> pd.Series:
    """log(current YoY / 5y peak YoY) using signed-log — log-space drop from peak (≤0)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    peak = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _safe_log_signed(yoy) - _safe_log_signed(peak)


def f43_hdcl_140_revenue_yoy_below_2y_max_log_distance(revenue: pd.Series) -> pd.Series:
    """log(current YoY / 2y peak YoY) — drop from 2y peak (signed-log)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    peak = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _safe_log_signed(yoy) - _safe_log_signed(peak)


def f43_hdcl_141_growth_cliff_composite_indicator(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if YoY drop ≥ 0.10 in 1q AND opinc YoY < 0 AND fcf YoY < 0 — fused cliff event."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = ((drop > 0.10) & (_safe_log_signed(opinc).diff(YDAYS) < 0) & (_safe_log_signed(fcf).diff(YDAYS) < 0)).astype(float)
    return flag.where(drop.notna(), np.nan)


def f43_hdcl_142_growth_cliff_intensity_score_8q(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean over 8q of (revenue 1q YoY-drop > 0.10) + (opinc YoY < 0) + (fcf YoY < 0) — composite intensity (0-3)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    s = ((drop > 0.10).astype(float) + (_safe_log_signed(opinc).diff(YDAYS) < 0).astype(float) + (_safe_log_signed(fcf).diff(YDAYS) < 0).astype(float))
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_143_growth_cliff_recency_5y(revenue: pd.Series) -> pd.Series:
    """Bars since the last cliff event (YoY 1q-drop > 0.10) within 5y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = (drop > 0.10).astype(float)
    return _recency_since_event(flag, DDAYS_5Y)


def f43_hdcl_144_growth_cliff_persistence_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where 1q YoY-drop > 0.05 — sustained cliffing persistence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = (drop > 0.05).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f43_hdcl_145_growth_cliff_zscore_5y(revenue: pd.Series) -> pd.Series:
    """Z-score of current 1q YoY-drop vs trailing-5y distribution of 1q YoY-drops."""
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return _rolling_zscore(drop, DDAYS_5Y)


def f43_hdcl_146_hypergrowth_to_decel_transition_score(revenue: pd.Series) -> pd.Series:
    """Mean over 5y of [indicator(YoY 252d ago > 0.30) × indicator(YoY now < 0.10)] — transition prevalence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    s = ((yoy.shift(YDAYS) > 0.30).astype(float) * (yoy < 0.10).astype(float))
    return s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """(5y max YoY revenue − current YoY revenue) × indicator(opinc and fcf both YoY < 0)."""
    yoy_r = _safe_log(revenue).diff(YDAYS)
    distance = yoy_r.rolling(DDAYS_5Y, min_periods=YDAYS).max() - yoy_r
    cond = ((_safe_log_signed(opinc).diff(YDAYS) < 0) & (_safe_log_signed(fcf).diff(YDAYS) < 0)).astype(float)
    return distance * cond


def f43_hdcl_148_composite_f43_hdcl_blowoff_score(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean over 5y of [rank_pct(revenue YoY) × (1 − rank_pct(opinc YoY)) × (1 − rank_pct(fcf YoY))] — high rev, low quality."""
    r_pct = _rolling_rank_pct(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    o_pct = _rolling_rank_pct(_safe_log_signed(opinc).diff(YDAYS), DDAYS_5Y)
    f_pct = _rolling_rank_pct(_safe_log_signed(fcf).diff(YDAYS), DDAYS_5Y)
    s = r_pct * (1.0 - o_pct) * (1.0 - f_pct)
    return s.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f43_hdcl_149_composite_f43_hdcl_distress_score(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Mean over 8q of [(revenue YoY decel) AND (opinc<0 OR fcf<0 OR netinc<0)] — distress prevalence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    decel = (yoy < yoy.shift(YDAYS))
    distress = (opinc < 0) | (fcf < 0) | (netinc < 0)
    flag = (decel & distress).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f43_hdcl_150_composite_f43_hdcl_topping_score(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Mean over 5y of [(1 − rank_pct of current YoY)] for revenue,gp,opinc,fcf,netinc,ebitda averaged — composite topping."""
    series_list = [
        _safe_log(revenue).diff(YDAYS),
        _safe_log(gp).diff(YDAYS),
        _safe_log_signed(opinc).diff(YDAYS),
        _safe_log_signed(fcf).diff(YDAYS),
        _safe_log_signed(netinc).diff(YDAYS),
        _safe_log_signed(ebitda).diff(YDAYS),
    ]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        r = _rolling_rank_pct(s, DDAYS_5Y)
        total = total + (1.0 - r)
        valid = valid & r.notna()
    avg = (total / len(series_list)).where(valid, np.nan)
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

HYPERGROWTH_DECELERATION_CLIFF_BASE_REGISTRY_076_150 = {
    "f43_hdcl_076_revenue_growth_trajectory_slope_8q": {"inputs": ["revenue"], "func": f43_hdcl_076_revenue_growth_trajectory_slope_8q},
    "f43_hdcl_077_revenue_growth_trajectory_slope_20q": {"inputs": ["revenue"], "func": f43_hdcl_077_revenue_growth_trajectory_slope_20q},
    "f43_hdcl_078_revenue_growth_trajectory_curvature_8q": {"inputs": ["revenue"], "func": f43_hdcl_078_revenue_growth_trajectory_curvature_8q},
    "f43_hdcl_079_revenue_growth_jump_count_negative_8q": {"inputs": ["revenue"], "func": f43_hdcl_079_revenue_growth_jump_count_negative_8q},
    "f43_hdcl_080_revenue_growth_step_change_negative_indicator": {"inputs": ["revenue"], "func": f43_hdcl_080_revenue_growth_step_change_negative_indicator},
    "f43_hdcl_081_revenue_growth_zscore_change_4q": {"inputs": ["revenue"], "func": f43_hdcl_081_revenue_growth_zscore_change_4q},
    "f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q": {"inputs": ["revenue"], "func": f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q},
    "f43_hdcl_083_revenue_yoy_distribution_skewness_20q": {"inputs": ["revenue"], "func": f43_hdcl_083_revenue_yoy_distribution_skewness_20q},
    "f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q": {"inputs": ["revenue"], "func": f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q},
    "f43_hdcl_085_revenue_yoy_distribution_minimum_20q": {"inputs": ["revenue"], "func": f43_hdcl_085_revenue_yoy_distribution_minimum_20q},
    "f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q": {"inputs": ["revenue"], "func": f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q},
    "f43_hdcl_087_revenue_growth_persistence_above_zero_streak": {"inputs": ["revenue"], "func": f43_hdcl_087_revenue_growth_persistence_above_zero_streak},
    "f43_hdcl_088_revenue_growth_persistence_below_zero_streak": {"inputs": ["revenue"], "func": f43_hdcl_088_revenue_growth_persistence_below_zero_streak},
    "f43_hdcl_089_revenue_growth_oscillation_count_8q": {"inputs": ["revenue"], "func": f43_hdcl_089_revenue_growth_oscillation_count_8q},
    "f43_hdcl_090_revenue_growth_directional_consistency_8q": {"inputs": ["revenue"], "func": f43_hdcl_090_revenue_growth_directional_consistency_8q},
    "f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q": {"inputs": ["revenue"], "func": f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q},
    "f43_hdcl_092_revenue_growth_ema5q_decel_thrust": {"inputs": ["revenue"], "func": f43_hdcl_092_revenue_growth_ema5q_decel_thrust},
    "f43_hdcl_093_revenue_growth_pivot_signal": {"inputs": ["revenue"], "func": f43_hdcl_093_revenue_growth_pivot_signal},
    "f43_hdcl_094_revenue_growth_inflection_recency_5y": {"inputs": ["revenue"], "func": f43_hdcl_094_revenue_growth_inflection_recency_5y},
    "f43_hdcl_095_revenue_growth_break_below_mean_recency_5y": {"inputs": ["revenue"], "func": f43_hdcl_095_revenue_growth_break_below_mean_recency_5y},
    "f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y": {"inputs": ["revenue"], "func": f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y},
    "f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q": {"inputs": ["revenue"], "func": f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q},
    "f43_hdcl_098_revenue_growth_trajectory_zscore_combination": {"inputs": ["revenue"], "func": f43_hdcl_098_revenue_growth_trajectory_zscore_combination},
    "f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff": {"inputs": ["revenue"], "func": f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff},
    "f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q": {"inputs": ["revenue"], "func": f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q},
    "f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q": {"inputs": ["revenue", "accountsreceivable"], "func": f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q},
    "f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q": {"inputs": ["revenue", "inventory"], "func": f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q},
    "f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q": {"inputs": ["revenue", "capex"], "func": f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q},
    "f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q": {"inputs": ["revenue", "sgna"], "func": f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q},
    "f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q": {"inputs": ["revenue", "rnd"], "func": f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q},
    "f43_hdcl_106_revenue_per_sgna_change_yoy": {"inputs": ["revenue", "sgna"], "func": f43_hdcl_106_revenue_per_sgna_change_yoy},
    "f43_hdcl_107_working_capital_growth_outpacing_revenue_streak": {"inputs": ["revenue", "workingcapital"], "func": f43_hdcl_107_working_capital_growth_outpacing_revenue_streak},
    "f43_hdcl_108_inventory_growth_outpacing_revenue_streak": {"inputs": ["revenue", "inventory"], "func": f43_hdcl_108_inventory_growth_outpacing_revenue_streak},
    "f43_hdcl_109_ar_growth_outpacing_revenue_streak": {"inputs": ["revenue", "accountsreceivable"], "func": f43_hdcl_109_ar_growth_outpacing_revenue_streak},
    "f43_hdcl_110_sgna_growth_outpacing_revenue_streak": {"inputs": ["revenue", "sgna"], "func": f43_hdcl_110_sgna_growth_outpacing_revenue_streak},
    "f43_hdcl_111_capex_growth_outpacing_revenue_streak": {"inputs": ["revenue", "capex"], "func": f43_hdcl_111_capex_growth_outpacing_revenue_streak},
    "f43_hdcl_112_revenue_growth_quality_score_8q": {"inputs": ["revenue", "accountsreceivable", "inventory"], "func": f43_hdcl_112_revenue_growth_quality_score_8q},
    "f43_hdcl_113_cash_conversion_with_revenue_growth_change": {"inputs": ["revenue", "fcf", "netinc"], "func": f43_hdcl_113_cash_conversion_with_revenue_growth_change},
    "f43_hdcl_114_ebitda_to_revenue_growth_decay_8q": {"inputs": ["revenue", "ebitda"], "func": f43_hdcl_114_ebitda_to_revenue_growth_decay_8q},
    "f43_hdcl_115_fcf_to_revenue_growth_decay_8q": {"inputs": ["revenue", "fcf"], "func": f43_hdcl_115_fcf_to_revenue_growth_decay_8q},
    "f43_hdcl_116_gp_to_revenue_growth_decay_8q": {"inputs": ["revenue", "gp"], "func": f43_hdcl_116_gp_to_revenue_growth_decay_8q},
    "f43_hdcl_117_incremental_revenue_per_incremental_capex_8q": {"inputs": ["revenue", "capex"], "func": f43_hdcl_117_incremental_revenue_per_incremental_capex_8q},
    "f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q": {"inputs": ["revenue", "rnd"], "func": f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q},
    "f43_hdcl_119_incremental_margin_decay_8q": {"inputs": ["revenue", "gp"], "func": f43_hdcl_119_incremental_margin_decay_8q},
    "f43_hdcl_120_capital_intensity_change_yoy": {"inputs": ["capex", "revenue"], "func": f43_hdcl_120_capital_intensity_change_yoy},
    "f43_hdcl_121_operating_leverage_breakdown_indicator": {"inputs": ["revenue", "opinc"], "func": f43_hdcl_121_operating_leverage_breakdown_indicator},
    "f43_hdcl_122_negative_operating_leverage_streak": {"inputs": ["revenue", "opinc"], "func": f43_hdcl_122_negative_operating_leverage_streak},
    "f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q": {"inputs": ["revenue", "opinc"], "func": f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q},
    "f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q": {"inputs": ["revenue", "fcf"], "func": f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q},
    "f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q": {"inputs": ["revenue", "netinc"], "func": f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q},
    "f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator": {"inputs": ["revenue"], "func": f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator},
    "f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator": {"inputs": ["revenue"], "func": f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator},
    "f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator": {"inputs": ["revenue"], "func": f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator},
    "f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator": {"inputs": ["revenue"], "func": f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator},
    "f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator": {"inputs": ["revenue"], "func": f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator},
    "f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator": {"inputs": ["revenue"], "func": f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator},
    "f43_hdcl_132_max_single_q_yoy_drop_8q": {"inputs": ["revenue"], "func": f43_hdcl_132_max_single_q_yoy_drop_8q},
    "f43_hdcl_133_max_2q_yoy_drop_8q": {"inputs": ["revenue"], "func": f43_hdcl_133_max_2q_yoy_drop_8q},
    "f43_hdcl_134_max_4q_yoy_drop_20q": {"inputs": ["revenue"], "func": f43_hdcl_134_max_4q_yoy_drop_20q},
    "f43_hdcl_135_cliff_breadth_count_4q": {"inputs": ["revenue", "opinc", "fcf", "netinc"], "func": f43_hdcl_135_cliff_breadth_count_4q},
    "f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator": {"inputs": ["revenue"], "func": f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator},
    "f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator": {"inputs": ["revenue"], "func": f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator},
    "f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q": {"inputs": ["revenue"], "func": f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q},
    "f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y": {"inputs": ["revenue"], "func": f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y},
    "f43_hdcl_140_revenue_yoy_below_2y_max_log_distance": {"inputs": ["revenue"], "func": f43_hdcl_140_revenue_yoy_below_2y_max_log_distance},
    "f43_hdcl_141_growth_cliff_composite_indicator": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_141_growth_cliff_composite_indicator},
    "f43_hdcl_142_growth_cliff_intensity_score_8q": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_142_growth_cliff_intensity_score_8q},
    "f43_hdcl_143_growth_cliff_recency_5y": {"inputs": ["revenue"], "func": f43_hdcl_143_growth_cliff_recency_5y},
    "f43_hdcl_144_growth_cliff_persistence_8q": {"inputs": ["revenue"], "func": f43_hdcl_144_growth_cliff_persistence_8q},
    "f43_hdcl_145_growth_cliff_zscore_5y": {"inputs": ["revenue"], "func": f43_hdcl_145_growth_cliff_zscore_5y},
    "f43_hdcl_146_hypergrowth_to_decel_transition_score": {"inputs": ["revenue"], "func": f43_hdcl_146_hypergrowth_to_decel_transition_score},
    "f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel},
    "f43_hdcl_148_composite_f43_hdcl_blowoff_score": {"inputs": ["revenue", "opinc", "fcf"], "func": f43_hdcl_148_composite_f43_hdcl_blowoff_score},
    "f43_hdcl_149_composite_f43_hdcl_distress_score": {"inputs": ["revenue", "opinc", "fcf", "netinc"], "func": f43_hdcl_149_composite_f43_hdcl_distress_score},
    "f43_hdcl_150_composite_f43_hdcl_topping_score": {"inputs": ["revenue", "gp", "opinc", "fcf", "netinc", "ebitda"], "func": f43_hdcl_150_composite_f43_hdcl_topping_score},
}
