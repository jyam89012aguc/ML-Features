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



def gds_151_gds_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def gds_152_gds_007_interest_coverage_stress_252_roc_42(gds_007_interest_coverage_stress_252):
    feature = _s(gds_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def gds_153_gds_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def gds_154_gds_019_interest_coverage_stress_84_roc_378(gds_019_interest_coverage_stress_84):
    feature = _s(gds_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def gds_155_gds_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















GUIDANCE_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    'gds_151_gds_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': gds_151_gds_001_netinc_decline_1_roc_1},
    'gds_152_gds_007_interest_coverage_stress_252_roc_42': {'inputs': ['gds_007_interest_coverage_stress_252'], 'func': gds_152_gds_007_interest_coverage_stress_252_roc_42},
    'gds_153_gds_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': gds_153_gds_013_netinc_decline_1_roc_126},
    'gds_154_gds_019_interest_coverage_stress_84_roc_378': {'inputs': ['gds_019_interest_coverage_stress_84'], 'func': gds_154_gds_019_interest_coverage_stress_84_roc_378},
    'gds_155_gds_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': gds_155_gds_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def gd_replacement_d2_001(gd_replacement_001):
    feature = _clean(gd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_001'] = {'inputs': ['gd_replacement_001'], 'func': gd_replacement_d2_001}


def gd_replacement_d2_002(gd_replacement_002):
    feature = _clean(gd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_002'] = {'inputs': ['gd_replacement_002'], 'func': gd_replacement_d2_002}


def gd_replacement_d2_003(gd_replacement_003):
    feature = _clean(gd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_003'] = {'inputs': ['gd_replacement_003'], 'func': gd_replacement_d2_003}


def gd_replacement_d2_004(gd_replacement_004):
    feature = _clean(gd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_004'] = {'inputs': ['gd_replacement_004'], 'func': gd_replacement_d2_004}


def gd_replacement_d2_005(gd_replacement_005):
    feature = _clean(gd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_005'] = {'inputs': ['gd_replacement_005'], 'func': gd_replacement_d2_005}


def gd_replacement_d2_006(gd_replacement_006):
    feature = _clean(gd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_006'] = {'inputs': ['gd_replacement_006'], 'func': gd_replacement_d2_006}


def gd_replacement_d2_007(gd_replacement_007):
    feature = _clean(gd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_007'] = {'inputs': ['gd_replacement_007'], 'func': gd_replacement_d2_007}


def gd_replacement_d2_008(gd_replacement_008):
    feature = _clean(gd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_008'] = {'inputs': ['gd_replacement_008'], 'func': gd_replacement_d2_008}


def gd_replacement_d2_009(gd_replacement_009):
    feature = _clean(gd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_009'] = {'inputs': ['gd_replacement_009'], 'func': gd_replacement_d2_009}


def gd_replacement_d2_010(gd_replacement_010):
    feature = _clean(gd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_010'] = {'inputs': ['gd_replacement_010'], 'func': gd_replacement_d2_010}


def gd_replacement_d2_011(gd_replacement_011):
    feature = _clean(gd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_011'] = {'inputs': ['gd_replacement_011'], 'func': gd_replacement_d2_011}


def gd_replacement_d2_012(gd_replacement_012):
    feature = _clean(gd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_012'] = {'inputs': ['gd_replacement_012'], 'func': gd_replacement_d2_012}


def gd_replacement_d2_013(gd_replacement_013):
    feature = _clean(gd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_013'] = {'inputs': ['gd_replacement_013'], 'func': gd_replacement_d2_013}


def gd_replacement_d2_014(gd_replacement_014):
    feature = _clean(gd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_014'] = {'inputs': ['gd_replacement_014'], 'func': gd_replacement_d2_014}


def gd_replacement_d2_015(gd_replacement_015):
    feature = _clean(gd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_015'] = {'inputs': ['gd_replacement_015'], 'func': gd_replacement_d2_015}


def gd_replacement_d2_016(gd_replacement_016):
    feature = _clean(gd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_016'] = {'inputs': ['gd_replacement_016'], 'func': gd_replacement_d2_016}


def gd_replacement_d2_017(gd_replacement_017):
    feature = _clean(gd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_017'] = {'inputs': ['gd_replacement_017'], 'func': gd_replacement_d2_017}


def gd_replacement_d2_018(gd_replacement_018):
    feature = _clean(gd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_018'] = {'inputs': ['gd_replacement_018'], 'func': gd_replacement_d2_018}


def gd_replacement_d2_019(gd_replacement_019):
    feature = _clean(gd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_019'] = {'inputs': ['gd_replacement_019'], 'func': gd_replacement_d2_019}


def gd_replacement_d2_020(gd_replacement_020):
    feature = _clean(gd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_020'] = {'inputs': ['gd_replacement_020'], 'func': gd_replacement_d2_020}


def gd_replacement_d2_021(gd_replacement_021):
    feature = _clean(gd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_021'] = {'inputs': ['gd_replacement_021'], 'func': gd_replacement_d2_021}


def gd_replacement_d2_022(gd_replacement_022):
    feature = _clean(gd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_022'] = {'inputs': ['gd_replacement_022'], 'func': gd_replacement_d2_022}


def gd_replacement_d2_023(gd_replacement_023):
    feature = _clean(gd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_023'] = {'inputs': ['gd_replacement_023'], 'func': gd_replacement_d2_023}


def gd_replacement_d2_024(gd_replacement_024):
    feature = _clean(gd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_024'] = {'inputs': ['gd_replacement_024'], 'func': gd_replacement_d2_024}


def gd_replacement_d2_025(gd_replacement_025):
    feature = _clean(gd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_025'] = {'inputs': ['gd_replacement_025'], 'func': gd_replacement_d2_025}


def gd_replacement_d2_026(gd_replacement_026):
    feature = _clean(gd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_026'] = {'inputs': ['gd_replacement_026'], 'func': gd_replacement_d2_026}


def gd_replacement_d2_027(gd_replacement_027):
    feature = _clean(gd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_027'] = {'inputs': ['gd_replacement_027'], 'func': gd_replacement_d2_027}


def gd_replacement_d2_028(gd_replacement_028):
    feature = _clean(gd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_028'] = {'inputs': ['gd_replacement_028'], 'func': gd_replacement_d2_028}


def gd_replacement_d2_029(gd_replacement_029):
    feature = _clean(gd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_029'] = {'inputs': ['gd_replacement_029'], 'func': gd_replacement_d2_029}


def gd_replacement_d2_030(gd_replacement_030):
    feature = _clean(gd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_030'] = {'inputs': ['gd_replacement_030'], 'func': gd_replacement_d2_030}


def gd_replacement_d2_031(gd_replacement_031):
    feature = _clean(gd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_031'] = {'inputs': ['gd_replacement_031'], 'func': gd_replacement_d2_031}


def gd_replacement_d2_032(gd_replacement_032):
    feature = _clean(gd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_032'] = {'inputs': ['gd_replacement_032'], 'func': gd_replacement_d2_032}


def gd_replacement_d2_033(gd_replacement_033):
    feature = _clean(gd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_033'] = {'inputs': ['gd_replacement_033'], 'func': gd_replacement_d2_033}


def gd_replacement_d2_034(gd_replacement_034):
    feature = _clean(gd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_034'] = {'inputs': ['gd_replacement_034'], 'func': gd_replacement_d2_034}


def gd_replacement_d2_035(gd_replacement_035):
    feature = _clean(gd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_035'] = {'inputs': ['gd_replacement_035'], 'func': gd_replacement_d2_035}


def gd_replacement_d2_036(gd_replacement_036):
    feature = _clean(gd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_036'] = {'inputs': ['gd_replacement_036'], 'func': gd_replacement_d2_036}


def gd_replacement_d2_037(gd_replacement_037):
    feature = _clean(gd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_037'] = {'inputs': ['gd_replacement_037'], 'func': gd_replacement_d2_037}


def gd_replacement_d2_038(gd_replacement_038):
    feature = _clean(gd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_038'] = {'inputs': ['gd_replacement_038'], 'func': gd_replacement_d2_038}


def gd_replacement_d2_039(gd_replacement_039):
    feature = _clean(gd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_039'] = {'inputs': ['gd_replacement_039'], 'func': gd_replacement_d2_039}


def gd_replacement_d2_040(gd_replacement_040):
    feature = _clean(gd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_040'] = {'inputs': ['gd_replacement_040'], 'func': gd_replacement_d2_040}


def gd_replacement_d2_041(gd_replacement_041):
    feature = _clean(gd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_041'] = {'inputs': ['gd_replacement_041'], 'func': gd_replacement_d2_041}


def gd_replacement_d2_042(gd_replacement_042):
    feature = _clean(gd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_042'] = {'inputs': ['gd_replacement_042'], 'func': gd_replacement_d2_042}


def gd_replacement_d2_043(gd_replacement_043):
    feature = _clean(gd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_043'] = {'inputs': ['gd_replacement_043'], 'func': gd_replacement_d2_043}


def gd_replacement_d2_044(gd_replacement_044):
    feature = _clean(gd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_044'] = {'inputs': ['gd_replacement_044'], 'func': gd_replacement_d2_044}


def gd_replacement_d2_045(gd_replacement_045):
    feature = _clean(gd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_045'] = {'inputs': ['gd_replacement_045'], 'func': gd_replacement_d2_045}


def gd_replacement_d2_046(gd_replacement_046):
    feature = _clean(gd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_046'] = {'inputs': ['gd_replacement_046'], 'func': gd_replacement_d2_046}


def gd_replacement_d2_047(gd_replacement_047):
    feature = _clean(gd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_047'] = {'inputs': ['gd_replacement_047'], 'func': gd_replacement_d2_047}


def gd_replacement_d2_048(gd_replacement_048):
    feature = _clean(gd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_048'] = {'inputs': ['gd_replacement_048'], 'func': gd_replacement_d2_048}


def gd_replacement_d2_049(gd_replacement_049):
    feature = _clean(gd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_049'] = {'inputs': ['gd_replacement_049'], 'func': gd_replacement_d2_049}


def gd_replacement_d2_050(gd_replacement_050):
    feature = _clean(gd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_050'] = {'inputs': ['gd_replacement_050'], 'func': gd_replacement_d2_050}


def gd_replacement_d2_051(gd_replacement_051):
    feature = _clean(gd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_051'] = {'inputs': ['gd_replacement_051'], 'func': gd_replacement_d2_051}


def gd_replacement_d2_052(gd_replacement_052):
    feature = _clean(gd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_052'] = {'inputs': ['gd_replacement_052'], 'func': gd_replacement_d2_052}


def gd_replacement_d2_053(gd_replacement_053):
    feature = _clean(gd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_053'] = {'inputs': ['gd_replacement_053'], 'func': gd_replacement_d2_053}


def gd_replacement_d2_054(gd_replacement_054):
    feature = _clean(gd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_054'] = {'inputs': ['gd_replacement_054'], 'func': gd_replacement_d2_054}


def gd_replacement_d2_055(gd_replacement_055):
    feature = _clean(gd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_055'] = {'inputs': ['gd_replacement_055'], 'func': gd_replacement_d2_055}


def gd_replacement_d2_056(gd_replacement_056):
    feature = _clean(gd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_056'] = {'inputs': ['gd_replacement_056'], 'func': gd_replacement_d2_056}


def gd_replacement_d2_057(gd_replacement_057):
    feature = _clean(gd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_057'] = {'inputs': ['gd_replacement_057'], 'func': gd_replacement_d2_057}


def gd_replacement_d2_058(gd_replacement_058):
    feature = _clean(gd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_058'] = {'inputs': ['gd_replacement_058'], 'func': gd_replacement_d2_058}


def gd_replacement_d2_059(gd_replacement_059):
    feature = _clean(gd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_059'] = {'inputs': ['gd_replacement_059'], 'func': gd_replacement_d2_059}


def gd_replacement_d2_060(gd_replacement_060):
    feature = _clean(gd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_060'] = {'inputs': ['gd_replacement_060'], 'func': gd_replacement_d2_060}


def gd_replacement_d2_061(gd_replacement_061):
    feature = _clean(gd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_061'] = {'inputs': ['gd_replacement_061'], 'func': gd_replacement_d2_061}


def gd_replacement_d2_062(gd_replacement_062):
    feature = _clean(gd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_062'] = {'inputs': ['gd_replacement_062'], 'func': gd_replacement_d2_062}


def gd_replacement_d2_063(gd_replacement_063):
    feature = _clean(gd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_063'] = {'inputs': ['gd_replacement_063'], 'func': gd_replacement_d2_063}


def gd_replacement_d2_064(gd_replacement_064):
    feature = _clean(gd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_064'] = {'inputs': ['gd_replacement_064'], 'func': gd_replacement_d2_064}


def gd_replacement_d2_065(gd_replacement_065):
    feature = _clean(gd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_065'] = {'inputs': ['gd_replacement_065'], 'func': gd_replacement_d2_065}


def gd_replacement_d2_066(gd_replacement_066):
    feature = _clean(gd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_066'] = {'inputs': ['gd_replacement_066'], 'func': gd_replacement_d2_066}


def gd_replacement_d2_067(gd_replacement_067):
    feature = _clean(gd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_067'] = {'inputs': ['gd_replacement_067'], 'func': gd_replacement_d2_067}


def gd_replacement_d2_068(gd_replacement_068):
    feature = _clean(gd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_068'] = {'inputs': ['gd_replacement_068'], 'func': gd_replacement_d2_068}


def gd_replacement_d2_069(gd_replacement_069):
    feature = _clean(gd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_069'] = {'inputs': ['gd_replacement_069'], 'func': gd_replacement_d2_069}


def gd_replacement_d2_070(gd_replacement_070):
    feature = _clean(gd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_070'] = {'inputs': ['gd_replacement_070'], 'func': gd_replacement_d2_070}


def gd_replacement_d2_071(gd_replacement_071):
    feature = _clean(gd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_071'] = {'inputs': ['gd_replacement_071'], 'func': gd_replacement_d2_071}


def gd_replacement_d2_072(gd_replacement_072):
    feature = _clean(gd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_072'] = {'inputs': ['gd_replacement_072'], 'func': gd_replacement_d2_072}


def gd_replacement_d2_073(gd_replacement_073):
    feature = _clean(gd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_073'] = {'inputs': ['gd_replacement_073'], 'func': gd_replacement_d2_073}


def gd_replacement_d2_074(gd_replacement_074):
    feature = _clean(gd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_074'] = {'inputs': ['gd_replacement_074'], 'func': gd_replacement_d2_074}


def gd_replacement_d2_075(gd_replacement_075):
    feature = _clean(gd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_075'] = {'inputs': ['gd_replacement_075'], 'func': gd_replacement_d2_075}


def gd_replacement_d2_076(gd_replacement_076):
    feature = _clean(gd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_076'] = {'inputs': ['gd_replacement_076'], 'func': gd_replacement_d2_076}


def gd_replacement_d2_077(gd_replacement_077):
    feature = _clean(gd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_077'] = {'inputs': ['gd_replacement_077'], 'func': gd_replacement_d2_077}


def gd_replacement_d2_078(gd_replacement_078):
    feature = _clean(gd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_078'] = {'inputs': ['gd_replacement_078'], 'func': gd_replacement_d2_078}


def gd_replacement_d2_079(gd_replacement_079):
    feature = _clean(gd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_079'] = {'inputs': ['gd_replacement_079'], 'func': gd_replacement_d2_079}


def gd_replacement_d2_080(gd_replacement_080):
    feature = _clean(gd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_080'] = {'inputs': ['gd_replacement_080'], 'func': gd_replacement_d2_080}


def gd_replacement_d2_081(gd_replacement_081):
    feature = _clean(gd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_081'] = {'inputs': ['gd_replacement_081'], 'func': gd_replacement_d2_081}


def gd_replacement_d2_082(gd_replacement_082):
    feature = _clean(gd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_082'] = {'inputs': ['gd_replacement_082'], 'func': gd_replacement_d2_082}


def gd_replacement_d2_083(gd_replacement_083):
    feature = _clean(gd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_083'] = {'inputs': ['gd_replacement_083'], 'func': gd_replacement_d2_083}


def gd_replacement_d2_084(gd_replacement_084):
    feature = _clean(gd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_084'] = {'inputs': ['gd_replacement_084'], 'func': gd_replacement_d2_084}


def gd_replacement_d2_085(gd_replacement_085):
    feature = _clean(gd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_085'] = {'inputs': ['gd_replacement_085'], 'func': gd_replacement_d2_085}


def gd_replacement_d2_086(gd_replacement_086):
    feature = _clean(gd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_086'] = {'inputs': ['gd_replacement_086'], 'func': gd_replacement_d2_086}


def gd_replacement_d2_087(gd_replacement_087):
    feature = _clean(gd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_087'] = {'inputs': ['gd_replacement_087'], 'func': gd_replacement_d2_087}


def gd_replacement_d2_088(gd_replacement_088):
    feature = _clean(gd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_088'] = {'inputs': ['gd_replacement_088'], 'func': gd_replacement_d2_088}


def gd_replacement_d2_089(gd_replacement_089):
    feature = _clean(gd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_089'] = {'inputs': ['gd_replacement_089'], 'func': gd_replacement_d2_089}


def gd_replacement_d2_090(gd_replacement_090):
    feature = _clean(gd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_090'] = {'inputs': ['gd_replacement_090'], 'func': gd_replacement_d2_090}


def gd_replacement_d2_091(gd_replacement_091):
    feature = _clean(gd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_091'] = {'inputs': ['gd_replacement_091'], 'func': gd_replacement_d2_091}


def gd_replacement_d2_092(gd_replacement_092):
    feature = _clean(gd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_092'] = {'inputs': ['gd_replacement_092'], 'func': gd_replacement_d2_092}


def gd_replacement_d2_093(gd_replacement_093):
    feature = _clean(gd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_093'] = {'inputs': ['gd_replacement_093'], 'func': gd_replacement_d2_093}


def gd_replacement_d2_094(gd_replacement_094):
    feature = _clean(gd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_094'] = {'inputs': ['gd_replacement_094'], 'func': gd_replacement_d2_094}


def gd_replacement_d2_095(gd_replacement_095):
    feature = _clean(gd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_095'] = {'inputs': ['gd_replacement_095'], 'func': gd_replacement_d2_095}


def gd_replacement_d2_096(gd_replacement_096):
    feature = _clean(gd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_096'] = {'inputs': ['gd_replacement_096'], 'func': gd_replacement_d2_096}


def gd_replacement_d2_097(gd_replacement_097):
    feature = _clean(gd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_097'] = {'inputs': ['gd_replacement_097'], 'func': gd_replacement_d2_097}


def gd_replacement_d2_098(gd_replacement_098):
    feature = _clean(gd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_098'] = {'inputs': ['gd_replacement_098'], 'func': gd_replacement_d2_098}


def gd_replacement_d2_099(gd_replacement_099):
    feature = _clean(gd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_099'] = {'inputs': ['gd_replacement_099'], 'func': gd_replacement_d2_099}


def gd_replacement_d2_100(gd_replacement_100):
    feature = _clean(gd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_100'] = {'inputs': ['gd_replacement_100'], 'func': gd_replacement_d2_100}


def gd_replacement_d2_101(gd_replacement_101):
    feature = _clean(gd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_101'] = {'inputs': ['gd_replacement_101'], 'func': gd_replacement_d2_101}


def gd_replacement_d2_102(gd_replacement_102):
    feature = _clean(gd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_102'] = {'inputs': ['gd_replacement_102'], 'func': gd_replacement_d2_102}


def gd_replacement_d2_103(gd_replacement_103):
    feature = _clean(gd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_103'] = {'inputs': ['gd_replacement_103'], 'func': gd_replacement_d2_103}


def gd_replacement_d2_104(gd_replacement_104):
    feature = _clean(gd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_104'] = {'inputs': ['gd_replacement_104'], 'func': gd_replacement_d2_104}


def gd_replacement_d2_105(gd_replacement_105):
    feature = _clean(gd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_105'] = {'inputs': ['gd_replacement_105'], 'func': gd_replacement_d2_105}


def gd_replacement_d2_106(gd_replacement_106):
    feature = _clean(gd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_106'] = {'inputs': ['gd_replacement_106'], 'func': gd_replacement_d2_106}


def gd_replacement_d2_107(gd_replacement_107):
    feature = _clean(gd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_107'] = {'inputs': ['gd_replacement_107'], 'func': gd_replacement_d2_107}


def gd_replacement_d2_108(gd_replacement_108):
    feature = _clean(gd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_108'] = {'inputs': ['gd_replacement_108'], 'func': gd_replacement_d2_108}


def gd_replacement_d2_109(gd_replacement_109):
    feature = _clean(gd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_109'] = {'inputs': ['gd_replacement_109'], 'func': gd_replacement_d2_109}


def gd_replacement_d2_110(gd_replacement_110):
    feature = _clean(gd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_110'] = {'inputs': ['gd_replacement_110'], 'func': gd_replacement_d2_110}


def gd_replacement_d2_111(gd_replacement_111):
    feature = _clean(gd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_111'] = {'inputs': ['gd_replacement_111'], 'func': gd_replacement_d2_111}


def gd_replacement_d2_112(gd_replacement_112):
    feature = _clean(gd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_112'] = {'inputs': ['gd_replacement_112'], 'func': gd_replacement_d2_112}


def gd_replacement_d2_113(gd_replacement_113):
    feature = _clean(gd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_113'] = {'inputs': ['gd_replacement_113'], 'func': gd_replacement_d2_113}


def gd_replacement_d2_114(gd_replacement_114):
    feature = _clean(gd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_114'] = {'inputs': ['gd_replacement_114'], 'func': gd_replacement_d2_114}


def gd_replacement_d2_115(gd_replacement_115):
    feature = _clean(gd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_115'] = {'inputs': ['gd_replacement_115'], 'func': gd_replacement_d2_115}


def gd_replacement_d2_116(gd_replacement_116):
    feature = _clean(gd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_116'] = {'inputs': ['gd_replacement_116'], 'func': gd_replacement_d2_116}


def gd_replacement_d2_117(gd_replacement_117):
    feature = _clean(gd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_117'] = {'inputs': ['gd_replacement_117'], 'func': gd_replacement_d2_117}


def gd_replacement_d2_118(gd_replacement_118):
    feature = _clean(gd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_118'] = {'inputs': ['gd_replacement_118'], 'func': gd_replacement_d2_118}


def gd_replacement_d2_119(gd_replacement_119):
    feature = _clean(gd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_119'] = {'inputs': ['gd_replacement_119'], 'func': gd_replacement_d2_119}


def gd_replacement_d2_120(gd_replacement_120):
    feature = _clean(gd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_120'] = {'inputs': ['gd_replacement_120'], 'func': gd_replacement_d2_120}


def gd_replacement_d2_121(gd_replacement_121):
    feature = _clean(gd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_121'] = {'inputs': ['gd_replacement_121'], 'func': gd_replacement_d2_121}


def gd_replacement_d2_122(gd_replacement_122):
    feature = _clean(gd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_122'] = {'inputs': ['gd_replacement_122'], 'func': gd_replacement_d2_122}


def gd_replacement_d2_123(gd_replacement_123):
    feature = _clean(gd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_123'] = {'inputs': ['gd_replacement_123'], 'func': gd_replacement_d2_123}


def gd_replacement_d2_124(gd_replacement_124):
    feature = _clean(gd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_124'] = {'inputs': ['gd_replacement_124'], 'func': gd_replacement_d2_124}


def gd_replacement_d2_125(gd_replacement_125):
    feature = _clean(gd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_125'] = {'inputs': ['gd_replacement_125'], 'func': gd_replacement_d2_125}


def gd_replacement_d2_126(gd_replacement_126):
    feature = _clean(gd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_126'] = {'inputs': ['gd_replacement_126'], 'func': gd_replacement_d2_126}


def gd_replacement_d2_127(gd_replacement_127):
    feature = _clean(gd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_127'] = {'inputs': ['gd_replacement_127'], 'func': gd_replacement_d2_127}


def gd_replacement_d2_128(gd_replacement_128):
    feature = _clean(gd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_128'] = {'inputs': ['gd_replacement_128'], 'func': gd_replacement_d2_128}


def gd_replacement_d2_129(gd_replacement_129):
    feature = _clean(gd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_129'] = {'inputs': ['gd_replacement_129'], 'func': gd_replacement_d2_129}


def gd_replacement_d2_130(gd_replacement_130):
    feature = _clean(gd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_130'] = {'inputs': ['gd_replacement_130'], 'func': gd_replacement_d2_130}


def gd_replacement_d2_131(gd_replacement_131):
    feature = _clean(gd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_131'] = {'inputs': ['gd_replacement_131'], 'func': gd_replacement_d2_131}


def gd_replacement_d2_132(gd_replacement_132):
    feature = _clean(gd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_132'] = {'inputs': ['gd_replacement_132'], 'func': gd_replacement_d2_132}


def gd_replacement_d2_133(gd_replacement_133):
    feature = _clean(gd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_133'] = {'inputs': ['gd_replacement_133'], 'func': gd_replacement_d2_133}


def gd_replacement_d2_134(gd_replacement_134):
    feature = _clean(gd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_134'] = {'inputs': ['gd_replacement_134'], 'func': gd_replacement_d2_134}


def gd_replacement_d2_135(gd_replacement_135):
    feature = _clean(gd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_135'] = {'inputs': ['gd_replacement_135'], 'func': gd_replacement_d2_135}


def gd_replacement_d2_136(gd_replacement_136):
    feature = _clean(gd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_136'] = {'inputs': ['gd_replacement_136'], 'func': gd_replacement_d2_136}


def gd_replacement_d2_137(gd_replacement_137):
    feature = _clean(gd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_137'] = {'inputs': ['gd_replacement_137'], 'func': gd_replacement_d2_137}


def gd_replacement_d2_138(gd_replacement_138):
    feature = _clean(gd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_138'] = {'inputs': ['gd_replacement_138'], 'func': gd_replacement_d2_138}


def gd_replacement_d2_139(gd_replacement_139):
    feature = _clean(gd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_139'] = {'inputs': ['gd_replacement_139'], 'func': gd_replacement_d2_139}


def gd_replacement_d2_140(gd_replacement_140):
    feature = _clean(gd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_140'] = {'inputs': ['gd_replacement_140'], 'func': gd_replacement_d2_140}


def gd_replacement_d2_141(gd_replacement_141):
    feature = _clean(gd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_141'] = {'inputs': ['gd_replacement_141'], 'func': gd_replacement_d2_141}


def gd_replacement_d2_142(gd_replacement_142):
    feature = _clean(gd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_142'] = {'inputs': ['gd_replacement_142'], 'func': gd_replacement_d2_142}


def gd_replacement_d2_143(gd_replacement_143):
    feature = _clean(gd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_143'] = {'inputs': ['gd_replacement_143'], 'func': gd_replacement_d2_143}


def gd_replacement_d2_144(gd_replacement_144):
    feature = _clean(gd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_144'] = {'inputs': ['gd_replacement_144'], 'func': gd_replacement_d2_144}


def gd_replacement_d2_145(gd_replacement_145):
    feature = _clean(gd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_145'] = {'inputs': ['gd_replacement_145'], 'func': gd_replacement_d2_145}


def gd_replacement_d2_146(gd_replacement_146):
    feature = _clean(gd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_146'] = {'inputs': ['gd_replacement_146'], 'func': gd_replacement_d2_146}


def gd_replacement_d2_147(gd_replacement_147):
    feature = _clean(gd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_147'] = {'inputs': ['gd_replacement_147'], 'func': gd_replacement_d2_147}


def gd_replacement_d2_148(gd_replacement_148):
    feature = _clean(gd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_148'] = {'inputs': ['gd_replacement_148'], 'func': gd_replacement_d2_148}


def gd_replacement_d2_149(gd_replacement_149):
    feature = _clean(gd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_149'] = {'inputs': ['gd_replacement_149'], 'func': gd_replacement_d2_149}


def gd_replacement_d2_150(gd_replacement_150):
    feature = _clean(gd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_150'] = {'inputs': ['gd_replacement_150'], 'func': gd_replacement_d2_150}


def gd_replacement_d2_151(gd_replacement_151):
    feature = _clean(gd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_151'] = {'inputs': ['gd_replacement_151'], 'func': gd_replacement_d2_151}


def gd_replacement_d2_152(gd_replacement_152):
    feature = _clean(gd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_152'] = {'inputs': ['gd_replacement_152'], 'func': gd_replacement_d2_152}


def gd_replacement_d2_153(gd_replacement_153):
    feature = _clean(gd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_153'] = {'inputs': ['gd_replacement_153'], 'func': gd_replacement_d2_153}


def gd_replacement_d2_154(gd_replacement_154):
    feature = _clean(gd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_154'] = {'inputs': ['gd_replacement_154'], 'func': gd_replacement_d2_154}


def gd_replacement_d2_155(gd_replacement_155):
    feature = _clean(gd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_155'] = {'inputs': ['gd_replacement_155'], 'func': gd_replacement_d2_155}


def gd_replacement_d2_156(gd_replacement_156):
    feature = _clean(gd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_156'] = {'inputs': ['gd_replacement_156'], 'func': gd_replacement_d2_156}


def gd_replacement_d2_157(gd_replacement_157):
    feature = _clean(gd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_157'] = {'inputs': ['gd_replacement_157'], 'func': gd_replacement_d2_157}


def gd_replacement_d2_158(gd_replacement_158):
    feature = _clean(gd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_158'] = {'inputs': ['gd_replacement_158'], 'func': gd_replacement_d2_158}


def gd_replacement_d2_159(gd_replacement_159):
    feature = _clean(gd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_159'] = {'inputs': ['gd_replacement_159'], 'func': gd_replacement_d2_159}


def gd_replacement_d2_160(gd_replacement_160):
    feature = _clean(gd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_160'] = {'inputs': ['gd_replacement_160'], 'func': gd_replacement_d2_160}


def gd_replacement_d2_161(gd_replacement_161):
    feature = _clean(gd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_161'] = {'inputs': ['gd_replacement_161'], 'func': gd_replacement_d2_161}


def gd_replacement_d2_162(gd_replacement_162):
    feature = _clean(gd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_162'] = {'inputs': ['gd_replacement_162'], 'func': gd_replacement_d2_162}


def gd_replacement_d2_163(gd_replacement_163):
    feature = _clean(gd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_163'] = {'inputs': ['gd_replacement_163'], 'func': gd_replacement_d2_163}


def gd_replacement_d2_164(gd_replacement_164):
    feature = _clean(gd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_164'] = {'inputs': ['gd_replacement_164'], 'func': gd_replacement_d2_164}


def gd_replacement_d2_165(gd_replacement_165):
    feature = _clean(gd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_165'] = {'inputs': ['gd_replacement_165'], 'func': gd_replacement_d2_165}


def gd_replacement_d2_166(gd_replacement_166):
    feature = _clean(gd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
GD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['gd_replacement_d2_166'] = {'inputs': ['gd_replacement_166'], 'func': gd_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63(gds_003_fcf_burn_to_cash_63):
    return _base_universe_d2(gds_003_fcf_burn_to_cash_63, 1)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63'] = {'inputs': ['gds_003_fcf_burn_to_cash_63'], 'func': gds_base_universe_d2_001_gds_003_fcf_burn_to_cash_63}


def gds_base_universe_d2_002_gds_004_debt_to_equity_84(gds_004_debt_to_equity_84):
    return _base_universe_d2(gds_004_debt_to_equity_84, 2)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_002_gds_004_debt_to_equity_84'] = {'inputs': ['gds_004_debt_to_equity_84'], 'func': gds_base_universe_d2_002_gds_004_debt_to_equity_84}


def gds_base_universe_d2_003_gds_005_debt_to_assets_126(gds_005_debt_to_assets_126):
    return _base_universe_d2(gds_005_debt_to_assets_126, 3)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_003_gds_005_debt_to_assets_126'] = {'inputs': ['gds_005_debt_to_assets_126'], 'func': gds_base_universe_d2_003_gds_005_debt_to_assets_126}


def gds_base_universe_d2_004_gds_012_accrual_gap_1260(gds_012_accrual_gap_1260):
    return _base_universe_d2(gds_012_accrual_gap_1260, 4)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_004_gds_012_accrual_gap_1260'] = {'inputs': ['gds_012_accrual_gap_1260'], 'func': gds_base_universe_d2_004_gds_012_accrual_gap_1260}


def gds_base_universe_d2_005_gds_016_debt_to_equity_21(gds_016_debt_to_equity_21):
    return _base_universe_d2(gds_016_debt_to_equity_21, 5)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_005_gds_016_debt_to_equity_21'] = {'inputs': ['gds_016_debt_to_equity_21'], 'func': gds_base_universe_d2_005_gds_016_debt_to_equity_21}


def gds_base_universe_d2_006_gds_017_debt_to_assets_42(gds_017_debt_to_assets_42):
    return _base_universe_d2(gds_017_debt_to_assets_42, 6)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_006_gds_017_debt_to_assets_42'] = {'inputs': ['gds_017_debt_to_assets_42'], 'func': gds_base_universe_d2_006_gds_017_debt_to_assets_42}


def gds_base_universe_d2_007_gds_024_accrual_gap_504(gds_024_accrual_gap_504):
    return _base_universe_d2(gds_024_accrual_gap_504, 7)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_007_gds_024_accrual_gap_504'] = {'inputs': ['gds_024_accrual_gap_504'], 'func': gds_base_universe_d2_007_gds_024_accrual_gap_504}


def gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260(gds_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(gds_027_fcf_burn_to_cash_1260, 8)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260'] = {'inputs': ['gds_027_fcf_burn_to_cash_1260'], 'func': gds_base_universe_d2_008_gds_027_fcf_burn_to_cash_1260}


def gds_base_universe_d2_009_gds_028_debt_to_equity_1512(gds_028_debt_to_equity_1512):
    return _base_universe_d2(gds_028_debt_to_equity_1512, 9)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_009_gds_028_debt_to_equity_1512'] = {'inputs': ['gds_028_debt_to_equity_1512'], 'func': gds_base_universe_d2_009_gds_028_debt_to_equity_1512}


def gds_base_universe_d2_010_gds_029_debt_to_assets_63(gds_029_debt_to_assets_63):
    return _base_universe_d2(gds_029_debt_to_assets_63, 10)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_010_gds_029_debt_to_assets_63'] = {'inputs': ['gds_029_debt_to_assets_63'], 'func': gds_base_universe_d2_010_gds_029_debt_to_assets_63}


def gds_base_universe_d2_011_gds_031_interest_coverage_stress_21(gds_031_interest_coverage_stress_21):
    return _base_universe_d2(gds_031_interest_coverage_stress_21, 11)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_011_gds_031_interest_coverage_stress_21'] = {'inputs': ['gds_031_interest_coverage_stress_21'], 'func': gds_base_universe_d2_011_gds_031_interest_coverage_stress_21}


def gds_base_universe_d2_012_gds_036_accrual_gap_189(gds_036_accrual_gap_189):
    return _base_universe_d2(gds_036_accrual_gap_189, 12)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_012_gds_036_accrual_gap_189'] = {'inputs': ['gds_036_accrual_gap_189'], 'func': gds_base_universe_d2_012_gds_036_accrual_gap_189}


def gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504(gds_039_fcf_burn_to_cash_504):
    return _base_universe_d2(gds_039_fcf_burn_to_cash_504, 13)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504'] = {'inputs': ['gds_039_fcf_burn_to_cash_504'], 'func': gds_base_universe_d2_013_gds_039_fcf_burn_to_cash_504}


def gds_base_universe_d2_014_gds_040_debt_to_equity_756(gds_040_debt_to_equity_756):
    return _base_universe_d2(gds_040_debt_to_equity_756, 14)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_014_gds_040_debt_to_equity_756'] = {'inputs': ['gds_040_debt_to_equity_756'], 'func': gds_base_universe_d2_014_gds_040_debt_to_equity_756}


def gds_base_universe_d2_015_gds_041_debt_to_assets_1008(gds_041_debt_to_assets_1008):
    return _base_universe_d2(gds_041_debt_to_assets_1008, 15)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_015_gds_041_debt_to_assets_1008'] = {'inputs': ['gds_041_debt_to_assets_1008'], 'func': gds_base_universe_d2_015_gds_041_debt_to_assets_1008}


def gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512(gds_043_interest_coverage_stress_1512):
    return _base_universe_d2(gds_043_interest_coverage_stress_1512, 16)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512'] = {'inputs': ['gds_043_interest_coverage_stress_1512'], 'func': gds_base_universe_d2_016_gds_043_interest_coverage_stress_1512}


def gds_base_universe_d2_017_gds_048_accrual_gap_63(gds_048_accrual_gap_63):
    return _base_universe_d2(gds_048_accrual_gap_63, 17)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_017_gds_048_accrual_gap_63'] = {'inputs': ['gds_048_accrual_gap_63'], 'func': gds_base_universe_d2_017_gds_048_accrual_gap_63}


def gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189(gds_051_fcf_burn_to_cash_189):
    return _base_universe_d2(gds_051_fcf_burn_to_cash_189, 18)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189'] = {'inputs': ['gds_051_fcf_burn_to_cash_189'], 'func': gds_base_universe_d2_018_gds_051_fcf_burn_to_cash_189}


def gds_base_universe_d2_019_gds_052_debt_to_equity_252(gds_052_debt_to_equity_252):
    return _base_universe_d2(gds_052_debt_to_equity_252, 19)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_019_gds_052_debt_to_equity_252'] = {'inputs': ['gds_052_debt_to_equity_252'], 'func': gds_base_universe_d2_019_gds_052_debt_to_equity_252}


def gds_base_universe_d2_020_gds_053_debt_to_assets_378(gds_053_debt_to_assets_378):
    return _base_universe_d2(gds_053_debt_to_assets_378, 20)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_020_gds_053_debt_to_assets_378'] = {'inputs': ['gds_053_debt_to_assets_378'], 'func': gds_base_universe_d2_020_gds_053_debt_to_assets_378}


def gds_base_universe_d2_021_gds_055_interest_coverage_stress_756(gds_055_interest_coverage_stress_756):
    return _base_universe_d2(gds_055_interest_coverage_stress_756, 21)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_021_gds_055_interest_coverage_stress_756'] = {'inputs': ['gds_055_interest_coverage_stress_756'], 'func': gds_base_universe_d2_021_gds_055_interest_coverage_stress_756}


def gds_base_universe_d2_022_gds_060_accrual_gap_252(gds_060_accrual_gap_252):
    return _base_universe_d2(gds_060_accrual_gap_252, 22)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_022_gds_060_accrual_gap_252'] = {'inputs': ['gds_060_accrual_gap_252'], 'func': gds_base_universe_d2_022_gds_060_accrual_gap_252}


def gds_base_universe_d2_023_gds_basefill_001(gds_basefill_001):
    return _base_universe_d2(gds_basefill_001, 23)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_023_gds_basefill_001'] = {'inputs': ['gds_basefill_001'], 'func': gds_base_universe_d2_023_gds_basefill_001}


def gds_base_universe_d2_024_gds_basefill_002(gds_basefill_002):
    return _base_universe_d2(gds_basefill_002, 24)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_024_gds_basefill_002'] = {'inputs': ['gds_basefill_002'], 'func': gds_base_universe_d2_024_gds_basefill_002}


def gds_base_universe_d2_025_gds_basefill_006(gds_basefill_006):
    return _base_universe_d2(gds_basefill_006, 25)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_025_gds_basefill_006'] = {'inputs': ['gds_basefill_006'], 'func': gds_base_universe_d2_025_gds_basefill_006}


def gds_base_universe_d2_026_gds_basefill_008(gds_basefill_008):
    return _base_universe_d2(gds_basefill_008, 26)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_026_gds_basefill_008'] = {'inputs': ['gds_basefill_008'], 'func': gds_base_universe_d2_026_gds_basefill_008}


def gds_base_universe_d2_027_gds_basefill_009(gds_basefill_009):
    return _base_universe_d2(gds_basefill_009, 27)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_027_gds_basefill_009'] = {'inputs': ['gds_basefill_009'], 'func': gds_base_universe_d2_027_gds_basefill_009}


def gds_base_universe_d2_028_gds_basefill_010(gds_basefill_010):
    return _base_universe_d2(gds_basefill_010, 28)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_028_gds_basefill_010'] = {'inputs': ['gds_basefill_010'], 'func': gds_base_universe_d2_028_gds_basefill_010}


def gds_base_universe_d2_029_gds_basefill_011(gds_basefill_011):
    return _base_universe_d2(gds_basefill_011, 29)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_029_gds_basefill_011'] = {'inputs': ['gds_basefill_011'], 'func': gds_base_universe_d2_029_gds_basefill_011}


def gds_base_universe_d2_030_gds_basefill_013(gds_basefill_013):
    return _base_universe_d2(gds_basefill_013, 30)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_030_gds_basefill_013'] = {'inputs': ['gds_basefill_013'], 'func': gds_base_universe_d2_030_gds_basefill_013}


def gds_base_universe_d2_031_gds_basefill_014(gds_basefill_014):
    return _base_universe_d2(gds_basefill_014, 31)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_031_gds_basefill_014'] = {'inputs': ['gds_basefill_014'], 'func': gds_base_universe_d2_031_gds_basefill_014}


def gds_base_universe_d2_032_gds_basefill_015(gds_basefill_015):
    return _base_universe_d2(gds_basefill_015, 32)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_032_gds_basefill_015'] = {'inputs': ['gds_basefill_015'], 'func': gds_base_universe_d2_032_gds_basefill_015}


def gds_base_universe_d2_033_gds_basefill_018(gds_basefill_018):
    return _base_universe_d2(gds_basefill_018, 33)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_033_gds_basefill_018'] = {'inputs': ['gds_basefill_018'], 'func': gds_base_universe_d2_033_gds_basefill_018}


def gds_base_universe_d2_034_gds_basefill_020(gds_basefill_020):
    return _base_universe_d2(gds_basefill_020, 34)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_034_gds_basefill_020'] = {'inputs': ['gds_basefill_020'], 'func': gds_base_universe_d2_034_gds_basefill_020}


def gds_base_universe_d2_035_gds_basefill_021(gds_basefill_021):
    return _base_universe_d2(gds_basefill_021, 35)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_035_gds_basefill_021'] = {'inputs': ['gds_basefill_021'], 'func': gds_base_universe_d2_035_gds_basefill_021}


def gds_base_universe_d2_036_gds_basefill_022(gds_basefill_022):
    return _base_universe_d2(gds_basefill_022, 36)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_036_gds_basefill_022'] = {'inputs': ['gds_basefill_022'], 'func': gds_base_universe_d2_036_gds_basefill_022}


def gds_base_universe_d2_037_gds_basefill_023(gds_basefill_023):
    return _base_universe_d2(gds_basefill_023, 37)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_037_gds_basefill_023'] = {'inputs': ['gds_basefill_023'], 'func': gds_base_universe_d2_037_gds_basefill_023}


def gds_base_universe_d2_038_gds_basefill_025(gds_basefill_025):
    return _base_universe_d2(gds_basefill_025, 38)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_038_gds_basefill_025'] = {'inputs': ['gds_basefill_025'], 'func': gds_base_universe_d2_038_gds_basefill_025}


def gds_base_universe_d2_039_gds_basefill_026(gds_basefill_026):
    return _base_universe_d2(gds_basefill_026, 39)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_039_gds_basefill_026'] = {'inputs': ['gds_basefill_026'], 'func': gds_base_universe_d2_039_gds_basefill_026}


def gds_base_universe_d2_040_gds_basefill_030(gds_basefill_030):
    return _base_universe_d2(gds_basefill_030, 40)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_040_gds_basefill_030'] = {'inputs': ['gds_basefill_030'], 'func': gds_base_universe_d2_040_gds_basefill_030}


def gds_base_universe_d2_041_gds_basefill_032(gds_basefill_032):
    return _base_universe_d2(gds_basefill_032, 41)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_041_gds_basefill_032'] = {'inputs': ['gds_basefill_032'], 'func': gds_base_universe_d2_041_gds_basefill_032}


def gds_base_universe_d2_042_gds_basefill_033(gds_basefill_033):
    return _base_universe_d2(gds_basefill_033, 42)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_042_gds_basefill_033'] = {'inputs': ['gds_basefill_033'], 'func': gds_base_universe_d2_042_gds_basefill_033}


def gds_base_universe_d2_043_gds_basefill_034(gds_basefill_034):
    return _base_universe_d2(gds_basefill_034, 43)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_043_gds_basefill_034'] = {'inputs': ['gds_basefill_034'], 'func': gds_base_universe_d2_043_gds_basefill_034}


def gds_base_universe_d2_044_gds_basefill_035(gds_basefill_035):
    return _base_universe_d2(gds_basefill_035, 44)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_044_gds_basefill_035'] = {'inputs': ['gds_basefill_035'], 'func': gds_base_universe_d2_044_gds_basefill_035}


def gds_base_universe_d2_045_gds_basefill_037(gds_basefill_037):
    return _base_universe_d2(gds_basefill_037, 45)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_045_gds_basefill_037'] = {'inputs': ['gds_basefill_037'], 'func': gds_base_universe_d2_045_gds_basefill_037}


def gds_base_universe_d2_046_gds_basefill_038(gds_basefill_038):
    return _base_universe_d2(gds_basefill_038, 46)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_046_gds_basefill_038'] = {'inputs': ['gds_basefill_038'], 'func': gds_base_universe_d2_046_gds_basefill_038}


def gds_base_universe_d2_047_gds_basefill_042(gds_basefill_042):
    return _base_universe_d2(gds_basefill_042, 47)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_047_gds_basefill_042'] = {'inputs': ['gds_basefill_042'], 'func': gds_base_universe_d2_047_gds_basefill_042}


def gds_base_universe_d2_048_gds_basefill_044(gds_basefill_044):
    return _base_universe_d2(gds_basefill_044, 48)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_048_gds_basefill_044'] = {'inputs': ['gds_basefill_044'], 'func': gds_base_universe_d2_048_gds_basefill_044}


def gds_base_universe_d2_049_gds_basefill_045(gds_basefill_045):
    return _base_universe_d2(gds_basefill_045, 49)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_049_gds_basefill_045'] = {'inputs': ['gds_basefill_045'], 'func': gds_base_universe_d2_049_gds_basefill_045}


def gds_base_universe_d2_050_gds_basefill_046(gds_basefill_046):
    return _base_universe_d2(gds_basefill_046, 50)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_050_gds_basefill_046'] = {'inputs': ['gds_basefill_046'], 'func': gds_base_universe_d2_050_gds_basefill_046}


def gds_base_universe_d2_051_gds_basefill_047(gds_basefill_047):
    return _base_universe_d2(gds_basefill_047, 51)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_051_gds_basefill_047'] = {'inputs': ['gds_basefill_047'], 'func': gds_base_universe_d2_051_gds_basefill_047}


def gds_base_universe_d2_052_gds_basefill_049(gds_basefill_049):
    return _base_universe_d2(gds_basefill_049, 52)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_052_gds_basefill_049'] = {'inputs': ['gds_basefill_049'], 'func': gds_base_universe_d2_052_gds_basefill_049}


def gds_base_universe_d2_053_gds_basefill_050(gds_basefill_050):
    return _base_universe_d2(gds_basefill_050, 53)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_053_gds_basefill_050'] = {'inputs': ['gds_basefill_050'], 'func': gds_base_universe_d2_053_gds_basefill_050}


def gds_base_universe_d2_054_gds_basefill_054(gds_basefill_054):
    return _base_universe_d2(gds_basefill_054, 54)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_054_gds_basefill_054'] = {'inputs': ['gds_basefill_054'], 'func': gds_base_universe_d2_054_gds_basefill_054}


def gds_base_universe_d2_055_gds_basefill_056(gds_basefill_056):
    return _base_universe_d2(gds_basefill_056, 55)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_055_gds_basefill_056'] = {'inputs': ['gds_basefill_056'], 'func': gds_base_universe_d2_055_gds_basefill_056}


def gds_base_universe_d2_056_gds_basefill_057(gds_basefill_057):
    return _base_universe_d2(gds_basefill_057, 56)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_056_gds_basefill_057'] = {'inputs': ['gds_basefill_057'], 'func': gds_base_universe_d2_056_gds_basefill_057}


def gds_base_universe_d2_057_gds_basefill_058(gds_basefill_058):
    return _base_universe_d2(gds_basefill_058, 57)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_057_gds_basefill_058'] = {'inputs': ['gds_basefill_058'], 'func': gds_base_universe_d2_057_gds_basefill_058}


def gds_base_universe_d2_058_gds_basefill_059(gds_basefill_059):
    return _base_universe_d2(gds_basefill_059, 58)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_058_gds_basefill_059'] = {'inputs': ['gds_basefill_059'], 'func': gds_base_universe_d2_058_gds_basefill_059}


def gds_base_universe_d2_059_gds_basefill_061(gds_basefill_061):
    return _base_universe_d2(gds_basefill_061, 59)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_059_gds_basefill_061'] = {'inputs': ['gds_basefill_061'], 'func': gds_base_universe_d2_059_gds_basefill_061}


def gds_base_universe_d2_060_gds_basefill_062(gds_basefill_062):
    return _base_universe_d2(gds_basefill_062, 60)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_060_gds_basefill_062'] = {'inputs': ['gds_basefill_062'], 'func': gds_base_universe_d2_060_gds_basefill_062}


def gds_base_universe_d2_061_gds_basefill_063(gds_basefill_063):
    return _base_universe_d2(gds_basefill_063, 61)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_061_gds_basefill_063'] = {'inputs': ['gds_basefill_063'], 'func': gds_base_universe_d2_061_gds_basefill_063}


def gds_base_universe_d2_062_gds_basefill_064(gds_basefill_064):
    return _base_universe_d2(gds_basefill_064, 62)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_062_gds_basefill_064'] = {'inputs': ['gds_basefill_064'], 'func': gds_base_universe_d2_062_gds_basefill_064}


def gds_base_universe_d2_063_gds_basefill_065(gds_basefill_065):
    return _base_universe_d2(gds_basefill_065, 63)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_063_gds_basefill_065'] = {'inputs': ['gds_basefill_065'], 'func': gds_base_universe_d2_063_gds_basefill_065}


def gds_base_universe_d2_064_gds_basefill_066(gds_basefill_066):
    return _base_universe_d2(gds_basefill_066, 64)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_064_gds_basefill_066'] = {'inputs': ['gds_basefill_066'], 'func': gds_base_universe_d2_064_gds_basefill_066}


def gds_base_universe_d2_065_gds_basefill_067(gds_basefill_067):
    return _base_universe_d2(gds_basefill_067, 65)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_065_gds_basefill_067'] = {'inputs': ['gds_basefill_067'], 'func': gds_base_universe_d2_065_gds_basefill_067}


def gds_base_universe_d2_066_gds_basefill_068(gds_basefill_068):
    return _base_universe_d2(gds_basefill_068, 66)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_066_gds_basefill_068'] = {'inputs': ['gds_basefill_068'], 'func': gds_base_universe_d2_066_gds_basefill_068}


def gds_base_universe_d2_067_gds_basefill_069(gds_basefill_069):
    return _base_universe_d2(gds_basefill_069, 67)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_067_gds_basefill_069'] = {'inputs': ['gds_basefill_069'], 'func': gds_base_universe_d2_067_gds_basefill_069}


def gds_base_universe_d2_068_gds_basefill_070(gds_basefill_070):
    return _base_universe_d2(gds_basefill_070, 68)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_068_gds_basefill_070'] = {'inputs': ['gds_basefill_070'], 'func': gds_base_universe_d2_068_gds_basefill_070}


def gds_base_universe_d2_069_gds_basefill_071(gds_basefill_071):
    return _base_universe_d2(gds_basefill_071, 69)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_069_gds_basefill_071'] = {'inputs': ['gds_basefill_071'], 'func': gds_base_universe_d2_069_gds_basefill_071}


def gds_base_universe_d2_070_gds_basefill_072(gds_basefill_072):
    return _base_universe_d2(gds_basefill_072, 70)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_070_gds_basefill_072'] = {'inputs': ['gds_basefill_072'], 'func': gds_base_universe_d2_070_gds_basefill_072}


def gds_base_universe_d2_071_gds_basefill_073(gds_basefill_073):
    return _base_universe_d2(gds_basefill_073, 71)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_071_gds_basefill_073'] = {'inputs': ['gds_basefill_073'], 'func': gds_base_universe_d2_071_gds_basefill_073}


def gds_base_universe_d2_072_gds_basefill_074(gds_basefill_074):
    return _base_universe_d2(gds_basefill_074, 72)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_072_gds_basefill_074'] = {'inputs': ['gds_basefill_074'], 'func': gds_base_universe_d2_072_gds_basefill_074}


def gds_base_universe_d2_073_gds_basefill_075(gds_basefill_075):
    return _base_universe_d2(gds_basefill_075, 73)
GDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['gds_base_universe_d2_073_gds_basefill_075'] = {'inputs': ['gds_basefill_075'], 'func': gds_base_universe_d2_073_gds_basefill_075}
