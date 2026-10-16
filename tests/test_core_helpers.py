import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "code" / "main.py"
SPEC = importlib.util.spec_from_file_location("riscv_simulator", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load simulator module from {MODULE_PATH}")
SIMULATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SIMULATOR)


class ArithmeticTests(unittest.TestCase):
    def test_r_type_operations(self) -> None:
        self.assertEqual(SIMULATOR.Calculate_R(0b0000000, 0b000, 9, 4), 13)
        self.assertEqual(SIMULATOR.Calculate_R(0b0100000, 0b000, 9, 4), 5)
        self.assertEqual(SIMULATOR.Calculate_R(0b0000000, 0b100, 0b1010, 0b0110), 0b1100)
        self.assertEqual(SIMULATOR.Calculate_R(0b0000000, 0b110, 0b1010, 0b0110), 0b1110)
        self.assertEqual(SIMULATOR.Calculate_R(0b0000000, 0b111, 0b1010, 0b0110), 0b0010)

    def test_i_type_sign_extension(self) -> None:
        self.assertEqual(SIMULATOR.Calculate_I(0b000, 10, 0x001), 11)
        self.assertEqual(SIMULATOR.Calculate_I(0b000, 10, 0xFFF), 9)


class RepresentationTests(unittest.TestCase):
    def test_signed_round_trip(self) -> None:
        encoded = SIMULATOR.int2bin(-7, 32)
        self.assertEqual(len(encoded), 32)
        self.assertEqual(SIMULATOR.bin2int(encoded, sign_ext=True), -7)

    def test_unsigned_conversion(self) -> None:
        self.assertEqual(SIMULATOR.int2bin(10, 8), "00001010")
        self.assertEqual(SIMULATOR.bin2int("00001010"), 10)


if __name__ == "__main__":
    unittest.main()
