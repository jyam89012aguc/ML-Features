"""terminal_decline_composite base features 001_075 — Pipeline 1a-inverse short-side blowup family (capstone #50/50).

Multi-source COMPOSITE signals (SF1 + SEP + ACTIONS) for terminal-decline detection.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
SF1 inputs arrive daily-forward-filled by the harness.
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

def f50_tdcp_001_neg_eps_streak_x_lo252_proxy(netinc, shareswadil, close):
    eps = _safe_div(netinc, shareswadil)
    neg = (eps < 0).astype(float)
    streak = neg.rolling(8, min_periods=2).sum()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    px_pos = _safe_div(close - rmin, rmax - rmin)
    return streak * (1.0 - px_pos)

def f50_tdcp_002_netloss_q_x_close_below_200d_ma(netinc, close):
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    loss_intensity = (-netinc).clip(lower=0)
    return loss_intensity * below

def f50_tdcp_003_ocf_neg_x_dist_below_252d_high(ncfo, close):
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    burn = (-ncfo).clip(lower=0)
    return _safe_div(burn, burn.abs() + 1.0) * dd

def f50_tdcp_004_fcf_neg_streak_x_drawdown(fcf, close):
    neg = (fcf < 0).astype(float).rolling(8, min_periods=2).sum()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    return neg * (-dd)

def f50_tdcp_005_margin_collapse_x_price_decay(opinc, revenue, close):
    margin = _safe_div(_ttm(opinc), _ttm(revenue))
    margin_chg = margin - margin.shift(QDAYS)
    px_chg = _safe_log(close) - _safe_log(close.shift(QDAYS))
    return margin_chg * px_chg

def f50_tdcp_006_debt_to_equity_x_dist_below_52w_high(debt, equity, close):
    leverage = _safe_div(debt, equity)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    return leverage * (-dd)

def f50_tdcp_007_interest_coverage_collapse_x_atr_expansion(ebit, intexp, high, low, close):
    cov = _safe_div(_ttm(ebit), _ttm(intexp).abs())
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr_q = tr.rolling(QDAYS, min_periods=MDAYS).mean()
    atr_y = tr.rolling(YDAYS, min_periods=QDAYS).mean()
    atr_ratio = _safe_div(atr_q, atr_y)
    return _safe_div(atr_ratio, cov.clip(lower=0.1))

def f50_tdcp_008_retained_earnings_negative_x_drawdown(retearn, close):
    neg = (retearn < 0).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    return neg * (-dd)

def f50_tdcp_009_eps_negative_x_pct_below_high(netinc, shareswadil, high):
    eps = _safe_div(netinc, shareswadil)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pct_below = _safe_div(rmax - high, rmax)
    return (eps < 0).astype(float) * pct_below

def f50_tdcp_010_revenue_decline_yoy_x_price_decline_yoy(revenue, close):
    rev_yoy = _safe_div(_ttm(revenue) - _ttm(revenue).shift(YDAYS), _ttm(revenue).shift(YDAYS).abs())
    px_yoy = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (-rev_yoy).clip(lower=0) * (-px_yoy).clip(lower=0)

def f50_tdcp_011_gp_collapse_x_volume_capitulation(gp, volume):
    gp_chg = _safe_div(_ttm(gp) - _ttm(gp).shift(QDAYS), _ttm(gp).shift(QDAYS).abs())
    vol_z = _rolling_zscore(volume, YDAYS)
    return (-gp_chg).clip(lower=0) * vol_z

def f50_tdcp_012_opcf_to_debt_collapse_x_close_decay(ncfo, debt, close):
    cov = _safe_div(_ttm(ncfo), debt)
    px_decay = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return cov * px_decay

def f50_tdcp_013_workingcap_neg_x_below_200d(workingcapital, close):
    neg = (workingcapital < 0).astype(float)
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    return neg * below

def f50_tdcp_014_liab_gt_assets_x_drawdown(liabilities, assets, close):
    insolv = (liabilities > assets).astype(float)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    return insolv * (-dd)

def f50_tdcp_015_cashneq_decline_x_price_decline_horizon(cashneq, close):
    cash_chg = _safe_div(cashneq - cashneq.shift(YDAYS), cashneq.shift(YDAYS).abs())
    px_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (-cash_chg).clip(lower=0) * (-px_chg).clip(lower=0)

def f50_tdcp_016_assets_decline_x_marketcap_collapse(assets, marketcap):
    a_chg = _safe_div(assets - assets.shift(YDAYS), assets.shift(YDAYS).abs())
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    return (-a_chg).clip(lower=0) * (-mc_chg).clip(lower=0)

def f50_tdcp_017_equity_erosion_x_price_erosion(equity, close):
    eq_chg = _safe_div(equity - equity.shift(YDAYS), equity.shift(YDAYS).abs())
    px_chg = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (-eq_chg) * (-px_chg)

def f50_tdcp_018_rev_qoq_drop_x_intraday_range_widen(revenue, high, low, close):
    rev_q = _safe_div(revenue.diff(), revenue.shift(QDAYS).abs())
    rng = _safe_div(high - low, close)
    rng_z = _rolling_zscore(rng, QDAYS)
    return (-rev_q).clip(lower=0) * rng_z

def f50_tdcp_019_ebitda_decline_x_close_below_50d(ebitda, close):
    e_chg = _safe_div(_ttm(ebitda) - _ttm(ebitda).shift(QDAYS), _ttm(ebitda).shift(QDAYS).abs())
    ma50 = close.rolling(50, min_periods=21).mean()
    below = (close < ma50).astype(float)
    return (-e_chg).clip(lower=0) * below

def f50_tdcp_020_opex_growth_x_revenue_decline_x_price_decline(opex, revenue, close):
    opex_g = _yoy_pct(_ttm(opex))
    rev_g = _yoy_pct(_ttm(revenue))
    px_g = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (opex_g - rev_g).clip(lower=0) * (-px_g).clip(lower=0)

def f50_tdcp_021_cash_runway_months_x_drawdown(cashneq, ncfo, close):
    burn = (-_ttm(ncfo)).clip(lower=0)
    runway = _safe_div(cashneq * 12.0, burn)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    return _safe_div(-dd, runway.clip(lower=0.5))

def f50_tdcp_022_burn_to_marketcap_ratio(ncfo, marketcap):
    burn = (-_ttm(ncfo)).clip(lower=0)
    return _safe_div(burn, marketcap)

def f50_tdcp_023_oploss_to_marketcap(opinc, marketcap):
    loss = (-_ttm(opinc)).clip(lower=0)
    return _safe_div(loss, marketcap)

def f50_tdcp_024_netloss_to_marketcap(netinc, marketcap):
    loss = (-_ttm(netinc)).clip(lower=0)
    return _safe_div(loss, marketcap)

def f50_tdcp_025_mc_collapse_with_debt_intact(marketcap, debt):
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    d_chg = _safe_log(debt.replace(0, np.nan)) - _safe_log(debt.replace(0, np.nan).shift(YDAYS))
    return (-mc_chg).clip(lower=0) - d_chg.fillna(0).clip(upper=0)

def f50_tdcp_026_burn_accel_x_mc_decline(ncfo, marketcap):
    burn = (-_ttm(ncfo)).clip(lower=0)
    burn_chg = burn.diff(QDAYS)
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(QDAYS))
    return burn_chg.clip(lower=0) * (-mc_chg).clip(lower=0)

def f50_tdcp_027_ev_to_revenue_collapse(marketcap, debt, cashneq, revenue):
    ev = marketcap + debt - cashneq
    return _safe_div(ev, _ttm(revenue))

def f50_tdcp_028_ev_change_x_revenue_change(marketcap, debt, cashneq, revenue):
    ev = marketcap + debt - cashneq
    ev_chg = _safe_log(ev.replace(0, np.nan)) - _safe_log(ev.replace(0, np.nan).shift(YDAYS))
    rev_chg = _yoy_pct(_ttm(revenue))
    return ev_chg * rev_chg

def f50_tdcp_029_cash_burn_quarters_until_zero_x_dd(cashneq, ncfo, close):
    burn_q = (-ncfo).clip(lower=0)
    q_left = _safe_div(cashneq, burn_q)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return _safe_div(-dd, q_left.clip(lower=0.5))

def f50_tdcp_030_debt_due_vs_cash_x_drawdown(debtc, cashneq, close):
    cover = _safe_div(debtc, cashneq)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return cover * (-dd)

def f50_tdcp_031_liquidity_gap_x_volume_decline(cashneq, liabilitiesc, volume):
    gap = _safe_div(liabilitiesc - cashneq, liabilitiesc.abs() + cashneq.abs())
    vol_chg = _safe_log(volume.replace(0, np.nan).rolling(MDAYS, min_periods=5).mean()) - _safe_log(volume.replace(0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean())
    return gap * (-vol_chg).clip(lower=0)

def f50_tdcp_032_fcf_yield_negative_x_dd(fcf, marketcap, close):
    fcy = _safe_div(_ttm(fcf), marketcap)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return (-fcy).clip(lower=0) * (-dd)

def f50_tdcp_033_cash_decline_speed_x_mc_decline_speed(cashneq, marketcap):
    c_speed = _safe_div(cashneq.diff(QDAYS), cashneq.shift(QDAYS).abs())
    m_speed = _safe_log(marketcap) - _safe_log(marketcap.shift(QDAYS))
    return (-c_speed).clip(lower=0) * (-m_speed).clip(lower=0)

def f50_tdcp_034_debt_to_ebitda_x_intraday_range_widen(debt, ebitda, high, low, close):
    lev = _safe_div(debt, _ttm(ebitda).abs())
    rng = _safe_div(high - low, close)
    rng_z = _rolling_zscore(rng, QDAYS)
    return lev * rng_z.clip(lower=0)

def f50_tdcp_035_intexp_to_ebit_x_atr_widen(intexp, ebit, high, low, close):
    burden = _safe_div(_ttm(intexp).abs(), _ttm(ebit).abs())
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr_z = _rolling_zscore(tr.rolling(MDAYS, min_periods=5).mean(), QDAYS)
    return burden * atr_z.clip(lower=0)

def f50_tdcp_036_debt_growth_x_close_decline(debt, close):
    d_g = _yoy_pct(debt)
    c_g = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return d_g.clip(lower=0) * (-c_g).clip(lower=0)

def f50_tdcp_037_debtnc_growth_x_drawdown(debtnc, close):
    d_g = _yoy_pct(debtnc)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return d_g.clip(lower=0) * (-dd)

def f50_tdcp_038_coverage_decline_speed_x_volume_spike(ebit, intexp, volume):
    cov = _safe_div(_ttm(ebit), _ttm(intexp).abs())
    cov_chg = cov.diff(QDAYS)
    v_spike = _rolling_zscore(volume, QDAYS)
    return (-cov_chg).clip(lower=0) * v_spike.clip(lower=0)

def f50_tdcp_039_intexp_growth_x_revenue_decline_x_close_decline(intexp, revenue, close):
    ie_g = _yoy_pct(_ttm(intexp))
    rv_g = _yoy_pct(_ttm(revenue))
    cx = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return ie_g.clip(lower=0) * (-rv_g).clip(lower=0) * (-cx).clip(lower=0)

def f50_tdcp_040_debt_to_marketcap_x_volume_decay(debt, marketcap, volume):
    ratio = _safe_div(debt, marketcap)
    v_chg = _safe_log(volume.replace(0, np.nan).rolling(MDAYS, min_periods=5).mean()) - _safe_log(volume.replace(0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean())
    return ratio * (-v_chg).clip(lower=0)

def f50_tdcp_041_debt_minus_cash_per_share_x_dd(debt, cashneq, shareswadil, close):
    net_debt_ps = _safe_div(debt - cashneq, shareswadil)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return net_debt_ps * (-dd)

def f50_tdcp_042_ebit_to_intexp_below1_persist_x_dd(ebit, intexp, close):
    cov = _safe_div(_ttm(ebit), _ttm(intexp).abs())
    bad = (cov < 1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return bad * (-dd)

def f50_tdcp_043_net_debt_growth_x_marketcap_decline(debt, cashneq, marketcap):
    nd = debt - cashneq
    nd_chg = _safe_div(nd - nd.shift(YDAYS), nd.shift(YDAYS).abs())
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    return nd_chg.clip(lower=0) * (-mc_chg).clip(lower=0)

def f50_tdcp_044_debtc_to_cash_persist_above1_x_below_ma(debtc, cashneq, close):
    cover = _safe_div(debtc, cashneq)
    bad = (cover > 1.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    return bad * below

def f50_tdcp_045_liab_to_ebitda_collapse_x_dd(liabilities, ebitda, close):
    ratio = _safe_div(liabilities, _ttm(ebitda).abs())
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return ratio * (-dd)

def f50_tdcp_046_debt_ttm_chg_neg_ebit_x_dd(debt, ebit, close):
    d_chg = debt.diff(YDAYS)
    neg_ebit = (_ttm(ebit) < 0).astype(float)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return d_chg.clip(lower=0) * neg_ebit * (-dd)

def f50_tdcp_047_sharesbas_growth_x_close_to_52w_high(sharesbas, close):
    sg = _yoy_pct(sharesbas)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ratio = _safe_div(close, rmax)
    return sg.clip(lower=0) * (1.0 - ratio)

def f50_tdcp_048_shareswadil_growth_x_drawdown(shareswadil, close):
    sg = _yoy_pct(shareswadil)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return sg.clip(lower=0) * (-dd)

def f50_tdcp_049_sbcomp_to_marketcap_x_dd(sbcomp, marketcap, close):
    burn = _safe_div(_ttm(sbcomp).abs(), marketcap)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return burn * (-dd)

def f50_tdcp_050_sbcomp_share_of_revenue_x_below_ma(sbcomp, revenue, close):
    share = _safe_div(_ttm(sbcomp).abs(), _ttm(revenue))
    ma = close.rolling(200, min_periods=63).mean()
    below = (close < ma).astype(float)
    return share * below

def f50_tdcp_051_shares_growth_x_volume_decline(sharesbas, volume):
    sg = _yoy_pct(sharesbas)
    v_chg = _safe_log(volume.replace(0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()) - _safe_log(volume.replace(0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean())
    return sg.clip(lower=0) * (-v_chg).clip(lower=0)

def f50_tdcp_052_market_cap_per_share_compression(marketcap, sharesbas):
    mcps = _safe_div(marketcap, sharesbas)
    return _safe_log(mcps) - _safe_log(mcps.rolling(YDAYS, min_periods=QDAYS).max())

def f50_tdcp_053_buyback_reversal_x_dd(sharesbas, close):
    s_q = sharesbas.diff(QDAYS)
    rising = (s_q > 0).astype(float)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return rising * (-dd)

def f50_tdcp_054_dilution_accel_x_drawdown_accel(sharesbas, close):
    s_g = sharesbas.diff(QDAYS)
    s_accel = s_g - s_g.shift(QDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_log(close) - _safe_log(rmax)
    dd_chg = dd - dd.shift(QDAYS)
    return s_accel.clip(lower=0) * (-dd_chg).clip(lower=0)

def f50_tdcp_055_rev_per_share_decline_x_close_decline(revenue, shareswadil, close):
    rps = _safe_div(_ttm(revenue), shareswadil)
    rps_chg = _safe_log(rps) - _safe_log(rps.shift(YDAYS))
    cx = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (-rps_chg).clip(lower=0) * (-cx).clip(lower=0)

def f50_tdcp_056_bps_decline_x_pb_decline(equity, shareswa, marketcap):
    bps = _safe_div(equity, shareswa)
    pb = _safe_div(_safe_div(marketcap, shareswa), bps)
    bps_chg = _safe_log(bps) - _safe_log(bps.shift(YDAYS))
    pb_chg = _safe_log(pb) - _safe_log(pb.shift(YDAYS))
    return (-bps_chg).clip(lower=0) * (-pb_chg).clip(lower=0)

def f50_tdcp_057_issuance_pressure_x_low_volume_proxy(sharesbas, volume):
    iss = sharesbas.diff(QDAYS).clip(lower=0)
    vol_p = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(iss, vol_p)

def f50_tdcp_058_dilution_to_mc_chg_ratio(sharesbas, marketcap):
    sg = _yoy_pct(sharesbas)
    mc_g = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    return _safe_div(sg.clip(lower=0), (-mc_g).clip(lower=0.01))

def f50_tdcp_059_dilution_persistence_x_dd_persistence(sharesbas, close):
    sd = sharesbas.diff()
    pos = (sd > 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    bad_px = (close < rmax * 0.7).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return pos * bad_px

def f50_tdcp_060_sbcomp_growth_x_revenue_decline_x_price_decline(sbcomp, revenue, close):
    s_g = _yoy_pct(_ttm(sbcomp).abs())
    r_g = _yoy_pct(_ttm(revenue))
    p_g = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return s_g.clip(lower=0) * (-r_g).clip(lower=0) * (-p_g).clip(lower=0)

def f50_tdcp_061_sharefactor_jump_x_close_collapse(sharefactor, close):
    sf_jump = _safe_div(sharefactor.diff().abs(), sharefactor.shift(1).abs())
    sf_event = (sf_jump > 0.05).astype(float)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return sf_event * (-dd)

def f50_tdcp_062_sharefactor_persistence_post_event(sharefactor):
    sf_jump = _safe_div(sharefactor.diff().abs(), sharefactor.shift(1).abs())
    event = (sf_jump > 0.05).astype(float)
    return event.rolling(YDAYS, min_periods=QDAYS).sum()

def f50_tdcp_063_post_split_decay_proxy(sharefactor, close):
    sf_jump = _safe_div(sharefactor.diff().abs(), sharefactor.shift(1).abs())
    event_recent = (sf_jump > 0.05).astype(float).rolling(QDAYS, min_periods=5).sum()
    px_chg = _safe_log(close) - _safe_log(close.shift(QDAYS))
    return event_recent * (-px_chg)

def f50_tdcp_064_reverse_split_proxy_x_drawdown(sharefactor, sharesbas, close):
    sf_jump = _safe_div(sharefactor.diff(), sharefactor.shift(1).abs())
    s_drop = sharesbas.diff() < 0
    rs_event = ((sf_jump.abs() > 0.05) & s_drop).astype(float)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return rs_event.rolling(QDAYS, min_periods=5).sum() * (-dd)

def f50_tdcp_065_sharefactor_volatility_x_price_volatility(sharefactor, close):
    sf_v = sharefactor.diff().abs().rolling(YDAYS, min_periods=QDAYS).std()
    px_ret = _safe_log(close).diff()
    px_v = px_ret.rolling(YDAYS, min_periods=QDAYS).std()
    return sf_v * px_v

def f50_tdcp_066_compound_action_density_x_price_decay(sharefactor, close):
    sf_event = (sharefactor.diff().abs() > 1e-6).astype(float)
    density = sf_event.rolling(YDAYS, min_periods=QDAYS).sum()
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return density * (-dd)

def f50_tdcp_067_sharefactor_jump_x_negative_eps(sharefactor, netinc):
    sf_event = (sharefactor.diff().abs() > 0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = (_ttm(netinc) < 0).astype(float)
    return sf_event * neg

def f50_tdcp_068_sharefactor_jump_x_high_leverage(sharefactor, debt, equity):
    sf_event = (sharefactor.diff().abs() > 0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    lev = _safe_div(debt, equity)
    return sf_event * lev

def f50_tdcp_069_sharefactor_recency_x_dd(sharefactor, close):
    sf_event = (sharefactor.diff().abs() > 0.05).astype(float)
    def _bsm(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) == 0:
            return np.nan
        return (len(w) - 1) - int(idx[-1])
    recency = sf_event.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return _safe_div(-dd, recency.clip(lower=1.0))

def f50_tdcp_070_multiple_actions_year_x_collapse(sharefactor, marketcap):
    sf_event = (sharefactor.diff().abs() > 1e-6).astype(float)
    n_events = sf_event.rolling(YDAYS, min_periods=QDAYS).sum()
    mc_chg = _safe_log(marketcap) - _safe_log(marketcap.shift(YDAYS))
    return n_events * (-mc_chg).clip(lower=0)

def f50_tdcp_071_dividend_cut_proxy_x_dd(sharefactor, close, equity):
    # heuristic dividend cut proxy: equity declines sharply while sharefactor unchanged
    sf_stable = (sharefactor.diff().abs() < 1e-6).astype(float)
    eq_chg = _safe_div(equity.diff(QDAYS), equity.shift(QDAYS).abs())
    cut = sf_stable * (-eq_chg).clip(lower=0)
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return cut * (-dd)

def f50_tdcp_072_sharefactor_change_x_revenue_decline(sharefactor, revenue):
    sf_change = sharefactor.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    r_chg = _yoy_pct(_ttm(revenue))
    return sf_change * (-r_chg).clip(lower=0)

def f50_tdcp_073_event_density_x_low_marketcap(sharefactor, marketcap):
    density = (sharefactor.diff().abs() > 1e-6).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    mc_log = _safe_log(marketcap)
    mc_pctile = mc_log.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return density * (1.0 - mc_pctile)

def f50_tdcp_074_going_concern_triple_neg(workingcapital, cashneq, retearn):
    wc_n = (workingcapital < 0).astype(float)
    cash_low = (cashneq < cashneq.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)).astype(float)
    re_n = (retearn < 0).astype(float)
    return wc_n + cash_low + re_n

def f50_tdcp_075_altman_z_proxy_with_price_overlay(workingcapital, assets, retearn, ebit, marketcap, liabilities, revenue, close):
    A = _safe_div(workingcapital, assets)
    B = _safe_div(retearn, assets)
    C = _safe_div(_ttm(ebit), assets)
    D = _safe_div(marketcap, liabilities)
    E = _safe_div(_ttm(revenue), assets)
    z = 1.2 * A + 1.4 * B + 3.3 * C + 0.6 * D + 1.0 * E
    dd = _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())
    return -z * (-dd)


TERMINAL_DECLINE_COMPOSITE_BASE_REGISTRY_001_075 = {
    "f50_tdcp_001_neg_eps_streak_x_lo252_proxy": {"inputs": ["netinc", "shareswadil", "close"], "func": f50_tdcp_001_neg_eps_streak_x_lo252_proxy},
    "f50_tdcp_002_netloss_q_x_close_below_200d_ma": {"inputs": ["netinc", "close"], "func": f50_tdcp_002_netloss_q_x_close_below_200d_ma},
    "f50_tdcp_003_ocf_neg_x_dist_below_252d_high": {"inputs": ["ncfo", "close"], "func": f50_tdcp_003_ocf_neg_x_dist_below_252d_high},
    "f50_tdcp_004_fcf_neg_streak_x_drawdown": {"inputs": ["fcf", "close"], "func": f50_tdcp_004_fcf_neg_streak_x_drawdown},
    "f50_tdcp_005_margin_collapse_x_price_decay": {"inputs": ["opinc", "revenue", "close"], "func": f50_tdcp_005_margin_collapse_x_price_decay},
    "f50_tdcp_006_debt_to_equity_x_dist_below_52w_high": {"inputs": ["debt", "equity", "close"], "func": f50_tdcp_006_debt_to_equity_x_dist_below_52w_high},
    "f50_tdcp_007_interest_coverage_collapse_x_atr_expansion": {"inputs": ["ebit", "intexp", "high", "low", "close"], "func": f50_tdcp_007_interest_coverage_collapse_x_atr_expansion},
    "f50_tdcp_008_retained_earnings_negative_x_drawdown": {"inputs": ["retearn", "close"], "func": f50_tdcp_008_retained_earnings_negative_x_drawdown},
    "f50_tdcp_009_eps_negative_x_pct_below_high": {"inputs": ["netinc", "shareswadil", "high"], "func": f50_tdcp_009_eps_negative_x_pct_below_high},
    "f50_tdcp_010_revenue_decline_yoy_x_price_decline_yoy": {"inputs": ["revenue", "close"], "func": f50_tdcp_010_revenue_decline_yoy_x_price_decline_yoy},
    "f50_tdcp_011_gp_collapse_x_volume_capitulation": {"inputs": ["gp", "volume"], "func": f50_tdcp_011_gp_collapse_x_volume_capitulation},
    "f50_tdcp_012_opcf_to_debt_collapse_x_close_decay": {"inputs": ["ncfo", "debt", "close"], "func": f50_tdcp_012_opcf_to_debt_collapse_x_close_decay},
    "f50_tdcp_013_workingcap_neg_x_below_200d": {"inputs": ["workingcapital", "close"], "func": f50_tdcp_013_workingcap_neg_x_below_200d},
    "f50_tdcp_014_liab_gt_assets_x_drawdown": {"inputs": ["liabilities", "assets", "close"], "func": f50_tdcp_014_liab_gt_assets_x_drawdown},
    "f50_tdcp_015_cashneq_decline_x_price_decline_horizon": {"inputs": ["cashneq", "close"], "func": f50_tdcp_015_cashneq_decline_x_price_decline_horizon},
    "f50_tdcp_016_assets_decline_x_marketcap_collapse": {"inputs": ["assets", "marketcap"], "func": f50_tdcp_016_assets_decline_x_marketcap_collapse},
    "f50_tdcp_017_equity_erosion_x_price_erosion": {"inputs": ["equity", "close"], "func": f50_tdcp_017_equity_erosion_x_price_erosion},
    "f50_tdcp_018_rev_qoq_drop_x_intraday_range_widen": {"inputs": ["revenue", "high", "low", "close"], "func": f50_tdcp_018_rev_qoq_drop_x_intraday_range_widen},
    "f50_tdcp_019_ebitda_decline_x_close_below_50d": {"inputs": ["ebitda", "close"], "func": f50_tdcp_019_ebitda_decline_x_close_below_50d},
    "f50_tdcp_020_opex_growth_x_revenue_decline_x_price_decline": {"inputs": ["opex", "revenue", "close"], "func": f50_tdcp_020_opex_growth_x_revenue_decline_x_price_decline},
    "f50_tdcp_021_cash_runway_months_x_drawdown": {"inputs": ["cashneq", "ncfo", "close"], "func": f50_tdcp_021_cash_runway_months_x_drawdown},
    "f50_tdcp_022_burn_to_marketcap_ratio": {"inputs": ["ncfo", "marketcap"], "func": f50_tdcp_022_burn_to_marketcap_ratio},
    "f50_tdcp_023_oploss_to_marketcap": {"inputs": ["opinc", "marketcap"], "func": f50_tdcp_023_oploss_to_marketcap},
    "f50_tdcp_024_netloss_to_marketcap": {"inputs": ["netinc", "marketcap"], "func": f50_tdcp_024_netloss_to_marketcap},
    "f50_tdcp_025_mc_collapse_with_debt_intact": {"inputs": ["marketcap", "debt"], "func": f50_tdcp_025_mc_collapse_with_debt_intact},
    "f50_tdcp_026_burn_accel_x_mc_decline": {"inputs": ["ncfo", "marketcap"], "func": f50_tdcp_026_burn_accel_x_mc_decline},
    "f50_tdcp_027_ev_to_revenue_collapse": {"inputs": ["marketcap", "debt", "cashneq", "revenue"], "func": f50_tdcp_027_ev_to_revenue_collapse},
    "f50_tdcp_028_ev_change_x_revenue_change": {"inputs": ["marketcap", "debt", "cashneq", "revenue"], "func": f50_tdcp_028_ev_change_x_revenue_change},
    "f50_tdcp_029_cash_burn_quarters_until_zero_x_dd": {"inputs": ["cashneq", "ncfo", "close"], "func": f50_tdcp_029_cash_burn_quarters_until_zero_x_dd},
    "f50_tdcp_030_debt_due_vs_cash_x_drawdown": {"inputs": ["debtc", "cashneq", "close"], "func": f50_tdcp_030_debt_due_vs_cash_x_drawdown},
    "f50_tdcp_031_liquidity_gap_x_volume_decline": {"inputs": ["cashneq", "liabilitiesc", "volume"], "func": f50_tdcp_031_liquidity_gap_x_volume_decline},
    "f50_tdcp_032_fcf_yield_negative_x_dd": {"inputs": ["fcf", "marketcap", "close"], "func": f50_tdcp_032_fcf_yield_negative_x_dd},
    "f50_tdcp_033_cash_decline_speed_x_mc_decline_speed": {"inputs": ["cashneq", "marketcap"], "func": f50_tdcp_033_cash_decline_speed_x_mc_decline_speed},
    "f50_tdcp_034_debt_to_ebitda_x_intraday_range_widen": {"inputs": ["debt", "ebitda", "high", "low", "close"], "func": f50_tdcp_034_debt_to_ebitda_x_intraday_range_widen},
    "f50_tdcp_035_intexp_to_ebit_x_atr_widen": {"inputs": ["intexp", "ebit", "high", "low", "close"], "func": f50_tdcp_035_intexp_to_ebit_x_atr_widen},
    "f50_tdcp_036_debt_growth_x_close_decline": {"inputs": ["debt", "close"], "func": f50_tdcp_036_debt_growth_x_close_decline},
    "f50_tdcp_037_debtnc_growth_x_drawdown": {"inputs": ["debtnc", "close"], "func": f50_tdcp_037_debtnc_growth_x_drawdown},
    "f50_tdcp_038_coverage_decline_speed_x_volume_spike": {"inputs": ["ebit", "intexp", "volume"], "func": f50_tdcp_038_coverage_decline_speed_x_volume_spike},
    "f50_tdcp_039_intexp_growth_x_revenue_decline_x_close_decline": {"inputs": ["intexp", "revenue", "close"], "func": f50_tdcp_039_intexp_growth_x_revenue_decline_x_close_decline},
    "f50_tdcp_040_debt_to_marketcap_x_volume_decay": {"inputs": ["debt", "marketcap", "volume"], "func": f50_tdcp_040_debt_to_marketcap_x_volume_decay},
    "f50_tdcp_041_debt_minus_cash_per_share_x_dd": {"inputs": ["debt", "cashneq", "shareswadil", "close"], "func": f50_tdcp_041_debt_minus_cash_per_share_x_dd},
    "f50_tdcp_042_ebit_to_intexp_below1_persist_x_dd": {"inputs": ["ebit", "intexp", "close"], "func": f50_tdcp_042_ebit_to_intexp_below1_persist_x_dd},
    "f50_tdcp_043_net_debt_growth_x_marketcap_decline": {"inputs": ["debt", "cashneq", "marketcap"], "func": f50_tdcp_043_net_debt_growth_x_marketcap_decline},
    "f50_tdcp_044_debtc_to_cash_persist_above1_x_below_ma": {"inputs": ["debtc", "cashneq", "close"], "func": f50_tdcp_044_debtc_to_cash_persist_above1_x_below_ma},
    "f50_tdcp_045_liab_to_ebitda_collapse_x_dd": {"inputs": ["liabilities", "ebitda", "close"], "func": f50_tdcp_045_liab_to_ebitda_collapse_x_dd},
    "f50_tdcp_046_debt_ttm_chg_neg_ebit_x_dd": {"inputs": ["debt", "ebit", "close"], "func": f50_tdcp_046_debt_ttm_chg_neg_ebit_x_dd},
    "f50_tdcp_047_sharesbas_growth_x_close_to_52w_high": {"inputs": ["sharesbas", "close"], "func": f50_tdcp_047_sharesbas_growth_x_close_to_52w_high},
    "f50_tdcp_048_shareswadil_growth_x_drawdown": {"inputs": ["shareswadil", "close"], "func": f50_tdcp_048_shareswadil_growth_x_drawdown},
    "f50_tdcp_049_sbcomp_to_marketcap_x_dd": {"inputs": ["sbcomp", "marketcap", "close"], "func": f50_tdcp_049_sbcomp_to_marketcap_x_dd},
    "f50_tdcp_050_sbcomp_share_of_revenue_x_below_ma": {"inputs": ["sbcomp", "revenue", "close"], "func": f50_tdcp_050_sbcomp_share_of_revenue_x_below_ma},
    "f50_tdcp_051_shares_growth_x_volume_decline": {"inputs": ["sharesbas", "volume"], "func": f50_tdcp_051_shares_growth_x_volume_decline},
    "f50_tdcp_052_market_cap_per_share_compression": {"inputs": ["marketcap", "sharesbas"], "func": f50_tdcp_052_market_cap_per_share_compression},
    "f50_tdcp_053_buyback_reversal_x_dd": {"inputs": ["sharesbas", "close"], "func": f50_tdcp_053_buyback_reversal_x_dd},
    "f50_tdcp_054_dilution_accel_x_drawdown_accel": {"inputs": ["sharesbas", "close"], "func": f50_tdcp_054_dilution_accel_x_drawdown_accel},
    "f50_tdcp_055_rev_per_share_decline_x_close_decline": {"inputs": ["revenue", "shareswadil", "close"], "func": f50_tdcp_055_rev_per_share_decline_x_close_decline},
    "f50_tdcp_056_bps_decline_x_pb_decline": {"inputs": ["equity", "shareswa", "marketcap"], "func": f50_tdcp_056_bps_decline_x_pb_decline},
    "f50_tdcp_057_issuance_pressure_x_low_volume_proxy": {"inputs": ["sharesbas", "volume"], "func": f50_tdcp_057_issuance_pressure_x_low_volume_proxy},
    "f50_tdcp_058_dilution_to_mc_chg_ratio": {"inputs": ["sharesbas", "marketcap"], "func": f50_tdcp_058_dilution_to_mc_chg_ratio},
    "f50_tdcp_059_dilution_persistence_x_dd_persistence": {"inputs": ["sharesbas", "close"], "func": f50_tdcp_059_dilution_persistence_x_dd_persistence},
    "f50_tdcp_060_sbcomp_growth_x_revenue_decline_x_price_decline": {"inputs": ["sbcomp", "revenue", "close"], "func": f50_tdcp_060_sbcomp_growth_x_revenue_decline_x_price_decline},
    "f50_tdcp_061_sharefactor_jump_x_close_collapse": {"inputs": ["sharefactor", "close"], "func": f50_tdcp_061_sharefactor_jump_x_close_collapse},
    "f50_tdcp_062_sharefactor_persistence_post_event": {"inputs": ["sharefactor"], "func": f50_tdcp_062_sharefactor_persistence_post_event},
    "f50_tdcp_063_post_split_decay_proxy": {"inputs": ["sharefactor", "close"], "func": f50_tdcp_063_post_split_decay_proxy},
    "f50_tdcp_064_reverse_split_proxy_x_drawdown": {"inputs": ["sharefactor", "sharesbas", "close"], "func": f50_tdcp_064_reverse_split_proxy_x_drawdown},
    "f50_tdcp_065_sharefactor_volatility_x_price_volatility": {"inputs": ["sharefactor", "close"], "func": f50_tdcp_065_sharefactor_volatility_x_price_volatility},
    "f50_tdcp_066_compound_action_density_x_price_decay": {"inputs": ["sharefactor", "close"], "func": f50_tdcp_066_compound_action_density_x_price_decay},
    "f50_tdcp_067_sharefactor_jump_x_negative_eps": {"inputs": ["sharefactor", "netinc"], "func": f50_tdcp_067_sharefactor_jump_x_negative_eps},
    "f50_tdcp_068_sharefactor_jump_x_high_leverage": {"inputs": ["sharefactor", "debt", "equity"], "func": f50_tdcp_068_sharefactor_jump_x_high_leverage},
    "f50_tdcp_069_sharefactor_recency_x_dd": {"inputs": ["sharefactor", "close"], "func": f50_tdcp_069_sharefactor_recency_x_dd},
    "f50_tdcp_070_multiple_actions_year_x_collapse": {"inputs": ["sharefactor", "marketcap"], "func": f50_tdcp_070_multiple_actions_year_x_collapse},
    "f50_tdcp_071_dividend_cut_proxy_x_dd": {"inputs": ["sharefactor", "close", "equity"], "func": f50_tdcp_071_dividend_cut_proxy_x_dd},
    "f50_tdcp_072_sharefactor_change_x_revenue_decline": {"inputs": ["sharefactor", "revenue"], "func": f50_tdcp_072_sharefactor_change_x_revenue_decline},
    "f50_tdcp_073_event_density_x_low_marketcap": {"inputs": ["sharefactor", "marketcap"], "func": f50_tdcp_073_event_density_x_low_marketcap},
    "f50_tdcp_074_going_concern_triple_neg": {"inputs": ["workingcapital", "cashneq", "retearn"], "func": f50_tdcp_074_going_concern_triple_neg},
    "f50_tdcp_075_altman_z_proxy_with_price_overlay": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "marketcap", "liabilities", "revenue", "close"], "func": f50_tdcp_075_altman_z_proxy_with_price_overlay},
}
