"""Family f103 - Insider transaction code and role signals.

Sharadar tables: SF2
Fields: transactioncode, securityadcode, formtype, isdirector, isofficer,
istenpercentowner, transactionshares, transactionvalue, transactionpricepershare,
sharesownedbeforetransaction, sharesownedfollowingtransaction, priceexercisable,
rownum.

Existing f092-f094 capture generic insider flow, but the raw SF2 categorical
codes carry direction and transaction-type information that should be modeled
explicitly.
"""
import numpy as np
import pandas as pd


PURCHASE_CODES = {"P"}
SALE_CODES = {"S", "F"}
AWARD_CODES = {"A"}
OPTION_EXERCISE_CODES = {"M", "C"}
DISPOSITION_CODES = {"D"}
GIFT_CODES = {"G"}


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _flag(s, values):
    return s.astype("string").str.upper().isin(values).astype(float)


def _text_contains(s, pattern):
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _z(s, w):
    m = _mean(s, w)
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return _clean(_safe_div(s - m, sd))


def _days_between(later, earlier):
    a = pd.to_datetime(later, errors="coerce")
    b = pd.to_datetime(earlier, errors="coerce")
    return _clean((a - b).dt.days.astype(float))


def icr_f103_purchase_trade_flag_signal(transactioncode):
    return _flag(transactioncode, PURCHASE_CODES)


def icr_f103_sale_trade_flag_signal(transactioncode):
    return _flag(transactioncode, SALE_CODES)


def icr_f103_award_trade_flag_signal(transactioncode):
    return _flag(transactioncode, AWARD_CODES)


def icr_f103_option_exercise_flag_signal(transactioncode):
    return _flag(transactioncode, OPTION_EXERCISE_CODES)


def icr_f103_gift_trade_flag_signal(transactioncode):
    return _flag(transactioncode, GIFT_CODES)


def icr_f103_disposition_trade_flag_signal(transactioncode):
    return _flag(transactioncode, DISPOSITION_CODES)


def icr_f103_open_market_net_flag_signal(transactioncode):
    return _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)


def icr_f103_open_market_net_value_signal(transactioncode, transactionvalue):
    return _clean(icr_f103_open_market_net_flag_signal(transactioncode) * transactionvalue.abs())


def icr_f103_open_market_net_shares_signal(transactioncode, transactionshares):
    return _clean(icr_f103_open_market_net_flag_signal(transactioncode) * transactionshares.abs())


def icr_f103_purchase_value_63d_sum_signal(transactioncode, transactionvalue):
    return _clean(_sum(_flag(transactioncode, PURCHASE_CODES) * transactionvalue.abs(), 63))


def icr_f103_sale_value_63d_sum_signal(transactioncode, transactionvalue):
    return _clean(_sum(_flag(transactioncode, SALE_CODES) * transactionvalue.abs(), 63))


def icr_f103_net_value_63d_sum_signal(transactioncode, transactionvalue):
    return _clean(_sum(icr_f103_open_market_net_value_signal(transactioncode, transactionvalue), 63))


def icr_f103_net_value_252d_z_signal(transactioncode, transactionvalue):
    return _z(icr_f103_open_market_net_value_signal(transactioncode, transactionvalue), 252)


def icr_f103_purchase_count_252d_signal(transactioncode):
    return _clean(_sum(_flag(transactioncode, PURCHASE_CODES), 252))


def icr_f103_sale_count_252d_signal(transactioncode):
    return _clean(_sum(_flag(transactioncode, SALE_CODES), 252))


def icr_f103_buy_sell_count_ratio_252d_signal(transactioncode):
    buys = _sum(_flag(transactioncode, PURCHASE_CODES), 252)
    sells = _sum(_flag(transactioncode, SALE_CODES), 252)
    return _clean(_safe_div(buys, sells))


def icr_f103_director_purchase_value_signal(transactioncode, isdirector, transactionvalue):
    return _clean(_flag(transactioncode, PURCHASE_CODES) * _text_contains(isdirector, "Y|TRUE|1") * transactionvalue.abs())


def icr_f103_officer_purchase_value_signal(transactioncode, isofficer, transactionvalue):
    return _clean(_flag(transactioncode, PURCHASE_CODES) * _text_contains(isofficer, "Y|TRUE|1") * transactionvalue.abs())


def icr_f103_ten_percent_owner_sale_value_signal(transactioncode, istenpercentowner, transactionvalue):
    return _clean(_flag(transactioncode, SALE_CODES) * _text_contains(istenpercentowner, "Y|TRUE|1") * transactionvalue.abs())


def icr_f103_role_weighted_net_value_signal(transactioncode, isdirector, isofficer, istenpercentowner, transactionvalue):
    role_weight = 1.0 + _text_contains(isdirector, "Y|TRUE|1") + _text_contains(isofficer, "Y|TRUE|1") + _text_contains(istenpercentowner, "Y|TRUE|1")
    return _clean(icr_f103_open_market_net_flag_signal(transactioncode) * transactionvalue.abs() * role_weight)


def icr_f103_derivative_security_flag_signal(securityadcode):
    return _text_contains(securityadcode, "D")


def icr_f103_non_derivative_security_flag_signal(securityadcode):
    return _text_contains(securityadcode, "^N|ND")


def icr_f103_derivative_net_value_signal(transactioncode, securityadcode, transactionvalue):
    return _clean(icr_f103_open_market_net_flag_signal(transactioncode) * icr_f103_derivative_security_flag_signal(securityadcode) * transactionvalue.abs())


def icr_f103_exercise_spread_signal(transactionpricepershare, priceexercisable):
    return _clean(transactionpricepershare - priceexercisable)


def icr_f103_exercise_moneyness_signal(transactionpricepershare, priceexercisable):
    return _clean(_safe_div(transactionpricepershare, priceexercisable) - 1.0)


def icr_f103_post_trade_ownership_change_signal(sharesownedbeforetransaction, sharesownedfollowingtransaction):
    return _clean(sharesownedfollowingtransaction - sharesownedbeforetransaction)


def icr_f103_post_trade_ownership_change_pct_signal(sharesownedbeforetransaction, sharesownedfollowingtransaction):
    return _clean(_safe_div(sharesownedfollowingtransaction - sharesownedbeforetransaction, sharesownedbeforetransaction.abs()))


def icr_f103_restatement_form_flag_signal(formtype):
    return _text_contains(formtype, "RESTATED")


def icr_f103_late_row_sequence_signal(rownum):
    return _clean(rownum)


def icr_f103_filing_lag_days_signal(filingdate, transactiondate):
    return _days_between(filingdate, transactiondate)


def icr_f103_days_until_exercisable_signal(transactiondate, dateexercisable):
    return _days_between(dateexercisable, transactiondate)


def icr_f103_days_until_expiration_signal(transactiondate, expirationdate):
    return _days_between(expirationdate, transactiondate)


def icr_f103_option_term_after_exercisable_signal(dateexercisable, expirationdate):
    return _days_between(expirationdate, dateexercisable)
