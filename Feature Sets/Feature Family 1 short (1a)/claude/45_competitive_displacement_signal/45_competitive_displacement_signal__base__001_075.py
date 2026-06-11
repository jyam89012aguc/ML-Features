"""competitive_displacement_signal base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: SF1-only signs that demand has been displaced (competitor is taking
share, market is shifting) — inventory/AR build-up (couldn't sell-through),
cash burn pressure, revenue volatility / discontinuity / shock events,
pricing-power loss (revenue per unit). Continued in __base__076_150.py
for 150 total. PIT-clean.
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


def _days_since_min(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmin(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f45_cdis_001_inventory_to_revenue_level(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory/revenue — raw inventory intensity per dollar of revenue."""
    return _safe_div(inventory, revenue)


def f45_cdis_002_inventory_to_revenue_change_yoy(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y change in inventory/revenue — rising = sell-through deteriorating."""
    return _safe_div(inventory, revenue).diff(YDAYS)


def f45_cdis_003_inventory_to_revenue_change_5y(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in inventory/revenue."""
    return _safe_div(inventory, revenue).diff(DDAYS_5Y)


def f45_cdis_004_inventory_to_revenue_zscore_5y(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of inventory/revenue vs 5y."""
    return _rolling_zscore(_safe_div(inventory, revenue), DDAYS_5Y)


def f45_cdis_005_inventory_to_revenue_rise_streak(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current streak where inv/rev > its trailing-1y mean — sustained build-up."""
    r = _safe_div(inventory, revenue)
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (r > m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_006_inventory_yoy_minus_revenue_yoy(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory YoY − revenue YoY — positive = inventory outpacing revenue (build-up)."""
    return _safe_log(inventory).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)


def f45_cdis_007_inventory_3y_minus_revenue_3y_growth(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory 3y log growth − revenue 3y log growth — long-window divergence."""
    return _safe_log(inventory).diff(DDAYS_3Y) - _safe_log(revenue).diff(DDAYS_3Y)


def f45_cdis_008_inventory_growth_above_revenue_count_8q(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where inventory YoY > revenue YoY — sustained-build-up persistence."""
    flag = (_safe_log(inventory).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_009_inventory_turnover_level(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """Inventory turnover = cor / inventory — higher = faster sell-through."""
    return _safe_div(cor, inventory)


def f45_cdis_010_inventory_turnover_change_5y(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """5y change in inventory turnover — declining = sell-through slowing."""
    return _safe_div(cor, inventory).diff(DDAYS_5Y)


def f45_cdis_011_inventory_turnover_zscore_5y(cor: pd.Series, inventory: pd.Series) -> pd.Series:
    """Z-score of inventory turnover vs 5y."""
    return _rolling_zscore(_safe_div(cor, inventory), DDAYS_5Y)


def f45_cdis_012_inventory_to_assets_level(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """Inventory / assets — share of balance sheet held as inventory."""
    return _safe_div(inventory, assets)


def f45_cdis_013_inventory_to_assets_change_5y(inventory: pd.Series, assets: pd.Series) -> pd.Series:
    """5y change in inventory/assets."""
    return _safe_div(inventory, assets).diff(DDAYS_5Y)


def f45_cdis_014_ar_to_revenue_level(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR/revenue level — DSO proxy."""
    return _safe_div(accountsreceivable, revenue)


def f45_cdis_015_ar_to_revenue_change_5y(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in AR/revenue — extending credit to maintain sales."""
    return _safe_div(accountsreceivable, revenue).diff(DDAYS_5Y)


def f45_cdis_016_ar_to_revenue_zscore_5y(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of AR/revenue vs 5y."""
    return _rolling_zscore(_safe_div(accountsreceivable, revenue), DDAYS_5Y)


def f45_cdis_017_ar_yoy_minus_revenue_yoy(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR YoY − revenue YoY — positive = AR outpacing revenue (channel-stuffing concern)."""
    return _safe_log(accountsreceivable).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)


def f45_cdis_018_ar_3y_minus_revenue_3y_growth(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """AR 3y log growth − revenue 3y log growth."""
    return _safe_log(accountsreceivable).diff(DDAYS_3Y) - _safe_log(revenue).diff(DDAYS_3Y)


def f45_cdis_019_ar_growth_above_revenue_count_8q(accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where AR YoY > revenue YoY — sustained AR build-up."""
    flag = (_safe_log(accountsreceivable).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_020_ar_turnover_level(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    """AR turnover = revenue / AR — higher = faster collection."""
    return _safe_div(revenue, accountsreceivable)


def f45_cdis_021_ar_to_assets_level(accountsreceivable: pd.Series, assets: pd.Series) -> pd.Series:
    """AR / assets — share of balance sheet held as receivables."""
    return _safe_div(accountsreceivable, assets)


def f45_cdis_022_ar_to_assets_change_5y(accountsreceivable: pd.Series, assets: pd.Series) -> pd.Series:
    """5y change in AR/assets."""
    return _safe_div(accountsreceivable, assets).diff(DDAYS_5Y)


def f45_cdis_023_ar_plus_inventory_to_revenue_level(accountsreceivable: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """(AR + Inventory) / revenue — combined working-capital-tied-to-revenue ratio."""
    return _safe_div(accountsreceivable + inventory, revenue)


def f45_cdis_024_ar_plus_inventory_to_revenue_change_5y(accountsreceivable: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in (AR+Inv)/revenue."""
    return _safe_div(accountsreceivable + inventory, revenue).diff(DDAYS_5Y)


def f45_cdis_025_ar_plus_inventory_growth_above_revenue_streak(accountsreceivable: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current streak where (AR+Inv) YoY > revenue YoY — combined-build-up persistence."""
    flag = (_safe_log(accountsreceivable + inventory).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_026_cash_to_revenue_change_5y(cashneq: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y change in cash / revenue — cash cover deteriorating as sales hold."""
    return _safe_div(cashneq, revenue).diff(DDAYS_5Y)


def f45_cdis_027_cash_burn_pace_relative_to_revenue_yoy(cashneq: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y change in (cash / revenue) — rate of cover decline."""
    return _safe_div(cashneq, revenue).diff(YDAYS)


def f45_cdis_028_fcf_negative_streak(fcf: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where fcf < 0 — sustained cash-burn run."""
    flag = (fcf < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_029_fcf_negative_count_8q(fcf: pd.Series) -> pd.Series:
    """Bars in trailing 8q where fcf < 0 — short-window cash-burn frequency."""
    flag = (fcf < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_030_fcf_negative_count_20q(fcf: pd.Series) -> pd.Series:
    """Bars in trailing 20q (5y) where fcf < 0 — long-window cash-burn frequency."""
    flag = (fcf < 0).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_031_cash_burn_acceleration_yoy(fcf: pd.Series) -> pd.Series:
    """1y change in signed-log fcf — acceleration of cash-flow trajectory."""
    return _safe_log_signed(fcf).diff(YDAYS)


def f45_cdis_032_cash_burn_with_revenue_growth_indicator(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if fcf < 0 AND revenue YoY > 0 — burning cash even while growing."""
    flag = ((fcf < 0) & (_safe_log(revenue).diff(YDAYS) > 0)).astype(float)
    return flag.where(fcf.notna() & revenue.notna(), np.nan)


def f45_cdis_033_cash_burn_with_revenue_decel_indicator(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if fcf < 0 AND revenue YoY is decelerating (< trailing-1y mean of YoY)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((fcf < 0) & (yoy < m)).astype(float)
    return flag.where(fcf.notna() & yoy.notna(), np.nan)


def f45_cdis_034_fcf_to_revenue_below_neg5pct_count_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where fcf/revenue < −0.05 (>5% burn rate)."""
    fm = _safe_div(fcf, revenue)
    flag = (fm < -0.05).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_035_fcf_to_revenue_below_neg10pct_count_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where fcf/revenue < −0.10 (>10% burn rate) — severe burn frequency."""
    fm = _safe_div(fcf, revenue)
    flag = (fm < -0.10).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_036_ncfo_negative_streak(ncfo: pd.Series) -> pd.Series:
    """Current streak where operating cash flow < 0 — fundamental cash-burn at the operations level."""
    flag = (ncfo < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_037_ncfo_yoy_decline_streak(ncfo: pd.Series) -> pd.Series:
    """Current streak where ncfo YoY < 0 — operating cash-flow deceleration persistence."""
    flag = (_safe_log_signed(ncfo).diff(YDAYS) < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_038_cash_burn_runway_proxy(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """cash / |trailing 4q sum of fcf| — quarters of cash runway when FCF is negative."""
    burn = fcf.rolling(YDAYS, min_periods=QDAYS).sum().abs()
    return _safe_div(cashneq, burn)


def f45_cdis_039_cash_burn_runway_change_yoy(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """1y change in runway proxy — runway extending or contracting."""
    burn = fcf.rolling(YDAYS, min_periods=QDAYS).sum().abs()
    runway = _safe_div(cashneq, burn)
    return runway.diff(YDAYS)


def f45_cdis_040_cash_burn_runway_zscore_5y(cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """Z-score of runway proxy vs 5y."""
    burn = fcf.rolling(YDAYS, min_periods=QDAYS).sum().abs()
    runway = _safe_div(cashneq, burn)
    return _rolling_zscore(runway, DDAYS_5Y)


def f45_cdis_041_cashneq_yoy_change_log(cashneq: pd.Series) -> pd.Series:
    """1y log change in cash — annual cash position shift."""
    return _safe_log(cashneq).diff(YDAYS)


def f45_cdis_042_cashneq_5y_change_log(cashneq: pd.Series) -> pd.Series:
    """5y log change in cash — long-horizon cash trajectory."""
    return _safe_log(cashneq).diff(DDAYS_5Y)


def f45_cdis_043_cashneq_decline_streak(cashneq: pd.Series) -> pd.Series:
    """Current streak where cash < trailing-1y mean of itself — sustained cash decline."""
    m = cashneq.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (cashneq < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_044_cashneq_below_5y_min_indicator(cashneq: pd.Series) -> pd.Series:
    """1 if current cash is at trailing-5y rolling min (within 1e-6 tol)."""
    mn = cashneq.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return ((cashneq <= mn + 1e-6) & cashneq.notna() & mn.notna()).astype(float)


def f45_cdis_045_cash_pressure_composite_score_8q(cashneq: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of indicator(cash/revenue declining 1y) AND (fcf<0)."""
    cov = _safe_div(cashneq, revenue)
    flag = ((cov.diff(YDAYS) < 0) & (fcf < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_046_revenue_volatility_yoy_8q(revenue: pd.Series) -> pd.Series:
    """Std of revenue YoY growth over trailing 8q — annual-growth wobble."""
    return _safe_log(revenue).diff(YDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f45_cdis_047_revenue_volatility_qoq_8q(revenue: pd.Series) -> pd.Series:
    """Std of revenue QoQ growth over trailing 8q — sequential-growth wobble."""
    return _safe_log(revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()


def f45_cdis_048_revenue_volatility_zscore_5y(revenue: pd.Series) -> pd.Series:
    """Z-score (vs 5y) of the 8q-rolling std of QoQ — wobble-of-wobble."""
    v = _safe_log(revenue).diff(QDAYS).rolling(DDAYS_2Y, min_periods=YDAYS).std()
    return _rolling_zscore(v, DDAYS_5Y)


def f45_cdis_049_revenue_qoq_kurtosis_8q(revenue: pd.Series) -> pd.Series:
    """Excess kurtosis of QoQ over 8q — fat-tailed sequential-growth regime."""
    qoq = _safe_log(revenue).diff(QDAYS)
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_k, raw=True)


def f45_cdis_050_revenue_qoq_skewness_8q(revenue: pd.Series) -> pd.Series:
    """Skewness of QoQ over 8q — negative skew indicates sudden-drop-prone regime."""
    qoq = _safe_log(revenue).diff(QDAYS)
    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / (sd ** 3))
    return qoq.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_sk, raw=True)


def f45_cdis_051_revenue_dispersion_yoy_5y(revenue: pd.Series) -> pd.Series:
    """(p75 − p25) of YoY growth in 5y — interquartile spread of annual growth."""
    yoy = _safe_log(revenue).diff(YDAYS)
    p75 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    p25 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    return p75 - p25


def f45_cdis_052_revenue_max_qoq_drop_5y(revenue: pd.Series) -> pd.Series:
    """Min QoQ growth in trailing 5y — worst single-quarter sequential drop."""
    return _safe_log(revenue).diff(QDAYS).rolling(DDAYS_5Y, min_periods=YDAYS).min()


def f45_cdis_053_revenue_max_yoy_drop_5y(revenue: pd.Series) -> pd.Series:
    """Min YoY growth in trailing 5y — worst single-quarter YoY reading."""
    return _safe_log(revenue).diff(YDAYS).rolling(DDAYS_5Y, min_periods=YDAYS).min()


def f45_cdis_054_revenue_drop_intensity_above_p95_count_5y(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 5y where |QoQ| > trailing-5y p95 — large-shock event count."""
    qoq = _safe_log(revenue).diff(QDAYS).abs()
    thr = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    flag = (qoq >= thr).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_055_revenue_post_drop_recovery_proxy_5y(revenue: pd.Series) -> pd.Series:
    """5y mean of (max(QoQ, 0)) − 5y mean of (|min(QoQ, 0)|) — asymmetric up vs down magnitude."""
    qoq = _safe_log(revenue).diff(QDAYS)
    up_mean = qoq.clip(lower=0).rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    down_mean = qoq.clip(upper=0).abs().rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return up_mean - down_mean


def f45_cdis_056_revenue_step_change_indicator_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where |QoQ| > trailing-5y mean + 2σ — step-event count."""
    qoq = _safe_log(revenue).diff(QDAYS).abs()
    m = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    flag = (qoq > (m + 2.0 * sd)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_057_revenue_jump_count_negative_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where QoQ < trailing-5y mean − 2σ — negative-jump count."""
    qoq = _safe_log(revenue).diff(QDAYS)
    m = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    flag = (qoq < (m - 2.0 * sd)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_058_revenue_outlier_count_5y(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 5y where YoY < trailing-5y mean − 2σ — annual-shock recurrence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    flag = (yoy < (m - 2.0 * sd)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_059_revenue_growth_below_mean_persistence_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of last 8q with YoY < trailing-5y mean — sub-mean persistence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (yoy < m).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_060_revenue_growth_persistence_below_zero_8q(revenue: pd.Series) -> pd.Series:
    """Fraction of last 8q with QoQ < 0 — sequential-decline persistence."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_061_revenue_above_trend_streak(revenue: pd.Series) -> pd.Series:
    """Current streak where revenue > 5y EMA of revenue — positive-trend persistence."""
    e = revenue.ewm(span=DDAYS_5Y, adjust=False, min_periods=YDAYS).mean()
    flag = (revenue > e).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_062_revenue_below_trend_streak(revenue: pd.Series) -> pd.Series:
    """Current streak where revenue < 5y EMA of revenue — negative-trend persistence."""
    e = revenue.ewm(span=DDAYS_5Y, adjust=False, min_periods=YDAYS).mean()
    flag = (revenue < e).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_063_revenue_trend_break_recency_5y(revenue: pd.Series) -> pd.Series:
    """Bars since the last sign-flip of (revenue − 5y EMA) — trend-break recency."""
    e = revenue.ewm(span=DDAYS_5Y, adjust=False, min_periods=YDAYS).mean()
    sg = np.sign((revenue - e).fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return _recency_since_event(flip, DDAYS_5Y)


def f45_cdis_064_revenue_smoothed_trend_slope_8q_vs_20q(revenue: pd.Series) -> pd.Series:
    """8q regression slope of revenue − 20q regression slope of revenue — short vs long trend differential."""
    return _rolling_slope(revenue, DDAYS_2Y) - _rolling_slope(revenue, DDAYS_5Y)


def f45_cdis_065_revenue_acceleration_breakdown_4q(revenue: pd.Series) -> pd.Series:
    """4q regression slope of QoQ growth — short-horizon acceleration shape (negative = decelerating)."""
    qoq = _safe_log(revenue).diff(QDAYS)
    return _rolling_slope(qoq, YDAYS)


def f45_cdis_066_revenue_qoq_zero_or_negative_count_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where QoQ ≤ 0 — stall/contraction frequency."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq <= 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_067_revenue_persistent_negativity_8q_streak(revenue: pd.Series) -> pd.Series:
    """Current streak of bars where QoQ < 0 — sequential-decline run."""
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_2Y)


def f45_cdis_068_revenue_below_lt_average_count_8q(revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where revenue < trailing-5y mean of revenue."""
    m = revenue.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (revenue < m).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_069_revenue_step_function_collapse_indicator(revenue: pd.Series) -> pd.Series:
    """1 if QoQ < −0.10 in current bar — single-quarter ≥10% step-down."""
    flag = (_safe_log(revenue).diff(QDAYS) < -0.10).astype(float)
    return flag.where(revenue.notna() & revenue.shift(QDAYS).notna(), np.nan)


def f45_cdis_070_revenue_discontinuity_score_5y(revenue: pd.Series) -> pd.Series:
    """Mean over 5y of indicator(|QoQ| > trailing-5y p95) — recurring-discontinuity prevalence."""
    qoq = _safe_log(revenue).diff(QDAYS).abs()
    thr = qoq.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    flag = (qoq >= thr).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_071_revenue_per_share_change_5y(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """5y log change in revenue per diluted share — pricing-power-per-unit-equity trajectory."""
    return _safe_log(_safe_div(revenue, shareswadil)).diff(DDAYS_5Y)


def f45_cdis_072_revenue_per_share_decline_streak(revenue: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Current streak where revenue/share < trailing-1y mean of itself."""
    rps = _safe_div(revenue, shareswadil)
    m = rps.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (rps < m).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_073_revenue_per_unit_inventory_change_5y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """5y change in (revenue / inventory) — pricing power per inventory unit."""
    return _safe_div(revenue, inventory).diff(DDAYS_5Y)


def f45_cdis_074_revenue_per_unit_inventory_zscore_5y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Z-score of (revenue / inventory) vs 5y."""
    return _rolling_zscore(_safe_div(revenue, inventory), DDAYS_5Y)


def f45_cdis_075_revenue_per_dollar_of_sgna_change_5y(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    """5y change in (revenue / sgna) — productivity (revenue per opex dollar) trajectory."""
    return _safe_div(revenue, sgna).diff(DDAYS_5Y)


# ============================================================
#                        REGISTRY
# ============================================================

COMPETITIVE_DISPLACEMENT_SIGNAL_BASE_REGISTRY_001_075 = {
    "f45_cdis_001_inventory_to_revenue_level": {"inputs": ["inventory", "revenue"], "func": f45_cdis_001_inventory_to_revenue_level},
    "f45_cdis_002_inventory_to_revenue_change_yoy": {"inputs": ["inventory", "revenue"], "func": f45_cdis_002_inventory_to_revenue_change_yoy},
    "f45_cdis_003_inventory_to_revenue_change_5y": {"inputs": ["inventory", "revenue"], "func": f45_cdis_003_inventory_to_revenue_change_5y},
    "f45_cdis_004_inventory_to_revenue_zscore_5y": {"inputs": ["inventory", "revenue"], "func": f45_cdis_004_inventory_to_revenue_zscore_5y},
    "f45_cdis_005_inventory_to_revenue_rise_streak": {"inputs": ["inventory", "revenue"], "func": f45_cdis_005_inventory_to_revenue_rise_streak},
    "f45_cdis_006_inventory_yoy_minus_revenue_yoy": {"inputs": ["inventory", "revenue"], "func": f45_cdis_006_inventory_yoy_minus_revenue_yoy},
    "f45_cdis_007_inventory_3y_minus_revenue_3y_growth": {"inputs": ["inventory", "revenue"], "func": f45_cdis_007_inventory_3y_minus_revenue_3y_growth},
    "f45_cdis_008_inventory_growth_above_revenue_count_8q": {"inputs": ["inventory", "revenue"], "func": f45_cdis_008_inventory_growth_above_revenue_count_8q},
    "f45_cdis_009_inventory_turnover_level": {"inputs": ["cor", "inventory"], "func": f45_cdis_009_inventory_turnover_level},
    "f45_cdis_010_inventory_turnover_change_5y": {"inputs": ["cor", "inventory"], "func": f45_cdis_010_inventory_turnover_change_5y},
    "f45_cdis_011_inventory_turnover_zscore_5y": {"inputs": ["cor", "inventory"], "func": f45_cdis_011_inventory_turnover_zscore_5y},
    "f45_cdis_012_inventory_to_assets_level": {"inputs": ["inventory", "assets"], "func": f45_cdis_012_inventory_to_assets_level},
    "f45_cdis_013_inventory_to_assets_change_5y": {"inputs": ["inventory", "assets"], "func": f45_cdis_013_inventory_to_assets_change_5y},
    "f45_cdis_014_ar_to_revenue_level": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_014_ar_to_revenue_level},
    "f45_cdis_015_ar_to_revenue_change_5y": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_015_ar_to_revenue_change_5y},
    "f45_cdis_016_ar_to_revenue_zscore_5y": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_016_ar_to_revenue_zscore_5y},
    "f45_cdis_017_ar_yoy_minus_revenue_yoy": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_017_ar_yoy_minus_revenue_yoy},
    "f45_cdis_018_ar_3y_minus_revenue_3y_growth": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_018_ar_3y_minus_revenue_3y_growth},
    "f45_cdis_019_ar_growth_above_revenue_count_8q": {"inputs": ["accountsreceivable", "revenue"], "func": f45_cdis_019_ar_growth_above_revenue_count_8q},
    "f45_cdis_020_ar_turnover_level": {"inputs": ["revenue", "accountsreceivable"], "func": f45_cdis_020_ar_turnover_level},
    "f45_cdis_021_ar_to_assets_level": {"inputs": ["accountsreceivable", "assets"], "func": f45_cdis_021_ar_to_assets_level},
    "f45_cdis_022_ar_to_assets_change_5y": {"inputs": ["accountsreceivable", "assets"], "func": f45_cdis_022_ar_to_assets_change_5y},
    "f45_cdis_023_ar_plus_inventory_to_revenue_level": {"inputs": ["accountsreceivable", "inventory", "revenue"], "func": f45_cdis_023_ar_plus_inventory_to_revenue_level},
    "f45_cdis_024_ar_plus_inventory_to_revenue_change_5y": {"inputs": ["accountsreceivable", "inventory", "revenue"], "func": f45_cdis_024_ar_plus_inventory_to_revenue_change_5y},
    "f45_cdis_025_ar_plus_inventory_growth_above_revenue_streak": {"inputs": ["accountsreceivable", "inventory", "revenue"], "func": f45_cdis_025_ar_plus_inventory_growth_above_revenue_streak},
    "f45_cdis_026_cash_to_revenue_change_5y": {"inputs": ["cashneq", "revenue"], "func": f45_cdis_026_cash_to_revenue_change_5y},
    "f45_cdis_027_cash_burn_pace_relative_to_revenue_yoy": {"inputs": ["cashneq", "revenue"], "func": f45_cdis_027_cash_burn_pace_relative_to_revenue_yoy},
    "f45_cdis_028_fcf_negative_streak": {"inputs": ["fcf"], "func": f45_cdis_028_fcf_negative_streak},
    "f45_cdis_029_fcf_negative_count_8q": {"inputs": ["fcf"], "func": f45_cdis_029_fcf_negative_count_8q},
    "f45_cdis_030_fcf_negative_count_20q": {"inputs": ["fcf"], "func": f45_cdis_030_fcf_negative_count_20q},
    "f45_cdis_031_cash_burn_acceleration_yoy": {"inputs": ["fcf"], "func": f45_cdis_031_cash_burn_acceleration_yoy},
    "f45_cdis_032_cash_burn_with_revenue_growth_indicator": {"inputs": ["fcf", "revenue"], "func": f45_cdis_032_cash_burn_with_revenue_growth_indicator},
    "f45_cdis_033_cash_burn_with_revenue_decel_indicator": {"inputs": ["fcf", "revenue"], "func": f45_cdis_033_cash_burn_with_revenue_decel_indicator},
    "f45_cdis_034_fcf_to_revenue_below_neg5pct_count_8q": {"inputs": ["fcf", "revenue"], "func": f45_cdis_034_fcf_to_revenue_below_neg5pct_count_8q},
    "f45_cdis_035_fcf_to_revenue_below_neg10pct_count_8q": {"inputs": ["fcf", "revenue"], "func": f45_cdis_035_fcf_to_revenue_below_neg10pct_count_8q},
    "f45_cdis_036_ncfo_negative_streak": {"inputs": ["ncfo"], "func": f45_cdis_036_ncfo_negative_streak},
    "f45_cdis_037_ncfo_yoy_decline_streak": {"inputs": ["ncfo"], "func": f45_cdis_037_ncfo_yoy_decline_streak},
    "f45_cdis_038_cash_burn_runway_proxy": {"inputs": ["cashneq", "fcf"], "func": f45_cdis_038_cash_burn_runway_proxy},
    "f45_cdis_039_cash_burn_runway_change_yoy": {"inputs": ["cashneq", "fcf"], "func": f45_cdis_039_cash_burn_runway_change_yoy},
    "f45_cdis_040_cash_burn_runway_zscore_5y": {"inputs": ["cashneq", "fcf"], "func": f45_cdis_040_cash_burn_runway_zscore_5y},
    "f45_cdis_041_cashneq_yoy_change_log": {"inputs": ["cashneq"], "func": f45_cdis_041_cashneq_yoy_change_log},
    "f45_cdis_042_cashneq_5y_change_log": {"inputs": ["cashneq"], "func": f45_cdis_042_cashneq_5y_change_log},
    "f45_cdis_043_cashneq_decline_streak": {"inputs": ["cashneq"], "func": f45_cdis_043_cashneq_decline_streak},
    "f45_cdis_044_cashneq_below_5y_min_indicator": {"inputs": ["cashneq"], "func": f45_cdis_044_cashneq_below_5y_min_indicator},
    "f45_cdis_045_cash_pressure_composite_score_8q": {"inputs": ["cashneq", "fcf", "revenue"], "func": f45_cdis_045_cash_pressure_composite_score_8q},
    "f45_cdis_046_revenue_volatility_yoy_8q": {"inputs": ["revenue"], "func": f45_cdis_046_revenue_volatility_yoy_8q},
    "f45_cdis_047_revenue_volatility_qoq_8q": {"inputs": ["revenue"], "func": f45_cdis_047_revenue_volatility_qoq_8q},
    "f45_cdis_048_revenue_volatility_zscore_5y": {"inputs": ["revenue"], "func": f45_cdis_048_revenue_volatility_zscore_5y},
    "f45_cdis_049_revenue_qoq_kurtosis_8q": {"inputs": ["revenue"], "func": f45_cdis_049_revenue_qoq_kurtosis_8q},
    "f45_cdis_050_revenue_qoq_skewness_8q": {"inputs": ["revenue"], "func": f45_cdis_050_revenue_qoq_skewness_8q},
    "f45_cdis_051_revenue_dispersion_yoy_5y": {"inputs": ["revenue"], "func": f45_cdis_051_revenue_dispersion_yoy_5y},
    "f45_cdis_052_revenue_max_qoq_drop_5y": {"inputs": ["revenue"], "func": f45_cdis_052_revenue_max_qoq_drop_5y},
    "f45_cdis_053_revenue_max_yoy_drop_5y": {"inputs": ["revenue"], "func": f45_cdis_053_revenue_max_yoy_drop_5y},
    "f45_cdis_054_revenue_drop_intensity_above_p95_count_5y": {"inputs": ["revenue"], "func": f45_cdis_054_revenue_drop_intensity_above_p95_count_5y},
    "f45_cdis_055_revenue_post_drop_recovery_proxy_5y": {"inputs": ["revenue"], "func": f45_cdis_055_revenue_post_drop_recovery_proxy_5y},
    "f45_cdis_056_revenue_step_change_indicator_8q": {"inputs": ["revenue"], "func": f45_cdis_056_revenue_step_change_indicator_8q},
    "f45_cdis_057_revenue_jump_count_negative_8q": {"inputs": ["revenue"], "func": f45_cdis_057_revenue_jump_count_negative_8q},
    "f45_cdis_058_revenue_outlier_count_5y": {"inputs": ["revenue"], "func": f45_cdis_058_revenue_outlier_count_5y},
    "f45_cdis_059_revenue_growth_below_mean_persistence_8q": {"inputs": ["revenue"], "func": f45_cdis_059_revenue_growth_below_mean_persistence_8q},
    "f45_cdis_060_revenue_growth_persistence_below_zero_8q": {"inputs": ["revenue"], "func": f45_cdis_060_revenue_growth_persistence_below_zero_8q},
    "f45_cdis_061_revenue_above_trend_streak": {"inputs": ["revenue"], "func": f45_cdis_061_revenue_above_trend_streak},
    "f45_cdis_062_revenue_below_trend_streak": {"inputs": ["revenue"], "func": f45_cdis_062_revenue_below_trend_streak},
    "f45_cdis_063_revenue_trend_break_recency_5y": {"inputs": ["revenue"], "func": f45_cdis_063_revenue_trend_break_recency_5y},
    "f45_cdis_064_revenue_smoothed_trend_slope_8q_vs_20q": {"inputs": ["revenue"], "func": f45_cdis_064_revenue_smoothed_trend_slope_8q_vs_20q},
    "f45_cdis_065_revenue_acceleration_breakdown_4q": {"inputs": ["revenue"], "func": f45_cdis_065_revenue_acceleration_breakdown_4q},
    "f45_cdis_066_revenue_qoq_zero_or_negative_count_8q": {"inputs": ["revenue"], "func": f45_cdis_066_revenue_qoq_zero_or_negative_count_8q},
    "f45_cdis_067_revenue_persistent_negativity_8q_streak": {"inputs": ["revenue"], "func": f45_cdis_067_revenue_persistent_negativity_8q_streak},
    "f45_cdis_068_revenue_below_lt_average_count_8q": {"inputs": ["revenue"], "func": f45_cdis_068_revenue_below_lt_average_count_8q},
    "f45_cdis_069_revenue_step_function_collapse_indicator": {"inputs": ["revenue"], "func": f45_cdis_069_revenue_step_function_collapse_indicator},
    "f45_cdis_070_revenue_discontinuity_score_5y": {"inputs": ["revenue"], "func": f45_cdis_070_revenue_discontinuity_score_5y},
    "f45_cdis_071_revenue_per_share_change_5y": {"inputs": ["revenue", "shareswadil"], "func": f45_cdis_071_revenue_per_share_change_5y},
    "f45_cdis_072_revenue_per_share_decline_streak": {"inputs": ["revenue", "shareswadil"], "func": f45_cdis_072_revenue_per_share_decline_streak},
    "f45_cdis_073_revenue_per_unit_inventory_change_5y": {"inputs": ["revenue", "inventory"], "func": f45_cdis_073_revenue_per_unit_inventory_change_5y},
    "f45_cdis_074_revenue_per_unit_inventory_zscore_5y": {"inputs": ["revenue", "inventory"], "func": f45_cdis_074_revenue_per_unit_inventory_zscore_5y},
    "f45_cdis_075_revenue_per_dollar_of_sgna_change_5y": {"inputs": ["revenue", "sgna"], "func": f45_cdis_075_revenue_per_dollar_of_sgna_change_5y},
}
