"""Family f105 - Insider transaction microstructure from silver DB sf2 | third derivatives 001-012."""
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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _code(transactioncode, values):
    return transactioncode.fillna("").astype(str).str.upper().isin(values).astype(float)


def _yes(flag):
    return flag.fillna("").astype(str).str.upper().eq("Y").astype(float)


def _txn_value(transactionshares, transactionpricepershare, transactionvalue):
    computed = transactionshares.abs() * transactionpricepershare.abs()
    return transactionvalue.where(transactionvalue.notna(), computed)


def itm_f105_insider_transaction_microstructure_open_purchase_value_90d_accel_v001_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    base = _sum(_txn_value(transactionshares, transactionpricepershare, transactionvalue) * _code(transactioncode, {"P"}), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_open_sale_value_90d_accel_v002_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    base = _sum(_txn_value(transactionshares, transactionpricepershare, transactionvalue) * _code(transactioncode, {"S"}), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_open_market_net_value_90d_accel_v003_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    base = _sum(val * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_open_market_net_value_180d_accel_v004_signal(transactioncode, transactionshares, transactionpricepershare, transactionvalue):
    val = _txn_value(transactionshares, transactionpricepershare, transactionvalue)
    base = _sum(val * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})), 180)
    return _clean(_accel(base, 60))


def itm_f105_insider_transaction_microstructure_non_open_market_activity_90d_accel_v005_signal(transactioncode, transactionvalue):
    base = _sum(transactionvalue.abs() * _code(transactioncode, {"A", "M", "F", "G"}), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_officer_net_flow_90d_accel_v006_signal(transactioncode, transactionvalue, isofficer):
    base = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(isofficer), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_director_net_flow_90d_accel_v007_signal(transactioncode, transactionvalue, isdirector):
    base = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(isdirector), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_tenpct_owner_net_flow_90d_accel_v008_signal(transactioncode, transactionvalue, istenpercentowner):
    base = _sum(transactionvalue * (_code(transactioncode, {"P"}) - _code(transactioncode, {"S"})) * _yes(istenpercentowner), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_value_to_prior_ownership_90d_accel_v009_signal(transactionvalue, sharesownedbeforetransaction, transactionpricepershare):
    prior_value = sharesownedbeforetransaction.abs() * transactionpricepershare.abs()
    base = _mean(_safe_div(transactionvalue.abs(), prior_value), 90)
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_exercise_discount_accel_v010_signal(priceexercisable, transactionpricepershare):
    base = _safe_div(transactionpricepershare - priceexercisable, transactionpricepershare.abs())
    return _clean(_accel(base, 30))


def itm_f105_insider_transaction_microstructure_derivative_disposition_180d_accel_v011_signal(securityadcode, transactionvalue):
    is_deriv_disposition = securityadcode.fillna("").astype(str).str.upper().isin({"D", "DA", "DD"}).astype(float)
    return _clean(_accel(_sum(transactionvalue.abs() * is_deriv_disposition, 180), 60))


def itm_f105_insider_transaction_microstructure_nonderivative_acquisition_180d_accel_v012_signal(securityadcode, transactionvalue):
    is_nonderiv_acq = securityadcode.fillna("").astype(str).str.upper().isin({"N", "ND"}).astype(float)
    return _clean(_accel(_sum(transactionvalue.abs() * is_nonderiv_acq, 180), 60))
