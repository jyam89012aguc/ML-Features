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



def hcd_176_hcd_001_holder_count_vs_peer_21_accel_1(hcd_151_hcd_001_holder_count_vs_peer_21_roc_1):
    feature = _s(hcd_151_hcd_001_holder_count_vs_peer_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def hcd_177_hcd_007_holder_breadth_peer_z_252_accel_42(hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42):
    feature = _s(hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def hcd_178_hcd_013_holder_count_vs_peer_1512_accel_126(hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126):
    feature = _s(hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def hcd_179_hcd_019_holder_breadth_peer_z_84_accel_378(hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378):
    feature = _s(hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def hcd_180_hcd_025_holder_count_vs_peer_756_accel_4(hcd_155_hcd_025_holder_count_vs_peer_756_roc_4):
    feature = _s(hcd_155_hcd_025_holder_count_vs_peer_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















HOLDER_COUNT_DYNAMICS_REGISTRY_3RD_DERIVATIVES = {
    'hcd_176_hcd_001_holder_count_vs_peer_21_accel_1': {'inputs': ['hcd_151_hcd_001_holder_count_vs_peer_21_roc_1'], 'func': hcd_176_hcd_001_holder_count_vs_peer_21_accel_1},
    'hcd_177_hcd_007_holder_breadth_peer_z_252_accel_42': {'inputs': ['hcd_152_hcd_007_holder_breadth_peer_z_252_roc_42'], 'func': hcd_177_hcd_007_holder_breadth_peer_z_252_accel_42},
    'hcd_178_hcd_013_holder_count_vs_peer_1512_accel_126': {'inputs': ['hcd_153_hcd_013_holder_count_vs_peer_1512_roc_126'], 'func': hcd_178_hcd_013_holder_count_vs_peer_1512_accel_126},
    'hcd_179_hcd_019_holder_breadth_peer_z_84_accel_378': {'inputs': ['hcd_154_hcd_019_holder_breadth_peer_z_84_roc_378'], 'func': hcd_179_hcd_019_holder_breadth_peer_z_84_accel_378},
    'hcd_180_hcd_025_holder_count_vs_peer_756_accel_4': {'inputs': ['hcd_155_hcd_025_holder_count_vs_peer_756_roc_4'], 'func': hcd_180_hcd_025_holder_count_vs_peer_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def hcd_replacement_d3_001(hcd_replacement_d2_001):
    feature = _clean(hcd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_001'] = {'inputs': ['hcd_replacement_d2_001'], 'func': hcd_replacement_d3_001}


def hcd_replacement_d3_002(hcd_replacement_d2_002):
    feature = _clean(hcd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_002'] = {'inputs': ['hcd_replacement_d2_002'], 'func': hcd_replacement_d3_002}


def hcd_replacement_d3_003(hcd_replacement_d2_003):
    feature = _clean(hcd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_003'] = {'inputs': ['hcd_replacement_d2_003'], 'func': hcd_replacement_d3_003}


def hcd_replacement_d3_004(hcd_replacement_d2_004):
    feature = _clean(hcd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_004'] = {'inputs': ['hcd_replacement_d2_004'], 'func': hcd_replacement_d3_004}


def hcd_replacement_d3_005(hcd_replacement_d2_005):
    feature = _clean(hcd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_005'] = {'inputs': ['hcd_replacement_d2_005'], 'func': hcd_replacement_d3_005}


def hcd_replacement_d3_006(hcd_replacement_d2_006):
    feature = _clean(hcd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_006'] = {'inputs': ['hcd_replacement_d2_006'], 'func': hcd_replacement_d3_006}


def hcd_replacement_d3_007(hcd_replacement_d2_007):
    feature = _clean(hcd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_007'] = {'inputs': ['hcd_replacement_d2_007'], 'func': hcd_replacement_d3_007}


def hcd_replacement_d3_008(hcd_replacement_d2_008):
    feature = _clean(hcd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_008'] = {'inputs': ['hcd_replacement_d2_008'], 'func': hcd_replacement_d3_008}


def hcd_replacement_d3_009(hcd_replacement_d2_009):
    feature = _clean(hcd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_009'] = {'inputs': ['hcd_replacement_d2_009'], 'func': hcd_replacement_d3_009}


def hcd_replacement_d3_010(hcd_replacement_d2_010):
    feature = _clean(hcd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_010'] = {'inputs': ['hcd_replacement_d2_010'], 'func': hcd_replacement_d3_010}


def hcd_replacement_d3_011(hcd_replacement_d2_011):
    feature = _clean(hcd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_011'] = {'inputs': ['hcd_replacement_d2_011'], 'func': hcd_replacement_d3_011}


def hcd_replacement_d3_012(hcd_replacement_d2_012):
    feature = _clean(hcd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_012'] = {'inputs': ['hcd_replacement_d2_012'], 'func': hcd_replacement_d3_012}


def hcd_replacement_d3_013(hcd_replacement_d2_013):
    feature = _clean(hcd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_013'] = {'inputs': ['hcd_replacement_d2_013'], 'func': hcd_replacement_d3_013}


def hcd_replacement_d3_014(hcd_replacement_d2_014):
    feature = _clean(hcd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_014'] = {'inputs': ['hcd_replacement_d2_014'], 'func': hcd_replacement_d3_014}


def hcd_replacement_d3_015(hcd_replacement_d2_015):
    feature = _clean(hcd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_015'] = {'inputs': ['hcd_replacement_d2_015'], 'func': hcd_replacement_d3_015}


def hcd_replacement_d3_016(hcd_replacement_d2_016):
    feature = _clean(hcd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_016'] = {'inputs': ['hcd_replacement_d2_016'], 'func': hcd_replacement_d3_016}


def hcd_replacement_d3_017(hcd_replacement_d2_017):
    feature = _clean(hcd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_017'] = {'inputs': ['hcd_replacement_d2_017'], 'func': hcd_replacement_d3_017}


def hcd_replacement_d3_018(hcd_replacement_d2_018):
    feature = _clean(hcd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_018'] = {'inputs': ['hcd_replacement_d2_018'], 'func': hcd_replacement_d3_018}


def hcd_replacement_d3_019(hcd_replacement_d2_019):
    feature = _clean(hcd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_019'] = {'inputs': ['hcd_replacement_d2_019'], 'func': hcd_replacement_d3_019}


def hcd_replacement_d3_020(hcd_replacement_d2_020):
    feature = _clean(hcd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_020'] = {'inputs': ['hcd_replacement_d2_020'], 'func': hcd_replacement_d3_020}


def hcd_replacement_d3_021(hcd_replacement_d2_021):
    feature = _clean(hcd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_021'] = {'inputs': ['hcd_replacement_d2_021'], 'func': hcd_replacement_d3_021}


def hcd_replacement_d3_022(hcd_replacement_d2_022):
    feature = _clean(hcd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_022'] = {'inputs': ['hcd_replacement_d2_022'], 'func': hcd_replacement_d3_022}


def hcd_replacement_d3_023(hcd_replacement_d2_023):
    feature = _clean(hcd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_023'] = {'inputs': ['hcd_replacement_d2_023'], 'func': hcd_replacement_d3_023}


def hcd_replacement_d3_024(hcd_replacement_d2_024):
    feature = _clean(hcd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_024'] = {'inputs': ['hcd_replacement_d2_024'], 'func': hcd_replacement_d3_024}


def hcd_replacement_d3_025(hcd_replacement_d2_025):
    feature = _clean(hcd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_025'] = {'inputs': ['hcd_replacement_d2_025'], 'func': hcd_replacement_d3_025}


def hcd_replacement_d3_026(hcd_replacement_d2_026):
    feature = _clean(hcd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_026'] = {'inputs': ['hcd_replacement_d2_026'], 'func': hcd_replacement_d3_026}


def hcd_replacement_d3_027(hcd_replacement_d2_027):
    feature = _clean(hcd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_027'] = {'inputs': ['hcd_replacement_d2_027'], 'func': hcd_replacement_d3_027}


def hcd_replacement_d3_028(hcd_replacement_d2_028):
    feature = _clean(hcd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_028'] = {'inputs': ['hcd_replacement_d2_028'], 'func': hcd_replacement_d3_028}


def hcd_replacement_d3_029(hcd_replacement_d2_029):
    feature = _clean(hcd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_029'] = {'inputs': ['hcd_replacement_d2_029'], 'func': hcd_replacement_d3_029}


def hcd_replacement_d3_030(hcd_replacement_d2_030):
    feature = _clean(hcd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_030'] = {'inputs': ['hcd_replacement_d2_030'], 'func': hcd_replacement_d3_030}


def hcd_replacement_d3_031(hcd_replacement_d2_031):
    feature = _clean(hcd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_031'] = {'inputs': ['hcd_replacement_d2_031'], 'func': hcd_replacement_d3_031}


def hcd_replacement_d3_032(hcd_replacement_d2_032):
    feature = _clean(hcd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_032'] = {'inputs': ['hcd_replacement_d2_032'], 'func': hcd_replacement_d3_032}


def hcd_replacement_d3_033(hcd_replacement_d2_033):
    feature = _clean(hcd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_033'] = {'inputs': ['hcd_replacement_d2_033'], 'func': hcd_replacement_d3_033}


def hcd_replacement_d3_034(hcd_replacement_d2_034):
    feature = _clean(hcd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_034'] = {'inputs': ['hcd_replacement_d2_034'], 'func': hcd_replacement_d3_034}


def hcd_replacement_d3_035(hcd_replacement_d2_035):
    feature = _clean(hcd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_035'] = {'inputs': ['hcd_replacement_d2_035'], 'func': hcd_replacement_d3_035}


def hcd_replacement_d3_036(hcd_replacement_d2_036):
    feature = _clean(hcd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_036'] = {'inputs': ['hcd_replacement_d2_036'], 'func': hcd_replacement_d3_036}


def hcd_replacement_d3_037(hcd_replacement_d2_037):
    feature = _clean(hcd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_037'] = {'inputs': ['hcd_replacement_d2_037'], 'func': hcd_replacement_d3_037}


def hcd_replacement_d3_038(hcd_replacement_d2_038):
    feature = _clean(hcd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_038'] = {'inputs': ['hcd_replacement_d2_038'], 'func': hcd_replacement_d3_038}


def hcd_replacement_d3_039(hcd_replacement_d2_039):
    feature = _clean(hcd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_039'] = {'inputs': ['hcd_replacement_d2_039'], 'func': hcd_replacement_d3_039}


def hcd_replacement_d3_040(hcd_replacement_d2_040):
    feature = _clean(hcd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_040'] = {'inputs': ['hcd_replacement_d2_040'], 'func': hcd_replacement_d3_040}


def hcd_replacement_d3_041(hcd_replacement_d2_041):
    feature = _clean(hcd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_041'] = {'inputs': ['hcd_replacement_d2_041'], 'func': hcd_replacement_d3_041}


def hcd_replacement_d3_042(hcd_replacement_d2_042):
    feature = _clean(hcd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_042'] = {'inputs': ['hcd_replacement_d2_042'], 'func': hcd_replacement_d3_042}


def hcd_replacement_d3_043(hcd_replacement_d2_043):
    feature = _clean(hcd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_043'] = {'inputs': ['hcd_replacement_d2_043'], 'func': hcd_replacement_d3_043}


def hcd_replacement_d3_044(hcd_replacement_d2_044):
    feature = _clean(hcd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_044'] = {'inputs': ['hcd_replacement_d2_044'], 'func': hcd_replacement_d3_044}


def hcd_replacement_d3_045(hcd_replacement_d2_045):
    feature = _clean(hcd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_045'] = {'inputs': ['hcd_replacement_d2_045'], 'func': hcd_replacement_d3_045}


def hcd_replacement_d3_046(hcd_replacement_d2_046):
    feature = _clean(hcd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_046'] = {'inputs': ['hcd_replacement_d2_046'], 'func': hcd_replacement_d3_046}


def hcd_replacement_d3_047(hcd_replacement_d2_047):
    feature = _clean(hcd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_047'] = {'inputs': ['hcd_replacement_d2_047'], 'func': hcd_replacement_d3_047}


def hcd_replacement_d3_048(hcd_replacement_d2_048):
    feature = _clean(hcd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_048'] = {'inputs': ['hcd_replacement_d2_048'], 'func': hcd_replacement_d3_048}


def hcd_replacement_d3_049(hcd_replacement_d2_049):
    feature = _clean(hcd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_049'] = {'inputs': ['hcd_replacement_d2_049'], 'func': hcd_replacement_d3_049}


def hcd_replacement_d3_050(hcd_replacement_d2_050):
    feature = _clean(hcd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_050'] = {'inputs': ['hcd_replacement_d2_050'], 'func': hcd_replacement_d3_050}


def hcd_replacement_d3_051(hcd_replacement_d2_051):
    feature = _clean(hcd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_051'] = {'inputs': ['hcd_replacement_d2_051'], 'func': hcd_replacement_d3_051}


def hcd_replacement_d3_052(hcd_replacement_d2_052):
    feature = _clean(hcd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_052'] = {'inputs': ['hcd_replacement_d2_052'], 'func': hcd_replacement_d3_052}


def hcd_replacement_d3_053(hcd_replacement_d2_053):
    feature = _clean(hcd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_053'] = {'inputs': ['hcd_replacement_d2_053'], 'func': hcd_replacement_d3_053}


def hcd_replacement_d3_054(hcd_replacement_d2_054):
    feature = _clean(hcd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_054'] = {'inputs': ['hcd_replacement_d2_054'], 'func': hcd_replacement_d3_054}


def hcd_replacement_d3_055(hcd_replacement_d2_055):
    feature = _clean(hcd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_055'] = {'inputs': ['hcd_replacement_d2_055'], 'func': hcd_replacement_d3_055}


def hcd_replacement_d3_056(hcd_replacement_d2_056):
    feature = _clean(hcd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_056'] = {'inputs': ['hcd_replacement_d2_056'], 'func': hcd_replacement_d3_056}


def hcd_replacement_d3_057(hcd_replacement_d2_057):
    feature = _clean(hcd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_057'] = {'inputs': ['hcd_replacement_d2_057'], 'func': hcd_replacement_d3_057}


def hcd_replacement_d3_058(hcd_replacement_d2_058):
    feature = _clean(hcd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_058'] = {'inputs': ['hcd_replacement_d2_058'], 'func': hcd_replacement_d3_058}


def hcd_replacement_d3_059(hcd_replacement_d2_059):
    feature = _clean(hcd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_059'] = {'inputs': ['hcd_replacement_d2_059'], 'func': hcd_replacement_d3_059}


def hcd_replacement_d3_060(hcd_replacement_d2_060):
    feature = _clean(hcd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_060'] = {'inputs': ['hcd_replacement_d2_060'], 'func': hcd_replacement_d3_060}


def hcd_replacement_d3_061(hcd_replacement_d2_061):
    feature = _clean(hcd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_061'] = {'inputs': ['hcd_replacement_d2_061'], 'func': hcd_replacement_d3_061}


def hcd_replacement_d3_062(hcd_replacement_d2_062):
    feature = _clean(hcd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_062'] = {'inputs': ['hcd_replacement_d2_062'], 'func': hcd_replacement_d3_062}


def hcd_replacement_d3_063(hcd_replacement_d2_063):
    feature = _clean(hcd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_063'] = {'inputs': ['hcd_replacement_d2_063'], 'func': hcd_replacement_d3_063}


def hcd_replacement_d3_064(hcd_replacement_d2_064):
    feature = _clean(hcd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_064'] = {'inputs': ['hcd_replacement_d2_064'], 'func': hcd_replacement_d3_064}


def hcd_replacement_d3_065(hcd_replacement_d2_065):
    feature = _clean(hcd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_065'] = {'inputs': ['hcd_replacement_d2_065'], 'func': hcd_replacement_d3_065}


def hcd_replacement_d3_066(hcd_replacement_d2_066):
    feature = _clean(hcd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_066'] = {'inputs': ['hcd_replacement_d2_066'], 'func': hcd_replacement_d3_066}


def hcd_replacement_d3_067(hcd_replacement_d2_067):
    feature = _clean(hcd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_067'] = {'inputs': ['hcd_replacement_d2_067'], 'func': hcd_replacement_d3_067}


def hcd_replacement_d3_068(hcd_replacement_d2_068):
    feature = _clean(hcd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_068'] = {'inputs': ['hcd_replacement_d2_068'], 'func': hcd_replacement_d3_068}


def hcd_replacement_d3_069(hcd_replacement_d2_069):
    feature = _clean(hcd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_069'] = {'inputs': ['hcd_replacement_d2_069'], 'func': hcd_replacement_d3_069}


def hcd_replacement_d3_070(hcd_replacement_d2_070):
    feature = _clean(hcd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_070'] = {'inputs': ['hcd_replacement_d2_070'], 'func': hcd_replacement_d3_070}


def hcd_replacement_d3_071(hcd_replacement_d2_071):
    feature = _clean(hcd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_071'] = {'inputs': ['hcd_replacement_d2_071'], 'func': hcd_replacement_d3_071}


def hcd_replacement_d3_072(hcd_replacement_d2_072):
    feature = _clean(hcd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_072'] = {'inputs': ['hcd_replacement_d2_072'], 'func': hcd_replacement_d3_072}


def hcd_replacement_d3_073(hcd_replacement_d2_073):
    feature = _clean(hcd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_073'] = {'inputs': ['hcd_replacement_d2_073'], 'func': hcd_replacement_d3_073}


def hcd_replacement_d3_074(hcd_replacement_d2_074):
    feature = _clean(hcd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_074'] = {'inputs': ['hcd_replacement_d2_074'], 'func': hcd_replacement_d3_074}


def hcd_replacement_d3_075(hcd_replacement_d2_075):
    feature = _clean(hcd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_075'] = {'inputs': ['hcd_replacement_d2_075'], 'func': hcd_replacement_d3_075}


def hcd_replacement_d3_076(hcd_replacement_d2_076):
    feature = _clean(hcd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_076'] = {'inputs': ['hcd_replacement_d2_076'], 'func': hcd_replacement_d3_076}


def hcd_replacement_d3_077(hcd_replacement_d2_077):
    feature = _clean(hcd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_077'] = {'inputs': ['hcd_replacement_d2_077'], 'func': hcd_replacement_d3_077}


def hcd_replacement_d3_078(hcd_replacement_d2_078):
    feature = _clean(hcd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_078'] = {'inputs': ['hcd_replacement_d2_078'], 'func': hcd_replacement_d3_078}


def hcd_replacement_d3_079(hcd_replacement_d2_079):
    feature = _clean(hcd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_079'] = {'inputs': ['hcd_replacement_d2_079'], 'func': hcd_replacement_d3_079}


def hcd_replacement_d3_080(hcd_replacement_d2_080):
    feature = _clean(hcd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_080'] = {'inputs': ['hcd_replacement_d2_080'], 'func': hcd_replacement_d3_080}


def hcd_replacement_d3_081(hcd_replacement_d2_081):
    feature = _clean(hcd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_081'] = {'inputs': ['hcd_replacement_d2_081'], 'func': hcd_replacement_d3_081}


def hcd_replacement_d3_082(hcd_replacement_d2_082):
    feature = _clean(hcd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_082'] = {'inputs': ['hcd_replacement_d2_082'], 'func': hcd_replacement_d3_082}


def hcd_replacement_d3_083(hcd_replacement_d2_083):
    feature = _clean(hcd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_083'] = {'inputs': ['hcd_replacement_d2_083'], 'func': hcd_replacement_d3_083}


def hcd_replacement_d3_084(hcd_replacement_d2_084):
    feature = _clean(hcd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_084'] = {'inputs': ['hcd_replacement_d2_084'], 'func': hcd_replacement_d3_084}


def hcd_replacement_d3_085(hcd_replacement_d2_085):
    feature = _clean(hcd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_085'] = {'inputs': ['hcd_replacement_d2_085'], 'func': hcd_replacement_d3_085}


def hcd_replacement_d3_086(hcd_replacement_d2_086):
    feature = _clean(hcd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_086'] = {'inputs': ['hcd_replacement_d2_086'], 'func': hcd_replacement_d3_086}


def hcd_replacement_d3_087(hcd_replacement_d2_087):
    feature = _clean(hcd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_087'] = {'inputs': ['hcd_replacement_d2_087'], 'func': hcd_replacement_d3_087}


def hcd_replacement_d3_088(hcd_replacement_d2_088):
    feature = _clean(hcd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_088'] = {'inputs': ['hcd_replacement_d2_088'], 'func': hcd_replacement_d3_088}


def hcd_replacement_d3_089(hcd_replacement_d2_089):
    feature = _clean(hcd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_089'] = {'inputs': ['hcd_replacement_d2_089'], 'func': hcd_replacement_d3_089}


def hcd_replacement_d3_090(hcd_replacement_d2_090):
    feature = _clean(hcd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_090'] = {'inputs': ['hcd_replacement_d2_090'], 'func': hcd_replacement_d3_090}


def hcd_replacement_d3_091(hcd_replacement_d2_091):
    feature = _clean(hcd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_091'] = {'inputs': ['hcd_replacement_d2_091'], 'func': hcd_replacement_d3_091}


def hcd_replacement_d3_092(hcd_replacement_d2_092):
    feature = _clean(hcd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_092'] = {'inputs': ['hcd_replacement_d2_092'], 'func': hcd_replacement_d3_092}


def hcd_replacement_d3_093(hcd_replacement_d2_093):
    feature = _clean(hcd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_093'] = {'inputs': ['hcd_replacement_d2_093'], 'func': hcd_replacement_d3_093}


def hcd_replacement_d3_094(hcd_replacement_d2_094):
    feature = _clean(hcd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_094'] = {'inputs': ['hcd_replacement_d2_094'], 'func': hcd_replacement_d3_094}


def hcd_replacement_d3_095(hcd_replacement_d2_095):
    feature = _clean(hcd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_095'] = {'inputs': ['hcd_replacement_d2_095'], 'func': hcd_replacement_d3_095}


def hcd_replacement_d3_096(hcd_replacement_d2_096):
    feature = _clean(hcd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_096'] = {'inputs': ['hcd_replacement_d2_096'], 'func': hcd_replacement_d3_096}


def hcd_replacement_d3_097(hcd_replacement_d2_097):
    feature = _clean(hcd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_097'] = {'inputs': ['hcd_replacement_d2_097'], 'func': hcd_replacement_d3_097}


def hcd_replacement_d3_098(hcd_replacement_d2_098):
    feature = _clean(hcd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_098'] = {'inputs': ['hcd_replacement_d2_098'], 'func': hcd_replacement_d3_098}


def hcd_replacement_d3_099(hcd_replacement_d2_099):
    feature = _clean(hcd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_099'] = {'inputs': ['hcd_replacement_d2_099'], 'func': hcd_replacement_d3_099}


def hcd_replacement_d3_100(hcd_replacement_d2_100):
    feature = _clean(hcd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_100'] = {'inputs': ['hcd_replacement_d2_100'], 'func': hcd_replacement_d3_100}


def hcd_replacement_d3_101(hcd_replacement_d2_101):
    feature = _clean(hcd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_101'] = {'inputs': ['hcd_replacement_d2_101'], 'func': hcd_replacement_d3_101}


def hcd_replacement_d3_102(hcd_replacement_d2_102):
    feature = _clean(hcd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_102'] = {'inputs': ['hcd_replacement_d2_102'], 'func': hcd_replacement_d3_102}


def hcd_replacement_d3_103(hcd_replacement_d2_103):
    feature = _clean(hcd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_103'] = {'inputs': ['hcd_replacement_d2_103'], 'func': hcd_replacement_d3_103}


def hcd_replacement_d3_104(hcd_replacement_d2_104):
    feature = _clean(hcd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_104'] = {'inputs': ['hcd_replacement_d2_104'], 'func': hcd_replacement_d3_104}


def hcd_replacement_d3_105(hcd_replacement_d2_105):
    feature = _clean(hcd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_105'] = {'inputs': ['hcd_replacement_d2_105'], 'func': hcd_replacement_d3_105}


def hcd_replacement_d3_106(hcd_replacement_d2_106):
    feature = _clean(hcd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_106'] = {'inputs': ['hcd_replacement_d2_106'], 'func': hcd_replacement_d3_106}


def hcd_replacement_d3_107(hcd_replacement_d2_107):
    feature = _clean(hcd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_107'] = {'inputs': ['hcd_replacement_d2_107'], 'func': hcd_replacement_d3_107}


def hcd_replacement_d3_108(hcd_replacement_d2_108):
    feature = _clean(hcd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_108'] = {'inputs': ['hcd_replacement_d2_108'], 'func': hcd_replacement_d3_108}


def hcd_replacement_d3_109(hcd_replacement_d2_109):
    feature = _clean(hcd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_109'] = {'inputs': ['hcd_replacement_d2_109'], 'func': hcd_replacement_d3_109}


def hcd_replacement_d3_110(hcd_replacement_d2_110):
    feature = _clean(hcd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_110'] = {'inputs': ['hcd_replacement_d2_110'], 'func': hcd_replacement_d3_110}


def hcd_replacement_d3_111(hcd_replacement_d2_111):
    feature = _clean(hcd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_111'] = {'inputs': ['hcd_replacement_d2_111'], 'func': hcd_replacement_d3_111}


def hcd_replacement_d3_112(hcd_replacement_d2_112):
    feature = _clean(hcd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_112'] = {'inputs': ['hcd_replacement_d2_112'], 'func': hcd_replacement_d3_112}


def hcd_replacement_d3_113(hcd_replacement_d2_113):
    feature = _clean(hcd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_113'] = {'inputs': ['hcd_replacement_d2_113'], 'func': hcd_replacement_d3_113}


def hcd_replacement_d3_114(hcd_replacement_d2_114):
    feature = _clean(hcd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_114'] = {'inputs': ['hcd_replacement_d2_114'], 'func': hcd_replacement_d3_114}


def hcd_replacement_d3_115(hcd_replacement_d2_115):
    feature = _clean(hcd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_115'] = {'inputs': ['hcd_replacement_d2_115'], 'func': hcd_replacement_d3_115}


def hcd_replacement_d3_116(hcd_replacement_d2_116):
    feature = _clean(hcd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_116'] = {'inputs': ['hcd_replacement_d2_116'], 'func': hcd_replacement_d3_116}


def hcd_replacement_d3_117(hcd_replacement_d2_117):
    feature = _clean(hcd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_117'] = {'inputs': ['hcd_replacement_d2_117'], 'func': hcd_replacement_d3_117}


def hcd_replacement_d3_118(hcd_replacement_d2_118):
    feature = _clean(hcd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_118'] = {'inputs': ['hcd_replacement_d2_118'], 'func': hcd_replacement_d3_118}


def hcd_replacement_d3_119(hcd_replacement_d2_119):
    feature = _clean(hcd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_119'] = {'inputs': ['hcd_replacement_d2_119'], 'func': hcd_replacement_d3_119}


def hcd_replacement_d3_120(hcd_replacement_d2_120):
    feature = _clean(hcd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_120'] = {'inputs': ['hcd_replacement_d2_120'], 'func': hcd_replacement_d3_120}


def hcd_replacement_d3_121(hcd_replacement_d2_121):
    feature = _clean(hcd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_121'] = {'inputs': ['hcd_replacement_d2_121'], 'func': hcd_replacement_d3_121}


def hcd_replacement_d3_122(hcd_replacement_d2_122):
    feature = _clean(hcd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_122'] = {'inputs': ['hcd_replacement_d2_122'], 'func': hcd_replacement_d3_122}


def hcd_replacement_d3_123(hcd_replacement_d2_123):
    feature = _clean(hcd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_123'] = {'inputs': ['hcd_replacement_d2_123'], 'func': hcd_replacement_d3_123}


def hcd_replacement_d3_124(hcd_replacement_d2_124):
    feature = _clean(hcd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_124'] = {'inputs': ['hcd_replacement_d2_124'], 'func': hcd_replacement_d3_124}


def hcd_replacement_d3_125(hcd_replacement_d2_125):
    feature = _clean(hcd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_125'] = {'inputs': ['hcd_replacement_d2_125'], 'func': hcd_replacement_d3_125}


def hcd_replacement_d3_126(hcd_replacement_d2_126):
    feature = _clean(hcd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_126'] = {'inputs': ['hcd_replacement_d2_126'], 'func': hcd_replacement_d3_126}


def hcd_replacement_d3_127(hcd_replacement_d2_127):
    feature = _clean(hcd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_127'] = {'inputs': ['hcd_replacement_d2_127'], 'func': hcd_replacement_d3_127}


def hcd_replacement_d3_128(hcd_replacement_d2_128):
    feature = _clean(hcd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_128'] = {'inputs': ['hcd_replacement_d2_128'], 'func': hcd_replacement_d3_128}


def hcd_replacement_d3_129(hcd_replacement_d2_129):
    feature = _clean(hcd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_129'] = {'inputs': ['hcd_replacement_d2_129'], 'func': hcd_replacement_d3_129}


def hcd_replacement_d3_130(hcd_replacement_d2_130):
    feature = _clean(hcd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_130'] = {'inputs': ['hcd_replacement_d2_130'], 'func': hcd_replacement_d3_130}


def hcd_replacement_d3_131(hcd_replacement_d2_131):
    feature = _clean(hcd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_131'] = {'inputs': ['hcd_replacement_d2_131'], 'func': hcd_replacement_d3_131}


def hcd_replacement_d3_132(hcd_replacement_d2_132):
    feature = _clean(hcd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_132'] = {'inputs': ['hcd_replacement_d2_132'], 'func': hcd_replacement_d3_132}


def hcd_replacement_d3_133(hcd_replacement_d2_133):
    feature = _clean(hcd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_133'] = {'inputs': ['hcd_replacement_d2_133'], 'func': hcd_replacement_d3_133}


def hcd_replacement_d3_134(hcd_replacement_d2_134):
    feature = _clean(hcd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_134'] = {'inputs': ['hcd_replacement_d2_134'], 'func': hcd_replacement_d3_134}


def hcd_replacement_d3_135(hcd_replacement_d2_135):
    feature = _clean(hcd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_135'] = {'inputs': ['hcd_replacement_d2_135'], 'func': hcd_replacement_d3_135}


def hcd_replacement_d3_136(hcd_replacement_d2_136):
    feature = _clean(hcd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_136'] = {'inputs': ['hcd_replacement_d2_136'], 'func': hcd_replacement_d3_136}


def hcd_replacement_d3_137(hcd_replacement_d2_137):
    feature = _clean(hcd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_137'] = {'inputs': ['hcd_replacement_d2_137'], 'func': hcd_replacement_d3_137}


def hcd_replacement_d3_138(hcd_replacement_d2_138):
    feature = _clean(hcd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_138'] = {'inputs': ['hcd_replacement_d2_138'], 'func': hcd_replacement_d3_138}


def hcd_replacement_d3_139(hcd_replacement_d2_139):
    feature = _clean(hcd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_139'] = {'inputs': ['hcd_replacement_d2_139'], 'func': hcd_replacement_d3_139}


def hcd_replacement_d3_140(hcd_replacement_d2_140):
    feature = _clean(hcd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_140'] = {'inputs': ['hcd_replacement_d2_140'], 'func': hcd_replacement_d3_140}


def hcd_replacement_d3_141(hcd_replacement_d2_141):
    feature = _clean(hcd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_141'] = {'inputs': ['hcd_replacement_d2_141'], 'func': hcd_replacement_d3_141}


def hcd_replacement_d3_142(hcd_replacement_d2_142):
    feature = _clean(hcd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_142'] = {'inputs': ['hcd_replacement_d2_142'], 'func': hcd_replacement_d3_142}


def hcd_replacement_d3_143(hcd_replacement_d2_143):
    feature = _clean(hcd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_143'] = {'inputs': ['hcd_replacement_d2_143'], 'func': hcd_replacement_d3_143}


def hcd_replacement_d3_144(hcd_replacement_d2_144):
    feature = _clean(hcd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_144'] = {'inputs': ['hcd_replacement_d2_144'], 'func': hcd_replacement_d3_144}


def hcd_replacement_d3_145(hcd_replacement_d2_145):
    feature = _clean(hcd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_145'] = {'inputs': ['hcd_replacement_d2_145'], 'func': hcd_replacement_d3_145}


def hcd_replacement_d3_146(hcd_replacement_d2_146):
    feature = _clean(hcd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_146'] = {'inputs': ['hcd_replacement_d2_146'], 'func': hcd_replacement_d3_146}


def hcd_replacement_d3_147(hcd_replacement_d2_147):
    feature = _clean(hcd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_147'] = {'inputs': ['hcd_replacement_d2_147'], 'func': hcd_replacement_d3_147}


def hcd_replacement_d3_148(hcd_replacement_d2_148):
    feature = _clean(hcd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_148'] = {'inputs': ['hcd_replacement_d2_148'], 'func': hcd_replacement_d3_148}


def hcd_replacement_d3_149(hcd_replacement_d2_149):
    feature = _clean(hcd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_149'] = {'inputs': ['hcd_replacement_d2_149'], 'func': hcd_replacement_d3_149}


def hcd_replacement_d3_150(hcd_replacement_d2_150):
    feature = _clean(hcd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_150'] = {'inputs': ['hcd_replacement_d2_150'], 'func': hcd_replacement_d3_150}


def hcd_replacement_d3_151(hcd_replacement_d2_151):
    feature = _clean(hcd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_151'] = {'inputs': ['hcd_replacement_d2_151'], 'func': hcd_replacement_d3_151}


def hcd_replacement_d3_152(hcd_replacement_d2_152):
    feature = _clean(hcd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_152'] = {'inputs': ['hcd_replacement_d2_152'], 'func': hcd_replacement_d3_152}


def hcd_replacement_d3_153(hcd_replacement_d2_153):
    feature = _clean(hcd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_153'] = {'inputs': ['hcd_replacement_d2_153'], 'func': hcd_replacement_d3_153}


def hcd_replacement_d3_154(hcd_replacement_d2_154):
    feature = _clean(hcd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_154'] = {'inputs': ['hcd_replacement_d2_154'], 'func': hcd_replacement_d3_154}


def hcd_replacement_d3_155(hcd_replacement_d2_155):
    feature = _clean(hcd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_155'] = {'inputs': ['hcd_replacement_d2_155'], 'func': hcd_replacement_d3_155}


def hcd_replacement_d3_156(hcd_replacement_d2_156):
    feature = _clean(hcd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_156'] = {'inputs': ['hcd_replacement_d2_156'], 'func': hcd_replacement_d3_156}


def hcd_replacement_d3_157(hcd_replacement_d2_157):
    feature = _clean(hcd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_157'] = {'inputs': ['hcd_replacement_d2_157'], 'func': hcd_replacement_d3_157}


def hcd_replacement_d3_158(hcd_replacement_d2_158):
    feature = _clean(hcd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_158'] = {'inputs': ['hcd_replacement_d2_158'], 'func': hcd_replacement_d3_158}


def hcd_replacement_d3_159(hcd_replacement_d2_159):
    feature = _clean(hcd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_159'] = {'inputs': ['hcd_replacement_d2_159'], 'func': hcd_replacement_d3_159}


def hcd_replacement_d3_160(hcd_replacement_d2_160):
    feature = _clean(hcd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_160'] = {'inputs': ['hcd_replacement_d2_160'], 'func': hcd_replacement_d3_160}


def hcd_replacement_d3_161(hcd_replacement_d2_161):
    feature = _clean(hcd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_161'] = {'inputs': ['hcd_replacement_d2_161'], 'func': hcd_replacement_d3_161}


def hcd_replacement_d3_162(hcd_replacement_d2_162):
    feature = _clean(hcd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_162'] = {'inputs': ['hcd_replacement_d2_162'], 'func': hcd_replacement_d3_162}


def hcd_replacement_d3_163(hcd_replacement_d2_163):
    feature = _clean(hcd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_163'] = {'inputs': ['hcd_replacement_d2_163'], 'func': hcd_replacement_d3_163}


def hcd_replacement_d3_164(hcd_replacement_d2_164):
    feature = _clean(hcd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_164'] = {'inputs': ['hcd_replacement_d2_164'], 'func': hcd_replacement_d3_164}


def hcd_replacement_d3_165(hcd_replacement_d2_165):
    feature = _clean(hcd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_165'] = {'inputs': ['hcd_replacement_d2_165'], 'func': hcd_replacement_d3_165}


def hcd_replacement_d3_166(hcd_replacement_d2_166):
    feature = _clean(hcd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_166'] = {'inputs': ['hcd_replacement_d2_166'], 'func': hcd_replacement_d3_166}


def hcd_replacement_d3_167(hcd_replacement_d2_167):
    feature = _clean(hcd_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_167'] = {'inputs': ['hcd_replacement_d2_167'], 'func': hcd_replacement_d3_167}


def hcd_replacement_d3_168(hcd_replacement_d2_168):
    feature = _clean(hcd_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_168'] = {'inputs': ['hcd_replacement_d2_168'], 'func': hcd_replacement_d3_168}


def hcd_replacement_d3_169(hcd_replacement_d2_169):
    feature = _clean(hcd_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_169'] = {'inputs': ['hcd_replacement_d2_169'], 'func': hcd_replacement_d3_169}


def hcd_replacement_d3_170(hcd_replacement_d2_170):
    feature = _clean(hcd_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_170'] = {'inputs': ['hcd_replacement_d2_170'], 'func': hcd_replacement_d3_170}


def hcd_replacement_d3_171(hcd_replacement_d2_171):
    feature = _clean(hcd_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_171'] = {'inputs': ['hcd_replacement_d2_171'], 'func': hcd_replacement_d3_171}


def hcd_replacement_d3_172(hcd_replacement_d2_172):
    feature = _clean(hcd_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_172'] = {'inputs': ['hcd_replacement_d2_172'], 'func': hcd_replacement_d3_172}


def hcd_replacement_d3_173(hcd_replacement_d2_173):
    feature = _clean(hcd_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_173'] = {'inputs': ['hcd_replacement_d2_173'], 'func': hcd_replacement_d3_173}


def hcd_replacement_d3_174(hcd_replacement_d2_174):
    feature = _clean(hcd_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_174'] = {'inputs': ['hcd_replacement_d2_174'], 'func': hcd_replacement_d3_174}


def hcd_replacement_d3_175(hcd_replacement_d2_175):
    feature = _clean(hcd_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_175'] = {'inputs': ['hcd_replacement_d2_175'], 'func': hcd_replacement_d3_175}


def hcd_replacement_d3_176(hcd_replacement_d2_176):
    feature = _clean(hcd_replacement_d2_176)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00088000).reindex(feature.index)
HCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['hcd_replacement_d3_176'] = {'inputs': ['hcd_replacement_d2_176'], 'func': hcd_replacement_d3_176}


# Third-derivative extensions for repaired first-base features.
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def hcd_base_universe_d3_001_hcd_003_holder_breadth_peer_z_63(hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63):
    return _base_universe_d3(hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63, 1)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_001_hcd_003_holder_breadth_peer_z_63'] = {'inputs': ['hcd_base_universe_d2_001_hcd_003_holder_breadth_peer_z_63'], 'func': hcd_base_universe_d3_001_hcd_003_holder_breadth_peer_z_63}


def hcd_base_universe_d3_002_hcd_011_holder_breadth_peer_z_1008(hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008):
    return _base_universe_d3(hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008, 2)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_002_hcd_011_holder_breadth_peer_z_1008'] = {'inputs': ['hcd_base_universe_d2_002_hcd_011_holder_breadth_peer_z_1008'], 'func': hcd_base_universe_d3_002_hcd_011_holder_breadth_peer_z_1008}


def hcd_base_universe_d3_003_hcd_023_holder_breadth_peer_z_378(hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378):
    return _base_universe_d3(hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378, 3)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_003_hcd_023_holder_breadth_peer_z_378'] = {'inputs': ['hcd_base_universe_d2_003_hcd_023_holder_breadth_peer_z_378'], 'func': hcd_base_universe_d3_003_hcd_023_holder_breadth_peer_z_378}


def hcd_base_universe_d3_004_hcd_027_holder_breadth_peer_z_1260(hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260):
    return _base_universe_d3(hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260, 4)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_004_hcd_027_holder_breadth_peer_z_1260'] = {'inputs': ['hcd_base_universe_d2_004_hcd_027_holder_breadth_peer_z_1260'], 'func': hcd_base_universe_d3_004_hcd_027_holder_breadth_peer_z_1260}


def hcd_base_universe_d3_005_hcd_031_holder_breadth_peer_z_21(hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21):
    return _base_universe_d3(hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21, 5)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_005_hcd_031_holder_breadth_peer_z_21'] = {'inputs': ['hcd_base_universe_d2_005_hcd_031_holder_breadth_peer_z_21'], 'func': hcd_base_universe_d3_005_hcd_031_holder_breadth_peer_z_21}


def hcd_base_universe_d3_006_hcd_035_holder_breadth_peer_z_126(hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126):
    return _base_universe_d3(hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126, 6)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_006_hcd_035_holder_breadth_peer_z_126'] = {'inputs': ['hcd_base_universe_d2_006_hcd_035_holder_breadth_peer_z_126'], 'func': hcd_base_universe_d3_006_hcd_035_holder_breadth_peer_z_126}


def hcd_base_universe_d3_007_hcd_039_holder_breadth_peer_z_504(hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504):
    return _base_universe_d3(hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504, 7)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_007_hcd_039_holder_breadth_peer_z_504'] = {'inputs': ['hcd_base_universe_d2_007_hcd_039_holder_breadth_peer_z_504'], 'func': hcd_base_universe_d3_007_hcd_039_holder_breadth_peer_z_504}


def hcd_base_universe_d3_008_hcd_043_holder_breadth_peer_z_1512(hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512):
    return _base_universe_d3(hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512, 8)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_008_hcd_043_holder_breadth_peer_z_1512'] = {'inputs': ['hcd_base_universe_d2_008_hcd_043_holder_breadth_peer_z_1512'], 'func': hcd_base_universe_d3_008_hcd_043_holder_breadth_peer_z_1512}


def hcd_base_universe_d3_009_hcd_047_holder_breadth_peer_z_42(hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42):
    return _base_universe_d3(hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42, 9)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_009_hcd_047_holder_breadth_peer_z_42'] = {'inputs': ['hcd_base_universe_d2_009_hcd_047_holder_breadth_peer_z_42'], 'func': hcd_base_universe_d3_009_hcd_047_holder_breadth_peer_z_42}


def hcd_base_universe_d3_010_hcd_051_holder_breadth_peer_z_189(hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189):
    return _base_universe_d3(hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189, 10)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_010_hcd_051_holder_breadth_peer_z_189'] = {'inputs': ['hcd_base_universe_d2_010_hcd_051_holder_breadth_peer_z_189'], 'func': hcd_base_universe_d3_010_hcd_051_holder_breadth_peer_z_189}


def hcd_base_universe_d3_011_hcd_055_holder_breadth_peer_z_756(hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756):
    return _base_universe_d3(hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756, 11)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_011_hcd_055_holder_breadth_peer_z_756'] = {'inputs': ['hcd_base_universe_d2_011_hcd_055_holder_breadth_peer_z_756'], 'func': hcd_base_universe_d3_011_hcd_055_holder_breadth_peer_z_756}


def hcd_base_universe_d3_012_hcd_basefill_002(hcd_base_universe_d2_012_hcd_basefill_002):
    return _base_universe_d3(hcd_base_universe_d2_012_hcd_basefill_002, 12)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_012_hcd_basefill_002'] = {'inputs': ['hcd_base_universe_d2_012_hcd_basefill_002'], 'func': hcd_base_universe_d3_012_hcd_basefill_002}


def hcd_base_universe_d3_013_hcd_basefill_004(hcd_base_universe_d2_013_hcd_basefill_004):
    return _base_universe_d3(hcd_base_universe_d2_013_hcd_basefill_004, 13)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_013_hcd_basefill_004'] = {'inputs': ['hcd_base_universe_d2_013_hcd_basefill_004'], 'func': hcd_base_universe_d3_013_hcd_basefill_004}


def hcd_base_universe_d3_014_hcd_basefill_005(hcd_base_universe_d2_014_hcd_basefill_005):
    return _base_universe_d3(hcd_base_universe_d2_014_hcd_basefill_005, 14)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_014_hcd_basefill_005'] = {'inputs': ['hcd_base_universe_d2_014_hcd_basefill_005'], 'func': hcd_base_universe_d3_014_hcd_basefill_005}


def hcd_base_universe_d3_015_hcd_basefill_006(hcd_base_universe_d2_015_hcd_basefill_006):
    return _base_universe_d3(hcd_base_universe_d2_015_hcd_basefill_006, 15)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_015_hcd_basefill_006'] = {'inputs': ['hcd_base_universe_d2_015_hcd_basefill_006'], 'func': hcd_base_universe_d3_015_hcd_basefill_006}


def hcd_base_universe_d3_016_hcd_basefill_008(hcd_base_universe_d2_016_hcd_basefill_008):
    return _base_universe_d3(hcd_base_universe_d2_016_hcd_basefill_008, 16)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_016_hcd_basefill_008'] = {'inputs': ['hcd_base_universe_d2_016_hcd_basefill_008'], 'func': hcd_base_universe_d3_016_hcd_basefill_008}


def hcd_base_universe_d3_017_hcd_basefill_009(hcd_base_universe_d2_017_hcd_basefill_009):
    return _base_universe_d3(hcd_base_universe_d2_017_hcd_basefill_009, 17)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_017_hcd_basefill_009'] = {'inputs': ['hcd_base_universe_d2_017_hcd_basefill_009'], 'func': hcd_base_universe_d3_017_hcd_basefill_009}


def hcd_base_universe_d3_018_hcd_basefill_010(hcd_base_universe_d2_018_hcd_basefill_010):
    return _base_universe_d3(hcd_base_universe_d2_018_hcd_basefill_010, 18)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_018_hcd_basefill_010'] = {'inputs': ['hcd_base_universe_d2_018_hcd_basefill_010'], 'func': hcd_base_universe_d3_018_hcd_basefill_010}


def hcd_base_universe_d3_019_hcd_basefill_012(hcd_base_universe_d2_019_hcd_basefill_012):
    return _base_universe_d3(hcd_base_universe_d2_019_hcd_basefill_012, 19)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_019_hcd_basefill_012'] = {'inputs': ['hcd_base_universe_d2_019_hcd_basefill_012'], 'func': hcd_base_universe_d3_019_hcd_basefill_012}


def hcd_base_universe_d3_020_hcd_basefill_013(hcd_base_universe_d2_020_hcd_basefill_013):
    return _base_universe_d3(hcd_base_universe_d2_020_hcd_basefill_013, 20)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_020_hcd_basefill_013'] = {'inputs': ['hcd_base_universe_d2_020_hcd_basefill_013'], 'func': hcd_base_universe_d3_020_hcd_basefill_013}


def hcd_base_universe_d3_021_hcd_basefill_014(hcd_base_universe_d2_021_hcd_basefill_014):
    return _base_universe_d3(hcd_base_universe_d2_021_hcd_basefill_014, 21)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_021_hcd_basefill_014'] = {'inputs': ['hcd_base_universe_d2_021_hcd_basefill_014'], 'func': hcd_base_universe_d3_021_hcd_basefill_014}


def hcd_base_universe_d3_022_hcd_basefill_015(hcd_base_universe_d2_022_hcd_basefill_015):
    return _base_universe_d3(hcd_base_universe_d2_022_hcd_basefill_015, 22)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_022_hcd_basefill_015'] = {'inputs': ['hcd_base_universe_d2_022_hcd_basefill_015'], 'func': hcd_base_universe_d3_022_hcd_basefill_015}


def hcd_base_universe_d3_023_hcd_basefill_016(hcd_base_universe_d2_023_hcd_basefill_016):
    return _base_universe_d3(hcd_base_universe_d2_023_hcd_basefill_016, 23)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_023_hcd_basefill_016'] = {'inputs': ['hcd_base_universe_d2_023_hcd_basefill_016'], 'func': hcd_base_universe_d3_023_hcd_basefill_016}


def hcd_base_universe_d3_024_hcd_basefill_017(hcd_base_universe_d2_024_hcd_basefill_017):
    return _base_universe_d3(hcd_base_universe_d2_024_hcd_basefill_017, 24)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_024_hcd_basefill_017'] = {'inputs': ['hcd_base_universe_d2_024_hcd_basefill_017'], 'func': hcd_base_universe_d3_024_hcd_basefill_017}


def hcd_base_universe_d3_025_hcd_basefill_018(hcd_base_universe_d2_025_hcd_basefill_018):
    return _base_universe_d3(hcd_base_universe_d2_025_hcd_basefill_018, 25)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_025_hcd_basefill_018'] = {'inputs': ['hcd_base_universe_d2_025_hcd_basefill_018'], 'func': hcd_base_universe_d3_025_hcd_basefill_018}


def hcd_base_universe_d3_026_hcd_basefill_020(hcd_base_universe_d2_026_hcd_basefill_020):
    return _base_universe_d3(hcd_base_universe_d2_026_hcd_basefill_020, 26)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_026_hcd_basefill_020'] = {'inputs': ['hcd_base_universe_d2_026_hcd_basefill_020'], 'func': hcd_base_universe_d3_026_hcd_basefill_020}


def hcd_base_universe_d3_027_hcd_basefill_021(hcd_base_universe_d2_027_hcd_basefill_021):
    return _base_universe_d3(hcd_base_universe_d2_027_hcd_basefill_021, 27)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_027_hcd_basefill_021'] = {'inputs': ['hcd_base_universe_d2_027_hcd_basefill_021'], 'func': hcd_base_universe_d3_027_hcd_basefill_021}


def hcd_base_universe_d3_028_hcd_basefill_022(hcd_base_universe_d2_028_hcd_basefill_022):
    return _base_universe_d3(hcd_base_universe_d2_028_hcd_basefill_022, 28)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_028_hcd_basefill_022'] = {'inputs': ['hcd_base_universe_d2_028_hcd_basefill_022'], 'func': hcd_base_universe_d3_028_hcd_basefill_022}


def hcd_base_universe_d3_029_hcd_basefill_024(hcd_base_universe_d2_029_hcd_basefill_024):
    return _base_universe_d3(hcd_base_universe_d2_029_hcd_basefill_024, 29)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_029_hcd_basefill_024'] = {'inputs': ['hcd_base_universe_d2_029_hcd_basefill_024'], 'func': hcd_base_universe_d3_029_hcd_basefill_024}


def hcd_base_universe_d3_030_hcd_basefill_025(hcd_base_universe_d2_030_hcd_basefill_025):
    return _base_universe_d3(hcd_base_universe_d2_030_hcd_basefill_025, 30)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_030_hcd_basefill_025'] = {'inputs': ['hcd_base_universe_d2_030_hcd_basefill_025'], 'func': hcd_base_universe_d3_030_hcd_basefill_025}


def hcd_base_universe_d3_031_hcd_basefill_026(hcd_base_universe_d2_031_hcd_basefill_026):
    return _base_universe_d3(hcd_base_universe_d2_031_hcd_basefill_026, 31)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_031_hcd_basefill_026'] = {'inputs': ['hcd_base_universe_d2_031_hcd_basefill_026'], 'func': hcd_base_universe_d3_031_hcd_basefill_026}


def hcd_base_universe_d3_032_hcd_basefill_028(hcd_base_universe_d2_032_hcd_basefill_028):
    return _base_universe_d3(hcd_base_universe_d2_032_hcd_basefill_028, 32)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_032_hcd_basefill_028'] = {'inputs': ['hcd_base_universe_d2_032_hcd_basefill_028'], 'func': hcd_base_universe_d3_032_hcd_basefill_028}


def hcd_base_universe_d3_033_hcd_basefill_029(hcd_base_universe_d2_033_hcd_basefill_029):
    return _base_universe_d3(hcd_base_universe_d2_033_hcd_basefill_029, 33)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_033_hcd_basefill_029'] = {'inputs': ['hcd_base_universe_d2_033_hcd_basefill_029'], 'func': hcd_base_universe_d3_033_hcd_basefill_029}


def hcd_base_universe_d3_034_hcd_basefill_030(hcd_base_universe_d2_034_hcd_basefill_030):
    return _base_universe_d3(hcd_base_universe_d2_034_hcd_basefill_030, 34)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_034_hcd_basefill_030'] = {'inputs': ['hcd_base_universe_d2_034_hcd_basefill_030'], 'func': hcd_base_universe_d3_034_hcd_basefill_030}


def hcd_base_universe_d3_035_hcd_basefill_032(hcd_base_universe_d2_035_hcd_basefill_032):
    return _base_universe_d3(hcd_base_universe_d2_035_hcd_basefill_032, 35)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_035_hcd_basefill_032'] = {'inputs': ['hcd_base_universe_d2_035_hcd_basefill_032'], 'func': hcd_base_universe_d3_035_hcd_basefill_032}


def hcd_base_universe_d3_036_hcd_basefill_033(hcd_base_universe_d2_036_hcd_basefill_033):
    return _base_universe_d3(hcd_base_universe_d2_036_hcd_basefill_033, 36)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_036_hcd_basefill_033'] = {'inputs': ['hcd_base_universe_d2_036_hcd_basefill_033'], 'func': hcd_base_universe_d3_036_hcd_basefill_033}


def hcd_base_universe_d3_037_hcd_basefill_034(hcd_base_universe_d2_037_hcd_basefill_034):
    return _base_universe_d3(hcd_base_universe_d2_037_hcd_basefill_034, 37)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_037_hcd_basefill_034'] = {'inputs': ['hcd_base_universe_d2_037_hcd_basefill_034'], 'func': hcd_base_universe_d3_037_hcd_basefill_034}


def hcd_base_universe_d3_038_hcd_basefill_036(hcd_base_universe_d2_038_hcd_basefill_036):
    return _base_universe_d3(hcd_base_universe_d2_038_hcd_basefill_036, 38)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_038_hcd_basefill_036'] = {'inputs': ['hcd_base_universe_d2_038_hcd_basefill_036'], 'func': hcd_base_universe_d3_038_hcd_basefill_036}


def hcd_base_universe_d3_039_hcd_basefill_037(hcd_base_universe_d2_039_hcd_basefill_037):
    return _base_universe_d3(hcd_base_universe_d2_039_hcd_basefill_037, 39)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_039_hcd_basefill_037'] = {'inputs': ['hcd_base_universe_d2_039_hcd_basefill_037'], 'func': hcd_base_universe_d3_039_hcd_basefill_037}


def hcd_base_universe_d3_040_hcd_basefill_038(hcd_base_universe_d2_040_hcd_basefill_038):
    return _base_universe_d3(hcd_base_universe_d2_040_hcd_basefill_038, 40)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_040_hcd_basefill_038'] = {'inputs': ['hcd_base_universe_d2_040_hcd_basefill_038'], 'func': hcd_base_universe_d3_040_hcd_basefill_038}


def hcd_base_universe_d3_041_hcd_basefill_040(hcd_base_universe_d2_041_hcd_basefill_040):
    return _base_universe_d3(hcd_base_universe_d2_041_hcd_basefill_040, 41)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_041_hcd_basefill_040'] = {'inputs': ['hcd_base_universe_d2_041_hcd_basefill_040'], 'func': hcd_base_universe_d3_041_hcd_basefill_040}


def hcd_base_universe_d3_042_hcd_basefill_041(hcd_base_universe_d2_042_hcd_basefill_041):
    return _base_universe_d3(hcd_base_universe_d2_042_hcd_basefill_041, 42)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_042_hcd_basefill_041'] = {'inputs': ['hcd_base_universe_d2_042_hcd_basefill_041'], 'func': hcd_base_universe_d3_042_hcd_basefill_041}


def hcd_base_universe_d3_043_hcd_basefill_042(hcd_base_universe_d2_043_hcd_basefill_042):
    return _base_universe_d3(hcd_base_universe_d2_043_hcd_basefill_042, 43)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_043_hcd_basefill_042'] = {'inputs': ['hcd_base_universe_d2_043_hcd_basefill_042'], 'func': hcd_base_universe_d3_043_hcd_basefill_042}


def hcd_base_universe_d3_044_hcd_basefill_044(hcd_base_universe_d2_044_hcd_basefill_044):
    return _base_universe_d3(hcd_base_universe_d2_044_hcd_basefill_044, 44)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_044_hcd_basefill_044'] = {'inputs': ['hcd_base_universe_d2_044_hcd_basefill_044'], 'func': hcd_base_universe_d3_044_hcd_basefill_044}


def hcd_base_universe_d3_045_hcd_basefill_045(hcd_base_universe_d2_045_hcd_basefill_045):
    return _base_universe_d3(hcd_base_universe_d2_045_hcd_basefill_045, 45)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_045_hcd_basefill_045'] = {'inputs': ['hcd_base_universe_d2_045_hcd_basefill_045'], 'func': hcd_base_universe_d3_045_hcd_basefill_045}


def hcd_base_universe_d3_046_hcd_basefill_046(hcd_base_universe_d2_046_hcd_basefill_046):
    return _base_universe_d3(hcd_base_universe_d2_046_hcd_basefill_046, 46)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_046_hcd_basefill_046'] = {'inputs': ['hcd_base_universe_d2_046_hcd_basefill_046'], 'func': hcd_base_universe_d3_046_hcd_basefill_046}


def hcd_base_universe_d3_047_hcd_basefill_048(hcd_base_universe_d2_047_hcd_basefill_048):
    return _base_universe_d3(hcd_base_universe_d2_047_hcd_basefill_048, 47)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_047_hcd_basefill_048'] = {'inputs': ['hcd_base_universe_d2_047_hcd_basefill_048'], 'func': hcd_base_universe_d3_047_hcd_basefill_048}


def hcd_base_universe_d3_048_hcd_basefill_049(hcd_base_universe_d2_048_hcd_basefill_049):
    return _base_universe_d3(hcd_base_universe_d2_048_hcd_basefill_049, 48)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_048_hcd_basefill_049'] = {'inputs': ['hcd_base_universe_d2_048_hcd_basefill_049'], 'func': hcd_base_universe_d3_048_hcd_basefill_049}


def hcd_base_universe_d3_049_hcd_basefill_050(hcd_base_universe_d2_049_hcd_basefill_050):
    return _base_universe_d3(hcd_base_universe_d2_049_hcd_basefill_050, 49)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_049_hcd_basefill_050'] = {'inputs': ['hcd_base_universe_d2_049_hcd_basefill_050'], 'func': hcd_base_universe_d3_049_hcd_basefill_050}


def hcd_base_universe_d3_050_hcd_basefill_052(hcd_base_universe_d2_050_hcd_basefill_052):
    return _base_universe_d3(hcd_base_universe_d2_050_hcd_basefill_052, 50)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_050_hcd_basefill_052'] = {'inputs': ['hcd_base_universe_d2_050_hcd_basefill_052'], 'func': hcd_base_universe_d3_050_hcd_basefill_052}


def hcd_base_universe_d3_051_hcd_basefill_053(hcd_base_universe_d2_051_hcd_basefill_053):
    return _base_universe_d3(hcd_base_universe_d2_051_hcd_basefill_053, 51)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_051_hcd_basefill_053'] = {'inputs': ['hcd_base_universe_d2_051_hcd_basefill_053'], 'func': hcd_base_universe_d3_051_hcd_basefill_053}


def hcd_base_universe_d3_052_hcd_basefill_054(hcd_base_universe_d2_052_hcd_basefill_054):
    return _base_universe_d3(hcd_base_universe_d2_052_hcd_basefill_054, 52)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_052_hcd_basefill_054'] = {'inputs': ['hcd_base_universe_d2_052_hcd_basefill_054'], 'func': hcd_base_universe_d3_052_hcd_basefill_054}


def hcd_base_universe_d3_053_hcd_basefill_056(hcd_base_universe_d2_053_hcd_basefill_056):
    return _base_universe_d3(hcd_base_universe_d2_053_hcd_basefill_056, 53)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_053_hcd_basefill_056'] = {'inputs': ['hcd_base_universe_d2_053_hcd_basefill_056'], 'func': hcd_base_universe_d3_053_hcd_basefill_056}


def hcd_base_universe_d3_054_hcd_basefill_057(hcd_base_universe_d2_054_hcd_basefill_057):
    return _base_universe_d3(hcd_base_universe_d2_054_hcd_basefill_057, 54)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_054_hcd_basefill_057'] = {'inputs': ['hcd_base_universe_d2_054_hcd_basefill_057'], 'func': hcd_base_universe_d3_054_hcd_basefill_057}


def hcd_base_universe_d3_055_hcd_basefill_058(hcd_base_universe_d2_055_hcd_basefill_058):
    return _base_universe_d3(hcd_base_universe_d2_055_hcd_basefill_058, 55)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_055_hcd_basefill_058'] = {'inputs': ['hcd_base_universe_d2_055_hcd_basefill_058'], 'func': hcd_base_universe_d3_055_hcd_basefill_058}


def hcd_base_universe_d3_056_hcd_basefill_059(hcd_base_universe_d2_056_hcd_basefill_059):
    return _base_universe_d3(hcd_base_universe_d2_056_hcd_basefill_059, 56)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_056_hcd_basefill_059'] = {'inputs': ['hcd_base_universe_d2_056_hcd_basefill_059'], 'func': hcd_base_universe_d3_056_hcd_basefill_059}


def hcd_base_universe_d3_057_hcd_basefill_060(hcd_base_universe_d2_057_hcd_basefill_060):
    return _base_universe_d3(hcd_base_universe_d2_057_hcd_basefill_060, 57)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_057_hcd_basefill_060'] = {'inputs': ['hcd_base_universe_d2_057_hcd_basefill_060'], 'func': hcd_base_universe_d3_057_hcd_basefill_060}


def hcd_base_universe_d3_058_hcd_basefill_061(hcd_base_universe_d2_058_hcd_basefill_061):
    return _base_universe_d3(hcd_base_universe_d2_058_hcd_basefill_061, 58)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_058_hcd_basefill_061'] = {'inputs': ['hcd_base_universe_d2_058_hcd_basefill_061'], 'func': hcd_base_universe_d3_058_hcd_basefill_061}


def hcd_base_universe_d3_059_hcd_basefill_062(hcd_base_universe_d2_059_hcd_basefill_062):
    return _base_universe_d3(hcd_base_universe_d2_059_hcd_basefill_062, 59)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_059_hcd_basefill_062'] = {'inputs': ['hcd_base_universe_d2_059_hcd_basefill_062'], 'func': hcd_base_universe_d3_059_hcd_basefill_062}


def hcd_base_universe_d3_060_hcd_basefill_063(hcd_base_universe_d2_060_hcd_basefill_063):
    return _base_universe_d3(hcd_base_universe_d2_060_hcd_basefill_063, 60)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_060_hcd_basefill_063'] = {'inputs': ['hcd_base_universe_d2_060_hcd_basefill_063'], 'func': hcd_base_universe_d3_060_hcd_basefill_063}


def hcd_base_universe_d3_061_hcd_basefill_064(hcd_base_universe_d2_061_hcd_basefill_064):
    return _base_universe_d3(hcd_base_universe_d2_061_hcd_basefill_064, 61)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_061_hcd_basefill_064'] = {'inputs': ['hcd_base_universe_d2_061_hcd_basefill_064'], 'func': hcd_base_universe_d3_061_hcd_basefill_064}


def hcd_base_universe_d3_062_hcd_basefill_065(hcd_base_universe_d2_062_hcd_basefill_065):
    return _base_universe_d3(hcd_base_universe_d2_062_hcd_basefill_065, 62)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_062_hcd_basefill_065'] = {'inputs': ['hcd_base_universe_d2_062_hcd_basefill_065'], 'func': hcd_base_universe_d3_062_hcd_basefill_065}


def hcd_base_universe_d3_063_hcd_basefill_066(hcd_base_universe_d2_063_hcd_basefill_066):
    return _base_universe_d3(hcd_base_universe_d2_063_hcd_basefill_066, 63)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_063_hcd_basefill_066'] = {'inputs': ['hcd_base_universe_d2_063_hcd_basefill_066'], 'func': hcd_base_universe_d3_063_hcd_basefill_066}


def hcd_base_universe_d3_064_hcd_basefill_067(hcd_base_universe_d2_064_hcd_basefill_067):
    return _base_universe_d3(hcd_base_universe_d2_064_hcd_basefill_067, 64)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_064_hcd_basefill_067'] = {'inputs': ['hcd_base_universe_d2_064_hcd_basefill_067'], 'func': hcd_base_universe_d3_064_hcd_basefill_067}


def hcd_base_universe_d3_065_hcd_basefill_068(hcd_base_universe_d2_065_hcd_basefill_068):
    return _base_universe_d3(hcd_base_universe_d2_065_hcd_basefill_068, 65)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_065_hcd_basefill_068'] = {'inputs': ['hcd_base_universe_d2_065_hcd_basefill_068'], 'func': hcd_base_universe_d3_065_hcd_basefill_068}


def hcd_base_universe_d3_066_hcd_basefill_069(hcd_base_universe_d2_066_hcd_basefill_069):
    return _base_universe_d3(hcd_base_universe_d2_066_hcd_basefill_069, 66)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_066_hcd_basefill_069'] = {'inputs': ['hcd_base_universe_d2_066_hcd_basefill_069'], 'func': hcd_base_universe_d3_066_hcd_basefill_069}


def hcd_base_universe_d3_067_hcd_basefill_070(hcd_base_universe_d2_067_hcd_basefill_070):
    return _base_universe_d3(hcd_base_universe_d2_067_hcd_basefill_070, 67)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_067_hcd_basefill_070'] = {'inputs': ['hcd_base_universe_d2_067_hcd_basefill_070'], 'func': hcd_base_universe_d3_067_hcd_basefill_070}


def hcd_base_universe_d3_068_hcd_basefill_071(hcd_base_universe_d2_068_hcd_basefill_071):
    return _base_universe_d3(hcd_base_universe_d2_068_hcd_basefill_071, 68)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_068_hcd_basefill_071'] = {'inputs': ['hcd_base_universe_d2_068_hcd_basefill_071'], 'func': hcd_base_universe_d3_068_hcd_basefill_071}


def hcd_base_universe_d3_069_hcd_basefill_072(hcd_base_universe_d2_069_hcd_basefill_072):
    return _base_universe_d3(hcd_base_universe_d2_069_hcd_basefill_072, 69)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_069_hcd_basefill_072'] = {'inputs': ['hcd_base_universe_d2_069_hcd_basefill_072'], 'func': hcd_base_universe_d3_069_hcd_basefill_072}


def hcd_base_universe_d3_070_hcd_basefill_073(hcd_base_universe_d2_070_hcd_basefill_073):
    return _base_universe_d3(hcd_base_universe_d2_070_hcd_basefill_073, 70)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_070_hcd_basefill_073'] = {'inputs': ['hcd_base_universe_d2_070_hcd_basefill_073'], 'func': hcd_base_universe_d3_070_hcd_basefill_073}


def hcd_base_universe_d3_071_hcd_basefill_074(hcd_base_universe_d2_071_hcd_basefill_074):
    return _base_universe_d3(hcd_base_universe_d2_071_hcd_basefill_074, 71)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_071_hcd_basefill_074'] = {'inputs': ['hcd_base_universe_d2_071_hcd_basefill_074'], 'func': hcd_base_universe_d3_071_hcd_basefill_074}


def hcd_base_universe_d3_072_hcd_basefill_075(hcd_base_universe_d2_072_hcd_basefill_075):
    return _base_universe_d3(hcd_base_universe_d2_072_hcd_basefill_075, 72)
HCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['hcd_base_universe_d3_072_hcd_basefill_075'] = {'inputs': ['hcd_base_universe_d2_072_hcd_basefill_075'], 'func': hcd_base_universe_d3_072_hcd_basefill_075}
