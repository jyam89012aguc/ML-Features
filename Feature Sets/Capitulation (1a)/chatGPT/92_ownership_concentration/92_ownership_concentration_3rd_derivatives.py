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



def ocn_176_ocn_001_holder_exit_1_accel_1(ocn_151_ocn_001_holder_exit_1_roc_1):
    feature = _s(ocn_151_ocn_001_holder_exit_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ocn_177_ocn_007_holder_exit_1_accel_42(ocn_152_ocn_007_holder_exit_1_roc_42):
    feature = _s(ocn_152_ocn_007_holder_exit_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ocn_178_ocn_013_holder_exit_1_accel_126(ocn_153_ocn_013_holder_exit_1_roc_126):
    feature = _s(ocn_153_ocn_013_holder_exit_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ocn_179_ocn_019_holder_exit_1_accel_378(ocn_154_ocn_019_holder_exit_1_roc_378):
    feature = _s(ocn_154_ocn_019_holder_exit_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ocn_180_ocn_025_holder_exit_1_accel_4(ocn_155_ocn_025_holder_exit_1_roc_4):
    feature = _s(ocn_155_ocn_025_holder_exit_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















OWNERSHIP_CONCENTRATION_REGISTRY_3RD_DERIVATIVES = {
    'ocn_176_ocn_001_holder_exit_1_accel_1': {'inputs': ['ocn_151_ocn_001_holder_exit_1_roc_1'], 'func': ocn_176_ocn_001_holder_exit_1_accel_1},
    'ocn_177_ocn_007_holder_exit_1_accel_42': {'inputs': ['ocn_152_ocn_007_holder_exit_1_roc_42'], 'func': ocn_177_ocn_007_holder_exit_1_accel_42},
    'ocn_178_ocn_013_holder_exit_1_accel_126': {'inputs': ['ocn_153_ocn_013_holder_exit_1_roc_126'], 'func': ocn_178_ocn_013_holder_exit_1_accel_126},
    'ocn_179_ocn_019_holder_exit_1_accel_378': {'inputs': ['ocn_154_ocn_019_holder_exit_1_roc_378'], 'func': ocn_179_ocn_019_holder_exit_1_accel_378},
    'ocn_180_ocn_025_holder_exit_1_accel_4': {'inputs': ['ocn_155_ocn_025_holder_exit_1_roc_4'], 'func': ocn_180_ocn_025_holder_exit_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def oc_replacement_d3_001(oc_replacement_d2_001):
    feature = _clean(oc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_001'] = {'inputs': ['oc_replacement_d2_001'], 'func': oc_replacement_d3_001}


def oc_replacement_d3_002(oc_replacement_d2_002):
    feature = _clean(oc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_002'] = {'inputs': ['oc_replacement_d2_002'], 'func': oc_replacement_d3_002}


def oc_replacement_d3_003(oc_replacement_d2_003):
    feature = _clean(oc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_003'] = {'inputs': ['oc_replacement_d2_003'], 'func': oc_replacement_d3_003}


def oc_replacement_d3_004(oc_replacement_d2_004):
    feature = _clean(oc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_004'] = {'inputs': ['oc_replacement_d2_004'], 'func': oc_replacement_d3_004}


def oc_replacement_d3_005(oc_replacement_d2_005):
    feature = _clean(oc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_005'] = {'inputs': ['oc_replacement_d2_005'], 'func': oc_replacement_d3_005}


def oc_replacement_d3_006(oc_replacement_d2_006):
    feature = _clean(oc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_006'] = {'inputs': ['oc_replacement_d2_006'], 'func': oc_replacement_d3_006}


def oc_replacement_d3_007(oc_replacement_d2_007):
    feature = _clean(oc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_007'] = {'inputs': ['oc_replacement_d2_007'], 'func': oc_replacement_d3_007}


def oc_replacement_d3_008(oc_replacement_d2_008):
    feature = _clean(oc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_008'] = {'inputs': ['oc_replacement_d2_008'], 'func': oc_replacement_d3_008}


def oc_replacement_d3_009(oc_replacement_d2_009):
    feature = _clean(oc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_009'] = {'inputs': ['oc_replacement_d2_009'], 'func': oc_replacement_d3_009}


def oc_replacement_d3_010(oc_replacement_d2_010):
    feature = _clean(oc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_010'] = {'inputs': ['oc_replacement_d2_010'], 'func': oc_replacement_d3_010}


def oc_replacement_d3_011(oc_replacement_d2_011):
    feature = _clean(oc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_011'] = {'inputs': ['oc_replacement_d2_011'], 'func': oc_replacement_d3_011}


def oc_replacement_d3_012(oc_replacement_d2_012):
    feature = _clean(oc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_012'] = {'inputs': ['oc_replacement_d2_012'], 'func': oc_replacement_d3_012}


def oc_replacement_d3_013(oc_replacement_d2_013):
    feature = _clean(oc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_013'] = {'inputs': ['oc_replacement_d2_013'], 'func': oc_replacement_d3_013}


def oc_replacement_d3_014(oc_replacement_d2_014):
    feature = _clean(oc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_014'] = {'inputs': ['oc_replacement_d2_014'], 'func': oc_replacement_d3_014}


def oc_replacement_d3_015(oc_replacement_d2_015):
    feature = _clean(oc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_015'] = {'inputs': ['oc_replacement_d2_015'], 'func': oc_replacement_d3_015}


def oc_replacement_d3_016(oc_replacement_d2_016):
    feature = _clean(oc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_016'] = {'inputs': ['oc_replacement_d2_016'], 'func': oc_replacement_d3_016}


def oc_replacement_d3_017(oc_replacement_d2_017):
    feature = _clean(oc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_017'] = {'inputs': ['oc_replacement_d2_017'], 'func': oc_replacement_d3_017}


def oc_replacement_d3_018(oc_replacement_d2_018):
    feature = _clean(oc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_018'] = {'inputs': ['oc_replacement_d2_018'], 'func': oc_replacement_d3_018}


def oc_replacement_d3_019(oc_replacement_d2_019):
    feature = _clean(oc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_019'] = {'inputs': ['oc_replacement_d2_019'], 'func': oc_replacement_d3_019}


def oc_replacement_d3_020(oc_replacement_d2_020):
    feature = _clean(oc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_020'] = {'inputs': ['oc_replacement_d2_020'], 'func': oc_replacement_d3_020}


def oc_replacement_d3_021(oc_replacement_d2_021):
    feature = _clean(oc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_021'] = {'inputs': ['oc_replacement_d2_021'], 'func': oc_replacement_d3_021}


def oc_replacement_d3_022(oc_replacement_d2_022):
    feature = _clean(oc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_022'] = {'inputs': ['oc_replacement_d2_022'], 'func': oc_replacement_d3_022}


def oc_replacement_d3_023(oc_replacement_d2_023):
    feature = _clean(oc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_023'] = {'inputs': ['oc_replacement_d2_023'], 'func': oc_replacement_d3_023}


def oc_replacement_d3_024(oc_replacement_d2_024):
    feature = _clean(oc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_024'] = {'inputs': ['oc_replacement_d2_024'], 'func': oc_replacement_d3_024}


def oc_replacement_d3_025(oc_replacement_d2_025):
    feature = _clean(oc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_025'] = {'inputs': ['oc_replacement_d2_025'], 'func': oc_replacement_d3_025}


def oc_replacement_d3_026(oc_replacement_d2_026):
    feature = _clean(oc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_026'] = {'inputs': ['oc_replacement_d2_026'], 'func': oc_replacement_d3_026}


def oc_replacement_d3_027(oc_replacement_d2_027):
    feature = _clean(oc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_027'] = {'inputs': ['oc_replacement_d2_027'], 'func': oc_replacement_d3_027}


def oc_replacement_d3_028(oc_replacement_d2_028):
    feature = _clean(oc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_028'] = {'inputs': ['oc_replacement_d2_028'], 'func': oc_replacement_d3_028}


def oc_replacement_d3_029(oc_replacement_d2_029):
    feature = _clean(oc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_029'] = {'inputs': ['oc_replacement_d2_029'], 'func': oc_replacement_d3_029}


def oc_replacement_d3_030(oc_replacement_d2_030):
    feature = _clean(oc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_030'] = {'inputs': ['oc_replacement_d2_030'], 'func': oc_replacement_d3_030}


def oc_replacement_d3_031(oc_replacement_d2_031):
    feature = _clean(oc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_031'] = {'inputs': ['oc_replacement_d2_031'], 'func': oc_replacement_d3_031}


def oc_replacement_d3_032(oc_replacement_d2_032):
    feature = _clean(oc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_032'] = {'inputs': ['oc_replacement_d2_032'], 'func': oc_replacement_d3_032}


def oc_replacement_d3_033(oc_replacement_d2_033):
    feature = _clean(oc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_033'] = {'inputs': ['oc_replacement_d2_033'], 'func': oc_replacement_d3_033}


def oc_replacement_d3_034(oc_replacement_d2_034):
    feature = _clean(oc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_034'] = {'inputs': ['oc_replacement_d2_034'], 'func': oc_replacement_d3_034}


def oc_replacement_d3_035(oc_replacement_d2_035):
    feature = _clean(oc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_035'] = {'inputs': ['oc_replacement_d2_035'], 'func': oc_replacement_d3_035}


def oc_replacement_d3_036(oc_replacement_d2_036):
    feature = _clean(oc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_036'] = {'inputs': ['oc_replacement_d2_036'], 'func': oc_replacement_d3_036}


def oc_replacement_d3_037(oc_replacement_d2_037):
    feature = _clean(oc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_037'] = {'inputs': ['oc_replacement_d2_037'], 'func': oc_replacement_d3_037}


def oc_replacement_d3_038(oc_replacement_d2_038):
    feature = _clean(oc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_038'] = {'inputs': ['oc_replacement_d2_038'], 'func': oc_replacement_d3_038}


def oc_replacement_d3_039(oc_replacement_d2_039):
    feature = _clean(oc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_039'] = {'inputs': ['oc_replacement_d2_039'], 'func': oc_replacement_d3_039}


def oc_replacement_d3_040(oc_replacement_d2_040):
    feature = _clean(oc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_040'] = {'inputs': ['oc_replacement_d2_040'], 'func': oc_replacement_d3_040}


def oc_replacement_d3_041(oc_replacement_d2_041):
    feature = _clean(oc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_041'] = {'inputs': ['oc_replacement_d2_041'], 'func': oc_replacement_d3_041}


def oc_replacement_d3_042(oc_replacement_d2_042):
    feature = _clean(oc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_042'] = {'inputs': ['oc_replacement_d2_042'], 'func': oc_replacement_d3_042}


def oc_replacement_d3_043(oc_replacement_d2_043):
    feature = _clean(oc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_043'] = {'inputs': ['oc_replacement_d2_043'], 'func': oc_replacement_d3_043}


def oc_replacement_d3_044(oc_replacement_d2_044):
    feature = _clean(oc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_044'] = {'inputs': ['oc_replacement_d2_044'], 'func': oc_replacement_d3_044}


def oc_replacement_d3_045(oc_replacement_d2_045):
    feature = _clean(oc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_045'] = {'inputs': ['oc_replacement_d2_045'], 'func': oc_replacement_d3_045}


def oc_replacement_d3_046(oc_replacement_d2_046):
    feature = _clean(oc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_046'] = {'inputs': ['oc_replacement_d2_046'], 'func': oc_replacement_d3_046}


def oc_replacement_d3_047(oc_replacement_d2_047):
    feature = _clean(oc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_047'] = {'inputs': ['oc_replacement_d2_047'], 'func': oc_replacement_d3_047}


def oc_replacement_d3_048(oc_replacement_d2_048):
    feature = _clean(oc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_048'] = {'inputs': ['oc_replacement_d2_048'], 'func': oc_replacement_d3_048}


def oc_replacement_d3_049(oc_replacement_d2_049):
    feature = _clean(oc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_049'] = {'inputs': ['oc_replacement_d2_049'], 'func': oc_replacement_d3_049}


def oc_replacement_d3_050(oc_replacement_d2_050):
    feature = _clean(oc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_050'] = {'inputs': ['oc_replacement_d2_050'], 'func': oc_replacement_d3_050}


def oc_replacement_d3_051(oc_replacement_d2_051):
    feature = _clean(oc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_051'] = {'inputs': ['oc_replacement_d2_051'], 'func': oc_replacement_d3_051}


def oc_replacement_d3_052(oc_replacement_d2_052):
    feature = _clean(oc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_052'] = {'inputs': ['oc_replacement_d2_052'], 'func': oc_replacement_d3_052}


def oc_replacement_d3_053(oc_replacement_d2_053):
    feature = _clean(oc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_053'] = {'inputs': ['oc_replacement_d2_053'], 'func': oc_replacement_d3_053}


def oc_replacement_d3_054(oc_replacement_d2_054):
    feature = _clean(oc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_054'] = {'inputs': ['oc_replacement_d2_054'], 'func': oc_replacement_d3_054}


def oc_replacement_d3_055(oc_replacement_d2_055):
    feature = _clean(oc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_055'] = {'inputs': ['oc_replacement_d2_055'], 'func': oc_replacement_d3_055}


def oc_replacement_d3_056(oc_replacement_d2_056):
    feature = _clean(oc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_056'] = {'inputs': ['oc_replacement_d2_056'], 'func': oc_replacement_d3_056}


def oc_replacement_d3_057(oc_replacement_d2_057):
    feature = _clean(oc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_057'] = {'inputs': ['oc_replacement_d2_057'], 'func': oc_replacement_d3_057}


def oc_replacement_d3_058(oc_replacement_d2_058):
    feature = _clean(oc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_058'] = {'inputs': ['oc_replacement_d2_058'], 'func': oc_replacement_d3_058}


def oc_replacement_d3_059(oc_replacement_d2_059):
    feature = _clean(oc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_059'] = {'inputs': ['oc_replacement_d2_059'], 'func': oc_replacement_d3_059}


def oc_replacement_d3_060(oc_replacement_d2_060):
    feature = _clean(oc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_060'] = {'inputs': ['oc_replacement_d2_060'], 'func': oc_replacement_d3_060}


def oc_replacement_d3_061(oc_replacement_d2_061):
    feature = _clean(oc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_061'] = {'inputs': ['oc_replacement_d2_061'], 'func': oc_replacement_d3_061}


def oc_replacement_d3_062(oc_replacement_d2_062):
    feature = _clean(oc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_062'] = {'inputs': ['oc_replacement_d2_062'], 'func': oc_replacement_d3_062}


def oc_replacement_d3_063(oc_replacement_d2_063):
    feature = _clean(oc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_063'] = {'inputs': ['oc_replacement_d2_063'], 'func': oc_replacement_d3_063}


def oc_replacement_d3_064(oc_replacement_d2_064):
    feature = _clean(oc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_064'] = {'inputs': ['oc_replacement_d2_064'], 'func': oc_replacement_d3_064}


def oc_replacement_d3_065(oc_replacement_d2_065):
    feature = _clean(oc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_065'] = {'inputs': ['oc_replacement_d2_065'], 'func': oc_replacement_d3_065}


def oc_replacement_d3_066(oc_replacement_d2_066):
    feature = _clean(oc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_066'] = {'inputs': ['oc_replacement_d2_066'], 'func': oc_replacement_d3_066}


def oc_replacement_d3_067(oc_replacement_d2_067):
    feature = _clean(oc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_067'] = {'inputs': ['oc_replacement_d2_067'], 'func': oc_replacement_d3_067}


def oc_replacement_d3_068(oc_replacement_d2_068):
    feature = _clean(oc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_068'] = {'inputs': ['oc_replacement_d2_068'], 'func': oc_replacement_d3_068}


def oc_replacement_d3_069(oc_replacement_d2_069):
    feature = _clean(oc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_069'] = {'inputs': ['oc_replacement_d2_069'], 'func': oc_replacement_d3_069}


def oc_replacement_d3_070(oc_replacement_d2_070):
    feature = _clean(oc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_070'] = {'inputs': ['oc_replacement_d2_070'], 'func': oc_replacement_d3_070}


def oc_replacement_d3_071(oc_replacement_d2_071):
    feature = _clean(oc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_071'] = {'inputs': ['oc_replacement_d2_071'], 'func': oc_replacement_d3_071}


def oc_replacement_d3_072(oc_replacement_d2_072):
    feature = _clean(oc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_072'] = {'inputs': ['oc_replacement_d2_072'], 'func': oc_replacement_d3_072}


def oc_replacement_d3_073(oc_replacement_d2_073):
    feature = _clean(oc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_073'] = {'inputs': ['oc_replacement_d2_073'], 'func': oc_replacement_d3_073}


def oc_replacement_d3_074(oc_replacement_d2_074):
    feature = _clean(oc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_074'] = {'inputs': ['oc_replacement_d2_074'], 'func': oc_replacement_d3_074}


def oc_replacement_d3_075(oc_replacement_d2_075):
    feature = _clean(oc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_075'] = {'inputs': ['oc_replacement_d2_075'], 'func': oc_replacement_d3_075}


def oc_replacement_d3_076(oc_replacement_d2_076):
    feature = _clean(oc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_076'] = {'inputs': ['oc_replacement_d2_076'], 'func': oc_replacement_d3_076}


def oc_replacement_d3_077(oc_replacement_d2_077):
    feature = _clean(oc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_077'] = {'inputs': ['oc_replacement_d2_077'], 'func': oc_replacement_d3_077}


def oc_replacement_d3_078(oc_replacement_d2_078):
    feature = _clean(oc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_078'] = {'inputs': ['oc_replacement_d2_078'], 'func': oc_replacement_d3_078}


def oc_replacement_d3_079(oc_replacement_d2_079):
    feature = _clean(oc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_079'] = {'inputs': ['oc_replacement_d2_079'], 'func': oc_replacement_d3_079}


def oc_replacement_d3_080(oc_replacement_d2_080):
    feature = _clean(oc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_080'] = {'inputs': ['oc_replacement_d2_080'], 'func': oc_replacement_d3_080}


def oc_replacement_d3_081(oc_replacement_d2_081):
    feature = _clean(oc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_081'] = {'inputs': ['oc_replacement_d2_081'], 'func': oc_replacement_d3_081}


def oc_replacement_d3_082(oc_replacement_d2_082):
    feature = _clean(oc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_082'] = {'inputs': ['oc_replacement_d2_082'], 'func': oc_replacement_d3_082}


def oc_replacement_d3_083(oc_replacement_d2_083):
    feature = _clean(oc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_083'] = {'inputs': ['oc_replacement_d2_083'], 'func': oc_replacement_d3_083}


def oc_replacement_d3_084(oc_replacement_d2_084):
    feature = _clean(oc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_084'] = {'inputs': ['oc_replacement_d2_084'], 'func': oc_replacement_d3_084}


def oc_replacement_d3_085(oc_replacement_d2_085):
    feature = _clean(oc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_085'] = {'inputs': ['oc_replacement_d2_085'], 'func': oc_replacement_d3_085}


def oc_replacement_d3_086(oc_replacement_d2_086):
    feature = _clean(oc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_086'] = {'inputs': ['oc_replacement_d2_086'], 'func': oc_replacement_d3_086}


def oc_replacement_d3_087(oc_replacement_d2_087):
    feature = _clean(oc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_087'] = {'inputs': ['oc_replacement_d2_087'], 'func': oc_replacement_d3_087}


def oc_replacement_d3_088(oc_replacement_d2_088):
    feature = _clean(oc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_088'] = {'inputs': ['oc_replacement_d2_088'], 'func': oc_replacement_d3_088}


def oc_replacement_d3_089(oc_replacement_d2_089):
    feature = _clean(oc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_089'] = {'inputs': ['oc_replacement_d2_089'], 'func': oc_replacement_d3_089}


def oc_replacement_d3_090(oc_replacement_d2_090):
    feature = _clean(oc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_090'] = {'inputs': ['oc_replacement_d2_090'], 'func': oc_replacement_d3_090}


def oc_replacement_d3_091(oc_replacement_d2_091):
    feature = _clean(oc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_091'] = {'inputs': ['oc_replacement_d2_091'], 'func': oc_replacement_d3_091}


def oc_replacement_d3_092(oc_replacement_d2_092):
    feature = _clean(oc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_092'] = {'inputs': ['oc_replacement_d2_092'], 'func': oc_replacement_d3_092}


def oc_replacement_d3_093(oc_replacement_d2_093):
    feature = _clean(oc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_093'] = {'inputs': ['oc_replacement_d2_093'], 'func': oc_replacement_d3_093}


def oc_replacement_d3_094(oc_replacement_d2_094):
    feature = _clean(oc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_094'] = {'inputs': ['oc_replacement_d2_094'], 'func': oc_replacement_d3_094}


def oc_replacement_d3_095(oc_replacement_d2_095):
    feature = _clean(oc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_095'] = {'inputs': ['oc_replacement_d2_095'], 'func': oc_replacement_d3_095}


def oc_replacement_d3_096(oc_replacement_d2_096):
    feature = _clean(oc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_096'] = {'inputs': ['oc_replacement_d2_096'], 'func': oc_replacement_d3_096}


def oc_replacement_d3_097(oc_replacement_d2_097):
    feature = _clean(oc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_097'] = {'inputs': ['oc_replacement_d2_097'], 'func': oc_replacement_d3_097}


def oc_replacement_d3_098(oc_replacement_d2_098):
    feature = _clean(oc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_098'] = {'inputs': ['oc_replacement_d2_098'], 'func': oc_replacement_d3_098}


def oc_replacement_d3_099(oc_replacement_d2_099):
    feature = _clean(oc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_099'] = {'inputs': ['oc_replacement_d2_099'], 'func': oc_replacement_d3_099}


def oc_replacement_d3_100(oc_replacement_d2_100):
    feature = _clean(oc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_100'] = {'inputs': ['oc_replacement_d2_100'], 'func': oc_replacement_d3_100}


def oc_replacement_d3_101(oc_replacement_d2_101):
    feature = _clean(oc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_101'] = {'inputs': ['oc_replacement_d2_101'], 'func': oc_replacement_d3_101}


def oc_replacement_d3_102(oc_replacement_d2_102):
    feature = _clean(oc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_102'] = {'inputs': ['oc_replacement_d2_102'], 'func': oc_replacement_d3_102}


def oc_replacement_d3_103(oc_replacement_d2_103):
    feature = _clean(oc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_103'] = {'inputs': ['oc_replacement_d2_103'], 'func': oc_replacement_d3_103}


def oc_replacement_d3_104(oc_replacement_d2_104):
    feature = _clean(oc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_104'] = {'inputs': ['oc_replacement_d2_104'], 'func': oc_replacement_d3_104}


def oc_replacement_d3_105(oc_replacement_d2_105):
    feature = _clean(oc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_105'] = {'inputs': ['oc_replacement_d2_105'], 'func': oc_replacement_d3_105}


def oc_replacement_d3_106(oc_replacement_d2_106):
    feature = _clean(oc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_106'] = {'inputs': ['oc_replacement_d2_106'], 'func': oc_replacement_d3_106}


def oc_replacement_d3_107(oc_replacement_d2_107):
    feature = _clean(oc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_107'] = {'inputs': ['oc_replacement_d2_107'], 'func': oc_replacement_d3_107}


def oc_replacement_d3_108(oc_replacement_d2_108):
    feature = _clean(oc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_108'] = {'inputs': ['oc_replacement_d2_108'], 'func': oc_replacement_d3_108}


def oc_replacement_d3_109(oc_replacement_d2_109):
    feature = _clean(oc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_109'] = {'inputs': ['oc_replacement_d2_109'], 'func': oc_replacement_d3_109}


def oc_replacement_d3_110(oc_replacement_d2_110):
    feature = _clean(oc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_110'] = {'inputs': ['oc_replacement_d2_110'], 'func': oc_replacement_d3_110}


def oc_replacement_d3_111(oc_replacement_d2_111):
    feature = _clean(oc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_111'] = {'inputs': ['oc_replacement_d2_111'], 'func': oc_replacement_d3_111}


def oc_replacement_d3_112(oc_replacement_d2_112):
    feature = _clean(oc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_112'] = {'inputs': ['oc_replacement_d2_112'], 'func': oc_replacement_d3_112}


def oc_replacement_d3_113(oc_replacement_d2_113):
    feature = _clean(oc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_113'] = {'inputs': ['oc_replacement_d2_113'], 'func': oc_replacement_d3_113}


def oc_replacement_d3_114(oc_replacement_d2_114):
    feature = _clean(oc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_114'] = {'inputs': ['oc_replacement_d2_114'], 'func': oc_replacement_d3_114}


def oc_replacement_d3_115(oc_replacement_d2_115):
    feature = _clean(oc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_115'] = {'inputs': ['oc_replacement_d2_115'], 'func': oc_replacement_d3_115}


def oc_replacement_d3_116(oc_replacement_d2_116):
    feature = _clean(oc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_116'] = {'inputs': ['oc_replacement_d2_116'], 'func': oc_replacement_d3_116}


def oc_replacement_d3_117(oc_replacement_d2_117):
    feature = _clean(oc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_117'] = {'inputs': ['oc_replacement_d2_117'], 'func': oc_replacement_d3_117}


def oc_replacement_d3_118(oc_replacement_d2_118):
    feature = _clean(oc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_118'] = {'inputs': ['oc_replacement_d2_118'], 'func': oc_replacement_d3_118}


def oc_replacement_d3_119(oc_replacement_d2_119):
    feature = _clean(oc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_119'] = {'inputs': ['oc_replacement_d2_119'], 'func': oc_replacement_d3_119}


def oc_replacement_d3_120(oc_replacement_d2_120):
    feature = _clean(oc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_120'] = {'inputs': ['oc_replacement_d2_120'], 'func': oc_replacement_d3_120}


def oc_replacement_d3_121(oc_replacement_d2_121):
    feature = _clean(oc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_121'] = {'inputs': ['oc_replacement_d2_121'], 'func': oc_replacement_d3_121}


def oc_replacement_d3_122(oc_replacement_d2_122):
    feature = _clean(oc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_122'] = {'inputs': ['oc_replacement_d2_122'], 'func': oc_replacement_d3_122}


def oc_replacement_d3_123(oc_replacement_d2_123):
    feature = _clean(oc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_123'] = {'inputs': ['oc_replacement_d2_123'], 'func': oc_replacement_d3_123}


def oc_replacement_d3_124(oc_replacement_d2_124):
    feature = _clean(oc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_124'] = {'inputs': ['oc_replacement_d2_124'], 'func': oc_replacement_d3_124}


def oc_replacement_d3_125(oc_replacement_d2_125):
    feature = _clean(oc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_125'] = {'inputs': ['oc_replacement_d2_125'], 'func': oc_replacement_d3_125}


def oc_replacement_d3_126(oc_replacement_d2_126):
    feature = _clean(oc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_126'] = {'inputs': ['oc_replacement_d2_126'], 'func': oc_replacement_d3_126}


def oc_replacement_d3_127(oc_replacement_d2_127):
    feature = _clean(oc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_127'] = {'inputs': ['oc_replacement_d2_127'], 'func': oc_replacement_d3_127}


def oc_replacement_d3_128(oc_replacement_d2_128):
    feature = _clean(oc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_128'] = {'inputs': ['oc_replacement_d2_128'], 'func': oc_replacement_d3_128}


def oc_replacement_d3_129(oc_replacement_d2_129):
    feature = _clean(oc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_129'] = {'inputs': ['oc_replacement_d2_129'], 'func': oc_replacement_d3_129}


def oc_replacement_d3_130(oc_replacement_d2_130):
    feature = _clean(oc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_130'] = {'inputs': ['oc_replacement_d2_130'], 'func': oc_replacement_d3_130}


def oc_replacement_d3_131(oc_replacement_d2_131):
    feature = _clean(oc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_131'] = {'inputs': ['oc_replacement_d2_131'], 'func': oc_replacement_d3_131}


def oc_replacement_d3_132(oc_replacement_d2_132):
    feature = _clean(oc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_132'] = {'inputs': ['oc_replacement_d2_132'], 'func': oc_replacement_d3_132}


def oc_replacement_d3_133(oc_replacement_d2_133):
    feature = _clean(oc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_133'] = {'inputs': ['oc_replacement_d2_133'], 'func': oc_replacement_d3_133}


def oc_replacement_d3_134(oc_replacement_d2_134):
    feature = _clean(oc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_134'] = {'inputs': ['oc_replacement_d2_134'], 'func': oc_replacement_d3_134}


def oc_replacement_d3_135(oc_replacement_d2_135):
    feature = _clean(oc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_135'] = {'inputs': ['oc_replacement_d2_135'], 'func': oc_replacement_d3_135}


def oc_replacement_d3_136(oc_replacement_d2_136):
    feature = _clean(oc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_136'] = {'inputs': ['oc_replacement_d2_136'], 'func': oc_replacement_d3_136}


def oc_replacement_d3_137(oc_replacement_d2_137):
    feature = _clean(oc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_137'] = {'inputs': ['oc_replacement_d2_137'], 'func': oc_replacement_d3_137}


def oc_replacement_d3_138(oc_replacement_d2_138):
    feature = _clean(oc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_138'] = {'inputs': ['oc_replacement_d2_138'], 'func': oc_replacement_d3_138}


def oc_replacement_d3_139(oc_replacement_d2_139):
    feature = _clean(oc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_139'] = {'inputs': ['oc_replacement_d2_139'], 'func': oc_replacement_d3_139}


def oc_replacement_d3_140(oc_replacement_d2_140):
    feature = _clean(oc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_140'] = {'inputs': ['oc_replacement_d2_140'], 'func': oc_replacement_d3_140}


def oc_replacement_d3_141(oc_replacement_d2_141):
    feature = _clean(oc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_141'] = {'inputs': ['oc_replacement_d2_141'], 'func': oc_replacement_d3_141}


def oc_replacement_d3_142(oc_replacement_d2_142):
    feature = _clean(oc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_142'] = {'inputs': ['oc_replacement_d2_142'], 'func': oc_replacement_d3_142}


def oc_replacement_d3_143(oc_replacement_d2_143):
    feature = _clean(oc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_143'] = {'inputs': ['oc_replacement_d2_143'], 'func': oc_replacement_d3_143}


def oc_replacement_d3_144(oc_replacement_d2_144):
    feature = _clean(oc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_144'] = {'inputs': ['oc_replacement_d2_144'], 'func': oc_replacement_d3_144}


def oc_replacement_d3_145(oc_replacement_d2_145):
    feature = _clean(oc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_145'] = {'inputs': ['oc_replacement_d2_145'], 'func': oc_replacement_d3_145}


def oc_replacement_d3_146(oc_replacement_d2_146):
    feature = _clean(oc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_146'] = {'inputs': ['oc_replacement_d2_146'], 'func': oc_replacement_d3_146}


def oc_replacement_d3_147(oc_replacement_d2_147):
    feature = _clean(oc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_147'] = {'inputs': ['oc_replacement_d2_147'], 'func': oc_replacement_d3_147}


def oc_replacement_d3_148(oc_replacement_d2_148):
    feature = _clean(oc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_148'] = {'inputs': ['oc_replacement_d2_148'], 'func': oc_replacement_d3_148}


def oc_replacement_d3_149(oc_replacement_d2_149):
    feature = _clean(oc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_149'] = {'inputs': ['oc_replacement_d2_149'], 'func': oc_replacement_d3_149}


def oc_replacement_d3_150(oc_replacement_d2_150):
    feature = _clean(oc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_150'] = {'inputs': ['oc_replacement_d2_150'], 'func': oc_replacement_d3_150}


def oc_replacement_d3_151(oc_replacement_d2_151):
    feature = _clean(oc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_151'] = {'inputs': ['oc_replacement_d2_151'], 'func': oc_replacement_d3_151}


def oc_replacement_d3_152(oc_replacement_d2_152):
    feature = _clean(oc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_152'] = {'inputs': ['oc_replacement_d2_152'], 'func': oc_replacement_d3_152}


def oc_replacement_d3_153(oc_replacement_d2_153):
    feature = _clean(oc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_153'] = {'inputs': ['oc_replacement_d2_153'], 'func': oc_replacement_d3_153}


def oc_replacement_d3_154(oc_replacement_d2_154):
    feature = _clean(oc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_154'] = {'inputs': ['oc_replacement_d2_154'], 'func': oc_replacement_d3_154}


def oc_replacement_d3_155(oc_replacement_d2_155):
    feature = _clean(oc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_155'] = {'inputs': ['oc_replacement_d2_155'], 'func': oc_replacement_d3_155}


def oc_replacement_d3_156(oc_replacement_d2_156):
    feature = _clean(oc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_156'] = {'inputs': ['oc_replacement_d2_156'], 'func': oc_replacement_d3_156}


def oc_replacement_d3_157(oc_replacement_d2_157):
    feature = _clean(oc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_157'] = {'inputs': ['oc_replacement_d2_157'], 'func': oc_replacement_d3_157}


def oc_replacement_d3_158(oc_replacement_d2_158):
    feature = _clean(oc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_158'] = {'inputs': ['oc_replacement_d2_158'], 'func': oc_replacement_d3_158}


def oc_replacement_d3_159(oc_replacement_d2_159):
    feature = _clean(oc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_159'] = {'inputs': ['oc_replacement_d2_159'], 'func': oc_replacement_d3_159}


def oc_replacement_d3_160(oc_replacement_d2_160):
    feature = _clean(oc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_160'] = {'inputs': ['oc_replacement_d2_160'], 'func': oc_replacement_d3_160}


def oc_replacement_d3_161(oc_replacement_d2_161):
    feature = _clean(oc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_161'] = {'inputs': ['oc_replacement_d2_161'], 'func': oc_replacement_d3_161}


def oc_replacement_d3_162(oc_replacement_d2_162):
    feature = _clean(oc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_162'] = {'inputs': ['oc_replacement_d2_162'], 'func': oc_replacement_d3_162}


def oc_replacement_d3_163(oc_replacement_d2_163):
    feature = _clean(oc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_163'] = {'inputs': ['oc_replacement_d2_163'], 'func': oc_replacement_d3_163}


def oc_replacement_d3_164(oc_replacement_d2_164):
    feature = _clean(oc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_164'] = {'inputs': ['oc_replacement_d2_164'], 'func': oc_replacement_d3_164}


def oc_replacement_d3_165(oc_replacement_d2_165):
    feature = _clean(oc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_165'] = {'inputs': ['oc_replacement_d2_165'], 'func': oc_replacement_d3_165}


def oc_replacement_d3_166(oc_replacement_d2_166):
    feature = _clean(oc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_166'] = {'inputs': ['oc_replacement_d2_166'], 'func': oc_replacement_d3_166}


def oc_replacement_d3_167(oc_replacement_d2_167):
    feature = _clean(oc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_167'] = {'inputs': ['oc_replacement_d2_167'], 'func': oc_replacement_d3_167}


def oc_replacement_d3_168(oc_replacement_d2_168):
    feature = _clean(oc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_168'] = {'inputs': ['oc_replacement_d2_168'], 'func': oc_replacement_d3_168}


def oc_replacement_d3_169(oc_replacement_d2_169):
    feature = _clean(oc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_169'] = {'inputs': ['oc_replacement_d2_169'], 'func': oc_replacement_d3_169}


def oc_replacement_d3_170(oc_replacement_d2_170):
    feature = _clean(oc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
OC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oc_replacement_d3_170'] = {'inputs': ['oc_replacement_d2_170'], 'func': oc_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ocn_base_universe_d3_001_ocn_003_top_holder_concentration_63(ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63):
    return _base_universe_d3(ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63, 1)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_001_ocn_003_top_holder_concentration_63'] = {'inputs': ['ocn_base_universe_d2_001_ocn_003_top_holder_concentration_63'], 'func': ocn_base_universe_d3_001_ocn_003_top_holder_concentration_63}


def ocn_base_universe_d3_002_ocn_004_institutional_net_flow_84(ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84):
    return _base_universe_d3(ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84, 2)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_002_ocn_004_institutional_net_flow_84'] = {'inputs': ['ocn_base_universe_d2_002_ocn_004_institutional_net_flow_84'], 'func': ocn_base_universe_d3_002_ocn_004_institutional_net_flow_84}


def ocn_base_universe_d3_003_ocn_005_forced_selling_pressure_126(ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126):
    return _base_universe_d3(ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126, 3)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_003_ocn_005_forced_selling_pressure_126'] = {'inputs': ['ocn_base_universe_d2_003_ocn_005_forced_selling_pressure_126'], 'func': ocn_base_universe_d3_003_ocn_005_forced_selling_pressure_126}


def ocn_base_universe_d3_004_ocn_006_holder_base_volatility_189(ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189):
    return _base_universe_d3(ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189, 4)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_004_ocn_006_holder_base_volatility_189'] = {'inputs': ['ocn_base_universe_d2_004_ocn_006_holder_base_volatility_189'], 'func': ocn_base_universe_d3_004_ocn_006_holder_base_volatility_189}


def ocn_base_universe_d3_005_ocn_009_top_holder_concentration_504(ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504):
    return _base_universe_d3(ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504, 5)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_005_ocn_009_top_holder_concentration_504'] = {'inputs': ['ocn_base_universe_d2_005_ocn_009_top_holder_concentration_504'], 'func': ocn_base_universe_d3_005_ocn_009_top_holder_concentration_504}


def ocn_base_universe_d3_006_ocn_010_institutional_net_flow_756(ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756):
    return _base_universe_d3(ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756, 6)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_006_ocn_010_institutional_net_flow_756'] = {'inputs': ['ocn_base_universe_d2_006_ocn_010_institutional_net_flow_756'], 'func': ocn_base_universe_d3_006_ocn_010_institutional_net_flow_756}


def ocn_base_universe_d3_007_ocn_011_forced_selling_pressure_1008(ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008):
    return _base_universe_d3(ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008, 7)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_007_ocn_011_forced_selling_pressure_1008'] = {'inputs': ['ocn_base_universe_d2_007_ocn_011_forced_selling_pressure_1008'], 'func': ocn_base_universe_d3_007_ocn_011_forced_selling_pressure_1008}


def ocn_base_universe_d3_008_ocn_012_holder_base_volatility_1260(ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260):
    return _base_universe_d3(ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260, 8)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_008_ocn_012_holder_base_volatility_1260'] = {'inputs': ['ocn_base_universe_d2_008_ocn_012_holder_base_volatility_1260'], 'func': ocn_base_universe_d3_008_ocn_012_holder_base_volatility_1260}


def ocn_base_universe_d3_009_ocn_015_top_holder_concentration_252(ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252):
    return _base_universe_d3(ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252, 9)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_009_ocn_015_top_holder_concentration_252'] = {'inputs': ['ocn_base_universe_d2_009_ocn_015_top_holder_concentration_252'], 'func': ocn_base_universe_d3_009_ocn_015_top_holder_concentration_252}


def ocn_base_universe_d3_010_ocn_016_institutional_net_flow_21(ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21):
    return _base_universe_d3(ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21, 10)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_010_ocn_016_institutional_net_flow_21'] = {'inputs': ['ocn_base_universe_d2_010_ocn_016_institutional_net_flow_21'], 'func': ocn_base_universe_d3_010_ocn_016_institutional_net_flow_21}


def ocn_base_universe_d3_011_ocn_017_forced_selling_pressure_42(ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42):
    return _base_universe_d3(ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42, 11)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_011_ocn_017_forced_selling_pressure_42'] = {'inputs': ['ocn_base_universe_d2_011_ocn_017_forced_selling_pressure_42'], 'func': ocn_base_universe_d3_011_ocn_017_forced_selling_pressure_42}


def ocn_base_universe_d3_012_ocn_018_holder_base_volatility_63(ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63):
    return _base_universe_d3(ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63, 12)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_012_ocn_018_holder_base_volatility_63'] = {'inputs': ['ocn_base_universe_d2_012_ocn_018_holder_base_volatility_63'], 'func': ocn_base_universe_d3_012_ocn_018_holder_base_volatility_63}


def ocn_base_universe_d3_013_ocn_021_top_holder_concentration_189(ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189):
    return _base_universe_d3(ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189, 13)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_013_ocn_021_top_holder_concentration_189'] = {'inputs': ['ocn_base_universe_d2_013_ocn_021_top_holder_concentration_189'], 'func': ocn_base_universe_d3_013_ocn_021_top_holder_concentration_189}


def ocn_base_universe_d3_014_ocn_022_institutional_net_flow_252(ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252):
    return _base_universe_d3(ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252, 14)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_014_ocn_022_institutional_net_flow_252'] = {'inputs': ['ocn_base_universe_d2_014_ocn_022_institutional_net_flow_252'], 'func': ocn_base_universe_d3_014_ocn_022_institutional_net_flow_252}


def ocn_base_universe_d3_015_ocn_023_forced_selling_pressure_378(ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378):
    return _base_universe_d3(ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378, 15)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_015_ocn_023_forced_selling_pressure_378'] = {'inputs': ['ocn_base_universe_d2_015_ocn_023_forced_selling_pressure_378'], 'func': ocn_base_universe_d3_015_ocn_023_forced_selling_pressure_378}


def ocn_base_universe_d3_016_ocn_024_holder_base_volatility_504(ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504):
    return _base_universe_d3(ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504, 16)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_016_ocn_024_holder_base_volatility_504'] = {'inputs': ['ocn_base_universe_d2_016_ocn_024_holder_base_volatility_504'], 'func': ocn_base_universe_d3_016_ocn_024_holder_base_volatility_504}


def ocn_base_universe_d3_017_ocn_027_top_holder_concentration_1260(ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260):
    return _base_universe_d3(ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260, 17)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_017_ocn_027_top_holder_concentration_1260'] = {'inputs': ['ocn_base_universe_d2_017_ocn_027_top_holder_concentration_1260'], 'func': ocn_base_universe_d3_017_ocn_027_top_holder_concentration_1260}


def ocn_base_universe_d3_018_ocn_028_institutional_net_flow_1512(ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512):
    return _base_universe_d3(ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512, 18)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_018_ocn_028_institutional_net_flow_1512'] = {'inputs': ['ocn_base_universe_d2_018_ocn_028_institutional_net_flow_1512'], 'func': ocn_base_universe_d3_018_ocn_028_institutional_net_flow_1512}


def ocn_base_universe_d3_019_ocn_029_forced_selling_pressure_63(ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63):
    return _base_universe_d3(ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63, 19)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_019_ocn_029_forced_selling_pressure_63'] = {'inputs': ['ocn_base_universe_d2_019_ocn_029_forced_selling_pressure_63'], 'func': ocn_base_universe_d3_019_ocn_029_forced_selling_pressure_63}


def ocn_base_universe_d3_020_ocn_030_holder_base_volatility_252(ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252):
    return _base_universe_d3(ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252, 20)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_020_ocn_030_holder_base_volatility_252'] = {'inputs': ['ocn_base_universe_d2_020_ocn_030_holder_base_volatility_252'], 'func': ocn_base_universe_d3_020_ocn_030_holder_base_volatility_252}


def ocn_base_universe_d3_021_ocn_basefill_001(ocn_base_universe_d2_021_ocn_basefill_001):
    return _base_universe_d3(ocn_base_universe_d2_021_ocn_basefill_001, 21)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_021_ocn_basefill_001'] = {'inputs': ['ocn_base_universe_d2_021_ocn_basefill_001'], 'func': ocn_base_universe_d3_021_ocn_basefill_001}


def ocn_base_universe_d3_022_ocn_basefill_002(ocn_base_universe_d2_022_ocn_basefill_002):
    return _base_universe_d3(ocn_base_universe_d2_022_ocn_basefill_002, 22)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_022_ocn_basefill_002'] = {'inputs': ['ocn_base_universe_d2_022_ocn_basefill_002'], 'func': ocn_base_universe_d3_022_ocn_basefill_002}


def ocn_base_universe_d3_023_ocn_basefill_007(ocn_base_universe_d2_023_ocn_basefill_007):
    return _base_universe_d3(ocn_base_universe_d2_023_ocn_basefill_007, 23)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_023_ocn_basefill_007'] = {'inputs': ['ocn_base_universe_d2_023_ocn_basefill_007'], 'func': ocn_base_universe_d3_023_ocn_basefill_007}


def ocn_base_universe_d3_024_ocn_basefill_008(ocn_base_universe_d2_024_ocn_basefill_008):
    return _base_universe_d3(ocn_base_universe_d2_024_ocn_basefill_008, 24)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_024_ocn_basefill_008'] = {'inputs': ['ocn_base_universe_d2_024_ocn_basefill_008'], 'func': ocn_base_universe_d3_024_ocn_basefill_008}


def ocn_base_universe_d3_025_ocn_basefill_013(ocn_base_universe_d2_025_ocn_basefill_013):
    return _base_universe_d3(ocn_base_universe_d2_025_ocn_basefill_013, 25)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_025_ocn_basefill_013'] = {'inputs': ['ocn_base_universe_d2_025_ocn_basefill_013'], 'func': ocn_base_universe_d3_025_ocn_basefill_013}


def ocn_base_universe_d3_026_ocn_basefill_014(ocn_base_universe_d2_026_ocn_basefill_014):
    return _base_universe_d3(ocn_base_universe_d2_026_ocn_basefill_014, 26)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_026_ocn_basefill_014'] = {'inputs': ['ocn_base_universe_d2_026_ocn_basefill_014'], 'func': ocn_base_universe_d3_026_ocn_basefill_014}


def ocn_base_universe_d3_027_ocn_basefill_019(ocn_base_universe_d2_027_ocn_basefill_019):
    return _base_universe_d3(ocn_base_universe_d2_027_ocn_basefill_019, 27)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_027_ocn_basefill_019'] = {'inputs': ['ocn_base_universe_d2_027_ocn_basefill_019'], 'func': ocn_base_universe_d3_027_ocn_basefill_019}


def ocn_base_universe_d3_028_ocn_basefill_020(ocn_base_universe_d2_028_ocn_basefill_020):
    return _base_universe_d3(ocn_base_universe_d2_028_ocn_basefill_020, 28)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_028_ocn_basefill_020'] = {'inputs': ['ocn_base_universe_d2_028_ocn_basefill_020'], 'func': ocn_base_universe_d3_028_ocn_basefill_020}


def ocn_base_universe_d3_029_ocn_basefill_025(ocn_base_universe_d2_029_ocn_basefill_025):
    return _base_universe_d3(ocn_base_universe_d2_029_ocn_basefill_025, 29)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_029_ocn_basefill_025'] = {'inputs': ['ocn_base_universe_d2_029_ocn_basefill_025'], 'func': ocn_base_universe_d3_029_ocn_basefill_025}


def ocn_base_universe_d3_030_ocn_basefill_026(ocn_base_universe_d2_030_ocn_basefill_026):
    return _base_universe_d3(ocn_base_universe_d2_030_ocn_basefill_026, 30)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_030_ocn_basefill_026'] = {'inputs': ['ocn_base_universe_d2_030_ocn_basefill_026'], 'func': ocn_base_universe_d3_030_ocn_basefill_026}


def ocn_base_universe_d3_031_ocn_basefill_031(ocn_base_universe_d2_031_ocn_basefill_031):
    return _base_universe_d3(ocn_base_universe_d2_031_ocn_basefill_031, 31)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_031_ocn_basefill_031'] = {'inputs': ['ocn_base_universe_d2_031_ocn_basefill_031'], 'func': ocn_base_universe_d3_031_ocn_basefill_031}


def ocn_base_universe_d3_032_ocn_basefill_032(ocn_base_universe_d2_032_ocn_basefill_032):
    return _base_universe_d3(ocn_base_universe_d2_032_ocn_basefill_032, 32)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_032_ocn_basefill_032'] = {'inputs': ['ocn_base_universe_d2_032_ocn_basefill_032'], 'func': ocn_base_universe_d3_032_ocn_basefill_032}


def ocn_base_universe_d3_033_ocn_basefill_033(ocn_base_universe_d2_033_ocn_basefill_033):
    return _base_universe_d3(ocn_base_universe_d2_033_ocn_basefill_033, 33)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_033_ocn_basefill_033'] = {'inputs': ['ocn_base_universe_d2_033_ocn_basefill_033'], 'func': ocn_base_universe_d3_033_ocn_basefill_033}


def ocn_base_universe_d3_034_ocn_basefill_034(ocn_base_universe_d2_034_ocn_basefill_034):
    return _base_universe_d3(ocn_base_universe_d2_034_ocn_basefill_034, 34)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_034_ocn_basefill_034'] = {'inputs': ['ocn_base_universe_d2_034_ocn_basefill_034'], 'func': ocn_base_universe_d3_034_ocn_basefill_034}


def ocn_base_universe_d3_035_ocn_basefill_035(ocn_base_universe_d2_035_ocn_basefill_035):
    return _base_universe_d3(ocn_base_universe_d2_035_ocn_basefill_035, 35)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_035_ocn_basefill_035'] = {'inputs': ['ocn_base_universe_d2_035_ocn_basefill_035'], 'func': ocn_base_universe_d3_035_ocn_basefill_035}


def ocn_base_universe_d3_036_ocn_basefill_036(ocn_base_universe_d2_036_ocn_basefill_036):
    return _base_universe_d3(ocn_base_universe_d2_036_ocn_basefill_036, 36)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_036_ocn_basefill_036'] = {'inputs': ['ocn_base_universe_d2_036_ocn_basefill_036'], 'func': ocn_base_universe_d3_036_ocn_basefill_036}


def ocn_base_universe_d3_037_ocn_basefill_037(ocn_base_universe_d2_037_ocn_basefill_037):
    return _base_universe_d3(ocn_base_universe_d2_037_ocn_basefill_037, 37)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_037_ocn_basefill_037'] = {'inputs': ['ocn_base_universe_d2_037_ocn_basefill_037'], 'func': ocn_base_universe_d3_037_ocn_basefill_037}


def ocn_base_universe_d3_038_ocn_basefill_038(ocn_base_universe_d2_038_ocn_basefill_038):
    return _base_universe_d3(ocn_base_universe_d2_038_ocn_basefill_038, 38)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_038_ocn_basefill_038'] = {'inputs': ['ocn_base_universe_d2_038_ocn_basefill_038'], 'func': ocn_base_universe_d3_038_ocn_basefill_038}


def ocn_base_universe_d3_039_ocn_basefill_039(ocn_base_universe_d2_039_ocn_basefill_039):
    return _base_universe_d3(ocn_base_universe_d2_039_ocn_basefill_039, 39)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_039_ocn_basefill_039'] = {'inputs': ['ocn_base_universe_d2_039_ocn_basefill_039'], 'func': ocn_base_universe_d3_039_ocn_basefill_039}


def ocn_base_universe_d3_040_ocn_basefill_040(ocn_base_universe_d2_040_ocn_basefill_040):
    return _base_universe_d3(ocn_base_universe_d2_040_ocn_basefill_040, 40)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_040_ocn_basefill_040'] = {'inputs': ['ocn_base_universe_d2_040_ocn_basefill_040'], 'func': ocn_base_universe_d3_040_ocn_basefill_040}


def ocn_base_universe_d3_041_ocn_basefill_041(ocn_base_universe_d2_041_ocn_basefill_041):
    return _base_universe_d3(ocn_base_universe_d2_041_ocn_basefill_041, 41)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_041_ocn_basefill_041'] = {'inputs': ['ocn_base_universe_d2_041_ocn_basefill_041'], 'func': ocn_base_universe_d3_041_ocn_basefill_041}


def ocn_base_universe_d3_042_ocn_basefill_042(ocn_base_universe_d2_042_ocn_basefill_042):
    return _base_universe_d3(ocn_base_universe_d2_042_ocn_basefill_042, 42)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_042_ocn_basefill_042'] = {'inputs': ['ocn_base_universe_d2_042_ocn_basefill_042'], 'func': ocn_base_universe_d3_042_ocn_basefill_042}


def ocn_base_universe_d3_043_ocn_basefill_043(ocn_base_universe_d2_043_ocn_basefill_043):
    return _base_universe_d3(ocn_base_universe_d2_043_ocn_basefill_043, 43)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_043_ocn_basefill_043'] = {'inputs': ['ocn_base_universe_d2_043_ocn_basefill_043'], 'func': ocn_base_universe_d3_043_ocn_basefill_043}


def ocn_base_universe_d3_044_ocn_basefill_044(ocn_base_universe_d2_044_ocn_basefill_044):
    return _base_universe_d3(ocn_base_universe_d2_044_ocn_basefill_044, 44)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_044_ocn_basefill_044'] = {'inputs': ['ocn_base_universe_d2_044_ocn_basefill_044'], 'func': ocn_base_universe_d3_044_ocn_basefill_044}


def ocn_base_universe_d3_045_ocn_basefill_045(ocn_base_universe_d2_045_ocn_basefill_045):
    return _base_universe_d3(ocn_base_universe_d2_045_ocn_basefill_045, 45)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_045_ocn_basefill_045'] = {'inputs': ['ocn_base_universe_d2_045_ocn_basefill_045'], 'func': ocn_base_universe_d3_045_ocn_basefill_045}


def ocn_base_universe_d3_046_ocn_basefill_046(ocn_base_universe_d2_046_ocn_basefill_046):
    return _base_universe_d3(ocn_base_universe_d2_046_ocn_basefill_046, 46)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_046_ocn_basefill_046'] = {'inputs': ['ocn_base_universe_d2_046_ocn_basefill_046'], 'func': ocn_base_universe_d3_046_ocn_basefill_046}


def ocn_base_universe_d3_047_ocn_basefill_047(ocn_base_universe_d2_047_ocn_basefill_047):
    return _base_universe_d3(ocn_base_universe_d2_047_ocn_basefill_047, 47)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_047_ocn_basefill_047'] = {'inputs': ['ocn_base_universe_d2_047_ocn_basefill_047'], 'func': ocn_base_universe_d3_047_ocn_basefill_047}


def ocn_base_universe_d3_048_ocn_basefill_048(ocn_base_universe_d2_048_ocn_basefill_048):
    return _base_universe_d3(ocn_base_universe_d2_048_ocn_basefill_048, 48)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_048_ocn_basefill_048'] = {'inputs': ['ocn_base_universe_d2_048_ocn_basefill_048'], 'func': ocn_base_universe_d3_048_ocn_basefill_048}


def ocn_base_universe_d3_049_ocn_basefill_049(ocn_base_universe_d2_049_ocn_basefill_049):
    return _base_universe_d3(ocn_base_universe_d2_049_ocn_basefill_049, 49)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_049_ocn_basefill_049'] = {'inputs': ['ocn_base_universe_d2_049_ocn_basefill_049'], 'func': ocn_base_universe_d3_049_ocn_basefill_049}


def ocn_base_universe_d3_050_ocn_basefill_050(ocn_base_universe_d2_050_ocn_basefill_050):
    return _base_universe_d3(ocn_base_universe_d2_050_ocn_basefill_050, 50)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_050_ocn_basefill_050'] = {'inputs': ['ocn_base_universe_d2_050_ocn_basefill_050'], 'func': ocn_base_universe_d3_050_ocn_basefill_050}


def ocn_base_universe_d3_051_ocn_basefill_051(ocn_base_universe_d2_051_ocn_basefill_051):
    return _base_universe_d3(ocn_base_universe_d2_051_ocn_basefill_051, 51)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_051_ocn_basefill_051'] = {'inputs': ['ocn_base_universe_d2_051_ocn_basefill_051'], 'func': ocn_base_universe_d3_051_ocn_basefill_051}


def ocn_base_universe_d3_052_ocn_basefill_052(ocn_base_universe_d2_052_ocn_basefill_052):
    return _base_universe_d3(ocn_base_universe_d2_052_ocn_basefill_052, 52)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_052_ocn_basefill_052'] = {'inputs': ['ocn_base_universe_d2_052_ocn_basefill_052'], 'func': ocn_base_universe_d3_052_ocn_basefill_052}


def ocn_base_universe_d3_053_ocn_basefill_053(ocn_base_universe_d2_053_ocn_basefill_053):
    return _base_universe_d3(ocn_base_universe_d2_053_ocn_basefill_053, 53)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_053_ocn_basefill_053'] = {'inputs': ['ocn_base_universe_d2_053_ocn_basefill_053'], 'func': ocn_base_universe_d3_053_ocn_basefill_053}


def ocn_base_universe_d3_054_ocn_basefill_054(ocn_base_universe_d2_054_ocn_basefill_054):
    return _base_universe_d3(ocn_base_universe_d2_054_ocn_basefill_054, 54)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_054_ocn_basefill_054'] = {'inputs': ['ocn_base_universe_d2_054_ocn_basefill_054'], 'func': ocn_base_universe_d3_054_ocn_basefill_054}


def ocn_base_universe_d3_055_ocn_basefill_055(ocn_base_universe_d2_055_ocn_basefill_055):
    return _base_universe_d3(ocn_base_universe_d2_055_ocn_basefill_055, 55)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_055_ocn_basefill_055'] = {'inputs': ['ocn_base_universe_d2_055_ocn_basefill_055'], 'func': ocn_base_universe_d3_055_ocn_basefill_055}


def ocn_base_universe_d3_056_ocn_basefill_056(ocn_base_universe_d2_056_ocn_basefill_056):
    return _base_universe_d3(ocn_base_universe_d2_056_ocn_basefill_056, 56)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_056_ocn_basefill_056'] = {'inputs': ['ocn_base_universe_d2_056_ocn_basefill_056'], 'func': ocn_base_universe_d3_056_ocn_basefill_056}


def ocn_base_universe_d3_057_ocn_basefill_057(ocn_base_universe_d2_057_ocn_basefill_057):
    return _base_universe_d3(ocn_base_universe_d2_057_ocn_basefill_057, 57)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_057_ocn_basefill_057'] = {'inputs': ['ocn_base_universe_d2_057_ocn_basefill_057'], 'func': ocn_base_universe_d3_057_ocn_basefill_057}


def ocn_base_universe_d3_058_ocn_basefill_058(ocn_base_universe_d2_058_ocn_basefill_058):
    return _base_universe_d3(ocn_base_universe_d2_058_ocn_basefill_058, 58)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_058_ocn_basefill_058'] = {'inputs': ['ocn_base_universe_d2_058_ocn_basefill_058'], 'func': ocn_base_universe_d3_058_ocn_basefill_058}


def ocn_base_universe_d3_059_ocn_basefill_059(ocn_base_universe_d2_059_ocn_basefill_059):
    return _base_universe_d3(ocn_base_universe_d2_059_ocn_basefill_059, 59)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_059_ocn_basefill_059'] = {'inputs': ['ocn_base_universe_d2_059_ocn_basefill_059'], 'func': ocn_base_universe_d3_059_ocn_basefill_059}


def ocn_base_universe_d3_060_ocn_basefill_060(ocn_base_universe_d2_060_ocn_basefill_060):
    return _base_universe_d3(ocn_base_universe_d2_060_ocn_basefill_060, 60)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_060_ocn_basefill_060'] = {'inputs': ['ocn_base_universe_d2_060_ocn_basefill_060'], 'func': ocn_base_universe_d3_060_ocn_basefill_060}


def ocn_base_universe_d3_061_ocn_basefill_061(ocn_base_universe_d2_061_ocn_basefill_061):
    return _base_universe_d3(ocn_base_universe_d2_061_ocn_basefill_061, 61)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_061_ocn_basefill_061'] = {'inputs': ['ocn_base_universe_d2_061_ocn_basefill_061'], 'func': ocn_base_universe_d3_061_ocn_basefill_061}


def ocn_base_universe_d3_062_ocn_basefill_062(ocn_base_universe_d2_062_ocn_basefill_062):
    return _base_universe_d3(ocn_base_universe_d2_062_ocn_basefill_062, 62)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_062_ocn_basefill_062'] = {'inputs': ['ocn_base_universe_d2_062_ocn_basefill_062'], 'func': ocn_base_universe_d3_062_ocn_basefill_062}


def ocn_base_universe_d3_063_ocn_basefill_063(ocn_base_universe_d2_063_ocn_basefill_063):
    return _base_universe_d3(ocn_base_universe_d2_063_ocn_basefill_063, 63)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_063_ocn_basefill_063'] = {'inputs': ['ocn_base_universe_d2_063_ocn_basefill_063'], 'func': ocn_base_universe_d3_063_ocn_basefill_063}


def ocn_base_universe_d3_064_ocn_basefill_064(ocn_base_universe_d2_064_ocn_basefill_064):
    return _base_universe_d3(ocn_base_universe_d2_064_ocn_basefill_064, 64)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_064_ocn_basefill_064'] = {'inputs': ['ocn_base_universe_d2_064_ocn_basefill_064'], 'func': ocn_base_universe_d3_064_ocn_basefill_064}


def ocn_base_universe_d3_065_ocn_basefill_065(ocn_base_universe_d2_065_ocn_basefill_065):
    return _base_universe_d3(ocn_base_universe_d2_065_ocn_basefill_065, 65)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_065_ocn_basefill_065'] = {'inputs': ['ocn_base_universe_d2_065_ocn_basefill_065'], 'func': ocn_base_universe_d3_065_ocn_basefill_065}


def ocn_base_universe_d3_066_ocn_basefill_066(ocn_base_universe_d2_066_ocn_basefill_066):
    return _base_universe_d3(ocn_base_universe_d2_066_ocn_basefill_066, 66)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_066_ocn_basefill_066'] = {'inputs': ['ocn_base_universe_d2_066_ocn_basefill_066'], 'func': ocn_base_universe_d3_066_ocn_basefill_066}


def ocn_base_universe_d3_067_ocn_basefill_067(ocn_base_universe_d2_067_ocn_basefill_067):
    return _base_universe_d3(ocn_base_universe_d2_067_ocn_basefill_067, 67)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_067_ocn_basefill_067'] = {'inputs': ['ocn_base_universe_d2_067_ocn_basefill_067'], 'func': ocn_base_universe_d3_067_ocn_basefill_067}


def ocn_base_universe_d3_068_ocn_basefill_068(ocn_base_universe_d2_068_ocn_basefill_068):
    return _base_universe_d3(ocn_base_universe_d2_068_ocn_basefill_068, 68)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_068_ocn_basefill_068'] = {'inputs': ['ocn_base_universe_d2_068_ocn_basefill_068'], 'func': ocn_base_universe_d3_068_ocn_basefill_068}


def ocn_base_universe_d3_069_ocn_basefill_069(ocn_base_universe_d2_069_ocn_basefill_069):
    return _base_universe_d3(ocn_base_universe_d2_069_ocn_basefill_069, 69)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_069_ocn_basefill_069'] = {'inputs': ['ocn_base_universe_d2_069_ocn_basefill_069'], 'func': ocn_base_universe_d3_069_ocn_basefill_069}


def ocn_base_universe_d3_070_ocn_basefill_070(ocn_base_universe_d2_070_ocn_basefill_070):
    return _base_universe_d3(ocn_base_universe_d2_070_ocn_basefill_070, 70)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_070_ocn_basefill_070'] = {'inputs': ['ocn_base_universe_d2_070_ocn_basefill_070'], 'func': ocn_base_universe_d3_070_ocn_basefill_070}


def ocn_base_universe_d3_071_ocn_basefill_071(ocn_base_universe_d2_071_ocn_basefill_071):
    return _base_universe_d3(ocn_base_universe_d2_071_ocn_basefill_071, 71)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_071_ocn_basefill_071'] = {'inputs': ['ocn_base_universe_d2_071_ocn_basefill_071'], 'func': ocn_base_universe_d3_071_ocn_basefill_071}


def ocn_base_universe_d3_072_ocn_basefill_072(ocn_base_universe_d2_072_ocn_basefill_072):
    return _base_universe_d3(ocn_base_universe_d2_072_ocn_basefill_072, 72)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_072_ocn_basefill_072'] = {'inputs': ['ocn_base_universe_d2_072_ocn_basefill_072'], 'func': ocn_base_universe_d3_072_ocn_basefill_072}


def ocn_base_universe_d3_073_ocn_basefill_073(ocn_base_universe_d2_073_ocn_basefill_073):
    return _base_universe_d3(ocn_base_universe_d2_073_ocn_basefill_073, 73)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_073_ocn_basefill_073'] = {'inputs': ['ocn_base_universe_d2_073_ocn_basefill_073'], 'func': ocn_base_universe_d3_073_ocn_basefill_073}


def ocn_base_universe_d3_074_ocn_basefill_074(ocn_base_universe_d2_074_ocn_basefill_074):
    return _base_universe_d3(ocn_base_universe_d2_074_ocn_basefill_074, 74)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_074_ocn_basefill_074'] = {'inputs': ['ocn_base_universe_d2_074_ocn_basefill_074'], 'func': ocn_base_universe_d3_074_ocn_basefill_074}


def ocn_base_universe_d3_075_ocn_basefill_075(ocn_base_universe_d2_075_ocn_basefill_075):
    return _base_universe_d3(ocn_base_universe_d2_075_ocn_basefill_075, 75)
OCN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocn_base_universe_d3_075_ocn_basefill_075'] = {'inputs': ['ocn_base_universe_d2_075_ocn_basefill_075'], 'func': ocn_base_universe_d3_075_ocn_basefill_075}
