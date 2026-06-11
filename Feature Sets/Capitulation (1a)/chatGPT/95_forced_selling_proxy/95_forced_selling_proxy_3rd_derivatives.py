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



def fsp_176_fsp_001_holder_exit_1_accel_1(fsp_151_fsp_001_holder_exit_1_roc_1):
    feature = _s(fsp_151_fsp_001_holder_exit_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def fsp_177_fsp_007_holder_exit_1_accel_42(fsp_152_fsp_007_holder_exit_1_roc_42):
    feature = _s(fsp_152_fsp_007_holder_exit_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def fsp_178_fsp_013_holder_exit_1_accel_126(fsp_153_fsp_013_holder_exit_1_roc_126):
    feature = _s(fsp_153_fsp_013_holder_exit_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def fsp_179_fsp_019_holder_exit_1_accel_378(fsp_154_fsp_019_holder_exit_1_roc_378):
    feature = _s(fsp_154_fsp_019_holder_exit_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def fsp_180_fsp_025_holder_exit_1_accel_4(fsp_155_fsp_025_holder_exit_1_roc_4):
    feature = _s(fsp_155_fsp_025_holder_exit_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















FORCED_SELLING_PROXY_REGISTRY_3RD_DERIVATIVES = {
    'fsp_176_fsp_001_holder_exit_1_accel_1': {'inputs': ['fsp_151_fsp_001_holder_exit_1_roc_1'], 'func': fsp_176_fsp_001_holder_exit_1_accel_1},
    'fsp_177_fsp_007_holder_exit_1_accel_42': {'inputs': ['fsp_152_fsp_007_holder_exit_1_roc_42'], 'func': fsp_177_fsp_007_holder_exit_1_accel_42},
    'fsp_178_fsp_013_holder_exit_1_accel_126': {'inputs': ['fsp_153_fsp_013_holder_exit_1_roc_126'], 'func': fsp_178_fsp_013_holder_exit_1_accel_126},
    'fsp_179_fsp_019_holder_exit_1_accel_378': {'inputs': ['fsp_154_fsp_019_holder_exit_1_roc_378'], 'func': fsp_179_fsp_019_holder_exit_1_accel_378},
    'fsp_180_fsp_025_holder_exit_1_accel_4': {'inputs': ['fsp_155_fsp_025_holder_exit_1_roc_4'], 'func': fsp_180_fsp_025_holder_exit_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def fsp_replacement_d3_001(fsp_replacement_d2_001):
    feature = _clean(fsp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_001'] = {'inputs': ['fsp_replacement_d2_001'], 'func': fsp_replacement_d3_001}


def fsp_replacement_d3_002(fsp_replacement_d2_002):
    feature = _clean(fsp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_002'] = {'inputs': ['fsp_replacement_d2_002'], 'func': fsp_replacement_d3_002}


def fsp_replacement_d3_003(fsp_replacement_d2_003):
    feature = _clean(fsp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_003'] = {'inputs': ['fsp_replacement_d2_003'], 'func': fsp_replacement_d3_003}


def fsp_replacement_d3_004(fsp_replacement_d2_004):
    feature = _clean(fsp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_004'] = {'inputs': ['fsp_replacement_d2_004'], 'func': fsp_replacement_d3_004}


def fsp_replacement_d3_005(fsp_replacement_d2_005):
    feature = _clean(fsp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_005'] = {'inputs': ['fsp_replacement_d2_005'], 'func': fsp_replacement_d3_005}


def fsp_replacement_d3_006(fsp_replacement_d2_006):
    feature = _clean(fsp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_006'] = {'inputs': ['fsp_replacement_d2_006'], 'func': fsp_replacement_d3_006}


def fsp_replacement_d3_007(fsp_replacement_d2_007):
    feature = _clean(fsp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_007'] = {'inputs': ['fsp_replacement_d2_007'], 'func': fsp_replacement_d3_007}


def fsp_replacement_d3_008(fsp_replacement_d2_008):
    feature = _clean(fsp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_008'] = {'inputs': ['fsp_replacement_d2_008'], 'func': fsp_replacement_d3_008}


def fsp_replacement_d3_009(fsp_replacement_d2_009):
    feature = _clean(fsp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_009'] = {'inputs': ['fsp_replacement_d2_009'], 'func': fsp_replacement_d3_009}


def fsp_replacement_d3_010(fsp_replacement_d2_010):
    feature = _clean(fsp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_010'] = {'inputs': ['fsp_replacement_d2_010'], 'func': fsp_replacement_d3_010}


def fsp_replacement_d3_011(fsp_replacement_d2_011):
    feature = _clean(fsp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_011'] = {'inputs': ['fsp_replacement_d2_011'], 'func': fsp_replacement_d3_011}


def fsp_replacement_d3_012(fsp_replacement_d2_012):
    feature = _clean(fsp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_012'] = {'inputs': ['fsp_replacement_d2_012'], 'func': fsp_replacement_d3_012}


def fsp_replacement_d3_013(fsp_replacement_d2_013):
    feature = _clean(fsp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_013'] = {'inputs': ['fsp_replacement_d2_013'], 'func': fsp_replacement_d3_013}


def fsp_replacement_d3_014(fsp_replacement_d2_014):
    feature = _clean(fsp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_014'] = {'inputs': ['fsp_replacement_d2_014'], 'func': fsp_replacement_d3_014}


def fsp_replacement_d3_015(fsp_replacement_d2_015):
    feature = _clean(fsp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_015'] = {'inputs': ['fsp_replacement_d2_015'], 'func': fsp_replacement_d3_015}


def fsp_replacement_d3_016(fsp_replacement_d2_016):
    feature = _clean(fsp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_016'] = {'inputs': ['fsp_replacement_d2_016'], 'func': fsp_replacement_d3_016}


def fsp_replacement_d3_017(fsp_replacement_d2_017):
    feature = _clean(fsp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_017'] = {'inputs': ['fsp_replacement_d2_017'], 'func': fsp_replacement_d3_017}


def fsp_replacement_d3_018(fsp_replacement_d2_018):
    feature = _clean(fsp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_018'] = {'inputs': ['fsp_replacement_d2_018'], 'func': fsp_replacement_d3_018}


def fsp_replacement_d3_019(fsp_replacement_d2_019):
    feature = _clean(fsp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_019'] = {'inputs': ['fsp_replacement_d2_019'], 'func': fsp_replacement_d3_019}


def fsp_replacement_d3_020(fsp_replacement_d2_020):
    feature = _clean(fsp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_020'] = {'inputs': ['fsp_replacement_d2_020'], 'func': fsp_replacement_d3_020}


def fsp_replacement_d3_021(fsp_replacement_d2_021):
    feature = _clean(fsp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_021'] = {'inputs': ['fsp_replacement_d2_021'], 'func': fsp_replacement_d3_021}


def fsp_replacement_d3_022(fsp_replacement_d2_022):
    feature = _clean(fsp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_022'] = {'inputs': ['fsp_replacement_d2_022'], 'func': fsp_replacement_d3_022}


def fsp_replacement_d3_023(fsp_replacement_d2_023):
    feature = _clean(fsp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_023'] = {'inputs': ['fsp_replacement_d2_023'], 'func': fsp_replacement_d3_023}


def fsp_replacement_d3_024(fsp_replacement_d2_024):
    feature = _clean(fsp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_024'] = {'inputs': ['fsp_replacement_d2_024'], 'func': fsp_replacement_d3_024}


def fsp_replacement_d3_025(fsp_replacement_d2_025):
    feature = _clean(fsp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_025'] = {'inputs': ['fsp_replacement_d2_025'], 'func': fsp_replacement_d3_025}


def fsp_replacement_d3_026(fsp_replacement_d2_026):
    feature = _clean(fsp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_026'] = {'inputs': ['fsp_replacement_d2_026'], 'func': fsp_replacement_d3_026}


def fsp_replacement_d3_027(fsp_replacement_d2_027):
    feature = _clean(fsp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_027'] = {'inputs': ['fsp_replacement_d2_027'], 'func': fsp_replacement_d3_027}


def fsp_replacement_d3_028(fsp_replacement_d2_028):
    feature = _clean(fsp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_028'] = {'inputs': ['fsp_replacement_d2_028'], 'func': fsp_replacement_d3_028}


def fsp_replacement_d3_029(fsp_replacement_d2_029):
    feature = _clean(fsp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_029'] = {'inputs': ['fsp_replacement_d2_029'], 'func': fsp_replacement_d3_029}


def fsp_replacement_d3_030(fsp_replacement_d2_030):
    feature = _clean(fsp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_030'] = {'inputs': ['fsp_replacement_d2_030'], 'func': fsp_replacement_d3_030}


def fsp_replacement_d3_031(fsp_replacement_d2_031):
    feature = _clean(fsp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_031'] = {'inputs': ['fsp_replacement_d2_031'], 'func': fsp_replacement_d3_031}


def fsp_replacement_d3_032(fsp_replacement_d2_032):
    feature = _clean(fsp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_032'] = {'inputs': ['fsp_replacement_d2_032'], 'func': fsp_replacement_d3_032}


def fsp_replacement_d3_033(fsp_replacement_d2_033):
    feature = _clean(fsp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_033'] = {'inputs': ['fsp_replacement_d2_033'], 'func': fsp_replacement_d3_033}


def fsp_replacement_d3_034(fsp_replacement_d2_034):
    feature = _clean(fsp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_034'] = {'inputs': ['fsp_replacement_d2_034'], 'func': fsp_replacement_d3_034}


def fsp_replacement_d3_035(fsp_replacement_d2_035):
    feature = _clean(fsp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_035'] = {'inputs': ['fsp_replacement_d2_035'], 'func': fsp_replacement_d3_035}


def fsp_replacement_d3_036(fsp_replacement_d2_036):
    feature = _clean(fsp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_036'] = {'inputs': ['fsp_replacement_d2_036'], 'func': fsp_replacement_d3_036}


def fsp_replacement_d3_037(fsp_replacement_d2_037):
    feature = _clean(fsp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_037'] = {'inputs': ['fsp_replacement_d2_037'], 'func': fsp_replacement_d3_037}


def fsp_replacement_d3_038(fsp_replacement_d2_038):
    feature = _clean(fsp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_038'] = {'inputs': ['fsp_replacement_d2_038'], 'func': fsp_replacement_d3_038}


def fsp_replacement_d3_039(fsp_replacement_d2_039):
    feature = _clean(fsp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_039'] = {'inputs': ['fsp_replacement_d2_039'], 'func': fsp_replacement_d3_039}


def fsp_replacement_d3_040(fsp_replacement_d2_040):
    feature = _clean(fsp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_040'] = {'inputs': ['fsp_replacement_d2_040'], 'func': fsp_replacement_d3_040}


def fsp_replacement_d3_041(fsp_replacement_d2_041):
    feature = _clean(fsp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_041'] = {'inputs': ['fsp_replacement_d2_041'], 'func': fsp_replacement_d3_041}


def fsp_replacement_d3_042(fsp_replacement_d2_042):
    feature = _clean(fsp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_042'] = {'inputs': ['fsp_replacement_d2_042'], 'func': fsp_replacement_d3_042}


def fsp_replacement_d3_043(fsp_replacement_d2_043):
    feature = _clean(fsp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_043'] = {'inputs': ['fsp_replacement_d2_043'], 'func': fsp_replacement_d3_043}


def fsp_replacement_d3_044(fsp_replacement_d2_044):
    feature = _clean(fsp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_044'] = {'inputs': ['fsp_replacement_d2_044'], 'func': fsp_replacement_d3_044}


def fsp_replacement_d3_045(fsp_replacement_d2_045):
    feature = _clean(fsp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_045'] = {'inputs': ['fsp_replacement_d2_045'], 'func': fsp_replacement_d3_045}


def fsp_replacement_d3_046(fsp_replacement_d2_046):
    feature = _clean(fsp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_046'] = {'inputs': ['fsp_replacement_d2_046'], 'func': fsp_replacement_d3_046}


def fsp_replacement_d3_047(fsp_replacement_d2_047):
    feature = _clean(fsp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_047'] = {'inputs': ['fsp_replacement_d2_047'], 'func': fsp_replacement_d3_047}


def fsp_replacement_d3_048(fsp_replacement_d2_048):
    feature = _clean(fsp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_048'] = {'inputs': ['fsp_replacement_d2_048'], 'func': fsp_replacement_d3_048}


def fsp_replacement_d3_049(fsp_replacement_d2_049):
    feature = _clean(fsp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_049'] = {'inputs': ['fsp_replacement_d2_049'], 'func': fsp_replacement_d3_049}


def fsp_replacement_d3_050(fsp_replacement_d2_050):
    feature = _clean(fsp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_050'] = {'inputs': ['fsp_replacement_d2_050'], 'func': fsp_replacement_d3_050}


def fsp_replacement_d3_051(fsp_replacement_d2_051):
    feature = _clean(fsp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_051'] = {'inputs': ['fsp_replacement_d2_051'], 'func': fsp_replacement_d3_051}


def fsp_replacement_d3_052(fsp_replacement_d2_052):
    feature = _clean(fsp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_052'] = {'inputs': ['fsp_replacement_d2_052'], 'func': fsp_replacement_d3_052}


def fsp_replacement_d3_053(fsp_replacement_d2_053):
    feature = _clean(fsp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_053'] = {'inputs': ['fsp_replacement_d2_053'], 'func': fsp_replacement_d3_053}


def fsp_replacement_d3_054(fsp_replacement_d2_054):
    feature = _clean(fsp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_054'] = {'inputs': ['fsp_replacement_d2_054'], 'func': fsp_replacement_d3_054}


def fsp_replacement_d3_055(fsp_replacement_d2_055):
    feature = _clean(fsp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_055'] = {'inputs': ['fsp_replacement_d2_055'], 'func': fsp_replacement_d3_055}


def fsp_replacement_d3_056(fsp_replacement_d2_056):
    feature = _clean(fsp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_056'] = {'inputs': ['fsp_replacement_d2_056'], 'func': fsp_replacement_d3_056}


def fsp_replacement_d3_057(fsp_replacement_d2_057):
    feature = _clean(fsp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_057'] = {'inputs': ['fsp_replacement_d2_057'], 'func': fsp_replacement_d3_057}


def fsp_replacement_d3_058(fsp_replacement_d2_058):
    feature = _clean(fsp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_058'] = {'inputs': ['fsp_replacement_d2_058'], 'func': fsp_replacement_d3_058}


def fsp_replacement_d3_059(fsp_replacement_d2_059):
    feature = _clean(fsp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_059'] = {'inputs': ['fsp_replacement_d2_059'], 'func': fsp_replacement_d3_059}


def fsp_replacement_d3_060(fsp_replacement_d2_060):
    feature = _clean(fsp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_060'] = {'inputs': ['fsp_replacement_d2_060'], 'func': fsp_replacement_d3_060}


def fsp_replacement_d3_061(fsp_replacement_d2_061):
    feature = _clean(fsp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_061'] = {'inputs': ['fsp_replacement_d2_061'], 'func': fsp_replacement_d3_061}


def fsp_replacement_d3_062(fsp_replacement_d2_062):
    feature = _clean(fsp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_062'] = {'inputs': ['fsp_replacement_d2_062'], 'func': fsp_replacement_d3_062}


def fsp_replacement_d3_063(fsp_replacement_d2_063):
    feature = _clean(fsp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_063'] = {'inputs': ['fsp_replacement_d2_063'], 'func': fsp_replacement_d3_063}


def fsp_replacement_d3_064(fsp_replacement_d2_064):
    feature = _clean(fsp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_064'] = {'inputs': ['fsp_replacement_d2_064'], 'func': fsp_replacement_d3_064}


def fsp_replacement_d3_065(fsp_replacement_d2_065):
    feature = _clean(fsp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_065'] = {'inputs': ['fsp_replacement_d2_065'], 'func': fsp_replacement_d3_065}


def fsp_replacement_d3_066(fsp_replacement_d2_066):
    feature = _clean(fsp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_066'] = {'inputs': ['fsp_replacement_d2_066'], 'func': fsp_replacement_d3_066}


def fsp_replacement_d3_067(fsp_replacement_d2_067):
    feature = _clean(fsp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_067'] = {'inputs': ['fsp_replacement_d2_067'], 'func': fsp_replacement_d3_067}


def fsp_replacement_d3_068(fsp_replacement_d2_068):
    feature = _clean(fsp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_068'] = {'inputs': ['fsp_replacement_d2_068'], 'func': fsp_replacement_d3_068}


def fsp_replacement_d3_069(fsp_replacement_d2_069):
    feature = _clean(fsp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_069'] = {'inputs': ['fsp_replacement_d2_069'], 'func': fsp_replacement_d3_069}


def fsp_replacement_d3_070(fsp_replacement_d2_070):
    feature = _clean(fsp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_070'] = {'inputs': ['fsp_replacement_d2_070'], 'func': fsp_replacement_d3_070}


def fsp_replacement_d3_071(fsp_replacement_d2_071):
    feature = _clean(fsp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_071'] = {'inputs': ['fsp_replacement_d2_071'], 'func': fsp_replacement_d3_071}


def fsp_replacement_d3_072(fsp_replacement_d2_072):
    feature = _clean(fsp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_072'] = {'inputs': ['fsp_replacement_d2_072'], 'func': fsp_replacement_d3_072}


def fsp_replacement_d3_073(fsp_replacement_d2_073):
    feature = _clean(fsp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_073'] = {'inputs': ['fsp_replacement_d2_073'], 'func': fsp_replacement_d3_073}


def fsp_replacement_d3_074(fsp_replacement_d2_074):
    feature = _clean(fsp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_074'] = {'inputs': ['fsp_replacement_d2_074'], 'func': fsp_replacement_d3_074}


def fsp_replacement_d3_075(fsp_replacement_d2_075):
    feature = _clean(fsp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_075'] = {'inputs': ['fsp_replacement_d2_075'], 'func': fsp_replacement_d3_075}


def fsp_replacement_d3_076(fsp_replacement_d2_076):
    feature = _clean(fsp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_076'] = {'inputs': ['fsp_replacement_d2_076'], 'func': fsp_replacement_d3_076}


def fsp_replacement_d3_077(fsp_replacement_d2_077):
    feature = _clean(fsp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_077'] = {'inputs': ['fsp_replacement_d2_077'], 'func': fsp_replacement_d3_077}


def fsp_replacement_d3_078(fsp_replacement_d2_078):
    feature = _clean(fsp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_078'] = {'inputs': ['fsp_replacement_d2_078'], 'func': fsp_replacement_d3_078}


def fsp_replacement_d3_079(fsp_replacement_d2_079):
    feature = _clean(fsp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_079'] = {'inputs': ['fsp_replacement_d2_079'], 'func': fsp_replacement_d3_079}


def fsp_replacement_d3_080(fsp_replacement_d2_080):
    feature = _clean(fsp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_080'] = {'inputs': ['fsp_replacement_d2_080'], 'func': fsp_replacement_d3_080}


def fsp_replacement_d3_081(fsp_replacement_d2_081):
    feature = _clean(fsp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_081'] = {'inputs': ['fsp_replacement_d2_081'], 'func': fsp_replacement_d3_081}


def fsp_replacement_d3_082(fsp_replacement_d2_082):
    feature = _clean(fsp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_082'] = {'inputs': ['fsp_replacement_d2_082'], 'func': fsp_replacement_d3_082}


def fsp_replacement_d3_083(fsp_replacement_d2_083):
    feature = _clean(fsp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_083'] = {'inputs': ['fsp_replacement_d2_083'], 'func': fsp_replacement_d3_083}


def fsp_replacement_d3_084(fsp_replacement_d2_084):
    feature = _clean(fsp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_084'] = {'inputs': ['fsp_replacement_d2_084'], 'func': fsp_replacement_d3_084}


def fsp_replacement_d3_085(fsp_replacement_d2_085):
    feature = _clean(fsp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_085'] = {'inputs': ['fsp_replacement_d2_085'], 'func': fsp_replacement_d3_085}


def fsp_replacement_d3_086(fsp_replacement_d2_086):
    feature = _clean(fsp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_086'] = {'inputs': ['fsp_replacement_d2_086'], 'func': fsp_replacement_d3_086}


def fsp_replacement_d3_087(fsp_replacement_d2_087):
    feature = _clean(fsp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_087'] = {'inputs': ['fsp_replacement_d2_087'], 'func': fsp_replacement_d3_087}


def fsp_replacement_d3_088(fsp_replacement_d2_088):
    feature = _clean(fsp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_088'] = {'inputs': ['fsp_replacement_d2_088'], 'func': fsp_replacement_d3_088}


def fsp_replacement_d3_089(fsp_replacement_d2_089):
    feature = _clean(fsp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_089'] = {'inputs': ['fsp_replacement_d2_089'], 'func': fsp_replacement_d3_089}


def fsp_replacement_d3_090(fsp_replacement_d2_090):
    feature = _clean(fsp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_090'] = {'inputs': ['fsp_replacement_d2_090'], 'func': fsp_replacement_d3_090}


def fsp_replacement_d3_091(fsp_replacement_d2_091):
    feature = _clean(fsp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_091'] = {'inputs': ['fsp_replacement_d2_091'], 'func': fsp_replacement_d3_091}


def fsp_replacement_d3_092(fsp_replacement_d2_092):
    feature = _clean(fsp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_092'] = {'inputs': ['fsp_replacement_d2_092'], 'func': fsp_replacement_d3_092}


def fsp_replacement_d3_093(fsp_replacement_d2_093):
    feature = _clean(fsp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_093'] = {'inputs': ['fsp_replacement_d2_093'], 'func': fsp_replacement_d3_093}


def fsp_replacement_d3_094(fsp_replacement_d2_094):
    feature = _clean(fsp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_094'] = {'inputs': ['fsp_replacement_d2_094'], 'func': fsp_replacement_d3_094}


def fsp_replacement_d3_095(fsp_replacement_d2_095):
    feature = _clean(fsp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_095'] = {'inputs': ['fsp_replacement_d2_095'], 'func': fsp_replacement_d3_095}


def fsp_replacement_d3_096(fsp_replacement_d2_096):
    feature = _clean(fsp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_096'] = {'inputs': ['fsp_replacement_d2_096'], 'func': fsp_replacement_d3_096}


def fsp_replacement_d3_097(fsp_replacement_d2_097):
    feature = _clean(fsp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_097'] = {'inputs': ['fsp_replacement_d2_097'], 'func': fsp_replacement_d3_097}


def fsp_replacement_d3_098(fsp_replacement_d2_098):
    feature = _clean(fsp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_098'] = {'inputs': ['fsp_replacement_d2_098'], 'func': fsp_replacement_d3_098}


def fsp_replacement_d3_099(fsp_replacement_d2_099):
    feature = _clean(fsp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_099'] = {'inputs': ['fsp_replacement_d2_099'], 'func': fsp_replacement_d3_099}


def fsp_replacement_d3_100(fsp_replacement_d2_100):
    feature = _clean(fsp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_100'] = {'inputs': ['fsp_replacement_d2_100'], 'func': fsp_replacement_d3_100}


def fsp_replacement_d3_101(fsp_replacement_d2_101):
    feature = _clean(fsp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_101'] = {'inputs': ['fsp_replacement_d2_101'], 'func': fsp_replacement_d3_101}


def fsp_replacement_d3_102(fsp_replacement_d2_102):
    feature = _clean(fsp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_102'] = {'inputs': ['fsp_replacement_d2_102'], 'func': fsp_replacement_d3_102}


def fsp_replacement_d3_103(fsp_replacement_d2_103):
    feature = _clean(fsp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_103'] = {'inputs': ['fsp_replacement_d2_103'], 'func': fsp_replacement_d3_103}


def fsp_replacement_d3_104(fsp_replacement_d2_104):
    feature = _clean(fsp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_104'] = {'inputs': ['fsp_replacement_d2_104'], 'func': fsp_replacement_d3_104}


def fsp_replacement_d3_105(fsp_replacement_d2_105):
    feature = _clean(fsp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_105'] = {'inputs': ['fsp_replacement_d2_105'], 'func': fsp_replacement_d3_105}


def fsp_replacement_d3_106(fsp_replacement_d2_106):
    feature = _clean(fsp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_106'] = {'inputs': ['fsp_replacement_d2_106'], 'func': fsp_replacement_d3_106}


def fsp_replacement_d3_107(fsp_replacement_d2_107):
    feature = _clean(fsp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_107'] = {'inputs': ['fsp_replacement_d2_107'], 'func': fsp_replacement_d3_107}


def fsp_replacement_d3_108(fsp_replacement_d2_108):
    feature = _clean(fsp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_108'] = {'inputs': ['fsp_replacement_d2_108'], 'func': fsp_replacement_d3_108}


def fsp_replacement_d3_109(fsp_replacement_d2_109):
    feature = _clean(fsp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_109'] = {'inputs': ['fsp_replacement_d2_109'], 'func': fsp_replacement_d3_109}


def fsp_replacement_d3_110(fsp_replacement_d2_110):
    feature = _clean(fsp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_110'] = {'inputs': ['fsp_replacement_d2_110'], 'func': fsp_replacement_d3_110}


def fsp_replacement_d3_111(fsp_replacement_d2_111):
    feature = _clean(fsp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_111'] = {'inputs': ['fsp_replacement_d2_111'], 'func': fsp_replacement_d3_111}


def fsp_replacement_d3_112(fsp_replacement_d2_112):
    feature = _clean(fsp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_112'] = {'inputs': ['fsp_replacement_d2_112'], 'func': fsp_replacement_d3_112}


def fsp_replacement_d3_113(fsp_replacement_d2_113):
    feature = _clean(fsp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_113'] = {'inputs': ['fsp_replacement_d2_113'], 'func': fsp_replacement_d3_113}


def fsp_replacement_d3_114(fsp_replacement_d2_114):
    feature = _clean(fsp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_114'] = {'inputs': ['fsp_replacement_d2_114'], 'func': fsp_replacement_d3_114}


def fsp_replacement_d3_115(fsp_replacement_d2_115):
    feature = _clean(fsp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_115'] = {'inputs': ['fsp_replacement_d2_115'], 'func': fsp_replacement_d3_115}


def fsp_replacement_d3_116(fsp_replacement_d2_116):
    feature = _clean(fsp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_116'] = {'inputs': ['fsp_replacement_d2_116'], 'func': fsp_replacement_d3_116}


def fsp_replacement_d3_117(fsp_replacement_d2_117):
    feature = _clean(fsp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_117'] = {'inputs': ['fsp_replacement_d2_117'], 'func': fsp_replacement_d3_117}


def fsp_replacement_d3_118(fsp_replacement_d2_118):
    feature = _clean(fsp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_118'] = {'inputs': ['fsp_replacement_d2_118'], 'func': fsp_replacement_d3_118}


def fsp_replacement_d3_119(fsp_replacement_d2_119):
    feature = _clean(fsp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_119'] = {'inputs': ['fsp_replacement_d2_119'], 'func': fsp_replacement_d3_119}


def fsp_replacement_d3_120(fsp_replacement_d2_120):
    feature = _clean(fsp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_120'] = {'inputs': ['fsp_replacement_d2_120'], 'func': fsp_replacement_d3_120}


def fsp_replacement_d3_121(fsp_replacement_d2_121):
    feature = _clean(fsp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_121'] = {'inputs': ['fsp_replacement_d2_121'], 'func': fsp_replacement_d3_121}


def fsp_replacement_d3_122(fsp_replacement_d2_122):
    feature = _clean(fsp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_122'] = {'inputs': ['fsp_replacement_d2_122'], 'func': fsp_replacement_d3_122}


def fsp_replacement_d3_123(fsp_replacement_d2_123):
    feature = _clean(fsp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_123'] = {'inputs': ['fsp_replacement_d2_123'], 'func': fsp_replacement_d3_123}


def fsp_replacement_d3_124(fsp_replacement_d2_124):
    feature = _clean(fsp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_124'] = {'inputs': ['fsp_replacement_d2_124'], 'func': fsp_replacement_d3_124}


def fsp_replacement_d3_125(fsp_replacement_d2_125):
    feature = _clean(fsp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_125'] = {'inputs': ['fsp_replacement_d2_125'], 'func': fsp_replacement_d3_125}


def fsp_replacement_d3_126(fsp_replacement_d2_126):
    feature = _clean(fsp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_126'] = {'inputs': ['fsp_replacement_d2_126'], 'func': fsp_replacement_d3_126}


def fsp_replacement_d3_127(fsp_replacement_d2_127):
    feature = _clean(fsp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_127'] = {'inputs': ['fsp_replacement_d2_127'], 'func': fsp_replacement_d3_127}


def fsp_replacement_d3_128(fsp_replacement_d2_128):
    feature = _clean(fsp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_128'] = {'inputs': ['fsp_replacement_d2_128'], 'func': fsp_replacement_d3_128}


def fsp_replacement_d3_129(fsp_replacement_d2_129):
    feature = _clean(fsp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_129'] = {'inputs': ['fsp_replacement_d2_129'], 'func': fsp_replacement_d3_129}


def fsp_replacement_d3_130(fsp_replacement_d2_130):
    feature = _clean(fsp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_130'] = {'inputs': ['fsp_replacement_d2_130'], 'func': fsp_replacement_d3_130}


def fsp_replacement_d3_131(fsp_replacement_d2_131):
    feature = _clean(fsp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_131'] = {'inputs': ['fsp_replacement_d2_131'], 'func': fsp_replacement_d3_131}


def fsp_replacement_d3_132(fsp_replacement_d2_132):
    feature = _clean(fsp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_132'] = {'inputs': ['fsp_replacement_d2_132'], 'func': fsp_replacement_d3_132}


def fsp_replacement_d3_133(fsp_replacement_d2_133):
    feature = _clean(fsp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_133'] = {'inputs': ['fsp_replacement_d2_133'], 'func': fsp_replacement_d3_133}


def fsp_replacement_d3_134(fsp_replacement_d2_134):
    feature = _clean(fsp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_134'] = {'inputs': ['fsp_replacement_d2_134'], 'func': fsp_replacement_d3_134}


def fsp_replacement_d3_135(fsp_replacement_d2_135):
    feature = _clean(fsp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_135'] = {'inputs': ['fsp_replacement_d2_135'], 'func': fsp_replacement_d3_135}


def fsp_replacement_d3_136(fsp_replacement_d2_136):
    feature = _clean(fsp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_136'] = {'inputs': ['fsp_replacement_d2_136'], 'func': fsp_replacement_d3_136}


def fsp_replacement_d3_137(fsp_replacement_d2_137):
    feature = _clean(fsp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_137'] = {'inputs': ['fsp_replacement_d2_137'], 'func': fsp_replacement_d3_137}


def fsp_replacement_d3_138(fsp_replacement_d2_138):
    feature = _clean(fsp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_138'] = {'inputs': ['fsp_replacement_d2_138'], 'func': fsp_replacement_d3_138}


def fsp_replacement_d3_139(fsp_replacement_d2_139):
    feature = _clean(fsp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_139'] = {'inputs': ['fsp_replacement_d2_139'], 'func': fsp_replacement_d3_139}


def fsp_replacement_d3_140(fsp_replacement_d2_140):
    feature = _clean(fsp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_140'] = {'inputs': ['fsp_replacement_d2_140'], 'func': fsp_replacement_d3_140}


def fsp_replacement_d3_141(fsp_replacement_d2_141):
    feature = _clean(fsp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_141'] = {'inputs': ['fsp_replacement_d2_141'], 'func': fsp_replacement_d3_141}


def fsp_replacement_d3_142(fsp_replacement_d2_142):
    feature = _clean(fsp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_142'] = {'inputs': ['fsp_replacement_d2_142'], 'func': fsp_replacement_d3_142}


def fsp_replacement_d3_143(fsp_replacement_d2_143):
    feature = _clean(fsp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_143'] = {'inputs': ['fsp_replacement_d2_143'], 'func': fsp_replacement_d3_143}


def fsp_replacement_d3_144(fsp_replacement_d2_144):
    feature = _clean(fsp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_144'] = {'inputs': ['fsp_replacement_d2_144'], 'func': fsp_replacement_d3_144}


def fsp_replacement_d3_145(fsp_replacement_d2_145):
    feature = _clean(fsp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_145'] = {'inputs': ['fsp_replacement_d2_145'], 'func': fsp_replacement_d3_145}


def fsp_replacement_d3_146(fsp_replacement_d2_146):
    feature = _clean(fsp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_146'] = {'inputs': ['fsp_replacement_d2_146'], 'func': fsp_replacement_d3_146}


def fsp_replacement_d3_147(fsp_replacement_d2_147):
    feature = _clean(fsp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_147'] = {'inputs': ['fsp_replacement_d2_147'], 'func': fsp_replacement_d3_147}


def fsp_replacement_d3_148(fsp_replacement_d2_148):
    feature = _clean(fsp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_148'] = {'inputs': ['fsp_replacement_d2_148'], 'func': fsp_replacement_d3_148}


def fsp_replacement_d3_149(fsp_replacement_d2_149):
    feature = _clean(fsp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_149'] = {'inputs': ['fsp_replacement_d2_149'], 'func': fsp_replacement_d3_149}


def fsp_replacement_d3_150(fsp_replacement_d2_150):
    feature = _clean(fsp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_150'] = {'inputs': ['fsp_replacement_d2_150'], 'func': fsp_replacement_d3_150}


def fsp_replacement_d3_151(fsp_replacement_d2_151):
    feature = _clean(fsp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_151'] = {'inputs': ['fsp_replacement_d2_151'], 'func': fsp_replacement_d3_151}


def fsp_replacement_d3_152(fsp_replacement_d2_152):
    feature = _clean(fsp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_152'] = {'inputs': ['fsp_replacement_d2_152'], 'func': fsp_replacement_d3_152}


def fsp_replacement_d3_153(fsp_replacement_d2_153):
    feature = _clean(fsp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_153'] = {'inputs': ['fsp_replacement_d2_153'], 'func': fsp_replacement_d3_153}


def fsp_replacement_d3_154(fsp_replacement_d2_154):
    feature = _clean(fsp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_154'] = {'inputs': ['fsp_replacement_d2_154'], 'func': fsp_replacement_d3_154}


def fsp_replacement_d3_155(fsp_replacement_d2_155):
    feature = _clean(fsp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_155'] = {'inputs': ['fsp_replacement_d2_155'], 'func': fsp_replacement_d3_155}


def fsp_replacement_d3_156(fsp_replacement_d2_156):
    feature = _clean(fsp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_156'] = {'inputs': ['fsp_replacement_d2_156'], 'func': fsp_replacement_d3_156}


def fsp_replacement_d3_157(fsp_replacement_d2_157):
    feature = _clean(fsp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_157'] = {'inputs': ['fsp_replacement_d2_157'], 'func': fsp_replacement_d3_157}


def fsp_replacement_d3_158(fsp_replacement_d2_158):
    feature = _clean(fsp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_158'] = {'inputs': ['fsp_replacement_d2_158'], 'func': fsp_replacement_d3_158}


def fsp_replacement_d3_159(fsp_replacement_d2_159):
    feature = _clean(fsp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_159'] = {'inputs': ['fsp_replacement_d2_159'], 'func': fsp_replacement_d3_159}


def fsp_replacement_d3_160(fsp_replacement_d2_160):
    feature = _clean(fsp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_160'] = {'inputs': ['fsp_replacement_d2_160'], 'func': fsp_replacement_d3_160}


def fsp_replacement_d3_161(fsp_replacement_d2_161):
    feature = _clean(fsp_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_161'] = {'inputs': ['fsp_replacement_d2_161'], 'func': fsp_replacement_d3_161}


def fsp_replacement_d3_162(fsp_replacement_d2_162):
    feature = _clean(fsp_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_162'] = {'inputs': ['fsp_replacement_d2_162'], 'func': fsp_replacement_d3_162}


def fsp_replacement_d3_163(fsp_replacement_d2_163):
    feature = _clean(fsp_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_163'] = {'inputs': ['fsp_replacement_d2_163'], 'func': fsp_replacement_d3_163}


def fsp_replacement_d3_164(fsp_replacement_d2_164):
    feature = _clean(fsp_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_164'] = {'inputs': ['fsp_replacement_d2_164'], 'func': fsp_replacement_d3_164}


def fsp_replacement_d3_165(fsp_replacement_d2_165):
    feature = _clean(fsp_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_165'] = {'inputs': ['fsp_replacement_d2_165'], 'func': fsp_replacement_d3_165}


def fsp_replacement_d3_166(fsp_replacement_d2_166):
    feature = _clean(fsp_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_166'] = {'inputs': ['fsp_replacement_d2_166'], 'func': fsp_replacement_d3_166}


def fsp_replacement_d3_167(fsp_replacement_d2_167):
    feature = _clean(fsp_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_167'] = {'inputs': ['fsp_replacement_d2_167'], 'func': fsp_replacement_d3_167}


def fsp_replacement_d3_168(fsp_replacement_d2_168):
    feature = _clean(fsp_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_168'] = {'inputs': ['fsp_replacement_d2_168'], 'func': fsp_replacement_d3_168}


def fsp_replacement_d3_169(fsp_replacement_d2_169):
    feature = _clean(fsp_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_169'] = {'inputs': ['fsp_replacement_d2_169'], 'func': fsp_replacement_d3_169}


def fsp_replacement_d3_170(fsp_replacement_d2_170):
    feature = _clean(fsp_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
FSP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['fsp_replacement_d3_170'] = {'inputs': ['fsp_replacement_d2_170'], 'func': fsp_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def fsp_base_universe_d3_001_fsp_003_top_holder_concentration_63(fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63):
    return _base_universe_d3(fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63, 1)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_001_fsp_003_top_holder_concentration_63'] = {'inputs': ['fsp_base_universe_d2_001_fsp_003_top_holder_concentration_63'], 'func': fsp_base_universe_d3_001_fsp_003_top_holder_concentration_63}


def fsp_base_universe_d3_002_fsp_004_institutional_net_flow_84(fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84):
    return _base_universe_d3(fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84, 2)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_002_fsp_004_institutional_net_flow_84'] = {'inputs': ['fsp_base_universe_d2_002_fsp_004_institutional_net_flow_84'], 'func': fsp_base_universe_d3_002_fsp_004_institutional_net_flow_84}


def fsp_base_universe_d3_003_fsp_005_forced_selling_pressure_126(fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126):
    return _base_universe_d3(fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126, 3)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_003_fsp_005_forced_selling_pressure_126'] = {'inputs': ['fsp_base_universe_d2_003_fsp_005_forced_selling_pressure_126'], 'func': fsp_base_universe_d3_003_fsp_005_forced_selling_pressure_126}


def fsp_base_universe_d3_004_fsp_006_holder_base_volatility_189(fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189):
    return _base_universe_d3(fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189, 4)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_004_fsp_006_holder_base_volatility_189'] = {'inputs': ['fsp_base_universe_d2_004_fsp_006_holder_base_volatility_189'], 'func': fsp_base_universe_d3_004_fsp_006_holder_base_volatility_189}


def fsp_base_universe_d3_005_fsp_009_top_holder_concentration_504(fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504):
    return _base_universe_d3(fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504, 5)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_005_fsp_009_top_holder_concentration_504'] = {'inputs': ['fsp_base_universe_d2_005_fsp_009_top_holder_concentration_504'], 'func': fsp_base_universe_d3_005_fsp_009_top_holder_concentration_504}


def fsp_base_universe_d3_006_fsp_010_institutional_net_flow_756(fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756):
    return _base_universe_d3(fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756, 6)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_006_fsp_010_institutional_net_flow_756'] = {'inputs': ['fsp_base_universe_d2_006_fsp_010_institutional_net_flow_756'], 'func': fsp_base_universe_d3_006_fsp_010_institutional_net_flow_756}


def fsp_base_universe_d3_007_fsp_011_forced_selling_pressure_1008(fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008):
    return _base_universe_d3(fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008, 7)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_007_fsp_011_forced_selling_pressure_1008'] = {'inputs': ['fsp_base_universe_d2_007_fsp_011_forced_selling_pressure_1008'], 'func': fsp_base_universe_d3_007_fsp_011_forced_selling_pressure_1008}


def fsp_base_universe_d3_008_fsp_012_holder_base_volatility_1260(fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260):
    return _base_universe_d3(fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260, 8)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_008_fsp_012_holder_base_volatility_1260'] = {'inputs': ['fsp_base_universe_d2_008_fsp_012_holder_base_volatility_1260'], 'func': fsp_base_universe_d3_008_fsp_012_holder_base_volatility_1260}


def fsp_base_universe_d3_009_fsp_015_top_holder_concentration_252(fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252):
    return _base_universe_d3(fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252, 9)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_009_fsp_015_top_holder_concentration_252'] = {'inputs': ['fsp_base_universe_d2_009_fsp_015_top_holder_concentration_252'], 'func': fsp_base_universe_d3_009_fsp_015_top_holder_concentration_252}


def fsp_base_universe_d3_010_fsp_016_institutional_net_flow_21(fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21):
    return _base_universe_d3(fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21, 10)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_010_fsp_016_institutional_net_flow_21'] = {'inputs': ['fsp_base_universe_d2_010_fsp_016_institutional_net_flow_21'], 'func': fsp_base_universe_d3_010_fsp_016_institutional_net_flow_21}


def fsp_base_universe_d3_011_fsp_017_forced_selling_pressure_42(fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42):
    return _base_universe_d3(fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42, 11)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_011_fsp_017_forced_selling_pressure_42'] = {'inputs': ['fsp_base_universe_d2_011_fsp_017_forced_selling_pressure_42'], 'func': fsp_base_universe_d3_011_fsp_017_forced_selling_pressure_42}


def fsp_base_universe_d3_012_fsp_018_holder_base_volatility_63(fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63):
    return _base_universe_d3(fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63, 12)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_012_fsp_018_holder_base_volatility_63'] = {'inputs': ['fsp_base_universe_d2_012_fsp_018_holder_base_volatility_63'], 'func': fsp_base_universe_d3_012_fsp_018_holder_base_volatility_63}


def fsp_base_universe_d3_013_fsp_021_top_holder_concentration_189(fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189):
    return _base_universe_d3(fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189, 13)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_013_fsp_021_top_holder_concentration_189'] = {'inputs': ['fsp_base_universe_d2_013_fsp_021_top_holder_concentration_189'], 'func': fsp_base_universe_d3_013_fsp_021_top_holder_concentration_189}


def fsp_base_universe_d3_014_fsp_022_institutional_net_flow_252(fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252):
    return _base_universe_d3(fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252, 14)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_014_fsp_022_institutional_net_flow_252'] = {'inputs': ['fsp_base_universe_d2_014_fsp_022_institutional_net_flow_252'], 'func': fsp_base_universe_d3_014_fsp_022_institutional_net_flow_252}


def fsp_base_universe_d3_015_fsp_023_forced_selling_pressure_378(fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378):
    return _base_universe_d3(fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378, 15)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_015_fsp_023_forced_selling_pressure_378'] = {'inputs': ['fsp_base_universe_d2_015_fsp_023_forced_selling_pressure_378'], 'func': fsp_base_universe_d3_015_fsp_023_forced_selling_pressure_378}


def fsp_base_universe_d3_016_fsp_024_holder_base_volatility_504(fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504):
    return _base_universe_d3(fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504, 16)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_016_fsp_024_holder_base_volatility_504'] = {'inputs': ['fsp_base_universe_d2_016_fsp_024_holder_base_volatility_504'], 'func': fsp_base_universe_d3_016_fsp_024_holder_base_volatility_504}


def fsp_base_universe_d3_017_fsp_027_top_holder_concentration_1260(fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260):
    return _base_universe_d3(fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260, 17)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_017_fsp_027_top_holder_concentration_1260'] = {'inputs': ['fsp_base_universe_d2_017_fsp_027_top_holder_concentration_1260'], 'func': fsp_base_universe_d3_017_fsp_027_top_holder_concentration_1260}


def fsp_base_universe_d3_018_fsp_028_institutional_net_flow_1512(fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512):
    return _base_universe_d3(fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512, 18)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_018_fsp_028_institutional_net_flow_1512'] = {'inputs': ['fsp_base_universe_d2_018_fsp_028_institutional_net_flow_1512'], 'func': fsp_base_universe_d3_018_fsp_028_institutional_net_flow_1512}


def fsp_base_universe_d3_019_fsp_029_forced_selling_pressure_63(fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63):
    return _base_universe_d3(fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63, 19)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_019_fsp_029_forced_selling_pressure_63'] = {'inputs': ['fsp_base_universe_d2_019_fsp_029_forced_selling_pressure_63'], 'func': fsp_base_universe_d3_019_fsp_029_forced_selling_pressure_63}


def fsp_base_universe_d3_020_fsp_030_holder_base_volatility_252(fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252):
    return _base_universe_d3(fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252, 20)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_020_fsp_030_holder_base_volatility_252'] = {'inputs': ['fsp_base_universe_d2_020_fsp_030_holder_base_volatility_252'], 'func': fsp_base_universe_d3_020_fsp_030_holder_base_volatility_252}


def fsp_base_universe_d3_021_fsp_basefill_001(fsp_base_universe_d2_021_fsp_basefill_001):
    return _base_universe_d3(fsp_base_universe_d2_021_fsp_basefill_001, 21)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_021_fsp_basefill_001'] = {'inputs': ['fsp_base_universe_d2_021_fsp_basefill_001'], 'func': fsp_base_universe_d3_021_fsp_basefill_001}


def fsp_base_universe_d3_022_fsp_basefill_002(fsp_base_universe_d2_022_fsp_basefill_002):
    return _base_universe_d3(fsp_base_universe_d2_022_fsp_basefill_002, 22)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_022_fsp_basefill_002'] = {'inputs': ['fsp_base_universe_d2_022_fsp_basefill_002'], 'func': fsp_base_universe_d3_022_fsp_basefill_002}


def fsp_base_universe_d3_023_fsp_basefill_007(fsp_base_universe_d2_023_fsp_basefill_007):
    return _base_universe_d3(fsp_base_universe_d2_023_fsp_basefill_007, 23)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_023_fsp_basefill_007'] = {'inputs': ['fsp_base_universe_d2_023_fsp_basefill_007'], 'func': fsp_base_universe_d3_023_fsp_basefill_007}


def fsp_base_universe_d3_024_fsp_basefill_008(fsp_base_universe_d2_024_fsp_basefill_008):
    return _base_universe_d3(fsp_base_universe_d2_024_fsp_basefill_008, 24)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_024_fsp_basefill_008'] = {'inputs': ['fsp_base_universe_d2_024_fsp_basefill_008'], 'func': fsp_base_universe_d3_024_fsp_basefill_008}


def fsp_base_universe_d3_025_fsp_basefill_013(fsp_base_universe_d2_025_fsp_basefill_013):
    return _base_universe_d3(fsp_base_universe_d2_025_fsp_basefill_013, 25)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_025_fsp_basefill_013'] = {'inputs': ['fsp_base_universe_d2_025_fsp_basefill_013'], 'func': fsp_base_universe_d3_025_fsp_basefill_013}


def fsp_base_universe_d3_026_fsp_basefill_014(fsp_base_universe_d2_026_fsp_basefill_014):
    return _base_universe_d3(fsp_base_universe_d2_026_fsp_basefill_014, 26)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_026_fsp_basefill_014'] = {'inputs': ['fsp_base_universe_d2_026_fsp_basefill_014'], 'func': fsp_base_universe_d3_026_fsp_basefill_014}


def fsp_base_universe_d3_027_fsp_basefill_019(fsp_base_universe_d2_027_fsp_basefill_019):
    return _base_universe_d3(fsp_base_universe_d2_027_fsp_basefill_019, 27)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_027_fsp_basefill_019'] = {'inputs': ['fsp_base_universe_d2_027_fsp_basefill_019'], 'func': fsp_base_universe_d3_027_fsp_basefill_019}


def fsp_base_universe_d3_028_fsp_basefill_020(fsp_base_universe_d2_028_fsp_basefill_020):
    return _base_universe_d3(fsp_base_universe_d2_028_fsp_basefill_020, 28)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_028_fsp_basefill_020'] = {'inputs': ['fsp_base_universe_d2_028_fsp_basefill_020'], 'func': fsp_base_universe_d3_028_fsp_basefill_020}


def fsp_base_universe_d3_029_fsp_basefill_025(fsp_base_universe_d2_029_fsp_basefill_025):
    return _base_universe_d3(fsp_base_universe_d2_029_fsp_basefill_025, 29)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_029_fsp_basefill_025'] = {'inputs': ['fsp_base_universe_d2_029_fsp_basefill_025'], 'func': fsp_base_universe_d3_029_fsp_basefill_025}


def fsp_base_universe_d3_030_fsp_basefill_026(fsp_base_universe_d2_030_fsp_basefill_026):
    return _base_universe_d3(fsp_base_universe_d2_030_fsp_basefill_026, 30)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_030_fsp_basefill_026'] = {'inputs': ['fsp_base_universe_d2_030_fsp_basefill_026'], 'func': fsp_base_universe_d3_030_fsp_basefill_026}


def fsp_base_universe_d3_031_fsp_basefill_031(fsp_base_universe_d2_031_fsp_basefill_031):
    return _base_universe_d3(fsp_base_universe_d2_031_fsp_basefill_031, 31)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_031_fsp_basefill_031'] = {'inputs': ['fsp_base_universe_d2_031_fsp_basefill_031'], 'func': fsp_base_universe_d3_031_fsp_basefill_031}


def fsp_base_universe_d3_032_fsp_basefill_032(fsp_base_universe_d2_032_fsp_basefill_032):
    return _base_universe_d3(fsp_base_universe_d2_032_fsp_basefill_032, 32)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_032_fsp_basefill_032'] = {'inputs': ['fsp_base_universe_d2_032_fsp_basefill_032'], 'func': fsp_base_universe_d3_032_fsp_basefill_032}


def fsp_base_universe_d3_033_fsp_basefill_033(fsp_base_universe_d2_033_fsp_basefill_033):
    return _base_universe_d3(fsp_base_universe_d2_033_fsp_basefill_033, 33)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_033_fsp_basefill_033'] = {'inputs': ['fsp_base_universe_d2_033_fsp_basefill_033'], 'func': fsp_base_universe_d3_033_fsp_basefill_033}


def fsp_base_universe_d3_034_fsp_basefill_034(fsp_base_universe_d2_034_fsp_basefill_034):
    return _base_universe_d3(fsp_base_universe_d2_034_fsp_basefill_034, 34)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_034_fsp_basefill_034'] = {'inputs': ['fsp_base_universe_d2_034_fsp_basefill_034'], 'func': fsp_base_universe_d3_034_fsp_basefill_034}


def fsp_base_universe_d3_035_fsp_basefill_035(fsp_base_universe_d2_035_fsp_basefill_035):
    return _base_universe_d3(fsp_base_universe_d2_035_fsp_basefill_035, 35)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_035_fsp_basefill_035'] = {'inputs': ['fsp_base_universe_d2_035_fsp_basefill_035'], 'func': fsp_base_universe_d3_035_fsp_basefill_035}


def fsp_base_universe_d3_036_fsp_basefill_036(fsp_base_universe_d2_036_fsp_basefill_036):
    return _base_universe_d3(fsp_base_universe_d2_036_fsp_basefill_036, 36)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_036_fsp_basefill_036'] = {'inputs': ['fsp_base_universe_d2_036_fsp_basefill_036'], 'func': fsp_base_universe_d3_036_fsp_basefill_036}


def fsp_base_universe_d3_037_fsp_basefill_037(fsp_base_universe_d2_037_fsp_basefill_037):
    return _base_universe_d3(fsp_base_universe_d2_037_fsp_basefill_037, 37)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_037_fsp_basefill_037'] = {'inputs': ['fsp_base_universe_d2_037_fsp_basefill_037'], 'func': fsp_base_universe_d3_037_fsp_basefill_037}


def fsp_base_universe_d3_038_fsp_basefill_038(fsp_base_universe_d2_038_fsp_basefill_038):
    return _base_universe_d3(fsp_base_universe_d2_038_fsp_basefill_038, 38)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_038_fsp_basefill_038'] = {'inputs': ['fsp_base_universe_d2_038_fsp_basefill_038'], 'func': fsp_base_universe_d3_038_fsp_basefill_038}


def fsp_base_universe_d3_039_fsp_basefill_039(fsp_base_universe_d2_039_fsp_basefill_039):
    return _base_universe_d3(fsp_base_universe_d2_039_fsp_basefill_039, 39)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_039_fsp_basefill_039'] = {'inputs': ['fsp_base_universe_d2_039_fsp_basefill_039'], 'func': fsp_base_universe_d3_039_fsp_basefill_039}


def fsp_base_universe_d3_040_fsp_basefill_040(fsp_base_universe_d2_040_fsp_basefill_040):
    return _base_universe_d3(fsp_base_universe_d2_040_fsp_basefill_040, 40)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_040_fsp_basefill_040'] = {'inputs': ['fsp_base_universe_d2_040_fsp_basefill_040'], 'func': fsp_base_universe_d3_040_fsp_basefill_040}


def fsp_base_universe_d3_041_fsp_basefill_041(fsp_base_universe_d2_041_fsp_basefill_041):
    return _base_universe_d3(fsp_base_universe_d2_041_fsp_basefill_041, 41)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_041_fsp_basefill_041'] = {'inputs': ['fsp_base_universe_d2_041_fsp_basefill_041'], 'func': fsp_base_universe_d3_041_fsp_basefill_041}


def fsp_base_universe_d3_042_fsp_basefill_042(fsp_base_universe_d2_042_fsp_basefill_042):
    return _base_universe_d3(fsp_base_universe_d2_042_fsp_basefill_042, 42)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_042_fsp_basefill_042'] = {'inputs': ['fsp_base_universe_d2_042_fsp_basefill_042'], 'func': fsp_base_universe_d3_042_fsp_basefill_042}


def fsp_base_universe_d3_043_fsp_basefill_043(fsp_base_universe_d2_043_fsp_basefill_043):
    return _base_universe_d3(fsp_base_universe_d2_043_fsp_basefill_043, 43)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_043_fsp_basefill_043'] = {'inputs': ['fsp_base_universe_d2_043_fsp_basefill_043'], 'func': fsp_base_universe_d3_043_fsp_basefill_043}


def fsp_base_universe_d3_044_fsp_basefill_044(fsp_base_universe_d2_044_fsp_basefill_044):
    return _base_universe_d3(fsp_base_universe_d2_044_fsp_basefill_044, 44)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_044_fsp_basefill_044'] = {'inputs': ['fsp_base_universe_d2_044_fsp_basefill_044'], 'func': fsp_base_universe_d3_044_fsp_basefill_044}


def fsp_base_universe_d3_045_fsp_basefill_045(fsp_base_universe_d2_045_fsp_basefill_045):
    return _base_universe_d3(fsp_base_universe_d2_045_fsp_basefill_045, 45)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_045_fsp_basefill_045'] = {'inputs': ['fsp_base_universe_d2_045_fsp_basefill_045'], 'func': fsp_base_universe_d3_045_fsp_basefill_045}


def fsp_base_universe_d3_046_fsp_basefill_046(fsp_base_universe_d2_046_fsp_basefill_046):
    return _base_universe_d3(fsp_base_universe_d2_046_fsp_basefill_046, 46)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_046_fsp_basefill_046'] = {'inputs': ['fsp_base_universe_d2_046_fsp_basefill_046'], 'func': fsp_base_universe_d3_046_fsp_basefill_046}


def fsp_base_universe_d3_047_fsp_basefill_047(fsp_base_universe_d2_047_fsp_basefill_047):
    return _base_universe_d3(fsp_base_universe_d2_047_fsp_basefill_047, 47)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_047_fsp_basefill_047'] = {'inputs': ['fsp_base_universe_d2_047_fsp_basefill_047'], 'func': fsp_base_universe_d3_047_fsp_basefill_047}


def fsp_base_universe_d3_048_fsp_basefill_048(fsp_base_universe_d2_048_fsp_basefill_048):
    return _base_universe_d3(fsp_base_universe_d2_048_fsp_basefill_048, 48)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_048_fsp_basefill_048'] = {'inputs': ['fsp_base_universe_d2_048_fsp_basefill_048'], 'func': fsp_base_universe_d3_048_fsp_basefill_048}


def fsp_base_universe_d3_049_fsp_basefill_049(fsp_base_universe_d2_049_fsp_basefill_049):
    return _base_universe_d3(fsp_base_universe_d2_049_fsp_basefill_049, 49)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_049_fsp_basefill_049'] = {'inputs': ['fsp_base_universe_d2_049_fsp_basefill_049'], 'func': fsp_base_universe_d3_049_fsp_basefill_049}


def fsp_base_universe_d3_050_fsp_basefill_050(fsp_base_universe_d2_050_fsp_basefill_050):
    return _base_universe_d3(fsp_base_universe_d2_050_fsp_basefill_050, 50)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_050_fsp_basefill_050'] = {'inputs': ['fsp_base_universe_d2_050_fsp_basefill_050'], 'func': fsp_base_universe_d3_050_fsp_basefill_050}


def fsp_base_universe_d3_051_fsp_basefill_051(fsp_base_universe_d2_051_fsp_basefill_051):
    return _base_universe_d3(fsp_base_universe_d2_051_fsp_basefill_051, 51)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_051_fsp_basefill_051'] = {'inputs': ['fsp_base_universe_d2_051_fsp_basefill_051'], 'func': fsp_base_universe_d3_051_fsp_basefill_051}


def fsp_base_universe_d3_052_fsp_basefill_052(fsp_base_universe_d2_052_fsp_basefill_052):
    return _base_universe_d3(fsp_base_universe_d2_052_fsp_basefill_052, 52)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_052_fsp_basefill_052'] = {'inputs': ['fsp_base_universe_d2_052_fsp_basefill_052'], 'func': fsp_base_universe_d3_052_fsp_basefill_052}


def fsp_base_universe_d3_053_fsp_basefill_053(fsp_base_universe_d2_053_fsp_basefill_053):
    return _base_universe_d3(fsp_base_universe_d2_053_fsp_basefill_053, 53)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_053_fsp_basefill_053'] = {'inputs': ['fsp_base_universe_d2_053_fsp_basefill_053'], 'func': fsp_base_universe_d3_053_fsp_basefill_053}


def fsp_base_universe_d3_054_fsp_basefill_054(fsp_base_universe_d2_054_fsp_basefill_054):
    return _base_universe_d3(fsp_base_universe_d2_054_fsp_basefill_054, 54)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_054_fsp_basefill_054'] = {'inputs': ['fsp_base_universe_d2_054_fsp_basefill_054'], 'func': fsp_base_universe_d3_054_fsp_basefill_054}


def fsp_base_universe_d3_055_fsp_basefill_055(fsp_base_universe_d2_055_fsp_basefill_055):
    return _base_universe_d3(fsp_base_universe_d2_055_fsp_basefill_055, 55)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_055_fsp_basefill_055'] = {'inputs': ['fsp_base_universe_d2_055_fsp_basefill_055'], 'func': fsp_base_universe_d3_055_fsp_basefill_055}


def fsp_base_universe_d3_056_fsp_basefill_056(fsp_base_universe_d2_056_fsp_basefill_056):
    return _base_universe_d3(fsp_base_universe_d2_056_fsp_basefill_056, 56)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_056_fsp_basefill_056'] = {'inputs': ['fsp_base_universe_d2_056_fsp_basefill_056'], 'func': fsp_base_universe_d3_056_fsp_basefill_056}


def fsp_base_universe_d3_057_fsp_basefill_057(fsp_base_universe_d2_057_fsp_basefill_057):
    return _base_universe_d3(fsp_base_universe_d2_057_fsp_basefill_057, 57)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_057_fsp_basefill_057'] = {'inputs': ['fsp_base_universe_d2_057_fsp_basefill_057'], 'func': fsp_base_universe_d3_057_fsp_basefill_057}


def fsp_base_universe_d3_058_fsp_basefill_058(fsp_base_universe_d2_058_fsp_basefill_058):
    return _base_universe_d3(fsp_base_universe_d2_058_fsp_basefill_058, 58)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_058_fsp_basefill_058'] = {'inputs': ['fsp_base_universe_d2_058_fsp_basefill_058'], 'func': fsp_base_universe_d3_058_fsp_basefill_058}


def fsp_base_universe_d3_059_fsp_basefill_059(fsp_base_universe_d2_059_fsp_basefill_059):
    return _base_universe_d3(fsp_base_universe_d2_059_fsp_basefill_059, 59)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_059_fsp_basefill_059'] = {'inputs': ['fsp_base_universe_d2_059_fsp_basefill_059'], 'func': fsp_base_universe_d3_059_fsp_basefill_059}


def fsp_base_universe_d3_060_fsp_basefill_060(fsp_base_universe_d2_060_fsp_basefill_060):
    return _base_universe_d3(fsp_base_universe_d2_060_fsp_basefill_060, 60)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_060_fsp_basefill_060'] = {'inputs': ['fsp_base_universe_d2_060_fsp_basefill_060'], 'func': fsp_base_universe_d3_060_fsp_basefill_060}


def fsp_base_universe_d3_061_fsp_basefill_061(fsp_base_universe_d2_061_fsp_basefill_061):
    return _base_universe_d3(fsp_base_universe_d2_061_fsp_basefill_061, 61)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_061_fsp_basefill_061'] = {'inputs': ['fsp_base_universe_d2_061_fsp_basefill_061'], 'func': fsp_base_universe_d3_061_fsp_basefill_061}


def fsp_base_universe_d3_062_fsp_basefill_062(fsp_base_universe_d2_062_fsp_basefill_062):
    return _base_universe_d3(fsp_base_universe_d2_062_fsp_basefill_062, 62)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_062_fsp_basefill_062'] = {'inputs': ['fsp_base_universe_d2_062_fsp_basefill_062'], 'func': fsp_base_universe_d3_062_fsp_basefill_062}


def fsp_base_universe_d3_063_fsp_basefill_063(fsp_base_universe_d2_063_fsp_basefill_063):
    return _base_universe_d3(fsp_base_universe_d2_063_fsp_basefill_063, 63)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_063_fsp_basefill_063'] = {'inputs': ['fsp_base_universe_d2_063_fsp_basefill_063'], 'func': fsp_base_universe_d3_063_fsp_basefill_063}


def fsp_base_universe_d3_064_fsp_basefill_064(fsp_base_universe_d2_064_fsp_basefill_064):
    return _base_universe_d3(fsp_base_universe_d2_064_fsp_basefill_064, 64)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_064_fsp_basefill_064'] = {'inputs': ['fsp_base_universe_d2_064_fsp_basefill_064'], 'func': fsp_base_universe_d3_064_fsp_basefill_064}


def fsp_base_universe_d3_065_fsp_basefill_065(fsp_base_universe_d2_065_fsp_basefill_065):
    return _base_universe_d3(fsp_base_universe_d2_065_fsp_basefill_065, 65)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_065_fsp_basefill_065'] = {'inputs': ['fsp_base_universe_d2_065_fsp_basefill_065'], 'func': fsp_base_universe_d3_065_fsp_basefill_065}


def fsp_base_universe_d3_066_fsp_basefill_066(fsp_base_universe_d2_066_fsp_basefill_066):
    return _base_universe_d3(fsp_base_universe_d2_066_fsp_basefill_066, 66)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_066_fsp_basefill_066'] = {'inputs': ['fsp_base_universe_d2_066_fsp_basefill_066'], 'func': fsp_base_universe_d3_066_fsp_basefill_066}


def fsp_base_universe_d3_067_fsp_basefill_067(fsp_base_universe_d2_067_fsp_basefill_067):
    return _base_universe_d3(fsp_base_universe_d2_067_fsp_basefill_067, 67)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_067_fsp_basefill_067'] = {'inputs': ['fsp_base_universe_d2_067_fsp_basefill_067'], 'func': fsp_base_universe_d3_067_fsp_basefill_067}


def fsp_base_universe_d3_068_fsp_basefill_068(fsp_base_universe_d2_068_fsp_basefill_068):
    return _base_universe_d3(fsp_base_universe_d2_068_fsp_basefill_068, 68)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_068_fsp_basefill_068'] = {'inputs': ['fsp_base_universe_d2_068_fsp_basefill_068'], 'func': fsp_base_universe_d3_068_fsp_basefill_068}


def fsp_base_universe_d3_069_fsp_basefill_069(fsp_base_universe_d2_069_fsp_basefill_069):
    return _base_universe_d3(fsp_base_universe_d2_069_fsp_basefill_069, 69)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_069_fsp_basefill_069'] = {'inputs': ['fsp_base_universe_d2_069_fsp_basefill_069'], 'func': fsp_base_universe_d3_069_fsp_basefill_069}


def fsp_base_universe_d3_070_fsp_basefill_070(fsp_base_universe_d2_070_fsp_basefill_070):
    return _base_universe_d3(fsp_base_universe_d2_070_fsp_basefill_070, 70)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_070_fsp_basefill_070'] = {'inputs': ['fsp_base_universe_d2_070_fsp_basefill_070'], 'func': fsp_base_universe_d3_070_fsp_basefill_070}


def fsp_base_universe_d3_071_fsp_basefill_071(fsp_base_universe_d2_071_fsp_basefill_071):
    return _base_universe_d3(fsp_base_universe_d2_071_fsp_basefill_071, 71)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_071_fsp_basefill_071'] = {'inputs': ['fsp_base_universe_d2_071_fsp_basefill_071'], 'func': fsp_base_universe_d3_071_fsp_basefill_071}


def fsp_base_universe_d3_072_fsp_basefill_072(fsp_base_universe_d2_072_fsp_basefill_072):
    return _base_universe_d3(fsp_base_universe_d2_072_fsp_basefill_072, 72)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_072_fsp_basefill_072'] = {'inputs': ['fsp_base_universe_d2_072_fsp_basefill_072'], 'func': fsp_base_universe_d3_072_fsp_basefill_072}


def fsp_base_universe_d3_073_fsp_basefill_073(fsp_base_universe_d2_073_fsp_basefill_073):
    return _base_universe_d3(fsp_base_universe_d2_073_fsp_basefill_073, 73)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_073_fsp_basefill_073'] = {'inputs': ['fsp_base_universe_d2_073_fsp_basefill_073'], 'func': fsp_base_universe_d3_073_fsp_basefill_073}


def fsp_base_universe_d3_074_fsp_basefill_074(fsp_base_universe_d2_074_fsp_basefill_074):
    return _base_universe_d3(fsp_base_universe_d2_074_fsp_basefill_074, 74)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_074_fsp_basefill_074'] = {'inputs': ['fsp_base_universe_d2_074_fsp_basefill_074'], 'func': fsp_base_universe_d3_074_fsp_basefill_074}


def fsp_base_universe_d3_075_fsp_basefill_075(fsp_base_universe_d2_075_fsp_basefill_075):
    return _base_universe_d3(fsp_base_universe_d2_075_fsp_basefill_075, 75)
FSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['fsp_base_universe_d3_075_fsp_basefill_075'] = {'inputs': ['fsp_base_universe_d2_075_fsp_basefill_075'], 'func': fsp_base_universe_d3_075_fsp_basefill_075}
