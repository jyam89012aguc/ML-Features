
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


def gm_f108_biotech_f108_underused_fundamental_fields_accoci_to_equity_signal(accoci, equity):
    return _safe_div(accoci, equity.abs()).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_accoci_to_assets_signal(accoci, assets):
    return _safe_div(accoci, assets.abs()).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_noncurrent_asset_share_signal(assetsnc, assets):
    return _safe_div(assetsnc, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_noncurrent_liability_share_signal(liabilitiesnc, liabilities):
    return _safe_div(liabilitiesnc, liabilities).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_noncurrent_investment_share_signal(investmentsnc, assets):
    return _safe_div(investmentsnc, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_de_ratio_signal(de):
    return de.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_deposits_to_assets_signal(deposits, assets):
    return _safe_div(deposits, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_divyield_signal(divyield):
    return divyield.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_ebit_usd_to_reported_signal(ebitusd, ebit):
    return _safe_div(ebitusd, ebit).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_ebitda_usd_to_reported_signal(ebitdausd, ebitda):
    return _safe_div(ebitdausd, ebitda).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_equity_usd_to_reported_signal(equityusd, equity):
    return _safe_div(equityusd, equity).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_eps_usd_to_reported_signal(epsusd, eps):
    return _safe_div(epsusd, eps).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_fxusd_signal(fxusd):
    return fxusd.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_fxusd_252d_z_signal(fxusd):
    return _z(fxusd, 252).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_common_income_share_signal(netinccmn, netinc):
    return _safe_div(netinccmn, netinc).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_common_income_usd_share_signal(netinccmnusd, netinccmn):
    return _safe_div(netinccmnusd, netinccmn).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_discontinued_income_drag_signal(netincdis, netinc):
    return _safe_div(netincdis, netinc.abs()).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_noncontrolling_income_share_signal(netincnci, netinc):
    return _safe_div(netincnci, netinc.abs()).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_total_ncf_to_assets_signal(ncf, assets):
    return _safe_div(ncf, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_business_acquisition_cashflow_to_assets_signal(ncfbus, assets):
    return _safe_div(ncfbus, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_investment_purchase_cashflow_to_assets_signal(ncfinv, assets):
    return _safe_div(ncfinv, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_fx_cashflow_to_assets_signal(ncfx, assets):
    return _safe_div(ncfx, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_tax_liability_to_assets_signal(taxliabilities, assets):
    return _safe_div(taxliabilities, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_tax_asset_liability_spread_signal(taxassets, taxliabilities, assets):
    return _safe_div(taxassets - taxliabilities, assets).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_equityavg_to_assetsavg_signal(equityavg, assetsavg):
    return _safe_div(equityavg, assetsavg).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_forward_pe_signal(pe1):
    return pe1.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_forward_ps_signal(ps1):
    return ps1.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_forward_pe_to_trailing_pe_signal(pe1, pe):
    return _safe_div(pe1, pe).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_forward_ps_to_trailing_ps_signal(ps1, ps):
    return _safe_div(ps1, ps).replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_return_on_sales_signal(ros):
    return ros.replace([np.inf, -np.inf], np.nan)


def gm_f108_biotech_f108_underused_fundamental_fields_income_quality_stack_signal(netincdis, netincnci, accoci, netinc, equity):
    frame = pd.concat([
        _safe_div(netincdis, netinc.abs()),
        _safe_div(netincnci, netinc.abs()),
        _safe_div(accoci, equity.abs()),
    ], axis=1)
    return frame.abs().sum(axis=1).replace([np.inf, -np.inf], np.nan)
