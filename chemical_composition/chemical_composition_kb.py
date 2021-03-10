#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8
"""
The knowledge base holds all constants required for chemical composistion

ISOTOPIC_DISTRIBUTIONS correspond to Berglund M. & Wieser M.E.
Isotopic compositions of the elements 2009 (IUPAC Technical Report)
Pure Appl. Chem., 2011, Vol. 83, No. 2, pp. 397-410
http://dx.doi.org/10.1351/PAC-REP-10-06-02
Published online 2011-01-14
http://www.ciaaw.org/pubs/TICE2009.pdf
"""

# updated 03-2021
PROTON = 1.007276466621

isotopic_distributions = {
    # Isotopic masses verified using
    # http://ciaaw.org/atomic-masses.htm
    # Wang, M., Audi, G., Wapstra, A. H., Kondev, F. G., MacCormick, M.,
    # Xu, X. and Pfeiffer, B. (2012)
    # The Ame2012 atomic mass evaluation. Chinese Phys. C 36, 1603–2014
    "H": [(1.0078250322, 0.999885), (2.0141017781, 0.000115)],
    "C": [(12.0000, 0.9894), (13.003354835, 0.0106)],
    "N": [(14.003074004, 0.996205), (15.000108899, 0.003795)],
    "O": [(15.994914620, 0.99757), (16.999131757, 0.00038), (17.999159613, 0.00205)],
    "Si": [(27.976926535, 0.92223), (28.976494665, 0.04685), (29.97377001, 0.03092)],
    "P": [(30.973761998, 1.00)],
    "S": [
        (31.972071174, 0.9499),
        (32.971458910, 0.0075),
        (33.9678670, 0.0425),
        (35.967081, 0.0001),
    ],
    "Na": [(22.98976928, 1.00)],
    "Cl": [(34.9688527, 0.7576), (36.9659026, 0.2424)],
    "Br": [(78.918338, 0.5069), (80.916290, 0.4931)],
    "Se": [
        (73.9224759, 0.0089),
        (75.9192137, 0.0937),
        (76.9199142, 0.0763),
        (77.917309, 0.2377),
        (79.916522, 0.4961),
        (81.916700, 0.0873),
    ],
    "F": [(18.99840322, 1.0000)],
    "Sr": [
        (83.913425, 0.0056),
        (85.9092602, 0.0986),
        (86.9088771, 0.07),
        (87.9056121, 0.8258),
    ],
    "I": [(126.904473, 1.0000)],
    "Co": [(58.933195, 1.0000)],
    "Cd": [
        (105.906459, 0.0125),
        (107.904184, 0.0089),
        (109.9030021, 0.1249),
        (110.9041781, 0.128),
        (111.9027578, 0.2413),
        (112.9044017, 0.1222),
        (113.9033585, 0.2873),
        (115.904756, 0.0749),
    ],
    "Fe": [
        (53.9396105, 0.05845),
        (55.9349375, 0.91754),
        (56.935394, 0.02119),
        (57.9332756, 0.00282),
    ],
    "As": [(74.9215965, 1.0000)],
    "Mg": [(23.9850417, 0.7899), (24.98583692, 0.1), (25.982592929, 0.1101)],
    "Mn": [(54.9380451, 1.000)],
    "Th": [(232.0380553, 0.9998), (230.0331338, 0.0002)],
    "Pt": [
        (189.959932, 0.00014),
        (191.961038, 0.00782),
        (193.9626803, 0.32967),
        (194.9647911, 0.33832),
        (195.9649515, 0.25242),
        (197.967893, 0.07163),
    ],
    "Gd": [
        (151.919791, 0.002),
        (153.9208656, 0.0218),
        (154.922622, 0.148),
        (155.9221227, 0.2047),
        (156.9239601, 0.1565),
        (157.9241039, 0.2484),
        (159.9270541, 0.2186),
    ],
    "Te": [
        (119.90402, 0.0009),
        (121.9030439, 0.0255),
        (122.90427, 0.0089),
        (123.9028179, 0.0474),
        (124.9044307, 0.0707),
        (125.9033117, 0.1884),
        (127.9044631, 0.3174),
        (129.9062244, 0.3408),
    ],
    "Pd": [
        (101.905609, 0.0102),
        (103.904036, 0.1114),
        (104.905085, 0.2233),
        (105.903486, 0.2733),
        (107.903892, 0.2646),
        (109.905153, 0.1172),
    ],
    "Cr": [
        (49.9460442, 0.04345),
        (51.9405075, 0.83789),
        (52.9406494, 0.09501),
        (53.9388804, 0.02365),
    ],
    "Mo": [
        (91.906811, 0.1477),
        (93.9050883, 0.0923),
        (94.9058421, 0.159),
        (95.9046795, 0.1668),
        (96.9060215, 0.0956),
        (97.9054082, 0.2419),
        (99.907477, 0.0967),
    ],
    "Ca": [
        (39.96259098, 0.96941),
        (41.95861801, 0.00647),
        (42.9587666, 0.00135),
        (43.9554818, 0.02086),
        (45.9536926, 0.00004),
        (47.952534, 0.00187),
    ],
    "Ge": [
        (69.9242474, 0.2038),
        (71.9220758, 0.2731),
        (72.9234589, 0.0776),
        (73.9211778, 0.3672),
        (75.9214026, 0.0783),
    ],
    "Cu": [(62.9295975, 0.6915), (64.9277895, 0.3085)],
    "Tl": [(202.9723442, 0.2952), (204.9744275, 0.7048)],
    "Zn": [
        (63.9291422, 0.4917),
        (65.9260334, 0.2773),
        (66.9271273, 0.0404),
        (67.9248442, 0.1845),
        (69.9253193, 0.0061),
    ],
    "Rb": [(84.911789738, 0.7217), (86.909180527, 0.2783)],
    "Au": [(196.9665687, 1.0000)],
    "Bi": [(208.9803987, 1.0000)],
    "B": [(10.012937, 0.199), (11.0093054, 0.801)],
    "Zr": [
        (89.9047044, 0.5145),
        (90.9056458, 0.1122),
        (91.9050408, 0.1715),
        (93.9063152, 0.1738),
        (95.9082734, 0.028),
    ],
    "He": [(3.0160293191, 0.00000134), (4.0026032542, 0.99999866)],
    "V": [(49.9471585, 0.0025), (50.9439595, 0.9975)],
    "Hg": [
        (195.965833, 0.0015),
        (197.966769, 0.0997),
        (198.9682799, 0.1687),
        (199.968326, 0.231),
        (200.9703023, 0.1318),
        (201.970643, 0.2986),
        (203.9734939, 0.0687),
    ],
    "Al": [(26.98153863, 1.0000)],
    "Ta": [(179.9474648, 0.00012), (180.9479958, 0.99988)],
    "Pb": [
        (203.9730436, 0.014),
        (205.9744653, 0.241),
        (206.9758969, 0.221),
        (207.9766521, 0.524),
    ],
    "Ag": [(106.905097, 0.51839), (108.904752, 0.48161)],
    "Cs": [(132.905451933, 1.000)],
    "Sn": [
        (111.904818, 0.0097),
        (113.902779, 0.0066),
        (114.903342, 0.0034),
        (115.901741, 0.1454),
        (116.902952, 0.0768),
        (117.901603, 0.2422),
        (118.903308, 0.0859),
        (119.9021947, 0.3258),
        (121.903439, 0.0463),
        (123.9052739, 0.0579),
    ],
    "Ru": [
        (95.907598, 0.0554),
        (97.905287, 0.0187),
        (98.9059393, 0.1276),
        (99.9042195, 0.126),
        (100.9055821, 0.1706),
        (101.9043493, 0.3155),
        (103.905433, 0.1862),
    ],
    "Ce": [
        (135.907172, 0.00185),
        (137.905991, 0.00251),
        (139.9054387, 0.8845),
        (141.909244, 0.11114),
    ],
    "Ni": [
        (57.9353429, 0.680769),
        (59.9307864, 0.262231),
        (60.931056, 0.011399),
        (61.9283451, 0.036345),
        (63.927966, 0.009256),
    ],
    "Li": [(6.015122795, 0.078), (7.01600455, 0.922)],
    "K": [(38.96370668, 0.932581), (39.96399848, 0.000117), (40.96182576, 0.067302)],
    "Sb": [(120.9038157, 0.5721), (122.904214, 0.4279)],
    "Ga": [(68.9255736, 0.60108), (70.9247013, 0.39892)],
    "Nd": [
        (141.9077233, 0.272),
        (142.9098143, 0.122),
        (143.9100873, 0.238),
        (144.9125736, 0.083),
        (145.9131169, 0.172),
        (147.916893, 0.057),
        (149.920891, 0.056),
    ],
    "Be": [(9.0121822, 1.0)],
    "Ba": [
        (129.9063208, 0.00106),
        (131.9050613, 0.00101),
        (133.9045084, 0.02417),
        (134.9056886, 0.06592),
        (135.9045759, 0.07854),
        (136.9058274, 0.11232),
        (137.9052472, 0.71698),
    ],
    "Ar": [(35.967545106, 0.003365), (37.9627324, 0.000632), (39.9623831225, 0.996003)],
    "Hf": [
        (173.940046, 0.0016),
        (175.9414086, 0.0526),
        (176.9432207, 0.186),
        (177.9436988, 0.2728),
        (178.9458161, 0.1362),
        (179.94655, 0.3508),
    ],
    "W": [
        (179.946704, 0.0012),
        (181.9482042, 0.265),
        (182.950223, 0.1431),
        (183.9509312, 0.3064),
        (185.9543641, 0.2843),
    ],
    "Re": [(184.952955, 0.374), (186.9557531, 0.626)],
    "Ti": [
        (45.9526316, 0.0825),
        (46.9517631, 0.0744),
        (47.9479463, 0.7372),
        (48.94787, 0.0541),
        (49.9447912, 0.0518),
    ],
}

aa_compositions = {
    "A": "C3H5NO",
    "C": "C3H5NOS",
    "D": "C4H5NO3",
    "E": "C5H7NO3",
    "F": "C9H9NO",
    "G": "C2H3NO",
    "H": "C6H7N3O",
    "I": "C6H11NO",
    "K": "C6H12N2O",
    "L": "C6H11NO",
    "M": "C5H9NOS",
    "N": "C4H6N2O2",
    "P": "C5H7NO",
    "Q": "C5H8N2O2",
    "R": "C6H12N4O",
    "S": "C3H5NO2",
    "T": "C4H7NO2",
    "V": "C5H9NO",
    "W": "C11H10N2O",
    "Y": "C9H9NO2",
    "U": "C3H5NOSe",  # Selenocystein
}

monosaccharide_compositions = {
    "dHex": "C6H10O4",
    "dHexNAc": "C8H13NO4",
    "Hex": "C6H10O5",
    "HexA": "C6H8O6",
    "HexNAc": "C8H13NO5",
    "Me2Hex": "C8H14O5",
    "MeHex": "C7H12O5",
    "MedHex": "C7H12O4",
    "NeuAc": "C11H17NO8",
    "Pent": "C5H8O4",
    "dHexN": "C6H11O3N",
    "HexN": "C6H11O4N",
    "MeHexA": "C7H10O6",
    "Hep": "C7H12O6",
    "SQv": "C6H10O7S",
    "SO3Hex": "C6H10O8S1",
}

aa_names = {
    "A": "alanine",
    "C": "cysteine",
    "D": "aspartic_acid",
    "E": "glutamic_acid",
    "F": "phenylalanine",
    "G": "glycine",
    "H": "histidine",
    "I": "isoleucine",
    "K": "lysine",
    "L": "leucine",
    "M": "methionine",
    "N": "asparagine",
    "P": "proline",
    "Q": "glutamine",
    "R": "arginine",
    "S": "serine",
    "T": "threonine",
    "V": "valine",
    "W": "tryptophan",
    "Y": "tyrosine",
    "U": "selenocystein",
}
