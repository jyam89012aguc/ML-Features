"""Family f102 - Institutional derivative positioning.

Sharadar tables: SF3A, SF3B
Fields: shrholders, cllholders, putholders, wntholders, dbtholders,
prfholders, fndholders, undholders, shrunits, cllunits, putunits, wntunits,
dbtunits, prfunits, fndunits, undunits, shrvalue, cllvalue, putvalue,
wntvalue, dbtvalue, prfvalue, fndvalue, undvalue, totalvalue, percentoftotal.

This fills the main ownership gap left by f095-f097, which mostly use aggregate
value/units and do not exploit option, warrant, debt, preferred, and fund holder
breadth from SF3A/SF3B.
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


def _sum_cols(*series):
    return pd.concat(series, axis=1).sum(axis=1)


def idp_f102_call_put_holder_ratio_signal(cllholders, putholders):
    return _clean(_safe_div(cllholders, putholders))


def idp_f102_call_put_unit_ratio_signal(cllunits, putunits):
    return _clean(_safe_div(cllunits, putunits))


def idp_f102_warrant_unit_share_signal(wntunits, shrunits):
    return _clean(_safe_div(wntunits, shrunits + wntunits))


def idp_f102_debt_preferred_unit_share_signal(dbtunits, prfunits, shrunits):
    return _clean(_safe_div(dbtunits + prfunits, shrunits + dbtunits + prfunits))


def idp_f102_fund_unit_share_signal(fndunits, shrunits):
    return _clean(_safe_div(fndunits, shrunits + fndunits))


def idp_f102_underlying_unit_share_signal(undunits, shrunits):
    return _clean(_safe_div(undunits, shrunits + undunits))


def idp_f102_call_put_value_ratio_signal(cllvalue, putvalue):
    return _clean(_safe_div(cllvalue, putvalue))


def idp_f102_option_holder_share_signal(cllholders, putholders, shrholders):
    return _clean(_safe_div(cllholders + putholders, shrholders + cllholders + putholders))


def idp_f102_option_value_share_signal(cllvalue, putvalue, totalvalue):
    return _clean(_safe_div(cllvalue + putvalue, totalvalue))


def idp_f102_warrant_holder_share_signal(wntholders, shrholders):
    return _clean(_safe_div(wntholders, shrholders + wntholders))


def idp_f102_warrant_value_share_signal(wntvalue, totalvalue):
    return _clean(_safe_div(wntvalue, totalvalue))


def idp_f102_debt_preferred_holder_share_signal(dbtholders, prfholders, shrholders):
    return _clean(_safe_div(dbtholders + prfholders, shrholders + dbtholders + prfholders))


def idp_f102_debt_preferred_value_share_signal(dbtvalue, prfvalue, totalvalue):
    return _clean(_safe_div(dbtvalue + prfvalue, totalvalue))


def idp_f102_fund_holder_share_signal(fndholders, shrholders):
    return _clean(_safe_div(fndholders, shrholders + fndholders))


def idp_f102_fund_value_share_signal(fndvalue, totalvalue):
    return _clean(_safe_div(fndvalue, totalvalue))


def idp_f102_underlying_value_share_signal(undvalue, totalvalue):
    return _clean(_safe_div(undvalue, totalvalue))


def idp_f102_non_common_value_share_signal(cllvalue, putvalue, wntvalue, dbtvalue, prfvalue, fndvalue, undvalue, totalvalue):
    non_common = _sum_cols(cllvalue, putvalue, wntvalue, dbtvalue, prfvalue, fndvalue, undvalue)
    return _clean(_safe_div(non_common, totalvalue))


def idp_f102_non_common_holder_share_signal(cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders, shrholders):
    non_common = _sum_cols(cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders)
    return _clean(_safe_div(non_common, shrholders + non_common))


def idp_f102_short_bias_value_signal(putvalue, cllvalue, shrvalue):
    return _clean(_safe_div(putvalue - cllvalue, shrvalue.abs()))


def idp_f102_convexity_bias_value_signal(cllvalue, putvalue, wntvalue, shrvalue):
    return _clean(_safe_div(cllvalue + putvalue + wntvalue, shrvalue.abs()))


def idp_f102_claim_seniority_value_signal(dbtvalue, prfvalue, shrvalue):
    return _clean(_safe_div(dbtvalue + prfvalue, shrvalue.abs()))


def idp_f102_holder_breadth_total_signal(shrholders, cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders):
    return _clean(_sum_cols(shrholders, cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders))


def idp_f102_holding_breadth_total_signal(shrholdings, cllholdings, putholdings, wntholdings, dbtholdings, prfholdings, fndholdings, undholdings):
    return _clean(_sum_cols(shrholdings, cllholdings, putholdings, wntholdings, dbtholdings, prfholdings, fndholdings, undholdings))


def idp_f102_option_holding_share_signal(cllholdings, putholdings, shrholdings):
    return _clean(_safe_div(cllholdings + putholdings, shrholdings + cllholdings + putholdings))


def idp_f102_warrant_holding_share_signal(wntholdings, shrholdings):
    return _clean(_safe_div(wntholdings, shrholdings + wntholdings))


def idp_f102_debt_preferred_holding_share_signal(dbtholdings, prfholdings, shrholdings):
    return _clean(_safe_div(dbtholdings + prfholdings, shrholdings + dbtholdings + prfholdings))


def idp_f102_holder_type_diversity_signal(shrholders, cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders):
    frame = pd.concat([shrholders, cllholders, putholders, wntholders, dbtholders, prfholders, fndholders, undholders], axis=1)
    return _clean(frame.gt(0).sum(axis=1) / frame.notna().sum(axis=1).replace(0, np.nan))


def idp_f102_totalvalue_252d_z_signal(totalvalue):
    return _z(totalvalue, 252)


def idp_f102_percentoftotal_252d_z_signal(percentoftotal):
    return _z(percentoftotal, 252)


def idp_f102_option_value_share_252d_mean_signal(cllvalue, putvalue, totalvalue):
    return _clean(_mean(idp_f102_option_value_share_signal(cllvalue, putvalue, totalvalue), 252))


def idp_f102_short_bias_value_252d_z_signal(putvalue, cllvalue, shrvalue):
    return _z(idp_f102_short_bias_value_signal(putvalue, cllvalue, shrvalue), 252)
