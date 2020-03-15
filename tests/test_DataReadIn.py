import DefectSupercellAnalyses as dsa
import LogFileSetup as lfs
import pytest
import numpy as np

# Functions created specifically for running test cases
def group_species_with_count(species_list, host_counts, defect_counts):
    '''Function to avoid false negatives with test_count_species, when order of species read in is different,
    but species type and corresponding count are correct. 
    
    Args: (outputs from dsa.read_atom_coords)
    - species_list (list of str): chemical symbol of elements in supercell
    - host_counts (list of int): number of each species type in perfect host supercell
    - defect_counts (list of int): number of each species (same order as above) but in defective supercell

    Returns: Set of tuples, where each tuple is species, host_count, defect_count. Set is chosen so that order is not
    important when comparing between supercell, but species, host_count and defect_count order is respected.
    '''
    species_countHostDefect = set() # Create set so that order is not important for later comparisons
    for species, host_count, defect_count in zip(species_list, host_counts, defect_counts):
        species_countHostDefect.add((species, host_count, defect_count))
    return species_countHostDefect

# Test log file function call
def test_log_file_config():
    lfs.configure_logging("log_test")

# Unit tests for functions
def test_read_lattice_vectors():
    vecs_test_x, vecs_test_y, vecs_test_z = dsa.read_lattice_vectors("tests/TestData/interstitial/geometry.in")
    vecs_verified_x, vecs_verified_y, vecs_verified_z = [14.8588928, 0.00046026, -0.00010556], [-0.00093786, 12.9147523, -0.00021786], [-0.00064498, -0.0010864, 12.33466882]
    assert vecs_test_x == pytest.approx(vecs_verified_x)
    assert vecs_test_y == pytest.approx(vecs_verified_y)
    assert vecs_test_z == pytest.approx(vecs_verified_z)
def test_lattice_vectors_array():
    latt_vec_array_test = dsa.lattice_vectors_array("tests/TestData/perfect/geometry.in")
    latt_vec_array_verified = np.array([[1.48588928e+01, -9.37860000e-04, -6.44980000e-04], [4.60260000e-04, 1.29147523e+01, -1.08640000e-03], [-1.05560000e-04, -2.17860000e-04, 1.23346688e+01]])
    assert latt_vec_array_test == pytest.approx(latt_vec_array_verified)
def test_count_atoms():
    count_verified = 128
    count_test = dsa.count_atoms("tests/TestData/perfect/geometry.in")
    assert count_verified == count_test

# Testing functions that use other functions
def test_read_atom_coords():
    host_coords_verified = [(0.00046534, 5.31329724, 2.20714242, 'S'), (0.00069547, 11.77067339, 2.20659922, 'S'), (0.00041256, 5.31318831, 8.37447683, 'S'), (0.00064269, 11.77056446, 8.37393363, 'S'), (1.80807171, 4.29617702, 11.59464988, 'S'), (1.80835462, 10.7536621, 5.42677227, 'S'), (1.80830184, 10.75355317, 11.59410668, 'S'), (1.80812449, 4.29628595, 5.42731547, 'S'), (1.90613764, 2.16070578, 8.51124779, 'S'), (1.90636777, 8.61808193, 8.51070459, 'S'), (1.90619042, 2.16081471, 2.34391338, 'S'), (1.90642055, 8.61819086, 2.34337018, 'S'), (3.71501546, 7.60088349, 5.2902933, 'S'), (3.71478533, 1.14350734, 5.2908365, 'S'), (3.71473255, 1.14339841, 11.45817091, 'S'), (3.71496268, 7.60077456, 11.45762771, 'S'), (3.71539278, 5.49819637, 2.31746116, 'S'), (3.71534, 5.49808744, 8.48479557, 'S'), (3.71562291, 11.95557252, 2.31691796, 'S'), (3.71557013, 11.95546359, 8.48425237, 'S'), (5.52350555, 2.16049082, 2.34383908, 'S'), (5.52345277, 2.16038189, 8.51117349, 'S'), (5.52373568, 8.61786697, 2.34329588, 'S'), (5.5236829, 8.61775804, 8.51063029, 'S'), (5.62070798, 4.29610045, 5.4274193, 'S'), (5.6206552, 4.29599152, 11.59475371, 'S'), (5.62093811, 10.7534766, 5.4268761, 'S'), (5.62088533, 10.75336767, 11.59421051, 'S'), (7.4291319, 0.95865372, 5.40180637, 'S'), (7.42930925, 7.41592094, 11.56859758, 'S'), (7.42907912, 0.95854479, 11.56914078, 'S'), (7.42936203, 7.41602987, 5.40126317, 'S'), (7.42991174, 5.31282831, 2.20681993, 'S'), (7.42985896, 5.31271938, 8.37415434, 'S'), (7.43014187, 11.77020446, 2.20627673, 'S'), (7.43008909, 11.77009553, 8.37361114, 'S'), (9.23757089, 4.29581702, 5.42699298, 'S'), (9.23751811, 4.29570809, 11.59432739, 'S'), (9.23774824, 10.75308424, 11.59378419, 'S'), (9.23780102, 10.75319317, 5.42644978, 'S'), (9.33558404, 2.16023685, 8.5109253, 'S'), (9.33586695, 8.61772193, 2.34304769, 'S'), (9.33563682, 2.16034578, 2.34359089, 'S'), (9.33581417, 8.617613, 8.5103821, 'S'), (11.14417895, 1.14292948, 11.45784842, 'S'), (11.14440908, 7.60030563, 11.45730522, 'S'), (11.14446186, 7.60041456, 5.28997081, 'S'), (11.14423173, 1.14303841, 5.29051401, 'S'), (11.14483918, 5.49772744, 2.31713867, 'S'), (11.14506931, 11.95510359, 2.31659547, 'S'), (11.14501653, 11.95499466, 8.48392988, 'S'), (11.1447864, 5.49761851, 8.48447308, 'S'), (12.95295195, 2.16002189, 2.34351659, 'S'), (12.95289917, 2.15991296, 8.510851, 'S'), (12.95318208, 8.61739804, 2.34297339, 'S'), (12.9531293, 8.61728911, 8.5103078, 'S'), (13.05015438, 4.29563152, 5.42709681, 'S'), (13.0501016, 4.29552259, 11.59443122, 'S'), (13.05033173, 10.75289874, 11.59388802, 'S'), (13.05038451, 10.75300767, 5.42655361, 'S'), (14.8585783, 0.95818479, 5.40148388, 'S'), (14.85852552, 0.95807586, 11.56881829, 'S'), (14.85880843, 7.41556094, 5.40094068, 'S'), (14.85875565, 7.41545201, 11.56827509, 'S'), (0.00047912, 7.44970272, 3.08713044, 'Cu'), (0.00024899, 0.99232657, 3.08767364, 'Cu'), (0.00019621, 0.99221764, 9.25500805, 'Cu'), (0.00042634, 7.44959379, 9.25446485, 'Cu'), (1.84463038, 2.10917543, 6.21072121, 'Cu'), (1.84486051, 8.56655158, 6.21017801, 'Cu'), (1.84468316, 2.10928436, 0.0433868, 'Cu'), (1.84491329, 8.56666051, 0.0428436, 'Cu'), (1.87067774, 4.34822328, 3.12682266, 'Cu'), (1.87062496, 4.34811435, 9.29415707, 'Cu'), (1.87090787, 10.80559943, 3.12627946, 'Cu'), (1.87085509, 10.8054905, 9.29361387, 'Cu'), (3.71427356, 11.92140147, 6.169767, 'Cu'), (3.71409621, 5.46413425, 0.00297579, 'Cu'), (3.71404343, 5.46402532, 6.1703102, 'Cu'), (3.71432634, 11.9215104, 0.00243259, 'Cu'), (5.56000419, 4.34780005, 3.12701191, 'Cu'), (5.55995141, 4.34769112, 9.29434632, 'Cu'), (5.56023432, 10.8051762, 3.12646871, 'Cu'), (5.56018154, 10.80506727, 9.29380312, 'Cu'), (5.58414185, 2.10877377, 6.21059918, 'Cu'), (5.58419463, 2.1088827, 0.04326477, 'Cu'), (5.58442476, 8.56625885, 0.04272157, 'Cu'), (5.58437198, 8.56614992, 6.21005598, 'Cu'), (7.42969539, 0.99185764, 3.08735115, 'Cu'), (7.42964261, 0.99174871, 9.25468556, 'Cu'), (7.42992552, 7.44923379, 3.08680795, 'Cu'), (7.42987274, 7.44912486, 9.25414236, 'Cu'), (9.27407678, 2.1087065, 6.21039872, 'Cu'), (9.27412956, 2.10881543, 0.04306431, 'Cu'), (9.27435969, 8.56619158, 0.04252111, 'Cu'), (9.27430691, 8.56608265, 6.20985552, 'Cu'), (9.30035427, 10.8051305, 3.12595697, 'Cu'), (9.30030149, 10.80502157, 9.29329138, 'Cu'), (9.30012414, 4.34775435, 3.12650017, 'Cu'), (9.30007136, 4.34764542, 9.29383458, 'Cu'), (11.14348983, 5.46355639, 6.16998771, 'Cu'), (11.14354261, 5.46366532, 0.0026533, 'Cu'), (11.14377274, 11.92104147, 0.0021101, 'Cu'), (11.14371996, 11.92093254, 6.16944451, 'Cu'), (12.98945059, 4.34733112, 3.12668942, 'Cu'), (12.98962794, 10.80459834, 9.29348063, 'Cu'), (12.98968072, 10.80470727, 3.12614622, 'Cu'), (12.98939781, 4.34722219, 9.29402383, 'Cu'), (13.01364103, 2.10841377, 0.04294228, 'Cu'), (13.01358825, 2.10830484, 6.21027669, 'Cu'), (13.01387116, 8.56578992, 0.04239908, 'Cu'), (13.01381838, 8.56568099, 6.20973349, 'Cu'), (3.71491586, 7.56702754, 3.07857021, 'As'), (3.71468573, 1.10965139, 3.07911341, 'As'), (3.71463295, 1.10954246, 9.24644782, 'As'), (3.71486308, 7.56691861, 9.24590462, 'As'), (7.42926588, 5.3470064, 6.16246914, 'As'), (7.42944323, 11.80427362, 12.32926035, 'As'), (7.4292131, 5.34689747, 12.32980355, 'As'), (7.42949601, 11.80438255, 6.16192594, 'As'), (11.14407935, 1.10907353, 9.24612533, 'As'), (11.14430948, 7.56644968, 9.24558213, 'As'), (11.14413213, 1.10918246, 3.07879092, 'As'), (11.14436226, 7.56655861, 3.07824772, 'As'), (14.8586595, 5.34642854, 12.32948106, 'As'), (14.85871228, 5.34653747, 6.16214665, 'As'), (14.85894241, 11.80391362, 6.16160345, 'As'), (14.85888963, 11.80380469, 12.32893786, 'As')]
    host_coords_test = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    for i in range(0, len(host_coords_verified)):
        # Comparing floats for x,y,z coords
        assert host_coords_verified[i][0:3] == pytest.approx(host_coords_test[i][0:3])
        # Comparing strings for atom type
        assert host_coords_verified[i][3] == host_coords_test[i][3]
def test_coords_to_array():
    coords_list = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    coords_array_test = dsa.coords_to_array(coords_list)
    coords_array_verified = np.array([[0.00046534, 5.31329724, 2.20714242], [0.00069547, 11.77067339, 2.20659922], [0.00041256, 5.31318831, 8.37447683], [0.00064269, 11.77056446, 8.37393363], [1.80807171, 4.29617702, 11.59464988], [1.80835462, 10.7536621, 5.42677227], [1.80830184, 10.75355317, 11.59410668], [1.80812449, 4.29628595, 5.42731547], [1.90613764, 2.16070578, 8.51124779], [1.90636777, 8.61808193, 8.51070459], [1.90619042, 2.16081471, 2.34391338], [1.90642055, 8.61819086, 2.34337018], [3.71501546, 7.60088349, 5.2902933], [3.71478533, 1.14350734, 5.2908365], [3.71473255, 1.14339841, 11.45817091], [3.71496268, 7.60077456, 11.45762771], [3.71539278, 5.49819637, 2.31746116], [3.71534, 5.49808744, 8.48479557], [3.71562291, 11.95557252, 2.31691796], [3.71557013, 11.95546359, 8.48425237], [5.52350555, 2.16049082, 2.34383908], [5.52345277, 2.16038189, 8.51117349], [5.52373568, 8.61786697, 2.34329588], [5.5236829, 8.61775804, 8.51063029], [5.62070798, 4.29610045, 5.4274193], [5.6206552, 4.29599152, 11.59475371], [5.62093811, 10.7534766, 5.4268761], [5.62088533, 10.75336767, 11.59421051], [7.4291319, 0.95865372, 5.40180637], [7.42930925, 7.41592094, 11.56859758], [7.42907912, 0.95854479, 11.56914078], [7.42936203, 7.41602987, 5.40126317], [7.42991174, 5.31282831, 2.20681993], [7.42985896, 5.31271938, 8.37415434], [7.43014187, 11.77020446, 2.20627673], [7.43008909, 11.77009553, 8.37361114], [9.23757089, 4.29581702, 5.42699298], [9.23751811, 4.29570809, 11.59432739], [9.23774824, 10.75308424, 11.59378419], [9.23780102, 10.75319317, 5.42644978], [9.33558404, 2.16023685, 8.5109253], [9.33586695, 8.61772193, 2.34304769], [9.33563682, 2.16034578, 2.34359089], [9.33581417, 8.617613, 8.5103821], [11.14417895, 1.14292948, 11.45784842], [11.14440908, 7.60030563, 11.45730522], [11.14446186, 7.60041456, 5.28997081], [11.14423173, 1.14303841, 5.29051401], [11.14483918, 5.49772744, 2.31713867], [11.14506931, 11.95510359, 2.31659547], [11.14501653, 11.95499466, 8.48392988], [11.1447864, 5.49761851, 8.48447308], [12.95295195, 2.16002189, 2.34351659], [12.95289917, 2.15991296, 8.510851], [12.95318208, 8.61739804, 2.34297339], [12.9531293, 8.61728911, 8.5103078], [13.05015438, 4.29563152, 5.42709681], [13.0501016, 4.29552259, 11.59443122], [13.05033173, 10.75289874, 11.59388802], [13.05038451, 10.75300767, 5.42655361], [14.8585783, 0.95818479, 5.40148388], [14.85852552, 0.95807586, 11.56881829], [14.85880843, 7.41556094, 5.40094068], [14.85875565, 7.41545201, 11.56827509], [0.00047912, 7.44970272, 3.08713044], [0.00024899, 0.99232657, 3.08767364], [0.00019621, 0.99221764, 9.25500805], [0.00042634, 7.44959379, 9.25446485], [1.84463038, 2.10917543, 6.21072121], [1.84486051, 8.56655158, 6.21017801], [1.84468316, 2.10928436, 0.0433868], [1.84491329, 8.56666051, 0.0428436], [1.87067774, 4.34822328, 3.12682266], [1.87062496, 4.34811435, 9.29415707], [1.87090787, 10.80559943, 3.12627946], [1.87085509, 10.8054905, 9.29361387], [3.71427356, 11.92140147, 6.169767], [3.71409621, 5.46413425, 0.00297579], [3.71404343, 5.46402532, 6.1703102], [3.71432634, 11.9215104, 0.00243259], [5.56000419, 4.34780005, 3.12701191], [5.55995141, 4.34769112, 9.29434632], [5.56023432, 10.8051762, 3.12646871], [5.56018154, 10.80506727, 9.29380312], [5.58414185, 2.10877377, 6.21059918], [5.58419463, 2.1088827, 0.04326477], [5.58442476, 8.56625885, 0.04272157], [5.58437198, 8.56614992, 6.21005598], [7.42969539, 0.99185764, 3.08735115], [7.42964261, 0.99174871, 9.25468556], [7.42992552, 7.44923379, 3.08680795], [7.42987274, 7.44912486, 9.25414236], [9.27407678, 2.1087065, 6.21039872], [9.27412956, 2.10881543, 0.04306431], [9.27435969, 8.56619158, 0.04252111], [9.27430691, 8.56608265, 6.20985552], [9.30035427, 10.8051305, 3.12595697], [9.30030149, 10.80502157, 9.29329138], [9.30012414, 4.34775435, 3.12650017], [9.30007136, 4.34764542, 9.29383458], [11.14348983, 5.46355639, 6.16998771], [11.14354261, 5.46366532, 0.0026533], [11.14377274, 11.92104147, 0.0021101], [11.14371996, 11.92093254, 6.16944451], [12.98945059, 4.34733112, 3.12668942], [12.98962794, 10.80459834, 9.29348063], [12.98968072, 10.80470727, 3.12614622], [12.98939781, 4.34722219, 9.29402383], [13.01364103, 2.10841377, 0.04294228], [13.01358825, 2.10830484, 6.21027669], [13.01387116, 8.56578992, 0.04239908], [13.01381838, 8.56568099, 6.20973349], [3.71491586, 7.56702754, 3.07857021], [3.71468573, 1.10965139, 3.07911341], [3.71463295, 1.10954246, 9.24644782], [3.71486308, 7.56691861, 9.24590462], [7.42926588, 5.3470064, 6.16246914], [7.42944323, 11.80427362, 12.32926035], [7.4292131, 5.34689747, 12.32980355], [7.42949601, 11.80438255, 6.16192594], [11.14407935, 1.10907353, 9.24612533], [11.14430948, 7.56644968, 9.24558213], [11.14413213, 1.10918246, 3.07879092], [11.14436226, 7.56655861, 3.07824772], [14.8586595, 5.34642854, 12.32948106], [14.85871228, 5.34653747, 6.16214665], [14.85894241, 11.80391362, 6.16160345], [14.85888963, 11.80380469, 12.32893786]])
    assert coords_array_test == pytest.approx(coords_array_verified)
def test_get_supercell_dimensions():
    dims_test = dsa.get_supercell_dimensions("tests/TestData/vacancy/geometry.in")
    dims_verified = [14.8588928, 12.9147523, 12.33466882]
    assert dims_test == pytest.approx(dims_verified)
def test_count_species():
    # Defect is S vacancy, therefore host has one more S ion than defect supercell
    # Species list, host supercell species count, defect supercell species count
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/vacancy/geometry.in")
    test_count = dsa.count_species(host_coords, defect_coords)
    test_grouped = group_species_with_count(test_count[0], test_count[1], test_count[2])
    verified_count = ['S', 'Cu', 'As'], [64, 48, 16], [63, 48, 16]
    verified_grouped = group_species_with_count(verified_count[0], verified_count[1], verified_count[2])
    assert verified_grouped == test_grouped
def test_find_defect_type():
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    vacancy_coords = dsa.read_atom_coords("tests/TestData/vacancy/geometry.in")
    antisite_coords = dsa.read_atom_coords("tests/TestData/antisite/geometry.in")
    interstitial_coords = dsa.read_atom_coords("tests/TestData/interstitial/geometry.in")
    vacancy_test = dsa.find_defect_type(host_coords, vacancy_coords)
    antisite_test = dsa.find_defect_type(host_coords, antisite_coords)
    interstitial_test = dsa.find_defect_type(host_coords, interstitial_coords)
    assert vacancy_test == 'vacancy'
    assert antisite_test == 'antisite'
    assert interstitial_test == 'interstitial'
def test_find_vacancy():
    verified_species = 'S'
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/vacancy/geometry.in")
    test_species = dsa.find_vacancy(host_coords, defect_coords)
    assert verified_species == test_species
def test_find_interstitial():
    verified_species = 'Cu'
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/interstitial/geometry.in")
    test_species = dsa.find_interstitial(host_coords, defect_coords)
    assert verified_species == test_species
def test_find_antisite():
    verified_species = 'As', 'Cu'
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/antisite/geometry.in")
    test_species = dsa.find_antisite(host_coords, defect_coords)
    assert verified_species == test_species
def test_vacancy_coords():
    verified_vac_coords = (5.52373568, 8.61786697, 2.34329588)
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/vacancy/geometry.in")
    test_vac_coords = dsa.vacancy_coords(host_coords, defect_coords)
    assert verified_vac_coords == pytest.approx(test_vac_coords[1:4])
def test_interstitial_coords():
    verified_int_coords = (5.6, 2.6, 4.6)
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/interstitial/geometry.in")
    test_int_coords = dsa.interstitial_coords(host_coords, defect_coords)
    assert verified_int_coords == pytest.approx(test_int_coords[1:4])
def test_antisite_coords():
    verified_anti_coords = (5.58437198, 8.56614992, 6.21005598)
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/antisite/geometry.in")
    test_anti_coords = dsa.antisite_coords(host_coords, defect_coords)
    assert verified_anti_coords == pytest.approx(test_anti_coords[2:5])
def test_defect_to_boundary():
    verified_defect_dist = (5.58437198, 4.348602379999999, 6.124612839999999)
    host_coords = dsa.read_atom_coords("tests/TestData/perfect/geometry.in")
    defect_coords = dsa.read_atom_coords("tests/TestData/antisite/geometry.in")
    species_in, species_out, defect_x, defect_y, defect_z, defect_line = dsa.antisite_coords(host_coords, defect_coords)
    supercell_dims = dsa.get_supercell_dimensions("tests/TestData/perfect/geometry.in")
    test_defect_dist = dsa.defect_to_boundary(defect_x, defect_y, defect_z, supercell_dims[0], supercell_dims[1], supercell_dims[2])
    assert verified_defect_dist == pytest.approx(test_defect_dist)   