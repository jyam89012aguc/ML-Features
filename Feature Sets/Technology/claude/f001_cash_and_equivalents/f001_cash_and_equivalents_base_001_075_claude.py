import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f001_cash_per_asset(cashneq, assets):
    return cashneq / assets.replace(0, np.nan).abs()


def _f001_cash_per_marketcap(cashneq, marketcap):
    return cashneq / marketcap.replace(0, np.nan).abs()


def _f001_cash_per_share(cashneq, sharesbas):
    return cashneq / sharesbas.replace(0, np.nan).abs()


def _f001_cash_log(cashneq):
    return np.log(cashneq.abs().replace(0, np.nan))


# 21d mean of cashneq level (scaled by closeadj for continuous variation)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_21d_base_v001_signal(cashneq, closeadj):
    result = _mean(cashneq, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of cashneq level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_63d_base_v002_signal(cashneq, closeadj):
    result = _mean(cashneq, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of cashneq level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_126d_base_v003_signal(cashneq, closeadj):
    result = _mean(cashneq, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of cashneq level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_252d_base_v004_signal(cashneq, closeadj):
    result = _mean(cashneq, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of cashneq level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashneq_lvl_504d_base_v005_signal(cashneq, closeadj):
    result = _mean(cashneq, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of cashnequsd level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashusd_lvl_21d_base_v006_signal(cashnequsd, closeadj):
    result = _mean(cashnequsd, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of cashnequsd level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashusd_lvl_63d_base_v007_signal(cashnequsd, closeadj):
    result = _mean(cashnequsd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of cashnequsd level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashusd_lvl_252d_base_v008_signal(cashnequsd, closeadj):
    result = _mean(cashnequsd, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of cashnequsd level (scaled by closeadj)
def f001ce_f001_cash_and_equivalents_cashusd_lvl_504d_base_v009_signal(cashnequsd, closeadj):
    result = _mean(cashnequsd, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# raw cashneq scaled by closeadj
def f001ce_f001_cash_and_equivalents_cashneq_raw_base_v010_signal(cashneq, closeadj):
    result = cashneq * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log cashneq scaled by closeadj
def f001ce_f001_cash_and_equivalents_logcash_21d_base_v011_signal(cashneq, closeadj):
    result = _mean(_f001_cash_log(cashneq), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log cashneq scaled by closeadj
def f001ce_f001_cash_and_equivalents_logcash_63d_base_v012_signal(cashneq, closeadj):
    result = _mean(_f001_cash_log(cashneq), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log cashneq scaled by closeadj
def f001ce_f001_cash_and_equivalents_logcash_252d_base_v013_signal(cashneq, closeadj):
    result = _mean(_f001_cash_log(cashneq), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log cashneq scaled by closeadj
def f001ce_f001_cash_and_equivalents_logcash_504d_base_v014_signal(cashneq, closeadj):
    result = _mean(_f001_cash_log(cashneq), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# log cashnequsd 252d
def f001ce_f001_cash_and_equivalents_logcashusd_252d_base_v015_signal(cashnequsd, closeadj):
    result = _mean(_f001_cash_log(cashnequsd), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per asset 21d
def f001ce_f001_cash_and_equivalents_cashtoasset_21d_base_v016_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per asset 63d
def f001ce_f001_cash_and_equivalents_cashtoasset_63d_base_v017_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per asset 126d
def f001ce_f001_cash_and_equivalents_cashtoasset_126d_base_v018_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per asset 252d
def f001ce_f001_cash_and_equivalents_cashtoasset_252d_base_v019_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per asset 504d
def f001ce_f001_cash_and_equivalents_cashtoasset_504d_base_v020_signal(cashneq, assets, closeadj):
    base = _f001_cash_per_asset(cashneq, assets)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per assetsc (current assets) 21d
def f001ce_f001_cash_and_equivalents_cashtoassetsc_21d_base_v021_signal(cashneq, assetsc, closeadj):
    base = cashneq / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per assetsc 63d
def f001ce_f001_cash_and_equivalents_cashtoassetsc_63d_base_v022_signal(cashneq, assetsc, closeadj):
    base = cashneq / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per assetsc 252d
def f001ce_f001_cash_and_equivalents_cashtoassetsc_252d_base_v023_signal(cashneq, assetsc, closeadj):
    base = cashneq / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per marketcap 21d
def f001ce_f001_cash_and_equivalents_cashtomcap_21d_base_v024_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per marketcap 63d
def f001ce_f001_cash_and_equivalents_cashtomcap_63d_base_v025_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per marketcap 126d
def f001ce_f001_cash_and_equivalents_cashtomcap_126d_base_v026_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per marketcap 252d
def f001ce_f001_cash_and_equivalents_cashtomcap_252d_base_v027_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per marketcap 504d
def f001ce_f001_cash_and_equivalents_cashtomcap_504d_base_v028_signal(cashneq, marketcap, closeadj):
    base = _f001_cash_per_marketcap(cashneq, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per share 21d
def f001ce_f001_cash_and_equivalents_cashpershare_21d_base_v029_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per share 63d
def f001ce_f001_cash_and_equivalents_cashpershare_63d_base_v030_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per share 252d
def f001ce_f001_cash_and_equivalents_cashpershare_252d_base_v031_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per share 504d
def f001ce_f001_cash_and_equivalents_cashpershare_504d_base_v032_signal(cashneq, sharesbas, closeadj):
    base = _f001_cash_per_share(cashneq, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per diluted share 252d
def f001ce_f001_cash_and_equivalents_cashperdilshare_252d_base_v033_signal(cashneq, shareswadil, closeadj):
    base = cashneq / shareswadil.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to equity 21d
def f001ce_f001_cash_and_equivalents_cashtoequity_21d_base_v034_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to equity 63d
def f001ce_f001_cash_and_equivalents_cashtoequity_63d_base_v035_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to equity 252d
def f001ce_f001_cash_and_equivalents_cashtoequity_252d_base_v036_signal(cashneq, equity, closeadj):
    base = cashneq / equity.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to liabilities 21d
def f001ce_f001_cash_and_equivalents_cashtoliab_21d_base_v037_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to liabilities 63d
def f001ce_f001_cash_and_equivalents_cashtoliab_63d_base_v038_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to liabilities 252d
def f001ce_f001_cash_and_equivalents_cashtoliab_252d_base_v039_signal(cashneq, liabilities, closeadj):
    base = cashneq / liabilities.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to current liabilities 21d
def f001ce_f001_cash_and_equivalents_cashtocurliab_21d_base_v040_signal(cashneq, liabilitiesc, closeadj):
    base = cashneq / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to current liabilities 63d
def f001ce_f001_cash_and_equivalents_cashtocurliab_63d_base_v041_signal(cashneq, liabilitiesc, closeadj):
    base = cashneq / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to current liabilities 252d
def f001ce_f001_cash_and_equivalents_cashtocurliab_252d_base_v042_signal(cashneq, liabilitiesc, closeadj):
    base = cashneq / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to revenue 21d
def f001ce_f001_cash_and_equivalents_cashtorev_21d_base_v043_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to revenue 63d
def f001ce_f001_cash_and_equivalents_cashtorev_63d_base_v044_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to revenue 252d
def f001ce_f001_cash_and_equivalents_cashtorev_252d_base_v045_signal(cashneq, revenue, closeadj):
    base = cashneq / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to opex 21d
def f001ce_f001_cash_and_equivalents_cashtoopex_21d_base_v046_signal(cashneq, opex, closeadj):
    base = cashneq / opex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to opex 63d
def f001ce_f001_cash_and_equivalents_cashtoopex_63d_base_v047_signal(cashneq, opex, closeadj):
    base = cashneq / opex.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to opex 252d
def f001ce_f001_cash_and_equivalents_cashtoopex_252d_base_v048_signal(cashneq, opex, closeadj):
    base = cashneq / opex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to R&D 21d (tech-specific reinvestment coverage)
def f001ce_f001_cash_and_equivalents_cashtornd_21d_base_v049_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to R&D 63d
def f001ce_f001_cash_and_equivalents_cashtornd_63d_base_v050_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to R&D 252d
def f001ce_f001_cash_and_equivalents_cashtornd_252d_base_v051_signal(cashneq, rnd, closeadj):
    base = cashneq / rnd.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to capex 21d
def f001ce_f001_cash_and_equivalents_cashtocapex_21d_base_v052_signal(cashneq, capex, closeadj):
    base = cashneq / capex.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to capex 252d
def f001ce_f001_cash_and_equivalents_cashtocapex_252d_base_v053_signal(cashneq, capex, closeadj):
    base = cashneq / capex.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to SBC 21d (cash to stock comp burden)
def f001ce_f001_cash_and_equivalents_cashtosbc_21d_base_v054_signal(cashneq, sbcomp, closeadj):
    base = cashneq / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to SBC 252d
def f001ce_f001_cash_and_equivalents_cashtosbc_252d_base_v055_signal(cashneq, sbcomp, closeadj):
    base = cashneq / sbcomp.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share of working capital from cash 21d
def f001ce_f001_cash_and_equivalents_cashtowc_21d_base_v056_signal(cashneq, workingcapital, closeadj):
    base = cashneq / workingcapital.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# share of working capital from cash 252d
def f001ce_f001_cash_and_equivalents_cashtowc_252d_base_v057_signal(cashneq, workingcapital, closeadj):
    base = cashneq / workingcapital.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to total debt 21d
def f001ce_f001_cash_and_equivalents_cashtodebt_21d_base_v058_signal(cashneq, debt, closeadj):
    base = cashneq / debt.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to total debt 63d
def f001ce_f001_cash_and_equivalents_cashtodebt_63d_base_v059_signal(cashneq, debt, closeadj):
    base = cashneq / debt.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq to total debt 252d
def f001ce_f001_cash_and_equivalents_cashtodebt_252d_base_v060_signal(cashneq, debt, closeadj):
    base = cashneq / debt.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq minus current debt scaled (immediate buffer)
def f001ce_f001_cash_and_equivalents_cashminusdebtc_21d_base_v061_signal(cashneq, debtc, closeadj):
    base = cashneq - debtc
    result = _mean(base, 21) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq minus current debt scaled 63d
def f001ce_f001_cash_and_equivalents_cashminusdebtc_63d_base_v062_signal(cashneq, debtc, closeadj):
    base = cashneq - debtc
    result = _mean(base, 63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq minus current debt scaled 252d
def f001ce_f001_cash_and_equivalents_cashminusdebtc_252d_base_v063_signal(cashneq, debtc, closeadj):
    base = cashneq - debtc
    result = _mean(base, 252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq plus short investments level 21d
def f001ce_f001_cash_and_equivalents_cashplusinv_21d_base_v064_signal(cashneq, investmentsc, closeadj):
    base = cashneq + investmentsc.fillna(0)
    result = _mean(base, 21) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq plus short investments 63d
def f001ce_f001_cash_and_equivalents_cashplusinv_63d_base_v065_signal(cashneq, investmentsc, closeadj):
    base = cashneq + investmentsc.fillna(0)
    result = _mean(base, 63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq plus short investments 252d
def f001ce_f001_cash_and_equivalents_cashplusinv_252d_base_v066_signal(cashneq, investmentsc, closeadj):
    base = cashneq + investmentsc.fillna(0)
    result = _mean(base, 252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# (cashneq + investments) per market cap 21d
def f001ce_f001_cash_and_equivalents_cashplusinvtomcap_21d_base_v067_signal(cashneq, investmentsc, marketcap, closeadj):
    base = (cashneq + investmentsc.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# (cashneq + investments) per market cap 252d
def f001ce_f001_cash_and_equivalents_cashplusinvtomcap_252d_base_v068_signal(cashneq, investmentsc, marketcap, closeadj):
    base = (cashneq + investmentsc.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per ev (cash share of EV) 21d
def f001ce_f001_cash_and_equivalents_cashtoev_21d_base_v069_signal(cashneq, ev, closeadj):
    base = cashneq / ev.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq per ev 252d
def f001ce_f001_cash_and_equivalents_cashtoev_252d_base_v070_signal(cashneq, ev, closeadj):
    base = cashneq / ev.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq smoothed expanding mean × closeadj
def f001ce_f001_cash_and_equivalents_cashneq_expmean_base_v071_signal(cashneq, closeadj):
    result = cashneq.expanding(min_periods=21).mean() * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq normalized to its own 252d max
def f001ce_f001_cash_and_equivalents_cashneq_to252max_base_v072_signal(cashneq, closeadj):
    mx = cashneq.rolling(252, min_periods=63).max().abs().replace(0, np.nan)
    result = (cashneq / mx) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq normalized to its 504d max
def f001ce_f001_cash_and_equivalents_cashneq_to504max_base_v073_signal(cashneq, closeadj):
    mx = cashneq.rolling(504, min_periods=126).max().abs().replace(0, np.nan)
    result = (cashneq / mx) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq distance from 252d max scaled
def f001ce_f001_cash_and_equivalents_cashneq_distmax_252d_base_v074_signal(cashneq, closeadj):
    mx = cashneq.rolling(252, min_periods=63).max()
    base = (cashneq - mx) / mx.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# cashneq distance from 252d min scaled
def f001ce_f001_cash_and_equivalents_cashneq_distmin_252d_base_v075_signal(cashneq, closeadj):
    mn = cashneq.rolling(252, min_periods=63).min()
    base = (cashneq - mn) / mn.replace(0, np.nan).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)
