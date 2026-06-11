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



def aqy_151_aqy_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def aqy_152_aqy_007_interest_coverage_stress_252_roc_42(aqy_007_interest_coverage_stress_252):
    feature = _s(aqy_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def aqy_153_aqy_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def aqy_154_aqy_019_interest_coverage_stress_84_roc_378(aqy_019_interest_coverage_stress_84):
    feature = _s(aqy_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def aqy_155_aqy_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















ASSET_QUALITY_REGISTRY_2ND_DERIVATIVES = {
    'aqy_151_aqy_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': aqy_151_aqy_001_netinc_decline_1_roc_1},
    'aqy_152_aqy_007_interest_coverage_stress_252_roc_42': {'inputs': ['aqy_007_interest_coverage_stress_252'], 'func': aqy_152_aqy_007_interest_coverage_stress_252_roc_42},
    'aqy_153_aqy_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': aqy_153_aqy_013_netinc_decline_1_roc_126},
    'aqy_154_aqy_019_interest_coverage_stress_84_roc_378': {'inputs': ['aqy_019_interest_coverage_stress_84'], 'func': aqy_154_aqy_019_interest_coverage_stress_84_roc_378},
    'aqy_155_aqy_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': aqy_155_aqy_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def aq_replacement_d2_001(aq_replacement_001):
    feature = _clean(aq_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_001'] = {'inputs': ['aq_replacement_001'], 'func': aq_replacement_d2_001}


def aq_replacement_d2_002(aq_replacement_002):
    feature = _clean(aq_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_002'] = {'inputs': ['aq_replacement_002'], 'func': aq_replacement_d2_002}


def aq_replacement_d2_003(aq_replacement_003):
    feature = _clean(aq_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_003'] = {'inputs': ['aq_replacement_003'], 'func': aq_replacement_d2_003}


def aq_replacement_d2_004(aq_replacement_004):
    feature = _clean(aq_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_004'] = {'inputs': ['aq_replacement_004'], 'func': aq_replacement_d2_004}


def aq_replacement_d2_005(aq_replacement_005):
    feature = _clean(aq_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_005'] = {'inputs': ['aq_replacement_005'], 'func': aq_replacement_d2_005}


def aq_replacement_d2_006(aq_replacement_006):
    feature = _clean(aq_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_006'] = {'inputs': ['aq_replacement_006'], 'func': aq_replacement_d2_006}


def aq_replacement_d2_007(aq_replacement_007):
    feature = _clean(aq_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_007'] = {'inputs': ['aq_replacement_007'], 'func': aq_replacement_d2_007}


def aq_replacement_d2_008(aq_replacement_008):
    feature = _clean(aq_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_008'] = {'inputs': ['aq_replacement_008'], 'func': aq_replacement_d2_008}


def aq_replacement_d2_009(aq_replacement_009):
    feature = _clean(aq_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_009'] = {'inputs': ['aq_replacement_009'], 'func': aq_replacement_d2_009}


def aq_replacement_d2_010(aq_replacement_010):
    feature = _clean(aq_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_010'] = {'inputs': ['aq_replacement_010'], 'func': aq_replacement_d2_010}


def aq_replacement_d2_011(aq_replacement_011):
    feature = _clean(aq_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_011'] = {'inputs': ['aq_replacement_011'], 'func': aq_replacement_d2_011}


def aq_replacement_d2_012(aq_replacement_012):
    feature = _clean(aq_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_012'] = {'inputs': ['aq_replacement_012'], 'func': aq_replacement_d2_012}


def aq_replacement_d2_013(aq_replacement_013):
    feature = _clean(aq_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_013'] = {'inputs': ['aq_replacement_013'], 'func': aq_replacement_d2_013}


def aq_replacement_d2_014(aq_replacement_014):
    feature = _clean(aq_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_014'] = {'inputs': ['aq_replacement_014'], 'func': aq_replacement_d2_014}


def aq_replacement_d2_015(aq_replacement_015):
    feature = _clean(aq_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_015'] = {'inputs': ['aq_replacement_015'], 'func': aq_replacement_d2_015}


def aq_replacement_d2_016(aq_replacement_016):
    feature = _clean(aq_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_016'] = {'inputs': ['aq_replacement_016'], 'func': aq_replacement_d2_016}


def aq_replacement_d2_017(aq_replacement_017):
    feature = _clean(aq_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_017'] = {'inputs': ['aq_replacement_017'], 'func': aq_replacement_d2_017}


def aq_replacement_d2_018(aq_replacement_018):
    feature = _clean(aq_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_018'] = {'inputs': ['aq_replacement_018'], 'func': aq_replacement_d2_018}


def aq_replacement_d2_019(aq_replacement_019):
    feature = _clean(aq_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_019'] = {'inputs': ['aq_replacement_019'], 'func': aq_replacement_d2_019}


def aq_replacement_d2_020(aq_replacement_020):
    feature = _clean(aq_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_020'] = {'inputs': ['aq_replacement_020'], 'func': aq_replacement_d2_020}


def aq_replacement_d2_021(aq_replacement_021):
    feature = _clean(aq_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_021'] = {'inputs': ['aq_replacement_021'], 'func': aq_replacement_d2_021}


def aq_replacement_d2_022(aq_replacement_022):
    feature = _clean(aq_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_022'] = {'inputs': ['aq_replacement_022'], 'func': aq_replacement_d2_022}


def aq_replacement_d2_023(aq_replacement_023):
    feature = _clean(aq_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_023'] = {'inputs': ['aq_replacement_023'], 'func': aq_replacement_d2_023}


def aq_replacement_d2_024(aq_replacement_024):
    feature = _clean(aq_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_024'] = {'inputs': ['aq_replacement_024'], 'func': aq_replacement_d2_024}


def aq_replacement_d2_025(aq_replacement_025):
    feature = _clean(aq_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_025'] = {'inputs': ['aq_replacement_025'], 'func': aq_replacement_d2_025}


def aq_replacement_d2_026(aq_replacement_026):
    feature = _clean(aq_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_026'] = {'inputs': ['aq_replacement_026'], 'func': aq_replacement_d2_026}


def aq_replacement_d2_027(aq_replacement_027):
    feature = _clean(aq_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_027'] = {'inputs': ['aq_replacement_027'], 'func': aq_replacement_d2_027}


def aq_replacement_d2_028(aq_replacement_028):
    feature = _clean(aq_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_028'] = {'inputs': ['aq_replacement_028'], 'func': aq_replacement_d2_028}


def aq_replacement_d2_029(aq_replacement_029):
    feature = _clean(aq_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_029'] = {'inputs': ['aq_replacement_029'], 'func': aq_replacement_d2_029}


def aq_replacement_d2_030(aq_replacement_030):
    feature = _clean(aq_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_030'] = {'inputs': ['aq_replacement_030'], 'func': aq_replacement_d2_030}


def aq_replacement_d2_031(aq_replacement_031):
    feature = _clean(aq_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_031'] = {'inputs': ['aq_replacement_031'], 'func': aq_replacement_d2_031}


def aq_replacement_d2_032(aq_replacement_032):
    feature = _clean(aq_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_032'] = {'inputs': ['aq_replacement_032'], 'func': aq_replacement_d2_032}


def aq_replacement_d2_033(aq_replacement_033):
    feature = _clean(aq_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_033'] = {'inputs': ['aq_replacement_033'], 'func': aq_replacement_d2_033}


def aq_replacement_d2_034(aq_replacement_034):
    feature = _clean(aq_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_034'] = {'inputs': ['aq_replacement_034'], 'func': aq_replacement_d2_034}


def aq_replacement_d2_035(aq_replacement_035):
    feature = _clean(aq_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_035'] = {'inputs': ['aq_replacement_035'], 'func': aq_replacement_d2_035}


def aq_replacement_d2_036(aq_replacement_036):
    feature = _clean(aq_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_036'] = {'inputs': ['aq_replacement_036'], 'func': aq_replacement_d2_036}


def aq_replacement_d2_037(aq_replacement_037):
    feature = _clean(aq_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_037'] = {'inputs': ['aq_replacement_037'], 'func': aq_replacement_d2_037}


def aq_replacement_d2_038(aq_replacement_038):
    feature = _clean(aq_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_038'] = {'inputs': ['aq_replacement_038'], 'func': aq_replacement_d2_038}


def aq_replacement_d2_039(aq_replacement_039):
    feature = _clean(aq_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_039'] = {'inputs': ['aq_replacement_039'], 'func': aq_replacement_d2_039}


def aq_replacement_d2_040(aq_replacement_040):
    feature = _clean(aq_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_040'] = {'inputs': ['aq_replacement_040'], 'func': aq_replacement_d2_040}


def aq_replacement_d2_041(aq_replacement_041):
    feature = _clean(aq_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_041'] = {'inputs': ['aq_replacement_041'], 'func': aq_replacement_d2_041}


def aq_replacement_d2_042(aq_replacement_042):
    feature = _clean(aq_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_042'] = {'inputs': ['aq_replacement_042'], 'func': aq_replacement_d2_042}


def aq_replacement_d2_043(aq_replacement_043):
    feature = _clean(aq_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_043'] = {'inputs': ['aq_replacement_043'], 'func': aq_replacement_d2_043}


def aq_replacement_d2_044(aq_replacement_044):
    feature = _clean(aq_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_044'] = {'inputs': ['aq_replacement_044'], 'func': aq_replacement_d2_044}


def aq_replacement_d2_045(aq_replacement_045):
    feature = _clean(aq_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_045'] = {'inputs': ['aq_replacement_045'], 'func': aq_replacement_d2_045}


def aq_replacement_d2_046(aq_replacement_046):
    feature = _clean(aq_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_046'] = {'inputs': ['aq_replacement_046'], 'func': aq_replacement_d2_046}


def aq_replacement_d2_047(aq_replacement_047):
    feature = _clean(aq_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_047'] = {'inputs': ['aq_replacement_047'], 'func': aq_replacement_d2_047}


def aq_replacement_d2_048(aq_replacement_048):
    feature = _clean(aq_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_048'] = {'inputs': ['aq_replacement_048'], 'func': aq_replacement_d2_048}


def aq_replacement_d2_049(aq_replacement_049):
    feature = _clean(aq_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_049'] = {'inputs': ['aq_replacement_049'], 'func': aq_replacement_d2_049}


def aq_replacement_d2_050(aq_replacement_050):
    feature = _clean(aq_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_050'] = {'inputs': ['aq_replacement_050'], 'func': aq_replacement_d2_050}


def aq_replacement_d2_051(aq_replacement_051):
    feature = _clean(aq_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_051'] = {'inputs': ['aq_replacement_051'], 'func': aq_replacement_d2_051}


def aq_replacement_d2_052(aq_replacement_052):
    feature = _clean(aq_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_052'] = {'inputs': ['aq_replacement_052'], 'func': aq_replacement_d2_052}


def aq_replacement_d2_053(aq_replacement_053):
    feature = _clean(aq_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_053'] = {'inputs': ['aq_replacement_053'], 'func': aq_replacement_d2_053}


def aq_replacement_d2_054(aq_replacement_054):
    feature = _clean(aq_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_054'] = {'inputs': ['aq_replacement_054'], 'func': aq_replacement_d2_054}


def aq_replacement_d2_055(aq_replacement_055):
    feature = _clean(aq_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_055'] = {'inputs': ['aq_replacement_055'], 'func': aq_replacement_d2_055}


def aq_replacement_d2_056(aq_replacement_056):
    feature = _clean(aq_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_056'] = {'inputs': ['aq_replacement_056'], 'func': aq_replacement_d2_056}


def aq_replacement_d2_057(aq_replacement_057):
    feature = _clean(aq_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_057'] = {'inputs': ['aq_replacement_057'], 'func': aq_replacement_d2_057}


def aq_replacement_d2_058(aq_replacement_058):
    feature = _clean(aq_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_058'] = {'inputs': ['aq_replacement_058'], 'func': aq_replacement_d2_058}


def aq_replacement_d2_059(aq_replacement_059):
    feature = _clean(aq_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_059'] = {'inputs': ['aq_replacement_059'], 'func': aq_replacement_d2_059}


def aq_replacement_d2_060(aq_replacement_060):
    feature = _clean(aq_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_060'] = {'inputs': ['aq_replacement_060'], 'func': aq_replacement_d2_060}


def aq_replacement_d2_061(aq_replacement_061):
    feature = _clean(aq_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_061'] = {'inputs': ['aq_replacement_061'], 'func': aq_replacement_d2_061}


def aq_replacement_d2_062(aq_replacement_062):
    feature = _clean(aq_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_062'] = {'inputs': ['aq_replacement_062'], 'func': aq_replacement_d2_062}


def aq_replacement_d2_063(aq_replacement_063):
    feature = _clean(aq_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_063'] = {'inputs': ['aq_replacement_063'], 'func': aq_replacement_d2_063}


def aq_replacement_d2_064(aq_replacement_064):
    feature = _clean(aq_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_064'] = {'inputs': ['aq_replacement_064'], 'func': aq_replacement_d2_064}


def aq_replacement_d2_065(aq_replacement_065):
    feature = _clean(aq_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_065'] = {'inputs': ['aq_replacement_065'], 'func': aq_replacement_d2_065}


def aq_replacement_d2_066(aq_replacement_066):
    feature = _clean(aq_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_066'] = {'inputs': ['aq_replacement_066'], 'func': aq_replacement_d2_066}


def aq_replacement_d2_067(aq_replacement_067):
    feature = _clean(aq_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_067'] = {'inputs': ['aq_replacement_067'], 'func': aq_replacement_d2_067}


def aq_replacement_d2_068(aq_replacement_068):
    feature = _clean(aq_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_068'] = {'inputs': ['aq_replacement_068'], 'func': aq_replacement_d2_068}


def aq_replacement_d2_069(aq_replacement_069):
    feature = _clean(aq_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_069'] = {'inputs': ['aq_replacement_069'], 'func': aq_replacement_d2_069}


def aq_replacement_d2_070(aq_replacement_070):
    feature = _clean(aq_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_070'] = {'inputs': ['aq_replacement_070'], 'func': aq_replacement_d2_070}


def aq_replacement_d2_071(aq_replacement_071):
    feature = _clean(aq_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_071'] = {'inputs': ['aq_replacement_071'], 'func': aq_replacement_d2_071}


def aq_replacement_d2_072(aq_replacement_072):
    feature = _clean(aq_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_072'] = {'inputs': ['aq_replacement_072'], 'func': aq_replacement_d2_072}


def aq_replacement_d2_073(aq_replacement_073):
    feature = _clean(aq_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_073'] = {'inputs': ['aq_replacement_073'], 'func': aq_replacement_d2_073}


def aq_replacement_d2_074(aq_replacement_074):
    feature = _clean(aq_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_074'] = {'inputs': ['aq_replacement_074'], 'func': aq_replacement_d2_074}


def aq_replacement_d2_075(aq_replacement_075):
    feature = _clean(aq_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_075'] = {'inputs': ['aq_replacement_075'], 'func': aq_replacement_d2_075}


def aq_replacement_d2_076(aq_replacement_076):
    feature = _clean(aq_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_076'] = {'inputs': ['aq_replacement_076'], 'func': aq_replacement_d2_076}


def aq_replacement_d2_077(aq_replacement_077):
    feature = _clean(aq_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_077'] = {'inputs': ['aq_replacement_077'], 'func': aq_replacement_d2_077}


def aq_replacement_d2_078(aq_replacement_078):
    feature = _clean(aq_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_078'] = {'inputs': ['aq_replacement_078'], 'func': aq_replacement_d2_078}


def aq_replacement_d2_079(aq_replacement_079):
    feature = _clean(aq_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_079'] = {'inputs': ['aq_replacement_079'], 'func': aq_replacement_d2_079}


def aq_replacement_d2_080(aq_replacement_080):
    feature = _clean(aq_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_080'] = {'inputs': ['aq_replacement_080'], 'func': aq_replacement_d2_080}


def aq_replacement_d2_081(aq_replacement_081):
    feature = _clean(aq_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_081'] = {'inputs': ['aq_replacement_081'], 'func': aq_replacement_d2_081}


def aq_replacement_d2_082(aq_replacement_082):
    feature = _clean(aq_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_082'] = {'inputs': ['aq_replacement_082'], 'func': aq_replacement_d2_082}


def aq_replacement_d2_083(aq_replacement_083):
    feature = _clean(aq_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_083'] = {'inputs': ['aq_replacement_083'], 'func': aq_replacement_d2_083}


def aq_replacement_d2_084(aq_replacement_084):
    feature = _clean(aq_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_084'] = {'inputs': ['aq_replacement_084'], 'func': aq_replacement_d2_084}


def aq_replacement_d2_085(aq_replacement_085):
    feature = _clean(aq_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_085'] = {'inputs': ['aq_replacement_085'], 'func': aq_replacement_d2_085}


def aq_replacement_d2_086(aq_replacement_086):
    feature = _clean(aq_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_086'] = {'inputs': ['aq_replacement_086'], 'func': aq_replacement_d2_086}


def aq_replacement_d2_087(aq_replacement_087):
    feature = _clean(aq_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_087'] = {'inputs': ['aq_replacement_087'], 'func': aq_replacement_d2_087}


def aq_replacement_d2_088(aq_replacement_088):
    feature = _clean(aq_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_088'] = {'inputs': ['aq_replacement_088'], 'func': aq_replacement_d2_088}


def aq_replacement_d2_089(aq_replacement_089):
    feature = _clean(aq_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_089'] = {'inputs': ['aq_replacement_089'], 'func': aq_replacement_d2_089}


def aq_replacement_d2_090(aq_replacement_090):
    feature = _clean(aq_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_090'] = {'inputs': ['aq_replacement_090'], 'func': aq_replacement_d2_090}


def aq_replacement_d2_091(aq_replacement_091):
    feature = _clean(aq_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_091'] = {'inputs': ['aq_replacement_091'], 'func': aq_replacement_d2_091}


def aq_replacement_d2_092(aq_replacement_092):
    feature = _clean(aq_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_092'] = {'inputs': ['aq_replacement_092'], 'func': aq_replacement_d2_092}


def aq_replacement_d2_093(aq_replacement_093):
    feature = _clean(aq_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_093'] = {'inputs': ['aq_replacement_093'], 'func': aq_replacement_d2_093}


def aq_replacement_d2_094(aq_replacement_094):
    feature = _clean(aq_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_094'] = {'inputs': ['aq_replacement_094'], 'func': aq_replacement_d2_094}


def aq_replacement_d2_095(aq_replacement_095):
    feature = _clean(aq_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_095'] = {'inputs': ['aq_replacement_095'], 'func': aq_replacement_d2_095}


def aq_replacement_d2_096(aq_replacement_096):
    feature = _clean(aq_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_096'] = {'inputs': ['aq_replacement_096'], 'func': aq_replacement_d2_096}


def aq_replacement_d2_097(aq_replacement_097):
    feature = _clean(aq_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_097'] = {'inputs': ['aq_replacement_097'], 'func': aq_replacement_d2_097}


def aq_replacement_d2_098(aq_replacement_098):
    feature = _clean(aq_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_098'] = {'inputs': ['aq_replacement_098'], 'func': aq_replacement_d2_098}


def aq_replacement_d2_099(aq_replacement_099):
    feature = _clean(aq_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_099'] = {'inputs': ['aq_replacement_099'], 'func': aq_replacement_d2_099}


def aq_replacement_d2_100(aq_replacement_100):
    feature = _clean(aq_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_100'] = {'inputs': ['aq_replacement_100'], 'func': aq_replacement_d2_100}


def aq_replacement_d2_101(aq_replacement_101):
    feature = _clean(aq_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_101'] = {'inputs': ['aq_replacement_101'], 'func': aq_replacement_d2_101}


def aq_replacement_d2_102(aq_replacement_102):
    feature = _clean(aq_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_102'] = {'inputs': ['aq_replacement_102'], 'func': aq_replacement_d2_102}


def aq_replacement_d2_103(aq_replacement_103):
    feature = _clean(aq_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_103'] = {'inputs': ['aq_replacement_103'], 'func': aq_replacement_d2_103}


def aq_replacement_d2_104(aq_replacement_104):
    feature = _clean(aq_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_104'] = {'inputs': ['aq_replacement_104'], 'func': aq_replacement_d2_104}


def aq_replacement_d2_105(aq_replacement_105):
    feature = _clean(aq_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_105'] = {'inputs': ['aq_replacement_105'], 'func': aq_replacement_d2_105}


def aq_replacement_d2_106(aq_replacement_106):
    feature = _clean(aq_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_106'] = {'inputs': ['aq_replacement_106'], 'func': aq_replacement_d2_106}


def aq_replacement_d2_107(aq_replacement_107):
    feature = _clean(aq_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_107'] = {'inputs': ['aq_replacement_107'], 'func': aq_replacement_d2_107}


def aq_replacement_d2_108(aq_replacement_108):
    feature = _clean(aq_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_108'] = {'inputs': ['aq_replacement_108'], 'func': aq_replacement_d2_108}


def aq_replacement_d2_109(aq_replacement_109):
    feature = _clean(aq_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_109'] = {'inputs': ['aq_replacement_109'], 'func': aq_replacement_d2_109}


def aq_replacement_d2_110(aq_replacement_110):
    feature = _clean(aq_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_110'] = {'inputs': ['aq_replacement_110'], 'func': aq_replacement_d2_110}


def aq_replacement_d2_111(aq_replacement_111):
    feature = _clean(aq_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_111'] = {'inputs': ['aq_replacement_111'], 'func': aq_replacement_d2_111}


def aq_replacement_d2_112(aq_replacement_112):
    feature = _clean(aq_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_112'] = {'inputs': ['aq_replacement_112'], 'func': aq_replacement_d2_112}


def aq_replacement_d2_113(aq_replacement_113):
    feature = _clean(aq_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_113'] = {'inputs': ['aq_replacement_113'], 'func': aq_replacement_d2_113}


def aq_replacement_d2_114(aq_replacement_114):
    feature = _clean(aq_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_114'] = {'inputs': ['aq_replacement_114'], 'func': aq_replacement_d2_114}


def aq_replacement_d2_115(aq_replacement_115):
    feature = _clean(aq_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_115'] = {'inputs': ['aq_replacement_115'], 'func': aq_replacement_d2_115}


def aq_replacement_d2_116(aq_replacement_116):
    feature = _clean(aq_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_116'] = {'inputs': ['aq_replacement_116'], 'func': aq_replacement_d2_116}


def aq_replacement_d2_117(aq_replacement_117):
    feature = _clean(aq_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_117'] = {'inputs': ['aq_replacement_117'], 'func': aq_replacement_d2_117}


def aq_replacement_d2_118(aq_replacement_118):
    feature = _clean(aq_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_118'] = {'inputs': ['aq_replacement_118'], 'func': aq_replacement_d2_118}


def aq_replacement_d2_119(aq_replacement_119):
    feature = _clean(aq_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_119'] = {'inputs': ['aq_replacement_119'], 'func': aq_replacement_d2_119}


def aq_replacement_d2_120(aq_replacement_120):
    feature = _clean(aq_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_120'] = {'inputs': ['aq_replacement_120'], 'func': aq_replacement_d2_120}


def aq_replacement_d2_121(aq_replacement_121):
    feature = _clean(aq_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_121'] = {'inputs': ['aq_replacement_121'], 'func': aq_replacement_d2_121}


def aq_replacement_d2_122(aq_replacement_122):
    feature = _clean(aq_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_122'] = {'inputs': ['aq_replacement_122'], 'func': aq_replacement_d2_122}


def aq_replacement_d2_123(aq_replacement_123):
    feature = _clean(aq_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_123'] = {'inputs': ['aq_replacement_123'], 'func': aq_replacement_d2_123}


def aq_replacement_d2_124(aq_replacement_124):
    feature = _clean(aq_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_124'] = {'inputs': ['aq_replacement_124'], 'func': aq_replacement_d2_124}


def aq_replacement_d2_125(aq_replacement_125):
    feature = _clean(aq_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_125'] = {'inputs': ['aq_replacement_125'], 'func': aq_replacement_d2_125}


def aq_replacement_d2_126(aq_replacement_126):
    feature = _clean(aq_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_126'] = {'inputs': ['aq_replacement_126'], 'func': aq_replacement_d2_126}


def aq_replacement_d2_127(aq_replacement_127):
    feature = _clean(aq_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_127'] = {'inputs': ['aq_replacement_127'], 'func': aq_replacement_d2_127}


def aq_replacement_d2_128(aq_replacement_128):
    feature = _clean(aq_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_128'] = {'inputs': ['aq_replacement_128'], 'func': aq_replacement_d2_128}


def aq_replacement_d2_129(aq_replacement_129):
    feature = _clean(aq_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_129'] = {'inputs': ['aq_replacement_129'], 'func': aq_replacement_d2_129}


def aq_replacement_d2_130(aq_replacement_130):
    feature = _clean(aq_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_130'] = {'inputs': ['aq_replacement_130'], 'func': aq_replacement_d2_130}


def aq_replacement_d2_131(aq_replacement_131):
    feature = _clean(aq_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_131'] = {'inputs': ['aq_replacement_131'], 'func': aq_replacement_d2_131}


def aq_replacement_d2_132(aq_replacement_132):
    feature = _clean(aq_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_132'] = {'inputs': ['aq_replacement_132'], 'func': aq_replacement_d2_132}


def aq_replacement_d2_133(aq_replacement_133):
    feature = _clean(aq_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_133'] = {'inputs': ['aq_replacement_133'], 'func': aq_replacement_d2_133}


def aq_replacement_d2_134(aq_replacement_134):
    feature = _clean(aq_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_134'] = {'inputs': ['aq_replacement_134'], 'func': aq_replacement_d2_134}


def aq_replacement_d2_135(aq_replacement_135):
    feature = _clean(aq_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_135'] = {'inputs': ['aq_replacement_135'], 'func': aq_replacement_d2_135}


def aq_replacement_d2_136(aq_replacement_136):
    feature = _clean(aq_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_136'] = {'inputs': ['aq_replacement_136'], 'func': aq_replacement_d2_136}


def aq_replacement_d2_137(aq_replacement_137):
    feature = _clean(aq_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_137'] = {'inputs': ['aq_replacement_137'], 'func': aq_replacement_d2_137}


def aq_replacement_d2_138(aq_replacement_138):
    feature = _clean(aq_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_138'] = {'inputs': ['aq_replacement_138'], 'func': aq_replacement_d2_138}


def aq_replacement_d2_139(aq_replacement_139):
    feature = _clean(aq_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_139'] = {'inputs': ['aq_replacement_139'], 'func': aq_replacement_d2_139}


def aq_replacement_d2_140(aq_replacement_140):
    feature = _clean(aq_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_140'] = {'inputs': ['aq_replacement_140'], 'func': aq_replacement_d2_140}


def aq_replacement_d2_141(aq_replacement_141):
    feature = _clean(aq_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_141'] = {'inputs': ['aq_replacement_141'], 'func': aq_replacement_d2_141}


def aq_replacement_d2_142(aq_replacement_142):
    feature = _clean(aq_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_142'] = {'inputs': ['aq_replacement_142'], 'func': aq_replacement_d2_142}


def aq_replacement_d2_143(aq_replacement_143):
    feature = _clean(aq_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_143'] = {'inputs': ['aq_replacement_143'], 'func': aq_replacement_d2_143}


def aq_replacement_d2_144(aq_replacement_144):
    feature = _clean(aq_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_144'] = {'inputs': ['aq_replacement_144'], 'func': aq_replacement_d2_144}


def aq_replacement_d2_145(aq_replacement_145):
    feature = _clean(aq_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_145'] = {'inputs': ['aq_replacement_145'], 'func': aq_replacement_d2_145}


def aq_replacement_d2_146(aq_replacement_146):
    feature = _clean(aq_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_146'] = {'inputs': ['aq_replacement_146'], 'func': aq_replacement_d2_146}


def aq_replacement_d2_147(aq_replacement_147):
    feature = _clean(aq_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_147'] = {'inputs': ['aq_replacement_147'], 'func': aq_replacement_d2_147}


def aq_replacement_d2_148(aq_replacement_148):
    feature = _clean(aq_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_148'] = {'inputs': ['aq_replacement_148'], 'func': aq_replacement_d2_148}


def aq_replacement_d2_149(aq_replacement_149):
    feature = _clean(aq_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_149'] = {'inputs': ['aq_replacement_149'], 'func': aq_replacement_d2_149}


def aq_replacement_d2_150(aq_replacement_150):
    feature = _clean(aq_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_150'] = {'inputs': ['aq_replacement_150'], 'func': aq_replacement_d2_150}


def aq_replacement_d2_151(aq_replacement_151):
    feature = _clean(aq_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_151'] = {'inputs': ['aq_replacement_151'], 'func': aq_replacement_d2_151}


def aq_replacement_d2_152(aq_replacement_152):
    feature = _clean(aq_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_152'] = {'inputs': ['aq_replacement_152'], 'func': aq_replacement_d2_152}


def aq_replacement_d2_153(aq_replacement_153):
    feature = _clean(aq_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_153'] = {'inputs': ['aq_replacement_153'], 'func': aq_replacement_d2_153}


def aq_replacement_d2_154(aq_replacement_154):
    feature = _clean(aq_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_154'] = {'inputs': ['aq_replacement_154'], 'func': aq_replacement_d2_154}


def aq_replacement_d2_155(aq_replacement_155):
    feature = _clean(aq_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_155'] = {'inputs': ['aq_replacement_155'], 'func': aq_replacement_d2_155}


def aq_replacement_d2_156(aq_replacement_156):
    feature = _clean(aq_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_156'] = {'inputs': ['aq_replacement_156'], 'func': aq_replacement_d2_156}


def aq_replacement_d2_157(aq_replacement_157):
    feature = _clean(aq_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_157'] = {'inputs': ['aq_replacement_157'], 'func': aq_replacement_d2_157}


def aq_replacement_d2_158(aq_replacement_158):
    feature = _clean(aq_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_158'] = {'inputs': ['aq_replacement_158'], 'func': aq_replacement_d2_158}


def aq_replacement_d2_159(aq_replacement_159):
    feature = _clean(aq_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_159'] = {'inputs': ['aq_replacement_159'], 'func': aq_replacement_d2_159}


def aq_replacement_d2_160(aq_replacement_160):
    feature = _clean(aq_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_160'] = {'inputs': ['aq_replacement_160'], 'func': aq_replacement_d2_160}


def aq_replacement_d2_161(aq_replacement_161):
    feature = _clean(aq_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_161'] = {'inputs': ['aq_replacement_161'], 'func': aq_replacement_d2_161}


def aq_replacement_d2_162(aq_replacement_162):
    feature = _clean(aq_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_162'] = {'inputs': ['aq_replacement_162'], 'func': aq_replacement_d2_162}


def aq_replacement_d2_163(aq_replacement_163):
    feature = _clean(aq_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_163'] = {'inputs': ['aq_replacement_163'], 'func': aq_replacement_d2_163}


def aq_replacement_d2_164(aq_replacement_164):
    feature = _clean(aq_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_164'] = {'inputs': ['aq_replacement_164'], 'func': aq_replacement_d2_164}


def aq_replacement_d2_165(aq_replacement_165):
    feature = _clean(aq_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_165'] = {'inputs': ['aq_replacement_165'], 'func': aq_replacement_d2_165}


def aq_replacement_d2_166(aq_replacement_166):
    feature = _clean(aq_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
AQ_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['aq_replacement_d2_166'] = {'inputs': ['aq_replacement_166'], 'func': aq_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63(aqy_003_fcf_burn_to_cash_63):
    return _base_universe_d2(aqy_003_fcf_burn_to_cash_63, 1)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63'] = {'inputs': ['aqy_003_fcf_burn_to_cash_63'], 'func': aqy_base_universe_d2_001_aqy_003_fcf_burn_to_cash_63}


def aqy_base_universe_d2_002_aqy_004_debt_to_equity_84(aqy_004_debt_to_equity_84):
    return _base_universe_d2(aqy_004_debt_to_equity_84, 2)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_002_aqy_004_debt_to_equity_84'] = {'inputs': ['aqy_004_debt_to_equity_84'], 'func': aqy_base_universe_d2_002_aqy_004_debt_to_equity_84}


def aqy_base_universe_d2_003_aqy_005_debt_to_assets_126(aqy_005_debt_to_assets_126):
    return _base_universe_d2(aqy_005_debt_to_assets_126, 3)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_003_aqy_005_debt_to_assets_126'] = {'inputs': ['aqy_005_debt_to_assets_126'], 'func': aqy_base_universe_d2_003_aqy_005_debt_to_assets_126}


def aqy_base_universe_d2_004_aqy_012_accrual_gap_1260(aqy_012_accrual_gap_1260):
    return _base_universe_d2(aqy_012_accrual_gap_1260, 4)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_004_aqy_012_accrual_gap_1260'] = {'inputs': ['aqy_012_accrual_gap_1260'], 'func': aqy_base_universe_d2_004_aqy_012_accrual_gap_1260}


def aqy_base_universe_d2_005_aqy_016_debt_to_equity_21(aqy_016_debt_to_equity_21):
    return _base_universe_d2(aqy_016_debt_to_equity_21, 5)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_005_aqy_016_debt_to_equity_21'] = {'inputs': ['aqy_016_debt_to_equity_21'], 'func': aqy_base_universe_d2_005_aqy_016_debt_to_equity_21}


def aqy_base_universe_d2_006_aqy_017_debt_to_assets_42(aqy_017_debt_to_assets_42):
    return _base_universe_d2(aqy_017_debt_to_assets_42, 6)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_006_aqy_017_debt_to_assets_42'] = {'inputs': ['aqy_017_debt_to_assets_42'], 'func': aqy_base_universe_d2_006_aqy_017_debt_to_assets_42}


def aqy_base_universe_d2_007_aqy_024_accrual_gap_504(aqy_024_accrual_gap_504):
    return _base_universe_d2(aqy_024_accrual_gap_504, 7)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_007_aqy_024_accrual_gap_504'] = {'inputs': ['aqy_024_accrual_gap_504'], 'func': aqy_base_universe_d2_007_aqy_024_accrual_gap_504}


def aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260(aqy_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(aqy_027_fcf_burn_to_cash_1260, 8)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260'] = {'inputs': ['aqy_027_fcf_burn_to_cash_1260'], 'func': aqy_base_universe_d2_008_aqy_027_fcf_burn_to_cash_1260}


def aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512(aqy_028_debt_to_equity_1512):
    return _base_universe_d2(aqy_028_debt_to_equity_1512, 9)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512'] = {'inputs': ['aqy_028_debt_to_equity_1512'], 'func': aqy_base_universe_d2_009_aqy_028_debt_to_equity_1512}


def aqy_base_universe_d2_010_aqy_029_debt_to_assets_63(aqy_029_debt_to_assets_63):
    return _base_universe_d2(aqy_029_debt_to_assets_63, 10)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_010_aqy_029_debt_to_assets_63'] = {'inputs': ['aqy_029_debt_to_assets_63'], 'func': aqy_base_universe_d2_010_aqy_029_debt_to_assets_63}


def aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21(aqy_031_interest_coverage_stress_21):
    return _base_universe_d2(aqy_031_interest_coverage_stress_21, 11)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21'] = {'inputs': ['aqy_031_interest_coverage_stress_21'], 'func': aqy_base_universe_d2_011_aqy_031_interest_coverage_stress_21}


def aqy_base_universe_d2_012_aqy_036_accrual_gap_189(aqy_036_accrual_gap_189):
    return _base_universe_d2(aqy_036_accrual_gap_189, 12)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_012_aqy_036_accrual_gap_189'] = {'inputs': ['aqy_036_accrual_gap_189'], 'func': aqy_base_universe_d2_012_aqy_036_accrual_gap_189}


def aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504(aqy_039_fcf_burn_to_cash_504):
    return _base_universe_d2(aqy_039_fcf_burn_to_cash_504, 13)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504'] = {'inputs': ['aqy_039_fcf_burn_to_cash_504'], 'func': aqy_base_universe_d2_013_aqy_039_fcf_burn_to_cash_504}


def aqy_base_universe_d2_014_aqy_040_debt_to_equity_756(aqy_040_debt_to_equity_756):
    return _base_universe_d2(aqy_040_debt_to_equity_756, 14)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_014_aqy_040_debt_to_equity_756'] = {'inputs': ['aqy_040_debt_to_equity_756'], 'func': aqy_base_universe_d2_014_aqy_040_debt_to_equity_756}


def aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008(aqy_041_debt_to_assets_1008):
    return _base_universe_d2(aqy_041_debt_to_assets_1008, 15)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008'] = {'inputs': ['aqy_041_debt_to_assets_1008'], 'func': aqy_base_universe_d2_015_aqy_041_debt_to_assets_1008}


def aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512(aqy_043_interest_coverage_stress_1512):
    return _base_universe_d2(aqy_043_interest_coverage_stress_1512, 16)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512'] = {'inputs': ['aqy_043_interest_coverage_stress_1512'], 'func': aqy_base_universe_d2_016_aqy_043_interest_coverage_stress_1512}


def aqy_base_universe_d2_017_aqy_048_accrual_gap_63(aqy_048_accrual_gap_63):
    return _base_universe_d2(aqy_048_accrual_gap_63, 17)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_017_aqy_048_accrual_gap_63'] = {'inputs': ['aqy_048_accrual_gap_63'], 'func': aqy_base_universe_d2_017_aqy_048_accrual_gap_63}


def aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189(aqy_051_fcf_burn_to_cash_189):
    return _base_universe_d2(aqy_051_fcf_burn_to_cash_189, 18)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189'] = {'inputs': ['aqy_051_fcf_burn_to_cash_189'], 'func': aqy_base_universe_d2_018_aqy_051_fcf_burn_to_cash_189}


def aqy_base_universe_d2_019_aqy_052_debt_to_equity_252(aqy_052_debt_to_equity_252):
    return _base_universe_d2(aqy_052_debt_to_equity_252, 19)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_019_aqy_052_debt_to_equity_252'] = {'inputs': ['aqy_052_debt_to_equity_252'], 'func': aqy_base_universe_d2_019_aqy_052_debt_to_equity_252}


def aqy_base_universe_d2_020_aqy_053_debt_to_assets_378(aqy_053_debt_to_assets_378):
    return _base_universe_d2(aqy_053_debt_to_assets_378, 20)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_020_aqy_053_debt_to_assets_378'] = {'inputs': ['aqy_053_debt_to_assets_378'], 'func': aqy_base_universe_d2_020_aqy_053_debt_to_assets_378}


def aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756(aqy_055_interest_coverage_stress_756):
    return _base_universe_d2(aqy_055_interest_coverage_stress_756, 21)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756'] = {'inputs': ['aqy_055_interest_coverage_stress_756'], 'func': aqy_base_universe_d2_021_aqy_055_interest_coverage_stress_756}


def aqy_base_universe_d2_022_aqy_060_accrual_gap_252(aqy_060_accrual_gap_252):
    return _base_universe_d2(aqy_060_accrual_gap_252, 22)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_022_aqy_060_accrual_gap_252'] = {'inputs': ['aqy_060_accrual_gap_252'], 'func': aqy_base_universe_d2_022_aqy_060_accrual_gap_252}


def aqy_base_universe_d2_023_aqy_basefill_001(aqy_basefill_001):
    return _base_universe_d2(aqy_basefill_001, 23)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_023_aqy_basefill_001'] = {'inputs': ['aqy_basefill_001'], 'func': aqy_base_universe_d2_023_aqy_basefill_001}


def aqy_base_universe_d2_024_aqy_basefill_002(aqy_basefill_002):
    return _base_universe_d2(aqy_basefill_002, 24)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_024_aqy_basefill_002'] = {'inputs': ['aqy_basefill_002'], 'func': aqy_base_universe_d2_024_aqy_basefill_002}


def aqy_base_universe_d2_025_aqy_basefill_006(aqy_basefill_006):
    return _base_universe_d2(aqy_basefill_006, 25)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_025_aqy_basefill_006'] = {'inputs': ['aqy_basefill_006'], 'func': aqy_base_universe_d2_025_aqy_basefill_006}


def aqy_base_universe_d2_026_aqy_basefill_008(aqy_basefill_008):
    return _base_universe_d2(aqy_basefill_008, 26)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_026_aqy_basefill_008'] = {'inputs': ['aqy_basefill_008'], 'func': aqy_base_universe_d2_026_aqy_basefill_008}


def aqy_base_universe_d2_027_aqy_basefill_009(aqy_basefill_009):
    return _base_universe_d2(aqy_basefill_009, 27)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_027_aqy_basefill_009'] = {'inputs': ['aqy_basefill_009'], 'func': aqy_base_universe_d2_027_aqy_basefill_009}


def aqy_base_universe_d2_028_aqy_basefill_010(aqy_basefill_010):
    return _base_universe_d2(aqy_basefill_010, 28)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_028_aqy_basefill_010'] = {'inputs': ['aqy_basefill_010'], 'func': aqy_base_universe_d2_028_aqy_basefill_010}


def aqy_base_universe_d2_029_aqy_basefill_011(aqy_basefill_011):
    return _base_universe_d2(aqy_basefill_011, 29)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_029_aqy_basefill_011'] = {'inputs': ['aqy_basefill_011'], 'func': aqy_base_universe_d2_029_aqy_basefill_011}


def aqy_base_universe_d2_030_aqy_basefill_013(aqy_basefill_013):
    return _base_universe_d2(aqy_basefill_013, 30)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_030_aqy_basefill_013'] = {'inputs': ['aqy_basefill_013'], 'func': aqy_base_universe_d2_030_aqy_basefill_013}


def aqy_base_universe_d2_031_aqy_basefill_014(aqy_basefill_014):
    return _base_universe_d2(aqy_basefill_014, 31)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_031_aqy_basefill_014'] = {'inputs': ['aqy_basefill_014'], 'func': aqy_base_universe_d2_031_aqy_basefill_014}


def aqy_base_universe_d2_032_aqy_basefill_015(aqy_basefill_015):
    return _base_universe_d2(aqy_basefill_015, 32)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_032_aqy_basefill_015'] = {'inputs': ['aqy_basefill_015'], 'func': aqy_base_universe_d2_032_aqy_basefill_015}


def aqy_base_universe_d2_033_aqy_basefill_018(aqy_basefill_018):
    return _base_universe_d2(aqy_basefill_018, 33)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_033_aqy_basefill_018'] = {'inputs': ['aqy_basefill_018'], 'func': aqy_base_universe_d2_033_aqy_basefill_018}


def aqy_base_universe_d2_034_aqy_basefill_020(aqy_basefill_020):
    return _base_universe_d2(aqy_basefill_020, 34)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_034_aqy_basefill_020'] = {'inputs': ['aqy_basefill_020'], 'func': aqy_base_universe_d2_034_aqy_basefill_020}


def aqy_base_universe_d2_035_aqy_basefill_021(aqy_basefill_021):
    return _base_universe_d2(aqy_basefill_021, 35)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_035_aqy_basefill_021'] = {'inputs': ['aqy_basefill_021'], 'func': aqy_base_universe_d2_035_aqy_basefill_021}


def aqy_base_universe_d2_036_aqy_basefill_022(aqy_basefill_022):
    return _base_universe_d2(aqy_basefill_022, 36)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_036_aqy_basefill_022'] = {'inputs': ['aqy_basefill_022'], 'func': aqy_base_universe_d2_036_aqy_basefill_022}


def aqy_base_universe_d2_037_aqy_basefill_023(aqy_basefill_023):
    return _base_universe_d2(aqy_basefill_023, 37)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_037_aqy_basefill_023'] = {'inputs': ['aqy_basefill_023'], 'func': aqy_base_universe_d2_037_aqy_basefill_023}


def aqy_base_universe_d2_038_aqy_basefill_025(aqy_basefill_025):
    return _base_universe_d2(aqy_basefill_025, 38)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_038_aqy_basefill_025'] = {'inputs': ['aqy_basefill_025'], 'func': aqy_base_universe_d2_038_aqy_basefill_025}


def aqy_base_universe_d2_039_aqy_basefill_026(aqy_basefill_026):
    return _base_universe_d2(aqy_basefill_026, 39)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_039_aqy_basefill_026'] = {'inputs': ['aqy_basefill_026'], 'func': aqy_base_universe_d2_039_aqy_basefill_026}


def aqy_base_universe_d2_040_aqy_basefill_030(aqy_basefill_030):
    return _base_universe_d2(aqy_basefill_030, 40)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_040_aqy_basefill_030'] = {'inputs': ['aqy_basefill_030'], 'func': aqy_base_universe_d2_040_aqy_basefill_030}


def aqy_base_universe_d2_041_aqy_basefill_032(aqy_basefill_032):
    return _base_universe_d2(aqy_basefill_032, 41)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_041_aqy_basefill_032'] = {'inputs': ['aqy_basefill_032'], 'func': aqy_base_universe_d2_041_aqy_basefill_032}


def aqy_base_universe_d2_042_aqy_basefill_033(aqy_basefill_033):
    return _base_universe_d2(aqy_basefill_033, 42)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_042_aqy_basefill_033'] = {'inputs': ['aqy_basefill_033'], 'func': aqy_base_universe_d2_042_aqy_basefill_033}


def aqy_base_universe_d2_043_aqy_basefill_034(aqy_basefill_034):
    return _base_universe_d2(aqy_basefill_034, 43)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_043_aqy_basefill_034'] = {'inputs': ['aqy_basefill_034'], 'func': aqy_base_universe_d2_043_aqy_basefill_034}


def aqy_base_universe_d2_044_aqy_basefill_035(aqy_basefill_035):
    return _base_universe_d2(aqy_basefill_035, 44)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_044_aqy_basefill_035'] = {'inputs': ['aqy_basefill_035'], 'func': aqy_base_universe_d2_044_aqy_basefill_035}


def aqy_base_universe_d2_045_aqy_basefill_037(aqy_basefill_037):
    return _base_universe_d2(aqy_basefill_037, 45)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_045_aqy_basefill_037'] = {'inputs': ['aqy_basefill_037'], 'func': aqy_base_universe_d2_045_aqy_basefill_037}


def aqy_base_universe_d2_046_aqy_basefill_038(aqy_basefill_038):
    return _base_universe_d2(aqy_basefill_038, 46)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_046_aqy_basefill_038'] = {'inputs': ['aqy_basefill_038'], 'func': aqy_base_universe_d2_046_aqy_basefill_038}


def aqy_base_universe_d2_047_aqy_basefill_042(aqy_basefill_042):
    return _base_universe_d2(aqy_basefill_042, 47)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_047_aqy_basefill_042'] = {'inputs': ['aqy_basefill_042'], 'func': aqy_base_universe_d2_047_aqy_basefill_042}


def aqy_base_universe_d2_048_aqy_basefill_044(aqy_basefill_044):
    return _base_universe_d2(aqy_basefill_044, 48)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_048_aqy_basefill_044'] = {'inputs': ['aqy_basefill_044'], 'func': aqy_base_universe_d2_048_aqy_basefill_044}


def aqy_base_universe_d2_049_aqy_basefill_045(aqy_basefill_045):
    return _base_universe_d2(aqy_basefill_045, 49)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_049_aqy_basefill_045'] = {'inputs': ['aqy_basefill_045'], 'func': aqy_base_universe_d2_049_aqy_basefill_045}


def aqy_base_universe_d2_050_aqy_basefill_046(aqy_basefill_046):
    return _base_universe_d2(aqy_basefill_046, 50)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_050_aqy_basefill_046'] = {'inputs': ['aqy_basefill_046'], 'func': aqy_base_universe_d2_050_aqy_basefill_046}


def aqy_base_universe_d2_051_aqy_basefill_047(aqy_basefill_047):
    return _base_universe_d2(aqy_basefill_047, 51)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_051_aqy_basefill_047'] = {'inputs': ['aqy_basefill_047'], 'func': aqy_base_universe_d2_051_aqy_basefill_047}


def aqy_base_universe_d2_052_aqy_basefill_049(aqy_basefill_049):
    return _base_universe_d2(aqy_basefill_049, 52)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_052_aqy_basefill_049'] = {'inputs': ['aqy_basefill_049'], 'func': aqy_base_universe_d2_052_aqy_basefill_049}


def aqy_base_universe_d2_053_aqy_basefill_050(aqy_basefill_050):
    return _base_universe_d2(aqy_basefill_050, 53)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_053_aqy_basefill_050'] = {'inputs': ['aqy_basefill_050'], 'func': aqy_base_universe_d2_053_aqy_basefill_050}


def aqy_base_universe_d2_054_aqy_basefill_054(aqy_basefill_054):
    return _base_universe_d2(aqy_basefill_054, 54)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_054_aqy_basefill_054'] = {'inputs': ['aqy_basefill_054'], 'func': aqy_base_universe_d2_054_aqy_basefill_054}


def aqy_base_universe_d2_055_aqy_basefill_056(aqy_basefill_056):
    return _base_universe_d2(aqy_basefill_056, 55)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_055_aqy_basefill_056'] = {'inputs': ['aqy_basefill_056'], 'func': aqy_base_universe_d2_055_aqy_basefill_056}


def aqy_base_universe_d2_056_aqy_basefill_057(aqy_basefill_057):
    return _base_universe_d2(aqy_basefill_057, 56)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_056_aqy_basefill_057'] = {'inputs': ['aqy_basefill_057'], 'func': aqy_base_universe_d2_056_aqy_basefill_057}


def aqy_base_universe_d2_057_aqy_basefill_058(aqy_basefill_058):
    return _base_universe_d2(aqy_basefill_058, 57)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_057_aqy_basefill_058'] = {'inputs': ['aqy_basefill_058'], 'func': aqy_base_universe_d2_057_aqy_basefill_058}


def aqy_base_universe_d2_058_aqy_basefill_059(aqy_basefill_059):
    return _base_universe_d2(aqy_basefill_059, 58)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_058_aqy_basefill_059'] = {'inputs': ['aqy_basefill_059'], 'func': aqy_base_universe_d2_058_aqy_basefill_059}


def aqy_base_universe_d2_059_aqy_basefill_061(aqy_basefill_061):
    return _base_universe_d2(aqy_basefill_061, 59)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_059_aqy_basefill_061'] = {'inputs': ['aqy_basefill_061'], 'func': aqy_base_universe_d2_059_aqy_basefill_061}


def aqy_base_universe_d2_060_aqy_basefill_062(aqy_basefill_062):
    return _base_universe_d2(aqy_basefill_062, 60)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_060_aqy_basefill_062'] = {'inputs': ['aqy_basefill_062'], 'func': aqy_base_universe_d2_060_aqy_basefill_062}


def aqy_base_universe_d2_061_aqy_basefill_063(aqy_basefill_063):
    return _base_universe_d2(aqy_basefill_063, 61)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_061_aqy_basefill_063'] = {'inputs': ['aqy_basefill_063'], 'func': aqy_base_universe_d2_061_aqy_basefill_063}


def aqy_base_universe_d2_062_aqy_basefill_064(aqy_basefill_064):
    return _base_universe_d2(aqy_basefill_064, 62)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_062_aqy_basefill_064'] = {'inputs': ['aqy_basefill_064'], 'func': aqy_base_universe_d2_062_aqy_basefill_064}


def aqy_base_universe_d2_063_aqy_basefill_065(aqy_basefill_065):
    return _base_universe_d2(aqy_basefill_065, 63)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_063_aqy_basefill_065'] = {'inputs': ['aqy_basefill_065'], 'func': aqy_base_universe_d2_063_aqy_basefill_065}


def aqy_base_universe_d2_064_aqy_basefill_066(aqy_basefill_066):
    return _base_universe_d2(aqy_basefill_066, 64)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_064_aqy_basefill_066'] = {'inputs': ['aqy_basefill_066'], 'func': aqy_base_universe_d2_064_aqy_basefill_066}


def aqy_base_universe_d2_065_aqy_basefill_067(aqy_basefill_067):
    return _base_universe_d2(aqy_basefill_067, 65)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_065_aqy_basefill_067'] = {'inputs': ['aqy_basefill_067'], 'func': aqy_base_universe_d2_065_aqy_basefill_067}


def aqy_base_universe_d2_066_aqy_basefill_068(aqy_basefill_068):
    return _base_universe_d2(aqy_basefill_068, 66)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_066_aqy_basefill_068'] = {'inputs': ['aqy_basefill_068'], 'func': aqy_base_universe_d2_066_aqy_basefill_068}


def aqy_base_universe_d2_067_aqy_basefill_069(aqy_basefill_069):
    return _base_universe_d2(aqy_basefill_069, 67)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_067_aqy_basefill_069'] = {'inputs': ['aqy_basefill_069'], 'func': aqy_base_universe_d2_067_aqy_basefill_069}


def aqy_base_universe_d2_068_aqy_basefill_070(aqy_basefill_070):
    return _base_universe_d2(aqy_basefill_070, 68)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_068_aqy_basefill_070'] = {'inputs': ['aqy_basefill_070'], 'func': aqy_base_universe_d2_068_aqy_basefill_070}


def aqy_base_universe_d2_069_aqy_basefill_071(aqy_basefill_071):
    return _base_universe_d2(aqy_basefill_071, 69)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_069_aqy_basefill_071'] = {'inputs': ['aqy_basefill_071'], 'func': aqy_base_universe_d2_069_aqy_basefill_071}


def aqy_base_universe_d2_070_aqy_basefill_072(aqy_basefill_072):
    return _base_universe_d2(aqy_basefill_072, 70)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_070_aqy_basefill_072'] = {'inputs': ['aqy_basefill_072'], 'func': aqy_base_universe_d2_070_aqy_basefill_072}


def aqy_base_universe_d2_071_aqy_basefill_073(aqy_basefill_073):
    return _base_universe_d2(aqy_basefill_073, 71)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_071_aqy_basefill_073'] = {'inputs': ['aqy_basefill_073'], 'func': aqy_base_universe_d2_071_aqy_basefill_073}


def aqy_base_universe_d2_072_aqy_basefill_074(aqy_basefill_074):
    return _base_universe_d2(aqy_basefill_074, 72)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_072_aqy_basefill_074'] = {'inputs': ['aqy_basefill_074'], 'func': aqy_base_universe_d2_072_aqy_basefill_074}


def aqy_base_universe_d2_073_aqy_basefill_075(aqy_basefill_075):
    return _base_universe_d2(aqy_basefill_075, 73)
AQY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['aqy_base_universe_d2_073_aqy_basefill_075'] = {'inputs': ['aqy_basefill_075'], 'func': aqy_base_universe_d2_073_aqy_basefill_075}
