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



def ocn_151_ocn_001_holder_exit_1_roc_1(ocn_001_holder_exit_1):
    feature = _s(ocn_001_holder_exit_1)
    return (_roc(feature, 1)).reindex(feature.index)

def ocn_152_ocn_007_holder_exit_1_roc_42(ocn_007_holder_exit_1):
    feature = _s(ocn_007_holder_exit_1)
    return (_roc(feature, 42)).reindex(feature.index)

def ocn_153_ocn_013_holder_exit_1_roc_126(ocn_013_holder_exit_1):
    feature = _s(ocn_013_holder_exit_1)
    return (_roc(feature, 126)).reindex(feature.index)

def ocn_154_ocn_019_holder_exit_1_roc_378(ocn_019_holder_exit_1):
    feature = _s(ocn_019_holder_exit_1)
    return (_roc(feature, 378)).reindex(feature.index)

def ocn_155_ocn_025_holder_exit_1_roc_4(ocn_025_holder_exit_1):
    feature = _s(ocn_025_holder_exit_1)
    return (_roc(feature, 4)).reindex(feature.index)






















OWNERSHIP_CONCENTRATION_REGISTRY_2ND_DERIVATIVES = {
    'ocn_151_ocn_001_holder_exit_1_roc_1': {'inputs': ['ocn_001_holder_exit_1'], 'func': ocn_151_ocn_001_holder_exit_1_roc_1},
    'ocn_152_ocn_007_holder_exit_1_roc_42': {'inputs': ['ocn_007_holder_exit_1'], 'func': ocn_152_ocn_007_holder_exit_1_roc_42},
    'ocn_153_ocn_013_holder_exit_1_roc_126': {'inputs': ['ocn_013_holder_exit_1'], 'func': ocn_153_ocn_013_holder_exit_1_roc_126},
    'ocn_154_ocn_019_holder_exit_1_roc_378': {'inputs': ['ocn_019_holder_exit_1'], 'func': ocn_154_ocn_019_holder_exit_1_roc_378},
    'ocn_155_ocn_025_holder_exit_1_roc_4': {'inputs': ['ocn_025_holder_exit_1'], 'func': ocn_155_ocn_025_holder_exit_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def oc_replacement_d2_001(ocn_001_holder_exit_1):
    feature = _clean(ocn_001_holder_exit_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_001'] = {'inputs': ['ocn_001_holder_exit_1'], 'func': oc_replacement_d2_001}


def oc_replacement_d2_002(ocn_007_holder_exit_1):
    feature = _clean(ocn_007_holder_exit_1)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_002'] = {'inputs': ['ocn_007_holder_exit_1'], 'func': oc_replacement_d2_002}


def oc_replacement_d2_003(ocn_013_holder_exit_1):
    feature = _clean(ocn_013_holder_exit_1)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_003'] = {'inputs': ['ocn_013_holder_exit_1'], 'func': oc_replacement_d2_003}


def oc_replacement_d2_004(ocn_019_holder_exit_1):
    feature = _clean(ocn_019_holder_exit_1)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_004'] = {'inputs': ['ocn_019_holder_exit_1'], 'func': oc_replacement_d2_004}


def oc_replacement_d2_005(ocn_025_holder_exit_1):
    feature = _clean(ocn_025_holder_exit_1)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_005'] = {'inputs': ['ocn_025_holder_exit_1'], 'func': oc_replacement_d2_005}


def oc_replacement_d2_006(oc_replacement_001):
    feature = _clean(oc_replacement_001)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_006'] = {'inputs': ['oc_replacement_001'], 'func': oc_replacement_d2_006}


def oc_replacement_d2_007(oc_replacement_002):
    feature = _clean(oc_replacement_002)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_007'] = {'inputs': ['oc_replacement_002'], 'func': oc_replacement_d2_007}


def oc_replacement_d2_008(oc_replacement_003):
    feature = _clean(oc_replacement_003)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_008'] = {'inputs': ['oc_replacement_003'], 'func': oc_replacement_d2_008}


def oc_replacement_d2_009(oc_replacement_004):
    feature = _clean(oc_replacement_004)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_009'] = {'inputs': ['oc_replacement_004'], 'func': oc_replacement_d2_009}


def oc_replacement_d2_010(oc_replacement_005):
    feature = _clean(oc_replacement_005)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_010'] = {'inputs': ['oc_replacement_005'], 'func': oc_replacement_d2_010}


def oc_replacement_d2_011(oc_replacement_006):
    feature = _clean(oc_replacement_006)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_011'] = {'inputs': ['oc_replacement_006'], 'func': oc_replacement_d2_011}


def oc_replacement_d2_012(oc_replacement_007):
    feature = _clean(oc_replacement_007)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_012'] = {'inputs': ['oc_replacement_007'], 'func': oc_replacement_d2_012}


def oc_replacement_d2_013(oc_replacement_008):
    feature = _clean(oc_replacement_008)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_013'] = {'inputs': ['oc_replacement_008'], 'func': oc_replacement_d2_013}


def oc_replacement_d2_014(oc_replacement_009):
    feature = _clean(oc_replacement_009)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_014'] = {'inputs': ['oc_replacement_009'], 'func': oc_replacement_d2_014}


def oc_replacement_d2_015(oc_replacement_010):
    feature = _clean(oc_replacement_010)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_015'] = {'inputs': ['oc_replacement_010'], 'func': oc_replacement_d2_015}


def oc_replacement_d2_016(oc_replacement_011):
    feature = _clean(oc_replacement_011)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_016'] = {'inputs': ['oc_replacement_011'], 'func': oc_replacement_d2_016}


def oc_replacement_d2_017(oc_replacement_012):
    feature = _clean(oc_replacement_012)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_017'] = {'inputs': ['oc_replacement_012'], 'func': oc_replacement_d2_017}


def oc_replacement_d2_018(oc_replacement_013):
    feature = _clean(oc_replacement_013)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_018'] = {'inputs': ['oc_replacement_013'], 'func': oc_replacement_d2_018}


def oc_replacement_d2_019(oc_replacement_014):
    feature = _clean(oc_replacement_014)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_019'] = {'inputs': ['oc_replacement_014'], 'func': oc_replacement_d2_019}


def oc_replacement_d2_020(oc_replacement_015):
    feature = _clean(oc_replacement_015)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_020'] = {'inputs': ['oc_replacement_015'], 'func': oc_replacement_d2_020}


def oc_replacement_d2_021(oc_replacement_016):
    feature = _clean(oc_replacement_016)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_021'] = {'inputs': ['oc_replacement_016'], 'func': oc_replacement_d2_021}


def oc_replacement_d2_022(oc_replacement_017):
    feature = _clean(oc_replacement_017)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_022'] = {'inputs': ['oc_replacement_017'], 'func': oc_replacement_d2_022}


def oc_replacement_d2_023(oc_replacement_018):
    feature = _clean(oc_replacement_018)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_023'] = {'inputs': ['oc_replacement_018'], 'func': oc_replacement_d2_023}


def oc_replacement_d2_024(oc_replacement_019):
    feature = _clean(oc_replacement_019)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_024'] = {'inputs': ['oc_replacement_019'], 'func': oc_replacement_d2_024}


def oc_replacement_d2_025(oc_replacement_020):
    feature = _clean(oc_replacement_020)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_025'] = {'inputs': ['oc_replacement_020'], 'func': oc_replacement_d2_025}


def oc_replacement_d2_026(oc_replacement_021):
    feature = _clean(oc_replacement_021)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_026'] = {'inputs': ['oc_replacement_021'], 'func': oc_replacement_d2_026}


def oc_replacement_d2_027(oc_replacement_022):
    feature = _clean(oc_replacement_022)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_027'] = {'inputs': ['oc_replacement_022'], 'func': oc_replacement_d2_027}


def oc_replacement_d2_028(oc_replacement_023):
    feature = _clean(oc_replacement_023)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_028'] = {'inputs': ['oc_replacement_023'], 'func': oc_replacement_d2_028}


def oc_replacement_d2_029(oc_replacement_024):
    feature = _clean(oc_replacement_024)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_029'] = {'inputs': ['oc_replacement_024'], 'func': oc_replacement_d2_029}


def oc_replacement_d2_030(oc_replacement_025):
    feature = _clean(oc_replacement_025)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_030'] = {'inputs': ['oc_replacement_025'], 'func': oc_replacement_d2_030}


def oc_replacement_d2_031(oc_replacement_026):
    feature = _clean(oc_replacement_026)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_031'] = {'inputs': ['oc_replacement_026'], 'func': oc_replacement_d2_031}


def oc_replacement_d2_032(oc_replacement_027):
    feature = _clean(oc_replacement_027)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_032'] = {'inputs': ['oc_replacement_027'], 'func': oc_replacement_d2_032}


def oc_replacement_d2_033(oc_replacement_028):
    feature = _clean(oc_replacement_028)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_033'] = {'inputs': ['oc_replacement_028'], 'func': oc_replacement_d2_033}


def oc_replacement_d2_034(oc_replacement_029):
    feature = _clean(oc_replacement_029)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_034'] = {'inputs': ['oc_replacement_029'], 'func': oc_replacement_d2_034}


def oc_replacement_d2_035(oc_replacement_030):
    feature = _clean(oc_replacement_030)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_035'] = {'inputs': ['oc_replacement_030'], 'func': oc_replacement_d2_035}


def oc_replacement_d2_036(oc_replacement_031):
    feature = _clean(oc_replacement_031)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_036'] = {'inputs': ['oc_replacement_031'], 'func': oc_replacement_d2_036}


def oc_replacement_d2_037(oc_replacement_032):
    feature = _clean(oc_replacement_032)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_037'] = {'inputs': ['oc_replacement_032'], 'func': oc_replacement_d2_037}


def oc_replacement_d2_038(oc_replacement_033):
    feature = _clean(oc_replacement_033)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_038'] = {'inputs': ['oc_replacement_033'], 'func': oc_replacement_d2_038}


def oc_replacement_d2_039(oc_replacement_034):
    feature = _clean(oc_replacement_034)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_039'] = {'inputs': ['oc_replacement_034'], 'func': oc_replacement_d2_039}


def oc_replacement_d2_040(oc_replacement_035):
    feature = _clean(oc_replacement_035)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_040'] = {'inputs': ['oc_replacement_035'], 'func': oc_replacement_d2_040}


def oc_replacement_d2_041(oc_replacement_036):
    feature = _clean(oc_replacement_036)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_041'] = {'inputs': ['oc_replacement_036'], 'func': oc_replacement_d2_041}


def oc_replacement_d2_042(oc_replacement_037):
    feature = _clean(oc_replacement_037)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_042'] = {'inputs': ['oc_replacement_037'], 'func': oc_replacement_d2_042}


def oc_replacement_d2_043(oc_replacement_038):
    feature = _clean(oc_replacement_038)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_043'] = {'inputs': ['oc_replacement_038'], 'func': oc_replacement_d2_043}


def oc_replacement_d2_044(oc_replacement_039):
    feature = _clean(oc_replacement_039)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_044'] = {'inputs': ['oc_replacement_039'], 'func': oc_replacement_d2_044}


def oc_replacement_d2_045(oc_replacement_040):
    feature = _clean(oc_replacement_040)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_045'] = {'inputs': ['oc_replacement_040'], 'func': oc_replacement_d2_045}


def oc_replacement_d2_046(oc_replacement_041):
    feature = _clean(oc_replacement_041)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_046'] = {'inputs': ['oc_replacement_041'], 'func': oc_replacement_d2_046}


def oc_replacement_d2_047(oc_replacement_042):
    feature = _clean(oc_replacement_042)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_047'] = {'inputs': ['oc_replacement_042'], 'func': oc_replacement_d2_047}


def oc_replacement_d2_048(oc_replacement_043):
    feature = _clean(oc_replacement_043)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_048'] = {'inputs': ['oc_replacement_043'], 'func': oc_replacement_d2_048}


def oc_replacement_d2_049(oc_replacement_044):
    feature = _clean(oc_replacement_044)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_049'] = {'inputs': ['oc_replacement_044'], 'func': oc_replacement_d2_049}


def oc_replacement_d2_050(oc_replacement_045):
    feature = _clean(oc_replacement_045)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_050'] = {'inputs': ['oc_replacement_045'], 'func': oc_replacement_d2_050}


def oc_replacement_d2_051(oc_replacement_046):
    feature = _clean(oc_replacement_046)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_051'] = {'inputs': ['oc_replacement_046'], 'func': oc_replacement_d2_051}


def oc_replacement_d2_052(oc_replacement_047):
    feature = _clean(oc_replacement_047)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_052'] = {'inputs': ['oc_replacement_047'], 'func': oc_replacement_d2_052}


def oc_replacement_d2_053(oc_replacement_048):
    feature = _clean(oc_replacement_048)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_053'] = {'inputs': ['oc_replacement_048'], 'func': oc_replacement_d2_053}


def oc_replacement_d2_054(oc_replacement_049):
    feature = _clean(oc_replacement_049)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_054'] = {'inputs': ['oc_replacement_049'], 'func': oc_replacement_d2_054}


def oc_replacement_d2_055(oc_replacement_050):
    feature = _clean(oc_replacement_050)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_055'] = {'inputs': ['oc_replacement_050'], 'func': oc_replacement_d2_055}


def oc_replacement_d2_056(oc_replacement_051):
    feature = _clean(oc_replacement_051)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_056'] = {'inputs': ['oc_replacement_051'], 'func': oc_replacement_d2_056}


def oc_replacement_d2_057(oc_replacement_052):
    feature = _clean(oc_replacement_052)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_057'] = {'inputs': ['oc_replacement_052'], 'func': oc_replacement_d2_057}


def oc_replacement_d2_058(oc_replacement_053):
    feature = _clean(oc_replacement_053)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_058'] = {'inputs': ['oc_replacement_053'], 'func': oc_replacement_d2_058}


def oc_replacement_d2_059(oc_replacement_054):
    feature = _clean(oc_replacement_054)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_059'] = {'inputs': ['oc_replacement_054'], 'func': oc_replacement_d2_059}


def oc_replacement_d2_060(oc_replacement_055):
    feature = _clean(oc_replacement_055)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_060'] = {'inputs': ['oc_replacement_055'], 'func': oc_replacement_d2_060}


def oc_replacement_d2_061(oc_replacement_056):
    feature = _clean(oc_replacement_056)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_061'] = {'inputs': ['oc_replacement_056'], 'func': oc_replacement_d2_061}


def oc_replacement_d2_062(oc_replacement_057):
    feature = _clean(oc_replacement_057)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_062'] = {'inputs': ['oc_replacement_057'], 'func': oc_replacement_d2_062}


def oc_replacement_d2_063(oc_replacement_058):
    feature = _clean(oc_replacement_058)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_063'] = {'inputs': ['oc_replacement_058'], 'func': oc_replacement_d2_063}


def oc_replacement_d2_064(oc_replacement_059):
    feature = _clean(oc_replacement_059)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_064'] = {'inputs': ['oc_replacement_059'], 'func': oc_replacement_d2_064}


def oc_replacement_d2_065(oc_replacement_060):
    feature = _clean(oc_replacement_060)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_065'] = {'inputs': ['oc_replacement_060'], 'func': oc_replacement_d2_065}


def oc_replacement_d2_066(oc_replacement_061):
    feature = _clean(oc_replacement_061)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_066'] = {'inputs': ['oc_replacement_061'], 'func': oc_replacement_d2_066}


def oc_replacement_d2_067(oc_replacement_062):
    feature = _clean(oc_replacement_062)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_067'] = {'inputs': ['oc_replacement_062'], 'func': oc_replacement_d2_067}


def oc_replacement_d2_068(oc_replacement_063):
    feature = _clean(oc_replacement_063)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_068'] = {'inputs': ['oc_replacement_063'], 'func': oc_replacement_d2_068}


def oc_replacement_d2_069(oc_replacement_064):
    feature = _clean(oc_replacement_064)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_069'] = {'inputs': ['oc_replacement_064'], 'func': oc_replacement_d2_069}


def oc_replacement_d2_070(oc_replacement_065):
    feature = _clean(oc_replacement_065)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_070'] = {'inputs': ['oc_replacement_065'], 'func': oc_replacement_d2_070}


def oc_replacement_d2_071(oc_replacement_066):
    feature = _clean(oc_replacement_066)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_071'] = {'inputs': ['oc_replacement_066'], 'func': oc_replacement_d2_071}


def oc_replacement_d2_072(oc_replacement_067):
    feature = _clean(oc_replacement_067)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_072'] = {'inputs': ['oc_replacement_067'], 'func': oc_replacement_d2_072}


def oc_replacement_d2_073(oc_replacement_068):
    feature = _clean(oc_replacement_068)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_073'] = {'inputs': ['oc_replacement_068'], 'func': oc_replacement_d2_073}


def oc_replacement_d2_074(oc_replacement_069):
    feature = _clean(oc_replacement_069)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_074'] = {'inputs': ['oc_replacement_069'], 'func': oc_replacement_d2_074}


def oc_replacement_d2_075(oc_replacement_070):
    feature = _clean(oc_replacement_070)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_075'] = {'inputs': ['oc_replacement_070'], 'func': oc_replacement_d2_075}


def oc_replacement_d2_076(oc_replacement_071):
    feature = _clean(oc_replacement_071)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_076'] = {'inputs': ['oc_replacement_071'], 'func': oc_replacement_d2_076}


def oc_replacement_d2_077(oc_replacement_072):
    feature = _clean(oc_replacement_072)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_077'] = {'inputs': ['oc_replacement_072'], 'func': oc_replacement_d2_077}


def oc_replacement_d2_078(oc_replacement_073):
    feature = _clean(oc_replacement_073)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_078'] = {'inputs': ['oc_replacement_073'], 'func': oc_replacement_d2_078}


def oc_replacement_d2_079(oc_replacement_074):
    feature = _clean(oc_replacement_074)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_079'] = {'inputs': ['oc_replacement_074'], 'func': oc_replacement_d2_079}


def oc_replacement_d2_080(oc_replacement_075):
    feature = _clean(oc_replacement_075)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_080'] = {'inputs': ['oc_replacement_075'], 'func': oc_replacement_d2_080}


def oc_replacement_d2_081(oc_replacement_076):
    feature = _clean(oc_replacement_076)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_081'] = {'inputs': ['oc_replacement_076'], 'func': oc_replacement_d2_081}


def oc_replacement_d2_082(oc_replacement_077):
    feature = _clean(oc_replacement_077)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_082'] = {'inputs': ['oc_replacement_077'], 'func': oc_replacement_d2_082}


def oc_replacement_d2_083(oc_replacement_078):
    feature = _clean(oc_replacement_078)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_083'] = {'inputs': ['oc_replacement_078'], 'func': oc_replacement_d2_083}


def oc_replacement_d2_084(oc_replacement_079):
    feature = _clean(oc_replacement_079)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_084'] = {'inputs': ['oc_replacement_079'], 'func': oc_replacement_d2_084}


def oc_replacement_d2_085(oc_replacement_080):
    feature = _clean(oc_replacement_080)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_085'] = {'inputs': ['oc_replacement_080'], 'func': oc_replacement_d2_085}


def oc_replacement_d2_086(oc_replacement_081):
    feature = _clean(oc_replacement_081)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_086'] = {'inputs': ['oc_replacement_081'], 'func': oc_replacement_d2_086}


def oc_replacement_d2_087(oc_replacement_082):
    feature = _clean(oc_replacement_082)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_087'] = {'inputs': ['oc_replacement_082'], 'func': oc_replacement_d2_087}


def oc_replacement_d2_088(oc_replacement_083):
    feature = _clean(oc_replacement_083)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_088'] = {'inputs': ['oc_replacement_083'], 'func': oc_replacement_d2_088}


def oc_replacement_d2_089(oc_replacement_084):
    feature = _clean(oc_replacement_084)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_089'] = {'inputs': ['oc_replacement_084'], 'func': oc_replacement_d2_089}


def oc_replacement_d2_090(oc_replacement_085):
    feature = _clean(oc_replacement_085)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_090'] = {'inputs': ['oc_replacement_085'], 'func': oc_replacement_d2_090}


def oc_replacement_d2_091(oc_replacement_086):
    feature = _clean(oc_replacement_086)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_091'] = {'inputs': ['oc_replacement_086'], 'func': oc_replacement_d2_091}


def oc_replacement_d2_092(oc_replacement_087):
    feature = _clean(oc_replacement_087)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_092'] = {'inputs': ['oc_replacement_087'], 'func': oc_replacement_d2_092}


def oc_replacement_d2_093(oc_replacement_088):
    feature = _clean(oc_replacement_088)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_093'] = {'inputs': ['oc_replacement_088'], 'func': oc_replacement_d2_093}


def oc_replacement_d2_094(oc_replacement_089):
    feature = _clean(oc_replacement_089)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_094'] = {'inputs': ['oc_replacement_089'], 'func': oc_replacement_d2_094}


def oc_replacement_d2_095(oc_replacement_090):
    feature = _clean(oc_replacement_090)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_095'] = {'inputs': ['oc_replacement_090'], 'func': oc_replacement_d2_095}


def oc_replacement_d2_096(oc_replacement_091):
    feature = _clean(oc_replacement_091)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_096'] = {'inputs': ['oc_replacement_091'], 'func': oc_replacement_d2_096}


def oc_replacement_d2_097(oc_replacement_092):
    feature = _clean(oc_replacement_092)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_097'] = {'inputs': ['oc_replacement_092'], 'func': oc_replacement_d2_097}


def oc_replacement_d2_098(oc_replacement_093):
    feature = _clean(oc_replacement_093)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_098'] = {'inputs': ['oc_replacement_093'], 'func': oc_replacement_d2_098}


def oc_replacement_d2_099(oc_replacement_094):
    feature = _clean(oc_replacement_094)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_099'] = {'inputs': ['oc_replacement_094'], 'func': oc_replacement_d2_099}


def oc_replacement_d2_100(oc_replacement_095):
    feature = _clean(oc_replacement_095)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_100'] = {'inputs': ['oc_replacement_095'], 'func': oc_replacement_d2_100}


def oc_replacement_d2_101(oc_replacement_096):
    feature = _clean(oc_replacement_096)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_101'] = {'inputs': ['oc_replacement_096'], 'func': oc_replacement_d2_101}


def oc_replacement_d2_102(oc_replacement_097):
    feature = _clean(oc_replacement_097)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_102'] = {'inputs': ['oc_replacement_097'], 'func': oc_replacement_d2_102}


def oc_replacement_d2_103(oc_replacement_098):
    feature = _clean(oc_replacement_098)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_103'] = {'inputs': ['oc_replacement_098'], 'func': oc_replacement_d2_103}


def oc_replacement_d2_104(oc_replacement_099):
    feature = _clean(oc_replacement_099)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_104'] = {'inputs': ['oc_replacement_099'], 'func': oc_replacement_d2_104}


def oc_replacement_d2_105(oc_replacement_100):
    feature = _clean(oc_replacement_100)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_105'] = {'inputs': ['oc_replacement_100'], 'func': oc_replacement_d2_105}


def oc_replacement_d2_106(oc_replacement_101):
    feature = _clean(oc_replacement_101)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_106'] = {'inputs': ['oc_replacement_101'], 'func': oc_replacement_d2_106}


def oc_replacement_d2_107(oc_replacement_102):
    feature = _clean(oc_replacement_102)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_107'] = {'inputs': ['oc_replacement_102'], 'func': oc_replacement_d2_107}


def oc_replacement_d2_108(oc_replacement_103):
    feature = _clean(oc_replacement_103)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_108'] = {'inputs': ['oc_replacement_103'], 'func': oc_replacement_d2_108}


def oc_replacement_d2_109(oc_replacement_104):
    feature = _clean(oc_replacement_104)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_109'] = {'inputs': ['oc_replacement_104'], 'func': oc_replacement_d2_109}


def oc_replacement_d2_110(oc_replacement_105):
    feature = _clean(oc_replacement_105)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_110'] = {'inputs': ['oc_replacement_105'], 'func': oc_replacement_d2_110}


def oc_replacement_d2_111(oc_replacement_106):
    feature = _clean(oc_replacement_106)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_111'] = {'inputs': ['oc_replacement_106'], 'func': oc_replacement_d2_111}


def oc_replacement_d2_112(oc_replacement_107):
    feature = _clean(oc_replacement_107)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_112'] = {'inputs': ['oc_replacement_107'], 'func': oc_replacement_d2_112}


def oc_replacement_d2_113(oc_replacement_108):
    feature = _clean(oc_replacement_108)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_113'] = {'inputs': ['oc_replacement_108'], 'func': oc_replacement_d2_113}


def oc_replacement_d2_114(oc_replacement_109):
    feature = _clean(oc_replacement_109)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_114'] = {'inputs': ['oc_replacement_109'], 'func': oc_replacement_d2_114}


def oc_replacement_d2_115(oc_replacement_110):
    feature = _clean(oc_replacement_110)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_115'] = {'inputs': ['oc_replacement_110'], 'func': oc_replacement_d2_115}


def oc_replacement_d2_116(oc_replacement_111):
    feature = _clean(oc_replacement_111)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_116'] = {'inputs': ['oc_replacement_111'], 'func': oc_replacement_d2_116}


def oc_replacement_d2_117(oc_replacement_112):
    feature = _clean(oc_replacement_112)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_117'] = {'inputs': ['oc_replacement_112'], 'func': oc_replacement_d2_117}


def oc_replacement_d2_118(oc_replacement_113):
    feature = _clean(oc_replacement_113)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_118'] = {'inputs': ['oc_replacement_113'], 'func': oc_replacement_d2_118}


def oc_replacement_d2_119(oc_replacement_114):
    feature = _clean(oc_replacement_114)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_119'] = {'inputs': ['oc_replacement_114'], 'func': oc_replacement_d2_119}


def oc_replacement_d2_120(oc_replacement_115):
    feature = _clean(oc_replacement_115)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_120'] = {'inputs': ['oc_replacement_115'], 'func': oc_replacement_d2_120}


def oc_replacement_d2_121(oc_replacement_116):
    feature = _clean(oc_replacement_116)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_121'] = {'inputs': ['oc_replacement_116'], 'func': oc_replacement_d2_121}


def oc_replacement_d2_122(oc_replacement_117):
    feature = _clean(oc_replacement_117)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_122'] = {'inputs': ['oc_replacement_117'], 'func': oc_replacement_d2_122}


def oc_replacement_d2_123(oc_replacement_118):
    feature = _clean(oc_replacement_118)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_123'] = {'inputs': ['oc_replacement_118'], 'func': oc_replacement_d2_123}


def oc_replacement_d2_124(oc_replacement_119):
    feature = _clean(oc_replacement_119)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_124'] = {'inputs': ['oc_replacement_119'], 'func': oc_replacement_d2_124}


def oc_replacement_d2_125(oc_replacement_120):
    feature = _clean(oc_replacement_120)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_125'] = {'inputs': ['oc_replacement_120'], 'func': oc_replacement_d2_125}


def oc_replacement_d2_126(oc_replacement_121):
    feature = _clean(oc_replacement_121)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_126'] = {'inputs': ['oc_replacement_121'], 'func': oc_replacement_d2_126}


def oc_replacement_d2_127(oc_replacement_122):
    feature = _clean(oc_replacement_122)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_127'] = {'inputs': ['oc_replacement_122'], 'func': oc_replacement_d2_127}


def oc_replacement_d2_128(oc_replacement_123):
    feature = _clean(oc_replacement_123)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_128'] = {'inputs': ['oc_replacement_123'], 'func': oc_replacement_d2_128}


def oc_replacement_d2_129(oc_replacement_124):
    feature = _clean(oc_replacement_124)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_129'] = {'inputs': ['oc_replacement_124'], 'func': oc_replacement_d2_129}


def oc_replacement_d2_130(oc_replacement_125):
    feature = _clean(oc_replacement_125)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_130'] = {'inputs': ['oc_replacement_125'], 'func': oc_replacement_d2_130}


def oc_replacement_d2_131(oc_replacement_126):
    feature = _clean(oc_replacement_126)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_131'] = {'inputs': ['oc_replacement_126'], 'func': oc_replacement_d2_131}


def oc_replacement_d2_132(oc_replacement_127):
    feature = _clean(oc_replacement_127)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_132'] = {'inputs': ['oc_replacement_127'], 'func': oc_replacement_d2_132}


def oc_replacement_d2_133(oc_replacement_128):
    feature = _clean(oc_replacement_128)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_133'] = {'inputs': ['oc_replacement_128'], 'func': oc_replacement_d2_133}


def oc_replacement_d2_134(oc_replacement_129):
    feature = _clean(oc_replacement_129)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_134'] = {'inputs': ['oc_replacement_129'], 'func': oc_replacement_d2_134}


def oc_replacement_d2_135(oc_replacement_130):
    feature = _clean(oc_replacement_130)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_135'] = {'inputs': ['oc_replacement_130'], 'func': oc_replacement_d2_135}


def oc_replacement_d2_136(oc_replacement_131):
    feature = _clean(oc_replacement_131)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_136'] = {'inputs': ['oc_replacement_131'], 'func': oc_replacement_d2_136}


def oc_replacement_d2_137(oc_replacement_132):
    feature = _clean(oc_replacement_132)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_137'] = {'inputs': ['oc_replacement_132'], 'func': oc_replacement_d2_137}


def oc_replacement_d2_138(oc_replacement_133):
    feature = _clean(oc_replacement_133)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_138'] = {'inputs': ['oc_replacement_133'], 'func': oc_replacement_d2_138}


def oc_replacement_d2_139(oc_replacement_134):
    feature = _clean(oc_replacement_134)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_139'] = {'inputs': ['oc_replacement_134'], 'func': oc_replacement_d2_139}


def oc_replacement_d2_140(oc_replacement_135):
    feature = _clean(oc_replacement_135)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_140'] = {'inputs': ['oc_replacement_135'], 'func': oc_replacement_d2_140}


def oc_replacement_d2_141(oc_replacement_136):
    feature = _clean(oc_replacement_136)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_141'] = {'inputs': ['oc_replacement_136'], 'func': oc_replacement_d2_141}


def oc_replacement_d2_142(oc_replacement_137):
    feature = _clean(oc_replacement_137)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_142'] = {'inputs': ['oc_replacement_137'], 'func': oc_replacement_d2_142}


def oc_replacement_d2_143(oc_replacement_138):
    feature = _clean(oc_replacement_138)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_143'] = {'inputs': ['oc_replacement_138'], 'func': oc_replacement_d2_143}


def oc_replacement_d2_144(oc_replacement_139):
    feature = _clean(oc_replacement_139)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_144'] = {'inputs': ['oc_replacement_139'], 'func': oc_replacement_d2_144}


def oc_replacement_d2_145(oc_replacement_140):
    feature = _clean(oc_replacement_140)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_145'] = {'inputs': ['oc_replacement_140'], 'func': oc_replacement_d2_145}


def oc_replacement_d2_146(oc_replacement_141):
    feature = _clean(oc_replacement_141)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_146'] = {'inputs': ['oc_replacement_141'], 'func': oc_replacement_d2_146}


def oc_replacement_d2_147(oc_replacement_142):
    feature = _clean(oc_replacement_142)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_147'] = {'inputs': ['oc_replacement_142'], 'func': oc_replacement_d2_147}


def oc_replacement_d2_148(oc_replacement_143):
    feature = _clean(oc_replacement_143)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_148'] = {'inputs': ['oc_replacement_143'], 'func': oc_replacement_d2_148}


def oc_replacement_d2_149(oc_replacement_144):
    feature = _clean(oc_replacement_144)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_149'] = {'inputs': ['oc_replacement_144'], 'func': oc_replacement_d2_149}


def oc_replacement_d2_150(oc_replacement_145):
    feature = _clean(oc_replacement_145)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_150'] = {'inputs': ['oc_replacement_145'], 'func': oc_replacement_d2_150}


def oc_replacement_d2_151(oc_replacement_146):
    feature = _clean(oc_replacement_146)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_151'] = {'inputs': ['oc_replacement_146'], 'func': oc_replacement_d2_151}


def oc_replacement_d2_152(oc_replacement_147):
    feature = _clean(oc_replacement_147)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_152'] = {'inputs': ['oc_replacement_147'], 'func': oc_replacement_d2_152}


def oc_replacement_d2_153(oc_replacement_148):
    feature = _clean(oc_replacement_148)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_153'] = {'inputs': ['oc_replacement_148'], 'func': oc_replacement_d2_153}


def oc_replacement_d2_154(oc_replacement_149):
    feature = _clean(oc_replacement_149)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_154'] = {'inputs': ['oc_replacement_149'], 'func': oc_replacement_d2_154}


def oc_replacement_d2_155(oc_replacement_150):
    feature = _clean(oc_replacement_150)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_155'] = {'inputs': ['oc_replacement_150'], 'func': oc_replacement_d2_155}


def oc_replacement_d2_156(oc_replacement_151):
    feature = _clean(oc_replacement_151)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_156'] = {'inputs': ['oc_replacement_151'], 'func': oc_replacement_d2_156}


def oc_replacement_d2_157(oc_replacement_152):
    feature = _clean(oc_replacement_152)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_157'] = {'inputs': ['oc_replacement_152'], 'func': oc_replacement_d2_157}


def oc_replacement_d2_158(oc_replacement_153):
    feature = _clean(oc_replacement_153)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_158'] = {'inputs': ['oc_replacement_153'], 'func': oc_replacement_d2_158}


def oc_replacement_d2_159(oc_replacement_154):
    feature = _clean(oc_replacement_154)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_159'] = {'inputs': ['oc_replacement_154'], 'func': oc_replacement_d2_159}


def oc_replacement_d2_160(oc_replacement_155):
    feature = _clean(oc_replacement_155)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_160'] = {'inputs': ['oc_replacement_155'], 'func': oc_replacement_d2_160}


def oc_replacement_d2_161(oc_replacement_156):
    feature = _clean(oc_replacement_156)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_161'] = {'inputs': ['oc_replacement_156'], 'func': oc_replacement_d2_161}


def oc_replacement_d2_162(oc_replacement_157):
    feature = _clean(oc_replacement_157)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_162'] = {'inputs': ['oc_replacement_157'], 'func': oc_replacement_d2_162}


def oc_replacement_d2_163(oc_replacement_158):
    feature = _clean(oc_replacement_158)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_163'] = {'inputs': ['oc_replacement_158'], 'func': oc_replacement_d2_163}


def oc_replacement_d2_164(oc_replacement_159):
    feature = _clean(oc_replacement_159)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_164'] = {'inputs': ['oc_replacement_159'], 'func': oc_replacement_d2_164}


def oc_replacement_d2_165(oc_replacement_160):
    feature = _clean(oc_replacement_160)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_165'] = {'inputs': ['oc_replacement_160'], 'func': oc_replacement_d2_165}


def oc_replacement_d2_166(oc_replacement_161):
    feature = _clean(oc_replacement_161)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_166'] = {'inputs': ['oc_replacement_161'], 'func': oc_replacement_d2_166}


def oc_replacement_d2_167(oc_replacement_162):
    feature = _clean(oc_replacement_162)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_167'] = {'inputs': ['oc_replacement_162'], 'func': oc_replacement_d2_167}


def oc_replacement_d2_168(oc_replacement_163):
    feature = _clean(oc_replacement_163)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_168'] = {'inputs': ['oc_replacement_163'], 'func': oc_replacement_d2_168}


def oc_replacement_d2_169(oc_replacement_164):
    feature = _clean(oc_replacement_164)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_169'] = {'inputs': ['oc_replacement_164'], 'func': oc_replacement_d2_169}


def oc_replacement_d2_170(oc_replacement_165):
    feature = _clean(oc_replacement_165)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
OC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['oc_replacement_d2_170'] = {'inputs': ['oc_replacement_165'], 'func': oc_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63(ocn_003_top_holder_concentration_63):
    return _base_universe_d2(ocn_003_top_holder_concentration_63, 1)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63'] = {'inputs': ['ocn_003_top_holder_concentration_63'], 'func': ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63}


def ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84(ocn_004_institutional_net_flow_84):
    return _base_universe_d2(ocn_004_institutional_net_flow_84, 2)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84'] = {'inputs': ['ocn_004_institutional_net_flow_84'], 'func': ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84}


def ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126(ocn_005_forced_selling_pressure_126):
    return _base_universe_d2(ocn_005_forced_selling_pressure_126, 3)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126'] = {'inputs': ['ocn_005_forced_selling_pressure_126'], 'func': ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126}


def ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189(ocn_006_holder_base_volatility_189):
    return _base_universe_d2(ocn_006_holder_base_volatility_189, 4)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189'] = {'inputs': ['ocn_006_holder_base_volatility_189'], 'func': ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189}


def ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504(ocn_009_top_holder_concentration_504):
    return _base_universe_d2(ocn_009_top_holder_concentration_504, 5)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504'] = {'inputs': ['ocn_009_top_holder_concentration_504'], 'func': ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504}


def ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756(ocn_010_institutional_net_flow_756):
    return _base_universe_d2(ocn_010_institutional_net_flow_756, 6)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756'] = {'inputs': ['ocn_010_institutional_net_flow_756'], 'func': ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756}


def ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008(ocn_011_forced_selling_pressure_1008):
    return _base_universe_d2(ocn_011_forced_selling_pressure_1008, 7)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008'] = {'inputs': ['ocn_011_forced_selling_pressure_1008'], 'func': ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008}


def ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260(ocn_012_holder_base_volatility_1260):
    return _base_universe_d2(ocn_012_holder_base_volatility_1260, 8)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260'] = {'inputs': ['ocn_012_holder_base_volatility_1260'], 'func': ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260}


def ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252(ocn_015_top_holder_concentration_252):
    return _base_universe_d2(ocn_015_top_holder_concentration_252, 9)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252'] = {'inputs': ['ocn_015_top_holder_concentration_252'], 'func': ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252}


def ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21(ocn_016_institutional_net_flow_21):
    return _base_universe_d2(ocn_016_institutional_net_flow_21, 10)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21'] = {'inputs': ['ocn_016_institutional_net_flow_21'], 'func': ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21}


def ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42(ocn_017_forced_selling_pressure_42):
    return _base_universe_d2(ocn_017_forced_selling_pressure_42, 11)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42'] = {'inputs': ['ocn_017_forced_selling_pressure_42'], 'func': ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42}


def ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63(ocn_018_holder_base_volatility_63):
    return _base_universe_d2(ocn_018_holder_base_volatility_63, 12)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63'] = {'inputs': ['ocn_018_holder_base_volatility_63'], 'func': ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63}


def ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189(ocn_021_top_holder_concentration_189):
    return _base_universe_d2(ocn_021_top_holder_concentration_189, 13)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189'] = {'inputs': ['ocn_021_top_holder_concentration_189'], 'func': ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189}


def ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252(ocn_022_institutional_net_flow_252):
    return _base_universe_d2(ocn_022_institutional_net_flow_252, 14)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252'] = {'inputs': ['ocn_022_institutional_net_flow_252'], 'func': ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252}


def ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378(ocn_023_forced_selling_pressure_378):
    return _base_universe_d2(ocn_023_forced_selling_pressure_378, 15)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378'] = {'inputs': ['ocn_023_forced_selling_pressure_378'], 'func': ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378}


def ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504(ocn_024_holder_base_volatility_504):
    return _base_universe_d2(ocn_024_holder_base_volatility_504, 16)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504'] = {'inputs': ['ocn_024_holder_base_volatility_504'], 'func': ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504}


def ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260(ocn_027_top_holder_concentration_1260):
    return _base_universe_d2(ocn_027_top_holder_concentration_1260, 17)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260'] = {'inputs': ['ocn_027_top_holder_concentration_1260'], 'func': ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260}


def ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512(ocn_028_institutional_net_flow_1512):
    return _base_universe_d2(ocn_028_institutional_net_flow_1512, 18)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512'] = {'inputs': ['ocn_028_institutional_net_flow_1512'], 'func': ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512}


def ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63(ocn_029_forced_selling_pressure_63):
    return _base_universe_d2(ocn_029_forced_selling_pressure_63, 19)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63'] = {'inputs': ['ocn_029_forced_selling_pressure_63'], 'func': ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63}


def ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252(ocn_030_holder_base_volatility_252):
    return _base_universe_d2(ocn_030_holder_base_volatility_252, 20)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252'] = {'inputs': ['ocn_030_holder_base_volatility_252'], 'func': ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252}


def ocn_base_universe_d2_021_ocn_basefill_001(ocn_basefill_001):
    return _base_universe_d2(ocn_basefill_001, 21)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_021_ocn_basefill_001'] = {'inputs': ['ocn_basefill_001'], 'func': ocn_base_universe_d2_021_ocn_basefill_001}


def ocn_base_universe_d2_022_ocn_basefill_002(ocn_basefill_002):
    return _base_universe_d2(ocn_basefill_002, 22)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_022_ocn_basefill_002'] = {'inputs': ['ocn_basefill_002'], 'func': ocn_base_universe_d2_022_ocn_basefill_002}


def ocn_base_universe_d2_023_ocn_basefill_007(ocn_basefill_007):
    return _base_universe_d2(ocn_basefill_007, 23)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_023_ocn_basefill_007'] = {'inputs': ['ocn_basefill_007'], 'func': ocn_base_universe_d2_023_ocn_basefill_007}


def ocn_base_universe_d2_024_ocn_basefill_008(ocn_basefill_008):
    return _base_universe_d2(ocn_basefill_008, 24)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_024_ocn_basefill_008'] = {'inputs': ['ocn_basefill_008'], 'func': ocn_base_universe_d2_024_ocn_basefill_008}


def ocn_base_universe_d2_025_ocn_basefill_013(ocn_basefill_013):
    return _base_universe_d2(ocn_basefill_013, 25)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_025_ocn_basefill_013'] = {'inputs': ['ocn_basefill_013'], 'func': ocn_base_universe_d2_025_ocn_basefill_013}


def ocn_base_universe_d2_026_ocn_basefill_014(ocn_basefill_014):
    return _base_universe_d2(ocn_basefill_014, 26)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_026_ocn_basefill_014'] = {'inputs': ['ocn_basefill_014'], 'func': ocn_base_universe_d2_026_ocn_basefill_014}


def ocn_base_universe_d2_027_ocn_basefill_019(ocn_basefill_019):
    return _base_universe_d2(ocn_basefill_019, 27)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_027_ocn_basefill_019'] = {'inputs': ['ocn_basefill_019'], 'func': ocn_base_universe_d2_027_ocn_basefill_019}


def ocn_base_universe_d2_028_ocn_basefill_020(ocn_basefill_020):
    return _base_universe_d2(ocn_basefill_020, 28)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_028_ocn_basefill_020'] = {'inputs': ['ocn_basefill_020'], 'func': ocn_base_universe_d2_028_ocn_basefill_020}


def ocn_base_universe_d2_029_ocn_basefill_025(ocn_basefill_025):
    return _base_universe_d2(ocn_basefill_025, 29)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_029_ocn_basefill_025'] = {'inputs': ['ocn_basefill_025'], 'func': ocn_base_universe_d2_029_ocn_basefill_025}


def ocn_base_universe_d2_030_ocn_basefill_026(ocn_basefill_026):
    return _base_universe_d2(ocn_basefill_026, 30)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_030_ocn_basefill_026'] = {'inputs': ['ocn_basefill_026'], 'func': ocn_base_universe_d2_030_ocn_basefill_026}


def ocn_base_universe_d2_031_ocn_basefill_031(ocn_basefill_031):
    return _base_universe_d2(ocn_basefill_031, 31)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_031_ocn_basefill_031'] = {'inputs': ['ocn_basefill_031'], 'func': ocn_base_universe_d2_031_ocn_basefill_031}


def ocn_base_universe_d2_032_ocn_basefill_032(ocn_basefill_032):
    return _base_universe_d2(ocn_basefill_032, 32)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_032_ocn_basefill_032'] = {'inputs': ['ocn_basefill_032'], 'func': ocn_base_universe_d2_032_ocn_basefill_032}


def ocn_base_universe_d2_033_ocn_basefill_033(ocn_basefill_033):
    return _base_universe_d2(ocn_basefill_033, 33)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_033_ocn_basefill_033'] = {'inputs': ['ocn_basefill_033'], 'func': ocn_base_universe_d2_033_ocn_basefill_033}


def ocn_base_universe_d2_034_ocn_basefill_034(ocn_basefill_034):
    return _base_universe_d2(ocn_basefill_034, 34)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_034_ocn_basefill_034'] = {'inputs': ['ocn_basefill_034'], 'func': ocn_base_universe_d2_034_ocn_basefill_034}


def ocn_base_universe_d2_035_ocn_basefill_035(ocn_basefill_035):
    return _base_universe_d2(ocn_basefill_035, 35)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_035_ocn_basefill_035'] = {'inputs': ['ocn_basefill_035'], 'func': ocn_base_universe_d2_035_ocn_basefill_035}


def ocn_base_universe_d2_036_ocn_basefill_036(ocn_basefill_036):
    return _base_universe_d2(ocn_basefill_036, 36)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_036_ocn_basefill_036'] = {'inputs': ['ocn_basefill_036'], 'func': ocn_base_universe_d2_036_ocn_basefill_036}


def ocn_base_universe_d2_037_ocn_basefill_037(ocn_basefill_037):
    return _base_universe_d2(ocn_basefill_037, 37)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_037_ocn_basefill_037'] = {'inputs': ['ocn_basefill_037'], 'func': ocn_base_universe_d2_037_ocn_basefill_037}


def ocn_base_universe_d2_038_ocn_basefill_038(ocn_basefill_038):
    return _base_universe_d2(ocn_basefill_038, 38)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_038_ocn_basefill_038'] = {'inputs': ['ocn_basefill_038'], 'func': ocn_base_universe_d2_038_ocn_basefill_038}


def ocn_base_universe_d2_039_ocn_basefill_039(ocn_basefill_039):
    return _base_universe_d2(ocn_basefill_039, 39)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_039_ocn_basefill_039'] = {'inputs': ['ocn_basefill_039'], 'func': ocn_base_universe_d2_039_ocn_basefill_039}


def ocn_base_universe_d2_040_ocn_basefill_040(ocn_basefill_040):
    return _base_universe_d2(ocn_basefill_040, 40)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_040_ocn_basefill_040'] = {'inputs': ['ocn_basefill_040'], 'func': ocn_base_universe_d2_040_ocn_basefill_040}


def ocn_base_universe_d2_041_ocn_basefill_041(ocn_basefill_041):
    return _base_universe_d2(ocn_basefill_041, 41)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_041_ocn_basefill_041'] = {'inputs': ['ocn_basefill_041'], 'func': ocn_base_universe_d2_041_ocn_basefill_041}


def ocn_base_universe_d2_042_ocn_basefill_042(ocn_basefill_042):
    return _base_universe_d2(ocn_basefill_042, 42)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_042_ocn_basefill_042'] = {'inputs': ['ocn_basefill_042'], 'func': ocn_base_universe_d2_042_ocn_basefill_042}


def ocn_base_universe_d2_043_ocn_basefill_043(ocn_basefill_043):
    return _base_universe_d2(ocn_basefill_043, 43)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_043_ocn_basefill_043'] = {'inputs': ['ocn_basefill_043'], 'func': ocn_base_universe_d2_043_ocn_basefill_043}


def ocn_base_universe_d2_044_ocn_basefill_044(ocn_basefill_044):
    return _base_universe_d2(ocn_basefill_044, 44)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_044_ocn_basefill_044'] = {'inputs': ['ocn_basefill_044'], 'func': ocn_base_universe_d2_044_ocn_basefill_044}


def ocn_base_universe_d2_045_ocn_basefill_045(ocn_basefill_045):
    return _base_universe_d2(ocn_basefill_045, 45)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_045_ocn_basefill_045'] = {'inputs': ['ocn_basefill_045'], 'func': ocn_base_universe_d2_045_ocn_basefill_045}


def ocn_base_universe_d2_046_ocn_basefill_046(ocn_basefill_046):
    return _base_universe_d2(ocn_basefill_046, 46)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_046_ocn_basefill_046'] = {'inputs': ['ocn_basefill_046'], 'func': ocn_base_universe_d2_046_ocn_basefill_046}


def ocn_base_universe_d2_047_ocn_basefill_047(ocn_basefill_047):
    return _base_universe_d2(ocn_basefill_047, 47)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_047_ocn_basefill_047'] = {'inputs': ['ocn_basefill_047'], 'func': ocn_base_universe_d2_047_ocn_basefill_047}


def ocn_base_universe_d2_048_ocn_basefill_048(ocn_basefill_048):
    return _base_universe_d2(ocn_basefill_048, 48)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_048_ocn_basefill_048'] = {'inputs': ['ocn_basefill_048'], 'func': ocn_base_universe_d2_048_ocn_basefill_048}


def ocn_base_universe_d2_049_ocn_basefill_049(ocn_basefill_049):
    return _base_universe_d2(ocn_basefill_049, 49)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_049_ocn_basefill_049'] = {'inputs': ['ocn_basefill_049'], 'func': ocn_base_universe_d2_049_ocn_basefill_049}


def ocn_base_universe_d2_050_ocn_basefill_050(ocn_basefill_050):
    return _base_universe_d2(ocn_basefill_050, 50)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_050_ocn_basefill_050'] = {'inputs': ['ocn_basefill_050'], 'func': ocn_base_universe_d2_050_ocn_basefill_050}


def ocn_base_universe_d2_051_ocn_basefill_051(ocn_basefill_051):
    return _base_universe_d2(ocn_basefill_051, 51)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_051_ocn_basefill_051'] = {'inputs': ['ocn_basefill_051'], 'func': ocn_base_universe_d2_051_ocn_basefill_051}


def ocn_base_universe_d2_052_ocn_basefill_052(ocn_basefill_052):
    return _base_universe_d2(ocn_basefill_052, 52)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_052_ocn_basefill_052'] = {'inputs': ['ocn_basefill_052'], 'func': ocn_base_universe_d2_052_ocn_basefill_052}


def ocn_base_universe_d2_053_ocn_basefill_053(ocn_basefill_053):
    return _base_universe_d2(ocn_basefill_053, 53)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_053_ocn_basefill_053'] = {'inputs': ['ocn_basefill_053'], 'func': ocn_base_universe_d2_053_ocn_basefill_053}


def ocn_base_universe_d2_054_ocn_basefill_054(ocn_basefill_054):
    return _base_universe_d2(ocn_basefill_054, 54)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_054_ocn_basefill_054'] = {'inputs': ['ocn_basefill_054'], 'func': ocn_base_universe_d2_054_ocn_basefill_054}


def ocn_base_universe_d2_055_ocn_basefill_055(ocn_basefill_055):
    return _base_universe_d2(ocn_basefill_055, 55)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_055_ocn_basefill_055'] = {'inputs': ['ocn_basefill_055'], 'func': ocn_base_universe_d2_055_ocn_basefill_055}


def ocn_base_universe_d2_056_ocn_basefill_056(ocn_basefill_056):
    return _base_universe_d2(ocn_basefill_056, 56)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_056_ocn_basefill_056'] = {'inputs': ['ocn_basefill_056'], 'func': ocn_base_universe_d2_056_ocn_basefill_056}


def ocn_base_universe_d2_057_ocn_basefill_057(ocn_basefill_057):
    return _base_universe_d2(ocn_basefill_057, 57)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_057_ocn_basefill_057'] = {'inputs': ['ocn_basefill_057'], 'func': ocn_base_universe_d2_057_ocn_basefill_057}


def ocn_base_universe_d2_058_ocn_basefill_058(ocn_basefill_058):
    return _base_universe_d2(ocn_basefill_058, 58)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_058_ocn_basefill_058'] = {'inputs': ['ocn_basefill_058'], 'func': ocn_base_universe_d2_058_ocn_basefill_058}


def ocn_base_universe_d2_059_ocn_basefill_059(ocn_basefill_059):
    return _base_universe_d2(ocn_basefill_059, 59)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_059_ocn_basefill_059'] = {'inputs': ['ocn_basefill_059'], 'func': ocn_base_universe_d2_059_ocn_basefill_059}


def ocn_base_universe_d2_060_ocn_basefill_060(ocn_basefill_060):
    return _base_universe_d2(ocn_basefill_060, 60)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_060_ocn_basefill_060'] = {'inputs': ['ocn_basefill_060'], 'func': ocn_base_universe_d2_060_ocn_basefill_060}


def ocn_base_universe_d2_061_ocn_basefill_061(ocn_basefill_061):
    return _base_universe_d2(ocn_basefill_061, 61)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_061_ocn_basefill_061'] = {'inputs': ['ocn_basefill_061'], 'func': ocn_base_universe_d2_061_ocn_basefill_061}


def ocn_base_universe_d2_062_ocn_basefill_062(ocn_basefill_062):
    return _base_universe_d2(ocn_basefill_062, 62)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_062_ocn_basefill_062'] = {'inputs': ['ocn_basefill_062'], 'func': ocn_base_universe_d2_062_ocn_basefill_062}


def ocn_base_universe_d2_063_ocn_basefill_063(ocn_basefill_063):
    return _base_universe_d2(ocn_basefill_063, 63)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_063_ocn_basefill_063'] = {'inputs': ['ocn_basefill_063'], 'func': ocn_base_universe_d2_063_ocn_basefill_063}


def ocn_base_universe_d2_064_ocn_basefill_064(ocn_basefill_064):
    return _base_universe_d2(ocn_basefill_064, 64)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_064_ocn_basefill_064'] = {'inputs': ['ocn_basefill_064'], 'func': ocn_base_universe_d2_064_ocn_basefill_064}


def ocn_base_universe_d2_065_ocn_basefill_065(ocn_basefill_065):
    return _base_universe_d2(ocn_basefill_065, 65)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_065_ocn_basefill_065'] = {'inputs': ['ocn_basefill_065'], 'func': ocn_base_universe_d2_065_ocn_basefill_065}


def ocn_base_universe_d2_066_ocn_basefill_066(ocn_basefill_066):
    return _base_universe_d2(ocn_basefill_066, 66)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_066_ocn_basefill_066'] = {'inputs': ['ocn_basefill_066'], 'func': ocn_base_universe_d2_066_ocn_basefill_066}


def ocn_base_universe_d2_067_ocn_basefill_067(ocn_basefill_067):
    return _base_universe_d2(ocn_basefill_067, 67)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_067_ocn_basefill_067'] = {'inputs': ['ocn_basefill_067'], 'func': ocn_base_universe_d2_067_ocn_basefill_067}


def ocn_base_universe_d2_068_ocn_basefill_068(ocn_basefill_068):
    return _base_universe_d2(ocn_basefill_068, 68)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_068_ocn_basefill_068'] = {'inputs': ['ocn_basefill_068'], 'func': ocn_base_universe_d2_068_ocn_basefill_068}


def ocn_base_universe_d2_069_ocn_basefill_069(ocn_basefill_069):
    return _base_universe_d2(ocn_basefill_069, 69)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_069_ocn_basefill_069'] = {'inputs': ['ocn_basefill_069'], 'func': ocn_base_universe_d2_069_ocn_basefill_069}


def ocn_base_universe_d2_070_ocn_basefill_070(ocn_basefill_070):
    return _base_universe_d2(ocn_basefill_070, 70)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_070_ocn_basefill_070'] = {'inputs': ['ocn_basefill_070'], 'func': ocn_base_universe_d2_070_ocn_basefill_070}


def ocn_base_universe_d2_071_ocn_basefill_071(ocn_basefill_071):
    return _base_universe_d2(ocn_basefill_071, 71)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_071_ocn_basefill_071'] = {'inputs': ['ocn_basefill_071'], 'func': ocn_base_universe_d2_071_ocn_basefill_071}


def ocn_base_universe_d2_072_ocn_basefill_072(ocn_basefill_072):
    return _base_universe_d2(ocn_basefill_072, 72)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_072_ocn_basefill_072'] = {'inputs': ['ocn_basefill_072'], 'func': ocn_base_universe_d2_072_ocn_basefill_072}


def ocn_base_universe_d2_073_ocn_basefill_073(ocn_basefill_073):
    return _base_universe_d2(ocn_basefill_073, 73)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_073_ocn_basefill_073'] = {'inputs': ['ocn_basefill_073'], 'func': ocn_base_universe_d2_073_ocn_basefill_073}


def ocn_base_universe_d2_074_ocn_basefill_074(ocn_basefill_074):
    return _base_universe_d2(ocn_basefill_074, 74)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_074_ocn_basefill_074'] = {'inputs': ['ocn_basefill_074'], 'func': ocn_base_universe_d2_074_ocn_basefill_074}


def ocn_base_universe_d2_075_ocn_basefill_075(ocn_basefill_075):
    return _base_universe_d2(ocn_basefill_075, 75)
OCN_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ocn_base_universe_d2_075_ocn_basefill_075'] = {'inputs': ['ocn_basefill_075'], 'func': ocn_base_universe_d2_075_ocn_basefill_075}
