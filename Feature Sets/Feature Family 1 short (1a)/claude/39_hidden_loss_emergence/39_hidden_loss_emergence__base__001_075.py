"""hidden_loss_emergence base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about hidden losses surfacing in fundamentals (writedowns,
impairments, accrual reversals, liability spikes, equity shocks). Continued in
__base__076_150.py. Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored
rolling, explicit min_periods, no forward-looking shifts.
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


def _signed_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.sign(s) * np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.sign(s) * np.log(np.where(a > eps, a, np.nan))


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


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: asset write-down / impairment (001-020) ----

def f39_hlem_001_intangibles_qoq_drop_pct(intangibles):
    return _qoq_pct(intangibles).clip(upper=0)


def f39_hlem_002_intangibles_4q_max_minus_current_to_max(intangibles):
    mx = intangibles.rolling(4, min_periods=2).max()
    return _safe_div(mx - intangibles, mx.abs())


def f39_hlem_003_intangibles_yoy_pct(intangibles):
    return _yoy_pct(intangibles)


def f39_hlem_004_intangibles_writedown_intensity(intangibles):
    return _safe_div(intangibles.diff().clip(upper=0).abs(), intangibles.shift(1).abs())


def f39_hlem_005_intangibles_share_of_assets_qoq_drop(intangibles, assets):
    share = _safe_div(intangibles, assets)
    return share.diff().clip(upper=0)


def f39_hlem_006_ppnenet_writedown_intensity(ppnenet):
    return _safe_div(ppnenet.diff().clip(upper=0).abs(), ppnenet.shift(1).abs())


def f39_hlem_007_ppnenet_qoq_pct(ppnenet):
    return _qoq_pct(ppnenet)


def f39_hlem_008_ppnenet_share_of_assets_yoy_drop(ppnenet, assets):
    share = _safe_div(ppnenet, assets)
    return _yoy(share).clip(upper=0)


def f39_hlem_009_assets_qoq_pct_drop(assets):
    return _qoq_pct(assets).clip(upper=0)


def f39_hlem_010_assets_to_revenue_qoq_drop(assets, revenue):
    ratio = _safe_div(assets, _ttm(revenue))
    return ratio.diff().clip(upper=0)


def f39_hlem_011_negative_assets_yoy_q_share_8q(assets):
    return (_yoy(assets) < 0).rolling(8, min_periods=3).mean()


def f39_hlem_012_assets_yoy_drop_max_8q(assets):
    return _yoy(assets).rolling(8, min_periods=3).min()


def f39_hlem_013_retearn_yoy_drop_max_8q(retearn):
    return _yoy(retearn).rolling(8, min_periods=3).min()


def f39_hlem_014_intangibles_growth_minus_revenue_growth_yoy(intangibles, revenue):
    return _yoy_pct(intangibles) - _yoy_pct(_ttm(revenue))


def f39_hlem_015_tangible_assets_ratio_decline(assets, intangibles):
    ratio = _safe_div(assets - intangibles, assets)
    return _yoy(ratio).clip(upper=0)


def f39_hlem_016_impairment_charge_proxy_depamor_yoy(depamor):
    return _yoy_pct(_ttm(depamor)).clip(lower=0)


def f39_hlem_017_depamor_zscore_8q(depamor):
    return _rolling_zscore(_ttm(depamor), 8, 3).clip(lower=0)


def f39_hlem_018_assets_growth_minus_revenue_growth_yoy(assets, revenue):
    return _yoy_pct(assets) - _yoy_pct(_ttm(revenue))


def f39_hlem_019_tangible_book_yoy_drop(equity, intangibles):
    return _yoy_pct(equity - intangibles).clip(upper=0)


def f39_hlem_020_intangibles_ratio_to_assets_yoy_change(intangibles, assets):
    return _yoy(_safe_div(intangibles, assets))


# ---- Block B: GP/margin reversal / COGS spikes (021-035) ----

def f39_hlem_021_gp_qoq_drop_zscore_8q(gp):
    return -_rolling_zscore(gp.diff().clip(upper=0).abs(), 8, 3)


def f39_hlem_022_cogs_to_revenue_qoq_jump(cor, revenue):
    ratio = _safe_div(cor, revenue)
    return ratio.diff().clip(lower=0)


def f39_hlem_023_inventory_writedown_intensity(inventory):
    return _safe_div(inventory.diff().clip(upper=0).abs(), inventory.shift(1).abs())


def f39_hlem_024_inventory_drop_with_revenue_up(inventory, revenue):
    inv_drop = inventory.diff() < 0
    rev_up = revenue.diff() > 0
    score = (inv_drop & rev_up).astype(float) * _safe_div(inventory.diff().abs(), inventory.shift(1).abs())
    return score


def f39_hlem_025_gross_margin_drop_zscore_8q(gp, revenue):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return -_rolling_zscore(gm.diff().clip(upper=0).abs(), 8, 3)


def f39_hlem_026_cogs_yoy_minus_revenue_yoy(cor, revenue):
    return _yoy_pct(_ttm(cor)) - _yoy_pct(_ttm(revenue))


def f39_hlem_027_inventory_share_of_assets_drop_yoy(inventory, assets):
    return _yoy(_safe_div(inventory, assets)).clip(upper=0)


def f39_hlem_028_inventory_obsolescence_charge_intensity_8q(inventory):
    drops = inventory.diff().clip(upper=0).abs()
    return drops.rolling(8, min_periods=3).max()


def f39_hlem_029_negative_gp_q_count_8q(gp):
    return (gp < 0).rolling(8, min_periods=3).sum()


def f39_hlem_030_opinc_drop_q_count_8q(opinc):
    return (opinc.diff() < 0).rolling(8, min_periods=3).sum()


def f39_hlem_031_opinc_yoy_drop_max_8q(opinc):
    return _yoy(_ttm(opinc)).rolling(8, min_periods=3).min()


def f39_hlem_032_ebit_qoq_drop_max_8q(ebit):
    return ebit.diff().rolling(8, min_periods=3).min()


def f39_hlem_033_ebit_minus_opinc_to_revenue_jump(ebit, opinc, revenue):
    ratio = _safe_div(ebit - opinc, revenue.abs())
    return ratio.diff()


def f39_hlem_034_cogs_share_of_revenue_q(cor, revenue):
    return _safe_div(cor, revenue)


def f39_hlem_035_gross_margin_minus_8q_min(gp, revenue):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(8, min_periods=3).min()


# ---- Block C: liability emergence (036-055) ----

def f39_hlem_036_liabilities_yoy_pct(liabilities):
    return _yoy_pct(liabilities)


def f39_hlem_037_liabilities_growth_minus_assets_growth(liabilities, assets):
    return _yoy_pct(liabilities) - _yoy_pct(assets)


def f39_hlem_038_liabilitiesnc_qoq_jump_zscore(liabilitiesnc):
    return _rolling_zscore(liabilitiesnc.diff().clip(lower=0), 12, 4)


def f39_hlem_039_accruedliab_residual_yoy_jump(liabilitiesc, debtc, payables, deferredrev):
    residual = liabilitiesc - debtc - payables - deferredrev
    return _yoy_pct(residual)


def f39_hlem_040_accrued_liab_qoq_jump_share(liabilitiesc, debtc, payables, deferredrev):
    residual = liabilitiesc - debtc - payables - deferredrev
    return _safe_div(residual.diff().clip(lower=0), residual.shift(1).abs())


def f39_hlem_041_taxliabilities_qoq_jump(taxliabilities):
    return taxliabilities.diff().clip(lower=0)


def f39_hlem_042_taxliabilities_zscore_8q(taxliabilities):
    return _rolling_zscore(taxliabilities, 8, 3)


def f39_hlem_043_deferredrev_minus_revenue_growth_yoy(deferredrev, revenue):
    return _yoy_pct(deferredrev) - _yoy_pct(_ttm(revenue))


def f39_hlem_044_payables_yoy_pct(payables):
    return _yoy_pct(payables)


def f39_hlem_045_payables_yoy_minus_cogs_yoy(payables, cor):
    return _yoy_pct(payables) - _yoy_pct(_ttm(cor))


def f39_hlem_046_liabilities_minus_equity_yoy_jump(liabilities, equity):
    return _yoy(liabilities) - _yoy(equity)


def f39_hlem_047_liabilities_to_assets_qoq_jump(liabilities, assets):
    return _safe_div(liabilities, assets).diff().clip(lower=0)


def f39_hlem_048_debt_qoq_jump_zscore_8q(debt):
    return _rolling_zscore(debt.diff().clip(lower=0), 8, 3)


def f39_hlem_049_debtnc_yoy_jump(debtnc):
    return _yoy(debtnc).clip(lower=0)


def f39_hlem_050_liabilities_growth_minus_revenue_growth_gap(liabilities, revenue):
    return _yoy_pct(liabilities) - _yoy_pct(_ttm(revenue))


def f39_hlem_051_liabilities_to_workingcapital_jump(liabilities, workingcapital):
    return _safe_div(liabilities, workingcapital.abs()).diff()


def f39_hlem_052_liabilities_qoq_pct(liabilities):
    return _qoq_pct(liabilities)


def f39_hlem_053_liabilities_share_of_assets_yoy_change(liabilities, assets):
    return _yoy(_safe_div(liabilities, assets))


def f39_hlem_054_accruedliab_share_of_liabilities(liabilitiesc, debtc, payables, deferredrev, liabilities):
    residual = liabilitiesc - debtc - payables - deferredrev
    return _safe_div(residual, liabilities)


def f39_hlem_055_liability_emergence_zscore_aggregate_8q(liabilities, taxliabilities, deferredrev):
    z_liab = _rolling_zscore(liabilities.diff().clip(lower=0), 8, 3)
    z_tax = _rolling_zscore(taxliabilities.diff().clip(lower=0), 8, 3)
    z_def = _rolling_zscore(deferredrev.diff().clip(lower=0), 8, 3)
    return (z_liab + z_tax + z_def) / 3.0


# ---- Block D: equity / retearn shocks (056-075) ----

def f39_hlem_056_retearn_qoq_change_zscore_8q(retearn):
    return _rolling_zscore(retearn.diff(), 8, 3).clip(upper=0).abs() * -1


def f39_hlem_057_negative_retearn_change_q_count_8q(retearn):
    return (retearn.diff() < 0).rolling(8, min_periods=3).sum()


def f39_hlem_058_equity_qoq_drop_max_8q(equity):
    return equity.diff().rolling(8, min_periods=3).min()


def f39_hlem_059_equity_yoy_drop_max_8q(equity):
    return _yoy(equity).rolling(8, min_periods=3).min()


def f39_hlem_060_equity_minus_paid_in_share_drop(equity, retearn, accoci):
    paid_in_proxy = equity - retearn - accoci
    return _yoy(paid_in_proxy)


def f39_hlem_061_retearn_yoy_drop_pct(retearn):
    return _yoy_pct(retearn).clip(upper=0)


def f39_hlem_062_retearn_share_of_equity_drop(retearn, equity):
    return _yoy(_safe_div(retearn, equity)).clip(upper=0)


def f39_hlem_063_accoci_qoq_change_zscore_8q(accoci):
    return _rolling_zscore(accoci.diff(), 8, 3)


def f39_hlem_064_accoci_yoy_change_abs(accoci):
    return _yoy(accoci).abs()


def f39_hlem_065_accoci_negative_q_count_8q(accoci):
    return (accoci.diff() < 0).rolling(8, min_periods=3).sum()


def f39_hlem_066_equity_change_residual(equity, retearn, accoci, netinc, ncfcommon):
    expected_change = netinc + ncfcommon + accoci.diff()
    actual_change = equity.diff()
    return actual_change - expected_change


def f39_hlem_067_equity_writedown_intensity_zscore_8q(equity):
    return -_rolling_zscore(equity.diff().clip(upper=0).abs(), 8, 3)


def f39_hlem_068_negative_equity_proximity(equity, assets):
    return _safe_div(-equity, assets.abs())


def f39_hlem_069_bvps_yoy_drop(equity, shareswadil):
    return _yoy_pct(_safe_div(equity, shareswadil)).clip(upper=0)


def f39_hlem_070_tangible_equity_yoy_drop(equity, intangibles):
    return _yoy_pct(equity - intangibles).clip(upper=0)


def f39_hlem_071_retearn_share_of_assets_yoy_drop(retearn, assets):
    return _yoy(_safe_div(retearn, assets)).clip(upper=0)


def f39_hlem_072_equity_minus_intangibles_to_assets_drop(equity, intangibles, assets):
    return _yoy(_safe_div(equity - intangibles, assets)).clip(upper=0)


def f39_hlem_073_consecutive_retearn_drop_streak_8q(retearn):
    drops = (retearn.diff() < 0).astype(int)
    return drops.rolling(8, min_periods=3).apply(lambda w: int(w[::-1].cumprod().sum()), raw=True)


def f39_hlem_074_equity_destruction_share_8q(equity):
    losses = equity.diff().clip(upper=0).abs()
    return _safe_div(losses.rolling(8, min_periods=3).sum(), equity.shift(8).abs())


def f39_hlem_075_equity_yoy_minus_netinc_ttm_share(equity, netinc, assets):
    expected = _ttm(netinc)
    actual = _yoy(equity)
    return _safe_div(actual - expected, assets)


# ============================================================
#                        REGISTRY
# ============================================================

HIDDEN_LOSS_EMERGENCE_BASE_REGISTRY_001_075 = {
    "f39_hlem_001_intangibles_qoq_drop_pct": {"inputs": ["intangibles"], "func": f39_hlem_001_intangibles_qoq_drop_pct},
    "f39_hlem_002_intangibles_4q_max_minus_current_to_max": {"inputs": ["intangibles"], "func": f39_hlem_002_intangibles_4q_max_minus_current_to_max},
    "f39_hlem_003_intangibles_yoy_pct": {"inputs": ["intangibles"], "func": f39_hlem_003_intangibles_yoy_pct},
    "f39_hlem_004_intangibles_writedown_intensity": {"inputs": ["intangibles"], "func": f39_hlem_004_intangibles_writedown_intensity},
    "f39_hlem_005_intangibles_share_of_assets_qoq_drop": {"inputs": ["intangibles", "assets"], "func": f39_hlem_005_intangibles_share_of_assets_qoq_drop},
    "f39_hlem_006_ppnenet_writedown_intensity": {"inputs": ["ppnenet"], "func": f39_hlem_006_ppnenet_writedown_intensity},
    "f39_hlem_007_ppnenet_qoq_pct": {"inputs": ["ppnenet"], "func": f39_hlem_007_ppnenet_qoq_pct},
    "f39_hlem_008_ppnenet_share_of_assets_yoy_drop": {"inputs": ["ppnenet", "assets"], "func": f39_hlem_008_ppnenet_share_of_assets_yoy_drop},
    "f39_hlem_009_assets_qoq_pct_drop": {"inputs": ["assets"], "func": f39_hlem_009_assets_qoq_pct_drop},
    "f39_hlem_010_assets_to_revenue_qoq_drop": {"inputs": ["assets", "revenue"], "func": f39_hlem_010_assets_to_revenue_qoq_drop},
    "f39_hlem_011_negative_assets_yoy_q_share_8q": {"inputs": ["assets"], "func": f39_hlem_011_negative_assets_yoy_q_share_8q},
    "f39_hlem_012_assets_yoy_drop_max_8q": {"inputs": ["assets"], "func": f39_hlem_012_assets_yoy_drop_max_8q},
    "f39_hlem_013_retearn_yoy_drop_max_8q": {"inputs": ["retearn"], "func": f39_hlem_013_retearn_yoy_drop_max_8q},
    "f39_hlem_014_intangibles_growth_minus_revenue_growth_yoy": {"inputs": ["intangibles", "revenue"], "func": f39_hlem_014_intangibles_growth_minus_revenue_growth_yoy},
    "f39_hlem_015_tangible_assets_ratio_decline": {"inputs": ["assets", "intangibles"], "func": f39_hlem_015_tangible_assets_ratio_decline},
    "f39_hlem_016_impairment_charge_proxy_depamor_yoy": {"inputs": ["depamor"], "func": f39_hlem_016_impairment_charge_proxy_depamor_yoy},
    "f39_hlem_017_depamor_zscore_8q": {"inputs": ["depamor"], "func": f39_hlem_017_depamor_zscore_8q},
    "f39_hlem_018_assets_growth_minus_revenue_growth_yoy": {"inputs": ["assets", "revenue"], "func": f39_hlem_018_assets_growth_minus_revenue_growth_yoy},
    "f39_hlem_019_tangible_book_yoy_drop": {"inputs": ["equity", "intangibles"], "func": f39_hlem_019_tangible_book_yoy_drop},
    "f39_hlem_020_intangibles_ratio_to_assets_yoy_change": {"inputs": ["intangibles", "assets"], "func": f39_hlem_020_intangibles_ratio_to_assets_yoy_change},
    "f39_hlem_021_gp_qoq_drop_zscore_8q": {"inputs": ["gp"], "func": f39_hlem_021_gp_qoq_drop_zscore_8q},
    "f39_hlem_022_cogs_to_revenue_qoq_jump": {"inputs": ["cor", "revenue"], "func": f39_hlem_022_cogs_to_revenue_qoq_jump},
    "f39_hlem_023_inventory_writedown_intensity": {"inputs": ["inventory"], "func": f39_hlem_023_inventory_writedown_intensity},
    "f39_hlem_024_inventory_drop_with_revenue_up": {"inputs": ["inventory", "revenue"], "func": f39_hlem_024_inventory_drop_with_revenue_up},
    "f39_hlem_025_gross_margin_drop_zscore_8q": {"inputs": ["gp", "revenue"], "func": f39_hlem_025_gross_margin_drop_zscore_8q},
    "f39_hlem_026_cogs_yoy_minus_revenue_yoy": {"inputs": ["cor", "revenue"], "func": f39_hlem_026_cogs_yoy_minus_revenue_yoy},
    "f39_hlem_027_inventory_share_of_assets_drop_yoy": {"inputs": ["inventory", "assets"], "func": f39_hlem_027_inventory_share_of_assets_drop_yoy},
    "f39_hlem_028_inventory_obsolescence_charge_intensity_8q": {"inputs": ["inventory"], "func": f39_hlem_028_inventory_obsolescence_charge_intensity_8q},
    "f39_hlem_029_negative_gp_q_count_8q": {"inputs": ["gp"], "func": f39_hlem_029_negative_gp_q_count_8q},
    "f39_hlem_030_opinc_drop_q_count_8q": {"inputs": ["opinc"], "func": f39_hlem_030_opinc_drop_q_count_8q},
    "f39_hlem_031_opinc_yoy_drop_max_8q": {"inputs": ["opinc"], "func": f39_hlem_031_opinc_yoy_drop_max_8q},
    "f39_hlem_032_ebit_qoq_drop_max_8q": {"inputs": ["ebit"], "func": f39_hlem_032_ebit_qoq_drop_max_8q},
    "f39_hlem_033_ebit_minus_opinc_to_revenue_jump": {"inputs": ["ebit", "opinc", "revenue"], "func": f39_hlem_033_ebit_minus_opinc_to_revenue_jump},
    "f39_hlem_034_cogs_share_of_revenue_q": {"inputs": ["cor", "revenue"], "func": f39_hlem_034_cogs_share_of_revenue_q},
    "f39_hlem_035_gross_margin_minus_8q_min": {"inputs": ["gp", "revenue"], "func": f39_hlem_035_gross_margin_minus_8q_min},
    "f39_hlem_036_liabilities_yoy_pct": {"inputs": ["liabilities"], "func": f39_hlem_036_liabilities_yoy_pct},
    "f39_hlem_037_liabilities_growth_minus_assets_growth": {"inputs": ["liabilities", "assets"], "func": f39_hlem_037_liabilities_growth_minus_assets_growth},
    "f39_hlem_038_liabilitiesnc_qoq_jump_zscore": {"inputs": ["liabilitiesnc"], "func": f39_hlem_038_liabilitiesnc_qoq_jump_zscore},
    "f39_hlem_039_accruedliab_residual_yoy_jump": {"inputs": ["liabilitiesc", "debtc", "payables", "deferredrev"], "func": f39_hlem_039_accruedliab_residual_yoy_jump},
    "f39_hlem_040_accrued_liab_qoq_jump_share": {"inputs": ["liabilitiesc", "debtc", "payables", "deferredrev"], "func": f39_hlem_040_accrued_liab_qoq_jump_share},
    "f39_hlem_041_taxliabilities_qoq_jump": {"inputs": ["taxliabilities"], "func": f39_hlem_041_taxliabilities_qoq_jump},
    "f39_hlem_042_taxliabilities_zscore_8q": {"inputs": ["taxliabilities"], "func": f39_hlem_042_taxliabilities_zscore_8q},
    "f39_hlem_043_deferredrev_minus_revenue_growth_yoy": {"inputs": ["deferredrev", "revenue"], "func": f39_hlem_043_deferredrev_minus_revenue_growth_yoy},
    "f39_hlem_044_payables_yoy_pct": {"inputs": ["payables"], "func": f39_hlem_044_payables_yoy_pct},
    "f39_hlem_045_payables_yoy_minus_cogs_yoy": {"inputs": ["payables", "cor"], "func": f39_hlem_045_payables_yoy_minus_cogs_yoy},
    "f39_hlem_046_liabilities_minus_equity_yoy_jump": {"inputs": ["liabilities", "equity"], "func": f39_hlem_046_liabilities_minus_equity_yoy_jump},
    "f39_hlem_047_liabilities_to_assets_qoq_jump": {"inputs": ["liabilities", "assets"], "func": f39_hlem_047_liabilities_to_assets_qoq_jump},
    "f39_hlem_048_debt_qoq_jump_zscore_8q": {"inputs": ["debt"], "func": f39_hlem_048_debt_qoq_jump_zscore_8q},
    "f39_hlem_049_debtnc_yoy_jump": {"inputs": ["debtnc"], "func": f39_hlem_049_debtnc_yoy_jump},
    "f39_hlem_050_liabilities_growth_minus_revenue_growth_gap": {"inputs": ["liabilities", "revenue"], "func": f39_hlem_050_liabilities_growth_minus_revenue_growth_gap},
    "f39_hlem_051_liabilities_to_workingcapital_jump": {"inputs": ["liabilities", "workingcapital"], "func": f39_hlem_051_liabilities_to_workingcapital_jump},
    "f39_hlem_052_liabilities_qoq_pct": {"inputs": ["liabilities"], "func": f39_hlem_052_liabilities_qoq_pct},
    "f39_hlem_053_liabilities_share_of_assets_yoy_change": {"inputs": ["liabilities", "assets"], "func": f39_hlem_053_liabilities_share_of_assets_yoy_change},
    "f39_hlem_054_accruedliab_share_of_liabilities": {"inputs": ["liabilitiesc", "debtc", "payables", "deferredrev", "liabilities"], "func": f39_hlem_054_accruedliab_share_of_liabilities},
    "f39_hlem_055_liability_emergence_zscore_aggregate_8q": {"inputs": ["liabilities", "taxliabilities", "deferredrev"], "func": f39_hlem_055_liability_emergence_zscore_aggregate_8q},
    "f39_hlem_056_retearn_qoq_change_zscore_8q": {"inputs": ["retearn"], "func": f39_hlem_056_retearn_qoq_change_zscore_8q},
    "f39_hlem_057_negative_retearn_change_q_count_8q": {"inputs": ["retearn"], "func": f39_hlem_057_negative_retearn_change_q_count_8q},
    "f39_hlem_058_equity_qoq_drop_max_8q": {"inputs": ["equity"], "func": f39_hlem_058_equity_qoq_drop_max_8q},
    "f39_hlem_059_equity_yoy_drop_max_8q": {"inputs": ["equity"], "func": f39_hlem_059_equity_yoy_drop_max_8q},
    "f39_hlem_060_equity_minus_paid_in_share_drop": {"inputs": ["equity", "retearn", "accoci"], "func": f39_hlem_060_equity_minus_paid_in_share_drop},
    "f39_hlem_061_retearn_yoy_drop_pct": {"inputs": ["retearn"], "func": f39_hlem_061_retearn_yoy_drop_pct},
    "f39_hlem_062_retearn_share_of_equity_drop": {"inputs": ["retearn", "equity"], "func": f39_hlem_062_retearn_share_of_equity_drop},
    "f39_hlem_063_accoci_qoq_change_zscore_8q": {"inputs": ["accoci"], "func": f39_hlem_063_accoci_qoq_change_zscore_8q},
    "f39_hlem_064_accoci_yoy_change_abs": {"inputs": ["accoci"], "func": f39_hlem_064_accoci_yoy_change_abs},
    "f39_hlem_065_accoci_negative_q_count_8q": {"inputs": ["accoci"], "func": f39_hlem_065_accoci_negative_q_count_8q},
    "f39_hlem_066_equity_change_residual": {"inputs": ["equity", "retearn", "accoci", "netinc", "ncfcommon"], "func": f39_hlem_066_equity_change_residual},
    "f39_hlem_067_equity_writedown_intensity_zscore_8q": {"inputs": ["equity"], "func": f39_hlem_067_equity_writedown_intensity_zscore_8q},
    "f39_hlem_068_negative_equity_proximity": {"inputs": ["equity", "assets"], "func": f39_hlem_068_negative_equity_proximity},
    "f39_hlem_069_bvps_yoy_drop": {"inputs": ["equity", "shareswadil"], "func": f39_hlem_069_bvps_yoy_drop},
    "f39_hlem_070_tangible_equity_yoy_drop": {"inputs": ["equity", "intangibles"], "func": f39_hlem_070_tangible_equity_yoy_drop},
    "f39_hlem_071_retearn_share_of_assets_yoy_drop": {"inputs": ["retearn", "assets"], "func": f39_hlem_071_retearn_share_of_assets_yoy_drop},
    "f39_hlem_072_equity_minus_intangibles_to_assets_drop": {"inputs": ["equity", "intangibles", "assets"], "func": f39_hlem_072_equity_minus_intangibles_to_assets_drop},
    "f39_hlem_073_consecutive_retearn_drop_streak_8q": {"inputs": ["retearn"], "func": f39_hlem_073_consecutive_retearn_drop_streak_8q},
    "f39_hlem_074_equity_destruction_share_8q": {"inputs": ["equity"], "func": f39_hlem_074_equity_destruction_share_8q},
    "f39_hlem_075_equity_yoy_minus_netinc_ttm_share": {"inputs": ["equity", "netinc", "assets"], "func": f39_hlem_075_equity_yoy_minus_netinc_ttm_share},
}
