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



def hcd_151_hcd_001_holder_count_vs_peer_21_roc_1(hcd_001_holder_count_vs_peer_21):
    feature = _s(hcd_001_holder_count_vs_peer_21)
    return (_roc(feature, 1)).reindex(feature.index)

def hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42(hcd_007_holder_breadth_peer_z_252):
    feature = _s(hcd_007_holder_breadth_peer_z_252)
    return (_roc(feature, 42)).reindex(feature.index)

def hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126(hcd_013_holder_count_vs_peer_1512):
    feature = _s(hcd_013_holder_count_vs_peer_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378(hcd_019_holder_breadth_peer_z_84):
    feature = _s(hcd_019_holder_breadth_peer_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def hcd_155_hcd_025_holder_count_vs_peer_756_roc_4(hcd_025_holder_count_vs_peer_756):
    feature = _s(hcd_025_holder_count_vs_peer_756)
    return (_roc(feature, 4)).reindex(feature.index)






















HOLDER_COUNT_DYNAMICS_REGISTRY_2ND_DERIVATIVES = {
    'hcd_151_hcd_001_holder_count_vs_peer_21_roc_1': {'inputs': ['hcd_001_holder_count_vs_peer_21'], 'func': hcd_151_hcd_001_holder_count_vs_peer_21_roc_1},
    'hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42': {'inputs': ['hcd_007_holder_breadth_peer_z_252'], 'func': hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42},
    'hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126': {'inputs': ['hcd_013_holder_count_vs_peer_1512'], 'func': hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126},
    'hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378': {'inputs': ['hcd_019_holder_breadth_peer_z_84'], 'func': hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378},
    'hcd_155_hcd_025_holder_count_vs_peer_756_roc_4': {'inputs': ['hcd_025_holder_count_vs_peer_756'], 'func': hcd_155_hcd_025_holder_count_vs_peer_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def hcd_replacement_d2_001(hcd_013_holder_count_vs_peer_1512):
    feature = _clean(hcd_013_holder_count_vs_peer_1512)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_001'] = {'inputs': ['hcd_013_holder_count_vs_peer_1512'], 'func': hcd_replacement_d2_001}


def hcd_replacement_d2_002(hcd_025_holder_count_vs_peer_756):
    feature = _clean(hcd_025_holder_count_vs_peer_756)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_002'] = {'inputs': ['hcd_025_holder_count_vs_peer_756'], 'func': hcd_replacement_d2_002}


def hcd_replacement_d2_003(hcd_replacement_001):
    feature = _clean(hcd_replacement_001)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_003'] = {'inputs': ['hcd_replacement_001'], 'func': hcd_replacement_d2_003}


def hcd_replacement_d2_004(hcd_replacement_002):
    feature = _clean(hcd_replacement_002)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_004'] = {'inputs': ['hcd_replacement_002'], 'func': hcd_replacement_d2_004}


def hcd_replacement_d2_005(hcd_replacement_003):
    feature = _clean(hcd_replacement_003)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_005'] = {'inputs': ['hcd_replacement_003'], 'func': hcd_replacement_d2_005}


def hcd_replacement_d2_006(hcd_replacement_004):
    feature = _clean(hcd_replacement_004)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_006'] = {'inputs': ['hcd_replacement_004'], 'func': hcd_replacement_d2_006}


def hcd_replacement_d2_007(hcd_replacement_005):
    feature = _clean(hcd_replacement_005)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_007'] = {'inputs': ['hcd_replacement_005'], 'func': hcd_replacement_d2_007}


def hcd_replacement_d2_008(hcd_replacement_006):
    feature = _clean(hcd_replacement_006)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_008'] = {'inputs': ['hcd_replacement_006'], 'func': hcd_replacement_d2_008}


def hcd_replacement_d2_009(hcd_replacement_007):
    feature = _clean(hcd_replacement_007)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_009'] = {'inputs': ['hcd_replacement_007'], 'func': hcd_replacement_d2_009}


def hcd_replacement_d2_010(hcd_replacement_008):
    feature = _clean(hcd_replacement_008)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_010'] = {'inputs': ['hcd_replacement_008'], 'func': hcd_replacement_d2_010}


def hcd_replacement_d2_011(hcd_replacement_009):
    feature = _clean(hcd_replacement_009)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_011'] = {'inputs': ['hcd_replacement_009'], 'func': hcd_replacement_d2_011}


def hcd_replacement_d2_012(hcd_replacement_010):
    feature = _clean(hcd_replacement_010)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_012'] = {'inputs': ['hcd_replacement_010'], 'func': hcd_replacement_d2_012}


def hcd_replacement_d2_013(hcd_replacement_011):
    feature = _clean(hcd_replacement_011)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_013'] = {'inputs': ['hcd_replacement_011'], 'func': hcd_replacement_d2_013}


def hcd_replacement_d2_014(hcd_replacement_012):
    feature = _clean(hcd_replacement_012)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_014'] = {'inputs': ['hcd_replacement_012'], 'func': hcd_replacement_d2_014}


def hcd_replacement_d2_015(hcd_replacement_013):
    feature = _clean(hcd_replacement_013)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_015'] = {'inputs': ['hcd_replacement_013'], 'func': hcd_replacement_d2_015}


def hcd_replacement_d2_016(hcd_replacement_014):
    feature = _clean(hcd_replacement_014)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_016'] = {'inputs': ['hcd_replacement_014'], 'func': hcd_replacement_d2_016}


def hcd_replacement_d2_017(hcd_replacement_015):
    feature = _clean(hcd_replacement_015)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_017'] = {'inputs': ['hcd_replacement_015'], 'func': hcd_replacement_d2_017}


def hcd_replacement_d2_018(hcd_replacement_016):
    feature = _clean(hcd_replacement_016)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_018'] = {'inputs': ['hcd_replacement_016'], 'func': hcd_replacement_d2_018}


def hcd_replacement_d2_019(hcd_replacement_017):
    feature = _clean(hcd_replacement_017)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_019'] = {'inputs': ['hcd_replacement_017'], 'func': hcd_replacement_d2_019}


def hcd_replacement_d2_020(hcd_replacement_018):
    feature = _clean(hcd_replacement_018)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_020'] = {'inputs': ['hcd_replacement_018'], 'func': hcd_replacement_d2_020}


def hcd_replacement_d2_021(hcd_replacement_019):
    feature = _clean(hcd_replacement_019)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_021'] = {'inputs': ['hcd_replacement_019'], 'func': hcd_replacement_d2_021}


def hcd_replacement_d2_022(hcd_replacement_020):
    feature = _clean(hcd_replacement_020)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_022'] = {'inputs': ['hcd_replacement_020'], 'func': hcd_replacement_d2_022}


def hcd_replacement_d2_023(hcd_replacement_021):
    feature = _clean(hcd_replacement_021)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_023'] = {'inputs': ['hcd_replacement_021'], 'func': hcd_replacement_d2_023}


def hcd_replacement_d2_024(hcd_replacement_022):
    feature = _clean(hcd_replacement_022)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_024'] = {'inputs': ['hcd_replacement_022'], 'func': hcd_replacement_d2_024}


def hcd_replacement_d2_025(hcd_replacement_023):
    feature = _clean(hcd_replacement_023)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_025'] = {'inputs': ['hcd_replacement_023'], 'func': hcd_replacement_d2_025}


def hcd_replacement_d2_026(hcd_replacement_024):
    feature = _clean(hcd_replacement_024)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_026'] = {'inputs': ['hcd_replacement_024'], 'func': hcd_replacement_d2_026}


def hcd_replacement_d2_027(hcd_replacement_025):
    feature = _clean(hcd_replacement_025)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_027'] = {'inputs': ['hcd_replacement_025'], 'func': hcd_replacement_d2_027}


def hcd_replacement_d2_028(hcd_replacement_026):
    feature = _clean(hcd_replacement_026)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_028'] = {'inputs': ['hcd_replacement_026'], 'func': hcd_replacement_d2_028}


def hcd_replacement_d2_029(hcd_replacement_027):
    feature = _clean(hcd_replacement_027)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_029'] = {'inputs': ['hcd_replacement_027'], 'func': hcd_replacement_d2_029}


def hcd_replacement_d2_030(hcd_replacement_028):
    feature = _clean(hcd_replacement_028)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_030'] = {'inputs': ['hcd_replacement_028'], 'func': hcd_replacement_d2_030}


def hcd_replacement_d2_031(hcd_replacement_029):
    feature = _clean(hcd_replacement_029)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_031'] = {'inputs': ['hcd_replacement_029'], 'func': hcd_replacement_d2_031}


def hcd_replacement_d2_032(hcd_replacement_030):
    feature = _clean(hcd_replacement_030)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_032'] = {'inputs': ['hcd_replacement_030'], 'func': hcd_replacement_d2_032}


def hcd_replacement_d2_033(hcd_replacement_031):
    feature = _clean(hcd_replacement_031)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_033'] = {'inputs': ['hcd_replacement_031'], 'func': hcd_replacement_d2_033}


def hcd_replacement_d2_034(hcd_replacement_032):
    feature = _clean(hcd_replacement_032)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_034'] = {'inputs': ['hcd_replacement_032'], 'func': hcd_replacement_d2_034}


def hcd_replacement_d2_035(hcd_replacement_033):
    feature = _clean(hcd_replacement_033)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_035'] = {'inputs': ['hcd_replacement_033'], 'func': hcd_replacement_d2_035}


def hcd_replacement_d2_036(hcd_replacement_034):
    feature = _clean(hcd_replacement_034)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_036'] = {'inputs': ['hcd_replacement_034'], 'func': hcd_replacement_d2_036}


def hcd_replacement_d2_037(hcd_replacement_035):
    feature = _clean(hcd_replacement_035)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_037'] = {'inputs': ['hcd_replacement_035'], 'func': hcd_replacement_d2_037}


def hcd_replacement_d2_038(hcd_replacement_036):
    feature = _clean(hcd_replacement_036)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_038'] = {'inputs': ['hcd_replacement_036'], 'func': hcd_replacement_d2_038}


def hcd_replacement_d2_039(hcd_replacement_037):
    feature = _clean(hcd_replacement_037)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_039'] = {'inputs': ['hcd_replacement_037'], 'func': hcd_replacement_d2_039}


def hcd_replacement_d2_040(hcd_replacement_038):
    feature = _clean(hcd_replacement_038)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_040'] = {'inputs': ['hcd_replacement_038'], 'func': hcd_replacement_d2_040}


def hcd_replacement_d2_041(hcd_replacement_039):
    feature = _clean(hcd_replacement_039)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_041'] = {'inputs': ['hcd_replacement_039'], 'func': hcd_replacement_d2_041}


def hcd_replacement_d2_042(hcd_replacement_040):
    feature = _clean(hcd_replacement_040)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_042'] = {'inputs': ['hcd_replacement_040'], 'func': hcd_replacement_d2_042}


def hcd_replacement_d2_043(hcd_replacement_041):
    feature = _clean(hcd_replacement_041)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_043'] = {'inputs': ['hcd_replacement_041'], 'func': hcd_replacement_d2_043}


def hcd_replacement_d2_044(hcd_replacement_042):
    feature = _clean(hcd_replacement_042)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_044'] = {'inputs': ['hcd_replacement_042'], 'func': hcd_replacement_d2_044}


def hcd_replacement_d2_045(hcd_replacement_043):
    feature = _clean(hcd_replacement_043)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_045'] = {'inputs': ['hcd_replacement_043'], 'func': hcd_replacement_d2_045}


def hcd_replacement_d2_046(hcd_replacement_044):
    feature = _clean(hcd_replacement_044)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_046'] = {'inputs': ['hcd_replacement_044'], 'func': hcd_replacement_d2_046}


def hcd_replacement_d2_047(hcd_replacement_045):
    feature = _clean(hcd_replacement_045)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_047'] = {'inputs': ['hcd_replacement_045'], 'func': hcd_replacement_d2_047}


def hcd_replacement_d2_048(hcd_replacement_046):
    feature = _clean(hcd_replacement_046)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_048'] = {'inputs': ['hcd_replacement_046'], 'func': hcd_replacement_d2_048}


def hcd_replacement_d2_049(hcd_replacement_047):
    feature = _clean(hcd_replacement_047)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_049'] = {'inputs': ['hcd_replacement_047'], 'func': hcd_replacement_d2_049}


def hcd_replacement_d2_050(hcd_replacement_048):
    feature = _clean(hcd_replacement_048)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_050'] = {'inputs': ['hcd_replacement_048'], 'func': hcd_replacement_d2_050}


def hcd_replacement_d2_051(hcd_replacement_049):
    feature = _clean(hcd_replacement_049)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_051'] = {'inputs': ['hcd_replacement_049'], 'func': hcd_replacement_d2_051}


def hcd_replacement_d2_052(hcd_replacement_050):
    feature = _clean(hcd_replacement_050)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_052'] = {'inputs': ['hcd_replacement_050'], 'func': hcd_replacement_d2_052}


def hcd_replacement_d2_053(hcd_replacement_051):
    feature = _clean(hcd_replacement_051)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_053'] = {'inputs': ['hcd_replacement_051'], 'func': hcd_replacement_d2_053}


def hcd_replacement_d2_054(hcd_replacement_052):
    feature = _clean(hcd_replacement_052)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_054'] = {'inputs': ['hcd_replacement_052'], 'func': hcd_replacement_d2_054}


def hcd_replacement_d2_055(hcd_replacement_053):
    feature = _clean(hcd_replacement_053)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_055'] = {'inputs': ['hcd_replacement_053'], 'func': hcd_replacement_d2_055}


def hcd_replacement_d2_056(hcd_replacement_054):
    feature = _clean(hcd_replacement_054)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_056'] = {'inputs': ['hcd_replacement_054'], 'func': hcd_replacement_d2_056}


def hcd_replacement_d2_057(hcd_replacement_055):
    feature = _clean(hcd_replacement_055)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_057'] = {'inputs': ['hcd_replacement_055'], 'func': hcd_replacement_d2_057}


def hcd_replacement_d2_058(hcd_replacement_056):
    feature = _clean(hcd_replacement_056)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_058'] = {'inputs': ['hcd_replacement_056'], 'func': hcd_replacement_d2_058}


def hcd_replacement_d2_059(hcd_replacement_057):
    feature = _clean(hcd_replacement_057)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_059'] = {'inputs': ['hcd_replacement_057'], 'func': hcd_replacement_d2_059}


def hcd_replacement_d2_060(hcd_replacement_058):
    feature = _clean(hcd_replacement_058)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_060'] = {'inputs': ['hcd_replacement_058'], 'func': hcd_replacement_d2_060}


def hcd_replacement_d2_061(hcd_replacement_059):
    feature = _clean(hcd_replacement_059)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_061'] = {'inputs': ['hcd_replacement_059'], 'func': hcd_replacement_d2_061}


def hcd_replacement_d2_062(hcd_replacement_060):
    feature = _clean(hcd_replacement_060)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_062'] = {'inputs': ['hcd_replacement_060'], 'func': hcd_replacement_d2_062}


def hcd_replacement_d2_063(hcd_replacement_061):
    feature = _clean(hcd_replacement_061)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_063'] = {'inputs': ['hcd_replacement_061'], 'func': hcd_replacement_d2_063}


def hcd_replacement_d2_064(hcd_replacement_062):
    feature = _clean(hcd_replacement_062)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_064'] = {'inputs': ['hcd_replacement_062'], 'func': hcd_replacement_d2_064}


def hcd_replacement_d2_065(hcd_replacement_063):
    feature = _clean(hcd_replacement_063)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_065'] = {'inputs': ['hcd_replacement_063'], 'func': hcd_replacement_d2_065}


def hcd_replacement_d2_066(hcd_replacement_064):
    feature = _clean(hcd_replacement_064)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_066'] = {'inputs': ['hcd_replacement_064'], 'func': hcd_replacement_d2_066}


def hcd_replacement_d2_067(hcd_replacement_065):
    feature = _clean(hcd_replacement_065)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_067'] = {'inputs': ['hcd_replacement_065'], 'func': hcd_replacement_d2_067}


def hcd_replacement_d2_068(hcd_replacement_066):
    feature = _clean(hcd_replacement_066)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_068'] = {'inputs': ['hcd_replacement_066'], 'func': hcd_replacement_d2_068}


def hcd_replacement_d2_069(hcd_replacement_067):
    feature = _clean(hcd_replacement_067)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_069'] = {'inputs': ['hcd_replacement_067'], 'func': hcd_replacement_d2_069}


def hcd_replacement_d2_070(hcd_replacement_068):
    feature = _clean(hcd_replacement_068)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_070'] = {'inputs': ['hcd_replacement_068'], 'func': hcd_replacement_d2_070}


def hcd_replacement_d2_071(hcd_replacement_069):
    feature = _clean(hcd_replacement_069)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_071'] = {'inputs': ['hcd_replacement_069'], 'func': hcd_replacement_d2_071}


def hcd_replacement_d2_072(hcd_replacement_070):
    feature = _clean(hcd_replacement_070)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_072'] = {'inputs': ['hcd_replacement_070'], 'func': hcd_replacement_d2_072}


def hcd_replacement_d2_073(hcd_replacement_071):
    feature = _clean(hcd_replacement_071)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_073'] = {'inputs': ['hcd_replacement_071'], 'func': hcd_replacement_d2_073}


def hcd_replacement_d2_074(hcd_replacement_072):
    feature = _clean(hcd_replacement_072)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_074'] = {'inputs': ['hcd_replacement_072'], 'func': hcd_replacement_d2_074}


def hcd_replacement_d2_075(hcd_replacement_073):
    feature = _clean(hcd_replacement_073)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_075'] = {'inputs': ['hcd_replacement_073'], 'func': hcd_replacement_d2_075}


def hcd_replacement_d2_076(hcd_replacement_074):
    feature = _clean(hcd_replacement_074)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_076'] = {'inputs': ['hcd_replacement_074'], 'func': hcd_replacement_d2_076}


def hcd_replacement_d2_077(hcd_replacement_075):
    feature = _clean(hcd_replacement_075)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_077'] = {'inputs': ['hcd_replacement_075'], 'func': hcd_replacement_d2_077}


def hcd_replacement_d2_078(hcd_replacement_076):
    feature = _clean(hcd_replacement_076)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_078'] = {'inputs': ['hcd_replacement_076'], 'func': hcd_replacement_d2_078}


def hcd_replacement_d2_079(hcd_replacement_077):
    feature = _clean(hcd_replacement_077)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_079'] = {'inputs': ['hcd_replacement_077'], 'func': hcd_replacement_d2_079}


def hcd_replacement_d2_080(hcd_replacement_078):
    feature = _clean(hcd_replacement_078)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_080'] = {'inputs': ['hcd_replacement_078'], 'func': hcd_replacement_d2_080}


def hcd_replacement_d2_081(hcd_replacement_079):
    feature = _clean(hcd_replacement_079)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_081'] = {'inputs': ['hcd_replacement_079'], 'func': hcd_replacement_d2_081}


def hcd_replacement_d2_082(hcd_replacement_080):
    feature = _clean(hcd_replacement_080)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_082'] = {'inputs': ['hcd_replacement_080'], 'func': hcd_replacement_d2_082}


def hcd_replacement_d2_083(hcd_replacement_081):
    feature = _clean(hcd_replacement_081)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_083'] = {'inputs': ['hcd_replacement_081'], 'func': hcd_replacement_d2_083}


def hcd_replacement_d2_084(hcd_replacement_082):
    feature = _clean(hcd_replacement_082)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_084'] = {'inputs': ['hcd_replacement_082'], 'func': hcd_replacement_d2_084}


def hcd_replacement_d2_085(hcd_replacement_083):
    feature = _clean(hcd_replacement_083)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_085'] = {'inputs': ['hcd_replacement_083'], 'func': hcd_replacement_d2_085}


def hcd_replacement_d2_086(hcd_replacement_084):
    feature = _clean(hcd_replacement_084)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_086'] = {'inputs': ['hcd_replacement_084'], 'func': hcd_replacement_d2_086}


def hcd_replacement_d2_087(hcd_replacement_085):
    feature = _clean(hcd_replacement_085)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_087'] = {'inputs': ['hcd_replacement_085'], 'func': hcd_replacement_d2_087}


def hcd_replacement_d2_088(hcd_replacement_086):
    feature = _clean(hcd_replacement_086)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_088'] = {'inputs': ['hcd_replacement_086'], 'func': hcd_replacement_d2_088}


def hcd_replacement_d2_089(hcd_replacement_087):
    feature = _clean(hcd_replacement_087)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_089'] = {'inputs': ['hcd_replacement_087'], 'func': hcd_replacement_d2_089}


def hcd_replacement_d2_090(hcd_replacement_088):
    feature = _clean(hcd_replacement_088)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_090'] = {'inputs': ['hcd_replacement_088'], 'func': hcd_replacement_d2_090}


def hcd_replacement_d2_091(hcd_replacement_089):
    feature = _clean(hcd_replacement_089)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_091'] = {'inputs': ['hcd_replacement_089'], 'func': hcd_replacement_d2_091}


def hcd_replacement_d2_092(hcd_replacement_090):
    feature = _clean(hcd_replacement_090)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_092'] = {'inputs': ['hcd_replacement_090'], 'func': hcd_replacement_d2_092}


def hcd_replacement_d2_093(hcd_replacement_091):
    feature = _clean(hcd_replacement_091)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_093'] = {'inputs': ['hcd_replacement_091'], 'func': hcd_replacement_d2_093}


def hcd_replacement_d2_094(hcd_replacement_092):
    feature = _clean(hcd_replacement_092)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_094'] = {'inputs': ['hcd_replacement_092'], 'func': hcd_replacement_d2_094}


def hcd_replacement_d2_095(hcd_replacement_093):
    feature = _clean(hcd_replacement_093)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_095'] = {'inputs': ['hcd_replacement_093'], 'func': hcd_replacement_d2_095}


def hcd_replacement_d2_096(hcd_replacement_094):
    feature = _clean(hcd_replacement_094)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_096'] = {'inputs': ['hcd_replacement_094'], 'func': hcd_replacement_d2_096}


def hcd_replacement_d2_097(hcd_replacement_095):
    feature = _clean(hcd_replacement_095)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_097'] = {'inputs': ['hcd_replacement_095'], 'func': hcd_replacement_d2_097}


def hcd_replacement_d2_098(hcd_replacement_096):
    feature = _clean(hcd_replacement_096)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_098'] = {'inputs': ['hcd_replacement_096'], 'func': hcd_replacement_d2_098}


def hcd_replacement_d2_099(hcd_replacement_097):
    feature = _clean(hcd_replacement_097)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_099'] = {'inputs': ['hcd_replacement_097'], 'func': hcd_replacement_d2_099}


def hcd_replacement_d2_100(hcd_replacement_098):
    feature = _clean(hcd_replacement_098)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_100'] = {'inputs': ['hcd_replacement_098'], 'func': hcd_replacement_d2_100}


def hcd_replacement_d2_101(hcd_replacement_099):
    feature = _clean(hcd_replacement_099)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_101'] = {'inputs': ['hcd_replacement_099'], 'func': hcd_replacement_d2_101}


def hcd_replacement_d2_102(hcd_replacement_100):
    feature = _clean(hcd_replacement_100)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_102'] = {'inputs': ['hcd_replacement_100'], 'func': hcd_replacement_d2_102}


def hcd_replacement_d2_103(hcd_replacement_101):
    feature = _clean(hcd_replacement_101)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_103'] = {'inputs': ['hcd_replacement_101'], 'func': hcd_replacement_d2_103}


def hcd_replacement_d2_104(hcd_replacement_102):
    feature = _clean(hcd_replacement_102)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_104'] = {'inputs': ['hcd_replacement_102'], 'func': hcd_replacement_d2_104}


def hcd_replacement_d2_105(hcd_replacement_103):
    feature = _clean(hcd_replacement_103)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_105'] = {'inputs': ['hcd_replacement_103'], 'func': hcd_replacement_d2_105}


def hcd_replacement_d2_106(hcd_replacement_104):
    feature = _clean(hcd_replacement_104)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_106'] = {'inputs': ['hcd_replacement_104'], 'func': hcd_replacement_d2_106}


def hcd_replacement_d2_107(hcd_replacement_105):
    feature = _clean(hcd_replacement_105)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_107'] = {'inputs': ['hcd_replacement_105'], 'func': hcd_replacement_d2_107}


def hcd_replacement_d2_108(hcd_replacement_106):
    feature = _clean(hcd_replacement_106)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_108'] = {'inputs': ['hcd_replacement_106'], 'func': hcd_replacement_d2_108}


def hcd_replacement_d2_109(hcd_replacement_107):
    feature = _clean(hcd_replacement_107)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_109'] = {'inputs': ['hcd_replacement_107'], 'func': hcd_replacement_d2_109}


def hcd_replacement_d2_110(hcd_replacement_108):
    feature = _clean(hcd_replacement_108)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_110'] = {'inputs': ['hcd_replacement_108'], 'func': hcd_replacement_d2_110}


def hcd_replacement_d2_111(hcd_replacement_109):
    feature = _clean(hcd_replacement_109)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_111'] = {'inputs': ['hcd_replacement_109'], 'func': hcd_replacement_d2_111}


def hcd_replacement_d2_112(hcd_replacement_110):
    feature = _clean(hcd_replacement_110)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_112'] = {'inputs': ['hcd_replacement_110'], 'func': hcd_replacement_d2_112}


def hcd_replacement_d2_113(hcd_replacement_111):
    feature = _clean(hcd_replacement_111)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_113'] = {'inputs': ['hcd_replacement_111'], 'func': hcd_replacement_d2_113}


def hcd_replacement_d2_114(hcd_replacement_112):
    feature = _clean(hcd_replacement_112)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_114'] = {'inputs': ['hcd_replacement_112'], 'func': hcd_replacement_d2_114}


def hcd_replacement_d2_115(hcd_replacement_113):
    feature = _clean(hcd_replacement_113)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_115'] = {'inputs': ['hcd_replacement_113'], 'func': hcd_replacement_d2_115}


def hcd_replacement_d2_116(hcd_replacement_114):
    feature = _clean(hcd_replacement_114)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_116'] = {'inputs': ['hcd_replacement_114'], 'func': hcd_replacement_d2_116}


def hcd_replacement_d2_117(hcd_replacement_115):
    feature = _clean(hcd_replacement_115)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_117'] = {'inputs': ['hcd_replacement_115'], 'func': hcd_replacement_d2_117}


def hcd_replacement_d2_118(hcd_replacement_116):
    feature = _clean(hcd_replacement_116)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_118'] = {'inputs': ['hcd_replacement_116'], 'func': hcd_replacement_d2_118}


def hcd_replacement_d2_119(hcd_replacement_117):
    feature = _clean(hcd_replacement_117)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_119'] = {'inputs': ['hcd_replacement_117'], 'func': hcd_replacement_d2_119}


def hcd_replacement_d2_120(hcd_replacement_118):
    feature = _clean(hcd_replacement_118)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_120'] = {'inputs': ['hcd_replacement_118'], 'func': hcd_replacement_d2_120}


def hcd_replacement_d2_121(hcd_replacement_119):
    feature = _clean(hcd_replacement_119)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_121'] = {'inputs': ['hcd_replacement_119'], 'func': hcd_replacement_d2_121}


def hcd_replacement_d2_122(hcd_replacement_120):
    feature = _clean(hcd_replacement_120)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_122'] = {'inputs': ['hcd_replacement_120'], 'func': hcd_replacement_d2_122}


def hcd_replacement_d2_123(hcd_replacement_121):
    feature = _clean(hcd_replacement_121)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_123'] = {'inputs': ['hcd_replacement_121'], 'func': hcd_replacement_d2_123}


def hcd_replacement_d2_124(hcd_replacement_122):
    feature = _clean(hcd_replacement_122)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_124'] = {'inputs': ['hcd_replacement_122'], 'func': hcd_replacement_d2_124}


def hcd_replacement_d2_125(hcd_replacement_123):
    feature = _clean(hcd_replacement_123)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_125'] = {'inputs': ['hcd_replacement_123'], 'func': hcd_replacement_d2_125}


def hcd_replacement_d2_126(hcd_replacement_124):
    feature = _clean(hcd_replacement_124)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_126'] = {'inputs': ['hcd_replacement_124'], 'func': hcd_replacement_d2_126}


def hcd_replacement_d2_127(hcd_replacement_125):
    feature = _clean(hcd_replacement_125)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_127'] = {'inputs': ['hcd_replacement_125'], 'func': hcd_replacement_d2_127}


def hcd_replacement_d2_128(hcd_replacement_126):
    feature = _clean(hcd_replacement_126)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_128'] = {'inputs': ['hcd_replacement_126'], 'func': hcd_replacement_d2_128}


def hcd_replacement_d2_129(hcd_replacement_127):
    feature = _clean(hcd_replacement_127)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_129'] = {'inputs': ['hcd_replacement_127'], 'func': hcd_replacement_d2_129}


def hcd_replacement_d2_130(hcd_replacement_128):
    feature = _clean(hcd_replacement_128)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_130'] = {'inputs': ['hcd_replacement_128'], 'func': hcd_replacement_d2_130}


def hcd_replacement_d2_131(hcd_replacement_129):
    feature = _clean(hcd_replacement_129)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_131'] = {'inputs': ['hcd_replacement_129'], 'func': hcd_replacement_d2_131}


def hcd_replacement_d2_132(hcd_replacement_130):
    feature = _clean(hcd_replacement_130)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_132'] = {'inputs': ['hcd_replacement_130'], 'func': hcd_replacement_d2_132}


def hcd_replacement_d2_133(hcd_replacement_131):
    feature = _clean(hcd_replacement_131)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_133'] = {'inputs': ['hcd_replacement_131'], 'func': hcd_replacement_d2_133}


def hcd_replacement_d2_134(hcd_replacement_132):
    feature = _clean(hcd_replacement_132)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_134'] = {'inputs': ['hcd_replacement_132'], 'func': hcd_replacement_d2_134}


def hcd_replacement_d2_135(hcd_replacement_133):
    feature = _clean(hcd_replacement_133)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_135'] = {'inputs': ['hcd_replacement_133'], 'func': hcd_replacement_d2_135}


def hcd_replacement_d2_136(hcd_replacement_134):
    feature = _clean(hcd_replacement_134)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_136'] = {'inputs': ['hcd_replacement_134'], 'func': hcd_replacement_d2_136}


def hcd_replacement_d2_137(hcd_replacement_135):
    feature = _clean(hcd_replacement_135)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_137'] = {'inputs': ['hcd_replacement_135'], 'func': hcd_replacement_d2_137}


def hcd_replacement_d2_138(hcd_replacement_136):
    feature = _clean(hcd_replacement_136)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_138'] = {'inputs': ['hcd_replacement_136'], 'func': hcd_replacement_d2_138}


def hcd_replacement_d2_139(hcd_replacement_137):
    feature = _clean(hcd_replacement_137)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_139'] = {'inputs': ['hcd_replacement_137'], 'func': hcd_replacement_d2_139}


def hcd_replacement_d2_140(hcd_replacement_138):
    feature = _clean(hcd_replacement_138)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_140'] = {'inputs': ['hcd_replacement_138'], 'func': hcd_replacement_d2_140}


def hcd_replacement_d2_141(hcd_replacement_139):
    feature = _clean(hcd_replacement_139)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_141'] = {'inputs': ['hcd_replacement_139'], 'func': hcd_replacement_d2_141}


def hcd_replacement_d2_142(hcd_replacement_140):
    feature = _clean(hcd_replacement_140)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_142'] = {'inputs': ['hcd_replacement_140'], 'func': hcd_replacement_d2_142}


def hcd_replacement_d2_143(hcd_replacement_141):
    feature = _clean(hcd_replacement_141)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_143'] = {'inputs': ['hcd_replacement_141'], 'func': hcd_replacement_d2_143}


def hcd_replacement_d2_144(hcd_replacement_142):
    feature = _clean(hcd_replacement_142)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_144'] = {'inputs': ['hcd_replacement_142'], 'func': hcd_replacement_d2_144}


def hcd_replacement_d2_145(hcd_replacement_143):
    feature = _clean(hcd_replacement_143)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_145'] = {'inputs': ['hcd_replacement_143'], 'func': hcd_replacement_d2_145}


def hcd_replacement_d2_146(hcd_replacement_144):
    feature = _clean(hcd_replacement_144)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_146'] = {'inputs': ['hcd_replacement_144'], 'func': hcd_replacement_d2_146}


def hcd_replacement_d2_147(hcd_replacement_145):
    feature = _clean(hcd_replacement_145)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_147'] = {'inputs': ['hcd_replacement_145'], 'func': hcd_replacement_d2_147}


def hcd_replacement_d2_148(hcd_replacement_146):
    feature = _clean(hcd_replacement_146)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_148'] = {'inputs': ['hcd_replacement_146'], 'func': hcd_replacement_d2_148}


def hcd_replacement_d2_149(hcd_replacement_147):
    feature = _clean(hcd_replacement_147)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_149'] = {'inputs': ['hcd_replacement_147'], 'func': hcd_replacement_d2_149}


def hcd_replacement_d2_150(hcd_replacement_148):
    feature = _clean(hcd_replacement_148)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_150'] = {'inputs': ['hcd_replacement_148'], 'func': hcd_replacement_d2_150}


def hcd_replacement_d2_151(hcd_replacement_149):
    feature = _clean(hcd_replacement_149)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_151'] = {'inputs': ['hcd_replacement_149'], 'func': hcd_replacement_d2_151}


def hcd_replacement_d2_152(hcd_replacement_150):
    feature = _clean(hcd_replacement_150)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_152'] = {'inputs': ['hcd_replacement_150'], 'func': hcd_replacement_d2_152}


def hcd_replacement_d2_153(hcd_replacement_151):
    feature = _clean(hcd_replacement_151)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_153'] = {'inputs': ['hcd_replacement_151'], 'func': hcd_replacement_d2_153}


def hcd_replacement_d2_154(hcd_replacement_152):
    feature = _clean(hcd_replacement_152)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_154'] = {'inputs': ['hcd_replacement_152'], 'func': hcd_replacement_d2_154}


def hcd_replacement_d2_155(hcd_replacement_153):
    feature = _clean(hcd_replacement_153)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_155'] = {'inputs': ['hcd_replacement_153'], 'func': hcd_replacement_d2_155}


def hcd_replacement_d2_156(hcd_replacement_154):
    feature = _clean(hcd_replacement_154)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_156'] = {'inputs': ['hcd_replacement_154'], 'func': hcd_replacement_d2_156}


def hcd_replacement_d2_157(hcd_replacement_155):
    feature = _clean(hcd_replacement_155)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_157'] = {'inputs': ['hcd_replacement_155'], 'func': hcd_replacement_d2_157}


def hcd_replacement_d2_158(hcd_replacement_156):
    feature = _clean(hcd_replacement_156)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_158'] = {'inputs': ['hcd_replacement_156'], 'func': hcd_replacement_d2_158}


def hcd_replacement_d2_159(hcd_replacement_157):
    feature = _clean(hcd_replacement_157)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_159'] = {'inputs': ['hcd_replacement_157'], 'func': hcd_replacement_d2_159}


def hcd_replacement_d2_160(hcd_replacement_158):
    feature = _clean(hcd_replacement_158)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_160'] = {'inputs': ['hcd_replacement_158'], 'func': hcd_replacement_d2_160}


def hcd_replacement_d2_161(hcd_replacement_159):
    feature = _clean(hcd_replacement_159)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_161'] = {'inputs': ['hcd_replacement_159'], 'func': hcd_replacement_d2_161}


def hcd_replacement_d2_162(hcd_replacement_160):
    feature = _clean(hcd_replacement_160)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_162'] = {'inputs': ['hcd_replacement_160'], 'func': hcd_replacement_d2_162}


def hcd_replacement_d2_163(hcd_replacement_161):
    feature = _clean(hcd_replacement_161)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_163'] = {'inputs': ['hcd_replacement_161'], 'func': hcd_replacement_d2_163}


def hcd_replacement_d2_164(hcd_replacement_162):
    feature = _clean(hcd_replacement_162)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_164'] = {'inputs': ['hcd_replacement_162'], 'func': hcd_replacement_d2_164}


def hcd_replacement_d2_165(hcd_replacement_163):
    feature = _clean(hcd_replacement_163)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_165'] = {'inputs': ['hcd_replacement_163'], 'func': hcd_replacement_d2_165}


def hcd_replacement_d2_166(hcd_replacement_164):
    feature = _clean(hcd_replacement_164)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_166'] = {'inputs': ['hcd_replacement_164'], 'func': hcd_replacement_d2_166}


def hcd_replacement_d2_167(hcd_replacement_165):
    feature = _clean(hcd_replacement_165)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_167'] = {'inputs': ['hcd_replacement_165'], 'func': hcd_replacement_d2_167}


def hcd_replacement_d2_168(hcd_replacement_166):
    feature = _clean(hcd_replacement_166)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_168'] = {'inputs': ['hcd_replacement_166'], 'func': hcd_replacement_d2_168}


def hcd_replacement_d2_169(hcd_replacement_167):
    feature = _clean(hcd_replacement_167)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_169'] = {'inputs': ['hcd_replacement_167'], 'func': hcd_replacement_d2_169}


def hcd_replacement_d2_170(hcd_replacement_168):
    feature = _clean(hcd_replacement_168)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_170'] = {'inputs': ['hcd_replacement_168'], 'func': hcd_replacement_d2_170}


def hcd_replacement_d2_171(hcd_replacement_169):
    feature = _clean(hcd_replacement_169)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_171'] = {'inputs': ['hcd_replacement_169'], 'func': hcd_replacement_d2_171}


def hcd_replacement_d2_172(hcd_replacement_170):
    feature = _clean(hcd_replacement_170)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_172'] = {'inputs': ['hcd_replacement_170'], 'func': hcd_replacement_d2_172}


def hcd_replacement_d2_173(hcd_replacement_171):
    feature = _clean(hcd_replacement_171)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_173'] = {'inputs': ['hcd_replacement_171'], 'func': hcd_replacement_d2_173}


def hcd_replacement_d2_174(hcd_replacement_172):
    feature = _clean(hcd_replacement_172)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_174'] = {'inputs': ['hcd_replacement_172'], 'func': hcd_replacement_d2_174}


def hcd_replacement_d2_175(hcd_replacement_173):
    feature = _clean(hcd_replacement_173)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_175'] = {'inputs': ['hcd_replacement_173'], 'func': hcd_replacement_d2_175}


def hcd_replacement_d2_176(hcd_replacement_174):
    feature = _clean(hcd_replacement_174)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00176000).reindex(feature.index)
HCD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['hcd_replacement_d2_176'] = {'inputs': ['hcd_replacement_174'], 'func': hcd_replacement_d2_176}


# Base-universe derivative extensions for repaired first-base features.
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63(hcd_003_holder_breadth_peer_z_63):
    return _base_universe_d2(hcd_003_holder_breadth_peer_z_63, 1)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63'] = {'inputs': ['hcd_003_holder_breadth_peer_z_63'], 'func': hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63}


def hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008(hcd_011_holder_breadth_peer_z_1008):
    return _base_universe_d2(hcd_011_holder_breadth_peer_z_1008, 2)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008'] = {'inputs': ['hcd_011_holder_breadth_peer_z_1008'], 'func': hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008}


def hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378(hcd_023_holder_breadth_peer_z_378):
    return _base_universe_d2(hcd_023_holder_breadth_peer_z_378, 3)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378'] = {'inputs': ['hcd_023_holder_breadth_peer_z_378'], 'func': hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378}


def hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260(hcd_027_holder_breadth_peer_z_1260):
    return _base_universe_d2(hcd_027_holder_breadth_peer_z_1260, 4)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260'] = {'inputs': ['hcd_027_holder_breadth_peer_z_1260'], 'func': hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260}


def hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21(hcd_031_holder_breadth_peer_z_21):
    return _base_universe_d2(hcd_031_holder_breadth_peer_z_21, 5)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21'] = {'inputs': ['hcd_031_holder_breadth_peer_z_21'], 'func': hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21}


def hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126(hcd_035_holder_breadth_peer_z_126):
    return _base_universe_d2(hcd_035_holder_breadth_peer_z_126, 6)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126'] = {'inputs': ['hcd_035_holder_breadth_peer_z_126'], 'func': hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126}


def hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504(hcd_039_holder_breadth_peer_z_504):
    return _base_universe_d2(hcd_039_holder_breadth_peer_z_504, 7)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504'] = {'inputs': ['hcd_039_holder_breadth_peer_z_504'], 'func': hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504}


def hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512(hcd_043_holder_breadth_peer_z_1512):
    return _base_universe_d2(hcd_043_holder_breadth_peer_z_1512, 8)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512'] = {'inputs': ['hcd_043_holder_breadth_peer_z_1512'], 'func': hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512}


def hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42(hcd_047_holder_breadth_peer_z_42):
    return _base_universe_d2(hcd_047_holder_breadth_peer_z_42, 9)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42'] = {'inputs': ['hcd_047_holder_breadth_peer_z_42'], 'func': hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42}


def hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189(hcd_051_holder_breadth_peer_z_189):
    return _base_universe_d2(hcd_051_holder_breadth_peer_z_189, 10)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189'] = {'inputs': ['hcd_051_holder_breadth_peer_z_189'], 'func': hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189}


def hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756(hcd_055_holder_breadth_peer_z_756):
    return _base_universe_d2(hcd_055_holder_breadth_peer_z_756, 11)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756'] = {'inputs': ['hcd_055_holder_breadth_peer_z_756'], 'func': hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756}


def hcd_base_universe_d2_012_hcd_basefill_002(hcd_basefill_002):
    return _base_universe_d2(hcd_basefill_002, 12)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_012_hcd_basefill_002'] = {'inputs': ['hcd_basefill_002'], 'func': hcd_base_universe_d2_012_hcd_basefill_002}


def hcd_base_universe_d2_013_hcd_basefill_004(hcd_basefill_004):
    return _base_universe_d2(hcd_basefill_004, 13)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_013_hcd_basefill_004'] = {'inputs': ['hcd_basefill_004'], 'func': hcd_base_universe_d2_013_hcd_basefill_004}


def hcd_base_universe_d2_014_hcd_basefill_005(hcd_basefill_005):
    return _base_universe_d2(hcd_basefill_005, 14)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_014_hcd_basefill_005'] = {'inputs': ['hcd_basefill_005'], 'func': hcd_base_universe_d2_014_hcd_basefill_005}


def hcd_base_universe_d2_015_hcd_basefill_006(hcd_basefill_006):
    return _base_universe_d2(hcd_basefill_006, 15)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_015_hcd_basefill_006'] = {'inputs': ['hcd_basefill_006'], 'func': hcd_base_universe_d2_015_hcd_basefill_006}


def hcd_base_universe_d2_016_hcd_basefill_008(hcd_basefill_008):
    return _base_universe_d2(hcd_basefill_008, 16)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_016_hcd_basefill_008'] = {'inputs': ['hcd_basefill_008'], 'func': hcd_base_universe_d2_016_hcd_basefill_008}


def hcd_base_universe_d2_017_hcd_basefill_009(hcd_basefill_009):
    return _base_universe_d2(hcd_basefill_009, 17)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_017_hcd_basefill_009'] = {'inputs': ['hcd_basefill_009'], 'func': hcd_base_universe_d2_017_hcd_basefill_009}


def hcd_base_universe_d2_018_hcd_basefill_010(hcd_basefill_010):
    return _base_universe_d2(hcd_basefill_010, 18)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_018_hcd_basefill_010'] = {'inputs': ['hcd_basefill_010'], 'func': hcd_base_universe_d2_018_hcd_basefill_010}


def hcd_base_universe_d2_019_hcd_basefill_012(hcd_basefill_012):
    return _base_universe_d2(hcd_basefill_012, 19)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_019_hcd_basefill_012'] = {'inputs': ['hcd_basefill_012'], 'func': hcd_base_universe_d2_019_hcd_basefill_012}


def hcd_base_universe_d2_020_hcd_basefill_013(hcd_basefill_013):
    return _base_universe_d2(hcd_basefill_013, 20)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_020_hcd_basefill_013'] = {'inputs': ['hcd_basefill_013'], 'func': hcd_base_universe_d2_020_hcd_basefill_013}


def hcd_base_universe_d2_021_hcd_basefill_014(hcd_basefill_014):
    return _base_universe_d2(hcd_basefill_014, 21)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_021_hcd_basefill_014'] = {'inputs': ['hcd_basefill_014'], 'func': hcd_base_universe_d2_021_hcd_basefill_014}


def hcd_base_universe_d2_022_hcd_basefill_015(hcd_basefill_015):
    return _base_universe_d2(hcd_basefill_015, 22)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_022_hcd_basefill_015'] = {'inputs': ['hcd_basefill_015'], 'func': hcd_base_universe_d2_022_hcd_basefill_015}


def hcd_base_universe_d2_023_hcd_basefill_016(hcd_basefill_016):
    return _base_universe_d2(hcd_basefill_016, 23)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_023_hcd_basefill_016'] = {'inputs': ['hcd_basefill_016'], 'func': hcd_base_universe_d2_023_hcd_basefill_016}


def hcd_base_universe_d2_024_hcd_basefill_017(hcd_basefill_017):
    return _base_universe_d2(hcd_basefill_017, 24)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_024_hcd_basefill_017'] = {'inputs': ['hcd_basefill_017'], 'func': hcd_base_universe_d2_024_hcd_basefill_017}


def hcd_base_universe_d2_025_hcd_basefill_018(hcd_basefill_018):
    return _base_universe_d2(hcd_basefill_018, 25)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_025_hcd_basefill_018'] = {'inputs': ['hcd_basefill_018'], 'func': hcd_base_universe_d2_025_hcd_basefill_018}


def hcd_base_universe_d2_026_hcd_basefill_020(hcd_basefill_020):
    return _base_universe_d2(hcd_basefill_020, 26)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_026_hcd_basefill_020'] = {'inputs': ['hcd_basefill_020'], 'func': hcd_base_universe_d2_026_hcd_basefill_020}


def hcd_base_universe_d2_027_hcd_basefill_021(hcd_basefill_021):
    return _base_universe_d2(hcd_basefill_021, 27)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_027_hcd_basefill_021'] = {'inputs': ['hcd_basefill_021'], 'func': hcd_base_universe_d2_027_hcd_basefill_021}


def hcd_base_universe_d2_028_hcd_basefill_022(hcd_basefill_022):
    return _base_universe_d2(hcd_basefill_022, 28)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_028_hcd_basefill_022'] = {'inputs': ['hcd_basefill_022'], 'func': hcd_base_universe_d2_028_hcd_basefill_022}


def hcd_base_universe_d2_029_hcd_basefill_024(hcd_basefill_024):
    return _base_universe_d2(hcd_basefill_024, 29)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_029_hcd_basefill_024'] = {'inputs': ['hcd_basefill_024'], 'func': hcd_base_universe_d2_029_hcd_basefill_024}


def hcd_base_universe_d2_030_hcd_basefill_025(hcd_basefill_025):
    return _base_universe_d2(hcd_basefill_025, 30)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_030_hcd_basefill_025'] = {'inputs': ['hcd_basefill_025'], 'func': hcd_base_universe_d2_030_hcd_basefill_025}


def hcd_base_universe_d2_031_hcd_basefill_026(hcd_basefill_026):
    return _base_universe_d2(hcd_basefill_026, 31)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_031_hcd_basefill_026'] = {'inputs': ['hcd_basefill_026'], 'func': hcd_base_universe_d2_031_hcd_basefill_026}


def hcd_base_universe_d2_032_hcd_basefill_028(hcd_basefill_028):
    return _base_universe_d2(hcd_basefill_028, 32)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_032_hcd_basefill_028'] = {'inputs': ['hcd_basefill_028'], 'func': hcd_base_universe_d2_032_hcd_basefill_028}


def hcd_base_universe_d2_033_hcd_basefill_029(hcd_basefill_029):
    return _base_universe_d2(hcd_basefill_029, 33)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_033_hcd_basefill_029'] = {'inputs': ['hcd_basefill_029'], 'func': hcd_base_universe_d2_033_hcd_basefill_029}


def hcd_base_universe_d2_034_hcd_basefill_030(hcd_basefill_030):
    return _base_universe_d2(hcd_basefill_030, 34)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_034_hcd_basefill_030'] = {'inputs': ['hcd_basefill_030'], 'func': hcd_base_universe_d2_034_hcd_basefill_030}


def hcd_base_universe_d2_035_hcd_basefill_032(hcd_basefill_032):
    return _base_universe_d2(hcd_basefill_032, 35)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_035_hcd_basefill_032'] = {'inputs': ['hcd_basefill_032'], 'func': hcd_base_universe_d2_035_hcd_basefill_032}


def hcd_base_universe_d2_036_hcd_basefill_033(hcd_basefill_033):
    return _base_universe_d2(hcd_basefill_033, 36)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_036_hcd_basefill_033'] = {'inputs': ['hcd_basefill_033'], 'func': hcd_base_universe_d2_036_hcd_basefill_033}


def hcd_base_universe_d2_037_hcd_basefill_034(hcd_basefill_034):
    return _base_universe_d2(hcd_basefill_034, 37)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_037_hcd_basefill_034'] = {'inputs': ['hcd_basefill_034'], 'func': hcd_base_universe_d2_037_hcd_basefill_034}


def hcd_base_universe_d2_038_hcd_basefill_036(hcd_basefill_036):
    return _base_universe_d2(hcd_basefill_036, 38)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_038_hcd_basefill_036'] = {'inputs': ['hcd_basefill_036'], 'func': hcd_base_universe_d2_038_hcd_basefill_036}


def hcd_base_universe_d2_039_hcd_basefill_037(hcd_basefill_037):
    return _base_universe_d2(hcd_basefill_037, 39)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_039_hcd_basefill_037'] = {'inputs': ['hcd_basefill_037'], 'func': hcd_base_universe_d2_039_hcd_basefill_037}


def hcd_base_universe_d2_040_hcd_basefill_038(hcd_basefill_038):
    return _base_universe_d2(hcd_basefill_038, 40)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_040_hcd_basefill_038'] = {'inputs': ['hcd_basefill_038'], 'func': hcd_base_universe_d2_040_hcd_basefill_038}


def hcd_base_universe_d2_041_hcd_basefill_040(hcd_basefill_040):
    return _base_universe_d2(hcd_basefill_040, 41)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_041_hcd_basefill_040'] = {'inputs': ['hcd_basefill_040'], 'func': hcd_base_universe_d2_041_hcd_basefill_040}


def hcd_base_universe_d2_042_hcd_basefill_041(hcd_basefill_041):
    return _base_universe_d2(hcd_basefill_041, 42)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_042_hcd_basefill_041'] = {'inputs': ['hcd_basefill_041'], 'func': hcd_base_universe_d2_042_hcd_basefill_041}


def hcd_base_universe_d2_043_hcd_basefill_042(hcd_basefill_042):
    return _base_universe_d2(hcd_basefill_042, 43)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_043_hcd_basefill_042'] = {'inputs': ['hcd_basefill_042'], 'func': hcd_base_universe_d2_043_hcd_basefill_042}


def hcd_base_universe_d2_044_hcd_basefill_044(hcd_basefill_044):
    return _base_universe_d2(hcd_basefill_044, 44)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_044_hcd_basefill_044'] = {'inputs': ['hcd_basefill_044'], 'func': hcd_base_universe_d2_044_hcd_basefill_044}


def hcd_base_universe_d2_045_hcd_basefill_045(hcd_basefill_045):
    return _base_universe_d2(hcd_basefill_045, 45)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_045_hcd_basefill_045'] = {'inputs': ['hcd_basefill_045'], 'func': hcd_base_universe_d2_045_hcd_basefill_045}


def hcd_base_universe_d2_046_hcd_basefill_046(hcd_basefill_046):
    return _base_universe_d2(hcd_basefill_046, 46)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_046_hcd_basefill_046'] = {'inputs': ['hcd_basefill_046'], 'func': hcd_base_universe_d2_046_hcd_basefill_046}


def hcd_base_universe_d2_047_hcd_basefill_048(hcd_basefill_048):
    return _base_universe_d2(hcd_basefill_048, 47)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_047_hcd_basefill_048'] = {'inputs': ['hcd_basefill_048'], 'func': hcd_base_universe_d2_047_hcd_basefill_048}


def hcd_base_universe_d2_048_hcd_basefill_049(hcd_basefill_049):
    return _base_universe_d2(hcd_basefill_049, 48)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_048_hcd_basefill_049'] = {'inputs': ['hcd_basefill_049'], 'func': hcd_base_universe_d2_048_hcd_basefill_049}


def hcd_base_universe_d2_049_hcd_basefill_050(hcd_basefill_050):
    return _base_universe_d2(hcd_basefill_050, 49)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_049_hcd_basefill_050'] = {'inputs': ['hcd_basefill_050'], 'func': hcd_base_universe_d2_049_hcd_basefill_050}


def hcd_base_universe_d2_050_hcd_basefill_052(hcd_basefill_052):
    return _base_universe_d2(hcd_basefill_052, 50)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_050_hcd_basefill_052'] = {'inputs': ['hcd_basefill_052'], 'func': hcd_base_universe_d2_050_hcd_basefill_052}


def hcd_base_universe_d2_051_hcd_basefill_053(hcd_basefill_053):
    return _base_universe_d2(hcd_basefill_053, 51)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_051_hcd_basefill_053'] = {'inputs': ['hcd_basefill_053'], 'func': hcd_base_universe_d2_051_hcd_basefill_053}


def hcd_base_universe_d2_052_hcd_basefill_054(hcd_basefill_054):
    return _base_universe_d2(hcd_basefill_054, 52)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_052_hcd_basefill_054'] = {'inputs': ['hcd_basefill_054'], 'func': hcd_base_universe_d2_052_hcd_basefill_054}


def hcd_base_universe_d2_053_hcd_basefill_056(hcd_basefill_056):
    return _base_universe_d2(hcd_basefill_056, 53)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_053_hcd_basefill_056'] = {'inputs': ['hcd_basefill_056'], 'func': hcd_base_universe_d2_053_hcd_basefill_056}


def hcd_base_universe_d2_054_hcd_basefill_057(hcd_basefill_057):
    return _base_universe_d2(hcd_basefill_057, 54)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_054_hcd_basefill_057'] = {'inputs': ['hcd_basefill_057'], 'func': hcd_base_universe_d2_054_hcd_basefill_057}


def hcd_base_universe_d2_055_hcd_basefill_058(hcd_basefill_058):
    return _base_universe_d2(hcd_basefill_058, 55)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_055_hcd_basefill_058'] = {'inputs': ['hcd_basefill_058'], 'func': hcd_base_universe_d2_055_hcd_basefill_058}


def hcd_base_universe_d2_056_hcd_basefill_059(hcd_basefill_059):
    return _base_universe_d2(hcd_basefill_059, 56)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_056_hcd_basefill_059'] = {'inputs': ['hcd_basefill_059'], 'func': hcd_base_universe_d2_056_hcd_basefill_059}


def hcd_base_universe_d2_057_hcd_basefill_060(hcd_basefill_060):
    return _base_universe_d2(hcd_basefill_060, 57)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_057_hcd_basefill_060'] = {'inputs': ['hcd_basefill_060'], 'func': hcd_base_universe_d2_057_hcd_basefill_060}


def hcd_base_universe_d2_058_hcd_basefill_061(hcd_basefill_061):
    return _base_universe_d2(hcd_basefill_061, 58)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_058_hcd_basefill_061'] = {'inputs': ['hcd_basefill_061'], 'func': hcd_base_universe_d2_058_hcd_basefill_061}


def hcd_base_universe_d2_059_hcd_basefill_062(hcd_basefill_062):
    return _base_universe_d2(hcd_basefill_062, 59)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_059_hcd_basefill_062'] = {'inputs': ['hcd_basefill_062'], 'func': hcd_base_universe_d2_059_hcd_basefill_062}


def hcd_base_universe_d2_060_hcd_basefill_063(hcd_basefill_063):
    return _base_universe_d2(hcd_basefill_063, 60)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_060_hcd_basefill_063'] = {'inputs': ['hcd_basefill_063'], 'func': hcd_base_universe_d2_060_hcd_basefill_063}


def hcd_base_universe_d2_061_hcd_basefill_064(hcd_basefill_064):
    return _base_universe_d2(hcd_basefill_064, 61)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_061_hcd_basefill_064'] = {'inputs': ['hcd_basefill_064'], 'func': hcd_base_universe_d2_061_hcd_basefill_064}


def hcd_base_universe_d2_062_hcd_basefill_065(hcd_basefill_065):
    return _base_universe_d2(hcd_basefill_065, 62)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_062_hcd_basefill_065'] = {'inputs': ['hcd_basefill_065'], 'func': hcd_base_universe_d2_062_hcd_basefill_065}


def hcd_base_universe_d2_063_hcd_basefill_066(hcd_basefill_066):
    return _base_universe_d2(hcd_basefill_066, 63)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_063_hcd_basefill_066'] = {'inputs': ['hcd_basefill_066'], 'func': hcd_base_universe_d2_063_hcd_basefill_066}


def hcd_base_universe_d2_064_hcd_basefill_067(hcd_basefill_067):
    return _base_universe_d2(hcd_basefill_067, 64)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_064_hcd_basefill_067'] = {'inputs': ['hcd_basefill_067'], 'func': hcd_base_universe_d2_064_hcd_basefill_067}


def hcd_base_universe_d2_065_hcd_basefill_068(hcd_basefill_068):
    return _base_universe_d2(hcd_basefill_068, 65)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_065_hcd_basefill_068'] = {'inputs': ['hcd_basefill_068'], 'func': hcd_base_universe_d2_065_hcd_basefill_068}


def hcd_base_universe_d2_066_hcd_basefill_069(hcd_basefill_069):
    return _base_universe_d2(hcd_basefill_069, 66)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_066_hcd_basefill_069'] = {'inputs': ['hcd_basefill_069'], 'func': hcd_base_universe_d2_066_hcd_basefill_069}


def hcd_base_universe_d2_067_hcd_basefill_070(hcd_basefill_070):
    return _base_universe_d2(hcd_basefill_070, 67)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_067_hcd_basefill_070'] = {'inputs': ['hcd_basefill_070'], 'func': hcd_base_universe_d2_067_hcd_basefill_070}


def hcd_base_universe_d2_068_hcd_basefill_071(hcd_basefill_071):
    return _base_universe_d2(hcd_basefill_071, 68)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_068_hcd_basefill_071'] = {'inputs': ['hcd_basefill_071'], 'func': hcd_base_universe_d2_068_hcd_basefill_071}


def hcd_base_universe_d2_069_hcd_basefill_072(hcd_basefill_072):
    return _base_universe_d2(hcd_basefill_072, 69)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_069_hcd_basefill_072'] = {'inputs': ['hcd_basefill_072'], 'func': hcd_base_universe_d2_069_hcd_basefill_072}


def hcd_base_universe_d2_070_hcd_basefill_073(hcd_basefill_073):
    return _base_universe_d2(hcd_basefill_073, 70)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_070_hcd_basefill_073'] = {'inputs': ['hcd_basefill_073'], 'func': hcd_base_universe_d2_070_hcd_basefill_073}


def hcd_base_universe_d2_071_hcd_basefill_074(hcd_basefill_074):
    return _base_universe_d2(hcd_basefill_074, 71)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_071_hcd_basefill_074'] = {'inputs': ['hcd_basefill_074'], 'func': hcd_base_universe_d2_071_hcd_basefill_074}


def hcd_base_universe_d2_072_hcd_basefill_075(hcd_basefill_075):
    return _base_universe_d2(hcd_basefill_075, 72)
HCD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['hcd_base_universe_d2_072_hcd_basefill_075'] = {'inputs': ['hcd_basefill_075'], 'func': hcd_base_universe_d2_072_hcd_basefill_075}
