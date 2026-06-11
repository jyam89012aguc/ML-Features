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



def icv_151_icv_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def icv_152_icv_007_interest_coverage_stress_252_roc_42(icv_007_interest_coverage_stress_252):
    feature = _s(icv_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def icv_153_icv_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def icv_154_icv_019_interest_coverage_stress_84_roc_378(icv_019_interest_coverage_stress_84):
    feature = _s(icv_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def icv_155_icv_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















INTEREST_COVERAGE_REGISTRY_2ND_DERIVATIVES = {
    'icv_151_icv_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': icv_151_icv_001_netinc_decline_1_roc_1},
    'icv_152_icv_007_interest_coverage_stress_252_roc_42': {'inputs': ['icv_007_interest_coverage_stress_252'], 'func': icv_152_icv_007_interest_coverage_stress_252_roc_42},
    'icv_153_icv_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': icv_153_icv_013_netinc_decline_1_roc_126},
    'icv_154_icv_019_interest_coverage_stress_84_roc_378': {'inputs': ['icv_019_interest_coverage_stress_84'], 'func': icv_154_icv_019_interest_coverage_stress_84_roc_378},
    'icv_155_icv_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': icv_155_icv_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ic_replacement_d2_001(ic_replacement_001):
    feature = _clean(ic_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_001'] = {'inputs': ['ic_replacement_001'], 'func': ic_replacement_d2_001}


def ic_replacement_d2_002(ic_replacement_002):
    feature = _clean(ic_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_002'] = {'inputs': ['ic_replacement_002'], 'func': ic_replacement_d2_002}


def ic_replacement_d2_003(ic_replacement_003):
    feature = _clean(ic_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_003'] = {'inputs': ['ic_replacement_003'], 'func': ic_replacement_d2_003}


def ic_replacement_d2_004(ic_replacement_004):
    feature = _clean(ic_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_004'] = {'inputs': ['ic_replacement_004'], 'func': ic_replacement_d2_004}


def ic_replacement_d2_005(ic_replacement_005):
    feature = _clean(ic_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_005'] = {'inputs': ['ic_replacement_005'], 'func': ic_replacement_d2_005}


def ic_replacement_d2_006(ic_replacement_006):
    feature = _clean(ic_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_006'] = {'inputs': ['ic_replacement_006'], 'func': ic_replacement_d2_006}


def ic_replacement_d2_007(ic_replacement_007):
    feature = _clean(ic_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_007'] = {'inputs': ['ic_replacement_007'], 'func': ic_replacement_d2_007}


def ic_replacement_d2_008(ic_replacement_008):
    feature = _clean(ic_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_008'] = {'inputs': ['ic_replacement_008'], 'func': ic_replacement_d2_008}


def ic_replacement_d2_009(ic_replacement_009):
    feature = _clean(ic_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_009'] = {'inputs': ['ic_replacement_009'], 'func': ic_replacement_d2_009}


def ic_replacement_d2_010(ic_replacement_010):
    feature = _clean(ic_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_010'] = {'inputs': ['ic_replacement_010'], 'func': ic_replacement_d2_010}


def ic_replacement_d2_011(ic_replacement_011):
    feature = _clean(ic_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_011'] = {'inputs': ['ic_replacement_011'], 'func': ic_replacement_d2_011}


def ic_replacement_d2_012(ic_replacement_012):
    feature = _clean(ic_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_012'] = {'inputs': ['ic_replacement_012'], 'func': ic_replacement_d2_012}


def ic_replacement_d2_013(ic_replacement_013):
    feature = _clean(ic_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_013'] = {'inputs': ['ic_replacement_013'], 'func': ic_replacement_d2_013}


def ic_replacement_d2_014(ic_replacement_014):
    feature = _clean(ic_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_014'] = {'inputs': ['ic_replacement_014'], 'func': ic_replacement_d2_014}


def ic_replacement_d2_015(ic_replacement_015):
    feature = _clean(ic_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_015'] = {'inputs': ['ic_replacement_015'], 'func': ic_replacement_d2_015}


def ic_replacement_d2_016(ic_replacement_016):
    feature = _clean(ic_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_016'] = {'inputs': ['ic_replacement_016'], 'func': ic_replacement_d2_016}


def ic_replacement_d2_017(ic_replacement_017):
    feature = _clean(ic_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_017'] = {'inputs': ['ic_replacement_017'], 'func': ic_replacement_d2_017}


def ic_replacement_d2_018(ic_replacement_018):
    feature = _clean(ic_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_018'] = {'inputs': ['ic_replacement_018'], 'func': ic_replacement_d2_018}


def ic_replacement_d2_019(ic_replacement_019):
    feature = _clean(ic_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_019'] = {'inputs': ['ic_replacement_019'], 'func': ic_replacement_d2_019}


def ic_replacement_d2_020(ic_replacement_020):
    feature = _clean(ic_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_020'] = {'inputs': ['ic_replacement_020'], 'func': ic_replacement_d2_020}


def ic_replacement_d2_021(ic_replacement_021):
    feature = _clean(ic_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_021'] = {'inputs': ['ic_replacement_021'], 'func': ic_replacement_d2_021}


def ic_replacement_d2_022(ic_replacement_022):
    feature = _clean(ic_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_022'] = {'inputs': ['ic_replacement_022'], 'func': ic_replacement_d2_022}


def ic_replacement_d2_023(ic_replacement_023):
    feature = _clean(ic_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_023'] = {'inputs': ['ic_replacement_023'], 'func': ic_replacement_d2_023}


def ic_replacement_d2_024(ic_replacement_024):
    feature = _clean(ic_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_024'] = {'inputs': ['ic_replacement_024'], 'func': ic_replacement_d2_024}


def ic_replacement_d2_025(ic_replacement_025):
    feature = _clean(ic_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_025'] = {'inputs': ['ic_replacement_025'], 'func': ic_replacement_d2_025}


def ic_replacement_d2_026(ic_replacement_026):
    feature = _clean(ic_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_026'] = {'inputs': ['ic_replacement_026'], 'func': ic_replacement_d2_026}


def ic_replacement_d2_027(ic_replacement_027):
    feature = _clean(ic_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_027'] = {'inputs': ['ic_replacement_027'], 'func': ic_replacement_d2_027}


def ic_replacement_d2_028(ic_replacement_028):
    feature = _clean(ic_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_028'] = {'inputs': ['ic_replacement_028'], 'func': ic_replacement_d2_028}


def ic_replacement_d2_029(ic_replacement_029):
    feature = _clean(ic_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_029'] = {'inputs': ['ic_replacement_029'], 'func': ic_replacement_d2_029}


def ic_replacement_d2_030(ic_replacement_030):
    feature = _clean(ic_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_030'] = {'inputs': ['ic_replacement_030'], 'func': ic_replacement_d2_030}


def ic_replacement_d2_031(ic_replacement_031):
    feature = _clean(ic_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_031'] = {'inputs': ['ic_replacement_031'], 'func': ic_replacement_d2_031}


def ic_replacement_d2_032(ic_replacement_032):
    feature = _clean(ic_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_032'] = {'inputs': ['ic_replacement_032'], 'func': ic_replacement_d2_032}


def ic_replacement_d2_033(ic_replacement_033):
    feature = _clean(ic_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_033'] = {'inputs': ['ic_replacement_033'], 'func': ic_replacement_d2_033}


def ic_replacement_d2_034(ic_replacement_034):
    feature = _clean(ic_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_034'] = {'inputs': ['ic_replacement_034'], 'func': ic_replacement_d2_034}


def ic_replacement_d2_035(ic_replacement_035):
    feature = _clean(ic_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_035'] = {'inputs': ['ic_replacement_035'], 'func': ic_replacement_d2_035}


def ic_replacement_d2_036(ic_replacement_036):
    feature = _clean(ic_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_036'] = {'inputs': ['ic_replacement_036'], 'func': ic_replacement_d2_036}


def ic_replacement_d2_037(ic_replacement_037):
    feature = _clean(ic_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_037'] = {'inputs': ['ic_replacement_037'], 'func': ic_replacement_d2_037}


def ic_replacement_d2_038(ic_replacement_038):
    feature = _clean(ic_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_038'] = {'inputs': ['ic_replacement_038'], 'func': ic_replacement_d2_038}


def ic_replacement_d2_039(ic_replacement_039):
    feature = _clean(ic_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_039'] = {'inputs': ['ic_replacement_039'], 'func': ic_replacement_d2_039}


def ic_replacement_d2_040(ic_replacement_040):
    feature = _clean(ic_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_040'] = {'inputs': ['ic_replacement_040'], 'func': ic_replacement_d2_040}


def ic_replacement_d2_041(ic_replacement_041):
    feature = _clean(ic_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_041'] = {'inputs': ['ic_replacement_041'], 'func': ic_replacement_d2_041}


def ic_replacement_d2_042(ic_replacement_042):
    feature = _clean(ic_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_042'] = {'inputs': ['ic_replacement_042'], 'func': ic_replacement_d2_042}


def ic_replacement_d2_043(ic_replacement_043):
    feature = _clean(ic_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_043'] = {'inputs': ['ic_replacement_043'], 'func': ic_replacement_d2_043}


def ic_replacement_d2_044(ic_replacement_044):
    feature = _clean(ic_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_044'] = {'inputs': ['ic_replacement_044'], 'func': ic_replacement_d2_044}


def ic_replacement_d2_045(ic_replacement_045):
    feature = _clean(ic_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_045'] = {'inputs': ['ic_replacement_045'], 'func': ic_replacement_d2_045}


def ic_replacement_d2_046(ic_replacement_046):
    feature = _clean(ic_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_046'] = {'inputs': ['ic_replacement_046'], 'func': ic_replacement_d2_046}


def ic_replacement_d2_047(ic_replacement_047):
    feature = _clean(ic_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_047'] = {'inputs': ['ic_replacement_047'], 'func': ic_replacement_d2_047}


def ic_replacement_d2_048(ic_replacement_048):
    feature = _clean(ic_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_048'] = {'inputs': ['ic_replacement_048'], 'func': ic_replacement_d2_048}


def ic_replacement_d2_049(ic_replacement_049):
    feature = _clean(ic_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_049'] = {'inputs': ['ic_replacement_049'], 'func': ic_replacement_d2_049}


def ic_replacement_d2_050(ic_replacement_050):
    feature = _clean(ic_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_050'] = {'inputs': ['ic_replacement_050'], 'func': ic_replacement_d2_050}


def ic_replacement_d2_051(ic_replacement_051):
    feature = _clean(ic_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_051'] = {'inputs': ['ic_replacement_051'], 'func': ic_replacement_d2_051}


def ic_replacement_d2_052(ic_replacement_052):
    feature = _clean(ic_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_052'] = {'inputs': ['ic_replacement_052'], 'func': ic_replacement_d2_052}


def ic_replacement_d2_053(ic_replacement_053):
    feature = _clean(ic_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_053'] = {'inputs': ['ic_replacement_053'], 'func': ic_replacement_d2_053}


def ic_replacement_d2_054(ic_replacement_054):
    feature = _clean(ic_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_054'] = {'inputs': ['ic_replacement_054'], 'func': ic_replacement_d2_054}


def ic_replacement_d2_055(ic_replacement_055):
    feature = _clean(ic_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_055'] = {'inputs': ['ic_replacement_055'], 'func': ic_replacement_d2_055}


def ic_replacement_d2_056(ic_replacement_056):
    feature = _clean(ic_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_056'] = {'inputs': ['ic_replacement_056'], 'func': ic_replacement_d2_056}


def ic_replacement_d2_057(ic_replacement_057):
    feature = _clean(ic_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_057'] = {'inputs': ['ic_replacement_057'], 'func': ic_replacement_d2_057}


def ic_replacement_d2_058(ic_replacement_058):
    feature = _clean(ic_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_058'] = {'inputs': ['ic_replacement_058'], 'func': ic_replacement_d2_058}


def ic_replacement_d2_059(ic_replacement_059):
    feature = _clean(ic_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_059'] = {'inputs': ['ic_replacement_059'], 'func': ic_replacement_d2_059}


def ic_replacement_d2_060(ic_replacement_060):
    feature = _clean(ic_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_060'] = {'inputs': ['ic_replacement_060'], 'func': ic_replacement_d2_060}


def ic_replacement_d2_061(ic_replacement_061):
    feature = _clean(ic_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_061'] = {'inputs': ['ic_replacement_061'], 'func': ic_replacement_d2_061}


def ic_replacement_d2_062(ic_replacement_062):
    feature = _clean(ic_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_062'] = {'inputs': ['ic_replacement_062'], 'func': ic_replacement_d2_062}


def ic_replacement_d2_063(ic_replacement_063):
    feature = _clean(ic_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_063'] = {'inputs': ['ic_replacement_063'], 'func': ic_replacement_d2_063}


def ic_replacement_d2_064(ic_replacement_064):
    feature = _clean(ic_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_064'] = {'inputs': ['ic_replacement_064'], 'func': ic_replacement_d2_064}


def ic_replacement_d2_065(ic_replacement_065):
    feature = _clean(ic_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_065'] = {'inputs': ['ic_replacement_065'], 'func': ic_replacement_d2_065}


def ic_replacement_d2_066(ic_replacement_066):
    feature = _clean(ic_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_066'] = {'inputs': ['ic_replacement_066'], 'func': ic_replacement_d2_066}


def ic_replacement_d2_067(ic_replacement_067):
    feature = _clean(ic_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_067'] = {'inputs': ['ic_replacement_067'], 'func': ic_replacement_d2_067}


def ic_replacement_d2_068(ic_replacement_068):
    feature = _clean(ic_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_068'] = {'inputs': ['ic_replacement_068'], 'func': ic_replacement_d2_068}


def ic_replacement_d2_069(ic_replacement_069):
    feature = _clean(ic_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_069'] = {'inputs': ['ic_replacement_069'], 'func': ic_replacement_d2_069}


def ic_replacement_d2_070(ic_replacement_070):
    feature = _clean(ic_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_070'] = {'inputs': ['ic_replacement_070'], 'func': ic_replacement_d2_070}


def ic_replacement_d2_071(ic_replacement_071):
    feature = _clean(ic_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_071'] = {'inputs': ['ic_replacement_071'], 'func': ic_replacement_d2_071}


def ic_replacement_d2_072(ic_replacement_072):
    feature = _clean(ic_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_072'] = {'inputs': ['ic_replacement_072'], 'func': ic_replacement_d2_072}


def ic_replacement_d2_073(ic_replacement_073):
    feature = _clean(ic_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_073'] = {'inputs': ['ic_replacement_073'], 'func': ic_replacement_d2_073}


def ic_replacement_d2_074(ic_replacement_074):
    feature = _clean(ic_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_074'] = {'inputs': ['ic_replacement_074'], 'func': ic_replacement_d2_074}


def ic_replacement_d2_075(ic_replacement_075):
    feature = _clean(ic_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_075'] = {'inputs': ['ic_replacement_075'], 'func': ic_replacement_d2_075}


def ic_replacement_d2_076(ic_replacement_076):
    feature = _clean(ic_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_076'] = {'inputs': ['ic_replacement_076'], 'func': ic_replacement_d2_076}


def ic_replacement_d2_077(ic_replacement_077):
    feature = _clean(ic_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_077'] = {'inputs': ['ic_replacement_077'], 'func': ic_replacement_d2_077}


def ic_replacement_d2_078(ic_replacement_078):
    feature = _clean(ic_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_078'] = {'inputs': ['ic_replacement_078'], 'func': ic_replacement_d2_078}


def ic_replacement_d2_079(ic_replacement_079):
    feature = _clean(ic_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_079'] = {'inputs': ['ic_replacement_079'], 'func': ic_replacement_d2_079}


def ic_replacement_d2_080(ic_replacement_080):
    feature = _clean(ic_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_080'] = {'inputs': ['ic_replacement_080'], 'func': ic_replacement_d2_080}


def ic_replacement_d2_081(ic_replacement_081):
    feature = _clean(ic_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_081'] = {'inputs': ['ic_replacement_081'], 'func': ic_replacement_d2_081}


def ic_replacement_d2_082(ic_replacement_082):
    feature = _clean(ic_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_082'] = {'inputs': ['ic_replacement_082'], 'func': ic_replacement_d2_082}


def ic_replacement_d2_083(ic_replacement_083):
    feature = _clean(ic_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_083'] = {'inputs': ['ic_replacement_083'], 'func': ic_replacement_d2_083}


def ic_replacement_d2_084(ic_replacement_084):
    feature = _clean(ic_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_084'] = {'inputs': ['ic_replacement_084'], 'func': ic_replacement_d2_084}


def ic_replacement_d2_085(ic_replacement_085):
    feature = _clean(ic_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_085'] = {'inputs': ['ic_replacement_085'], 'func': ic_replacement_d2_085}


def ic_replacement_d2_086(ic_replacement_086):
    feature = _clean(ic_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_086'] = {'inputs': ['ic_replacement_086'], 'func': ic_replacement_d2_086}


def ic_replacement_d2_087(ic_replacement_087):
    feature = _clean(ic_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_087'] = {'inputs': ['ic_replacement_087'], 'func': ic_replacement_d2_087}


def ic_replacement_d2_088(ic_replacement_088):
    feature = _clean(ic_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_088'] = {'inputs': ['ic_replacement_088'], 'func': ic_replacement_d2_088}


def ic_replacement_d2_089(ic_replacement_089):
    feature = _clean(ic_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_089'] = {'inputs': ['ic_replacement_089'], 'func': ic_replacement_d2_089}


def ic_replacement_d2_090(ic_replacement_090):
    feature = _clean(ic_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_090'] = {'inputs': ['ic_replacement_090'], 'func': ic_replacement_d2_090}


def ic_replacement_d2_091(ic_replacement_091):
    feature = _clean(ic_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_091'] = {'inputs': ['ic_replacement_091'], 'func': ic_replacement_d2_091}


def ic_replacement_d2_092(ic_replacement_092):
    feature = _clean(ic_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_092'] = {'inputs': ['ic_replacement_092'], 'func': ic_replacement_d2_092}


def ic_replacement_d2_093(ic_replacement_093):
    feature = _clean(ic_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_093'] = {'inputs': ['ic_replacement_093'], 'func': ic_replacement_d2_093}


def ic_replacement_d2_094(ic_replacement_094):
    feature = _clean(ic_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_094'] = {'inputs': ['ic_replacement_094'], 'func': ic_replacement_d2_094}


def ic_replacement_d2_095(ic_replacement_095):
    feature = _clean(ic_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_095'] = {'inputs': ['ic_replacement_095'], 'func': ic_replacement_d2_095}


def ic_replacement_d2_096(ic_replacement_096):
    feature = _clean(ic_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_096'] = {'inputs': ['ic_replacement_096'], 'func': ic_replacement_d2_096}


def ic_replacement_d2_097(ic_replacement_097):
    feature = _clean(ic_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_097'] = {'inputs': ['ic_replacement_097'], 'func': ic_replacement_d2_097}


def ic_replacement_d2_098(ic_replacement_098):
    feature = _clean(ic_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_098'] = {'inputs': ['ic_replacement_098'], 'func': ic_replacement_d2_098}


def ic_replacement_d2_099(ic_replacement_099):
    feature = _clean(ic_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_099'] = {'inputs': ['ic_replacement_099'], 'func': ic_replacement_d2_099}


def ic_replacement_d2_100(ic_replacement_100):
    feature = _clean(ic_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_100'] = {'inputs': ['ic_replacement_100'], 'func': ic_replacement_d2_100}


def ic_replacement_d2_101(ic_replacement_101):
    feature = _clean(ic_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_101'] = {'inputs': ['ic_replacement_101'], 'func': ic_replacement_d2_101}


def ic_replacement_d2_102(ic_replacement_102):
    feature = _clean(ic_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_102'] = {'inputs': ['ic_replacement_102'], 'func': ic_replacement_d2_102}


def ic_replacement_d2_103(ic_replacement_103):
    feature = _clean(ic_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_103'] = {'inputs': ['ic_replacement_103'], 'func': ic_replacement_d2_103}


def ic_replacement_d2_104(ic_replacement_104):
    feature = _clean(ic_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_104'] = {'inputs': ['ic_replacement_104'], 'func': ic_replacement_d2_104}


def ic_replacement_d2_105(ic_replacement_105):
    feature = _clean(ic_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_105'] = {'inputs': ['ic_replacement_105'], 'func': ic_replacement_d2_105}


def ic_replacement_d2_106(ic_replacement_106):
    feature = _clean(ic_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_106'] = {'inputs': ['ic_replacement_106'], 'func': ic_replacement_d2_106}


def ic_replacement_d2_107(ic_replacement_107):
    feature = _clean(ic_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_107'] = {'inputs': ['ic_replacement_107'], 'func': ic_replacement_d2_107}


def ic_replacement_d2_108(ic_replacement_108):
    feature = _clean(ic_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_108'] = {'inputs': ['ic_replacement_108'], 'func': ic_replacement_d2_108}


def ic_replacement_d2_109(ic_replacement_109):
    feature = _clean(ic_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_109'] = {'inputs': ['ic_replacement_109'], 'func': ic_replacement_d2_109}


def ic_replacement_d2_110(ic_replacement_110):
    feature = _clean(ic_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_110'] = {'inputs': ['ic_replacement_110'], 'func': ic_replacement_d2_110}


def ic_replacement_d2_111(ic_replacement_111):
    feature = _clean(ic_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_111'] = {'inputs': ['ic_replacement_111'], 'func': ic_replacement_d2_111}


def ic_replacement_d2_112(ic_replacement_112):
    feature = _clean(ic_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_112'] = {'inputs': ['ic_replacement_112'], 'func': ic_replacement_d2_112}


def ic_replacement_d2_113(ic_replacement_113):
    feature = _clean(ic_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_113'] = {'inputs': ['ic_replacement_113'], 'func': ic_replacement_d2_113}


def ic_replacement_d2_114(ic_replacement_114):
    feature = _clean(ic_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_114'] = {'inputs': ['ic_replacement_114'], 'func': ic_replacement_d2_114}


def ic_replacement_d2_115(ic_replacement_115):
    feature = _clean(ic_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_115'] = {'inputs': ['ic_replacement_115'], 'func': ic_replacement_d2_115}


def ic_replacement_d2_116(ic_replacement_116):
    feature = _clean(ic_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_116'] = {'inputs': ['ic_replacement_116'], 'func': ic_replacement_d2_116}


def ic_replacement_d2_117(ic_replacement_117):
    feature = _clean(ic_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_117'] = {'inputs': ['ic_replacement_117'], 'func': ic_replacement_d2_117}


def ic_replacement_d2_118(ic_replacement_118):
    feature = _clean(ic_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_118'] = {'inputs': ['ic_replacement_118'], 'func': ic_replacement_d2_118}


def ic_replacement_d2_119(ic_replacement_119):
    feature = _clean(ic_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_119'] = {'inputs': ['ic_replacement_119'], 'func': ic_replacement_d2_119}


def ic_replacement_d2_120(ic_replacement_120):
    feature = _clean(ic_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_120'] = {'inputs': ['ic_replacement_120'], 'func': ic_replacement_d2_120}


def ic_replacement_d2_121(ic_replacement_121):
    feature = _clean(ic_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_121'] = {'inputs': ['ic_replacement_121'], 'func': ic_replacement_d2_121}


def ic_replacement_d2_122(ic_replacement_122):
    feature = _clean(ic_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_122'] = {'inputs': ['ic_replacement_122'], 'func': ic_replacement_d2_122}


def ic_replacement_d2_123(ic_replacement_123):
    feature = _clean(ic_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_123'] = {'inputs': ['ic_replacement_123'], 'func': ic_replacement_d2_123}


def ic_replacement_d2_124(ic_replacement_124):
    feature = _clean(ic_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_124'] = {'inputs': ['ic_replacement_124'], 'func': ic_replacement_d2_124}


def ic_replacement_d2_125(ic_replacement_125):
    feature = _clean(ic_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_125'] = {'inputs': ['ic_replacement_125'], 'func': ic_replacement_d2_125}


def ic_replacement_d2_126(ic_replacement_126):
    feature = _clean(ic_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_126'] = {'inputs': ['ic_replacement_126'], 'func': ic_replacement_d2_126}


def ic_replacement_d2_127(ic_replacement_127):
    feature = _clean(ic_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_127'] = {'inputs': ['ic_replacement_127'], 'func': ic_replacement_d2_127}


def ic_replacement_d2_128(ic_replacement_128):
    feature = _clean(ic_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_128'] = {'inputs': ['ic_replacement_128'], 'func': ic_replacement_d2_128}


def ic_replacement_d2_129(ic_replacement_129):
    feature = _clean(ic_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_129'] = {'inputs': ['ic_replacement_129'], 'func': ic_replacement_d2_129}


def ic_replacement_d2_130(ic_replacement_130):
    feature = _clean(ic_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_130'] = {'inputs': ['ic_replacement_130'], 'func': ic_replacement_d2_130}


def ic_replacement_d2_131(ic_replacement_131):
    feature = _clean(ic_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_131'] = {'inputs': ['ic_replacement_131'], 'func': ic_replacement_d2_131}


def ic_replacement_d2_132(ic_replacement_132):
    feature = _clean(ic_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_132'] = {'inputs': ['ic_replacement_132'], 'func': ic_replacement_d2_132}


def ic_replacement_d2_133(ic_replacement_133):
    feature = _clean(ic_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_133'] = {'inputs': ['ic_replacement_133'], 'func': ic_replacement_d2_133}


def ic_replacement_d2_134(ic_replacement_134):
    feature = _clean(ic_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_134'] = {'inputs': ['ic_replacement_134'], 'func': ic_replacement_d2_134}


def ic_replacement_d2_135(ic_replacement_135):
    feature = _clean(ic_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_135'] = {'inputs': ['ic_replacement_135'], 'func': ic_replacement_d2_135}


def ic_replacement_d2_136(ic_replacement_136):
    feature = _clean(ic_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_136'] = {'inputs': ['ic_replacement_136'], 'func': ic_replacement_d2_136}


def ic_replacement_d2_137(ic_replacement_137):
    feature = _clean(ic_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_137'] = {'inputs': ['ic_replacement_137'], 'func': ic_replacement_d2_137}


def ic_replacement_d2_138(ic_replacement_138):
    feature = _clean(ic_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_138'] = {'inputs': ['ic_replacement_138'], 'func': ic_replacement_d2_138}


def ic_replacement_d2_139(ic_replacement_139):
    feature = _clean(ic_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_139'] = {'inputs': ['ic_replacement_139'], 'func': ic_replacement_d2_139}


def ic_replacement_d2_140(ic_replacement_140):
    feature = _clean(ic_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_140'] = {'inputs': ['ic_replacement_140'], 'func': ic_replacement_d2_140}


def ic_replacement_d2_141(ic_replacement_141):
    feature = _clean(ic_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_141'] = {'inputs': ['ic_replacement_141'], 'func': ic_replacement_d2_141}


def ic_replacement_d2_142(ic_replacement_142):
    feature = _clean(ic_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_142'] = {'inputs': ['ic_replacement_142'], 'func': ic_replacement_d2_142}


def ic_replacement_d2_143(ic_replacement_143):
    feature = _clean(ic_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_143'] = {'inputs': ['ic_replacement_143'], 'func': ic_replacement_d2_143}


def ic_replacement_d2_144(ic_replacement_144):
    feature = _clean(ic_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_144'] = {'inputs': ['ic_replacement_144'], 'func': ic_replacement_d2_144}


def ic_replacement_d2_145(ic_replacement_145):
    feature = _clean(ic_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_145'] = {'inputs': ['ic_replacement_145'], 'func': ic_replacement_d2_145}


def ic_replacement_d2_146(ic_replacement_146):
    feature = _clean(ic_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_146'] = {'inputs': ['ic_replacement_146'], 'func': ic_replacement_d2_146}


def ic_replacement_d2_147(ic_replacement_147):
    feature = _clean(ic_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_147'] = {'inputs': ['ic_replacement_147'], 'func': ic_replacement_d2_147}


def ic_replacement_d2_148(ic_replacement_148):
    feature = _clean(ic_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_148'] = {'inputs': ['ic_replacement_148'], 'func': ic_replacement_d2_148}


def ic_replacement_d2_149(ic_replacement_149):
    feature = _clean(ic_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_149'] = {'inputs': ['ic_replacement_149'], 'func': ic_replacement_d2_149}


def ic_replacement_d2_150(ic_replacement_150):
    feature = _clean(ic_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_150'] = {'inputs': ['ic_replacement_150'], 'func': ic_replacement_d2_150}


def ic_replacement_d2_151(ic_replacement_151):
    feature = _clean(ic_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_151'] = {'inputs': ['ic_replacement_151'], 'func': ic_replacement_d2_151}


def ic_replacement_d2_152(ic_replacement_152):
    feature = _clean(ic_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_152'] = {'inputs': ['ic_replacement_152'], 'func': ic_replacement_d2_152}


def ic_replacement_d2_153(ic_replacement_153):
    feature = _clean(ic_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_153'] = {'inputs': ['ic_replacement_153'], 'func': ic_replacement_d2_153}


def ic_replacement_d2_154(ic_replacement_154):
    feature = _clean(ic_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_154'] = {'inputs': ['ic_replacement_154'], 'func': ic_replacement_d2_154}


def ic_replacement_d2_155(ic_replacement_155):
    feature = _clean(ic_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_155'] = {'inputs': ['ic_replacement_155'], 'func': ic_replacement_d2_155}


def ic_replacement_d2_156(ic_replacement_156):
    feature = _clean(ic_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_156'] = {'inputs': ['ic_replacement_156'], 'func': ic_replacement_d2_156}


def ic_replacement_d2_157(ic_replacement_157):
    feature = _clean(ic_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_157'] = {'inputs': ['ic_replacement_157'], 'func': ic_replacement_d2_157}


def ic_replacement_d2_158(ic_replacement_158):
    feature = _clean(ic_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_158'] = {'inputs': ['ic_replacement_158'], 'func': ic_replacement_d2_158}


def ic_replacement_d2_159(ic_replacement_159):
    feature = _clean(ic_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_159'] = {'inputs': ['ic_replacement_159'], 'func': ic_replacement_d2_159}


def ic_replacement_d2_160(ic_replacement_160):
    feature = _clean(ic_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_160'] = {'inputs': ['ic_replacement_160'], 'func': ic_replacement_d2_160}


def ic_replacement_d2_161(ic_replacement_161):
    feature = _clean(ic_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_161'] = {'inputs': ['ic_replacement_161'], 'func': ic_replacement_d2_161}


def ic_replacement_d2_162(ic_replacement_162):
    feature = _clean(ic_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_162'] = {'inputs': ['ic_replacement_162'], 'func': ic_replacement_d2_162}


def ic_replacement_d2_163(ic_replacement_163):
    feature = _clean(ic_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_163'] = {'inputs': ['ic_replacement_163'], 'func': ic_replacement_d2_163}


def ic_replacement_d2_164(ic_replacement_164):
    feature = _clean(ic_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_164'] = {'inputs': ['ic_replacement_164'], 'func': ic_replacement_d2_164}


def ic_replacement_d2_165(ic_replacement_165):
    feature = _clean(ic_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_165'] = {'inputs': ['ic_replacement_165'], 'func': ic_replacement_d2_165}


def ic_replacement_d2_166(ic_replacement_166):
    feature = _clean(ic_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
IC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ic_replacement_d2_166'] = {'inputs': ['ic_replacement_166'], 'func': ic_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63(icv_003_fcf_burn_to_cash_63):
    return _base_universe_d2(icv_003_fcf_burn_to_cash_63, 1)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63'] = {'inputs': ['icv_003_fcf_burn_to_cash_63'], 'func': icv_base_universe_d2_001_icv_003_fcf_burn_to_cash_63}


def icv_base_universe_d2_002_icv_004_debt_to_equity_84(icv_004_debt_to_equity_84):
    return _base_universe_d2(icv_004_debt_to_equity_84, 2)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_002_icv_004_debt_to_equity_84'] = {'inputs': ['icv_004_debt_to_equity_84'], 'func': icv_base_universe_d2_002_icv_004_debt_to_equity_84}


def icv_base_universe_d2_003_icv_005_debt_to_assets_126(icv_005_debt_to_assets_126):
    return _base_universe_d2(icv_005_debt_to_assets_126, 3)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_003_icv_005_debt_to_assets_126'] = {'inputs': ['icv_005_debt_to_assets_126'], 'func': icv_base_universe_d2_003_icv_005_debt_to_assets_126}


def icv_base_universe_d2_004_icv_012_accrual_gap_1260(icv_012_accrual_gap_1260):
    return _base_universe_d2(icv_012_accrual_gap_1260, 4)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_004_icv_012_accrual_gap_1260'] = {'inputs': ['icv_012_accrual_gap_1260'], 'func': icv_base_universe_d2_004_icv_012_accrual_gap_1260}


def icv_base_universe_d2_005_icv_016_debt_to_equity_21(icv_016_debt_to_equity_21):
    return _base_universe_d2(icv_016_debt_to_equity_21, 5)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_005_icv_016_debt_to_equity_21'] = {'inputs': ['icv_016_debt_to_equity_21'], 'func': icv_base_universe_d2_005_icv_016_debt_to_equity_21}


def icv_base_universe_d2_006_icv_017_debt_to_assets_42(icv_017_debt_to_assets_42):
    return _base_universe_d2(icv_017_debt_to_assets_42, 6)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_006_icv_017_debt_to_assets_42'] = {'inputs': ['icv_017_debt_to_assets_42'], 'func': icv_base_universe_d2_006_icv_017_debt_to_assets_42}


def icv_base_universe_d2_007_icv_024_accrual_gap_504(icv_024_accrual_gap_504):
    return _base_universe_d2(icv_024_accrual_gap_504, 7)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_007_icv_024_accrual_gap_504'] = {'inputs': ['icv_024_accrual_gap_504'], 'func': icv_base_universe_d2_007_icv_024_accrual_gap_504}


def icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260(icv_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(icv_027_fcf_burn_to_cash_1260, 8)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260'] = {'inputs': ['icv_027_fcf_burn_to_cash_1260'], 'func': icv_base_universe_d2_008_icv_027_fcf_burn_to_cash_1260}


def icv_base_universe_d2_009_icv_028_debt_to_equity_1512(icv_028_debt_to_equity_1512):
    return _base_universe_d2(icv_028_debt_to_equity_1512, 9)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_009_icv_028_debt_to_equity_1512'] = {'inputs': ['icv_028_debt_to_equity_1512'], 'func': icv_base_universe_d2_009_icv_028_debt_to_equity_1512}


def icv_base_universe_d2_010_icv_029_debt_to_assets_63(icv_029_debt_to_assets_63):
    return _base_universe_d2(icv_029_debt_to_assets_63, 10)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_010_icv_029_debt_to_assets_63'] = {'inputs': ['icv_029_debt_to_assets_63'], 'func': icv_base_universe_d2_010_icv_029_debt_to_assets_63}


def icv_base_universe_d2_011_icv_031_interest_coverage_stress_21(icv_031_interest_coverage_stress_21):
    return _base_universe_d2(icv_031_interest_coverage_stress_21, 11)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_011_icv_031_interest_coverage_stress_21'] = {'inputs': ['icv_031_interest_coverage_stress_21'], 'func': icv_base_universe_d2_011_icv_031_interest_coverage_stress_21}


def icv_base_universe_d2_012_icv_036_accrual_gap_189(icv_036_accrual_gap_189):
    return _base_universe_d2(icv_036_accrual_gap_189, 12)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_012_icv_036_accrual_gap_189'] = {'inputs': ['icv_036_accrual_gap_189'], 'func': icv_base_universe_d2_012_icv_036_accrual_gap_189}


def icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504(icv_039_fcf_burn_to_cash_504):
    return _base_universe_d2(icv_039_fcf_burn_to_cash_504, 13)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504'] = {'inputs': ['icv_039_fcf_burn_to_cash_504'], 'func': icv_base_universe_d2_013_icv_039_fcf_burn_to_cash_504}


def icv_base_universe_d2_014_icv_040_debt_to_equity_756(icv_040_debt_to_equity_756):
    return _base_universe_d2(icv_040_debt_to_equity_756, 14)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_014_icv_040_debt_to_equity_756'] = {'inputs': ['icv_040_debt_to_equity_756'], 'func': icv_base_universe_d2_014_icv_040_debt_to_equity_756}


def icv_base_universe_d2_015_icv_041_debt_to_assets_1008(icv_041_debt_to_assets_1008):
    return _base_universe_d2(icv_041_debt_to_assets_1008, 15)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_015_icv_041_debt_to_assets_1008'] = {'inputs': ['icv_041_debt_to_assets_1008'], 'func': icv_base_universe_d2_015_icv_041_debt_to_assets_1008}


def icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512(icv_043_interest_coverage_stress_1512):
    return _base_universe_d2(icv_043_interest_coverage_stress_1512, 16)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512'] = {'inputs': ['icv_043_interest_coverage_stress_1512'], 'func': icv_base_universe_d2_016_icv_043_interest_coverage_stress_1512}


def icv_base_universe_d2_017_icv_048_accrual_gap_63(icv_048_accrual_gap_63):
    return _base_universe_d2(icv_048_accrual_gap_63, 17)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_017_icv_048_accrual_gap_63'] = {'inputs': ['icv_048_accrual_gap_63'], 'func': icv_base_universe_d2_017_icv_048_accrual_gap_63}


def icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189(icv_051_fcf_burn_to_cash_189):
    return _base_universe_d2(icv_051_fcf_burn_to_cash_189, 18)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189'] = {'inputs': ['icv_051_fcf_burn_to_cash_189'], 'func': icv_base_universe_d2_018_icv_051_fcf_burn_to_cash_189}


def icv_base_universe_d2_019_icv_052_debt_to_equity_252(icv_052_debt_to_equity_252):
    return _base_universe_d2(icv_052_debt_to_equity_252, 19)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_019_icv_052_debt_to_equity_252'] = {'inputs': ['icv_052_debt_to_equity_252'], 'func': icv_base_universe_d2_019_icv_052_debt_to_equity_252}


def icv_base_universe_d2_020_icv_053_debt_to_assets_378(icv_053_debt_to_assets_378):
    return _base_universe_d2(icv_053_debt_to_assets_378, 20)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_020_icv_053_debt_to_assets_378'] = {'inputs': ['icv_053_debt_to_assets_378'], 'func': icv_base_universe_d2_020_icv_053_debt_to_assets_378}


def icv_base_universe_d2_021_icv_055_interest_coverage_stress_756(icv_055_interest_coverage_stress_756):
    return _base_universe_d2(icv_055_interest_coverage_stress_756, 21)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_021_icv_055_interest_coverage_stress_756'] = {'inputs': ['icv_055_interest_coverage_stress_756'], 'func': icv_base_universe_d2_021_icv_055_interest_coverage_stress_756}


def icv_base_universe_d2_022_icv_060_accrual_gap_252(icv_060_accrual_gap_252):
    return _base_universe_d2(icv_060_accrual_gap_252, 22)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_022_icv_060_accrual_gap_252'] = {'inputs': ['icv_060_accrual_gap_252'], 'func': icv_base_universe_d2_022_icv_060_accrual_gap_252}


def icv_base_universe_d2_023_icv_basefill_001(icv_basefill_001):
    return _base_universe_d2(icv_basefill_001, 23)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_023_icv_basefill_001'] = {'inputs': ['icv_basefill_001'], 'func': icv_base_universe_d2_023_icv_basefill_001}


def icv_base_universe_d2_024_icv_basefill_002(icv_basefill_002):
    return _base_universe_d2(icv_basefill_002, 24)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_024_icv_basefill_002'] = {'inputs': ['icv_basefill_002'], 'func': icv_base_universe_d2_024_icv_basefill_002}


def icv_base_universe_d2_025_icv_basefill_006(icv_basefill_006):
    return _base_universe_d2(icv_basefill_006, 25)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_025_icv_basefill_006'] = {'inputs': ['icv_basefill_006'], 'func': icv_base_universe_d2_025_icv_basefill_006}


def icv_base_universe_d2_026_icv_basefill_008(icv_basefill_008):
    return _base_universe_d2(icv_basefill_008, 26)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_026_icv_basefill_008'] = {'inputs': ['icv_basefill_008'], 'func': icv_base_universe_d2_026_icv_basefill_008}


def icv_base_universe_d2_027_icv_basefill_009(icv_basefill_009):
    return _base_universe_d2(icv_basefill_009, 27)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_027_icv_basefill_009'] = {'inputs': ['icv_basefill_009'], 'func': icv_base_universe_d2_027_icv_basefill_009}


def icv_base_universe_d2_028_icv_basefill_010(icv_basefill_010):
    return _base_universe_d2(icv_basefill_010, 28)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_028_icv_basefill_010'] = {'inputs': ['icv_basefill_010'], 'func': icv_base_universe_d2_028_icv_basefill_010}


def icv_base_universe_d2_029_icv_basefill_011(icv_basefill_011):
    return _base_universe_d2(icv_basefill_011, 29)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_029_icv_basefill_011'] = {'inputs': ['icv_basefill_011'], 'func': icv_base_universe_d2_029_icv_basefill_011}


def icv_base_universe_d2_030_icv_basefill_013(icv_basefill_013):
    return _base_universe_d2(icv_basefill_013, 30)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_030_icv_basefill_013'] = {'inputs': ['icv_basefill_013'], 'func': icv_base_universe_d2_030_icv_basefill_013}


def icv_base_universe_d2_031_icv_basefill_014(icv_basefill_014):
    return _base_universe_d2(icv_basefill_014, 31)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_031_icv_basefill_014'] = {'inputs': ['icv_basefill_014'], 'func': icv_base_universe_d2_031_icv_basefill_014}


def icv_base_universe_d2_032_icv_basefill_015(icv_basefill_015):
    return _base_universe_d2(icv_basefill_015, 32)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_032_icv_basefill_015'] = {'inputs': ['icv_basefill_015'], 'func': icv_base_universe_d2_032_icv_basefill_015}


def icv_base_universe_d2_033_icv_basefill_018(icv_basefill_018):
    return _base_universe_d2(icv_basefill_018, 33)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_033_icv_basefill_018'] = {'inputs': ['icv_basefill_018'], 'func': icv_base_universe_d2_033_icv_basefill_018}


def icv_base_universe_d2_034_icv_basefill_020(icv_basefill_020):
    return _base_universe_d2(icv_basefill_020, 34)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_034_icv_basefill_020'] = {'inputs': ['icv_basefill_020'], 'func': icv_base_universe_d2_034_icv_basefill_020}


def icv_base_universe_d2_035_icv_basefill_021(icv_basefill_021):
    return _base_universe_d2(icv_basefill_021, 35)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_035_icv_basefill_021'] = {'inputs': ['icv_basefill_021'], 'func': icv_base_universe_d2_035_icv_basefill_021}


def icv_base_universe_d2_036_icv_basefill_022(icv_basefill_022):
    return _base_universe_d2(icv_basefill_022, 36)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_036_icv_basefill_022'] = {'inputs': ['icv_basefill_022'], 'func': icv_base_universe_d2_036_icv_basefill_022}


def icv_base_universe_d2_037_icv_basefill_023(icv_basefill_023):
    return _base_universe_d2(icv_basefill_023, 37)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_037_icv_basefill_023'] = {'inputs': ['icv_basefill_023'], 'func': icv_base_universe_d2_037_icv_basefill_023}


def icv_base_universe_d2_038_icv_basefill_025(icv_basefill_025):
    return _base_universe_d2(icv_basefill_025, 38)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_038_icv_basefill_025'] = {'inputs': ['icv_basefill_025'], 'func': icv_base_universe_d2_038_icv_basefill_025}


def icv_base_universe_d2_039_icv_basefill_026(icv_basefill_026):
    return _base_universe_d2(icv_basefill_026, 39)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_039_icv_basefill_026'] = {'inputs': ['icv_basefill_026'], 'func': icv_base_universe_d2_039_icv_basefill_026}


def icv_base_universe_d2_040_icv_basefill_030(icv_basefill_030):
    return _base_universe_d2(icv_basefill_030, 40)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_040_icv_basefill_030'] = {'inputs': ['icv_basefill_030'], 'func': icv_base_universe_d2_040_icv_basefill_030}


def icv_base_universe_d2_041_icv_basefill_032(icv_basefill_032):
    return _base_universe_d2(icv_basefill_032, 41)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_041_icv_basefill_032'] = {'inputs': ['icv_basefill_032'], 'func': icv_base_universe_d2_041_icv_basefill_032}


def icv_base_universe_d2_042_icv_basefill_033(icv_basefill_033):
    return _base_universe_d2(icv_basefill_033, 42)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_042_icv_basefill_033'] = {'inputs': ['icv_basefill_033'], 'func': icv_base_universe_d2_042_icv_basefill_033}


def icv_base_universe_d2_043_icv_basefill_034(icv_basefill_034):
    return _base_universe_d2(icv_basefill_034, 43)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_043_icv_basefill_034'] = {'inputs': ['icv_basefill_034'], 'func': icv_base_universe_d2_043_icv_basefill_034}


def icv_base_universe_d2_044_icv_basefill_035(icv_basefill_035):
    return _base_universe_d2(icv_basefill_035, 44)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_044_icv_basefill_035'] = {'inputs': ['icv_basefill_035'], 'func': icv_base_universe_d2_044_icv_basefill_035}


def icv_base_universe_d2_045_icv_basefill_037(icv_basefill_037):
    return _base_universe_d2(icv_basefill_037, 45)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_045_icv_basefill_037'] = {'inputs': ['icv_basefill_037'], 'func': icv_base_universe_d2_045_icv_basefill_037}


def icv_base_universe_d2_046_icv_basefill_038(icv_basefill_038):
    return _base_universe_d2(icv_basefill_038, 46)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_046_icv_basefill_038'] = {'inputs': ['icv_basefill_038'], 'func': icv_base_universe_d2_046_icv_basefill_038}


def icv_base_universe_d2_047_icv_basefill_042(icv_basefill_042):
    return _base_universe_d2(icv_basefill_042, 47)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_047_icv_basefill_042'] = {'inputs': ['icv_basefill_042'], 'func': icv_base_universe_d2_047_icv_basefill_042}


def icv_base_universe_d2_048_icv_basefill_044(icv_basefill_044):
    return _base_universe_d2(icv_basefill_044, 48)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_048_icv_basefill_044'] = {'inputs': ['icv_basefill_044'], 'func': icv_base_universe_d2_048_icv_basefill_044}


def icv_base_universe_d2_049_icv_basefill_045(icv_basefill_045):
    return _base_universe_d2(icv_basefill_045, 49)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_049_icv_basefill_045'] = {'inputs': ['icv_basefill_045'], 'func': icv_base_universe_d2_049_icv_basefill_045}


def icv_base_universe_d2_050_icv_basefill_046(icv_basefill_046):
    return _base_universe_d2(icv_basefill_046, 50)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_050_icv_basefill_046'] = {'inputs': ['icv_basefill_046'], 'func': icv_base_universe_d2_050_icv_basefill_046}


def icv_base_universe_d2_051_icv_basefill_047(icv_basefill_047):
    return _base_universe_d2(icv_basefill_047, 51)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_051_icv_basefill_047'] = {'inputs': ['icv_basefill_047'], 'func': icv_base_universe_d2_051_icv_basefill_047}


def icv_base_universe_d2_052_icv_basefill_049(icv_basefill_049):
    return _base_universe_d2(icv_basefill_049, 52)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_052_icv_basefill_049'] = {'inputs': ['icv_basefill_049'], 'func': icv_base_universe_d2_052_icv_basefill_049}


def icv_base_universe_d2_053_icv_basefill_050(icv_basefill_050):
    return _base_universe_d2(icv_basefill_050, 53)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_053_icv_basefill_050'] = {'inputs': ['icv_basefill_050'], 'func': icv_base_universe_d2_053_icv_basefill_050}


def icv_base_universe_d2_054_icv_basefill_054(icv_basefill_054):
    return _base_universe_d2(icv_basefill_054, 54)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_054_icv_basefill_054'] = {'inputs': ['icv_basefill_054'], 'func': icv_base_universe_d2_054_icv_basefill_054}


def icv_base_universe_d2_055_icv_basefill_056(icv_basefill_056):
    return _base_universe_d2(icv_basefill_056, 55)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_055_icv_basefill_056'] = {'inputs': ['icv_basefill_056'], 'func': icv_base_universe_d2_055_icv_basefill_056}


def icv_base_universe_d2_056_icv_basefill_057(icv_basefill_057):
    return _base_universe_d2(icv_basefill_057, 56)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_056_icv_basefill_057'] = {'inputs': ['icv_basefill_057'], 'func': icv_base_universe_d2_056_icv_basefill_057}


def icv_base_universe_d2_057_icv_basefill_058(icv_basefill_058):
    return _base_universe_d2(icv_basefill_058, 57)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_057_icv_basefill_058'] = {'inputs': ['icv_basefill_058'], 'func': icv_base_universe_d2_057_icv_basefill_058}


def icv_base_universe_d2_058_icv_basefill_059(icv_basefill_059):
    return _base_universe_d2(icv_basefill_059, 58)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_058_icv_basefill_059'] = {'inputs': ['icv_basefill_059'], 'func': icv_base_universe_d2_058_icv_basefill_059}


def icv_base_universe_d2_059_icv_basefill_061(icv_basefill_061):
    return _base_universe_d2(icv_basefill_061, 59)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_059_icv_basefill_061'] = {'inputs': ['icv_basefill_061'], 'func': icv_base_universe_d2_059_icv_basefill_061}


def icv_base_universe_d2_060_icv_basefill_062(icv_basefill_062):
    return _base_universe_d2(icv_basefill_062, 60)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_060_icv_basefill_062'] = {'inputs': ['icv_basefill_062'], 'func': icv_base_universe_d2_060_icv_basefill_062}


def icv_base_universe_d2_061_icv_basefill_063(icv_basefill_063):
    return _base_universe_d2(icv_basefill_063, 61)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_061_icv_basefill_063'] = {'inputs': ['icv_basefill_063'], 'func': icv_base_universe_d2_061_icv_basefill_063}


def icv_base_universe_d2_062_icv_basefill_064(icv_basefill_064):
    return _base_universe_d2(icv_basefill_064, 62)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_062_icv_basefill_064'] = {'inputs': ['icv_basefill_064'], 'func': icv_base_universe_d2_062_icv_basefill_064}


def icv_base_universe_d2_063_icv_basefill_065(icv_basefill_065):
    return _base_universe_d2(icv_basefill_065, 63)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_063_icv_basefill_065'] = {'inputs': ['icv_basefill_065'], 'func': icv_base_universe_d2_063_icv_basefill_065}


def icv_base_universe_d2_064_icv_basefill_066(icv_basefill_066):
    return _base_universe_d2(icv_basefill_066, 64)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_064_icv_basefill_066'] = {'inputs': ['icv_basefill_066'], 'func': icv_base_universe_d2_064_icv_basefill_066}


def icv_base_universe_d2_065_icv_basefill_067(icv_basefill_067):
    return _base_universe_d2(icv_basefill_067, 65)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_065_icv_basefill_067'] = {'inputs': ['icv_basefill_067'], 'func': icv_base_universe_d2_065_icv_basefill_067}


def icv_base_universe_d2_066_icv_basefill_068(icv_basefill_068):
    return _base_universe_d2(icv_basefill_068, 66)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_066_icv_basefill_068'] = {'inputs': ['icv_basefill_068'], 'func': icv_base_universe_d2_066_icv_basefill_068}


def icv_base_universe_d2_067_icv_basefill_069(icv_basefill_069):
    return _base_universe_d2(icv_basefill_069, 67)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_067_icv_basefill_069'] = {'inputs': ['icv_basefill_069'], 'func': icv_base_universe_d2_067_icv_basefill_069}


def icv_base_universe_d2_068_icv_basefill_070(icv_basefill_070):
    return _base_universe_d2(icv_basefill_070, 68)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_068_icv_basefill_070'] = {'inputs': ['icv_basefill_070'], 'func': icv_base_universe_d2_068_icv_basefill_070}


def icv_base_universe_d2_069_icv_basefill_071(icv_basefill_071):
    return _base_universe_d2(icv_basefill_071, 69)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_069_icv_basefill_071'] = {'inputs': ['icv_basefill_071'], 'func': icv_base_universe_d2_069_icv_basefill_071}


def icv_base_universe_d2_070_icv_basefill_072(icv_basefill_072):
    return _base_universe_d2(icv_basefill_072, 70)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_070_icv_basefill_072'] = {'inputs': ['icv_basefill_072'], 'func': icv_base_universe_d2_070_icv_basefill_072}


def icv_base_universe_d2_071_icv_basefill_073(icv_basefill_073):
    return _base_universe_d2(icv_basefill_073, 71)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_071_icv_basefill_073'] = {'inputs': ['icv_basefill_073'], 'func': icv_base_universe_d2_071_icv_basefill_073}


def icv_base_universe_d2_072_icv_basefill_074(icv_basefill_074):
    return _base_universe_d2(icv_basefill_074, 72)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_072_icv_basefill_074'] = {'inputs': ['icv_basefill_074'], 'func': icv_base_universe_d2_072_icv_basefill_074}


def icv_base_universe_d2_073_icv_basefill_075(icv_basefill_075):
    return _base_universe_d2(icv_basefill_075, 73)
ICV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['icv_base_universe_d2_073_icv_basefill_075'] = {'inputs': ['icv_basefill_075'], 'func': icv_base_universe_d2_073_icv_basefill_075}
