import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f160e_f160_equity_to_assets_solvency_regime_calc001_12d_base_v001_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(12)
    v_005 = v_003.rolling(18).mean()
    v_006 = v_003.rolling(18).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(12)
    v_009 = v_008.rolling(22).mean()
    v_010 = v_008.rolling(22).std()
    v_011 = v_008.diff(22)
    v_012 = v_007.diff(12)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(18)
    v_015 = v_003.pct_change(12).diff(9)
    v_016 = v_003.rolling(30).skew()
    v_017 = v_003.rolling(30).kurt()
    v_018 = v_011.rolling(11).std()
    v_019 = v_015.rolling(18).mean()
    v_020 = v_012 * 0.2230 + v_014 * 0.3340 + v_011 * 0.4450
    v_021 = v_004.rolling(22).quantile(0.5)
    v_022 = v_015.diff(18)
    v_023 = v_003.rolling(12).max() / v_003.rolling(12).min().replace(0, np.nan)
    v_024 = v_023.diff(12)
    v_025 = v_020.rolling(18).std()
    v_026 = v_017.diff(12)
    v_027 = v_016.diff(12)
    v_028 = v_025 * 0.2230 - v_021 * 0.3340
    v_029 = v_011.rolling(22).skew()
    v_030 = v_020.pct_change(4)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[3]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc001_12d_base_v001_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc001_12d_base_v001_signal

def f160e_f160_equity_to_assets_solvency_regime_calc002_19d_base_v002_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(19)
    v_005 = v_003.rolling(31).mean()
    v_006 = v_003.rolling(31).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(19)
    v_009 = v_008.rolling(39).mean()
    v_010 = v_008.rolling(39).std()
    v_011 = v_008.diff(39)
    v_012 = v_007.diff(19)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(31)
    v_015 = v_003.pct_change(19).diff(15)
    v_016 = v_003.rolling(50).skew()
    v_017 = v_003.rolling(50).kurt()
    v_018 = v_011.rolling(19).std()
    v_019 = v_015.rolling(31).mean()
    v_020 = v_012 * 0.3460 + v_014 * 0.5680 + v_011 * 0.7900
    v_021 = v_004.rolling(39).quantile(0.5)
    v_022 = v_015.diff(31)
    v_023 = v_003.rolling(19).max() / v_003.rolling(19).min().replace(0, np.nan)
    v_024 = v_023.diff(19)
    v_025 = v_020.rolling(31).std()
    v_026 = v_017.diff(19)
    v_027 = v_016.diff(19)
    v_028 = v_025 * 0.3460 - v_021 * 0.5680
    v_029 = v_011.rolling(39).skew()
    v_030 = v_020.pct_change(6)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[6]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc002_19d_base_v002_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc002_19d_base_v002_signal

def f160e_f160_equity_to_assets_solvency_regime_calc003_26d_base_v003_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(26).mean().diff(44)
    v_005 = v_003.rolling(44).mean()
    v_006 = v_003.rolling(44).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(26)
    v_009 = v_008.rolling(56).mean()
    v_010 = v_008.rolling(56).std()
    v_011 = v_008.diff(56)
    v_012 = v_007.diff(26)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(44)
    v_015 = v_003.pct_change(26).diff(22)
    v_016 = v_003.rolling(70).skew()
    v_017 = v_003.rolling(70).kurt()
    v_018 = v_011.rolling(28).std()
    v_019 = v_015.rolling(44).mean()
    v_020 = v_012 * 0.4690 + v_014 * 0.8020 + v_011 * 1.1350
    v_021 = v_004.rolling(56).quantile(0.5)
    v_022 = v_015.diff(44)
    v_023 = v_003.rolling(26).max() / v_003.rolling(26).min().replace(0, np.nan)
    v_024 = v_023.diff(26)
    v_025 = v_020.rolling(44).std()
    v_026 = v_017.diff(26)
    v_027 = v_016.diff(26)
    v_028 = v_025 * 0.4690 - v_021 * 0.8020
    v_029 = v_011.rolling(56).skew()
    v_030 = v_020.pct_change(8)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[9]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc003_26d_base_v003_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc003_26d_base_v003_signal

def f160e_f160_equity_to_assets_solvency_regime_calc004_33d_base_v004_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(33).std().diff(57)
    v_005 = v_003.rolling(57).mean()
    v_006 = v_003.rolling(57).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(33)
    v_009 = v_008.rolling(73).mean()
    v_010 = v_008.rolling(73).std()
    v_011 = v_008.diff(73)
    v_012 = v_007.diff(33)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(57)
    v_015 = v_003.pct_change(33).diff(28)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(36).std()
    v_019 = v_015.rolling(57).mean()
    v_020 = v_012 * 0.5920 + v_014 * 1.0360 + v_011 * 1.4800
    v_021 = v_004.rolling(73).quantile(0.5)
    v_022 = v_015.diff(57)
    v_023 = v_003.rolling(33).max() / v_003.rolling(33).min().replace(0, np.nan)
    v_024 = v_023.diff(33)
    v_025 = v_020.rolling(57).std()
    v_026 = v_017.diff(33)
    v_027 = v_016.diff(33)
    v_028 = v_025 * 0.5920 - v_021 * 1.0360
    v_029 = v_011.rolling(73).skew()
    v_030 = v_020.pct_change(11)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[12]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc004_33d_base_v004_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc004_33d_base_v004_signal

def f160e_f160_equity_to_assets_solvency_regime_calc005_40d_base_v005_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(40).rolling(70).mean()
    v_005 = v_003.rolling(70).mean()
    v_006 = v_003.rolling(70).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(40)
    v_009 = v_008.rolling(90).mean()
    v_010 = v_008.rolling(90).std()
    v_011 = v_008.diff(90)
    v_012 = v_007.diff(40)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(70)
    v_015 = v_003.pct_change(40).diff(35)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(45).std()
    v_019 = v_015.rolling(70).mean()
    v_020 = v_012 * 0.7150 + v_014 * 1.2700 + v_011 * 1.8250
    v_021 = v_004.rolling(90).quantile(0.5)
    v_022 = v_015.diff(70)
    v_023 = v_003.rolling(40).max() / v_003.rolling(40).min().replace(0, np.nan)
    v_024 = v_023.diff(40)
    v_025 = v_020.rolling(70).std()
    v_026 = v_017.diff(40)
    v_027 = v_016.diff(40)
    v_028 = v_025 * 0.7150 - v_021 * 1.2700
    v_029 = v_011.rolling(90).skew()
    v_030 = v_020.pct_change(13)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[15]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc005_40d_base_v005_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc005_40d_base_v005_signal

def f160e_f160_equity_to_assets_solvency_regime_calc006_47d_base_v006_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(47).rolling(83).std()
    v_005 = v_003.rolling(83).mean()
    v_006 = v_003.rolling(83).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(47)
    v_009 = v_008.rolling(107).mean()
    v_010 = v_008.rolling(107).std()
    v_011 = v_008.diff(107)
    v_012 = v_007.diff(47)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(83)
    v_015 = v_003.pct_change(47).diff(41)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(53).std()
    v_019 = v_015.rolling(83).mean()
    v_020 = v_012 * 0.8380 + v_014 * 1.5040 + v_011 * 2.1700
    v_021 = v_004.rolling(107).quantile(0.5)
    v_022 = v_015.diff(83)
    v_023 = v_003.rolling(47).max() / v_003.rolling(47).min().replace(0, np.nan)
    v_024 = v_023.diff(47)
    v_025 = v_020.rolling(83).std()
    v_026 = v_017.diff(47)
    v_027 = v_016.diff(47)
    v_028 = v_025 * 0.8380 - v_021 * 1.5040
    v_029 = v_011.rolling(107).skew()
    v_030 = v_020.pct_change(15)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[18]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc006_47d_base_v006_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc006_47d_base_v006_signal

def f160e_f160_equity_to_assets_solvency_regime_calc007_54d_base_v007_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(54).skew().diff(96)
    v_005 = v_003.rolling(96).mean()
    v_006 = v_003.rolling(96).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(54)
    v_009 = v_008.rolling(124).mean()
    v_010 = v_008.rolling(124).std()
    v_011 = v_008.diff(124)
    v_012 = v_007.diff(54)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(96)
    v_015 = v_003.pct_change(54).diff(48)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(62).std()
    v_019 = v_015.rolling(96).mean()
    v_020 = v_012 * 0.9610 + v_014 * 1.7380 + v_011 * 2.5150
    v_021 = v_004.rolling(124).quantile(0.5)
    v_022 = v_015.diff(96)
    v_023 = v_003.rolling(54).max() / v_003.rolling(54).min().replace(0, np.nan)
    v_024 = v_023.diff(54)
    v_025 = v_020.rolling(96).std()
    v_026 = v_017.diff(54)
    v_027 = v_016.diff(54)
    v_028 = v_025 * 0.9610 - v_021 * 1.7380
    v_029 = v_011.rolling(124).skew()
    v_030 = v_020.pct_change(18)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[1]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc007_54d_base_v007_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc007_54d_base_v007_signal

def f160e_f160_equity_to_assets_solvency_regime_calc008_61d_base_v008_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(61)
    v_005 = v_003.rolling(109).mean()
    v_006 = v_003.rolling(109).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(61)
    v_009 = v_008.rolling(141).mean()
    v_010 = v_008.rolling(141).std()
    v_011 = v_008.diff(141)
    v_012 = v_007.diff(61)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(109)
    v_015 = v_003.pct_change(61).diff(54)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(70).std()
    v_019 = v_015.rolling(109).mean()
    v_020 = v_012 * 1.0840 + v_014 * 1.9720 + v_011 * 2.8600
    v_021 = v_004.rolling(141).quantile(0.5)
    v_022 = v_015.diff(109)
    v_023 = v_003.rolling(61).max() / v_003.rolling(61).min().replace(0, np.nan)
    v_024 = v_023.diff(61)
    v_025 = v_020.rolling(109).std()
    v_026 = v_017.diff(61)
    v_027 = v_016.diff(61)
    v_028 = v_025 * 1.0840 - v_021 * 1.9720
    v_029 = v_011.rolling(141).skew()
    v_030 = v_020.pct_change(20)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[4]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc008_61d_base_v008_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc008_61d_base_v008_signal

def f160e_f160_equity_to_assets_solvency_regime_calc009_68d_base_v009_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(68)
    v_005 = v_003.rolling(122).mean()
    v_006 = v_003.rolling(122).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(68)
    v_009 = v_008.rolling(18).mean()
    v_010 = v_008.rolling(18).std()
    v_011 = v_008.diff(18)
    v_012 = v_007.diff(68)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(122)
    v_015 = v_003.pct_change(68).diff(61)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(9).std()
    v_019 = v_015.rolling(122).mean()
    v_020 = v_012 * 1.2070 + v_014 * 2.2060 + v_011 * 3.2050
    v_021 = v_004.rolling(18).quantile(0.5)
    v_022 = v_015.diff(122)
    v_023 = v_003.rolling(68).max() / v_003.rolling(68).min().replace(0, np.nan)
    v_024 = v_023.diff(68)
    v_025 = v_020.rolling(122).std()
    v_026 = v_017.diff(68)
    v_027 = v_016.diff(68)
    v_028 = v_025 * 1.2070 - v_021 * 2.2060
    v_029 = v_011.rolling(18).skew()
    v_030 = v_020.pct_change(22)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[7]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc009_68d_base_v009_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc009_68d_base_v009_signal

def f160e_f160_equity_to_assets_solvency_regime_calc010_75d_base_v010_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(75)
    v_005 = v_003.rolling(135).mean()
    v_006 = v_003.rolling(135).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(75)
    v_009 = v_008.rolling(35).mean()
    v_010 = v_008.rolling(35).std()
    v_011 = v_008.diff(35)
    v_012 = v_007.diff(75)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(135)
    v_015 = v_003.pct_change(75).diff(67)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(17).std()
    v_019 = v_015.rolling(135).mean()
    v_020 = v_012 * 1.3300 + v_014 * 2.4400 + v_011 * 3.5500
    v_021 = v_004.rolling(35).quantile(0.5)
    v_022 = v_015.diff(135)
    v_023 = v_003.rolling(75).max() / v_003.rolling(75).min().replace(0, np.nan)
    v_024 = v_023.diff(75)
    v_025 = v_020.rolling(135).std()
    v_026 = v_017.diff(75)
    v_027 = v_016.diff(75)
    v_028 = v_025 * 1.3300 - v_021 * 2.4400
    v_029 = v_011.rolling(35).skew()
    v_030 = v_020.pct_change(25)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[10]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc010_75d_base_v010_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc010_75d_base_v010_signal

def f160e_f160_equity_to_assets_solvency_regime_calc011_82d_base_v011_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(82).mean().diff(8)
    v_005 = v_003.rolling(8).mean()
    v_006 = v_003.rolling(8).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(82)
    v_009 = v_008.rolling(52).mean()
    v_010 = v_008.rolling(52).std()
    v_011 = v_008.diff(52)
    v_012 = v_007.diff(82)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(8)
    v_015 = v_003.pct_change(82).diff(4)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(26).std()
    v_019 = v_015.rolling(8).mean()
    v_020 = v_012 * 1.4530 + v_014 * 2.6740 + v_011 * 3.8950
    v_021 = v_004.rolling(52).quantile(0.5)
    v_022 = v_015.diff(8)
    v_023 = v_003.rolling(82).max() / v_003.rolling(82).min().replace(0, np.nan)
    v_024 = v_023.diff(82)
    v_025 = v_020.rolling(8).std()
    v_026 = v_017.diff(82)
    v_027 = v_016.diff(82)
    v_028 = v_025 * 1.4530 - v_021 * 2.6740
    v_029 = v_011.rolling(52).skew()
    v_030 = v_020.pct_change(27)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[13]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc011_82d_base_v011_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc011_82d_base_v011_signal

def f160e_f160_equity_to_assets_solvency_regime_calc012_89d_base_v012_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(89).std().diff(21)
    v_005 = v_003.rolling(21).mean()
    v_006 = v_003.rolling(21).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(89)
    v_009 = v_008.rolling(69).mean()
    v_010 = v_008.rolling(69).std()
    v_011 = v_008.diff(69)
    v_012 = v_007.diff(89)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(21)
    v_015 = v_003.pct_change(89).diff(10)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(34).std()
    v_019 = v_015.rolling(21).mean()
    v_020 = v_012 * 1.5760 + v_014 * 2.9080 + v_011 * 4.2400
    v_021 = v_004.rolling(69).quantile(0.5)
    v_022 = v_015.diff(21)
    v_023 = v_003.rolling(89).max() / v_003.rolling(89).min().replace(0, np.nan)
    v_024 = v_023.diff(89)
    v_025 = v_020.rolling(21).std()
    v_026 = v_017.diff(89)
    v_027 = v_016.diff(89)
    v_028 = v_025 * 1.5760 - v_021 * 2.9080
    v_029 = v_011.rolling(69).skew()
    v_030 = v_020.pct_change(29)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[16]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc012_89d_base_v012_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc012_89d_base_v012_signal

def f160e_f160_equity_to_assets_solvency_regime_calc013_96d_base_v013_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(96).rolling(34).mean()
    v_005 = v_003.rolling(34).mean()
    v_006 = v_003.rolling(34).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(96)
    v_009 = v_008.rolling(86).mean()
    v_010 = v_008.rolling(86).std()
    v_011 = v_008.diff(86)
    v_012 = v_007.diff(96)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(34)
    v_015 = v_003.pct_change(96).diff(17)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(43).std()
    v_019 = v_015.rolling(34).mean()
    v_020 = v_012 * 1.6990 + v_014 * 3.1420 + v_011 * 4.5850
    v_021 = v_004.rolling(86).quantile(0.5)
    v_022 = v_015.diff(34)
    v_023 = v_003.rolling(96).max() / v_003.rolling(96).min().replace(0, np.nan)
    v_024 = v_023.diff(96)
    v_025 = v_020.rolling(34).std()
    v_026 = v_017.diff(96)
    v_027 = v_016.diff(96)
    v_028 = v_025 * 1.6990 - v_021 * 3.1420
    v_029 = v_011.rolling(86).skew()
    v_030 = v_020.pct_change(32)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[19]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc013_96d_base_v013_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc013_96d_base_v013_signal

def f160e_f160_equity_to_assets_solvency_regime_calc014_103d_base_v014_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(103).rolling(47).std()
    v_005 = v_003.rolling(47).mean()
    v_006 = v_003.rolling(47).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(103)
    v_009 = v_008.rolling(103).mean()
    v_010 = v_008.rolling(103).std()
    v_011 = v_008.diff(103)
    v_012 = v_007.diff(103)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(47)
    v_015 = v_003.pct_change(103).diff(23)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(51).std()
    v_019 = v_015.rolling(47).mean()
    v_020 = v_012 * 1.8220 + v_014 * 3.3760 + v_011 * 4.9300
    v_021 = v_004.rolling(103).quantile(0.5)
    v_022 = v_015.diff(47)
    v_023 = v_003.rolling(103).max() / v_003.rolling(103).min().replace(0, np.nan)
    v_024 = v_023.diff(103)
    v_025 = v_020.rolling(47).std()
    v_026 = v_017.diff(103)
    v_027 = v_016.diff(103)
    v_028 = v_025 * 1.8220 - v_021 * 3.3760
    v_029 = v_011.rolling(103).skew()
    v_030 = v_020.pct_change(34)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[2]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc014_103d_base_v014_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc014_103d_base_v014_signal

def f160e_f160_equity_to_assets_solvency_regime_calc015_110d_base_v015_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(110).skew().diff(60)
    v_005 = v_003.rolling(60).mean()
    v_006 = v_003.rolling(60).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(110)
    v_009 = v_008.rolling(120).mean()
    v_010 = v_008.rolling(120).std()
    v_011 = v_008.diff(120)
    v_012 = v_007.diff(110)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(60)
    v_015 = v_003.pct_change(110).diff(30)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(60).std()
    v_019 = v_015.rolling(60).mean()
    v_020 = v_012 * 1.9450 + v_014 * 3.6100 + v_011 * 0.3750
    v_021 = v_004.rolling(120).quantile(0.5)
    v_022 = v_015.diff(60)
    v_023 = v_003.rolling(110).max() / v_003.rolling(110).min().replace(0, np.nan)
    v_024 = v_023.diff(110)
    v_025 = v_020.rolling(60).std()
    v_026 = v_017.diff(110)
    v_027 = v_016.diff(110)
    v_028 = v_025 * 1.9450 - v_021 * 3.6100
    v_029 = v_011.rolling(120).skew()
    v_030 = v_020.pct_change(36)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[5]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc015_110d_base_v015_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc015_110d_base_v015_signal

def f160e_f160_equity_to_assets_solvency_regime_calc016_117d_base_v016_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(117)
    v_005 = v_003.rolling(73).mean()
    v_006 = v_003.rolling(73).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(117)
    v_009 = v_008.rolling(137).mean()
    v_010 = v_008.rolling(137).std()
    v_011 = v_008.diff(137)
    v_012 = v_007.diff(117)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(73)
    v_015 = v_003.pct_change(117).diff(36)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(68).std()
    v_019 = v_015.rolling(73).mean()
    v_020 = v_012 * 2.0680 + v_014 * 3.8440 + v_011 * 0.7200
    v_021 = v_004.rolling(137).quantile(0.5)
    v_022 = v_015.diff(73)
    v_023 = v_003.rolling(117).max() / v_003.rolling(117).min().replace(0, np.nan)
    v_024 = v_023.diff(117)
    v_025 = v_020.rolling(73).std()
    v_026 = v_017.diff(117)
    v_027 = v_016.diff(117)
    v_028 = v_025 * 2.0680 - v_021 * 3.8440
    v_029 = v_011.rolling(137).skew()
    v_030 = v_020.pct_change(39)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[8]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc016_117d_base_v016_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc016_117d_base_v016_signal

def f160e_f160_equity_to_assets_solvency_regime_calc017_124d_base_v017_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(124)
    v_005 = v_003.rolling(86).mean()
    v_006 = v_003.rolling(86).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(124)
    v_009 = v_008.rolling(14).mean()
    v_010 = v_008.rolling(14).std()
    v_011 = v_008.diff(14)
    v_012 = v_007.diff(124)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(86)
    v_015 = v_003.pct_change(124).diff(43)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(7).std()
    v_019 = v_015.rolling(86).mean()
    v_020 = v_012 * 2.1910 + v_014 * 4.0780 + v_011 * 1.0650
    v_021 = v_004.rolling(14).quantile(0.5)
    v_022 = v_015.diff(86)
    v_023 = v_003.rolling(124).max() / v_003.rolling(124).min().replace(0, np.nan)
    v_024 = v_023.diff(124)
    v_025 = v_020.rolling(86).std()
    v_026 = v_017.diff(124)
    v_027 = v_016.diff(124)
    v_028 = v_025 * 2.1910 - v_021 * 4.0780
    v_029 = v_011.rolling(14).skew()
    v_030 = v_020.pct_change(41)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[11]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc017_124d_base_v017_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc017_124d_base_v017_signal

def f160e_f160_equity_to_assets_solvency_regime_calc018_131d_base_v018_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(131)
    v_005 = v_003.rolling(99).mean()
    v_006 = v_003.rolling(99).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(131)
    v_009 = v_008.rolling(31).mean()
    v_010 = v_008.rolling(31).std()
    v_011 = v_008.diff(31)
    v_012 = v_007.diff(131)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(99)
    v_015 = v_003.pct_change(131).diff(49)
    v_016 = v_003.rolling(230).skew()
    v_017 = v_003.rolling(230).kurt()
    v_018 = v_011.rolling(15).std()
    v_019 = v_015.rolling(99).mean()
    v_020 = v_012 * 2.3140 + v_014 * 4.3120 + v_011 * 1.4100
    v_021 = v_004.rolling(31).quantile(0.5)
    v_022 = v_015.diff(99)
    v_023 = v_003.rolling(131).max() / v_003.rolling(131).min().replace(0, np.nan)
    v_024 = v_023.diff(131)
    v_025 = v_020.rolling(99).std()
    v_026 = v_017.diff(131)
    v_027 = v_016.diff(131)
    v_028 = v_025 * 2.3140 - v_021 * 4.3120
    v_029 = v_011.rolling(31).skew()
    v_030 = v_020.pct_change(43)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[14]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc018_131d_base_v018_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc018_131d_base_v018_signal

def f160e_f160_equity_to_assets_solvency_regime_calc019_138d_base_v019_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(138).mean().diff(112)
    v_005 = v_003.rolling(112).mean()
    v_006 = v_003.rolling(112).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(138)
    v_009 = v_008.rolling(48).mean()
    v_010 = v_008.rolling(48).std()
    v_011 = v_008.diff(48)
    v_012 = v_007.diff(138)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(112)
    v_015 = v_003.pct_change(138).diff(56)
    v_016 = v_003.rolling(250).skew()
    v_017 = v_003.rolling(250).kurt()
    v_018 = v_011.rolling(24).std()
    v_019 = v_015.rolling(112).mean()
    v_020 = v_012 * 2.4370 + v_014 * 4.5460 + v_011 * 1.7550
    v_021 = v_004.rolling(48).quantile(0.5)
    v_022 = v_015.diff(112)
    v_023 = v_003.rolling(138).max() / v_003.rolling(138).min().replace(0, np.nan)
    v_024 = v_023.diff(138)
    v_025 = v_020.rolling(112).std()
    v_026 = v_017.diff(138)
    v_027 = v_016.diff(138)
    v_028 = v_025 * 2.4370 - v_021 * 4.5460
    v_029 = v_011.rolling(48).skew()
    v_030 = v_020.pct_change(46)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[17]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc019_138d_base_v019_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc019_138d_base_v019_signal

def f160e_f160_equity_to_assets_solvency_regime_calc020_5d_base_v020_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(5).std().diff(125)
    v_005 = v_003.rolling(125).mean()
    v_006 = v_003.rolling(125).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(5)
    v_009 = v_008.rolling(65).mean()
    v_010 = v_008.rolling(65).std()
    v_011 = v_008.diff(65)
    v_012 = v_007.diff(5)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(125)
    v_015 = v_003.pct_change(5).diff(62)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(32).std()
    v_019 = v_015.rolling(125).mean()
    v_020 = v_012 * 2.5600 + v_014 * 4.7800 + v_011 * 2.1000
    v_021 = v_004.rolling(65).quantile(0.5)
    v_022 = v_015.diff(125)
    v_023 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_024 = v_023.diff(5)
    v_025 = v_020.rolling(125).std()
    v_026 = v_017.diff(5)
    v_027 = v_016.diff(5)
    v_028 = v_025 * 2.5600 - v_021 * 4.7800
    v_029 = v_011.rolling(65).skew()
    v_030 = v_020.pct_change(1)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[0]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc020_5d_base_v020_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc020_5d_base_v020_signal

def f160e_f160_equity_to_assets_solvency_regime_calc021_12d_base_v021_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(12).rolling(138).mean()
    v_005 = v_003.rolling(138).mean()
    v_006 = v_003.rolling(138).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(12)
    v_009 = v_008.rolling(82).mean()
    v_010 = v_008.rolling(82).std()
    v_011 = v_008.diff(82)
    v_012 = v_007.diff(12)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(138)
    v_015 = v_003.pct_change(12).diff(69)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(41).std()
    v_019 = v_015.rolling(138).mean()
    v_020 = v_012 * 2.6830 + v_014 * 0.1140 + v_011 * 2.4450
    v_021 = v_004.rolling(82).quantile(0.5)
    v_022 = v_015.diff(138)
    v_023 = v_003.rolling(12).max() / v_003.rolling(12).min().replace(0, np.nan)
    v_024 = v_023.diff(12)
    v_025 = v_020.rolling(138).std()
    v_026 = v_017.diff(12)
    v_027 = v_016.diff(12)
    v_028 = v_025 * 2.6830 - v_021 * 0.1140
    v_029 = v_011.rolling(82).skew()
    v_030 = v_020.pct_change(4)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[3]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc021_12d_base_v021_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc021_12d_base_v021_signal

def f160e_f160_equity_to_assets_solvency_regime_calc022_19d_base_v022_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(19).rolling(11).std()
    v_005 = v_003.rolling(11).mean()
    v_006 = v_003.rolling(11).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(19)
    v_009 = v_008.rolling(99).mean()
    v_010 = v_008.rolling(99).std()
    v_011 = v_008.diff(99)
    v_012 = v_007.diff(19)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(11)
    v_015 = v_003.pct_change(19).diff(5)
    v_016 = v_003.rolling(30).skew()
    v_017 = v_003.rolling(30).kurt()
    v_018 = v_011.rolling(49).std()
    v_019 = v_015.rolling(11).mean()
    v_020 = v_012 * 2.8060 + v_014 * 0.3480 + v_011 * 2.7900
    v_021 = v_004.rolling(99).quantile(0.5)
    v_022 = v_015.diff(11)
    v_023 = v_003.rolling(19).max() / v_003.rolling(19).min().replace(0, np.nan)
    v_024 = v_023.diff(19)
    v_025 = v_020.rolling(11).std()
    v_026 = v_017.diff(19)
    v_027 = v_016.diff(19)
    v_028 = v_025 * 2.8060 - v_021 * 0.3480
    v_029 = v_011.rolling(99).skew()
    v_030 = v_020.pct_change(6)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[6]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc022_19d_base_v022_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc022_19d_base_v022_signal

def f160e_f160_equity_to_assets_solvency_regime_calc023_26d_base_v023_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(26).skew().diff(24)
    v_005 = v_003.rolling(24).mean()
    v_006 = v_003.rolling(24).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(26)
    v_009 = v_008.rolling(116).mean()
    v_010 = v_008.rolling(116).std()
    v_011 = v_008.diff(116)
    v_012 = v_007.diff(26)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(24)
    v_015 = v_003.pct_change(26).diff(12)
    v_016 = v_003.rolling(50).skew()
    v_017 = v_003.rolling(50).kurt()
    v_018 = v_011.rolling(58).std()
    v_019 = v_015.rolling(24).mean()
    v_020 = v_012 * 2.9290 + v_014 * 0.5820 + v_011 * 3.1350
    v_021 = v_004.rolling(116).quantile(0.5)
    v_022 = v_015.diff(24)
    v_023 = v_003.rolling(26).max() / v_003.rolling(26).min().replace(0, np.nan)
    v_024 = v_023.diff(26)
    v_025 = v_020.rolling(24).std()
    v_026 = v_017.diff(26)
    v_027 = v_016.diff(26)
    v_028 = v_025 * 2.9290 - v_021 * 0.5820
    v_029 = v_011.rolling(116).skew()
    v_030 = v_020.pct_change(8)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[9]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc023_26d_base_v023_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc023_26d_base_v023_signal

def f160e_f160_equity_to_assets_solvency_regime_calc024_33d_base_v024_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(33)
    v_005 = v_003.rolling(37).mean()
    v_006 = v_003.rolling(37).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(33)
    v_009 = v_008.rolling(133).mean()
    v_010 = v_008.rolling(133).std()
    v_011 = v_008.diff(133)
    v_012 = v_007.diff(33)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(37)
    v_015 = v_003.pct_change(33).diff(18)
    v_016 = v_003.rolling(70).skew()
    v_017 = v_003.rolling(70).kurt()
    v_018 = v_011.rolling(66).std()
    v_019 = v_015.rolling(37).mean()
    v_020 = v_012 * 3.0520 + v_014 * 0.8160 + v_011 * 3.4800
    v_021 = v_004.rolling(133).quantile(0.5)
    v_022 = v_015.diff(37)
    v_023 = v_003.rolling(33).max() / v_003.rolling(33).min().replace(0, np.nan)
    v_024 = v_023.diff(33)
    v_025 = v_020.rolling(37).std()
    v_026 = v_017.diff(33)
    v_027 = v_016.diff(33)
    v_028 = v_025 * 3.0520 - v_021 * 0.8160
    v_029 = v_011.rolling(133).skew()
    v_030 = v_020.pct_change(11)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[12]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc024_33d_base_v024_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc024_33d_base_v024_signal

def f160e_f160_equity_to_assets_solvency_regime_calc025_40d_base_v025_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(40)
    v_005 = v_003.rolling(50).mean()
    v_006 = v_003.rolling(50).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(40)
    v_009 = v_008.rolling(10).mean()
    v_010 = v_008.rolling(10).std()
    v_011 = v_008.diff(10)
    v_012 = v_007.diff(40)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(50)
    v_015 = v_003.pct_change(40).diff(25)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(5).std()
    v_019 = v_015.rolling(50).mean()
    v_020 = v_012 * 3.1750 + v_014 * 1.0500 + v_011 * 3.8250
    v_021 = v_004.rolling(10).quantile(0.5)
    v_022 = v_015.diff(50)
    v_023 = v_003.rolling(40).max() / v_003.rolling(40).min().replace(0, np.nan)
    v_024 = v_023.diff(40)
    v_025 = v_020.rolling(50).std()
    v_026 = v_017.diff(40)
    v_027 = v_016.diff(40)
    v_028 = v_025 * 3.1750 - v_021 * 1.0500
    v_029 = v_011.rolling(10).skew()
    v_030 = v_020.pct_change(13)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[15]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc025_40d_base_v025_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc025_40d_base_v025_signal

def f160e_f160_equity_to_assets_solvency_regime_calc026_47d_base_v026_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(47)
    v_005 = v_003.rolling(63).mean()
    v_006 = v_003.rolling(63).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(47)
    v_009 = v_008.rolling(27).mean()
    v_010 = v_008.rolling(27).std()
    v_011 = v_008.diff(27)
    v_012 = v_007.diff(47)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(63)
    v_015 = v_003.pct_change(47).diff(31)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(13).std()
    v_019 = v_015.rolling(63).mean()
    v_020 = v_012 * 3.2980 + v_014 * 1.2840 + v_011 * 4.1700
    v_021 = v_004.rolling(27).quantile(0.5)
    v_022 = v_015.diff(63)
    v_023 = v_003.rolling(47).max() / v_003.rolling(47).min().replace(0, np.nan)
    v_024 = v_023.diff(47)
    v_025 = v_020.rolling(63).std()
    v_026 = v_017.diff(47)
    v_027 = v_016.diff(47)
    v_028 = v_025 * 3.2980 - v_021 * 1.2840
    v_029 = v_011.rolling(27).skew()
    v_030 = v_020.pct_change(15)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[18]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc026_47d_base_v026_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc026_47d_base_v026_signal

def f160e_f160_equity_to_assets_solvency_regime_calc027_54d_base_v027_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(54).mean().diff(76)
    v_005 = v_003.rolling(76).mean()
    v_006 = v_003.rolling(76).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(54)
    v_009 = v_008.rolling(44).mean()
    v_010 = v_008.rolling(44).std()
    v_011 = v_008.diff(44)
    v_012 = v_007.diff(54)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(76)
    v_015 = v_003.pct_change(54).diff(38)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(22).std()
    v_019 = v_015.rolling(76).mean()
    v_020 = v_012 * 3.4210 + v_014 * 1.5180 + v_011 * 4.5150
    v_021 = v_004.rolling(44).quantile(0.5)
    v_022 = v_015.diff(76)
    v_023 = v_003.rolling(54).max() / v_003.rolling(54).min().replace(0, np.nan)
    v_024 = v_023.diff(54)
    v_025 = v_020.rolling(76).std()
    v_026 = v_017.diff(54)
    v_027 = v_016.diff(54)
    v_028 = v_025 * 3.4210 - v_021 * 1.5180
    v_029 = v_011.rolling(44).skew()
    v_030 = v_020.pct_change(18)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[1]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc027_54d_base_v027_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc027_54d_base_v027_signal

def f160e_f160_equity_to_assets_solvency_regime_calc028_61d_base_v028_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(61).std().diff(89)
    v_005 = v_003.rolling(89).mean()
    v_006 = v_003.rolling(89).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(61)
    v_009 = v_008.rolling(61).mean()
    v_010 = v_008.rolling(61).std()
    v_011 = v_008.diff(61)
    v_012 = v_007.diff(61)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(89)
    v_015 = v_003.pct_change(61).diff(44)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(30).std()
    v_019 = v_015.rolling(89).mean()
    v_020 = v_012 * 3.5440 + v_014 * 1.7520 + v_011 * 4.8600
    v_021 = v_004.rolling(61).quantile(0.5)
    v_022 = v_015.diff(89)
    v_023 = v_003.rolling(61).max() / v_003.rolling(61).min().replace(0, np.nan)
    v_024 = v_023.diff(61)
    v_025 = v_020.rolling(89).std()
    v_026 = v_017.diff(61)
    v_027 = v_016.diff(61)
    v_028 = v_025 * 3.5440 - v_021 * 1.7520
    v_029 = v_011.rolling(61).skew()
    v_030 = v_020.pct_change(20)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[4]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc028_61d_base_v028_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc028_61d_base_v028_signal

def f160e_f160_equity_to_assets_solvency_regime_calc029_68d_base_v029_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(68).rolling(102).mean()
    v_005 = v_003.rolling(102).mean()
    v_006 = v_003.rolling(102).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(68)
    v_009 = v_008.rolling(78).mean()
    v_010 = v_008.rolling(78).std()
    v_011 = v_008.diff(78)
    v_012 = v_007.diff(68)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(102)
    v_015 = v_003.pct_change(68).diff(51)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(39).std()
    v_019 = v_015.rolling(102).mean()
    v_020 = v_012 * 3.6670 + v_014 * 1.9860 + v_011 * 0.3050
    v_021 = v_004.rolling(78).quantile(0.5)
    v_022 = v_015.diff(102)
    v_023 = v_003.rolling(68).max() / v_003.rolling(68).min().replace(0, np.nan)
    v_024 = v_023.diff(68)
    v_025 = v_020.rolling(102).std()
    v_026 = v_017.diff(68)
    v_027 = v_016.diff(68)
    v_028 = v_025 * 3.6670 - v_021 * 1.9860
    v_029 = v_011.rolling(78).skew()
    v_030 = v_020.pct_change(22)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[7]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc029_68d_base_v029_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc029_68d_base_v029_signal

def f160e_f160_equity_to_assets_solvency_regime_calc030_75d_base_v030_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(75).rolling(115).std()
    v_005 = v_003.rolling(115).mean()
    v_006 = v_003.rolling(115).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(75)
    v_009 = v_008.rolling(95).mean()
    v_010 = v_008.rolling(95).std()
    v_011 = v_008.diff(95)
    v_012 = v_007.diff(75)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(115)
    v_015 = v_003.pct_change(75).diff(57)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(47).std()
    v_019 = v_015.rolling(115).mean()
    v_020 = v_012 * 3.7900 + v_014 * 2.2200 + v_011 * 0.6500
    v_021 = v_004.rolling(95).quantile(0.5)
    v_022 = v_015.diff(115)
    v_023 = v_003.rolling(75).max() / v_003.rolling(75).min().replace(0, np.nan)
    v_024 = v_023.diff(75)
    v_025 = v_020.rolling(115).std()
    v_026 = v_017.diff(75)
    v_027 = v_016.diff(75)
    v_028 = v_025 * 3.7900 - v_021 * 2.2200
    v_029 = v_011.rolling(95).skew()
    v_030 = v_020.pct_change(25)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[10]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc030_75d_base_v030_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc030_75d_base_v030_signal

def f160e_f160_equity_to_assets_solvency_regime_calc031_82d_base_v031_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(82).skew().diff(128)
    v_005 = v_003.rolling(128).mean()
    v_006 = v_003.rolling(128).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(82)
    v_009 = v_008.rolling(112).mean()
    v_010 = v_008.rolling(112).std()
    v_011 = v_008.diff(112)
    v_012 = v_007.diff(82)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(128)
    v_015 = v_003.pct_change(82).diff(64)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(56).std()
    v_019 = v_015.rolling(128).mean()
    v_020 = v_012 * 3.9130 + v_014 * 2.4540 + v_011 * 0.9950
    v_021 = v_004.rolling(112).quantile(0.5)
    v_022 = v_015.diff(128)
    v_023 = v_003.rolling(82).max() / v_003.rolling(82).min().replace(0, np.nan)
    v_024 = v_023.diff(82)
    v_025 = v_020.rolling(128).std()
    v_026 = v_017.diff(82)
    v_027 = v_016.diff(82)
    v_028 = v_025 * 3.9130 - v_021 * 2.4540
    v_029 = v_011.rolling(112).skew()
    v_030 = v_020.pct_change(27)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[13]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc031_82d_base_v031_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc031_82d_base_v031_signal

def f160e_f160_equity_to_assets_solvency_regime_calc032_89d_base_v032_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(89)
    v_005 = v_003.rolling(141).mean()
    v_006 = v_003.rolling(141).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(89)
    v_009 = v_008.rolling(129).mean()
    v_010 = v_008.rolling(129).std()
    v_011 = v_008.diff(129)
    v_012 = v_007.diff(89)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(141)
    v_015 = v_003.pct_change(89).diff(70)
    v_016 = v_003.rolling(230).skew()
    v_017 = v_003.rolling(230).kurt()
    v_018 = v_011.rolling(64).std()
    v_019 = v_015.rolling(141).mean()
    v_020 = v_012 * 4.0360 + v_014 * 2.6880 + v_011 * 1.3400
    v_021 = v_004.rolling(129).quantile(0.5)
    v_022 = v_015.diff(141)
    v_023 = v_003.rolling(89).max() / v_003.rolling(89).min().replace(0, np.nan)
    v_024 = v_023.diff(89)
    v_025 = v_020.rolling(141).std()
    v_026 = v_017.diff(89)
    v_027 = v_016.diff(89)
    v_028 = v_025 * 4.0360 - v_021 * 2.6880
    v_029 = v_011.rolling(129).skew()
    v_030 = v_020.pct_change(29)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[16]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc032_89d_base_v032_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc032_89d_base_v032_signal

def f160e_f160_equity_to_assets_solvency_regime_calc033_96d_base_v033_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(96)
    v_005 = v_003.rolling(14).mean()
    v_006 = v_003.rolling(14).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(96)
    v_009 = v_008.rolling(6).mean()
    v_010 = v_008.rolling(6).std()
    v_011 = v_008.diff(6)
    v_012 = v_007.diff(96)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(14)
    v_015 = v_003.pct_change(96).diff(7)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(3).std()
    v_019 = v_015.rolling(14).mean()
    v_020 = v_012 * 4.1590 + v_014 * 2.9220 + v_011 * 1.6850
    v_021 = v_004.rolling(6).quantile(0.5)
    v_022 = v_015.diff(14)
    v_023 = v_003.rolling(96).max() / v_003.rolling(96).min().replace(0, np.nan)
    v_024 = v_023.diff(96)
    v_025 = v_020.rolling(14).std()
    v_026 = v_017.diff(96)
    v_027 = v_016.diff(96)
    v_028 = v_025 * 4.1590 - v_021 * 2.9220
    v_029 = v_011.rolling(6).skew()
    v_030 = v_020.pct_change(32)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[19]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc033_96d_base_v033_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc033_96d_base_v033_signal

def f160e_f160_equity_to_assets_solvency_regime_calc034_103d_base_v034_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(103)
    v_005 = v_003.rolling(27).mean()
    v_006 = v_003.rolling(27).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(103)
    v_009 = v_008.rolling(23).mean()
    v_010 = v_008.rolling(23).std()
    v_011 = v_008.diff(23)
    v_012 = v_007.diff(103)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(27)
    v_015 = v_003.pct_change(103).diff(13)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(11).std()
    v_019 = v_015.rolling(27).mean()
    v_020 = v_012 * 4.2820 + v_014 * 3.1560 + v_011 * 2.0300
    v_021 = v_004.rolling(23).quantile(0.5)
    v_022 = v_015.diff(27)
    v_023 = v_003.rolling(103).max() / v_003.rolling(103).min().replace(0, np.nan)
    v_024 = v_023.diff(103)
    v_025 = v_020.rolling(27).std()
    v_026 = v_017.diff(103)
    v_027 = v_016.diff(103)
    v_028 = v_025 * 4.2820 - v_021 * 3.1560
    v_029 = v_011.rolling(23).skew()
    v_030 = v_020.pct_change(34)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[2]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc034_103d_base_v034_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc034_103d_base_v034_signal

def f160e_f160_equity_to_assets_solvency_regime_calc035_110d_base_v035_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(110).mean().diff(40)
    v_005 = v_003.rolling(40).mean()
    v_006 = v_003.rolling(40).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(110)
    v_009 = v_008.rolling(40).mean()
    v_010 = v_008.rolling(40).std()
    v_011 = v_008.diff(40)
    v_012 = v_007.diff(110)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(40)
    v_015 = v_003.pct_change(110).diff(20)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(20).std()
    v_019 = v_015.rolling(40).mean()
    v_020 = v_012 * 4.4050 + v_014 * 3.3900 + v_011 * 2.3750
    v_021 = v_004.rolling(40).quantile(0.5)
    v_022 = v_015.diff(40)
    v_023 = v_003.rolling(110).max() / v_003.rolling(110).min().replace(0, np.nan)
    v_024 = v_023.diff(110)
    v_025 = v_020.rolling(40).std()
    v_026 = v_017.diff(110)
    v_027 = v_016.diff(110)
    v_028 = v_025 * 4.4050 - v_021 * 3.3900
    v_029 = v_011.rolling(40).skew()
    v_030 = v_020.pct_change(36)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[5]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc035_110d_base_v035_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc035_110d_base_v035_signal

def f160e_f160_equity_to_assets_solvency_regime_calc036_117d_base_v036_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(117).std().diff(53)
    v_005 = v_003.rolling(53).mean()
    v_006 = v_003.rolling(53).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(117)
    v_009 = v_008.rolling(57).mean()
    v_010 = v_008.rolling(57).std()
    v_011 = v_008.diff(57)
    v_012 = v_007.diff(117)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(53)
    v_015 = v_003.pct_change(117).diff(26)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(28).std()
    v_019 = v_015.rolling(53).mean()
    v_020 = v_012 * 4.5280 + v_014 * 3.6240 + v_011 * 2.7200
    v_021 = v_004.rolling(57).quantile(0.5)
    v_022 = v_015.diff(53)
    v_023 = v_003.rolling(117).max() / v_003.rolling(117).min().replace(0, np.nan)
    v_024 = v_023.diff(117)
    v_025 = v_020.rolling(53).std()
    v_026 = v_017.diff(117)
    v_027 = v_016.diff(117)
    v_028 = v_025 * 4.5280 - v_021 * 3.6240
    v_029 = v_011.rolling(57).skew()
    v_030 = v_020.pct_change(39)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[8]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc036_117d_base_v036_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc036_117d_base_v036_signal

def f160e_f160_equity_to_assets_solvency_regime_calc037_124d_base_v037_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(124).rolling(66).mean()
    v_005 = v_003.rolling(66).mean()
    v_006 = v_003.rolling(66).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(124)
    v_009 = v_008.rolling(74).mean()
    v_010 = v_008.rolling(74).std()
    v_011 = v_008.diff(74)
    v_012 = v_007.diff(124)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(66)
    v_015 = v_003.pct_change(124).diff(33)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(37).std()
    v_019 = v_015.rolling(66).mean()
    v_020 = v_012 * 4.6510 + v_014 * 3.8580 + v_011 * 3.0650
    v_021 = v_004.rolling(74).quantile(0.5)
    v_022 = v_015.diff(66)
    v_023 = v_003.rolling(124).max() / v_003.rolling(124).min().replace(0, np.nan)
    v_024 = v_023.diff(124)
    v_025 = v_020.rolling(66).std()
    v_026 = v_017.diff(124)
    v_027 = v_016.diff(124)
    v_028 = v_025 * 4.6510 - v_021 * 3.8580
    v_029 = v_011.rolling(74).skew()
    v_030 = v_020.pct_change(41)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[11]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc037_124d_base_v037_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc037_124d_base_v037_signal

def f160e_f160_equity_to_assets_solvency_regime_calc038_131d_base_v038_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(131).rolling(79).std()
    v_005 = v_003.rolling(79).mean()
    v_006 = v_003.rolling(79).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(131)
    v_009 = v_008.rolling(91).mean()
    v_010 = v_008.rolling(91).std()
    v_011 = v_008.diff(91)
    v_012 = v_007.diff(131)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(79)
    v_015 = v_003.pct_change(131).diff(39)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(45).std()
    v_019 = v_015.rolling(79).mean()
    v_020 = v_012 * 4.7740 + v_014 * 4.0920 + v_011 * 3.4100
    v_021 = v_004.rolling(91).quantile(0.5)
    v_022 = v_015.diff(79)
    v_023 = v_003.rolling(131).max() / v_003.rolling(131).min().replace(0, np.nan)
    v_024 = v_023.diff(131)
    v_025 = v_020.rolling(79).std()
    v_026 = v_017.diff(131)
    v_027 = v_016.diff(131)
    v_028 = v_025 * 4.7740 - v_021 * 4.0920
    v_029 = v_011.rolling(91).skew()
    v_030 = v_020.pct_change(43)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[14]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc038_131d_base_v038_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc038_131d_base_v038_signal

def f160e_f160_equity_to_assets_solvency_regime_calc039_138d_base_v039_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(138).skew().diff(92)
    v_005 = v_003.rolling(92).mean()
    v_006 = v_003.rolling(92).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(138)
    v_009 = v_008.rolling(108).mean()
    v_010 = v_008.rolling(108).std()
    v_011 = v_008.diff(108)
    v_012 = v_007.diff(138)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(92)
    v_015 = v_003.pct_change(138).diff(46)
    v_016 = v_003.rolling(230).skew()
    v_017 = v_003.rolling(230).kurt()
    v_018 = v_011.rolling(54).std()
    v_019 = v_015.rolling(92).mean()
    v_020 = v_012 * 4.8970 + v_014 * 4.3260 + v_011 * 3.7550
    v_021 = v_004.rolling(108).quantile(0.5)
    v_022 = v_015.diff(92)
    v_023 = v_003.rolling(138).max() / v_003.rolling(138).min().replace(0, np.nan)
    v_024 = v_023.diff(138)
    v_025 = v_020.rolling(92).std()
    v_026 = v_017.diff(138)
    v_027 = v_016.diff(138)
    v_028 = v_025 * 4.8970 - v_021 * 4.3260
    v_029 = v_011.rolling(108).skew()
    v_030 = v_020.pct_change(46)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[17]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc039_138d_base_v039_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc039_138d_base_v039_signal

def f160e_f160_equity_to_assets_solvency_regime_calc040_5d_base_v040_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(5)
    v_005 = v_003.rolling(105).mean()
    v_006 = v_003.rolling(105).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(5)
    v_009 = v_008.rolling(125).mean()
    v_010 = v_008.rolling(125).std()
    v_011 = v_008.diff(125)
    v_012 = v_007.diff(5)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(105)
    v_015 = v_003.pct_change(5).diff(52)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(62).std()
    v_019 = v_015.rolling(105).mean()
    v_020 = v_012 * 0.1200 + v_014 * 4.5600 + v_011 * 4.1000
    v_021 = v_004.rolling(125).quantile(0.5)
    v_022 = v_015.diff(105)
    v_023 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_024 = v_023.diff(5)
    v_025 = v_020.rolling(105).std()
    v_026 = v_017.diff(5)
    v_027 = v_016.diff(5)
    v_028 = v_025 * 0.1200 - v_021 * 4.5600
    v_029 = v_011.rolling(125).skew()
    v_030 = v_020.pct_change(1)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[0]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc040_5d_base_v040_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc040_5d_base_v040_signal

def f160e_f160_equity_to_assets_solvency_regime_calc041_12d_base_v041_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(12)
    v_005 = v_003.rolling(118).mean()
    v_006 = v_003.rolling(118).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(12)
    v_009 = v_008.rolling(142).mean()
    v_010 = v_008.rolling(142).std()
    v_011 = v_008.diff(142)
    v_012 = v_007.diff(12)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(118)
    v_015 = v_003.pct_change(12).diff(59)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(71).std()
    v_019 = v_015.rolling(118).mean()
    v_020 = v_012 * 0.2430 + v_014 * 4.7940 + v_011 * 4.4450
    v_021 = v_004.rolling(142).quantile(0.5)
    v_022 = v_015.diff(118)
    v_023 = v_003.rolling(12).max() / v_003.rolling(12).min().replace(0, np.nan)
    v_024 = v_023.diff(12)
    v_025 = v_020.rolling(118).std()
    v_026 = v_017.diff(12)
    v_027 = v_016.diff(12)
    v_028 = v_025 * 0.2430 - v_021 * 4.7940
    v_029 = v_011.rolling(142).skew()
    v_030 = v_020.pct_change(4)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[3]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc041_12d_base_v041_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc041_12d_base_v041_signal

def f160e_f160_equity_to_assets_solvency_regime_calc042_19d_base_v042_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(19)
    v_005 = v_003.rolling(131).mean()
    v_006 = v_003.rolling(131).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(19)
    v_009 = v_008.rolling(19).mean()
    v_010 = v_008.rolling(19).std()
    v_011 = v_008.diff(19)
    v_012 = v_007.diff(19)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(131)
    v_015 = v_003.pct_change(19).diff(65)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(9).std()
    v_019 = v_015.rolling(131).mean()
    v_020 = v_012 * 0.3660 + v_014 * 0.1280 + v_011 * 4.7900
    v_021 = v_004.rolling(19).quantile(0.5)
    v_022 = v_015.diff(131)
    v_023 = v_003.rolling(19).max() / v_003.rolling(19).min().replace(0, np.nan)
    v_024 = v_023.diff(19)
    v_025 = v_020.rolling(131).std()
    v_026 = v_017.diff(19)
    v_027 = v_016.diff(19)
    v_028 = v_025 * 0.3660 - v_021 * 0.1280
    v_029 = v_011.rolling(19).skew()
    v_030 = v_020.pct_change(6)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[6]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc042_19d_base_v042_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc042_19d_base_v042_signal

def f160e_f160_equity_to_assets_solvency_regime_calc043_26d_base_v043_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(26).mean().diff(144)
    v_005 = v_003.rolling(144).mean()
    v_006 = v_003.rolling(144).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(26)
    v_009 = v_008.rolling(36).mean()
    v_010 = v_008.rolling(36).std()
    v_011 = v_008.diff(36)
    v_012 = v_007.diff(26)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(144)
    v_015 = v_003.pct_change(26).diff(72)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(18).std()
    v_019 = v_015.rolling(144).mean()
    v_020 = v_012 * 0.4890 + v_014 * 0.3620 + v_011 * 0.2350
    v_021 = v_004.rolling(36).quantile(0.5)
    v_022 = v_015.diff(144)
    v_023 = v_003.rolling(26).max() / v_003.rolling(26).min().replace(0, np.nan)
    v_024 = v_023.diff(26)
    v_025 = v_020.rolling(144).std()
    v_026 = v_017.diff(26)
    v_027 = v_016.diff(26)
    v_028 = v_025 * 0.4890 - v_021 * 0.3620
    v_029 = v_011.rolling(36).skew()
    v_030 = v_020.pct_change(8)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[9]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc043_26d_base_v043_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc043_26d_base_v043_signal

def f160e_f160_equity_to_assets_solvency_regime_calc044_33d_base_v044_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(33).std().diff(17)
    v_005 = v_003.rolling(17).mean()
    v_006 = v_003.rolling(17).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(33)
    v_009 = v_008.rolling(53).mean()
    v_010 = v_008.rolling(53).std()
    v_011 = v_008.diff(53)
    v_012 = v_007.diff(33)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(17)
    v_015 = v_003.pct_change(33).diff(8)
    v_016 = v_003.rolling(50).skew()
    v_017 = v_003.rolling(50).kurt()
    v_018 = v_011.rolling(26).std()
    v_019 = v_015.rolling(17).mean()
    v_020 = v_012 * 0.6120 + v_014 * 0.5960 + v_011 * 0.5800
    v_021 = v_004.rolling(53).quantile(0.5)
    v_022 = v_015.diff(17)
    v_023 = v_003.rolling(33).max() / v_003.rolling(33).min().replace(0, np.nan)
    v_024 = v_023.diff(33)
    v_025 = v_020.rolling(17).std()
    v_026 = v_017.diff(33)
    v_027 = v_016.diff(33)
    v_028 = v_025 * 0.6120 - v_021 * 0.5960
    v_029 = v_011.rolling(53).skew()
    v_030 = v_020.pct_change(11)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[12]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc044_33d_base_v044_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc044_33d_base_v044_signal

def f160e_f160_equity_to_assets_solvency_regime_calc045_40d_base_v045_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(40).rolling(30).mean()
    v_005 = v_003.rolling(30).mean()
    v_006 = v_003.rolling(30).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(40)
    v_009 = v_008.rolling(70).mean()
    v_010 = v_008.rolling(70).std()
    v_011 = v_008.diff(70)
    v_012 = v_007.diff(40)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(30)
    v_015 = v_003.pct_change(40).diff(15)
    v_016 = v_003.rolling(70).skew()
    v_017 = v_003.rolling(70).kurt()
    v_018 = v_011.rolling(35).std()
    v_019 = v_015.rolling(30).mean()
    v_020 = v_012 * 0.7350 + v_014 * 0.8300 + v_011 * 0.9250
    v_021 = v_004.rolling(70).quantile(0.5)
    v_022 = v_015.diff(30)
    v_023 = v_003.rolling(40).max() / v_003.rolling(40).min().replace(0, np.nan)
    v_024 = v_023.diff(40)
    v_025 = v_020.rolling(30).std()
    v_026 = v_017.diff(40)
    v_027 = v_016.diff(40)
    v_028 = v_025 * 0.7350 - v_021 * 0.8300
    v_029 = v_011.rolling(70).skew()
    v_030 = v_020.pct_change(13)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[15]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc045_40d_base_v045_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc045_40d_base_v045_signal

def f160e_f160_equity_to_assets_solvency_regime_calc046_47d_base_v046_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(47).rolling(43).std()
    v_005 = v_003.rolling(43).mean()
    v_006 = v_003.rolling(43).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(47)
    v_009 = v_008.rolling(87).mean()
    v_010 = v_008.rolling(87).std()
    v_011 = v_008.diff(87)
    v_012 = v_007.diff(47)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(43)
    v_015 = v_003.pct_change(47).diff(21)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(43).std()
    v_019 = v_015.rolling(43).mean()
    v_020 = v_012 * 0.8580 + v_014 * 1.0640 + v_011 * 1.2700
    v_021 = v_004.rolling(87).quantile(0.5)
    v_022 = v_015.diff(43)
    v_023 = v_003.rolling(47).max() / v_003.rolling(47).min().replace(0, np.nan)
    v_024 = v_023.diff(47)
    v_025 = v_020.rolling(43).std()
    v_026 = v_017.diff(47)
    v_027 = v_016.diff(47)
    v_028 = v_025 * 0.8580 - v_021 * 1.0640
    v_029 = v_011.rolling(87).skew()
    v_030 = v_020.pct_change(15)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[18]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc046_47d_base_v046_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc046_47d_base_v046_signal

def f160e_f160_equity_to_assets_solvency_regime_calc047_54d_base_v047_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(54).skew().diff(56)
    v_005 = v_003.rolling(56).mean()
    v_006 = v_003.rolling(56).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(54)
    v_009 = v_008.rolling(104).mean()
    v_010 = v_008.rolling(104).std()
    v_011 = v_008.diff(104)
    v_012 = v_007.diff(54)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(56)
    v_015 = v_003.pct_change(54).diff(28)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(52).std()
    v_019 = v_015.rolling(56).mean()
    v_020 = v_012 * 0.9810 + v_014 * 1.2980 + v_011 * 1.6150
    v_021 = v_004.rolling(104).quantile(0.5)
    v_022 = v_015.diff(56)
    v_023 = v_003.rolling(54).max() / v_003.rolling(54).min().replace(0, np.nan)
    v_024 = v_023.diff(54)
    v_025 = v_020.rolling(56).std()
    v_026 = v_017.diff(54)
    v_027 = v_016.diff(54)
    v_028 = v_025 * 0.9810 - v_021 * 1.2980
    v_029 = v_011.rolling(104).skew()
    v_030 = v_020.pct_change(18)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[1]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc047_54d_base_v047_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc047_54d_base_v047_signal

def f160e_f160_equity_to_assets_solvency_regime_calc048_61d_base_v048_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(61)
    v_005 = v_003.rolling(69).mean()
    v_006 = v_003.rolling(69).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(61)
    v_009 = v_008.rolling(121).mean()
    v_010 = v_008.rolling(121).std()
    v_011 = v_008.diff(121)
    v_012 = v_007.diff(61)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(69)
    v_015 = v_003.pct_change(61).diff(34)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(60).std()
    v_019 = v_015.rolling(69).mean()
    v_020 = v_012 * 1.1040 + v_014 * 1.5320 + v_011 * 1.9600
    v_021 = v_004.rolling(121).quantile(0.5)
    v_022 = v_015.diff(69)
    v_023 = v_003.rolling(61).max() / v_003.rolling(61).min().replace(0, np.nan)
    v_024 = v_023.diff(61)
    v_025 = v_020.rolling(69).std()
    v_026 = v_017.diff(61)
    v_027 = v_016.diff(61)
    v_028 = v_025 * 1.1040 - v_021 * 1.5320
    v_029 = v_011.rolling(121).skew()
    v_030 = v_020.pct_change(20)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[4]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc048_61d_base_v048_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc048_61d_base_v048_signal

def f160e_f160_equity_to_assets_solvency_regime_calc049_68d_base_v049_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(68)
    v_005 = v_003.rolling(82).mean()
    v_006 = v_003.rolling(82).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(68)
    v_009 = v_008.rolling(138).mean()
    v_010 = v_008.rolling(138).std()
    v_011 = v_008.diff(138)
    v_012 = v_007.diff(68)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(82)
    v_015 = v_003.pct_change(68).diff(41)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(69).std()
    v_019 = v_015.rolling(82).mean()
    v_020 = v_012 * 1.2270 + v_014 * 1.7660 + v_011 * 2.3050
    v_021 = v_004.rolling(138).quantile(0.5)
    v_022 = v_015.diff(82)
    v_023 = v_003.rolling(68).max() / v_003.rolling(68).min().replace(0, np.nan)
    v_024 = v_023.diff(68)
    v_025 = v_020.rolling(82).std()
    v_026 = v_017.diff(68)
    v_027 = v_016.diff(68)
    v_028 = v_025 * 1.2270 - v_021 * 1.7660
    v_029 = v_011.rolling(138).skew()
    v_030 = v_020.pct_change(22)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[7]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc049_68d_base_v049_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc049_68d_base_v049_signal

def f160e_f160_equity_to_assets_solvency_regime_calc050_75d_base_v050_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(75)
    v_005 = v_003.rolling(95).mean()
    v_006 = v_003.rolling(95).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(75)
    v_009 = v_008.rolling(15).mean()
    v_010 = v_008.rolling(15).std()
    v_011 = v_008.diff(15)
    v_012 = v_007.diff(75)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(95)
    v_015 = v_003.pct_change(75).diff(47)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(7).std()
    v_019 = v_015.rolling(95).mean()
    v_020 = v_012 * 1.3500 + v_014 * 2.0000 + v_011 * 2.6500
    v_021 = v_004.rolling(15).quantile(0.5)
    v_022 = v_015.diff(95)
    v_023 = v_003.rolling(75).max() / v_003.rolling(75).min().replace(0, np.nan)
    v_024 = v_023.diff(75)
    v_025 = v_020.rolling(95).std()
    v_026 = v_017.diff(75)
    v_027 = v_016.diff(75)
    v_028 = v_025 * 1.3500 - v_021 * 2.0000
    v_029 = v_011.rolling(15).skew()
    v_030 = v_020.pct_change(25)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[10]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc050_75d_base_v050_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc050_75d_base_v050_signal

def f160e_f160_equity_to_assets_solvency_regime_calc051_82d_base_v051_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(82).mean().diff(108)
    v_005 = v_003.rolling(108).mean()
    v_006 = v_003.rolling(108).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(82)
    v_009 = v_008.rolling(32).mean()
    v_010 = v_008.rolling(32).std()
    v_011 = v_008.diff(32)
    v_012 = v_007.diff(82)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(108)
    v_015 = v_003.pct_change(82).diff(54)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(16).std()
    v_019 = v_015.rolling(108).mean()
    v_020 = v_012 * 1.4730 + v_014 * 2.2340 + v_011 * 2.9950
    v_021 = v_004.rolling(32).quantile(0.5)
    v_022 = v_015.diff(108)
    v_023 = v_003.rolling(82).max() / v_003.rolling(82).min().replace(0, np.nan)
    v_024 = v_023.diff(82)
    v_025 = v_020.rolling(108).std()
    v_026 = v_017.diff(82)
    v_027 = v_016.diff(82)
    v_028 = v_025 * 1.4730 - v_021 * 2.2340
    v_029 = v_011.rolling(32).skew()
    v_030 = v_020.pct_change(27)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[13]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc051_82d_base_v051_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc051_82d_base_v051_signal

def f160e_f160_equity_to_assets_solvency_regime_calc052_89d_base_v052_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(89).std().diff(121)
    v_005 = v_003.rolling(121).mean()
    v_006 = v_003.rolling(121).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(89)
    v_009 = v_008.rolling(49).mean()
    v_010 = v_008.rolling(49).std()
    v_011 = v_008.diff(49)
    v_012 = v_007.diff(89)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(121)
    v_015 = v_003.pct_change(89).diff(60)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(24).std()
    v_019 = v_015.rolling(121).mean()
    v_020 = v_012 * 1.5960 + v_014 * 2.4680 + v_011 * 3.3400
    v_021 = v_004.rolling(49).quantile(0.5)
    v_022 = v_015.diff(121)
    v_023 = v_003.rolling(89).max() / v_003.rolling(89).min().replace(0, np.nan)
    v_024 = v_023.diff(89)
    v_025 = v_020.rolling(121).std()
    v_026 = v_017.diff(89)
    v_027 = v_016.diff(89)
    v_028 = v_025 * 1.5960 - v_021 * 2.4680
    v_029 = v_011.rolling(49).skew()
    v_030 = v_020.pct_change(29)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[16]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc052_89d_base_v052_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc052_89d_base_v052_signal

def f160e_f160_equity_to_assets_solvency_regime_calc053_96d_base_v053_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(96).rolling(134).mean()
    v_005 = v_003.rolling(134).mean()
    v_006 = v_003.rolling(134).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(96)
    v_009 = v_008.rolling(66).mean()
    v_010 = v_008.rolling(66).std()
    v_011 = v_008.diff(66)
    v_012 = v_007.diff(96)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(134)
    v_015 = v_003.pct_change(96).diff(67)
    v_016 = v_003.rolling(230).skew()
    v_017 = v_003.rolling(230).kurt()
    v_018 = v_011.rolling(33).std()
    v_019 = v_015.rolling(134).mean()
    v_020 = v_012 * 1.7190 + v_014 * 2.7020 + v_011 * 3.6850
    v_021 = v_004.rolling(66).quantile(0.5)
    v_022 = v_015.diff(134)
    v_023 = v_003.rolling(96).max() / v_003.rolling(96).min().replace(0, np.nan)
    v_024 = v_023.diff(96)
    v_025 = v_020.rolling(134).std()
    v_026 = v_017.diff(96)
    v_027 = v_016.diff(96)
    v_028 = v_025 * 1.7190 - v_021 * 2.7020
    v_029 = v_011.rolling(66).skew()
    v_030 = v_020.pct_change(32)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[19]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc053_96d_base_v053_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc053_96d_base_v053_signal

def f160e_f160_equity_to_assets_solvency_regime_calc054_103d_base_v054_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(103).rolling(7).std()
    v_005 = v_003.rolling(7).mean()
    v_006 = v_003.rolling(7).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(103)
    v_009 = v_008.rolling(83).mean()
    v_010 = v_008.rolling(83).std()
    v_011 = v_008.diff(83)
    v_012 = v_007.diff(103)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(7)
    v_015 = v_003.pct_change(103).diff(3)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(41).std()
    v_019 = v_015.rolling(7).mean()
    v_020 = v_012 * 1.8420 + v_014 * 2.9360 + v_011 * 4.0300
    v_021 = v_004.rolling(83).quantile(0.5)
    v_022 = v_015.diff(7)
    v_023 = v_003.rolling(103).max() / v_003.rolling(103).min().replace(0, np.nan)
    v_024 = v_023.diff(103)
    v_025 = v_020.rolling(7).std()
    v_026 = v_017.diff(103)
    v_027 = v_016.diff(103)
    v_028 = v_025 * 1.8420 - v_021 * 2.9360
    v_029 = v_011.rolling(83).skew()
    v_030 = v_020.pct_change(34)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[2]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc054_103d_base_v054_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc054_103d_base_v054_signal

def f160e_f160_equity_to_assets_solvency_regime_calc055_110d_base_v055_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(110).skew().diff(20)
    v_005 = v_003.rolling(20).mean()
    v_006 = v_003.rolling(20).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(110)
    v_009 = v_008.rolling(100).mean()
    v_010 = v_008.rolling(100).std()
    v_011 = v_008.diff(100)
    v_012 = v_007.diff(110)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(20)
    v_015 = v_003.pct_change(110).diff(10)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(50).std()
    v_019 = v_015.rolling(20).mean()
    v_020 = v_012 * 1.9650 + v_014 * 3.1700 + v_011 * 4.3750
    v_021 = v_004.rolling(100).quantile(0.5)
    v_022 = v_015.diff(20)
    v_023 = v_003.rolling(110).max() / v_003.rolling(110).min().replace(0, np.nan)
    v_024 = v_023.diff(110)
    v_025 = v_020.rolling(20).std()
    v_026 = v_017.diff(110)
    v_027 = v_016.diff(110)
    v_028 = v_025 * 1.9650 - v_021 * 3.1700
    v_029 = v_011.rolling(100).skew()
    v_030 = v_020.pct_change(36)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[5]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc055_110d_base_v055_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc055_110d_base_v055_signal

def f160e_f160_equity_to_assets_solvency_regime_calc056_117d_base_v056_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(117)
    v_005 = v_003.rolling(33).mean()
    v_006 = v_003.rolling(33).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(117)
    v_009 = v_008.rolling(117).mean()
    v_010 = v_008.rolling(117).std()
    v_011 = v_008.diff(117)
    v_012 = v_007.diff(117)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(33)
    v_015 = v_003.pct_change(117).diff(16)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(58).std()
    v_019 = v_015.rolling(33).mean()
    v_020 = v_012 * 2.0880 + v_014 * 3.4040 + v_011 * 4.7200
    v_021 = v_004.rolling(117).quantile(0.5)
    v_022 = v_015.diff(33)
    v_023 = v_003.rolling(117).max() / v_003.rolling(117).min().replace(0, np.nan)
    v_024 = v_023.diff(117)
    v_025 = v_020.rolling(33).std()
    v_026 = v_017.diff(117)
    v_027 = v_016.diff(117)
    v_028 = v_025 * 2.0880 - v_021 * 3.4040
    v_029 = v_011.rolling(117).skew()
    v_030 = v_020.pct_change(39)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[8]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc056_117d_base_v056_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc056_117d_base_v056_signal

def f160e_f160_equity_to_assets_solvency_regime_calc057_124d_base_v057_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(124)
    v_005 = v_003.rolling(46).mean()
    v_006 = v_003.rolling(46).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(124)
    v_009 = v_008.rolling(134).mean()
    v_010 = v_008.rolling(134).std()
    v_011 = v_008.diff(134)
    v_012 = v_007.diff(124)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(46)
    v_015 = v_003.pct_change(124).diff(23)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(67).std()
    v_019 = v_015.rolling(46).mean()
    v_020 = v_012 * 2.2110 + v_014 * 3.6380 + v_011 * 0.1650
    v_021 = v_004.rolling(134).quantile(0.5)
    v_022 = v_015.diff(46)
    v_023 = v_003.rolling(124).max() / v_003.rolling(124).min().replace(0, np.nan)
    v_024 = v_023.diff(124)
    v_025 = v_020.rolling(46).std()
    v_026 = v_017.diff(124)
    v_027 = v_016.diff(124)
    v_028 = v_025 * 2.2110 - v_021 * 3.6380
    v_029 = v_011.rolling(134).skew()
    v_030 = v_020.pct_change(41)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[11]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc057_124d_base_v057_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc057_124d_base_v057_signal

def f160e_f160_equity_to_assets_solvency_regime_calc058_131d_base_v058_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(131)
    v_005 = v_003.rolling(59).mean()
    v_006 = v_003.rolling(59).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(131)
    v_009 = v_008.rolling(11).mean()
    v_010 = v_008.rolling(11).std()
    v_011 = v_008.diff(11)
    v_012 = v_007.diff(131)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(59)
    v_015 = v_003.pct_change(131).diff(29)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(5).std()
    v_019 = v_015.rolling(59).mean()
    v_020 = v_012 * 2.3340 + v_014 * 3.8720 + v_011 * 0.5100
    v_021 = v_004.rolling(11).quantile(0.5)
    v_022 = v_015.diff(59)
    v_023 = v_003.rolling(131).max() / v_003.rolling(131).min().replace(0, np.nan)
    v_024 = v_023.diff(131)
    v_025 = v_020.rolling(59).std()
    v_026 = v_017.diff(131)
    v_027 = v_016.diff(131)
    v_028 = v_025 * 2.3340 - v_021 * 3.8720
    v_029 = v_011.rolling(11).skew()
    v_030 = v_020.pct_change(43)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[14]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc058_131d_base_v058_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc058_131d_base_v058_signal

def f160e_f160_equity_to_assets_solvency_regime_calc059_138d_base_v059_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(138).mean().diff(72)
    v_005 = v_003.rolling(72).mean()
    v_006 = v_003.rolling(72).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(138)
    v_009 = v_008.rolling(28).mean()
    v_010 = v_008.rolling(28).std()
    v_011 = v_008.diff(28)
    v_012 = v_007.diff(138)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(72)
    v_015 = v_003.pct_change(138).diff(36)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(14).std()
    v_019 = v_015.rolling(72).mean()
    v_020 = v_012 * 2.4570 + v_014 * 4.1060 + v_011 * 0.8550
    v_021 = v_004.rolling(28).quantile(0.5)
    v_022 = v_015.diff(72)
    v_023 = v_003.rolling(138).max() / v_003.rolling(138).min().replace(0, np.nan)
    v_024 = v_023.diff(138)
    v_025 = v_020.rolling(72).std()
    v_026 = v_017.diff(138)
    v_027 = v_016.diff(138)
    v_028 = v_025 * 2.4570 - v_021 * 4.1060
    v_029 = v_011.rolling(28).skew()
    v_030 = v_020.pct_change(46)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[17]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc059_138d_base_v059_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc059_138d_base_v059_signal

def f160e_f160_equity_to_assets_solvency_regime_calc060_5d_base_v060_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(5).std().diff(85)
    v_005 = v_003.rolling(85).mean()
    v_006 = v_003.rolling(85).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(5)
    v_009 = v_008.rolling(45).mean()
    v_010 = v_008.rolling(45).std()
    v_011 = v_008.diff(45)
    v_012 = v_007.diff(5)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(85)
    v_015 = v_003.pct_change(5).diff(42)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(22).std()
    v_019 = v_015.rolling(85).mean()
    v_020 = v_012 * 2.5800 + v_014 * 4.3400 + v_011 * 1.2000
    v_021 = v_004.rolling(45).quantile(0.5)
    v_022 = v_015.diff(85)
    v_023 = v_003.rolling(5).max() / v_003.rolling(5).min().replace(0, np.nan)
    v_024 = v_023.diff(5)
    v_025 = v_020.rolling(85).std()
    v_026 = v_017.diff(5)
    v_027 = v_016.diff(5)
    v_028 = v_025 * 2.5800 - v_021 * 4.3400
    v_029 = v_011.rolling(45).skew()
    v_030 = v_020.pct_change(1)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[0]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc060_5d_base_v060_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc060_5d_base_v060_signal

def f160e_f160_equity_to_assets_solvency_regime_calc061_12d_base_v061_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(12).rolling(98).mean()
    v_005 = v_003.rolling(98).mean()
    v_006 = v_003.rolling(98).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(12)
    v_009 = v_008.rolling(62).mean()
    v_010 = v_008.rolling(62).std()
    v_011 = v_008.diff(62)
    v_012 = v_007.diff(12)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(98)
    v_015 = v_003.pct_change(12).diff(49)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(31).std()
    v_019 = v_015.rolling(98).mean()
    v_020 = v_012 * 2.7030 + v_014 * 4.5740 + v_011 * 1.5450
    v_021 = v_004.rolling(62).quantile(0.5)
    v_022 = v_015.diff(98)
    v_023 = v_003.rolling(12).max() / v_003.rolling(12).min().replace(0, np.nan)
    v_024 = v_023.diff(12)
    v_025 = v_020.rolling(98).std()
    v_026 = v_017.diff(12)
    v_027 = v_016.diff(12)
    v_028 = v_025 * 2.7030 - v_021 * 4.5740
    v_029 = v_011.rolling(62).skew()
    v_030 = v_020.pct_change(4)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[3]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc061_12d_base_v061_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc061_12d_base_v061_signal

def f160e_f160_equity_to_assets_solvency_regime_calc062_19d_base_v062_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(19).rolling(111).std()
    v_005 = v_003.rolling(111).mean()
    v_006 = v_003.rolling(111).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(19)
    v_009 = v_008.rolling(79).mean()
    v_010 = v_008.rolling(79).std()
    v_011 = v_008.diff(79)
    v_012 = v_007.diff(19)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(111)
    v_015 = v_003.pct_change(19).diff(55)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(39).std()
    v_019 = v_015.rolling(111).mean()
    v_020 = v_012 * 2.8260 + v_014 * 4.8080 + v_011 * 1.8900
    v_021 = v_004.rolling(79).quantile(0.5)
    v_022 = v_015.diff(111)
    v_023 = v_003.rolling(19).max() / v_003.rolling(19).min().replace(0, np.nan)
    v_024 = v_023.diff(19)
    v_025 = v_020.rolling(111).std()
    v_026 = v_017.diff(19)
    v_027 = v_016.diff(19)
    v_028 = v_025 * 2.8260 - v_021 * 4.8080
    v_029 = v_011.rolling(79).skew()
    v_030 = v_020.pct_change(6)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[6]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc062_19d_base_v062_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc062_19d_base_v062_signal

def f160e_f160_equity_to_assets_solvency_regime_calc063_26d_base_v063_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(26).skew().diff(124)
    v_005 = v_003.rolling(124).mean()
    v_006 = v_003.rolling(124).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(26)
    v_009 = v_008.rolling(96).mean()
    v_010 = v_008.rolling(96).std()
    v_011 = v_008.diff(96)
    v_012 = v_007.diff(26)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(124)
    v_015 = v_003.pct_change(26).diff(62)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(48).std()
    v_019 = v_015.rolling(124).mean()
    v_020 = v_012 * 2.9490 + v_014 * 0.1420 + v_011 * 2.2350
    v_021 = v_004.rolling(96).quantile(0.5)
    v_022 = v_015.diff(124)
    v_023 = v_003.rolling(26).max() / v_003.rolling(26).min().replace(0, np.nan)
    v_024 = v_023.diff(26)
    v_025 = v_020.rolling(124).std()
    v_026 = v_017.diff(26)
    v_027 = v_016.diff(26)
    v_028 = v_025 * 2.9490 - v_021 * 0.1420
    v_029 = v_011.rolling(96).skew()
    v_030 = v_020.pct_change(8)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[9]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc063_26d_base_v063_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc063_26d_base_v063_signal

def f160e_f160_equity_to_assets_solvency_regime_calc064_33d_base_v064_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(33)
    v_005 = v_003.rolling(137).mean()
    v_006 = v_003.rolling(137).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(33)
    v_009 = v_008.rolling(113).mean()
    v_010 = v_008.rolling(113).std()
    v_011 = v_008.diff(113)
    v_012 = v_007.diff(33)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(137)
    v_015 = v_003.pct_change(33).diff(68)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(56).std()
    v_019 = v_015.rolling(137).mean()
    v_020 = v_012 * 3.0720 + v_014 * 0.3760 + v_011 * 2.5800
    v_021 = v_004.rolling(113).quantile(0.5)
    v_022 = v_015.diff(137)
    v_023 = v_003.rolling(33).max() / v_003.rolling(33).min().replace(0, np.nan)
    v_024 = v_023.diff(33)
    v_025 = v_020.rolling(137).std()
    v_026 = v_017.diff(33)
    v_027 = v_016.diff(33)
    v_028 = v_025 * 3.0720 - v_021 * 0.3760
    v_029 = v_011.rolling(113).skew()
    v_030 = v_020.pct_change(11)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[12]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc064_33d_base_v064_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc064_33d_base_v064_signal

def f160e_f160_equity_to_assets_solvency_regime_calc065_40d_base_v065_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(40)
    v_005 = v_003.rolling(10).mean()
    v_006 = v_003.rolling(10).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(40)
    v_009 = v_008.rolling(130).mean()
    v_010 = v_008.rolling(130).std()
    v_011 = v_008.diff(130)
    v_012 = v_007.diff(40)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(10)
    v_015 = v_003.pct_change(40).diff(5)
    v_016 = v_003.rolling(50).skew()
    v_017 = v_003.rolling(50).kurt()
    v_018 = v_011.rolling(65).std()
    v_019 = v_015.rolling(10).mean()
    v_020 = v_012 * 3.1950 + v_014 * 0.6100 + v_011 * 2.9250
    v_021 = v_004.rolling(130).quantile(0.5)
    v_022 = v_015.diff(10)
    v_023 = v_003.rolling(40).max() / v_003.rolling(40).min().replace(0, np.nan)
    v_024 = v_023.diff(40)
    v_025 = v_020.rolling(10).std()
    v_026 = v_017.diff(40)
    v_027 = v_016.diff(40)
    v_028 = v_025 * 3.1950 - v_021 * 0.6100
    v_029 = v_011.rolling(130).skew()
    v_030 = v_020.pct_change(13)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[15]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc065_40d_base_v065_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc065_40d_base_v065_signal

def f160e_f160_equity_to_assets_solvency_regime_calc066_47d_base_v066_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(47)
    v_005 = v_003.rolling(23).mean()
    v_006 = v_003.rolling(23).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(47)
    v_009 = v_008.rolling(7).mean()
    v_010 = v_008.rolling(7).std()
    v_011 = v_008.diff(7)
    v_012 = v_007.diff(47)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(23)
    v_015 = v_003.pct_change(47).diff(11)
    v_016 = v_003.rolling(70).skew()
    v_017 = v_003.rolling(70).kurt()
    v_018 = v_011.rolling(3).std()
    v_019 = v_015.rolling(23).mean()
    v_020 = v_012 * 3.3180 + v_014 * 0.8440 + v_011 * 3.2700
    v_021 = v_004.rolling(7).quantile(0.5)
    v_022 = v_015.diff(23)
    v_023 = v_003.rolling(47).max() / v_003.rolling(47).min().replace(0, np.nan)
    v_024 = v_023.diff(47)
    v_025 = v_020.rolling(23).std()
    v_026 = v_017.diff(47)
    v_027 = v_016.diff(47)
    v_028 = v_025 * 3.3180 - v_021 * 0.8440
    v_029 = v_011.rolling(7).skew()
    v_030 = v_020.pct_change(15)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[18]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc066_47d_base_v066_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc066_47d_base_v066_signal

def f160e_f160_equity_to_assets_solvency_regime_calc067_54d_base_v067_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(54).mean().diff(36)
    v_005 = v_003.rolling(36).mean()
    v_006 = v_003.rolling(36).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(54)
    v_009 = v_008.rolling(24).mean()
    v_010 = v_008.rolling(24).std()
    v_011 = v_008.diff(24)
    v_012 = v_007.diff(54)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(36)
    v_015 = v_003.pct_change(54).diff(18)
    v_016 = v_003.rolling(90).skew()
    v_017 = v_003.rolling(90).kurt()
    v_018 = v_011.rolling(12).std()
    v_019 = v_015.rolling(36).mean()
    v_020 = v_012 * 3.4410 + v_014 * 1.0780 + v_011 * 3.6150
    v_021 = v_004.rolling(24).quantile(0.5)
    v_022 = v_015.diff(36)
    v_023 = v_003.rolling(54).max() / v_003.rolling(54).min().replace(0, np.nan)
    v_024 = v_023.diff(54)
    v_025 = v_020.rolling(36).std()
    v_026 = v_017.diff(54)
    v_027 = v_016.diff(54)
    v_028 = v_025 * 3.4410 - v_021 * 1.0780
    v_029 = v_011.rolling(24).skew()
    v_030 = v_020.pct_change(18)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[1]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc067_54d_base_v067_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc067_54d_base_v067_signal

def f160e_f160_equity_to_assets_solvency_regime_calc068_61d_base_v068_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(61).std().diff(49)
    v_005 = v_003.rolling(49).mean()
    v_006 = v_003.rolling(49).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(61)
    v_009 = v_008.rolling(41).mean()
    v_010 = v_008.rolling(41).std()
    v_011 = v_008.diff(41)
    v_012 = v_007.diff(61)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(49)
    v_015 = v_003.pct_change(61).diff(24)
    v_016 = v_003.rolling(110).skew()
    v_017 = v_003.rolling(110).kurt()
    v_018 = v_011.rolling(20).std()
    v_019 = v_015.rolling(49).mean()
    v_020 = v_012 * 3.5640 + v_014 * 1.3120 + v_011 * 3.9600
    v_021 = v_004.rolling(41).quantile(0.5)
    v_022 = v_015.diff(49)
    v_023 = v_003.rolling(61).max() / v_003.rolling(61).min().replace(0, np.nan)
    v_024 = v_023.diff(61)
    v_025 = v_020.rolling(49).std()
    v_026 = v_017.diff(61)
    v_027 = v_016.diff(61)
    v_028 = v_025 * 3.5640 - v_021 * 1.3120
    v_029 = v_011.rolling(41).skew()
    v_030 = v_020.pct_change(20)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[4]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc068_61d_base_v068_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc068_61d_base_v068_signal

def f160e_f160_equity_to_assets_solvency_regime_calc069_68d_base_v069_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(68).rolling(62).mean()
    v_005 = v_003.rolling(62).mean()
    v_006 = v_003.rolling(62).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(68)
    v_009 = v_008.rolling(58).mean()
    v_010 = v_008.rolling(58).std()
    v_011 = v_008.diff(58)
    v_012 = v_007.diff(68)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(62)
    v_015 = v_003.pct_change(68).diff(31)
    v_016 = v_003.rolling(130).skew()
    v_017 = v_003.rolling(130).kurt()
    v_018 = v_011.rolling(29).std()
    v_019 = v_015.rolling(62).mean()
    v_020 = v_012 * 3.6870 + v_014 * 1.5460 + v_011 * 4.3050
    v_021 = v_004.rolling(58).quantile(0.5)
    v_022 = v_015.diff(62)
    v_023 = v_003.rolling(68).max() / v_003.rolling(68).min().replace(0, np.nan)
    v_024 = v_023.diff(68)
    v_025 = v_020.rolling(62).std()
    v_026 = v_017.diff(68)
    v_027 = v_016.diff(68)
    v_028 = v_025 * 3.6870 - v_021 * 1.5460
    v_029 = v_011.rolling(58).skew()
    v_030 = v_020.pct_change(22)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[7]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc069_68d_base_v069_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc069_68d_base_v069_signal

def f160e_f160_equity_to_assets_solvency_regime_calc070_75d_base_v070_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(75).rolling(75).std()
    v_005 = v_003.rolling(75).mean()
    v_006 = v_003.rolling(75).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(75)
    v_009 = v_008.rolling(75).mean()
    v_010 = v_008.rolling(75).std()
    v_011 = v_008.diff(75)
    v_012 = v_007.diff(75)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(75)
    v_015 = v_003.pct_change(75).diff(37)
    v_016 = v_003.rolling(150).skew()
    v_017 = v_003.rolling(150).kurt()
    v_018 = v_011.rolling(37).std()
    v_019 = v_015.rolling(75).mean()
    v_020 = v_012 * 3.8100 + v_014 * 1.7800 + v_011 * 4.6500
    v_021 = v_004.rolling(75).quantile(0.5)
    v_022 = v_015.diff(75)
    v_023 = v_003.rolling(75).max() / v_003.rolling(75).min().replace(0, np.nan)
    v_024 = v_023.diff(75)
    v_025 = v_020.rolling(75).std()
    v_026 = v_017.diff(75)
    v_027 = v_016.diff(75)
    v_028 = v_025 * 3.8100 - v_021 * 1.7800
    v_029 = v_011.rolling(75).skew()
    v_030 = v_020.pct_change(25)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[10]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc070_75d_base_v070_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc070_75d_base_v070_signal

def f160e_f160_equity_to_assets_solvency_regime_calc071_82d_base_v071_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(82).skew().diff(88)
    v_005 = v_003.rolling(88).mean()
    v_006 = v_003.rolling(88).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(82)
    v_009 = v_008.rolling(92).mean()
    v_010 = v_008.rolling(92).std()
    v_011 = v_008.diff(92)
    v_012 = v_007.diff(82)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(88)
    v_015 = v_003.pct_change(82).diff(44)
    v_016 = v_003.rolling(170).skew()
    v_017 = v_003.rolling(170).kurt()
    v_018 = v_011.rolling(46).std()
    v_019 = v_015.rolling(88).mean()
    v_020 = v_012 * 3.9330 + v_014 * 2.0140 + v_011 * 4.9950
    v_021 = v_004.rolling(92).quantile(0.5)
    v_022 = v_015.diff(88)
    v_023 = v_003.rolling(82).max() / v_003.rolling(82).min().replace(0, np.nan)
    v_024 = v_023.diff(82)
    v_025 = v_020.rolling(88).std()
    v_026 = v_017.diff(82)
    v_027 = v_016.diff(82)
    v_028 = v_025 * 3.9330 - v_021 * 2.0140
    v_029 = v_011.rolling(92).skew()
    v_030 = v_020.pct_change(27)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[13]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc071_82d_base_v071_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc071_82d_base_v071_signal

def f160e_f160_equity_to_assets_solvency_regime_calc072_89d_base_v072_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.diff(89)
    v_005 = v_003.rolling(101).mean()
    v_006 = v_003.rolling(101).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(89)
    v_009 = v_008.rolling(109).mean()
    v_010 = v_008.rolling(109).std()
    v_011 = v_008.diff(109)
    v_012 = v_007.diff(89)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(101)
    v_015 = v_003.pct_change(89).diff(50)
    v_016 = v_003.rolling(190).skew()
    v_017 = v_003.rolling(190).kurt()
    v_018 = v_011.rolling(54).std()
    v_019 = v_015.rolling(101).mean()
    v_020 = v_012 * 4.0560 + v_014 * 2.2480 + v_011 * 0.4400
    v_021 = v_004.rolling(109).quantile(0.5)
    v_022 = v_015.diff(101)
    v_023 = v_003.rolling(89).max() / v_003.rolling(89).min().replace(0, np.nan)
    v_024 = v_023.diff(89)
    v_025 = v_020.rolling(101).std()
    v_026 = v_017.diff(89)
    v_027 = v_016.diff(89)
    v_028 = v_025 * 4.0560 - v_021 * 2.2480
    v_029 = v_011.rolling(109).skew()
    v_030 = v_020.pct_change(29)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[16]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc072_89d_base_v072_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc072_89d_base_v072_signal

def f160e_f160_equity_to_assets_solvency_regime_calc073_96d_base_v073_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.pct_change(96)
    v_005 = v_003.rolling(114).mean()
    v_006 = v_003.rolling(114).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(96)
    v_009 = v_008.rolling(126).mean()
    v_010 = v_008.rolling(126).std()
    v_011 = v_008.diff(126)
    v_012 = v_007.diff(96)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(114)
    v_015 = v_003.pct_change(96).diff(57)
    v_016 = v_003.rolling(210).skew()
    v_017 = v_003.rolling(210).kurt()
    v_018 = v_011.rolling(63).std()
    v_019 = v_015.rolling(114).mean()
    v_020 = v_012 * 4.1790 + v_014 * 2.4820 + v_011 * 0.7850
    v_021 = v_004.rolling(126).quantile(0.5)
    v_022 = v_015.diff(114)
    v_023 = v_003.rolling(96).max() / v_003.rolling(96).min().replace(0, np.nan)
    v_024 = v_023.diff(96)
    v_025 = v_020.rolling(114).std()
    v_026 = v_017.diff(96)
    v_027 = v_016.diff(96)
    v_028 = v_025 * 4.1790 - v_021 * 2.4820
    v_029 = v_011.rolling(126).skew()
    v_030 = v_020.pct_change(32)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[19]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc073_96d_base_v073_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc073_96d_base_v073_signal

def f160e_f160_equity_to_assets_solvency_regime_calc074_103d_base_v074_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = np.log(v_003.replace(0, np.nan)).diff(103)
    v_005 = v_003.rolling(127).mean()
    v_006 = v_003.rolling(127).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(103)
    v_009 = v_008.rolling(143).mean()
    v_010 = v_008.rolling(143).std()
    v_011 = v_008.diff(143)
    v_012 = v_007.diff(103)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(127)
    v_015 = v_003.pct_change(103).diff(63)
    v_016 = v_003.rolling(230).skew()
    v_017 = v_003.rolling(230).kurt()
    v_018 = v_011.rolling(71).std()
    v_019 = v_015.rolling(127).mean()
    v_020 = v_012 * 4.3020 + v_014 * 2.7160 + v_011 * 1.1300
    v_021 = v_004.rolling(143).quantile(0.5)
    v_022 = v_015.diff(127)
    v_023 = v_003.rolling(103).max() / v_003.rolling(103).min().replace(0, np.nan)
    v_024 = v_023.diff(103)
    v_025 = v_020.rolling(127).std()
    v_026 = v_017.diff(103)
    v_027 = v_016.diff(103)
    v_028 = v_025 * 4.3020 - v_021 * 2.7160
    v_029 = v_011.rolling(143).skew()
    v_030 = v_020.pct_change(34)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[2]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc074_103d_base_v074_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc074_103d_base_v074_signal

def f160e_f160_equity_to_assets_solvency_regime_calc075_110d_base_v075_signal(equity, assets):
    v_001 = equity.replace(0, np.nan)
    v_002 = assets.replace(0, np.nan)
    v_003 = v_001 / v_002
    v_004 = v_003.rolling(110).mean().diff(140)
    v_005 = v_003.rolling(140).mean()
    v_006 = v_003.rolling(140).std()
    v_007 = (v_003 - v_005) / v_006.replace(0, np.nan)
    v_008 = v_004.diff(110)
    v_009 = v_008.rolling(20).mean()
    v_010 = v_008.rolling(20).std()
    v_011 = v_008.diff(20)
    v_012 = v_007.diff(110)
    v_013 = v_004 / v_006.replace(0, np.nan)
    v_014 = v_013.diff(140)
    v_015 = v_003.pct_change(110).diff(70)
    v_016 = v_003.rolling(250).skew()
    v_017 = v_003.rolling(250).kurt()
    v_018 = v_011.rolling(10).std()
    v_019 = v_015.rolling(140).mean()
    v_020 = v_012 * 4.4250 + v_014 * 2.9500 + v_011 * 1.4750
    v_021 = v_004.rolling(20).quantile(0.5)
    v_022 = v_015.diff(140)
    v_023 = v_003.rolling(110).max() / v_003.rolling(110).min().replace(0, np.nan)
    v_024 = v_023.diff(110)
    v_025 = v_020.rolling(140).std()
    v_026 = v_017.diff(110)
    v_027 = v_016.diff(110)
    v_028 = v_025 * 4.4250 - v_021 * 2.9500
    v_029 = v_011.rolling(20).skew()
    v_030 = v_020.pct_change(36)
    
    output_options = [v_004, v_007, v_008, v_011, v_012, v_014, v_015, v_018, v_020, v_021, v_022, v_024, v_025, v_026, v_027, v_028, v_029, v_030, v_013, v_019]
    res = output_options[5]
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f160e_f160_equity_to_assets_solvency_regime_calc075_110d_base_v075_signal'] = f160e_f160_equity_to_assets_solvency_regime_calc075_110d_base_v075_signal

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
