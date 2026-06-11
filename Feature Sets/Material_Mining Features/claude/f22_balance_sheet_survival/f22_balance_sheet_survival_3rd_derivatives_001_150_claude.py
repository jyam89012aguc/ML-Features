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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    # 1st math derivative: discrete first difference over window w
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    # 2nd math derivative: discrete second difference over window w
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)


def _rng(s, w):
    return _rmax(s, w) - _rmin(s, w)


# ===== folder domain primitives: BALANCE-SHEET LEVERAGE & LIQUIDITY STRUCTURE =====
# Debt/currentratio-centric leverage & liquidity STRUCTURE base ratios; these derivative
# files take the math slope/jerk of each base and deliberately avoid f21's liabilities
# based Altman-Z distress composites, cash/liabilities and cash/assets going-concern flags.
def _abs_floor(s):
    return s.abs().replace(0, np.nan)


def _debt_equity(debt, equity):
    return (debt / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _debt_assets(debt, assets):
    return debt / assets.replace(0, np.nan)


def _net_debt_equity(debt, cashneq, equity):
    return ((debt - cashneq) / _abs_floor(equity)).clip(lower=-50.0, upper=50.0)


def _net_gearing(debt, cashneq, equity):
    nd = debt - cashneq
    cap = (nd + equity).replace(0, np.nan)
    return (nd / cap).clip(lower=-5.0, upper=5.0)


def _debt_capital(debt, equity, cashneq):
    cap = (debt + equity + cashneq).replace(0, np.nan)
    return (debt / cap).clip(lower=-5.0, upper=5.0)


def _cash_debt(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def _debt_wc(debt, workingcapital):
    return (debt / _abs_floor(workingcapital)).clip(lower=-50.0, upper=50.0)


def _wc_debt(workingcapital, debt):
    return (workingcapital / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)


def _quick_ratio(currentratio, cashneq, liabilities):
    cl = (cashneq / liabilities.replace(0, np.nan)).clip(lower=0.0, upper=10.0)
    return (0.5 * currentratio + cl).clip(lower=0.0, upper=20.0)


def _liq_buffer_debt(cashneq, workingcapital, debt):
    return ((cashneq + workingcapital) / debt.replace(0, np.nan)).clip(lower=-50.0, upper=50.0)


def _debt_currcover(debt, assets, currentratio):
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=2.0)
    return da / (currentratio.clip(lower=0.05))


def _maturity_proxy(currentratio, debt, assets):
    # liquidity-rich / debt-light structure score dominated by the current-ratio term
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=1.0)
    return currentratio.clip(lower=0.05) * (1.0 - da)


def _dbt_quick(debt, assets, currentratio, cashneq, liabilities):
    q = _quick_ratio(currentratio, cashneq, liabilities).clip(lower=0.05)
    da = _debt_assets(debt, assets).clip(lower=0.0, upper=2.0)
    return da / q


# jerk (2nd deriv, 21d) of dbteq_lvl
def f22bs_f22_balance_sheet_survival_dbteq_lvl_21d_jerk_v001_signal(debt, equity):
    feat = _debt_equity(debt, equity)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbteq_z252
def f22bs_f22_balance_sheet_survival_dbteq_z252_63d_jerk_v002_signal(debt, equity):
    feat = _z(_debt_equity(debt, equity), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbteq_z126
def f22bs_f22_balance_sheet_survival_dbteq_z126_63d_jerk_v003_signal(debt, equity):
    feat = _z(_debt_equity(debt, equity), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbteq_ema63
def f22bs_f22_balance_sheet_survival_dbteq_ema63_21d_jerk_v004_signal(debt, equity):
    feat = _debt_equity(debt, equity).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbteq_smz63
def f22bs_f22_balance_sheet_survival_dbteq_smz63_21d_jerk_v005_signal(debt, equity):
    r = _debt_equity(debt, equity)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbteq_dsp126
def f22bs_f22_balance_sheet_survival_dbteq_dsp126_63d_jerk_v006_signal(debt, equity):
    feat = _std(_debt_equity(debt, equity), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtassets_lvl
def f22bs_f22_balance_sheet_survival_dbtassets_lvl_21d_jerk_v007_signal(debt, assets):
    feat = _debt_assets(debt, assets)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtassets_z252
def f22bs_f22_balance_sheet_survival_dbtassets_z252_63d_jerk_v008_signal(debt, assets):
    feat = _z(_debt_assets(debt, assets), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtassets_z126
def f22bs_f22_balance_sheet_survival_dbtassets_z126_63d_jerk_v009_signal(debt, assets):
    feat = _z(_debt_assets(debt, assets), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtassets_ema63
def f22bs_f22_balance_sheet_survival_dbtassets_ema63_21d_jerk_v010_signal(debt, assets):
    feat = _debt_assets(debt, assets).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtassets_smz63
def f22bs_f22_balance_sheet_survival_dbtassets_smz63_21d_jerk_v011_signal(debt, assets):
    r = _debt_assets(debt, assets)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtusdassets_lvl
def f22bs_f22_balance_sheet_survival_dbtusdassets_lvl_21d_jerk_v012_signal(debtusd, assets):
    feat = debtusd / assets.replace(0, np.nan)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtusdassets_z252
def f22bs_f22_balance_sheet_survival_dbtusdassets_z252_63d_jerk_v013_signal(debtusd, assets):
    feat = _z(debtusd / assets.replace(0, np.nan), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtwc_z126
def f22bs_f22_balance_sheet_survival_dbtwc_z126_63d_jerk_v014_signal(debt, workingcapital):
    feat = _z(_debt_wc(debt, workingcapital), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtwc_rng252
def f22bs_f22_balance_sheet_survival_dbtwc_rng252_63d_jerk_v015_signal(debt, workingcapital):
    feat = _rng(_debt_wc(debt, workingcapital), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndeq_lvl
def f22bs_f22_balance_sheet_survival_ndeq_lvl_21d_jerk_v016_signal(debt, cashneq, equity):
    feat = _net_debt_equity(debt, cashneq, equity)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of ndeq_z252
def f22bs_f22_balance_sheet_survival_ndeq_z252_63d_jerk_v017_signal(debt, cashneq, equity):
    feat = _z(_net_debt_equity(debt, cashneq, equity), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of ndeq_z126
def f22bs_f22_balance_sheet_survival_ndeq_z126_63d_jerk_v018_signal(debt, cashneq, equity):
    feat = _z(_net_debt_equity(debt, cashneq, equity), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndeq_ema63
def f22bs_f22_balance_sheet_survival_ndeq_ema63_21d_jerk_v019_signal(debt, cashneq, equity):
    feat = _net_debt_equity(debt, cashneq, equity).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndeq_smz63
def f22bs_f22_balance_sheet_survival_ndeq_smz63_21d_jerk_v020_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of netgear_lvl
def f22bs_f22_balance_sheet_survival_netgear_lvl_21d_jerk_v021_signal(debt, cashneq, equity):
    feat = _net_gearing(debt, cashneq, equity)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of netgear_z252
def f22bs_f22_balance_sheet_survival_netgear_z252_63d_jerk_v022_signal(debt, cashneq, equity):
    feat = _z(_net_gearing(debt, cashneq, equity), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of netgear_ema63
def f22bs_f22_balance_sheet_survival_netgear_ema63_21d_jerk_v023_signal(debt, cashneq, equity):
    feat = _net_gearing(debt, cashneq, equity).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtquick_lvl
def f22bs_f22_balance_sheet_survival_dbtquick_lvl_21d_jerk_v024_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _dbt_quick(debt, assets, currentratio, cashneq, liabilities)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtquick_z252
def f22bs_f22_balance_sheet_survival_dbtquick_z252_63d_jerk_v025_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _z(_dbt_quick(debt, assets, currentratio, cashneq, liabilities), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtquick_smz63
def f22bs_f22_balance_sheet_survival_dbtquick_smz63_21d_jerk_v026_signal(debt, assets, currentratio, cashneq, liabilities):
    r = _dbt_quick(debt, assets, currentratio, cashneq, liabilities)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtcap_lvl
def f22bs_f22_balance_sheet_survival_dbtcap_lvl_21d_jerk_v027_signal(debt, equity, cashneq):
    feat = _debt_capital(debt, equity, cashneq)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtcap_z252
def f22bs_f22_balance_sheet_survival_dbtcap_z252_63d_jerk_v028_signal(debt, equity, cashneq):
    feat = _z(_debt_capital(debt, equity, cashneq), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtcap_ema63
def f22bs_f22_balance_sheet_survival_dbtcap_ema63_21d_jerk_v029_signal(debt, equity, cashneq):
    feat = _debt_capital(debt, equity, cashneq).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of cashdebt_lvl
def f22bs_f22_balance_sheet_survival_cashdebt_lvl_21d_jerk_v030_signal(cashneq, debt):
    feat = _cash_debt(cashneq, debt)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of cashdebt_z252
def f22bs_f22_balance_sheet_survival_cashdebt_z252_63d_jerk_v031_signal(cashneq, debt):
    feat = _z(_cash_debt(cashneq, debt), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of cashdebt_z126
def f22bs_f22_balance_sheet_survival_cashdebt_z126_63d_jerk_v032_signal(cashneq, debt):
    feat = _z(_cash_debt(cashneq, debt), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of cashdebt_ema63
def f22bs_f22_balance_sheet_survival_cashdebt_ema63_21d_jerk_v033_signal(cashneq, debt):
    feat = _cash_debt(cashneq, debt).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of cashdebt_smz63
def f22bs_f22_balance_sheet_survival_cashdebt_smz63_21d_jerk_v034_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtwc_lvl
def f22bs_f22_balance_sheet_survival_dbtwc_lvl_21d_jerk_v035_signal(debt, workingcapital):
    feat = _debt_wc(debt, workingcapital)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtwc_z252
def f22bs_f22_balance_sheet_survival_dbtwc_z252_63d_jerk_v036_signal(debt, workingcapital):
    feat = _z(_debt_wc(debt, workingcapital), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtwc_ema63
def f22bs_f22_balance_sheet_survival_dbtwc_ema63_21d_jerk_v037_signal(debt, workingcapital):
    feat = _debt_wc(debt, workingcapital).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtgrow
def f22bs_f22_balance_sheet_survival_dbtgrow_21d_jerk_v038_signal(debt):
    feat = np.log(debt.replace(0, np.nan) / debt.shift(63).replace(0, np.nan))
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtdd252
def f22bs_f22_balance_sheet_survival_dbtdd252_63d_jerk_v039_signal(debt):
    peak = _rmax(debt, 252)
    feat = debt / peak.replace(0, np.nan) - 1.0
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of wcdebt_lvl
def f22bs_f22_balance_sheet_survival_wcdebt_lvl_21d_jerk_v040_signal(workingcapital, debt):
    feat = _wc_debt(workingcapital, debt)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of liqbuf_lvl
def f22bs_f22_balance_sheet_survival_liqbuf_lvl_21d_jerk_v041_signal(cashneq, workingcapital, debt):
    feat = _liq_buffer_debt(cashneq, workingcapital, debt)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of liqbuf_z252
def f22bs_f22_balance_sheet_survival_liqbuf_z252_63d_jerk_v042_signal(cashneq, workingcapital, debt):
    feat = _z(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of liqbuf_ema63
def f22bs_f22_balance_sheet_survival_liqbuf_ema63_21d_jerk_v043_signal(cashneq, workingcapital, debt):
    feat = _liq_buffer_debt(cashneq, workingcapital, debt).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of liqbuf_smz63
def f22bs_f22_balance_sheet_survival_liqbuf_smz63_21d_jerk_v044_signal(cashneq, workingcapital, debt):
    r = _liq_buffer_debt(cashneq, workingcapital, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of curratio_lvl
def f22bs_f22_balance_sheet_survival_curratio_lvl_21d_jerk_v045_signal(currentratio):
    feat = currentratio
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of curratio_z252
def f22bs_f22_balance_sheet_survival_curratio_z252_63d_jerk_v046_signal(currentratio):
    feat = _z(currentratio, 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of curratio_z126
def f22bs_f22_balance_sheet_survival_curratio_z126_63d_jerk_v047_signal(currentratio):
    feat = _z(currentratio, 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of curratio_ema63
def f22bs_f22_balance_sheet_survival_curratio_ema63_21d_jerk_v048_signal(currentratio):
    feat = currentratio.ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of curratio_smz63
def f22bs_f22_balance_sheet_survival_curratio_smz63_21d_jerk_v049_signal(currentratio):
    feat = currentratio - currentratio.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of quick_lvl
def f22bs_f22_balance_sheet_survival_quick_lvl_21d_jerk_v050_signal(currentratio, cashneq, liabilities):
    feat = _quick_ratio(currentratio, cashneq, liabilities)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of quick_z252
def f22bs_f22_balance_sheet_survival_quick_z252_63d_jerk_v051_signal(currentratio, cashneq, liabilities):
    feat = _z(_quick_ratio(currentratio, cashneq, liabilities), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of quick_ema63
def f22bs_f22_balance_sheet_survival_quick_ema63_21d_jerk_v052_signal(currentratio, cashneq, liabilities):
    feat = _quick_ratio(currentratio, cashneq, liabilities).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndassets_lvl
def f22bs_f22_balance_sheet_survival_ndassets_lvl_21d_jerk_v053_signal(debt, cashneq, assets):
    feat = (debt - cashneq) / assets.replace(0, np.nan)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of ndassets_z252
def f22bs_f22_balance_sheet_survival_ndassets_z252_63d_jerk_v054_signal(debt, cashneq, assets):
    feat = _z((debt - cashneq) / assets.replace(0, np.nan), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndassets_ema63
def f22bs_f22_balance_sheet_survival_ndassets_ema63_21d_jerk_v055_signal(debt, cashneq, assets):
    feat = ((debt - cashneq) / assets.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of ndassets_smz63
def f22bs_f22_balance_sheet_survival_ndassets_smz63_21d_jerk_v056_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtcurr_lvl
def f22bs_f22_balance_sheet_survival_dbtcurr_lvl_21d_jerk_v057_signal(debt, assets, currentratio):
    feat = _debt_currcover(debt, assets, currentratio)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtcurr_z252
def f22bs_f22_balance_sheet_survival_dbtcurr_z252_63d_jerk_v058_signal(debt, assets, currentratio):
    feat = _z(_debt_currcover(debt, assets, currentratio), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtcurr_ema63
def f22bs_f22_balance_sheet_survival_dbtcurr_ema63_21d_jerk_v059_signal(debt, assets, currentratio):
    feat = _debt_currcover(debt, assets, currentratio).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of matpress_lvl
def f22bs_f22_balance_sheet_survival_matpress_lvl_21d_jerk_v060_signal(currentratio, debt, assets):
    feat = _maturity_proxy(currentratio, debt, assets)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of matpress_z252
def f22bs_f22_balance_sheet_survival_matpress_z252_63d_jerk_v061_signal(currentratio, debt, assets):
    feat = _z(_maturity_proxy(currentratio, debt, assets), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of matpress_smz63
def f22bs_f22_balance_sheet_survival_matpress_smz63_21d_jerk_v062_signal(currentratio, debt, assets):
    r = _maturity_proxy(currentratio, debt, assets)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of matpress_dsp126
def f22bs_f22_balance_sheet_survival_matpress_dsp126_63d_jerk_v063_signal(currentratio, debt, assets):
    feat = _std(_maturity_proxy(currentratio, debt, assets), 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtlevel_z252
def f22bs_f22_balance_sheet_survival_dbtlevel_z252_63d_jerk_v064_signal(debt):
    feat = _z(debt, 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtlevel_z126
def f22bs_f22_balance_sheet_survival_dbtlevel_z126_63d_jerk_v065_signal(debt):
    feat = _z(debt, 126)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of dbtgrowh
def f22bs_f22_balance_sheet_survival_dbtgrowh_63d_jerk_v066_signal(debt):
    feat = np.log(debt.replace(0, np.nan) / debt.shift(126).replace(0, np.nan))
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of wcdebt_rng252
def f22bs_f22_balance_sheet_survival_wcdebt_rng252_63d_jerk_v067_signal(workingcapital, debt):
    feat = _rng(_wc_debt(workingcapital, debt), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of wcdebt_smz63
def f22bs_f22_balance_sheet_survival_wcdebt_smz63_21d_jerk_v068_signal(workingcapital, debt):
    r = _wc_debt(workingcapital, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtcap_smz63
def f22bs_f22_balance_sheet_survival_dbtcap_smz63_21d_jerk_v069_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    feat = r - r.rolling(63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of levmix_lvl
def f22bs_f22_balance_sheet_survival_levmix_lvl_21d_jerk_v070_signal(debt, equity, assets):
    feat = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of levmix_z252
def f22bs_f22_balance_sheet_survival_levmix_z252_63d_jerk_v071_signal(debt, equity, assets):
    feat = _z(_debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of levmix_ema63
def f22bs_f22_balance_sheet_survival_levmix_ema63_21d_jerk_v072_signal(debt, equity, assets):
    feat = (_debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets)).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of cashdebt_dd252
def f22bs_f22_balance_sheet_survival_cashdebt_dd252_63d_jerk_v073_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    feat = r - _rmax(r, 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of liqbuf_rng252
def f22bs_f22_balance_sheet_survival_liqbuf_rng252_63d_jerk_v074_signal(cashneq, workingcapital, debt):
    feat = _rng(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of dbtquick_ema63
def f22bs_f22_balance_sheet_survival_dbtquick_ema63_21d_jerk_v075_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _dbt_quick(debt, assets, currentratio, cashneq, liabilities).ewm(span=63, min_periods=21).mean()
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbteq_lvl
def f22bs_f22_balance_sheet_survival_dbteq_lvlmom_63d_jerk_v076_signal(debt, equity):
    feat = _debt_equity(debt, equity)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbteq_z252
def f22bs_f22_balance_sheet_survival_dbteq_z252mom_126d_jerk_v077_signal(debt, equity):
    feat = _z(_debt_equity(debt, equity), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbteq_z126
def f22bs_f22_balance_sheet_survival_dbteq_z126mom_21d_jerk_v078_signal(debt, equity):
    feat = _z(_debt_equity(debt, equity), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbteq_ema63
def f22bs_f22_balance_sheet_survival_dbteq_ema63mom_63d_jerk_v079_signal(debt, equity):
    feat = _debt_equity(debt, equity).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbteq_smz63
def f22bs_f22_balance_sheet_survival_dbteq_smz63mom_63d_jerk_v080_signal(debt, equity):
    r = _debt_equity(debt, equity)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbteq_dsp126
def f22bs_f22_balance_sheet_survival_dbteq_dsp126mom_21d_jerk_v081_signal(debt, equity):
    feat = _std(_debt_equity(debt, equity), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtassets_lvl
def f22bs_f22_balance_sheet_survival_dbtassets_lvlmom_63d_jerk_v082_signal(debt, assets):
    feat = _debt_assets(debt, assets)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtassets_z252
def f22bs_f22_balance_sheet_survival_dbtassets_z252mom_126d_jerk_v083_signal(debt, assets):
    feat = _z(_debt_assets(debt, assets), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbtassets_z126
def f22bs_f22_balance_sheet_survival_dbtassets_z126mom_21d_jerk_v084_signal(debt, assets):
    feat = _z(_debt_assets(debt, assets), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtassets_ema63
def f22bs_f22_balance_sheet_survival_dbtassets_ema63mom_63d_jerk_v085_signal(debt, assets):
    feat = _debt_assets(debt, assets).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtassets_smz63
def f22bs_f22_balance_sheet_survival_dbtassets_smz63mom_63d_jerk_v086_signal(debt, assets):
    r = _debt_assets(debt, assets)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtusdassets_lvl
def f22bs_f22_balance_sheet_survival_dbtusdassets_lvlmom_63d_jerk_v087_signal(debtusd, assets):
    feat = debtusd / assets.replace(0, np.nan)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtusdassets_z252
def f22bs_f22_balance_sheet_survival_dbtusdassets_z252mom_126d_jerk_v088_signal(debtusd, assets):
    feat = _z(debtusd / assets.replace(0, np.nan), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbtwc_z126
def f22bs_f22_balance_sheet_survival_dbtwc_z126mom_21d_jerk_v089_signal(debt, workingcapital):
    feat = _z(_debt_wc(debt, workingcapital), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtwc_rng252
def f22bs_f22_balance_sheet_survival_dbtwc_rng252mom_126d_jerk_v090_signal(debt, workingcapital):
    feat = _rng(_debt_wc(debt, workingcapital), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndeq_lvl
def f22bs_f22_balance_sheet_survival_ndeq_lvlmom_63d_jerk_v091_signal(debt, cashneq, equity):
    feat = _net_debt_equity(debt, cashneq, equity)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of ndeq_z252
def f22bs_f22_balance_sheet_survival_ndeq_z252mom_126d_jerk_v092_signal(debt, cashneq, equity):
    feat = _z(_net_debt_equity(debt, cashneq, equity), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of ndeq_z126
def f22bs_f22_balance_sheet_survival_ndeq_z126mom_21d_jerk_v093_signal(debt, cashneq, equity):
    feat = _z(_net_debt_equity(debt, cashneq, equity), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndeq_ema63
def f22bs_f22_balance_sheet_survival_ndeq_ema63mom_63d_jerk_v094_signal(debt, cashneq, equity):
    feat = _net_debt_equity(debt, cashneq, equity).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndeq_smz63
def f22bs_f22_balance_sheet_survival_ndeq_smz63mom_63d_jerk_v095_signal(debt, cashneq, equity):
    r = _net_debt_equity(debt, cashneq, equity)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of netgear_lvl
def f22bs_f22_balance_sheet_survival_netgear_lvlmom_63d_jerk_v096_signal(debt, cashneq, equity):
    feat = _net_gearing(debt, cashneq, equity)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of netgear_z252
def f22bs_f22_balance_sheet_survival_netgear_z252mom_126d_jerk_v097_signal(debt, cashneq, equity):
    feat = _z(_net_gearing(debt, cashneq, equity), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of netgear_ema63
def f22bs_f22_balance_sheet_survival_netgear_ema63mom_63d_jerk_v098_signal(debt, cashneq, equity):
    feat = _net_gearing(debt, cashneq, equity).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtquick_lvl
def f22bs_f22_balance_sheet_survival_dbtquick_lvlmom_63d_jerk_v099_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _dbt_quick(debt, assets, currentratio, cashneq, liabilities)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtquick_z252
def f22bs_f22_balance_sheet_survival_dbtquick_z252mom_126d_jerk_v100_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _z(_dbt_quick(debt, assets, currentratio, cashneq, liabilities), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtquick_smz63
def f22bs_f22_balance_sheet_survival_dbtquick_smz63mom_63d_jerk_v101_signal(debt, assets, currentratio, cashneq, liabilities):
    r = _dbt_quick(debt, assets, currentratio, cashneq, liabilities)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtcap_lvl
def f22bs_f22_balance_sheet_survival_dbtcap_lvlmom_63d_jerk_v102_signal(debt, equity, cashneq):
    feat = _debt_capital(debt, equity, cashneq)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtcap_z252
def f22bs_f22_balance_sheet_survival_dbtcap_z252mom_126d_jerk_v103_signal(debt, equity, cashneq):
    feat = _z(_debt_capital(debt, equity, cashneq), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtcap_ema63
def f22bs_f22_balance_sheet_survival_dbtcap_ema63mom_63d_jerk_v104_signal(debt, equity, cashneq):
    feat = _debt_capital(debt, equity, cashneq).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of cashdebt_lvl
def f22bs_f22_balance_sheet_survival_cashdebt_lvlmom_63d_jerk_v105_signal(cashneq, debt):
    feat = _cash_debt(cashneq, debt)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of cashdebt_z252
def f22bs_f22_balance_sheet_survival_cashdebt_z252mom_126d_jerk_v106_signal(cashneq, debt):
    feat = _z(_cash_debt(cashneq, debt), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of cashdebt_z126
def f22bs_f22_balance_sheet_survival_cashdebt_z126mom_21d_jerk_v107_signal(cashneq, debt):
    feat = _z(_cash_debt(cashneq, debt), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of cashdebt_ema63
def f22bs_f22_balance_sheet_survival_cashdebt_ema63mom_63d_jerk_v108_signal(cashneq, debt):
    feat = _cash_debt(cashneq, debt).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of cashdebt_smz63
def f22bs_f22_balance_sheet_survival_cashdebt_smz63mom_63d_jerk_v109_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtwc_lvl
def f22bs_f22_balance_sheet_survival_dbtwc_lvlmom_63d_jerk_v110_signal(debt, workingcapital):
    feat = _debt_wc(debt, workingcapital)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtwc_z252
def f22bs_f22_balance_sheet_survival_dbtwc_z252mom_126d_jerk_v111_signal(debt, workingcapital):
    feat = _z(_debt_wc(debt, workingcapital), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtwc_ema63
def f22bs_f22_balance_sheet_survival_dbtwc_ema63mom_63d_jerk_v112_signal(debt, workingcapital):
    feat = _debt_wc(debt, workingcapital).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtgrow
def f22bs_f22_balance_sheet_survival_dbtgrowmom_63d_jerk_v113_signal(debt):
    feat = np.log(debt.replace(0, np.nan) / debt.shift(63).replace(0, np.nan))
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtdd252
def f22bs_f22_balance_sheet_survival_dbtdd252mom_126d_jerk_v114_signal(debt):
    peak = _rmax(debt, 252)
    feat = debt / peak.replace(0, np.nan) - 1.0
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of wcdebt_lvl
def f22bs_f22_balance_sheet_survival_wcdebt_lvlmom_63d_jerk_v115_signal(workingcapital, debt):
    feat = _wc_debt(workingcapital, debt)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of liqbuf_lvl
def f22bs_f22_balance_sheet_survival_liqbuf_lvlmom_63d_jerk_v116_signal(cashneq, workingcapital, debt):
    feat = _liq_buffer_debt(cashneq, workingcapital, debt)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of liqbuf_z252
def f22bs_f22_balance_sheet_survival_liqbuf_z252mom_126d_jerk_v117_signal(cashneq, workingcapital, debt):
    feat = _z(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of liqbuf_ema63
def f22bs_f22_balance_sheet_survival_liqbuf_ema63mom_63d_jerk_v118_signal(cashneq, workingcapital, debt):
    feat = _liq_buffer_debt(cashneq, workingcapital, debt).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of liqbuf_smz63
def f22bs_f22_balance_sheet_survival_liqbuf_smz63mom_63d_jerk_v119_signal(cashneq, workingcapital, debt):
    r = _liq_buffer_debt(cashneq, workingcapital, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of curratio_lvl
def f22bs_f22_balance_sheet_survival_curratio_lvlmom_63d_jerk_v120_signal(currentratio):
    feat = currentratio
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of curratio_z252
def f22bs_f22_balance_sheet_survival_curratio_z252mom_126d_jerk_v121_signal(currentratio):
    feat = _z(currentratio, 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of curratio_z126
def f22bs_f22_balance_sheet_survival_curratio_z126mom_21d_jerk_v122_signal(currentratio):
    feat = _z(currentratio, 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of curratio_ema63
def f22bs_f22_balance_sheet_survival_curratio_ema63mom_63d_jerk_v123_signal(currentratio):
    feat = currentratio.ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of curratio_smz63
def f22bs_f22_balance_sheet_survival_curratio_smz63mom_63d_jerk_v124_signal(currentratio):
    feat = currentratio - currentratio.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of quick_lvl
def f22bs_f22_balance_sheet_survival_quick_lvlmom_63d_jerk_v125_signal(currentratio, cashneq, liabilities):
    feat = _quick_ratio(currentratio, cashneq, liabilities)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of quick_z252
def f22bs_f22_balance_sheet_survival_quick_z252mom_126d_jerk_v126_signal(currentratio, cashneq, liabilities):
    feat = _z(_quick_ratio(currentratio, cashneq, liabilities), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of quick_ema63
def f22bs_f22_balance_sheet_survival_quick_ema63mom_63d_jerk_v127_signal(currentratio, cashneq, liabilities):
    feat = _quick_ratio(currentratio, cashneq, liabilities).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndassets_lvl
def f22bs_f22_balance_sheet_survival_ndassets_lvlmom_63d_jerk_v128_signal(debt, cashneq, assets):
    feat = (debt - cashneq) / assets.replace(0, np.nan)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of ndassets_z252
def f22bs_f22_balance_sheet_survival_ndassets_z252mom_126d_jerk_v129_signal(debt, cashneq, assets):
    feat = _z((debt - cashneq) / assets.replace(0, np.nan), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndassets_ema63
def f22bs_f22_balance_sheet_survival_ndassets_ema63mom_63d_jerk_v130_signal(debt, cashneq, assets):
    feat = ((debt - cashneq) / assets.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of ndassets_smz63
def f22bs_f22_balance_sheet_survival_ndassets_smz63mom_63d_jerk_v131_signal(debt, cashneq, assets):
    r = (debt - cashneq) / assets.replace(0, np.nan)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtcurr_lvl
def f22bs_f22_balance_sheet_survival_dbtcurr_lvlmom_63d_jerk_v132_signal(debt, assets, currentratio):
    feat = _debt_currcover(debt, assets, currentratio)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtcurr_z252
def f22bs_f22_balance_sheet_survival_dbtcurr_z252mom_126d_jerk_v133_signal(debt, assets, currentratio):
    feat = _z(_debt_currcover(debt, assets, currentratio), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtcurr_ema63
def f22bs_f22_balance_sheet_survival_dbtcurr_ema63mom_63d_jerk_v134_signal(debt, assets, currentratio):
    feat = _debt_currcover(debt, assets, currentratio).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of matpress_lvl
def f22bs_f22_balance_sheet_survival_matpress_lvlmom_63d_jerk_v135_signal(currentratio, debt, assets):
    feat = _maturity_proxy(currentratio, debt, assets)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of matpress_z252
def f22bs_f22_balance_sheet_survival_matpress_z252mom_126d_jerk_v136_signal(currentratio, debt, assets):
    feat = _z(_maturity_proxy(currentratio, debt, assets), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of matpress_smz63
def f22bs_f22_balance_sheet_survival_matpress_smz63mom_63d_jerk_v137_signal(currentratio, debt, assets):
    r = _maturity_proxy(currentratio, debt, assets)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of matpress_dsp126
def f22bs_f22_balance_sheet_survival_matpress_dsp126mom_21d_jerk_v138_signal(currentratio, debt, assets):
    feat = _std(_maturity_proxy(currentratio, debt, assets), 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of dbtlevel_z252
def f22bs_f22_balance_sheet_survival_dbtlevel_z252mom_126d_jerk_v139_signal(debt):
    feat = _z(debt, 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbtlevel_z126
def f22bs_f22_balance_sheet_survival_dbtlevel_z126mom_21d_jerk_v140_signal(debt):
    feat = _z(debt, 126)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 21d) of the quarterly momentum of dbtgrowh
def f22bs_f22_balance_sheet_survival_dbtgrowhmom_21d_jerk_v141_signal(debt):
    feat = np.log(debt.replace(0, np.nan) / debt.shift(126).replace(0, np.nan))
    feat = feat - feat.shift(63)
    result = _jerk(feat, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of wcdebt_rng252
def f22bs_f22_balance_sheet_survival_wcdebt_rng252mom_126d_jerk_v142_signal(workingcapital, debt):
    feat = _rng(_wc_debt(workingcapital, debt), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of wcdebt_smz63
def f22bs_f22_balance_sheet_survival_wcdebt_smz63mom_63d_jerk_v143_signal(workingcapital, debt):
    r = _wc_debt(workingcapital, debt)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtcap_smz63
def f22bs_f22_balance_sheet_survival_dbtcap_smz63mom_63d_jerk_v144_signal(debt, equity, cashneq):
    r = _debt_capital(debt, equity, cashneq)
    feat = r - r.rolling(63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of levmix_lvl
def f22bs_f22_balance_sheet_survival_levmix_lvlmom_63d_jerk_v145_signal(debt, equity, assets):
    feat = _debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of levmix_z252
def f22bs_f22_balance_sheet_survival_levmix_z252mom_126d_jerk_v146_signal(debt, equity, assets):
    feat = _z(_debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of levmix_ema63
def f22bs_f22_balance_sheet_survival_levmix_ema63mom_63d_jerk_v147_signal(debt, equity, assets):
    feat = (_debt_equity(debt, equity).clip(lower=-10.0, upper=10.0) - 5.0 * _debt_assets(debt, assets)).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of cashdebt_dd252
def f22bs_f22_balance_sheet_survival_cashdebt_dd252mom_126d_jerk_v148_signal(cashneq, debt):
    r = _cash_debt(cashneq, debt)
    feat = r - _rmax(r, 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 126d) of the quarterly momentum of liqbuf_rng252
def f22bs_f22_balance_sheet_survival_liqbuf_rng252mom_126d_jerk_v149_signal(cashneq, workingcapital, debt):
    feat = _rng(_liq_buffer_debt(cashneq, workingcapital, debt), 252)
    feat = feat - feat.shift(63)
    result = _jerk(feat, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (2nd deriv, 63d) of the quarterly momentum of dbtquick_ema63
def f22bs_f22_balance_sheet_survival_dbtquick_ema63mom_63d_jerk_v150_signal(debt, assets, currentratio, cashneq, liabilities):
    feat = _dbt_quick(debt, assets, currentratio, cashneq, liabilities).ewm(span=63, min_periods=21).mean()
    feat = feat - feat.shift(63)
    result = _jerk(feat, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f22bs_f22_balance_sheet_survival_dbteq_lvl_21d_jerk_v001_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z252_63d_jerk_v002_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z126_63d_jerk_v003_signal,
    f22bs_f22_balance_sheet_survival_dbteq_ema63_21d_jerk_v004_signal,
    f22bs_f22_balance_sheet_survival_dbteq_smz63_21d_jerk_v005_signal,
    f22bs_f22_balance_sheet_survival_dbteq_dsp126_63d_jerk_v006_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_lvl_21d_jerk_v007_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z252_63d_jerk_v008_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z126_63d_jerk_v009_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_ema63_21d_jerk_v010_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_smz63_21d_jerk_v011_signal,
    f22bs_f22_balance_sheet_survival_dbtusdassets_lvl_21d_jerk_v012_signal,
    f22bs_f22_balance_sheet_survival_dbtusdassets_z252_63d_jerk_v013_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z126_63d_jerk_v014_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_rng252_63d_jerk_v015_signal,
    f22bs_f22_balance_sheet_survival_ndeq_lvl_21d_jerk_v016_signal,
    f22bs_f22_balance_sheet_survival_ndeq_z252_63d_jerk_v017_signal,
    f22bs_f22_balance_sheet_survival_ndeq_z126_63d_jerk_v018_signal,
    f22bs_f22_balance_sheet_survival_ndeq_ema63_21d_jerk_v019_signal,
    f22bs_f22_balance_sheet_survival_ndeq_smz63_21d_jerk_v020_signal,
    f22bs_f22_balance_sheet_survival_netgear_lvl_21d_jerk_v021_signal,
    f22bs_f22_balance_sheet_survival_netgear_z252_63d_jerk_v022_signal,
    f22bs_f22_balance_sheet_survival_netgear_ema63_21d_jerk_v023_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_lvl_21d_jerk_v024_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_z252_63d_jerk_v025_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_smz63_21d_jerk_v026_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_lvl_21d_jerk_v027_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_z252_63d_jerk_v028_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_ema63_21d_jerk_v029_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_lvl_21d_jerk_v030_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z252_63d_jerk_v031_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z126_63d_jerk_v032_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_ema63_21d_jerk_v033_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_smz63_21d_jerk_v034_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_lvl_21d_jerk_v035_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z252_63d_jerk_v036_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_ema63_21d_jerk_v037_signal,
    f22bs_f22_balance_sheet_survival_dbtgrow_21d_jerk_v038_signal,
    f22bs_f22_balance_sheet_survival_dbtdd252_63d_jerk_v039_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_lvl_21d_jerk_v040_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_lvl_21d_jerk_v041_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_z252_63d_jerk_v042_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_ema63_21d_jerk_v043_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_smz63_21d_jerk_v044_signal,
    f22bs_f22_balance_sheet_survival_curratio_lvl_21d_jerk_v045_signal,
    f22bs_f22_balance_sheet_survival_curratio_z252_63d_jerk_v046_signal,
    f22bs_f22_balance_sheet_survival_curratio_z126_63d_jerk_v047_signal,
    f22bs_f22_balance_sheet_survival_curratio_ema63_21d_jerk_v048_signal,
    f22bs_f22_balance_sheet_survival_curratio_smz63_21d_jerk_v049_signal,
    f22bs_f22_balance_sheet_survival_quick_lvl_21d_jerk_v050_signal,
    f22bs_f22_balance_sheet_survival_quick_z252_63d_jerk_v051_signal,
    f22bs_f22_balance_sheet_survival_quick_ema63_21d_jerk_v052_signal,
    f22bs_f22_balance_sheet_survival_ndassets_lvl_21d_jerk_v053_signal,
    f22bs_f22_balance_sheet_survival_ndassets_z252_63d_jerk_v054_signal,
    f22bs_f22_balance_sheet_survival_ndassets_ema63_21d_jerk_v055_signal,
    f22bs_f22_balance_sheet_survival_ndassets_smz63_21d_jerk_v056_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_lvl_21d_jerk_v057_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_z252_63d_jerk_v058_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_ema63_21d_jerk_v059_signal,
    f22bs_f22_balance_sheet_survival_matpress_lvl_21d_jerk_v060_signal,
    f22bs_f22_balance_sheet_survival_matpress_z252_63d_jerk_v061_signal,
    f22bs_f22_balance_sheet_survival_matpress_smz63_21d_jerk_v062_signal,
    f22bs_f22_balance_sheet_survival_matpress_dsp126_63d_jerk_v063_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z252_63d_jerk_v064_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z126_63d_jerk_v065_signal,
    f22bs_f22_balance_sheet_survival_dbtgrowh_63d_jerk_v066_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_rng252_63d_jerk_v067_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_smz63_21d_jerk_v068_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_smz63_21d_jerk_v069_signal,
    f22bs_f22_balance_sheet_survival_levmix_lvl_21d_jerk_v070_signal,
    f22bs_f22_balance_sheet_survival_levmix_z252_63d_jerk_v071_signal,
    f22bs_f22_balance_sheet_survival_levmix_ema63_21d_jerk_v072_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_dd252_63d_jerk_v073_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_rng252_63d_jerk_v074_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_ema63_21d_jerk_v075_signal,
    f22bs_f22_balance_sheet_survival_dbteq_lvlmom_63d_jerk_v076_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z252mom_126d_jerk_v077_signal,
    f22bs_f22_balance_sheet_survival_dbteq_z126mom_21d_jerk_v078_signal,
    f22bs_f22_balance_sheet_survival_dbteq_ema63mom_63d_jerk_v079_signal,
    f22bs_f22_balance_sheet_survival_dbteq_smz63mom_63d_jerk_v080_signal,
    f22bs_f22_balance_sheet_survival_dbteq_dsp126mom_21d_jerk_v081_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_lvlmom_63d_jerk_v082_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z252mom_126d_jerk_v083_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_z126mom_21d_jerk_v084_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_ema63mom_63d_jerk_v085_signal,
    f22bs_f22_balance_sheet_survival_dbtassets_smz63mom_63d_jerk_v086_signal,
    f22bs_f22_balance_sheet_survival_dbtusdassets_lvlmom_63d_jerk_v087_signal,
    f22bs_f22_balance_sheet_survival_dbtusdassets_z252mom_126d_jerk_v088_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z126mom_21d_jerk_v089_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_rng252mom_126d_jerk_v090_signal,
    f22bs_f22_balance_sheet_survival_ndeq_lvlmom_63d_jerk_v091_signal,
    f22bs_f22_balance_sheet_survival_ndeq_z252mom_126d_jerk_v092_signal,
    f22bs_f22_balance_sheet_survival_ndeq_z126mom_21d_jerk_v093_signal,
    f22bs_f22_balance_sheet_survival_ndeq_ema63mom_63d_jerk_v094_signal,
    f22bs_f22_balance_sheet_survival_ndeq_smz63mom_63d_jerk_v095_signal,
    f22bs_f22_balance_sheet_survival_netgear_lvlmom_63d_jerk_v096_signal,
    f22bs_f22_balance_sheet_survival_netgear_z252mom_126d_jerk_v097_signal,
    f22bs_f22_balance_sheet_survival_netgear_ema63mom_63d_jerk_v098_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_lvlmom_63d_jerk_v099_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_z252mom_126d_jerk_v100_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_smz63mom_63d_jerk_v101_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_lvlmom_63d_jerk_v102_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_z252mom_126d_jerk_v103_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_ema63mom_63d_jerk_v104_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_lvlmom_63d_jerk_v105_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z252mom_126d_jerk_v106_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_z126mom_21d_jerk_v107_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_ema63mom_63d_jerk_v108_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_smz63mom_63d_jerk_v109_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_lvlmom_63d_jerk_v110_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_z252mom_126d_jerk_v111_signal,
    f22bs_f22_balance_sheet_survival_dbtwc_ema63mom_63d_jerk_v112_signal,
    f22bs_f22_balance_sheet_survival_dbtgrowmom_63d_jerk_v113_signal,
    f22bs_f22_balance_sheet_survival_dbtdd252mom_126d_jerk_v114_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_lvlmom_63d_jerk_v115_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_lvlmom_63d_jerk_v116_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_z252mom_126d_jerk_v117_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_ema63mom_63d_jerk_v118_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_smz63mom_63d_jerk_v119_signal,
    f22bs_f22_balance_sheet_survival_curratio_lvlmom_63d_jerk_v120_signal,
    f22bs_f22_balance_sheet_survival_curratio_z252mom_126d_jerk_v121_signal,
    f22bs_f22_balance_sheet_survival_curratio_z126mom_21d_jerk_v122_signal,
    f22bs_f22_balance_sheet_survival_curratio_ema63mom_63d_jerk_v123_signal,
    f22bs_f22_balance_sheet_survival_curratio_smz63mom_63d_jerk_v124_signal,
    f22bs_f22_balance_sheet_survival_quick_lvlmom_63d_jerk_v125_signal,
    f22bs_f22_balance_sheet_survival_quick_z252mom_126d_jerk_v126_signal,
    f22bs_f22_balance_sheet_survival_quick_ema63mom_63d_jerk_v127_signal,
    f22bs_f22_balance_sheet_survival_ndassets_lvlmom_63d_jerk_v128_signal,
    f22bs_f22_balance_sheet_survival_ndassets_z252mom_126d_jerk_v129_signal,
    f22bs_f22_balance_sheet_survival_ndassets_ema63mom_63d_jerk_v130_signal,
    f22bs_f22_balance_sheet_survival_ndassets_smz63mom_63d_jerk_v131_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_lvlmom_63d_jerk_v132_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_z252mom_126d_jerk_v133_signal,
    f22bs_f22_balance_sheet_survival_dbtcurr_ema63mom_63d_jerk_v134_signal,
    f22bs_f22_balance_sheet_survival_matpress_lvlmom_63d_jerk_v135_signal,
    f22bs_f22_balance_sheet_survival_matpress_z252mom_126d_jerk_v136_signal,
    f22bs_f22_balance_sheet_survival_matpress_smz63mom_63d_jerk_v137_signal,
    f22bs_f22_balance_sheet_survival_matpress_dsp126mom_21d_jerk_v138_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z252mom_126d_jerk_v139_signal,
    f22bs_f22_balance_sheet_survival_dbtlevel_z126mom_21d_jerk_v140_signal,
    f22bs_f22_balance_sheet_survival_dbtgrowhmom_21d_jerk_v141_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_rng252mom_126d_jerk_v142_signal,
    f22bs_f22_balance_sheet_survival_wcdebt_smz63mom_63d_jerk_v143_signal,
    f22bs_f22_balance_sheet_survival_dbtcap_smz63mom_63d_jerk_v144_signal,
    f22bs_f22_balance_sheet_survival_levmix_lvlmom_63d_jerk_v145_signal,
    f22bs_f22_balance_sheet_survival_levmix_z252mom_126d_jerk_v146_signal,
    f22bs_f22_balance_sheet_survival_levmix_ema63mom_63d_jerk_v147_signal,
    f22bs_f22_balance_sheet_survival_cashdebt_dd252mom_126d_jerk_v148_signal,
    f22bs_f22_balance_sheet_survival_liqbuf_rng252mom_126d_jerk_v149_signal,
    f22bs_f22_balance_sheet_survival_dbtquick_ema63mom_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_BALANCE_SHEET_SURVIVAL_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    debt = _fund(2201, base=8e7, drift=0.01, vol=0.14).rename("debt")
    debtusd = _fund(2202, base=8.2e7, drift=0.012, vol=0.15).rename("debtusd")
    equity = _fund(2203, base=1.5e8, drift=-0.01, vol=0.16, allow_neg=True).rename("equity")
    assets = _fund(2204, base=3.0e8, drift=0.005, vol=0.09).rename("assets")
    liabilities = _fund(2205, base=1.4e8, drift=0.008, vol=0.11).rename("liabilities")
    currentratio = (1.0 + _fund(2206, base=1.0, drift=0.0, vol=0.18).clip(lower=0.05)).rename("currentratio")
    workingcapital = _fund(2207, base=6e7, drift=0.0, vol=0.20, allow_neg=True).rename("workingcapital")
    cashneq = _fund(2208, base=5e7, drift=-0.005, vol=0.17).rename("cashneq")

    cols = {"debt": debt, "debtusd": debtusd, "equity": equity,
            "assets": assets, "liabilities": liabilities,
            "currentratio": currentratio, "workingcapital": workingcapital,
            "cashneq": cashneq}
    _FUND_SET = ("debt", "debtusd", "equity", "assets", "liabilities",
                 "currentratio", "workingcapital", "cashneq")

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in _FUND_SET for c in meta["inputs"]), name
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
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

    print("OK f22_balance_sheet_survival_3rd_derivatives_001_150_claude.py: %d features pass" % n_features)
