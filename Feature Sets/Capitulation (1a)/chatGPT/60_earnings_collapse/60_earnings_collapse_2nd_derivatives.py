import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def ecl_151_ecl_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def ecl_152_ecl_007_interest_coverage_stress_252_roc_42(ecl_007_interest_coverage_stress_252):
    feature = _s(ecl_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def ecl_153_ecl_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def ecl_154_ecl_019_interest_coverage_stress_84_roc_378(ecl_019_interest_coverage_stress_84):
    feature = _s(ecl_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def ecl_155_ecl_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















EARNINGS_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    'ecl_151_ecl_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': ecl_151_ecl_001_netinc_decline_1_roc_1},
    'ecl_152_ecl_007_interest_coverage_stress_252_roc_42': {'inputs': ['ecl_007_interest_coverage_stress_252'], 'func': ecl_152_ecl_007_interest_coverage_stress_252_roc_42},
    'ecl_153_ecl_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': ecl_153_ecl_013_netinc_decline_1_roc_126},
    'ecl_154_ecl_019_interest_coverage_stress_84_roc_378': {'inputs': ['ecl_019_interest_coverage_stress_84'], 'func': ecl_154_ecl_019_interest_coverage_stress_84_roc_378},
    'ecl_155_ecl_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': ecl_155_ecl_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ec_replacement_d2_001(ec_replacement_001):
    feature = _clean(ec_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_001'] = {'inputs': ['ec_replacement_001'], 'func': ec_replacement_d2_001}


def ec_replacement_d2_002(ec_replacement_002):
    feature = _clean(ec_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_002'] = {'inputs': ['ec_replacement_002'], 'func': ec_replacement_d2_002}


def ec_replacement_d2_003(ec_replacement_003):
    feature = _clean(ec_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_003'] = {'inputs': ['ec_replacement_003'], 'func': ec_replacement_d2_003}


def ec_replacement_d2_004(ec_replacement_004):
    feature = _clean(ec_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_004'] = {'inputs': ['ec_replacement_004'], 'func': ec_replacement_d2_004}


def ec_replacement_d2_005(ec_replacement_005):
    feature = _clean(ec_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_005'] = {'inputs': ['ec_replacement_005'], 'func': ec_replacement_d2_005}


def ec_replacement_d2_006(ec_replacement_006):
    feature = _clean(ec_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_006'] = {'inputs': ['ec_replacement_006'], 'func': ec_replacement_d2_006}


def ec_replacement_d2_007(ec_replacement_007):
    feature = _clean(ec_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_007'] = {'inputs': ['ec_replacement_007'], 'func': ec_replacement_d2_007}


def ec_replacement_d2_008(ec_replacement_008):
    feature = _clean(ec_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_008'] = {'inputs': ['ec_replacement_008'], 'func': ec_replacement_d2_008}


def ec_replacement_d2_009(ec_replacement_009):
    feature = _clean(ec_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_009'] = {'inputs': ['ec_replacement_009'], 'func': ec_replacement_d2_009}


def ec_replacement_d2_010(ec_replacement_010):
    feature = _clean(ec_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_010'] = {'inputs': ['ec_replacement_010'], 'func': ec_replacement_d2_010}


def ec_replacement_d2_011(ec_replacement_011):
    feature = _clean(ec_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_011'] = {'inputs': ['ec_replacement_011'], 'func': ec_replacement_d2_011}


def ec_replacement_d2_012(ec_replacement_012):
    feature = _clean(ec_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_012'] = {'inputs': ['ec_replacement_012'], 'func': ec_replacement_d2_012}


def ec_replacement_d2_013(ec_replacement_013):
    feature = _clean(ec_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_013'] = {'inputs': ['ec_replacement_013'], 'func': ec_replacement_d2_013}


def ec_replacement_d2_014(ec_replacement_014):
    feature = _clean(ec_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_014'] = {'inputs': ['ec_replacement_014'], 'func': ec_replacement_d2_014}


def ec_replacement_d2_015(ec_replacement_015):
    feature = _clean(ec_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_015'] = {'inputs': ['ec_replacement_015'], 'func': ec_replacement_d2_015}


def ec_replacement_d2_016(ec_replacement_016):
    feature = _clean(ec_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_016'] = {'inputs': ['ec_replacement_016'], 'func': ec_replacement_d2_016}


def ec_replacement_d2_017(ec_replacement_017):
    feature = _clean(ec_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_017'] = {'inputs': ['ec_replacement_017'], 'func': ec_replacement_d2_017}


def ec_replacement_d2_018(ec_replacement_018):
    feature = _clean(ec_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_018'] = {'inputs': ['ec_replacement_018'], 'func': ec_replacement_d2_018}


def ec_replacement_d2_019(ec_replacement_019):
    feature = _clean(ec_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_019'] = {'inputs': ['ec_replacement_019'], 'func': ec_replacement_d2_019}


def ec_replacement_d2_020(ec_replacement_020):
    feature = _clean(ec_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_020'] = {'inputs': ['ec_replacement_020'], 'func': ec_replacement_d2_020}


def ec_replacement_d2_021(ec_replacement_021):
    feature = _clean(ec_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_021'] = {'inputs': ['ec_replacement_021'], 'func': ec_replacement_d2_021}


def ec_replacement_d2_022(ec_replacement_022):
    feature = _clean(ec_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_022'] = {'inputs': ['ec_replacement_022'], 'func': ec_replacement_d2_022}


def ec_replacement_d2_023(ec_replacement_023):
    feature = _clean(ec_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_023'] = {'inputs': ['ec_replacement_023'], 'func': ec_replacement_d2_023}


def ec_replacement_d2_024(ec_replacement_024):
    feature = _clean(ec_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_024'] = {'inputs': ['ec_replacement_024'], 'func': ec_replacement_d2_024}


def ec_replacement_d2_025(ec_replacement_025):
    feature = _clean(ec_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_025'] = {'inputs': ['ec_replacement_025'], 'func': ec_replacement_d2_025}


def ec_replacement_d2_026(ec_replacement_026):
    feature = _clean(ec_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_026'] = {'inputs': ['ec_replacement_026'], 'func': ec_replacement_d2_026}


def ec_replacement_d2_027(ec_replacement_027):
    feature = _clean(ec_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_027'] = {'inputs': ['ec_replacement_027'], 'func': ec_replacement_d2_027}


def ec_replacement_d2_028(ec_replacement_028):
    feature = _clean(ec_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_028'] = {'inputs': ['ec_replacement_028'], 'func': ec_replacement_d2_028}


def ec_replacement_d2_029(ec_replacement_029):
    feature = _clean(ec_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_029'] = {'inputs': ['ec_replacement_029'], 'func': ec_replacement_d2_029}


def ec_replacement_d2_030(ec_replacement_030):
    feature = _clean(ec_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_030'] = {'inputs': ['ec_replacement_030'], 'func': ec_replacement_d2_030}


def ec_replacement_d2_031(ec_replacement_031):
    feature = _clean(ec_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_031'] = {'inputs': ['ec_replacement_031'], 'func': ec_replacement_d2_031}


def ec_replacement_d2_032(ec_replacement_032):
    feature = _clean(ec_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_032'] = {'inputs': ['ec_replacement_032'], 'func': ec_replacement_d2_032}


def ec_replacement_d2_033(ec_replacement_033):
    feature = _clean(ec_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_033'] = {'inputs': ['ec_replacement_033'], 'func': ec_replacement_d2_033}


def ec_replacement_d2_034(ec_replacement_034):
    feature = _clean(ec_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_034'] = {'inputs': ['ec_replacement_034'], 'func': ec_replacement_d2_034}


def ec_replacement_d2_035(ec_replacement_035):
    feature = _clean(ec_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_035'] = {'inputs': ['ec_replacement_035'], 'func': ec_replacement_d2_035}


def ec_replacement_d2_036(ec_replacement_036):
    feature = _clean(ec_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_036'] = {'inputs': ['ec_replacement_036'], 'func': ec_replacement_d2_036}


def ec_replacement_d2_037(ec_replacement_037):
    feature = _clean(ec_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_037'] = {'inputs': ['ec_replacement_037'], 'func': ec_replacement_d2_037}


def ec_replacement_d2_038(ec_replacement_038):
    feature = _clean(ec_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_038'] = {'inputs': ['ec_replacement_038'], 'func': ec_replacement_d2_038}


def ec_replacement_d2_039(ec_replacement_039):
    feature = _clean(ec_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_039'] = {'inputs': ['ec_replacement_039'], 'func': ec_replacement_d2_039}


def ec_replacement_d2_040(ec_replacement_040):
    feature = _clean(ec_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_040'] = {'inputs': ['ec_replacement_040'], 'func': ec_replacement_d2_040}


def ec_replacement_d2_041(ec_replacement_041):
    feature = _clean(ec_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_041'] = {'inputs': ['ec_replacement_041'], 'func': ec_replacement_d2_041}


def ec_replacement_d2_042(ec_replacement_042):
    feature = _clean(ec_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_042'] = {'inputs': ['ec_replacement_042'], 'func': ec_replacement_d2_042}


def ec_replacement_d2_043(ec_replacement_043):
    feature = _clean(ec_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_043'] = {'inputs': ['ec_replacement_043'], 'func': ec_replacement_d2_043}


def ec_replacement_d2_044(ec_replacement_044):
    feature = _clean(ec_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_044'] = {'inputs': ['ec_replacement_044'], 'func': ec_replacement_d2_044}


def ec_replacement_d2_045(ec_replacement_045):
    feature = _clean(ec_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_045'] = {'inputs': ['ec_replacement_045'], 'func': ec_replacement_d2_045}


def ec_replacement_d2_046(ec_replacement_046):
    feature = _clean(ec_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_046'] = {'inputs': ['ec_replacement_046'], 'func': ec_replacement_d2_046}


def ec_replacement_d2_047(ec_replacement_047):
    feature = _clean(ec_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_047'] = {'inputs': ['ec_replacement_047'], 'func': ec_replacement_d2_047}


def ec_replacement_d2_048(ec_replacement_048):
    feature = _clean(ec_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_048'] = {'inputs': ['ec_replacement_048'], 'func': ec_replacement_d2_048}


def ec_replacement_d2_049(ec_replacement_049):
    feature = _clean(ec_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_049'] = {'inputs': ['ec_replacement_049'], 'func': ec_replacement_d2_049}


def ec_replacement_d2_050(ec_replacement_050):
    feature = _clean(ec_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_050'] = {'inputs': ['ec_replacement_050'], 'func': ec_replacement_d2_050}


def ec_replacement_d2_051(ec_replacement_051):
    feature = _clean(ec_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_051'] = {'inputs': ['ec_replacement_051'], 'func': ec_replacement_d2_051}


def ec_replacement_d2_052(ec_replacement_052):
    feature = _clean(ec_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_052'] = {'inputs': ['ec_replacement_052'], 'func': ec_replacement_d2_052}


def ec_replacement_d2_053(ec_replacement_053):
    feature = _clean(ec_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_053'] = {'inputs': ['ec_replacement_053'], 'func': ec_replacement_d2_053}


def ec_replacement_d2_054(ec_replacement_054):
    feature = _clean(ec_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_054'] = {'inputs': ['ec_replacement_054'], 'func': ec_replacement_d2_054}


def ec_replacement_d2_055(ec_replacement_055):
    feature = _clean(ec_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_055'] = {'inputs': ['ec_replacement_055'], 'func': ec_replacement_d2_055}


def ec_replacement_d2_056(ec_replacement_056):
    feature = _clean(ec_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_056'] = {'inputs': ['ec_replacement_056'], 'func': ec_replacement_d2_056}


def ec_replacement_d2_057(ec_replacement_057):
    feature = _clean(ec_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_057'] = {'inputs': ['ec_replacement_057'], 'func': ec_replacement_d2_057}


def ec_replacement_d2_058(ec_replacement_058):
    feature = _clean(ec_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_058'] = {'inputs': ['ec_replacement_058'], 'func': ec_replacement_d2_058}


def ec_replacement_d2_059(ec_replacement_059):
    feature = _clean(ec_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_059'] = {'inputs': ['ec_replacement_059'], 'func': ec_replacement_d2_059}


def ec_replacement_d2_060(ec_replacement_060):
    feature = _clean(ec_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_060'] = {'inputs': ['ec_replacement_060'], 'func': ec_replacement_d2_060}


def ec_replacement_d2_061(ec_replacement_061):
    feature = _clean(ec_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_061'] = {'inputs': ['ec_replacement_061'], 'func': ec_replacement_d2_061}


def ec_replacement_d2_062(ec_replacement_062):
    feature = _clean(ec_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_062'] = {'inputs': ['ec_replacement_062'], 'func': ec_replacement_d2_062}


def ec_replacement_d2_063(ec_replacement_063):
    feature = _clean(ec_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_063'] = {'inputs': ['ec_replacement_063'], 'func': ec_replacement_d2_063}


def ec_replacement_d2_064(ec_replacement_064):
    feature = _clean(ec_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_064'] = {'inputs': ['ec_replacement_064'], 'func': ec_replacement_d2_064}


def ec_replacement_d2_065(ec_replacement_065):
    feature = _clean(ec_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_065'] = {'inputs': ['ec_replacement_065'], 'func': ec_replacement_d2_065}


def ec_replacement_d2_066(ec_replacement_066):
    feature = _clean(ec_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_066'] = {'inputs': ['ec_replacement_066'], 'func': ec_replacement_d2_066}


def ec_replacement_d2_067(ec_replacement_067):
    feature = _clean(ec_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_067'] = {'inputs': ['ec_replacement_067'], 'func': ec_replacement_d2_067}


def ec_replacement_d2_068(ec_replacement_068):
    feature = _clean(ec_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_068'] = {'inputs': ['ec_replacement_068'], 'func': ec_replacement_d2_068}


def ec_replacement_d2_069(ec_replacement_069):
    feature = _clean(ec_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_069'] = {'inputs': ['ec_replacement_069'], 'func': ec_replacement_d2_069}


def ec_replacement_d2_070(ec_replacement_070):
    feature = _clean(ec_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_070'] = {'inputs': ['ec_replacement_070'], 'func': ec_replacement_d2_070}


def ec_replacement_d2_071(ec_replacement_071):
    feature = _clean(ec_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_071'] = {'inputs': ['ec_replacement_071'], 'func': ec_replacement_d2_071}


def ec_replacement_d2_072(ec_replacement_072):
    feature = _clean(ec_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_072'] = {'inputs': ['ec_replacement_072'], 'func': ec_replacement_d2_072}


def ec_replacement_d2_073(ec_replacement_073):
    feature = _clean(ec_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_073'] = {'inputs': ['ec_replacement_073'], 'func': ec_replacement_d2_073}


def ec_replacement_d2_074(ec_replacement_074):
    feature = _clean(ec_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_074'] = {'inputs': ['ec_replacement_074'], 'func': ec_replacement_d2_074}


def ec_replacement_d2_075(ec_replacement_075):
    feature = _clean(ec_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_075'] = {'inputs': ['ec_replacement_075'], 'func': ec_replacement_d2_075}


def ec_replacement_d2_076(ec_replacement_076):
    feature = _clean(ec_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_076'] = {'inputs': ['ec_replacement_076'], 'func': ec_replacement_d2_076}


def ec_replacement_d2_077(ec_replacement_077):
    feature = _clean(ec_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_077'] = {'inputs': ['ec_replacement_077'], 'func': ec_replacement_d2_077}


def ec_replacement_d2_078(ec_replacement_078):
    feature = _clean(ec_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_078'] = {'inputs': ['ec_replacement_078'], 'func': ec_replacement_d2_078}


def ec_replacement_d2_079(ec_replacement_079):
    feature = _clean(ec_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_079'] = {'inputs': ['ec_replacement_079'], 'func': ec_replacement_d2_079}


def ec_replacement_d2_080(ec_replacement_080):
    feature = _clean(ec_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_080'] = {'inputs': ['ec_replacement_080'], 'func': ec_replacement_d2_080}


def ec_replacement_d2_081(ec_replacement_081):
    feature = _clean(ec_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_081'] = {'inputs': ['ec_replacement_081'], 'func': ec_replacement_d2_081}


def ec_replacement_d2_082(ec_replacement_082):
    feature = _clean(ec_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_082'] = {'inputs': ['ec_replacement_082'], 'func': ec_replacement_d2_082}


def ec_replacement_d2_083(ec_replacement_083):
    feature = _clean(ec_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_083'] = {'inputs': ['ec_replacement_083'], 'func': ec_replacement_d2_083}


def ec_replacement_d2_084(ec_replacement_084):
    feature = _clean(ec_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_084'] = {'inputs': ['ec_replacement_084'], 'func': ec_replacement_d2_084}


def ec_replacement_d2_085(ec_replacement_085):
    feature = _clean(ec_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_085'] = {'inputs': ['ec_replacement_085'], 'func': ec_replacement_d2_085}


def ec_replacement_d2_086(ec_replacement_086):
    feature = _clean(ec_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_086'] = {'inputs': ['ec_replacement_086'], 'func': ec_replacement_d2_086}


def ec_replacement_d2_087(ec_replacement_087):
    feature = _clean(ec_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_087'] = {'inputs': ['ec_replacement_087'], 'func': ec_replacement_d2_087}


def ec_replacement_d2_088(ec_replacement_088):
    feature = _clean(ec_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_088'] = {'inputs': ['ec_replacement_088'], 'func': ec_replacement_d2_088}


def ec_replacement_d2_089(ec_replacement_089):
    feature = _clean(ec_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_089'] = {'inputs': ['ec_replacement_089'], 'func': ec_replacement_d2_089}


def ec_replacement_d2_090(ec_replacement_090):
    feature = _clean(ec_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_090'] = {'inputs': ['ec_replacement_090'], 'func': ec_replacement_d2_090}


def ec_replacement_d2_091(ec_replacement_091):
    feature = _clean(ec_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_091'] = {'inputs': ['ec_replacement_091'], 'func': ec_replacement_d2_091}


def ec_replacement_d2_092(ec_replacement_092):
    feature = _clean(ec_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_092'] = {'inputs': ['ec_replacement_092'], 'func': ec_replacement_d2_092}


def ec_replacement_d2_093(ec_replacement_093):
    feature = _clean(ec_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_093'] = {'inputs': ['ec_replacement_093'], 'func': ec_replacement_d2_093}


def ec_replacement_d2_094(ec_replacement_094):
    feature = _clean(ec_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_094'] = {'inputs': ['ec_replacement_094'], 'func': ec_replacement_d2_094}


def ec_replacement_d2_095(ec_replacement_095):
    feature = _clean(ec_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_095'] = {'inputs': ['ec_replacement_095'], 'func': ec_replacement_d2_095}


def ec_replacement_d2_096(ec_replacement_096):
    feature = _clean(ec_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_096'] = {'inputs': ['ec_replacement_096'], 'func': ec_replacement_d2_096}


def ec_replacement_d2_097(ec_replacement_097):
    feature = _clean(ec_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_097'] = {'inputs': ['ec_replacement_097'], 'func': ec_replacement_d2_097}


def ec_replacement_d2_098(ec_replacement_098):
    feature = _clean(ec_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_098'] = {'inputs': ['ec_replacement_098'], 'func': ec_replacement_d2_098}


def ec_replacement_d2_099(ec_replacement_099):
    feature = _clean(ec_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_099'] = {'inputs': ['ec_replacement_099'], 'func': ec_replacement_d2_099}


def ec_replacement_d2_100(ec_replacement_100):
    feature = _clean(ec_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_100'] = {'inputs': ['ec_replacement_100'], 'func': ec_replacement_d2_100}


def ec_replacement_d2_101(ec_replacement_101):
    feature = _clean(ec_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_101'] = {'inputs': ['ec_replacement_101'], 'func': ec_replacement_d2_101}


def ec_replacement_d2_102(ec_replacement_102):
    feature = _clean(ec_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_102'] = {'inputs': ['ec_replacement_102'], 'func': ec_replacement_d2_102}


def ec_replacement_d2_103(ec_replacement_103):
    feature = _clean(ec_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_103'] = {'inputs': ['ec_replacement_103'], 'func': ec_replacement_d2_103}


def ec_replacement_d2_104(ec_replacement_104):
    feature = _clean(ec_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_104'] = {'inputs': ['ec_replacement_104'], 'func': ec_replacement_d2_104}


def ec_replacement_d2_105(ec_replacement_105):
    feature = _clean(ec_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_105'] = {'inputs': ['ec_replacement_105'], 'func': ec_replacement_d2_105}


def ec_replacement_d2_106(ec_replacement_106):
    feature = _clean(ec_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_106'] = {'inputs': ['ec_replacement_106'], 'func': ec_replacement_d2_106}


def ec_replacement_d2_107(ec_replacement_107):
    feature = _clean(ec_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_107'] = {'inputs': ['ec_replacement_107'], 'func': ec_replacement_d2_107}


def ec_replacement_d2_108(ec_replacement_108):
    feature = _clean(ec_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_108'] = {'inputs': ['ec_replacement_108'], 'func': ec_replacement_d2_108}


def ec_replacement_d2_109(ec_replacement_109):
    feature = _clean(ec_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_109'] = {'inputs': ['ec_replacement_109'], 'func': ec_replacement_d2_109}


def ec_replacement_d2_110(ec_replacement_110):
    feature = _clean(ec_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_110'] = {'inputs': ['ec_replacement_110'], 'func': ec_replacement_d2_110}


def ec_replacement_d2_111(ec_replacement_111):
    feature = _clean(ec_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_111'] = {'inputs': ['ec_replacement_111'], 'func': ec_replacement_d2_111}


def ec_replacement_d2_112(ec_replacement_112):
    feature = _clean(ec_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_112'] = {'inputs': ['ec_replacement_112'], 'func': ec_replacement_d2_112}


def ec_replacement_d2_113(ec_replacement_113):
    feature = _clean(ec_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_113'] = {'inputs': ['ec_replacement_113'], 'func': ec_replacement_d2_113}


def ec_replacement_d2_114(ec_replacement_114):
    feature = _clean(ec_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_114'] = {'inputs': ['ec_replacement_114'], 'func': ec_replacement_d2_114}


def ec_replacement_d2_115(ec_replacement_115):
    feature = _clean(ec_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_115'] = {'inputs': ['ec_replacement_115'], 'func': ec_replacement_d2_115}


def ec_replacement_d2_116(ec_replacement_116):
    feature = _clean(ec_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_116'] = {'inputs': ['ec_replacement_116'], 'func': ec_replacement_d2_116}


def ec_replacement_d2_117(ec_replacement_117):
    feature = _clean(ec_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_117'] = {'inputs': ['ec_replacement_117'], 'func': ec_replacement_d2_117}


def ec_replacement_d2_118(ec_replacement_118):
    feature = _clean(ec_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_118'] = {'inputs': ['ec_replacement_118'], 'func': ec_replacement_d2_118}


def ec_replacement_d2_119(ec_replacement_119):
    feature = _clean(ec_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_119'] = {'inputs': ['ec_replacement_119'], 'func': ec_replacement_d2_119}


def ec_replacement_d2_120(ec_replacement_120):
    feature = _clean(ec_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_120'] = {'inputs': ['ec_replacement_120'], 'func': ec_replacement_d2_120}


def ec_replacement_d2_121(ec_replacement_121):
    feature = _clean(ec_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_121'] = {'inputs': ['ec_replacement_121'], 'func': ec_replacement_d2_121}


def ec_replacement_d2_122(ec_replacement_122):
    feature = _clean(ec_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_122'] = {'inputs': ['ec_replacement_122'], 'func': ec_replacement_d2_122}


def ec_replacement_d2_123(ec_replacement_123):
    feature = _clean(ec_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_123'] = {'inputs': ['ec_replacement_123'], 'func': ec_replacement_d2_123}


def ec_replacement_d2_124(ec_replacement_124):
    feature = _clean(ec_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_124'] = {'inputs': ['ec_replacement_124'], 'func': ec_replacement_d2_124}


def ec_replacement_d2_125(ec_replacement_125):
    feature = _clean(ec_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_125'] = {'inputs': ['ec_replacement_125'], 'func': ec_replacement_d2_125}


def ec_replacement_d2_126(ec_replacement_126):
    feature = _clean(ec_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_126'] = {'inputs': ['ec_replacement_126'], 'func': ec_replacement_d2_126}


def ec_replacement_d2_127(ec_replacement_127):
    feature = _clean(ec_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_127'] = {'inputs': ['ec_replacement_127'], 'func': ec_replacement_d2_127}


def ec_replacement_d2_128(ec_replacement_128):
    feature = _clean(ec_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_128'] = {'inputs': ['ec_replacement_128'], 'func': ec_replacement_d2_128}


def ec_replacement_d2_129(ec_replacement_129):
    feature = _clean(ec_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_129'] = {'inputs': ['ec_replacement_129'], 'func': ec_replacement_d2_129}


def ec_replacement_d2_130(ec_replacement_130):
    feature = _clean(ec_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_130'] = {'inputs': ['ec_replacement_130'], 'func': ec_replacement_d2_130}


def ec_replacement_d2_131(ec_replacement_131):
    feature = _clean(ec_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_131'] = {'inputs': ['ec_replacement_131'], 'func': ec_replacement_d2_131}


def ec_replacement_d2_132(ec_replacement_132):
    feature = _clean(ec_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_132'] = {'inputs': ['ec_replacement_132'], 'func': ec_replacement_d2_132}


def ec_replacement_d2_133(ec_replacement_133):
    feature = _clean(ec_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_133'] = {'inputs': ['ec_replacement_133'], 'func': ec_replacement_d2_133}


def ec_replacement_d2_134(ec_replacement_134):
    feature = _clean(ec_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_134'] = {'inputs': ['ec_replacement_134'], 'func': ec_replacement_d2_134}


def ec_replacement_d2_135(ec_replacement_135):
    feature = _clean(ec_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_135'] = {'inputs': ['ec_replacement_135'], 'func': ec_replacement_d2_135}


def ec_replacement_d2_136(ec_replacement_136):
    feature = _clean(ec_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_136'] = {'inputs': ['ec_replacement_136'], 'func': ec_replacement_d2_136}


def ec_replacement_d2_137(ec_replacement_137):
    feature = _clean(ec_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_137'] = {'inputs': ['ec_replacement_137'], 'func': ec_replacement_d2_137}


def ec_replacement_d2_138(ec_replacement_138):
    feature = _clean(ec_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_138'] = {'inputs': ['ec_replacement_138'], 'func': ec_replacement_d2_138}


def ec_replacement_d2_139(ec_replacement_139):
    feature = _clean(ec_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_139'] = {'inputs': ['ec_replacement_139'], 'func': ec_replacement_d2_139}


def ec_replacement_d2_140(ec_replacement_140):
    feature = _clean(ec_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_140'] = {'inputs': ['ec_replacement_140'], 'func': ec_replacement_d2_140}


def ec_replacement_d2_141(ec_replacement_141):
    feature = _clean(ec_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_141'] = {'inputs': ['ec_replacement_141'], 'func': ec_replacement_d2_141}


def ec_replacement_d2_142(ec_replacement_142):
    feature = _clean(ec_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_142'] = {'inputs': ['ec_replacement_142'], 'func': ec_replacement_d2_142}


def ec_replacement_d2_143(ec_replacement_143):
    feature = _clean(ec_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_143'] = {'inputs': ['ec_replacement_143'], 'func': ec_replacement_d2_143}


def ec_replacement_d2_144(ec_replacement_144):
    feature = _clean(ec_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_144'] = {'inputs': ['ec_replacement_144'], 'func': ec_replacement_d2_144}


def ec_replacement_d2_145(ec_replacement_145):
    feature = _clean(ec_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_145'] = {'inputs': ['ec_replacement_145'], 'func': ec_replacement_d2_145}


def ec_replacement_d2_146(ec_replacement_146):
    feature = _clean(ec_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_146'] = {'inputs': ['ec_replacement_146'], 'func': ec_replacement_d2_146}


def ec_replacement_d2_147(ec_replacement_147):
    feature = _clean(ec_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_147'] = {'inputs': ['ec_replacement_147'], 'func': ec_replacement_d2_147}


def ec_replacement_d2_148(ec_replacement_148):
    feature = _clean(ec_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_148'] = {'inputs': ['ec_replacement_148'], 'func': ec_replacement_d2_148}


def ec_replacement_d2_149(ec_replacement_149):
    feature = _clean(ec_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_149'] = {'inputs': ['ec_replacement_149'], 'func': ec_replacement_d2_149}


def ec_replacement_d2_150(ec_replacement_150):
    feature = _clean(ec_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_150'] = {'inputs': ['ec_replacement_150'], 'func': ec_replacement_d2_150}


def ec_replacement_d2_151(ec_replacement_151):
    feature = _clean(ec_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_151'] = {'inputs': ['ec_replacement_151'], 'func': ec_replacement_d2_151}


def ec_replacement_d2_152(ec_replacement_152):
    feature = _clean(ec_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_152'] = {'inputs': ['ec_replacement_152'], 'func': ec_replacement_d2_152}


def ec_replacement_d2_153(ec_replacement_153):
    feature = _clean(ec_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_153'] = {'inputs': ['ec_replacement_153'], 'func': ec_replacement_d2_153}


def ec_replacement_d2_154(ec_replacement_154):
    feature = _clean(ec_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_154'] = {'inputs': ['ec_replacement_154'], 'func': ec_replacement_d2_154}


def ec_replacement_d2_155(ec_replacement_155):
    feature = _clean(ec_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_155'] = {'inputs': ['ec_replacement_155'], 'func': ec_replacement_d2_155}


def ec_replacement_d2_156(ec_replacement_156):
    feature = _clean(ec_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_156'] = {'inputs': ['ec_replacement_156'], 'func': ec_replacement_d2_156}


def ec_replacement_d2_157(ec_replacement_157):
    feature = _clean(ec_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_157'] = {'inputs': ['ec_replacement_157'], 'func': ec_replacement_d2_157}


def ec_replacement_d2_158(ec_replacement_158):
    feature = _clean(ec_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_158'] = {'inputs': ['ec_replacement_158'], 'func': ec_replacement_d2_158}


def ec_replacement_d2_159(ec_replacement_159):
    feature = _clean(ec_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_159'] = {'inputs': ['ec_replacement_159'], 'func': ec_replacement_d2_159}


def ec_replacement_d2_160(ec_replacement_160):
    feature = _clean(ec_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_160'] = {'inputs': ['ec_replacement_160'], 'func': ec_replacement_d2_160}


def ec_replacement_d2_161(ec_replacement_161):
    feature = _clean(ec_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_161'] = {'inputs': ['ec_replacement_161'], 'func': ec_replacement_d2_161}


def ec_replacement_d2_162(ec_replacement_162):
    feature = _clean(ec_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_162'] = {'inputs': ['ec_replacement_162'], 'func': ec_replacement_d2_162}


def ec_replacement_d2_163(ec_replacement_163):
    feature = _clean(ec_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_163'] = {'inputs': ['ec_replacement_163'], 'func': ec_replacement_d2_163}


def ec_replacement_d2_164(ec_replacement_164):
    feature = _clean(ec_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_164'] = {'inputs': ['ec_replacement_164'], 'func': ec_replacement_d2_164}


def ec_replacement_d2_165(ec_replacement_165):
    feature = _clean(ec_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_165'] = {'inputs': ['ec_replacement_165'], 'func': ec_replacement_d2_165}


def ec_replacement_d2_166(ec_replacement_166):
    feature = _clean(ec_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
EC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ec_replacement_d2_166'] = {'inputs': ['ec_replacement_166'], 'func': ec_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63(ecl_003_fcf_burn_to_cash_63):
    return _base_universe_d2(ecl_003_fcf_burn_to_cash_63, 1)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63'] = {'inputs': ['ecl_003_fcf_burn_to_cash_63'], 'func': ecl_base_universe_d2_001_ecl_003_fcf_burn_to_cash_63}


def ecl_base_universe_d2_002_ecl_004_debt_to_equity_84(ecl_004_debt_to_equity_84):
    return _base_universe_d2(ecl_004_debt_to_equity_84, 2)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_002_ecl_004_debt_to_equity_84'] = {'inputs': ['ecl_004_debt_to_equity_84'], 'func': ecl_base_universe_d2_002_ecl_004_debt_to_equity_84}


def ecl_base_universe_d2_003_ecl_005_debt_to_assets_126(ecl_005_debt_to_assets_126):
    return _base_universe_d2(ecl_005_debt_to_assets_126, 3)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_003_ecl_005_debt_to_assets_126'] = {'inputs': ['ecl_005_debt_to_assets_126'], 'func': ecl_base_universe_d2_003_ecl_005_debt_to_assets_126}


def ecl_base_universe_d2_004_ecl_012_accrual_gap_1260(ecl_012_accrual_gap_1260):
    return _base_universe_d2(ecl_012_accrual_gap_1260, 4)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_004_ecl_012_accrual_gap_1260'] = {'inputs': ['ecl_012_accrual_gap_1260'], 'func': ecl_base_universe_d2_004_ecl_012_accrual_gap_1260}


def ecl_base_universe_d2_005_ecl_016_debt_to_equity_21(ecl_016_debt_to_equity_21):
    return _base_universe_d2(ecl_016_debt_to_equity_21, 5)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_005_ecl_016_debt_to_equity_21'] = {'inputs': ['ecl_016_debt_to_equity_21'], 'func': ecl_base_universe_d2_005_ecl_016_debt_to_equity_21}


def ecl_base_universe_d2_006_ecl_017_debt_to_assets_42(ecl_017_debt_to_assets_42):
    return _base_universe_d2(ecl_017_debt_to_assets_42, 6)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_006_ecl_017_debt_to_assets_42'] = {'inputs': ['ecl_017_debt_to_assets_42'], 'func': ecl_base_universe_d2_006_ecl_017_debt_to_assets_42}


def ecl_base_universe_d2_007_ecl_024_accrual_gap_504(ecl_024_accrual_gap_504):
    return _base_universe_d2(ecl_024_accrual_gap_504, 7)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_007_ecl_024_accrual_gap_504'] = {'inputs': ['ecl_024_accrual_gap_504'], 'func': ecl_base_universe_d2_007_ecl_024_accrual_gap_504}


def ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260(ecl_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(ecl_027_fcf_burn_to_cash_1260, 8)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260'] = {'inputs': ['ecl_027_fcf_burn_to_cash_1260'], 'func': ecl_base_universe_d2_008_ecl_027_fcf_burn_to_cash_1260}


def ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512(ecl_028_debt_to_equity_1512):
    return _base_universe_d2(ecl_028_debt_to_equity_1512, 9)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512'] = {'inputs': ['ecl_028_debt_to_equity_1512'], 'func': ecl_base_universe_d2_009_ecl_028_debt_to_equity_1512}


def ecl_base_universe_d2_010_ecl_029_debt_to_assets_63(ecl_029_debt_to_assets_63):
    return _base_universe_d2(ecl_029_debt_to_assets_63, 10)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_010_ecl_029_debt_to_assets_63'] = {'inputs': ['ecl_029_debt_to_assets_63'], 'func': ecl_base_universe_d2_010_ecl_029_debt_to_assets_63}


def ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21(ecl_031_interest_coverage_stress_21):
    return _base_universe_d2(ecl_031_interest_coverage_stress_21, 11)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21'] = {'inputs': ['ecl_031_interest_coverage_stress_21'], 'func': ecl_base_universe_d2_011_ecl_031_interest_coverage_stress_21}


def ecl_base_universe_d2_012_ecl_036_accrual_gap_189(ecl_036_accrual_gap_189):
    return _base_universe_d2(ecl_036_accrual_gap_189, 12)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_012_ecl_036_accrual_gap_189'] = {'inputs': ['ecl_036_accrual_gap_189'], 'func': ecl_base_universe_d2_012_ecl_036_accrual_gap_189}


def ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504(ecl_039_fcf_burn_to_cash_504):
    return _base_universe_d2(ecl_039_fcf_burn_to_cash_504, 13)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504'] = {'inputs': ['ecl_039_fcf_burn_to_cash_504'], 'func': ecl_base_universe_d2_013_ecl_039_fcf_burn_to_cash_504}


def ecl_base_universe_d2_014_ecl_040_debt_to_equity_756(ecl_040_debt_to_equity_756):
    return _base_universe_d2(ecl_040_debt_to_equity_756, 14)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_014_ecl_040_debt_to_equity_756'] = {'inputs': ['ecl_040_debt_to_equity_756'], 'func': ecl_base_universe_d2_014_ecl_040_debt_to_equity_756}


def ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008(ecl_041_debt_to_assets_1008):
    return _base_universe_d2(ecl_041_debt_to_assets_1008, 15)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008'] = {'inputs': ['ecl_041_debt_to_assets_1008'], 'func': ecl_base_universe_d2_015_ecl_041_debt_to_assets_1008}


def ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512(ecl_043_interest_coverage_stress_1512):
    return _base_universe_d2(ecl_043_interest_coverage_stress_1512, 16)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512'] = {'inputs': ['ecl_043_interest_coverage_stress_1512'], 'func': ecl_base_universe_d2_016_ecl_043_interest_coverage_stress_1512}


def ecl_base_universe_d2_017_ecl_048_accrual_gap_63(ecl_048_accrual_gap_63):
    return _base_universe_d2(ecl_048_accrual_gap_63, 17)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_017_ecl_048_accrual_gap_63'] = {'inputs': ['ecl_048_accrual_gap_63'], 'func': ecl_base_universe_d2_017_ecl_048_accrual_gap_63}


def ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189(ecl_051_fcf_burn_to_cash_189):
    return _base_universe_d2(ecl_051_fcf_burn_to_cash_189, 18)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189'] = {'inputs': ['ecl_051_fcf_burn_to_cash_189'], 'func': ecl_base_universe_d2_018_ecl_051_fcf_burn_to_cash_189}


def ecl_base_universe_d2_019_ecl_052_debt_to_equity_252(ecl_052_debt_to_equity_252):
    return _base_universe_d2(ecl_052_debt_to_equity_252, 19)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_019_ecl_052_debt_to_equity_252'] = {'inputs': ['ecl_052_debt_to_equity_252'], 'func': ecl_base_universe_d2_019_ecl_052_debt_to_equity_252}


def ecl_base_universe_d2_020_ecl_053_debt_to_assets_378(ecl_053_debt_to_assets_378):
    return _base_universe_d2(ecl_053_debt_to_assets_378, 20)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_020_ecl_053_debt_to_assets_378'] = {'inputs': ['ecl_053_debt_to_assets_378'], 'func': ecl_base_universe_d2_020_ecl_053_debt_to_assets_378}


def ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756(ecl_055_interest_coverage_stress_756):
    return _base_universe_d2(ecl_055_interest_coverage_stress_756, 21)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756'] = {'inputs': ['ecl_055_interest_coverage_stress_756'], 'func': ecl_base_universe_d2_021_ecl_055_interest_coverage_stress_756}


def ecl_base_universe_d2_022_ecl_060_accrual_gap_252(ecl_060_accrual_gap_252):
    return _base_universe_d2(ecl_060_accrual_gap_252, 22)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_022_ecl_060_accrual_gap_252'] = {'inputs': ['ecl_060_accrual_gap_252'], 'func': ecl_base_universe_d2_022_ecl_060_accrual_gap_252}


def ecl_base_universe_d2_023_ecl_basefill_001(ecl_basefill_001):
    return _base_universe_d2(ecl_basefill_001, 23)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_023_ecl_basefill_001'] = {'inputs': ['ecl_basefill_001'], 'func': ecl_base_universe_d2_023_ecl_basefill_001}


def ecl_base_universe_d2_024_ecl_basefill_002(ecl_basefill_002):
    return _base_universe_d2(ecl_basefill_002, 24)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_024_ecl_basefill_002'] = {'inputs': ['ecl_basefill_002'], 'func': ecl_base_universe_d2_024_ecl_basefill_002}


def ecl_base_universe_d2_025_ecl_basefill_006(ecl_basefill_006):
    return _base_universe_d2(ecl_basefill_006, 25)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_025_ecl_basefill_006'] = {'inputs': ['ecl_basefill_006'], 'func': ecl_base_universe_d2_025_ecl_basefill_006}


def ecl_base_universe_d2_026_ecl_basefill_008(ecl_basefill_008):
    return _base_universe_d2(ecl_basefill_008, 26)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_026_ecl_basefill_008'] = {'inputs': ['ecl_basefill_008'], 'func': ecl_base_universe_d2_026_ecl_basefill_008}


def ecl_base_universe_d2_027_ecl_basefill_009(ecl_basefill_009):
    return _base_universe_d2(ecl_basefill_009, 27)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_027_ecl_basefill_009'] = {'inputs': ['ecl_basefill_009'], 'func': ecl_base_universe_d2_027_ecl_basefill_009}


def ecl_base_universe_d2_028_ecl_basefill_010(ecl_basefill_010):
    return _base_universe_d2(ecl_basefill_010, 28)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_028_ecl_basefill_010'] = {'inputs': ['ecl_basefill_010'], 'func': ecl_base_universe_d2_028_ecl_basefill_010}


def ecl_base_universe_d2_029_ecl_basefill_011(ecl_basefill_011):
    return _base_universe_d2(ecl_basefill_011, 29)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_029_ecl_basefill_011'] = {'inputs': ['ecl_basefill_011'], 'func': ecl_base_universe_d2_029_ecl_basefill_011}


def ecl_base_universe_d2_030_ecl_basefill_013(ecl_basefill_013):
    return _base_universe_d2(ecl_basefill_013, 30)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_030_ecl_basefill_013'] = {'inputs': ['ecl_basefill_013'], 'func': ecl_base_universe_d2_030_ecl_basefill_013}


def ecl_base_universe_d2_031_ecl_basefill_014(ecl_basefill_014):
    return _base_universe_d2(ecl_basefill_014, 31)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_031_ecl_basefill_014'] = {'inputs': ['ecl_basefill_014'], 'func': ecl_base_universe_d2_031_ecl_basefill_014}


def ecl_base_universe_d2_032_ecl_basefill_015(ecl_basefill_015):
    return _base_universe_d2(ecl_basefill_015, 32)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_032_ecl_basefill_015'] = {'inputs': ['ecl_basefill_015'], 'func': ecl_base_universe_d2_032_ecl_basefill_015}


def ecl_base_universe_d2_033_ecl_basefill_018(ecl_basefill_018):
    return _base_universe_d2(ecl_basefill_018, 33)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_033_ecl_basefill_018'] = {'inputs': ['ecl_basefill_018'], 'func': ecl_base_universe_d2_033_ecl_basefill_018}


def ecl_base_universe_d2_034_ecl_basefill_020(ecl_basefill_020):
    return _base_universe_d2(ecl_basefill_020, 34)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_034_ecl_basefill_020'] = {'inputs': ['ecl_basefill_020'], 'func': ecl_base_universe_d2_034_ecl_basefill_020}


def ecl_base_universe_d2_035_ecl_basefill_021(ecl_basefill_021):
    return _base_universe_d2(ecl_basefill_021, 35)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_035_ecl_basefill_021'] = {'inputs': ['ecl_basefill_021'], 'func': ecl_base_universe_d2_035_ecl_basefill_021}


def ecl_base_universe_d2_036_ecl_basefill_022(ecl_basefill_022):
    return _base_universe_d2(ecl_basefill_022, 36)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_036_ecl_basefill_022'] = {'inputs': ['ecl_basefill_022'], 'func': ecl_base_universe_d2_036_ecl_basefill_022}


def ecl_base_universe_d2_037_ecl_basefill_023(ecl_basefill_023):
    return _base_universe_d2(ecl_basefill_023, 37)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_037_ecl_basefill_023'] = {'inputs': ['ecl_basefill_023'], 'func': ecl_base_universe_d2_037_ecl_basefill_023}


def ecl_base_universe_d2_038_ecl_basefill_025(ecl_basefill_025):
    return _base_universe_d2(ecl_basefill_025, 38)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_038_ecl_basefill_025'] = {'inputs': ['ecl_basefill_025'], 'func': ecl_base_universe_d2_038_ecl_basefill_025}


def ecl_base_universe_d2_039_ecl_basefill_026(ecl_basefill_026):
    return _base_universe_d2(ecl_basefill_026, 39)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_039_ecl_basefill_026'] = {'inputs': ['ecl_basefill_026'], 'func': ecl_base_universe_d2_039_ecl_basefill_026}


def ecl_base_universe_d2_040_ecl_basefill_030(ecl_basefill_030):
    return _base_universe_d2(ecl_basefill_030, 40)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_040_ecl_basefill_030'] = {'inputs': ['ecl_basefill_030'], 'func': ecl_base_universe_d2_040_ecl_basefill_030}


def ecl_base_universe_d2_041_ecl_basefill_032(ecl_basefill_032):
    return _base_universe_d2(ecl_basefill_032, 41)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_041_ecl_basefill_032'] = {'inputs': ['ecl_basefill_032'], 'func': ecl_base_universe_d2_041_ecl_basefill_032}


def ecl_base_universe_d2_042_ecl_basefill_033(ecl_basefill_033):
    return _base_universe_d2(ecl_basefill_033, 42)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_042_ecl_basefill_033'] = {'inputs': ['ecl_basefill_033'], 'func': ecl_base_universe_d2_042_ecl_basefill_033}


def ecl_base_universe_d2_043_ecl_basefill_034(ecl_basefill_034):
    return _base_universe_d2(ecl_basefill_034, 43)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_043_ecl_basefill_034'] = {'inputs': ['ecl_basefill_034'], 'func': ecl_base_universe_d2_043_ecl_basefill_034}


def ecl_base_universe_d2_044_ecl_basefill_035(ecl_basefill_035):
    return _base_universe_d2(ecl_basefill_035, 44)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_044_ecl_basefill_035'] = {'inputs': ['ecl_basefill_035'], 'func': ecl_base_universe_d2_044_ecl_basefill_035}


def ecl_base_universe_d2_045_ecl_basefill_037(ecl_basefill_037):
    return _base_universe_d2(ecl_basefill_037, 45)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_045_ecl_basefill_037'] = {'inputs': ['ecl_basefill_037'], 'func': ecl_base_universe_d2_045_ecl_basefill_037}


def ecl_base_universe_d2_046_ecl_basefill_038(ecl_basefill_038):
    return _base_universe_d2(ecl_basefill_038, 46)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_046_ecl_basefill_038'] = {'inputs': ['ecl_basefill_038'], 'func': ecl_base_universe_d2_046_ecl_basefill_038}


def ecl_base_universe_d2_047_ecl_basefill_042(ecl_basefill_042):
    return _base_universe_d2(ecl_basefill_042, 47)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_047_ecl_basefill_042'] = {'inputs': ['ecl_basefill_042'], 'func': ecl_base_universe_d2_047_ecl_basefill_042}


def ecl_base_universe_d2_048_ecl_basefill_044(ecl_basefill_044):
    return _base_universe_d2(ecl_basefill_044, 48)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_048_ecl_basefill_044'] = {'inputs': ['ecl_basefill_044'], 'func': ecl_base_universe_d2_048_ecl_basefill_044}


def ecl_base_universe_d2_049_ecl_basefill_045(ecl_basefill_045):
    return _base_universe_d2(ecl_basefill_045, 49)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_049_ecl_basefill_045'] = {'inputs': ['ecl_basefill_045'], 'func': ecl_base_universe_d2_049_ecl_basefill_045}


def ecl_base_universe_d2_050_ecl_basefill_046(ecl_basefill_046):
    return _base_universe_d2(ecl_basefill_046, 50)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_050_ecl_basefill_046'] = {'inputs': ['ecl_basefill_046'], 'func': ecl_base_universe_d2_050_ecl_basefill_046}


def ecl_base_universe_d2_051_ecl_basefill_047(ecl_basefill_047):
    return _base_universe_d2(ecl_basefill_047, 51)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_051_ecl_basefill_047'] = {'inputs': ['ecl_basefill_047'], 'func': ecl_base_universe_d2_051_ecl_basefill_047}


def ecl_base_universe_d2_052_ecl_basefill_049(ecl_basefill_049):
    return _base_universe_d2(ecl_basefill_049, 52)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_052_ecl_basefill_049'] = {'inputs': ['ecl_basefill_049'], 'func': ecl_base_universe_d2_052_ecl_basefill_049}


def ecl_base_universe_d2_053_ecl_basefill_050(ecl_basefill_050):
    return _base_universe_d2(ecl_basefill_050, 53)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_053_ecl_basefill_050'] = {'inputs': ['ecl_basefill_050'], 'func': ecl_base_universe_d2_053_ecl_basefill_050}


def ecl_base_universe_d2_054_ecl_basefill_054(ecl_basefill_054):
    return _base_universe_d2(ecl_basefill_054, 54)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_054_ecl_basefill_054'] = {'inputs': ['ecl_basefill_054'], 'func': ecl_base_universe_d2_054_ecl_basefill_054}


def ecl_base_universe_d2_055_ecl_basefill_056(ecl_basefill_056):
    return _base_universe_d2(ecl_basefill_056, 55)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_055_ecl_basefill_056'] = {'inputs': ['ecl_basefill_056'], 'func': ecl_base_universe_d2_055_ecl_basefill_056}


def ecl_base_universe_d2_056_ecl_basefill_057(ecl_basefill_057):
    return _base_universe_d2(ecl_basefill_057, 56)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_056_ecl_basefill_057'] = {'inputs': ['ecl_basefill_057'], 'func': ecl_base_universe_d2_056_ecl_basefill_057}


def ecl_base_universe_d2_057_ecl_basefill_058(ecl_basefill_058):
    return _base_universe_d2(ecl_basefill_058, 57)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_057_ecl_basefill_058'] = {'inputs': ['ecl_basefill_058'], 'func': ecl_base_universe_d2_057_ecl_basefill_058}


def ecl_base_universe_d2_058_ecl_basefill_059(ecl_basefill_059):
    return _base_universe_d2(ecl_basefill_059, 58)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_058_ecl_basefill_059'] = {'inputs': ['ecl_basefill_059'], 'func': ecl_base_universe_d2_058_ecl_basefill_059}


def ecl_base_universe_d2_059_ecl_basefill_061(ecl_basefill_061):
    return _base_universe_d2(ecl_basefill_061, 59)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_059_ecl_basefill_061'] = {'inputs': ['ecl_basefill_061'], 'func': ecl_base_universe_d2_059_ecl_basefill_061}


def ecl_base_universe_d2_060_ecl_basefill_062(ecl_basefill_062):
    return _base_universe_d2(ecl_basefill_062, 60)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_060_ecl_basefill_062'] = {'inputs': ['ecl_basefill_062'], 'func': ecl_base_universe_d2_060_ecl_basefill_062}


def ecl_base_universe_d2_061_ecl_basefill_063(ecl_basefill_063):
    return _base_universe_d2(ecl_basefill_063, 61)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_061_ecl_basefill_063'] = {'inputs': ['ecl_basefill_063'], 'func': ecl_base_universe_d2_061_ecl_basefill_063}


def ecl_base_universe_d2_062_ecl_basefill_064(ecl_basefill_064):
    return _base_universe_d2(ecl_basefill_064, 62)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_062_ecl_basefill_064'] = {'inputs': ['ecl_basefill_064'], 'func': ecl_base_universe_d2_062_ecl_basefill_064}


def ecl_base_universe_d2_063_ecl_basefill_065(ecl_basefill_065):
    return _base_universe_d2(ecl_basefill_065, 63)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_063_ecl_basefill_065'] = {'inputs': ['ecl_basefill_065'], 'func': ecl_base_universe_d2_063_ecl_basefill_065}


def ecl_base_universe_d2_064_ecl_basefill_066(ecl_basefill_066):
    return _base_universe_d2(ecl_basefill_066, 64)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_064_ecl_basefill_066'] = {'inputs': ['ecl_basefill_066'], 'func': ecl_base_universe_d2_064_ecl_basefill_066}


def ecl_base_universe_d2_065_ecl_basefill_067(ecl_basefill_067):
    return _base_universe_d2(ecl_basefill_067, 65)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_065_ecl_basefill_067'] = {'inputs': ['ecl_basefill_067'], 'func': ecl_base_universe_d2_065_ecl_basefill_067}


def ecl_base_universe_d2_066_ecl_basefill_068(ecl_basefill_068):
    return _base_universe_d2(ecl_basefill_068, 66)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_066_ecl_basefill_068'] = {'inputs': ['ecl_basefill_068'], 'func': ecl_base_universe_d2_066_ecl_basefill_068}


def ecl_base_universe_d2_067_ecl_basefill_069(ecl_basefill_069):
    return _base_universe_d2(ecl_basefill_069, 67)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_067_ecl_basefill_069'] = {'inputs': ['ecl_basefill_069'], 'func': ecl_base_universe_d2_067_ecl_basefill_069}


def ecl_base_universe_d2_068_ecl_basefill_070(ecl_basefill_070):
    return _base_universe_d2(ecl_basefill_070, 68)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_068_ecl_basefill_070'] = {'inputs': ['ecl_basefill_070'], 'func': ecl_base_universe_d2_068_ecl_basefill_070}


def ecl_base_universe_d2_069_ecl_basefill_071(ecl_basefill_071):
    return _base_universe_d2(ecl_basefill_071, 69)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_069_ecl_basefill_071'] = {'inputs': ['ecl_basefill_071'], 'func': ecl_base_universe_d2_069_ecl_basefill_071}


def ecl_base_universe_d2_070_ecl_basefill_072(ecl_basefill_072):
    return _base_universe_d2(ecl_basefill_072, 70)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_070_ecl_basefill_072'] = {'inputs': ['ecl_basefill_072'], 'func': ecl_base_universe_d2_070_ecl_basefill_072}


def ecl_base_universe_d2_071_ecl_basefill_073(ecl_basefill_073):
    return _base_universe_d2(ecl_basefill_073, 71)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_071_ecl_basefill_073'] = {'inputs': ['ecl_basefill_073'], 'func': ecl_base_universe_d2_071_ecl_basefill_073}


def ecl_base_universe_d2_072_ecl_basefill_074(ecl_basefill_074):
    return _base_universe_d2(ecl_basefill_074, 72)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_072_ecl_basefill_074'] = {'inputs': ['ecl_basefill_074'], 'func': ecl_base_universe_d2_072_ecl_basefill_074}


def ecl_base_universe_d2_073_ecl_basefill_075(ecl_basefill_075):
    return _base_universe_d2(ecl_basefill_075, 73)
ECL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ecl_base_universe_d2_073_ecl_basefill_075'] = {'inputs': ['ecl_basefill_075'], 'func': ecl_base_universe_d2_073_ecl_basefill_075}
