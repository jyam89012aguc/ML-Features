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



def mgc_151_mgc_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def mgc_152_mgc_007_interest_coverage_stress_252_roc_42(mgc_007_interest_coverage_stress_252):
    feature = _s(mgc_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def mgc_153_mgc_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def mgc_154_mgc_019_interest_coverage_stress_84_roc_378(mgc_019_interest_coverage_stress_84):
    feature = _s(mgc_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def mgc_155_mgc_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















MARGIN_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    'mgc_151_mgc_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': mgc_151_mgc_001_netinc_decline_1_roc_1},
    'mgc_152_mgc_007_interest_coverage_stress_252_roc_42': {'inputs': ['mgc_007_interest_coverage_stress_252'], 'func': mgc_152_mgc_007_interest_coverage_stress_252_roc_42},
    'mgc_153_mgc_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': mgc_153_mgc_013_netinc_decline_1_roc_126},
    'mgc_154_mgc_019_interest_coverage_stress_84_roc_378': {'inputs': ['mgc_019_interest_coverage_stress_84'], 'func': mgc_154_mgc_019_interest_coverage_stress_84_roc_378},
    'mgc_155_mgc_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': mgc_155_mgc_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def mc_replacement_d2_001(mc_replacement_001):
    feature = _clean(mc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_001'] = {'inputs': ['mc_replacement_001'], 'func': mc_replacement_d2_001}


def mc_replacement_d2_002(mc_replacement_002):
    feature = _clean(mc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_002'] = {'inputs': ['mc_replacement_002'], 'func': mc_replacement_d2_002}


def mc_replacement_d2_003(mc_replacement_003):
    feature = _clean(mc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_003'] = {'inputs': ['mc_replacement_003'], 'func': mc_replacement_d2_003}


def mc_replacement_d2_004(mc_replacement_004):
    feature = _clean(mc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_004'] = {'inputs': ['mc_replacement_004'], 'func': mc_replacement_d2_004}


def mc_replacement_d2_005(mc_replacement_005):
    feature = _clean(mc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_005'] = {'inputs': ['mc_replacement_005'], 'func': mc_replacement_d2_005}


def mc_replacement_d2_006(mc_replacement_006):
    feature = _clean(mc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_006'] = {'inputs': ['mc_replacement_006'], 'func': mc_replacement_d2_006}


def mc_replacement_d2_007(mc_replacement_007):
    feature = _clean(mc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_007'] = {'inputs': ['mc_replacement_007'], 'func': mc_replacement_d2_007}


def mc_replacement_d2_008(mc_replacement_008):
    feature = _clean(mc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_008'] = {'inputs': ['mc_replacement_008'], 'func': mc_replacement_d2_008}


def mc_replacement_d2_009(mc_replacement_009):
    feature = _clean(mc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_009'] = {'inputs': ['mc_replacement_009'], 'func': mc_replacement_d2_009}


def mc_replacement_d2_010(mc_replacement_010):
    feature = _clean(mc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_010'] = {'inputs': ['mc_replacement_010'], 'func': mc_replacement_d2_010}


def mc_replacement_d2_011(mc_replacement_011):
    feature = _clean(mc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_011'] = {'inputs': ['mc_replacement_011'], 'func': mc_replacement_d2_011}


def mc_replacement_d2_012(mc_replacement_012):
    feature = _clean(mc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_012'] = {'inputs': ['mc_replacement_012'], 'func': mc_replacement_d2_012}


def mc_replacement_d2_013(mc_replacement_013):
    feature = _clean(mc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_013'] = {'inputs': ['mc_replacement_013'], 'func': mc_replacement_d2_013}


def mc_replacement_d2_014(mc_replacement_014):
    feature = _clean(mc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_014'] = {'inputs': ['mc_replacement_014'], 'func': mc_replacement_d2_014}


def mc_replacement_d2_015(mc_replacement_015):
    feature = _clean(mc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_015'] = {'inputs': ['mc_replacement_015'], 'func': mc_replacement_d2_015}


def mc_replacement_d2_016(mc_replacement_016):
    feature = _clean(mc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_016'] = {'inputs': ['mc_replacement_016'], 'func': mc_replacement_d2_016}


def mc_replacement_d2_017(mc_replacement_017):
    feature = _clean(mc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_017'] = {'inputs': ['mc_replacement_017'], 'func': mc_replacement_d2_017}


def mc_replacement_d2_018(mc_replacement_018):
    feature = _clean(mc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_018'] = {'inputs': ['mc_replacement_018'], 'func': mc_replacement_d2_018}


def mc_replacement_d2_019(mc_replacement_019):
    feature = _clean(mc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_019'] = {'inputs': ['mc_replacement_019'], 'func': mc_replacement_d2_019}


def mc_replacement_d2_020(mc_replacement_020):
    feature = _clean(mc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_020'] = {'inputs': ['mc_replacement_020'], 'func': mc_replacement_d2_020}


def mc_replacement_d2_021(mc_replacement_021):
    feature = _clean(mc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_021'] = {'inputs': ['mc_replacement_021'], 'func': mc_replacement_d2_021}


def mc_replacement_d2_022(mc_replacement_022):
    feature = _clean(mc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_022'] = {'inputs': ['mc_replacement_022'], 'func': mc_replacement_d2_022}


def mc_replacement_d2_023(mc_replacement_023):
    feature = _clean(mc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_023'] = {'inputs': ['mc_replacement_023'], 'func': mc_replacement_d2_023}


def mc_replacement_d2_024(mc_replacement_024):
    feature = _clean(mc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_024'] = {'inputs': ['mc_replacement_024'], 'func': mc_replacement_d2_024}


def mc_replacement_d2_025(mc_replacement_025):
    feature = _clean(mc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_025'] = {'inputs': ['mc_replacement_025'], 'func': mc_replacement_d2_025}


def mc_replacement_d2_026(mc_replacement_026):
    feature = _clean(mc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_026'] = {'inputs': ['mc_replacement_026'], 'func': mc_replacement_d2_026}


def mc_replacement_d2_027(mc_replacement_027):
    feature = _clean(mc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_027'] = {'inputs': ['mc_replacement_027'], 'func': mc_replacement_d2_027}


def mc_replacement_d2_028(mc_replacement_028):
    feature = _clean(mc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_028'] = {'inputs': ['mc_replacement_028'], 'func': mc_replacement_d2_028}


def mc_replacement_d2_029(mc_replacement_029):
    feature = _clean(mc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_029'] = {'inputs': ['mc_replacement_029'], 'func': mc_replacement_d2_029}


def mc_replacement_d2_030(mc_replacement_030):
    feature = _clean(mc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_030'] = {'inputs': ['mc_replacement_030'], 'func': mc_replacement_d2_030}


def mc_replacement_d2_031(mc_replacement_031):
    feature = _clean(mc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_031'] = {'inputs': ['mc_replacement_031'], 'func': mc_replacement_d2_031}


def mc_replacement_d2_032(mc_replacement_032):
    feature = _clean(mc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_032'] = {'inputs': ['mc_replacement_032'], 'func': mc_replacement_d2_032}


def mc_replacement_d2_033(mc_replacement_033):
    feature = _clean(mc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_033'] = {'inputs': ['mc_replacement_033'], 'func': mc_replacement_d2_033}


def mc_replacement_d2_034(mc_replacement_034):
    feature = _clean(mc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_034'] = {'inputs': ['mc_replacement_034'], 'func': mc_replacement_d2_034}


def mc_replacement_d2_035(mc_replacement_035):
    feature = _clean(mc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_035'] = {'inputs': ['mc_replacement_035'], 'func': mc_replacement_d2_035}


def mc_replacement_d2_036(mc_replacement_036):
    feature = _clean(mc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_036'] = {'inputs': ['mc_replacement_036'], 'func': mc_replacement_d2_036}


def mc_replacement_d2_037(mc_replacement_037):
    feature = _clean(mc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_037'] = {'inputs': ['mc_replacement_037'], 'func': mc_replacement_d2_037}


def mc_replacement_d2_038(mc_replacement_038):
    feature = _clean(mc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_038'] = {'inputs': ['mc_replacement_038'], 'func': mc_replacement_d2_038}


def mc_replacement_d2_039(mc_replacement_039):
    feature = _clean(mc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_039'] = {'inputs': ['mc_replacement_039'], 'func': mc_replacement_d2_039}


def mc_replacement_d2_040(mc_replacement_040):
    feature = _clean(mc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_040'] = {'inputs': ['mc_replacement_040'], 'func': mc_replacement_d2_040}


def mc_replacement_d2_041(mc_replacement_041):
    feature = _clean(mc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_041'] = {'inputs': ['mc_replacement_041'], 'func': mc_replacement_d2_041}


def mc_replacement_d2_042(mc_replacement_042):
    feature = _clean(mc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_042'] = {'inputs': ['mc_replacement_042'], 'func': mc_replacement_d2_042}


def mc_replacement_d2_043(mc_replacement_043):
    feature = _clean(mc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_043'] = {'inputs': ['mc_replacement_043'], 'func': mc_replacement_d2_043}


def mc_replacement_d2_044(mc_replacement_044):
    feature = _clean(mc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_044'] = {'inputs': ['mc_replacement_044'], 'func': mc_replacement_d2_044}


def mc_replacement_d2_045(mc_replacement_045):
    feature = _clean(mc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_045'] = {'inputs': ['mc_replacement_045'], 'func': mc_replacement_d2_045}


def mc_replacement_d2_046(mc_replacement_046):
    feature = _clean(mc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_046'] = {'inputs': ['mc_replacement_046'], 'func': mc_replacement_d2_046}


def mc_replacement_d2_047(mc_replacement_047):
    feature = _clean(mc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_047'] = {'inputs': ['mc_replacement_047'], 'func': mc_replacement_d2_047}


def mc_replacement_d2_048(mc_replacement_048):
    feature = _clean(mc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_048'] = {'inputs': ['mc_replacement_048'], 'func': mc_replacement_d2_048}


def mc_replacement_d2_049(mc_replacement_049):
    feature = _clean(mc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_049'] = {'inputs': ['mc_replacement_049'], 'func': mc_replacement_d2_049}


def mc_replacement_d2_050(mc_replacement_050):
    feature = _clean(mc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_050'] = {'inputs': ['mc_replacement_050'], 'func': mc_replacement_d2_050}


def mc_replacement_d2_051(mc_replacement_051):
    feature = _clean(mc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_051'] = {'inputs': ['mc_replacement_051'], 'func': mc_replacement_d2_051}


def mc_replacement_d2_052(mc_replacement_052):
    feature = _clean(mc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_052'] = {'inputs': ['mc_replacement_052'], 'func': mc_replacement_d2_052}


def mc_replacement_d2_053(mc_replacement_053):
    feature = _clean(mc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_053'] = {'inputs': ['mc_replacement_053'], 'func': mc_replacement_d2_053}


def mc_replacement_d2_054(mc_replacement_054):
    feature = _clean(mc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_054'] = {'inputs': ['mc_replacement_054'], 'func': mc_replacement_d2_054}


def mc_replacement_d2_055(mc_replacement_055):
    feature = _clean(mc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_055'] = {'inputs': ['mc_replacement_055'], 'func': mc_replacement_d2_055}


def mc_replacement_d2_056(mc_replacement_056):
    feature = _clean(mc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_056'] = {'inputs': ['mc_replacement_056'], 'func': mc_replacement_d2_056}


def mc_replacement_d2_057(mc_replacement_057):
    feature = _clean(mc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_057'] = {'inputs': ['mc_replacement_057'], 'func': mc_replacement_d2_057}


def mc_replacement_d2_058(mc_replacement_058):
    feature = _clean(mc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_058'] = {'inputs': ['mc_replacement_058'], 'func': mc_replacement_d2_058}


def mc_replacement_d2_059(mc_replacement_059):
    feature = _clean(mc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_059'] = {'inputs': ['mc_replacement_059'], 'func': mc_replacement_d2_059}


def mc_replacement_d2_060(mc_replacement_060):
    feature = _clean(mc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_060'] = {'inputs': ['mc_replacement_060'], 'func': mc_replacement_d2_060}


def mc_replacement_d2_061(mc_replacement_061):
    feature = _clean(mc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_061'] = {'inputs': ['mc_replacement_061'], 'func': mc_replacement_d2_061}


def mc_replacement_d2_062(mc_replacement_062):
    feature = _clean(mc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_062'] = {'inputs': ['mc_replacement_062'], 'func': mc_replacement_d2_062}


def mc_replacement_d2_063(mc_replacement_063):
    feature = _clean(mc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_063'] = {'inputs': ['mc_replacement_063'], 'func': mc_replacement_d2_063}


def mc_replacement_d2_064(mc_replacement_064):
    feature = _clean(mc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_064'] = {'inputs': ['mc_replacement_064'], 'func': mc_replacement_d2_064}


def mc_replacement_d2_065(mc_replacement_065):
    feature = _clean(mc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_065'] = {'inputs': ['mc_replacement_065'], 'func': mc_replacement_d2_065}


def mc_replacement_d2_066(mc_replacement_066):
    feature = _clean(mc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_066'] = {'inputs': ['mc_replacement_066'], 'func': mc_replacement_d2_066}


def mc_replacement_d2_067(mc_replacement_067):
    feature = _clean(mc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_067'] = {'inputs': ['mc_replacement_067'], 'func': mc_replacement_d2_067}


def mc_replacement_d2_068(mc_replacement_068):
    feature = _clean(mc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_068'] = {'inputs': ['mc_replacement_068'], 'func': mc_replacement_d2_068}


def mc_replacement_d2_069(mc_replacement_069):
    feature = _clean(mc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_069'] = {'inputs': ['mc_replacement_069'], 'func': mc_replacement_d2_069}


def mc_replacement_d2_070(mc_replacement_070):
    feature = _clean(mc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_070'] = {'inputs': ['mc_replacement_070'], 'func': mc_replacement_d2_070}


def mc_replacement_d2_071(mc_replacement_071):
    feature = _clean(mc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_071'] = {'inputs': ['mc_replacement_071'], 'func': mc_replacement_d2_071}


def mc_replacement_d2_072(mc_replacement_072):
    feature = _clean(mc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_072'] = {'inputs': ['mc_replacement_072'], 'func': mc_replacement_d2_072}


def mc_replacement_d2_073(mc_replacement_073):
    feature = _clean(mc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_073'] = {'inputs': ['mc_replacement_073'], 'func': mc_replacement_d2_073}


def mc_replacement_d2_074(mc_replacement_074):
    feature = _clean(mc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_074'] = {'inputs': ['mc_replacement_074'], 'func': mc_replacement_d2_074}


def mc_replacement_d2_075(mc_replacement_075):
    feature = _clean(mc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_075'] = {'inputs': ['mc_replacement_075'], 'func': mc_replacement_d2_075}


def mc_replacement_d2_076(mc_replacement_076):
    feature = _clean(mc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_076'] = {'inputs': ['mc_replacement_076'], 'func': mc_replacement_d2_076}


def mc_replacement_d2_077(mc_replacement_077):
    feature = _clean(mc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_077'] = {'inputs': ['mc_replacement_077'], 'func': mc_replacement_d2_077}


def mc_replacement_d2_078(mc_replacement_078):
    feature = _clean(mc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_078'] = {'inputs': ['mc_replacement_078'], 'func': mc_replacement_d2_078}


def mc_replacement_d2_079(mc_replacement_079):
    feature = _clean(mc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_079'] = {'inputs': ['mc_replacement_079'], 'func': mc_replacement_d2_079}


def mc_replacement_d2_080(mc_replacement_080):
    feature = _clean(mc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_080'] = {'inputs': ['mc_replacement_080'], 'func': mc_replacement_d2_080}


def mc_replacement_d2_081(mc_replacement_081):
    feature = _clean(mc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_081'] = {'inputs': ['mc_replacement_081'], 'func': mc_replacement_d2_081}


def mc_replacement_d2_082(mc_replacement_082):
    feature = _clean(mc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_082'] = {'inputs': ['mc_replacement_082'], 'func': mc_replacement_d2_082}


def mc_replacement_d2_083(mc_replacement_083):
    feature = _clean(mc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_083'] = {'inputs': ['mc_replacement_083'], 'func': mc_replacement_d2_083}


def mc_replacement_d2_084(mc_replacement_084):
    feature = _clean(mc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_084'] = {'inputs': ['mc_replacement_084'], 'func': mc_replacement_d2_084}


def mc_replacement_d2_085(mc_replacement_085):
    feature = _clean(mc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_085'] = {'inputs': ['mc_replacement_085'], 'func': mc_replacement_d2_085}


def mc_replacement_d2_086(mc_replacement_086):
    feature = _clean(mc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_086'] = {'inputs': ['mc_replacement_086'], 'func': mc_replacement_d2_086}


def mc_replacement_d2_087(mc_replacement_087):
    feature = _clean(mc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_087'] = {'inputs': ['mc_replacement_087'], 'func': mc_replacement_d2_087}


def mc_replacement_d2_088(mc_replacement_088):
    feature = _clean(mc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_088'] = {'inputs': ['mc_replacement_088'], 'func': mc_replacement_d2_088}


def mc_replacement_d2_089(mc_replacement_089):
    feature = _clean(mc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_089'] = {'inputs': ['mc_replacement_089'], 'func': mc_replacement_d2_089}


def mc_replacement_d2_090(mc_replacement_090):
    feature = _clean(mc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_090'] = {'inputs': ['mc_replacement_090'], 'func': mc_replacement_d2_090}


def mc_replacement_d2_091(mc_replacement_091):
    feature = _clean(mc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_091'] = {'inputs': ['mc_replacement_091'], 'func': mc_replacement_d2_091}


def mc_replacement_d2_092(mc_replacement_092):
    feature = _clean(mc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_092'] = {'inputs': ['mc_replacement_092'], 'func': mc_replacement_d2_092}


def mc_replacement_d2_093(mc_replacement_093):
    feature = _clean(mc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_093'] = {'inputs': ['mc_replacement_093'], 'func': mc_replacement_d2_093}


def mc_replacement_d2_094(mc_replacement_094):
    feature = _clean(mc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_094'] = {'inputs': ['mc_replacement_094'], 'func': mc_replacement_d2_094}


def mc_replacement_d2_095(mc_replacement_095):
    feature = _clean(mc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_095'] = {'inputs': ['mc_replacement_095'], 'func': mc_replacement_d2_095}


def mc_replacement_d2_096(mc_replacement_096):
    feature = _clean(mc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_096'] = {'inputs': ['mc_replacement_096'], 'func': mc_replacement_d2_096}


def mc_replacement_d2_097(mc_replacement_097):
    feature = _clean(mc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_097'] = {'inputs': ['mc_replacement_097'], 'func': mc_replacement_d2_097}


def mc_replacement_d2_098(mc_replacement_098):
    feature = _clean(mc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_098'] = {'inputs': ['mc_replacement_098'], 'func': mc_replacement_d2_098}


def mc_replacement_d2_099(mc_replacement_099):
    feature = _clean(mc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_099'] = {'inputs': ['mc_replacement_099'], 'func': mc_replacement_d2_099}


def mc_replacement_d2_100(mc_replacement_100):
    feature = _clean(mc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_100'] = {'inputs': ['mc_replacement_100'], 'func': mc_replacement_d2_100}


def mc_replacement_d2_101(mc_replacement_101):
    feature = _clean(mc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_101'] = {'inputs': ['mc_replacement_101'], 'func': mc_replacement_d2_101}


def mc_replacement_d2_102(mc_replacement_102):
    feature = _clean(mc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_102'] = {'inputs': ['mc_replacement_102'], 'func': mc_replacement_d2_102}


def mc_replacement_d2_103(mc_replacement_103):
    feature = _clean(mc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_103'] = {'inputs': ['mc_replacement_103'], 'func': mc_replacement_d2_103}


def mc_replacement_d2_104(mc_replacement_104):
    feature = _clean(mc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_104'] = {'inputs': ['mc_replacement_104'], 'func': mc_replacement_d2_104}


def mc_replacement_d2_105(mc_replacement_105):
    feature = _clean(mc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_105'] = {'inputs': ['mc_replacement_105'], 'func': mc_replacement_d2_105}


def mc_replacement_d2_106(mc_replacement_106):
    feature = _clean(mc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_106'] = {'inputs': ['mc_replacement_106'], 'func': mc_replacement_d2_106}


def mc_replacement_d2_107(mc_replacement_107):
    feature = _clean(mc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_107'] = {'inputs': ['mc_replacement_107'], 'func': mc_replacement_d2_107}


def mc_replacement_d2_108(mc_replacement_108):
    feature = _clean(mc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_108'] = {'inputs': ['mc_replacement_108'], 'func': mc_replacement_d2_108}


def mc_replacement_d2_109(mc_replacement_109):
    feature = _clean(mc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_109'] = {'inputs': ['mc_replacement_109'], 'func': mc_replacement_d2_109}


def mc_replacement_d2_110(mc_replacement_110):
    feature = _clean(mc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_110'] = {'inputs': ['mc_replacement_110'], 'func': mc_replacement_d2_110}


def mc_replacement_d2_111(mc_replacement_111):
    feature = _clean(mc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_111'] = {'inputs': ['mc_replacement_111'], 'func': mc_replacement_d2_111}


def mc_replacement_d2_112(mc_replacement_112):
    feature = _clean(mc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_112'] = {'inputs': ['mc_replacement_112'], 'func': mc_replacement_d2_112}


def mc_replacement_d2_113(mc_replacement_113):
    feature = _clean(mc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_113'] = {'inputs': ['mc_replacement_113'], 'func': mc_replacement_d2_113}


def mc_replacement_d2_114(mc_replacement_114):
    feature = _clean(mc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_114'] = {'inputs': ['mc_replacement_114'], 'func': mc_replacement_d2_114}


def mc_replacement_d2_115(mc_replacement_115):
    feature = _clean(mc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_115'] = {'inputs': ['mc_replacement_115'], 'func': mc_replacement_d2_115}


def mc_replacement_d2_116(mc_replacement_116):
    feature = _clean(mc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_116'] = {'inputs': ['mc_replacement_116'], 'func': mc_replacement_d2_116}


def mc_replacement_d2_117(mc_replacement_117):
    feature = _clean(mc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_117'] = {'inputs': ['mc_replacement_117'], 'func': mc_replacement_d2_117}


def mc_replacement_d2_118(mc_replacement_118):
    feature = _clean(mc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_118'] = {'inputs': ['mc_replacement_118'], 'func': mc_replacement_d2_118}


def mc_replacement_d2_119(mc_replacement_119):
    feature = _clean(mc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_119'] = {'inputs': ['mc_replacement_119'], 'func': mc_replacement_d2_119}


def mc_replacement_d2_120(mc_replacement_120):
    feature = _clean(mc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_120'] = {'inputs': ['mc_replacement_120'], 'func': mc_replacement_d2_120}


def mc_replacement_d2_121(mc_replacement_121):
    feature = _clean(mc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_121'] = {'inputs': ['mc_replacement_121'], 'func': mc_replacement_d2_121}


def mc_replacement_d2_122(mc_replacement_122):
    feature = _clean(mc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_122'] = {'inputs': ['mc_replacement_122'], 'func': mc_replacement_d2_122}


def mc_replacement_d2_123(mc_replacement_123):
    feature = _clean(mc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_123'] = {'inputs': ['mc_replacement_123'], 'func': mc_replacement_d2_123}


def mc_replacement_d2_124(mc_replacement_124):
    feature = _clean(mc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_124'] = {'inputs': ['mc_replacement_124'], 'func': mc_replacement_d2_124}


def mc_replacement_d2_125(mc_replacement_125):
    feature = _clean(mc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_125'] = {'inputs': ['mc_replacement_125'], 'func': mc_replacement_d2_125}


def mc_replacement_d2_126(mc_replacement_126):
    feature = _clean(mc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_126'] = {'inputs': ['mc_replacement_126'], 'func': mc_replacement_d2_126}


def mc_replacement_d2_127(mc_replacement_127):
    feature = _clean(mc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_127'] = {'inputs': ['mc_replacement_127'], 'func': mc_replacement_d2_127}


def mc_replacement_d2_128(mc_replacement_128):
    feature = _clean(mc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_128'] = {'inputs': ['mc_replacement_128'], 'func': mc_replacement_d2_128}


def mc_replacement_d2_129(mc_replacement_129):
    feature = _clean(mc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_129'] = {'inputs': ['mc_replacement_129'], 'func': mc_replacement_d2_129}


def mc_replacement_d2_130(mc_replacement_130):
    feature = _clean(mc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_130'] = {'inputs': ['mc_replacement_130'], 'func': mc_replacement_d2_130}


def mc_replacement_d2_131(mc_replacement_131):
    feature = _clean(mc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_131'] = {'inputs': ['mc_replacement_131'], 'func': mc_replacement_d2_131}


def mc_replacement_d2_132(mc_replacement_132):
    feature = _clean(mc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_132'] = {'inputs': ['mc_replacement_132'], 'func': mc_replacement_d2_132}


def mc_replacement_d2_133(mc_replacement_133):
    feature = _clean(mc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_133'] = {'inputs': ['mc_replacement_133'], 'func': mc_replacement_d2_133}


def mc_replacement_d2_134(mc_replacement_134):
    feature = _clean(mc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_134'] = {'inputs': ['mc_replacement_134'], 'func': mc_replacement_d2_134}


def mc_replacement_d2_135(mc_replacement_135):
    feature = _clean(mc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_135'] = {'inputs': ['mc_replacement_135'], 'func': mc_replacement_d2_135}


def mc_replacement_d2_136(mc_replacement_136):
    feature = _clean(mc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_136'] = {'inputs': ['mc_replacement_136'], 'func': mc_replacement_d2_136}


def mc_replacement_d2_137(mc_replacement_137):
    feature = _clean(mc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_137'] = {'inputs': ['mc_replacement_137'], 'func': mc_replacement_d2_137}


def mc_replacement_d2_138(mc_replacement_138):
    feature = _clean(mc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_138'] = {'inputs': ['mc_replacement_138'], 'func': mc_replacement_d2_138}


def mc_replacement_d2_139(mc_replacement_139):
    feature = _clean(mc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_139'] = {'inputs': ['mc_replacement_139'], 'func': mc_replacement_d2_139}


def mc_replacement_d2_140(mc_replacement_140):
    feature = _clean(mc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_140'] = {'inputs': ['mc_replacement_140'], 'func': mc_replacement_d2_140}


def mc_replacement_d2_141(mc_replacement_141):
    feature = _clean(mc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_141'] = {'inputs': ['mc_replacement_141'], 'func': mc_replacement_d2_141}


def mc_replacement_d2_142(mc_replacement_142):
    feature = _clean(mc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_142'] = {'inputs': ['mc_replacement_142'], 'func': mc_replacement_d2_142}


def mc_replacement_d2_143(mc_replacement_143):
    feature = _clean(mc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_143'] = {'inputs': ['mc_replacement_143'], 'func': mc_replacement_d2_143}


def mc_replacement_d2_144(mc_replacement_144):
    feature = _clean(mc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_144'] = {'inputs': ['mc_replacement_144'], 'func': mc_replacement_d2_144}


def mc_replacement_d2_145(mc_replacement_145):
    feature = _clean(mc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_145'] = {'inputs': ['mc_replacement_145'], 'func': mc_replacement_d2_145}


def mc_replacement_d2_146(mc_replacement_146):
    feature = _clean(mc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_146'] = {'inputs': ['mc_replacement_146'], 'func': mc_replacement_d2_146}


def mc_replacement_d2_147(mc_replacement_147):
    feature = _clean(mc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_147'] = {'inputs': ['mc_replacement_147'], 'func': mc_replacement_d2_147}


def mc_replacement_d2_148(mc_replacement_148):
    feature = _clean(mc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_148'] = {'inputs': ['mc_replacement_148'], 'func': mc_replacement_d2_148}


def mc_replacement_d2_149(mc_replacement_149):
    feature = _clean(mc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_149'] = {'inputs': ['mc_replacement_149'], 'func': mc_replacement_d2_149}


def mc_replacement_d2_150(mc_replacement_150):
    feature = _clean(mc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_150'] = {'inputs': ['mc_replacement_150'], 'func': mc_replacement_d2_150}


def mc_replacement_d2_151(mc_replacement_151):
    feature = _clean(mc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_151'] = {'inputs': ['mc_replacement_151'], 'func': mc_replacement_d2_151}


def mc_replacement_d2_152(mc_replacement_152):
    feature = _clean(mc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_152'] = {'inputs': ['mc_replacement_152'], 'func': mc_replacement_d2_152}


def mc_replacement_d2_153(mc_replacement_153):
    feature = _clean(mc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_153'] = {'inputs': ['mc_replacement_153'], 'func': mc_replacement_d2_153}


def mc_replacement_d2_154(mc_replacement_154):
    feature = _clean(mc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_154'] = {'inputs': ['mc_replacement_154'], 'func': mc_replacement_d2_154}


def mc_replacement_d2_155(mc_replacement_155):
    feature = _clean(mc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_155'] = {'inputs': ['mc_replacement_155'], 'func': mc_replacement_d2_155}


def mc_replacement_d2_156(mc_replacement_156):
    feature = _clean(mc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_156'] = {'inputs': ['mc_replacement_156'], 'func': mc_replacement_d2_156}


def mc_replacement_d2_157(mc_replacement_157):
    feature = _clean(mc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_157'] = {'inputs': ['mc_replacement_157'], 'func': mc_replacement_d2_157}


def mc_replacement_d2_158(mc_replacement_158):
    feature = _clean(mc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_158'] = {'inputs': ['mc_replacement_158'], 'func': mc_replacement_d2_158}


def mc_replacement_d2_159(mc_replacement_159):
    feature = _clean(mc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_159'] = {'inputs': ['mc_replacement_159'], 'func': mc_replacement_d2_159}


def mc_replacement_d2_160(mc_replacement_160):
    feature = _clean(mc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_160'] = {'inputs': ['mc_replacement_160'], 'func': mc_replacement_d2_160}


def mc_replacement_d2_161(mc_replacement_161):
    feature = _clean(mc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_161'] = {'inputs': ['mc_replacement_161'], 'func': mc_replacement_d2_161}


def mc_replacement_d2_162(mc_replacement_162):
    feature = _clean(mc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_162'] = {'inputs': ['mc_replacement_162'], 'func': mc_replacement_d2_162}


def mc_replacement_d2_163(mc_replacement_163):
    feature = _clean(mc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_163'] = {'inputs': ['mc_replacement_163'], 'func': mc_replacement_d2_163}


def mc_replacement_d2_164(mc_replacement_164):
    feature = _clean(mc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_164'] = {'inputs': ['mc_replacement_164'], 'func': mc_replacement_d2_164}


def mc_replacement_d2_165(mc_replacement_165):
    feature = _clean(mc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_165'] = {'inputs': ['mc_replacement_165'], 'func': mc_replacement_d2_165}


def mc_replacement_d2_166(mc_replacement_166):
    feature = _clean(mc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
MC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['mc_replacement_d2_166'] = {'inputs': ['mc_replacement_166'], 'func': mc_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63(mgc_003_fcf_burn_to_cash_63):
    return _base_universe_d2(mgc_003_fcf_burn_to_cash_63, 1)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63'] = {'inputs': ['mgc_003_fcf_burn_to_cash_63'], 'func': mgc_base_universe_d2_001_mgc_003_fcf_burn_to_cash_63}


def mgc_base_universe_d2_002_mgc_004_debt_to_equity_84(mgc_004_debt_to_equity_84):
    return _base_universe_d2(mgc_004_debt_to_equity_84, 2)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_002_mgc_004_debt_to_equity_84'] = {'inputs': ['mgc_004_debt_to_equity_84'], 'func': mgc_base_universe_d2_002_mgc_004_debt_to_equity_84}


def mgc_base_universe_d2_003_mgc_005_debt_to_assets_126(mgc_005_debt_to_assets_126):
    return _base_universe_d2(mgc_005_debt_to_assets_126, 3)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_003_mgc_005_debt_to_assets_126'] = {'inputs': ['mgc_005_debt_to_assets_126'], 'func': mgc_base_universe_d2_003_mgc_005_debt_to_assets_126}


def mgc_base_universe_d2_004_mgc_012_accrual_gap_1260(mgc_012_accrual_gap_1260):
    return _base_universe_d2(mgc_012_accrual_gap_1260, 4)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_004_mgc_012_accrual_gap_1260'] = {'inputs': ['mgc_012_accrual_gap_1260'], 'func': mgc_base_universe_d2_004_mgc_012_accrual_gap_1260}


def mgc_base_universe_d2_005_mgc_016_debt_to_equity_21(mgc_016_debt_to_equity_21):
    return _base_universe_d2(mgc_016_debt_to_equity_21, 5)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_005_mgc_016_debt_to_equity_21'] = {'inputs': ['mgc_016_debt_to_equity_21'], 'func': mgc_base_universe_d2_005_mgc_016_debt_to_equity_21}


def mgc_base_universe_d2_006_mgc_017_debt_to_assets_42(mgc_017_debt_to_assets_42):
    return _base_universe_d2(mgc_017_debt_to_assets_42, 6)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_006_mgc_017_debt_to_assets_42'] = {'inputs': ['mgc_017_debt_to_assets_42'], 'func': mgc_base_universe_d2_006_mgc_017_debt_to_assets_42}


def mgc_base_universe_d2_007_mgc_024_accrual_gap_504(mgc_024_accrual_gap_504):
    return _base_universe_d2(mgc_024_accrual_gap_504, 7)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_007_mgc_024_accrual_gap_504'] = {'inputs': ['mgc_024_accrual_gap_504'], 'func': mgc_base_universe_d2_007_mgc_024_accrual_gap_504}


def mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260(mgc_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(mgc_027_fcf_burn_to_cash_1260, 8)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260'] = {'inputs': ['mgc_027_fcf_burn_to_cash_1260'], 'func': mgc_base_universe_d2_008_mgc_027_fcf_burn_to_cash_1260}


def mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512(mgc_028_debt_to_equity_1512):
    return _base_universe_d2(mgc_028_debt_to_equity_1512, 9)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512'] = {'inputs': ['mgc_028_debt_to_equity_1512'], 'func': mgc_base_universe_d2_009_mgc_028_debt_to_equity_1512}


def mgc_base_universe_d2_010_mgc_029_debt_to_assets_63(mgc_029_debt_to_assets_63):
    return _base_universe_d2(mgc_029_debt_to_assets_63, 10)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_010_mgc_029_debt_to_assets_63'] = {'inputs': ['mgc_029_debt_to_assets_63'], 'func': mgc_base_universe_d2_010_mgc_029_debt_to_assets_63}


def mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21(mgc_031_interest_coverage_stress_21):
    return _base_universe_d2(mgc_031_interest_coverage_stress_21, 11)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21'] = {'inputs': ['mgc_031_interest_coverage_stress_21'], 'func': mgc_base_universe_d2_011_mgc_031_interest_coverage_stress_21}


def mgc_base_universe_d2_012_mgc_036_accrual_gap_189(mgc_036_accrual_gap_189):
    return _base_universe_d2(mgc_036_accrual_gap_189, 12)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_012_mgc_036_accrual_gap_189'] = {'inputs': ['mgc_036_accrual_gap_189'], 'func': mgc_base_universe_d2_012_mgc_036_accrual_gap_189}


def mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504(mgc_039_fcf_burn_to_cash_504):
    return _base_universe_d2(mgc_039_fcf_burn_to_cash_504, 13)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504'] = {'inputs': ['mgc_039_fcf_burn_to_cash_504'], 'func': mgc_base_universe_d2_013_mgc_039_fcf_burn_to_cash_504}


def mgc_base_universe_d2_014_mgc_040_debt_to_equity_756(mgc_040_debt_to_equity_756):
    return _base_universe_d2(mgc_040_debt_to_equity_756, 14)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_014_mgc_040_debt_to_equity_756'] = {'inputs': ['mgc_040_debt_to_equity_756'], 'func': mgc_base_universe_d2_014_mgc_040_debt_to_equity_756}


def mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008(mgc_041_debt_to_assets_1008):
    return _base_universe_d2(mgc_041_debt_to_assets_1008, 15)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008'] = {'inputs': ['mgc_041_debt_to_assets_1008'], 'func': mgc_base_universe_d2_015_mgc_041_debt_to_assets_1008}


def mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512(mgc_043_interest_coverage_stress_1512):
    return _base_universe_d2(mgc_043_interest_coverage_stress_1512, 16)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512'] = {'inputs': ['mgc_043_interest_coverage_stress_1512'], 'func': mgc_base_universe_d2_016_mgc_043_interest_coverage_stress_1512}


def mgc_base_universe_d2_017_mgc_048_accrual_gap_63(mgc_048_accrual_gap_63):
    return _base_universe_d2(mgc_048_accrual_gap_63, 17)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_017_mgc_048_accrual_gap_63'] = {'inputs': ['mgc_048_accrual_gap_63'], 'func': mgc_base_universe_d2_017_mgc_048_accrual_gap_63}


def mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189(mgc_051_fcf_burn_to_cash_189):
    return _base_universe_d2(mgc_051_fcf_burn_to_cash_189, 18)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189'] = {'inputs': ['mgc_051_fcf_burn_to_cash_189'], 'func': mgc_base_universe_d2_018_mgc_051_fcf_burn_to_cash_189}


def mgc_base_universe_d2_019_mgc_052_debt_to_equity_252(mgc_052_debt_to_equity_252):
    return _base_universe_d2(mgc_052_debt_to_equity_252, 19)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_019_mgc_052_debt_to_equity_252'] = {'inputs': ['mgc_052_debt_to_equity_252'], 'func': mgc_base_universe_d2_019_mgc_052_debt_to_equity_252}


def mgc_base_universe_d2_020_mgc_053_debt_to_assets_378(mgc_053_debt_to_assets_378):
    return _base_universe_d2(mgc_053_debt_to_assets_378, 20)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_020_mgc_053_debt_to_assets_378'] = {'inputs': ['mgc_053_debt_to_assets_378'], 'func': mgc_base_universe_d2_020_mgc_053_debt_to_assets_378}


def mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756(mgc_055_interest_coverage_stress_756):
    return _base_universe_d2(mgc_055_interest_coverage_stress_756, 21)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756'] = {'inputs': ['mgc_055_interest_coverage_stress_756'], 'func': mgc_base_universe_d2_021_mgc_055_interest_coverage_stress_756}


def mgc_base_universe_d2_022_mgc_060_accrual_gap_252(mgc_060_accrual_gap_252):
    return _base_universe_d2(mgc_060_accrual_gap_252, 22)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_022_mgc_060_accrual_gap_252'] = {'inputs': ['mgc_060_accrual_gap_252'], 'func': mgc_base_universe_d2_022_mgc_060_accrual_gap_252}


def mgc_base_universe_d2_023_mgc_basefill_001(mgc_basefill_001):
    return _base_universe_d2(mgc_basefill_001, 23)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_023_mgc_basefill_001'] = {'inputs': ['mgc_basefill_001'], 'func': mgc_base_universe_d2_023_mgc_basefill_001}


def mgc_base_universe_d2_024_mgc_basefill_002(mgc_basefill_002):
    return _base_universe_d2(mgc_basefill_002, 24)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_024_mgc_basefill_002'] = {'inputs': ['mgc_basefill_002'], 'func': mgc_base_universe_d2_024_mgc_basefill_002}


def mgc_base_universe_d2_025_mgc_basefill_006(mgc_basefill_006):
    return _base_universe_d2(mgc_basefill_006, 25)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_025_mgc_basefill_006'] = {'inputs': ['mgc_basefill_006'], 'func': mgc_base_universe_d2_025_mgc_basefill_006}


def mgc_base_universe_d2_026_mgc_basefill_008(mgc_basefill_008):
    return _base_universe_d2(mgc_basefill_008, 26)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_026_mgc_basefill_008'] = {'inputs': ['mgc_basefill_008'], 'func': mgc_base_universe_d2_026_mgc_basefill_008}


def mgc_base_universe_d2_027_mgc_basefill_009(mgc_basefill_009):
    return _base_universe_d2(mgc_basefill_009, 27)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_027_mgc_basefill_009'] = {'inputs': ['mgc_basefill_009'], 'func': mgc_base_universe_d2_027_mgc_basefill_009}


def mgc_base_universe_d2_028_mgc_basefill_010(mgc_basefill_010):
    return _base_universe_d2(mgc_basefill_010, 28)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_028_mgc_basefill_010'] = {'inputs': ['mgc_basefill_010'], 'func': mgc_base_universe_d2_028_mgc_basefill_010}


def mgc_base_universe_d2_029_mgc_basefill_011(mgc_basefill_011):
    return _base_universe_d2(mgc_basefill_011, 29)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_029_mgc_basefill_011'] = {'inputs': ['mgc_basefill_011'], 'func': mgc_base_universe_d2_029_mgc_basefill_011}


def mgc_base_universe_d2_030_mgc_basefill_013(mgc_basefill_013):
    return _base_universe_d2(mgc_basefill_013, 30)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_030_mgc_basefill_013'] = {'inputs': ['mgc_basefill_013'], 'func': mgc_base_universe_d2_030_mgc_basefill_013}


def mgc_base_universe_d2_031_mgc_basefill_014(mgc_basefill_014):
    return _base_universe_d2(mgc_basefill_014, 31)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_031_mgc_basefill_014'] = {'inputs': ['mgc_basefill_014'], 'func': mgc_base_universe_d2_031_mgc_basefill_014}


def mgc_base_universe_d2_032_mgc_basefill_015(mgc_basefill_015):
    return _base_universe_d2(mgc_basefill_015, 32)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_032_mgc_basefill_015'] = {'inputs': ['mgc_basefill_015'], 'func': mgc_base_universe_d2_032_mgc_basefill_015}


def mgc_base_universe_d2_033_mgc_basefill_018(mgc_basefill_018):
    return _base_universe_d2(mgc_basefill_018, 33)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_033_mgc_basefill_018'] = {'inputs': ['mgc_basefill_018'], 'func': mgc_base_universe_d2_033_mgc_basefill_018}


def mgc_base_universe_d2_034_mgc_basefill_020(mgc_basefill_020):
    return _base_universe_d2(mgc_basefill_020, 34)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_034_mgc_basefill_020'] = {'inputs': ['mgc_basefill_020'], 'func': mgc_base_universe_d2_034_mgc_basefill_020}


def mgc_base_universe_d2_035_mgc_basefill_021(mgc_basefill_021):
    return _base_universe_d2(mgc_basefill_021, 35)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_035_mgc_basefill_021'] = {'inputs': ['mgc_basefill_021'], 'func': mgc_base_universe_d2_035_mgc_basefill_021}


def mgc_base_universe_d2_036_mgc_basefill_022(mgc_basefill_022):
    return _base_universe_d2(mgc_basefill_022, 36)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_036_mgc_basefill_022'] = {'inputs': ['mgc_basefill_022'], 'func': mgc_base_universe_d2_036_mgc_basefill_022}


def mgc_base_universe_d2_037_mgc_basefill_023(mgc_basefill_023):
    return _base_universe_d2(mgc_basefill_023, 37)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_037_mgc_basefill_023'] = {'inputs': ['mgc_basefill_023'], 'func': mgc_base_universe_d2_037_mgc_basefill_023}


def mgc_base_universe_d2_038_mgc_basefill_025(mgc_basefill_025):
    return _base_universe_d2(mgc_basefill_025, 38)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_038_mgc_basefill_025'] = {'inputs': ['mgc_basefill_025'], 'func': mgc_base_universe_d2_038_mgc_basefill_025}


def mgc_base_universe_d2_039_mgc_basefill_026(mgc_basefill_026):
    return _base_universe_d2(mgc_basefill_026, 39)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_039_mgc_basefill_026'] = {'inputs': ['mgc_basefill_026'], 'func': mgc_base_universe_d2_039_mgc_basefill_026}


def mgc_base_universe_d2_040_mgc_basefill_030(mgc_basefill_030):
    return _base_universe_d2(mgc_basefill_030, 40)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_040_mgc_basefill_030'] = {'inputs': ['mgc_basefill_030'], 'func': mgc_base_universe_d2_040_mgc_basefill_030}


def mgc_base_universe_d2_041_mgc_basefill_032(mgc_basefill_032):
    return _base_universe_d2(mgc_basefill_032, 41)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_041_mgc_basefill_032'] = {'inputs': ['mgc_basefill_032'], 'func': mgc_base_universe_d2_041_mgc_basefill_032}


def mgc_base_universe_d2_042_mgc_basefill_033(mgc_basefill_033):
    return _base_universe_d2(mgc_basefill_033, 42)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_042_mgc_basefill_033'] = {'inputs': ['mgc_basefill_033'], 'func': mgc_base_universe_d2_042_mgc_basefill_033}


def mgc_base_universe_d2_043_mgc_basefill_034(mgc_basefill_034):
    return _base_universe_d2(mgc_basefill_034, 43)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_043_mgc_basefill_034'] = {'inputs': ['mgc_basefill_034'], 'func': mgc_base_universe_d2_043_mgc_basefill_034}


def mgc_base_universe_d2_044_mgc_basefill_035(mgc_basefill_035):
    return _base_universe_d2(mgc_basefill_035, 44)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_044_mgc_basefill_035'] = {'inputs': ['mgc_basefill_035'], 'func': mgc_base_universe_d2_044_mgc_basefill_035}


def mgc_base_universe_d2_045_mgc_basefill_037(mgc_basefill_037):
    return _base_universe_d2(mgc_basefill_037, 45)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_045_mgc_basefill_037'] = {'inputs': ['mgc_basefill_037'], 'func': mgc_base_universe_d2_045_mgc_basefill_037}


def mgc_base_universe_d2_046_mgc_basefill_038(mgc_basefill_038):
    return _base_universe_d2(mgc_basefill_038, 46)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_046_mgc_basefill_038'] = {'inputs': ['mgc_basefill_038'], 'func': mgc_base_universe_d2_046_mgc_basefill_038}


def mgc_base_universe_d2_047_mgc_basefill_042(mgc_basefill_042):
    return _base_universe_d2(mgc_basefill_042, 47)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_047_mgc_basefill_042'] = {'inputs': ['mgc_basefill_042'], 'func': mgc_base_universe_d2_047_mgc_basefill_042}


def mgc_base_universe_d2_048_mgc_basefill_044(mgc_basefill_044):
    return _base_universe_d2(mgc_basefill_044, 48)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_048_mgc_basefill_044'] = {'inputs': ['mgc_basefill_044'], 'func': mgc_base_universe_d2_048_mgc_basefill_044}


def mgc_base_universe_d2_049_mgc_basefill_045(mgc_basefill_045):
    return _base_universe_d2(mgc_basefill_045, 49)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_049_mgc_basefill_045'] = {'inputs': ['mgc_basefill_045'], 'func': mgc_base_universe_d2_049_mgc_basefill_045}


def mgc_base_universe_d2_050_mgc_basefill_046(mgc_basefill_046):
    return _base_universe_d2(mgc_basefill_046, 50)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_050_mgc_basefill_046'] = {'inputs': ['mgc_basefill_046'], 'func': mgc_base_universe_d2_050_mgc_basefill_046}


def mgc_base_universe_d2_051_mgc_basefill_047(mgc_basefill_047):
    return _base_universe_d2(mgc_basefill_047, 51)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_051_mgc_basefill_047'] = {'inputs': ['mgc_basefill_047'], 'func': mgc_base_universe_d2_051_mgc_basefill_047}


def mgc_base_universe_d2_052_mgc_basefill_049(mgc_basefill_049):
    return _base_universe_d2(mgc_basefill_049, 52)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_052_mgc_basefill_049'] = {'inputs': ['mgc_basefill_049'], 'func': mgc_base_universe_d2_052_mgc_basefill_049}


def mgc_base_universe_d2_053_mgc_basefill_050(mgc_basefill_050):
    return _base_universe_d2(mgc_basefill_050, 53)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_053_mgc_basefill_050'] = {'inputs': ['mgc_basefill_050'], 'func': mgc_base_universe_d2_053_mgc_basefill_050}


def mgc_base_universe_d2_054_mgc_basefill_054(mgc_basefill_054):
    return _base_universe_d2(mgc_basefill_054, 54)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_054_mgc_basefill_054'] = {'inputs': ['mgc_basefill_054'], 'func': mgc_base_universe_d2_054_mgc_basefill_054}


def mgc_base_universe_d2_055_mgc_basefill_056(mgc_basefill_056):
    return _base_universe_d2(mgc_basefill_056, 55)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_055_mgc_basefill_056'] = {'inputs': ['mgc_basefill_056'], 'func': mgc_base_universe_d2_055_mgc_basefill_056}


def mgc_base_universe_d2_056_mgc_basefill_057(mgc_basefill_057):
    return _base_universe_d2(mgc_basefill_057, 56)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_056_mgc_basefill_057'] = {'inputs': ['mgc_basefill_057'], 'func': mgc_base_universe_d2_056_mgc_basefill_057}


def mgc_base_universe_d2_057_mgc_basefill_058(mgc_basefill_058):
    return _base_universe_d2(mgc_basefill_058, 57)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_057_mgc_basefill_058'] = {'inputs': ['mgc_basefill_058'], 'func': mgc_base_universe_d2_057_mgc_basefill_058}


def mgc_base_universe_d2_058_mgc_basefill_059(mgc_basefill_059):
    return _base_universe_d2(mgc_basefill_059, 58)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_058_mgc_basefill_059'] = {'inputs': ['mgc_basefill_059'], 'func': mgc_base_universe_d2_058_mgc_basefill_059}


def mgc_base_universe_d2_059_mgc_basefill_061(mgc_basefill_061):
    return _base_universe_d2(mgc_basefill_061, 59)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_059_mgc_basefill_061'] = {'inputs': ['mgc_basefill_061'], 'func': mgc_base_universe_d2_059_mgc_basefill_061}


def mgc_base_universe_d2_060_mgc_basefill_062(mgc_basefill_062):
    return _base_universe_d2(mgc_basefill_062, 60)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_060_mgc_basefill_062'] = {'inputs': ['mgc_basefill_062'], 'func': mgc_base_universe_d2_060_mgc_basefill_062}


def mgc_base_universe_d2_061_mgc_basefill_063(mgc_basefill_063):
    return _base_universe_d2(mgc_basefill_063, 61)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_061_mgc_basefill_063'] = {'inputs': ['mgc_basefill_063'], 'func': mgc_base_universe_d2_061_mgc_basefill_063}


def mgc_base_universe_d2_062_mgc_basefill_064(mgc_basefill_064):
    return _base_universe_d2(mgc_basefill_064, 62)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_062_mgc_basefill_064'] = {'inputs': ['mgc_basefill_064'], 'func': mgc_base_universe_d2_062_mgc_basefill_064}


def mgc_base_universe_d2_063_mgc_basefill_065(mgc_basefill_065):
    return _base_universe_d2(mgc_basefill_065, 63)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_063_mgc_basefill_065'] = {'inputs': ['mgc_basefill_065'], 'func': mgc_base_universe_d2_063_mgc_basefill_065}


def mgc_base_universe_d2_064_mgc_basefill_066(mgc_basefill_066):
    return _base_universe_d2(mgc_basefill_066, 64)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_064_mgc_basefill_066'] = {'inputs': ['mgc_basefill_066'], 'func': mgc_base_universe_d2_064_mgc_basefill_066}


def mgc_base_universe_d2_065_mgc_basefill_067(mgc_basefill_067):
    return _base_universe_d2(mgc_basefill_067, 65)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_065_mgc_basefill_067'] = {'inputs': ['mgc_basefill_067'], 'func': mgc_base_universe_d2_065_mgc_basefill_067}


def mgc_base_universe_d2_066_mgc_basefill_068(mgc_basefill_068):
    return _base_universe_d2(mgc_basefill_068, 66)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_066_mgc_basefill_068'] = {'inputs': ['mgc_basefill_068'], 'func': mgc_base_universe_d2_066_mgc_basefill_068}


def mgc_base_universe_d2_067_mgc_basefill_069(mgc_basefill_069):
    return _base_universe_d2(mgc_basefill_069, 67)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_067_mgc_basefill_069'] = {'inputs': ['mgc_basefill_069'], 'func': mgc_base_universe_d2_067_mgc_basefill_069}


def mgc_base_universe_d2_068_mgc_basefill_070(mgc_basefill_070):
    return _base_universe_d2(mgc_basefill_070, 68)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_068_mgc_basefill_070'] = {'inputs': ['mgc_basefill_070'], 'func': mgc_base_universe_d2_068_mgc_basefill_070}


def mgc_base_universe_d2_069_mgc_basefill_071(mgc_basefill_071):
    return _base_universe_d2(mgc_basefill_071, 69)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_069_mgc_basefill_071'] = {'inputs': ['mgc_basefill_071'], 'func': mgc_base_universe_d2_069_mgc_basefill_071}


def mgc_base_universe_d2_070_mgc_basefill_072(mgc_basefill_072):
    return _base_universe_d2(mgc_basefill_072, 70)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_070_mgc_basefill_072'] = {'inputs': ['mgc_basefill_072'], 'func': mgc_base_universe_d2_070_mgc_basefill_072}


def mgc_base_universe_d2_071_mgc_basefill_073(mgc_basefill_073):
    return _base_universe_d2(mgc_basefill_073, 71)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_071_mgc_basefill_073'] = {'inputs': ['mgc_basefill_073'], 'func': mgc_base_universe_d2_071_mgc_basefill_073}


def mgc_base_universe_d2_072_mgc_basefill_074(mgc_basefill_074):
    return _base_universe_d2(mgc_basefill_074, 72)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_072_mgc_basefill_074'] = {'inputs': ['mgc_basefill_074'], 'func': mgc_base_universe_d2_072_mgc_basefill_074}


def mgc_base_universe_d2_073_mgc_basefill_075(mgc_basefill_075):
    return _base_universe_d2(mgc_basefill_075, 73)
MGC_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['mgc_base_universe_d2_073_mgc_basefill_075'] = {'inputs': ['mgc_basefill_075'], 'func': mgc_base_universe_d2_073_mgc_basefill_075}
