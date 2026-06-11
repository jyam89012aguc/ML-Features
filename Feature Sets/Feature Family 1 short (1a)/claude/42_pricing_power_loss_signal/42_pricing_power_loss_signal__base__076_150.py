"""pricing_power_loss_signal base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py for 150 total. Same lane, same conventions:
SF1 quarterly fundamentals only; PIT-clean rolling; explicit min_periods; no centered windows.
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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lo=0.01, hi=0.99):
    if not isinstance(s, pd.Series):
        return s
    q_lo = s.quantile(lo)
    q_hi = s.quantile(hi)
    return s.clip(lower=q_lo, upper=q_hi)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _quarters_since_max(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _qsm(w):
        if np.all(np.isnan(w)):
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return s.rolling(n, min_periods=min_periods).apply(_qsm, raw=True)


def _pct_rank(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _pr(w):
        if np.all(np.isnan(w)):
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        valid = w[~np.isnan(w)]
        if len(valid) < 2:
            return np.nan
        return (valid <= last).sum() / len(valid)
    return s.rolling(n, min_periods=min_periods).apply(_pr, raw=True)


def _autocorr_lag1(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 3)
    def _ac(w):
        if np.isnan(w).any():
            valid = ~np.isnan(w)
            if valid.sum() < min_periods:
                return np.nan
            wv = w[valid]
        else:
            wv = w
        if len(wv) < 3:
            return np.nan
        a = wv[:-1]; b = wv[1:]
        am = a.mean(); bm = b.mean()
        num = ((a - am) * (b - bm)).sum()
        da = ((a - am) ** 2).sum()
        db = ((b - bm) ** 2).sum()
        den = np.sqrt(da * db)
        if den == 0 or np.isnan(den):
            return np.nan
        return num / den
    return s.rolling(n, min_periods=min_periods).apply(_ac, raw=True)


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


# ============================================================
#                    FEATURES 076-150
# ============================================================

# ---- Block N (cont): GM z-score vs own history (076-080) ----

def f42_pplo_076_gm_zscore_12q(revenue, gp):
    """GM z-score vs 12Q — medium regime."""
    return _rolling_zscore(_safe_div(gp, revenue), 12, min_periods=4)


def f42_pplo_077_gm_zscore_16q(revenue, gp):
    """GM z-score vs 16Q — multi-year regime."""
    return _rolling_zscore(_safe_div(gp, revenue), 16, min_periods=5)


def f42_pplo_078_gm_ttm_zscore_8q(revenue, gp):
    """GM_ttm z-score vs 8Q."""
    return _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 8, min_periods=3)


def f42_pplo_079_gm_ttm_zscore_12q(revenue, gp):
    """GM_ttm z-score vs 12Q."""
    return _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 12, min_periods=4)


def f42_pplo_080_gm_ttm_zscore_16q(revenue, gp):
    """GM_ttm z-score vs 16Q."""
    return _rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)


# ---- Block O: Margin variance over rolling windows (081-086) ----

def f42_pplo_081_cv_gm_4q(revenue, gp):
    """CV of GM over 4Q."""
    gm = _safe_div(gp, revenue)
    m = gm.rolling(4, min_periods=2).mean()
    sd = gm.rolling(4, min_periods=2).std()
    return _safe_div(sd, m.abs())


def f42_pplo_082_cv_gm_12q(revenue, gp):
    """CV of GM over 12Q."""
    gm = _safe_div(gp, revenue)
    m = gm.rolling(12, min_periods=4).mean()
    sd = gm.rolling(12, min_periods=4).std()
    return _safe_div(sd, m.abs())


def f42_pplo_083_cv_ebitm_8q(revenue, ebit):
    """CV of EBIT margin over 8Q."""
    em = _safe_div(ebit, revenue)
    m = em.rolling(8, min_periods=3).mean()
    sd = em.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs())


def f42_pplo_084_cv_ebitm_12q(revenue, ebit):
    """CV of EBIT margin over 12Q."""
    em = _safe_div(ebit, revenue)
    m = em.rolling(12, min_periods=4).mean()
    sd = em.rolling(12, min_periods=4).std()
    return _safe_div(sd, m.abs())


def f42_pplo_085_std_om_8q(revenue, ebit):
    """Std of operating margin (EBIT/rev) over 8Q."""
    return _safe_div(ebit, revenue).rolling(8, min_periods=3).std()


def f42_pplo_086_std_om_12q(revenue, ebit):
    """Std of operating margin (EBIT/rev) over 12Q."""
    return _safe_div(ebit, revenue).rolling(12, min_periods=4).std()


# ---- Block P: Pricing-power degradation composites (087-094) ----

def f42_pplo_087_composite_gm_compress_plus_ar_bloat(revenue, gp, receivables):
    """(-GM_compression_4q) + (AR/rev_ttm yoy change). Higher = worse."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar_ratio = _safe_div(receivables, _ttm(revenue))
    return gm_compress + ar_ratio.diff(4)


def f42_pplo_088_composite_gm_compress_plus_inv_bloat(revenue, gp, inventory):
    """(-GM_compression_4q) + (inventory/rev_ttm yoy change)."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    inv_ratio = _safe_div(inventory, _ttm(revenue))
    return gm_compress + inv_ratio.diff(4)


def f42_pplo_089_composite_gm_compress_plus_defrev_decline(revenue, gp, deferredrev):
    """(-GM_compression_4q) + (-DefRev/rev_ttm yoy change)."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    def_ratio = _safe_div(deferredrev, _ttm(revenue))
    return gm_compress + (-def_ratio.diff(4))


def f42_pplo_090_composite_full(revenue, gp, receivables, inventory, deferredrev):
    """Full composite: GM compression + AR bloat + inv bloat + (-DefRev change)."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return gm_compress + ar + iv + dr


def f42_pplo_091_composite_normalized_zscore_8q(revenue, gp, receivables, inventory):
    """Z-score (8Q) of (GM_compression + AR_bloat + inv_bloat)."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    comp = gm_compress + ar + iv
    return _rolling_zscore(comp, 8, min_periods=3)


def f42_pplo_092_composite_full_yoy_change(revenue, gp, receivables, inventory, deferredrev):
    """YoY change in full composite — acceleration of pricing-power loss."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return (gm_compress + ar + iv + dr).diff(4)


def f42_pplo_093_composite_full_8q_avg(revenue, gp, receivables, inventory, deferredrev):
    """8Q moving average of full composite — persistent signal."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return (gm_compress + ar + iv + dr).rolling(8, min_periods=3).mean()


def f42_pplo_094_composite_with_dso(revenue, gp, receivables, inventory):
    """Composite using DSO yoy change instead of AR/rev change."""
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    return gm_compress + dso.diff(4) / 365.0 + iv


# ---- Block Q: Revenue quality (cash vs AR/inv) (095-100) ----

def f42_pplo_095_rev_growth_fueled_by_ar(revenue, receivables):
    """ΔAR / ΔRevenue — share of revenue growth that became receivables."""
    return _safe_div(receivables.diff(), revenue.diff())


def f42_pplo_096_rev_growth_fueled_by_inv(revenue, inventory):
    """ΔInventory / ΔRevenue — buildup ratio."""
    return _safe_div(inventory.diff(), revenue.diff())


def f42_pplo_097_rev_cash_collection_quality(revenue, ncfo):
    """NCFO / revenue — cash-conversion of top line."""
    return _safe_div(ncfo, revenue)


def f42_pplo_098_rev_cash_collection_yoy_change(revenue, ncfo):
    """YoY change in NCFO/revenue."""
    return _safe_div(ncfo, revenue).diff(4)


def f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth(revenue, ncfo):
    """Revenue YoY growth − NCFO YoY growth — pricing-power vs cash divergence."""
    return _yoy_pct(revenue) - _yoy_pct(ncfo)


def f42_pplo_100_cash_conversion_efficiency(gp, ncfo):
    """NCFO / GP — cash conversion of gross profit."""
    return _safe_div(ncfo, gp)


# ---- Block R: COGS regime indicators (101-104) ----

def f42_pplo_101_cogs_to_rev_above_p80_12q(revenue, cor):
    """Indicator: COGS/rev currently above its 12Q 80th percentile."""
    r = _safe_div(cor, revenue)
    p80 = r.rolling(12, min_periods=4).quantile(0.80)
    return (r > p80).astype(float).where(r.notna() & p80.notna())


def f42_pplo_102_cogs_to_rev_above_p80_16q(revenue, cor):
    """Indicator: COGS/rev currently above its 16Q 80th percentile."""
    r = _safe_div(cor, revenue)
    p80 = r.rolling(16, min_periods=5).quantile(0.80)
    return (r > p80).astype(float).where(r.notna() & p80.notna())


def f42_pplo_103_cogs_to_rev_pct_rank_12q(revenue, cor):
    """COGS/rev percentile rank vs 12Q history."""
    return _pct_rank(_safe_div(cor, revenue), 12, min_periods=4)


def f42_pplo_104_cogs_to_rev_pct_rank_16q(revenue, cor):
    """COGS/rev percentile rank vs 16Q history."""
    return _pct_rank(_safe_div(cor, revenue), 16, min_periods=5)


# ---- Block S: GM persistence — autocorr (105-108) ----

def f42_pplo_105_gm_diff_autocorr_lag1_8q(revenue, gp):
    """Lag-1 autocorr of GM diffs over 8Q — persistence of change direction."""
    return _autocorr_lag1(_safe_div(gp, revenue).diff(), 8, min_periods=4)


def f42_pplo_106_gm_diff_autocorr_lag1_12q(revenue, gp):
    """Lag-1 autocorr of GM diffs over 12Q."""
    return _autocorr_lag1(_safe_div(gp, revenue).diff(), 12, min_periods=5)


def f42_pplo_107_gm_level_autocorr_lag1_8q(revenue, gp):
    """Lag-1 autocorr of GM level over 8Q — stickiness."""
    return _autocorr_lag1(_safe_div(gp, revenue), 8, min_periods=4)


def f42_pplo_108_gm_level_autocorr_lag1_12q(revenue, gp):
    """Lag-1 autocorr of GM level over 12Q."""
    return _autocorr_lag1(_safe_div(gp, revenue), 12, min_periods=5)


# ---- Block T: GM rank percentile vs own history (109-112) ----

def f42_pplo_109_gm_pct_rank_8q(revenue, gp):
    """GM percentile rank vs 8Q."""
    return _pct_rank(_safe_div(gp, revenue), 8, min_periods=3)


def f42_pplo_110_gm_pct_rank_12q(revenue, gp):
    """GM percentile rank vs 12Q."""
    return _pct_rank(_safe_div(gp, revenue), 12, min_periods=4)


def f42_pplo_111_gm_pct_rank_16q(revenue, gp):
    """GM percentile rank vs 16Q."""
    return _pct_rank(_safe_div(gp, revenue), 16, min_periods=5)


def f42_pplo_112_gm_ttm_pct_rank_16q(revenue, gp):
    """GM_ttm percentile rank vs 16Q."""
    return _pct_rank(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)


# ---- Block U: Quarters since GM max (113-116) ----

def f42_pplo_113_quarters_since_gm_max_8q(revenue, gp):
    """Quarters since GM max in trailing 8Q — recency of pricing-power peak."""
    return _quarters_since_max(_safe_div(gp, revenue), 8, min_periods=3)


def f42_pplo_114_quarters_since_gm_max_12q(revenue, gp):
    """Quarters since GM max in trailing 12Q."""
    return _quarters_since_max(_safe_div(gp, revenue), 12, min_periods=4)


def f42_pplo_115_quarters_since_gm_max_16q(revenue, gp):
    """Quarters since GM max in trailing 16Q."""
    return _quarters_since_max(_safe_div(gp, revenue), 16, min_periods=5)


def f42_pplo_116_quarters_since_gm_ttm_max_16q(revenue, gp):
    """Quarters since GM_ttm max over 16Q."""
    return _quarters_since_max(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)


# ---- Block V: Negative pricing-power flags (117-122) ----

def f42_pplo_117_flag_gm_down_and_ar_up_yoy(revenue, gp, receivables):
    """Flag: GM falling YoY AND AR/rev rising YoY."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    return ((gm.diff(4) < 0) & (ar.diff(4) > 0)).astype(float)


def f42_pplo_118_flag_gm_down_and_inv_up_yoy(revenue, gp, inventory):
    """Flag: GM falling YoY AND inventory/rev rising YoY."""
    gm = _safe_div(gp, revenue)
    iv = _safe_div(inventory, _ttm(revenue))
    return ((gm.diff(4) < 0) & (iv.diff(4) > 0)).astype(float)


def f42_pplo_119_flag_gm_down_and_defrev_down_yoy(revenue, gp, deferredrev):
    """Flag: GM falling YoY AND DefRev/rev falling YoY."""
    gm = _safe_div(gp, revenue)
    dr = _safe_div(deferredrev, _ttm(revenue))
    return ((gm.diff(4) < 0) & (dr.diff(4) < 0)).astype(float)


def f42_pplo_120_flag_gm_down_and_dso_up(revenue, gp, receivables):
    """Flag: GM falling YoY AND DSO rising YoY."""
    gm = _safe_div(gp, revenue)
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    return ((gm.diff(4) < 0) & (dso.diff(4) > 0)).astype(float)


def f42_pplo_121_flag_gm_down_and_dio_up(revenue, gp, cor, inventory):
    """Flag: GM falling YoY AND DIO rising YoY."""
    _ = revenue
    gm = _safe_div(gp, revenue)
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return ((gm.diff(4) < 0) & (dio.diff(4) > 0)).astype(float)


def f42_pplo_122_gm_falling_4q_streak(revenue, gp):
    """Length of current consecutive-quarters-of-GM-decline streak."""
    gm = _safe_div(gp, revenue)
    decl = (gm.diff() < 0).astype(float)
    grp = (decl == 0).cumsum()
    return decl.groupby(grp).cumsum()


# ---- Block W: GM-EBITmargin spread (123-126) ----

def f42_pplo_123_gm_minus_ebitm(revenue, gp, ebit):
    """GM − EBITmargin — SGA/opex consumption of gross profit."""
    return _safe_div(gp, revenue) - _safe_div(ebit, revenue)


def f42_pplo_124_gm_minus_ebitm_yoy_change(revenue, gp, ebit):
    """YoY change in (GM − EBITmargin)."""
    return (_safe_div(gp, revenue) - _safe_div(ebit, revenue)).diff(4)


def f42_pplo_125_gm_minus_ebitm_2y_change(revenue, gp, ebit):
    """2y change in (GM − EBITmargin)."""
    return (_safe_div(gp, revenue) - _safe_div(ebit, revenue)).diff(8)


def f42_pplo_126_gm_minus_ebitm_slope_8q(revenue, gp, ebit):
    """8Q slope of (GM − EBITmargin)."""
    return _rolling_slope(_safe_div(gp, revenue) - _safe_div(ebit, revenue), 8, min_periods=3)


# ---- Block X: SBC-burden adjustment (127-130) ----

def f42_pplo_127_gm_minus_sbc_to_rev(revenue, gp, sbcomp):
    """GM − SBC/revenue — effective gross margin after stock-based comp."""
    return _safe_div(gp, revenue) - _safe_div(sbcomp, revenue)


def f42_pplo_128_gm_minus_sbc_to_rev_yoy(revenue, gp, sbcomp):
    """YoY change in effective GM after SBC."""
    return (_safe_div(gp, revenue) - _safe_div(sbcomp, revenue)).diff(4)


def f42_pplo_129_sbc_to_rev_yoy_change(revenue, sbcomp):
    """YoY change in SBC/revenue — rising SBC burden."""
    return _safe_div(sbcomp, revenue).diff(4)


def f42_pplo_130_effective_gm_after_sbc_zscore_12q(revenue, gp, sbcomp):
    """Z-score (12Q) of (GM − SBC/rev)."""
    return _rolling_zscore(_safe_div(gp, revenue) - _safe_div(sbcomp, revenue), 12, min_periods=4)


# ---- Block Y: Pricing-power composite scores (131-136) ----

def f42_pplo_131_composite_v1(revenue, gp, receivables, cor, inventory):
    """(-GM_yoy_change) + (AR/rev yoy change) + (DIO yoy change)."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0


def f42_pplo_132_composite_v2_zscore(revenue, gp, receivables, inventory):
    """(-GM_zscore_12q) + (AR/rev_zscore_12q) + (inv/rev_zscore_12q)."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    iv = _safe_div(inventory, _ttm(revenue))
    return (-_rolling_zscore(gm, 12, 4)) + _rolling_zscore(ar, 12, 4) + _rolling_zscore(iv, 12, 4)


def f42_pplo_133_composite_signal_count(revenue, gp, receivables, cor, inventory, deferredrev):
    """Count of negative-pricing-power signals firing (out of 6 binary tests)."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    iv = _safe_div(inventory, _ttm(revenue))
    dr = _safe_div(deferredrev, _ttm(revenue))
    f1 = (gm.diff(4) < 0).astype(float)
    f2 = (ar.diff(4) > 0).astype(float)
    f3 = (dso.diff(4) > 0).astype(float)
    f4 = (dio.diff(4) > 0).astype(float)
    f5 = (iv.diff(4) > 0).astype(float)
    f6 = (dr.diff(4) < 0).astype(float)
    return f1 + f2 + f3 + f4 + f5 + f6


def f42_pplo_134_composite_v1_yoy_delta(revenue, gp, receivables, cor, inventory):
    """YoY change in composite_v1 — acceleration of pricing-power loss."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    return comp.diff(4)


def f42_pplo_135_composite_v1_normalized(revenue, gp, receivables, cor, inventory):
    """composite_v1 / std(composite_v1, 12Q)."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    sd = comp.rolling(12, min_periods=4).std()
    return _safe_div(comp, sd)


def f42_pplo_136_composite_extreme_quintile_flag(revenue, gp, receivables, cor, inventory):
    """Flag: composite_v1 in top quintile of its 16Q history."""
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    p80 = comp.rolling(16, min_periods=5).quantile(0.80)
    return (comp > p80).astype(float).where(comp.notna() & p80.notna())


# ---- Block Z: Pricing-power lane fillers (137-150) ----

def f42_pplo_137_gp_to_assets(gp, assets):
    """Gross profitability ratio (Novy-Marx) — gp / assets."""
    return _safe_div(gp, assets)


def f42_pplo_138_gp_to_assets_yoy_change(gp, assets):
    """YoY change in gp/assets."""
    return _safe_div(gp, assets).diff(4)


def f42_pplo_139_gp_to_assets_zscore_12q(gp, assets):
    """Z-score (12Q) of gp/assets."""
    return _rolling_zscore(_safe_div(gp, assets), 12, min_periods=4)


def f42_pplo_140_gp_to_tangible_assets(gp, assets, intangibles):
    """gp / (assets − intangibles) — tangible-asset gross profitability."""
    return _safe_div(gp, assets - intangibles)


def f42_pplo_141_gp_to_invested_capital_proxy(gp, assets, payables):
    """gp / (assets − payables) — proxy for return on invested capital from GP."""
    return _safe_div(gp, assets - payables)


def f42_pplo_142_revenue_per_ppne(revenue, ppnenet):
    """revenue / net PP&E — asset productivity / pricing-power dependency."""
    return _safe_div(revenue, ppnenet)


def f42_pplo_143_revenue_per_ppne_yoy_change(revenue, ppnenet):
    """YoY change in revenue / PP&E."""
    return _safe_div(revenue, ppnenet).diff(4)


def f42_pplo_144_payables_to_cogs(cor, payables):
    """payables / COGS_ttm — supplier-credit days proxy."""
    return _safe_div(payables, _ttm(cor))


def f42_pplo_145_payables_to_cogs_yoy_change(cor, payables):
    """YoY change in payables/COGS_ttm — stretching suppliers."""
    return _safe_div(payables, _ttm(cor)).diff(4)


def f42_pplo_146_payables_growth_minus_cogs_growth_yoy(cor, payables):
    """Payables YoY growth − COGS YoY growth — credit grab vs underlying."""
    return _yoy_pct(payables) - _yoy_pct(cor)


def f42_pplo_147_cash_gm_proxy(revenue, ncfo, receivables, inventory, payables):
    """(NCFO − ΔAR − ΔInv + ΔPayables) / revenue — cash-based GM proxy."""
    num = ncfo - receivables.diff() - inventory.diff() + payables.diff()
    return _safe_div(num, revenue)


def f42_pplo_148_cash_gm_proxy_yoy_change(revenue, ncfo, receivables, inventory, payables):
    """YoY change in cash-based GM proxy."""
    num = ncfo - receivables.diff() - inventory.diff() + payables.diff()
    return _safe_div(num, revenue).diff(4)


def f42_pplo_149_gm_times_rev_growth(revenue, gp):
    """GM × revenue YoY growth — pricing-power preservation amid growth."""
    return _safe_div(gp, revenue) * _yoy_pct(revenue)


def f42_pplo_150_pricing_power_quality_index(revenue, gp, receivables, cor, inventory):
    """Composite: 0.4*GM_z − 0.3*DSO_z − 0.3*DIO_z (12Q)."""
    gm = _safe_div(gp, revenue)
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return (0.4 * _rolling_zscore(gm, 12, 4)
            - 0.3 * _rolling_zscore(dso, 12, 4)
            - 0.3 * _rolling_zscore(dio, 12, 4))


# ============================================================
#                        REGISTRY
# ============================================================

PRICING_POWER_LOSS_SIGNAL_BASE_REGISTRY_076_150 = {
    "f42_pplo_076_gm_zscore_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_076_gm_zscore_12q},
    "f42_pplo_077_gm_zscore_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_077_gm_zscore_16q},
    "f42_pplo_078_gm_ttm_zscore_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_078_gm_ttm_zscore_8q},
    "f42_pplo_079_gm_ttm_zscore_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_079_gm_ttm_zscore_12q},
    "f42_pplo_080_gm_ttm_zscore_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_080_gm_ttm_zscore_16q},
    "f42_pplo_081_cv_gm_4q": {"inputs": ["revenue", "gp"], "func": f42_pplo_081_cv_gm_4q},
    "f42_pplo_082_cv_gm_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_082_cv_gm_12q},
    "f42_pplo_083_cv_ebitm_8q": {"inputs": ["revenue", "ebit"], "func": f42_pplo_083_cv_ebitm_8q},
    "f42_pplo_084_cv_ebitm_12q": {"inputs": ["revenue", "ebit"], "func": f42_pplo_084_cv_ebitm_12q},
    "f42_pplo_085_std_om_8q": {"inputs": ["revenue", "ebit"], "func": f42_pplo_085_std_om_8q},
    "f42_pplo_086_std_om_12q": {"inputs": ["revenue", "ebit"], "func": f42_pplo_086_std_om_12q},
    "f42_pplo_087_composite_gm_compress_plus_ar_bloat": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_087_composite_gm_compress_plus_ar_bloat},
    "f42_pplo_088_composite_gm_compress_plus_inv_bloat": {"inputs": ["revenue", "gp", "inventory"], "func": f42_pplo_088_composite_gm_compress_plus_inv_bloat},
    "f42_pplo_089_composite_gm_compress_plus_defrev_decline": {"inputs": ["revenue", "gp", "deferredrev"], "func": f42_pplo_089_composite_gm_compress_plus_defrev_decline},
    "f42_pplo_090_composite_full": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_090_composite_full},
    "f42_pplo_091_composite_normalized_zscore_8q": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_091_composite_normalized_zscore_8q},
    "f42_pplo_092_composite_full_yoy_change": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_092_composite_full_yoy_change},
    "f42_pplo_093_composite_full_8q_avg": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_093_composite_full_8q_avg},
    "f42_pplo_094_composite_with_dso": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_094_composite_with_dso},
    "f42_pplo_095_rev_growth_fueled_by_ar": {"inputs": ["revenue", "receivables"], "func": f42_pplo_095_rev_growth_fueled_by_ar},
    "f42_pplo_096_rev_growth_fueled_by_inv": {"inputs": ["revenue", "inventory"], "func": f42_pplo_096_rev_growth_fueled_by_inv},
    "f42_pplo_097_rev_cash_collection_quality": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_097_rev_cash_collection_quality},
    "f42_pplo_098_rev_cash_collection_yoy_change": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_098_rev_cash_collection_yoy_change},
    "f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth},
    "f42_pplo_100_cash_conversion_efficiency": {"inputs": ["gp", "ncfo"], "func": f42_pplo_100_cash_conversion_efficiency},
    "f42_pplo_101_cogs_to_rev_above_p80_12q": {"inputs": ["revenue", "cor"], "func": f42_pplo_101_cogs_to_rev_above_p80_12q},
    "f42_pplo_102_cogs_to_rev_above_p80_16q": {"inputs": ["revenue", "cor"], "func": f42_pplo_102_cogs_to_rev_above_p80_16q},
    "f42_pplo_103_cogs_to_rev_pct_rank_12q": {"inputs": ["revenue", "cor"], "func": f42_pplo_103_cogs_to_rev_pct_rank_12q},
    "f42_pplo_104_cogs_to_rev_pct_rank_16q": {"inputs": ["revenue", "cor"], "func": f42_pplo_104_cogs_to_rev_pct_rank_16q},
    "f42_pplo_105_gm_diff_autocorr_lag1_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_105_gm_diff_autocorr_lag1_8q},
    "f42_pplo_106_gm_diff_autocorr_lag1_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_106_gm_diff_autocorr_lag1_12q},
    "f42_pplo_107_gm_level_autocorr_lag1_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_107_gm_level_autocorr_lag1_8q},
    "f42_pplo_108_gm_level_autocorr_lag1_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_108_gm_level_autocorr_lag1_12q},
    "f42_pplo_109_gm_pct_rank_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_109_gm_pct_rank_8q},
    "f42_pplo_110_gm_pct_rank_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_110_gm_pct_rank_12q},
    "f42_pplo_111_gm_pct_rank_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_111_gm_pct_rank_16q},
    "f42_pplo_112_gm_ttm_pct_rank_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_112_gm_ttm_pct_rank_16q},
    "f42_pplo_113_quarters_since_gm_max_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_113_quarters_since_gm_max_8q},
    "f42_pplo_114_quarters_since_gm_max_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_114_quarters_since_gm_max_12q},
    "f42_pplo_115_quarters_since_gm_max_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_115_quarters_since_gm_max_16q},
    "f42_pplo_116_quarters_since_gm_ttm_max_16q": {"inputs": ["revenue", "gp"], "func": f42_pplo_116_quarters_since_gm_ttm_max_16q},
    "f42_pplo_117_flag_gm_down_and_ar_up_yoy": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_117_flag_gm_down_and_ar_up_yoy},
    "f42_pplo_118_flag_gm_down_and_inv_up_yoy": {"inputs": ["revenue", "gp", "inventory"], "func": f42_pplo_118_flag_gm_down_and_inv_up_yoy},
    "f42_pplo_119_flag_gm_down_and_defrev_down_yoy": {"inputs": ["revenue", "gp", "deferredrev"], "func": f42_pplo_119_flag_gm_down_and_defrev_down_yoy},
    "f42_pplo_120_flag_gm_down_and_dso_up": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_120_flag_gm_down_and_dso_up},
    "f42_pplo_121_flag_gm_down_and_dio_up": {"inputs": ["revenue", "gp", "cor", "inventory"], "func": f42_pplo_121_flag_gm_down_and_dio_up},
    "f42_pplo_122_gm_falling_4q_streak": {"inputs": ["revenue", "gp"], "func": f42_pplo_122_gm_falling_4q_streak},
    "f42_pplo_123_gm_minus_ebitm": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_123_gm_minus_ebitm},
    "f42_pplo_124_gm_minus_ebitm_yoy_change": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_124_gm_minus_ebitm_yoy_change},
    "f42_pplo_125_gm_minus_ebitm_2y_change": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_125_gm_minus_ebitm_2y_change},
    "f42_pplo_126_gm_minus_ebitm_slope_8q": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_126_gm_minus_ebitm_slope_8q},
    "f42_pplo_127_gm_minus_sbc_to_rev": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_127_gm_minus_sbc_to_rev},
    "f42_pplo_128_gm_minus_sbc_to_rev_yoy": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_128_gm_minus_sbc_to_rev_yoy},
    "f42_pplo_129_sbc_to_rev_yoy_change": {"inputs": ["revenue", "sbcomp"], "func": f42_pplo_129_sbc_to_rev_yoy_change},
    "f42_pplo_130_effective_gm_after_sbc_zscore_12q": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_130_effective_gm_after_sbc_zscore_12q},
    "f42_pplo_131_composite_v1": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_131_composite_v1},
    "f42_pplo_132_composite_v2_zscore": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_132_composite_v2_zscore},
    "f42_pplo_133_composite_signal_count": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory", "deferredrev"], "func": f42_pplo_133_composite_signal_count},
    "f42_pplo_134_composite_v1_yoy_delta": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_134_composite_v1_yoy_delta},
    "f42_pplo_135_composite_v1_normalized": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_135_composite_v1_normalized},
    "f42_pplo_136_composite_extreme_quintile_flag": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_136_composite_extreme_quintile_flag},
    "f42_pplo_137_gp_to_assets": {"inputs": ["gp", "assets"], "func": f42_pplo_137_gp_to_assets},
    "f42_pplo_138_gp_to_assets_yoy_change": {"inputs": ["gp", "assets"], "func": f42_pplo_138_gp_to_assets_yoy_change},
    "f42_pplo_139_gp_to_assets_zscore_12q": {"inputs": ["gp", "assets"], "func": f42_pplo_139_gp_to_assets_zscore_12q},
    "f42_pplo_140_gp_to_tangible_assets": {"inputs": ["gp", "assets", "intangibles"], "func": f42_pplo_140_gp_to_tangible_assets},
    "f42_pplo_141_gp_to_invested_capital_proxy": {"inputs": ["gp", "assets", "payables"], "func": f42_pplo_141_gp_to_invested_capital_proxy},
    "f42_pplo_142_revenue_per_ppne": {"inputs": ["revenue", "ppnenet"], "func": f42_pplo_142_revenue_per_ppne},
    "f42_pplo_143_revenue_per_ppne_yoy_change": {"inputs": ["revenue", "ppnenet"], "func": f42_pplo_143_revenue_per_ppne_yoy_change},
    "f42_pplo_144_payables_to_cogs": {"inputs": ["cor", "payables"], "func": f42_pplo_144_payables_to_cogs},
    "f42_pplo_145_payables_to_cogs_yoy_change": {"inputs": ["cor", "payables"], "func": f42_pplo_145_payables_to_cogs_yoy_change},
    "f42_pplo_146_payables_growth_minus_cogs_growth_yoy": {"inputs": ["cor", "payables"], "func": f42_pplo_146_payables_growth_minus_cogs_growth_yoy},
    "f42_pplo_147_cash_gm_proxy": {"inputs": ["revenue", "ncfo", "receivables", "inventory", "payables"], "func": f42_pplo_147_cash_gm_proxy},
    "f42_pplo_148_cash_gm_proxy_yoy_change": {"inputs": ["revenue", "ncfo", "receivables", "inventory", "payables"], "func": f42_pplo_148_cash_gm_proxy_yoy_change},
    "f42_pplo_149_gm_times_rev_growth": {"inputs": ["revenue", "gp"], "func": f42_pplo_149_gm_times_rev_growth},
    "f42_pplo_150_pricing_power_quality_index": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_150_pricing_power_quality_index},
}
