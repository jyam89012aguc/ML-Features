import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def pbs_001_realized_vol_z_accel_1(pbs_001_realized_vol_z_roc_1):
    feature = _s(pbs_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def pbs_007_realized_vol_z_accel_5(pbs_007_realized_vol_z_roc_5):
    feature = _s(pbs_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def pbs_013_realized_vol_z_accel_42(pbs_013_realized_vol_z_roc_42):
    feature = _s(pbs_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def pbs_179_pbs_019_realized_vol_z_42_019_accel_126(pbs_154_pbs_019_realized_vol_z_42_019_roc_126):
    feature = _s(pbs_154_pbs_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def pbs_180_pbs_025_realized_vol_z_378_025_accel_378(pbs_155_pbs_025_realized_vol_z_378_025_roc_378):
    feature = _s(pbs_155_pbs_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















PANIC_BAR_SIGNATURES_REGISTRY_3RD_DERIVATIVES = {
    'pbs_001_realized_vol_z_accel_1': {'inputs': ['pbs_001_realized_vol_z_roc_1'], 'func': pbs_001_realized_vol_z_accel_1},
    'pbs_007_realized_vol_z_accel_5': {'inputs': ['pbs_007_realized_vol_z_roc_5'], 'func': pbs_007_realized_vol_z_accel_5},
    'pbs_013_realized_vol_z_accel_42': {'inputs': ['pbs_013_realized_vol_z_roc_42'], 'func': pbs_013_realized_vol_z_accel_42},
    'pbs_179_pbs_019_realized_vol_z_42_019_accel_126': {'inputs': ['pbs_154_pbs_019_realized_vol_z_42_019_roc_126'], 'func': pbs_179_pbs_019_realized_vol_z_42_019_accel_126},
    'pbs_180_pbs_025_realized_vol_z_378_025_accel_378': {'inputs': ['pbs_155_pbs_025_realized_vol_z_378_025_roc_378'], 'func': pbs_180_pbs_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def pbs_replacement_d3_001(pbs_replacement_d2_001):
    feature = _clean(pbs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_001'] = {'inputs': ['pbs_replacement_d2_001'], 'func': pbs_replacement_d3_001}


def pbs_replacement_d3_002(pbs_replacement_d2_002):
    feature = _clean(pbs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_002'] = {'inputs': ['pbs_replacement_d2_002'], 'func': pbs_replacement_d3_002}


def pbs_replacement_d3_003(pbs_replacement_d2_003):
    feature = _clean(pbs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_003'] = {'inputs': ['pbs_replacement_d2_003'], 'func': pbs_replacement_d3_003}


def pbs_replacement_d3_004(pbs_replacement_d2_004):
    feature = _clean(pbs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_004'] = {'inputs': ['pbs_replacement_d2_004'], 'func': pbs_replacement_d3_004}


def pbs_replacement_d3_005(pbs_replacement_d2_005):
    feature = _clean(pbs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_005'] = {'inputs': ['pbs_replacement_d2_005'], 'func': pbs_replacement_d3_005}


def pbs_replacement_d3_006(pbs_replacement_d2_006):
    feature = _clean(pbs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_006'] = {'inputs': ['pbs_replacement_d2_006'], 'func': pbs_replacement_d3_006}


def pbs_replacement_d3_007(pbs_replacement_d2_007):
    feature = _clean(pbs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_007'] = {'inputs': ['pbs_replacement_d2_007'], 'func': pbs_replacement_d3_007}


def pbs_replacement_d3_008(pbs_replacement_d2_008):
    feature = _clean(pbs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_008'] = {'inputs': ['pbs_replacement_d2_008'], 'func': pbs_replacement_d3_008}


def pbs_replacement_d3_009(pbs_replacement_d2_009):
    feature = _clean(pbs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_009'] = {'inputs': ['pbs_replacement_d2_009'], 'func': pbs_replacement_d3_009}


def pbs_replacement_d3_010(pbs_replacement_d2_010):
    feature = _clean(pbs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_010'] = {'inputs': ['pbs_replacement_d2_010'], 'func': pbs_replacement_d3_010}


def pbs_replacement_d3_011(pbs_replacement_d2_011):
    feature = _clean(pbs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_011'] = {'inputs': ['pbs_replacement_d2_011'], 'func': pbs_replacement_d3_011}


def pbs_replacement_d3_012(pbs_replacement_d2_012):
    feature = _clean(pbs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_012'] = {'inputs': ['pbs_replacement_d2_012'], 'func': pbs_replacement_d3_012}


def pbs_replacement_d3_013(pbs_replacement_d2_013):
    feature = _clean(pbs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_013'] = {'inputs': ['pbs_replacement_d2_013'], 'func': pbs_replacement_d3_013}


def pbs_replacement_d3_014(pbs_replacement_d2_014):
    feature = _clean(pbs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_014'] = {'inputs': ['pbs_replacement_d2_014'], 'func': pbs_replacement_d3_014}


def pbs_replacement_d3_015(pbs_replacement_d2_015):
    feature = _clean(pbs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_015'] = {'inputs': ['pbs_replacement_d2_015'], 'func': pbs_replacement_d3_015}


def pbs_replacement_d3_016(pbs_replacement_d2_016):
    feature = _clean(pbs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_016'] = {'inputs': ['pbs_replacement_d2_016'], 'func': pbs_replacement_d3_016}


def pbs_replacement_d3_017(pbs_replacement_d2_017):
    feature = _clean(pbs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_017'] = {'inputs': ['pbs_replacement_d2_017'], 'func': pbs_replacement_d3_017}


def pbs_replacement_d3_018(pbs_replacement_d2_018):
    feature = _clean(pbs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_018'] = {'inputs': ['pbs_replacement_d2_018'], 'func': pbs_replacement_d3_018}


def pbs_replacement_d3_019(pbs_replacement_d2_019):
    feature = _clean(pbs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_019'] = {'inputs': ['pbs_replacement_d2_019'], 'func': pbs_replacement_d3_019}


def pbs_replacement_d3_020(pbs_replacement_d2_020):
    feature = _clean(pbs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_020'] = {'inputs': ['pbs_replacement_d2_020'], 'func': pbs_replacement_d3_020}


def pbs_replacement_d3_021(pbs_replacement_d2_021):
    feature = _clean(pbs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_021'] = {'inputs': ['pbs_replacement_d2_021'], 'func': pbs_replacement_d3_021}


def pbs_replacement_d3_022(pbs_replacement_d2_022):
    feature = _clean(pbs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_022'] = {'inputs': ['pbs_replacement_d2_022'], 'func': pbs_replacement_d3_022}


def pbs_replacement_d3_023(pbs_replacement_d2_023):
    feature = _clean(pbs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_023'] = {'inputs': ['pbs_replacement_d2_023'], 'func': pbs_replacement_d3_023}


def pbs_replacement_d3_024(pbs_replacement_d2_024):
    feature = _clean(pbs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_024'] = {'inputs': ['pbs_replacement_d2_024'], 'func': pbs_replacement_d3_024}


def pbs_replacement_d3_025(pbs_replacement_d2_025):
    feature = _clean(pbs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_025'] = {'inputs': ['pbs_replacement_d2_025'], 'func': pbs_replacement_d3_025}


def pbs_replacement_d3_026(pbs_replacement_d2_026):
    feature = _clean(pbs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_026'] = {'inputs': ['pbs_replacement_d2_026'], 'func': pbs_replacement_d3_026}


def pbs_replacement_d3_027(pbs_replacement_d2_027):
    feature = _clean(pbs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_027'] = {'inputs': ['pbs_replacement_d2_027'], 'func': pbs_replacement_d3_027}


def pbs_replacement_d3_028(pbs_replacement_d2_028):
    feature = _clean(pbs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_028'] = {'inputs': ['pbs_replacement_d2_028'], 'func': pbs_replacement_d3_028}


def pbs_replacement_d3_029(pbs_replacement_d2_029):
    feature = _clean(pbs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_029'] = {'inputs': ['pbs_replacement_d2_029'], 'func': pbs_replacement_d3_029}


def pbs_replacement_d3_030(pbs_replacement_d2_030):
    feature = _clean(pbs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_030'] = {'inputs': ['pbs_replacement_d2_030'], 'func': pbs_replacement_d3_030}


def pbs_replacement_d3_031(pbs_replacement_d2_031):
    feature = _clean(pbs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_031'] = {'inputs': ['pbs_replacement_d2_031'], 'func': pbs_replacement_d3_031}


def pbs_replacement_d3_032(pbs_replacement_d2_032):
    feature = _clean(pbs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_032'] = {'inputs': ['pbs_replacement_d2_032'], 'func': pbs_replacement_d3_032}


def pbs_replacement_d3_033(pbs_replacement_d2_033):
    feature = _clean(pbs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_033'] = {'inputs': ['pbs_replacement_d2_033'], 'func': pbs_replacement_d3_033}


def pbs_replacement_d3_034(pbs_replacement_d2_034):
    feature = _clean(pbs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_034'] = {'inputs': ['pbs_replacement_d2_034'], 'func': pbs_replacement_d3_034}


def pbs_replacement_d3_035(pbs_replacement_d2_035):
    feature = _clean(pbs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_035'] = {'inputs': ['pbs_replacement_d2_035'], 'func': pbs_replacement_d3_035}


def pbs_replacement_d3_036(pbs_replacement_d2_036):
    feature = _clean(pbs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_036'] = {'inputs': ['pbs_replacement_d2_036'], 'func': pbs_replacement_d3_036}


def pbs_replacement_d3_037(pbs_replacement_d2_037):
    feature = _clean(pbs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_037'] = {'inputs': ['pbs_replacement_d2_037'], 'func': pbs_replacement_d3_037}


def pbs_replacement_d3_038(pbs_replacement_d2_038):
    feature = _clean(pbs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_038'] = {'inputs': ['pbs_replacement_d2_038'], 'func': pbs_replacement_d3_038}


def pbs_replacement_d3_039(pbs_replacement_d2_039):
    feature = _clean(pbs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_039'] = {'inputs': ['pbs_replacement_d2_039'], 'func': pbs_replacement_d3_039}


def pbs_replacement_d3_040(pbs_replacement_d2_040):
    feature = _clean(pbs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_040'] = {'inputs': ['pbs_replacement_d2_040'], 'func': pbs_replacement_d3_040}


def pbs_replacement_d3_041(pbs_replacement_d2_041):
    feature = _clean(pbs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_041'] = {'inputs': ['pbs_replacement_d2_041'], 'func': pbs_replacement_d3_041}


def pbs_replacement_d3_042(pbs_replacement_d2_042):
    feature = _clean(pbs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_042'] = {'inputs': ['pbs_replacement_d2_042'], 'func': pbs_replacement_d3_042}


def pbs_replacement_d3_043(pbs_replacement_d2_043):
    feature = _clean(pbs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_043'] = {'inputs': ['pbs_replacement_d2_043'], 'func': pbs_replacement_d3_043}


def pbs_replacement_d3_044(pbs_replacement_d2_044):
    feature = _clean(pbs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_044'] = {'inputs': ['pbs_replacement_d2_044'], 'func': pbs_replacement_d3_044}


def pbs_replacement_d3_045(pbs_replacement_d2_045):
    feature = _clean(pbs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_045'] = {'inputs': ['pbs_replacement_d2_045'], 'func': pbs_replacement_d3_045}


def pbs_replacement_d3_046(pbs_replacement_d2_046):
    feature = _clean(pbs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_046'] = {'inputs': ['pbs_replacement_d2_046'], 'func': pbs_replacement_d3_046}


def pbs_replacement_d3_047(pbs_replacement_d2_047):
    feature = _clean(pbs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_047'] = {'inputs': ['pbs_replacement_d2_047'], 'func': pbs_replacement_d3_047}


def pbs_replacement_d3_048(pbs_replacement_d2_048):
    feature = _clean(pbs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_048'] = {'inputs': ['pbs_replacement_d2_048'], 'func': pbs_replacement_d3_048}


def pbs_replacement_d3_049(pbs_replacement_d2_049):
    feature = _clean(pbs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_049'] = {'inputs': ['pbs_replacement_d2_049'], 'func': pbs_replacement_d3_049}


def pbs_replacement_d3_050(pbs_replacement_d2_050):
    feature = _clean(pbs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_050'] = {'inputs': ['pbs_replacement_d2_050'], 'func': pbs_replacement_d3_050}


def pbs_replacement_d3_051(pbs_replacement_d2_051):
    feature = _clean(pbs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_051'] = {'inputs': ['pbs_replacement_d2_051'], 'func': pbs_replacement_d3_051}


def pbs_replacement_d3_052(pbs_replacement_d2_052):
    feature = _clean(pbs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_052'] = {'inputs': ['pbs_replacement_d2_052'], 'func': pbs_replacement_d3_052}


def pbs_replacement_d3_053(pbs_replacement_d2_053):
    feature = _clean(pbs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_053'] = {'inputs': ['pbs_replacement_d2_053'], 'func': pbs_replacement_d3_053}


def pbs_replacement_d3_054(pbs_replacement_d2_054):
    feature = _clean(pbs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_054'] = {'inputs': ['pbs_replacement_d2_054'], 'func': pbs_replacement_d3_054}


def pbs_replacement_d3_055(pbs_replacement_d2_055):
    feature = _clean(pbs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_055'] = {'inputs': ['pbs_replacement_d2_055'], 'func': pbs_replacement_d3_055}


def pbs_replacement_d3_056(pbs_replacement_d2_056):
    feature = _clean(pbs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_056'] = {'inputs': ['pbs_replacement_d2_056'], 'func': pbs_replacement_d3_056}


def pbs_replacement_d3_057(pbs_replacement_d2_057):
    feature = _clean(pbs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_057'] = {'inputs': ['pbs_replacement_d2_057'], 'func': pbs_replacement_d3_057}


def pbs_replacement_d3_058(pbs_replacement_d2_058):
    feature = _clean(pbs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_058'] = {'inputs': ['pbs_replacement_d2_058'], 'func': pbs_replacement_d3_058}


def pbs_replacement_d3_059(pbs_replacement_d2_059):
    feature = _clean(pbs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_059'] = {'inputs': ['pbs_replacement_d2_059'], 'func': pbs_replacement_d3_059}


def pbs_replacement_d3_060(pbs_replacement_d2_060):
    feature = _clean(pbs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_060'] = {'inputs': ['pbs_replacement_d2_060'], 'func': pbs_replacement_d3_060}


def pbs_replacement_d3_061(pbs_replacement_d2_061):
    feature = _clean(pbs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_061'] = {'inputs': ['pbs_replacement_d2_061'], 'func': pbs_replacement_d3_061}


def pbs_replacement_d3_062(pbs_replacement_d2_062):
    feature = _clean(pbs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_062'] = {'inputs': ['pbs_replacement_d2_062'], 'func': pbs_replacement_d3_062}


def pbs_replacement_d3_063(pbs_replacement_d2_063):
    feature = _clean(pbs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_063'] = {'inputs': ['pbs_replacement_d2_063'], 'func': pbs_replacement_d3_063}


def pbs_replacement_d3_064(pbs_replacement_d2_064):
    feature = _clean(pbs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_064'] = {'inputs': ['pbs_replacement_d2_064'], 'func': pbs_replacement_d3_064}


def pbs_replacement_d3_065(pbs_replacement_d2_065):
    feature = _clean(pbs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_065'] = {'inputs': ['pbs_replacement_d2_065'], 'func': pbs_replacement_d3_065}


def pbs_replacement_d3_066(pbs_replacement_d2_066):
    feature = _clean(pbs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_066'] = {'inputs': ['pbs_replacement_d2_066'], 'func': pbs_replacement_d3_066}


def pbs_replacement_d3_067(pbs_replacement_d2_067):
    feature = _clean(pbs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_067'] = {'inputs': ['pbs_replacement_d2_067'], 'func': pbs_replacement_d3_067}


def pbs_replacement_d3_068(pbs_replacement_d2_068):
    feature = _clean(pbs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_068'] = {'inputs': ['pbs_replacement_d2_068'], 'func': pbs_replacement_d3_068}


def pbs_replacement_d3_069(pbs_replacement_d2_069):
    feature = _clean(pbs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_069'] = {'inputs': ['pbs_replacement_d2_069'], 'func': pbs_replacement_d3_069}


def pbs_replacement_d3_070(pbs_replacement_d2_070):
    feature = _clean(pbs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_070'] = {'inputs': ['pbs_replacement_d2_070'], 'func': pbs_replacement_d3_070}


def pbs_replacement_d3_071(pbs_replacement_d2_071):
    feature = _clean(pbs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_071'] = {'inputs': ['pbs_replacement_d2_071'], 'func': pbs_replacement_d3_071}


def pbs_replacement_d3_072(pbs_replacement_d2_072):
    feature = _clean(pbs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_072'] = {'inputs': ['pbs_replacement_d2_072'], 'func': pbs_replacement_d3_072}


def pbs_replacement_d3_073(pbs_replacement_d2_073):
    feature = _clean(pbs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_073'] = {'inputs': ['pbs_replacement_d2_073'], 'func': pbs_replacement_d3_073}


def pbs_replacement_d3_074(pbs_replacement_d2_074):
    feature = _clean(pbs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_074'] = {'inputs': ['pbs_replacement_d2_074'], 'func': pbs_replacement_d3_074}


def pbs_replacement_d3_075(pbs_replacement_d2_075):
    feature = _clean(pbs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_075'] = {'inputs': ['pbs_replacement_d2_075'], 'func': pbs_replacement_d3_075}


def pbs_replacement_d3_076(pbs_replacement_d2_076):
    feature = _clean(pbs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_076'] = {'inputs': ['pbs_replacement_d2_076'], 'func': pbs_replacement_d3_076}


def pbs_replacement_d3_077(pbs_replacement_d2_077):
    feature = _clean(pbs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_077'] = {'inputs': ['pbs_replacement_d2_077'], 'func': pbs_replacement_d3_077}


def pbs_replacement_d3_078(pbs_replacement_d2_078):
    feature = _clean(pbs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_078'] = {'inputs': ['pbs_replacement_d2_078'], 'func': pbs_replacement_d3_078}


def pbs_replacement_d3_079(pbs_replacement_d2_079):
    feature = _clean(pbs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_079'] = {'inputs': ['pbs_replacement_d2_079'], 'func': pbs_replacement_d3_079}


def pbs_replacement_d3_080(pbs_replacement_d2_080):
    feature = _clean(pbs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_080'] = {'inputs': ['pbs_replacement_d2_080'], 'func': pbs_replacement_d3_080}


def pbs_replacement_d3_081(pbs_replacement_d2_081):
    feature = _clean(pbs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_081'] = {'inputs': ['pbs_replacement_d2_081'], 'func': pbs_replacement_d3_081}


def pbs_replacement_d3_082(pbs_replacement_d2_082):
    feature = _clean(pbs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_082'] = {'inputs': ['pbs_replacement_d2_082'], 'func': pbs_replacement_d3_082}


def pbs_replacement_d3_083(pbs_replacement_d2_083):
    feature = _clean(pbs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_083'] = {'inputs': ['pbs_replacement_d2_083'], 'func': pbs_replacement_d3_083}


def pbs_replacement_d3_084(pbs_replacement_d2_084):
    feature = _clean(pbs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_084'] = {'inputs': ['pbs_replacement_d2_084'], 'func': pbs_replacement_d3_084}


def pbs_replacement_d3_085(pbs_replacement_d2_085):
    feature = _clean(pbs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_085'] = {'inputs': ['pbs_replacement_d2_085'], 'func': pbs_replacement_d3_085}


def pbs_replacement_d3_086(pbs_replacement_d2_086):
    feature = _clean(pbs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_086'] = {'inputs': ['pbs_replacement_d2_086'], 'func': pbs_replacement_d3_086}


def pbs_replacement_d3_087(pbs_replacement_d2_087):
    feature = _clean(pbs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_087'] = {'inputs': ['pbs_replacement_d2_087'], 'func': pbs_replacement_d3_087}


def pbs_replacement_d3_088(pbs_replacement_d2_088):
    feature = _clean(pbs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_088'] = {'inputs': ['pbs_replacement_d2_088'], 'func': pbs_replacement_d3_088}


def pbs_replacement_d3_089(pbs_replacement_d2_089):
    feature = _clean(pbs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_089'] = {'inputs': ['pbs_replacement_d2_089'], 'func': pbs_replacement_d3_089}


def pbs_replacement_d3_090(pbs_replacement_d2_090):
    feature = _clean(pbs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_090'] = {'inputs': ['pbs_replacement_d2_090'], 'func': pbs_replacement_d3_090}


def pbs_replacement_d3_091(pbs_replacement_d2_091):
    feature = _clean(pbs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_091'] = {'inputs': ['pbs_replacement_d2_091'], 'func': pbs_replacement_d3_091}


def pbs_replacement_d3_092(pbs_replacement_d2_092):
    feature = _clean(pbs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_092'] = {'inputs': ['pbs_replacement_d2_092'], 'func': pbs_replacement_d3_092}


def pbs_replacement_d3_093(pbs_replacement_d2_093):
    feature = _clean(pbs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_093'] = {'inputs': ['pbs_replacement_d2_093'], 'func': pbs_replacement_d3_093}


def pbs_replacement_d3_094(pbs_replacement_d2_094):
    feature = _clean(pbs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_094'] = {'inputs': ['pbs_replacement_d2_094'], 'func': pbs_replacement_d3_094}


def pbs_replacement_d3_095(pbs_replacement_d2_095):
    feature = _clean(pbs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_095'] = {'inputs': ['pbs_replacement_d2_095'], 'func': pbs_replacement_d3_095}


def pbs_replacement_d3_096(pbs_replacement_d2_096):
    feature = _clean(pbs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_096'] = {'inputs': ['pbs_replacement_d2_096'], 'func': pbs_replacement_d3_096}


def pbs_replacement_d3_097(pbs_replacement_d2_097):
    feature = _clean(pbs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_097'] = {'inputs': ['pbs_replacement_d2_097'], 'func': pbs_replacement_d3_097}


def pbs_replacement_d3_098(pbs_replacement_d2_098):
    feature = _clean(pbs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_098'] = {'inputs': ['pbs_replacement_d2_098'], 'func': pbs_replacement_d3_098}


def pbs_replacement_d3_099(pbs_replacement_d2_099):
    feature = _clean(pbs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_099'] = {'inputs': ['pbs_replacement_d2_099'], 'func': pbs_replacement_d3_099}


def pbs_replacement_d3_100(pbs_replacement_d2_100):
    feature = _clean(pbs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_100'] = {'inputs': ['pbs_replacement_d2_100'], 'func': pbs_replacement_d3_100}


def pbs_replacement_d3_101(pbs_replacement_d2_101):
    feature = _clean(pbs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_101'] = {'inputs': ['pbs_replacement_d2_101'], 'func': pbs_replacement_d3_101}


def pbs_replacement_d3_102(pbs_replacement_d2_102):
    feature = _clean(pbs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_102'] = {'inputs': ['pbs_replacement_d2_102'], 'func': pbs_replacement_d3_102}


def pbs_replacement_d3_103(pbs_replacement_d2_103):
    feature = _clean(pbs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_103'] = {'inputs': ['pbs_replacement_d2_103'], 'func': pbs_replacement_d3_103}


def pbs_replacement_d3_104(pbs_replacement_d2_104):
    feature = _clean(pbs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_104'] = {'inputs': ['pbs_replacement_d2_104'], 'func': pbs_replacement_d3_104}


def pbs_replacement_d3_105(pbs_replacement_d2_105):
    feature = _clean(pbs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_105'] = {'inputs': ['pbs_replacement_d2_105'], 'func': pbs_replacement_d3_105}


def pbs_replacement_d3_106(pbs_replacement_d2_106):
    feature = _clean(pbs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_106'] = {'inputs': ['pbs_replacement_d2_106'], 'func': pbs_replacement_d3_106}


def pbs_replacement_d3_107(pbs_replacement_d2_107):
    feature = _clean(pbs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_107'] = {'inputs': ['pbs_replacement_d2_107'], 'func': pbs_replacement_d3_107}


def pbs_replacement_d3_108(pbs_replacement_d2_108):
    feature = _clean(pbs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_108'] = {'inputs': ['pbs_replacement_d2_108'], 'func': pbs_replacement_d3_108}


def pbs_replacement_d3_109(pbs_replacement_d2_109):
    feature = _clean(pbs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_109'] = {'inputs': ['pbs_replacement_d2_109'], 'func': pbs_replacement_d3_109}


def pbs_replacement_d3_110(pbs_replacement_d2_110):
    feature = _clean(pbs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_110'] = {'inputs': ['pbs_replacement_d2_110'], 'func': pbs_replacement_d3_110}


def pbs_replacement_d3_111(pbs_replacement_d2_111):
    feature = _clean(pbs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_111'] = {'inputs': ['pbs_replacement_d2_111'], 'func': pbs_replacement_d3_111}


def pbs_replacement_d3_112(pbs_replacement_d2_112):
    feature = _clean(pbs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_112'] = {'inputs': ['pbs_replacement_d2_112'], 'func': pbs_replacement_d3_112}


def pbs_replacement_d3_113(pbs_replacement_d2_113):
    feature = _clean(pbs_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_113'] = {'inputs': ['pbs_replacement_d2_113'], 'func': pbs_replacement_d3_113}


def pbs_replacement_d3_114(pbs_replacement_d2_114):
    feature = _clean(pbs_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_114'] = {'inputs': ['pbs_replacement_d2_114'], 'func': pbs_replacement_d3_114}


def pbs_replacement_d3_115(pbs_replacement_d2_115):
    feature = _clean(pbs_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_115'] = {'inputs': ['pbs_replacement_d2_115'], 'func': pbs_replacement_d3_115}


def pbs_replacement_d3_116(pbs_replacement_d2_116):
    feature = _clean(pbs_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_116'] = {'inputs': ['pbs_replacement_d2_116'], 'func': pbs_replacement_d3_116}


def pbs_replacement_d3_117(pbs_replacement_d2_117):
    feature = _clean(pbs_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_117'] = {'inputs': ['pbs_replacement_d2_117'], 'func': pbs_replacement_d3_117}


def pbs_replacement_d3_118(pbs_replacement_d2_118):
    feature = _clean(pbs_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_118'] = {'inputs': ['pbs_replacement_d2_118'], 'func': pbs_replacement_d3_118}


def pbs_replacement_d3_119(pbs_replacement_d2_119):
    feature = _clean(pbs_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_119'] = {'inputs': ['pbs_replacement_d2_119'], 'func': pbs_replacement_d3_119}


def pbs_replacement_d3_120(pbs_replacement_d2_120):
    feature = _clean(pbs_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_120'] = {'inputs': ['pbs_replacement_d2_120'], 'func': pbs_replacement_d3_120}


def pbs_replacement_d3_121(pbs_replacement_d2_121):
    feature = _clean(pbs_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_121'] = {'inputs': ['pbs_replacement_d2_121'], 'func': pbs_replacement_d3_121}


def pbs_replacement_d3_122(pbs_replacement_d2_122):
    feature = _clean(pbs_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_122'] = {'inputs': ['pbs_replacement_d2_122'], 'func': pbs_replacement_d3_122}


def pbs_replacement_d3_123(pbs_replacement_d2_123):
    feature = _clean(pbs_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_123'] = {'inputs': ['pbs_replacement_d2_123'], 'func': pbs_replacement_d3_123}


def pbs_replacement_d3_124(pbs_replacement_d2_124):
    feature = _clean(pbs_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_124'] = {'inputs': ['pbs_replacement_d2_124'], 'func': pbs_replacement_d3_124}


def pbs_replacement_d3_125(pbs_replacement_d2_125):
    feature = _clean(pbs_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_125'] = {'inputs': ['pbs_replacement_d2_125'], 'func': pbs_replacement_d3_125}


def pbs_replacement_d3_126(pbs_replacement_d2_126):
    feature = _clean(pbs_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_126'] = {'inputs': ['pbs_replacement_d2_126'], 'func': pbs_replacement_d3_126}


def pbs_replacement_d3_127(pbs_replacement_d2_127):
    feature = _clean(pbs_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_127'] = {'inputs': ['pbs_replacement_d2_127'], 'func': pbs_replacement_d3_127}


def pbs_replacement_d3_128(pbs_replacement_d2_128):
    feature = _clean(pbs_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_128'] = {'inputs': ['pbs_replacement_d2_128'], 'func': pbs_replacement_d3_128}


def pbs_replacement_d3_129(pbs_replacement_d2_129):
    feature = _clean(pbs_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_129'] = {'inputs': ['pbs_replacement_d2_129'], 'func': pbs_replacement_d3_129}


def pbs_replacement_d3_130(pbs_replacement_d2_130):
    feature = _clean(pbs_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_130'] = {'inputs': ['pbs_replacement_d2_130'], 'func': pbs_replacement_d3_130}


def pbs_replacement_d3_131(pbs_replacement_d2_131):
    feature = _clean(pbs_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_131'] = {'inputs': ['pbs_replacement_d2_131'], 'func': pbs_replacement_d3_131}


def pbs_replacement_d3_132(pbs_replacement_d2_132):
    feature = _clean(pbs_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_132'] = {'inputs': ['pbs_replacement_d2_132'], 'func': pbs_replacement_d3_132}


def pbs_replacement_d3_133(pbs_replacement_d2_133):
    feature = _clean(pbs_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_133'] = {'inputs': ['pbs_replacement_d2_133'], 'func': pbs_replacement_d3_133}


def pbs_replacement_d3_134(pbs_replacement_d2_134):
    feature = _clean(pbs_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_134'] = {'inputs': ['pbs_replacement_d2_134'], 'func': pbs_replacement_d3_134}


def pbs_replacement_d3_135(pbs_replacement_d2_135):
    feature = _clean(pbs_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_135'] = {'inputs': ['pbs_replacement_d2_135'], 'func': pbs_replacement_d3_135}


def pbs_replacement_d3_136(pbs_replacement_d2_136):
    feature = _clean(pbs_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_136'] = {'inputs': ['pbs_replacement_d2_136'], 'func': pbs_replacement_d3_136}


def pbs_replacement_d3_137(pbs_replacement_d2_137):
    feature = _clean(pbs_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_137'] = {'inputs': ['pbs_replacement_d2_137'], 'func': pbs_replacement_d3_137}


def pbs_replacement_d3_138(pbs_replacement_d2_138):
    feature = _clean(pbs_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_138'] = {'inputs': ['pbs_replacement_d2_138'], 'func': pbs_replacement_d3_138}


def pbs_replacement_d3_139(pbs_replacement_d2_139):
    feature = _clean(pbs_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_139'] = {'inputs': ['pbs_replacement_d2_139'], 'func': pbs_replacement_d3_139}


def pbs_replacement_d3_140(pbs_replacement_d2_140):
    feature = _clean(pbs_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_140'] = {'inputs': ['pbs_replacement_d2_140'], 'func': pbs_replacement_d3_140}


def pbs_replacement_d3_141(pbs_replacement_d2_141):
    feature = _clean(pbs_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_141'] = {'inputs': ['pbs_replacement_d2_141'], 'func': pbs_replacement_d3_141}


def pbs_replacement_d3_142(pbs_replacement_d2_142):
    feature = _clean(pbs_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_142'] = {'inputs': ['pbs_replacement_d2_142'], 'func': pbs_replacement_d3_142}


def pbs_replacement_d3_143(pbs_replacement_d2_143):
    feature = _clean(pbs_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_143'] = {'inputs': ['pbs_replacement_d2_143'], 'func': pbs_replacement_d3_143}


def pbs_replacement_d3_144(pbs_replacement_d2_144):
    feature = _clean(pbs_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_144'] = {'inputs': ['pbs_replacement_d2_144'], 'func': pbs_replacement_d3_144}


def pbs_replacement_d3_145(pbs_replacement_d2_145):
    feature = _clean(pbs_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_145'] = {'inputs': ['pbs_replacement_d2_145'], 'func': pbs_replacement_d3_145}


def pbs_replacement_d3_146(pbs_replacement_d2_146):
    feature = _clean(pbs_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_146'] = {'inputs': ['pbs_replacement_d2_146'], 'func': pbs_replacement_d3_146}


def pbs_replacement_d3_147(pbs_replacement_d2_147):
    feature = _clean(pbs_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_147'] = {'inputs': ['pbs_replacement_d2_147'], 'func': pbs_replacement_d3_147}


def pbs_replacement_d3_148(pbs_replacement_d2_148):
    feature = _clean(pbs_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_148'] = {'inputs': ['pbs_replacement_d2_148'], 'func': pbs_replacement_d3_148}


def pbs_replacement_d3_149(pbs_replacement_d2_149):
    feature = _clean(pbs_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_149'] = {'inputs': ['pbs_replacement_d2_149'], 'func': pbs_replacement_d3_149}


def pbs_replacement_d3_150(pbs_replacement_d2_150):
    feature = _clean(pbs_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_150'] = {'inputs': ['pbs_replacement_d2_150'], 'func': pbs_replacement_d3_150}


def pbs_replacement_d3_151(pbs_replacement_d2_151):
    feature = _clean(pbs_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_151'] = {'inputs': ['pbs_replacement_d2_151'], 'func': pbs_replacement_d3_151}


def pbs_replacement_d3_152(pbs_replacement_d2_152):
    feature = _clean(pbs_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_152'] = {'inputs': ['pbs_replacement_d2_152'], 'func': pbs_replacement_d3_152}


def pbs_replacement_d3_153(pbs_replacement_d2_153):
    feature = _clean(pbs_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_153'] = {'inputs': ['pbs_replacement_d2_153'], 'func': pbs_replacement_d3_153}


def pbs_replacement_d3_154(pbs_replacement_d2_154):
    feature = _clean(pbs_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_154'] = {'inputs': ['pbs_replacement_d2_154'], 'func': pbs_replacement_d3_154}


def pbs_replacement_d3_155(pbs_replacement_d2_155):
    feature = _clean(pbs_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_155'] = {'inputs': ['pbs_replacement_d2_155'], 'func': pbs_replacement_d3_155}


def pbs_replacement_d3_156(pbs_replacement_d2_156):
    feature = _clean(pbs_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_156'] = {'inputs': ['pbs_replacement_d2_156'], 'func': pbs_replacement_d3_156}


def pbs_replacement_d3_157(pbs_replacement_d2_157):
    feature = _clean(pbs_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_157'] = {'inputs': ['pbs_replacement_d2_157'], 'func': pbs_replacement_d3_157}


def pbs_replacement_d3_158(pbs_replacement_d2_158):
    feature = _clean(pbs_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_158'] = {'inputs': ['pbs_replacement_d2_158'], 'func': pbs_replacement_d3_158}


def pbs_replacement_d3_159(pbs_replacement_d2_159):
    feature = _clean(pbs_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_159'] = {'inputs': ['pbs_replacement_d2_159'], 'func': pbs_replacement_d3_159}


def pbs_replacement_d3_160(pbs_replacement_d2_160):
    feature = _clean(pbs_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_160'] = {'inputs': ['pbs_replacement_d2_160'], 'func': pbs_replacement_d3_160}


def pbs_replacement_d3_161(pbs_replacement_d2_161):
    feature = _clean(pbs_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_161'] = {'inputs': ['pbs_replacement_d2_161'], 'func': pbs_replacement_d3_161}


def pbs_replacement_d3_162(pbs_replacement_d2_162):
    feature = _clean(pbs_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_162'] = {'inputs': ['pbs_replacement_d2_162'], 'func': pbs_replacement_d3_162}


def pbs_replacement_d3_163(pbs_replacement_d2_163):
    feature = _clean(pbs_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_163'] = {'inputs': ['pbs_replacement_d2_163'], 'func': pbs_replacement_d3_163}


def pbs_replacement_d3_164(pbs_replacement_d2_164):
    feature = _clean(pbs_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_164'] = {'inputs': ['pbs_replacement_d2_164'], 'func': pbs_replacement_d3_164}


def pbs_replacement_d3_165(pbs_replacement_d2_165):
    feature = _clean(pbs_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_165'] = {'inputs': ['pbs_replacement_d2_165'], 'func': pbs_replacement_d3_165}


def pbs_replacement_d3_166(pbs_replacement_d2_166):
    feature = _clean(pbs_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_166'] = {'inputs': ['pbs_replacement_d2_166'], 'func': pbs_replacement_d3_166}


def pbs_replacement_d3_167(pbs_replacement_d2_167):
    feature = _clean(pbs_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_167'] = {'inputs': ['pbs_replacement_d2_167'], 'func': pbs_replacement_d3_167}


def pbs_replacement_d3_168(pbs_replacement_d2_168):
    feature = _clean(pbs_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_168'] = {'inputs': ['pbs_replacement_d2_168'], 'func': pbs_replacement_d3_168}


def pbs_replacement_d3_169(pbs_replacement_d2_169):
    feature = _clean(pbs_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_169'] = {'inputs': ['pbs_replacement_d2_169'], 'func': pbs_replacement_d3_169}


def pbs_replacement_d3_170(pbs_replacement_d2_170):
    feature = _clean(pbs_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_170'] = {'inputs': ['pbs_replacement_d2_170'], 'func': pbs_replacement_d3_170}


def pbs_replacement_d3_171(pbs_replacement_d2_171):
    feature = _clean(pbs_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_171'] = {'inputs': ['pbs_replacement_d2_171'], 'func': pbs_replacement_d3_171}


def pbs_replacement_d3_172(pbs_replacement_d2_172):
    feature = _clean(pbs_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_172'] = {'inputs': ['pbs_replacement_d2_172'], 'func': pbs_replacement_d3_172}


def pbs_replacement_d3_173(pbs_replacement_d2_173):
    feature = _clean(pbs_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_173'] = {'inputs': ['pbs_replacement_d2_173'], 'func': pbs_replacement_d3_173}


def pbs_replacement_d3_174(pbs_replacement_d2_174):
    feature = _clean(pbs_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_174'] = {'inputs': ['pbs_replacement_d2_174'], 'func': pbs_replacement_d3_174}


def pbs_replacement_d3_175(pbs_replacement_d2_175):
    feature = _clean(pbs_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
PBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pbs_replacement_d3_175'] = {'inputs': ['pbs_replacement_d2_175'], 'func': pbs_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pbs_base_universe_d3_001_pbs_002_range_expansion_10_002(pbs_base_universe_d2_001_pbs_002_range_expansion_10_002):
    return _base_universe_d3(pbs_base_universe_d2_001_pbs_002_range_expansion_10_002, 1)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_001_pbs_002_range_expansion_10_002'] = {'inputs': ['pbs_base_universe_d2_001_pbs_002_range_expansion_10_002'], 'func': pbs_base_universe_d3_001_pbs_002_range_expansion_10_002}


def pbs_base_universe_d3_002_pbs_004_close_location_42_004(pbs_base_universe_d2_002_pbs_004_close_location_42_004):
    return _base_universe_d3(pbs_base_universe_d2_002_pbs_004_close_location_42_004, 2)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_002_pbs_004_close_location_42_004'] = {'inputs': ['pbs_base_universe_d2_002_pbs_004_close_location_42_004'], 'func': pbs_base_universe_d3_002_pbs_004_close_location_42_004}


def pbs_base_universe_d3_003_pbs_005_atr_move_63_005(pbs_base_universe_d2_003_pbs_005_atr_move_63_005):
    return _base_universe_d3(pbs_base_universe_d2_003_pbs_005_atr_move_63_005, 3)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_003_pbs_005_atr_move_63_005'] = {'inputs': ['pbs_base_universe_d2_003_pbs_005_atr_move_63_005'], 'func': pbs_base_universe_d3_003_pbs_005_atr_move_63_005}


def pbs_base_universe_d3_004_pbs_008_range_expansion_189_008(pbs_base_universe_d2_004_pbs_008_range_expansion_189_008):
    return _base_universe_d3(pbs_base_universe_d2_004_pbs_008_range_expansion_189_008, 4)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_004_pbs_008_range_expansion_189_008'] = {'inputs': ['pbs_base_universe_d2_004_pbs_008_range_expansion_189_008'], 'func': pbs_base_universe_d3_004_pbs_008_range_expansion_189_008}


def pbs_base_universe_d3_005_pbs_010_close_location_378_010(pbs_base_universe_d2_005_pbs_010_close_location_378_010):
    return _base_universe_d3(pbs_base_universe_d2_005_pbs_010_close_location_378_010, 5)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_005_pbs_010_close_location_378_010'] = {'inputs': ['pbs_base_universe_d2_005_pbs_010_close_location_378_010'], 'func': pbs_base_universe_d3_005_pbs_010_close_location_378_010}


def pbs_base_universe_d3_006_pbs_011_atr_move_504_011(pbs_base_universe_d2_006_pbs_011_atr_move_504_011):
    return _base_universe_d3(pbs_base_universe_d2_006_pbs_011_atr_move_504_011, 6)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_006_pbs_011_atr_move_504_011'] = {'inputs': ['pbs_base_universe_d2_006_pbs_011_atr_move_504_011'], 'func': pbs_base_universe_d3_006_pbs_011_atr_move_504_011}


def pbs_base_universe_d3_007_pbs_014_range_expansion_1260_014(pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014):
    return _base_universe_d3(pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014, 7)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_007_pbs_014_range_expansion_1260_014'] = {'inputs': ['pbs_base_universe_d2_007_pbs_014_range_expansion_1260_014'], 'func': pbs_base_universe_d3_007_pbs_014_range_expansion_1260_014}


def pbs_base_universe_d3_008_pbs_016_close_location_5_016(pbs_base_universe_d2_008_pbs_016_close_location_5_016):
    return _base_universe_d3(pbs_base_universe_d2_008_pbs_016_close_location_5_016, 8)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_008_pbs_016_close_location_5_016'] = {'inputs': ['pbs_base_universe_d2_008_pbs_016_close_location_5_016'], 'func': pbs_base_universe_d3_008_pbs_016_close_location_5_016}


def pbs_base_universe_d3_009_pbs_017_atr_move_10_017(pbs_base_universe_d2_009_pbs_017_atr_move_10_017):
    return _base_universe_d3(pbs_base_universe_d2_009_pbs_017_atr_move_10_017, 9)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_009_pbs_017_atr_move_10_017'] = {'inputs': ['pbs_base_universe_d2_009_pbs_017_atr_move_10_017'], 'func': pbs_base_universe_d3_009_pbs_017_atr_move_10_017}


def pbs_base_universe_d3_010_pbs_020_range_expansion_63_020(pbs_base_universe_d2_010_pbs_020_range_expansion_63_020):
    return _base_universe_d3(pbs_base_universe_d2_010_pbs_020_range_expansion_63_020, 10)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_010_pbs_020_range_expansion_63_020'] = {'inputs': ['pbs_base_universe_d2_010_pbs_020_range_expansion_63_020'], 'func': pbs_base_universe_d3_010_pbs_020_range_expansion_63_020}


def pbs_base_universe_d3_011_pbs_022_close_location_126_022(pbs_base_universe_d2_011_pbs_022_close_location_126_022):
    return _base_universe_d3(pbs_base_universe_d2_011_pbs_022_close_location_126_022, 11)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_011_pbs_022_close_location_126_022'] = {'inputs': ['pbs_base_universe_d2_011_pbs_022_close_location_126_022'], 'func': pbs_base_universe_d3_011_pbs_022_close_location_126_022}


def pbs_base_universe_d3_012_pbs_023_atr_move_189_023(pbs_base_universe_d2_012_pbs_023_atr_move_189_023):
    return _base_universe_d3(pbs_base_universe_d2_012_pbs_023_atr_move_189_023, 12)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_012_pbs_023_atr_move_189_023'] = {'inputs': ['pbs_base_universe_d2_012_pbs_023_atr_move_189_023'], 'func': pbs_base_universe_d3_012_pbs_023_atr_move_189_023}


def pbs_base_universe_d3_013_pbs_026_range_expansion_504_026(pbs_base_universe_d2_013_pbs_026_range_expansion_504_026):
    return _base_universe_d3(pbs_base_universe_d2_013_pbs_026_range_expansion_504_026, 13)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_013_pbs_026_range_expansion_504_026'] = {'inputs': ['pbs_base_universe_d2_013_pbs_026_range_expansion_504_026'], 'func': pbs_base_universe_d3_013_pbs_026_range_expansion_504_026}


def pbs_base_universe_d3_014_pbs_028_close_location_1008_028(pbs_base_universe_d2_014_pbs_028_close_location_1008_028):
    return _base_universe_d3(pbs_base_universe_d2_014_pbs_028_close_location_1008_028, 14)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_014_pbs_028_close_location_1008_028'] = {'inputs': ['pbs_base_universe_d2_014_pbs_028_close_location_1008_028'], 'func': pbs_base_universe_d3_014_pbs_028_close_location_1008_028}


def pbs_base_universe_d3_015_pbs_029_atr_move_1260_029(pbs_base_universe_d2_015_pbs_029_atr_move_1260_029):
    return _base_universe_d3(pbs_base_universe_d2_015_pbs_029_atr_move_1260_029, 15)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_015_pbs_029_atr_move_1260_029'] = {'inputs': ['pbs_base_universe_d2_015_pbs_029_atr_move_1260_029'], 'func': pbs_base_universe_d3_015_pbs_029_atr_move_1260_029}


def pbs_base_universe_d3_016_pbs_basefill_001(pbs_base_universe_d2_016_pbs_basefill_001):
    return _base_universe_d3(pbs_base_universe_d2_016_pbs_basefill_001, 16)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_016_pbs_basefill_001'] = {'inputs': ['pbs_base_universe_d2_016_pbs_basefill_001'], 'func': pbs_base_universe_d3_016_pbs_basefill_001}


def pbs_base_universe_d3_017_pbs_basefill_003(pbs_base_universe_d2_017_pbs_basefill_003):
    return _base_universe_d3(pbs_base_universe_d2_017_pbs_basefill_003, 17)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_017_pbs_basefill_003'] = {'inputs': ['pbs_base_universe_d2_017_pbs_basefill_003'], 'func': pbs_base_universe_d3_017_pbs_basefill_003}


def pbs_base_universe_d3_018_pbs_basefill_006(pbs_base_universe_d2_018_pbs_basefill_006):
    return _base_universe_d3(pbs_base_universe_d2_018_pbs_basefill_006, 18)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_018_pbs_basefill_006'] = {'inputs': ['pbs_base_universe_d2_018_pbs_basefill_006'], 'func': pbs_base_universe_d3_018_pbs_basefill_006}


def pbs_base_universe_d3_019_pbs_basefill_007(pbs_base_universe_d2_019_pbs_basefill_007):
    return _base_universe_d3(pbs_base_universe_d2_019_pbs_basefill_007, 19)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_019_pbs_basefill_007'] = {'inputs': ['pbs_base_universe_d2_019_pbs_basefill_007'], 'func': pbs_base_universe_d3_019_pbs_basefill_007}


def pbs_base_universe_d3_020_pbs_basefill_009(pbs_base_universe_d2_020_pbs_basefill_009):
    return _base_universe_d3(pbs_base_universe_d2_020_pbs_basefill_009, 20)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_020_pbs_basefill_009'] = {'inputs': ['pbs_base_universe_d2_020_pbs_basefill_009'], 'func': pbs_base_universe_d3_020_pbs_basefill_009}


def pbs_base_universe_d3_021_pbs_basefill_012(pbs_base_universe_d2_021_pbs_basefill_012):
    return _base_universe_d3(pbs_base_universe_d2_021_pbs_basefill_012, 21)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_021_pbs_basefill_012'] = {'inputs': ['pbs_base_universe_d2_021_pbs_basefill_012'], 'func': pbs_base_universe_d3_021_pbs_basefill_012}


def pbs_base_universe_d3_022_pbs_basefill_013(pbs_base_universe_d2_022_pbs_basefill_013):
    return _base_universe_d3(pbs_base_universe_d2_022_pbs_basefill_013, 22)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_022_pbs_basefill_013'] = {'inputs': ['pbs_base_universe_d2_022_pbs_basefill_013'], 'func': pbs_base_universe_d3_022_pbs_basefill_013}


def pbs_base_universe_d3_023_pbs_basefill_015(pbs_base_universe_d2_023_pbs_basefill_015):
    return _base_universe_d3(pbs_base_universe_d2_023_pbs_basefill_015, 23)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_023_pbs_basefill_015'] = {'inputs': ['pbs_base_universe_d2_023_pbs_basefill_015'], 'func': pbs_base_universe_d3_023_pbs_basefill_015}


def pbs_base_universe_d3_024_pbs_basefill_018(pbs_base_universe_d2_024_pbs_basefill_018):
    return _base_universe_d3(pbs_base_universe_d2_024_pbs_basefill_018, 24)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_024_pbs_basefill_018'] = {'inputs': ['pbs_base_universe_d2_024_pbs_basefill_018'], 'func': pbs_base_universe_d3_024_pbs_basefill_018}


def pbs_base_universe_d3_025_pbs_basefill_019(pbs_base_universe_d2_025_pbs_basefill_019):
    return _base_universe_d3(pbs_base_universe_d2_025_pbs_basefill_019, 25)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_025_pbs_basefill_019'] = {'inputs': ['pbs_base_universe_d2_025_pbs_basefill_019'], 'func': pbs_base_universe_d3_025_pbs_basefill_019}


def pbs_base_universe_d3_026_pbs_basefill_021(pbs_base_universe_d2_026_pbs_basefill_021):
    return _base_universe_d3(pbs_base_universe_d2_026_pbs_basefill_021, 26)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_026_pbs_basefill_021'] = {'inputs': ['pbs_base_universe_d2_026_pbs_basefill_021'], 'func': pbs_base_universe_d3_026_pbs_basefill_021}


def pbs_base_universe_d3_027_pbs_basefill_024(pbs_base_universe_d2_027_pbs_basefill_024):
    return _base_universe_d3(pbs_base_universe_d2_027_pbs_basefill_024, 27)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_027_pbs_basefill_024'] = {'inputs': ['pbs_base_universe_d2_027_pbs_basefill_024'], 'func': pbs_base_universe_d3_027_pbs_basefill_024}


def pbs_base_universe_d3_028_pbs_basefill_025(pbs_base_universe_d2_028_pbs_basefill_025):
    return _base_universe_d3(pbs_base_universe_d2_028_pbs_basefill_025, 28)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_028_pbs_basefill_025'] = {'inputs': ['pbs_base_universe_d2_028_pbs_basefill_025'], 'func': pbs_base_universe_d3_028_pbs_basefill_025}


def pbs_base_universe_d3_029_pbs_basefill_027(pbs_base_universe_d2_029_pbs_basefill_027):
    return _base_universe_d3(pbs_base_universe_d2_029_pbs_basefill_027, 29)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_029_pbs_basefill_027'] = {'inputs': ['pbs_base_universe_d2_029_pbs_basefill_027'], 'func': pbs_base_universe_d3_029_pbs_basefill_027}


def pbs_base_universe_d3_030_pbs_basefill_030(pbs_base_universe_d2_030_pbs_basefill_030):
    return _base_universe_d3(pbs_base_universe_d2_030_pbs_basefill_030, 30)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_030_pbs_basefill_030'] = {'inputs': ['pbs_base_universe_d2_030_pbs_basefill_030'], 'func': pbs_base_universe_d3_030_pbs_basefill_030}


def pbs_base_universe_d3_031_pbs_basefill_031(pbs_base_universe_d2_031_pbs_basefill_031):
    return _base_universe_d3(pbs_base_universe_d2_031_pbs_basefill_031, 31)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_031_pbs_basefill_031'] = {'inputs': ['pbs_base_universe_d2_031_pbs_basefill_031'], 'func': pbs_base_universe_d3_031_pbs_basefill_031}


def pbs_base_universe_d3_032_pbs_basefill_032(pbs_base_universe_d2_032_pbs_basefill_032):
    return _base_universe_d3(pbs_base_universe_d2_032_pbs_basefill_032, 32)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_032_pbs_basefill_032'] = {'inputs': ['pbs_base_universe_d2_032_pbs_basefill_032'], 'func': pbs_base_universe_d3_032_pbs_basefill_032}


def pbs_base_universe_d3_033_pbs_basefill_033(pbs_base_universe_d2_033_pbs_basefill_033):
    return _base_universe_d3(pbs_base_universe_d2_033_pbs_basefill_033, 33)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_033_pbs_basefill_033'] = {'inputs': ['pbs_base_universe_d2_033_pbs_basefill_033'], 'func': pbs_base_universe_d3_033_pbs_basefill_033}


def pbs_base_universe_d3_034_pbs_basefill_034(pbs_base_universe_d2_034_pbs_basefill_034):
    return _base_universe_d3(pbs_base_universe_d2_034_pbs_basefill_034, 34)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_034_pbs_basefill_034'] = {'inputs': ['pbs_base_universe_d2_034_pbs_basefill_034'], 'func': pbs_base_universe_d3_034_pbs_basefill_034}


def pbs_base_universe_d3_035_pbs_basefill_035(pbs_base_universe_d2_035_pbs_basefill_035):
    return _base_universe_d3(pbs_base_universe_d2_035_pbs_basefill_035, 35)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_035_pbs_basefill_035'] = {'inputs': ['pbs_base_universe_d2_035_pbs_basefill_035'], 'func': pbs_base_universe_d3_035_pbs_basefill_035}


def pbs_base_universe_d3_036_pbs_basefill_036(pbs_base_universe_d2_036_pbs_basefill_036):
    return _base_universe_d3(pbs_base_universe_d2_036_pbs_basefill_036, 36)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_036_pbs_basefill_036'] = {'inputs': ['pbs_base_universe_d2_036_pbs_basefill_036'], 'func': pbs_base_universe_d3_036_pbs_basefill_036}


def pbs_base_universe_d3_037_pbs_basefill_037(pbs_base_universe_d2_037_pbs_basefill_037):
    return _base_universe_d3(pbs_base_universe_d2_037_pbs_basefill_037, 37)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_037_pbs_basefill_037'] = {'inputs': ['pbs_base_universe_d2_037_pbs_basefill_037'], 'func': pbs_base_universe_d3_037_pbs_basefill_037}


def pbs_base_universe_d3_038_pbs_basefill_038(pbs_base_universe_d2_038_pbs_basefill_038):
    return _base_universe_d3(pbs_base_universe_d2_038_pbs_basefill_038, 38)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_038_pbs_basefill_038'] = {'inputs': ['pbs_base_universe_d2_038_pbs_basefill_038'], 'func': pbs_base_universe_d3_038_pbs_basefill_038}


def pbs_base_universe_d3_039_pbs_basefill_039(pbs_base_universe_d2_039_pbs_basefill_039):
    return _base_universe_d3(pbs_base_universe_d2_039_pbs_basefill_039, 39)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_039_pbs_basefill_039'] = {'inputs': ['pbs_base_universe_d2_039_pbs_basefill_039'], 'func': pbs_base_universe_d3_039_pbs_basefill_039}


def pbs_base_universe_d3_040_pbs_basefill_040(pbs_base_universe_d2_040_pbs_basefill_040):
    return _base_universe_d3(pbs_base_universe_d2_040_pbs_basefill_040, 40)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_040_pbs_basefill_040'] = {'inputs': ['pbs_base_universe_d2_040_pbs_basefill_040'], 'func': pbs_base_universe_d3_040_pbs_basefill_040}


def pbs_base_universe_d3_041_pbs_basefill_041(pbs_base_universe_d2_041_pbs_basefill_041):
    return _base_universe_d3(pbs_base_universe_d2_041_pbs_basefill_041, 41)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_041_pbs_basefill_041'] = {'inputs': ['pbs_base_universe_d2_041_pbs_basefill_041'], 'func': pbs_base_universe_d3_041_pbs_basefill_041}


def pbs_base_universe_d3_042_pbs_basefill_042(pbs_base_universe_d2_042_pbs_basefill_042):
    return _base_universe_d3(pbs_base_universe_d2_042_pbs_basefill_042, 42)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_042_pbs_basefill_042'] = {'inputs': ['pbs_base_universe_d2_042_pbs_basefill_042'], 'func': pbs_base_universe_d3_042_pbs_basefill_042}


def pbs_base_universe_d3_043_pbs_basefill_043(pbs_base_universe_d2_043_pbs_basefill_043):
    return _base_universe_d3(pbs_base_universe_d2_043_pbs_basefill_043, 43)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_043_pbs_basefill_043'] = {'inputs': ['pbs_base_universe_d2_043_pbs_basefill_043'], 'func': pbs_base_universe_d3_043_pbs_basefill_043}


def pbs_base_universe_d3_044_pbs_basefill_044(pbs_base_universe_d2_044_pbs_basefill_044):
    return _base_universe_d3(pbs_base_universe_d2_044_pbs_basefill_044, 44)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_044_pbs_basefill_044'] = {'inputs': ['pbs_base_universe_d2_044_pbs_basefill_044'], 'func': pbs_base_universe_d3_044_pbs_basefill_044}


def pbs_base_universe_d3_045_pbs_basefill_045(pbs_base_universe_d2_045_pbs_basefill_045):
    return _base_universe_d3(pbs_base_universe_d2_045_pbs_basefill_045, 45)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_045_pbs_basefill_045'] = {'inputs': ['pbs_base_universe_d2_045_pbs_basefill_045'], 'func': pbs_base_universe_d3_045_pbs_basefill_045}


def pbs_base_universe_d3_046_pbs_basefill_046(pbs_base_universe_d2_046_pbs_basefill_046):
    return _base_universe_d3(pbs_base_universe_d2_046_pbs_basefill_046, 46)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_046_pbs_basefill_046'] = {'inputs': ['pbs_base_universe_d2_046_pbs_basefill_046'], 'func': pbs_base_universe_d3_046_pbs_basefill_046}


def pbs_base_universe_d3_047_pbs_basefill_047(pbs_base_universe_d2_047_pbs_basefill_047):
    return _base_universe_d3(pbs_base_universe_d2_047_pbs_basefill_047, 47)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_047_pbs_basefill_047'] = {'inputs': ['pbs_base_universe_d2_047_pbs_basefill_047'], 'func': pbs_base_universe_d3_047_pbs_basefill_047}


def pbs_base_universe_d3_048_pbs_basefill_048(pbs_base_universe_d2_048_pbs_basefill_048):
    return _base_universe_d3(pbs_base_universe_d2_048_pbs_basefill_048, 48)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_048_pbs_basefill_048'] = {'inputs': ['pbs_base_universe_d2_048_pbs_basefill_048'], 'func': pbs_base_universe_d3_048_pbs_basefill_048}


def pbs_base_universe_d3_049_pbs_basefill_049(pbs_base_universe_d2_049_pbs_basefill_049):
    return _base_universe_d3(pbs_base_universe_d2_049_pbs_basefill_049, 49)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_049_pbs_basefill_049'] = {'inputs': ['pbs_base_universe_d2_049_pbs_basefill_049'], 'func': pbs_base_universe_d3_049_pbs_basefill_049}


def pbs_base_universe_d3_050_pbs_basefill_050(pbs_base_universe_d2_050_pbs_basefill_050):
    return _base_universe_d3(pbs_base_universe_d2_050_pbs_basefill_050, 50)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_050_pbs_basefill_050'] = {'inputs': ['pbs_base_universe_d2_050_pbs_basefill_050'], 'func': pbs_base_universe_d3_050_pbs_basefill_050}


def pbs_base_universe_d3_051_pbs_basefill_051(pbs_base_universe_d2_051_pbs_basefill_051):
    return _base_universe_d3(pbs_base_universe_d2_051_pbs_basefill_051, 51)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_051_pbs_basefill_051'] = {'inputs': ['pbs_base_universe_d2_051_pbs_basefill_051'], 'func': pbs_base_universe_d3_051_pbs_basefill_051}


def pbs_base_universe_d3_052_pbs_basefill_052(pbs_base_universe_d2_052_pbs_basefill_052):
    return _base_universe_d3(pbs_base_universe_d2_052_pbs_basefill_052, 52)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_052_pbs_basefill_052'] = {'inputs': ['pbs_base_universe_d2_052_pbs_basefill_052'], 'func': pbs_base_universe_d3_052_pbs_basefill_052}


def pbs_base_universe_d3_053_pbs_basefill_053(pbs_base_universe_d2_053_pbs_basefill_053):
    return _base_universe_d3(pbs_base_universe_d2_053_pbs_basefill_053, 53)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_053_pbs_basefill_053'] = {'inputs': ['pbs_base_universe_d2_053_pbs_basefill_053'], 'func': pbs_base_universe_d3_053_pbs_basefill_053}


def pbs_base_universe_d3_054_pbs_basefill_054(pbs_base_universe_d2_054_pbs_basefill_054):
    return _base_universe_d3(pbs_base_universe_d2_054_pbs_basefill_054, 54)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_054_pbs_basefill_054'] = {'inputs': ['pbs_base_universe_d2_054_pbs_basefill_054'], 'func': pbs_base_universe_d3_054_pbs_basefill_054}


def pbs_base_universe_d3_055_pbs_basefill_055(pbs_base_universe_d2_055_pbs_basefill_055):
    return _base_universe_d3(pbs_base_universe_d2_055_pbs_basefill_055, 55)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_055_pbs_basefill_055'] = {'inputs': ['pbs_base_universe_d2_055_pbs_basefill_055'], 'func': pbs_base_universe_d3_055_pbs_basefill_055}


def pbs_base_universe_d3_056_pbs_basefill_056(pbs_base_universe_d2_056_pbs_basefill_056):
    return _base_universe_d3(pbs_base_universe_d2_056_pbs_basefill_056, 56)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_056_pbs_basefill_056'] = {'inputs': ['pbs_base_universe_d2_056_pbs_basefill_056'], 'func': pbs_base_universe_d3_056_pbs_basefill_056}


def pbs_base_universe_d3_057_pbs_basefill_057(pbs_base_universe_d2_057_pbs_basefill_057):
    return _base_universe_d3(pbs_base_universe_d2_057_pbs_basefill_057, 57)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_057_pbs_basefill_057'] = {'inputs': ['pbs_base_universe_d2_057_pbs_basefill_057'], 'func': pbs_base_universe_d3_057_pbs_basefill_057}


def pbs_base_universe_d3_058_pbs_basefill_058(pbs_base_universe_d2_058_pbs_basefill_058):
    return _base_universe_d3(pbs_base_universe_d2_058_pbs_basefill_058, 58)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_058_pbs_basefill_058'] = {'inputs': ['pbs_base_universe_d2_058_pbs_basefill_058'], 'func': pbs_base_universe_d3_058_pbs_basefill_058}


def pbs_base_universe_d3_059_pbs_basefill_059(pbs_base_universe_d2_059_pbs_basefill_059):
    return _base_universe_d3(pbs_base_universe_d2_059_pbs_basefill_059, 59)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_059_pbs_basefill_059'] = {'inputs': ['pbs_base_universe_d2_059_pbs_basefill_059'], 'func': pbs_base_universe_d3_059_pbs_basefill_059}


def pbs_base_universe_d3_060_pbs_basefill_060(pbs_base_universe_d2_060_pbs_basefill_060):
    return _base_universe_d3(pbs_base_universe_d2_060_pbs_basefill_060, 60)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_060_pbs_basefill_060'] = {'inputs': ['pbs_base_universe_d2_060_pbs_basefill_060'], 'func': pbs_base_universe_d3_060_pbs_basefill_060}


def pbs_base_universe_d3_061_pbs_basefill_061(pbs_base_universe_d2_061_pbs_basefill_061):
    return _base_universe_d3(pbs_base_universe_d2_061_pbs_basefill_061, 61)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_061_pbs_basefill_061'] = {'inputs': ['pbs_base_universe_d2_061_pbs_basefill_061'], 'func': pbs_base_universe_d3_061_pbs_basefill_061}


def pbs_base_universe_d3_062_pbs_basefill_062(pbs_base_universe_d2_062_pbs_basefill_062):
    return _base_universe_d3(pbs_base_universe_d2_062_pbs_basefill_062, 62)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_062_pbs_basefill_062'] = {'inputs': ['pbs_base_universe_d2_062_pbs_basefill_062'], 'func': pbs_base_universe_d3_062_pbs_basefill_062}


def pbs_base_universe_d3_063_pbs_basefill_063(pbs_base_universe_d2_063_pbs_basefill_063):
    return _base_universe_d3(pbs_base_universe_d2_063_pbs_basefill_063, 63)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_063_pbs_basefill_063'] = {'inputs': ['pbs_base_universe_d2_063_pbs_basefill_063'], 'func': pbs_base_universe_d3_063_pbs_basefill_063}


def pbs_base_universe_d3_064_pbs_basefill_064(pbs_base_universe_d2_064_pbs_basefill_064):
    return _base_universe_d3(pbs_base_universe_d2_064_pbs_basefill_064, 64)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_064_pbs_basefill_064'] = {'inputs': ['pbs_base_universe_d2_064_pbs_basefill_064'], 'func': pbs_base_universe_d3_064_pbs_basefill_064}


def pbs_base_universe_d3_065_pbs_basefill_065(pbs_base_universe_d2_065_pbs_basefill_065):
    return _base_universe_d3(pbs_base_universe_d2_065_pbs_basefill_065, 65)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_065_pbs_basefill_065'] = {'inputs': ['pbs_base_universe_d2_065_pbs_basefill_065'], 'func': pbs_base_universe_d3_065_pbs_basefill_065}


def pbs_base_universe_d3_066_pbs_basefill_066(pbs_base_universe_d2_066_pbs_basefill_066):
    return _base_universe_d3(pbs_base_universe_d2_066_pbs_basefill_066, 66)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_066_pbs_basefill_066'] = {'inputs': ['pbs_base_universe_d2_066_pbs_basefill_066'], 'func': pbs_base_universe_d3_066_pbs_basefill_066}


def pbs_base_universe_d3_067_pbs_basefill_067(pbs_base_universe_d2_067_pbs_basefill_067):
    return _base_universe_d3(pbs_base_universe_d2_067_pbs_basefill_067, 67)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_067_pbs_basefill_067'] = {'inputs': ['pbs_base_universe_d2_067_pbs_basefill_067'], 'func': pbs_base_universe_d3_067_pbs_basefill_067}


def pbs_base_universe_d3_068_pbs_basefill_068(pbs_base_universe_d2_068_pbs_basefill_068):
    return _base_universe_d3(pbs_base_universe_d2_068_pbs_basefill_068, 68)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_068_pbs_basefill_068'] = {'inputs': ['pbs_base_universe_d2_068_pbs_basefill_068'], 'func': pbs_base_universe_d3_068_pbs_basefill_068}


def pbs_base_universe_d3_069_pbs_basefill_069(pbs_base_universe_d2_069_pbs_basefill_069):
    return _base_universe_d3(pbs_base_universe_d2_069_pbs_basefill_069, 69)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_069_pbs_basefill_069'] = {'inputs': ['pbs_base_universe_d2_069_pbs_basefill_069'], 'func': pbs_base_universe_d3_069_pbs_basefill_069}


def pbs_base_universe_d3_070_pbs_basefill_070(pbs_base_universe_d2_070_pbs_basefill_070):
    return _base_universe_d3(pbs_base_universe_d2_070_pbs_basefill_070, 70)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_070_pbs_basefill_070'] = {'inputs': ['pbs_base_universe_d2_070_pbs_basefill_070'], 'func': pbs_base_universe_d3_070_pbs_basefill_070}


def pbs_base_universe_d3_071_pbs_basefill_071(pbs_base_universe_d2_071_pbs_basefill_071):
    return _base_universe_d3(pbs_base_universe_d2_071_pbs_basefill_071, 71)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_071_pbs_basefill_071'] = {'inputs': ['pbs_base_universe_d2_071_pbs_basefill_071'], 'func': pbs_base_universe_d3_071_pbs_basefill_071}


def pbs_base_universe_d3_072_pbs_basefill_072(pbs_base_universe_d2_072_pbs_basefill_072):
    return _base_universe_d3(pbs_base_universe_d2_072_pbs_basefill_072, 72)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_072_pbs_basefill_072'] = {'inputs': ['pbs_base_universe_d2_072_pbs_basefill_072'], 'func': pbs_base_universe_d3_072_pbs_basefill_072}


def pbs_base_universe_d3_073_pbs_basefill_073(pbs_base_universe_d2_073_pbs_basefill_073):
    return _base_universe_d3(pbs_base_universe_d2_073_pbs_basefill_073, 73)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_073_pbs_basefill_073'] = {'inputs': ['pbs_base_universe_d2_073_pbs_basefill_073'], 'func': pbs_base_universe_d3_073_pbs_basefill_073}


def pbs_base_universe_d3_074_pbs_basefill_074(pbs_base_universe_d2_074_pbs_basefill_074):
    return _base_universe_d3(pbs_base_universe_d2_074_pbs_basefill_074, 74)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_074_pbs_basefill_074'] = {'inputs': ['pbs_base_universe_d2_074_pbs_basefill_074'], 'func': pbs_base_universe_d3_074_pbs_basefill_074}


def pbs_base_universe_d3_075_pbs_basefill_075(pbs_base_universe_d2_075_pbs_basefill_075):
    return _base_universe_d3(pbs_base_universe_d2_075_pbs_basefill_075, 75)
PBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pbs_base_universe_d3_075_pbs_basefill_075'] = {'inputs': ['pbs_base_universe_d2_075_pbs_basefill_075'], 'func': pbs_base_universe_d3_075_pbs_basefill_075}
