"""Family f105 - Insider transaction microstructure from silver DB sf2 | base 001-012."""
import numpy as np
import pandas as pd


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _code(transactioncode, values):
    return transactioncode.fillna("").astype(str).str.upper().isin(values).astype(float)


def _yes(flag):
    return flag.fillna("").astype(str).str.upper().eq("Y").astype(float)


def _txn_value(transactionshares, transactionpricepershare, transactionvalue):
    computed = transactionshares.abs() * transactionpricepershare.abs()
    return transactionvalue.where(transactionvalue.notna(), computed)


# 90d open-market purchase value
def itm_f105_insider_transaction_microstructure_open_purchase_value_90d_base_v001_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    result = _sum(val * _code(transactioncode, {"P"}), 90)
    return _clean(result)


# 90d open-market sale value
def itm_f105_insider_transaction_microstructure_open_sale_value_90d_base_v002_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    result = _sum(val * _code(transactioncode, {"S"}), 90)
    return _clean(result)


# 90d purchase minus sale value
def itm_f105_insider_transaction_microstructure_open_market_net_value_90d_base_v003_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    result = _sum(val * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})), 90)
    return _clean(result)


# 180d purchase minus sale value
def itm_f105_insider_transaction_microstructure_open_market_net_value_180d_base_v004_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    result = _sum(val * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})), 180)
    return _clean(result)


# 90d grant/exercise/tax-withholding activity
def itm_f105_insider_transaction_microstructure_non_open_market_activity_90d_base_v005_signal(transactioncode, transactionvalue):
    result = _sum(transactionvalue.abs() * _code(transactioncode, {"A", "M", "F", "G"}), 90)
    return _clean(result)


# 90d officer-weighted net open-market flow
def itm_f105_insider_transaction_microstructure_officer_net_flow_90d_base_v006_signal(transactioncode, transactionvalue, isofficer):
    result = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(isofficer), 90)
    return _clean(result)


# 90d director-weighted net open-market flow
def itm_f105_insider_transaction_microstructure_director_net_flow_90d_base_v007_signal(transactioncode, transactionvalue, isdirector):
    result = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(isdirector), 90)
    return _clean(result)


# 90d ten-percent-owner-weighted net open-market flow
def itm_f105_insider_transaction_microstructure_tenpct_owner_net_flow_90d_base_v008_signal(transactioncode, transactionvalue, istenpercentowner):
    result = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(istenpercentowner), 90)
    return _clean(result)


# Transaction value relative to prior insider ownership
def itm_f105_insider_transaction_microstructure_value_to_prior_ownership_90d_base_v009_signal(transactionvalue, sharesownedbeforetransaction, transactionpricepershare):
    prior_value = sharesownedbeforetransaction.abs() * transactionpricepershare.abs()
    result = _mean(_safe_div(transactionvalue.abs(), prior_value), 90)
    return _clean(result)


# Exercise discount proxy
def itm_f105_insider_transaction_microstructure_exercise_discount_base_v010_signal(priceexercisable, transactionpricepershare):
    result = _safe_div(transactionpricepershare - priceexercisable, transactionpricepershare.abs())
    return _clean(result)


# Derivative disposition pressure
def itm_f105_insider_transaction_microstructure_derivative_disposition_180d_base_v011_signal(securityadcode, transactionvalue):
    is_deriv_disposition = securityadcode.fillna("").astype(str).str.upper().isin({"D", "DA", "DD"}).astype(float)
    result = _sum(transactionvalue.abs() * is_deriv_disposition, 180)
    return _clean(result)


# Non-derivative acquisition pressure
def itm_f105_insider_transaction_microstructure_nonderivative_acquisition_180d_base_v012_signal(securityadcode, transactionvalue):
    is_nonderiv_acq = securityadcode.fillna("").astype(str).str.upper().isin({"N", "ND"}).astype(float)
    result = _sum(transactionvalue.abs() * is_nonderiv_acq, 180)
    return _clean(result)
