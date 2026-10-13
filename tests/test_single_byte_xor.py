import sys
import unittest
from pathlib import Path

CHALLENGE = Path(__file__).resolve().parents[1] / "challenges" / "single_byte_xor"
sys.path.insert(0, str(CHALLENGE))

from make_challenge import KEY, PLAINTEXT, encrypt  # noqa: E402
from solve import crack, xor_with_key  # noqa: E402


class SingleByteXorTest(unittest.TestCase):
    def test_xor_is_its_own_inverse(self):
        self.assertEqual(xor_with_key(encrypt(PLAINTEXT, KEY), KEY), PLAINTEXT)

    def test_committed_challenge_matches_generator(self):
        committed = bytes.fromhex((CHALLENGE / "challenge.hex").read_text().strip())
        self.assertEqual(committed, encrypt(PLAINTEXT, KEY))

    def test_solver_recovers_key_and_flag(self):
        score, key, plaintext = crack(encrypt(PLAINTEXT, KEY))[0]
        self.assertEqual(key, KEY)
        self.assertIn(b"flag{demo_single_byte_xor}", plaintext)


if __name__ == "__main__":
    unittest.main()
