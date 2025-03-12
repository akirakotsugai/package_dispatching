def is_bulky(width, height, length):
    dimensions = [width, height, length]
    return any(d >= 150 for d in dimensions) or (width * height * length) >= 1000000

def is_heavy(mass):
    return mass >= 20

def sort(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)
    
    if heavy and bulky:
        return "REJECTED"

    if heavy or bulky:
        return "SPECIAL"
    
    return "STANDARD"
    
def test_standard_case():
    assert sort(50, 60, 70, 10) == "STANDARD"

def test_special_case_bulky_dimension():
    assert sort(150, 60, 70, 10) == "SPECIAL"

def test_special_case_product_of_dimensions():
    assert sort(10, 10, 1000, 10) == "SPECIAL"

def test_special_case_heavy_mass():
    assert sort(50, 50, 50, 21) == "SPECIAL"

def test_rejected_case_bulky_and_heavy():
    assert sort(150, 150, 150, 21) == "REJECTED"

def test_special_case_mass_exactly_20():
    assert sort(50, 50, 50, 20) == "SPECIAL"

def test_case_bulky_but_not_heavy():
    assert sort(150, 50, 50, 10) == "SPECIAL"

def test_case_heavy_but_not_bulky():
    assert sort(50, 50, 50, 21) == "SPECIAL"

def test_case_bulky_and_heavy_but_not_rejected():
    assert sort(150, 50, 50, 19) == "SPECIAL"

def test_case_dimensions_below_threshold_and_light_mass():
    assert sort(50, 50, 50, 10) == "STANDARD"

def test_case_product_of_dimensions_barely_above_threshold():
    assert sort(10, 10, 1000, 10) == "SPECIAL"

def test_case_all_dimensions_above_threshold_but_mass_below_20():
    assert sort(151, 151, 151, 10) == "SPECIAL"

def test_case_all_thresholds_maxed_out_but_not_rejected():
    assert sort(150, 150, 150, 19) == "SPECIAL"
    
    
def run_all_tests():
    test_standard_case()
    test_special_case_bulky_dimension()
    test_special_case_product_of_dimensions()
    test_special_case_heavy_mass()
    test_rejected_case_bulky_and_heavy()
    test_special_case_mass_exactly_20()
    test_case_bulky_but_not_heavy()
    test_case_heavy_but_not_bulky()
    test_case_bulky_and_heavy_but_not_rejected()
    test_case_dimensions_below_threshold_and_light_mass()
    test_case_product_of_dimensions_barely_above_threshold()
    test_case_all_dimensions_above_threshold_but_mass_below_20()
    test_case_all_thresholds_maxed_out_but_not_rejected()

if __name__ == "__main__":
    run_all_tests()
    print("SUCCESS")
