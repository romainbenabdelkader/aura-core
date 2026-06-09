from pathlib import Path
import tempfile
import unittest

from aura_core import hashing, manifest, signing, verification


class AuraCoreTest(unittest.TestCase):
    def test_sign_and_verify_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / "track.wav"
            asset.write_bytes(b"aura demo bytes")

            asset_hash = hashing.compute_hash(asset)
            unsigned = manifest.create_manifest(
                asset_hash=asset_hash,
                issuer_id="LOCAL-ISSUER",
                asset_type="audio_file",
                asset_title="track.wav",
                asset_filename="track.wav",
                aura_id="AURA-LOCAL-TEST",
            )

            private_key = signing.generate_private_key()
            signed = signing.sign_manifest(unsigned, private_key)
            result = verification.verify_asset_manifest(str(asset), signed)

            self.assertTrue(result.valid)
            self.assertIsNone(result.reason)
            self.assertTrue(result.asset_hash_ok)
            self.assertTrue(result.signature_ok)

    def test_modified_asset_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / "track.wav"
            asset.write_bytes(b"original")

            unsigned = manifest.create_manifest(
                asset_hash=hashing.compute_hash(asset),
                issuer_id="LOCAL-ISSUER",
                asset_type="audio_file",
            )
            signed = signing.sign_manifest(unsigned, signing.generate_private_key())

            asset.write_bytes(b"modified")
            result = verification.verify_asset_manifest(str(asset), signed)

            self.assertFalse(result.valid)
            self.assertEqual(result.reason, "file hash mismatch")
            self.assertFalse(result.asset_hash_ok)
            self.assertTrue(result.signature_ok)

    def test_modified_manifest_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / "track.wav"
            asset.write_bytes(b"original")

            unsigned = manifest.create_manifest(
                asset_hash=hashing.compute_hash(asset),
                issuer_id="LOCAL-ISSUER",
                asset_type="audio_file",
            )
            signed = signing.sign_manifest(unsigned, signing.generate_private_key())
            signed["issuer_id"] = "TAMPERED"

            result = verification.verify_asset_manifest(str(asset), signed)

            self.assertFalse(result.valid)
            self.assertEqual(result.reason, "manifest signature mismatch")
            self.assertTrue(result.asset_hash_ok)
            self.assertFalse(result.signature_ok)


if __name__ == "__main__":
    unittest.main()
