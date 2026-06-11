
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

PURCHASE_CODES = {"P"}
SALE_CODES = {"S", "F"}
AWARD_CODES = {"A"}
OPTION_EXERCISE_CODES = {"M", "C"}
DISPOSITION_CODES = {"D"}
GIFT_CODES = {"G"}

def _flag(s, values):
    return s.astype("string").str.upper().isin(values).astype(float)

def _text_contains(s, pattern):
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)

def _sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _days_between(later, earlier):
    a = pd.to_datetime(later, errors="coerce")
    b = pd.to_datetime(earlier, errors="coerce")
    result = (a - b).dt.days.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)

# v001: purchase trade flag
def gm_f105_biotech_f105_purchase_trade_flag_v001_signal(transactioncode):
    result = _flag(transactioncode, PURCHASE_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v002: sale trade flag
def gm_f105_biotech_f105_sale_trade_flag_v002_signal(transactioncode):
    result = _flag(transactioncode, SALE_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v003: award trade flag
def gm_f105_biotech_f105_award_trade_flag_v003_signal(transactioncode):
    result = _flag(transactioncode, AWARD_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v004: option exercise flag
def gm_f105_biotech_f105_option_exercise_flag_v004_signal(transactioncode):
    result = _flag(transactioncode, OPTION_EXERCISE_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v005: gift trade flag
def gm_f105_biotech_f105_gift_trade_flag_v005_signal(transactioncode):
    result = _flag(transactioncode, GIFT_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v006: disposition trade flag
def gm_f105_biotech_f105_disposition_trade_flag_v006_signal(transactioncode):
    result = _flag(transactioncode, DISPOSITION_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v007: open market net flag
def gm_f105_biotech_f105_open_market_net_flag_v007_signal(transactioncode):
    result = _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)
    return result.replace([np.inf, -np.inf], np.nan)

# v008: open market net value
def gm_f105_biotech_f105_open_market_net_value_v008_signal(transactioncode, transactionvalue):
    net_flag = _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)
    result = net_flag * transactionvalue.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v009: open market net shares
def gm_f105_biotech_f105_open_market_net_shares_v009_signal(transactioncode, transactionshares):
    net_flag = _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)
    result = net_flag * transactionshares.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v010: purchase value 63d sum
def gm_f105_biotech_f105_purchase_value_63d_sum_v010_signal(transactioncode, transactionvalue):
    val = _flag(transactioncode, PURCHASE_CODES) * transactionvalue.abs()
    result = _sum(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# v011: sale value 63d sum
def gm_f105_biotech_f105_sale_value_63d_sum_v011_signal(transactioncode, transactionvalue):
    val = _flag(transactioncode, SALE_CODES) * transactionvalue.abs()
    result = _sum(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# v012: net value 63d sum
def gm_f105_biotech_f105_net_value_63d_sum_v012_signal(transactioncode, transactionvalue):
    net_val = (_flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)) * transactionvalue.abs()
    result = _sum(net_val, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# v013: net value 252d z-score
def gm_f105_biotech_f105_net_value_252d_z_v013_signal(transactioncode, transactionvalue):
    net_val = (_flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)) * transactionvalue.abs()
    result = _z(net_val, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v014: purchase count 252d
def gm_f105_biotech_f105_purchase_count_252d_v014_signal(transactioncode):
    result = _sum(_flag(transactioncode, PURCHASE_CODES), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v015: sale count 252d
def gm_f105_biotech_f105_sale_count_252d_v015_signal(transactioncode):
    result = _sum(_flag(transactioncode, SALE_CODES), 252)
    return result.replace([np.inf, -np.inf], np.nan)

# v016: buy sell count ratio 252d
def gm_f105_biotech_f105_buy_sell_count_ratio_252d_v016_signal(transactioncode):
    buys = _sum(_flag(transactioncode, PURCHASE_CODES), 252)
    sells = _sum(_flag(transactioncode, SALE_CODES), 252)
    result = _safe_div(buys, sells)
    return result.replace([np.inf, -np.inf], np.nan)

# v017: director purchase value
def gm_f105_biotech_f105_director_purchase_value_v017_signal(transactioncode, isdirector, transactionvalue):
    result = _flag(transactioncode, PURCHASE_CODES) * _text_contains(isdirector, "Y|TRUE|1") * transactionvalue.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v018: officer purchase value
def gm_f105_biotech_f105_officer_purchase_value_v018_signal(transactioncode, isofficer, transactionvalue):
    result = _flag(transactioncode, PURCHASE_CODES) * _text_contains(isofficer, "Y|TRUE|1") * transactionvalue.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v019: ten percent owner sale value
def gm_f105_biotech_f105_ten_percent_owner_sale_value_v019_signal(transactioncode, istenpercentowner, transactionvalue):
    result = _flag(transactioncode, SALE_CODES) * _text_contains(istenpercentowner, "Y|TRUE|1") * transactionvalue.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v020: role weighted net value
def gm_f105_biotech_f105_role_weighted_net_value_v020_signal(transactioncode, isdirector, isofficer, istenpercentowner, transactionvalue):
    role_weight = 1.0 + _text_contains(isdirector, "Y|TRUE|1") + _text_contains(isofficer, "Y|TRUE|1") + _text_contains(istenpercentowner, "Y|TRUE|1")
    net_flag = _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)
    result = net_flag * transactionvalue.abs() * role_weight
    return result.replace([np.inf, -np.inf], np.nan)

# v021: derivative security flag
def gm_f105_biotech_f105_derivative_security_flag_v021_signal(securityadcode):
    result = _text_contains(securityadcode, "D")
    return result.replace([np.inf, -np.inf], np.nan)

# v022: non derivative security flag
def gm_f105_biotech_f105_non_derivative_security_flag_v022_signal(securityadcode):
    result = _text_contains(securityadcode, "^N|ND")
    return result.replace([np.inf, -np.inf], np.nan)

# v023: derivative net value
def gm_f105_biotech_f105_derivative_net_value_v023_signal(transactioncode, securityadcode, transactionvalue):
    net_flag = _flag(transactioncode, PURCHASE_CODES) - _flag(transactioncode, SALE_CODES)
    result = net_flag * _text_contains(securityadcode, "D") * transactionvalue.abs()
    return result.replace([np.inf, -np.inf], np.nan)

# v024: exercise spread
def gm_f105_biotech_f105_exercise_spread_v024_signal(transactionpricepershare, priceexercisable):
    result = transactionpricepershare - priceexercisable
    return result.replace([np.inf, -np.inf], np.nan)

# v025: exercise moneyness
def gm_f105_biotech_f105_exercise_moneyness_v025_signal(transactionpricepershare, priceexercisable):
    result = _safe_div(transactionpricepershare, priceexercisable) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)

# v026: post trade ownership change
def gm_f105_biotech_f105_post_trade_ownership_change_v026_signal(sharesownedbeforetransaction, sharesownedfollowingtransaction):
    result = sharesownedfollowingtransaction - sharesownedbeforetransaction
    return result.replace([np.inf, -np.inf], np.nan)

# v027: post trade ownership change pct
def gm_f105_biotech_f105_post_trade_ownership_change_pct_v027_signal(sharesownedbeforetransaction, sharesownedfollowingtransaction):
    result = _safe_div(sharesownedfollowingtransaction - sharesownedbeforetransaction, sharesownedbeforetransaction.abs())
    return result.replace([np.inf, -np.inf], np.nan)

# v028: restatement form flag
def gm_f105_biotech_f105_restatement_form_flag_v028_signal(formtype):
    result = _text_contains(formtype, "RESTATED")
    return result.replace([np.inf, -np.inf], np.nan)

# v029: late row sequence
def gm_f105_biotech_f105_late_row_sequence_v029_signal(rownum):
    return rownum.replace([np.inf, -np.inf], np.nan)

# v030: filing lag days
def gm_f105_biotech_f105_filing_lag_days_v030_signal(filingdate, transactiondate):
    return _days_between(filingdate, transactiondate)

# v031: days until exercisable
def gm_f105_biotech_f105_days_until_exercisable_v031_signal(transactiondate, dateexercisable):
    return _days_between(dateexercisable, transactiondate)

# v032: days until expiration
def gm_f105_biotech_f105_days_until_expiration_v032_signal(transactiondate, expirationdate):
    return _days_between(expirationdate, transactiondate)

# v033: option term after exercisable
def gm_f105_biotech_f105_option_term_after_exercisable_v033_signal(dateexercisable, expirationdate):
    return _days_between(expirationdate, dateexercisable)
