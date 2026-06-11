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



def wcd_151_wcd_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def wcd_152_wcd_007_interest_coverage_stress_252_roc_42(wcd_007_interest_coverage_stress_252):
    feature = _s(wcd_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def wcd_153_wcd_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def wcd_154_wcd_019_interest_coverage_stress_84_roc_378(wcd_019_interest_coverage_stress_84):
    feature = _s(wcd_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def wcd_155_wcd_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















WORKING_CAPITAL_DRAIN_REGISTRY_2ND_DERIVATIVES = {
    'wcd_151_wcd_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': wcd_151_wcd_001_netinc_decline_1_roc_1},
    'wcd_152_wcd_007_interest_coverage_stress_252_roc_42': {'inputs': ['wcd_007_interest_coverage_stress_252'], 'func': wcd_152_wcd_007_interest_coverage_stress_252_roc_42},
    'wcd_153_wcd_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': wcd_153_wcd_013_netinc_decline_1_roc_126},
    'wcd_154_wcd_019_interest_coverage_stress_84_roc_378': {'inputs': ['wcd_019_interest_coverage_stress_84'], 'func': wcd_154_wcd_019_interest_coverage_stress_84_roc_378},
    'wcd_155_wcd_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': wcd_155_wcd_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def wcd_replacement_d2_001(wcd_replacement_001):
    feature = _clean(wcd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_001'] = {'inputs': ['wcd_replacement_001'], 'func': wcd_replacement_d2_001}


def wcd_replacement_d2_002(wcd_replacement_002):
    feature = _clean(wcd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_002'] = {'inputs': ['wcd_replacement_002'], 'func': wcd_replacement_d2_002}


def wcd_replacement_d2_003(wcd_replacement_003):
    feature = _clean(wcd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_003'] = {'inputs': ['wcd_replacement_003'], 'func': wcd_replacement_d2_003}


def wcd_replacement_d2_004(wcd_replacement_004):
    feature = _clean(wcd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_004'] = {'inputs': ['wcd_replacement_004'], 'func': wcd_replacement_d2_004}


def wcd_replacement_d2_005(wcd_replacement_005):
    feature = _clean(wcd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_005'] = {'inputs': ['wcd_replacement_005'], 'func': wcd_replacement_d2_005}


def wcd_replacement_d2_006(wcd_replacement_006):
    feature = _clean(wcd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_006'] = {'inputs': ['wcd_replacement_006'], 'func': wcd_replacement_d2_006}


def wcd_replacement_d2_007(wcd_replacement_007):
    feature = _clean(wcd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_007'] = {'inputs': ['wcd_replacement_007'], 'func': wcd_replacement_d2_007}


def wcd_replacement_d2_008(wcd_replacement_008):
    feature = _clean(wcd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_008'] = {'inputs': ['wcd_replacement_008'], 'func': wcd_replacement_d2_008}


def wcd_replacement_d2_009(wcd_replacement_009):
    feature = _clean(wcd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_009'] = {'inputs': ['wcd_replacement_009'], 'func': wcd_replacement_d2_009}


def wcd_replacement_d2_010(wcd_replacement_010):
    feature = _clean(wcd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_010'] = {'inputs': ['wcd_replacement_010'], 'func': wcd_replacement_d2_010}


def wcd_replacement_d2_011(wcd_replacement_011):
    feature = _clean(wcd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_011'] = {'inputs': ['wcd_replacement_011'], 'func': wcd_replacement_d2_011}


def wcd_replacement_d2_012(wcd_replacement_012):
    feature = _clean(wcd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_012'] = {'inputs': ['wcd_replacement_012'], 'func': wcd_replacement_d2_012}


def wcd_replacement_d2_013(wcd_replacement_013):
    feature = _clean(wcd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_013'] = {'inputs': ['wcd_replacement_013'], 'func': wcd_replacement_d2_013}


def wcd_replacement_d2_014(wcd_replacement_014):
    feature = _clean(wcd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_014'] = {'inputs': ['wcd_replacement_014'], 'func': wcd_replacement_d2_014}


def wcd_replacement_d2_015(wcd_replacement_015):
    feature = _clean(wcd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_015'] = {'inputs': ['wcd_replacement_015'], 'func': wcd_replacement_d2_015}


def wcd_replacement_d2_016(wcd_replacement_016):
    feature = _clean(wcd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_016'] = {'inputs': ['wcd_replacement_016'], 'func': wcd_replacement_d2_016}


def wcd_replacement_d2_017(wcd_replacement_017):
    feature = _clean(wcd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_017'] = {'inputs': ['wcd_replacement_017'], 'func': wcd_replacement_d2_017}


def wcd_replacement_d2_018(wcd_replacement_018):
    feature = _clean(wcd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_018'] = {'inputs': ['wcd_replacement_018'], 'func': wcd_replacement_d2_018}


def wcd_replacement_d2_019(wcd_replacement_019):
    feature = _clean(wcd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_019'] = {'inputs': ['wcd_replacement_019'], 'func': wcd_replacement_d2_019}


def wcd_replacement_d2_020(wcd_replacement_020):
    feature = _clean(wcd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_020'] = {'inputs': ['wcd_replacement_020'], 'func': wcd_replacement_d2_020}


def wcd_replacement_d2_021(wcd_replacement_021):
    feature = _clean(wcd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_021'] = {'inputs': ['wcd_replacement_021'], 'func': wcd_replacement_d2_021}


def wcd_replacement_d2_022(wcd_replacement_022):
    feature = _clean(wcd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_022'] = {'inputs': ['wcd_replacement_022'], 'func': wcd_replacement_d2_022}


def wcd_replacement_d2_023(wcd_replacement_023):
    feature = _clean(wcd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_023'] = {'inputs': ['wcd_replacement_023'], 'func': wcd_replacement_d2_023}


def wcd_replacement_d2_024(wcd_replacement_024):
    feature = _clean(wcd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_024'] = {'inputs': ['wcd_replacement_024'], 'func': wcd_replacement_d2_024}


def wcd_replacement_d2_025(wcd_replacement_025):
    feature = _clean(wcd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_025'] = {'inputs': ['wcd_replacement_025'], 'func': wcd_replacement_d2_025}


def wcd_replacement_d2_026(wcd_replacement_026):
    feature = _clean(wcd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_026'] = {'inputs': ['wcd_replacement_026'], 'func': wcd_replacement_d2_026}


def wcd_replacement_d2_027(wcd_replacement_027):
    feature = _clean(wcd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_027'] = {'inputs': ['wcd_replacement_027'], 'func': wcd_replacement_d2_027}


def wcd_replacement_d2_028(wcd_replacement_028):
    feature = _clean(wcd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_028'] = {'inputs': ['wcd_replacement_028'], 'func': wcd_replacement_d2_028}


def wcd_replacement_d2_029(wcd_replacement_029):
    feature = _clean(wcd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_029'] = {'inputs': ['wcd_replacement_029'], 'func': wcd_replacement_d2_029}


def wcd_replacement_d2_030(wcd_replacement_030):
    feature = _clean(wcd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_030'] = {'inputs': ['wcd_replacement_030'], 'func': wcd_replacement_d2_030}


def wcd_replacement_d2_031(wcd_replacement_031):
    feature = _clean(wcd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_031'] = {'inputs': ['wcd_replacement_031'], 'func': wcd_replacement_d2_031}


def wcd_replacement_d2_032(wcd_replacement_032):
    feature = _clean(wcd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_032'] = {'inputs': ['wcd_replacement_032'], 'func': wcd_replacement_d2_032}


def wcd_replacement_d2_033(wcd_replacement_033):
    feature = _clean(wcd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_033'] = {'inputs': ['wcd_replacement_033'], 'func': wcd_replacement_d2_033}


def wcd_replacement_d2_034(wcd_replacement_034):
    feature = _clean(wcd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_034'] = {'inputs': ['wcd_replacement_034'], 'func': wcd_replacement_d2_034}


def wcd_replacement_d2_035(wcd_replacement_035):
    feature = _clean(wcd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_035'] = {'inputs': ['wcd_replacement_035'], 'func': wcd_replacement_d2_035}


def wcd_replacement_d2_036(wcd_replacement_036):
    feature = _clean(wcd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_036'] = {'inputs': ['wcd_replacement_036'], 'func': wcd_replacement_d2_036}


def wcd_replacement_d2_037(wcd_replacement_037):
    feature = _clean(wcd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_037'] = {'inputs': ['wcd_replacement_037'], 'func': wcd_replacement_d2_037}


def wcd_replacement_d2_038(wcd_replacement_038):
    feature = _clean(wcd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_038'] = {'inputs': ['wcd_replacement_038'], 'func': wcd_replacement_d2_038}


def wcd_replacement_d2_039(wcd_replacement_039):
    feature = _clean(wcd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_039'] = {'inputs': ['wcd_replacement_039'], 'func': wcd_replacement_d2_039}


def wcd_replacement_d2_040(wcd_replacement_040):
    feature = _clean(wcd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_040'] = {'inputs': ['wcd_replacement_040'], 'func': wcd_replacement_d2_040}


def wcd_replacement_d2_041(wcd_replacement_041):
    feature = _clean(wcd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_041'] = {'inputs': ['wcd_replacement_041'], 'func': wcd_replacement_d2_041}


def wcd_replacement_d2_042(wcd_replacement_042):
    feature = _clean(wcd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_042'] = {'inputs': ['wcd_replacement_042'], 'func': wcd_replacement_d2_042}


def wcd_replacement_d2_043(wcd_replacement_043):
    feature = _clean(wcd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_043'] = {'inputs': ['wcd_replacement_043'], 'func': wcd_replacement_d2_043}


def wcd_replacement_d2_044(wcd_replacement_044):
    feature = _clean(wcd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_044'] = {'inputs': ['wcd_replacement_044'], 'func': wcd_replacement_d2_044}


def wcd_replacement_d2_045(wcd_replacement_045):
    feature = _clean(wcd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_045'] = {'inputs': ['wcd_replacement_045'], 'func': wcd_replacement_d2_045}


def wcd_replacement_d2_046(wcd_replacement_046):
    feature = _clean(wcd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_046'] = {'inputs': ['wcd_replacement_046'], 'func': wcd_replacement_d2_046}


def wcd_replacement_d2_047(wcd_replacement_047):
    feature = _clean(wcd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_047'] = {'inputs': ['wcd_replacement_047'], 'func': wcd_replacement_d2_047}


def wcd_replacement_d2_048(wcd_replacement_048):
    feature = _clean(wcd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_048'] = {'inputs': ['wcd_replacement_048'], 'func': wcd_replacement_d2_048}


def wcd_replacement_d2_049(wcd_replacement_049):
    feature = _clean(wcd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_049'] = {'inputs': ['wcd_replacement_049'], 'func': wcd_replacement_d2_049}


def wcd_replacement_d2_050(wcd_replacement_050):
    feature = _clean(wcd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_050'] = {'inputs': ['wcd_replacement_050'], 'func': wcd_replacement_d2_050}


def wcd_replacement_d2_051(wcd_replacement_051):
    feature = _clean(wcd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_051'] = {'inputs': ['wcd_replacement_051'], 'func': wcd_replacement_d2_051}


def wcd_replacement_d2_052(wcd_replacement_052):
    feature = _clean(wcd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_052'] = {'inputs': ['wcd_replacement_052'], 'func': wcd_replacement_d2_052}


def wcd_replacement_d2_053(wcd_replacement_053):
    feature = _clean(wcd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_053'] = {'inputs': ['wcd_replacement_053'], 'func': wcd_replacement_d2_053}


def wcd_replacement_d2_054(wcd_replacement_054):
    feature = _clean(wcd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_054'] = {'inputs': ['wcd_replacement_054'], 'func': wcd_replacement_d2_054}


def wcd_replacement_d2_055(wcd_replacement_055):
    feature = _clean(wcd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_055'] = {'inputs': ['wcd_replacement_055'], 'func': wcd_replacement_d2_055}


def wcd_replacement_d2_056(wcd_replacement_056):
    feature = _clean(wcd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_056'] = {'inputs': ['wcd_replacement_056'], 'func': wcd_replacement_d2_056}


def wcd_replacement_d2_057(wcd_replacement_057):
    feature = _clean(wcd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_057'] = {'inputs': ['wcd_replacement_057'], 'func': wcd_replacement_d2_057}


def wcd_replacement_d2_058(wcd_replacement_058):
    feature = _clean(wcd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_058'] = {'inputs': ['wcd_replacement_058'], 'func': wcd_replacement_d2_058}


def wcd_replacement_d2_059(wcd_replacement_059):
    feature = _clean(wcd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_059'] = {'inputs': ['wcd_replacement_059'], 'func': wcd_replacement_d2_059}


def wcd_replacement_d2_060(wcd_replacement_060):
    feature = _clean(wcd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_060'] = {'inputs': ['wcd_replacement_060'], 'func': wcd_replacement_d2_060}


def wcd_replacement_d2_061(wcd_replacement_061):
    feature = _clean(wcd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_061'] = {'inputs': ['wcd_replacement_061'], 'func': wcd_replacement_d2_061}


def wcd_replacement_d2_062(wcd_replacement_062):
    feature = _clean(wcd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_062'] = {'inputs': ['wcd_replacement_062'], 'func': wcd_replacement_d2_062}


def wcd_replacement_d2_063(wcd_replacement_063):
    feature = _clean(wcd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_063'] = {'inputs': ['wcd_replacement_063'], 'func': wcd_replacement_d2_063}


def wcd_replacement_d2_064(wcd_replacement_064):
    feature = _clean(wcd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_064'] = {'inputs': ['wcd_replacement_064'], 'func': wcd_replacement_d2_064}


def wcd_replacement_d2_065(wcd_replacement_065):
    feature = _clean(wcd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_065'] = {'inputs': ['wcd_replacement_065'], 'func': wcd_replacement_d2_065}


def wcd_replacement_d2_066(wcd_replacement_066):
    feature = _clean(wcd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_066'] = {'inputs': ['wcd_replacement_066'], 'func': wcd_replacement_d2_066}


def wcd_replacement_d2_067(wcd_replacement_067):
    feature = _clean(wcd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_067'] = {'inputs': ['wcd_replacement_067'], 'func': wcd_replacement_d2_067}


def wcd_replacement_d2_068(wcd_replacement_068):
    feature = _clean(wcd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_068'] = {'inputs': ['wcd_replacement_068'], 'func': wcd_replacement_d2_068}


def wcd_replacement_d2_069(wcd_replacement_069):
    feature = _clean(wcd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_069'] = {'inputs': ['wcd_replacement_069'], 'func': wcd_replacement_d2_069}


def wcd_replacement_d2_070(wcd_replacement_070):
    feature = _clean(wcd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_070'] = {'inputs': ['wcd_replacement_070'], 'func': wcd_replacement_d2_070}


def wcd_replacement_d2_071(wcd_replacement_071):
    feature = _clean(wcd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_071'] = {'inputs': ['wcd_replacement_071'], 'func': wcd_replacement_d2_071}


def wcd_replacement_d2_072(wcd_replacement_072):
    feature = _clean(wcd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_072'] = {'inputs': ['wcd_replacement_072'], 'func': wcd_replacement_d2_072}


def wcd_replacement_d2_073(wcd_replacement_073):
    feature = _clean(wcd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_073'] = {'inputs': ['wcd_replacement_073'], 'func': wcd_replacement_d2_073}


def wcd_replacement_d2_074(wcd_replacement_074):
    feature = _clean(wcd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_074'] = {'inputs': ['wcd_replacement_074'], 'func': wcd_replacement_d2_074}


def wcd_replacement_d2_075(wcd_replacement_075):
    feature = _clean(wcd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_075'] = {'inputs': ['wcd_replacement_075'], 'func': wcd_replacement_d2_075}


def wcd_replacement_d2_076(wcd_replacement_076):
    feature = _clean(wcd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_076'] = {'inputs': ['wcd_replacement_076'], 'func': wcd_replacement_d2_076}


def wcd_replacement_d2_077(wcd_replacement_077):
    feature = _clean(wcd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_077'] = {'inputs': ['wcd_replacement_077'], 'func': wcd_replacement_d2_077}


def wcd_replacement_d2_078(wcd_replacement_078):
    feature = _clean(wcd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_078'] = {'inputs': ['wcd_replacement_078'], 'func': wcd_replacement_d2_078}


def wcd_replacement_d2_079(wcd_replacement_079):
    feature = _clean(wcd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_079'] = {'inputs': ['wcd_replacement_079'], 'func': wcd_replacement_d2_079}


def wcd_replacement_d2_080(wcd_replacement_080):
    feature = _clean(wcd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_080'] = {'inputs': ['wcd_replacement_080'], 'func': wcd_replacement_d2_080}


def wcd_replacement_d2_081(wcd_replacement_081):
    feature = _clean(wcd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_081'] = {'inputs': ['wcd_replacement_081'], 'func': wcd_replacement_d2_081}


def wcd_replacement_d2_082(wcd_replacement_082):
    feature = _clean(wcd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_082'] = {'inputs': ['wcd_replacement_082'], 'func': wcd_replacement_d2_082}


def wcd_replacement_d2_083(wcd_replacement_083):
    feature = _clean(wcd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_083'] = {'inputs': ['wcd_replacement_083'], 'func': wcd_replacement_d2_083}


def wcd_replacement_d2_084(wcd_replacement_084):
    feature = _clean(wcd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_084'] = {'inputs': ['wcd_replacement_084'], 'func': wcd_replacement_d2_084}


def wcd_replacement_d2_085(wcd_replacement_085):
    feature = _clean(wcd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_085'] = {'inputs': ['wcd_replacement_085'], 'func': wcd_replacement_d2_085}


def wcd_replacement_d2_086(wcd_replacement_086):
    feature = _clean(wcd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_086'] = {'inputs': ['wcd_replacement_086'], 'func': wcd_replacement_d2_086}


def wcd_replacement_d2_087(wcd_replacement_087):
    feature = _clean(wcd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_087'] = {'inputs': ['wcd_replacement_087'], 'func': wcd_replacement_d2_087}


def wcd_replacement_d2_088(wcd_replacement_088):
    feature = _clean(wcd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_088'] = {'inputs': ['wcd_replacement_088'], 'func': wcd_replacement_d2_088}


def wcd_replacement_d2_089(wcd_replacement_089):
    feature = _clean(wcd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_089'] = {'inputs': ['wcd_replacement_089'], 'func': wcd_replacement_d2_089}


def wcd_replacement_d2_090(wcd_replacement_090):
    feature = _clean(wcd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_090'] = {'inputs': ['wcd_replacement_090'], 'func': wcd_replacement_d2_090}


def wcd_replacement_d2_091(wcd_replacement_091):
    feature = _clean(wcd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_091'] = {'inputs': ['wcd_replacement_091'], 'func': wcd_replacement_d2_091}


def wcd_replacement_d2_092(wcd_replacement_092):
    feature = _clean(wcd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_092'] = {'inputs': ['wcd_replacement_092'], 'func': wcd_replacement_d2_092}


def wcd_replacement_d2_093(wcd_replacement_093):
    feature = _clean(wcd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_093'] = {'inputs': ['wcd_replacement_093'], 'func': wcd_replacement_d2_093}


def wcd_replacement_d2_094(wcd_replacement_094):
    feature = _clean(wcd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_094'] = {'inputs': ['wcd_replacement_094'], 'func': wcd_replacement_d2_094}


def wcd_replacement_d2_095(wcd_replacement_095):
    feature = _clean(wcd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_095'] = {'inputs': ['wcd_replacement_095'], 'func': wcd_replacement_d2_095}


def wcd_replacement_d2_096(wcd_replacement_096):
    feature = _clean(wcd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_096'] = {'inputs': ['wcd_replacement_096'], 'func': wcd_replacement_d2_096}


def wcd_replacement_d2_097(wcd_replacement_097):
    feature = _clean(wcd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_097'] = {'inputs': ['wcd_replacement_097'], 'func': wcd_replacement_d2_097}


def wcd_replacement_d2_098(wcd_replacement_098):
    feature = _clean(wcd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_098'] = {'inputs': ['wcd_replacement_098'], 'func': wcd_replacement_d2_098}


def wcd_replacement_d2_099(wcd_replacement_099):
    feature = _clean(wcd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_099'] = {'inputs': ['wcd_replacement_099'], 'func': wcd_replacement_d2_099}


def wcd_replacement_d2_100(wcd_replacement_100):
    feature = _clean(wcd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_100'] = {'inputs': ['wcd_replacement_100'], 'func': wcd_replacement_d2_100}


def wcd_replacement_d2_101(wcd_replacement_101):
    feature = _clean(wcd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_101'] = {'inputs': ['wcd_replacement_101'], 'func': wcd_replacement_d2_101}


def wcd_replacement_d2_102(wcd_replacement_102):
    feature = _clean(wcd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_102'] = {'inputs': ['wcd_replacement_102'], 'func': wcd_replacement_d2_102}


def wcd_replacement_d2_103(wcd_replacement_103):
    feature = _clean(wcd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_103'] = {'inputs': ['wcd_replacement_103'], 'func': wcd_replacement_d2_103}


def wcd_replacement_d2_104(wcd_replacement_104):
    feature = _clean(wcd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_104'] = {'inputs': ['wcd_replacement_104'], 'func': wcd_replacement_d2_104}


def wcd_replacement_d2_105(wcd_replacement_105):
    feature = _clean(wcd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_105'] = {'inputs': ['wcd_replacement_105'], 'func': wcd_replacement_d2_105}


def wcd_replacement_d2_106(wcd_replacement_106):
    feature = _clean(wcd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_106'] = {'inputs': ['wcd_replacement_106'], 'func': wcd_replacement_d2_106}


def wcd_replacement_d2_107(wcd_replacement_107):
    feature = _clean(wcd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_107'] = {'inputs': ['wcd_replacement_107'], 'func': wcd_replacement_d2_107}


def wcd_replacement_d2_108(wcd_replacement_108):
    feature = _clean(wcd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_108'] = {'inputs': ['wcd_replacement_108'], 'func': wcd_replacement_d2_108}


def wcd_replacement_d2_109(wcd_replacement_109):
    feature = _clean(wcd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_109'] = {'inputs': ['wcd_replacement_109'], 'func': wcd_replacement_d2_109}


def wcd_replacement_d2_110(wcd_replacement_110):
    feature = _clean(wcd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_110'] = {'inputs': ['wcd_replacement_110'], 'func': wcd_replacement_d2_110}


def wcd_replacement_d2_111(wcd_replacement_111):
    feature = _clean(wcd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_111'] = {'inputs': ['wcd_replacement_111'], 'func': wcd_replacement_d2_111}


def wcd_replacement_d2_112(wcd_replacement_112):
    feature = _clean(wcd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_112'] = {'inputs': ['wcd_replacement_112'], 'func': wcd_replacement_d2_112}


def wcd_replacement_d2_113(wcd_replacement_113):
    feature = _clean(wcd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_113'] = {'inputs': ['wcd_replacement_113'], 'func': wcd_replacement_d2_113}


def wcd_replacement_d2_114(wcd_replacement_114):
    feature = _clean(wcd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_114'] = {'inputs': ['wcd_replacement_114'], 'func': wcd_replacement_d2_114}


def wcd_replacement_d2_115(wcd_replacement_115):
    feature = _clean(wcd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_115'] = {'inputs': ['wcd_replacement_115'], 'func': wcd_replacement_d2_115}


def wcd_replacement_d2_116(wcd_replacement_116):
    feature = _clean(wcd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_116'] = {'inputs': ['wcd_replacement_116'], 'func': wcd_replacement_d2_116}


def wcd_replacement_d2_117(wcd_replacement_117):
    feature = _clean(wcd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_117'] = {'inputs': ['wcd_replacement_117'], 'func': wcd_replacement_d2_117}


def wcd_replacement_d2_118(wcd_replacement_118):
    feature = _clean(wcd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_118'] = {'inputs': ['wcd_replacement_118'], 'func': wcd_replacement_d2_118}


def wcd_replacement_d2_119(wcd_replacement_119):
    feature = _clean(wcd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_119'] = {'inputs': ['wcd_replacement_119'], 'func': wcd_replacement_d2_119}


def wcd_replacement_d2_120(wcd_replacement_120):
    feature = _clean(wcd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_120'] = {'inputs': ['wcd_replacement_120'], 'func': wcd_replacement_d2_120}


def wcd_replacement_d2_121(wcd_replacement_121):
    feature = _clean(wcd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_121'] = {'inputs': ['wcd_replacement_121'], 'func': wcd_replacement_d2_121}


def wcd_replacement_d2_122(wcd_replacement_122):
    feature = _clean(wcd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_122'] = {'inputs': ['wcd_replacement_122'], 'func': wcd_replacement_d2_122}


def wcd_replacement_d2_123(wcd_replacement_123):
    feature = _clean(wcd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_123'] = {'inputs': ['wcd_replacement_123'], 'func': wcd_replacement_d2_123}


def wcd_replacement_d2_124(wcd_replacement_124):
    feature = _clean(wcd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_124'] = {'inputs': ['wcd_replacement_124'], 'func': wcd_replacement_d2_124}


def wcd_replacement_d2_125(wcd_replacement_125):
    feature = _clean(wcd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_125'] = {'inputs': ['wcd_replacement_125'], 'func': wcd_replacement_d2_125}


def wcd_replacement_d2_126(wcd_replacement_126):
    feature = _clean(wcd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_126'] = {'inputs': ['wcd_replacement_126'], 'func': wcd_replacement_d2_126}


def wcd_replacement_d2_127(wcd_replacement_127):
    feature = _clean(wcd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_127'] = {'inputs': ['wcd_replacement_127'], 'func': wcd_replacement_d2_127}


def wcd_replacement_d2_128(wcd_replacement_128):
    feature = _clean(wcd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_128'] = {'inputs': ['wcd_replacement_128'], 'func': wcd_replacement_d2_128}


def wcd_replacement_d2_129(wcd_replacement_129):
    feature = _clean(wcd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_129'] = {'inputs': ['wcd_replacement_129'], 'func': wcd_replacement_d2_129}


def wcd_replacement_d2_130(wcd_replacement_130):
    feature = _clean(wcd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_130'] = {'inputs': ['wcd_replacement_130'], 'func': wcd_replacement_d2_130}


def wcd_replacement_d2_131(wcd_replacement_131):
    feature = _clean(wcd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_131'] = {'inputs': ['wcd_replacement_131'], 'func': wcd_replacement_d2_131}


def wcd_replacement_d2_132(wcd_replacement_132):
    feature = _clean(wcd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_132'] = {'inputs': ['wcd_replacement_132'], 'func': wcd_replacement_d2_132}


def wcd_replacement_d2_133(wcd_replacement_133):
    feature = _clean(wcd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_133'] = {'inputs': ['wcd_replacement_133'], 'func': wcd_replacement_d2_133}


def wcd_replacement_d2_134(wcd_replacement_134):
    feature = _clean(wcd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_134'] = {'inputs': ['wcd_replacement_134'], 'func': wcd_replacement_d2_134}


def wcd_replacement_d2_135(wcd_replacement_135):
    feature = _clean(wcd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_135'] = {'inputs': ['wcd_replacement_135'], 'func': wcd_replacement_d2_135}


def wcd_replacement_d2_136(wcd_replacement_136):
    feature = _clean(wcd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_136'] = {'inputs': ['wcd_replacement_136'], 'func': wcd_replacement_d2_136}


def wcd_replacement_d2_137(wcd_replacement_137):
    feature = _clean(wcd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_137'] = {'inputs': ['wcd_replacement_137'], 'func': wcd_replacement_d2_137}


def wcd_replacement_d2_138(wcd_replacement_138):
    feature = _clean(wcd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_138'] = {'inputs': ['wcd_replacement_138'], 'func': wcd_replacement_d2_138}


def wcd_replacement_d2_139(wcd_replacement_139):
    feature = _clean(wcd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_139'] = {'inputs': ['wcd_replacement_139'], 'func': wcd_replacement_d2_139}


def wcd_replacement_d2_140(wcd_replacement_140):
    feature = _clean(wcd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_140'] = {'inputs': ['wcd_replacement_140'], 'func': wcd_replacement_d2_140}


def wcd_replacement_d2_141(wcd_replacement_141):
    feature = _clean(wcd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_141'] = {'inputs': ['wcd_replacement_141'], 'func': wcd_replacement_d2_141}


def wcd_replacement_d2_142(wcd_replacement_142):
    feature = _clean(wcd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_142'] = {'inputs': ['wcd_replacement_142'], 'func': wcd_replacement_d2_142}


def wcd_replacement_d2_143(wcd_replacement_143):
    feature = _clean(wcd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_143'] = {'inputs': ['wcd_replacement_143'], 'func': wcd_replacement_d2_143}


def wcd_replacement_d2_144(wcd_replacement_144):
    feature = _clean(wcd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_144'] = {'inputs': ['wcd_replacement_144'], 'func': wcd_replacement_d2_144}


def wcd_replacement_d2_145(wcd_replacement_145):
    feature = _clean(wcd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_145'] = {'inputs': ['wcd_replacement_145'], 'func': wcd_replacement_d2_145}


def wcd_replacement_d2_146(wcd_replacement_146):
    feature = _clean(wcd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_146'] = {'inputs': ['wcd_replacement_146'], 'func': wcd_replacement_d2_146}


def wcd_replacement_d2_147(wcd_replacement_147):
    feature = _clean(wcd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_147'] = {'inputs': ['wcd_replacement_147'], 'func': wcd_replacement_d2_147}


def wcd_replacement_d2_148(wcd_replacement_148):
    feature = _clean(wcd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_148'] = {'inputs': ['wcd_replacement_148'], 'func': wcd_replacement_d2_148}


def wcd_replacement_d2_149(wcd_replacement_149):
    feature = _clean(wcd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_149'] = {'inputs': ['wcd_replacement_149'], 'func': wcd_replacement_d2_149}


def wcd_replacement_d2_150(wcd_replacement_150):
    feature = _clean(wcd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_150'] = {'inputs': ['wcd_replacement_150'], 'func': wcd_replacement_d2_150}


def wcd_replacement_d2_151(wcd_replacement_151):
    feature = _clean(wcd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_151'] = {'inputs': ['wcd_replacement_151'], 'func': wcd_replacement_d2_151}


def wcd_replacement_d2_152(wcd_replacement_152):
    feature = _clean(wcd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_152'] = {'inputs': ['wcd_replacement_152'], 'func': wcd_replacement_d2_152}


def wcd_replacement_d2_153(wcd_replacement_153):
    feature = _clean(wcd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_153'] = {'inputs': ['wcd_replacement_153'], 'func': wcd_replacement_d2_153}


def wcd_replacement_d2_154(wcd_replacement_154):
    feature = _clean(wcd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_154'] = {'inputs': ['wcd_replacement_154'], 'func': wcd_replacement_d2_154}


def wcd_replacement_d2_155(wcd_replacement_155):
    feature = _clean(wcd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_155'] = {'inputs': ['wcd_replacement_155'], 'func': wcd_replacement_d2_155}


def wcd_replacement_d2_156(wcd_replacement_156):
    feature = _clean(wcd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_156'] = {'inputs': ['wcd_replacement_156'], 'func': wcd_replacement_d2_156}


def wcd_replacement_d2_157(wcd_replacement_157):
    feature = _clean(wcd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_157'] = {'inputs': ['wcd_replacement_157'], 'func': wcd_replacement_d2_157}


def wcd_replacement_d2_158(wcd_replacement_158):
    feature = _clean(wcd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_158'] = {'inputs': ['wcd_replacement_158'], 'func': wcd_replacement_d2_158}


def wcd_replacement_d2_159(wcd_replacement_159):
    feature = _clean(wcd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_159'] = {'inputs': ['wcd_replacement_159'], 'func': wcd_replacement_d2_159}


def wcd_replacement_d2_160(wcd_replacement_160):
    feature = _clean(wcd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_160'] = {'inputs': ['wcd_replacement_160'], 'func': wcd_replacement_d2_160}


def wcd_replacement_d2_161(wcd_replacement_161):
    feature = _clean(wcd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_161'] = {'inputs': ['wcd_replacement_161'], 'func': wcd_replacement_d2_161}


def wcd_replacement_d2_162(wcd_replacement_162):
    feature = _clean(wcd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_162'] = {'inputs': ['wcd_replacement_162'], 'func': wcd_replacement_d2_162}


def wcd_replacement_d2_163(wcd_replacement_163):
    feature = _clean(wcd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_163'] = {'inputs': ['wcd_replacement_163'], 'func': wcd_replacement_d2_163}


def wcd_replacement_d2_164(wcd_replacement_164):
    feature = _clean(wcd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_164'] = {'inputs': ['wcd_replacement_164'], 'func': wcd_replacement_d2_164}


def wcd_replacement_d2_165(wcd_replacement_165):
    feature = _clean(wcd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_165'] = {'inputs': ['wcd_replacement_165'], 'func': wcd_replacement_d2_165}


def wcd_replacement_d2_166(wcd_replacement_166):
    feature = _clean(wcd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
WCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['wcd_replacement_d2_166'] = {'inputs': ['wcd_replacement_166'], 'func': wcd_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63(wcd_003_fcf_burn_to_cash_63):
    return _base_universe_d2(wcd_003_fcf_burn_to_cash_63, 1)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63'] = {'inputs': ['wcd_003_fcf_burn_to_cash_63'], 'func': wcd_base_universe_d2_001_wcd_003_fcf_burn_to_cash_63}


def wcd_base_universe_d2_002_wcd_004_debt_to_equity_84(wcd_004_debt_to_equity_84):
    return _base_universe_d2(wcd_004_debt_to_equity_84, 2)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_002_wcd_004_debt_to_equity_84'] = {'inputs': ['wcd_004_debt_to_equity_84'], 'func': wcd_base_universe_d2_002_wcd_004_debt_to_equity_84}


def wcd_base_universe_d2_003_wcd_005_debt_to_assets_126(wcd_005_debt_to_assets_126):
    return _base_universe_d2(wcd_005_debt_to_assets_126, 3)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_003_wcd_005_debt_to_assets_126'] = {'inputs': ['wcd_005_debt_to_assets_126'], 'func': wcd_base_universe_d2_003_wcd_005_debt_to_assets_126}


def wcd_base_universe_d2_004_wcd_012_accrual_gap_1260(wcd_012_accrual_gap_1260):
    return _base_universe_d2(wcd_012_accrual_gap_1260, 4)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_004_wcd_012_accrual_gap_1260'] = {'inputs': ['wcd_012_accrual_gap_1260'], 'func': wcd_base_universe_d2_004_wcd_012_accrual_gap_1260}


def wcd_base_universe_d2_005_wcd_016_debt_to_equity_21(wcd_016_debt_to_equity_21):
    return _base_universe_d2(wcd_016_debt_to_equity_21, 5)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_005_wcd_016_debt_to_equity_21'] = {'inputs': ['wcd_016_debt_to_equity_21'], 'func': wcd_base_universe_d2_005_wcd_016_debt_to_equity_21}


def wcd_base_universe_d2_006_wcd_017_debt_to_assets_42(wcd_017_debt_to_assets_42):
    return _base_universe_d2(wcd_017_debt_to_assets_42, 6)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_006_wcd_017_debt_to_assets_42'] = {'inputs': ['wcd_017_debt_to_assets_42'], 'func': wcd_base_universe_d2_006_wcd_017_debt_to_assets_42}


def wcd_base_universe_d2_007_wcd_024_accrual_gap_504(wcd_024_accrual_gap_504):
    return _base_universe_d2(wcd_024_accrual_gap_504, 7)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_007_wcd_024_accrual_gap_504'] = {'inputs': ['wcd_024_accrual_gap_504'], 'func': wcd_base_universe_d2_007_wcd_024_accrual_gap_504}


def wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260(wcd_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(wcd_027_fcf_burn_to_cash_1260, 8)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260'] = {'inputs': ['wcd_027_fcf_burn_to_cash_1260'], 'func': wcd_base_universe_d2_008_wcd_027_fcf_burn_to_cash_1260}


def wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512(wcd_028_debt_to_equity_1512):
    return _base_universe_d2(wcd_028_debt_to_equity_1512, 9)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512'] = {'inputs': ['wcd_028_debt_to_equity_1512'], 'func': wcd_base_universe_d2_009_wcd_028_debt_to_equity_1512}


def wcd_base_universe_d2_010_wcd_029_debt_to_assets_63(wcd_029_debt_to_assets_63):
    return _base_universe_d2(wcd_029_debt_to_assets_63, 10)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_010_wcd_029_debt_to_assets_63'] = {'inputs': ['wcd_029_debt_to_assets_63'], 'func': wcd_base_universe_d2_010_wcd_029_debt_to_assets_63}


def wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21(wcd_031_interest_coverage_stress_21):
    return _base_universe_d2(wcd_031_interest_coverage_stress_21, 11)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21'] = {'inputs': ['wcd_031_interest_coverage_stress_21'], 'func': wcd_base_universe_d2_011_wcd_031_interest_coverage_stress_21}


def wcd_base_universe_d2_012_wcd_036_accrual_gap_189(wcd_036_accrual_gap_189):
    return _base_universe_d2(wcd_036_accrual_gap_189, 12)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_012_wcd_036_accrual_gap_189'] = {'inputs': ['wcd_036_accrual_gap_189'], 'func': wcd_base_universe_d2_012_wcd_036_accrual_gap_189}


def wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504(wcd_039_fcf_burn_to_cash_504):
    return _base_universe_d2(wcd_039_fcf_burn_to_cash_504, 13)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504'] = {'inputs': ['wcd_039_fcf_burn_to_cash_504'], 'func': wcd_base_universe_d2_013_wcd_039_fcf_burn_to_cash_504}


def wcd_base_universe_d2_014_wcd_040_debt_to_equity_756(wcd_040_debt_to_equity_756):
    return _base_universe_d2(wcd_040_debt_to_equity_756, 14)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_014_wcd_040_debt_to_equity_756'] = {'inputs': ['wcd_040_debt_to_equity_756'], 'func': wcd_base_universe_d2_014_wcd_040_debt_to_equity_756}


def wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008(wcd_041_debt_to_assets_1008):
    return _base_universe_d2(wcd_041_debt_to_assets_1008, 15)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008'] = {'inputs': ['wcd_041_debt_to_assets_1008'], 'func': wcd_base_universe_d2_015_wcd_041_debt_to_assets_1008}


def wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512(wcd_043_interest_coverage_stress_1512):
    return _base_universe_d2(wcd_043_interest_coverage_stress_1512, 16)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512'] = {'inputs': ['wcd_043_interest_coverage_stress_1512'], 'func': wcd_base_universe_d2_016_wcd_043_interest_coverage_stress_1512}


def wcd_base_universe_d2_017_wcd_048_accrual_gap_63(wcd_048_accrual_gap_63):
    return _base_universe_d2(wcd_048_accrual_gap_63, 17)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_017_wcd_048_accrual_gap_63'] = {'inputs': ['wcd_048_accrual_gap_63'], 'func': wcd_base_universe_d2_017_wcd_048_accrual_gap_63}


def wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189(wcd_051_fcf_burn_to_cash_189):
    return _base_universe_d2(wcd_051_fcf_burn_to_cash_189, 18)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189'] = {'inputs': ['wcd_051_fcf_burn_to_cash_189'], 'func': wcd_base_universe_d2_018_wcd_051_fcf_burn_to_cash_189}


def wcd_base_universe_d2_019_wcd_052_debt_to_equity_252(wcd_052_debt_to_equity_252):
    return _base_universe_d2(wcd_052_debt_to_equity_252, 19)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_019_wcd_052_debt_to_equity_252'] = {'inputs': ['wcd_052_debt_to_equity_252'], 'func': wcd_base_universe_d2_019_wcd_052_debt_to_equity_252}


def wcd_base_universe_d2_020_wcd_053_debt_to_assets_378(wcd_053_debt_to_assets_378):
    return _base_universe_d2(wcd_053_debt_to_assets_378, 20)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_020_wcd_053_debt_to_assets_378'] = {'inputs': ['wcd_053_debt_to_assets_378'], 'func': wcd_base_universe_d2_020_wcd_053_debt_to_assets_378}


def wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756(wcd_055_interest_coverage_stress_756):
    return _base_universe_d2(wcd_055_interest_coverage_stress_756, 21)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756'] = {'inputs': ['wcd_055_interest_coverage_stress_756'], 'func': wcd_base_universe_d2_021_wcd_055_interest_coverage_stress_756}


def wcd_base_universe_d2_022_wcd_060_accrual_gap_252(wcd_060_accrual_gap_252):
    return _base_universe_d2(wcd_060_accrual_gap_252, 22)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_022_wcd_060_accrual_gap_252'] = {'inputs': ['wcd_060_accrual_gap_252'], 'func': wcd_base_universe_d2_022_wcd_060_accrual_gap_252}


def wcd_base_universe_d2_023_wcd_basefill_001(wcd_basefill_001):
    return _base_universe_d2(wcd_basefill_001, 23)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_023_wcd_basefill_001'] = {'inputs': ['wcd_basefill_001'], 'func': wcd_base_universe_d2_023_wcd_basefill_001}


def wcd_base_universe_d2_024_wcd_basefill_002(wcd_basefill_002):
    return _base_universe_d2(wcd_basefill_002, 24)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_024_wcd_basefill_002'] = {'inputs': ['wcd_basefill_002'], 'func': wcd_base_universe_d2_024_wcd_basefill_002}


def wcd_base_universe_d2_025_wcd_basefill_006(wcd_basefill_006):
    return _base_universe_d2(wcd_basefill_006, 25)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_025_wcd_basefill_006'] = {'inputs': ['wcd_basefill_006'], 'func': wcd_base_universe_d2_025_wcd_basefill_006}


def wcd_base_universe_d2_026_wcd_basefill_008(wcd_basefill_008):
    return _base_universe_d2(wcd_basefill_008, 26)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_026_wcd_basefill_008'] = {'inputs': ['wcd_basefill_008'], 'func': wcd_base_universe_d2_026_wcd_basefill_008}


def wcd_base_universe_d2_027_wcd_basefill_009(wcd_basefill_009):
    return _base_universe_d2(wcd_basefill_009, 27)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_027_wcd_basefill_009'] = {'inputs': ['wcd_basefill_009'], 'func': wcd_base_universe_d2_027_wcd_basefill_009}


def wcd_base_universe_d2_028_wcd_basefill_010(wcd_basefill_010):
    return _base_universe_d2(wcd_basefill_010, 28)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_028_wcd_basefill_010'] = {'inputs': ['wcd_basefill_010'], 'func': wcd_base_universe_d2_028_wcd_basefill_010}


def wcd_base_universe_d2_029_wcd_basefill_011(wcd_basefill_011):
    return _base_universe_d2(wcd_basefill_011, 29)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_029_wcd_basefill_011'] = {'inputs': ['wcd_basefill_011'], 'func': wcd_base_universe_d2_029_wcd_basefill_011}


def wcd_base_universe_d2_030_wcd_basefill_013(wcd_basefill_013):
    return _base_universe_d2(wcd_basefill_013, 30)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_030_wcd_basefill_013'] = {'inputs': ['wcd_basefill_013'], 'func': wcd_base_universe_d2_030_wcd_basefill_013}


def wcd_base_universe_d2_031_wcd_basefill_014(wcd_basefill_014):
    return _base_universe_d2(wcd_basefill_014, 31)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_031_wcd_basefill_014'] = {'inputs': ['wcd_basefill_014'], 'func': wcd_base_universe_d2_031_wcd_basefill_014}


def wcd_base_universe_d2_032_wcd_basefill_015(wcd_basefill_015):
    return _base_universe_d2(wcd_basefill_015, 32)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_032_wcd_basefill_015'] = {'inputs': ['wcd_basefill_015'], 'func': wcd_base_universe_d2_032_wcd_basefill_015}


def wcd_base_universe_d2_033_wcd_basefill_018(wcd_basefill_018):
    return _base_universe_d2(wcd_basefill_018, 33)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_033_wcd_basefill_018'] = {'inputs': ['wcd_basefill_018'], 'func': wcd_base_universe_d2_033_wcd_basefill_018}


def wcd_base_universe_d2_034_wcd_basefill_020(wcd_basefill_020):
    return _base_universe_d2(wcd_basefill_020, 34)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_034_wcd_basefill_020'] = {'inputs': ['wcd_basefill_020'], 'func': wcd_base_universe_d2_034_wcd_basefill_020}


def wcd_base_universe_d2_035_wcd_basefill_021(wcd_basefill_021):
    return _base_universe_d2(wcd_basefill_021, 35)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_035_wcd_basefill_021'] = {'inputs': ['wcd_basefill_021'], 'func': wcd_base_universe_d2_035_wcd_basefill_021}


def wcd_base_universe_d2_036_wcd_basefill_022(wcd_basefill_022):
    return _base_universe_d2(wcd_basefill_022, 36)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_036_wcd_basefill_022'] = {'inputs': ['wcd_basefill_022'], 'func': wcd_base_universe_d2_036_wcd_basefill_022}


def wcd_base_universe_d2_037_wcd_basefill_023(wcd_basefill_023):
    return _base_universe_d2(wcd_basefill_023, 37)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_037_wcd_basefill_023'] = {'inputs': ['wcd_basefill_023'], 'func': wcd_base_universe_d2_037_wcd_basefill_023}


def wcd_base_universe_d2_038_wcd_basefill_025(wcd_basefill_025):
    return _base_universe_d2(wcd_basefill_025, 38)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_038_wcd_basefill_025'] = {'inputs': ['wcd_basefill_025'], 'func': wcd_base_universe_d2_038_wcd_basefill_025}


def wcd_base_universe_d2_039_wcd_basefill_026(wcd_basefill_026):
    return _base_universe_d2(wcd_basefill_026, 39)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_039_wcd_basefill_026'] = {'inputs': ['wcd_basefill_026'], 'func': wcd_base_universe_d2_039_wcd_basefill_026}


def wcd_base_universe_d2_040_wcd_basefill_030(wcd_basefill_030):
    return _base_universe_d2(wcd_basefill_030, 40)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_040_wcd_basefill_030'] = {'inputs': ['wcd_basefill_030'], 'func': wcd_base_universe_d2_040_wcd_basefill_030}


def wcd_base_universe_d2_041_wcd_basefill_032(wcd_basefill_032):
    return _base_universe_d2(wcd_basefill_032, 41)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_041_wcd_basefill_032'] = {'inputs': ['wcd_basefill_032'], 'func': wcd_base_universe_d2_041_wcd_basefill_032}


def wcd_base_universe_d2_042_wcd_basefill_033(wcd_basefill_033):
    return _base_universe_d2(wcd_basefill_033, 42)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_042_wcd_basefill_033'] = {'inputs': ['wcd_basefill_033'], 'func': wcd_base_universe_d2_042_wcd_basefill_033}


def wcd_base_universe_d2_043_wcd_basefill_034(wcd_basefill_034):
    return _base_universe_d2(wcd_basefill_034, 43)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_043_wcd_basefill_034'] = {'inputs': ['wcd_basefill_034'], 'func': wcd_base_universe_d2_043_wcd_basefill_034}


def wcd_base_universe_d2_044_wcd_basefill_035(wcd_basefill_035):
    return _base_universe_d2(wcd_basefill_035, 44)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_044_wcd_basefill_035'] = {'inputs': ['wcd_basefill_035'], 'func': wcd_base_universe_d2_044_wcd_basefill_035}


def wcd_base_universe_d2_045_wcd_basefill_037(wcd_basefill_037):
    return _base_universe_d2(wcd_basefill_037, 45)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_045_wcd_basefill_037'] = {'inputs': ['wcd_basefill_037'], 'func': wcd_base_universe_d2_045_wcd_basefill_037}


def wcd_base_universe_d2_046_wcd_basefill_038(wcd_basefill_038):
    return _base_universe_d2(wcd_basefill_038, 46)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_046_wcd_basefill_038'] = {'inputs': ['wcd_basefill_038'], 'func': wcd_base_universe_d2_046_wcd_basefill_038}


def wcd_base_universe_d2_047_wcd_basefill_042(wcd_basefill_042):
    return _base_universe_d2(wcd_basefill_042, 47)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_047_wcd_basefill_042'] = {'inputs': ['wcd_basefill_042'], 'func': wcd_base_universe_d2_047_wcd_basefill_042}


def wcd_base_universe_d2_048_wcd_basefill_044(wcd_basefill_044):
    return _base_universe_d2(wcd_basefill_044, 48)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_048_wcd_basefill_044'] = {'inputs': ['wcd_basefill_044'], 'func': wcd_base_universe_d2_048_wcd_basefill_044}


def wcd_base_universe_d2_049_wcd_basefill_045(wcd_basefill_045):
    return _base_universe_d2(wcd_basefill_045, 49)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_049_wcd_basefill_045'] = {'inputs': ['wcd_basefill_045'], 'func': wcd_base_universe_d2_049_wcd_basefill_045}


def wcd_base_universe_d2_050_wcd_basefill_046(wcd_basefill_046):
    return _base_universe_d2(wcd_basefill_046, 50)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_050_wcd_basefill_046'] = {'inputs': ['wcd_basefill_046'], 'func': wcd_base_universe_d2_050_wcd_basefill_046}


def wcd_base_universe_d2_051_wcd_basefill_047(wcd_basefill_047):
    return _base_universe_d2(wcd_basefill_047, 51)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_051_wcd_basefill_047'] = {'inputs': ['wcd_basefill_047'], 'func': wcd_base_universe_d2_051_wcd_basefill_047}


def wcd_base_universe_d2_052_wcd_basefill_049(wcd_basefill_049):
    return _base_universe_d2(wcd_basefill_049, 52)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_052_wcd_basefill_049'] = {'inputs': ['wcd_basefill_049'], 'func': wcd_base_universe_d2_052_wcd_basefill_049}


def wcd_base_universe_d2_053_wcd_basefill_050(wcd_basefill_050):
    return _base_universe_d2(wcd_basefill_050, 53)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_053_wcd_basefill_050'] = {'inputs': ['wcd_basefill_050'], 'func': wcd_base_universe_d2_053_wcd_basefill_050}


def wcd_base_universe_d2_054_wcd_basefill_054(wcd_basefill_054):
    return _base_universe_d2(wcd_basefill_054, 54)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_054_wcd_basefill_054'] = {'inputs': ['wcd_basefill_054'], 'func': wcd_base_universe_d2_054_wcd_basefill_054}


def wcd_base_universe_d2_055_wcd_basefill_056(wcd_basefill_056):
    return _base_universe_d2(wcd_basefill_056, 55)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_055_wcd_basefill_056'] = {'inputs': ['wcd_basefill_056'], 'func': wcd_base_universe_d2_055_wcd_basefill_056}


def wcd_base_universe_d2_056_wcd_basefill_057(wcd_basefill_057):
    return _base_universe_d2(wcd_basefill_057, 56)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_056_wcd_basefill_057'] = {'inputs': ['wcd_basefill_057'], 'func': wcd_base_universe_d2_056_wcd_basefill_057}


def wcd_base_universe_d2_057_wcd_basefill_058(wcd_basefill_058):
    return _base_universe_d2(wcd_basefill_058, 57)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_057_wcd_basefill_058'] = {'inputs': ['wcd_basefill_058'], 'func': wcd_base_universe_d2_057_wcd_basefill_058}


def wcd_base_universe_d2_058_wcd_basefill_059(wcd_basefill_059):
    return _base_universe_d2(wcd_basefill_059, 58)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_058_wcd_basefill_059'] = {'inputs': ['wcd_basefill_059'], 'func': wcd_base_universe_d2_058_wcd_basefill_059}


def wcd_base_universe_d2_059_wcd_basefill_061(wcd_basefill_061):
    return _base_universe_d2(wcd_basefill_061, 59)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_059_wcd_basefill_061'] = {'inputs': ['wcd_basefill_061'], 'func': wcd_base_universe_d2_059_wcd_basefill_061}


def wcd_base_universe_d2_060_wcd_basefill_062(wcd_basefill_062):
    return _base_universe_d2(wcd_basefill_062, 60)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_060_wcd_basefill_062'] = {'inputs': ['wcd_basefill_062'], 'func': wcd_base_universe_d2_060_wcd_basefill_062}


def wcd_base_universe_d2_061_wcd_basefill_063(wcd_basefill_063):
    return _base_universe_d2(wcd_basefill_063, 61)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_061_wcd_basefill_063'] = {'inputs': ['wcd_basefill_063'], 'func': wcd_base_universe_d2_061_wcd_basefill_063}


def wcd_base_universe_d2_062_wcd_basefill_064(wcd_basefill_064):
    return _base_universe_d2(wcd_basefill_064, 62)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_062_wcd_basefill_064'] = {'inputs': ['wcd_basefill_064'], 'func': wcd_base_universe_d2_062_wcd_basefill_064}


def wcd_base_universe_d2_063_wcd_basefill_065(wcd_basefill_065):
    return _base_universe_d2(wcd_basefill_065, 63)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_063_wcd_basefill_065'] = {'inputs': ['wcd_basefill_065'], 'func': wcd_base_universe_d2_063_wcd_basefill_065}


def wcd_base_universe_d2_064_wcd_basefill_066(wcd_basefill_066):
    return _base_universe_d2(wcd_basefill_066, 64)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_064_wcd_basefill_066'] = {'inputs': ['wcd_basefill_066'], 'func': wcd_base_universe_d2_064_wcd_basefill_066}


def wcd_base_universe_d2_065_wcd_basefill_067(wcd_basefill_067):
    return _base_universe_d2(wcd_basefill_067, 65)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_065_wcd_basefill_067'] = {'inputs': ['wcd_basefill_067'], 'func': wcd_base_universe_d2_065_wcd_basefill_067}


def wcd_base_universe_d2_066_wcd_basefill_068(wcd_basefill_068):
    return _base_universe_d2(wcd_basefill_068, 66)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_066_wcd_basefill_068'] = {'inputs': ['wcd_basefill_068'], 'func': wcd_base_universe_d2_066_wcd_basefill_068}


def wcd_base_universe_d2_067_wcd_basefill_069(wcd_basefill_069):
    return _base_universe_d2(wcd_basefill_069, 67)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_067_wcd_basefill_069'] = {'inputs': ['wcd_basefill_069'], 'func': wcd_base_universe_d2_067_wcd_basefill_069}


def wcd_base_universe_d2_068_wcd_basefill_070(wcd_basefill_070):
    return _base_universe_d2(wcd_basefill_070, 68)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_068_wcd_basefill_070'] = {'inputs': ['wcd_basefill_070'], 'func': wcd_base_universe_d2_068_wcd_basefill_070}


def wcd_base_universe_d2_069_wcd_basefill_071(wcd_basefill_071):
    return _base_universe_d2(wcd_basefill_071, 69)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_069_wcd_basefill_071'] = {'inputs': ['wcd_basefill_071'], 'func': wcd_base_universe_d2_069_wcd_basefill_071}


def wcd_base_universe_d2_070_wcd_basefill_072(wcd_basefill_072):
    return _base_universe_d2(wcd_basefill_072, 70)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_070_wcd_basefill_072'] = {'inputs': ['wcd_basefill_072'], 'func': wcd_base_universe_d2_070_wcd_basefill_072}


def wcd_base_universe_d2_071_wcd_basefill_073(wcd_basefill_073):
    return _base_universe_d2(wcd_basefill_073, 71)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_071_wcd_basefill_073'] = {'inputs': ['wcd_basefill_073'], 'func': wcd_base_universe_d2_071_wcd_basefill_073}


def wcd_base_universe_d2_072_wcd_basefill_074(wcd_basefill_074):
    return _base_universe_d2(wcd_basefill_074, 72)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_072_wcd_basefill_074'] = {'inputs': ['wcd_basefill_074'], 'func': wcd_base_universe_d2_072_wcd_basefill_074}


def wcd_base_universe_d2_073_wcd_basefill_075(wcd_basefill_075):
    return _base_universe_d2(wcd_basefill_075, 73)
WCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['wcd_base_universe_d2_073_wcd_basefill_075'] = {'inputs': ['wcd_basefill_075'], 'func': wcd_base_universe_d2_073_wcd_basefill_075}
