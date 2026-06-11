"""Family f106 - Underused source-backed fundamental fields.

Sharadar tables: FUNDAMENTALS
Fields: accoci, assetsnc, de, deposits, divyield, ebitdausd, ebitusd, epsusd,
equityavg, equityusd, fxusd, investmentsnc, liabilitiesnc, ncf, ncfbus,
ncfinv, ncfx, netinccmn, netinccmnusd, netincdis, netincnci, pe1, ps1, ros,
taxliabilities.

These fields exist in silverdb but were not materially used by the original
feature families. The functions below focus on biotech-relevant balance-sheet
composition, USD normalization, discontinued/non-controlling income quality,
FX effects, and valuation fallbacks.
"""
import numpy as np
import pandas as pd


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _z(s, w):
    m = _mean(s, w)
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return _clean(_safe_div(s - m, sd))


def uff_f106_accoci_to_equity_signal(accoci, equity):
    return _clean(_safe_div(accoci, equity.abs()))


def uff_f106_accoci_to_assets_signal(accoci, assets):
    return _clean(_safe_div(accoci, assets.abs()))


def uff_f106_noncurrent_asset_share_signal(assetsnc, assets):
    return _clean(_safe_div(assetsnc, assets))


def uff_f106_noncurrent_liability_share_signal(liabilitiesnc, liabilities):
    return _clean(_safe_div(liabilitiesnc, liabilities))


def uff_f106_noncurrent_investment_share_signal(investmentsnc, assets):
    return _clean(_safe_div(investmentsnc, assets))


def uff_f106_de_ratio_signal(de):
    return _clean(de)


def uff_f106_deposits_to_assets_signal(deposits, assets):
    return _clean(_safe_div(deposits, assets))


def uff_f106_divyield_signal(divyield):
    return _clean(divyield)


def uff_f106_ebit_usd_to_reported_signal(ebitusd, ebit):
    return _clean(_safe_div(ebitusd, ebit))


def uff_f106_ebitda_usd_to_reported_signal(ebitdausd, ebitda):
    return _clean(_safe_div(ebitdausd, ebitda))


def uff_f106_equity_usd_to_reported_signal(equityusd, equity):
    return _clean(_safe_div(equityusd, equity))


def uff_f106_eps_usd_to_reported_signal(epsusd, eps):
    return _clean(_safe_div(epsusd, eps))


def uff_f106_fxusd_signal(fxusd):
    return _clean(fxusd)


def uff_f106_fxusd_252d_z_signal(fxusd):
    return _z(fxusd, 252)


def uff_f106_common_income_share_signal(netinccmn, netinc):
    return _clean(_safe_div(netinccmn, netinc))


def uff_f106_common_income_usd_share_signal(netinccmnusd, netinccmn):
    return _clean(_safe_div(netinccmnusd, netinccmn))


def uff_f106_discontinued_income_drag_signal(netincdis, netinc):
    return _clean(_safe_div(netincdis, netinc.abs()))


def uff_f106_noncontrolling_income_share_signal(netincnci, netinc):
    return _clean(_safe_div(netincnci, netinc.abs()))


def uff_f106_total_ncf_to_assets_signal(ncf, assets):
    return _clean(_safe_div(ncf, assets))


def uff_f106_business_acquisition_cashflow_to_assets_signal(ncfbus, assets):
    return _clean(_safe_div(ncfbus, assets))


def uff_f106_investment_purchase_cashflow_to_assets_signal(ncfinv, assets):
    return _clean(_safe_div(ncfinv, assets))


def uff_f106_fx_cashflow_to_assets_signal(ncfx, assets):
    return _clean(_safe_div(ncfx, assets))


def uff_f106_tax_liability_to_assets_signal(taxliabilities, assets):
    return _clean(_safe_div(taxliabilities, assets))


def uff_f106_tax_asset_liability_spread_signal(taxassets, taxliabilities, assets):
    return _clean(_safe_div(taxassets - taxliabilities, assets))


def uff_f106_equityavg_to_assetsavg_signal(equityavg, assetsavg):
    return _clean(_safe_div(equityavg, assetsavg))


def uff_f106_forward_pe_signal(pe1):
    return _clean(pe1)


def uff_f106_forward_ps_signal(ps1):
    return _clean(ps1)


def uff_f106_forward_pe_to_trailing_pe_signal(pe1, pe):
    return _clean(_safe_div(pe1, pe))


def uff_f106_forward_ps_to_trailing_ps_signal(ps1, ps):
    return _clean(_safe_div(ps1, ps))


def uff_f106_return_on_sales_signal(ros):
    return _clean(ros)


def uff_f106_income_quality_stack_signal(netincdis, netincnci, accoci, netinc, equity):
    frame = pd.concat([
        _safe_div(netincdis, netinc.abs()),
        _safe_div(netincnci, netinc.abs()),
        _safe_div(accoci, equity.abs()),
    ], axis=1)
    return _clean(frame.abs().sum(axis=1))
