"""pricing_power_loss_signal D3 features 076-150 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff() applied
3 time(s). Self-contained; helpers redefined locally per HANDOFF. PIT-clean.
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
#                    D3 FEATURES 076-150
# ============================================================

def f42_pplo_076_gm_zscore_12q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(gp, revenue), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_077_gm_zscore_16q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(gp, revenue), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_078_gm_ttm_zscore_8q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 8, min_periods=3)).diff().diff().diff()


def f42_pplo_079_gm_ttm_zscore_12q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_080_gm_ttm_zscore_16q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_081_cv_gm_4q_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    m = gm.rolling(4, min_periods=2).mean()
    sd = gm.rolling(4, min_periods=2).std()
    return (_safe_div(sd, m.abs())).diff().diff().diff()


def f42_pplo_082_cv_gm_12q_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    m = gm.rolling(12, min_periods=4).mean()
    sd = gm.rolling(12, min_periods=4).std()
    return (_safe_div(sd, m.abs())).diff().diff().diff()


def f42_pplo_083_cv_ebitm_8q_d3(revenue, ebit):
    em = _safe_div(ebit, revenue)
    m = em.rolling(8, min_periods=3).mean()
    sd = em.rolling(8, min_periods=3).std()
    return (_safe_div(sd, m.abs())).diff().diff().diff()


def f42_pplo_084_cv_ebitm_12q_d3(revenue, ebit):
    em = _safe_div(ebit, revenue)
    m = em.rolling(12, min_periods=4).mean()
    sd = em.rolling(12, min_periods=4).std()
    return (_safe_div(sd, m.abs())).diff().diff().diff()


def f42_pplo_085_std_om_8q_d3(revenue, ebit):
    return (_safe_div(ebit, revenue).rolling(8, min_periods=3).std()).diff().diff().diff()


def f42_pplo_086_std_om_12q_d3(revenue, ebit):
    return (_safe_div(ebit, revenue).rolling(12, min_periods=4).std()).diff().diff().diff()


def f42_pplo_087_composite_gm_compress_plus_ar_bloat_d3(revenue, gp, receivables):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar_ratio = _safe_div(receivables, _ttm(revenue))
    return (gm_compress + ar_ratio.diff(4)).diff().diff().diff()


def f42_pplo_088_composite_gm_compress_plus_inv_bloat_d3(revenue, gp, inventory):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    inv_ratio = _safe_div(inventory, _ttm(revenue))
    return (gm_compress + inv_ratio.diff(4)).diff().diff().diff()


def f42_pplo_089_composite_gm_compress_plus_defrev_decline_d3(revenue, gp, deferredrev):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    def_ratio = _safe_div(deferredrev, _ttm(revenue))
    return (gm_compress + (-def_ratio.diff(4))).diff().diff().diff()


def f42_pplo_090_composite_full_d3(revenue, gp, receivables, inventory, deferredrev):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return (gm_compress + ar + iv + dr).diff().diff().diff()


def f42_pplo_091_composite_normalized_zscore_8q_d3(revenue, gp, receivables, inventory):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    comp = gm_compress + ar + iv
    return (_rolling_zscore(comp, 8, min_periods=3)).diff().diff().diff()


def f42_pplo_092_composite_full_yoy_change_d3(revenue, gp, receivables, inventory, deferredrev):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return ((gm_compress + ar + iv + dr).diff(4)).diff().diff().diff()


def f42_pplo_093_composite_full_8q_avg_d3(revenue, gp, receivables, inventory, deferredrev):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    ar = _safe_div(receivables, _ttm(revenue)).diff(4)
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    dr = -_safe_div(deferredrev, _ttm(revenue)).diff(4)
    return ((gm_compress + ar + iv + dr).rolling(8, min_periods=3).mean()).diff().diff().diff()


def f42_pplo_094_composite_with_dso_d3(revenue, gp, receivables, inventory):
    gm = _safe_div(gp, revenue)
    gm_compress = -(gm - gm.rolling(4, min_periods=2).mean())
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    iv = _safe_div(inventory, _ttm(revenue)).diff(4)
    return (gm_compress + dso.diff(4) / 365.0 + iv).diff().diff().diff()


def f42_pplo_095_rev_growth_fueled_by_ar_d3(revenue, receivables):
    return (_safe_div(receivables.diff(), revenue.diff())).diff().diff().diff()


def f42_pplo_096_rev_growth_fueled_by_inv_d3(revenue, inventory):
    return (_safe_div(inventory.diff(), revenue.diff())).diff().diff().diff()


def f42_pplo_097_rev_cash_collection_quality_d3(revenue, ncfo):
    return (_safe_div(ncfo, revenue)).diff().diff().diff()


def f42_pplo_098_rev_cash_collection_yoy_change_d3(revenue, ncfo):
    return (_safe_div(ncfo, revenue).diff(4)).diff().diff().diff()


def f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth_d3(revenue, ncfo):
    return (_yoy_pct(revenue) - _yoy_pct(ncfo)).diff().diff().diff()


def f42_pplo_100_cash_conversion_efficiency_d3(gp, ncfo):
    return (_safe_div(ncfo, gp)).diff().diff().diff()


def f42_pplo_101_cogs_to_rev_above_p80_12q_d3(revenue, cor):
    r = _safe_div(cor, revenue)
    p80 = r.rolling(12, min_periods=4).quantile(0.80)
    return ((r > p80).astype(float).where(r.notna() & p80.notna())).diff().diff().diff()


def f42_pplo_102_cogs_to_rev_above_p80_16q_d3(revenue, cor):
    r = _safe_div(cor, revenue)
    p80 = r.rolling(16, min_periods=5).quantile(0.80)
    return ((r > p80).astype(float).where(r.notna() & p80.notna())).diff().diff().diff()


def f42_pplo_103_cogs_to_rev_pct_rank_12q_d3(revenue, cor):
    return (_pct_rank(_safe_div(cor, revenue), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_104_cogs_to_rev_pct_rank_16q_d3(revenue, cor):
    return (_pct_rank(_safe_div(cor, revenue), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_105_gm_diff_autocorr_lag1_8q_d3(revenue, gp):
    return (_autocorr_lag1(_safe_div(gp, revenue).diff(), 8, min_periods=4)).diff().diff().diff()


def f42_pplo_106_gm_diff_autocorr_lag1_12q_d3(revenue, gp):
    return (_autocorr_lag1(_safe_div(gp, revenue).diff(), 12, min_periods=5)).diff().diff().diff()


def f42_pplo_107_gm_level_autocorr_lag1_8q_d3(revenue, gp):
    return (_autocorr_lag1(_safe_div(gp, revenue), 8, min_periods=4)).diff().diff().diff()


def f42_pplo_108_gm_level_autocorr_lag1_12q_d3(revenue, gp):
    return (_autocorr_lag1(_safe_div(gp, revenue), 12, min_periods=5)).diff().diff().diff()


def f42_pplo_109_gm_pct_rank_8q_d3(revenue, gp):
    return (_pct_rank(_safe_div(gp, revenue), 8, min_periods=3)).diff().diff().diff()


def f42_pplo_110_gm_pct_rank_12q_d3(revenue, gp):
    return (_pct_rank(_safe_div(gp, revenue), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_111_gm_pct_rank_16q_d3(revenue, gp):
    return (_pct_rank(_safe_div(gp, revenue), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_112_gm_ttm_pct_rank_16q_d3(revenue, gp):
    return (_pct_rank(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_113_quarters_since_gm_max_8q_d3(revenue, gp):
    return (_quarters_since_max(_safe_div(gp, revenue), 8, min_periods=3)).diff().diff().diff()


def f42_pplo_114_quarters_since_gm_max_12q_d3(revenue, gp):
    return (_quarters_since_max(_safe_div(gp, revenue), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_115_quarters_since_gm_max_16q_d3(revenue, gp):
    return (_quarters_since_max(_safe_div(gp, revenue), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_116_quarters_since_gm_ttm_max_16q_d3(revenue, gp):
    return (_quarters_since_max(_safe_div(_ttm(gp), _ttm(revenue)), 16, min_periods=5)).diff().diff().diff()


def f42_pplo_117_flag_gm_down_and_ar_up_yoy_d3(revenue, gp, receivables):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    return (((gm.diff(4) < 0) & (ar.diff(4) > 0)).astype(float)).diff().diff().diff()


def f42_pplo_118_flag_gm_down_and_inv_up_yoy_d3(revenue, gp, inventory):
    gm = _safe_div(gp, revenue)
    iv = _safe_div(inventory, _ttm(revenue))
    return (((gm.diff(4) < 0) & (iv.diff(4) > 0)).astype(float)).diff().diff().diff()


def f42_pplo_119_flag_gm_down_and_defrev_down_yoy_d3(revenue, gp, deferredrev):
    gm = _safe_div(gp, revenue)
    dr = _safe_div(deferredrev, _ttm(revenue))
    return (((gm.diff(4) < 0) & (dr.diff(4) < 0)).astype(float)).diff().diff().diff()


def f42_pplo_120_flag_gm_down_and_dso_up_d3(revenue, gp, receivables):
    gm = _safe_div(gp, revenue)
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    return (((gm.diff(4) < 0) & (dso.diff(4) > 0)).astype(float)).diff().diff().diff()


def f42_pplo_121_flag_gm_down_and_dio_up_d3(revenue, gp, cor, inventory):
    _ = revenue
    gm = _safe_div(gp, revenue)
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return (((gm.diff(4) < 0) & (dio.diff(4) > 0)).astype(float)).diff().diff().diff()


def f42_pplo_122_gm_falling_4q_streak_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    decl = (gm.diff() < 0).astype(float)
    grp = (decl == 0).cumsum()
    return (decl.groupby(grp).cumsum()).diff().diff().diff()


def f42_pplo_123_gm_minus_ebitm_d3(revenue, gp, ebit):
    return (_safe_div(gp, revenue) - _safe_div(ebit, revenue)).diff().diff().diff()


def f42_pplo_124_gm_minus_ebitm_yoy_change_d3(revenue, gp, ebit):
    return ((_safe_div(gp, revenue) - _safe_div(ebit, revenue)).diff(4)).diff().diff().diff()


def f42_pplo_125_gm_minus_ebitm_2y_change_d3(revenue, gp, ebit):
    return ((_safe_div(gp, revenue) - _safe_div(ebit, revenue)).diff(8)).diff().diff().diff()


def f42_pplo_126_gm_minus_ebitm_slope_8q_d3(revenue, gp, ebit):
    return (_rolling_slope(_safe_div(gp, revenue) - _safe_div(ebit, revenue), 8, min_periods=3)).diff().diff().diff()


def f42_pplo_127_gm_minus_sbc_to_rev_d3(revenue, gp, sbcomp):
    return (_safe_div(gp, revenue) - _safe_div(sbcomp, revenue)).diff().diff().diff()


def f42_pplo_128_gm_minus_sbc_to_rev_yoy_d3(revenue, gp, sbcomp):
    return ((_safe_div(gp, revenue) - _safe_div(sbcomp, revenue)).diff(4)).diff().diff().diff()


def f42_pplo_129_sbc_to_rev_yoy_change_d3(revenue, sbcomp):
    return (_safe_div(sbcomp, revenue).diff(4)).diff().diff().diff()


def f42_pplo_130_effective_gm_after_sbc_zscore_12q_d3(revenue, gp, sbcomp):
    return (_rolling_zscore(_safe_div(gp, revenue) - _safe_div(sbcomp, revenue), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_131_composite_v1_d3(revenue, gp, receivables, cor, inventory):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return ((-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0).diff().diff().diff()


def f42_pplo_132_composite_v2_zscore_d3(revenue, gp, receivables, inventory):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    iv = _safe_div(inventory, _ttm(revenue))
    return ((-_rolling_zscore(gm, 12, 4)) + _rolling_zscore(ar, 12, 4) + _rolling_zscore(iv, 12, 4)).diff().diff().diff()


def f42_pplo_133_composite_signal_count_d3(revenue, gp, receivables, cor, inventory, deferredrev):
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
    return (f1 + f2 + f3 + f4 + f5 + f6).diff().diff().diff()


def f42_pplo_134_composite_v1_yoy_delta_d3(revenue, gp, receivables, cor, inventory):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    return (comp.diff(4)).diff().diff().diff()


def f42_pplo_135_composite_v1_normalized_d3(revenue, gp, receivables, cor, inventory):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    sd = comp.rolling(12, min_periods=4).std()
    return (_safe_div(comp, sd)).diff().diff().diff()


def f42_pplo_136_composite_extreme_quintile_flag_d3(revenue, gp, receivables, cor, inventory):
    gm = _safe_div(gp, revenue)
    ar = _safe_div(receivables, _ttm(revenue))
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    comp = (-gm.diff(4)) + ar.diff(4) + dio.diff(4) / 365.0
    p80 = comp.rolling(16, min_periods=5).quantile(0.80)
    return ((comp > p80).astype(float).where(comp.notna() & p80.notna())).diff().diff().diff()


def f42_pplo_137_gp_to_assets_d3(gp, assets):
    return (_safe_div(gp, assets)).diff().diff().diff()


def f42_pplo_138_gp_to_assets_yoy_change_d3(gp, assets):
    return (_safe_div(gp, assets).diff(4)).diff().diff().diff()


def f42_pplo_139_gp_to_assets_zscore_12q_d3(gp, assets):
    return (_rolling_zscore(_safe_div(gp, assets), 12, min_periods=4)).diff().diff().diff()


def f42_pplo_140_gp_to_tangible_assets_d3(gp, assets, intangibles):
    return (_safe_div(gp, assets - intangibles)).diff().diff().diff()


def f42_pplo_141_gp_to_invested_capital_proxy_d3(gp, assets, payables):
    return (_safe_div(gp, assets - payables)).diff().diff().diff()


def f42_pplo_142_revenue_per_ppne_d3(revenue, ppnenet):
    return (_safe_div(revenue, ppnenet)).diff().diff().diff()


def f42_pplo_143_revenue_per_ppne_yoy_change_d3(revenue, ppnenet):
    return (_safe_div(revenue, ppnenet).diff(4)).diff().diff().diff()


def f42_pplo_144_payables_to_cogs_d3(cor, payables):
    return (_safe_div(payables, _ttm(cor))).diff().diff().diff()


def f42_pplo_145_payables_to_cogs_yoy_change_d3(cor, payables):
    return (_safe_div(payables, _ttm(cor)).diff(4)).diff().diff().diff()


def f42_pplo_146_payables_growth_minus_cogs_growth_yoy_d3(cor, payables):
    return (_yoy_pct(payables) - _yoy_pct(cor)).diff().diff().diff()


def f42_pplo_147_cash_gm_proxy_d3(revenue, ncfo, receivables, inventory, payables):
    num = ncfo - receivables.diff() - inventory.diff() + payables.diff()
    return (_safe_div(num, revenue)).diff().diff().diff()


def f42_pplo_148_cash_gm_proxy_yoy_change_d3(revenue, ncfo, receivables, inventory, payables):
    num = ncfo - receivables.diff() - inventory.diff() + payables.diff()
    return (_safe_div(num, revenue).diff(4)).diff().diff().diff()


def f42_pplo_149_gm_times_rev_growth_d3(revenue, gp):
    return (_safe_div(gp, revenue) * _yoy_pct(revenue)).diff().diff().diff()


def f42_pplo_150_pricing_power_quality_index_d3(revenue, gp, receivables, cor, inventory):
    gm = _safe_div(gp, revenue)
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return (0.4 * _rolling_zscore(gm, 12, 4)
            - 0.3 * _rolling_zscore(dso, 12, 4)
            - 0.3 * _rolling_zscore(dio, 12, 4)).diff().diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

PRICING_POWER_LOSS_SIGNAL_D3_REGISTRY_076_150 = {
    "f42_pplo_076_gm_zscore_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_076_gm_zscore_12q_d3},
    "f42_pplo_077_gm_zscore_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_077_gm_zscore_16q_d3},
    "f42_pplo_078_gm_ttm_zscore_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_078_gm_ttm_zscore_8q_d3},
    "f42_pplo_079_gm_ttm_zscore_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_079_gm_ttm_zscore_12q_d3},
    "f42_pplo_080_gm_ttm_zscore_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_080_gm_ttm_zscore_16q_d3},
    "f42_pplo_081_cv_gm_4q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_081_cv_gm_4q_d3},
    "f42_pplo_082_cv_gm_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_082_cv_gm_12q_d3},
    "f42_pplo_083_cv_ebitm_8q_d3": {"inputs": ["revenue", "ebit"], "func": f42_pplo_083_cv_ebitm_8q_d3},
    "f42_pplo_084_cv_ebitm_12q_d3": {"inputs": ["revenue", "ebit"], "func": f42_pplo_084_cv_ebitm_12q_d3},
    "f42_pplo_085_std_om_8q_d3": {"inputs": ["revenue", "ebit"], "func": f42_pplo_085_std_om_8q_d3},
    "f42_pplo_086_std_om_12q_d3": {"inputs": ["revenue", "ebit"], "func": f42_pplo_086_std_om_12q_d3},
    "f42_pplo_087_composite_gm_compress_plus_ar_bloat_d3": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_087_composite_gm_compress_plus_ar_bloat_d3},
    "f42_pplo_088_composite_gm_compress_plus_inv_bloat_d3": {"inputs": ["revenue", "gp", "inventory"], "func": f42_pplo_088_composite_gm_compress_plus_inv_bloat_d3},
    "f42_pplo_089_composite_gm_compress_plus_defrev_decline_d3": {"inputs": ["revenue", "gp", "deferredrev"], "func": f42_pplo_089_composite_gm_compress_plus_defrev_decline_d3},
    "f42_pplo_090_composite_full_d3": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_090_composite_full_d3},
    "f42_pplo_091_composite_normalized_zscore_8q_d3": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_091_composite_normalized_zscore_8q_d3},
    "f42_pplo_092_composite_full_yoy_change_d3": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_092_composite_full_yoy_change_d3},
    "f42_pplo_093_composite_full_8q_avg_d3": {"inputs": ["revenue", "gp", "receivables", "inventory", "deferredrev"], "func": f42_pplo_093_composite_full_8q_avg_d3},
    "f42_pplo_094_composite_with_dso_d3": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_094_composite_with_dso_d3},
    "f42_pplo_095_rev_growth_fueled_by_ar_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_095_rev_growth_fueled_by_ar_d3},
    "f42_pplo_096_rev_growth_fueled_by_inv_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_096_rev_growth_fueled_by_inv_d3},
    "f42_pplo_097_rev_cash_collection_quality_d3": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_097_rev_cash_collection_quality_d3},
    "f42_pplo_098_rev_cash_collection_yoy_change_d3": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_098_rev_cash_collection_yoy_change_d3},
    "f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth_d3": {"inputs": ["revenue", "ncfo"], "func": f42_pplo_099_rev_yoy_minus_ncfo_yoy_growth_d3},
    "f42_pplo_100_cash_conversion_efficiency_d3": {"inputs": ["gp", "ncfo"], "func": f42_pplo_100_cash_conversion_efficiency_d3},
    "f42_pplo_101_cogs_to_rev_above_p80_12q_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_101_cogs_to_rev_above_p80_12q_d3},
    "f42_pplo_102_cogs_to_rev_above_p80_16q_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_102_cogs_to_rev_above_p80_16q_d3},
    "f42_pplo_103_cogs_to_rev_pct_rank_12q_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_103_cogs_to_rev_pct_rank_12q_d3},
    "f42_pplo_104_cogs_to_rev_pct_rank_16q_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_104_cogs_to_rev_pct_rank_16q_d3},
    "f42_pplo_105_gm_diff_autocorr_lag1_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_105_gm_diff_autocorr_lag1_8q_d3},
    "f42_pplo_106_gm_diff_autocorr_lag1_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_106_gm_diff_autocorr_lag1_12q_d3},
    "f42_pplo_107_gm_level_autocorr_lag1_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_107_gm_level_autocorr_lag1_8q_d3},
    "f42_pplo_108_gm_level_autocorr_lag1_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_108_gm_level_autocorr_lag1_12q_d3},
    "f42_pplo_109_gm_pct_rank_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_109_gm_pct_rank_8q_d3},
    "f42_pplo_110_gm_pct_rank_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_110_gm_pct_rank_12q_d3},
    "f42_pplo_111_gm_pct_rank_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_111_gm_pct_rank_16q_d3},
    "f42_pplo_112_gm_ttm_pct_rank_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_112_gm_ttm_pct_rank_16q_d3},
    "f42_pplo_113_quarters_since_gm_max_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_113_quarters_since_gm_max_8q_d3},
    "f42_pplo_114_quarters_since_gm_max_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_114_quarters_since_gm_max_12q_d3},
    "f42_pplo_115_quarters_since_gm_max_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_115_quarters_since_gm_max_16q_d3},
    "f42_pplo_116_quarters_since_gm_ttm_max_16q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_116_quarters_since_gm_ttm_max_16q_d3},
    "f42_pplo_117_flag_gm_down_and_ar_up_yoy_d3": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_117_flag_gm_down_and_ar_up_yoy_d3},
    "f42_pplo_118_flag_gm_down_and_inv_up_yoy_d3": {"inputs": ["revenue", "gp", "inventory"], "func": f42_pplo_118_flag_gm_down_and_inv_up_yoy_d3},
    "f42_pplo_119_flag_gm_down_and_defrev_down_yoy_d3": {"inputs": ["revenue", "gp", "deferredrev"], "func": f42_pplo_119_flag_gm_down_and_defrev_down_yoy_d3},
    "f42_pplo_120_flag_gm_down_and_dso_up_d3": {"inputs": ["revenue", "gp", "receivables"], "func": f42_pplo_120_flag_gm_down_and_dso_up_d3},
    "f42_pplo_121_flag_gm_down_and_dio_up_d3": {"inputs": ["revenue", "gp", "cor", "inventory"], "func": f42_pplo_121_flag_gm_down_and_dio_up_d3},
    "f42_pplo_122_gm_falling_4q_streak_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_122_gm_falling_4q_streak_d3},
    "f42_pplo_123_gm_minus_ebitm_d3": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_123_gm_minus_ebitm_d3},
    "f42_pplo_124_gm_minus_ebitm_yoy_change_d3": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_124_gm_minus_ebitm_yoy_change_d3},
    "f42_pplo_125_gm_minus_ebitm_2y_change_d3": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_125_gm_minus_ebitm_2y_change_d3},
    "f42_pplo_126_gm_minus_ebitm_slope_8q_d3": {"inputs": ["revenue", "gp", "ebit"], "func": f42_pplo_126_gm_minus_ebitm_slope_8q_d3},
    "f42_pplo_127_gm_minus_sbc_to_rev_d3": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_127_gm_minus_sbc_to_rev_d3},
    "f42_pplo_128_gm_minus_sbc_to_rev_yoy_d3": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_128_gm_minus_sbc_to_rev_yoy_d3},
    "f42_pplo_129_sbc_to_rev_yoy_change_d3": {"inputs": ["revenue", "sbcomp"], "func": f42_pplo_129_sbc_to_rev_yoy_change_d3},
    "f42_pplo_130_effective_gm_after_sbc_zscore_12q_d3": {"inputs": ["revenue", "gp", "sbcomp"], "func": f42_pplo_130_effective_gm_after_sbc_zscore_12q_d3},
    "f42_pplo_131_composite_v1_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_131_composite_v1_d3},
    "f42_pplo_132_composite_v2_zscore_d3": {"inputs": ["revenue", "gp", "receivables", "inventory"], "func": f42_pplo_132_composite_v2_zscore_d3},
    "f42_pplo_133_composite_signal_count_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory", "deferredrev"], "func": f42_pplo_133_composite_signal_count_d3},
    "f42_pplo_134_composite_v1_yoy_delta_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_134_composite_v1_yoy_delta_d3},
    "f42_pplo_135_composite_v1_normalized_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_135_composite_v1_normalized_d3},
    "f42_pplo_136_composite_extreme_quintile_flag_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_136_composite_extreme_quintile_flag_d3},
    "f42_pplo_137_gp_to_assets_d3": {"inputs": ["gp", "assets"], "func": f42_pplo_137_gp_to_assets_d3},
    "f42_pplo_138_gp_to_assets_yoy_change_d3": {"inputs": ["gp", "assets"], "func": f42_pplo_138_gp_to_assets_yoy_change_d3},
    "f42_pplo_139_gp_to_assets_zscore_12q_d3": {"inputs": ["gp", "assets"], "func": f42_pplo_139_gp_to_assets_zscore_12q_d3},
    "f42_pplo_140_gp_to_tangible_assets_d3": {"inputs": ["gp", "assets", "intangibles"], "func": f42_pplo_140_gp_to_tangible_assets_d3},
    "f42_pplo_141_gp_to_invested_capital_proxy_d3": {"inputs": ["gp", "assets", "payables"], "func": f42_pplo_141_gp_to_invested_capital_proxy_d3},
    "f42_pplo_142_revenue_per_ppne_d3": {"inputs": ["revenue", "ppnenet"], "func": f42_pplo_142_revenue_per_ppne_d3},
    "f42_pplo_143_revenue_per_ppne_yoy_change_d3": {"inputs": ["revenue", "ppnenet"], "func": f42_pplo_143_revenue_per_ppne_yoy_change_d3},
    "f42_pplo_144_payables_to_cogs_d3": {"inputs": ["cor", "payables"], "func": f42_pplo_144_payables_to_cogs_d3},
    "f42_pplo_145_payables_to_cogs_yoy_change_d3": {"inputs": ["cor", "payables"], "func": f42_pplo_145_payables_to_cogs_yoy_change_d3},
    "f42_pplo_146_payables_growth_minus_cogs_growth_yoy_d3": {"inputs": ["cor", "payables"], "func": f42_pplo_146_payables_growth_minus_cogs_growth_yoy_d3},
    "f42_pplo_147_cash_gm_proxy_d3": {"inputs": ["revenue", "ncfo", "receivables", "inventory", "payables"], "func": f42_pplo_147_cash_gm_proxy_d3},
    "f42_pplo_148_cash_gm_proxy_yoy_change_d3": {"inputs": ["revenue", "ncfo", "receivables", "inventory", "payables"], "func": f42_pplo_148_cash_gm_proxy_yoy_change_d3},
    "f42_pplo_149_gm_times_rev_growth_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_149_gm_times_rev_growth_d3},
    "f42_pplo_150_pricing_power_quality_index_d3": {"inputs": ["revenue", "gp", "receivables", "cor", "inventory"], "func": f42_pplo_150_pricing_power_quality_index_d3},
}
