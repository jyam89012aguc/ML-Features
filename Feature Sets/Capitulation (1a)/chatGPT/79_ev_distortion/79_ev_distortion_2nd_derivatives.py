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



def evd_151_evd_001_pe_compression_z_21_roc_1(evd_001_pe_compression_z_21):
    feature = _s(evd_001_pe_compression_z_21)
    return (_roc(feature, 1)).reindex(feature.index)

def evd_152_evd_007_earnings_yield_spike_252_roc_42(evd_007_earnings_yield_spike_252):
    feature = _s(evd_007_earnings_yield_spike_252)
    return (_roc(feature, 42)).reindex(feature.index)

def evd_153_evd_013_ev_marketcap_gap_1512_roc_126(evd_013_ev_marketcap_gap_1512):
    feature = _s(evd_013_ev_marketcap_gap_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def evd_154_evd_019_ps_compression_z_84_roc_378(evd_019_ps_compression_z_84):
    feature = _s(evd_019_ps_compression_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def evd_155_evd_025_pe_compression_z_756_roc_4(evd_025_pe_compression_z_756):
    feature = _s(evd_025_pe_compression_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















EV_DISTORTION_REGISTRY_2ND_DERIVATIVES = {
    'evd_151_evd_001_pe_compression_z_21_roc_1': {'inputs': ['evd_001_pe_compression_z_21'], 'func': evd_151_evd_001_pe_compression_z_21_roc_1},
    'evd_152_evd_007_earnings_yield_spike_252_roc_42': {'inputs': ['evd_007_earnings_yield_spike_252'], 'func': evd_152_evd_007_earnings_yield_spike_252_roc_42},
    'evd_153_evd_013_ev_marketcap_gap_1512_roc_126': {'inputs': ['evd_013_ev_marketcap_gap_1512'], 'func': evd_153_evd_013_ev_marketcap_gap_1512_roc_126},
    'evd_154_evd_019_ps_compression_z_84_roc_378': {'inputs': ['evd_019_ps_compression_z_84'], 'func': evd_154_evd_019_ps_compression_z_84_roc_378},
    'evd_155_evd_025_pe_compression_z_756_roc_4': {'inputs': ['evd_025_pe_compression_z_756'], 'func': evd_155_evd_025_pe_compression_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ed_replacement_d2_001(evd_025_pe_compression_z_756):
    feature = _clean(evd_025_pe_compression_z_756)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_001'] = {'inputs': ['evd_025_pe_compression_z_756'], 'func': ed_replacement_d2_001}


def ed_replacement_d2_002(ed_replacement_001):
    feature = _clean(ed_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_002'] = {'inputs': ['ed_replacement_001'], 'func': ed_replacement_d2_002}


def ed_replacement_d2_003(ed_replacement_002):
    feature = _clean(ed_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_003'] = {'inputs': ['ed_replacement_002'], 'func': ed_replacement_d2_003}


def ed_replacement_d2_004(ed_replacement_003):
    feature = _clean(ed_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_004'] = {'inputs': ['ed_replacement_003'], 'func': ed_replacement_d2_004}


def ed_replacement_d2_005(ed_replacement_004):
    feature = _clean(ed_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_005'] = {'inputs': ['ed_replacement_004'], 'func': ed_replacement_d2_005}


def ed_replacement_d2_006(ed_replacement_005):
    feature = _clean(ed_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_006'] = {'inputs': ['ed_replacement_005'], 'func': ed_replacement_d2_006}


def ed_replacement_d2_007(ed_replacement_006):
    feature = _clean(ed_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_007'] = {'inputs': ['ed_replacement_006'], 'func': ed_replacement_d2_007}


def ed_replacement_d2_008(ed_replacement_007):
    feature = _clean(ed_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_008'] = {'inputs': ['ed_replacement_007'], 'func': ed_replacement_d2_008}


def ed_replacement_d2_009(ed_replacement_008):
    feature = _clean(ed_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_009'] = {'inputs': ['ed_replacement_008'], 'func': ed_replacement_d2_009}


def ed_replacement_d2_010(ed_replacement_009):
    feature = _clean(ed_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_010'] = {'inputs': ['ed_replacement_009'], 'func': ed_replacement_d2_010}


def ed_replacement_d2_011(ed_replacement_010):
    feature = _clean(ed_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_011'] = {'inputs': ['ed_replacement_010'], 'func': ed_replacement_d2_011}


def ed_replacement_d2_012(ed_replacement_011):
    feature = _clean(ed_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_012'] = {'inputs': ['ed_replacement_011'], 'func': ed_replacement_d2_012}


def ed_replacement_d2_013(ed_replacement_012):
    feature = _clean(ed_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_013'] = {'inputs': ['ed_replacement_012'], 'func': ed_replacement_d2_013}


def ed_replacement_d2_014(ed_replacement_013):
    feature = _clean(ed_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_014'] = {'inputs': ['ed_replacement_013'], 'func': ed_replacement_d2_014}


def ed_replacement_d2_015(ed_replacement_014):
    feature = _clean(ed_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_015'] = {'inputs': ['ed_replacement_014'], 'func': ed_replacement_d2_015}


def ed_replacement_d2_016(ed_replacement_015):
    feature = _clean(ed_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_016'] = {'inputs': ['ed_replacement_015'], 'func': ed_replacement_d2_016}


def ed_replacement_d2_017(ed_replacement_016):
    feature = _clean(ed_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_017'] = {'inputs': ['ed_replacement_016'], 'func': ed_replacement_d2_017}


def ed_replacement_d2_018(ed_replacement_017):
    feature = _clean(ed_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_018'] = {'inputs': ['ed_replacement_017'], 'func': ed_replacement_d2_018}


def ed_replacement_d2_019(ed_replacement_018):
    feature = _clean(ed_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_019'] = {'inputs': ['ed_replacement_018'], 'func': ed_replacement_d2_019}


def ed_replacement_d2_020(ed_replacement_019):
    feature = _clean(ed_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_020'] = {'inputs': ['ed_replacement_019'], 'func': ed_replacement_d2_020}


def ed_replacement_d2_021(ed_replacement_020):
    feature = _clean(ed_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_021'] = {'inputs': ['ed_replacement_020'], 'func': ed_replacement_d2_021}


def ed_replacement_d2_022(ed_replacement_021):
    feature = _clean(ed_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_022'] = {'inputs': ['ed_replacement_021'], 'func': ed_replacement_d2_022}


def ed_replacement_d2_023(ed_replacement_022):
    feature = _clean(ed_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_023'] = {'inputs': ['ed_replacement_022'], 'func': ed_replacement_d2_023}


def ed_replacement_d2_024(ed_replacement_023):
    feature = _clean(ed_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_024'] = {'inputs': ['ed_replacement_023'], 'func': ed_replacement_d2_024}


def ed_replacement_d2_025(ed_replacement_024):
    feature = _clean(ed_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_025'] = {'inputs': ['ed_replacement_024'], 'func': ed_replacement_d2_025}


def ed_replacement_d2_026(ed_replacement_025):
    feature = _clean(ed_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_026'] = {'inputs': ['ed_replacement_025'], 'func': ed_replacement_d2_026}


def ed_replacement_d2_027(ed_replacement_026):
    feature = _clean(ed_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_027'] = {'inputs': ['ed_replacement_026'], 'func': ed_replacement_d2_027}


def ed_replacement_d2_028(ed_replacement_027):
    feature = _clean(ed_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_028'] = {'inputs': ['ed_replacement_027'], 'func': ed_replacement_d2_028}


def ed_replacement_d2_029(ed_replacement_028):
    feature = _clean(ed_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_029'] = {'inputs': ['ed_replacement_028'], 'func': ed_replacement_d2_029}


def ed_replacement_d2_030(ed_replacement_029):
    feature = _clean(ed_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_030'] = {'inputs': ['ed_replacement_029'], 'func': ed_replacement_d2_030}


def ed_replacement_d2_031(ed_replacement_030):
    feature = _clean(ed_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_031'] = {'inputs': ['ed_replacement_030'], 'func': ed_replacement_d2_031}


def ed_replacement_d2_032(ed_replacement_031):
    feature = _clean(ed_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_032'] = {'inputs': ['ed_replacement_031'], 'func': ed_replacement_d2_032}


def ed_replacement_d2_033(ed_replacement_032):
    feature = _clean(ed_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_033'] = {'inputs': ['ed_replacement_032'], 'func': ed_replacement_d2_033}


def ed_replacement_d2_034(ed_replacement_033):
    feature = _clean(ed_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_034'] = {'inputs': ['ed_replacement_033'], 'func': ed_replacement_d2_034}


def ed_replacement_d2_035(ed_replacement_034):
    feature = _clean(ed_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_035'] = {'inputs': ['ed_replacement_034'], 'func': ed_replacement_d2_035}


def ed_replacement_d2_036(ed_replacement_035):
    feature = _clean(ed_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_036'] = {'inputs': ['ed_replacement_035'], 'func': ed_replacement_d2_036}


def ed_replacement_d2_037(ed_replacement_036):
    feature = _clean(ed_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_037'] = {'inputs': ['ed_replacement_036'], 'func': ed_replacement_d2_037}


def ed_replacement_d2_038(ed_replacement_037):
    feature = _clean(ed_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_038'] = {'inputs': ['ed_replacement_037'], 'func': ed_replacement_d2_038}


def ed_replacement_d2_039(ed_replacement_038):
    feature = _clean(ed_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_039'] = {'inputs': ['ed_replacement_038'], 'func': ed_replacement_d2_039}


def ed_replacement_d2_040(ed_replacement_039):
    feature = _clean(ed_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_040'] = {'inputs': ['ed_replacement_039'], 'func': ed_replacement_d2_040}


def ed_replacement_d2_041(ed_replacement_040):
    feature = _clean(ed_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_041'] = {'inputs': ['ed_replacement_040'], 'func': ed_replacement_d2_041}


def ed_replacement_d2_042(ed_replacement_041):
    feature = _clean(ed_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_042'] = {'inputs': ['ed_replacement_041'], 'func': ed_replacement_d2_042}


def ed_replacement_d2_043(ed_replacement_042):
    feature = _clean(ed_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_043'] = {'inputs': ['ed_replacement_042'], 'func': ed_replacement_d2_043}


def ed_replacement_d2_044(ed_replacement_043):
    feature = _clean(ed_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_044'] = {'inputs': ['ed_replacement_043'], 'func': ed_replacement_d2_044}


def ed_replacement_d2_045(ed_replacement_044):
    feature = _clean(ed_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_045'] = {'inputs': ['ed_replacement_044'], 'func': ed_replacement_d2_045}


def ed_replacement_d2_046(ed_replacement_045):
    feature = _clean(ed_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_046'] = {'inputs': ['ed_replacement_045'], 'func': ed_replacement_d2_046}


def ed_replacement_d2_047(ed_replacement_046):
    feature = _clean(ed_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_047'] = {'inputs': ['ed_replacement_046'], 'func': ed_replacement_d2_047}


def ed_replacement_d2_048(ed_replacement_047):
    feature = _clean(ed_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_048'] = {'inputs': ['ed_replacement_047'], 'func': ed_replacement_d2_048}


def ed_replacement_d2_049(ed_replacement_048):
    feature = _clean(ed_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_049'] = {'inputs': ['ed_replacement_048'], 'func': ed_replacement_d2_049}


def ed_replacement_d2_050(ed_replacement_049):
    feature = _clean(ed_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_050'] = {'inputs': ['ed_replacement_049'], 'func': ed_replacement_d2_050}


def ed_replacement_d2_051(ed_replacement_050):
    feature = _clean(ed_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_051'] = {'inputs': ['ed_replacement_050'], 'func': ed_replacement_d2_051}


def ed_replacement_d2_052(ed_replacement_051):
    feature = _clean(ed_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_052'] = {'inputs': ['ed_replacement_051'], 'func': ed_replacement_d2_052}


def ed_replacement_d2_053(ed_replacement_052):
    feature = _clean(ed_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_053'] = {'inputs': ['ed_replacement_052'], 'func': ed_replacement_d2_053}


def ed_replacement_d2_054(ed_replacement_053):
    feature = _clean(ed_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_054'] = {'inputs': ['ed_replacement_053'], 'func': ed_replacement_d2_054}


def ed_replacement_d2_055(ed_replacement_054):
    feature = _clean(ed_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_055'] = {'inputs': ['ed_replacement_054'], 'func': ed_replacement_d2_055}


def ed_replacement_d2_056(ed_replacement_055):
    feature = _clean(ed_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_056'] = {'inputs': ['ed_replacement_055'], 'func': ed_replacement_d2_056}


def ed_replacement_d2_057(ed_replacement_056):
    feature = _clean(ed_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_057'] = {'inputs': ['ed_replacement_056'], 'func': ed_replacement_d2_057}


def ed_replacement_d2_058(ed_replacement_057):
    feature = _clean(ed_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_058'] = {'inputs': ['ed_replacement_057'], 'func': ed_replacement_d2_058}


def ed_replacement_d2_059(ed_replacement_058):
    feature = _clean(ed_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_059'] = {'inputs': ['ed_replacement_058'], 'func': ed_replacement_d2_059}


def ed_replacement_d2_060(ed_replacement_059):
    feature = _clean(ed_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_060'] = {'inputs': ['ed_replacement_059'], 'func': ed_replacement_d2_060}


def ed_replacement_d2_061(ed_replacement_060):
    feature = _clean(ed_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_061'] = {'inputs': ['ed_replacement_060'], 'func': ed_replacement_d2_061}


def ed_replacement_d2_062(ed_replacement_061):
    feature = _clean(ed_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_062'] = {'inputs': ['ed_replacement_061'], 'func': ed_replacement_d2_062}


def ed_replacement_d2_063(ed_replacement_062):
    feature = _clean(ed_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_063'] = {'inputs': ['ed_replacement_062'], 'func': ed_replacement_d2_063}


def ed_replacement_d2_064(ed_replacement_063):
    feature = _clean(ed_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_064'] = {'inputs': ['ed_replacement_063'], 'func': ed_replacement_d2_064}


def ed_replacement_d2_065(ed_replacement_064):
    feature = _clean(ed_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_065'] = {'inputs': ['ed_replacement_064'], 'func': ed_replacement_d2_065}


def ed_replacement_d2_066(ed_replacement_065):
    feature = _clean(ed_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_066'] = {'inputs': ['ed_replacement_065'], 'func': ed_replacement_d2_066}


def ed_replacement_d2_067(ed_replacement_066):
    feature = _clean(ed_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_067'] = {'inputs': ['ed_replacement_066'], 'func': ed_replacement_d2_067}


def ed_replacement_d2_068(ed_replacement_067):
    feature = _clean(ed_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_068'] = {'inputs': ['ed_replacement_067'], 'func': ed_replacement_d2_068}


def ed_replacement_d2_069(ed_replacement_068):
    feature = _clean(ed_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_069'] = {'inputs': ['ed_replacement_068'], 'func': ed_replacement_d2_069}


def ed_replacement_d2_070(ed_replacement_069):
    feature = _clean(ed_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_070'] = {'inputs': ['ed_replacement_069'], 'func': ed_replacement_d2_070}


def ed_replacement_d2_071(ed_replacement_070):
    feature = _clean(ed_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_071'] = {'inputs': ['ed_replacement_070'], 'func': ed_replacement_d2_071}


def ed_replacement_d2_072(ed_replacement_071):
    feature = _clean(ed_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_072'] = {'inputs': ['ed_replacement_071'], 'func': ed_replacement_d2_072}


def ed_replacement_d2_073(ed_replacement_072):
    feature = _clean(ed_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_073'] = {'inputs': ['ed_replacement_072'], 'func': ed_replacement_d2_073}


def ed_replacement_d2_074(ed_replacement_073):
    feature = _clean(ed_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_074'] = {'inputs': ['ed_replacement_073'], 'func': ed_replacement_d2_074}


def ed_replacement_d2_075(ed_replacement_074):
    feature = _clean(ed_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_075'] = {'inputs': ['ed_replacement_074'], 'func': ed_replacement_d2_075}


def ed_replacement_d2_076(ed_replacement_075):
    feature = _clean(ed_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_076'] = {'inputs': ['ed_replacement_075'], 'func': ed_replacement_d2_076}


def ed_replacement_d2_077(ed_replacement_076):
    feature = _clean(ed_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_077'] = {'inputs': ['ed_replacement_076'], 'func': ed_replacement_d2_077}


def ed_replacement_d2_078(ed_replacement_077):
    feature = _clean(ed_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_078'] = {'inputs': ['ed_replacement_077'], 'func': ed_replacement_d2_078}


def ed_replacement_d2_079(ed_replacement_078):
    feature = _clean(ed_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_079'] = {'inputs': ['ed_replacement_078'], 'func': ed_replacement_d2_079}


def ed_replacement_d2_080(ed_replacement_079):
    feature = _clean(ed_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_080'] = {'inputs': ['ed_replacement_079'], 'func': ed_replacement_d2_080}


def ed_replacement_d2_081(ed_replacement_080):
    feature = _clean(ed_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_081'] = {'inputs': ['ed_replacement_080'], 'func': ed_replacement_d2_081}


def ed_replacement_d2_082(ed_replacement_081):
    feature = _clean(ed_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_082'] = {'inputs': ['ed_replacement_081'], 'func': ed_replacement_d2_082}


def ed_replacement_d2_083(ed_replacement_082):
    feature = _clean(ed_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_083'] = {'inputs': ['ed_replacement_082'], 'func': ed_replacement_d2_083}


def ed_replacement_d2_084(ed_replacement_083):
    feature = _clean(ed_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_084'] = {'inputs': ['ed_replacement_083'], 'func': ed_replacement_d2_084}


def ed_replacement_d2_085(ed_replacement_084):
    feature = _clean(ed_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_085'] = {'inputs': ['ed_replacement_084'], 'func': ed_replacement_d2_085}


def ed_replacement_d2_086(ed_replacement_085):
    feature = _clean(ed_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_086'] = {'inputs': ['ed_replacement_085'], 'func': ed_replacement_d2_086}


def ed_replacement_d2_087(ed_replacement_086):
    feature = _clean(ed_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_087'] = {'inputs': ['ed_replacement_086'], 'func': ed_replacement_d2_087}


def ed_replacement_d2_088(ed_replacement_087):
    feature = _clean(ed_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_088'] = {'inputs': ['ed_replacement_087'], 'func': ed_replacement_d2_088}


def ed_replacement_d2_089(ed_replacement_088):
    feature = _clean(ed_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_089'] = {'inputs': ['ed_replacement_088'], 'func': ed_replacement_d2_089}


def ed_replacement_d2_090(ed_replacement_089):
    feature = _clean(ed_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_090'] = {'inputs': ['ed_replacement_089'], 'func': ed_replacement_d2_090}


def ed_replacement_d2_091(ed_replacement_090):
    feature = _clean(ed_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_091'] = {'inputs': ['ed_replacement_090'], 'func': ed_replacement_d2_091}


def ed_replacement_d2_092(ed_replacement_091):
    feature = _clean(ed_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_092'] = {'inputs': ['ed_replacement_091'], 'func': ed_replacement_d2_092}


def ed_replacement_d2_093(ed_replacement_092):
    feature = _clean(ed_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_093'] = {'inputs': ['ed_replacement_092'], 'func': ed_replacement_d2_093}


def ed_replacement_d2_094(ed_replacement_093):
    feature = _clean(ed_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_094'] = {'inputs': ['ed_replacement_093'], 'func': ed_replacement_d2_094}


def ed_replacement_d2_095(ed_replacement_094):
    feature = _clean(ed_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_095'] = {'inputs': ['ed_replacement_094'], 'func': ed_replacement_d2_095}


def ed_replacement_d2_096(ed_replacement_095):
    feature = _clean(ed_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_096'] = {'inputs': ['ed_replacement_095'], 'func': ed_replacement_d2_096}


def ed_replacement_d2_097(ed_replacement_096):
    feature = _clean(ed_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_097'] = {'inputs': ['ed_replacement_096'], 'func': ed_replacement_d2_097}


def ed_replacement_d2_098(ed_replacement_097):
    feature = _clean(ed_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_098'] = {'inputs': ['ed_replacement_097'], 'func': ed_replacement_d2_098}


def ed_replacement_d2_099(ed_replacement_098):
    feature = _clean(ed_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_099'] = {'inputs': ['ed_replacement_098'], 'func': ed_replacement_d2_099}


def ed_replacement_d2_100(ed_replacement_099):
    feature = _clean(ed_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_100'] = {'inputs': ['ed_replacement_099'], 'func': ed_replacement_d2_100}


def ed_replacement_d2_101(ed_replacement_100):
    feature = _clean(ed_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_101'] = {'inputs': ['ed_replacement_100'], 'func': ed_replacement_d2_101}


def ed_replacement_d2_102(ed_replacement_101):
    feature = _clean(ed_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_102'] = {'inputs': ['ed_replacement_101'], 'func': ed_replacement_d2_102}


def ed_replacement_d2_103(ed_replacement_102):
    feature = _clean(ed_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_103'] = {'inputs': ['ed_replacement_102'], 'func': ed_replacement_d2_103}


def ed_replacement_d2_104(ed_replacement_103):
    feature = _clean(ed_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_104'] = {'inputs': ['ed_replacement_103'], 'func': ed_replacement_d2_104}


def ed_replacement_d2_105(ed_replacement_104):
    feature = _clean(ed_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_105'] = {'inputs': ['ed_replacement_104'], 'func': ed_replacement_d2_105}


def ed_replacement_d2_106(ed_replacement_105):
    feature = _clean(ed_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_106'] = {'inputs': ['ed_replacement_105'], 'func': ed_replacement_d2_106}


def ed_replacement_d2_107(ed_replacement_106):
    feature = _clean(ed_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_107'] = {'inputs': ['ed_replacement_106'], 'func': ed_replacement_d2_107}


def ed_replacement_d2_108(ed_replacement_107):
    feature = _clean(ed_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_108'] = {'inputs': ['ed_replacement_107'], 'func': ed_replacement_d2_108}


def ed_replacement_d2_109(ed_replacement_108):
    feature = _clean(ed_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_109'] = {'inputs': ['ed_replacement_108'], 'func': ed_replacement_d2_109}


def ed_replacement_d2_110(ed_replacement_109):
    feature = _clean(ed_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_110'] = {'inputs': ['ed_replacement_109'], 'func': ed_replacement_d2_110}


def ed_replacement_d2_111(ed_replacement_110):
    feature = _clean(ed_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_111'] = {'inputs': ['ed_replacement_110'], 'func': ed_replacement_d2_111}


def ed_replacement_d2_112(ed_replacement_111):
    feature = _clean(ed_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_112'] = {'inputs': ['ed_replacement_111'], 'func': ed_replacement_d2_112}


def ed_replacement_d2_113(ed_replacement_112):
    feature = _clean(ed_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_113'] = {'inputs': ['ed_replacement_112'], 'func': ed_replacement_d2_113}


def ed_replacement_d2_114(ed_replacement_113):
    feature = _clean(ed_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_114'] = {'inputs': ['ed_replacement_113'], 'func': ed_replacement_d2_114}


def ed_replacement_d2_115(ed_replacement_114):
    feature = _clean(ed_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_115'] = {'inputs': ['ed_replacement_114'], 'func': ed_replacement_d2_115}


def ed_replacement_d2_116(ed_replacement_115):
    feature = _clean(ed_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_116'] = {'inputs': ['ed_replacement_115'], 'func': ed_replacement_d2_116}


def ed_replacement_d2_117(ed_replacement_116):
    feature = _clean(ed_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_117'] = {'inputs': ['ed_replacement_116'], 'func': ed_replacement_d2_117}


def ed_replacement_d2_118(ed_replacement_117):
    feature = _clean(ed_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_118'] = {'inputs': ['ed_replacement_117'], 'func': ed_replacement_d2_118}


def ed_replacement_d2_119(ed_replacement_118):
    feature = _clean(ed_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_119'] = {'inputs': ['ed_replacement_118'], 'func': ed_replacement_d2_119}


def ed_replacement_d2_120(ed_replacement_119):
    feature = _clean(ed_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_120'] = {'inputs': ['ed_replacement_119'], 'func': ed_replacement_d2_120}


def ed_replacement_d2_121(ed_replacement_120):
    feature = _clean(ed_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_121'] = {'inputs': ['ed_replacement_120'], 'func': ed_replacement_d2_121}


def ed_replacement_d2_122(ed_replacement_121):
    feature = _clean(ed_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_122'] = {'inputs': ['ed_replacement_121'], 'func': ed_replacement_d2_122}


def ed_replacement_d2_123(ed_replacement_122):
    feature = _clean(ed_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_123'] = {'inputs': ['ed_replacement_122'], 'func': ed_replacement_d2_123}


def ed_replacement_d2_124(ed_replacement_123):
    feature = _clean(ed_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_124'] = {'inputs': ['ed_replacement_123'], 'func': ed_replacement_d2_124}


def ed_replacement_d2_125(ed_replacement_124):
    feature = _clean(ed_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_125'] = {'inputs': ['ed_replacement_124'], 'func': ed_replacement_d2_125}


def ed_replacement_d2_126(ed_replacement_125):
    feature = _clean(ed_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_126'] = {'inputs': ['ed_replacement_125'], 'func': ed_replacement_d2_126}


def ed_replacement_d2_127(ed_replacement_126):
    feature = _clean(ed_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_127'] = {'inputs': ['ed_replacement_126'], 'func': ed_replacement_d2_127}


def ed_replacement_d2_128(ed_replacement_127):
    feature = _clean(ed_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_128'] = {'inputs': ['ed_replacement_127'], 'func': ed_replacement_d2_128}


def ed_replacement_d2_129(ed_replacement_128):
    feature = _clean(ed_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_129'] = {'inputs': ['ed_replacement_128'], 'func': ed_replacement_d2_129}


def ed_replacement_d2_130(ed_replacement_129):
    feature = _clean(ed_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_130'] = {'inputs': ['ed_replacement_129'], 'func': ed_replacement_d2_130}


def ed_replacement_d2_131(ed_replacement_130):
    feature = _clean(ed_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_131'] = {'inputs': ['ed_replacement_130'], 'func': ed_replacement_d2_131}


def ed_replacement_d2_132(ed_replacement_131):
    feature = _clean(ed_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_132'] = {'inputs': ['ed_replacement_131'], 'func': ed_replacement_d2_132}


def ed_replacement_d2_133(ed_replacement_132):
    feature = _clean(ed_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_133'] = {'inputs': ['ed_replacement_132'], 'func': ed_replacement_d2_133}


def ed_replacement_d2_134(ed_replacement_133):
    feature = _clean(ed_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_134'] = {'inputs': ['ed_replacement_133'], 'func': ed_replacement_d2_134}


def ed_replacement_d2_135(ed_replacement_134):
    feature = _clean(ed_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_135'] = {'inputs': ['ed_replacement_134'], 'func': ed_replacement_d2_135}


def ed_replacement_d2_136(ed_replacement_135):
    feature = _clean(ed_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_136'] = {'inputs': ['ed_replacement_135'], 'func': ed_replacement_d2_136}


def ed_replacement_d2_137(ed_replacement_136):
    feature = _clean(ed_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_137'] = {'inputs': ['ed_replacement_136'], 'func': ed_replacement_d2_137}


def ed_replacement_d2_138(ed_replacement_137):
    feature = _clean(ed_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
ED_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ed_replacement_d2_138'] = {'inputs': ['ed_replacement_137'], 'func': ed_replacement_d2_138}


# Base-universe derivative extensions for repaired first-base features.
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def evd_base_universe_d2_001_evd_002_pb_compression_z_42(evd_002_pb_compression_z_42):
    return _base_universe_d2(evd_002_pb_compression_z_42, 1)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_001_evd_002_pb_compression_z_42'] = {'inputs': ['evd_002_pb_compression_z_42'], 'func': evd_base_universe_d2_001_evd_002_pb_compression_z_42}


def evd_base_universe_d2_002_evd_003_ps_compression_z_63(evd_003_ps_compression_z_63):
    return _base_universe_d2(evd_003_ps_compression_z_63, 2)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_002_evd_003_ps_compression_z_63'] = {'inputs': ['evd_003_ps_compression_z_63'], 'func': evd_base_universe_d2_002_evd_003_ps_compression_z_63}


def evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126(evd_005_ev_marketcap_gap_126):
    return _base_universe_d2(evd_005_ev_marketcap_gap_126, 3)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126'] = {'inputs': ['evd_005_ev_marketcap_gap_126'], 'func': evd_base_universe_d2_003_evd_005_ev_marketcap_gap_126}


def evd_base_universe_d2_004_evd_006_dividend_yield_spike_189(evd_006_dividend_yield_spike_189):
    return _base_universe_d2(evd_006_dividend_yield_spike_189, 4)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_004_evd_006_dividend_yield_spike_189'] = {'inputs': ['evd_006_dividend_yield_spike_189'], 'func': evd_base_universe_d2_004_evd_006_dividend_yield_spike_189}


def evd_base_universe_d2_005_evd_008_valuation_history_depth_378(evd_008_valuation_history_depth_378):
    return _base_universe_d2(evd_008_valuation_history_depth_378, 5)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_005_evd_008_valuation_history_depth_378'] = {'inputs': ['evd_008_valuation_history_depth_378'], 'func': evd_base_universe_d2_005_evd_008_valuation_history_depth_378}


def evd_base_universe_d2_006_evd_009_pe_compression_z_504(evd_009_pe_compression_z_504):
    return _base_universe_d2(evd_009_pe_compression_z_504, 6)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_006_evd_009_pe_compression_z_504'] = {'inputs': ['evd_009_pe_compression_z_504'], 'func': evd_base_universe_d2_006_evd_009_pe_compression_z_504}


def evd_base_universe_d2_007_evd_010_pb_compression_z_756(evd_010_pb_compression_z_756):
    return _base_universe_d2(evd_010_pb_compression_z_756, 7)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_007_evd_010_pb_compression_z_756'] = {'inputs': ['evd_010_pb_compression_z_756'], 'func': evd_base_universe_d2_007_evd_010_pb_compression_z_756}


def evd_base_universe_d2_008_evd_011_ps_compression_z_1008(evd_011_ps_compression_z_1008):
    return _base_universe_d2(evd_011_ps_compression_z_1008, 8)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_008_evd_011_ps_compression_z_1008'] = {'inputs': ['evd_011_ps_compression_z_1008'], 'func': evd_base_universe_d2_008_evd_011_ps_compression_z_1008}


def evd_base_universe_d2_009_evd_014_dividend_yield_spike_63(evd_014_dividend_yield_spike_63):
    return _base_universe_d2(evd_014_dividend_yield_spike_63, 9)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_009_evd_014_dividend_yield_spike_63'] = {'inputs': ['evd_014_dividend_yield_spike_63'], 'func': evd_base_universe_d2_009_evd_014_dividend_yield_spike_63}


def evd_base_universe_d2_010_evd_016_valuation_history_depth_21(evd_016_valuation_history_depth_21):
    return _base_universe_d2(evd_016_valuation_history_depth_21, 10)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_010_evd_016_valuation_history_depth_21'] = {'inputs': ['evd_016_valuation_history_depth_21'], 'func': evd_base_universe_d2_010_evd_016_valuation_history_depth_21}


def evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189(evd_021_ev_marketcap_gap_189):
    return _base_universe_d2(evd_021_ev_marketcap_gap_189, 11)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189'] = {'inputs': ['evd_021_ev_marketcap_gap_189'], 'func': evd_base_universe_d2_011_evd_021_ev_marketcap_gap_189}


def evd_base_universe_d2_012_evd_023_earnings_yield_spike_378(evd_023_earnings_yield_spike_378):
    return _base_universe_d2(evd_023_earnings_yield_spike_378, 12)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_012_evd_023_earnings_yield_spike_378'] = {'inputs': ['evd_023_earnings_yield_spike_378'], 'func': evd_base_universe_d2_012_evd_023_earnings_yield_spike_378}


def evd_base_universe_d2_013_evd_024_valuation_history_depth_504(evd_024_valuation_history_depth_504):
    return _base_universe_d2(evd_024_valuation_history_depth_504, 13)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_013_evd_024_valuation_history_depth_504'] = {'inputs': ['evd_024_valuation_history_depth_504'], 'func': evd_base_universe_d2_013_evd_024_valuation_history_depth_504}


def evd_base_universe_d2_014_evd_027_ps_compression_z_1260(evd_027_ps_compression_z_1260):
    return _base_universe_d2(evd_027_ps_compression_z_1260, 14)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_014_evd_027_ps_compression_z_1260'] = {'inputs': ['evd_027_ps_compression_z_1260'], 'func': evd_base_universe_d2_014_evd_027_ps_compression_z_1260}


def evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63(evd_029_ev_marketcap_gap_63):
    return _base_universe_d2(evd_029_ev_marketcap_gap_63, 15)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63'] = {'inputs': ['evd_029_ev_marketcap_gap_63'], 'func': evd_base_universe_d2_015_evd_029_ev_marketcap_gap_63}


def evd_base_universe_d2_016_evd_031_earnings_yield_spike_21(evd_031_earnings_yield_spike_21):
    return _base_universe_d2(evd_031_earnings_yield_spike_21, 16)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_016_evd_031_earnings_yield_spike_21'] = {'inputs': ['evd_031_earnings_yield_spike_21'], 'func': evd_base_universe_d2_016_evd_031_earnings_yield_spike_21}


def evd_base_universe_d2_017_evd_032_valuation_history_depth_42(evd_032_valuation_history_depth_42):
    return _base_universe_d2(evd_032_valuation_history_depth_42, 17)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_017_evd_032_valuation_history_depth_42'] = {'inputs': ['evd_032_valuation_history_depth_42'], 'func': evd_base_universe_d2_017_evd_032_valuation_history_depth_42}


def evd_base_universe_d2_018_evd_035_ps_compression_z_126(evd_035_ps_compression_z_126):
    return _base_universe_d2(evd_035_ps_compression_z_126, 18)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_018_evd_035_ps_compression_z_126'] = {'inputs': ['evd_035_ps_compression_z_126'], 'func': evd_base_universe_d2_018_evd_035_ps_compression_z_126}


def evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252(evd_037_ev_marketcap_gap_252):
    return _base_universe_d2(evd_037_ev_marketcap_gap_252, 19)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252'] = {'inputs': ['evd_037_ev_marketcap_gap_252'], 'func': evd_base_universe_d2_019_evd_037_ev_marketcap_gap_252}


def evd_base_universe_d2_020_evd_039_earnings_yield_spike_504(evd_039_earnings_yield_spike_504):
    return _base_universe_d2(evd_039_earnings_yield_spike_504, 20)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_020_evd_039_earnings_yield_spike_504'] = {'inputs': ['evd_039_earnings_yield_spike_504'], 'func': evd_base_universe_d2_020_evd_039_earnings_yield_spike_504}


def evd_base_universe_d2_021_evd_040_valuation_history_depth_756(evd_040_valuation_history_depth_756):
    return _base_universe_d2(evd_040_valuation_history_depth_756, 21)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_021_evd_040_valuation_history_depth_756'] = {'inputs': ['evd_040_valuation_history_depth_756'], 'func': evd_base_universe_d2_021_evd_040_valuation_history_depth_756}


def evd_base_universe_d2_022_evd_043_ps_compression_z_1512(evd_043_ps_compression_z_1512):
    return _base_universe_d2(evd_043_ps_compression_z_1512, 22)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_022_evd_043_ps_compression_z_1512'] = {'inputs': ['evd_043_ps_compression_z_1512'], 'func': evd_base_universe_d2_022_evd_043_ps_compression_z_1512}


def evd_base_universe_d2_023_evd_047_earnings_yield_spike_42(evd_047_earnings_yield_spike_42):
    return _base_universe_d2(evd_047_earnings_yield_spike_42, 23)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_023_evd_047_earnings_yield_spike_42'] = {'inputs': ['evd_047_earnings_yield_spike_42'], 'func': evd_base_universe_d2_023_evd_047_earnings_yield_spike_42}


def evd_base_universe_d2_024_evd_048_valuation_history_depth_63(evd_048_valuation_history_depth_63):
    return _base_universe_d2(evd_048_valuation_history_depth_63, 24)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_024_evd_048_valuation_history_depth_63'] = {'inputs': ['evd_048_valuation_history_depth_63'], 'func': evd_base_universe_d2_024_evd_048_valuation_history_depth_63}


def evd_base_universe_d2_025_evd_051_ps_compression_z_189(evd_051_ps_compression_z_189):
    return _base_universe_d2(evd_051_ps_compression_z_189, 25)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_025_evd_051_ps_compression_z_189'] = {'inputs': ['evd_051_ps_compression_z_189'], 'func': evd_base_universe_d2_025_evd_051_ps_compression_z_189}


def evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378(evd_053_ev_marketcap_gap_378):
    return _base_universe_d2(evd_053_ev_marketcap_gap_378, 26)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378'] = {'inputs': ['evd_053_ev_marketcap_gap_378'], 'func': evd_base_universe_d2_026_evd_053_ev_marketcap_gap_378}


def evd_base_universe_d2_027_evd_055_earnings_yield_spike_756(evd_055_earnings_yield_spike_756):
    return _base_universe_d2(evd_055_earnings_yield_spike_756, 27)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_027_evd_055_earnings_yield_spike_756'] = {'inputs': ['evd_055_earnings_yield_spike_756'], 'func': evd_base_universe_d2_027_evd_055_earnings_yield_spike_756}


def evd_base_universe_d2_028_evd_056_valuation_history_depth_1008(evd_056_valuation_history_depth_1008):
    return _base_universe_d2(evd_056_valuation_history_depth_1008, 28)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_028_evd_056_valuation_history_depth_1008'] = {'inputs': ['evd_056_valuation_history_depth_1008'], 'func': evd_base_universe_d2_028_evd_056_valuation_history_depth_1008}


def evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21(evd_061_ev_marketcap_gap_21):
    return _base_universe_d2(evd_061_ev_marketcap_gap_21, 29)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21'] = {'inputs': ['evd_061_ev_marketcap_gap_21'], 'func': evd_base_universe_d2_029_evd_061_ev_marketcap_gap_21}


def evd_base_universe_d2_030_evd_064_valuation_history_depth_84(evd_064_valuation_history_depth_84):
    return _base_universe_d2(evd_064_valuation_history_depth_84, 30)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_030_evd_064_valuation_history_depth_84'] = {'inputs': ['evd_064_valuation_history_depth_84'], 'func': evd_base_universe_d2_030_evd_064_valuation_history_depth_84}


def evd_base_universe_d2_031_evd_067_ps_compression_z_252(evd_067_ps_compression_z_252):
    return _base_universe_d2(evd_067_ps_compression_z_252, 31)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_031_evd_067_ps_compression_z_252'] = {'inputs': ['evd_067_ps_compression_z_252'], 'func': evd_base_universe_d2_031_evd_067_ps_compression_z_252}


def evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504(evd_069_ev_marketcap_gap_504):
    return _base_universe_d2(evd_069_ev_marketcap_gap_504, 32)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504'] = {'inputs': ['evd_069_ev_marketcap_gap_504'], 'func': evd_base_universe_d2_032_evd_069_ev_marketcap_gap_504}


def evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008(evd_071_earnings_yield_spike_1008):
    return _base_universe_d2(evd_071_earnings_yield_spike_1008, 33)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008'] = {'inputs': ['evd_071_earnings_yield_spike_1008'], 'func': evd_base_universe_d2_033_evd_071_earnings_yield_spike_1008}


def evd_base_universe_d2_034_evd_072_valuation_history_depth_1260(evd_072_valuation_history_depth_1260):
    return _base_universe_d2(evd_072_valuation_history_depth_1260, 34)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_034_evd_072_valuation_history_depth_1260'] = {'inputs': ['evd_072_valuation_history_depth_1260'], 'func': evd_base_universe_d2_034_evd_072_valuation_history_depth_1260}


def evd_base_universe_d2_035_evd_basefill_004(evd_basefill_004):
    return _base_universe_d2(evd_basefill_004, 35)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_035_evd_basefill_004'] = {'inputs': ['evd_basefill_004'], 'func': evd_base_universe_d2_035_evd_basefill_004}


def evd_base_universe_d2_036_evd_basefill_012(evd_basefill_012):
    return _base_universe_d2(evd_basefill_012, 36)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_036_evd_basefill_012'] = {'inputs': ['evd_basefill_012'], 'func': evd_base_universe_d2_036_evd_basefill_012}


def evd_base_universe_d2_037_evd_basefill_015(evd_basefill_015):
    return _base_universe_d2(evd_basefill_015, 37)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_037_evd_basefill_015'] = {'inputs': ['evd_basefill_015'], 'func': evd_base_universe_d2_037_evd_basefill_015}


def evd_base_universe_d2_038_evd_basefill_017(evd_basefill_017):
    return _base_universe_d2(evd_basefill_017, 38)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_038_evd_basefill_017'] = {'inputs': ['evd_basefill_017'], 'func': evd_base_universe_d2_038_evd_basefill_017}


def evd_base_universe_d2_039_evd_basefill_018(evd_basefill_018):
    return _base_universe_d2(evd_basefill_018, 39)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_039_evd_basefill_018'] = {'inputs': ['evd_basefill_018'], 'func': evd_base_universe_d2_039_evd_basefill_018}


def evd_base_universe_d2_040_evd_basefill_020(evd_basefill_020):
    return _base_universe_d2(evd_basefill_020, 40)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_040_evd_basefill_020'] = {'inputs': ['evd_basefill_020'], 'func': evd_base_universe_d2_040_evd_basefill_020}


def evd_base_universe_d2_041_evd_basefill_022(evd_basefill_022):
    return _base_universe_d2(evd_basefill_022, 41)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_041_evd_basefill_022'] = {'inputs': ['evd_basefill_022'], 'func': evd_base_universe_d2_041_evd_basefill_022}


def evd_base_universe_d2_042_evd_basefill_025(evd_basefill_025):
    return _base_universe_d2(evd_basefill_025, 42)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_042_evd_basefill_025'] = {'inputs': ['evd_basefill_025'], 'func': evd_base_universe_d2_042_evd_basefill_025}


def evd_base_universe_d2_043_evd_basefill_026(evd_basefill_026):
    return _base_universe_d2(evd_basefill_026, 43)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_043_evd_basefill_026'] = {'inputs': ['evd_basefill_026'], 'func': evd_base_universe_d2_043_evd_basefill_026}


def evd_base_universe_d2_044_evd_basefill_028(evd_basefill_028):
    return _base_universe_d2(evd_basefill_028, 44)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_044_evd_basefill_028'] = {'inputs': ['evd_basefill_028'], 'func': evd_base_universe_d2_044_evd_basefill_028}


def evd_base_universe_d2_045_evd_basefill_030(evd_basefill_030):
    return _base_universe_d2(evd_basefill_030, 45)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_045_evd_basefill_030'] = {'inputs': ['evd_basefill_030'], 'func': evd_base_universe_d2_045_evd_basefill_030}


def evd_base_universe_d2_046_evd_basefill_033(evd_basefill_033):
    return _base_universe_d2(evd_basefill_033, 46)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_046_evd_basefill_033'] = {'inputs': ['evd_basefill_033'], 'func': evd_base_universe_d2_046_evd_basefill_033}


def evd_base_universe_d2_047_evd_basefill_034(evd_basefill_034):
    return _base_universe_d2(evd_basefill_034, 47)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_047_evd_basefill_034'] = {'inputs': ['evd_basefill_034'], 'func': evd_base_universe_d2_047_evd_basefill_034}


def evd_base_universe_d2_048_evd_basefill_036(evd_basefill_036):
    return _base_universe_d2(evd_basefill_036, 48)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_048_evd_basefill_036'] = {'inputs': ['evd_basefill_036'], 'func': evd_base_universe_d2_048_evd_basefill_036}


def evd_base_universe_d2_049_evd_basefill_038(evd_basefill_038):
    return _base_universe_d2(evd_basefill_038, 49)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_049_evd_basefill_038'] = {'inputs': ['evd_basefill_038'], 'func': evd_base_universe_d2_049_evd_basefill_038}


def evd_base_universe_d2_050_evd_basefill_041(evd_basefill_041):
    return _base_universe_d2(evd_basefill_041, 50)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_050_evd_basefill_041'] = {'inputs': ['evd_basefill_041'], 'func': evd_base_universe_d2_050_evd_basefill_041}


def evd_base_universe_d2_051_evd_basefill_042(evd_basefill_042):
    return _base_universe_d2(evd_basefill_042, 51)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_051_evd_basefill_042'] = {'inputs': ['evd_basefill_042'], 'func': evd_base_universe_d2_051_evd_basefill_042}


def evd_base_universe_d2_052_evd_basefill_044(evd_basefill_044):
    return _base_universe_d2(evd_basefill_044, 52)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_052_evd_basefill_044'] = {'inputs': ['evd_basefill_044'], 'func': evd_base_universe_d2_052_evd_basefill_044}


def evd_base_universe_d2_053_evd_basefill_045(evd_basefill_045):
    return _base_universe_d2(evd_basefill_045, 53)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_053_evd_basefill_045'] = {'inputs': ['evd_basefill_045'], 'func': evd_base_universe_d2_053_evd_basefill_045}


def evd_base_universe_d2_054_evd_basefill_046(evd_basefill_046):
    return _base_universe_d2(evd_basefill_046, 54)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_054_evd_basefill_046'] = {'inputs': ['evd_basefill_046'], 'func': evd_base_universe_d2_054_evd_basefill_046}


def evd_base_universe_d2_055_evd_basefill_049(evd_basefill_049):
    return _base_universe_d2(evd_basefill_049, 55)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_055_evd_basefill_049'] = {'inputs': ['evd_basefill_049'], 'func': evd_base_universe_d2_055_evd_basefill_049}


def evd_base_universe_d2_056_evd_basefill_050(evd_basefill_050):
    return _base_universe_d2(evd_basefill_050, 56)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_056_evd_basefill_050'] = {'inputs': ['evd_basefill_050'], 'func': evd_base_universe_d2_056_evd_basefill_050}


def evd_base_universe_d2_057_evd_basefill_052(evd_basefill_052):
    return _base_universe_d2(evd_basefill_052, 57)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_057_evd_basefill_052'] = {'inputs': ['evd_basefill_052'], 'func': evd_base_universe_d2_057_evd_basefill_052}


def evd_base_universe_d2_058_evd_basefill_054(evd_basefill_054):
    return _base_universe_d2(evd_basefill_054, 58)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_058_evd_basefill_054'] = {'inputs': ['evd_basefill_054'], 'func': evd_base_universe_d2_058_evd_basefill_054}


def evd_base_universe_d2_059_evd_basefill_057(evd_basefill_057):
    return _base_universe_d2(evd_basefill_057, 59)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_059_evd_basefill_057'] = {'inputs': ['evd_basefill_057'], 'func': evd_base_universe_d2_059_evd_basefill_057}


def evd_base_universe_d2_060_evd_basefill_058(evd_basefill_058):
    return _base_universe_d2(evd_basefill_058, 60)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_060_evd_basefill_058'] = {'inputs': ['evd_basefill_058'], 'func': evd_base_universe_d2_060_evd_basefill_058}


def evd_base_universe_d2_061_evd_basefill_059(evd_basefill_059):
    return _base_universe_d2(evd_basefill_059, 61)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_061_evd_basefill_059'] = {'inputs': ['evd_basefill_059'], 'func': evd_base_universe_d2_061_evd_basefill_059}


def evd_base_universe_d2_062_evd_basefill_060(evd_basefill_060):
    return _base_universe_d2(evd_basefill_060, 62)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_062_evd_basefill_060'] = {'inputs': ['evd_basefill_060'], 'func': evd_base_universe_d2_062_evd_basefill_060}


def evd_base_universe_d2_063_evd_basefill_062(evd_basefill_062):
    return _base_universe_d2(evd_basefill_062, 63)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_063_evd_basefill_062'] = {'inputs': ['evd_basefill_062'], 'func': evd_base_universe_d2_063_evd_basefill_062}


def evd_base_universe_d2_064_evd_basefill_063(evd_basefill_063):
    return _base_universe_d2(evd_basefill_063, 64)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_064_evd_basefill_063'] = {'inputs': ['evd_basefill_063'], 'func': evd_base_universe_d2_064_evd_basefill_063}


def evd_base_universe_d2_065_evd_basefill_065(evd_basefill_065):
    return _base_universe_d2(evd_basefill_065, 65)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_065_evd_basefill_065'] = {'inputs': ['evd_basefill_065'], 'func': evd_base_universe_d2_065_evd_basefill_065}


def evd_base_universe_d2_066_evd_basefill_066(evd_basefill_066):
    return _base_universe_d2(evd_basefill_066, 66)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_066_evd_basefill_066'] = {'inputs': ['evd_basefill_066'], 'func': evd_base_universe_d2_066_evd_basefill_066}


def evd_base_universe_d2_067_evd_basefill_068(evd_basefill_068):
    return _base_universe_d2(evd_basefill_068, 67)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_067_evd_basefill_068'] = {'inputs': ['evd_basefill_068'], 'func': evd_base_universe_d2_067_evd_basefill_068}


def evd_base_universe_d2_068_evd_basefill_070(evd_basefill_070):
    return _base_universe_d2(evd_basefill_070, 68)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_068_evd_basefill_070'] = {'inputs': ['evd_basefill_070'], 'func': evd_base_universe_d2_068_evd_basefill_070}


def evd_base_universe_d2_069_evd_basefill_073(evd_basefill_073):
    return _base_universe_d2(evd_basefill_073, 69)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_069_evd_basefill_073'] = {'inputs': ['evd_basefill_073'], 'func': evd_base_universe_d2_069_evd_basefill_073}


def evd_base_universe_d2_070_evd_basefill_074(evd_basefill_074):
    return _base_universe_d2(evd_basefill_074, 70)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_070_evd_basefill_074'] = {'inputs': ['evd_basefill_074'], 'func': evd_base_universe_d2_070_evd_basefill_074}


def evd_base_universe_d2_071_evd_basefill_075(evd_basefill_075):
    return _base_universe_d2(evd_basefill_075, 71)
EVD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['evd_base_universe_d2_071_evd_basefill_075'] = {'inputs': ['evd_basefill_075'], 'func': evd_base_universe_d2_071_evd_basefill_075}
