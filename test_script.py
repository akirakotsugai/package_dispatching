import csv
from typing import List, Optional


class Package:
    STATUS_REJECTED = "REJECTED"
    STATUS_SPECIAL = "SPECIAL"
    STATUS_STANDARD = "STANDARD"
    STATUSES = (STATUS_REJECTED, STATUS_SPECIAL, STATUS_STANDARD,)

    def __init__(self, width, height, length, mass):
        self._width = width
        self._height = height
        self._length = length
        self._mass = mass

    @property
    def _is_bulky(self) -> bool:
        dimensions = [self._width, self._height, self._length]
        return any(d >= 150 for d in dimensions) or (self._width * self._height * self._length) >= 1000000

    @property
    def _is_heavy(self) -> bool:
        return self._mass >= 20

    @property
    def _dimensions(self) -> Optional[List[int]]:
        try:
            return [int(self._width), int(self._height), int(self._length), int(self._mass)]
        except:
            return None

    @property
    def is_invalid(self) -> bool:
        return not self._dimensions


    def sort(self) -> str:
        if (self._is_bulky and self._is_heavy) or self.is_invalid:
            return self.STATUS_REJECTED

        if self._is_heavy or self._is_bulky:
            return self.STATUS_SPECIAL

        return self.STATUS_STANDARD


class PackagesReport:
    def __init__(self, packages: List[Package]):
        self._packages = packages

    @property
    def total_number(self) -> int:
        return len(self._packages)

    @staticmethod
    def get_numbers_per_stack(stack: str):






def load_packages() -> List[Package]:
    with open('thoughtful_exercise.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        packages = [Package(*row) for row in spamreader]
        return packages
    
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
    # run_all_tests()
    # print("SUCCESS")
    packages = load_packages()
    report = PackagesReport(packages)
