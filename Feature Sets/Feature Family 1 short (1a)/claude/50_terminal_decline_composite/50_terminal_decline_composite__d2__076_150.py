"""terminal_decline_composite d2 features 076_150 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the final return with .diff().diff(). Self-contained.
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


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _rolling_max(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).max()


def _rolling_min(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).min()


# ============================================================
#                    FEATURES
# ============================================================

def f50_tdcp_076_compound_stress_z_index_d2(debt, equity, ncfo, revenue, close):
    lev = _safe_div(debt, equity)
    burn = _safe_div(-_ttm(ncfo), _ttm(revenue).abs())
    px_z = -_rolling_zscore(close, YDAYS)
    lev_z = _rolling_zscore(lev, YDAYS)
    burn_z = _rolling_zscore(burn, YDAYS)
    return (lev_z + burn_z + px_z).diff().diff()

def f50_tdcp_077_multi_pctile_distress_sum_d2(ncfo, debt, equity, close):
    cf_p = _rolling_zscore(_ttm(ncfo), YDAYS)
    de_p = _rolling_zscore(_safe_div(debt, equity), YDAYS)
    px_p = _rolling_zscore(close, YDAYS)
    return (-cf_p + de_p - px_p).diff().diff()

def f50_tdcp_078_two_yr_dual_deterioration_proxy_d2(revenue, close):
    r_chg = _yoy_pct(_ttm(revenue))
    p_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    both = ((r_chg < 0) & (p_chg < 0)).astype(float)
    return (both.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f50_tdcp_079_triple_trend_decline_d2(revenue, ncfo, close):
    rs = _ttm(revenue) - _ttm(revenue).shift(QDAYS)
    cs = _ttm(ncfo) - _ttm(ncfo).shift(QDAYS)
    ps = close - close.shift(QDAYS)
    return (((rs < 0).astype(float) + (cs < 0).astype(float) + (ps < 0).astype(float))).diff().diff()

def f50_tdcp_080_zombie_proxy_neg_roe_high_lev_falling_rev_d2(netinc, equity, debt, marketcap, revenue):
    roe = _safe_div(_ttm(netinc), equity)
    zombie = (roe < 0).astype(float) * (debt > marketcap).astype(float)
    r_decl = (_yoy_pct(_ttm(revenue)) < 0).astype(float)
    return (zombie * r_decl).diff().diff()

def f50_tdcp_081_multi_q_accel_loss_x_below_200d_d2(netinc, close):
    inc_q = netinc
    accel_loss = (inc_q < inc_q.shift(QDAYS)).astype(float) * (inc_q < 0).astype(float)
    accel_persist = accel_loss.rolling(YDAYS, min_periods=QDAYS).mean()
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    return (accel_persist * below).diff().diff()

def f50_tdcp_082_regime_change_dual_flip_d2(revenue, close):
    rev_chg = _ttm(revenue).diff(QDAYS)
    px_chg = close.diff(QDAYS)
    flip = ((rev_chg < 0) & (px_chg < 0) & (rev_chg.shift(QDAYS) > 0) & (px_chg.shift(QDAYS) > 0)).astype(float)
    return (flip.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f50_tdcp_083_trend_congruence_fundamentals_price_d2(ebitda, close):
    e_slope = _ttm(ebitda).diff(QDAYS)
    p_slope = close.diff(QDAYS)
    return (_safe_div(e_slope * p_slope, e_slope.abs() * p_slope.abs())).diff().diff()

def f50_tdcp_084_volatility_regime_instability_compound_d2(revenue, close):
    rev_v = _ttm(revenue).rolling(YDAYS, min_periods=QDAYS).std()
    rev_m = _ttm(revenue).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    rev_cv = _safe_div(rev_v, rev_m)
    px_ret = _safe_log(close).diff()
    px_v = px_ret.rolling(YDAYS, min_periods=QDAYS).std()
    return (rev_cv * px_v).diff().diff()

def f50_tdcp_085_time_since_positive_fcf_x_dd_d2(fcf, close):
    pos = (fcf > 0).astype(float)
    def _last_pos(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) == 0:
            return float(len(w))
        return float(len(w) - 1 - idx[-1])
    last = pos.rolling(YDAYS, min_periods=QDAYS).apply(_last_pos, raw=True)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (last * (-dd)).diff().diff()

def f50_tdcp_086_capitulation_volume_x_dd_x_burn_d2(volume, close, ncfo):
    v_z = _rolling_zscore(volume, YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    burn = (-_ttm(ncfo)).clip(lower=0)
    return (v_z.clip(lower=0) * (-dd) * _safe_div(burn, burn.abs() + 1.0)).diff().diff()

def f50_tdcp_087_liquidity_drying_composite_d2(volume, marketcap, high, low, close):
    v_chg = _safe_log(volume.replace(0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()) - _safe_log(volume.replace(0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean())
    spread = _safe_div(high - low, close)
    mc_log = _safe_log(marketcap)
    mc_p = mc_log.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((-v_chg).clip(lower=0) * spread * (1.0 - mc_p)).diff().diff()

def f50_tdcp_088_persistent_below_peak_x_fund_decline_d2(close, revenue):
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    below_50pct = (close < 0.5 * rmax).astype(float)
    persist = below_50pct.rolling(YDAYS, min_periods=QDAYS).mean()
    r_decline = (_yoy_pct(_ttm(revenue)) < 0).astype(float)
    return (persist * r_decline).diff().diff()

def f50_tdcp_089_intangibles_share_erosion_x_dd_d2(intangibles, assets, close):
    share = _safe_div(intangibles, assets)
    s_chg = share - share.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (s_chg * (-dd)).diff().diff()

def f50_tdcp_090_tangible_book_collapse_x_dd_d2(equity, intangibles, close):
    tbk = equity - intangibles
    chg = _safe_div(tbk - tbk.shift(YDAYS), tbk.shift(YDAYS).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_091_ppe_writedown_x_volume_capit_d2(ppnenet, volume):
    ppe_chg = _safe_div(ppnenet.diff(QDAYS), ppnenet.shift(QDAYS).abs())
    v_z = _rolling_zscore(volume, YDAYS)
    return ((-ppe_chg).clip(lower=0) * v_z.clip(lower=0)).diff().diff()

def f50_tdcp_092_depamor_jump_x_drawdown_d2(depamor, close):
    d_chg = _safe_div(depamor.diff(QDAYS), depamor.shift(QDAYS).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (d_chg.clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_093_intangibles_writedown_proxy_x_dd_d2(intangibles, close):
    chg = _safe_div(intangibles.diff(QDAYS), intangibles.shift(QDAYS).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_094_inventory_buildup_x_price_decline_d2(inventory, close):
    inv_g = _yoy_pct(inventory)
    px_g = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (inv_g.clip(lower=0) * (-px_g).clip(lower=0)).diff().diff()

def f50_tdcp_095_receivables_buildup_x_dd_d2(receivables, revenue, close):
    dso = _safe_div(receivables * 365.0, _ttm(revenue))
    dso_chg = dso - dso.shift(QDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (dso_chg.clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_096_asset_turnover_collapse_x_price_decline_d2(revenue, assets, close):
    at_r = _safe_div(_ttm(revenue), assets)
    at_chg = at_r - at_r.shift(YDAYS)
    px_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return ((-at_chg).clip(lower=0) * (-px_chg).clip(lower=0)).diff().diff()

def f50_tdcp_097_payables_stretching_x_dd_d2(payables, cor, close):
    dpo = _safe_div(payables * 365.0, _ttm(cor).abs())
    dpo_chg = dpo - dpo.shift(QDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (dpo_chg.clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_098_capex_collapse_x_dd_d2(capex, close):
    cx_chg = _safe_div(_ttm(capex).abs().diff(YDAYS), _ttm(capex).abs().shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-cx_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_099_rnd_decline_x_revenue_decline_x_price_decline_d2(rnd, revenue, close):
    r_chg = _yoy_pct(_ttm(rnd))
    rv_chg = _yoy_pct(_ttm(revenue))
    px_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return ((-r_chg).clip(lower=0) * (-rv_chg).clip(lower=0) * (-px_chg).clip(lower=0)).diff().diff()

def f50_tdcp_100_ncfi_invest_collapse_x_dd_d2(ncfi, close):
    nv = _safe_div(_ttm(ncfi).abs().diff(YDAYS), _ttm(ncfi).abs().shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-nv).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_101_ncff_financing_drying_up_x_dd_d2(ncff, close):
    nf = _safe_div(_ttm(ncff).abs().diff(YDAYS), _ttm(ncff).abs().shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-nf).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_102_inventory_revenue_divergence_x_price_d2(inventory, revenue, close):
    inv_g = _yoy_pct(inventory)
    rev_g = _yoy_pct(_ttm(revenue))
    div = inv_g - rev_g
    px = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (div.clip(lower=0) * (-px).clip(lower=0)).diff().diff()

def f50_tdcp_103_receivables_revenue_divergence_x_dd_d2(receivables, revenue, close):
    rec_g = _yoy_pct(receivables)
    rev_g = _yoy_pct(_ttm(revenue))
    div = rec_g - rev_g
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (div.clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_104_close_pct_x_ncfo_pct_x_de_pct_d2(close, ncfo, debt, equity):
    c_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    cf_p = _ttm(ncfo).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    de_p = _safe_div(debt, equity).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((1.0 - c_p) + (1.0 - cf_p) + de_p).diff().diff()

def f50_tdcp_105_close_pct_low_x_burn_pct_high_d2(close, ncfo):
    c_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    burn = -_ttm(ncfo)
    b_p = burn.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((1.0 - c_p) * b_p).diff().diff()

def f50_tdcp_106_marketcap_pctile_x_debt_pctile_d2(marketcap, debt):
    mc_p = marketcap.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    d_p = debt.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((1.0 - mc_p) * d_p).diff().diff()

def f50_tdcp_107_revenue_pctile_low_x_close_pctile_low_d2(revenue, close):
    r_p = _ttm(revenue).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    c_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((1.0 - r_p) * (1.0 - c_p)).diff().diff()

def f50_tdcp_108_equity_pctile_low_x_dd_d2(equity, close):
    e_p = equity.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((1.0 - e_p) * (-dd)).diff().diff()

def f50_tdcp_109_five_signal_distress_sum_d2(netinc, ncfo, workingcapital, retearn, close):
    s1 = (netinc < 0).astype(float)
    s2 = (ncfo < 0).astype(float)
    s3 = (workingcapital < 0).astype(float)
    s4 = (retearn < 0).astype(float)
    ma = close.rolling(200, min_periods=63).mean()
    s5 = (close < ma).astype(float)
    return (s1 + s2 + s3 + s4 + s5).diff().diff()

def f50_tdcp_110_triple_quarterly_neg_x_price_below_low_d2(netinc, ncfo, ebit, close):
    n = (netinc < 0).astype(float)
    c = (ncfo < 0).astype(float)
    e = (ebit < 0).astype(float)
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    near_lo = (close < rmin * 1.05).astype(float)
    return ((n + c + e) * near_lo).diff().diff()

def f50_tdcp_111_stress_lookback_window_persistence_d2(netinc, close):
    neg_inc = (netinc < 0).astype(float)
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    return ((neg_inc * below).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f50_tdcp_112_ev_to_assets_collapse_x_dd_d2(marketcap, debt, cashneq, assets, close):
    ev = marketcap + debt - cashneq
    ratio = _safe_div(ev, assets)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (ratio * dd).diff().diff()

def f50_tdcp_113_composite_distress_rank_sum_d2(debt, equity, ncfo, close):
    de_r = _safe_div(debt, equity).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    cf_r = _ttm(ncfo).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    px_r = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (de_r - cf_r - px_r).diff().diff()

def f50_tdcp_114_acceleration_of_losses_x_dd_accel_d2(netinc, close):
    inc_chg = _ttm(netinc).diff(QDAYS)
    inc_accel = inc_chg - inc_chg.shift(QDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    dd_accel = dd.diff(QDAYS)
    return ((-inc_accel).clip(lower=0) * (-dd_accel).clip(lower=0)).diff().diff()

def f50_tdcp_115_multi_horizon_dual_decline_score_d2(revenue, close):
    s = 0.0
    for h in (QDAYS, 2 * QDAYS, YDAYS):
        r = _yoy_pct(_ttm(revenue)) if h == YDAYS else _safe_div(_ttm(revenue).diff(h), _ttm(revenue).shift(h).abs())
        p = _safe_log(close) - _safe_log(close.shift(h))
        s = s + ((r < 0) & (p < 0)).astype(float)
    return (s).diff().diff()

def f50_tdcp_116_price_below_50pct_high_x_neg_eps_persistent_d2(close, netinc):
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    below = (close < 0.5 * rmax).astype(float)
    neg = (netinc < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (below * neg).diff().diff()

def f50_tdcp_117_fund_vol_x_price_vol_x_dd_d2(netinc, close):
    f_v = netinc.rolling(YDAYS, min_periods=QDAYS).std()
    f_m = netinc.rolling(YDAYS, min_periods=QDAYS).mean().abs()
    f_cv = _safe_div(f_v, f_m)
    p_v = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (f_cv * p_v * (-dd)).diff().diff()

def f50_tdcp_118_margin_volatility_x_price_volatility_d2(opinc, revenue, close):
    margin = _safe_div(opinc, revenue)
    m_v = margin.rolling(YDAYS, min_periods=QDAYS).std()
    p_v = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    return (m_v * p_v).diff().diff()

def f50_tdcp_119_revenue_cv_x_intraday_range_cv_d2(revenue, high, low, close):
    r_cv = _safe_div(_ttm(revenue).rolling(YDAYS, min_periods=QDAYS).std(), _ttm(revenue).rolling(YDAYS, min_periods=QDAYS).mean().abs())
    rng = _safe_div(high - low, close)
    rng_cv = _safe_div(rng.rolling(YDAYS, min_periods=QDAYS).std(), rng.rolling(YDAYS, min_periods=QDAYS).mean())
    return (r_cv * rng_cv).diff().diff()

def f50_tdcp_120_ebitda_vol_x_price_drawdown_severity_d2(ebitda, close):
    e_v = ebitda.rolling(YDAYS, min_periods=QDAYS).std()
    e_m = ebitda.rolling(YDAYS, min_periods=QDAYS).mean().abs()
    cv = _safe_div(e_v, e_m)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (cv * (-dd)).diff().diff()

def f50_tdcp_121_erratic_revenue_x_erratic_close_d2(revenue, close):
    r_v = _yoy_pct(_ttm(revenue)).rolling(YDAYS, min_periods=QDAYS).std()
    p_v = (_safe_log(close) - _safe_log(close.shift(YDAYS))).rolling(YDAYS, min_periods=QDAYS).std()
    return (r_v * p_v).diff().diff()

def f50_tdcp_122_debt_path_vol_x_price_vol_d2(debt, close):
    d_v = debt.diff(QDAYS).abs().rolling(YDAYS, min_periods=QDAYS).std()
    p_v = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    return (d_v * p_v).diff().diff()

def f50_tdcp_123_equity_vol_x_price_vol_x_dd_d2(equity, close):
    e_v = equity.diff(QDAYS).abs().rolling(YDAYS, min_periods=QDAYS).std()
    p_v = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (e_v * p_v * (-dd)).diff().diff()

def f50_tdcp_124_operating_vol_proxy_x_drawdown_d2(opinc, close):
    o_v = opinc.diff(QDAYS).abs().rolling(YDAYS, min_periods=QDAYS).std()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (o_v * (-dd)).diff().diff()

def f50_tdcp_125_cash_to_burn_quarters_x_volume_collapse_d2(cashneq, ncfo, volume):
    burn = (-ncfo).clip(lower=0)
    q_left = _safe_div(cashneq, burn)
    v_chg = _safe_log(volume.replace(0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()) - _safe_log(volume.replace(0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean())
    return (_safe_div((-v_chg).clip(lower=0), q_left.clip(lower=0.5))).diff().diff()

def f50_tdcp_126_disclosure_density_proxy_x_dd_d2(sharefactor, marketcap, close):
    a_density = (sharefactor.diff().abs() > 1e-6).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (a_density * (-mc_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_127_composite_z_revenue_cash_close_d2(revenue, cashneq, close):
    r_z = -_rolling_zscore(_ttm(revenue), YDAYS)
    c_z = -_rolling_zscore(cashneq, YDAYS)
    p_z = -_rolling_zscore(close, YDAYS)
    return (r_z + c_z + p_z).diff().diff()

def f50_tdcp_128_fundamentals_low_pctile_x_price_low_pctile_d2(ebit, close):
    e_p = _ttm(ebit).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    p_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((1.0 - e_p) * (1.0 - p_p)).diff().diff()

def f50_tdcp_129_price_velocity_x_fundamentals_velocity_d2(revenue, close):
    pv = _safe_log(close) - _safe_log(close.shift(QDAYS))
    fv = _safe_div(_ttm(revenue).diff(QDAYS), _ttm(revenue).shift(QDAYS).abs())
    return (pv * fv).diff().diff()

def f50_tdcp_130_price_below_ma200_persistence_x_burn_persistence_d2(close, ncfo):
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    burn_persist = (ncfo < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (below * burn_persist).diff().diff()

def f50_tdcp_131_multi_quarter_loss_streak_x_drawdown_severity_d2(netinc, close):
    streak = (netinc < 0).astype(float).rolling(8 * QDAYS, min_periods=QDAYS).sum()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (streak * (-dd) ** 2).diff().diff()

def f50_tdcp_132_debt_growing_revenue_falling_price_falling_d2(debt, revenue, close):
    d_g = _yoy_pct(debt)
    r_g = _yoy_pct(_ttm(revenue))
    p_g = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (d_g.clip(lower=0) * (-r_g).clip(lower=0) * (-p_g).clip(lower=0)).diff().diff()

def f50_tdcp_133_share_count_growth_x_revenue_per_share_decline_x_dd_d2(sharesbas, revenue, close):
    sg = _yoy_pct(sharesbas)
    rps = _safe_div(_ttm(revenue), sharesbas)
    rps_chg = _safe_log(rps) - _safe_log(rps.shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (sg.clip(lower=0) * (-rps_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_134_operating_cycle_lengthening_x_dd_d2(inventory, receivables, cor, revenue, close):
    dio = _safe_div(inventory * 365.0, _ttm(cor).abs())
    dso = _safe_div(receivables * 365.0, _ttm(revenue))
    cycle = dio + dso
    cycle_chg = cycle - cycle.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (cycle_chg.clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_135_equity_minus_intangibles_neg_x_dd_d2(equity, intangibles, close):
    tbk = equity - intangibles
    neg = (tbk < 0).astype(float)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (neg * (-dd)).diff().diff()

def f50_tdcp_136_current_ratio_collapse_x_dd_d2(assetsc, liabilitiesc, close):
    cr = _safe_div(assetsc, liabilitiesc)
    cr_chg = cr - cr.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-cr_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_137_quick_ratio_collapse_x_dd_d2(cashneq, receivables, liabilitiesc, close):
    qr = _safe_div(cashneq + receivables, liabilitiesc)
    qr_chg = qr - qr.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-qr_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_138_declining_book_value_x_declining_close_d2(equity, shareswadil, close):
    bps = _safe_div(equity, shareswadil)
    bps_chg = _safe_log(bps) - _safe_log(bps.shift(YDAYS))
    px_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return ((-bps_chg).clip(lower=0) * (-px_chg).clip(lower=0)).diff().diff()

def f50_tdcp_139_operating_loss_to_assets_x_dd_d2(opinc, assets, close):
    loss = _safe_div(-_ttm(opinc).clip(upper=0), assets)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (loss * (-dd)).diff().diff()

def f50_tdcp_140_net_debt_to_marketcap_x_drawdown_d2(debt, cashneq, marketcap, close):
    nd = debt - cashneq
    ratio = _safe_div(nd, marketcap)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (ratio * (-dd)).diff().diff()

def f50_tdcp_141_composite_short_blowup_z6_d2(netinc, ncfo, debt, equity, close, volume):
    z1 = -_rolling_zscore(_ttm(netinc), YDAYS)
    z2 = -_rolling_zscore(_ttm(ncfo), YDAYS)
    z3 = _rolling_zscore(_safe_div(debt, equity), YDAYS)
    z4 = -_rolling_zscore(close, YDAYS)
    z5 = _rolling_zscore(volume, YDAYS)
    z6 = -_rolling_zscore(equity, YDAYS)
    return (z1 + z2 + z3 + z4 + z5 + z6).diff().diff()

def f50_tdcp_142_retained_earnings_decline_speed_x_dd_d2(retearn, close):
    re_chg = _safe_div(retearn.diff(YDAYS), retearn.shift(YDAYS).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-re_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_143_equity_per_share_collapse_x_close_pctile_d2(equity, shareswadil, close):
    eps = _safe_div(equity, shareswadil)
    eps_chg = _safe_log(eps.replace(0, np.nan)) - _safe_log(eps.replace(0, np.nan).shift(YDAYS))
    c_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((-eps_chg).clip(lower=0) * (1.0 - c_p)).diff().diff()

def f50_tdcp_144_revenue_q_yield_decay_x_dd_d2(revenue, marketcap, close):
    ry = _safe_div(_ttm(revenue), marketcap)
    ry_chg = ry - ry.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-ry_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_145_investments_liquidation_x_dd_d2(investments, close):
    inv_chg = _safe_div(investments.diff(QDAYS), investments.shift(QDAYS).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-inv_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_146_loss_per_share_x_close_per_share_decay_d2(netinc, shareswadil, close):
    lps = _safe_div(-_ttm(netinc).clip(upper=0), shareswadil)
    px_decay = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (lps * (-px_decay)).diff().diff()

def f50_tdcp_147_debt_buildup_x_assetsturn_collapse_x_dd_d2(debt, revenue, assets, close):
    d_g = _yoy_pct(debt)
    at_r = _safe_div(_ttm(revenue), assets)
    at_chg = at_r - at_r.shift(YDAYS)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (d_g.clip(lower=0) * (-at_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_148_liab_to_marketcap_x_close_below_low_d2(liabilities, marketcap, close):
    ratio = _safe_div(liabilities, marketcap)
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    near_lo = (close < rmin * 1.10).astype(float)
    return (ratio * near_lo).diff().diff()

def f50_tdcp_149_ev_per_share_decay_x_dd_d2(marketcap, debt, cashneq, shareswadil, close):
    ev = marketcap + debt - cashneq
    eps = _safe_div(ev, shareswadil)
    eps_chg = _safe_log(eps.replace(0, np.nan)) - _safe_log(eps.replace(0, np.nan).shift(YDAYS))
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ((-eps_chg).clip(lower=0) * (-dd)).diff().diff()

def f50_tdcp_150_compound_terminal_decline_score_d2(netinc, ncfo, debt, marketcap, close, sharesbas):
    s1 = (_ttm(netinc) < 0).astype(float)
    s2 = (_ttm(ncfo) < 0).astype(float)
    s3 = (debt > marketcap).astype(float)
    s4 = (close < close.rolling(YDAYS, min_periods=QDAYS).max() * 0.5).astype(float)
    s5 = (sharesbas > sharesbas.shift(YDAYS)).astype(float)
    return (s1 + s2 + s3 + s4 + s5).diff().diff()


TERMINAL_DECLINE_COMPOSITE_D2_REGISTRY_076_150 = {
    "f50_tdcp_076_compound_stress_z_index_d2": {"inputs": ["debt", "equity", "ncfo", "revenue", "close"], "func": f50_tdcp_076_compound_stress_z_index_d2},
    "f50_tdcp_077_multi_pctile_distress_sum_d2": {"inputs": ["ncfo", "debt", "equity", "close"], "func": f50_tdcp_077_multi_pctile_distress_sum_d2},
    "f50_tdcp_078_two_yr_dual_deterioration_proxy_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_078_two_yr_dual_deterioration_proxy_d2},
    "f50_tdcp_079_triple_trend_decline_d2": {"inputs": ["revenue", "ncfo", "close"], "func": f50_tdcp_079_triple_trend_decline_d2},
    "f50_tdcp_080_zombie_proxy_neg_roe_high_lev_falling_rev_d2": {"inputs": ["netinc", "equity", "debt", "marketcap", "revenue"], "func": f50_tdcp_080_zombie_proxy_neg_roe_high_lev_falling_rev_d2},
    "f50_tdcp_081_multi_q_accel_loss_x_below_200d_d2": {"inputs": ["netinc", "close"], "func": f50_tdcp_081_multi_q_accel_loss_x_below_200d_d2},
    "f50_tdcp_082_regime_change_dual_flip_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_082_regime_change_dual_flip_d2},
    "f50_tdcp_083_trend_congruence_fundamentals_price_d2": {"inputs": ["ebitda", "close"], "func": f50_tdcp_083_trend_congruence_fundamentals_price_d2},
    "f50_tdcp_084_volatility_regime_instability_compound_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_084_volatility_regime_instability_compound_d2},
    "f50_tdcp_085_time_since_positive_fcf_x_dd_d2": {"inputs": ["fcf", "close"], "func": f50_tdcp_085_time_since_positive_fcf_x_dd_d2},
    "f50_tdcp_086_capitulation_volume_x_dd_x_burn_d2": {"inputs": ["volume", "close", "ncfo"], "func": f50_tdcp_086_capitulation_volume_x_dd_x_burn_d2},
    "f50_tdcp_087_liquidity_drying_composite_d2": {"inputs": ["volume", "marketcap", "high", "low", "close"], "func": f50_tdcp_087_liquidity_drying_composite_d2},
    "f50_tdcp_088_persistent_below_peak_x_fund_decline_d2": {"inputs": ["close", "revenue"], "func": f50_tdcp_088_persistent_below_peak_x_fund_decline_d2},
    "f50_tdcp_089_intangibles_share_erosion_x_dd_d2": {"inputs": ["intangibles", "assets", "close"], "func": f50_tdcp_089_intangibles_share_erosion_x_dd_d2},
    "f50_tdcp_090_tangible_book_collapse_x_dd_d2": {"inputs": ["equity", "intangibles", "close"], "func": f50_tdcp_090_tangible_book_collapse_x_dd_d2},
    "f50_tdcp_091_ppe_writedown_x_volume_capit_d2": {"inputs": ["ppnenet", "volume"], "func": f50_tdcp_091_ppe_writedown_x_volume_capit_d2},
    "f50_tdcp_092_depamor_jump_x_drawdown_d2": {"inputs": ["depamor", "close"], "func": f50_tdcp_092_depamor_jump_x_drawdown_d2},
    "f50_tdcp_093_intangibles_writedown_proxy_x_dd_d2": {"inputs": ["intangibles", "close"], "func": f50_tdcp_093_intangibles_writedown_proxy_x_dd_d2},
    "f50_tdcp_094_inventory_buildup_x_price_decline_d2": {"inputs": ["inventory", "close"], "func": f50_tdcp_094_inventory_buildup_x_price_decline_d2},
    "f50_tdcp_095_receivables_buildup_x_dd_d2": {"inputs": ["receivables", "revenue", "close"], "func": f50_tdcp_095_receivables_buildup_x_dd_d2},
    "f50_tdcp_096_asset_turnover_collapse_x_price_decline_d2": {"inputs": ["revenue", "assets", "close"], "func": f50_tdcp_096_asset_turnover_collapse_x_price_decline_d2},
    "f50_tdcp_097_payables_stretching_x_dd_d2": {"inputs": ["payables", "cor", "close"], "func": f50_tdcp_097_payables_stretching_x_dd_d2},
    "f50_tdcp_098_capex_collapse_x_dd_d2": {"inputs": ["capex", "close"], "func": f50_tdcp_098_capex_collapse_x_dd_d2},
    "f50_tdcp_099_rnd_decline_x_revenue_decline_x_price_decline_d2": {"inputs": ["rnd", "revenue", "close"], "func": f50_tdcp_099_rnd_decline_x_revenue_decline_x_price_decline_d2},
    "f50_tdcp_100_ncfi_invest_collapse_x_dd_d2": {"inputs": ["ncfi", "close"], "func": f50_tdcp_100_ncfi_invest_collapse_x_dd_d2},
    "f50_tdcp_101_ncff_financing_drying_up_x_dd_d2": {"inputs": ["ncff", "close"], "func": f50_tdcp_101_ncff_financing_drying_up_x_dd_d2},
    "f50_tdcp_102_inventory_revenue_divergence_x_price_d2": {"inputs": ["inventory", "revenue", "close"], "func": f50_tdcp_102_inventory_revenue_divergence_x_price_d2},
    "f50_tdcp_103_receivables_revenue_divergence_x_dd_d2": {"inputs": ["receivables", "revenue", "close"], "func": f50_tdcp_103_receivables_revenue_divergence_x_dd_d2},
    "f50_tdcp_104_close_pct_x_ncfo_pct_x_de_pct_d2": {"inputs": ["close", "ncfo", "debt", "equity"], "func": f50_tdcp_104_close_pct_x_ncfo_pct_x_de_pct_d2},
    "f50_tdcp_105_close_pct_low_x_burn_pct_high_d2": {"inputs": ["close", "ncfo"], "func": f50_tdcp_105_close_pct_low_x_burn_pct_high_d2},
    "f50_tdcp_106_marketcap_pctile_x_debt_pctile_d2": {"inputs": ["marketcap", "debt"], "func": f50_tdcp_106_marketcap_pctile_x_debt_pctile_d2},
    "f50_tdcp_107_revenue_pctile_low_x_close_pctile_low_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_107_revenue_pctile_low_x_close_pctile_low_d2},
    "f50_tdcp_108_equity_pctile_low_x_dd_d2": {"inputs": ["equity", "close"], "func": f50_tdcp_108_equity_pctile_low_x_dd_d2},
    "f50_tdcp_109_five_signal_distress_sum_d2": {"inputs": ["netinc", "ncfo", "workingcapital", "retearn", "close"], "func": f50_tdcp_109_five_signal_distress_sum_d2},
    "f50_tdcp_110_triple_quarterly_neg_x_price_below_low_d2": {"inputs": ["netinc", "ncfo", "ebit", "close"], "func": f50_tdcp_110_triple_quarterly_neg_x_price_below_low_d2},
    "f50_tdcp_111_stress_lookback_window_persistence_d2": {"inputs": ["netinc", "close"], "func": f50_tdcp_111_stress_lookback_window_persistence_d2},
    "f50_tdcp_112_ev_to_assets_collapse_x_dd_d2": {"inputs": ["marketcap", "debt", "cashneq", "assets", "close"], "func": f50_tdcp_112_ev_to_assets_collapse_x_dd_d2},
    "f50_tdcp_113_composite_distress_rank_sum_d2": {"inputs": ["debt", "equity", "ncfo", "close"], "func": f50_tdcp_113_composite_distress_rank_sum_d2},
    "f50_tdcp_114_acceleration_of_losses_x_dd_accel_d2": {"inputs": ["netinc", "close"], "func": f50_tdcp_114_acceleration_of_losses_x_dd_accel_d2},
    "f50_tdcp_115_multi_horizon_dual_decline_score_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_115_multi_horizon_dual_decline_score_d2},
    "f50_tdcp_116_price_below_50pct_high_x_neg_eps_persistent_d2": {"inputs": ["close", "netinc"], "func": f50_tdcp_116_price_below_50pct_high_x_neg_eps_persistent_d2},
    "f50_tdcp_117_fund_vol_x_price_vol_x_dd_d2": {"inputs": ["netinc", "close"], "func": f50_tdcp_117_fund_vol_x_price_vol_x_dd_d2},
    "f50_tdcp_118_margin_volatility_x_price_volatility_d2": {"inputs": ["opinc", "revenue", "close"], "func": f50_tdcp_118_margin_volatility_x_price_volatility_d2},
    "f50_tdcp_119_revenue_cv_x_intraday_range_cv_d2": {"inputs": ["revenue", "high", "low", "close"], "func": f50_tdcp_119_revenue_cv_x_intraday_range_cv_d2},
    "f50_tdcp_120_ebitda_vol_x_price_drawdown_severity_d2": {"inputs": ["ebitda", "close"], "func": f50_tdcp_120_ebitda_vol_x_price_drawdown_severity_d2},
    "f50_tdcp_121_erratic_revenue_x_erratic_close_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_121_erratic_revenue_x_erratic_close_d2},
    "f50_tdcp_122_debt_path_vol_x_price_vol_d2": {"inputs": ["debt", "close"], "func": f50_tdcp_122_debt_path_vol_x_price_vol_d2},
    "f50_tdcp_123_equity_vol_x_price_vol_x_dd_d2": {"inputs": ["equity", "close"], "func": f50_tdcp_123_equity_vol_x_price_vol_x_dd_d2},
    "f50_tdcp_124_operating_vol_proxy_x_drawdown_d2": {"inputs": ["opinc", "close"], "func": f50_tdcp_124_operating_vol_proxy_x_drawdown_d2},
    "f50_tdcp_125_cash_to_burn_quarters_x_volume_collapse_d2": {"inputs": ["cashneq", "ncfo", "volume"], "func": f50_tdcp_125_cash_to_burn_quarters_x_volume_collapse_d2},
    "f50_tdcp_126_disclosure_density_proxy_x_dd_d2": {"inputs": ["sharefactor", "marketcap", "close"], "func": f50_tdcp_126_disclosure_density_proxy_x_dd_d2},
    "f50_tdcp_127_composite_z_revenue_cash_close_d2": {"inputs": ["revenue", "cashneq", "close"], "func": f50_tdcp_127_composite_z_revenue_cash_close_d2},
    "f50_tdcp_128_fundamentals_low_pctile_x_price_low_pctile_d2": {"inputs": ["ebit", "close"], "func": f50_tdcp_128_fundamentals_low_pctile_x_price_low_pctile_d2},
    "f50_tdcp_129_price_velocity_x_fundamentals_velocity_d2": {"inputs": ["revenue", "close"], "func": f50_tdcp_129_price_velocity_x_fundamentals_velocity_d2},
    "f50_tdcp_130_price_below_ma200_persistence_x_burn_persistence_d2": {"inputs": ["close", "ncfo"], "func": f50_tdcp_130_price_below_ma200_persistence_x_burn_persistence_d2},
    "f50_tdcp_131_multi_quarter_loss_streak_x_drawdown_severity_d2": {"inputs": ["netinc", "close"], "func": f50_tdcp_131_multi_quarter_loss_streak_x_drawdown_severity_d2},
    "f50_tdcp_132_debt_growing_revenue_falling_price_falling_d2": {"inputs": ["debt", "revenue", "close"], "func": f50_tdcp_132_debt_growing_revenue_falling_price_falling_d2},
    "f50_tdcp_133_share_count_growth_x_revenue_per_share_decline_x_dd_d2": {"inputs": ["sharesbas", "revenue", "close"], "func": f50_tdcp_133_share_count_growth_x_revenue_per_share_decline_x_dd_d2},
    "f50_tdcp_134_operating_cycle_lengthening_x_dd_d2": {"inputs": ["inventory", "receivables", "cor", "revenue", "close"], "func": f50_tdcp_134_operating_cycle_lengthening_x_dd_d2},
    "f50_tdcp_135_equity_minus_intangibles_neg_x_dd_d2": {"inputs": ["equity", "intangibles", "close"], "func": f50_tdcp_135_equity_minus_intangibles_neg_x_dd_d2},
    "f50_tdcp_136_current_ratio_collapse_x_dd_d2": {"inputs": ["assetsc", "liabilitiesc", "close"], "func": f50_tdcp_136_current_ratio_collapse_x_dd_d2},
    "f50_tdcp_137_quick_ratio_collapse_x_dd_d2": {"inputs": ["cashneq", "receivables", "liabilitiesc", "close"], "func": f50_tdcp_137_quick_ratio_collapse_x_dd_d2},
    "f50_tdcp_138_declining_book_value_x_declining_close_d2": {"inputs": ["equity", "shareswadil", "close"], "func": f50_tdcp_138_declining_book_value_x_declining_close_d2},
    "f50_tdcp_139_operating_loss_to_assets_x_dd_d2": {"inputs": ["opinc", "assets", "close"], "func": f50_tdcp_139_operating_loss_to_assets_x_dd_d2},
    "f50_tdcp_140_net_debt_to_marketcap_x_drawdown_d2": {"inputs": ["debt", "cashneq", "marketcap", "close"], "func": f50_tdcp_140_net_debt_to_marketcap_x_drawdown_d2},
    "f50_tdcp_141_composite_short_blowup_z6_d2": {"inputs": ["netinc", "ncfo", "debt", "equity", "close", "volume"], "func": f50_tdcp_141_composite_short_blowup_z6_d2},
    "f50_tdcp_142_retained_earnings_decline_speed_x_dd_d2": {"inputs": ["retearn", "close"], "func": f50_tdcp_142_retained_earnings_decline_speed_x_dd_d2},
    "f50_tdcp_143_equity_per_share_collapse_x_close_pctile_d2": {"inputs": ["equity", "shareswadil", "close"], "func": f50_tdcp_143_equity_per_share_collapse_x_close_pctile_d2},
    "f50_tdcp_144_revenue_q_yield_decay_x_dd_d2": {"inputs": ["revenue", "marketcap", "close"], "func": f50_tdcp_144_revenue_q_yield_decay_x_dd_d2},
    "f50_tdcp_145_investments_liquidation_x_dd_d2": {"inputs": ["investments", "close"], "func": f50_tdcp_145_investments_liquidation_x_dd_d2},
    "f50_tdcp_146_loss_per_share_x_close_per_share_decay_d2": {"inputs": ["netinc", "shareswadil", "close"], "func": f50_tdcp_146_loss_per_share_x_close_per_share_decay_d2},
    "f50_tdcp_147_debt_buildup_x_assetsturn_collapse_x_dd_d2": {"inputs": ["debt", "revenue", "assets", "close"], "func": f50_tdcp_147_debt_buildup_x_assetsturn_collapse_x_dd_d2},
    "f50_tdcp_148_liab_to_marketcap_x_close_below_low_d2": {"inputs": ["liabilities", "marketcap", "close"], "func": f50_tdcp_148_liab_to_marketcap_x_close_below_low_d2},
    "f50_tdcp_149_ev_per_share_decay_x_dd_d2": {"inputs": ["marketcap", "debt", "cashneq", "shareswadil", "close"], "func": f50_tdcp_149_ev_per_share_decay_x_dd_d2},
    "f50_tdcp_150_compound_terminal_decline_score_d2": {"inputs": ["netinc", "ncfo", "debt", "marketcap", "close", "sharesbas"], "func": f50_tdcp_150_compound_terminal_decline_score_d2},
}
