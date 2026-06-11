import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

HURDLE = 0.08  # fixed cost-of-capital / hurdle rate for value-creation spreads


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _pctrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (capital-returns quality) =====
def _f50_roic_spread(roic):
    return roic - HURDLE


def _f50_tangible_roic(ebit, tangibles):
    return ebit / tangibles.replace(0, np.nan)


def _f50_assetturn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f50_equityturn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _f50_invcap_turn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _f50_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f50_tang_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f50_returns_mean(roic, roa, ros):
    return pd.concat([roic, roa, ros], axis=1).mean(axis=1)


def _f50_returns_disp(roic, roa, ros):
    return pd.concat([roic, roa, ros], axis=1).std(axis=1)


# ============================================================
# --- composite quality & value-creation regimes (v076-v090) ---

# composite return level (mean of roic/roa/ros) smoothed (overall earning-power level)
def f50rq_f50_capital_returns_quality_retcompema_base_v076_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return percentile vs its own 504d history (cyclical quality position)
def f50rq_f50_capital_returns_quality_retcomppct_base_v077_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = _pctrank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return trend over a year (improving/deteriorating overall returns)
def f50rq_f50_capital_returns_quality_retcomptrend_base_v078_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion normalized by mean level (coefficient of variation across return measures)
def f50rq_f50_capital_returns_quality_retcv_base_v079_signal(roic, roa, ros):
    d = _f50_returns_disp(roic, roa, ros)
    m = _f50_returns_mean(roic, roa, ros).abs()
    b = d / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion percentile (instability-of-quality regime position)
def f50rq_f50_capital_returns_quality_retdisppct_base_v080_signal(roic, roa, ros):
    d = _f50_returns_disp(roic, roa, ros)
    b = _pctrank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC minus ROA spread (capital-structure leverage on returns)
def f50rq_f50_capital_returns_quality_roicroaspr_base_v081_signal(roic, roa):
    b = roic - roa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC minus ROS spread (capital-intensity gap between capital and margin returns)
def f50rq_f50_capital_returns_quality_roicrosspr_base_v082_signal(roic, ros):
    b = roic - ros
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA minus ROS spread z-scored (turnover-driven vs margin-driven returns gap)
def f50rq_f50_capital_returns_quality_roarosspr_base_v083_signal(roa, ros):
    b = _z(roa - ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-three-returns-clear-hurdle regime: fraction of last year roic,roa,ros all above their medians
def f50rq_f50_capital_returns_quality_alltop_base_v084_signal(roic, roa, ros):
    mc = roic.rolling(504, min_periods=126).median()
    ma = roa.rolling(504, min_periods=126).median()
    ms = ros.rolling(504, min_periods=126).median()
    allup = ((roic >= mc) & (roa >= ma) & (ros >= ms)).astype(float)
    b = allup.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-creation persistence streak: consecutive-fraction of last quarter ROIC above hurdle
def f50rq_f50_capital_returns_quality_creatstreak_base_v085_signal(roic):
    above = (roic >= HURDLE).astype(float)
    b = above.rolling(63, min_periods=21).mean() - above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-destruction persistence: fraction of last 2yr ROIC below hurdle (chronic capital-sink)
def f50rq_f50_capital_returns_quality_destroypersist_base_v086_signal(roic):
    below = (roic < HURDLE).astype(float)
    b = below.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-creation regime instability: crossing count blended with average distance from the hurdle
def f50rq_f50_capital_returns_quality_hurdlecross_base_v087_signal(roic):
    above = (roic >= HURDLE).astype(float)
    cross = (above != above.shift(1)).astype(float)
    cnt = cross.rolling(252, min_periods=126).sum()
    dist = (roic - HURDLE).abs().rolling(63, min_periods=21).mean()
    b = cnt + 50.0 * dist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite returns squashed spread above hurdle (bounded overall compounder strength)
def f50rq_f50_capital_returns_quality_retcomphurd_base_v088_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = np.tanh(10.0 * (m - HURDLE))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC quality consistency: smoothed ROIC divided by its dispersion (durable-returns score)
def f50rq_f50_capital_returns_quality_roicconsist_base_v089_signal(roic):
    m = roic.ewm(span=126, min_periods=42).mean()
    sd = _std(roic, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite return acceleration: trend now minus trend a half-year ago
def f50rq_f50_capital_returns_quality_retcompaccel_base_v090_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    tr = m - m.shift(126)
    b = tr - tr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- invested-capital efficiency & capital-base dynamics (v091-v105) ---

# invested-capital turnover smoothed (capital-deployment efficiency level)
def f50rq_f50_capital_returns_quality_invcapturnema_base_v091_signal(revenue, invcap):
    it = _f50_invcap_turn(revenue, invcap)
    b = it.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover trend over a year
def f50rq_f50_capital_returns_quality_invcapturntrend_base_v092_signal(revenue, invcap):
    it = _f50_invcap_turn(revenue, invcap)
    b = it - it.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth rate (capital-base expansion — deployment pace)
def f50rq_f50_capital_returns_quality_invcapgrow_base_v093_signal(invcap):
    b = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-per-deployment: value-creation spread divided by invested-capital growth (compounding vs empire-building)
def f50rq_f50_capital_returns_quality_roicvsgrow_base_v094_signal(roic, invcap):
    grow = (invcap / invcap.shift(252).replace(0, np.nan) - 1.0).abs() + 0.01
    b = _f50_roic_spread(roic) / grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth acceleration (capital-deployment momentum)
def f50rq_f50_capital_returns_quality_invcapaccel_base_v095_signal(invcap):
    g = invcap / invcap.shift(126).replace(0, np.nan) - 1.0
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied NOPAT proxy: ROIC x invested capital, z-scored (absolute economic profit scale)
def f50rq_f50_capital_returns_quality_econprofit_base_v096_signal(roic, invcap):
    ep = _f50_roic_spread(roic) * invcap
    b = _z(ep, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit trend: change in ROIC-spread-weighted invested capital over a year
def f50rq_f50_capital_returns_quality_econproftrend_base_v097_signal(roic, invcap):
    ep = _f50_roic_spread(roic) * invcap
    b = (ep - ep.shift(252)) / invcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth rate (book-equity expansion / retention pace)
def f50rq_f50_capital_returns_quality_eqgrow_base_v098_signal(equity):
    b = equity / equity.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth rate, percentile-ranked (capital-base expansion cycle position)
def f50rq_f50_capital_returns_quality_assetgrow_base_v099_signal(assets):
    g = assets / assets.shift(252).replace(0, np.nan) - 1.0
    b = _pctrank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-on-growing-base: ROA minus asset-growth (organic earning power vs balance-sheet bloat)
def f50rq_f50_capital_returns_quality_roavsasgrow_base_v100_signal(roa, assets):
    g = assets / assets.shift(252).replace(0, np.nan) - 1.0
    b = roa - g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-base vs equity divergence: invested-capital growth minus equity growth (debt-funded deployment)
def f50rq_f50_capital_returns_quality_invcapeqdiv_base_v101_signal(invcap, equity):
    gi = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    ge = equity / equity.shift(252).replace(0, np.nan) - 1.0
    b = gi - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover percentile-ranked dispersion vs asset turnover (efficiency-measure disagreement)
def f50rq_f50_capital_returns_quality_turnspr_base_v102_signal(revenue, invcap, assets):
    it = _f50_invcap_turn(revenue, invcap)
    at = _f50_assetturn(revenue, assets)
    b = _z(it, 252) - _z(at, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per equity trend acceleration (equity-efficiency momentum)
def f50rq_f50_capital_returns_quality_eqturnaccel_base_v103_signal(revenue, equity):
    et = _f50_equityturn(revenue, equity)
    tr = et - et.shift(126)
    b = tr - tr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainable-growth proxy: ROIC x (1 - capital payout assumed) approximated by ROIC x invcap-retention
def f50rq_f50_capital_returns_quality_sustgrow_base_v104_signal(roic, invcap):
    ret = (invcap / invcap.shift(126).replace(0, np.nan) - 1.0).clip(lower=0)
    b = roic * ret
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital-turnover quality consistency (level / dispersion)
def f50rq_f50_capital_returns_quality_invcapconsist_base_v105_signal(revenue, invcap):
    it = _f50_invcap_turn(revenue, invcap)
    m = it.ewm(span=126, min_periods=42).mean()
    sd = _std(it, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tangible vs intangible asset-mix & return drag (v106-v120) ---

# tangible-asset share level (hard-asset intensity of the balance sheet)
def f50rq_f50_capital_returns_quality_tangshare_base_v106_signal(tangibles, assets):
    b = _f50_tang_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share trend over a year (goodwill/intangible build-up)
def f50rq_f50_capital_returns_quality_intangtrend_base_v107_signal(intangibles, assets):
    share = _f50_intang_share(intangibles, assets)
    b = share - share.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-to-intangible ratio z-scored (asset-quality mix)
def f50rq_f50_capital_returns_quality_tangintratio_base_v108_signal(tangibles, intangibles):
    r = tangibles / intangibles.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA on tangible-heavy balance sheet: ROA x tangible share (hard-asset earning power)
def f50rq_f50_capital_returns_quality_tangroa_base_v109_signal(roa, tangibles, assets):
    share = _f50_tang_share(tangibles, assets)
    b = (roa * share).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-drag percentile: intangible share ranked vs history (overhang position)
def f50rq_f50_capital_returns_quality_intangpct_base_v110_signal(intangibles, assets):
    share = _f50_intang_share(intangibles, assets)
    b = _pctrank(share, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC vs reported ROIC spread, smoothed (intangible-return drag, persistent)
def f50rq_f50_capital_returns_quality_tangdragema_base_v111_signal(ebit, tangibles, roic):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = (tr - roic).ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC percentile vs its own history
def f50rq_f50_capital_returns_quality_tangroicpct_base_v112_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = _pctrank(tr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible ROIC value-creation: tangible ROIC minus hurdle, squashed (hard-asset compounder strength)
def f50rq_f50_capital_returns_quality_tangcreate_base_v113_signal(ebit, tangibles):
    tr = _f50_tangible_roic(ebit, tangibles)
    b = np.tanh(8.0 * (tr - HURDLE).ewm(span=63, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-heavy-and-low-return regime: high intangible share while ROIC below hurdle (acquisition-driven sink)
def f50rq_f50_capital_returns_quality_intangsinkreg_base_v114_signal(intangibles, assets, roic):
    share = _f50_intang_share(intangibles, assets)
    hi_intang = (share >= share.rolling(504, min_periods=126).median()).astype(float)
    below = (roic < HURDLE).astype(float)
    b = (hi_intang * below).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset earning yield: EBIT per total assets weighted toward tangibles
def f50rq_f50_capital_returns_quality_tangebityield_base_v115_signal(ebit, tangibles, assets):
    yld = ebit / assets.replace(0, np.nan)
    share = _f50_tang_share(tangibles, assets)
    b = yld * share
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share trend interacted with ROIC trend (hard-asset shift improving returns)
def f50rq_f50_capital_returns_quality_tangshift_base_v116_signal(tangibles, assets, roic):
    share = _f50_tang_share(tangibles, assets)
    sh_tr = share - share.shift(126)
    ro_tr = roic - roic.shift(126)
    b = sh_tr * ro_tr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-to-equity ratio (goodwill overhang vs book equity)
def f50rq_f50_capital_returns_quality_intangeq_base_v117_signal(intangibles, equity):
    b = _z(intangibles / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-capital turnover: revenue per tangible asset (hard-asset productivity)
def f50rq_f50_capital_returns_quality_tangturn_base_v118_signal(revenue, tangibles):
    b = revenue / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-capital turnover trend (hard-asset productivity momentum)
def f50rq_f50_capital_returns_quality_tangturntrend_base_v119_signal(revenue, tangibles):
    t = revenue / tangibles.replace(0, np.nan)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-bloat momentum: intangible share rising while tangible turnover falling (low-quality expansion)
def f50rq_f50_capital_returns_quality_bloatmom_base_v120_signal(intangibles, assets, revenue, tangibles):
    share = _f50_intang_share(intangibles, assets)
    tt = revenue / tangibles.replace(0, np.nan)
    b = (share - share.shift(126)) * (-(tt - tt.shift(126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBIT-driven returns, equity returns & cross-ratios (v121-v135) ---

# EBIT margin trend over a year (operating-margin trajectory)
def f50rq_f50_capital_returns_quality_ebitmargintrend_base_v121_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin percentile vs its 504d history (cyclical operating-margin position)
def f50rq_f50_capital_returns_quality_ebitmarginpct_base_v122_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    b = _pctrank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT on assets (operating ROA) smoothed
def f50rq_f50_capital_returns_quality_ebitonassets_base_v123_signal(ebit, assets):
    b = (ebit / assets.replace(0, np.nan)).ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT on invested capital (operating ROIC) value-creation spread
def f50rq_f50_capital_returns_quality_ebitroicspr_base_v124_signal(ebit, invcap):
    b = ebit / invcap.replace(0, np.nan) - HURDLE
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-ROIC vs reported ROIC consistency (accrual/quality check)
def f50rq_f50_capital_returns_quality_opvsrepqual_base_v125_signal(ebit, invcap, roic):
    op = ebit / invcap.replace(0, np.nan)
    b = op - roic
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT on equity z-scored (operating return on book)
def f50rq_f50_capital_returns_quality_ebitoneqz_base_v126_signal(ebit, equity):
    b = _z(ebit / equity.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-ROIC acceleration: 2nd difference of ebit/invcap (deployment-efficiency curvature)
def f50rq_f50_capital_returns_quality_ebittrendinv_base_v127_signal(ebit, invcap):
    op = ebit / invcap.replace(0, np.nan)
    tr = op - op.shift(126)
    b = tr - tr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT margin consistency (level / dispersion — operating-margin durability)
def f50rq_f50_capital_returns_quality_ebitmargconsist_base_v128_signal(ebit, revenue):
    m = ebit / revenue.replace(0, np.nan)
    lvl = m.ewm(span=126, min_periods=42).mean()
    sd = _std(m, 252)
    b = lvl / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-ROIC above-trend persistence: fraction of last year ebit/invcap exceeds its 504d median
def f50rq_f50_capital_returns_quality_opcreate_base_v129_signal(ebit, invcap):
    op = ebit / invcap.replace(0, np.nan)
    med = op.rolling(504, min_periods=126).median()
    above = (op >= med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-on-equity minus EBIT-on-assets (operating leverage return premium)
def f50rq_f50_capital_returns_quality_oplevprem_base_v130_signal(ebit, equity, assets):
    e = ebit / equity.replace(0, np.nan)
    a = ebit / assets.replace(0, np.nan)
    b = e - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-asset vs revenue-per-equity ratio (asset-vs-equity efficiency tilt, ranked)
def f50rq_f50_capital_returns_quality_effratiotilt_base_v131_signal(revenue, assets, equity):
    at = _f50_assetturn(revenue, assets)
    et = _f50_equityturn(revenue, equity)
    b = _pctrank(at / et.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite efficiency: geometric-style blend of asset turnover and EBIT margin (return drivers product, z)
def f50rq_f50_capital_returns_quality_effblend_base_v132_signal(revenue, assets, ebit):
    at = _f50_assetturn(revenue, assets)
    m = ebit / revenue.replace(0, np.nan)
    b = _z(at * m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-driver dominance: which moved more, margin or turnover (sign of z-difference, smoothed)
def f50rq_f50_capital_returns_quality_driverdom_base_v133_signal(ebit, revenue, assets):
    m = _z(ebit / revenue.replace(0, np.nan), 252)
    at = _z(_f50_assetturn(revenue, assets), 252)
    b = (m - at).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT yield on tangibles minus EBIT yield on assets (intangible dilution of operating returns)
def f50rq_f50_capital_returns_quality_ebittangdil_base_v134_signal(ebit, tangibles, assets):
    yt = ebit / tangibles.replace(0, np.nan)
    ya = ebit / assets.replace(0, np.nan)
    b = yt - ya
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-ROIC erosion from peak normalized by volatility (operating value-creation drawdown)
def f50rq_f50_capital_returns_quality_operode_base_v135_signal(ebit, invcap):
    op = ebit / invcap.replace(0, np.nan)
    hi = op.rolling(504, min_periods=252).max()
    vol = _std(op, 126)
    b = (op - hi) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-measure regimes, interactions & quality scores (v136-v150) ---

# quality compounder score: ROIC level x asset turnover (return x efficiency interaction, z)
def f50rq_f50_capital_returns_quality_compscore_base_v136_signal(roic, assetturnover):
    b = _z(roic * assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-and-turnover both-improving regime (twin-engine improvement)
def f50rq_f50_capital_returns_quality_twinengine_base_v137_signal(roic, assetturnover):
    ru = (roic > roic.shift(63)).astype(float)
    au = (assetturnover > assetturnover.shift(63)).astype(float)
    both = (ru * au)
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-quality vs efficiency divergence: ROIC z minus asset-turnover z
def f50rq_f50_capital_returns_quality_roicturndiv_base_v138_signal(roic, assetturnover):
    b = _z(roic, 252) - _z(assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA-weighted asset turnover (efficiency that actually earns — returns x churn)
def f50rq_f50_capital_returns_quality_earnchurn_base_v139_signal(roa, assetturnover):
    b = (roa * assetturnover).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported asset-turnover trend (capital-efficiency trajectory from the reported column)
def f50rq_f50_capital_returns_quality_atcoltrend_base_v140_signal(assetturnover):
    b = assetturnover - assetturnover.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported asset-turnover percentile (efficiency cycle position)
def f50rq_f50_capital_returns_quality_atcolpct_base_v141_signal(assetturnover):
    b = _pctrank(assetturnover, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS x reported-turnover DuPont level z-scored (margin x churn return)
def f50rq_f50_capital_returns_quality_dupontcolz_base_v142_signal(ros, assetturnover):
    b = _z(ros * assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink recovery: was-below-hurdle now-above (turnaround flag fraction)
def f50rq_f50_capital_returns_quality_turnaround_base_v143_signal(roic):
    above = (roic >= HURDLE).astype(float)
    was_below = (roic.shift(126) < HURDLE).astype(float)
    flag = (above * was_below)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns mean reversion: distance of composite returns from its long mean (over/under-earning)
def f50rq_f50_capital_returns_quality_retmeanrev_base_v144_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    b = m - m.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability regime: low-dispersion-and-above-hurdle fraction (high-quality compounder regime)
def f50rq_f50_capital_returns_quality_stablequal_base_v145_signal(roic):
    above = (roic >= HURDLE).astype(float)
    sd = _std(roic, 63)
    calm = (sd <= sd.rolling(504, min_periods=126).median()).astype(float)
    b = (above * calm).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit margin: ROIC-spread x invested-capital turnover (value created per unit revenue)
def f50rq_f50_capital_returns_quality_epmargin_base_v146_signal(roic, revenue, invcap):
    it = _f50_invcap_turn(revenue, invcap)
    b = _f50_roic_spread(roic) / it.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns quadrant: sign of (ROIC-hurdle) x sign of ROIC-trend (compounder/turnaround/fader/sink classification)
def f50rq_f50_capital_returns_quality_quadrant_base_v147_signal(roic):
    spr = np.sign(roic - HURDLE)
    tr = np.sign((roic - roic.shift(126)))
    raw = spr * 2.0 + tr
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-efficiency dispersion across asset/equity/invcap turnover (efficiency-measure spread)
def f50rq_f50_capital_returns_quality_turndisp_base_v148_signal(revenue, assets, equity, invcap):
    at = _f50_assetturn(revenue, assets)
    et = _f50_equityturn(revenue, equity)
    it = _f50_invcap_turn(revenue, invcap)
    b = pd.concat([_z(at, 252), _z(et, 252), _z(it, 252)], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overall quality composite: average of standardized ROIC-spread, EBIT-margin, asset turnover (multi-facet score)
def f50rq_f50_capital_returns_quality_qualcomposite_base_v149_signal(roic, ebit, revenue, assets):
    a = _z(_f50_roic_spread(roic), 252)
    m = _z(ebit / revenue.replace(0, np.nan), 252)
    t = _z(_f50_assetturn(revenue, assets), 252)
    b = (a + m + t) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable-compounder flag: composite returns above own 504d median AND rising, persistence fraction
def f50rq_f50_capital_returns_quality_durablecomp_base_v150_signal(roic, roa, ros):
    m = _f50_returns_mean(roic, roa, ros)
    above = (m >= m.rolling(504, min_periods=126).median()).astype(float)
    rising = (m > m.shift(63)).astype(float)
    b = (above * rising).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50rq_f50_capital_returns_quality_retcompema_base_v076_signal,
    f50rq_f50_capital_returns_quality_retcomppct_base_v077_signal,
    f50rq_f50_capital_returns_quality_retcomptrend_base_v078_signal,
    f50rq_f50_capital_returns_quality_retcv_base_v079_signal,
    f50rq_f50_capital_returns_quality_retdisppct_base_v080_signal,
    f50rq_f50_capital_returns_quality_roicroaspr_base_v081_signal,
    f50rq_f50_capital_returns_quality_roicrosspr_base_v082_signal,
    f50rq_f50_capital_returns_quality_roarosspr_base_v083_signal,
    f50rq_f50_capital_returns_quality_alltop_base_v084_signal,
    f50rq_f50_capital_returns_quality_creatstreak_base_v085_signal,
    f50rq_f50_capital_returns_quality_destroypersist_base_v086_signal,
    f50rq_f50_capital_returns_quality_hurdlecross_base_v087_signal,
    f50rq_f50_capital_returns_quality_retcomphurd_base_v088_signal,
    f50rq_f50_capital_returns_quality_roicconsist_base_v089_signal,
    f50rq_f50_capital_returns_quality_retcompaccel_base_v090_signal,
    f50rq_f50_capital_returns_quality_invcapturnema_base_v091_signal,
    f50rq_f50_capital_returns_quality_invcapturntrend_base_v092_signal,
    f50rq_f50_capital_returns_quality_invcapgrow_base_v093_signal,
    f50rq_f50_capital_returns_quality_roicvsgrow_base_v094_signal,
    f50rq_f50_capital_returns_quality_invcapaccel_base_v095_signal,
    f50rq_f50_capital_returns_quality_econprofit_base_v096_signal,
    f50rq_f50_capital_returns_quality_econproftrend_base_v097_signal,
    f50rq_f50_capital_returns_quality_eqgrow_base_v098_signal,
    f50rq_f50_capital_returns_quality_assetgrow_base_v099_signal,
    f50rq_f50_capital_returns_quality_roavsasgrow_base_v100_signal,
    f50rq_f50_capital_returns_quality_invcapeqdiv_base_v101_signal,
    f50rq_f50_capital_returns_quality_turnspr_base_v102_signal,
    f50rq_f50_capital_returns_quality_eqturnaccel_base_v103_signal,
    f50rq_f50_capital_returns_quality_sustgrow_base_v104_signal,
    f50rq_f50_capital_returns_quality_invcapconsist_base_v105_signal,
    f50rq_f50_capital_returns_quality_tangshare_base_v106_signal,
    f50rq_f50_capital_returns_quality_intangtrend_base_v107_signal,
    f50rq_f50_capital_returns_quality_tangintratio_base_v108_signal,
    f50rq_f50_capital_returns_quality_tangroa_base_v109_signal,
    f50rq_f50_capital_returns_quality_intangpct_base_v110_signal,
    f50rq_f50_capital_returns_quality_tangdragema_base_v111_signal,
    f50rq_f50_capital_returns_quality_tangroicpct_base_v112_signal,
    f50rq_f50_capital_returns_quality_tangcreate_base_v113_signal,
    f50rq_f50_capital_returns_quality_intangsinkreg_base_v114_signal,
    f50rq_f50_capital_returns_quality_tangebityield_base_v115_signal,
    f50rq_f50_capital_returns_quality_tangshift_base_v116_signal,
    f50rq_f50_capital_returns_quality_intangeq_base_v117_signal,
    f50rq_f50_capital_returns_quality_tangturn_base_v118_signal,
    f50rq_f50_capital_returns_quality_tangturntrend_base_v119_signal,
    f50rq_f50_capital_returns_quality_bloatmom_base_v120_signal,
    f50rq_f50_capital_returns_quality_ebitmargintrend_base_v121_signal,
    f50rq_f50_capital_returns_quality_ebitmarginpct_base_v122_signal,
    f50rq_f50_capital_returns_quality_ebitonassets_base_v123_signal,
    f50rq_f50_capital_returns_quality_ebitroicspr_base_v124_signal,
    f50rq_f50_capital_returns_quality_opvsrepqual_base_v125_signal,
    f50rq_f50_capital_returns_quality_ebitoneqz_base_v126_signal,
    f50rq_f50_capital_returns_quality_ebittrendinv_base_v127_signal,
    f50rq_f50_capital_returns_quality_ebitmargconsist_base_v128_signal,
    f50rq_f50_capital_returns_quality_opcreate_base_v129_signal,
    f50rq_f50_capital_returns_quality_oplevprem_base_v130_signal,
    f50rq_f50_capital_returns_quality_effratiotilt_base_v131_signal,
    f50rq_f50_capital_returns_quality_effblend_base_v132_signal,
    f50rq_f50_capital_returns_quality_driverdom_base_v133_signal,
    f50rq_f50_capital_returns_quality_ebittangdil_base_v134_signal,
    f50rq_f50_capital_returns_quality_operode_base_v135_signal,
    f50rq_f50_capital_returns_quality_compscore_base_v136_signal,
    f50rq_f50_capital_returns_quality_twinengine_base_v137_signal,
    f50rq_f50_capital_returns_quality_roicturndiv_base_v138_signal,
    f50rq_f50_capital_returns_quality_earnchurn_base_v139_signal,
    f50rq_f50_capital_returns_quality_atcoltrend_base_v140_signal,
    f50rq_f50_capital_returns_quality_atcolpct_base_v141_signal,
    f50rq_f50_capital_returns_quality_dupontcolz_base_v142_signal,
    f50rq_f50_capital_returns_quality_turnaround_base_v143_signal,
    f50rq_f50_capital_returns_quality_retmeanrev_base_v144_signal,
    f50rq_f50_capital_returns_quality_stablequal_base_v145_signal,
    f50rq_f50_capital_returns_quality_epmargin_base_v146_signal,
    f50rq_f50_capital_returns_quality_quadrant_base_v147_signal,
    f50rq_f50_capital_returns_quality_turndisp_base_v148_signal,
    f50rq_f50_capital_returns_quality_qualcomposite_base_v149_signal,
    f50rq_f50_capital_returns_quality_durablecomp_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CAPITAL_RETURNS_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    roic = _fund(1, base=0.12, drift=0.0, vol=0.10, allow_neg=True).rename("roic")
    roa = _fund(2, base=0.08, drift=0.0, vol=0.09, allow_neg=True).rename("roa")
    ros = _fund(3, base=0.10, drift=0.0, vol=0.11, allow_neg=True).rename("ros")
    ebit = _fund(4, base=5e7, drift=0.0, vol=0.12, allow_neg=True).rename("ebit")
    assetturnover = (_fund(5, base=0.7, drift=0.0, vol=0.07) + 0.1).rename("assetturnover")
    invcap = _fund(6, base=8e8, drift=0.01, vol=0.05).rename("invcap")
    equity = _fund(7, base=6e8, drift=0.01, vol=0.05).rename("equity")
    intangibles = _fund(8, base=2e8, drift=0.0, vol=0.06).rename("intangibles")
    tangibles = _fund(9, base=7e8, drift=0.005, vol=0.05).rename("tangibles")
    revenue = _fund(10, base=9e8, drift=0.01, vol=0.06).rename("revenue")
    assets = _fund(11, base=1.2e9, drift=0.01, vol=0.05).rename("assets")

    cols = {"roic": roic, "roa": roa, "ros": ros, "ebit": ebit,
            "assetturnover": assetturnover, "invcap": invcap, "equity": equity,
            "intangibles": intangibles, "tangibles": tangibles,
            "revenue": revenue, "assets": assets}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f50_capital_returns_quality_base_076_150_claude: %d features pass" % n_features)
