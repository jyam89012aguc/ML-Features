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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s on time over window w (per-step); handles short warm-up windows
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (Altman-Z / distress / runway) =====
def _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    a = assets.replace(0, np.nan)
    x1 = workingcapital / a
    x2 = retearn / a
    x3 = ebit / a
    x4 = equity / liabilities.replace(0, np.nan)
    x5 = revenue / a
    return 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5


def _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets):
    # Altman Z'' (private/non-manufacturing variant, no revenue term)
    a = assets.replace(0, np.nan)
    x1 = workingcapital / a
    x2 = retearn / a
    x3 = ebit / a
    x4 = equity / liabilities.replace(0, np.nan)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _f37_wc_assets(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f37_re_assets(retearn, assets):
    return retearn / assets.replace(0, np.nan)


def _f37_ebit_assets(ebit, assets):
    return ebit / assets.replace(0, np.nan)


def _f37_eq_liab(equity, liabilities):
    return equity / liabilities.replace(0, np.nan)


def _f37_rev_assets(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f37_runway(cashneq, opex):
    # months of cash at current operating-expense burn (opex per quarter -> per day proxy)
    return cashneq / opex.replace(0, np.nan)


# ============================================================
# --- Altman-Z component levels & composite ---

# X1: working-capital / assets (liquidity buffer)
def f37da_f37_distress_risk_altman_wcassets_lvl_63d_base_v001_signal(workingcapital, assets):
    b = _mean(_f37_wc_assets(workingcapital, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# X2: retained-earnings / assets (cumulative profitability cushion)
def f37da_f37_distress_risk_altman_reassets_lvl_63d_base_v002_signal(retearn, assets):
    b = _mean(_f37_re_assets(retearn, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# X3: EBIT / assets (operating return on assets)
def f37da_f37_distress_risk_altman_ebitassets_lvl_63d_base_v003_signal(ebit, assets):
    b = _mean(_f37_ebit_assets(ebit, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# X4: equity / liabilities (solvency cushion)
def f37da_f37_distress_risk_altman_eqliab_lvl_63d_base_v004_signal(equity, liabilities):
    b = _mean(_f37_eq_liab(equity, liabilities), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# X5: revenue / assets (asset turnover term)
def f37da_f37_distress_risk_altman_revassets_lvl_63d_base_v005_signal(revenue, assets):
    b = _mean(_f37_rev_assets(revenue, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# composite Altman-Z level
def f37da_f37_distress_risk_altman_zscore_lvl_63d_base_v006_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _mean(z, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# Z'' percentile rank vs own 2yr history (non-manufacturing distress standing)
def f37da_f37_distress_risk_altman_zprime_lvl_63d_base_v007_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    zp = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    b = _rank(zp, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# distress zone occupancy: fraction of last half-year below 1.81, plus continuous depth below it
def f37da_f37_distress_risk_altman_distzone_126d_base_v008_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    flag = (z < 1.81).astype(float)
    occ = flag.rolling(126, min_periods=42).mean()
    depth = (1.81 - z).clip(lower=0).rolling(63, min_periods=21).mean()
    b = occ + depth
    return b.replace([np.inf, -np.inf], np.nan)


# safe-zone occupancy: fraction of last half-year above 2.99, plus continuous headroom above it
def f37da_f37_distress_risk_altman_safezone_126d_base_v009_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    flag = (z > 2.99).astype(float)
    occ = flag.rolling(126, min_periods=42).mean()
    head = (z - 2.99).clip(lower=0).rolling(63, min_periods=21).mean()
    b = occ + head
    return b.replace([np.inf, -np.inf], np.nan)


# distance of Z above the 1.81 distress floor, scaled by its own dispersion
def f37da_f37_distress_risk_altman_zcushion_126d_base_v010_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    sd = _std(z, 126)
    b = (z - 1.81) / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# --- cash runway / burn ---

# cash runway level: cash / opex
def f37da_f37_distress_risk_altman_runway_lvl_63d_base_v011_signal(cashneq, opex):
    b = _mean(_f37_runway(cashneq, opex), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# cash runway de-trended: runway minus its slow EWMA (acute change in survival horizon)
def f37da_f37_distress_risk_altman_runwaylog_63d_base_v012_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    rl = np.log(r.replace(0, np.nan))
    b = rl - rl.ewm(span=252, min_periods=63).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# burn-rate stress: opex relative to cash (inverse runway), short window
def f37da_f37_distress_risk_altman_burnstress_21d_base_v013_signal(opex, cashneq):
    b = _mean(_safe_div(opex, cashneq), 21)
    return b.replace([np.inf, -np.inf], np.nan)


# runway coverage by retained earnings: (cash + retearn) / opex
def f37da_f37_distress_risk_altman_runwayre_63d_base_v014_signal(cashneq, retearn, opex):
    b = _mean(_safe_div(cashneq + retearn, opex), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# self-funding gap z-score: EBIT/opex coverage de-trended vs its own year history
def f37da_f37_distress_risk_altman_ebitcover_63d_base_v015_signal(ebit, opex):
    b = _z(_safe_div(ebit, opex), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- solvency / leverage stress ---

# liabilities / assets (gross leverage)
def f37da_f37_distress_risk_altman_liabassets_63d_base_v016_signal(liabilities, assets):
    b = _mean(_safe_div(liabilities, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities relative to EBIT (years of operating profit to repay)
def f37da_f37_distress_risk_altman_liabebit_63d_base_v017_signal(liabilities, ebit):
    b = _mean(_safe_div(liabilities, ebit), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities / revenue (debt load vs sales scale)
def f37da_f37_distress_risk_altman_liabrev_63d_base_v018_signal(liabilities, revenue):
    b = _mean(_safe_div(liabilities, revenue), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# negative-equity flag: fraction of half-year with equity < 0
def f37da_f37_distress_risk_altman_negeq_126d_base_v019_signal(equity):
    flag = (equity < 0).astype(float)
    b = flag.rolling(126, min_periods=42).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# equity buffer relative to liabilities, signed magnitude (stabilized)
def f37da_f37_distress_risk_altman_eqbuffer_63d_base_v020_signal(equity, liabilities):
    r = _f37_eq_liab(equity, liabilities)
    sm = np.sign(r) * np.sqrt(r.abs())
    b = _mean(sm, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- z-scored components (de-trended distress shifts) ---

# X1 z-scored vs own year history
def f37da_f37_distress_risk_altman_wcassetsz_252d_base_v021_signal(workingcapital, assets):
    b = _z(_f37_wc_assets(workingcapital, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# X2 z-scored vs own year history
def f37da_f37_distress_risk_altman_reassetsz_252d_base_v022_signal(retearn, assets):
    b = _z(_f37_re_assets(retearn, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# X3 z-scored vs own year history
def f37da_f37_distress_risk_altman_ebitassetsz_252d_base_v023_signal(ebit, assets):
    b = _z(_f37_ebit_assets(ebit, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# X4 z-scored vs own year history
def f37da_f37_distress_risk_altman_eqliabz_252d_base_v024_signal(equity, liabilities):
    b = _z(_f37_eq_liab(equity, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# X5 z-scored vs own year history
def f37da_f37_distress_risk_altman_revassetsz_252d_base_v025_signal(revenue, assets):
    b = _z(_f37_rev_assets(revenue, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# composite Z z-scored vs own 2yr history (distress regime extremity)
def f37da_f37_distress_risk_altman_zscorez_504d_base_v026_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _z(z, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# runway z-scored vs own year history
def f37da_f37_distress_risk_altman_runwayz_252d_base_v027_signal(cashneq, opex):
    b = _z(_f37_runway(cashneq, opex), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# liabilities/assets z-scored (leverage regime shift)
def f37da_f37_distress_risk_altman_liabassetsz_252d_base_v028_signal(liabilities, assets):
    b = _z(_safe_div(liabilities, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- percentile ranks ---

# Z percentile-rank gap: short-window rank minus long-window rank (recent vs structural standing)
def f37da_f37_distress_risk_altman_zscorerank_504d_base_v029_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _rank(z, 126) - _rank(z, 504)
    return b.replace([np.inf, -np.inf], np.nan)


# runway rank vs own 2yr history
def f37da_f37_distress_risk_altman_runwayrank_504d_base_v030_signal(cashneq, opex):
    b = _rank(_f37_runway(cashneq, opex), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# EBIT/assets rank vs own 2yr history (operating-return percentile)
def f37da_f37_distress_risk_altman_ebitassetsrank_504d_base_v031_signal(ebit, assets):
    b = _rank(_f37_ebit_assets(ebit, assets), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# equity/liabilities rank (solvency percentile)
def f37da_f37_distress_risk_altman_eqliabrank_504d_base_v032_signal(equity, liabilities):
    b = _rank(_f37_eq_liab(equity, liabilities), 504)
    return b.replace([np.inf, -np.inf], np.nan)


# --- slope / trajectory of distress metrics ---

# Z trajectory: OLS slope of Z over a year (improving vs deteriorating solvency)
def f37da_f37_distress_risk_altman_zslope_252d_base_v033_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _slope(z, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# runway trajectory slope (burning vs building cash)
def f37da_f37_distress_risk_altman_runwayslope_252d_base_v034_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = _slope(r, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# leverage trajectory: slope of liabilities/assets (leveraging up = distress build)
def f37da_f37_distress_risk_altman_levslope_252d_base_v035_signal(liabilities, assets):
    b = _slope(_safe_div(liabilities, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# retained-earnings/assets trajectory (cushion build/erosion)
def f37da_f37_distress_risk_altman_reslope_252d_base_v036_signal(retearn, assets):
    b = _slope(_f37_re_assets(retearn, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- year-over-year / change differences ---

# Z change vs one year ago
def f37da_f37_distress_risk_altman_zyoy_252d_base_v037_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    zs = _mean(z, 21)
    b = zs - zs.shift(252)
    return b.replace([np.inf, -np.inf], np.nan)


# working-capital/assets change vs half-year ago
def f37da_f37_distress_risk_altman_wcchg_126d_base_v038_signal(workingcapital, assets):
    x = _f37_wc_assets(workingcapital, assets)
    b = x - x.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)


# EBIT/assets change vs half-year ago (operating-return deterioration)
def f37da_f37_distress_risk_altman_ebitchg_126d_base_v039_signal(ebit, assets):
    x = _f37_ebit_assets(ebit, assets)
    b = x - x.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)


# runway change vs quarter ago (acceleration of burn)
def f37da_f37_distress_risk_altman_runwaychg_63d_base_v040_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = r - r.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- interaction / composite stress signatures ---

# distress interaction: Z trajectory weighted by leverage level (deleveraging vs leveraging stress)
def f37da_f37_distress_risk_altman_zlev_63d_base_v041_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    lev = _safe_div(liabilities, assets)
    zchg = z - z.shift(63)
    b = _mean(zchg * lev, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# quality-adjusted survival: runway rank times operating-return sign (profitable firms get credit)
def f37da_f37_distress_risk_altman_runwayebit_63d_base_v042_signal(cashneq, opex, ebit, assets):
    r = _f37_runway(cashneq, opex)
    roa = _f37_ebit_assets(ebit, assets)
    rr = _rank(r, 252)
    b = rr * np.tanh(20.0 * roa)
    return b.replace([np.inf, -np.inf], np.nan)


# distress composite: average of three normalized stress components
def f37da_f37_distress_risk_altman_stresscomp_126d_base_v043_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    wc = _z(_f37_wc_assets(workingcapital, assets), 126)
    re = _z(_f37_re_assets(retearn, assets), 126)
    eq = _z(_f37_eq_liab(equity, liabilities), 126)
    b = (wc + re + eq) / 3.0
    return b.replace([np.inf, -np.inf], np.nan)


# operating-burden stress: opex vs revenue (cost coverage)
def f37da_f37_distress_risk_altman_opexrev_63d_base_v044_signal(opex, revenue):
    b = _mean(_safe_div(opex, revenue), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# operating-surplus trajectory: slope of (revenue - opex)/assets (scaling into/out of losses)
def f37da_f37_distress_risk_altman_opsurplus_63d_base_v045_signal(revenue, opex, assets):
    b = _slope(_safe_div(revenue - opex, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- dispersion / volatility of distress metrics ---

# Z instability: std of Z over half-year (volatile solvency)
def f37da_f37_distress_risk_altman_zvol_126d_base_v046_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _std(z, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# runway instability: std of runway over half-year
def f37da_f37_distress_risk_altman_runwayvol_126d_base_v047_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = _std(r, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# leverage instability: std of liabilities/equity
def f37da_f37_distress_risk_altman_levvol_126d_base_v048_signal(liabilities, equity):
    r = _safe_div(liabilities, equity)
    b = _std(r, 126)
    return b.replace([np.inf, -np.inf], np.nan)


# --- additional component ratios & cross-terms ---

# cash / assets (liquidity density)
def f37da_f37_distress_risk_altman_cashassets_63d_base_v049_signal(cashneq, assets):
    b = _mean(_safe_div(cashneq, assets), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# cash / liabilities (immediate coverage)
def f37da_f37_distress_risk_altman_cashliab_63d_base_v050_signal(cashneq, liabilities):
    b = _mean(_safe_div(cashneq, liabilities), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# working-capital / liabilities (short-term solvency)
def f37da_f37_distress_risk_altman_wcliab_63d_base_v051_signal(workingcapital, liabilities):
    b = _mean(_safe_div(workingcapital, liabilities), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# retained-earnings / equity (earned vs contributed capital)
def f37da_f37_distress_risk_altman_reequity_63d_base_v052_signal(retearn, equity):
    b = _mean(_safe_div(retearn, equity), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# EBIT / liabilities trajectory: slope of debt-service generation over a year
def f37da_f37_distress_risk_altman_ebitliab_63d_base_v053_signal(ebit, liabilities):
    b = _slope(_safe_div(ebit, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# revenue / liabilities trajectory: slope of sales-to-debt coverage (deleveraging-by-growth)
def f37da_f37_distress_risk_altman_revliab_63d_base_v054_signal(revenue, liabilities):
    b = _slope(_safe_div(revenue, liabilities), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- weighted Z subcomponents (which term drives the score) ---

# profitability-vs-solvency tilt: ratio of X3 to X4 contribution, sign-magnitude squashed
def f37da_f37_distress_risk_altman_x3share_63d_base_v055_signal(ebit, assets, equity, liabilities):
    c3 = 3.3 * _f37_ebit_assets(ebit, assets)
    c4 = 0.6 * _f37_eq_liab(equity, liabilities)
    ratio = c3 / c4.replace(0, np.nan)
    b = _mean(np.tanh(ratio), 63)
    return b.replace([np.inf, -np.inf], np.nan)


# weighted X4 contribution (0.6*equity/liab) as share of |Z|
def f37da_f37_distress_risk_altman_x4share_63d_base_v056_signal(equity, liabilities, workingcapital, retearn, ebit, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    contrib = 0.6 * _f37_eq_liab(equity, liabilities)
    share = contrib / z.abs().replace(0, np.nan)
    b = _mean(share, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- min-over-window worst-case distress ---

# worst (minimum) Z over the last half-year (peak distress in window)
def f37da_f37_distress_risk_altman_zmin_126d_base_v057_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = z.rolling(126, min_periods=42).min()
    return b.replace([np.inf, -np.inf], np.nan)


# worst (minimum) runway over the last half-year (tightest survival point)
def f37da_f37_distress_risk_altman_runwaymin_126d_base_v058_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = r.rolling(126, min_periods=42).min()
    return b.replace([np.inf, -np.inf], np.nan)


# --- deterioration composite & sign features ---

# deterioration composite: count of metrics deteriorating vs half-year ago, smoothed (continuous)
def f37da_f37_distress_risk_altman_deteriorate_126d_base_v059_signal(workingcapital, retearn, ebit, assets, equity, liabilities):
    wc = _f37_wc_assets(workingcapital, assets)
    re = _f37_re_assets(retearn, assets)
    eb = _f37_ebit_assets(ebit, assets)
    eq = _f37_eq_liab(equity, liabilities)
    d = ((wc < wc.shift(126)).astype(float)
         + (re < re.shift(126)).astype(float)
         + (eb < eb.shift(126)).astype(float)
         + (eq < eq.shift(126)).astype(float))
    b = d.rolling(63, min_periods=21).mean() - 2.0
    return b.replace([np.inf, -np.inf], np.nan)


# improvement composite: count of metrics improving vs year ago, smoothed (continuous)
def f37da_f37_distress_risk_altman_improve_252d_base_v060_signal(workingcapital, retearn, ebit, assets, revenue):
    wc = _f37_wc_assets(workingcapital, assets)
    re = _f37_re_assets(retearn, assets)
    eb = _f37_ebit_assets(ebit, assets)
    rv = _f37_rev_assets(revenue, assets)
    d = ((wc > wc.shift(252)).astype(float)
         + (re > re.shift(252)).astype(float)
         + (eb > eb.shift(252)).astype(float)
         + (rv > rv.shift(252)).astype(float))
    b = d.rolling(63, min_periods=21).mean() - 2.0
    return b.replace([np.inf, -np.inf], np.nan)


# --- exponential-weighted distress smoothing ---

# Z fast-vs-slow EWMA crossover (solvency-trend regime, level-detrended)
def f37da_f37_distress_risk_altman_zema_base_v061_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    fast = z.ewm(span=21, min_periods=10).mean()
    slow = z.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    return b.replace([np.inf, -np.inf], np.nan)


# Z displacement vs its rolling median, normalized by rolling IQR-proxy (robust distress shock)
def f37da_f37_distress_risk_altman_zdisp_base_v062_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    med = z.rolling(252, min_periods=63).median()
    mad = (z - med).abs().rolling(252, min_periods=63).median()
    b = (z - med) / mad.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


# runway EWMA displacement (acute cash shock)
def f37da_f37_distress_risk_altman_runwaydisp_base_v063_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = r - r.ewm(span=63, min_periods=21).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# --- tanh-bounded shock features ---

# bounded EBIT/assets shock (deterioration of operating return, squashed)
def f37da_f37_distress_risk_altman_ebitshock_63d_base_v064_signal(ebit, assets):
    x = _f37_ebit_assets(ebit, assets)
    chg = x - x.shift(63)
    b = np.tanh(15.0 * chg)
    return b.replace([np.inf, -np.inf], np.nan)


# bounded leverage shock (jump in liabilities/assets)
def f37da_f37_distress_risk_altman_levshock_63d_base_v065_signal(liabilities, assets):
    x = _safe_div(liabilities, assets)
    chg = x - x.shift(63)
    b = np.tanh(8.0 * chg)
    return b.replace([np.inf, -np.inf], np.nan)


# --- asymmetry & sign-magnitude composites ---

# solvency-balance momentum: change in the equity-vs-liability balance over a quarter
def f37da_f37_distress_risk_altman_solvbalance_63d_base_v066_signal(equity, liabilities, assets):
    eq = _safe_div(equity, assets)
    lb = _safe_div(liabilities, assets)
    bal = (eq - lb) / (eq.abs() + lb.abs()).replace(0, np.nan)
    b = bal - bal.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


# runway vs burn asymmetry: balance of cash against opex burden
def f37da_f37_distress_risk_altman_runbalance_63d_base_v067_signal(cashneq, opex, revenue):
    cov = _safe_div(cashneq, opex)
    burn = _safe_div(opex, revenue)
    bal = (np.log1p(cov) - burn)
    b = _mean(bal, 63)
    return b.replace([np.inf, -np.inf], np.nan)


# --- hit-rate / persistence of distress ---

# persistence in distress: fraction of year with Z'' below its own 504d median (relative weakness)
def f37da_f37_distress_risk_altman_zprimedist_252d_base_v068_signal(workingcapital, retearn, ebit, equity, liabilities, assets):
    z = _f37_zprime(workingcapital, retearn, ebit, equity, liabilities, assets)
    ref = z.rolling(504, min_periods=126).median()
    flag = (z < ref).astype(float)
    b = flag.rolling(252, min_periods=63).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# persistence of negative operating return: fraction of year EBIT<0
def f37da_f37_distress_risk_altman_negebit_252d_base_v069_signal(ebit):
    flag = (ebit < 0).astype(float)
    b = flag.rolling(252, min_periods=63).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# persistence of accumulated-deficit: fraction of year retearn<0
def f37da_f37_distress_risk_altman_negre_252d_base_v070_signal(retearn):
    flag = (retearn < 0).astype(float)
    b = flag.rolling(252, min_periods=63).mean()
    return b.replace([np.inf, -np.inf], np.nan)


# --- multi-window distress spreads ---

# Z short-vs-long spread: 63d mean Z minus 252d mean Z (recent vs structural)
def f37da_f37_distress_risk_altman_zspread_63v252_base_v071_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    b = _mean(z, 63) - _mean(z, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# runway short-vs-long spread (recent burn vs structural)
def f37da_f37_distress_risk_altman_runwayspread_63v252_base_v072_signal(cashneq, opex):
    r = _f37_runway(cashneq, opex)
    b = _mean(r, 63) - _mean(r, 252)
    return b.replace([np.inf, -np.inf], np.nan)


# --- composite survival score ---

# survival score: runway coverage + solvency cushion, blended
def f37da_f37_distress_risk_altman_survival_126d_base_v073_signal(cashneq, opex, equity, liabilities):
    cov = np.log1p(_safe_div(cashneq, opex).clip(lower=0))
    solv = _f37_eq_liab(equity, liabilities)
    b = _mean(cov + 0.5 * np.sign(solv) * np.sqrt(solv.abs()), 126)
    return b.replace([np.inf, -np.inf], np.nan)


# capital-erosion rate: slope of equity/assets (book-value bleed)
def f37da_f37_distress_risk_altman_eqerosion_252d_base_v074_signal(equity, assets):
    b = _slope(_safe_div(equity, assets), 252)
    return b.replace([np.inf, -np.inf], np.nan)


# distress momentum: change in distress-zone occupancy quarter-over-quarter
def f37da_f37_distress_risk_altman_distmom_126d_base_v075_signal(workingcapital, retearn, ebit, equity, liabilities, assets, revenue):
    z = _f37_altman_z(workingcapital, retearn, ebit, equity, liabilities, assets, revenue)
    flag = (z < 1.81).astype(float)
    occ = flag.rolling(126, min_periods=42).mean()
    b = occ - occ.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37da_f37_distress_risk_altman_wcassets_lvl_63d_base_v001_signal,
    f37da_f37_distress_risk_altman_reassets_lvl_63d_base_v002_signal,
    f37da_f37_distress_risk_altman_ebitassets_lvl_63d_base_v003_signal,
    f37da_f37_distress_risk_altman_eqliab_lvl_63d_base_v004_signal,
    f37da_f37_distress_risk_altman_revassets_lvl_63d_base_v005_signal,
    f37da_f37_distress_risk_altman_zscore_lvl_63d_base_v006_signal,
    f37da_f37_distress_risk_altman_zprime_lvl_63d_base_v007_signal,
    f37da_f37_distress_risk_altman_distzone_126d_base_v008_signal,
    f37da_f37_distress_risk_altman_safezone_126d_base_v009_signal,
    f37da_f37_distress_risk_altman_zcushion_126d_base_v010_signal,
    f37da_f37_distress_risk_altman_runway_lvl_63d_base_v011_signal,
    f37da_f37_distress_risk_altman_runwaylog_63d_base_v012_signal,
    f37da_f37_distress_risk_altman_burnstress_21d_base_v013_signal,
    f37da_f37_distress_risk_altman_runwayre_63d_base_v014_signal,
    f37da_f37_distress_risk_altman_ebitcover_63d_base_v015_signal,
    f37da_f37_distress_risk_altman_liabassets_63d_base_v016_signal,
    f37da_f37_distress_risk_altman_liabebit_63d_base_v017_signal,
    f37da_f37_distress_risk_altman_liabrev_63d_base_v018_signal,
    f37da_f37_distress_risk_altman_negeq_126d_base_v019_signal,
    f37da_f37_distress_risk_altman_eqbuffer_63d_base_v020_signal,
    f37da_f37_distress_risk_altman_wcassetsz_252d_base_v021_signal,
    f37da_f37_distress_risk_altman_reassetsz_252d_base_v022_signal,
    f37da_f37_distress_risk_altman_ebitassetsz_252d_base_v023_signal,
    f37da_f37_distress_risk_altman_eqliabz_252d_base_v024_signal,
    f37da_f37_distress_risk_altman_revassetsz_252d_base_v025_signal,
    f37da_f37_distress_risk_altman_zscorez_504d_base_v026_signal,
    f37da_f37_distress_risk_altman_runwayz_252d_base_v027_signal,
    f37da_f37_distress_risk_altman_liabassetsz_252d_base_v028_signal,
    f37da_f37_distress_risk_altman_zscorerank_504d_base_v029_signal,
    f37da_f37_distress_risk_altman_runwayrank_504d_base_v030_signal,
    f37da_f37_distress_risk_altman_ebitassetsrank_504d_base_v031_signal,
    f37da_f37_distress_risk_altman_eqliabrank_504d_base_v032_signal,
    f37da_f37_distress_risk_altman_zslope_252d_base_v033_signal,
    f37da_f37_distress_risk_altman_runwayslope_252d_base_v034_signal,
    f37da_f37_distress_risk_altman_levslope_252d_base_v035_signal,
    f37da_f37_distress_risk_altman_reslope_252d_base_v036_signal,
    f37da_f37_distress_risk_altman_zyoy_252d_base_v037_signal,
    f37da_f37_distress_risk_altman_wcchg_126d_base_v038_signal,
    f37da_f37_distress_risk_altman_ebitchg_126d_base_v039_signal,
    f37da_f37_distress_risk_altman_runwaychg_63d_base_v040_signal,
    f37da_f37_distress_risk_altman_zlev_63d_base_v041_signal,
    f37da_f37_distress_risk_altman_runwayebit_63d_base_v042_signal,
    f37da_f37_distress_risk_altman_stresscomp_126d_base_v043_signal,
    f37da_f37_distress_risk_altman_opexrev_63d_base_v044_signal,
    f37da_f37_distress_risk_altman_opsurplus_63d_base_v045_signal,
    f37da_f37_distress_risk_altman_zvol_126d_base_v046_signal,
    f37da_f37_distress_risk_altman_runwayvol_126d_base_v047_signal,
    f37da_f37_distress_risk_altman_levvol_126d_base_v048_signal,
    f37da_f37_distress_risk_altman_cashassets_63d_base_v049_signal,
    f37da_f37_distress_risk_altman_cashliab_63d_base_v050_signal,
    f37da_f37_distress_risk_altman_wcliab_63d_base_v051_signal,
    f37da_f37_distress_risk_altman_reequity_63d_base_v052_signal,
    f37da_f37_distress_risk_altman_ebitliab_63d_base_v053_signal,
    f37da_f37_distress_risk_altman_revliab_63d_base_v054_signal,
    f37da_f37_distress_risk_altman_x3share_63d_base_v055_signal,
    f37da_f37_distress_risk_altman_x4share_63d_base_v056_signal,
    f37da_f37_distress_risk_altman_zmin_126d_base_v057_signal,
    f37da_f37_distress_risk_altman_runwaymin_126d_base_v058_signal,
    f37da_f37_distress_risk_altman_deteriorate_126d_base_v059_signal,
    f37da_f37_distress_risk_altman_improve_252d_base_v060_signal,
    f37da_f37_distress_risk_altman_zema_base_v061_signal,
    f37da_f37_distress_risk_altman_zdisp_base_v062_signal,
    f37da_f37_distress_risk_altman_runwaydisp_base_v063_signal,
    f37da_f37_distress_risk_altman_ebitshock_63d_base_v064_signal,
    f37da_f37_distress_risk_altman_levshock_63d_base_v065_signal,
    f37da_f37_distress_risk_altman_solvbalance_63d_base_v066_signal,
    f37da_f37_distress_risk_altman_runbalance_63d_base_v067_signal,
    f37da_f37_distress_risk_altman_zprimedist_252d_base_v068_signal,
    f37da_f37_distress_risk_altman_negebit_252d_base_v069_signal,
    f37da_f37_distress_risk_altman_negre_252d_base_v070_signal,
    f37da_f37_distress_risk_altman_zspread_63v252_base_v071_signal,
    f37da_f37_distress_risk_altman_runwayspread_63v252_base_v072_signal,
    f37da_f37_distress_risk_altman_survival_126d_base_v073_signal,
    f37da_f37_distress_risk_altman_eqerosion_252d_base_v074_signal,
    f37da_f37_distress_risk_altman_distmom_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_DISTRESS_RISK_ALTMAN_REGISTRY_001_075 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    cols = {}
    cols["assets"] = _fund(1, base=1e9, drift=0.0, vol=0.12).rename("assets")
    cols["revenue"] = _fund(2, base=6e8, drift=0.0, vol=0.18).rename("revenue")
    cols["liabilities"] = _fund(3, base=5e8, drift=0.0, vol=0.15).rename("liabilities")
    cols["cashneq"] = _fund(4, base=1.5e8, drift=0.0, vol=0.2).rename("cashneq")
    cols["opex"] = _fund(5, base=5e8, drift=0.0, vol=0.15).rename("opex")
    cols["workingcapital"] = _fund(6, base=2e8, drift=0.0, vol=0.22, allow_neg=True).rename("workingcapital")
    cols["retearn"] = _fund(7, base=3e8, drift=0.0, vol=0.25, allow_neg=True).rename("retearn")
    cols["ebit"] = _fund(8, base=1.2e8, drift=-0.02, vol=0.35, allow_neg=True).rename("ebit")
    cols["equity"] = _fund(9, base=4e8, drift=-0.03, vol=0.35, allow_neg=True).rename("equity")
    return cols


if __name__ == "__main__":
    cols = _build_synth()

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f37_distress_risk_altman_base_001_075_claude: %d features pass" % n_features)
