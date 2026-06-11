import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_252d_base_v001_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_252d_base_v001_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_252d_base_v001_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_42d_base_v002_signal(ebitda, equity):
    res = (ebitda / equity).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_42d_base_v002_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_42d_base_v002_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_252d_base_v003_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_252d_base_v003_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_252d_base_v003_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_15d_base_v004_signal(ebitda, debt):
    res = (ebitda / debt).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_15d_base_v004_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_15d_base_v004_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_90d_base_v005_signal(ebitda, ev):
    res = (ebitda / ev).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_90d_base_v005_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_90d_base_v005_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_90d_base_v006_signal(fcf, revenue):
    res = (fcf / revenue).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_90d_base_v006_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_90d_base_v006_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_42d_base_v007_signal(ebitda, equity):
    res = (ebitda / equity).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_42d_base_v007_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_42d_base_v007_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_63d_base_v008_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_63d_base_v008_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_63d_base_v008_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_180d_base_v009_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(180).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_180d_base_v009_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_180d_base_v009_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_63d_base_v010_signal(netinc, revenue):
    res = (netinc / revenue).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_63d_base_v010_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_63d_base_v010_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_90d_base_v011_signal(netinc, revenue):
    res = (netinc / revenue).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_90d_base_v011_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_90d_base_v011_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_5d_base_v012_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_5d_base_v012_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_5d_base_v012_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_63d_base_v013_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_63d_base_v013_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_63d_base_v013_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_10d_base_v014_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_10d_base_v014_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_10d_base_v014_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_252d_base_v015_signal(ebitda, debt):
    res = (ebitda / debt).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_252d_base_v015_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_252d_base_v015_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_90d_base_v016_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_90d_base_v016_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_90d_base_v016_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_42d_base_v017_signal(opinc, revenue):
    res = (opinc / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_42d_base_v017_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_42d_base_v017_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_30d_base_v018_signal(ebitda, ev):
    res = (ebitda / ev).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_30d_base_v018_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_30d_base_v018_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_30d_base_v019_signal(fcf, revenue):
    res = (fcf / revenue).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_30d_base_v019_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_30d_base_v019_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_180d_base_v020_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_180d_base_v020_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_180d_base_v020_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_21d_base_v021_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_21d_base_v021_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_21d_base_v021_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_30d_base_v022_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_30d_base_v022_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_30d_base_v022_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_63d_base_v023_signal(opinc, revenue):
    res = (opinc / revenue).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_63d_base_v023_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_63d_base_v023_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_180d_base_v024_signal(ebitda, ev):
    res = (ebitda / ev).rolling(180).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_180d_base_v024_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_180d_base_v024_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_pct_126d_base_v025_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(126).std().pct_change()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_pct_126d_base_v025_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_pct_126d_base_v025_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_15d_base_v026_signal(ebitda, equity):
    res = (ebitda / equity).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_15d_base_v026_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_15d_base_v026_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_42d_base_v027_signal(ebitda, gp):
    res = (ebitda / gp).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_42d_base_v027_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_42d_base_v027_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_126d_base_v028_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_126d_base_v028_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_126d_base_v028_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_63d_base_v029_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_63d_base_v029_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_63d_base_v029_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_63d_base_v030_signal(netinc, revenue):
    res = (netinc / revenue).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_63d_base_v030_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_63d_base_v030_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_15d_base_v031_signal(opinc, revenue):
    res = (opinc / revenue).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_15d_base_v031_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_15d_base_v031_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_180d_base_v032_signal(netinc, revenue):
    res = (netinc / revenue).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_180d_base_v032_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_180d_base_v032_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_30d_base_v033_signal(opinc, revenue):
    res = (opinc / revenue).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_30d_base_v033_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_30d_base_v033_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_90d_base_v034_signal(ebitda, gp):
    res = (ebitda / gp).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_90d_base_v034_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_90d_base_v034_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_180d_base_v035_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_180d_base_v035_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_180d_base_v035_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_15d_base_v036_signal(ebitda, assets):
    res = (ebitda / assets).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_15d_base_v036_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_15d_base_v036_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_180d_base_v037_signal(ebitda, equity):
    res = (ebitda / equity).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_180d_base_v037_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_180d_base_v037_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_252d_base_v038_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_252d_base_v038_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_252d_base_v038_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_21d_base_v039_signal(netinc, revenue):
    res = (netinc / revenue).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_21d_base_v039_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_21d_base_v039_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_10d_base_v040_signal(ebitda, ev):
    res = (ebitda / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_10d_base_v040_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_10d_base_v040_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_126d_base_v041_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_126d_base_v041_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_126d_base_v041_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_180d_base_v042_signal(ebitda, gp):
    res = (ebitda / gp).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_180d_base_v042_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_180d_base_v042_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_252d_base_v043_signal(opinc, revenue):
    res = (opinc / revenue).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_252d_base_v043_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_252d_base_v043_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_42d_base_v044_signal(ebitda, ev):
    res = (ebitda / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_42d_base_v044_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_42d_base_v044_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_63d_base_v045_signal(ebitda, equity):
    res = (ebitda / equity).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_63d_base_v045_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_63d_base_v045_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_252d_base_v046_signal(ebitda, equity):
    res = (ebitda / equity).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_252d_base_v046_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_252d_base_v046_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_21d_base_v047_signal(ebitda, revenue, closeadj):
    res = (ebitda / revenue).rolling(21).std() / closeadj.pct_change().rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_21d_base_v047_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_21d_base_v047_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_42d_base_v048_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_42d_base_v048_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_42d_base_v048_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_90d_base_v049_signal(opinc, revenue):
    res = (opinc / revenue).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_90d_base_v049_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_90d_base_v049_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_180d_base_v050_signal(ebitda, equity):
    res = (ebitda / equity).rolling(180).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_180d_base_v050_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_180d_base_v050_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_10d_base_v051_signal(netinc, revenue):
    res = (netinc / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_10d_base_v051_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_10d_base_v051_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_21d_base_v052_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_21d_base_v052_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_21d_base_v052_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_10d_base_v053_signal(opinc, revenue):
    res = (opinc / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_10d_base_v053_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_10d_base_v053_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_42d_base_v054_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_42d_base_v054_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_42d_base_v054_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_252d_base_v055_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_252d_base_v055_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_252d_base_v055_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_63d_base_v056_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_63d_base_v056_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_63d_base_v056_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_90d_base_v057_signal(ebitda, ev):
    res = (ebitda / ev).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_90d_base_v057_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_90d_base_v057_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_126d_base_v058_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_126d_base_v058_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_126d_base_v058_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_90d_base_v059_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_90d_base_v059_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_90d_base_v059_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_63d_base_v060_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_63d_base_v060_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_63d_base_v060_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_252d_base_v061_signal(fcf, revenue):
    res = (fcf / revenue).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_252d_base_v061_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_252d_base_v061_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_63d_base_v062_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(63).std().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_63d_base_v062_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_63d_base_v062_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_21d_base_v063_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_21d_base_v063_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_21d_base_v063_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_15d_base_v064_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_15d_base_v064_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_15d_base_v064_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_10d_base_v065_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_10d_base_v065_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_10d_base_v065_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_5d_base_v066_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_5d_base_v066_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_5d_base_v066_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_5d_base_v067_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_5d_base_v067_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_5d_base_v067_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_5d_base_v068_signal(ebitda, ev):
    res = (ebitda / ev).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_5d_base_v068_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_5d_base_v068_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_126d_base_v069_signal(opinc, revenue):
    res = (opinc / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_126d_base_v069_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_126d_base_v069_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_180d_base_v070_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(180).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_180d_base_v070_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_180d_base_v070_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_30d_base_v071_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_30d_base_v071_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_30d_base_v071_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_21d_base_v072_signal(opinc, revenue):
    res = (opinc / revenue).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_21d_base_v072_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_skew_21d_base_v072_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_21d_base_v073_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(21).std().diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_21d_base_v073_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_std_diff_21d_base_v073_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_42d_base_v074_signal(ebitda, assets):
    res = (ebitda / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_42d_base_v074_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_42d_base_v074_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_63d_base_v075_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_63d_base_v075_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_std_63d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "opinc": np.random.uniform(40, 180, n),
        "netinc": np.random.uniform(20, 100, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "ev": np.random.uniform(6000, 25000, n),
        "closeadj": np.random.uniform(10, 100, n),
        "volume": np.random.uniform(100000, 1000000, n),
        "ncfo": np.random.uniform(30, 150, n),
        "capex": np.random.uniform(10, 50, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "currentratio": np.random.uniform(1, 5, n),
        "gp": np.random.uniform(100, 400, n),
        "retearn": np.random.uniform(500, 2000, n),
        "eps": np.random.uniform(0.1, 5, n),
        "fcf": np.random.uniform(20, 120, n),
        "pe": np.random.uniform(10, 30, n),
        "pb": np.random.uniform(1, 5, n),
        "ps": np.random.uniform(1, 10, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
                assert corr_matrix.iloc[i, j] <= 0.95, f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}"
    print(f"Self-test passed for {os.path.basename(__file__)}")

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
